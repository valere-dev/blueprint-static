# Batch 01 — template intake and clone plan (worksheet §8, filled for Edenvia · 2026-10-11)

Source of the templates: Adrien's Blueprint batch 01 for Wildhorn — the 79 `c####_template.webp` of the swipe file
(Drive › blueprint-machineroom-scrape › ex/web; mirror on the VPS at `/srv/blueprint/ex/web/`), already sorted by Adrien
into the 9 concept families (`example.md`, "The 79 templates, sorted into 9 concept families"). The families are reused
as they are (R1, R2). Raw-photo natives are not templates (founder, 2026-10-11).

## §8.1 Template intake — the 79, by family (Adrien's sort, kept 1:1)

| Family | Templates (c-id) | Count | Status |
|---|---|---|---|
| 1 US vs THEM / comparison | c0021 c0138 c0178 c0183 c0192 c0196 c0233 c0259 c0310 c0376 | 10 | **briefed — gate 2** |
| 2 Before-after / timeline | c0126 c0193 c0228 c0325 c0330 c0331 c0379 c0381 | 8 | briefed (2026-10-11) |
| 3 Problem reframe (X is not the problem) | c0039 c0113 c0118 c0128 c0157 c0198 c0234 c0245 | 8 | queued |
| 4 Mechanism / anatomy / ingredients | c0182 c0190 c0235 c0243 c0249 c0251 | 6 | queued |
| 5 Origin / source / real food | c0068 c0152 c0153 c0154 c0188 c0189 c0221 c0380 | 8 | queued |
| 6 Offer / bundle / price | c0124 c0127 c0158 c0232 c0248 c0317 c0318 c0319 c0323 c0327 c0335 | 11 | queued |
| 7 Bold claim + hero product | c0164 c0179 c0181 c0185 c0191 c0271 c0326 c0378 c0384 | 9 | queued |
| 8 Meme / humour / UGC | c0033 c0123 c0135 c0142 c0149 c0174 c0194 c0264 c0305 c0382 | 10 | queued |
| 9 Off-avatar, re-skin last | c0143 c0165 c0180 c0227 c0252 c0253 c0262 c0267 c0328 | 9 | queued |

One ad per template: 79 in, 79 out (R4). Files for the current family are in `edenvia/batch/templates/` named
`MM-DD_cNNNN_Source.webp` (real format, D10; sorted order = ad order). Families 2–9 are copied from the mirror on the
VPS when their turn comes (`cp /srv/blueprint/ex/web/cNNNN_template.webp …`).

Angles signed at gate 1 (all under `A8`, the lint prefix): **A8-L** heavy, swollen legs / puffy belly — "it was never
fat" (king) · **A8-F** puffy face and jawline · **A8-M** the man's belly that isn't fat. Inside each family the three are
spread, but each template keeps the angle it naturally carries (R3).

## §8.2 Clone plan — family 1 (10 ads)

| Template | Aspect | Angle carried (their ad) | Assigned | Change distance (witness / clock / setting / body / belief) | Headline (ours) | Production |
|---|---|---|---|---|---|---|
| c0021 Primal Edge Bison | 4:5 | "I tested 3 supplements" table | A8-L | reader / 30 days / product grid / legs / the fixes she tried graded | 3 Leg-Swelling Fixes. 1 Pair Of Heavy Legs. Here's The Truth. | table collage, pouch pasted |
| c0138 Mars Vitasteron | 1:1 | lose fat not definition (anatomy) | A8-L | none / none / medical plate / calf cross-section / fluid, not fat | Lose The Fluid, Not More Weight. | illustration, logo + button by script |
| c0178 Alevia AMLA | 1:1 | product vs coffee | A8-L | none / none / split page / none / tea only flushes | Edenvia's HYDROGEN vs Detox Tea | collage, pouch pasted |
| c0183 Bioma | 9:16 | us vs Ozempic (Pixar) | A8-L | self / none / studio split / legs & ankles / another diet never reached the legs | What comes with ANOTHER D!ET · What comes with EDENVIA | Pixar 3D regeneration |
| c0192 Primal Storm | 1:1 | blood-flow mechanism | A8-L | none / none / diagram / drainage vessel in the calf / fluid sitting still | DIETED FOR YEARS: LEGS STILL SWOLLEN? LOOK AT YOUR DRAINAGE. | sketch illustration, pouch pasted |
| c0196 Dyno Myo-Grow | 1:1 | guess who's on X (arms) | **A8-M** | friends / none / backyard BBQ / belly over the belt / blame the beer | Belt Buckle vs. Keg — Guess who's on EDENVIA | photo (A25 method), pouch pasted |
| c0233 Arctic glow balm | 9:16 | old me / new me pile | A8-L | none / none / flat lay / none / the graveyard of fixes | OLD ME / NEW ME · FOR HEAVY, SWOLLEN LEGS | photo flat lay, pouch pasted |
| c0259 Goli | 3:4 | your routine lets you down | A8-L | none / night → morning / bathroom counter → kitchen / none / routine, not willpower | Your current leg-swelling routine may be letting you down. | photo, pouch + fizzing glass |
| c0310 Overload | 1:1 | wojak vs chad (sexual) | **A8-M** | wife / none / meme card / gut / sucks it in vs tucks it in | HYDROGEN + MAGNESIUM + MINERALS — The Glass That Changes Everything. | meme line art, text by script |
| c0376 Mars Men | 9:16 | keep the drug, fix the side effect | **A8-F** | self / none / portrait / face & jawline / dieting with Edenvia | DIETING · DIETING WITH EDENVIA | comic illustration, both products pasted |

Coverage: A8-L 7 · A8-F 1 · A8-M 2. Already-made check: `creatives.jsonl` is empty (first batch).
Briefs: `edenvia/briefs/EDENVIA_B01_C####_V1.json` (worksheet §9). Draft specs from them lint clean
(`brief2spec.py` → `lint.py`, 10/10, 2026-10-11, cloud session). Generated on the VPS 2026-10-11 (10/10 first pass, 6 QC fixes, ~$5).
Loom 1 (written): product images rejected on all 10 (→ C23, product library), S2 offer slot → "-50%" (→ B23), rest validated.
Round 2 = product re-placement only, see VPS-SETUP §3c. Families 2–9 follow after the founder validates round 2.

## §8.3 Clone plan — family 2 (8 ads, before-after / timeline)

Briefed 2026-10-11 (cloud session) while the VPS generates family 1. These briefs are written before Loom 1, so the
first rules may retouch them before generation — they are not frozen. c0325 and c0330 are the same file in Adrien's
library (identical bytes); he ran it twice with two angles, we do the same.

| Template | Aspect | Angle carried (their ad / Adrien's final) | Assigned | Change distance (witness / clock / setting / body / belief) | Headline (ours) | Production |
|---|---|---|---|---|---|---|
| c0126 Mars Men | 1:1 | "Size doesn't matter, thickness does" → Adrien "…unless it's your belly" | A8-L | none / day 0 → 30 / sandals on a tiled floor / ankles / the scale is the wrong number | THE SCALE DOESN'T MATTER, SWOLLEN LEGS DO! | photo (A25), pouch + glass pasted |
| c0193 pregnant vs belly | 1:1 | "Only one of them is pregnant." (visual joke) | **A8-M** | wife / none / grey studio / belly / his is fluid | Only one of them is pregnant. | photo (A25), pouch pasted small |
| c0228 face day tags | 1:1 | Day 1 / Day 30 stacked, no headline | **A8-F** | self / day 1 → 30 / phone close-up / jawline & chin / the proof speaks | (no headline) Day 1 · Day 30 | photo (A25), native, no product |
| c0325 Primal Viking sketch | 4:5 | WEEK 0/2/4 "GOODBYE DAD BOD BELLY" | **A8-M** | none / 4 weeks / anatomy sketch / belly / flat, not abs | GOODBYE KEG BELLY | pencil illustration, pouch pasted |
| c0330 same sketch, 2nd use | 4:5 | Adrien "MAN BOOBS? DON'T HIDE — MELT THEM." | A8-L | none / 4 weeks / anatomy sketch / calves & ankles / stop hiding them | HEAVY LEGS? DON'T HIDE THEM — DRAIN THEM. | pencil illustration, pouch pasted |
| c0331 Primal Viking glow | 9:16 | "DISSOLVES LOVE HANDLES & CORTISOL BELLY BY DAY 28" (5 rounds) | A8-L | none / day 6-12-27-30 / medical poster / back of the calves / glow = where it drains | DRAINS HEAVY, SWOLLEN LEGS BY DAY 30 | flat illustration, pouch pasted (never squashed) |
| c0379 Beef Liver cartoon | 1:1 | "DRAINS BEER BELLY IN 14 DAYS" | **A8-M** | none / 30 days / red-blue split / belly / drains, doesn't burn | DRAINS THE BELLY THAT ISN'T FAT · IN 30 DAYS | Pixar 3D, pouch pasted |
| c0381 YOLO deal | 4:5 | "Flat But Flabby? Try YOLO." → "Beer Belly? Try WILDHORN." | A8-L | none / Jul-Aug-Sep / navy product hero / calves in rings / slim body, swollen legs | Slim Body, Swollen Legs? Try EDENVIA. · $39.00 ~~$79.99~~ | collage, pouch + glass pasted |

Coverage: A8-L 4 · A8-F 1 · A8-M 3 (running total after 18 ads: L 11 · F 2 · M 5). Draft specs lint clean
(`brief2spec.py` → `lint.py`, 8/8, 2026-10-11). Lessons carried from Adrien's run on these templates: c0331 keeps a small
glow on the result panel and a pouch in true proportions; c0228 keeps no headline; c0381 keeps the month labels;
c0379 keeps the verb DRAINS word for word; c0193 keeps the single line (the B1 subline was dropped at Loom 2).
