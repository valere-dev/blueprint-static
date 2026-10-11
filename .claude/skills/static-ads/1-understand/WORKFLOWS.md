# 1-understand — read, decode and choose before anything is made

This folder is the **understanding half** of the static-ads skill (step 2 of the 6 steps in `SKILL.md`). It never generates
images or final copy. It produces decisions and locked inputs: the product's mechanisms, the angle map, the avatar, the ranked
list of winners worth cloning, and one decoded brief per template. The rest of the skill:

| Part | Job | Relationship |
|---|---|---|
| `BRAND-KIT.md` + `brand.json` (skill root) | The brand's facts, voice, offer, avatar, bans | The only source of facts; this folder fills the gaps and locks them |
| **`1-understand/`** (this folder) | Research, decode, choose, lock | Produces the Brand Kit + decoded briefs |
| `2-make/` | Turns a decoded brief + template into a finished static (`2-make/PIPELINE.md`) | Consumes this folder's output |
| `3-improve/` | Review loop, rules, stats (`3-improve/feedback-loop.md`) | Turns every review comment into a rule |
| wildhorn-static-ads (separate skill) | The same skill with the Wildhorn brand already loaded (`wildhorn/` folder) | A filled-in instance of this folder's outputs |
| ad-blueprint-gpt-image-2 (separate skill) | JSON blueprint + GPT Image 2 prompts from a URL | Not needed for template cloning |
| media-buying-bible / ads-decisions (separate skills) | Account structure, kill/scale | Downstream of creative decisions |

Everything you write here is in **English** (sites, briefs, prompts, tables), even when the user speaks French.

---

## 0. The six principles (read these even if you read nothing else)

1. **Clone a winner: same skeleton, new flesh.** We do not invent ads. We take an ad that has proven
   itself (long run time, many duplicates, top spend) and transplant it: same structure, same beats,
   same length, same shot grammar, same visual trick, same awareness level, same amount of text.
   Only the product, the customer and the angle change. Inventing a format from scratch is the
   exception, not the method.
2. **Avatar first, then angle. The mechanism follows the angle.** Pick who (a sub-avatar defined by
   situation, trigger, what they tried — never just demographics), then the outcome they want (the
   angle). The mechanism is not chosen freely: it comes from the product's **mechanism → angles map**.
   If no mechanism of the product credibly reaches the angle, **refuse the angle** instead of inventing
   a link.
3. **Product → Mechanism → Angles.** The mechanism (the hidden cause) is the pivot, not the product.
   One validated mechanism opens N angles (oregano oil: parasites → poor absorption → fat → estrogen →
   man boobs / weak erections / hair loss / focus / belly). One product can have several mechanisms,
   each with its own family of angles. Every ad review outputs: product, mechanism used, angle used,
   other angles on the same mechanism, other mechanisms for the product.
4. **The 4 big levers.** When iterating or remixing a winner, the levers that matter are
   **Hook · Avatar · Angle · Format** (plus the small ones: actor, length, edit, remove a beat).
   The product never changes inside a remix. Micro-details (button colour, badge, music track, logo)
   are not levers — never spend a test on them.
5. **Never invent.** Every angle, headline, number, testimonial and authority must point back to a
   source (a competitor ad, a landing page, a review, the brand's product sheet). Missing fact =
   write `[MISSING]` and flag it. Numbers in a source ad are never copied as facts for our brand.
6. **Research once, then lock.** The research produces a Brand Kit (angles, headline bank, avatar,
   product sheet, product photo, list of creatives already made). After sign-off it is frozen: new
   batches reuse it, they do not re-research.

---

## 1. What this folder decides vs what it never does

**Decides:** which mechanisms the product has · which angles each mechanism opens · which avatar /
sub-avatar each angle targets · which competitor ads are winners · which templates to clone and on
which angle · what in a template must be kept and what must be swapped · which headline from the bank
fits · what compliance risk each line carries · what is missing from the brand file.

**Never does:** generate images · write final prompts for an image model · invent proof · launch ads ·
spend research credits without a budget · move on from research to production without the founder's
sign-off.

---

## 2. Workflow A — a NEW brand, end to end

Run the steps in order. Each step has a deliverable; do not start the next step until the previous
deliverable exists (and, at step 4 and step 8, until the founder signs off).

### Step 1 — Product teardown (½ day)
- Physical product (form, dose, ingredients, packaging, ritual) vs functional product (what it DOES).
  "People buy what it does, not what it is."
- List features → benefits ("why does that matter?") → assumed desires ("why would someone want
  that?").
- Collect the exact commercial facts: price, crossed price, bundles, subscription terms, guarantee
  length and wording, allowed proof numbers, banned claims. These go in the **product sheet** and are
  the only numbers any ad may use.
- Deliverable: `product.md` (see `1-understand/new-brand-worksheet.md` §1).

### Step 2 — Mechanisms (UMP + UMS) and the mechanism → angles map
- For each mechanism: the enemy (UMP, the hidden cause, named in 2–4 plain words), the fix (UMS,
  "A + B = C"), the 3-link causal chain, the belief-bridge fact the avatar already accepts, the
  elimination triad ("not X, not Y, not Z"), and the failed solutions it explains.
- Then list every angle each mechanism can credibly reach. One line per mechanism:
  `Mechanism (enemy → fix) :: angle | angle | angle`.
- Score each mechanism on **Freshness × Belief** (Crafter): fresh + believed = sweet spot.
- Deliverable: mechanism cards + the map. Method and worked examples:
  `1-understand/product-mechanism-angle.md`.

### Step 3 — Research the market (competitors + voice of customer)
- Competitors: find who sells the same product or the same desire; pull their ads (TrendTrack /
  Apify Meta Ad Library), rank them by run time / impressions order / duplicates, read every landing
  page top to bottom, map ad → landing → product page → offer.
- Voice of customer: Reddit, YouTube and TikTok comments, Amazon 1★ and 5★ reviews, Trustpilot,
  ad comments, support tickets, post-purchase surveys. Copy verbatim, never paraphrase.
- Diagnose market sophistication (level 1–5) from the competitors' top 10 scaling ads.
- Deliverable: the market research report (structure in `1-understand/research-playbook.md` §7).
  Tools, signals and budgets: `1-understand/research-playbook.md`. Past studies to reuse:
  `1-understand/competitor-case-studies.md`.

### Step 4 — Angle map + avatar (founder sign-off required)
- Rank angles by observed weight (number of ads, duplicates, run time, landing pages built for it).
  Group near-identical ads into BIG angles (two cortisol ads = one cortisol angle).
- Keep the **top 5 angles** + 5 secondary ones; each angle gets its headline bank (verbatim).
- Build one master avatar, then 3–10 sub-avatars by exclusion (when / why / what tried / what exactly).
  Run the Avatar Check (every box specific, or UNKNOWN).
- Lock each angle with an Angle Sniper card (5 locks: angle, main desire, extra desire, awareness,
  sub-avatar) and an angle card (symptom words, problem scenes, payoff scenes, who notices, timeline,
  objection, guarantee line, visual bans, destination).
- Deliverable: angle map + angle cards + avatar sheet. Method:
  `1-understand/avatar-angle-system.md`. **Stop and get sign-off.**

### Step 5 — Hunt winners to clone (templates)
- Sources: competitor winners (same product), adjacent-category winners (same avatar, other product),
  out-of-niche format winners, the brand's own winners.
- A winner is a creative, not an ad ID: judge by run time, duplicates ("N ads use this creative"),
  number of pages carrying it, relaunches, top position in the impressions order.
- Deliverable: a ranked template list with the evidence for each (days live, copies, source).

### Step 6 — Decode every template
- For each template: DNA (genes), the scroll-stop trick in one sentence, scene logic, the visual trick,
  the production method, the copy formula, shock / innuendo level, the angle it naturally carries, and
  the full KEEP / SWAP inventory. Method + every evidence case: `1-understand/template-reading.md`.
- Score the ad with Ad DNA if useful (`1-understand/ad-dna.md`), and the copy with
  `1-understand/copy-analysis.md`.

### Step 7 — Choose what to clone and on which angle
- Sort templates into concept families (us vs them, before/after, problem reframe, mechanism /
  ingredients, origin, offer, bold claim + product, meme / humour / UGC, off-avatar re-skin).
- Accept every template the founder picked. Never skip one because it "doesn't look like our angles":
  find the angle it naturally carries; if none, rewrite until one of the top angles fits.
- Assign one angle per template (the angle the template carries, not a forced spread), while making
  sure each family covers the top angles across its templates.
- Rank angles per template by **change distance** (witness, time of day, setting, body zone, belief
  cost): the cheapest transplant is the closest angle.
- Deliverable: the clone plan table (template · family · angle · headline source · change distance).

### Step 8 — Hand-off brief for the generator (founder sign-off on the first family)
- One decoded brief per template (format in `1-understand/new-brand-worksheet.md` §9): template id,
  family, angle, sub-avatar, the decode, the KEEP/SWAP inventory, exact text slots (same count as the
  template), headline source line, proof allowed, visual bans, production-method note, missing fields.
- Send the first concept family first; the rest only after the founder validates it.
- Save the Brand Kit (research report, angle cards, product sheet, product photo path, creatives log).

---

## 3. Workflow B — analyze ONE ad (video or static) in 10 minutes

Output a single table, in this order. No summary before the table.

| Field | What to write |
|---|---|
| Source | brand, ad id / link, format, run time in days, copies/variants, landing URL |
| Product | what is sold, form, offer shown |
| Hook | first 3 s or the headline, word for word (on-screen text AND voice if video) |
| Problem | the symptom shown, in the customer's words |
| Mechanism | enemy (UMP) → fix (UMS) as the ad says it |
| Angle | the outcome the viewer should remember (outcome, not problem) |
| Avatar | who it calls out: trigger, cause, what they tried |
| Awareness × sophistication | AW level where the ad starts; the sophistication response it uses |
| Proof | type and exact items (counts, timeline, reviews, authority, guarantee) |
| Offer + CTA | price, bundle, guarantee, booster |
| DNA code | `AV·AN·ME·ST·AW | HK·MS·FO·PR·SC·TO` (see `1-understand/ad-dna.md`) |
| Why it wins | the scroll-stop trick in ONE sentence |
| Compliance flags | each risky line + the safer rewrite |
| Spin-offs | 3 other angles on the same mechanism + 1–2 other mechanisms for the product |

Then, only if asked, the long-form breakdown (beat map with timecodes for video; zone map for statics).

---

## 4. Workflow C — decode a static template before cloning (the 13-question pass)

Answer every question in writing before any brief exists. Each one prevents a mistake that has
already cost a full regeneration round.

1. **Scroll-stop trick**: why does this stop the thumb, in one sentence?
2. **Template DNA**: list every element that exists only because of what THEY sell (material, texture,
   flavour, symbol, body part, logo, offer, copy formula, innuendo object). Each one gets our equivalent.
3. **Scene logic**: why is the scene where it is? (shower = hair in the drain; kid's bedroom = kids'
   sleep product). If the reason doesn't apply to us, move to where OUR problem is directly visible —
   never to an indirect consequence.
4. **Hidden reading**: innuendo, double meaning, joke, social mechanism. Ours must carry the same
   meaning at the same intensity.
5. **Angle carried**: which of our research angles does it naturally carry? Same angle → keep their
   words and their visual mechanism.
6. **Read as our customer**: does the line already work for our buyer as is? If yes, copy it word for
   word. Flipping a line that already works is a fail.
7. **Shape / function equivalents**: can an object of the same shape or function carry our problem
   (round moon ↔ round beer belly)? Look for these first.
8. **The verb of the scene**: what ACTION happens (pour, hold, measure, hide)? Copy the action, not
   only the objects.
9. **Shock level**: match it. Gross stays gross, cheeky stays cheeky, calm stays calm.
10. **Visual trick**: copy it literally (the face IS the product → our jar IS the face, same render).
11. **Structure type**: before/after stays before/after (one problem state vs one solved state);
    progressions read left → right toward the result.
12. **Production method**: how was it made (real photo + pasted product, illustration, 3D render,
    screenshot, painted text)? The clone must use the same method.
13. **Text inventory**: count every text slot. Ours has the same count, same hierarchy, same treatment
    (handwriting, bubbles, clay letters stay so). Add nothing.

Then write the KEEP / SWAP inventory, pixel zone by pixel zone. Full method, evidence cases and the
inventory template: `1-understand/template-reading.md`.

---

## 5. Workflow D — study a competitor (the method that produced every study so far)

1. **Identify the real advertiser footprint**: never trust page names. Search by the landing domain
   (Meta Ad Library keyword = domain; TrendTrack domain search), keep every ad whose real link
   points to the domain, whatever the page. Brands run through many disguised pages
   (advertorial/"review" pages). Exclude resellers and homonyms.
2. **Pull a bounded set**: all ads for small advertisers; for big ones, top 150–250 by the Meta
   impressions order + the 100 most recent launches. Statics-only studies: last 30 + top 30 by run time.
3. **Rank winners** without spend data: impressions order (Meta), run time (`minDaysRunning`),
   number of duplicates / variants, number of pages carrying the creative, relaunches.
4. **Analyze every ad** with the Workflow B table (videos transcribed with `mr-transcribe`, never
   local whisper).
5. **Read every landing page 100 %, top to bottom**: flow problem → cause → failed solutions →
   mechanism → bridge → proof → offer. Note which product page it sends to, prices, bundles,
   subscription, guarantee.
6. **Group into BIG angles** with a fixed taxonomy (decide it before classifying). Estimate budget share
   honestly (it is an estimate: rank-weighted, e.g. weight = 1/rank^0.8 on the impressions order).
7. **Map routing**: which angle goes to which landing page ("one landing per villain").
8. **Write the strategy read**: pillar product, angle being pushed now, what is in test, launch cadence,
   cut speed, new angles this month, weaknesses (traffic trend, live-ad trend).
9. **Deliver a site** (`<name>.machineroom.app`, English, big and simple, thumbnails for slow networks).

Full playbook with tool calls, credit budgets and gotchas: `1-understand/research-playbook.md`.

---

## 6. Core vocabulary (one meaning per word)

| Word | Meaning here | Not to be confused with |
|---|---|---|
| Desire | One of the core/primary desires the product can honestly serve (Evolve 6 core, Crafter 13 primary) | The product benefit |
| Sub-avatar | A precise person in a precise situation: trigger + cause + what they tried + emotion; demographics only as a filter | "Men 45-55" (that is a demographic, not an avatar) |
| Angle | The reason to buy, customer-centred, phrased as the OUTCOME ("energy back by 10 a.m.") | The format ("us vs them" is a format; us vs them OF WHAT is the angle) |
| Mechanism | UMP = hidden cause of the problem; UMS = why this product fixes it ("A + B = C") | An ingredient list |
| Concept (Evolve) | The idea being tested, centred on us ("test us-vs-them") | Concept in Ad DNA = strategy genes |
| Variation | Another way to say the same angle | A new angle |
| Iteration | A change of one gene/lever on a winner | A remake of the whole winner |
| Format | How the ad is packaged (talking head, static comparison, iPhone note…) | Product delivery format (gummy vs capsule) |
| Template | A proven ad we decode and clone | Inspiration we "riff on" |
| Skeleton | Beat order, beat jobs, timing, hook type, shot grammar, visual trick, text count, awareness | The words |
| Flesh / slots | Product name, hero ingredient, enemy name, proof, scenes, angle line, offer, CTA destination | The structure |
| Winner | ROAS above break-even AND a real share of spend (≥10–15 % of monthly spend), confirmed by month-2 rebill | A high hook rate |

---

## 7. Checklists

### 7.1 Before calling an angle "validated"
- [ ] It is phrased as an outcome in the customer's words, ≤ 8 words.
- [ ] A mechanism from the map reaches it credibly (chain of ≤ 5 plain links).
- [ ] At least one competitor runs it with a long-running or duplicated ad, OR the voice of customer
      repeats it many times (10+ mentions, high-upvote threads) — not a single comment.
- [ ] The product can honour it (Evolve: error #1 is targeting a desire the product can't deliver).
- [ ] It names a sub-avatar narrower than "people with X" and passes the "niche but shared" gate.
- [ ] It has a headline bank (≥ 5 verbatim lines from sources) and ≥ 4 problem scenes and payoff scenes.
- [ ] A non-customer would not feel concerned by its hook.

### 7.2 Before handing a template to the generator
- [ ] Scroll-stop trick written in one sentence.
- [ ] Template DNA list done: nothing from their product world survives.
- [ ] Scene logic checked; scene moved only to where our problem is directly visible.
- [ ] Hidden reading decoded; ours keeps the same meaning and intensity.
- [ ] Angle chosen = the one the template carries; headline from the bank (or their words if same angle).
- [ ] Same number of text slots; no added tagline, context line, deadline or disclaimer.
- [ ] Production method identified (and named in the brief).
- [ ] KEEP/SWAP inventory complete, every zone has a reason.
- [ ] Every person shown as the customer matches the avatar's age and look.
- [ ] Compliance flags listed per line.

### 7.3 Before delivering a competitor study
- [ ] Footprint by domain, not by page; resellers excluded.
- [ ] Ranking method stated (impressions order / run time / duplicates) and "budget share = estimate".
- [ ] Every landing page read fully; ad → LP → PDP → offer mapped.
- [ ] BIG angles only; taxonomy fixed; every ad classified.
- [ ] Strategy read + weaknesses + what to copy first.
- [ ] Credits spent logged; no keyword search on Meta that returns thousands of unrelated ads.

---

## 8. Output formats (house style)

- **Tables first, synthesis second.** For any multi-ad analysis, give the per-ad table before grouping
  ("don't summarize too early").
- **Verbatim in quotes, sourced.** Every headline or hook quoted word for word with its source (brand,
  ad id or LP URL, days live).
- **Estimates labelled.** Any % of budget, reach or spend that is inferred is written "≈" and the method
  is named.
- **One sentence per box** in avatar/angle cards. `UNKNOWN` beats a guess.
- **Simple words.** Reading level of an 11–14-year-old; no jargon the avatar doesn't use.
- **Batch requests end with a checklist** `request → status (✅ done+verified / 🔨 in progress / ⏳
  blocked + reason)`.
- **Deliverables people browse** (studies, maps) go on a site `<name>.machineroom.app` (English,
  noindex, clean URLs, thumbnails), not in chat.

---

## 9. Decision rules that came from real reviews (non-negotiable)

- Name who it's for by their **problem**, not their age ("For stubborn beer belly", not "For men over 40").
- **Same amount of text** as the template. Nothing added, not even a small tie-in line.
- Benefits = the result he wants vs what he already tried. Never product features. No mechanism jargon
  ("conversion", "aromatase") in ad text.
- **Concede the pleasure, attack its consequence** ("Beer is fun. Beer belly isn't.").
- **Aggression = precision** on the deepest pain (the bedroom lights), not volume.
- The **proof object** is something the avatar is proud to see (his old jeans fit), not a technical
  detail (one belt notch).
- **Stranger test**: a man who never heard of the brand must understand what it is and what it does
  on first read.
- **Simplest words win**; if a plainer phrase exists, use it.
- Stats are **benefit claims phrased like the template's stat**, with the survey footnote.
- Never mention subscription / autoship mechanics in ads; use the offer framing the template uses.
- When the founder validates a version, it is **frozen**; a redo changes only what he named. His latest
  verdict wins.
- "Another version" = change the idea, not the wording. "Change only the wording" = keep everything
  else pixel for pixel.

---

## 10. Common failure modes (and the rule that fixes each)

| Failure | Rule |
|---|---|
| Template skipped because "not our angle" | Accept every template; find the angle it carries |
| Their body part / material / symbol kept (arm, brisket, chocolate, hair ribbon) | Template DNA swap |
| Scene copied without reason (shower, kids' beds) | Scene logic |
| Moved to an indirect consequence (shoelaces) | Only where the problem is directly visible |
| Sexual template sanitized into nothing | Keep the innuendo, re-derive it for our product |
| Objects copied, action lost (capsules beside the beer) | Copy the verb (pour into the beer) |
| A tame version of a shocking template | Match the shock level |
| Line flipped that already worked for our buyer | Read the line as our customer |
| Before/after turned into two good states | Before/after stays before/after |
| Context line, deadline or disclaimer added | Same amount of text |
| Re-generating a scene that was a simple composite | Work out the production method first |
| Angle invented to fit a template | Only research angles; mechanism must reach it |
| Demographic avatar ("men 45-55") | Situation-based sub-avatar |
| Two desires / two promises in one ad | One ad, one idea |
| Iterating on button colour or badge | Not a lever |

---

## 11. Budget and tool etiquette

- TrendTrack credits are shared with scheduled jobs (radar ~250/day): give every agent a credit budget
  and keep a floor (≥ 1,000). `lookup` calls are free; ad rows cost 1 credit each via REST.
- Apify has a monthly cap (currently low): estimate the cost before a run; the Meta Ad Library actor
  `apify~facebook-ads-scraper` handled 200 ads in under a minute.
- Never run two Meta Ad Library scrapers from the VPS at once (soft IP block). Keep ≤ 60–70 Meta
  requests/hour.
- Transcription = `mr-transcribe` (OpenAI API). Never batch local whisper.
- Heavy media (videos, image dumps) go to B2 with `mr-archive`; only JSON and text stay on the VPS.
- Never run Playwright/Chromium on the Mac; landing captures run on the VPS (`nice -n 19`).

---

## 12. Map of references

| File | Read it when |
|---|---|
| `1-understand/product-mechanism-angle.md` | Building mechanisms, UMP/UMS, the mechanism → angles map; reviewing an ad's mechanism; spinning N angles from one mechanism |
| `1-understand/avatar-angle-system.md` | Building the master avatar, sub-avatars, Avatar Check, Bridge, Angle Sniper, Angle Expansion Map, angle cards; validating an angle |
| `1-understand/ad-dna.md` | Scoring/naming an ad gene by gene, counting concepts vs variations vs iterations, planning crosses, test order |
| `1-understand/frameworks-evolve-crafter.md` | Any question of desire, sophistication, awareness, angle vs concept, testing (Marksman/Sniper), iteration levers, winner definition, how Evolve and Crafter combine |
| `1-understand/template-reading.md` | Decoding any static template before cloning; KEEP/SWAP inventory; evidence cases from 9 review rounds |
| `1-understand/copy-analysis.md` | Judging headlines and hooks, stat phrasing, copy formulas, compliance traps, choosing an AI model for copy |
| `1-understand/research-playbook.md` | Finding winners (TrendTrack, Meta Ad Library, Apify, radar, scaling shops), signals that an ad scales, competitor/quiz/landing teardown method, credit budgets |
| `1-understand/competitor-case-studies.md` | Reusing what we already know about Primal Edge, Elora, Primal Viking, Mars Men, Ancestral, Primal Storm, Resilia, quiz funnels, scaling shops |
| `1-understand/new-brand-worksheet.md` | Running the whole analysis for brand X and producing the hand-off pack for `2-make/` |

### Source material on the VPS (read-only)
- Ad DNA site: `/srv/adn/` (index = 20 genes, simple = Evolve × Crafter, brief = clone a winner,
  machine/system = copy machine spec, builder = spec JSON, script = pipeline).
- Evolve course synthesis: `/srv/mrr/evolve.html`.
- Crafter Club extractions: `/root/workspace/adn-crafter/{strategy,creative,execution,missing-lessons}.md`;
  transcripts `/root/workspace/crafter/txt_api/`.
- Copy doctrine: `/root/claude-vault/knowledge/copywriting/COPY-CONSTITUTION.md`, `TRANSPLANT-STUDY.md`,
  annotated winners `swipe-annotated/` (197 ads).
- Avatar/angle doc system: `/root/claude-vault/knowledge/product-research/` (SOP, templates, prompts).
- Template-clone lessons: `/root/workspace/wh-remix/LESSONS.md`; protocols `/srv/blueprint/protocols.html`;
  blueprint `/srv/blueprint/index.html`, worked example `/srv/blueprint/example.html`.
- Competitor data: `/root/workspace/competitors/` (adlib, angles-site, *-statics, quiz-map, offers);
  sites intel / angles / quizmap / radar / scaling / testo-map under `/srv/`.
- AI copy model study: `/root/workspace/copy-ai-study/` (workflows.md, quotes.md, stats.json).
