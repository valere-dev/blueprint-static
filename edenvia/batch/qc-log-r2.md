# Edenvia batch 01 — QC log, round 2 (2026-10-11, after Loom 1: product from the library, C23)

Scope (VPS-SETUP §3c): every validated layout kept pixel for pixel (D21); only the product placement redone from the founder's photo library;
S2's offer button → "-50%" (B23). S4 untouched (no product in the template, C7). All by script except one masked edit (S8).

Library: 26 photos (12 fetched on the VPS with gdown, described in `assets/product/library/INDEX.md`). Cutouts built with BiRefNet
(`assets/product/cutouts/make_cutouts.py`): `pouch-standing-studio.png` (front-on, droplets, now brand.json `product_cutout`),
`pouch-held-hand-kitchen.png` (pouch + real hand), `tablets-flatlay.png`.

| Ad | Try | Product placement | QC |
|---|---|---|---|
| S1 | v5 | studio pouch at the old pouch's footprint in the gold column; old pouch area filled row-wise from the frame glow | v3 too big (covered the EDENVIA label), v4 flat fill showed as a box → v5 |
| S2 | v3 | unchanged (no product); button "FLAT 20% OFF" slot → "-50%" (B23) | OK |
| S3 | v2 | studio pouch under the headline, 40 % of the half, bigger than the AI one | OK |
| S4 | v2 | — (no product, C7) | unchanged |
| S5 | v4 | studio pouch between the two diagrams | OK |
| S6 | v2 | studio pouch floating top-left, graded darker (brightness 0.86) for the night scene | OK |
| S7 | v2 | studio pouch on the empty right half | OK |
| S8 | v4 | old AI pouch removed by a masked gpt-image-2 edit (empty counter), then the studio pouch + the fizzing glass kept | v3 (counter strip copied) showed a seam → v4 |
| S9 | v2 | studio pouch bottom right over the split | OK |
| S10 | v5 | masked gpt-image-2 edit of the pouch box with the library pouch as reference: ink-style pouch, label complete, her illustrated hands kept | v3 (photo hand cutout on an ink drawing) clashed, v4 (studio cutout + fingers re-overlaid) showed a flat box → v5 |

Open for the founder (C23 vs A8/C5 on illustrated templates): on S10 the pouch is drawn in the template's ink style from the library photo rather than
pasted as a photo — a photo hand on a drawing read as a sticker (v3). Say if the photo cutout is wanted there anyway.

Round-2 cost: 2 OpenAI masked edits (≈ $0.60 at ~$0.30 each), 0 Seedream, 13 script composites (free).
Batch 01 total so far: 16 OpenAI calls ≈ $4.80 + 15 kie credits. Budget $30 per round: round 2 used ≈ $0.60.
