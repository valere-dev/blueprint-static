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
/root/workspace/blueprint-static. Read README.md, VPS-SETUP.md, edenvia/BRAND-KIT.md and
.claude/skills/static-ads/SKILL.md before anything else. Working folder for every batch:
SAC_WORKDIR=/root/workspace/blueprint-static/edenvia, SKILL=/root/workspace/blueprint-static/.claude/skills/static-ads.
Check that /etc/secrets/openai_api_key and /etc/secrets/kie_api_key exist (never print them).
Then tell me what is missing from the pre-flight checklist in $SKILL/2-make/first-batch.md §6.
```

## 2. Secrets (founder puts them on the VPS, never in a chat)

| File | Used by |
|---|---|
| `/etc/secrets/openai_api_key` | `scripts/remix.py`, `scripts/jarswap.py` (gpt-image-2), Loom transcription (Whisper API) |
| `/etc/secrets/kie_api_key` | `scripts/kie6.py` (Seedream fallback) |

`chmod 600`, owned or readable by `adanalysis`. The scripts read the path, not an env var (`OPENAI_KEY_FILE`, `KIE_KEY_FILE` in `scripts/sac_config.py`). Creating `/etc/secrets` needs root.

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
