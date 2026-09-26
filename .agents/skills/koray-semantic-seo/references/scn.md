# Semantic Content Network (SCN) — Reference Guide

## What Is a Semantic Content Network?

A Semantic Content Network is the internal linking architecture that connects all posts within a category (and across categories) into a coherent topical cluster. The SCN tells Google: "This site owns this topic."

A well-built SCN achieves 3 outcomes:
1. PageRank flows efficiently between posts — ranking power is not siloed.
2. Google can crawl the full topic without orphaned pages.
3. Users find related content without leaving the site, increasing engagement signals.

---

## The 3 Node Types

### S-node (Supporting Node)
A post that covers a subtopic within a category. S-nodes support the C-node by diving deeper into one aspect.

- Example: "How to Reduce Chargebacks for High-Risk Merchants" is an S-node supporting the "High-Risk Merchant Account" C-node.
- S-nodes link: up to the C-node, sideways to 2-4 related S-nodes.
- S-nodes do NOT link to every other page on the site — only to topically adjacent pages.

### C-node (Central Node)
The primary page for a topic cluster. Usually the category index page.

- Example: `/high-risk/` is the C-node for the high-risk category.
- C-nodes link: down to all S-nodes in the category, up to the homepage (I-node).
- C-nodes receive the most internal links and accumulate the most authority in the cluster.

### I-node (Informational Node)
Broad, top-of-funnel pages that introduce a topic and link down to C-nodes. Usually the homepage or a pillar page.

- Example: The homepage linking to all category indexes.
- I-nodes link: to C-nodes. They rarely link to S-nodes directly.

---

## The 6-Tier SCN Structure

Each category's SCN should cover all 6 tiers. This is the minimum coverage required for topical authority in that category:

### Tier 1 — Macro / Definitional
"What is X" and "How does X work" content. Broad, awareness-stage.

- Purpose: catches top-of-funnel traffic, establishes the category's existence to Google.
- Anchor text pointing here: category name, definitional phrases.
- Example: "What Is a High-Risk Merchant Account and How Does It Work?"

### Tier 2 — Operational
"How to do X" and "Steps to accomplish X" content. Process-oriented.

- Purpose: signals depth of coverage to Google, serves users in active decision stage.
- Example: "How to Apply for a High-Risk Merchant Account: Step-by-Step"

### Tier 3 — Payment / Financial
Cost, fees, rates, revenue, financial impact content. Commercial intent.

- Purpose: highest conversion potential; users comparing options.
- Example: "High-Risk Merchant Account Fees: What to Expect in 2026"

### Tier 4 — Growth / Marketing
How to grow, scale, acquire customers, market the business.

- Purpose: broadens topical authority beyond just "what is X" into adjacent queries.
- Example: "How to Market a High-Risk Business Without a Big Ad Budget"

### Tier 5 — Legal / Compliance
Regulations, licenses, compliance requirements, risk management.

- Purpose: captures high-value queries that competitors often ignore; strong E-E-A-T signal.
- Example: "State-by-State Compliance Requirements for High-Risk Merchants"

### Tier 6 — Technology / Tools
Software, platforms, integrations, automation, tech stack.

- Purpose: captures bottom-of-funnel comparison queries; strong conversion intent.
- Example: "Best Payment Gateways for High-Risk Merchants: Features Compared"

---

## Internal Linking Rules

### Mandatory Links Per Post
Every published post must have:
1. **1 link to its C-node** (the category index) — in the first 200 words.
2. **2-4 links to related S-nodes** in the same category — in body sections.
3. **0-2 cross-category links** — only where topically justified.

### Anchor Text Rules
- Anchor text must match the target page's H1 keyword (exact or near-exact).
- Never use "click here," "read more," or "this article."
- Vary anchor text slightly across multiple links to the same page (e.g. "high-risk merchant account" and "merchant accounts for high-risk businesses" both pointing to the same C-node).
- Maximum 2 links to the same URL within one post.
- Maximum 3 links total to any one URL from any post.

### Link Depth Rules
- No post should be more than 3 clicks from the homepage.
- Category indexes must be 1 click from the homepage.
- Posts must be 2 clicks from the homepage (via the category index).
- Orphaned pages (0 internal links pointing to them) must be fixed immediately.

### Do Not Link
- Do not link from an S-node to a post in a completely different category unless there is a direct topical connection.
- Do not link from a post to the homepage. (The homepage is an I-node; it receives links, it does not need to be linked to from posts.)
- Do not add more than 8 total links in a single blog post — link quality degrades.

---

## Crawl Efficiency Rules

Google's crawler has a budget. Pages that are expensive to crawl get crawled less frequently.

**To reduce cost of retrieval:**
- Answer the H1 keyword in the first sentence of the article.
- Answer each H2 in the first sentence of that section (no wind-up).
- Keep paragraphs to 3 sentences maximum.
- Use bulleted or numbered lists every 300 words.
- No paragraph orphans — never two consecutive paragraphs without a structural element (heading, list, or callout) between them.
- Include FAQ schema on every post (3-5 Q&A pairs minimum).
- Include Article schema and BreadcrumbList schema.

**To signal freshness:**
- Update `dateModified` in Article schema whenever a post is meaningfully updated.
- Add a "Last updated: [Month Year]" note at the top of the post.
- Refresh posts that have dropped more than 5 positions without new competition.

---

## SCN Health Checklist

Run this check on any category before calling it complete:

- [ ] C-node exists and links to all S-nodes
- [ ] All S-nodes link back to the C-node
- [ ] All 6 tiers have at least 1 post
- [ ] No orphaned posts (0 internal links pointing to them)
- [ ] No duplicate intent (two posts targeting the same keyword)
- [ ] Every post has Article schema and BreadcrumbList schema
- [ ] Every post has a FAQ section with FAQ schema
- [ ] Publishing cadence is active (at least 1 new post per week in this category)
