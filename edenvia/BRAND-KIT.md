# Edenvia — Brand Kit (DRAFT v0.2, 2026-10-11)

**Status: second pass.** Label, packshot, offer, guarantee, proof, tone and the nine avatar sheets came from the
founder on 2026-10-11. Still open: the price the ads carry, the default A1 avatar, the step-1 competitor, the brand
font file, a few compliance choices. `[MISSING]` = nothing on file, do not invent. `[TO CONFIRM]` = sourced, waiting
for the founder's verdict. Machine-readable twin: `edenvia/brand.json`. Field guide: `.claude/skills/static-ads/BRAND-KIT.md`.

**Golden rule: never invent a fact.** An ad is never generated with an unresolved `[MISSING]` fact (rule B20).

## Sources used

| Tag | Source | Date |
|---|---|---|
| S1 | Founder, in chat (price screenshot, guarantee wording, packshots, site screenshots, proof lines, tone, avatars folder) | 2026-10-11 |
| S2 | Shopify Admin: shop info + product *Molecular Hydrogen* (SKU 51358823) and its landing-page variants | 2026-10-11 |
| S3 | Drive › Edenvia › Branding \| Logo › *Colors* (Google Doc) + logo PNGs | 2026-04-16 |
| S4 | Drive › Molecular Hydrogen › *product_analysis.md* (product page teardown) | 2026-03-07 |
| S5 | Drive › Molecular Hydrogen › *Creative Strategy Report* (avatar "Carol") | 2026-03-07 |
| S6 | Drive › Molecular Hydrogen › *09_competitor_teardown.md* | 2026-03-07 |
| S7 | Drive › *edenvia-disclaimer-rollout.md* (DSHEA compliance rules) | 2026-09-21 |
| S8 | Drive › *EDENVIA — AI PHONE AGENT KNOWLEDGE BASE* v1.3 (medical guardrails, usage) | 2026-07 |
| S9 | Konvert brand record "Edenvia" (scrape of edenvia.com: description, colours, font) | 2026-10-10 |
| S10 | Founder's avatar sheets, 9 ODT files → `edenvia/avatars/*.md` | 2026-10-11 |
| S11 | Site screenshots saved in `edenvia/assets/reference/` (homepage, inflammation landing, offer block) | 2026-10-11 |

Not reachable from this environment: edenvia.com and cdn.shopify.com (network policy). The founder's static-ads
Drive folder ("JC", owned by team@nutraflow.io) returns empty to this connector — a share to valere@nutraflow.io or a
re-upload under the founder's own Drive is needed before I can read the "ads doc".

---

## 1. Brand voice

| Field | Fill in | Source |
|---|---|---|
| Tone in 3 words | `[TO CONFIRM]` direct, confident, root-cause | S11 copy, S1 |
| How aggressive | **very aggressive** — on the pain, the enemy belief and the offer; never on a disease claim | S1 |
| Words we always use | stiff joints / morning stiffness / creaky joints / "woke up wrecked"; "oxidative stress"; "inflammatory response"; "from the inside out"; "at the cellular level"; "root cause"; "one tablet in a glass of water" | S10, S11 |
| Words we never use | treat / cure / prevent / reverse / heal / manage [condition]; any disease name; Dr. / PhD / celebrity; FDA-approved / clinically proven; autoship / subscription; competitor names; capsule / pill / powder; selective antioxidant / hydroxyl radical / ROS / endothelial / redox / NSAID | S7, S8, rules |
| Example lines that sound like the brand | "Help Your Body Fight Daily Inflammation From The Inside Out" · "What if daily support started at the cellular level?" · "Why inflammation drives so many age-related health issues" · "The tiny molecule that helps your body calm the stress behind inflammation" · "What changes when you finally address the root cause" · "You're not waking up wrecked because you trained yesterday…" (A1 sheet) | S11, S10 |
| Sign-off lines allowed | `[TO CONFIRM]` edenvia.com | S1 |

## 2. Product facts (exact, never paraphrased)

| Field | Fill in | Source |
|---|---|---|
| Brand name, exactly as printed | Edenvia (label, mixed case bold italic) · EDENVIA (site header) | packshot, S11 |
| Product name on the label | MOLECULAR HYDROGEN | packshot |
| What it is | 30 effervescent tablets, 30-day supply, 1 tablet a day in a glass of water | packshot, S1 |
| Label claim | GENERATES 8PPM OF HYDROGEN PER TABLET | packshot |
| Ingredients | molecular hydrogen (H2), magnesium blend, citric acid, mineral support complex — `[MISSING]` amounts | S4 |
| What it DOES, in one line | turns a glass of water into hydrogen-rich water that helps support a healthy inflammatory response and the body's defence against oxidative stress | S11 |
| The ritual | drop 1 tablet in room-temperature or chilled water, let it dissolve ~3 minutes, drink within 30 minutes, once daily, never hot water | S4, S8 |
| What the ingredient must LOOK like in an ad | `[TO CONFIRM]` a clear glass, white tablet fizzing at the bottom, fine bubbles rising, water stays clear | proposal |
| What the tablet looks like | round, flat, white, matte, no imprint | packshot 2 |
| What the product is NOT | never a capsule, gel cap, pill, powder, scoop, liquid, hydrogen-water bottle or generator | — |
| Product word the specs use | pouch | — |

## 3. Label text (the packaging must show exactly this)

Transcribed from the founder's packshot (`edenvia/assets/product/edenvia-molecular-hydrogen-pouch-front.png`):

```
Container:  stand-up resealable pouch with zip seal, white at the top fading to sky blue at the bottom,
            fine water droplets all over, matte finish
Line 1:     [atom icon] Edenvia                       (bold italic, dark navy)
Line 2:     MOLECULAR                                 (navy capitals)
Line 3:     HYDROGEN                                  (very large bold navy capitals)
Line 4:     GENERATES 8PPM OF HYDROGEN
Line 5:     PER TABLET
Line 6:     CONSUME DAILY ANTIOXIDANTS AND
Line 7:     EXHIBIT HEALTHIER, IMPROVED LIVING
Band:       DIETARY SUPPLEMENT  (over a thin rule)
Count:      30 TABLETS | 30 DAY SUPPLY
```

→ `product_lock` in brand.json. The AI never draws the label: the real cutout is pasted by script (golden rule 4).

## 4. Offer, price, guarantee (the ONLY numbers allowed in an ad)

Landing page offer block (S1, 2026-10-11), "Available for the First 1,000 Orders Only", scarcity bar "93% Sold":

| Tier | Price | Was | Extras |
|---|---|---|---|
| Buy One (1 pack) | **$39.00** | $79.99 | — |
| Buy 2 Get 1 Free (3 pack) — Most Popular | **$78.00** | $239.97 | + FREE Cellular Recovery Protocol |
| Buy 3 Get 2 Free (5 pack) — Best Value | **$117.00** | $399.95 | + FREE Cellular Recovery Protocol + FREE Shipping (Express) |

- **Price the ads carry: `[TO CONFIRM]`.** Proposal: "$39" with "$79.99" crossed, or the BOGO tier when the template has a deal slot.
- **Site inconsistency to fix:** the homepage product card shows **$79.90**; the landing strike-through shows **$79.99**; Shopify's variant price is $79.99. Ads will use $79.99 unless told otherwise.
- Guarantee (S1, exact): **30-Day Money Back Guarantee** — "We're confident you'll love how this fits into your daily routine. If you're not satisfied for any reason, simply contact us within 30 days for a full refund—no questions asked."
- Also on site: "FREE exclusive guide with every order today", a "Fall Reset Sale" countdown. `[TO CONFIRM]` whether either goes in ads.
- Never in ads: autoship / subscription / "50% off with subscription"; the Shopify post-purchase one-time offers (2 bags $54, 3 bags $81).

## 5. Proof (each with its source)

| Claim, exact wording | Source | Status |
|---|---|---|
| "Rated 4.9/5" | landing star row | **approved by founder** |
| "93% sold" / "93% sold out" | landing scarcity bar | **approved by founder** |
| "12,000+ customers" / "More than 12,000 happy Edenvia customers" | homepage | **approved by founder** |
| "30-Day Money Back Guarantee" | site FAQ | approved |
| "Third-party lab tested" | product page (March) | `[TO CONFIRM]` certificate on file? |
| "Trusted by healthcare professionals" | landing section with a doctor photo | `[TO CONFIRM]` who, with permission? Otherwise never |
| Customer survey stat | — | `[MISSING]`; a stat template cannot be cloned until one exists |
| Real reviews we may quote | site carousel shows first name + initial (Jane D., Ethan L., Jade D.) | `[MISSING]` the reviews export, to quote verbatim (rule B12) |

The site also shows "Rated 4.9/5 by 5,000+ reviews", "Trustscore 4.8/5 · 12,000+ reviews" and "879 Reviews". Only the three approved lines go in ads.

## 6. Avatar (who buys)

Edenvia sells one product to **many avatars, one per angle**. The founder's nine sheets are in `edenvia/avatars/`
(index in `edenvia/avatars/README.md`). Every spec names its angle and takes the avatar from that sheet.

**Default angle A1 — Inflammation & joints.** Two candidate avatars are on file; `[TO CONFIRM]` which one:

| | (a) A1 sheet (S10) | (b) "Carol" (S5) |
|---|---|---|
| Who | active adults, mostly **men 35–60**, still train, wake up sore, stiff, "wrecked" | **woman 56**, formerly active, grandmother, chronic stiff joints |
| Core problem | recovery never finishes: stiff, creaky joints the morning after | morning stiffness, knee/back pain, years of ibuprofen |
| Enemy belief | "being wrecked the next morning is the price of training or age" | "it's just getting older; nothing works for me" |
| Already tried | rest, hydration, sleep, lactic-acid thinking, generic antioxidants | ibuprofen, turmeric, glucosamine, CBD, collagen, prescriptions |
| Trigger | feet hit the floor the morning after a normal workout | first step out of bed is a negotiation |
| Proud proof | same workout, woke up recovered | garden, grandkids, stairs without the rail, ibuprofen untouched |

Other angles, one line each (full sheets in `edenvia/avatars/`): A2 energy/fatigue (50–65, 2 p.m. crash) · A3 heart (men 55–70, winded on stairs) · A4 cholesterol (men 40s–50s, last night's dinner) · A5 blood sugar (men 40+, post-meal crash) · A6 liver (hard belly, borderline markers) · A7 kidneys/detox (foamy urine, swollen ankles) · A8 lymphatic bloating (woman 30s–50s, heavy legs) · A9 weight/metabolism (woman 40+, stubborn belly despite effort).

## 7. The core problem in the customer's own words

A1, from the sheet (`[ads]` = competitor Rovina's ad lines, `[inferred]` = strategist):

```
"Same workout. Two guys. One variable."                                   — [ads]
"One woke up recovered. One woke up wrecked."                              — [ads]
"Everyone blames soreness on lactic acid. That's only half the story."     — [ads]
"Joints feel stiff and creaky every morning."                              — [ads]
"Most people just accept this as normal."                                  — [ads]
"You stay sore and run down."                                              — [ads]
"My body is starting to break down, and this is only going to get worse."  — [inferred]
"Why am I still paying for it today?"                                      — [inferred]
```

Chronic-pain register (S5, Reddit): "Chained to my couch." · "A shadow of my former self." · "It did nothing for me." · "You're gonna destroy your stomach." (daily ibuprofen) · "I'm really in disbelief. There's no way this is placebo."

## 8. Angles and mechanisms

| Field | Fill in |
|---|---|
| Mechanism (plain words) | a workout, or just a day, creates oxidative stress; when the body can't clear it the inflammatory response stays switched on and recovery never finishes. The tablet turns water into hydrogen-rich water; hydrogen is the smallest molecule there is, reaches the cells where the stress sits, and helps the body switch the response back off. Structure/function wording only. |
| Mechanism words never printed | selective antioxidant, hydroxyl radical, reactive oxygen species, endothelial, redox, NSAID, bioavailability, pharmacokinetic |
| Mechanism words the brand itself prints (allowed) | inflammation, inflammatory response, oxidative stress, cellular, 8PPM, antioxidants |
| Angles | A1 inflammation & joints (**default, first test angle**) · A2 energy · A3 heart · A4 cholesterol · A5 blood sugar · A6 liver · A7 kidneys · A8 lymphatic bloating · A9 weight · `[TO CONFIRM]` A10 reflux · A11 stress · A12 longevity (landing pages exist, no sheet) |
| Big Idea per angle | in each sheet, Step 6 (e.g. A1: "You're not waking up wrecked because you trained yesterday, you're waking up wrecked because yesterday's oxidative stress is still keeping your recovery response switched on.") |
| Headlines that already won | `[MISSING]` — in the founder's static-ads Drive folder, not readable yet |
| Angles the product can NOT reach | settled in step 2 |

Note: every sheet's Steps 2–6 are written under a *counterfactual* evidence assumption. They give the story, not the claims. Printed claims stay structure/function.

## 9. Banned words and compliance

Machine-checked list: `brand.json › banned`. Human-readable (S7, S8, rules):

- Structure/function only. Never diagnose / treat / cure / prevent / reverse / heal / manage a condition.
- Never name a disease (arthritis, GERD, hypertension, diabetes, fatty liver, kidney disease, lipedema…). "Stiff joints", "stubborn numbers", "post-meal crash" are fine.
- No invented doctors, titles or celebrities. `[TO CONFIRM]` the site's own "Trusted by healthcare professionals".
- Never say it replaces a medication (painkillers, PPIs, statins, metformin, insulin…).
- No fake testimonials as real; no stat without source + footnote; no body before/after as a real customer.
- Disclaimer (short DSHEA), only where the template has the slot. `[TO CONFIRM]` "*Results may vary" footnote.
- `[TO CONFIRM]` the "men/women over 40" callout ban: the brand's own sheets say "after 40" in body copy.
- Visual checks (C2/D6): tablet never a capsule/pill/powder; glass stays clear; container is a pouch; never hot water.

## 10. Logo rule

| Field | Fill in |
|---|---|
| Icon outside the label | the Edenvia atom icon only (two crossed elliptical orbit rings with two round dots), NO letters |
| Full wordmark | only on the real label, or pasted by script from the official file (D19) |

Files (`edenvia/assets/logo/`): white wordmark no-bg 5818×1080 (jagged edges at full size), blue wordmark no-bg 5818×1080, icon on blue disc 500×500, icon on blue square 1210×1080. `[MISSING]` transparent icon without the disc, and a vector/lossless master — none in the Branding | Logo folder.

## 11. Fonts and colours

Colours (S3, the *Colors* doc wins over Konvert's scrape):

| Name | Hex | Usage |
|---|---|---|
| Brand Blue | #1468DB | primary accent, CTA, logo |
| Royal Blue | #176DE1 | hover |
| Dark Navy Blue | #14488F | badge text, secondary accents |
| Deep Navy | #172A54 | dark backgrounds |
| Darkest Navy | #0A1327 | gradient endpoint |
| Steel Blue | #547AAB | gradient accent, deal bar |
| Ice Blue | #EAF1F9 | light backgrounds, cards |
| Soft Blue | #CCDDF1 | CTA gradient endpoint |
| Pure White | #FFFFFF | backgrounds, text on dark |
| Near Black | #121212 | body text on light |

Font: Manrope `[TO CONFIRM]` (Konvert scrape; the site screenshots match a Manrope-like geometric sans). Font file `[MISSING]`; Anton, Montserrat, Oswald, Fredoka ship with the skill.

## 12. Product photo and cutout

- **Product photo** → `edenvia/assets/product/edenvia-molecular-hydrogen-pouch-front.png` (1206×1658, founder's site packshot, label fully readable). Image 1 of every generation. A higher-resolution master is welcome.
- **Product cutout** → `edenvia/assets/product/edenvia-molecular-hydrogen-pouch-cutout.png` (1140×1506, transparent, made here with a u2net mask, hard edge, checked on white and black). Replace with the studio cutout if one exists.
- Second packshot with three tablets: `…-pouch-with-tablets.png` (686×886), reference for the tablet look.
- The AI render in Drive (hero image) is reference for nothing: garbled label.

## 13. Competitors

Names never printed. **Rovina** (S10: the ads the avatar sheets decode; its top-100 video ads are in the founder's Drive) plus the hydrogen-tablet field from S6: Dr. Mercola H2, Drink HRW, Quicksilver H2 Elite, H2TAB, Vital Reaction / Active H2, Gundry MD Ultimate H2.

**The competitor whose 35 ads we clone in step 1: `[MISSING]`** — the founder announces it after the first angle test.

---

## Open items for the founder (one verdict each)

1. **Price in ads:** "$39, was $79.99"? Or the Buy 2 Get 1 tier? And align the site ($79.90 on the homepage card vs $79.99 everywhere else).
2. **A1 avatar:** (a) active men 35–60 "woke up wrecked", or (b) Carol 56 chronic stiffness? Or both as A1a / A1b?
3. **Compliance choices:** keep "Trusted by healthcare professionals"? Allow "*Results may vary"? Allow "after 40" callouts?
4. **Extras in ads:** FREE Cellular Recovery Protocol, free express shipping, "First 1,000 orders", free guide — which may appear?
5. **Proof extras:** third-party lab certificate; reviews export for verbatim quotes.
6. **Access:** share the static-ads Drive folder ("JC") with valere@nutraflow.io, or re-upload it, so I can read the ads doc and the winning headlines.
7. **Logo master:** vector or lossless PNG, and the icon alone on transparent.
8. **Font file:** Manrope, if that is the brand font.
9. **Step 1 competitor**, when you are ready.
