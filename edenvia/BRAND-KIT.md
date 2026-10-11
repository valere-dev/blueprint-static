# Edenvia — Brand Kit (DRAFT v0.1, 2026-10-11)

**Status: first pass, NOT validated.** Filled only from sourced material; every value names its source.
`[MISSING]` = nothing on file, do not invent. `[TO CONFIRM]` = sourced, waiting for the founder's verdict.
The machine-readable twin is `edenvia/brand.json` (same facts, read by the scripts). The blank template and the
field-by-field guide are in `.claude/skills/static-ads/BRAND-KIT.md`.

**Golden rule: never invent a fact.** An ad is never generated with an unresolved `[MISSING]` fact (rule B20).

## Sources used

| Tag | Source | Date |
|---|---|---|
| S1 | Founder brief (chat, this repo) | 2026-10-11 |
| S2 | Shopify Admin: shop info + product *Molecular Hydrogen* (SKU 51358823) and its landing-page variants | 2026-10-11 |
| S3 | Drive › Edenvia › Branding \| Logo › *Colors* (Google Doc) + logo PNGs | 2026-04-16 |
| S4 | Drive › Edenvia › Molecular Hydrogen › *product_analysis.md* (product page teardown) | 2026-03-07 |
| S5 | Drive › Edenvia › Molecular Hydrogen › *Creative Strategy Report: Molecular Hydrogen* (avatar "Carol") | 2026-03-07 |
| S6 | Drive › Edenvia › Molecular Hydrogen › *09_competitor_teardown.md* | 2026-03-07 |
| S7 | Drive › *edenvia-disclaimer-rollout.md* (DSHEA compliance rules) | 2026-09-21 |
| S8 | Drive › *EDENVIA — AI PHONE AGENT KNOWLEDGE BASE* v1.3 (medical guardrails, usage) | 2026-07 |
| S9 | Konvert brand record "Edenvia" (scrape of edenvia.com: description, colours, font) | 2026-10-10 |
| S10 | Drive › Branding \| Logo › Website › *Edenvia - Hero Image - 11.png* (AI render of the pouch, label partly legible) | 2026-03-08 |

Not reachable from this environment: edenvia.com itself and cdn.shopify.com (network policy). The live product
page copy, the real packshot and the label text therefore come from S4/S10 and must be re-confirmed by the founder.

---

## 1. Brand voice

| Field | Fill in | Source |
|---|---|---|
| Tone in 3 words | `[TO CONFIRM]` warm, plain, reassuring (site copy per S9: "clean, effective formulas… simplify health routines") | S9 |
| How aggressive the founder wants the ads | `[MISSING]` soft / direct / shock | — |
| Words we always use | `[TO CONFIRM]` "stiff joints", "morning stiffness", "one tablet in a glass of water", "supports" | S4, S5 |
| Words we never use | treat / cure / prevent / reverse / heal / manage [condition]; any disease name; doctor / PhD / celebrity; FDA-approved / clinically proven; autoship / subscription; competitor names; capsule / pill / powder; PPM / selective antioxidant / hydroxyl radical / NSAID | S7, S8 |
| 3–5 example lines that sound like the brand | `[TO CONFIRM]` from the product page (S4, March 2026): "Less Inflammation. Less Daily Pain. Move Freely Again." · "Fast-Dissolving. Sugar-Free. No Daily Painkillers." · "See Results in 30 Days or Get Your Money Back" — NOTE: "Less Inflammation / Pain Relief" lines are borderline under S7; the founder decides which survive | S4, S7 |
| Sign-off lines allowed | `[TO CONFIRM]` edenvia.com | S1, S2 |

## 2. Product facts (exact, never paraphrased)

| Field | Fill in | Source |
|---|---|---|
| Brand name, exactly as printed | EDENVIA | S3, S10 |
| Product name on the label | `[TO CONFIRM]` MOLECULAR HYDROGEN (Shopify title: "Molecular Hydrogen"; landing variants: "Molecular Hydrogen Tablets") | S2, S10 |
| What it is | `[TO CONFIRM]` 30 effervescent tablets per pouch; 1 tablet a day | S1, S4 |
| Ingredients | `[TO CONFIRM]` molecular hydrogen (H2), magnesium blend, citric acid, mineral support complex — `[MISSING]` amounts per tablet, PPM | S4 |
| What it DOES, in one line | `[TO CONFIRM]` turns a glass of water into hydrogen-rich water that supports the body's natural response to everyday oxidative stress | S8 (allowed language) |
| The ritual | drop 1 tablet in room-temperature or chilled water, let it dissolve ~3 minutes, drink within 30 minutes, once daily, never hot water | S4, S8 |
| What the ingredient must LOOK like in an ad | `[TO CONFIRM]` a clear glass of water, white tablet fizzing at the bottom, fine bubbles rising; water stays clear | — (proposal) |
| What the tablet looks like | `[TO CONFIRM]` round, flat, white, matte effervescent tablet, no imprint | — (proposal, needs a photo) |
| What the product is NOT | never a capsule, gel cap, pill, powder, scoop, liquid bottle, hydrogen water bottle/generator | S4 |
| Product word the specs use | pouch | S10 |

## 3. Label text (the packaging must show exactly this)

`[MISSING]` — to transcribe from the physical pouch, line by line in reading order. What S10 (AI render) shows, partly legible:

```
Container:  stand-up resealable pouch, white at the top fading to light blue at the bottom, matte
Line 1:     [atom icon] EDENVIA                      (dark navy)
Line 2:     MOLECULAR HYDROGEN                       (bold dark navy capitals)
Line 3:     [small descriptor — illegible in render: "…PPM of hydrogen per tablet"?]
Line 4:     [short benefit line — illegible]
Band:       DIETARY SUPPLEMENT [TO CONFIRM]
Count:      [MISSING] "30 TABLETS"?
```

The founder sends a sharp photo of the front of the pouch, or the artwork file; I transcribe. This becomes `product_lock`.

## 4. Offer, price, guarantee (the ONLY numbers allowed in an ad)

| Field | Fill in | Source |
|---|---|---|
| Price in ads | `[TO CONFIRM]` **$79.99** (Shopify live price). The founder's brief said **$79.90**. One of the two is wrong; lint blocks any price until this is settled. | S1 vs S2 |
| Crossed-out price | `[MISSING]` none on the Shopify variant; the landing page may display one | S2 |
| Deal wording allowed | `[MISSING]` — Shopify carries one-time post-purchase offers "2 Bags $54.00" and "3 Bags $81.00" (checkout upsells). Not for ads unless the founder says so. Product page in March 2026 showed BOGO-style tiers (S4) — unknown if still live. | S2, S4 |
| Guarantee | `[TO CONFIRM]` 30-day money-back guarantee (S1); March 2026 wording: "See Results in 30 Days or Get Your Money Back" (S4). Exact wording and conditions (first order only? opened pouch?) `[MISSING]` | S1, S4 |
| Site offers that must NEVER appear in ads | autoship, subscription, "50% off with subscription" | S4, rule |
| Bundles, gifts, free shipping | `[MISSING]` "FREE Cellular Recovery Protocol" and "free express shipping" appeared in March 2026 (S4) — only if still real | S4 |

## 5. Proof (each with its source)

| Claim, exact wording | Footnote / source | Status |
|---|---|---|
| "12,674 reviews" | product page, 2026-03-07 | `[TO CONFIRM]` recheck live count |
| "50,000+ sold" | product page, 2026-03-07 | `[TO CONFIRM]` |
| "Rated 4.9/5" | product page, 2026-03-07 | `[TO CONFIRM]` |
| "Third-party lab tested" | product page claim | `[TO CONFIRM]` certificate on file? |
| Customer survey stat | — | `[MISSING]` none on file; a stat template cannot be cloned until one exists |
| Real reviews we may quote | — | `[MISSING]` path to the reviews export (first name + initial only, rule B12) |
| Real authorities | — | none; never invent a doctor (S8) |

## 6. Avatar (who buys)

Primary persona from S5: **"Carol", 56**, formerly active, grandmother, researcher by necessity, professional skeptic.

| Field | Fill in | Status |
|---|---|---|
| Age range and look | 50–65, women and men, greying/silver hair, soft midlife build, US | `[TO CONFIRM]` (S4 says 40–65+) |
| Situation | married, kids grown, wants time with the grandkids and the garden | `[TO CONFIRM]` |
| The visible problem (core problem) | stiff, achy joints; morning stiffness; the knee/back that "negotiates" every first step | `[TO CONFIRM]` |
| Secondary problems | acid reflux; heart & arteries; kidneys (years of painkillers); low energy; stress; healthy aging | `[TO CONFIRM]` (S1 landing angles + S2 handles) |
| How she hides it | rail on the stairs, pause before standing, skips the walk/garden/floor time, ibuprofen in the bag | `[TO CONFIRM]` (derived from S5) |
| What they already tried | ibuprofen/Advil, Aleve, Tylenol; turmeric, glucosamine, fish oil, CBD, collagen; gabapentin, diclofenac, steroid shots; diets, stretching, yoga | S5 |
| The pleasure they won't give up | coffee, garden, walks, grandkids — nothing to give up, one tablet in water | `[TO CONFIRM]` |
| The proof they want to SEE | first step out of bed without the negotiation; stairs without the rail; the ibuprofen bottle untouched; a full morning in the garden | `[TO CONFIRM]` (S5 desire stack) |
| Deepest pains | "chained to my couch", "a burden on my husband", "I don't know who I am anymore" | S5 |
| Desires | to feel like herself again; independence; a future | S5 |

## 7. The core problem in the customer's own words

All from S5 (Reddit r/ChronicPain, r/Aging, r/Supplements, r/rheumatoid). `[TO CONFIRM]` which the founder wants as headline material.

```
"My body is taking the day off at an alarming rate."            — r/Aging
"I just don't know who I am anymore outside of this pain."       — r/ChronicPain
"Chained to my couch."                                           — r/ChronicPain
"A shadow of my former self."                                    — r/ChronicPain
"It did nothing for me." (turmeric)                              — r/Supplements
"You're gonna destroy your stomach." (daily ibuprofen)           — r/ChronicPain
"Kidney disease. Ask me how I know." (daily ibuprofen)           — r/ChronicPain
"It has stripped my independence, my self worth, my zest for life." — r/rheumatoid
"Just existing because that's all I can manage."                 — r/ChronicPain
"I'm really in disbelief. There's no way this is placebo."       — r/Supplements (H2 discovery)
```

## 8. Angles and mechanisms

| Field | Fill in | Status |
|---|---|---|
| Mechanism (plain words) | the tablet turns water into hydrogen-rich water; hydrogen is the smallest molecule there is, reaches every cell, and helps the body handle everyday oxidative stress — structure/function wording only | `[TO CONFIRM]` |
| Mechanism words never printed | selective antioxidant, hydroxyl radical, PPM, oxidative stress (headline), NSAID, bioavailability | `[TO CONFIRM]` |
| Top angles | A1 inflammation & stiffness (default) · A2 acid reflux · A3 heart & arteries · A4 kidneys · A5 energy · A6 stress · A7 longevity | `[TO CONFIRM]` default + which to keep |
| Headlines that already won | `[MISSING]` — founder to share the validated ads / winning headlines | — |
| Angles the product can NOT reach | `[MISSING]` — settled in step 2 | — |

Step 2 (`1-understand/new-brand-worksheet.md`) builds the mechanism map and the angle cards with two founder sign-offs, then this section is completed.

## 9. Banned words and compliance

Machine-checked list: `brand.json › banned` (regex + reason). Human-readable (S7, S8):

- Structure/function only: "supports", "helps maintain", "may support". Never diagnose / treat / cure / prevent / reverse / heal / manage a condition.
- Never name a disease or condition (arthritis, GERD, heart disease, kidney disease, fatty liver, autoimmune, anxiety…).
- No doctors, celebrities, invented experts or institutions. No "FDA-approved", "clinically proven".
- Never say it replaces a medication or that someone should stop one.
- No fake testimonials as real; no stat without a real source and footnote; no body before/after presented as a real customer.
- Disclaimer (short DSHEA version), only where the template has the slot: *"These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."*
- `[TO CONFIRM]` "*Results may vary" allowed as footnote.
- Angle keyword (B2, default angle): "pain" / "stiff" alone → must say "stiff joints", "morning stiffness", "achy joints" `[TO CONFIRM wording]`.
- Visual checks (C2): never a capsule/pill/powder; the glass stays clear; the container is a pouch; never hot water.

## 10. Logo rule

| Field | Fill in |
|---|---|
| The icon to use outside the label | the Edenvia atom icon only (two crossed elliptical orbit rings with two round dots), NO letters |
| Where the full wordmark is allowed | only on the real label, or pasted by script from the official file (D19) |

Files on hand (`edenvia/assets/logo/`): white wordmark no-bg (5818×1080, jagged edges at full size — needs a clean export), blue wordmark no-bg (`[TO CONFIRM]` quality), 500×500 icon on blue disc, icon on blue square. `[MISSING]` a transparent icon without the disc, and a vector/lossless master.

## 11. Fonts and colours

Colours (S3, Google Doc *Colors*; Konvert's scrape disagrees slightly, the doc wins):

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

Fonts: `[TO CONFIRM]` Manrope (S9, scraped from the site). Font file `[MISSING]`. Anton, Montserrat, Oswald, Fredoka ship with the skill.

## 12. Product photo and cutout (the two most important files)

- **Product photo** → `product_photo`: `[MISSING]`. Shopify's first product image (`1P.png`) is the candidate but could not be fetched from here. Founder sends the source packshot (front label readable, neutral background, high resolution).
- **Product cutout** → `product_cutout`: `[MISSING]`. Made from the packshot: transparent PNG, tight crop, upright, ≥800 px tall, edges checked on white and on black.
- S10 (the hero render) is an AI image with a garbled label: usable as a reference for the pouch shape and gradient, never as Image 1.

## 13. Competitors

From S6 (US molecular-hydrogen tablets). Names never printed in an ad.

| Name | What they sell | Why they matter | Their angles |
|---|---|---|---|
| Dr. Mercola H2 | 90 tablets, ~$24–30, 8 PPM | biggest name, best value | authority, value |
| Drink HRW Rejuvenation | 30 tablets, ~$40–50, 12.4 PPM | science-first, used in studies | PPM, research |
| Quicksilver Scientific H2 Elite | 10 PPM, premium | formulator authority | absorption, clean |
| H2TAB | 30 tablets, ~$30, 12 PPM, flavoured | Amazon's Choice | flavour, accessibility |
| Vital Reaction / Active H2 Ultra | 10+ PPM, clinical-grade | practitioner channel | clinical |
| Gundry MD Ultimate H2 | celebrity-doctor brand | big audience | authority |

**The competitor whose 35 ads we clone in step 1: `[MISSING]` — founder's choice.** Candidates by ad volume to check in the ad libraries: Gundry MD, Dr. Mercola, Drink HRW, H2TAB.

---

## Open items for the founder (one verdict each)

1. Price: $79.99 (Shopify) or $79.90 (brief)? Compare-at price? Any deal wording for ads?
2. Guarantee: exact wording and conditions.
3. Packshot source file + a sharp photo of the pouch front for the label transcription. A photo of one tablet and of a glass mid-fizz if available.
4. Logo masters: vector or lossless PNG of the wordmark (white and blue) and the icon alone on transparent.
5. Avatar: 50–65 women and men as proposed, or narrower? Default angle A1 inflammation & stiffness, or another? Which of A2–A7 stay?
6. Proof: current review count, rating, units sold; third-party test certificate; reviews export.
7. Tone in 3 words, aggressiveness level, winning headlines already validated.
8. The competitor for step 1.
9. Brand font file (Manrope?).
