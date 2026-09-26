# Lovable Integration Prompt Template

Use this template when generating a Lovable prompt for any site being built with the Koray semantic SEO framework. Fill in the bracketed fields before sending to Lovable.

---

## Template

```
Build a content-first blog and resource platform for [SITE NAME] ([DOMAIN]).

## Rendering (Required)
- SSR (server-side rendering) on all blog and category pages. Google must receive fully rendered HTML on first request. No client-side-only rendering.
- Canonical URLs on every page (self-referencing).
- Article schema (JSON-LD) on every post: headline, author (Person), datePublished, dateModified, publisher (Organization with logo).
- BreadcrumbList schema on all pages below the homepage.
- FAQ schema on any post with a FAQ section.
- Open Graph tags: og:title, og:description, og:image, og:url, og:type.
- Twitter Card tags.
- Sitemap at /sitemap.xml — auto-updated as posts are added.
- robots.txt: allow all, disallow /admin/.
- All images served as WebP with width and height attributes set.
- No render-blocking scripts.

## URL Architecture
/                                    Homepage (I-node)
/blog/                               All-posts index (paginates across categories)
/[category-slug]/                    Category index (C-node per category)
/[category-slug]/[post-slug]/        Individual post (S-node)

## Categories to Launch
[LIST CATEGORY SLUGS HERE — one per line]

## Blog Post Template (mandatory layout)
Left column (65% width desktop):
- Breadcrumb: Home > [Category] > [Post Title]
- H1 (keyword-targeted, matches slug)
- Author byline with avatar, name, and update date
- Featured image (16:9, keyword alt text)
- Table of Contents (auto-generated from H2s, sticky on scroll)
- Article body
- Author bio box
- Related articles grid (3 posts, same category)

Right column (35% width desktop, sticky):
- CTA Widget: [DESCRIBE CTA — form fields, headline, button text]
- Wire form to Resend template [TEMPLATE ID] sending to [DESTINATION EMAIL]
- Trust signals below button: "[TRUST COPY]"

Mobile: sticky bottom bar with "[CTA BUTTON TEXT]" that expands to full form sheet.

## Author System
- [NUMBER] author profiles: name, title, avatar, bio (2-3 sentences), slug
- Author archive at /author/[slug]/
- Person schema with sameAs LinkedIn links
- Rotate authors across posts

## CMS Requirements
- Post creation: title, slug (auto from title, editable), category (single-select), author (select), featured image, body (rich text), meta title, meta description, date published, date modified (auto)
- Post statuses: Draft, Published, Scheduled
- Bulk JSON import (must support 10,000+ posts without manual steps)
- Admin at /admin/ — password protected

## Homepage Layout
[DESCRIBE HERO, CATEGORY GRID, FEATURED POSTS, CTA BANNER, FOOTER]

## Design Tokens
[REFERENCE EXISTING SITE OR DESCRIBE COLOR PALETTE, TYPOGRAPHY, BUTTON STYLES]

## SEO Meta
- <title>: [Post Title] | [Site Name]
- <meta name="description">: unique per page, 145-155 chars, from first paragraph
- Lighthouse SEO target: 100
- Lighthouse Accessibility target: 90+

## Do Not Build
- No e-commerce
- No user accounts
- No comment system
- No pop-ups or chat widgets (Core Web Vitals impact)
```

---

## Notes on Using This Template

**SSR is non-negotiable.** Lovable defaults to client-side rendering in some configurations. Explicitly requiring SSR ensures Google can crawl all category and post pages.

**CMS bulk import is non-negotiable.** The Koray framework requires publishing at high cadence (3-5 posts per week per category). Manual CMS entry does not scale. JSON import must be tested with 1,000+ records before launch.

**Author system is non-negotiable.** Google's E-E-A-T signals require identifiable, expert authors on YMYL-adjacent content. Anonymous "Admin" posts will not build authority in competitive verticals.

**Resend integration.** Lovable should already have the Resend API key and template from the client's existing projects. Reference by template ID — do not re-enter credentials.

**Category indexes must be content pages**, not just archive lists. Each category index needs: 150-word editorial intro, "Topics we cover" sidebar list, article grid, and the sticky CTA widget.
