# Edenvia batch 01 — QC log, round 1 (2026-10-11, before the founder's review)

Full-resolution QC of every try next to its template (2-make/qc-checklist.md). 10/10 generated on the first pass (7 openai, 3 seedream_comp).
Sell version = latest try of each ad (no sell_override yet). All verdicts ⏳ To review.

| Ad | Problem found | Fix applied | Rule |
|---|---|---|---|
| S1 | top crop of the 2:3 OpenAI canvas cut the badge and the first headline line (try 1 and try 2: the model ignored the LETTERBOX note) | try 2 finished from the uncropped master with `pad_fit.py` (navy extended on both sides, no crop) | D15 |
| S2 | logo spot left empty by the model as instructed | blue Edenvia wordmark pasted by script (try 2) | D19 |
| S4 | side crop cut the first/last letters of the body lines (try 1 and try 2) | try 2 finished from the master with `pad_fit.py` (background extended top/bottom) | D15 |
| S5 | AI-drawn pouch label garbled (no icon, blurred lines) | real cutout pasted over it by script (try 3; try 2 sat on the footer) | C6, golden rule 4 |
| S8 | top crop cut the first headline line; button touched the bottom edge (try 1) | regenerated with the LETTERBOX note → try 2 complete | D15 |
| S10 | side crop clipped 'PUFFY FACE STAYS'; pouch label without the Edenvia wordmark/icon (try 1) | regenerated with the label named element by element + `pad_fit.py` finish → try 2 | C6, D15 |
| S3 S6 S7 S9 | — | first try accepted | — |

Lesson (seen 4×): gpt-image-2 only renders 1:1, 2:3 or 3:2; a 4:5 / 3:4 / 9:16 ad must be finished from the 2:3 master by EXTENDING the
background (`batch/pad_fit.py`) when the smart crop would cut content — prompt-side margin notes are not obeyed. Added to rules.md under D15.
Calls: 14 OpenAI (≈ $4.20 at ~$0.30), 3 Seedream (15 kie credits), 4 script composites. Budget $30: ~$5 used.
