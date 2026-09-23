# Location Eligibility Framework

We will not generate 1,800+ city pages immediately. Instead, we use a programmatic eligibility funnel based on data signals to manage crawl budget and content quality.

## Statuses
- **candidate**: Exists in the dataset (valid location) but does not meet the minimum commercial threshold yet. No page is generated.
- **approved**: Meets baseline commercial thresholds (e.g., CPL >= $20). Eligible for a standard service-location page when content is available.
- **priority**: High-value location (e.g., CPL >= $80 AND population data exists). These 199 top-tier locations are the first targets for unique content injection and indexation.
- **indexable**: Has passed QA, has unique differentiated content, and is ready to be crawled by search engines. Added to `sitemap.xml`.
- **excluded**: Known low-quality or irrelevant locations.
- **future**: Scheduled for future expansion phases.

## Activation Rules
1. Only `indexable` locations will output HTML pages during the Astro build.
2. An `approved` or `priority` location must have specific content populated before it can be marked `indexable`.
3. `priority` locations will be the initial batch of pages built during the Phase 3 implementation.
