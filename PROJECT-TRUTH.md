# Kivo Garage Door Services - Project Truth

**Status**: Active Development (Phase 7: Technical SEO, QA & Deployment)

This document contains the authoritative project facts, decisions, constraints, architecture, data sources, business model, technical stack, and current assumptions.

## 1. Business Model [CONFIRMED]
- **Type**: US-focused rank-and-rent / lead-generation website.
- **Niche**: Garage door services (repair, installation, replacement, opener repair/installation, spring repair, emergency repair).
- **Monetization**: Leads routed via phone calls / LeadSmart / Ringba ecosystem.
- **Brand Rules**: Internal monetization data, CPLs, and buyer information must NEVER be exposed publicly. Do not fabricate entities, reviews, or physical offices. 

## 2. Brand & Domain [CONFIRMED]
- **Brand**: Kivo Garage Door Services
- **Domain**: kivogaragedoorservices.us

## 3. Public-Facing Brand & Content Rules [CONFIRMED]
- Kivo Garage Door Services should present publicly as a professional garage-door service brand.
- The internal rank-and-rent / lead-generation business model must not be exposed or emphasized in normal public-facing website copy.
- Public copy should use natural professional service language.
- Never fabricate or imply unsupported facts about Kivo.
- Never fabricate reviews/testimonials, exact pricing, discounts, physical offices, addresses, employees, technicians, licenses, certifications, awards, customer history, project history, years of experience, guarantees, response times, 24/7 availability, or same-day availability.
- Years of experience, customer/project information, credentials, or other business facts may be used only when verified and explicitly provided as approved business information.
- Do not use "our technicians" or equivalent language unless actual Kivo technicians are verified.
- Do not expose LeadSmart, Ringba, CPLs, buyers, routing rules, or internal monetization information.
- Do not create fake LocalBusiness data or fake local entities.
- These rules apply to all national, state, and service-city pages.

## 4. URL Architecture [DECIDED - LOCKED]
- **Homepage**: `/`
- **National Service Pages**: 
  - `/garage-door-repair/`
  - `/garage-door-installation/`
  - `/garage-door-replacement/`
  - `/garage-door-opener-repair/`
  - `/garage-door-opener-installation/`
  - `/garage-door-spring-repair/`
  - `/emergency-garage-door-repair/`
- **State Landing Pages**: `/{state}/` (e.g., `/texas/`)
- **Primary Location/Service Pages**: `/{state}/{service-city}/` (e.g., `/texas/garage-door-repair-houston/`)
- **Supporting Pages**: `/about/`, `/contact/`, `/service-areas/`, `/privacy-policy/`, `/terms/`

*Note: There will NOT automatically be a separate generic city page (e.g., `/texas/houston/`). The scalable SEO model is State pages + Selective service-city pages.*

## 5. Location Data & Eligibility [DECIDED]
- **Dataset**: 1,800 unique city/state locations and 3,745 ZIP records.
- **Eligibility**: Inclusion in the dataset does not guarantee a page. Pages are generated based on criteria defined in `LOCATION-ELIGIBILITY.md` (e.g. CPL >= $20 = approved, CPL >= $80 = priority).
- **Statuses**: `candidate`, `priority`, `approved`, `indexable`, `excluded`, `future`

## 6. SEO & Content Principles [CONFIRMED]
- **Audience First:** Write for a real homeowner first, not an SEO crawler. Copy should feel human, empathetic, and grounded in the visitor's situation.
- **Problem & Solution Structure:** Lead with the problem the visitor is experiencing (stuck door, damaged panel, etc.). Then, explain how the service solves that problem and improves their situation using persuasive benefits (safety, security, curb appeal, peace of mind).
- **Balanced Persuasion:** Do not make every section a sales pitch. Mix empathy, useful information, benefits, confidence, and clear CTAs. The copy must remain strong and persuasive without watering down ordinary service-benefit language.
- **Factual Boundaries:** Keep hard boundaries around fabricated Kivo-specific facts. Do not invent reviews, credentials, guarantees, fake technicians, pricing, or unsupported claims (e.g., "#1", "lowest price").
- Design for sustainable organic SEO. No thin doorway pages, spinning, keyword stuffing, or manufactured local entities.
- Cluster by search intent, not single keywords. Key clusters identified: Opener, Repair, Replacement, Spring, Installation, Commercial, Emergency.
- Google Ads competition must NOT be treated as organic SEO difficulty.
- Every indexable page must contain genuinely useful, locally relevant, and differentiated content.

## 7. Technical Stack & Design System [CONFIRMED]
- **Framework**: Astro
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Design System**: Defined in `DESIGN-DIRECTION.md`. Premium, editorial, human-designed.
  - **Colors**: Alabaster (#F9F9F8), Charcoal (#1A1C1E). Accent color (Rust/Terracotta) is a candidate and will be refined.
  - **Typography**: Clash Display / Archivo (Headings), Inter / DM Sans (Body).
  - **Geometry**: Sharp corners, generous padding, asymmetrical grids. No AI-generic gradients, glassmorphism, or pill buttons.
- **Architecture**: Static-first, SEO-focused HTML
- **Hosting**: SiteGround GrowBig (GitHub → Astro build → dist/ → SiteGround public_html/)
- **Media**: Optimized images (AVIF/WebP)
- **Version Control**: Git / GitHub

## 8. Performance & Technical SEO [CONFIRMED]
- Prioritize fast loads, minimal JS, strong Core Web Vitals, and semantic HTML.
- Proper canonicals, XML sitemap, Robots.txt, Open Graph, Breadcrumbs, structured data (only when accurate).

## 9. Data Model & Page Generation (Proposed Architecture) [TODO]
- **Concept**: A data-driven architecture where locations, services, SEO metadata, content inputs, internal links, and page eligibility can be managed through structured data (e.g., JSON/Markdown/CSV).
- **Entities**: 
  - Locations (states, cities, ZIPs, CPLs from `canonical_locations.csv`)
  - Services (Repair, Installation, Opener, etc.)
  - Service-location eligibility mappings
  - SEO metadata & content modules
  - Internal linking relationships
- *Note: This will allow activating/deactivating locations without rebuilding the architecture manually.*

## 10. Internal Linking [DECIDED]
- Homepage → national service pages → state pages → service + city pages.
- State pages link to relevant service/location pages.
- National service pages link to relevant state/location pages where appropriate.
- Location pages link naturally to relevant services and nearby/related locations.
- *No massive artificial link blocks.*

## 11. Data Sources [CONFIRMED]
- LeadSmart coverage / payout data (3,745 ZIPs)
- Secondary mentor/reference city dataset (1,000 cities, 893 overlap)
- Google Keyword Planner export (5,240 keywords)
- Processed Canonical Locations (`data/processed/canonical_locations.csv`)

## 12. Open Questions & Assumptions [OPEN QUESTION]
- **Routing Implementation**: Lead-routing implementation and analytics requirements need to be specified before development.
- **Content System**: The content differentiation system needs to be designed.
