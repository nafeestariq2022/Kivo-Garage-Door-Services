# Data Dictionary

## Raw Datasets

### 1. LeadSmart Coverage Data (`garage door coverage-2026-09-22.csv`)
- **zip**: 5-digit US ZIP Code.
- **city**: Name of the city for the ZIP code.
- **state**: 2-letter State abbreviation.
- **ringba_offer_name**: The backend routing offer name.
- **top_net_cpl_payout**: The maximum payout per lead (Cost Per Lead) in USD for this ZIP.

### 2. Mentor / Secondary City Dataset (`leadsmart_Garage_Door_CPL.csv`)
- **rank**: The ranking of the city based on the mentor's score.
- **city**: Name of the city.
- **state**: 2-letter State abbreviation.
- **payout**: The maximum payout from the mentor dataset (often overlaps with LeadSmart).
- **population**: Total population of the city.
- **density**: Population density of the city.
- **score**: Proprietary mentor score calculating viability/opportunity.

### 3. Google Keyword Planner Data (`Keyword Stats 2026-09-22 at 22_03_50.csv`)
- **Keyword**: The search query term.
- **Avg. monthly searches**: Total average monthly searches over the last 12 months.
- **Competition**: Google Ads competition index (Low, Medium, High). *Note: NOT organic SEO difficulty.*
- **Top of page bid**: CPC bid range indicating commercial value.

## Processed Datasets

### `canonical_locations.csv`
- **state**: 2-letter abbreviation.
- **city**: Original city name.
- **slug**: URL-safe normalized slug (`{state}/{city-name}`).
- **zips**: Pipe-separated list of all ZIPs covered in this city.
- **max_cpl**: The maximum CPL value across all ZIPs in the city.
- **population**: Population from the mentor dataset (if available).
- **mentor_score**: Mentor score (if available).
- **status**: Proposed location eligibility status (`candidate`, `approved`, `priority`, etc.).
