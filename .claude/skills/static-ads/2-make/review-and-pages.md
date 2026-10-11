# Review pages, numbering, sell versions, exports

The reviewer only ever sees pages. Pages decide whether a review is fast (one Loom, ad by ad, by number) or a mess.

## Numbering (never renumber)
- Templates are sorted by file name in `$SAC_BATCH/templates/`; **ad number = rank in that sorted list** (S1 = first file). Lint enforces it (D13).
  Wildhorn names were `MM-DD_cNNNN_Brand.ext` (e.g. `09-14_c0003_Mars-Men.png`), so the order is stable.
- The ad keeps its number for life: every try, every page, every Loom, every verdict uses it. Run 1 used `#1…#79` (mapping `batch-01/numbers.json`);
  the Sam batch used `S1…S83`. Use a fresh prefix per batch of templates (S, T, U…) so numbers never collide across batches.
- Output files: `out/<prefix>_NN_vK.png` — K = try number, 1-based, never reused. Try K on the page = file vK (`pages_common.outs_for` sorts by K).
  Side files (`_sd_vK` Seedream scenes, `_bg` canvases) never count as tries.
- Ask the reviewer to say the number out loud in the Loom ("S42…"); transcription garbles numbers — resolve them against the page order.

## The pages (scripts write to `$SAC_PAGES`)

| Page | Script | Shows | When |
|---|---|---|---|
| Review (`review.html`) | `build_sam.py` | Only ads NOT yet validated: template + every try (current highlighted) + why / DNA / scene & placement / texts + inventory + backend prompt; hit-rate table vs baseline | After each generation round — the link sent for the Loom |
| Final (`final.html`) | `build_samfinal.py` | Every ad: template + every try + **SELL VERSION** (orange frame) + `why`; stats | When the batch is complete or for an overview |
| Validated (`validated.html`) | `build_validated.py` | Images only: sell version of every ✅ ad, renumbered 01…N, no templates, no angle names | The shareable demo link (team, partner, media buyer) |
| All ads (`all-ads/index.html`) | `build_all.py "Run 1=/path" "Batch 2=/path"` | Several finished sets, images only | Portfolio of everything shipped |
| Rules (`lessons.html`) | `build_lessons.py` | 3-improve/rules.md (or a brand LESSONS.md via `SAC_RULES`) as tables | After every rule change |
| Comparison (blueprint step 4) | (brand-specific, e.g. `batch-01/build_pages.py`) | template left / our ad right, one pair per row, grouped by concept family, angle + headline under each pair | First batch of a new brand (R6) |

Review-page rules (D3 + Looms):
- Validated ads disappear from the review page ("remove the validated ones" — L4/L6). A row stays until its verdict starts with ✅.
- Show every version of a redone ad, oldest first, the first try included ("give me the example of the first generation so I see the improvement" — L2; "batch 1, 2, 3, 4… all the batches" — L3).
- Show the decode (why, DNA, scene, placement, text) and the pixel inventory under each ad, and the exact backend prompt in a collapsible block: the reviewer checks your reasoning, not only the image.
- Thumbnails are 900 px webp; every thumbnail links the full PNG (he zooms on logos and text).
- Mobile works (one column, horizontal strip of tries).

## Serving the pages (VPS conventions)
- One subdomain per site: `<name>.machineroom.app`, added as a `handle` INSIDE the `*.machineroom.app` wildcard block of the Caddyfile (never a top-level block — it would leak the name in Certificate Transparency logs).
- Every site carries `X-Robots-Tag "noindex, nofollow, noarchive, nosnippet"`; never `Disallow: /` in robots.txt.
- Static sites get clean URLs: `try_files {path} {path}.html` + the `.html → clean` 301 redirect. Always share `…/review`, never `…/review.html`.
- Before any Caddyfile edit: snapshot, diff directive counts (basic_auth, reverse_proxy, file_server, root), `caddy validate`, then reload.
- Wildhorn used `blueprint.machineroom.app` (`/srv/blueprint/`): `/sam` (review), `/sam-final`, `/wildhorn-ads` (validated), `/all-ads`, `/lessons`, `/protocols`.
  Those are the brand's live pages — this skill never writes there; point `SAC_PAGES` at a new folder per brand and wire it once.

## Verdict files
- `validated.json` — `{"num": "✅ Validated (first try)" | "✅ Validated (redo 1)" | "✅ Loom 4 (after fix)" | "❌ reason" | "⏳ To review"}`. Vocabulary: 3-improve/feedback-loop.md §2. Back it up before each rewrite.
- `sell_override.json` — `{"num": try_index}` (1-based). Default sell version = the latest try. Override whenever the reviewer prefers an earlier try
  (Wildhorn: `{"9": 1, "58": 1, "79": 1, "35": 2, "42": 1}`). A validated/overridden try is frozen: never regenerated (A20), and the latest verdict wins (A26).
- `rounds.json` (optional) — `{"num": rounds}` when the verdict text can't express the round count (S11 = 4).
- `calls.jsonl` — one line per engine call `{"num", "engine", "ok", "ts"}` written by srun.py. Calls made by hand (A25 steps, manual fixes) must be appended by hand.

## Sell version logic
```
sell_i = sell_override.get(num, len(tries))     # 1-based
sell   = tries[sell_i - 1]                      # copied to $SAC_BATCH/sell/<Prefix>_S<NN>.png
```
`build_validated.py` re-exports every sell version first (validated ones included), then copies the ✅ ones to `$SAC_BATCH/validated/<Prefix>_NN.png` in S order.

## Exports for the user
- Sell versions: `$SAC_BATCH/sell/` (one per ad, review state irrelevant) — what to launch.
- Validated set: `$SAC_BATCH/validated/` (✅ only, renumbered) — the deliverable.
- Getting files to the Mac: `rsync`/`scp` from the VPS into `~/Downloads/<Brand>-<Batch>/` (Wildhorn: `~/Downloads/Wildhorn-Sam-Batch` (83 sell), `~/Downloads/Wildhorn-Validated` (83)).
  Heavy media archives go to Backblaze B2 (`mr-archive push`), never left in `/root/workspace` long-term.

## What the reviewer receives after each round
1. The review link (only ads to review).
2. A table `ad → verdict last round → what changed now → rule applied`.
3. The stats line (first-try %, after-one-fix %, hit rate, generations/validated ad) — `stats.py`.
4. New rules added this round (IDs).
Nothing else. No victory lap.

## Page history (what the Wildhorn reviewer saw, and why the format ended where it did)
- Batch 01 → `/example` (blueprint Module 2) and `/before-after`: template | our ad, one pair per row, grouped by concept family, numbered #1–#79
  (`#adN` anchors). Rule R6 (side by side) and the numbering the reviewer used in every later Loom.
- Batch 02–04 → `/batch-02…04`: template | batch-01 version | current version, plus decode, feedback and prompt per ad. Loom 3: "show batch 1, 2, 3, 4 — all the batches" → every version.
- Batch 05+ → only the ads to review ("remove the validated ones"). Batch 07–09: template | B1 | B8 | B9.
- Sam batch → `/sam` (review, validated hidden, decode + inventory + backend prompt, hit-rate table vs run 1) and `/sam-final` (every try + SELL VERSION frame).
- Finished sets → `/wildhorn-ads` (validated, images only, the demo link) and `/all-ads` (run 1 + Sam batch).
- Rules → `/lessons` (rulebook table) and `/protocols` (protocol 0–4 + the feedback-loop log of every round, newest first).

## Comparison page and demo link (blueprint step 4, first batch of a new brand)
1. **Comparison**: for each creative, the template on the left and our ad on the right, grouped by concept family, with the angle and headline under each pair.
   One pair per row on desktop; stacked on mobile.
2. **Demo**: a grid with ONLY our final images — no templates, no concept or angle names, no technical text (for someone outside the team).
Both on the VPS (`<name>.machineroom.app`, noindex, clean URLs). `build_validated.py` produces the demo grid; the comparison page is a small brand-specific builder
(Wildhorn: `batch-01/build_pages.py`).

## Review tabs: validated ads move to a Validated tab; To review shows only non-validated; new versions side by side
(set up on the Oct 08 batch, 08/10 — reuse for every batch)
- One verdicts file per batch (`verdicts.json`): `{ "O01": {"status": "validated"|"redo"|"todo", "try": N, "note": "...", "loom": "...", "redo_from": N} }`, all start as `todo`.
- After each Loom, record verdicts with one command, which also rebuilds both pages and the ZIP:
  `python3 verdict.py O05=ok O06=redo:"note" O12=ok@2 --loom <url>` (ok = the try shown big; ok@N = that try; redo:"note" = the note shows above the next version; `--dry-run` to preview; `--file/--out/--zip` to test on a copy).
- Two pages, two tabs at the top ("To review (N)" / "Validated (N)"):
  - **To review** (`/<batch>`) = only `todo` + `redo` ads. Validated ads disappear from it.
  - **Validated** (`/<batch>-validated`) = only the validated try of each validated ad, big, simple grid with ID + angle, click → full-size PNG, plus "Download all validated (ZIP)".
- A `redo` ad that has a new try: the NEW try big with a "New version" badge and the Loom note above it, then the previous tries side by side right under it (same row, same size), then the template. A `redo` with no new try yet keeps a "Redo asked" badge + the note.
- Same image rules on both pages: first image eager + fetchpriority high + preload, all others lazy + async, webp q80 at 2× display, width/height set.
- Reference implementation: `/root/workspace/wh-remix/oct08/` (`build_oct08.py`, `verdict.py`, `oct08_state.py`, check `tabchk.js`).
