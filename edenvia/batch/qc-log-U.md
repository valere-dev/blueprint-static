# Batch U — 270 templates (the whole remaining swipe file), 2026-10-11

Pipeline: prompts written by a vision LLM (gpt-5.4-mini, `write_prompts.py`, brief in `BRIEF-for-prompts.md`), ONE kie gpt-image-2 call each (`kgen.py`), 20 in parallel, 3 passes.
Result: 269/270 generated (U249 refused by both gpt-image-2 and Nano Banana: the template is a bare-chest ad). 3 refusals rescued with Nano Banana Pro (U066 U205 U265).
Cost: 295 kie calls ≈ 1,650 credits ≈ $8. Wall clock ≈ 40 min.

Flagged for a second pass (the prompt writer kept the template's copy or invented numbers) — not yet redone:
- off-avatar copy left in: U027 (vapes/porn list), U060 (sugar/fiber), U080 (snack, grass-fed), U109 (ponytail), U122 (0g sugar), U131 (sunscreen), U185 (parasites), U200 (mental focus), U203 (toned), U235 (acne), U242 (sugar-free tone), U246 (kids bedtime), U261 (acne under 30), U264 (weight gain), U071 (invented ingredient list)
- offer not in prices_allowed: U003 (70%), U086 (70%), U087 (65%), U090 ($20), U083 (45%), U099/U100/U101/U103 (40%), U106 ($19.50), U111 ($74), U124 (70%), U108/U269 (30%), U233 (35%), U156 (20%), U258 (61%), U176 (100-day trial), U191/U192 (60-day returns)
- authority claims the founder may not want: U010 (clinically proven), U053 (Harvard), U162 (Oxford doctor), U187 (Big Pharma)
- blank/wrong pouch: U012, U032, U095, U116, U125, U159, U164, U244
Everything else accepted as generated. Sell = v1.
