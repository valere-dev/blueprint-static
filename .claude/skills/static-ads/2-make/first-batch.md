# First batch — from a filled brand kit to the first 10 ads

Step by step for a new brand, once `BRAND-KIT.md` is filled (and, for a brand with no research yet, once
`1-understand/new-brand-worksheet.md` is signed off). The product images, `brand.json` field by field and what is
Wildhorn-only are in `BRAND-KIT.md`. The full pipeline behind each step: `2-make/PIPELINE.md`.

## 0. Division of labour inside this skill
- **`1-understand/`** does the research and the reading: product sheet, mechanism map, competitor ads, avatar,
  top-5 angles + headline bank, template intake + concept families, and one **hand-off brief per template** (`1-understand/new-brand-worksheet.md` §9).
  Run it first, with its two sign-off gates (angles/avatar; first concept family of briefs). Don't duplicate it here.
- **`2-make/`** turns briefs into specs, generates, QCs and builds the review pages; **`3-improve/`** runs the review loop and keeps the rulebook.
- If the reviewer hands you templates without a brief, do the decode yourself in the spec (`why`, `dna`, `scene`, `inventory`) using
  `1-understand/template-reading.md` as the checklist.

## 1. Working folder
```bash
ssh vps-claude
mkdir -p /root/workspace/<brand>-remix/{batch/templates,batch/prompts,out,feedback,pages}
cd /root/workspace/<brand>-remix
cp /root/claude-vault/skills/static-ads/brand.json brand.json
export SAC_WORKDIR=$PWD SKILL=/root/claude-vault/skills/static-ads
```
Everything a batch produces stays in this folder; never write into another brand's workspace or into `/srv` directly.

## 2. Spec constants for the brand
Rewrite the shared strings at the top of the first spec file (`2-make/spec-format.md`): `OLD` (avatar look), the ingredient constant (`ORGANS` for
Wildhorn), the capsule constant, `HORN` (icon-only sentence), `STD` (generic KEEP lines). These carry the latest wording of C2/A11/D8 into every ad.

## 3. Templates
- The reviewer (or `1-understand/new-brand-worksheet.md` §8) provides the winning templates. Accept every template (R1); sort into concept families (R2).
- Copy them (never move) into `$SAC_BATCH/templates/`, named so that sorted order = ad order (`MM-DD_cNNNN_Source.ext`). The extension must be the real format (D10).
- Read each template at full resolution before writing its spec. Note its aspect ratio and production method (photo, illustration, text-only,
  photo + pasted product → A25).

## 4. First batch of 10
1. Briefs → draft specs: `python3 $SKILL/scripts/brief2spec.py $SAC_BATCH/s1specs.py <kit>/briefs/*.json` (or write specs by hand).
2. Do the judgment by hand: inventory ≥ 5 lines, angle per template, texts slot by slot, `visual` rewritten as one scene, fallback recipe for sexual/skin ads.
3. `python3 $SKILL/scripts/lint.py $SAC_BATCH/s1specs.py` → LINT OK.
4. Generate: `for n in $(seq 1 10); do python3 $SKILL/scripts/srun.py $SAC_BATCH/s1specs.py $n; done` (or `xargs -P 5`).
5. Full-res QC of the 10 (2-make/qc-checklist.md); fix before showing (QC log).
6. `python3 $SKILL/scripts/build_sam.py` → wire `$SAC_PAGES` to a `<brand>-review.machineroom.app` handle once → send the link.
7. Loom → 3-improve/feedback-loop.md.

## 5. What to expect
- The generic rules transfer (decode, inventory, text count, placement, engines, QC). Expect the first misses on **brand taste**: the reviewer's
  idea of aggressive, the avatar's real behaviours, which angle is default, how the ingredient must look. Those become new rules in round 1–2.
- Expect 40–60 % first try on the first 10, rising to 70 %+ by round 3 if every miss becomes a rule (Wildhorn: 60 % → 76 % → 72 % with 13 QC catches).
- Expect OpenAI refusals on anything sexual or with bare skin close-ups: plan `seedream_comp` for those templates at spec time.
- Expect the logo to be misspelled whenever it appears outside the label: icon-only from day one (D8).

## 6. Pre-flight checklist (before the first generation of a new brand)
- [ ] `1-understand/` sign-off gate 1 passed (angles + avatar) and gate 2 for the first concept family of briefs.
- [ ] `BRAND-KIT.md` and `brand.json` filled (no `[MISSING]` left); `python3 -c "import json;json.load(open('brand.json'))"` OK; `lint.py` runs without a JSON error.
- [ ] `product_photo` opens, label readable at full resolution; `product_cutout` has a clean alpha edge (render one composite on white and on black to check halos).
- [ ] `product_lock` names every visible packaging element; `lock_extra` carries the icon-only sentence; `icon_description` matches the real icon.
- [ ] `prices_allowed`, `offer`, `proof` match the live offer exactly (reconfirm the price with the founder — Wildhorn's was locked at $49.95 only after asking).
- [ ] `banned` includes competitor names, jargon, compliance bans; `angle_keyword` set for the default angle; `visual_checks` cover the ingredient look.
- [ ] Spec constants written (avatar look, ingredient look, capsule look, icon sentence, `STD`).
- [ ] Templates copied into `batch/templates/`, sorted order = ad order, real extensions; aspect ratio and production method noted per template.
- [ ] `SAC_PAGES` served on its own `*.machineroom.app` handle (noindex, clean URLs) — or the founder knows where to look.
- [ ] `calls.jsonl`, `validated.json`, `sell_override.json` start empty for the batch; `rounds.json` only if needed.
- [ ] Budget agreed for the round (10 ads ≈ 10–20 OpenAI calls ≈ $3–6 at ~$0.30/image, plus a few Seedream scenes).
