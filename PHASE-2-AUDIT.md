# Phase 2 Audit Report

This document contains a rigorous independent audit of the data analysis performed in Phase 2.

## 1. Datasets & Identification [CONFIRMED]
All three datasets were correctly identified and parsed:
- LeadSmart Coverage: 3,745 rows (ZIPs), 1,800 unique city/state combinations.
- Mentor Dataset: 1,000 rows.
- Keyword Planner: 5,240 keyword rows.

## 2. Dataset Joins (`canonical_locations.csv`) [CONFIRMED]
The Exact-Match assumption (`city|state` lowered and trimmed) correctly joined LeadSmart and Mentor records. A fuzzy-match audit (stripping all punctuation/spaces) yielded exactly 893 matches, proving that no records were missed due to standard formatting differences.

## 3. CPL Statistics & Commercial Thresholds [INCORRECT / RECOMMENDED CHANGE]
- **Original Claim**: Average CPL was calculated at $53.59.
- **Audit Finding**: When properly grouped by unique city/state (max CPL per location rather than raw ZIP average), the true Average CPL is **$50.68**. Median remains $38.50, Min $13, Max $86.

**Location Threshold Analysis (Out of 1,800)**:
- CPL >= $20: 1,654
- CPL >= $40: 722
- CPL >= $50: 703
- CPL >= $60: 703
- CPL >= $70: 703
- CPL >= $74: 703
- CPL >= $80: 199

**Audit Finding on Viability**: The claim that the $38.50 median indicates "broad commercial viability" was misleading. While 91% clear the $20 baseline, the true high-value opportunities jump sharply. Notice the massive plateau: there are exactly 703 locations between $74 and $79. 
- **Action**: The "Priority" rule of CPL >= $40 + Population is inadequate, as it leaves ~700 cities. To achieve a realistic Phase 1 rollout of ~200 locations, we should change the `priority` rule to **CPL >= $80**.

## 4. Keyword Planner Clustering [QUESTIONABLE / RECOMMENDED CHANGE]
- **Original Claim**: Gross search volumes were reported (e.g., Opener: ~7.29M).
- **Audit Finding**: The gross volume included massive branded search intent (Chamberlain, LiftMaster, Genie, Craftsman, Lowes, Home Depot), which are not viable lead-gen queries.
- **Revised Commercial (Non-Brand) Volumes**:
  - **Opener**: 5,790,400 (Dropped ~1.5M branded searches)
  - **Repair**: 4,695,450
  - **Replacement**: 895,900
  - **Spring**: 559,350
  - **Installation**: 512,900

## 5. Recommended Updates
1. Update `DATA-ANALYSIS.md` to fix the Average CPL and adjust the priority batch logic to target the 199 locations with CPL >= $80.
2. Update `LOCATION-ELIGIBILITY.md` to reflect the multi-signal priority rule (CPL >= $80).
3. Update `KEYWORD-STRATEGY.md` to show true commercial/non-branded search volumes.
