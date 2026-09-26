# Topical Map — Reference Guide

## What Is a Topical Map?

A topical map is the complete blueprint of every URL a site needs to achieve full topical authority in its niche. It is the output of Step 1 in the Koray framework. Every URL on the site should trace back to a node in the topical map.

---

## How to Build a Topical Map

### Step 1 — Define the Central Entity

The Central Entity is the primary thing the site is about. One noun phrase.

- Good: "high-risk merchant account"
- Good: "addiction treatment center"
- Too broad: "business finance"
- Too narrow: "MOTO payment processing for firearms dealers"

### Step 2 — Build the Phrase Taxonomy

A phrase taxonomy is a hierarchical list of noun phrases radiating outward from the central entity. It seeds the topical map.

**Tier 1 — The central entity itself**
E.g. "high-risk merchant account"

**Tier 2 — Direct attributes of the entity**
E.g. "high-risk merchant account fees," "high-risk merchant account approval," "high-risk merchant account providers"

**Tier 3 — Processes and actions involving the entity**
E.g. "how to get a high-risk merchant account," "high-risk merchant account application," "high-risk merchant account requirements"

**Tier 4 — Adjacent entities and comparisons**
E.g. "high-risk vs low-risk merchant account," "payment gateway for high-risk merchants," "high-risk merchant account vs PayPal"

**Tier 5 — Industry and use-case specifics**
E.g. "high-risk merchant account for CBD," "high-risk merchant account for adult content," "high-risk merchant account for firearms"

### Step 3 — Map to URL Hierarchy

```
/ (homepage — targets Tier 1 keyword)
/[category-slug]/ (category index — targets Tier 2 or 5 grouping)
/[category-slug]/[post-slug]/ (post — targets Tier 2-5 keyword)
```

**Rules:**
- One keyword per URL. Never optimize one page for two different intent types.
- The URL slug must match the H1 keyword (exact or near-exact).
- Category indexes are C-nodes. Posts are S-nodes. The homepage is the I-node.
- Subcategories are allowed but should not exceed 3 URL levels deep.

### Step 4 — Check Coverage With the 6-Tier SCN Model

Every category must eventually cover all 6 tiers to achieve full topical authority:

| Tier | Type | Example (High-Risk Merchants) |
|---|---|---|
| 1 | Macro/definitional | What is a high-risk merchant account |
| 2 | Operational | How to apply for a high-risk merchant account |
| 3 | Payment/financial | High-risk merchant account fees explained |
| 4 | Growth/marketing | How to grow a high-risk business |
| 5 | Legal/compliance | High-risk industry regulations by state |
| 6 | Technology/tools | Best payment gateways for high-risk merchants |

A category with only Tier 1 and Tier 3 coverage has a content gap. Google's algorithm recognizes incomplete topical coverage and reduces the site's authority in that category.

### Step 5 — Identify Query Gaps

A query gap is a question users search that the site does not answer. Use Semrush phrase_questions to surface gaps:

1. Pull the top 50 question keywords for the category's central seed phrase
2. Cross-reference against the existing topical map
3. Every unanswered question with volume > 0 is a potential URL to build
4. Prioritize by: (1) KD < 35, (2) high commercial intent, (3) Tier 3-4 gaps (often underserved)

---

## Topical Map Output Format

When outputting a topical map, use this format:

```
CATEGORY: [Category Name]
URL: /[category-slug]/
Target keyword: [keyword]
KD: [score] | Volume: [monthly]
SCN tier: C-node (category index)

  POST: [Post Title]
  URL: /[category-slug]/[post-slug]/
  Target keyword: [keyword]
  KD: [score] | Volume: [monthly]
  SCN tier: [1-6] — [type]
  Internal links to: [other posts in this category]

  POST: [Post Title]
  ...
```

---

## Rules That Cannot Be Broken

1. The homepage is the I-node. It must link to every category index.
2. Every category index is a C-node. It must link to every post in the category.
3. Every post is an S-node. It must link back to its category C-node.
4. Cross-category links are allowed but should be topically justified — not forced.
5. Never create two URLs that target the same search intent. This creates keyword cannibalization.
6. Never use date-based URLs (e.g. `/2026/05/post-title/`). Use flat keyword slugs only.
7. Pagination is allowed for category archives but paginated pages must use `rel="canonical"` pointing to page 1.

---

## Momentum: Publishing Cadence Required

Topical authority is not static. Google's algorithm rewards consistent publishing cadence within a topic. Koray's minimum cadence recommendations:

| Site size / maturity | Recommended cadence |
|---|---|
| New site (0-6 months) | 3-5 posts per week per active category |
| Growing site (6-18 months) | 2-3 posts per week per active category |
| Established site (18+ months) | 1-2 posts per week per active category, focus on quality and refresh |

Do not publish in bursts followed by long gaps. Consistent cadence outperforms sporadic volume in Koray's framework.
