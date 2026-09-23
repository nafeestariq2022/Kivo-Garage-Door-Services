import csv
import json
import re
from collections import defaultdict
from statistics import median, mean

audit_results = {}

# 1. Load Datasets
ls_file = "data/raw/garage door coverage-2026-09-22.csv"
ls_rows = []
with open(ls_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader: ls_rows.append(r)

m_file = "data/raw/leadsmart_Garage_Door_CPL.csv"
m_rows = []
with open(m_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader: m_rows.append(r)

kw_file = "data/raw/Keyword Stats 2026-09-22 at 22_03_50.csv"
with open(kw_file, "r", encoding="utf-16") as f: content = f.read()
if "Keyword" not in content[:500]:
    with open(kw_file, "r", encoding="utf-8") as f: content = f.read()

lines = content.splitlines()
start_idx = next(i for i, l in enumerate(lines) if l.startswith("Keyword\t") or l.startswith("Keyword,"))
delimiter = '\t' if '\t' in lines[start_idx] else ','
reader = csv.DictReader(lines[start_idx:], delimiter=delimiter)
kw_rows = [r for r in reader if r and r.get('Keyword')]

# 2. Re-calculate LeadSmart CPL Stats & City-State Grouping
city_state_cpls = defaultdict(list)
for r in ls_rows:
    city = (r.get('city') or "").strip()
    state = (r.get('state') or "").strip()
    if not city or not state: continue
    
    key = f"{city}|{state}".lower()
    val = r.get('top_net_cpl_payout', '0')
    try:
        val_f = float(val)
        if val_f > 0: city_state_cpls[key].append(val_f)
    except:
        pass

# Determine max CPL for each city/state combo
city_max_cpls = {k: max(v) for k, v in city_state_cpls.items() if v}
all_max_cpls = list(city_max_cpls.values())

# Thresholds based on max CPL per city/state
thresholds = {20: 0, 40: 0, 50: 0, 60: 0, 70: 0, 74: 0, 80: 0}
for cpl in all_max_cpls:
    for t in thresholds.keys():
        if cpl >= t: thresholds[t] += 1

audit_results["leadsmart_cpl"] = {
    "total_unique_city_states_with_cpl": len(city_max_cpls),
    "cpl_min": min(all_max_cpls) if all_max_cpls else 0,
    "cpl_max": max(all_max_cpls) if all_max_cpls else 0,
    "cpl_median": median(all_max_cpls) if all_max_cpls else 0,
    "cpl_avg": mean(all_max_cpls) if all_max_cpls else 0,
    "thresholds": thresholds
}

# 3. Exact Match vs Fuzzy Match Join Test
m_city_states = set(f"{r['city'].strip()}|{r['state'].strip()}".lower() for r in m_rows if r.get('city') and r.get('state'))
ls_keys = set(city_state_cpls.keys())

exact_matches = m_city_states.intersection(ls_keys)

# Look for missed matches (ignoring punctuation, spaces, etc.)
def normalize_name(s):
    return re.sub(r'[^a-z0-9]', '', s)
m_normalized = {normalize_name(k): k for k in m_city_states}
ls_normalized = {normalize_name(k): k for k in ls_keys}
fuzzy_matches = set(m_normalized.keys()).intersection(ls_normalized.keys())

audit_results["join_audit"] = {
    "mentor_total": len(m_city_states),
    "exact_matches": len(exact_matches),
    "fuzzy_matches": len(fuzzy_matches),
    "missed_due_to_exact_match": len(fuzzy_matches) - len(exact_matches)
}

# 4. Keyword Audit (Irrelevant/Brand/Product Filtering)
# We need to filter out brands like chamberlain, liftmaster, genie, craftsman, home depot, lowes
brand_terms = ['chamberlain', 'liftmaster', 'genie', 'craftsman', 'home depot', 'lowes', 'menards', 'linear', 'clopay', 'amarr', 'wayne dalton', 'sears', 'ryobi']
product_terms = ['remote', 'battery', 'parts', 'manual', 'how to', 'lubricant', 'sensor', 'keypad', 'clicker', 'costco']

kw_audit = {
    "repair": {"total_kw": 0, "total_vol": 0, "commercial_kw": 0, "commercial_vol": 0, "top": []},
    "installation": {"total_kw": 0, "total_vol": 0, "commercial_kw": 0, "commercial_vol": 0, "top": []},
    "opener": {"total_kw": 0, "total_vol": 0, "commercial_kw": 0, "commercial_vol": 0, "top": []},
    "spring": {"total_kw": 0, "total_vol": 0, "commercial_kw": 0, "commercial_vol": 0, "top": []},
    "replacement": {"total_kw": 0, "total_vol": 0, "commercial_kw": 0, "commercial_vol": 0, "top": []}
}

for r in kw_rows:
    kw = str(r['Keyword']).lower()
    vol_str = str(r.get('Avg. monthly searches', '0')).replace(',', '')
    vol = int(vol_str) if vol_str.isdigit() else 0
    
    # Check if branded or informational/product
    is_irrelevant = any(b in kw for b in brand_terms) or any(p in kw for p in product_terms)
    
    # Assign cluster
    cluster = None
    if "repair" in kw and "opener" not in kw and "spring" not in kw: cluster = "repair"
    elif "installation" in kw and "opener" not in kw: cluster = "installation"
    elif "replacement" in kw: cluster = "replacement"
    elif "opener" in kw: cluster = "opener"
    elif "spring" in kw: cluster = "spring"
    
    if cluster:
        kw_audit[cluster]["total_kw"] += 1
        kw_audit[cluster]["total_vol"] += vol
        if not is_irrelevant:
            kw_audit[cluster]["commercial_kw"] += 1
            kw_audit[cluster]["commercial_vol"] += vol
            kw_audit[cluster]["top"].append((kw, vol))

# Sort top keywords
for c in kw_audit:
    kw_audit[c]["top"] = sorted(kw_audit[c]["top"], key=lambda x: x[1], reverse=True)[:5]

audit_results["keyword_audit"] = kw_audit

with open("data/analysis/audit_metrics.json", "w") as f:
    json.dump(audit_results, f, indent=2)

print("Audit script complete.")
