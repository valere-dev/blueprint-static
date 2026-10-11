# Stats — definitions, benchmarks, how to compute

Stats prove the loop works and tell where to spend the next fix. Report them after every round.

## Definitions
| Metric | Formula | Notes |
|---|---|---|
| Generations | count of engine calls (`calls.jsonl` lines) | OK or not: refusals and failures count (they cost time and money). Script-only renders (pure_comp) are logged as `script` and count as one. |
| Hit rate | validated ads ÷ generations | "% of generations validated" |
| Generations per validated ad | generations ÷ validated ads | inverse of hit rate |
| First-try rate | ads validated on the first review of the first try ÷ ads reviewed | verdict contains "first try" |
| After-one-fix rate | ads validated within 2 review rounds ÷ ads in the batch | |
| Final rate | validated ÷ ads in the batch | target 100 % |
| Rounds per ad | mean number of reviews until validation (validated ads) | 1 = first try |
| Refused/failed calls | `ok: false` lines | by engine; OpenAI refusals are the fallback trigger |

Round classification (when no `rounds.json`): verdict text "first try" → 1; "redo 1", "(redo)", "both tries", "= sell" → 2; "after fix", "try 1 validated" → 3; anything else → 4 + warning.

## Compute
```bash
SAC_WORKDIR=/root/workspace/<brand> python3 /root/claude-vault/skills/static-ads/scripts/stats.py --ads 83
```
Writes `$SAC_BATCH/stats.json`. `build_sam.py` shows a baseline column if `$SAC_WORKDIR/stats_baseline.json` (or `SAC_BASELINE`) exists —
copy a previous batch's `stats.json` there to compare runs.

Run-1-style stats (no calls log, several batch folders): the Wildhorn `stats.py` counted every image file per ad (`out/<key>_v*.png` + `_sd_` + `_raw_`)
plus "moderation_blocked" lines in logs, and rounds = number of batches in which the ad got a version. Use calls.jsonl from day one instead.

## Benchmarks (Wildhorn)

| | Run 1 (79 ads, before the rulebook) | Sam batch (83 ads, rulebook + lint + inventory) |
|---|---|---|
| Generations | 258 + 3 refused = 261 | 133 (108 OpenAI ok, 8 OpenAI refused/failed, 16 Seedream, 1 script) |
| Validated on the first try | **0 %** (0/79) | **71.1 %** (59/83) |
| Validated after one fix | — | **86.7 %** (72/83) |
| Final | 79/79 after 9 rounds | **100 %** (83/83; 82 after Loom 4, S11 at Loom 5) |
| Hit rate (validated ÷ generations) | **30.3 %** | **62.4 %** |
| Generations per validated ad | **3.3** | **1.6** |
| Review rounds per ad | **2.5** (2 rounds: 51 ads · 3: 21 · 4: 4 · 5: 3) | **1.4** (1: 59 · 2: 13 · 3: 10 · 4: 1) |

Per round in the Sam batch: round 1 6/10 first try (60 %), round 2 26/34 new ads (76 %), round 3 31/43 new ads (72 %); QC round 3 fixed 13 defects before review.

What moved the numbers (in order of impact, from the case studies): the pixel inventory (A13) → 0 % to 60–76 % first try; "change the minimum + one-word angle swap" (E7–E10);
scene-only Seedream + composite for refusals (D7) → no garbled sexual ads; frozen tries + sell overrides (A20/A26) → no regression on redos; the blocking lint (D-rules).

## Known measurement caveats
- `calls.jsonl` undercounts the Sam batch slightly: the A25 steps for S11 (extra Seedream edits `s_11_sd_v4…v6` and the `jarswap.py` call) were run by hand and not logged (5 calls logged for S11; ~3–4 more were made). Log manual calls by hand.
- Two "first try" figures exist on the Wildhorn pages: `/sam` showed 67.5 % (counted ads with exactly one output file = 56/83), `/sam-final` showed 71.1 % (verdict text = 59/83).
  The difference is S38, S43 and S71: each got a second file from my own QC fix BEFORE the reviewer saw it (avatar age, misspelled logo, leftover template prop), then was validated
  on its first review. **Use the verdict-based number** (it measures the reviewer's first look); report pre-review QC fixes separately (13 in Sam round 3).
- Run 1 "first try" is 0 %: every one of the 79 ads got at least one later version after the reviewer's batch-01 feedback (rounds = number of batches with a version; minimum 2).
- The `/sam` page's run-1 rounds line showed "2 rounds: 0 ads" because `stats_run1.json` stores the distribution with string keys and the page looked them up with int keys (cosmetic bug in the Wildhorn builder; fixed in the copied builders by not reading that file).

## Targets for a new brand
- First batch of 10: expect 40–60 % first try (the rules are generic; brand facts and taste are new). By round 3: ≥ 70 %.
- Hit rate ≥ 55 %, generations per validated ad ≤ 2.
- Any metric that drops vs the previous round → look at which rule the misses share, not at the engine.

## Run 1 round history (from the checkpoint log, 01/10/2026)
| Round | Reviewed by | Redos | New ads | QC fixes before showing | Rules born |
|---|---|---|---|---|---|
| Batch 01 | written feedback (L1) | — | 79 (all templates, 1 per template) | c0245 "reindeer", c0232 guarantee twice, c0123/c0262 blocked → product-only | R11–R14, B1–B4, A6 |
| Batch 02 | Loom 2 | #1–#20 redone | — | #2 arm→belly, #4 Pixar style, #10 avatar age, #13 obvious before/after | C5, C6, C12, A27 |
| Batch 03 | Loom 3 | #2 #6 #8 #10 #11 #16 | #21–#30 | #22 jar covering the hero | E9, E10, A28, B11, C7 |
| Batch 04 | Loom 4 | #2 #8 #23 #26 (+ upgrades #16 #29 #30) | #31–#40 | #26 #33 #35 #38 | A2 (Template DNA = "Protocol 0"), B5, C2 |
| Batch 05 | Loom 5 | #2 #16 #23 #35–#40 | #41–#50 | #35 logo → icon only | C15, B9, C8 |
| Batch 06 | Loom 6 | #35 #39 #44 #47 | #51–#60 | #60 blocked (man boobs + torso) → rewritten | C3, B7, B8, A6 (fat bottle) |
| Batch 07 | Loom 7 | #35 #51 #57 #58 | #61–#70 | #62 objects only (OpenAI blocks chest) | A3, A4, D1 → LESSONS.md + blocking lint created |
| Batch 08 | Loom 8 | #57 #61 #62 #63 #65 #68 #69 #70 | #71–#79 | — | A7–A12, B6, B12, B13, C2, C9, D5 |
| Batch 09 | Loom 9 | 12 redos | — | — | A13 (pixel inventory), C10 |
Every redo went back on the review page with all its earlier versions; 79/79 were final after Loom 9 (`run1-final/`, #74 = its B8 version).

## What the Sam batch ledger says (where first tries are lost)
| Slice | First try |
|---|---|
| OpenAI only (76 ads) | 57/76 = **75 %** |
| OpenAI refused → Seedream scene + composite (6 ads) | 1/6 = **17 %** |
| Script only (1 ad) | 1/1 |
| Default angle "A1 beer belly" (62 ads) | 44/62 = 71 % |
| Sexual / drive templates (12 ads) | 8/12 = 67 % |
Reading: the refusal path is where first tries die (it was also where D6, D7 and A25 were learned). For a new brand, plan every sexual/skin template
at spec time with a complete scene recipe (sd_prompt with empty zones, composite with every placement), or choose the A25 method directly.
Sources with mostly-UGC/photo templates with people (Sugar-Splash 1/4, Resilia 1/3) were harder than designed posters (Everly 5/5, Spicy-Cubes 9/10).

## Sam batch ledger (all 83 ads)
Generated from `sam-batch/s*specs.py` (last spec per ad), `templates/` (rank = ad number), `calls.jsonl`, `validated.json`, `sell_override.json`.
"Tries" = output files `out/s_NN_vK.png`; "Calls" = engine calls logged (a refused call produces no file; QC fixes produce files).

| S | Template | Angle (last spec) | Engines | Tries | Calls | Sell try | Verdict |
|---|---|---|---|---|---|---|---|
| S1 | c0003 Mars-Men | A1 Beer belly (inches, flipped) | openai | 1 | 1 | 1 | Validated (first try) |
| S2 | c0008 Mars-Men | A1 Beer belly + GLP-1 (fused) | openai | 2 | 2 | 2 | Validated (redo 1) |
| S3 | c0010 Mars-Men | A4 Product system | openai | 1 | 1 | 1 | Validated (first try) |
| S4 | c0012 Mars-Men | A1 Beer belly (identity) | script | 1 | 1 | 1 | Validated (first try) |
| S5 | c0013 Mars-Men | A1 Beer belly = estrogen | openai | 1 | 1 | 1 | Validated (first try) |
| S6 | c0015 Resilia | A1 Beer belly = estrogen | openai | 1 | 1 | 1 | Validated (first try) |
| S7 | c0016 Resilia | A1 Beer belly (shock) | openai | 2 | 2 | 2 | Validated (redo 1) |
| S8 | c0017 Resilia | A1 Beer belly | openai | 4 | 4 | 4 | Validated (redo 1) — make more aggressive |
| S9 | c0019 Menerals | A3 Wild vs farmed + beer belly | openai | 2 | 2 | 1 | Validated (both tries) |
| S10 | c0023 Primal-Viking | Drive (same angle as template) | openai | 1 | 1 | 1 | Validated (first try) |
| S11 | c0025 Primal-Viking | A1 + drive (fused) | openai+seedream | 5 | 5 | 5 | Loom 5 — made like theirs (A25) |
| S12 | c0026 Primal-Viking | Drive + beer belly (fused, sexual) | openai+seedream | 1 | 2 | 1 | Validated (first try) |
| S13 | c0024 Ryze | A1 Beer belly (same angle as template) | openai | 1 | 1 | 1 | Validated (first try) |
| S14 | c0027 RYZE | A1 (same angle — copy) | openai | 2 | 2 | 2 | Loom 4 (after fix) |
| S15 | c0028 RYZR | A1 Beer belly (Pixar) | openai | 2 | 2 | 2 | Validated (redo) |
| S16 | c0029 Primal-Viking | A1 Beer belly (same angle — competitor) | openai | 1 | 1 | 1 | Validated (first try) |
| S17 | c0030 Primal-Viking | A1 Beer belly (Primal Edge — our category) | openai | 2 | 2 | 2 | Validated (redo) |
| S18 | c0031 Cowboy-Colostrum | A1 Beer belly | openai | 4 | 4 | 4 | Loom 4 (after fix) |
| S19 | c0032 Olux | A1 Beer belly (multi-benefit) | openai | 1 | 1 | 1 | Validated (first try) |
| S20 | c0034 O-Positive | A1 + drive (UGC) | openai | 1 | 1 | 1 | Validated (first try) |
| S21 | c0035 Mammoth-Headwear | A1 Beer belly (UGC Day 0 / Day 90) | openai | 1 | 1 | 1 | Validated (first try) |
| S22 | c0036 Thriving-in-Menopause | A1 Beer belly (thermal) | openai | 1 | 1 | 1 | Validated (first try) |
| S23 | c0037 Happy-Mammoth-US | A1 Beer belly (visual pun) | openai | 1 | 1 | 1 | Validated (first try) |
| S24 | c0038 Happy-Mammoth | A1 Beer belly | openai | 2 | 2 | 2 | Validated (redo) |
| S25 | c0040 Spicy-Cubes | A1 Beer belly (mirror) | openai | 1 | 1 | 1 | Validated (first try) |
| S26 | c0042 Froya-Organics | A1 Beer belly | openai | 1 | 1 | 1 | Validated (first try) |
| S27 | c0044 Primal-Queen | A1 Beer belly (shock/humor) | openai | 1 | 1 | 1 | Validated (first try) |
| S28 | c0045 Mars-Men | Testosterone + beer belly (fused) | openai | 1 | 1 | 1 | Validated (first try) |
| S29 | c0047 Mars-Men | A1 Beer belly | openai | 4 | 4 | 4 | Loom 4 (after fix) |
| S30 | c0049 Primal-Viking | Drive + beer belly (fused, illustrated) | openai | 1 | 1 | 1 | Validated (first try) |
| S31 | c0056 Zapply | A1 Beer belly | openai | 1 | 1 | 1 | Validated (first try) |
| S32 | c0057 Zapply | A1 Beer belly (dad guilt) | openai | 1 | 1 | 1 | Validated (first try) |
| S33 | c0058 Zapply | A1 Beer belly | openai | 2 | 2 | 2 | Validated (redo) |
| S34 | c0059 Zapply | A1 Beer belly (said no wife ever) | openai | 1 | 1 | 1 | Validated (first try) |
| S35 | c0060 Zapply | A1 Beer belly | openai | 3 | 3 | 2 | Validated (redo) |
| S36 | c0061 Everly | A1 Beer belly (offer urgency) | openai | 1 | 1 | 1 | Validated (first try) |
| S37 | c0062 Everly | A4 Category takedown | openai | 1 | 1 | 1 | Validated (first try) |
| S38 | c0063 Everly | A1 Beer belly (progress) | openai | 2 | 2 | 2 | Validated (first try) |
| S39 | c0064 Everly | A1 Beer belly (timeline) | openai | 1 | 1 | 1 | Validated (first try) |
| S40 | c0065 Everly | A1 Beer belly (same structure as template) | openai | 1 | 1 | 1 | Validated (first try) |
| S41 | c0066 Primal-Viking | A1 Beer belly (challenge) | openai | 1 | 1 | 1 | Validated (first try) |
| S42 | c0067 Primal-Viking | A1 Beer belly (vs fat burners) | openai | 2 | 5 | 1 | Loom 4 — try 1 validated, keep it |
| S43 | c0075 Infiniwell | A1 Beer belly | openai | 2 | 2 | 2 | Validated (first try) |
| S44 | c0076 RYZE | A1 Beer belly (offer) | openai | 1 | 1 | 1 | Validated (first try) |
| S45 | c0077 RYZE | A1 Beer belly | openai | 1 | 1 | 1 | Validated (first try) |
| S46 | c0078 RESIA | A1 Beer belly = estrogen | openai | 1 | 1 | 1 | Validated (first try) |
| S47 | c0079 Gruns | A1 Beer belly (meme) | openai | 2 | 2 | 2 | Validated (redo) |
| S48 | c0080 Primal-Queen | A1 (same angle — copy) | openai | 1 | 1 | 1 | Validated (first try) |
| S49 | c0081 Primal-Queen | A1 Beer belly = estrogen (doll callouts) | openai | 1 | 1 | 1 | Validated (first try) |
| S50 | c0082 Primal-Queen | A1 Beer belly | openai | 2 | 2 | 2 | Loom 4 (after fix) |
| S51 | c0083 Primal-Queen | A1 Beer belly (shame moment) | openai | 1 | 1 | 1 | Validated (first try) |
| S52 | c0084 Primal-Queen | A1 Beer belly = estrogen | openai | 2 | 2 | 2 | Loom 4 (after fix) |
| S53 | c0085 Mars-Men | A2 Man boobs (same angle — copy) | openai | 1 | 1 | 1 | Validated (first try) |
| S54 | c0094 Sugar-Splash | A1 Beer belly (vs fat burners) | openai | 1 | 1 | 1 | Validated (first try) |
| S55 | c0095 Sugar-Splash | Drive + beer belly (sexual) | openai+seedream | 2 | 3 | 2 | Validated (redo) |
| S56 | c0102 Sugar-Splash | A1 Beer belly | openai | 2 | 3 | 2 | Loom 4 (after fix) |
| S57 | c0104 Sugar-Splash | A1 + drive (woman angle) | openai | 2 | 2 | 2 | Loom 4 (after fix) |
| S58 | c0105 Spicy-Cubes | Drive (sexual — same buyer) | openai+seedream | 3 | 4 | 1 | Validated (try 1 = sell) |
| S59 | c0106 Spicy-Cubes | Drive + beer belly (humor) | openai | 1 | 1 | 1 | Validated (first try) |
| S60 | c0107 Spicy-Cubes | A3 Wild vs farmed | openai | 1 | 1 | 1 | Validated (first try) |
| S61 | c0108 Spicy-Cubes | A1 Beer belly (starter pack) | openai | 1 | 1 | 1 | Validated (first try) |
| S62 | c0109 Spicy-Cubes | Drive (sexual — wilderness) | openai | 1 | 1 | 1 | first try (Loom 4) |
| S63 | c0110 Spicy-Cubes | A1 Beer belly | openai | 1 | 1 | 1 | Validated (first try) |
| S64 | c0111 Spicy-Cubes | Drive (cheeky) | openai | 1 | 1 | 1 | Validated (first try) |
| S65 | c0112 Spicy-Cubes | A1 (vs fat burners) | openai | 1 | 1 | 1 | Validated (first try) |
| S66 | c0114 Spicy-Cubes | A1 + drive (fused) | openai | 1 | 1 | 1 | Validated (first try) |
| S67 | c0115 Wandering-Bear-Coffee | A3 Wild (food) | openai | 1 | 1 | 1 | Validated (first try) |
| S68 | c0116 Olux | A1 (same angle — copy) | openai | 1 | 1 | 1 | Validated (first try) |
| S69 | c0117 Primal-Queen | A1 Beer belly (Primal Queen organs) | openai | 1 | 1 | 1 | Validated (first try) |
| S70 | c0118 Primal-Queen | A1 Beer belly = estrogen (validated concept) | openai | 1 | 1 | 1 | Validated (first try) |
| S71 | c0119 Cowboy-Colostrum | A4 Product system | openai | 2 | 2 | 2 | Validated (first try) |
| S72 | c0120 Cowboy-Colostrum | A1 Beer belly (testimonial) | openai | 1 | 1 | 1 | Validated (first try) |
| S73 | c0121 Cowboy-Colostrum | A1 Beer belly | openai | 1 | 1 | 1 | Validated (first try) |
| S74 | c0122 RYZE | A1 (same angle) | openai+seedream | 4 | 5 | 4 | Loom 4 (after fix) |
| S75 | c0124 RYZE | A1 (validated concept) | openai | 1 | 1 | 1 | Validated (first try) |
| S76 | c0125 RYZE | A1 Beer belly (doll) | openai | 1 | 1 | 1 | Validated (first try) |
| S77 | c0126 Mars-Men | A1 (validated concept) | openai | 1 | 1 | 1 | Validated (first try) |
| S78 | c0127 RYZE | A1 (validated concept) | openai | 1 | 1 | 1 | Validated (first try) |
| S79 | c0130 Mars-Men | A2 Man boobs (same angle — copy) | openai+seedream | 3 | 4 | 1 | Validated (try 1 = sell) |
| S80 | c0131 RYZE | A1 Beer belly | openai | 2 | 2 | 2 | Loom 4 (after fix) |
| S81 | c0132 RYZE | A1 Beer belly (Muppet) | openai | 1 | 1 | 1 | Validated (first try) |
| S82 | c0133 RYZE | A1 Beer belly (retro TV) | openai | 1 | 1 | 1 | Validated (first try) |
| S83 | c0134 RYZE | A1 (same angle — copy) | openai | 1 | 1 | 1 | Validated (first try) |
