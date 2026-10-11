# Template pool — 319 statics (Adrien's 79 + 52 coded ads + 188 from the founder's Image_Ad_Concepts)

Source: Drive folder `192i8yNFlCZVnClzsIch_L3ZRvoAIjKMj` (Adrien's full swipe file). One folder per Adrien family (F1–F9).
- `F<n>_c<id>.webp` = Adrien's original 79 templates (Wildhorn ids), same as the previous zip.
- `NN_<CODE>_<id>_before.webp` = the 52 new ads, kept with their original Drive filenames, placed by code → family mapping below.
- Every other file (`IMG - …`, `BOF - …`, `Bundle Headline v(n)`, …) = the 188 ads of the founder's `Image_Ad_Concepts` (Top / Middle / Bottom of Funnel, 235 files, 47 byte-identical duplicates filed once), sorted with `sort-ad` on 2026-10-11 by looking at every image. Original filenames kept (several `.jpg` are really PNG or WEBP inside; PIL reads them). The reason for each placement is in the folder INDEX under "Image_Ad_Concepts".

## Code → family mapping used
- **UVT** → Us vs Them = F1 (sure)
- **BA** → Before/After = F2 (sure)
- **PS** → Problem/Solution = F3 (sure)
- **FB** → Feature/Benefit = F4 (probable)
- **OS** → Offer Stack = F6 (sure)
- **BC** → Bold Claim = F7 (sure)
- **MEME** → Meme = F8 (sure)
- **ST** → Stat = F7 (sure; one number + product hero)
- **NH** → Negative Hook = tone, no family of its own; sorted by the picture (verified one by one)

ST = Stat and NH = Negative Hook (verified on the images, not testimonial / native headline). Each new ad's line in the folder INDEX gives the reason. Sorting rules: .claude/skills/sort-ad in the repo.
Notes: c0325/c0330 and c0378/c0384 are byte-identical pairs in Adrien's library; all four are kept.

## Rules added for the Image_Ad_Concepts sort (now in `.claude/skills/sort-ad/SKILL.md`)
1. **Off-avatar wins over mechanic** — the promise belongs to another avatar/niche (acne, menopause, cellulite, women's hair, kids) → F9, with a **re-skin as F<n>** tag. A woman as model is not enough.
2. **Price vs badge** — strike-through price, price card or "buy 2 get 1" bar under the headline → F6; a corner roundel or a closing "47% off today" is a footer, the ad keeps its family.
3. **Native / advertorial** — classified by what the copy does (nearly all are reframes → F3).
4. **Names are hints only** — the image wins over the folder or file name.

## Folders (templates + 52 coded + 188 Image_Ad_Concepts)
- **F1_us-vs-them--comparison/** — 23 files (10 + 6 + 7)
- **F2_before-after--timeline/** — 23 files (8 + 10 + 5)
- **F3_problem-reframe-x-is-not-the-problem/** — 34 files (8 + 8 + 18)
- **F4_mechanism--anatomy--ingredients/** — 16 files (6 + 6 + 4, one missing, see below)
- **F5_origin--ranch--real-food/** — 8 files (8 + 0 + 0)
- **F6_offer--bundle--price/** — 53 files (11 + 6 + 36, one missing)
- **F7_bold-claim--hero-product/** — 72 files (9 + 13 + 50, one missing)
- **F8_meme--humor--ugc/** — 37 files (10 + 3 + 24)
- **F9_off-avatar-re-skin-last/** — 47 files (9 + 0 + 38, three missing) — by re-skin target: F8 ×17, F2 ×10, F7 ×8, F6 ×2, F3 ×2, F1 ×1, F4 ×1

Image_Ad_Concepts confidence: sure 65 · probable 121 · uncertain 2 (IMG4.jpg in F3, IMG - Authority - Expert Endorsement.jpg in F7).

## 6 files classified but not in the repo (over the Drive-tool size limit, 4.4–6.9 MB)
They are sorted in the INDEX ("FILE NOT IN REPO") and keep their place in the plan; pull them on the VPS with `gdown --id <id> -O "<folder>/<name>"` once the swipe-file folder is shared by link:
- F4 · `IMG - Mechanism Visualization.jpg` — 1j472ccJW_Lx61TNzv9zEvpC-9dfPU1RT
- F6 · `IMG - Offer Stack (3).jpg` — 1AHEF34G-TfqHhP0NWVaZnUXr_njZbE06
- F7 · `MOF - Drawing Benefits Claim.jpg` — 1nXXFcnbXgLl47U4-02z1EKEl2hndshjR
- F9 · `Sticker Face.png` — 1OM4quIxY0s6T2UGtKrUJyr_g4T6BL4kB
- F9 · `Do Not Buy if you want PROBLEM.png` — 1GjwlCH9wGBFG2EY6oaLllI88IcctoBku
- F9 · `Before After.jpg` — 1PSEuIqHeXE5QXwlO_8VDM8I8eaMEfDyL
Founder's Drive copy of the full sorted pool: folder `1djZbc2xfuVkLqpuXe2qi877LkkAysJ-5`.
