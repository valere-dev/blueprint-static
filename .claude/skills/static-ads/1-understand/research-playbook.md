# Research Playbook — finding winners and studying competitors

Where to find ads that are winning, how to tell they are winning without spend data, how to study a
competitor end to end (ads → landing pages → product pages → offers → quizzes), how to mine the voice of
customer, and what each step costs. Everything runs on the VPS (`ssh vps-claude`), never in the Mac's
browser.

---

## 1. Source map

| Source | Best for | Cost | Main gotcha |
|---|---|---|---|
| **TrendTrack** (REST `https://api.trendtrack.io/v1`, key in `/etc/secrets/trendtrack_api_key`; or the TrendTrack MCP) | Ad search by domain, run-time filters, brand trackers, scaling ads, transcripts, shop search, landing pages | ~1 credit per row via REST (~1.5× via MCP); `lookup` = 0 credit | Credits shared with scheduled jobs; `sortBy=reach` returns 0 for US ads; `longestRunning` returns empty; ~1-day lag on new ads; weak on cuts |
| **Meta Ad Library via Apify** (`apify~facebook-ads-scraper`, token `/etc/apify/token`) | Full ad lists for a domain, sorted by Meta's impressions order, with media and copy | Low (≈ $8.6 for 1,295 ads across 4 brands) | Monthly cap; US impression numbers aren't public, only the ORDER |
| **Meta Ad Library direct from the VPS** | Free spot checks, "N ads use this creative", exact active hours, cut dates | Free | ~30 results per query from a datacenter IP; soft block at ~100 requests / 23 min; never 2 scrapers at once |
| **Radar** (`radar.machineroom.app`, `/root/workspace/radar/`) | Daily life of one competitor's ads: launches, cuts, lifetimes, pages, products | TrendTrack ~250 credits/day | TrendTrack sees few cuts (lifetimes inflated) |
| **Scaling shops** (`scaling.machineroom.app`, `/root/workspace/scaling/`) | New shops whose active ads grow fast; product discovery | ~1 credit/row | Shop `createdAt` = TrendTrack indexing date, not launch |
| **Competitor list** (`brands.machineroom.app`, `/root/workspace/competitors/big-list-2026-09.md`) | Who to watch per brand (Minx, Wildhorn, big US supplement spenders) | — | Snapshot from early September |
| **Offers study** (`offers.machineroom.app`, `/root/workspace/competitors/offers/`) | Real landing pages, bundles, gifts, mobile captures of ~120 brands | Done | Rebuild only with a budget |
| **Annotated swipe** (`/root/claude-vault/knowledge/copywriting/swipe-annotated/`, 197 winners) | Video winners already decoded (DNA, beat map, steal-this, score) | Free | Mixed niches |
| **Template folders** (`/root/workspace/wh-remix/templates/`: before-after, bold claim, feature-benefit, meme, negative hook, problem-solution, us vs them, offer/sales, statistic) | Static templates by concept | Free | Sort into families before use |

---

## 2. TrendTrack recipes

**Statics of a domain, newest and longest-running** (`/root/workspace/competitors/tt_statics.py
<domain> <slug>`; `tt_dl_only.py <slug>` re-downloads without credits):
```
search=[domain], searchType="domain", mediaType="image", status="all", sortBy="newest", order="desc"
→ newest 30
same + minDaysRunning=<threshold>  → the "most performing" proxy
```
Choose the threshold by probing totals (`limit=1`) at several `minDaysRunning` values until ~30–45 ads
remain. Thresholds used: Primal Viking ≥ 200 days (32 statics), Mars Men ≥ 200 (39), Ancestral ≥ 200
(44), Primal Storm ≥ 135 (29 — young brand).

**Why run time and not reach**: `sortBy=reach` returns 0 for US ads and `sortBy=longestRunning` returns
empty (API bug). Run time is the honest proxy.

**MCP tools for a brand overview** (Step 1B of the blueprint): `search_advertisers` / `lookup` (pages of
the competitor AND our brand) · `search_ads` / `get_brandtracker_scaling_ads` (active, past, scaling) ·
`get_brandtracker_transcripts` (video transcripts already indexed) · `analyze_tracked_brand` /
`brief_competitor` (strategic overview) · `search_shops` / `analyze_brand_changes` (traffic, trend, offers)
· `search_emails` / `analyze_shop_emails` (email sequences).

**Freshness filter that works** (product discovery): don't trust shop `createdAt`. Use the weekly
`advertising.history`: keep shops where ads ≈ 0–10 around 60 days ago and active ads ≥ 50 now; or
`search_ads` with `created_after = today − 60 d` + `sort_by reachDelta7d` (ad `firstSeenAt` = real first
run date).

**Givenche's three hacks** (ads > traffic; traffic data lags 30–60 days):
1. Recent shops sorted by active ads (many show 0 traffic but are scaling).
2. AppLovin pixel on shops < 3 months old (insiders scaling on a new network).
3. Recurring products (subscription apps installed: Kaching Subscriptions, Recharge, Seal…) = big LTV.

**Scaling calculation** (scaling-shops method): last 5 weekly points of `advertising.history`, ≥ 3
points, last > first, growth ≥ +50 %. Collapse mirror shops (identical ad history) into one card.

---

## 3. Meta Ad Library via Apify (the full-library pull)

Actor `apify~facebook-ads-scraper`, parameters used (`/root/workspace/competitors/adlib/collect.py`):
`active_status=all`, `ad_type=all`, `country=ALL`, query = the landing DOMAIN, `sort_data[mode] =
total_impressions`, `sort_data[direction] = desc`, limit per set (e.g. 1,200 for small brands = all ads;
220–320 for big ones). Second set per big brand: the 100 most recent launches (`sort_data[mode] =
time_active` for "newest").

What you get: ad id, page, start/end, active flag, variants (DCO), copy, titles, link, media URLs.
Downstream (adlib pipeline): `media.py` (download, B2 copy), `transcribe.py` (videos via API),
`analyze_ads.py` (per-ad fields: hook, problem, root cause, mechanism, angle, proof, offer, summary),
`lpscan.py` (landing pages), `site/classify.py` (fixed taxonomy), `site/build_data.py` (site data).

**Budget share estimate**: Meta's impression ORDER is real (checked 29/29 against the live page) but US
numbers are hidden. Weight each ad 1/rank^0.8 and sum by angle → "≈ % of budget". Always label it an
estimate.

**Never**: run Meta keyword searches on generic words (they return 50,000 unrelated ads); run two Meta
scrapers from the VPS at once.

---

## 4. Radar — following one competitor day by day

Built for Resilia (`/root/workspace/radar/`, site `radar.machineroom.app`). Use when the goal is to learn
a competitor's STRATEGY over ~20 days: winners, cut speed, iterations, angles per product, pages,
funnels.

Rules learned:
- **Never base the footprint on pages.** Search by the landing domain (`q=resilia.shop`, cross-checked
  with the brand name), keep every ad whose REAL link (the `l.facebook.com/l.php?u=` href) points to the
  domain. The brand ran ~17–38 pages, most disguised as health-review sites ("Vascular Wellness Report",
  "The Blood Sugar Report"). Exclude resellers (Amazon, other shops) and homonyms.
- **Dedupe by creative** (video hash), not by ad id: Meta runs the same video under many ids ("N ads use
  this creative" = N ads).
- **Product identification** from the ad text + landing path (each product had its own description
  pattern and pre-landers).
- Meta gives lifetimes to the hour ("Total active time N hrs"); big advertisers launch in waves several
  times a day (Resilia ~150–220 new creatives/day) → at least 2 passes/day.
- Current setup: TrendTrack-only (cron 4×/day for new ads, daily cuts and pages), ~250 credits/day,
  caps 400/pass and 9,000/period, ledger `data/<domain>/tt_ledger.json`.
- Winner signals without spend: survival > 7 / 14 days, growing duplicates, number of pages carrying the
  creative, relaunches/iterations.

---

## 5. Signals that an ad (or a brand) is scaling

| Signal | Strength | How to read it |
|---|---|---|
| Top of Meta's impressions order | Strong | Real order; budget share by rank weighting |
| Run time ≥ 60 days (≥ 135–200 days for mature brands) | Strong for statics | Nobody keeps paying for a loser for months |
| Many duplicates / DCO variants / "N ads use this creative" | Strong | The advertiser is pushing it across ad sets/pages |
| Same creative on several pages | Strong | Scaling through page diversification |
| Relaunched / iterated versions (same headline, new visual) | Strong | They believe in that gene |
| A dedicated landing page for the angle | Strong | "One landing per villain" = investment |
| Rising weekly active-ad count (shop level) | Medium–strong | +50 % in 4 weeks = scaling shop |
| Launch cadence (new creatives/day) | Context | 150–220/day = big tester; few = extending winners |
| Cut speed (share of creatives cut < 7 days) | Context | Resilia: 1 in 4 cut creatives die in < 1 week; survivors of 2 weeks often last 1–2 months |
| Traffic trend (TrendTrack/SimilarWeb) | Weak, lagging | Use only to describe a brand's trajectory (e.g. Primal Edge −21 % in 30 days, live ads ÷5 since April) |
| Hook rate / likes | Weak | Soft metrics; can mislead |

Our own winners (account data): ROAS above break-even and ≥ 10–15 % of monthly spend (20–25 % = very
big), confirmed by month-2 rebill. Never judge before 72 h.

---

## 6. Voice-of-customer mining (always, for every new product)

Evolve's order: Reddit → YouTube → TikTok comments → Amazon reviews → post-purchase survey →
AnswerThePublic. Actors that work from the VPS datacenter IP (no residential proxy):

| Platform | Actor | Notes |
|---|---|---|
| Reddit | `fatihtahta~reddit-scraper-search-fast` (API) | The HTML scraper `trudax~reddit-scraper-lite` fails (403) |
| YouTube comments | `apidojo~youtube-comments-scraper` | Competitor videos + niche searches |
| TikTok comments | `clockworks~tiktok-comments-scraper` | Reactions to competitor ads |
| TikTok search/hashtags | `clockworks~tiktok-scraper` / `tiktok-hashtag-scraper` | Find niche videos |
| Amazon reviews | `web_wanderer~amazon-reviews-extractor` (≤ 50/product) | Ours + ALL competitors, 1★–3★ especially |
| Trustpilot | `memo23~trustpilot-scraper-ppe` | Negative reviews = unsolved pains |
| Quora | `fatihtahta~quora-scraper` | Beliefs, awareness |
| Google SERP | `apify~google-search-scraper` | "X reddit", "X horror story" |

Script: `python3 /root/research_scrape.py <slug> [platforms]` reading
`products/<slug>/research-config.json`. Query patterns: desires "I want [outcome] reddit" · emotions
"[problem] makes me feel reddit" · product experience "anyone tried [solution] reddit" (capture the
OUTCOME) · demographics "at what age does [problem] start" · horror "[solution] gone wrong".
Capture in 3 columns: Desire | Customer language (verbatim) | Ad idea. **Report every scraping failure
explicitly** (blocked actor, aborted run, empty dataset); never hide it.

---

## 7. The market research report (Step 1 deliverable — exact structure)

1. **Top 5 angles** — table: # · Angle · The idea (2–3 sentences including the mechanism) · Weight
   (# ads · copies · run time).
2. **5 secondary angles** — one line each (common leads: results timeline, origin/heritage,
   scarcity/authenticity, alternative mechanism, the expert who let the customer down).
3. **Top 5 headlines** — word for word, with source ad and angle.
4. **Headline bank** — by category: Pain & mechanism · Comparison · Product · Story · Urgency.
5. **Video hooks** — word for word.
6. **Avatar** — age, situation, visible problem, what they tried and spent, everyday shame behaviours.
7. **What proves it to them** — everyday proof objects they'd notice themselves.
8. **Winning formats** — static/video split, dominant formats.
9. **Their offer** — price, subscription, guarantee, social proof.
10. **Their weaknesses** — backed by numbers (traffic trend, live ads trend).
11. **Recommendation** — the 3 angles and 10 headlines to attack first.

Process (blueprint 1A → 1B → 1C): (1A) for EACH ad one row: format · exact headline · sub-headline ·
video hook (first 3 s) · angle · mechanism · visual format · proof · offer · CTA; group by angle; rank by
weight — give the per-ad table first, then the synthesis. (1B) TrendTrack cross-check with every number
sourced. (1C) the report above. Get sign-off before step 2.

---

## 8. Competitor study — full method

1. **Scope**: small advertiser → 100 % of ads (active + inactive). Big advertiser → top 150–250 by
   impressions + 100 latest launches. Statics study → newest 30 + top 30 by run time (+ more pages if an
   angle needs it).
2. **Collect** (Apify or TrendTrack), save raw JSON on the VPS, media to B2 (`mr-archive`).
3. **Transcribe** videos with `mr-transcribe` (API). Beat-by-beat analysis only if asked (it's
   expensive); full transcripts are enough for the global analysis.
4. **Per-ad analysis** (Workflow B table in SKILL.md): hook, problem, cause, mechanism, angle, proof,
   offer, landing.
5. **Landing pages**: read every one 100 % (method §9), map ad → LP → PDP.
6. **Classify into BIG angles** with a taxonomy fixed before classifying. The testosterone taxonomy used
   for 1,295 ads: angles = libido · size · belly · man boobs · face/jaw · energy · hair · muscle · 40+ ·
   generation · digestion · GLP-1 · alcohol · comparison · generic T · other; mechanisms = aromatase ·
   cortisol · deficiency · absorption · endocrine disruptors · SHBG · nitric oxide · DHEA/precursors · age
   decline · none · other. Promo ads get the angle underlying the promo.
7. **Weight** angles (rank-weighted share, run time, variants, LPs).
8. **Routing**: which angle goes to which landing page.
9. **Strategy read**: pillar, current push, tests, cadence, cuts, new angles, weaknesses, what to copy.
10. **Deliver** a site per brand (English, big, simple, all images as small thumbnails `_m.jpg` for slow
    networks, "Which landing page for which angle" section).

Example costs: 4-brand Meta library study = Apify $8.63 + OpenAI ≈ $38 (analysis with a GPT model) for
1,295 ads, 67 LPs, 21 PDPs, 238 videos. 4-brand statics study ≈ 330 TrendTrack credits.

---

## 9. Landing page teardown

For each landing page (advertorial, listicle, quiz, PDP, comparison, VSL):
1. **Type** and **headline**.
2. **Flow**, block by block: problem → cause (UMP) → failed solutions → mechanism (UMS) → bridge
   (story/authority) → proof → offer. Quote the key line of each block.
3. **Which ads send traffic here** (count) and which angle they carry → congruence check.
4. **Where it sends next** (PDP URL), and the PDP's prices, compare-at prices, bundles, subscription,
   guarantee, gifts, countdowns.
5. **Persona call-outs** used ("Men 45–65", "for men who've tried everything").
6. **Compliance** posture (site is stricter than ads).
Captures: Playwright mobile 390×844 on the VPS (`nice -n 19 ionice -c3`), forcing US locale with Shopify
cookies (`localization=US`, `cart_currency=USD`) when the VPS IP geolocates elsewhere.

Patterns seen: "one landing per villain" (Primal Viking) · one "10 reasons" listicle cloned per angle
(Mars Men) · advertorial "I tested the 2 top-selling…" for comparison angles (Primal Edge, Elora) ·
persona-specific PDP headlines ("For Men With Man Boobs Who've Tried Everything") · proof ads → proof
page · media co-branded listicles (don't copy).

---

## 10. Quiz teardown

Method (quizmap study): crawl the quiz end to end on a phone-sized screen; click EVERY answer of every
question; screenshot every screen; draw the tree (a straight line if all answers lead to the same next
screen, a branch otherwise); run several full profiles to the result and landing page; then compare word
by word what each answer changes ("dead questions" = no visible effect). Intercept submissions so nothing
is sent to the competitor.

What to record: opening promise · length (questions, loaders, proof screens) · question formats ·
branches · proof inside the quiz · result screen (verdict levels, named root causes, score, projection
chart with a date) · offer screen · landing page and whether it uses the answers · email capture ·
data passed in the URL (persona) · live A/B tests (e.g. "SKIP QUIZ & BUY NOW") · mistakes.

Takeaways that generalise: ~10 one-tap questions; a verdict with 3 levels + a named root cause the
product answers + a dated projection tied to the offer length; cheap "made for me" hooks (dream-body
picture, event + date countdown); nobody passes the quiz; test a skippable email step; actually USE the
persona on the landing page (both competitors collect it and throw it away); every question should
change the result or feed a segment; avoid diagnosis wording.

---

## 11. Product discovery (when the brand is not chosen yet)

- Two strategies: traffic curve ("the curve that explodes", lagging) vs ads-first (Givenche, faster).
  Ask which one to run.
- Scaling-shops run (28 Sep): shops created 15 May–15 Jun with ≥ 10 active ads → 4,302 domains → 1,276
  scaling (≥ +50 % in 4 weeks), 145 new in health; dominant new health angle: lymphatic drainage drops
  (5 brands).
- A watchlist product is never launched without an explicit go. Keep candidates in a list with the
  shop URL and TrendTrack id.

---

## 12. Budgets and etiquette (hard rules)

- Give every research agent a credit budget; keep a TrendTrack floor (≥ 1,000; the radar uses ~250/day;
  the monthly 10,000 recharge was burned in one afternoon once by 8 parallel agents).
- Apify: monthly cap is small — estimate first; reconfirm any amount the founder dictates (voice
  dictation is ambiguous).
- Meta direct: ≤ 60–70 requests/hour total for the VPS, one scraper at a time.
- Transcription via API only; local whisper batches are banned (they saturated the VPS for days).
- Media > 2 MB to B2; JSON/text stays local. Look for archived files with `mr-archive find` before
  re-downloading.
- Reuse finished studies (`competitor-case-studies.md`) before paying for new data.
