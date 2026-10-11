# Running the Edenvia system on the VPS (Adrien's setup, 1:1)

The cloud session that built this repo cannot reach the VPS (no SSH client, outbound limited to an HTTPS
allow-list). Everything below runs **on the VPS itself**, in a Claude Code session opened there, exactly as
Adrien runs Wildhorn ("ssh vps-claude", everything on the VPS, never in the Mac's browser).

## 0. Reality check (2026-10-11, from the VPS session)

- Host `nutraflow1`, user `adanalysis` (not root). Checkout: `/home/adanalysis/workspace/blueprint-static`.
- `export SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia SKILL=/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads`
- The Blueprint mirror is already on the host at `/srv/blueprint` (world-readable): 79 source templates in `ex/web/`, 1,106 concept files in `external-wildhorn/remix/`. No Drive download needed.
- Pages are served by nginx on `blueprint.nutraflow.app` (noindex header + review API already there), not Caddy. Section 4 below is superseded: add a location/server block for `edenvia/pages`.
- `brand.json` asset paths are absolute to this checkout since v1.3.
- Research outputs live in `edenvia/research/<competitor>/` (step 1) and `edenvia/briefs/` (step 2); `git pull` before every batch.

## 1. One-time bootstrap (paste into Claude Code on the VPS)

```
Clone https://github.com/valere-dev/blueprint-static (branch claude/friendly-bell-v79g1w) into
/home/adanalysis/workspace/blueprint-static (already done on nutraflow1 — then just `git pull`). Read README.md, VPS-SETUP.md, edenvia/BRAND-KIT.md and
.claude/skills/static-ads/SKILL.md before anything else. Working folder for every batch:
SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia, SKILL=/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads.
Check that /etc/secrets/openai_api_key and /etc/secrets/kie_api_key exist (never print them).
Then tell me what is missing from the pre-flight checklist in $SKILL/2-make/first-batch.md §6.
```

## 2. Secrets (founder puts them on the VPS, never in a chat)

| File | Used by |
|---|---|
| `/etc/secrets/openai_api_key` | `scripts/remix.py`, `scripts/jarswap.py` (gpt-image-2), Loom transcription (Whisper API) |
| `/etc/secrets/kie_api_key` | `scripts/kie6.py` (Seedream fallback) |

`chmod 600`, owned or readable by `adanalysis`. The scripts read the path, not an env var (`OPENAI_KEY_FILE`, `KIE_KEY_FILE` in `scripts/sac_config.py`). Creating `/etc/secrets` needs root.
On nutraflow1 (2026-10-11) the session has no root, so the files live in `/home/adanalysis/.secrets/` (dir 700, files 600) and
`sac_config.py` falls back to `~/.secrets/<name>` when `/etc/secrets/<name>` is absent; `~/.bashrc` and `~/.profile` also export
`OPENAI_KEY_FILE` / `KIE_KEY_FILE`. Both keys verified 2026-10-11 (OpenAI: gpt-image-2 + whisper-1 listed, Whisper end to end; kie: credit balance read).
The keys were pasted in the chat to be installed: rotate them after the first batch and drop the new values into the same files.

## 3. Templates (step 2 input)

Adrien's template folders live on his VPS at `/root/workspace/wh-remix/templates/` (before-after, bold claim,
feature-benefit, meme, negative hook, problem-solution, us vs them, offer/sales, statistic). Two sources to
rebuild the same folders here:

- **The Blueprint mirror in the founder's Drive** (`blueprint-machineroom-scrape`): `ex/web/c####_template.webp`
  = the source template of every batch ad (thumbnails, ~100 files) and `external-wildhorn/remix/` = the concept
  remix page with 1,105 concept images at full size. Download the folder to the VPS (Drive desktop export or
  `gdown`), then copy into `edenvia/batch/templates/` named `MM-DD_cNNNN_Source.ext` (sorted order = ad order,
  real extension, rule D10).
- **Lymphoria's own winning statics** (step-1 competitor): the 35 decoded in step 1, pulled from Brandsearch
  by EU spend. Same buyer, same desire, so their structures are the first concept families to clone.

## 3b. Step 2 hand-off (2026-10-11): concept family 1 is briefed

```
git pull
export SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia SKILL=/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads
export SAC_BATCH=$SAC_WORKDIR/batch BRAND_JSON=$SAC_WORKDIR/brand.json
python3 $SKILL/scripts/brief2spec.py $SAC_BATCH/s1specs.py $SAC_WORKDIR/briefs/EDENVIA_B01_C*.json
python3 $SKILL/scripts/lint.py $SAC_BATCH/s1specs.py        # passes as drafted (checked in the cloud session)
```
Then, per `2-make/spec-format.md`: rewrite each `visual` as one scene description, keep every KEEP product placement in
the composite (D6), set the engine per `production_method` (c0196 is a photo → A25 method; c0310 meme text by script),
generate the 10 ads of family 1 only (gate 2), QC at full resolution, build the comparison page (template | ad) and the
demo page under `edenvia/pages/`, and send the two links. Budget per round: $30 (founder).

## 3c. Round 2 of family 1 (after Edenvia Loom 1, 2026-10-11)

```
git pull    # brings rules C23 + B23, brief c0138 (-50%), edenvia/assets/product/library/ (14 photos + INDEX.md), brand.json product_library
```
1. **Product library.** The founder's folder is now public ("anyone with the link"). On the VPS:
   ```
   pip install -q gdown
   mkdir -p /tmp/edenvia-prodref && gdown --folder --remaining-ok -O /tmp/edenvia-prodref "https://drive.google.com/drive/folders/1yRiSc4xCw66dJdPtz_FzLD0cEJ1RbeWd"
   ```
   Then run `python3 $SKILL/../sort-ad/../../edenvia/assets/product/library/import_library.py /tmp/edenvia-prodref` — it imports only the files not yet in
   `edenvia/assets/product/library/` (lifestyle shots → 1536 px JPEG q92, product-only shots → full-size PNG), appends one line per file to
   `INDEX.md` with a placeholder description to fill after looking at each image, and skips the three logos. Then build the cutouts: pouch standing (from
   `studio_pouch-ice-bowl-glass-straw-v2.png`), pouch in hand with the hand (from `hand_pouch-kitchen.jpg` and `people_*`), tablets (from
   `flatlay_pouch-tablets-drops.png`). Save them as `edenvia/assets/product/cutouts/<name>.png` and point `brand.json` `product_cutout` at the standing one.
2. **Redo S1–S10 per C23**: keep every validated pixel (D21), replace only the pouch placement: right library cutout for the slot, scaled to the
   template's product size or bigger, droplets kept, colour grade and contact shadow matched, hand from the library when the template's product is
   held. S2 also gets the button `-50%` (B23). Masters in `out/_raw/`, outputs 1080 wide (D15).
3. QC side by side with the template AND with the library photo (C22/C23), then rebuild the comparison page and the demo page (D20) and republish
   the two artifacts in place. Report cost against the $30 round budget.
4. Push on the deploy key once the founder has added it (Settings → Deploy keys → write access).

Family 2 is briefed (plan §8.3); regenerate it only after the founder validates round 2 of family 1.

## 4. Review pages

The mirror's `deploy/` folder has Adrien's deploy: `bash deploy/deploy.sh root@IP domain` installs Caddy + the
review API (`review_api.py`, `review-api.service`, `Caddyfile`). Serve `$SAC_PAGES` (`edenvia/pages/`) on its own
handle, noindex, clean URLs, mobile OK. The founder gets two links per batch: comparison (template | ad) and demo.

## 5. Looms

`scripts/ingest_loom.sh` = yt-dlp on the Loom URL + transcription through the OpenAI API into `edenvia/feedback/`.
On the VPS nothing is blocked. If a Loom is private, the founder downloads the mp4 and drops it in Drive.
Tooling on nutraflow1 (2026-10-11): missing `yt-dlp`, `mr-transcribe`, python `openai`. Approved replacement: `pip install --user yt-dlp openai`
and a 20-line `scripts/transcribe.py` that calls the Whisper API (`audio.transcriptions`, model `whisper-1`) with the key file —
same output (a `.txt` transcript in `feedback/`), same step in `3-improve/feedback-loop.md`. Record it as a system rule when added.

## 6. What stays in the cloud session

Research tools (Brandsearch, Trendtrack, Konvert, Drive) are connected to the cloud session, not to the VPS.
Step 1 (market research) and the research half of step 2 (decoding) run there; their outputs are committed to
this repo (`edenvia/research/`, `edenvia/briefs/`) and pulled on the VPS. Generation, QC, pages and the review
loop run on the VPS.
