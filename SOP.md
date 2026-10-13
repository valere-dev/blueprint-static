# SOP — Edenvia static ads (state of the art, 2026-10-11)

This is THE process. It replaces the heavy skill pipeline in `.claude/skills/static-ads/` (kept for reference only: briefs, specs,
lint, OpenAI direct, cutout pasting are retired for generation — the founder dropped them on 2026-10-11, "ça va pas du tout").
Read this file, then `edenvia/batch/BRIEF-for-prompts.md`, then `edenvia/batch/pipeline2.py`. That is all a new session needs.

## 0. Where things are

| What | Path |
|---|---|
| Brand facts (prices, proof, avatar, bans, colours) | `edenvia/BRAND-KIT.md`, `edenvia/brand.json` (v1.6) |
| The brief the prompt-writer reads (product, avatar, tone, rival rule, offers) | `edenvia/batch/BRIEF-for-prompts.md` |
| The generator (analysis → prompt → validator → kie → vision QC) | `edenvia/batch/pipeline2.py` |
| Low-level kie call (one image, credits logged) | `edenvia/batch/kgen.py` |
| Founder's product photos (26) + cutouts + rival assets | `edenvia/assets/product/library/`, `…/cutouts/`, `…/rival/` |
| Official logo (blue, white, icon) | `edenvia/assets/logo/` |
| Template pool: all 311 swipe-file statics sorted in 9 families | `edenvia/batch/templates-pool/F1…F9/` (+ `templates-pool/README.md`) |
| Batches done: family 1 (S1–S10), batch T (25 random), batch U (the other 270) | `edenvia/batch/templates/`, `templates-T/`, `templates-U/` + `prompts/kie*/` |
| Every generated try (never deleted) | `edenvia/out/<prefix>_<num>_v<k>.png` (1080 wide); masters in `out/_raw/` |
| Founder verdicts | `edenvia/batch/validated.json` (S), `validated-U.json` (U) |
| Validated deliverable, batch U v1 (269 PNG) | `edenvia/batch/validated-U/Edenvia_U###.png` |
| Review pages (template | ad, and image-only demo) | `edenvia/pages/compare*.html`, `demo*.html`; builder `edenvia/batch/build_pages.py` |
| Logs of every call and QC verdict | `edenvia/batch/calls.jsonl`, `pipeline2.log.jsonl`, `qc-log-*.md`, `logs-*.txt` |
| Loom-2 lessons and the plan that followed | `edenvia/batch/PLAN-after-loom2.md` |
| Secrets (never in git, never in chat) | `~/.secrets/openai_api_key`, `~/.secrets/kie_api_key` on nutraflow1 |

Host: VPS `nutraflow1`, user `adanalysis` (no root), repo at `/home/adanalysis/workspace/blueprint-static`, push over the SSH deploy key.
`export SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia` before any script.

## 1. The process, one ad = one kie call

1. **Analyse the template** (vision LLM inside `pipeline2.py`): format, family, mechanism, and the ROLE of each zone (rival / ours, before / after, pain / desire).
2. **Write one short prompt** (JSON: template_lines, our_lines, prompt, needs_rival). Every text line rewritten for the avatar.
3. **Validate the text** (free): no line identical to the template, no word of another niche, only allowed prices/percentages, no discount code, year 2026, only hydrogen / magnesium / minerals as ingredients.
4. **Generate on kie.ai** with `gpt-image-2-image-to-image` (6 credits ≈ $0.03), references = template + studio pouch + official logo (+ rival asset on comparison templates), the template's own ratio. Nano Banana Pro (18 credits) when GPT refuses; Seedream (6) last resort.
5. **Vision QC** of the image (pouch is the studio one, no foreign logo, Edenvia never on the losing side, text on-niche, anatomy, nothing cut) → automatic redo, 2 tries max, then flagged for a human.
6. **Pages** (`build_pages.py` with `SAC_KEY_PREFIX=s|t|u`) → publish → founder reviews by number (Loom or written) → verdicts into `validated*.json` → every complaint becomes a line in the BRIEF or in the SYS/QC prompts of `pipeline2.py`.

Commands:
```
export SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia
python3 edenvia/batch/pipeline2.py 12 20 45 --force      # (re)generate these template numbers of batch U
python3 edenvia/batch/pipeline2.py --qc 102 103 104      # vision QC only
SAC_KEY_PREFIX=u python3 edenvia/batch/build_pages.py    # pages/compare-U.html + demo-U.html
```
For a NEW batch: copy the templates into `batch/templates-<X>/` as `X###_F<family>_<name>.<real ext>`, adapt the `tfile()` / prefix in `pipeline2.py` (today hard-wired to batch U), run.

## 2. Rules learned from the founder (never regress)

From Loom 1 (family 1): the product must come from the founder's photo library, lit by the scene — never a flat cutout pasted on; the offer slot keeps the template's mechanic (a % stays a %: "-50%", not "$39").
From Loom 2 (batch U, 65 % first try → the 6 fixes in `PLAN-after-loom2.md`):
1. Comparison templates: the losing side shows a generic rival + what she suffers; Edenvia + what she wants on the winning side. Never Edenvia on both sides.
2. The pouch is only the studio photo; the logo is only the official file. Never an invented badge.
3. Every text line is rewritten for the avatar; no template line survives, no other-niche word.
4. Sell, don't describe: action verbs, urgency, the avatar's desire; benefit list ≥ the template's.
5. Offers only from `prices_allowed`; a discount code becomes a discount, a price or a benefit.
6. Ingredients: only hydrogen, magnesium, minerals.
Rival naming (founder, same day): **"Average + angle + form"** — "AVERAGE DEBLOAT PILLS" on the bloating/legs angle, "AVERAGE DE-PUFF PILLS" on the face angle, etc. Never "water pills", "classic" or "generic".
Compliance: set aside by the founder for now (copy the swipe file's level of claim); invented testimonials and percentages allowed; still never a competitor name, a disease or drug name, a capsule/pill/powder for Edenvia.

## 3. Costs (measured)

| Item | Cost |
|---|---|
| gpt-image-2 on kie | 6 credits ≈ $0.03 per image (OpenAI direct was 6–8× more: never again for generation) |
| Nano Banana Pro on kie | 18 credits; Seedream 6 |
| Prompt + QC tokens (gpt-5.4-mini) | ≈ $0.01 per ad |
| Family 1 (10) | $0.30 · Batch T (25) ≈ $1 · Batch U (270, two rounds) ≈ $11 |
| Throughput | 20 calls in parallel ≈ 270 ads in 40 min |

## 4. State on 2026-10-11 (end of day)

- Family 1 S1–S10: round 3 (kie) generated; founder validated the batch-T/U style, S not re-reviewed since.
- Batch T (25 random): generated, not reviewed.
- Batch U (270): round 2 done, **validated v1 by the founder** (269 ads, U249 refused by both engines). Deliverable in `batch/validated-U/`.
- kie balance ≈ 7,500 credits (subscription). OpenAI key used only for prompts/QC/Whisper.
- Next candidates: a second avatar (puffy face or man's belly) over the same pool with the "Average + angle" rival; or the two-step pouch-label check tightened (the QC let a wrong pouch pass once: U12 v1).

## 5. Bootstrap prompt for the next session

```
Clone / pull https://github.com/valere-dev/blueprint-static (branch claude/friendly-bell-v79g1w) into
/home/adanalysis/workspace/blueprint-static. Read SOP.md, edenvia/batch/BRIEF-for-prompts.md and edenvia/batch/pipeline2.py.
export SAC_WORKDIR=/home/adanalysis/workspace/blueprint-static/edenvia. Keys are in ~/.secrets (never print them).
Then: <the task>.
```
