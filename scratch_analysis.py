import csv
import json
import os
import re
from collections import defaultdict
from statistics import median, mean

os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/analysis", exist_ok=True)

metrics = {}

def canonicalize_city(city):
    if not city: return ""
    c = city.lower().strip()
    c = re.sub(r"[^a-z0-9\s-]", "", c) # remove apostrophes, etc.
    c = re.sub(r"\s+", "-", c) # spaces to hyphens
    return c

# 1. LeadSmart Dataset (garage door coverage)
ls_file = "data/raw/garage door coverage-2026-09-22.csv"
ls_rows = []
with open(ls_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    ls_headers = reader.fieldnames
    for row in reader:
        ls_rows.append(row)

zips = [r['zip'] for r in ls_rows if r['zip']]
cities = [r['city'] for r in ls_rows if r['city']]
cpls = []
for r in ls_rows:
    try:
        val = float(r.get('top_net_cpl_payout', 0))
        if val > 0: cpls.append(val)
    except: pass

ls_city_states = set(f"{r['city']}|{r['state']}" for r in ls_rows if r['city'] and r['state'])

metrics["leadsmart"] = {
    "filename": "garage door coverage-2026-09-22.csv",
    "rows": len(ls_rows),
    "cols": len(ls_headers),
    "headers": ls_headers,
    "unique_zips": len(set(zips)),
    "unique_cities": len(set(cities)),
    "unique_city_states": len(ls_city_states),
    "cpl_min": min(cpls) if cpls else 0,
    "cpl_max": max(cpls) if cpls else 0,
    "cpl_median": median(cpls) if cpls else 0,
    "cpl_avg": mean(cpls) if cpls else 0,
}

# 2. Mentor Dataset (leadsmart_Garage_Door_CPL)
# Filename is misleading, contains rank, population, density, score
mentor_file = "data/raw/leadsmart_Garage_Door_CPL.csv"
m_rows = []
with open(mentor_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    m_headers = reader.fieldnames
    for row in reader:
        m_rows.append(row)

m_city_states = set(f"{r['city']}|{r['state']}" for r in m_rows if r['city'] and r['state'])
overlap = len(ls_city_states.intersection(m_city_states))
pops = [int(r['population']) for r in m_rows if r.get('population', '').isdigit()]
payouts = [float(r['payout']) for r in m_rows if r.get('payout', '').replace('.','').isdigit()]

metrics["mentor"] = {
    "filename": "leadsmart_Garage_Door_CPL.csv",
    "rows": len(m_rows),
    "cols": len(m_headers),
    "headers": m_headers,
    "total_cities": len(m_rows),
    "overlap_with_leadsmart": overlap,
    "avg_pop": mean(pops) if pops else 0,
    "avg_payout": mean(payouts) if payouts else 0
}

# 3. Keywords Dataset
kw_file = "data/raw/Keyword Stats 2026-09-22 at 22_03_50.csv"
kw_rows = []
with open(kw_file, "r", encoding="utf-16") as f:
    # Try utf-16 first (Google Ads default), if fails try utf-8 in except
    content = f.read()

if "Keyword" not in content[:500]:
    with open(kw_file, "r", encoding="utf-8") as f:
        content = f.read()

lines = content.splitlines()
start_idx = 0
for i, l in enumerate(lines):
    if l.startswith("Keyword\t") or l.startswith("Keyword,"):
        start_idx = i
        break

delimiter = '\t' if '\t' in lines[start_idx] else ','
reader = csv.DictReader(lines[start_idx:], delimiter=delimiter)
kw_headers = reader.fieldnames
for row in reader:
    if row and row.get('Keyword'):
        kw_rows.append(row)

clusters = defaultdict(int)
for r in kw_rows:
    kw = str(r['Keyword']).lower()
    vol = str(r.get('Avg. monthly searches', '0')).replace(',', '')
    if not vol.isdigit(): vol = 0
    vol = int(vol)
    
    if "repair" in kw and "opener" not in kw and "spring" not in kw: clusters["repair"] += vol
    elif "installation" in kw and "opener" not in kw: clusters["installation"] += vol
    elif "replacement" in kw: clusters["replacement"] += vol
    elif "opener" in kw: clusters["opener"] += vol
    elif "spring" in kw: clusters["spring"] += vol
    elif "emergency" in kw: clusters["emergency"] += vol
    elif "commercial" in kw: clusters["commercial"] += vol
    else: clusters["other"] += vol

metrics["keywords"] = {
    "filename": "Keyword Stats 2026-09-22 at 22_03_50.csv",
    "rows": len(kw_rows),
    "cols": len(kw_headers),
    "clusters_volume": dict(clusters)
}

with open("data/analysis/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

# Build normalized processed dataset
# Combine based on LeadSmart dataset, enrich with Mentor dataset
mentor_dict = {f"{r['city']}|{r['state']}": r for r in m_rows}

processed_cities = {}
for r in ls_rows:
    key = f"{r['city']}|{r['state']}"
    if key not in processed_cities:
        c = canonicalize_city(r['city'])
        processed_cities[key] = {
            "city": r['city'],
            "state": r['state'],
            "slug": f"{r['state'].lower()}/{c}",
            "zips": set(),
            "max_cpl": 0,
            "mentor_score": mentor_dict.get(key, {}).get('score', ''),
            "population": mentor_dict.get(key, {}).get('population', ''),
            "status": "candidate"
        }
    
    zip_val = r['zip']
    if zip_val: processed_cities[key]['zips'].add(zip_val)
    
    try:
        cpl = float(r.get('top_net_cpl_payout', 0))
        if cpl > processed_cities[key]['max_cpl']:
            processed_cities[key]['max_cpl'] = cpl
    except: pass

# Output processed cities
with open("data/processed/canonical_locations.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["state", "city", "slug", "zips", "max_cpl", "population", "mentor_score", "status"])
    for v in processed_cities.values():
        # Evaluate eligibility logic mock (e.g. CPL > $20 -> approved)
        status = "candidate"
        if v["max_cpl"] >= 20: status = "approved"
        if v["max_cpl"] >= 40 and v["population"]: status = "priority"
        
        writer.writerow([v['state'], v['city'], v['slug'], "|".join(v['zips']), v['max_cpl'], v['population'], v['mentor_score'], status])

print("Processing complete.")
