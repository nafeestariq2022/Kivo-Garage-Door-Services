# Kivo Garage Door Services - Design Direction

## 1. Design Research Summary
I have inspected the local templates (`DoorSync`, `SureFix`, `Doorix`) and synthesized the overarching aesthetic of the garage door/home service industry. Most templates rely heavily on high-contrast, primary colors (navy/black and bright yellow) and heavily stylized, centered hero sections with dark overlays. While this clearly communicates "construction/repair," it often looks generic, template-driven, and lacks a premium, established brand feel. Our goal is to pivot away from these cliché local-directory looks into a distinctive, human-designed, and editorial visual system.

## 2. Reference-by-Reference Observations
- **DoorSync**: Utilizes a stark white, black, and bright yellow palette. The layout is highly traditional (hero, trust stats, 6-card service grid, testimonials, FAQ, contact). **Critique**: Highly legible but feels like a standard Envato template. The 6-card grid is repetitive.
- **SureFix**: Uses a dark navy background with bright yellow accents. Features a centered hero with a darkened image background, followed by a 3-step process and a standard card grid. **Critique**: The dark overlay hero is exactly the type of generic "stock photo with white text" pattern we want to avoid. 
- **Doorix**: A darker, slightly more modern approach mixing solid and outline typography. Uses pill-shaped buttons and Envato-style UI floats. **Critique**: The outline typography is a nice touch for a mechanical service, but the excessive rounded corners conflict with the "sturdy/architectural" nature of garage doors.

## 3. Common Patterns Worth Adopting
- Prominent and persistent CTA placement (especially phone numbers).
- Clear, immediate visibility of trust signals (years of experience, licensing, real statistics).
- Breakdown of services into scannable, distinct visual blocks (but we will execute this without standard identical cards).
- Step-by-step process sections that demystify the service.

## 4. Patterns to Avoid
- Centered heroes with darkened, generic stock photos and white text.
- Bright "construction yellow" paired with standard navy blue.
- 3x2 identical card grids with a stock photo on top and text below.
- Floating glassmorphism cards.
- Pill-shaped buttons (`rounded-full`) that look like SaaS UI.

## 5. Final Visual Direction
**"Architectural Sturdiness & Premium Reliability"**
Kivo Garage Door Services will look like a national, established, high-end service provider. The design will feel editorial, rooted in architectural photography, clean geometry, and controlled asymmetry. We will avoid the "cheap local repair" aesthetic in favor of a trustworthy, premium home-services brand.

## 6. Typography System
- **Heading Typeface**: **Clash Display** or **Archivo** (Bold, slightly condensed, geometric). Conveys structural integrity, mechanical precision, and modernity.
- **Body Typeface**: **Inter** or **DM Sans**. Highly legible, neutral, and clean.
- **Hierarchy**: Extreme contrast in font sizing. Massive, tight headings for heroes (`text-5xl` to `text-7xl`) paired with highly readable, slightly larger-than-normal body text (`text-lg`).
- **Styling**: Use uppercase selectively for kickers and subheadings to create an editorial feel.

## 7. Color System
- **Primary Background**: Alabaster / Off-White (`#F9F9F8`) - Adds human warmth, avoiding sterile `#FFFFFF`.
- **Primary Text/Brand**: Charcoal / Deep Slate (`#1A1C1E`) - Softer and more premium than pure black.
- **Accent/Action**: Rust / Terracotta (`#C25934`) or Ochre (`#D69E2E`) are current **candidates**. This replaces the cliché bright yellow with a more grounded tone. Note: This color is not permanently locked and will be refined based on Kivo brand positioning during final implementation.
- **Surface**: Muted Stone/Gray (`#E5E7EB`) for subtle section background changes without resorting to cards.

## 8. Spacing/Grid System
- **Grid**: 12-column CSS Grid.
- **Spacing**: Generous, deliberate padding. Use `py-24` or `py-32` for main sections to let content breathe.
- **Borders/Radius**: Sharp edges (`rounded-none`) or minimal radius (`rounded-sm`). Garage doors are architectural and geometric; our UI should reflect that sturdiness. No pill buttons.

## 9. Component Philosophy
Instead of repeating isolated "cards," we will use CSS Grid to create dynamic, editorial layouts (e.g., alternating large and small image blocks, text-heavy sidebars alongside image galleries). Components must be reusable (Hero, Trust Banner, Service List, FAQ) but designed so they don't look like isolated boxes floating on a page.

## 10. Homepage Direction
- **Hero**: Asymmetrical split layout. Left side: Strong typography (Headline, subtext, CTA). Right side: High-quality, un-overlayed image of a beautiful garage door or professional technician in natural light.
- **Trust Section**: Integrated cleanly into the grid below the hero, using typography rather than generic badge icons.
- **Services**: A list or masonry-style layout, rather than 6 identical square cards.
- **Coverage/Locations**: A clean, typographic list or map visualization pointing to the `priority` states/cities.

## 11. Service-Page Direction
- Consistent header style, but diving immediately into technical competence.
- Use a "sidebar navigation" (sticky left or right) for users to easily jump between Repair, Installation, Openers, etc.
- Focus on real problems, parts, and solutions rather than generic marketing fluff.

## 12. Location-Page Direction
- Follows the `/{state}/{service-city}/` structure.
- Must share the structural DNA of the Service pages but inject localized data (City name, state, specific local climate/architectural context if applicable, dynamic map integration).
- Avoid identical cloning; use conditional rendering to swap out imagery or layout order so each page feels individually crafted.

## 13. Image Strategy
- Focus on architectural home photography and crisp, well-lit garage door installations.
- Use realistic technician imagery (working on springs/openers) that doesn't look staged.
- **Rule**: No dark overlays. If text must go over an image, the image itself must have natural negative space (e.g., a clear sky or solid wall).
- **No Fakes**: Do not generate images of fake Kivo-branded trucks or fake offices.

## 14. Animation/Motion Strategy
- Extremely subtle. No scroll-jacking.
- Use simple fade-ins (`opacity` and slight `translate-y`) only for primary elements on first load.
- Hover states should rely on color shifts or slight border expansions, not massive scaling or floating shadows.

## 15. Mobile Strategy
- Typography scales down intelligently.
- Asymmetrical desktop grids stack cleanly into single columns.
- Sticky bottom CTA (Phone Number) on mobile to drive conversions.

## 16. Accessibility Considerations
- WCAG AA compliant contrast ratios (especially with the Rust/Ochre accent on Alabaster).
- Focus states must be explicitly styled (no default blue rings, use the Charcoal color).
- Semantic HTML (`<nav>`, `<article>`, `<section>`).

## 17. Performance Considerations
- Astro static generation.
- Zero client-side JavaScript unless required for the lead form or mobile menu.
- Images converted to WebP/AVIF via Astro's `<Image>` component.
- Tailwind CSS purged of unused styles.

## 18. Explicit "AI Website Giveaways to Avoid" Checklist
- [x] No purple/blue gradients or glowing blobs.
- [x] No glassmorphism.
- [x] No rounded pill buttons.
- [x] No 3-card identical grid repeating down the page.
- [x] No centered dark-overlay stock-photo heroes.
- [x] No fake numbers (e.g., "Trusted by 10,000+").
- [x] No excessive box-shadows on every element.
- [x] No formulaic "Problem -> Solution -> Testimonial" strict template on every page.

## 19. Originality Rules
- The design must look like it was hand-crafted in Figma by a senior designer specifically for Kivo.
- We will rely on typography, spacing, and image curation over CSS tricks.

## 20. Recommended Implementation Principles
- Build a global `Tailwind` config that enforces the color and typography system.
- Build a generic `Section` wrapper component that enforces the `py-24` vertical rhythm.
- Build UI primitives (`Button`, `Heading`, `Text`) before assembling complex sections.
