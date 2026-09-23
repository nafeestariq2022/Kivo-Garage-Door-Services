# Data Analysis Findings

## 1. LeadSmart Coverage
- **Total Unique ZIPs**: 3,745
- **Total Unique Cities**: 1,653
- **Unique City/State Combinations**: 1,800
- **CPL Distribution (Max per City)**:
  - Minimum CPL: $13.00
  - Maximum CPL: $86.00
  - Median CPL: $38.50
  - Average CPL: $50.68

## 2. Mentor Dataset
- **Total Cities**: 1,000
- **Overlap with LeadSmart**: 893 cities (High overlap, confirming strong correlation).
- **Average Population**: ~42,449
- **Average Payout**: $63.41

## 3. Findings & Eligibility Adjustments
- While 1,654 locations (91.8%) clear a baseline $20 CPL, the high-value locations are heavily tiered. There are exactly 703 locations tiered at $74+ CPL, and exactly 199 locations tiered at $80+ CPL.
- We have 1,800 potential city/state combinations. If we multiplied this by 6 services, we would have 10,800 pages. This is too many for a fresh site.
- **Action**: To achieve a manageable initial rollout of ~200 top-tier cities, we will adjust the `priority` threshold to **CPL >= $80**. This gives us precisely 199 locations for Phase 1.
