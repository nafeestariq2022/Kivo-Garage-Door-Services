---
name: koray-semantic-seo
description: >
  Apply Koray Tuğberk GÜBÜR's holistic semantic SEO framework to audit, restructure, and produce content for any website. Use this skill whenever the user asks to: build a topical map, plan a content strategy, write or optimize blog posts, improve topical authority, design URL/site architecture for a blog, set up a Semantic Content Network (SCN), plan internal linking, generate SEO briefs, audit a site's content coverage, or automate blog production at scale. Also trigger when the user mentions Lovable site edits, programmatic SEO, content gaps, semantic SEO, entity-based SEO, or when they ask how to dominate a niche with content. Do not require the user to name Koray explicitly — trigger on any content strategy or SEO architecture task.
---

# Koray's Semantic SEO Skill

This skill implements Koray Tuğberk GÜBÜR's holistic semantic SEO methodology end-to-end: topical maps, Semantic Content Networks, algorithmic authorship, internal linking, and site architecture. It is built for two use cases:

1. **Editing an existing site** — auditing coverage, restructuring URLs, fixing internal links, rewriting posts.
2. **Building a new content machine** — designing the topical map, SCN, and post pipeline from scratch (including Lovable integration).

---

## Core Formula

**Topical Authority = Topical Coverage + Historical Data (+ Cost of Retrieval)**

- **Topical Coverage**: Every question a user could ask within a topic is answered somewhere on the site, organized into a logical hierarchy.
- **Historical Data**: Google rewards sites with a sustained publishing track record in a topic. Momentum (consistent cadence) compounds authority.
- **Cost of Retrieval**: How efficiently Google can extract the correct answer from your page. Lower cost = more crawlable, structured, answer-first content.

---

## The 3 Core Artifacts

Every Koray SEO engagement produces 3 artifacts. Read the reference files before producing any of them.

### 1. Topical Map → `references/topical-map.md`
The complete blueprint of every URL the site needs. Built from a phrase taxonomy and organized by contextual hierarchy.

### 2. Semantic Content Network (SCN) → `references/scn.md`
The internal linking architecture connecting all posts within and across categories. Defines S-nodes, C-nodes, and I-nodes.

### 3. Algorithmic Authorship Rules → `references/authorship-rules.md`
41 sentence-level writing rules that produce crawlable, answer-first, featured-snippet-eligible content ("Koraynese").

---

## Workflow — Choose Your Path

### Path A: Audit an Existing Site

**Step 1 — Crawl and inventory**
- Fetch the sitemap (`/sitemap.xml`) to get all URLs
- Group URLs by topic cluster (H2 and H3 of the topical map)
- Identify coverage gaps: which of the 6 SCN tiers (macro, operational, payment, growth, legal, tech) are missing?

**Step 2 — Score existing posts**
- Does each post have a keyword-targeted H1 matching the URL slug?
- Does each H2 open with a direct answer sentence?
- Are there at least 3 internal links per post?
- Is there a FAQ section with FAQ schema?
- Is there a bulleted list per 300 words?
- Apply the full authorship rules from `references/authorship-rules.md`

**Step 3 — Prioritize fixes**
Priority order: (1) pages ranking position 4–15 with high volume (quick wins), (2) pages with broken internal links, (3) pages missing from the topical map, (4) pages with thin content.

**Step 4 — Report to user**
One summary block: coverage gaps, posts needing rewrites, missing URLs to build, internal link opportunities.

---

### Path B: Build a New Content Site (Lovable Integration)

**Step 1 — Define the Central Entity and Domain**
Identify: Central Entity (what the site is about), Central Topic (the single keyword the homepage targets), Central Knowledge Domain (the full knowledge graph the site will own).

**Step 2 — Build the Topical Map**
See `references/topical-map.md`. Output: full URL list organized by category > subcategory > post, matching the schema in `assets/topical-map-schema.json`.

**Step 3 — Define the SCN Per Category**
See `references/scn.md`. Each category (top-level folder) is its own SCN with all 6 tiers.

**Step 4 — Generate the Lovable Prompt**
See `prompts/lovable-integration.md` for the exact prompt structure to give Lovable to build the site with correct SSR, schema, CMS, author system, and CTA integration.

**Step 5 — Write Content to Brief**
Apply authorship rules from `references/authorship-rules.md`. Every post needs: keyword H1, question H2s, answer-first sentences, FAQ section, bulleted lists, Article schema, BreadcrumbList schema, and 3–5 internal links.

---

## Quick Reference — Koray's Terminology

| Term | Definition |
|---|---|
| Topical Authority | Site's ability to rank for all queries in a topic, built via coverage + history |
| Topical Map | Blueprint of all URLs needed to achieve full coverage of a topic |
| SCN | Semantic Content Network — the internal linking system connecting a category |
| S-node | Supporting node — a post that supports a C-node by covering a subtopic |
| C-node | Central node — the primary post for a topic cluster (usually the category index) |
| I-node | Informational node — broad awareness posts that link down to C-nodes |
| Algorithmic Authorship | 41 sentence-level rules for producing crawlable, answer-first content |
| Macro intent | Top-of-funnel: what is X, how does X work |
| Micro intent | Bottom-of-funnel: how do I do X, best X for Y |
| EAV | Entity-Attribute-Value — how Google understands entities on a page |
| FMP | First Meaningful Paragraph — the opening answer block Google extracts for snippets |
| Web Decay | Traffic loss from outdated, thin, or stale content; requires regular refresh |
| Momentum | Sustained publishing cadence that signals consistent authority to Google |
| KD threshold | Koray targets KD < 35 for new sites; < 50 for established sites |
| Query Network | The full set of related queries around a central topic |
| Query Gap | Queries in the network not yet covered by any page on the site |

---

## Always Do Before Writing Any Content

1. Read `references/authorship-rules.md` — apply all 41 rules
2. Check URL structure — slug must match H1 keyword
3. Verify no duplicate content against the existing sitemap
4. Assign the post to one of the 6 SCN tiers
5. Plan 3–5 internal links (at least 1 to the category C-node)
6. Plan 1 FAQ section with at least 3 Q&A pairs
7. Confirm Article schema and BreadcrumbList schema will be present

---

## Never Do

- Never use em dashes in body copy
- Never bold text in body paragraphs (bold in headings only)
- Never stack 2 paragraphs in a row without a heading, H3, or list between them
- Never write a vague H2 like "Overview" or "Introduction" — every heading is a specific question
- Never start a sentence with "Many people" or "It is important to note"
- Never use "many," "lots," or "several" — always use a specific number
- Never publish without an internal link to the category C-node
- Never leave a page without a FAQ section if the topic supports questions

---

## Reference Files (read when needed)

| File | When to Read |
|---|---|
| `references/topical-map.md` | When building or auditing the URL structure |
| `references/scn.md` | When designing internal linking or defining a new category |
| `references/authorship-rules.md` | Before writing or editing any blog post |
| `prompts/lovable-integration.md` | When generating a Lovable build prompt for a new site |
| `assets/topical-map-schema.json` | When outputting a topical map in structured format |
