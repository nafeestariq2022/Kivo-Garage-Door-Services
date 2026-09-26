---
name: seo-strategy
description: ALWAYS use this skill when building any website, landing page, Next.js app, React site, HTML site, WordPress theme, or any web project — even if the user doesn't explicitly mention SEO. This contains mandatory build requirements that must be on every site we ship. Every page needs proper meta tags, schema, canonicals, breadcrumbs, alt text, Open Graph, robots.txt, sitemaps, HSTS, semantic HTML, and keyword-optimized content structure. Also use when creating sitemaps, site plans, URL structures, content docs, designer docs, or writing any content that will live on a website. If a Semrush or Ahrefs MCP connector is available, use it for keyword research to inform page titles, H1s, meta descriptions, and content strategy. If you're touching a website or writing content for one, read this first.
---

# SEO Site Build Framework

This is the master playbook for building websites. When a user says "build me a site for [company]," every page you create must follow these rules. This isn't optional optimization — it's how we build.

---

## 1. First Steps: Research & Structure

Before writing a single line of code, do this:

### Keyword Research (if Semrush/Ahrefs connector is available)
1. Pull organic keywords for the domain (or competitors if it's a new site).
2. Filter to KD 0-30 for longtail blog opportunities.
3. Filter to KD 0-50 for service/product page targets.
4. Group keywords into topical clusters aligned to the company's service lines or product categories.
5. Each cluster becomes a content silo: a parent service page + supporting blog posts that interlink.
6. Use the highest-volume keyword per cluster as the primary target for the service page. Secondary variations go in alt text, schema, and meta (see Semantic SEO below).

If no connector is available, ask the user for target keywords or research competitors manually.

### URL Structure & Sitemap
Design the URL structure BEFORE building. Rules:
- URLs reflect the path the user takes to get there. Navigation path = URL path.
- Max 3 levels deep. Keep it flat where possible.
- No parameters, underscores, or excessive nesting. Hyphens only.
- Topical silos are clear in the URL hierarchy.

Examples:
```
/                                    → Homepage
/services/                           → Services index
/services/seo/                       → SEO service page
/services/web-design/                → Web design service page
/blog/                               → Blog index
/blog/seo-strategies-for-dentists/   → Blog post (links back to /services/seo/)
/industries/                         → Industries index
/industries/healthcare/              → Healthcare vertical
/industries/healthcare/dental-marketing/  → Niche industry page
/locations/austin/                   → Location page
/about/                              → About
/contact/                            → Contact
```

### Sitemap & Site Plan Deliverables
When outputting a sitemap/site plan for dev or client review:
- Output as both organized markdown AND color-coded CSV/XLSX.
- Include columns: URL, page title, H1, meta description, parent page, nav placement, schema type, target keyword, notes.
- Color code by: new page, existing (no changes), existing (needs updates), blog, utility.
- Include nav structure (primary nav, footer, dropdowns) as a separate sheet/section.

---

## 2. On-Page SEO — Every Single Page

These are non-negotiable. Every page on every site must have all of the following.

### Head / Meta
- **`<title>`** — Target keyword FIRST, then filler. Google reads left to right. Under 60 characters.
  - Good: `Echeck Payment Processing | Accept Echecks for Business`
  - Bad: `Everything You Need to Know About Echeck Payments`
- **`<meta name="description">`** — Keyword-inclusive, compelling, under 160 characters.
- **`<link rel="canonical">`** — Self-referencing canonical on all main URLs. Paginated URLs canonical to the root URL.
- **Hreflang tags** if multi-language or multi-region.
- **No `noindex`** on any page that should be indexed. Verify before launch.
- **Favicon** included (`<link rel="icon">`).

### Open Graph & Social
Every page:
```html
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:image" content="..." />
<meta property="og:url" content="..." />
<meta property="og:type" content="website" />  <!-- "article" for blog posts -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="..." />
<meta name="twitter:description" content="..." />
<meta name="twitter:image" content="..." />
```

### Heading Structure
- **One H1 per page.** Keyword-optimized. Target keyword positioned first.
- H2s for major sections. H3s for subsections. Never skip levels.
- Headings should read as an outline of the page's content.

### Images
- **Alt text on every image.** Keyword-optimized but use DIFFERENT keyword variations than visible page copy (see Semantic SEO below).
- **WebP format** preferred for speed.
- **`loading="lazy"`** on all images below the fold.
- Descriptive filenames: `echeck-payment-processing.webp` not `IMG_4832.webp`.

### Semantic HTML
Use proper elements — Google reads these to understand page structure:
```html
<nav>       <!-- Navigation -->
<main>      <!-- One per page, wraps primary content -->
<article>   <!-- Blog posts, news articles -->
<section>   <!-- Thematic groupings within a page -->
<header>    <!-- Page or section header -->
<footer>    <!-- Page or section footer -->
<aside>     <!-- Sidebars, related content -->
```

### Breadcrumbs
- Breadcrumbs on every page except homepage.
- Must mimic URL structure exactly.
- Visible to users AND marked up with BreadcrumbList schema.

---

## 3. Schema Markup

Implement the correct schema type on every page:

| Page Type | Schema |
|---|---|
| Homepage | Organization (+ LocalBusiness if applicable) |
| Service pages | Service or Product |
| Local/location pages | LocalBusiness (location-specific NAP) |
| Blog posts | Article (with real author name + author page URL) |
| Product pages | Product (even without price/reviews — helps Google understand the page) |
| Category/collection pages | CollectionPage |
| All pages except homepage | BreadcrumbList |

### Schema Implementation Notes
- Organization schema: only on homepage. Include name, logo, URL, social profiles, contact info.
- LocalBusiness schema: homepage + each location page. Must have accurate NAP (Name, Address, Phone) per location.
- Article schema: every blog post. Must reference a real human author with a dedicated author page on the site.
- Product schema: still valuable without price or reviews — it helps Google crawl and categorize the product.
- Validate all schema at https://search.google.com/test/rich-results before launch.

---

## 4. E-E-A-T & CRO Signals

Google ranks sites higher when they demonstrate Experience, Expertise, Authoritativeness, and Trustworthiness. These aren't just SEO signals — they also convert visitors. Build every site with these baked in.

### Trust Signals Above the Fold
- **Reviews/testimonials** visible above the fold on the homepage and key service pages. Don't bury them — they're the first thing a visitor (and Google) should see proving credibility.
- **Star ratings, review count, or trust badges** (Google reviews, Trustpilot, BBB, industry certifications) in the hero or directly below it.
- **Client logos** or "trusted by" bar above the fold where applicable.

### Case Studies Page
- Every site should have a `/case-studies/` page (or `/results/`, `/portfolio/`, `/our-work/` depending on industry).
- Individual case study pages nested under it: `/case-studies/[client-or-project-slug]/`.
- Each case study should include: the problem, the solution, measurable results with specific numbers, and a client testimonial if possible.
- Case studies demonstrate **Experience** — proof the company has done the work.
- Add CaseStudy or Article schema to each case study page.
- Interlink case studies from related service pages ("See how we helped [client] achieve [result]").

### Industry Reports / Data Pages
- Build a `/reports/` or `/resources/` section for data-driven industry content.
- Research commonly searched statistical questions in the client's industry and answer them directly on the page.
- Include the question AND statistical answer prominently — optimized for featured snippets and AI answers.
- Use statistical images, charts, and tables. Image backlinks are common — other sites embed these visuals and link back, creating a diverse natural backlink profile.
- Link out to authoritative sources (government agencies, industry associations, peer-reviewed research) with contextual anchor text.
- Follow all content writing rules — clear, factual, number-specific, answer-first format.
- When optimized well, AI tools like ChatGPT will auto-cite these reports in generated content, earning passive reference-style backlinks.

### Blog Authors & Author Pages
- Every blog post attributed to a **real person** — never "Admin" or the company name.
- Author byline on every post linking to their dedicated author page.
- **Author pages** must include: real headshot, short bio with relevant credentials/experience, links to all their published articles on the site, and optionally links to their LinkedIn or professional profiles.
- This is critical for E-E-A-T. Google checks whether the person writing about a topic has genuine expertise.
- Article schema on every blog post must reference the author's name and author page URL.

### Additional Trust Architecture
- **About page** with real team members, company history, and credentials. Not generic filler.
- **Contact page** with real address, phone number, email, and embedded map if applicable.
- **Privacy Policy and Terms** pages — required for trust signals.
- **Secure site (SSL/HSTS)** — covered in Technical Requirements.
- **Consistent NAP** across the site and all external citations.

---

## 5. Semantic SEO Strategy

This is how we rank for multiple keyword variations without stuffing the front-end.

### The Rule
Prioritize ONE keyword variation across elements users see (H1, page title, headings, visible body). Optimize for OTHER variations in elements users don't directly read:

| Element | What goes here |
|---|---|
| H1 / Page title | Primary target keyword |
| Visible body copy | Primary keyword + close variations naturally |
| Image alt text | Different keyword variations |
| Schema descriptions | Different keyword variations |
| Meta description | Different keyword variations |
| Internal link anchor text | Different keyword variations |

### Example
Page target: **"Custom Branded Merchandise for Events"**

- **H1**: "Custom Branded Merchandise for Events"
- **Body**: "branded merchandise," "custom event products"
- **Alt text**: "promotional products for corporate events"
- **Schema description**: "branded promotional items for trade shows and conferences"
- **Internal link anchor from another page**: "branded swag for trade shows"
- **Meta description**: "event merchandise and promotional giveaway items"

Google correlates all these signals and associates the page with every variation — without any of them competing on the visible page.

---

## 6. Blog Architecture

Every blog must be built with these components:

### Blog Post Template Requirements
- **Table of contents** at the top with anchor links to each section.
- **Pinned/sticky CTA** (floating sidebar or bottom bar) — always visible while reading.
- **Inline CTAs** within the body content (after 2nd or 3rd section, and near the end).
- **Author byline** with link to the author's page. Authors must be real people.
- **Author pages** with headshot, bio, credentials, and links to all their published articles. Supports E-E-A-T signals.
- **Article schema** on every blog post referencing the author.

### Internal Linking Within Blogs

**Blog → Service Page**:
Every blog post links back to its parent service page with keyword-optimized anchor text.
- Example: Blog "How to Accept Echeck Payments" links to the echeck service page with anchor text "accept echecks for your business."

**Blog → Blog Cross-Links**:
When topics overlap:
1. Add a section with the related blog's title as the heading.
2. Write 2-3 sentences about that topic.
3. Internal link to the full article with keyword-focused anchor text (exact title or variation).

### Content Ratio
- 75% of the blog directly answers the main topic.
- 25% covers supporting subtopics in 2-3 sentences each, linking to the detailed resource.
- Anchor text on internal links must match the target article's keyword or topic.

---

## 7. Content Writing Rules

All content on the site — pages, blogs, descriptions — follows these rules. They're designed for Googlebot information retrieval and featured snippet / AI answer positioning.

**1. Be Clear and Certain.** Factual statements, not hedging. "Bananas are rich in potassium." Not "Bananas might have some health benefits."

**2. Avoid Fluff.** No filler words. Every sentence adds information. "The report contained 10 data charts explaining quarterly growth." Not "The report was quite interesting."

**3. Use Specific Numbers.** Never "many" or "lots." Pair numbers with adjectives. "We found 4 essential steps to reduce energy costs."

**4. Match Verbs to Context.** "Improve skills" / "Increase steps" — not the reverse.

**5. Provide Examples After Plural Nouns.** "3 essential vitamins like Vitamin C, D, and B12." Not "3 essential vitamins to consider."

**6. Consistent Sentence Structure.** Listed items start with the same part of speech. "Wash the vegetables. Chop the onions. Add salt." Not "Wash the vegetables. The onions need chopping."

**7. Optimize Subtext.** After a heading, the first sentence directly answers the heading. Heading: "How to Save Money" → "To save money, start by creating a monthly budget."

**8. Answer Immediately.** The answer goes at the START of the first sentence. No preamble, no "Many people wonder..." Just answer.

**9. Anchor Text Alignment.** Anchor text matches the target page's title or keyword. Never "click here" or "read more."

**10. Optimize for Search Engines and AI.** Use question-and-answer format where appropriate. Concise, direct structure.

**11. Ask Unique Questions.** Section headings as specific questions. "What are the top 3 security risks for small business websites?" Not "Why is security important?"

**12. 75/25 Rule.** 75% main topic, 25% related subtopics with internal links.

**13. External Linking.** Link out to authoritative sources — industry leaders, government agencies, statistics, research. Use natural contextual anchor text (branded or keyword-focused), NOT APA-style inline references. These outbound links signal to Google that your content is well-researched and connected to trusted sources.

### Blog Formatting
- No bold in body copy.
- No em dashes in body copy.
- 800+ word minimum per blog article.
- Natural, contextual internal links.

---

## 8. Sitewide Technical Requirements

### robots.txt
```
User-agent: *
Allow: /
Sitemap: https://[domain]/sitemap.xml
```

### XML Sitemap
- Auto-generated, includes all indexable pages.
- Exclude noindex pages, redirects, parameterized URLs.
- Submit to Google Search Console.

### Security & Performance
- **HSTS enabled** — Google prefers this security setting.
- **SSL certificate** active on all pages.
- **Minified JS and CSS.**
- **No render-blocking resources** — audit and remove unnecessary scripts.
- **Core Web Vitals** optimized: LCP < 2.5s, FID < 100ms, CLS < 0.1.
- **Mobile-first responsive** — Google indexes mobile-first.

### Redirects & Errors
- Custom 404 page with navigation back to key pages.
- 301 redirects for any changed URLs.
- Flatten redirect chains (A→B→C becomes A→C).

---

## 9. Multi-Location Sites

When the client has multiple locations:
- Primary location's existing optimization stays untouched.
- New locations get dedicated pages: `/locations/[city]/`.
- Each location page lists all services/treatments available at that location.
- Service pages can mention all locations served (no need to duplicate every service page per location).
- LocalBusiness schema on each location page with that location's specific NAP data.
- Location pages interlink with relevant service pages and blog content.

---

## 10. Quick Reference — Page Type Cheat Sheet

### Homepage
- Organization schema (+ LocalBusiness if applicable)
- H1: brand + primary keyword
- No breadcrumbs
- Links to all major service categories
- Reviews/testimonials above the fold
- Client logos or trust badges above the fold

### Service Page
- Service/Product schema + BreadcrumbList schema
- H1: target keyword first
- Breadcrumbs matching URL path
- Internal links from related blogs
- Reviews/testimonials above the fold or directly below hero
- Link to relevant case studies

### Blog Post
- Article schema + BreadcrumbList schema
- H1: target keyword first
- TOC with anchor links
- Author byline → author page (real person, real photo, real credentials)
- Pinned CTA + inline CTAs
- Links back to parent service page
- Cross-links to related blogs

### Case Study Page
- Article or CaseStudy schema + BreadcrumbList schema
- H1: "[Client/Project] — [Result]"
- Structure: Problem → Solution → Results (with specific numbers)
- Client testimonial included
- Interlinked from related service pages

### Location Page
- LocalBusiness schema + BreadcrumbList schema
- H1: "[Service/Brand] in [City]"
- Location-specific NAP
- Lists all services at that location
- Location-specific reviews if available

### Product Page
- Product schema + BreadcrumbList schema
- H1: product name + key modifier
- Alt text with keyword variations

### Category/Collection Page
- CollectionPage schema + BreadcrumbList schema
- H1: category keyword
- Links to all child pages

### Industry Report / Data Page
- Article schema + BreadcrumbList schema
- H1: statistical question or data topic, keyword first
- Charts, tables, statistical images throughout
- Q&A format for featured snippet targeting
- External links to authoritative sources (contextual anchor text, not APA)
- Designed to earn organic backlinks and AI citations
