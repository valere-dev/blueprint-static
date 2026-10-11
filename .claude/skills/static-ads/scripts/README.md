# scripts/ — generic copies of the Wildhorn pipeline

## Where brand.json lives (since 2026-10-02)
The brand file is at the **root of the skill** (`../brand.json`), next to `BRAND-KIT.md` — no longer `brand.json`.
In static-ads it is the blank template (`"_template": true`, every value `[MISSING]`); in wildhorn-static-ads it is filled with the Wildhorn values.
`sac_config.py` resolves it in this order: `$BRAND_JSON` (env) → `$SAC_WORKDIR/brand.json` → `../brand.json` (skill root).
For a new brand: `cp $SKILL/brand.json $SAC_WORKDIR/brand.json` and fill it from `BRAND-KIT.md`. Loading the blank template prints a warning on stderr.

Copies (not moves) of the scripts that produced Wildhorn run 1 and the Sam batch, with every brand path moved into `sac_config.py` / `brand.json`.
The originals in `/root/workspace/wh-remix/` are untouched and stay the Wildhorn production tools.

## Configuration (environment → brand.json → default)
| Variable | Default | Used by |
|---|---|---|
| `SAC_WORKDIR` | current directory | everything: `out/`, `log.jsonl`, `brand.json`, `feedback/` |
| `SAC_BATCH` | `$SAC_WORKDIR/batch` | specs, `templates/`, `prompts/`, `calls.jsonl`, `validated.json`, `sell_override.json`, `sell/`, `validated/` |
| `BRAND_JSON` | `$SAC_WORKDIR/brand.json`, else `../brand.json` (skill root) | all (see the skill's `brand.json` and `BRAND-KIT.md`) |
| `SAC_PAGES` | `$SAC_WORKDIR/pages` | page builders |
| `SAC_PUB` | none | remix.py: optional public copy of every output |
| `SAC_KEY_PREFIX` | `s` | output names `s_01_v1.png` (use another letter per template batch) |
| `SAC_BASELINE` | `$SAC_WORKDIR/stats_baseline.json` | build_sam.py baseline column |
| `SAC_RULES` | `../3-improve/rules.md` | build_lessons.py source |
| `SAC_NO_D13` | unset | `1` disables the template-rank check in lint |
| `SAC_FINAL_ALL` | `1` | build_samfinal.py: `0` hides validated ads |
| `OPENAI_KEY_FILE` | `/etc/secrets/openai_api_key` | remix.py, jarswap.py (path only) |
| `KIE_KEY_FILE` | `/etc/secrets/kie_api_key` | kie6.py (path only) |

## Files
| Script | Original | What changed in the copy |
|---|---|---|
| `sac_config.py` | — (new) | central paths + brand.json loader (env → working folder → skill root) |
| `srun.py` | `wh-remix/sam-batch/srun.py` | paths from config; LOCK/CONS built from brand.json (`product_lock`, `lock_extra`); passes `--product`; `aspect` spec field → Seedream `image_size`; refuses `seedream_full`; stops (instead of guessing) when a refused ad has no fallback recipe; Seedream "OK" also requires a new file (D10) |
| `lint.py` | `wh-remix/lint.py` | generic checks hard-coded; brand bans/competitors/angle keyword/visual checks/prices from brand.json; B12 allows signed quotes when `template_has_signature`; scene-engine fallback = error only for sexual/primary engines, warning otherwise; `sd_prompt` required with composite; **D13** template-rank check; **B20** price check |
| `remix.py` | `wh-remix/remix.py` | paths from config; no hard-coded `/srv/wildhorn-lp/remix` publish and no gallery rebuild (optional `SAC_PUB`); correct MIME for png/jpg |
| `kie_gen.py` | `wh-remix/kie_gen.py` | imports `kie6.py` from this folder instead of `/root/workspace/wildhorn-lp/p6/gen/kie6.py` |
| `kie6.py` | `wildhorn-lp/p6/gen/kie6.py` | output dir `$SAC_WORKDIR/out/_kie`; upload path from brand prefix; log date = today (was hard-coded 2026-09-25) |
| `composite.py` | `wh-remix/composite.py` | fonts dir + product cutout from brand.json; extra fonts via `fonts`; per-product `src`; same drawing logic |
| `jarswap.py` | `wh-remix/jarswap.py` | product description from `product_lock`; the S11 "jar replaces the head" sentence moved to `--context`; `--product`; tile clamped to the image |
| `build_sam.py` | `sam-batch/build_sam.py` | review page → `$SAC_PAGES/review.html`; embedded CSS (was read from `/srv/blueprint/batch-04.html`); no patching of other pages' tabs; optional baseline |
| `build_samfinal.py` | `sam-batch/build_samfinal.py` | final page → `$SAC_PAGES/final.html`; shows validated ads too (the original skipped them despite its title); sell PNGs `<Prefix>_SNN.png` |
| `build_validated.py` | `sam-batch/build_validated.py` | writes its own `validated.html` (the original regex-patched an existing `/srv/blueprint/wildhorn-ads/index.html`) |
| `build_all.py` | `wh-remix/build_all.py` | sets passed as `"Title=/folder"` arguments |
| `build_lessons.py` | `wh-remix/build_lessons.py` | renders `3-improve/rules.md` (### blocks) or a LESSONS.md (`- ID · rule · origin` lines) |
| `pages_common.py` | — (new) | CSS, page shell, spec loader, webp thumbs, tries sorted by version number (originals sorted by mtime) |
| `stats.py` | — (new; Wildhorn `wh-remix/stats.py` was run-1-specific) | batch metrics from calls.jsonl + validated.json (+ rounds.json) |
| `brief2spec.py` | — (new) | `1-understand/` hand-off briefs (`1-understand/new-brand-worksheet.md` §9) → draft spec file |
| `ingest_loom.sh` | — (new) | yt-dlp + mr-transcribe into `feedback/` |
| `../brand.json` | — (new; was `brand.json`) | the brand file, at the skill root: blank template in static-ads, filled Wildhorn values in wildhorn-static-ads |
| `fonts/` | `wh-remix/fonts/` (copied) | Anton, Montserrat (variable), Oswald (variable), Fredoka. DejaVu is the system font `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf` |

All `.py` files pass `python3 -m py_compile`. Tested on copies: lint on the Sam spec files (reproduces the latest-rule behaviour and the six D13 mismatches),
stats on the Sam calls/verdicts (reproduces 71.1 % / 86.7 % / 62.4 % / 1.6 / 1.43), composite on a pure_comp spec, brief2spec on the example hand-off brief,
build_lessons / build_sam / build_samfinal / build_validated on a copy of the Sam data (build_validated reproduced the 83 Wildhorn validated PNGs byte for byte).
Not run end to end against the APIs (no generation was triggered while building the skill).

## Constants still to set per brand (everything that was hard-coded for Wildhorn)
| Where | Wildhorn value | Set via |
|---|---|---|
| Product photo (Image 1) | `/root/workspace/wh-remix/product-jar.jpg` | brand.json `product_photo` |
| Product cutout | `/srv/wildhorn-lp/p6/jar-30.webp` | brand.json `product_cutout` |
| LOCK product sentence | "the WILDHORN Wild American Bison capsule jar … 30 CAPSULES." | brand.json `product_lock` |
| Brand name in CONS ("the WILDHORN jar") | WILDHORN / jar | brand.json `name`, `product_noun` |
| Icon-only sentence (D8) | "horn icon ONLY (two curved horns), NO letters" | brand.json `lock_extra`, `icon_description` |
| Bare-wordmark lint (D8) | `WILDHORN` | brand.json `wordmark` |
| Banned words | autoship, subscription, conversion, aromatase, compression shirt, reindeer/primal/viking/mars men, men over 40 | generic in lint.py + brand.json `banned`, `competitors` |
| "beer belly not belly" lint (B2) | `\bbelly\b` vs beer belly… on A1 | brand.json `angle_keyword` |
| Organ checks (C2) | capsule/organ/raw/veins/freeze-dried regexes | brand.json `visual_checks` |
| Prices (B20) | $49.95, $100 | brand.json `prices_allowed` |
| D6 product word | "jar" in placement | brand.json `product_noun` |
| Fonts dir | `/root/workspace/wh-remix/fonts/` | brand.json `fonts_dir` (default: `scripts/fonts` of this skill) |
| Output/publish dirs | `wh-remix/out`, `/srv/wildhorn-lp/remix`, `/srv/blueprint/*` | `SAC_WORKDIR`, `SAC_PUB`, `SAC_PAGES` |
| Sell/validated file names | `Wildhorn_S01.png`, `Wildhorn_01.png` | brand.json `file_prefix` |
| Avatar / ingredient wording in specs | `OLD`, `ORGANS`, `CAPS`, `HORN`, `STD` constants | top of each `sNspecs.py` |
| kie upload path | `images/wh-p6` | derived from `file_prefix` |
| Page title / tabs | "Sam batch", Wildhorn tabs | derived from `name` |
