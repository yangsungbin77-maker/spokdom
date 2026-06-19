# Auto-publish playbook (Spokdom)

A scheduled routine follows this procedure **once every two days**. The goal is not just to publish,
but to ship **one post that is more thorough and better-optimized for Google than the current top
results** for the target keyword. Each post includes 1 external link, 1 internal link, and 2 images,
and **must be fact-checked on the web before publishing**.

**Output language: English.** This is an English-market site. All post content, titles, and
descriptions are written in natural, native-sounding English.

**Niche: non-YMYL AI tool & SaaS reviews and comparisons.** Stay out of YMYL (finance, medical,
legal) advice. Focus on buy-intent clusters: alternatives, X vs Y, pricing/plans, and best-tool-for
[use case]. Where relevant, prefer recommending tools that have affiliate programs (ideally recurring
commission) — but the verdict is always driven by which tool is actually best, never by payout.

## Procedure (4 steps)

Working directory is the repo root (`spokdom`). If `node` is not on PATH, set it first.

### Step 1 — Get the assignment
```
node automation/prepare.mjs
```
Output JSON (= `automation/assignment.json`): `topic`, `pubDate`, `heroImage`, `internalLink{url,title}`,
`externalLink{url,label}`. If it stops with "no topics", do not write anything — **exit immediately**
(no empty posts).

### Step 2 — Deep competitor analysis (required before writing)
Search the `topic` with WebSearch and **open at least 5 of the top 10 results with WebFetch** to analyze.
- **Search intent** — does the searcher want information, a recommendation list, a how-to, or a tool/download?
- **Structure of top posts** — which H2 sections do they cover; what's the average length?
- **Common must-have checklist (required)** — list the items that appear in the majority of top posts.
  **Include every one of them** in our post, or we lose on intent satisfaction.
- **Gaps** — what the top posts miss or cover poorly. This is our differentiation.

Build an outline that **covers everything the top posts cover + fills the gaps**. Verify product facts
(tool names, pricing tiers, features, limits) during this step.

### Step 3 — Write the post
Write `src/content/blog/<english-slug>.md` following the quality & SEO rules below.

### Step 4 — Fact-check → publish
Re-verify factual claims (see fact-check rules), then:
```
node automation/finalize.mjs <slug>
```
It validates links, image, minimum length, and H2 count, runs the build, and on success auto-commits
and pushes. If it fails, fix per the message and re-run.

## Quality & format rules (required)

- Body **at least ~1,100 words** (recommended 1,200–1,800), and **more thorough than the average top
  competitor**. finalize blocks anything too short.
- **7–10 `##` H2 sections**, each at least 3 substantial paragraphs. Use comparison tables, step lists,
  checklists, real examples/scenarios, and an **FAQ (4+ questions)** to add length and value together.
- **Expansion pass (required):** after the first draft, re-read each section and strengthen anything
  thin or generic with concrete examples, numbers, and comparisons. Don't pad with filler — if short,
  add a sub-topic the competitors covered but you missed.
- No filler ("it's great", "very useful"). Use specific examples, reasons, real tool names, and
  comparisons. The reader should be able to act on this single post.
- Tone: helpful, first-hand, like someone who has actually used the tools. Avoid robotic label lists.
- **Affiliate disclosure:** if the post contains affiliate links, include a one-line disclosure near
  the top (the About and Privacy pages also cover this site-wide).

## SEO rules (required)

- **Title:** put the `topic` keyword **near the front**, naturally. Make it click-worthy, ≤ 60 chars
  recommended.
- **Description:** 120–155 chars including the keyword. It shows in search results, so write for clicks.
- **Keyword placement:** in the title (H1), the **first paragraph (within the first ~100 chars)**, at
  least one `##` H2, and naturally through the body. No keyword stuffing — use synonyms and related terms.
- **Structure:** scannable `##`/`###` hierarchy. Put the core answer near the top (fast intent match).
- **1 internal link:** `[natural anchor](internalLink.url)`. **1 external link:** `[natural anchor](externalLink.url)`.
- **2 images (required):** ① hero — frontmatter `heroImage` (layout auto-handles alt=title + OG).
  ② one in-body image — placed at `src/assets/posts/<keyword-slug>.png`, inserted around the 1/3–1/2
  mark as `![alt with target keyword](../../assets/posts/<keyword-slug>.png)`. **Filename and alt must
  contain the target keyword** (no empty alt, no "image1"). Put it in `posts/`, not the rotating
  `pool/`, so prepare won't reassign it. Generate with Higgsfield `recraft-v4-1` 2k cinematic.
- **slug:** short, meaningful kebab-case derived from the keyword (English).
- **Related keywords footer (required):** at the very end, after a `---`, one line of related keywords:
  `**Related keywords** — #keyword1 #keyword2 …` (target + synonyms + variants, 8–12 hashtags, no spaces).
  Only genuinely related terms — no stuffing.
- **Tables & callout boxes for readability:** write comparisons as Markdown tables. Use callout boxes
  for key summaries/tips/warnings. Boxes are raw HTML and **the inside must be HTML tags too** (Markdown
  is not rendered inside a div). Put one `cg-summary` 3-line box at the very top.
  - Format: `<div class="cg-box cg-summary"><span class="cg-title">📌 Quick take</span><p>…</p><p>…</p></div>`
  - Types: `cg-summary` (green) · `cg-tip` (blue) · `cg-warn` (yellow) · `cg-danger` (red). Defined in
    `src/layouts/BlogPost.astro`.
- **FAQ format for rich results:** write FAQ entries as `**Q. question**` on one line, then `A. answer`
  on the next. The template auto-extracts these into FAQPage structured data.
- frontmatter format:
  ```markdown
  ---
  title: 'Keyword-first English title'
  description: 'Keyword-rich 120–155 char summary'
  pubDate: '<assignment pubDate as-is>'
  heroImage: '<assignment heroImage as-is>'
  ---
  ```

## Fact-check rules (required before publishing)

- **(Required) Verify numbers, pricing, limits, dates against the primary source (official site) or 2+
  top results opened directly (WebFetch).** Never write from search-snippet summaries alone.
- **If sources disagree, don't assert** — use only the value they agree on, or note "varies by source,
  check the official page" and drop conflicting numbers.
- Verify **every concrete fact** (tool name, plan, price, feature, limit) on the web.
- If you can't confirm it, delete it or hedge ("typically", "in most cases").
- **Volatile info — never assert exact, time-sensitive specifics.** Pricing changes; say "starts at"
  or "free tier available", not "always $X". Don't quote exact prices as permanent.
- Don't use statistics with no clear source. **When in doubt, leave it out** (wrong info is worse than
  thin info).

## 🥇 Ranking strategy — SERP dissection · 10x · winnable keywords

A new domain has weak authority, so head keywords won't rank on content alone. The real strategy is:
**① pick a SERP you can win → ② write something dramatically more thorough than the top 10 → ③ build
internal authority with topic clusters.**

### A. SERP dissection (structure the analysis as a table)
Open the top 10 and record the below; the last two rows are where your edge comes from.

| Item | Notes |
| --- | --- |
| Search intent | information / recommendation list / how-to / tool-download — which is it |
| Common must-haves | sections the majority cover — **include every one** |
| Each post's strengths | what the top results do well (match at minimum) |
| Each post's weaknesses/gaps | thin or missing — **your differentiation (the #1 play)** |
| Average length | be more thorough than average (without filler) |
| SERP features | featured snippet · PAA (People Also Ask) · image pack present? |

### B. 10x elements (what competitors rarely include — add these)
- **First-hand experience & concrete scenarios** — "when X, do Y" (Google E-E-A-T Experience).
- **Decision tools** — comparison tables, checklists, simple math.
- **PAA-targeted FAQ** — turn "People Also Ask" into FAQ (template auto-generates FAQPage schema).
- **Primary-source citations + freshness** — official numbers + "as of 2026".
- **Featured-snippet targeting** — compress each H2's core answer into the first 2–3 sentences.

### C. Picking winnable keywords (higher score = more likely to rank)
Before adding a topic to topics.md, search it and look at the top 10 SERP.

| Signal | + winnable | − winnable |
| --- | --- | --- |
| Top results | many personal blogs/forums/thin pages | official orgs/big media/wikis |
| Content depth | even the top results are thin (room to beat) | already very thorough |
| Keyword length | specific long-tail (3+ words) | short head term |
| Search intent | informational/how-to (a post can satisfy) | transactional/brand/navigation |

→ Attack the keywords with more (+) first. Defer head keywords until authority builds. **Instant #1 is
a fantasy; stacking winnable long-tail to build traffic and authority is the real path.**

### D. Cluster internal links
Link posts within the same topic cluster to each other to concentrate authority (link to a **related**
post, not just any post). If prepare assigned an internal link that doesn't match the topic, swap it
for a more relevant existing post.

## When topics run out
If prepare stops with "no topics", don't publish — just exit (no empty posts). A human adds topics to
`automation/topics.md`.


## Extra rules — keyword frequency · CTA buttons · TOC (added 2026-06)

- **Keyword frequency**: place the main keyword once each in the title, first paragraph, and conclusion, plus 5-7 times naturally in the body. Never repeat any single word/phrase more than ~20 times (anti-stuffing) — spread with synonyms and related terms.
- **CTA buttons**: ⚠️ **only after the affiliate program is approved/active**. Until then, do NOT add affiliate CTA buttons or links (no dead/placeholder links). Once active, add 1-2 `.btn` buttons on recommendation posts.
  - Format: `<a class="btn" href="AFFILIATE/EXTERNAL URL" target="_blank" rel="nofollow sponsored noopener">→ Check the price</a>`
  - Affiliate links must use `rel="nofollow sponsored"`.
- **Table of contents (automatic)**: if a post has 3+ `##` H2 headings, the layout auto-generates a TOC — no need to write one. Make H2 titles clear enough that the TOC alone shows the flow.
