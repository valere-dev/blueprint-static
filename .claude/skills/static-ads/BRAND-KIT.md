# Brand Kit — the only thing you bring

Everything the skill knows about a brand comes from two files at the root of this skill:

- **`BRAND-KIT.md`** (this file) — the brand in plain English. Fill it once per brand, in a copy saved with the brand's
  work (for example `/root/workspace/<brand>-kit/BRAND-KIT.md`). Humans and Claude read it.
- **`brand.json`** — the same facts in the shape the scripts read (product photo, price list, banned words, checks). Copy it to the
  brand's working folder and fill it from this kit. Scripts read it; nothing is hard-coded.

**Golden rule: never invent a fact.** If you don't know a field, write `[MISSING]` and ask the founder. An ad is never generated
with an unresolved `[MISSING]` fact (rule B20). A filled example for a real brand: the wildhorn-static-ads skill
(`/root/claude-vault/skills/wildhorn-static-ads/wildhorn/brand.md` and `/root/claude-vault/skills/wildhorn-static-ads/brand.json`).

Each field says **which step uses it** (the 6 steps are in `SKILL.md`: 1 Brand kit · 2 Understand · 3 Make · 4 Review · 5 Improve · 6 Measure).
Fields marked → `brand.json key` must also be copied into `brand.json`.

---

## 1. Brand voice

| Field | Fill in | Used in |
|---|---|---|
| Tone in 3 words | e.g. blunt, warm, a bit cheeky | Step 3 — every headline and body line |
| How aggressive the founder wants the ads | soft / direct / shock | Step 2 (angle choice, rule A33) · Step 3 |
| Words we always use | e.g. "beer belly" (never just "belly") | Step 3 copy · lint → `angle_keyword` |
| Words we never use | e.g. jargon, the competitor's words, "men over 40" | Step 3 copy · lint → `banned` |
| 3–5 example lines that sound like the brand | copy them from ads the founder validated or from the site | Step 3 — tone reference |
| Sign-off lines allowed | site URL, tagline | Step 3 — template's sign-off slot |

## 2. Product facts (exact, never paraphrased)

| Field | Fill in | Used in |
|---|---|---|
| Brand name, exactly as printed | | Step 3 → `name`, `wordmark`, `file_prefix` |
| Product name on the label | | Step 3 — prompt lock |
| What it is (form · count · dose · ingredients with amounts) | e.g. 30 capsules, 2 a day, 4 organs | Step 2 mechanism · Step 3 → `product.what` |
| What it DOES, in one line | | Step 2 — mechanism and angles |
| The ritual (when / how it's taken) | | Step 3 — scenes that show the product in use |
| What the ingredient must LOOK like in an ad | e.g. fresh, clean, appetizing, recognizable shapes | Step 3 → `product.ingredient_visual` · lint → `visual_checks` |
| What the capsule / pill / powder looks like | | Step 3 → `product.capsule_visual` |
| What the product is NOT (form it must never take) | e.g. never powder, never a scoop | Step 3 → `visual_checks` |
| Product word the specs use | jar / pouch / bottle / box | Step 3 → `product_noun` (lint counts it) |

## 3. Label text (the packaging must show exactly this)

Write every line of the label in reading order, exactly as printed, plus the container (material, colour, lid).

```
Container:  e.g. amber glass jar, matte black lid, cream label
Line 1:     [logo] BRAND
Line 2:     PRODUCT NAME
Line 3:     ...
Band:       ...
Count:      30 CAPSULES
```
Used in: Step 3 → `product_lock` (one sentence naming every visible element in reading order — pasted into every prompt).
The AI never draws the label or the text alone: the real cutout and the exact text are pasted by script (golden rule 4).

## 4. Offer, price, guarantee (the ONLY numbers allowed in an ad)

| Field | Fill in | Used in |
|---|---|---|
| Price in ads | e.g. $49.95 | Step 3 → `offer.price`, `prices_allowed` (lint blocks any other $ amount) |
| Crossed-out price | e.g. $100 | Step 3 → `offer.compare_at`, `prices_allowed` |
| Deal wording allowed | e.g. "Buy 1 Get 1 Free" | Step 3 → `offer.deal` |
| Guarantee (length · wording · conditions) | e.g. 60-day money-back guarantee (first order) | Step 3 → `offer.guarantee` |
| Site offers that must NEVER appear in ads | e.g. autoship, subscription, "subscribe & save" | Step 3 → `banned` |
| Bundles, gifts, free shipping | only if real | Step 3 — never invent the template's gifts or bonuses |

Reconfirm the price with the founder before the first batch (Wildhorn's was locked only after asking).

## 5. Proof (each with its source)

| Claim, exact wording | Footnote / source | Allowed where |
|---|---|---|
| e.g. "50,000+ men" | order count, date checked | any proof slot |
| e.g. "93% saw their beer belly shrink*" | "*Based on a 12-week customer survey" — always with the * | stat slots only |
| Star rating | | review / badge slots |
| Real reviews we may quote | path to the file | review templates (first name + initial only if the template signs its reviews, rule B12) |
| Real authorities (founder, expert, institution) | | never invent a doctor or a celebrity |

Used in: Step 3 → `proof` (and the copy). Step 2 — which templates we can clone (a stat template needs a real stat).

## 6. Avatar (who buys)

| Field | Fill in | Used in |
|---|---|---|
| Age range and look of every person shown as the customer | e.g. 45–60, short greying hair, grey stubble | Step 3 → `avatar.who` · rule A11 (never a young model) |
| Situation | e.g. married, blue-collar | Step 2 · Step 3 scenes |
| The visible problem (core problem) | e.g. beer belly | Step 2 · Step 3 → `avatar.core_problem` (golden rule 5) |
| Secondary problems | | Step 2 — secondary angles → `avatar.secondary_problems` |
| How he/she hides it | e.g. sucks the belly in for photos, baggy shirts | Step 3 → `avatar.hides_it_by` (rule B8) |
| What they already tried | e.g. fat burners, gym, keto | Step 3 → `avatar.already_tried` (rule B5) |
| The pleasure they won't give up | e.g. beer | Step 3 → `avatar.pleasure_he_keeps` (rule B11) |
| The proof they want to SEE | e.g. old jeans fit again, shirt tucked in | Step 3 → `avatar.proud_proof` (rule B9) |
| Deepest pains | e.g. lights off in the bedroom, the pool, photos | Step 2 — aggressive angles (rule B10) |
| Desires | what changes in their life when it works | Step 2 — angle cards |

## 7. The core problem in the customer's own words

Write 5–10 sentences the customer actually says (reviews, comments, Reddit, call notes), in quotes, with the source.
The simplest words win: these become headlines.

```
"..."   — source
"..."   — source
```
Used in: Step 2 (angles, bridge sentence) · Step 3 (headlines). Rule B2: every line names the core problem in plain words.

## 8. Angles and mechanisms

| Field | Fill in | Used in |
|---|---|---|
| Mechanism (the hidden cause, in plain words) | e.g. after 40 the body turns testosterone into estrogen, which stores fat on the belly | Step 2 · Step 3 → `mechanism` |
| Mechanism words never printed in an ad | e.g. "conversion", "aromatase" | Step 3 → `banned` (rule B4) |
| Top angles (3–5), one marked default | e.g. A1 beer belly = estrogen (default) · A2 man boobs · A3 wild vs farmed | Step 2 · Step 3 → `angles` (one `default: true`, rule A14) |
| Headlines that already won | | Step 3 — reuse, never rewrite a winner |
| Angles the product can NOT reach | | Step 2 — refuse them (`1-understand/product-mechanism-angle.md`) |

Not sure yet? Run step 2 first: `1-understand/new-brand-worksheet.md` builds the mechanism map, avatar and angle map
with two founder sign-offs, then come back and fill this section.

## 9. Banned words and compliance

| Field | Fill in | Used in |
|---|---|---|
| Banned words (regex + reason) | e.g. `\bdoctor` → no doctors | Step 3 lint → `banned` |
| Competitor names never printed | | Step 3 lint → `competitors` |
| Compliance bans (human-readable) | e.g. no fake testimonials presented as real, no numeric hormone claim, no doctors or celebrities, no body before/after presented as a real customer | Step 3 QC → `compliance` |
| Disclaimers allowed (only where the template has the slot) | e.g. "*Results may vary" | Step 3 copy |
| Visual checks (regex on the image description) | e.g. ingredient never raw or bloody | Step 3 lint → `visual_checks` |
| The vague word vs the full phrase on the default angle | e.g. "belly" alone → must say "beer belly" | Step 3 lint → `angle_keyword` |

## 10. Logo rule

| Field | Fill in | Used in |
|---|---|---|
| The icon to use outside the label | e.g. "the horn icon only (two curved horns), NO letters" | Step 3 → `icon_description`, `lock_extra` (rule D8) |
| Where the full wordmark is allowed | only on the real label, or rendered by script | Step 3 — AI misspells brand names (golden rule 9) |

## 11. Fonts and colours

| Field | Fill in | Used in |
|---|---|---|
| Brand accent colour(s) (hex) | | Step 3 → `colors` (highlight boxes, review pages) |
| Brand fonts (files) | Anton, Montserrat, Oswald, Fredoka already ship in `scripts/fonts/` | Step 3 → `fonts_dir`, `fonts` (used by `scripts/composite.py`) |

## 12. Product photo and cutout (the two most important files)

- **Product photo** → `product_photo` — Image 1 of every generation. The real packshot, front label readable, neutral background,
  high resolution. The model copies what it sees: a blurry label = a garbled label in every ad.
- **Product cutout** → `product_cutout` — pasted by `scripts/composite.py`. Transparent background (PNG/WebP with alpha), tight crop,
  upright, front label, at least 800 px tall. Make it from the photo with a background-removal pass; check the edges at full resolution
  (a halo looks fake). Render one composite on white and one on black to check.
- Several products? One cutout each; `composite` product blocks take `"src"`.
- Put both under `$SAC_WORKDIR` (or reference the brand's existing asset paths read-only).

Used in: Step 3 (every generation and every composite).

## 13. Competitors

| Name | What they sell | Why they matter (same buyer? template source?) | Their angles |
|---|---|---|---|
| | | | |

Used in: Step 2 (research, `1-understand/competitor-case-studies.md`) · Step 3 → `competitors` (never printed).
When a template comes from a brand that sells to the same buyer, its angle usually IS ours: copy it (rule A6).

---

## brand.json — key by key

`brand.json` at the root of this skill is the blank template (every value is `[MISSING]`). Keys starting with `_` are notes.

| Key | What | Example (Wildhorn) |
|---|---|---|
| `name`, `wordmark`, `file_prefix` | brand name as printed, file prefix | WILDHORN / Wildhorn |
| `icon_description` | the standalone mark to use instead of letters (D8) | "the horn icon only (two curved horns), NO letters" |
| `product_noun` | what specs call the product (lint D6 counts it) | jar |
| `product_photo`, `product_cutout` | the two files of section 12 | `/root/workspace/wh-remix/product-jar.jpg`, `/srv/wildhorn-lp/p6/jar-30.webp` |
| `product_lock` | one sentence naming every visible packaging element in reading order (section 3) | "the WILDHORN Wild American Bison capsule jar. Reproduce it exactly…: amber glass jar, matte black lid, cream label…" |
| `lock_extra` | sentence appended to every prompt's constraints | the D8 icon-only sentence |
| `fonts_dir`, `fonts` | fonts for composite.py + brand fonts | — |
| `colors` | brand colours | accent #E0662C |
| `product.*` | what it is, the ingredient visual, the capsule visual (C2 wording) | organs fresh/appetizing; transparent capsules with mini organs |
| `offer`, `prices_allowed` | exact price, compare-at, deal, guarantee — the ONLY numbers allowed (B20) | $49.95 / $100 / Buy 1 Get 1 Free / 60-day |
| `proof` | allowed proof claims with their footnotes (B16) | 50,000+ men; 93% saw their beer belly shrink* (12-week survey) |
| `avatar.*` | who (A11), core problem, hiding behaviours (B8), already tried (B5), pleasure kept (B11), proud proof (B9) | 45–60 greying; beer belly; baggy shirts…; fat burners…; beer; old jeans fit |
| `mechanism` | the villain in plain words + the jargon never to print (B4, A28) | estrogen after 40 |
| `angles` | top angles; one `default: true` (A14) | A1 beer belly = estrogen … A5 anti-waste |
| `competitors` | names never printed | Primal, Viking, Mars Men |
| `banned` | `{regex: reason}` — jargon, avatar misreads, compliance bans | aromatase, compression shirt, +60% T, doctor/celebrity |
| `compliance` | human-readable bans for QC | no fake testimonials… |
| `angle_keyword` | B2 lint: vague word vs required full phrase on the default angle | `\bbelly\b` → "beer belly\|belly fat\|…" on angle A1 |
| `visual_checks` | C2-style regex checks on the `visual` field | generic capsule, raw/bloody, veins, freeze-dried/brown organs |

Where the scripts find it (`scripts/sac_config.py`): `$BRAND_JSON` if set → `$SAC_WORKDIR/brand.json` → the `brand.json` at the root
of this skill. Copy it into the brand's working folder and fill it there; the skill's own copy stays the blank template.
Check it loads: `python3 -c "import json;json.load(open('brand.json'))"`, then `python3 $SKILL/scripts/lint.py <any spec file>`
(a JSON error shows there first).

---

## What is Wildhorn-only (do NOT carry over blindly)

- The beer-belly default, the estrogen villain, the organ visuals (C2's wording), the horn icon, the 45–60 greying avatar, the $49.95/BOGO offer,
  the competitor list — all come from brand.json/specs and must be replaced.
- The rules themselves stay; their Wildhorn evidence explains WHY. When a rule's wording names a Wildhorn thing, apply its principle to the new brand's equivalent.
- The brand's own rule additions go into the brand's `LESSONS.md` (or a brand section) AND, if they are general, into `3-improve/rules.md` with a new ID.

Next: `2-make/first-batch.md` (working folder, templates, the first 10 ads, pre-flight checklist).
