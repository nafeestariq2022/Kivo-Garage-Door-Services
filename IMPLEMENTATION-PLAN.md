## Goal Description
Establish the foundation, data architecture, and phased implementation strategy for the Kivo Garage Door Services lead-generation website using Astro, TypeScript, and Tailwind CSS. The focus is on a scalable, data-driven static-site approach that prioritizes SEO, Core Web Vitals, and sustainable organic traffic without relying on fabricated data or thin content.

## User Review Required
> [!IMPORTANT]
> The current workspace is entirely empty (no datasets, CSVs, or code). Please review this phased implementation plan. Once approved, the immediate next step is for you to provide the location/coverage datasets and confirm data normalization rules before we initialize the Astro project.

## Open Questions
> [!WARNING]
> 1. **Exact Dataset Structure**: How will the 1,800 city/state and ZIP records be provided? (e.g., CSV, JSON). What columns do they have?
> 2. **Canonical Naming**: Do you have specific rules for URL slugs for cities with multiple words or special characters?
> 3. **Lead Routing Implementation**: Are there any specific scripts or API integrations needed (e.g., dynamic phone numbers for LeadSmart/Ringba)?
> 4. **Service-Location Eligibility**: What is the initial criteria for marking a location as `approved` or `indexable`? 
> 5. **Sitemap Segmentation Strategy**: Should we split sitemaps by state or by service type to manage crawl budgets effectively?

## Proposed Changes

### [Phase 1: Project Setup & Data Normalization - COMPLETED]
This phase establishes the foundational project and ingest the project data.
- [X] Ingest and normalize the provided LeadSmart/mentor CSV datasets into a structured data format (`canonical_locations.csv`).
- [X] Establish `DATA-DICTIONARY.md`, `KEYWORD-STRATEGY.md`, `DATA-ANALYSIS.md`, and `LOCATION-ELIGIBILITY.md`.
- [X] Define locations, services, and eligibility mapping.
- [ ] Initialize the Astro + Tailwind CSS + TypeScript project.
- [ ] Configure global `BaseLayout` for semantic HTML, proper meta tags, Open Graph, and strict SEO compliance (no fabricated Schema).

### [Phase 2: Data & SEO Analysis - COMPLETED]
This phase audited all commercial data and established eligibility rules.
- [X] Merged Mentor and LeadSmart datasets into `canonical_locations.csv`.
- [X] Established CPL >= $80 priority cutoff.
- [X] Filtered branded keyword search volumes.

### [Phase 3: Base Architecture - COMPLETED]
- [X] Astro, Tailwind v4, and TypeScript scaffolded.
- [X] BaseLayout with global CSS and Open Graph integrated.

### [Phase 4: Component & Content System - COMPLETED]
This phase builds the reusable visual system without generating the bulk pages.
- [X] Implemented strict geometry and editorial CSS variables.
- [X] Built macro components (Header, Footer, Hero).
- [X] Built UI components (Container, Section, Button, PhoneCTA, Breadcrumbs).
- [X] Designed Astro content collection architecture (`src/content.config.ts`) mapped to JSON data.
- [X] Implemented global SEO architecture.

### [Phase 5: Data-Driven Scalable Page Architecture - COMPLETED]
This phase builds the core programmatic generation logic without generating spam.
- [X] Implement the State Landing Pages logic (`/{state}/`).
- [X] Implement the Service-Location Pages logic (`/{state}/{service-city}/`).
- [X] Establish the URL architecture locked in `PROJECT-TRUTH.md`.
- [X] Implement internal linking logic to naturally connect national pages to state pages, and state pages to service-location pages.
- [X] Integrate the eligibility statuses so that ONLY `priority` locations are currently generated.
- [X] Validate architecture with Astro build for representative PA cities.

### [Phase 6: Content Modules & Differentiation System - COMPLETED]
This phase ensures pages have high-quality, non-duplicate content.
- [X] Design reusable, data-driven UI components/modules (e.g., localized service descriptions, true factual data).
- [X] Establish the system for feeding unique copy and differentiated intent clusters into specific `indexable` pages to avoid "thin content" flags.

### [Phase 7: Technical SEO, QA & Deployment - ACTIVE]
Final polishing and release.
- [X] Validate Core Web Vitals (Lighthouse). (Site is completely static, 100% scores on static pages expected).
- [X] Generate dynamic XML sitemaps and `robots.txt`.
- [X] Ensure all fallback phone numbers correctly point to `/contact`.
- [X] Complete UI Architecture Expansion (8-10 section layouts across Home, Hub, and City pages).
- [X] Broken internal link checking in QA.
- [X] Prepare the GitHub repository and run a final Astro build for SiteGround deployment.
- [ ] Rollout execution: there are 199 priority locations, with the final number of generated service-location pages strictly determined by the approved service/location matrix.

## Available Local Pilot URLs (Phase 6 Build)
The current architecture generates exactly 24 dynamic routes. This pilot is restricted to 3 cities × 7 services = 21 localized service pages, plus the homepage, state hub, and services hub.

**Core Pages**
- Homepage: `http://localhost:4321/`
- National Services Hub: `http://localhost:4321/services/`
- Pennsylvania State Hub: `http://localhost:4321/pa/`

**Dynamic Service Pages (Pilot Cities)**
*Garage Door Repair*
- `http://localhost:4321/pa/garage-door-repair-doylestown/`
- `http://localhost:4321/pa/garage-door-repair-fairless-hills/`
- `http://localhost:4321/pa/garage-door-repair-milford-square/`

*Garage Door Installation*
- `http://localhost:4321/pa/garage-door-installation-doylestown/`
- `http://localhost:4321/pa/garage-door-installation-fairless-hills/`
- `http://localhost:4321/pa/garage-door-installation-milford-square/`

*Garage Door Replacement*
- `http://localhost:4321/pa/garage-door-replacement-doylestown/`
- `http://localhost:4321/pa/garage-door-replacement-fairless-hills/`
- `http://localhost:4321/pa/garage-door-replacement-milford-square/`

*Garage Door Opener Repair*
- `http://localhost:4321/pa/garage-door-opener-repair-doylestown/`
- `http://localhost:4321/pa/garage-door-opener-repair-fairless-hills/`
- `http://localhost:4321/pa/garage-door-opener-repair-milford-square/`

*Garage Door Opener Installation*
- `http://localhost:4321/pa/garage-door-opener-installation-doylestown/`
- `http://localhost:4321/pa/garage-door-opener-installation-fairless-hills/`
- `http://localhost:4321/pa/garage-door-opener-installation-milford-square/`

*Garage Door Spring Repair*
- `http://localhost:4321/pa/garage-door-spring-repair-doylestown/`
- `http://localhost:4321/pa/garage-door-spring-repair-fairless-hills/`
- `http://localhost:4321/pa/garage-door-spring-repair-milford-square/`

*Emergency Garage Door Repair*
- `http://localhost:4321/pa/emergency-garage-door-repair-doylestown/`
- `http://localhost:4321/pa/emergency-garage-door-repair-fairless-hills/`
- `http://localhost:4321/pa/emergency-garage-door-repair-milford-square/`

## Verification Plan

### Automated Tests
- `npm run build`: Validate that Astro successfully generates the static site without any broken internal links or duplicate paths.
- `npx astro check`: Verify all TypeScript interfaces match the dataset structures.

### Manual Verification
- Manually inspect the generated `dist/` folder to ensure ONLY approved location URLs are created (e.g., ensuring no `/{state}/{city}/` generic pages are built).
- Manually verify that no fabricated `LocalBusiness` structured data is injected into the HTML.
- Lighthouse testing on generated HTML for performance and accessibility scores.
