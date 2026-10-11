# Batch U — round 2 (pipeline v2 after Loom 2), 2026-10-11

Loom 2 (U1–U101): 66 ✅ first try (65 %), 35 ❌. Verdicts in `validated-U.json`. Plan: `PLAN-after-loom2.md`.
Pipeline v2 (`pipeline2.py`): analysis with zone roles → JSON prompt → text validator (unchanged lines, other-niche words, prices, codes, year)
→ kie gpt-image-2 with 3–4 refs (template, studio pouch, official logo, rival asset) → vision QC → up to 2 tries.
Rival assets generated once: `assets/product/rival/{pills,gummies,drops}.png`.

- 35 founder-rejected redone: 30 pass the QC on try 1–2; flagged after 2 tries: U021 U062 U069 (logo/pouch nitpicks, to eyeball); U095 failed (kie 500).
- 168 unreviewed (U102–U270) passed through the QC: 119 pass, 49 rejected → regenerated: 42 pass; still flagged: U182 U225 U235 U240 U255 U261
  (templates whose own niche — acne, skin, HRT belly — the model keeps copying).
Cost of round 2: ≈ 108 kie calls ≈ 650 credits (≈ $3.25) + ≈ $2 of prompt/QC tokens. Credits left: 7,491.
