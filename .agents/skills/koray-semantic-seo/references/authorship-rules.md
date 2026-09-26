# Algorithmic Authorship Rules

These are Koray's sentence-level writing rules for producing content that maximizes crawlability, featured-snippet eligibility, and topical authority signals. All 41 rules apply to every blog post. The style these rules produce is called "Koraynese."

Apply every rule before publishing. Check against the compliance checklist at the bottom.

---

## The Core Principle

Every sentence should serve one of 3 functions:
1. **Answer** — directly answers the heading or subheading above it.
2. **Prove** — provides a number, source, or example that validates the answer.
3. **Extend** — adds a related fact that increases the entity coverage of the page.

Filler sentences (transitions, opinions without data, preamble) reduce the signal-to-noise ratio. Remove them.

---

## Structure Rules

**Rule 1 — One H1 per article.** The H1 is the target keyword. It matches the URL slug exactly or near-exactly.

**Rule 2 — Every H2 is a specific question or descriptive phrase.** Never "Overview," "Introduction," or "Conclusion." Good: "How Much Do High-Risk Merchant Account Fees Cost?" Bad: "About Fees."

**Rule 3 — The first sentence after every H2 directly answers the heading.** No wind-up. No "In this section, we will discuss..." The answer is sentence 1.

**Rule 4 — No two paragraphs appear consecutively without a structural element between them.** Between any two paragraphs: use an H3, H4, bulleted list, numbered list, or callout box.

**Rule 5 — Maximum 3 sentences per paragraph.** Most paragraphs should be 1-2 sentences. Long paragraphs reduce crawlability.

**Rule 6 — At least 1 bulleted or numbered list per 300 words of body content.**

**Rule 7 — Every article includes a FAQ section** with at least 3 Q&A pairs. The FAQ section uses question H3s with direct-answer paragraphs below.

**Rule 8 — Every article has a Table of Contents** linking to each H2. This improves crawlability and reduces cost of retrieval.

**Rule 9 — Target 600-900 words for standard blog posts.** Long-form (1,200+ words) only when the topic genuinely requires comprehensive coverage (e.g. "Complete Guide to X").

**Rule 10 — Every article has a First Meaningful Paragraph (FMP)** — the first paragraph answers the article's central question in 2-3 sentences. This is what Google extracts for featured snippets.

---

## Sentence-Level Writing Rules

**Rule 11 — Answer-first sentence structure.** Put the conclusion at the start. "ACH payments cost 0.5% per transaction, compared to 2.9% for credit cards." Not: "When comparing payment methods, there are several factors to consider."

**Rule 12 — Use specific numbers. Always.** Never "many," "most," "several," "some," "a lot of." Every claim that can have a number should have one.

**Rule 13 — Pair numbers with adjectives.** "3 essential steps to reduce chargebacks" not "steps to reduce chargebacks."

**Rule 14 — Use SPO sentence structure.** Subject-Predicate-Object. "High-risk merchants pay 1.5% to 3.5% in processing fees." Avoid inverted or passive constructions.

**Rule 15 — Factual statements over opinions.** "High-risk merchant accounts take 2-5 business days to approve." Not "Getting approved can sometimes feel challenging."

**Rule 16 — No hedging language.** Remove: "might," "could potentially," "in some cases," "it's possible that," "generally speaking." Every sentence is a definitive statement.

**Rule 17 — No filler openings.** Never start an article with: "In today's world," "It is well known that," "Many business owners wonder," "Have you ever thought about."

**Rule 18 — No preamble after headings.** The sentence directly after an H2 is the answer, not a setup for the answer.

**Rule 19 — Provide examples after plural nouns.** "There are 3 fees associated with high-risk accounts: the monthly fee, the chargeback fee, and the rolling reserve." Not: "There are several fees to be aware of."

**Rule 20 — Consistent sentence structure within lists.** All bullet points in a list start with the same part of speech (all nouns, all verbs, all adjectives). Never mix.

---

## Keyword and Entity Rules

**Rule 21 — Include the target keyword in the H1, in the first 100 words, and in at least 1 H2.**

**Rule 22 — Use keyword variations throughout the article.** If the target is "high-risk merchant account," also use: "merchant account for high-risk businesses," "high-risk payment processing account," "merchant accounts in high-risk industries." This builds EAV (Entity-Attribute-Value) coverage.

**Rule 23 — Include related entities in the article.** For a post about "high-risk merchant accounts," related entities include: payment processors, chargebacks, rolling reserves, ACH payments, credit card networks. Name them explicitly.

**Rule 24 — Use alt text on every image.** Alt text should include the target keyword or a close variation.

**Rule 25 — Name your sources.** "According to NACHA, the average ACH transaction costs $0.26." Not "According to industry sources."

---

## Formatting Rules

**Rule 26 — No em dashes anywhere in body copy.** Use a colon (:) or a comma instead.

**Rule 27 — No bold text in body paragraphs.** Bold is for headings only. Using bold mid-paragraph dilutes the heading hierarchy Google uses to understand page structure.

**Rule 28 — No italics for emphasis.** Italics are acceptable for titles of publications, not for adding stress to words.

**Rule 29 — Use H3 and H4 aggressively.** Do not let any H2 section run longer than 300 words without an H3 break.

**Rule 30 — Use numbered lists for sequences and steps.** Use bulleted lists for non-sequential items. Never use a bulleted list for a process that has a required order.

---

## Internal Linking Rules (in authorship context)

**Rule 31 — Anchor text matches the target page's H1.** If linking to a page with H1 "ACH Payment Processing," the anchor text is "ACH payment processing" or a close variation. Never "click here" or "learn more."

**Rule 32 — Maximum 2 links to the same URL in one article.**

**Rule 33 — Maximum 8 total outbound links per article** (internal + external combined).

**Rule 34 — At least 1 link to the category C-node in the first 200 words.**

**Rule 35 — External links open in a new tab.** Internal links open in the same tab.

---

## Schema and Technical Rules

**Rule 36 — Every post has Article schema** (JSON-LD): headline, author (Person), datePublished, dateModified, publisher (Organization with logo).

**Rule 37 — Every post has BreadcrumbList schema** matching the visible breadcrumb.

**Rule 38 — Every post with a FAQ section has FAQ schema** (Question/Answer pairs matching the FAQ content).

**Rule 39 — The canonical URL is self-referencing** on every post.

**Rule 40 — The meta description is unique** per page, 145-155 characters, written from the FMP (First Meaningful Paragraph).

**Rule 41 — The page title is unique**, contains the target keyword, and is under 60 characters: "[Target Keyword] | [Site Name]"

---

## Compliance Checklist (run before publishing every post)

- [ ] H1 matches URL slug (exact or near-exact)
- [ ] First sentence of article answers the H1 question
- [ ] Every H2 is a specific question or descriptive phrase
- [ ] First sentence after every H2 directly answers the heading
- [ ] No two consecutive paragraphs (structural element between all paragraphs)
- [ ] No paragraph longer than 3 sentences
- [ ] At least 1 list per 300 words
- [ ] FAQ section with 3+ Q&A pairs
- [ ] Table of Contents present
- [ ] Target keyword in H1, first 100 words, and at least 1 H2
- [ ] Specific numbers in every major claim (no "many" or "several")
- [ ] No em dashes anywhere
- [ ] No bold in body paragraphs
- [ ] No hedging language
- [ ] Anchor text matches target page H1
- [ ] At least 1 internal link to category C-node in first 200 words
- [ ] Article schema (JSON-LD) present
- [ ] BreadcrumbList schema present
- [ ] FAQ schema present
- [ ] Meta description 145-155 characters, unique, from FMP
- [ ] Page title unique, under 60 characters, contains target keyword
- [ ] All images have keyword-relevant alt text
