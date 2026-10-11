# Edenvia — round 1, concept family 1 "US vs THEM" (S1–S10). 2026-10-11.
# Drafted by brief2spec.py from edenvia/briefs/EDENVIA_B01_C*.json (cloud session), then rewritten by hand on the VPS:
# `visual` as one scene per ad, `dna` filled, engine per production method (§3b: c0196 photo → scene + real product + script text,
# c0310 meme → minimal edit of the template + text by script; c0233 flat-lay photo → scene + real pouch by script), composite recipes
# with every placement (D6), crop margins for the 2:3 OpenAI canvas (D15: 4:5 / 3:4 / 9:16 are cropped from 1024x1536).
# Inventories are the briefs' (A13). Lint: python3 $SKILL/scripts/lint.py $SAC_BATCH/s1specs.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from constants_a8 import OLD_L, OLD_F, OLD_M, TABLET, GLASS, POUCH, STD

ROOT = "/home/adanalysis/workspace/blueprint-static/edenvia"
T = ROOT + "/batch/templates/"            # the family's templates (cloud session names) = the briefs' paths = the gate-2 page
TF = ROOT + "/batch/templates-pool-full/"  # full-size twins of the same templates (Image 2 at full resolution where the thumb is small)
LOGO_BLUE = ROOT + "/assets/logo/edenvia-logo-blue-nobg.png"   # D19: pasted by script on light backgrounds

# D15 crop margins: OpenAI renders 1024x1536 (2:3) for every portrait format; adformat then crops to the template's ratio.
M45 = (" FRAMING: the canvas is 2:3 but the ad is 4:5 — keep the top 8% and the bottom 8% of the canvas as plain empty background "
       "(no text, no element there); everything sits in the middle 84%.")
M34 = (" FRAMING: the canvas is 2:3 but the ad is 3:4 — keep the top 6% and the bottom 6% of the canvas as plain empty background; "
       "everything sits in the middle 88%.")
TRUTH = " Product truth: one effervescent tablet dropped in a glass of clear water, never hot water."
M916 = (" FRAMING: the canvas is 2:3 but the ad is a 9:16 Story — keep the left 8% and the right 8% of the canvas as plain background "
        "of the same colour as the area next to it (no text, no element there); everything sits inside the central 84% of the width.")

S = [
# ---------------------------------------------------------------------------------------------------------------------------- S1
# compliance (deferred by the founder 2026-10-11): 'HEAVY LEGS GONE IN 30 DAYS' (template carries the deadline, B6); '2026 INDEPENDENT TEST' (invented proof allowed).
{'num': 1, 'tpl_abs': T + '10-11_c0021_PrimalEdgeBison.webp',
 'angle': "A8 A8-L heavy, swollen legs that diets never fixed — 'it was never fat'",
 'why': "A fake 'independent test' table where three rival products are graded row by row and the third column glows gold as the only winner — "
        "the buyer reads the verdict before she reads the ad. Authority by layout: badge + grid + star ratings read as a lab report. "
        "Visual trick to copy literally: the glowing gold third column and the red → orange → green verdict words.",
 'dna': "Their three bottles (two rival organ supplements + Primal Edge Bison) → two generic things she already tried (a white 'WATER TABLETS' pill "
        "bottle, a brown 'LYMPH DROPS' dropper bottle) + the Edenvia pouch; their rows (Source/Origin/Organs/Filler/Testicle) → our rows "
        "(Form/Works on/Per day/Reaches the tissue/Hydrogen); 'beer belly' → 'heavy legs'; bison emoji → water drop.",
 'scene': "no scene — a product grid; ours is the same grid with the three things she already tried against her swollen legs: water-tablet "
          "diuretics, herbal drainage drops, Edenvia",
 'placement': "same spots; pouch in column 3 at the same height as the two rival bottles — like the template",
 'inventory': ["KEEP badge: '2026 INDEPENDENT TEST' red/white badge top (template device; invented proof allowed (founder override 2026-10-11))",
               "SWAP headline: '3 Organ Supplements. 1 Beer Belly. Here's The Truth.' white serif, 2 lines → '3 Leg-Swelling Fixes. 1 Pair Of Heavy Legs. "
               "Here's The Truth.' (copy formula: [3 rivals]. [1 problem]. Here's The Truth — problem named in full (B2))",
               "SWAP column_1: Ancestral Supplements black bottle → a white plastic diuretic bottle labelled 'WATER TABLETS' (generic, no brand) (rival #1 = "
               "what she tried; no competitor name)",
               "SWAP column_2: Primal Viking amber bottle → a brown dropper bottle labelled 'LYMPH DROPS' (generic) (rival #2 = the competitor's herbal "
               "drainage drops, unnamed)",
               "SWAP column_3: Primal Edge Bison bottle in gold frame → the EDENVIA pouch of Image 1 in the gold frame (product_spot: the winner column)",
               "KEEP product_spot: three products at the top of each column, ~60 % column width (placement (A8))",
               "SWAP rows: Source / Origin / Organs / Filler / Testicle → Form / Works on / Per day / Reaches the tissue / Hydrogen (same 5-row grid, our "
               "facts; the last row is the ✓/✗ row like 'Testicle')",
               "SWAP result_row: 'Result After 90 Days:' + GUT UNCHANGED / MINOR ENERGY ONLY / GUT FLATTENING → 'Result After 30 Days:' + STILL SWOLLEN / "
               "SLIGHTLY LESS PUFFY / LEGS FEEL LIGHT (same colours red / orange / green; 30 days = our supply)",
               "KEEP rating_row: ★★ Would Not Recommend / ★★★ Overhyped / ★★★★★ Editor's Choice ✓ (already works for our buyer)",
               "SWAP bottom_banner: 'BEER BELLY GONE IN 21 DAYS. 60-DAY GUARANTEE 🦬👇' → 'HEAVY LEGS GONE IN 30 DAYS. 30-DAY MONEY-BACK 💧👇' (template carries a "
               "deadline so ours may (B6); our real guarantee; bison emoji → water drop)",
               "KEEP background: dark navy #0b1b2b, thin column dividers (render style)",
               "KEEP logo: none (template has no logo slot)"],
 'visual': ("Dark navy (#0b1b2b) flat comparison layout, exactly the template's grid: a small red-and-white badge top centre, a two-line white serif "
            "headline, then three columns separated by thin dividers, each with a product photo at the top (about 60% of the column width, soft drop "
            "shadow), five bold-label rows, a 'Result After 30 Days:' line with one big verdict word, and a star-rating line; the third column framed "
            "in a glowing gold rounded border; a gold banner strip across the bottom. Column 1 product: a plain white plastic bottle whose label "
            "reads only WATER TABLETS (generic, no brand). Column 2 product: a plain brown glass dropper bottle whose label reads only LYMPH DROPS "
            "(generic). Column 3 product: " + POUCH + ", the same height as the two bottles, label to camera. Verdict words: column 1 red, column 2 "
            "orange, column 3 green, like the template. No person. Do NOT draw: no bison, no organs, no other dosage form in any column; no real brand "
            "on the rival bottles; no bottle, jar or tub for Edenvia; no glass." + M45),
 'texts': ['Badge: "2026 INDEPENDENT TEST"',
           'Headline: "3 Leg-Swelling Fixes. 1 Pair Of Heavy Legs. Here\'s The Truth."',
           'Col1_label: "WATER TABLETS"',
           'Col1_rows: "Form: 2 tablets, swallowed / Works on: water only / Per day: 2 + bathroom runs / Reaches the tissue: No ❌ / Hydrogen: None ❌"',
           'Col1_result: "Result After 30 Days: STILL SWOLLEN"',
           'Col1_rating: "★★ — Would Not Recommend"',
           'Col2_label: "LYMPH DROPS"',
           'Col2_rows: "Form: 20 drops in water / Works on: herbs, \'drainage\' / Per day: 2 doses, bitter / Reaches the tissue: Barely ❌ / Hydrogen: None ❌"',
           'Col2_result: "Result After 30 Days: SLIGHTLY LESS PUFFY"',
           'Col2_rating: "★★★ — Overhyped"',
           'Col3_label: "EDENVIA"',
           'Col3_rows: "Form: 1 tablet in a glass of water / Works on: the inflamed tissue holding the fluid / Per day: 1 glass, 3 minutes / Reaches the '
           'tissue: Yes — smallest molecule ✅ / Hydrogen: 8 PPM ✅"',
           'Col3_result: "Result After 30 Days: LEGS FEEL LIGHT"',
           'Col3_rating: "★★★★★ — Editor\'s Choice ✅"',
           'Bottom_banner: "HEAVY LEGS GONE IN 30 DAYS. 30-DAY MONEY-BACK 💧👇"'],
 'engine': 'openai', 'fallback': 'none', 'aspect': 'portrait_4_3', 'template_has_deadline': True},

# ---------------------------------------------------------------------------------------------------------------------------- S2
# Logo slot (bottom centre 'mars' wordmark): left EMPTY by the model (lock_extra), the blue Edenvia wordmark is pasted by script after QC (D19).
{'num': 2, 'tpl_abs': TF + '10-11_02_c0138_Blueprint.png',
 'angle': "A8 A8-L heavy, swollen legs — 'lose the fluid, not more weight'",
 'why': "The same limb cut open twice: on the left the cross-section is packed with yellow fat around a shrunken muscle, on the right it is lean muscle — "
        "the buyer sees inside her own body; the authority of a textbook drawing. Visual trick to copy literally: two cross-sections side by side with "
        "a thin vertical divider, the 'bad' tissue lumpy and pale, the 'good' tissue clean red/pink — same pose, same cut line.",
 'dna': "upper arm bent at the elbow → a woman's lower leg from knee to foot, cut lengthwise (her problem lives in the calf and ankle); yellow fat "
        "globules → pale water-logged tissue with yellowish fluid pockets (fluid, not fat); 'Men on …' → 'Women on …'; 'Lose Fat, Not Definition' → "
        "'Lose The Fluid, Not More Weight'; 'FLAT 20% OFF' → 'NOW $39.00'; 'mars' wordmark → Edenvia wordmark pasted by script.",
 'scene': "no scene; a medical plate on a beige page — ours is the same plate, lower leg instead of upper arm, because her problem is inside the calf and ankle",
 'placement': "none — the template has no product — like the template",
 'inventory': ["SWAP header_left: 'Men on Other brands' → 'Women on other brands' (template words kept, gender swapped (A19))",
               "SWAP header_right: 'Men on Mars Vitasteron' → 'Women on Edenvia' (brand slot)",
               "SWAP body_part: upper arm, bent at the elbow, cut lengthwise → lower leg from knee to foot, cut lengthwise, foot at the bottom (their body "
               "part = their problem; ours = the calf and ankle (C1))",
               "SWAP left_tissue: yellow fat globules crowding a small red muscle → pale water-logged tissue with yellowish fluid pockets swelling the calf "
               "outward, skin stretched, ankle thick (the invisible made visible (C2): fluid, not fat)",
               "KEEP right_tissue: full red muscle, thin fat layer (before/after stays before/after)",
               "KEEP divider: thin vertical black line (structure)",
               "SWAP tagline: 'Lose Fat, Not Definition.' → 'Lose The Fluid, Not More Weight.' (copy formula 'Lose X, Not Y'; her failed solution = losing weight)",
               "SWAP button: black rounded button 'FLAT 20% OFF' → black rounded button 'NOW $39.00' (our offer framing; $39.00 is in prices_allowed)",
               "SWAP logo: 'mars' wordmark small bottom centre → Edenvia wordmark (blue, light_bg file), same size, pasted by script (brand slot (D19))",
               "KEEP footnote: '*Results may vary' grey bottom right (template words kept)",
               "KEEP product_spot: none (C6: no product added)",
               "KEEP background: warm beige (render style)"],
 'visual': ("Flat medical illustration on a warm beige (#f3efe9) page, NOT photoreal, exactly the template's layout: two bold black headers top left and "
            "top right, a thin vertical black divider down the middle, two cut-open limbs facing each other, an italic-accented tagline centred under "
            "them, a black rounded button, a tiny grey footnote bottom right. The limb is a woman's LOWER LEG from the knee to the foot, seen from the "
            "side, cut lengthwise: LEFT the leg swollen and thick at the calf and ankle, skin stretched, the tissue under the skin pale and water-logged "
            "with yellowish fluid pockets crowding a small muscle; RIGHT the same leg slim, skin close to a full red-pink muscle, a thin clean fat layer, "
            "the ankle defined. Same pose, same cut line, same soft pastel rendering with no outlines. The bottom-centre logo spot stays EMPTY plain "
            "beige. Do NOT draw: no arm, no elbow, no muscle-building reading, no veins drawn as a disease, no red inflamed skin; NO product, no pouch, "
            "no glass (the template has none)."),
 'texts': ['Header_left: "Women on other brands"', 'Header_right: "Women on Edenvia"', 'Tagline: "Lose The Fluid, Not More Weight."',
           'Button: "NOW $39.00"', 'Footnote: "*Results may vary"'],
 'engine': 'openai', 'fallback': 'none'},

# ---------------------------------------------------------------------------------------------------------------------------- S3
{'num': 3, 'tpl_abs': TF + '10-11_03_c0178_Blueprint.jpg',
 'angle': "A8 A8-L heavy, swollen legs — the detox tea only flushes water for a few hours",
 'why': "The brand's bottle faces the everyday thing the buyer already uses (coffee) with a VS badge between them, and the two columns of green ticks "
        "vs red crosses settle the fight before she reads a word; the familiar object becomes the loser. Visual trick to copy literally: cut-out product "
        "left on the brand-colour half, cut-out everyday object right on a grey half, big VS circle on the divider.",
 'dna': "green brand half → Edenvia blue gradient; Alevia AMLA bottle → the Edenvia pouch; coffee cup → the same white cup holding 'detox tea' with a "
        "DETOX teabag tag (cup ↔ cup); 'Alevia's AMLA' → 'Edenvia's HYDROGEN'; 'Coffee' → 'Detox Tea'; energy ticks/crosses → leg-swelling ticks/crosses.",
 'scene': "no scene; a split page. Ours: the Edenvia pouch vs the cup of 'detox tea' she drinks for her swollen legs — the same cup shape, same place",
 'placement': "Edenvia pouch from Image 1, same spot and size as the Alevia bottle (left half, under the headline, ~40 % of the half) — like the template",
 'inventory': ["SWAP left_half_colour: green gradient → Edenvia accent blue gradient #1468DB → #14488F (brand colour slot)",
               "SWAP headline_left: 'Alevia's AMLA' white, 2 lines → 'Edenvia's HYDROGEN' (copy formula [Brand]'s [INGREDIENT])",
               "KEEP vs_badge: black circle 'VS' (structure)",
               "SWAP headline_right: 'Coffee' black → 'Detox Tea' (the rival habit she already knows (A31))",
               "SWAP product_spot: Alevia bottle left, ~40 % width, centred under the headline → the EDENVIA pouch, same spot and size (placement)",
               "SWAP rival_object: white coffee cup on saucer, steam → the same white cup on a saucer, pale yellow-green tea, a teabag tag hanging over the "
               "rim reading 'DETOX' (shape equivalent: cup ↔ cup)",
               "SWAP tick_list: 5 green ✅ benefit lines → 5 lines in our words (see slots) (same count, same hierarchy)",
               "SWAP cross_list: 5 red ❌ lines → 5 lines in our words (same count)",
               "KEEP logo: none beyond the product label (template has no logo slot)"],
 'visual': ("Flat split poster exactly like the template: LEFT half an Edenvia blue vertical gradient (#1468DB at the top to #14488F at the bottom), "
            "RIGHT half light grey; a black circle with VS sitting on the centre line at headline height. Left: a two-line white rounded bold headline, "
            "under it " + POUCH + " standing upright, about 40% of the half's width, soft shadow, label to camera. Right: the black headline, under it "
            "a plain white cup on a white saucer at the same size and spot as the template's coffee cup, filled with pale yellow-green tea, a small paper "
            "teabag tag hanging over the rim that reads DETOX. Below each: five lines, green ✅ ticks on the left, red ❌ crosses on the right, regular "
            "sans, same size and spacing as the template. No person. Do NOT draw: no coffee, no brand on the cup, no second product, no glass."),
 'texts': ['Headline_left: "Edenvia\'s HYDROGEN"', 'Vs_badge: "VS"', 'Headline_right: "Detox Tea"',
           'Tick_1: "Reaches the fluid stuck in your legs"', 'Tick_2: "No bathroom runs every hour"', 'Tick_3: "Legs feel lighter by evening"',
           'Tick_4: "No swelling bounce-back tomorrow"', 'Tick_5: "One tablet, one glass of water"',
           'Cross_1: "Only flushes water for a few hours"', 'Cross_2: "Keeps you up for the bathroom"', 'Cross_3: "Legs heavy again by noon"',
           'Cross_4: "Washes out minerals, not the puffiness"', 'Cross_5: "Only a temporary flush"'],
 'engine': 'openai', 'fallback': 'none'},

# ---------------------------------------------------------------------------------------------------------------------------- S4
# compliance (deferred): 'Puffiness: GONE' (template formula).
{'num': 4, 'tpl_abs': TF + '10-11_04_c0183_Blueprint.png',
 'angle': "A8 A8-L heavy, swollen legs — another diet vs one tablet in a glass of water",
 'why': "A Pixar woman drawn twice — miserable in grey sweats on a black half, glowing in a white blouse on a purple half — with the rival's name spelled "
        "in leet so it reads as a secret ('OZ3MP!C'): the buyer feels let in on something; the sad character wears what she wears when she has given up. "
        "Visual trick to copy literally: the same character, two emotional states, leet-spelled rival name — ours 'ANOTHER D!ET'.",
 'dna': "Pixar woman ~30 in sweatpants (hides nothing: their problem is appetite) → the same Pixar woman at 45–50 in capri leggings so the swollen calves "
        "and thick ankles show; pencil skirt → knee-length skirt with slim calves on show; 'OZ3MP!C' → 'ANOTHER D!ET'; 'BIOMA' → 'EDENVIA'; purple → "
        "Edenvia blue; needles/food-noise lines → heavy-legs lines.",
 'scene': "no scene, studio gradient; ours keeps the split and the two characters, legs visible because the problem lives there",
 'placement': "none — like the template",
 'inventory': ["SWAP person_left: Pixar woman ~30, long dark hair, grey T-shirt and grey sweatpants, sad → Pixar woman 45–50, same face as the right one, "
               "hair tied back, grey T-shirt and grey capri leggings so the swollen calves and thick ankles show, sad, standing heavy (avatar age + body "
               "part visible (A11, C1))",
               "SWAP person_right: Pixar woman, white blouse, black pencil skirt, smiling → the same woman, white blouse, knee-length skirt, slim calves and "
               "ankles, heeled sandals, smiling (before/after stays before/after; proud proof = legs in the open)",
               "SWAP header_left: 'What comes with' + 'OZ3MP!C' leet → 'What comes with' + 'ANOTHER D!ET' (the leet trick kept on our rival (A21))",
               "SWAP header_right: 'What comes with' + 'BIOMA' → 'What comes with' + 'EDENVIA' (brand slot)",
               "SWAP left_lines: 4 lines: needles, side effects, bill, weight comes back → 4 lines in our words (same count, same rhythm)",
               "SWAP right_lines: 4 lines: '2 … a day' / Food noise: GONE / Flatter belly, less bloat / 'Lost 24 lbs!' → 4 lines: 1 tablet in a glass of water "
               "/ Puffiness: GONE / Lighter legs, slimmer ankles / 'My boots zip again!' (same formula incl. 'X: GONE' and the quoted proof line)",
               "SWAP background: black left, purple gradient right → black left, Edenvia blue gradient right (#1468DB → #0A1327) (brand colour slot)",
               "KEEP product_spot: none (C6: template has no product)",
               "KEEP logo: none (no logo slot)"],
 'visual': ("Pixar-style 3D render, big expressive eyes, soft studio light, NOT photoreal, exactly the template's split: LEFT half black studio fading to "
            "grey at the floor, RIGHT half an Edenvia blue gradient (#1468DB fading down to #0A1327). The same woman twice, standing full length, feet in "
            "frame: LEFT a woman of 45–50 with a soft midlife build, hair tied back, grey T-shirt and grey capri leggings so her visibly swollen, heavy "
            "calves and thick puffy ankles show, standing heavy, sad; RIGHT the same face and hair, a white blouse and a knee-length black skirt, slim "
            "calves and defined ankles, heeled sandals, smiling. Headers above each character: 'What comes with' in white rounded bold, under it the "
            "rival/brand name in a chunky cartoon display font with a dark outline; four short white lines beside the legs on each side with a soft "
            "shadow. NO product (the template has none). Do NOT draw: no needles, no drug imagery, no young slim character on the left (same "
            "45-year-old face on both sides), no belly focus — the legs are the subject; do NOT copy the template's person." + M916),
 'texts': ['Header_left_1: "What comes with"', 'Header_left_2: "ANOTHER D!ET"',
           'Left_1: "Hungry all day"', 'Left_2: "Legs still heavy by 5 p.m."', 'Left_3: "Scale moves, swelling doesn\'t"', 'Left_4: "Puffiness back the week you stop"',
           'Header_right_1: "What comes with"', 'Header_right_2: "EDENVIA"',
           'Right_1: "1 tablet in a glass of water"', 'Right_2: "Puffiness: GONE"', 'Right_3: "Lighter legs, slimmer ankles"', 'Right_4: "“My boots zip again!”"'],
 'engine': 'openai', 'fallback': 'none', 'aspect': 'portrait_16_9'},

# ---------------------------------------------------------------------------------------------------------------------------- S5
# compliance (deferred): 'BLOCKED DRAINAGE / CLEAR DRAINAGE' ('lymphatic drainage support' wording the brand prints).
# The brief flags A25 (photo + pasted product); the template is a coloured-pencil ILLUSTRATION with a pasted render → first try by regeneration (openai),
# A25 (Seedream edit of the template + jarswap + script text) is the fix path if two regenerations fail.
{'num': 5, 'tpl_abs': TF + '10-11_05_c0192_Blueprint.png',
 'angle': "A8 A8-L heavy, swollen legs — look at what's holding the fluid",
 'why': "A blunt three-line question in black condensed caps over two cut-open tubes, one clogged, one clear, with the product standing between them as "
        "the switch. Visual trick to copy literally: two diagonal cut-open tubes mirrored left/right, left narrowed and clogged with a small arrow, "
        "right wide and clear with a big arrow; thin callout lines with small labels; the product centred at the bottom under a long thin line.",
 'dna': "artery with yellow plaque and red blood cells → the drainage vessel of a lower leg squeezed by swollen, water-logged tissue; 'blood flow' → "
        "'drainage'; 'prediabetic men / can't stay hard' → 'dieted for years / legs still swollen'; 'ER3CT!ONS' → 'light, slim legs'; Primal Storm tub → "
        "the Edenvia pouch.",
 'scene': "no scene; a diagram on cream paper. Ours: the same diagram, the vessel that drains the leg instead of an artery, because her problem is fluid "
          "that stopped moving",
 'placement': "Edenvia pouch from Image 1, same spot and size as the tub: centred at the bottom between the two diagrams, the thin line above it — like the template",
 'inventory': ["SWAP headline: 'PREDIABETIC MEN: CAN'T STAY HARD? LOOK AT YOUR BLOOD FLOW.' 3 lines → 'DIETED FOR YEARS: LEGS STILL SWOLLEN? LOOK AT YOUR "
               "DRAINAGE.' 3 lines (copy formula [who]: [problem?] LOOK AT YOUR [mechanism]; problem named in full (B2))",
               "SWAP panel_label_left: 'WEAK BLOOD-FLOW' → 'BLOCKED DRAINAGE' (mechanism noun swap)",
               "SWAP panel_label_right: 'STRONGER BLOOD-FLOW' → 'CLEAR DRAINAGE' (mechanism noun swap)",
               "SWAP left_diagram: narrowed artery, yellow plaque, red cells squeezed, small arrow → drainage vessel squeezed by swollen pale tissue, stagnant "
               "yellowish fluid, small arrow (shape equivalent: tube ↔ tube)",
               "SWAP right_diagram: wide artery, free red cells, big arrow → open vessel, calm pink tissue, clear fluid moving, big arrow (before/after stays before/after)",
               "SWAP callouts_left: 'Narrowed Arteries' / 'Reduced Blood-flow' → 'Inflamed, swollen tissue' / 'Fluid sitting still' (mechanism in plain words (B4))",
               "SWAP callouts_right: 'Wider Arteries' / 'Improved Blood-flow' → 'Calm tissue' / 'Fluid draining' (plain words)",
               "SWAP product_spot: Primal Storm tub centred bottom, ~25 % width, between the two diagrams, thin line above it → the EDENVIA pouch, same spot, "
               "real proportions (placement (A8))",
               "SWAP footer: 'SUPPORT THE BLOOD FLOW BEHIND YOUR ER3CT!ONS.' 2 lines → 'SUPPORT THE DRAINAGE BEHIND LIGHT, SLIM LEGS.' 2 lines (copy formula "
               "SUPPORT THE [mechanism] BEHIND [result])",
               "KEEP background: cream paper (render style)"],
 'visual': ("Coloured-pencil medical sketch on cream (#f5e9d8) paper, hand-drawn hatching, NOT a photo, exactly the template: a three-line heavy condensed "
            "black headline at the top, two bold caps panel labels, two mirrored diagonal cut-open tubes left and right with thin black callout lines "
            "and small labels, " + POUCH + " standing centred at the bottom between the two diagrams with a long thin vertical line down to it, and a "
            "two-line heavy condensed footer. The tubes are the drainage vessels inside a lower leg: LEFT the vessel squeezed narrow by swollen, pale, "
            "water-logged tissue around it, stagnant yellowish fluid inside, a small arrow; RIGHT the vessel wide open in calm pink tissue, clear fluid "
            "moving, a big arrow. Do NOT draw: no artery, no red blood cells, no plaque, no heart; no jar or tub — the product is the pouch of Image 1 "
            "at real proportions, label untouched; no glass; no person."),
 'texts': ['Headline: "DIETED FOR YEARS: LEGS STILL SWOLLEN? LOOK AT YOUR DRAINAGE."', 'Panel_left: "BLOCKED DRAINAGE"', 'Panel_right: "CLEAR DRAINAGE"',
           'Callout_left_1: "Inflamed, swollen tissue"', 'Callout_left_2: "Fluid sitting still"', 'Callout_right_1: "Calm tissue"', 'Callout_right_2: "Fluid draining"',
           'Footer: "SUPPORT THE DRAINAGE BEHIND LIGHT, SLIM LEGS."'],
 'engine': 'openai', 'fallback': 'none'},

# ---------------------------------------------------------------------------------------------------------------------------- S6
# compliance (deferred): 'Belt Buckle vs. Keg' (matches the template's 'Spaghetti' insult).
# Production method = photo + pasted product + typeset text (§3b): Seedream renders the photo scene only, composite.py pastes the real pouch and the text.
{'num': 6, 'tpl_abs': TF + '10-11_06_c0196_Blueprint.png',
 'angle': "A8 A8-M the man's belly that isn't fat — 'it's not the beer, it's what your body stopped clearing'",
 'why': "Two arms locked in an arm-wrestle, one thick and veined, one thin and pale, under 'Beef vs. Spaghetti' — the metaphor and the photo say the same "
        "thing in half a second; everyone can see which one you are. Visual trick to copy literally: two bodies touching at the centre, the winner on the "
        "left, dark vignette, product floating top-left, brand-colour footer band.",
 'dna': "arm-wrestling arms (their problem = muscle) → two men's waistlines side by side (our problem = the belly over the belt); 'Beef vs. Spaghetti' → "
        "'Belt Buckle vs. Keg'; 'MYO-GROW' red → 'EDENVIA' blue; Myo-Grow bottle → the Edenvia pouch pasted by script; red band → navy band; 'refuse to "
        "shrink with age' → 'refuse to blame the beer'.",
 'scene': "a contest where the body difference is the whole point. Ours: two men side by side at a backyard BBQ, shirts tucked, belt line in frame — the "
          "belly difference is the contest",
 'placement': "Edenvia pouch from Image 1, same spot and size as the bottle: floating top-left over the photo, ~22 % width — like the template",
 'inventory': ["SWAP line_1: 'Beef vs. Spaghetti' white regular → 'Belt Buckle vs. Keg' (metaphor pair for our body part (E6))",
               "SWAP line_2: 'Guess who's on MYO-GROW' bold, brand in red → 'Guess who's on EDENVIA' bold, brand in Edenvia accent blue (template words kept + brand slot)",
               "SWAP scene: two arms arm-wrestling, dark studio → two men 45–60 at a backyard BBQ in the evening, side by side from chest to thigh, shirts "
               "tucked into jeans, each holding a beer; left man flat waist and visible belt buckle, right man a round belly hanging over the belt (scene "
               "where OUR problem is directly visible (A3); concede the beer (B11))",
               "KEEP product_spot: product top-left, ~22 % width, floating over the photo (placement) — the real pouch cutout pasted by script",
               "SWAP footer_band: red band, 2 lines white bold → Edenvia navy #14488F band, 2 lines white bold (brand colour)",
               "SWAP footer_text: 'MYO-GROW was made for men who refuse to shrink with age.' → 'EDENVIA was made for men who refuse to blame the beer.' (copy "
               "formula + B11 (concede the pleasure))",
               "KEEP logo: none (no logo slot)"],
 'visual': ("Photoreal, dark moody background with the template's vignette, warm skin, sharp detail: two men of 45–60 (" + OLD_M + ") standing shoulder to "
            "shoulder at a backyard barbecue in the evening, framed chest to thigh, no faces, each holding a bottle of beer. LEFT man: shirt tucked into "
            "jeans, flat waist, visible brass belt buckle. RIGHT man: polo tucked into jeans, a big round belly pushing out over the belt. Scene by "
            "Seedream (no text, no product); the real Edenvia pouch top-left and the three text slots (two white lines at the top, the navy footer band) "
            "are added by script. Do NOT draw: no arm wrestling, no muscles, no bare skin, no bodybuilders, no faces."),
 'texts': ['Line_1: "Belt Buckle vs. Keg"', 'Line_2: "Guess who\'s on EDENVIA"', 'Footer: "EDENVIA was made for men who refuse to blame the beer."'],
 'engine': 'seedream_comp', 'fallback': 'none', 'sexual': False,
 'sd_prompt': ("Photoreal, dark and moody, same lighting and dark vignette as the reference photo, square: two men in their late 40s to 50s standing shoulder "
               "to shoulder at a backyard barbecue in the evening, framed from the chest to the thigh so no faces are visible, each holding a bottle of "
               "beer in one hand. LEFT man: a button shirt tucked into jeans, flat waist, a visible brass belt buckle. RIGHT man: a polo shirt tucked into "
               "jeans, a big round belly pushing out over his belt. Ordinary middle-aged bodies, not bodybuilders, no bare skin, no faces. The top 22% "
               "of the image is plain dark, nearly black, empty background and the bottom 14% is plain dark empty background. No text, no product, no logo."),
 'composite': {"jar": {"x": 0.19, "y": 0.56, "h": 0.30},
               "rects": [[0, 0.87, 1, 1, "#14488F"]],
               "texts": [{"y": 0.025, "size": 0.055, "font": "Montserrat", "weight": 500, "runs": [["Belt Buckle vs. Keg", "#FFFFFF", 500]]},
                         {"y": 0.10, "size": 0.066, "font": "Montserrat", "weight": 800, "runs": [["Guess who's on", "#FFFFFF", 800], [" EDENVIA", "#1468DB", 800]]},
                         {"y": 0.885, "size": 0.042, "font": "Montserrat", "weight": 800, "runs": [["EDENVIA was made for men", "#FFFFFF", 800]]},
                         {"y": 0.935, "size": 0.042, "font": "Montserrat", "weight": 800, "runs": [["who refuse to blame the beer.", "#FFFFFF", 800]]}]}},

# ---------------------------------------------------------------------------------------------------------------------------- S7
# Production method = photo flat lay + pasted product (A25 family): Seedream renders the still life (9:16) with the right half empty; the real pouch,
# the headers, the two captions and the button are composited by script (exact typography on a 338x600 template).
{'num': 7, 'tpl_abs': T + '10-11_c0233_ArcticGlowBalm.webp',
 'angle': "A8 A8-L heavy, swollen legs — everything she bought vs one tablet in a glass of water",
 'why': "A pile of fifteen skincare products on the left against a single jar on the right under 'OLD ME / NEW ME' — the clutter is the confession; she "
        "recognises her own bathroom shelf. Visual trick to copy literally: many vs one, same lighting, same table; the one product gets all the space on the right.",
 'dna': "skincare bottles, fan, jade roller (her old face routine) → compression socks, detox tea, dry brush, water tablets, tape measure, scale (her old "
        "leg routine); amber balm jar → the Edenvia pouch pasted by script; plum → deep navy; 'FOR PERIMENOPAUSE' → 'FOR HEAVY, SWOLLEN LEGS'; beige → ice blue.",
 'scene': "a product still life on a warm tabletop; ours is the same still life with HER graveyard: compression socks, a box of 'detox tea', a dry brush, a "
          "white diuretic bottle, a measuring tape, a bathroom scale corner",
 'placement': "Edenvia pouch from Image 1 standing upright, right half, same spot and visual weight as the jar — like the template",
 'inventory': ["SWAP header_left: 'OLD ME' plum serif caps → 'OLD ME' deep navy (template words kept; brand colour)",
               "SWAP header_right: 'NEW ME' → 'NEW ME' deep navy (template words kept)",
               "SWAP left_pile: ~15 white skincare bottles, tubes, jars, a small fan, a jade roller → a pile of her leg-swelling fixes: two rolled beige "
               "compression socks, a box of herbal tea, a wooden dry brush, a plain white pill bottle, a tape measure, a corner of a bathroom scale (props of OUR problem (A12))",
               "SWAP product_spot: one amber jar with white lid, right half, ~45 % width, centred → the EDENVIA pouch, same spot, pasted by script (placement; product alone = the point)",
               "SWAP caption_left: 'Dryness, thinning, uneven tone and unexpected breakouts.' → 'Compression, teas, dry brushing — and legs still heavy by 5 p.m.' (list formula, problem named (B2))",
               "SWAP caption_right: 'Cold-pressed, undiluted, arctic formula.' → 'One tablet, one glass of water, 8 PPM of hydrogen.' (three-beat product formula; label claim)",
               "SWAP button: 'FOR PERIMENOPAUSE' plum rounded → 'FOR HEAVY, SWOLLEN LEGS' deep navy rounded (name the problem, not the condition (B2))",
               "SWAP background: warm beige tabletop → Edenvia ice blue tabletop, same soft daylight (brand palette; render style kept)",
               "KEEP logo: none (no logo slot)"],
 'visual': ("Photoreal flat-lay still life, 9:16, on a pale ice-blue (#EAF1F9) tabletop in soft daylight, the look of a skincare product photo: on the LEFT "
            "half a cluttered pile of her leg-swelling fixes (rolled beige compression socks, a box of herbal tea, a wooden dry brush, a plain white "
            "bottle, a tape measure, the corner of a bathroom scale); the RIGHT half empty tabletop where the real Edenvia pouch is pasted by script; "
            "the two navy headers, the two small captions and the navy button are typeset by script. Do NOT draw: no skincare, no jade roller, no fan, "
            "no brand on any prop, no person."),
 'texts': ['Header_left: "OLD ME"', 'Header_right: "NEW ME"',
           'Caption_left: "Compression, teas, dry brushing — and legs still heavy by 5 p.m."', 'Caption_right: "One tablet, one glass of water, 8 PPM of hydrogen."',
           'Button: "FOR HEAVY, SWOLLEN LEGS"'],
 'engine': 'seedream_comp', 'fallback': 'none', 'aspect': 'portrait_16_9',
 'sd_prompt': ("Vertical 9:16 photoreal flat-lay still life on a pale ice-blue (#EAF1F9) tabletop with soft daylight, the clean look of a skincare product "
               "photo, same camera angle and lighting as the reference. On the LEFT half only, between 17% and 62% of the image height, a cluttered pile "
               "of a middle-aged woman's leg-swelling remedies: two rolled beige compression socks, a plain white box of herbal tea with a blank label, "
               "a plain white pill bottle with a blank label, a wooden dry brush, a yellow tape measure, the corner of a white bathroom scale. The RIGHT "
               "half of the image is completely empty plain tabletop. The top 15% and the bottom 35% of the image are empty plain background. No text, "
               "no product, no logo, no person."),
 'composite': {"jar": {"x": 0.74, "y": 0.64, "h": 0.27},
               "rects": [[0.10, 0.845, 0.90, 0.903, "#172A54"]],
               "texts": [{"y": 0.093, "size": 0.032, "font": "Manrope-ExtraBold", "cx": 0.26, "runs": [["OLD ME", "#172A54"]]},
                         {"y": 0.093, "size": 0.032, "font": "Manrope-ExtraBold", "cx": 0.74, "runs": [["NEW ME", "#172A54"]]},
                         {"y": 0.68, "size": 0.019, "font": "Manrope-Regular", "cx": 0.26, "maxw": 0.40, "lh": 1.35,
                          "runs": [["Compression, teas, dry brushing — and legs still heavy by 5 p.m.", "#172A54"]]},
                         {"y": 0.68, "size": 0.019, "font": "Manrope-Regular", "cx": 0.74, "maxw": 0.40, "lh": 1.35,
                          "runs": [["One tablet, one glass of water, 8 PPM of hydrogen.", "#172A54"]]},
                         {"y": 0.859, "size": 0.024, "font": "Manrope-ExtraBold", "cx": 0.5, "runs": [["FOR HEAVY, SWOLLEN LEGS", "#FFFFFF"]]}]}},

# ---------------------------------------------------------------------------------------------------------------------------- S8
# The brief flags A25 (photo collage + pasted product); first try by regeneration (the two scenes change completely), A25 is the fix path.
{'num': 8, 'tpl_abs': T + '10-11_c0259_GoliAshwagandha.webp',
 'angle': "A8 A8-L heavy, swollen legs — your leg-swelling routine is letting you down",
 'why': "Two desks stacked: the top one is chaos (energy cans, notifications, crumpled paper), the bottom one is calm with the bottle and a glass of water — "
        "the ad shows the before and after of a habit, not a body; the relief of the clean desk. Visual trick to copy literally: same camera angle for "
        "both halves, the bottom half warmer and tidier.",
 'dna': "messy desk with energy cans and a phone (their problem = evenings) → messy bathroom counter at night with her leg-swelling props; calm desk with "
        "gummies and water → calm kitchen counter in the morning with the Edenvia pouch and the fizzing glass; 'wind-down routine' → 'leg-swelling routine'; "
        "'calm / plant-based / clinically proven' → 'lighter legs / 8 PPM hydrogen / third-party lab tested'; yellow button → Edenvia blue.",
 'scene': "desk because the product fixes evenings at the desk. Ours: top = her evening leg routine on the bathroom counter (compression socks peeled off, "
          "'detox tea' box, dry brush, a white bottle, legs-up pillow); bottom = the kitchen counter in the morning, the pouch and a clear glass with the tablet fizzing",
 'placement': "Edenvia pouch, same spot and size as the Goli bottle (lower-left of the bottom scene, ~20 % width); the glass to its right with the tablet fizzing — like the template",
 'inventory': ["SWAP headline: 'Your current wind-down routine may be letting you down.' 3 lines → 'Your current leg-swelling routine may be letting you "
               "down.' 3 lines (copy formula, one noun swapped, same length)",
               "SWAP subline: 'Support calm without the crash. Plant-based. Clinically proven.' → 'Legs feel lighter without the bathroom runs. 8 PPM hydrogen. "
               "Third-party lab tested.' (three-beat formula; proof from the kit)",
               "SWAP top_scene: messy desk: energy cans, iced coffee, phone with notifications, crumpled notes → messy bathroom counter at night: peeled-off "
               "compression socks, a box of herbal tea, a dry brush, a plain white pill bottle, a wedge pillow, a phone lying face up (props of OUR problem)",
               "SWAP bottom_scene: calm desk: lamp, book, bottle, glass of water, plant → calm kitchen counter in the morning: the Edenvia pouch, a clear "
               "glass of water with the white tablet fizzing at the bottom and fine bubbles rising, a plant, a window (scene of the fix; glass kept)",
               "SWAP product_spot: Goli bottle lower-left of the bottom scene, ~20 % width, glass of water to its right → the EDENVIA pouch, same spot, the "
               "glass with the tablet fizzing to its right (placement + the ingredient visual (C2))",
               "SWAP button: yellow 'Upgrade your routine →' → Edenvia accent blue button, same words 'Upgrade your routine →' (template words kept; brand colour)",
               "KEEP logo: none (no logo slot)"],
 'visual': ("Photoreal, exactly the template's stacked layout: the TOP half a messy bathroom counter at night under warm lamp light — peeled-off beige "
            "compression socks, a box of herbal tea, a wooden dry brush, a plain white bottle, a wedge leg pillow, a phone lying face up with a dark "
            "screen — with the three-line white bold headline and the two-line white regular subline over it; the BOTTOM half a calm kitchen counter in "
            "soft morning light, shallow depth of field: " + POUCH + " standing lower-left (about 20% of the width, real proportions, label to camera), to "
            "its right " + GLASS + ", a small plant and a window behind; an Edenvia blue (#1468DB) rounded button with white text across the bottom. No "
            "person. Do NOT draw: no desk, no energy cans, no laptop, no gummies, no bottle or jar for Edenvia; no text on the phone." + M34),
 'texts': ['Headline: "Your current leg-swelling routine may be letting you down."',
           'Subline: "Legs feel lighter without the bathroom runs. 8 PPM hydrogen. Third-party lab tested."',
           'Button: "Upgrade your routine →"'],
 'engine': 'openai', 'fallback': 'none', 'aspect': 'portrait_4_3'},

# ---------------------------------------------------------------------------------------------------------------------------- S9
# compliance (deferred): WIFE: "HOLY SHIT, WHERE DID YOUR GUT GO?" (template register, founder: hardcore marketing).
# §3b: meme text by script. Method = minimal Seedream edit of the template itself (faces kept, text + tub removed, red → blue), then composite.py
# pastes the real pouch and every text slot (Oswald condensed caps like the template; DejaVu for the arrow).
{'num': 9, 'tpl_abs': T + '10-11_c0310_Overload.webp',
 'angle': "A8 A8-M the man's belly that isn't fat — he sucks it in, the other one tucks his shirt in",
 'why': "The crying wojak and the bearded chad — the internet's own 'loser vs winner' — with three brutally specific lines under each; the reader knows "
        "which one he is, and the wife is the witness. Visual trick to copy literally: two meme faces facing each other across a white/red split, product "
        "tucked bottom right, 'ingredient stack' line bottom left; red half → Edenvia blue.",
 'dna': "bedroom shame/triumph lines → belly shame/triumph lines with the same wife witness and the same profanity; 'PYGEUM + ZINC + LECITHIN' → "
        "'HYDROGEN + MAGNESIUM + MINERALS'; 'The Stack' → 'The Glass'; red half → Edenvia blue; black tub → the Edenvia pouch pasted by script; red CTA → blue CTA.",
 'scene': "no scene; a meme card. Ours: same card, same two faces, belly lines instead of bedroom lines",
 'placement': "Edenvia pouch from Image 1, same spot and size as the tub: bottom right, ~20 % width, overlapping the split — like the template",
 'inventory': ["KEEP left_face: crying wojak, line art (meme stays meme)",
               "KEEP right_face: bearded chad profile (meme stays meme)",
               "SWAP left_lines: 3 sexual shame lines → 3 belly shame lines (see slots) (same count, same register, our problem)",
               "SWAP right_lines: 3 sexual triumph lines incl. 'WIFE: HOLY SHIT…' → 3 belly triumph lines incl. 'WIFE: HOLY SHIT, WHERE DID YOUR GUT GO?' "
               "(copy formula + profanity level kept (A15))",
               "SWAP ingredient_line: 'PYGEUM + ZINC + LECITHIN' big caps → 'HYDROGEN + MAGNESIUM + MINERALS' (our literal contents in the same display (C2))",
               "SWAP tagline: 'The Stack That Changes Everything.' → 'The Glass That Changes Everything.' (copy formula; one noun = our ritual)",
               "SWAP cta: red 'SHOP NOW →' → Edenvia blue 'SHOP NOW →' (template words kept)",
               "SWAP product_spot: black tub bottom right, ~20 % width, overlapping the split → the EDENVIA pouch, same spot, pasted by script (placement)",
               "SWAP right_half_colour: red → Edenvia accent blue (brand colour)",
               "KEEP logo: none (no logo slot)"],
 'visual': ("The template itself, minimally edited: the two black line-art meme faces kept pixel-identical (crying wojak top-left on the white half, bearded "
            "chad profile top-right), the right half recoloured from red to Edenvia blue #1468DB, every text and the black tub removed so the areas become "
            "plain background; then the real Edenvia pouch bottom right and all nine text slots are typeset by script in the template's heavy condensed "
            "caps. Do NOT draw: no sexual imagery, no tub, no beer can, no photo of a person."),
 'texts': ['Left_1: "SUCKS HIS GUT IN FOR EVERY PHOTO"', 'Left_2: "WIFE SAYS \'IT\'S THE BEER\' WITHOUT LOOKING UP"',
           'Left_3: "KEEPS HIS SHIRT ON AT THE POOL SO NOBODY CAN SEE"',
           'Right_1: "TUCKS HIS SHIRT IN. ON PURPOSE."', 'Right_2: "WIFE: \\"HOLY SHIT, WHERE DID YOUR GUT GO?\\""',
           'Right_3: "STANDS FOR THE PHOTO BECAUSE HE KNOWS THE BELT WILL IMPRESS"',
           'Ingredient_line: "HYDROGEN + MAGNESIUM + MINERALS"', 'Tagline: "The Glass That Changes Everything."', 'Cta: "SHOP NOW →"'],
 'engine': 'seedream_comp', 'fallback': 'none',
 'sd_prompt': ("Edit the reference image with the smallest possible change. Keep the two meme faces pixel-identical and in the same place: the crying black "
               "line-art face at the top left on the white half, and the bearded man's profile at the top right. Change ONLY these things: 1. the RIGHT "
               "half background from red to a flat Edenvia blue (#1468DB) with the same soft gradient, same vertical split line in the middle, the bottom "
               "strip stays white across the full width; 2. remove ALL text everywhere — the three text blocks under each face, the big capital line and "
               "the sentence at the bottom left, the red button at the bottom right — those areas become plain background (white on the left half, blue "
               "on the right half, white on the bottom strip); 3. remove the black tub at the bottom right — plain background there. No text, no product, no logo."),
 'composite': {"jar": {"x": 0.85, "y": 0.86, "h": 0.24},
               "rects": [[0.715, 0.925, 0.955, 0.975, "#1468DB"]],
               "texts": [{"y": 0.39, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.08, "maxw": 0.36, "lh": 1.22, "runs": [["SUCKS HIS GUT IN FOR EVERY PHOTO", "#111111"]]},
                         {"y": 0.465, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.08, "maxw": 0.36, "lh": 1.22, "runs": [["WIFE SAYS 'IT'S THE BEER' WITHOUT LOOKING UP", "#111111"]]},
                         {"y": 0.54, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.08, "maxw": 0.36, "lh": 1.22, "runs": [["KEEPS HIS SHIRT ON AT THE POOL SO NOBODY CAN SEE", "#111111"]]},
                         {"y": 0.39, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.57, "maxw": 0.36, "lh": 1.22, "runs": [["TUCKS HIS SHIRT IN. ON PURPOSE.", "#FFFFFF"]]},
                         {"y": 0.465, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.57, "maxw": 0.36, "lh": 1.22, "runs": [["WIFE: \"HOLY SHIT, WHERE DID YOUR GUT GO?\"", "#FFFFFF"]]},
                         {"y": 0.54, "size": 0.021, "font": "Oswald", "weight": 700, "align": "left", "x": 0.57, "maxw": 0.36, "lh": 1.22, "runs": [["STANDS FOR THE PHOTO BECAUSE HE KNOWS THE BELT WILL IMPRESS", "#FFFFFF"]]},
                         {"y": 0.838, "size": 0.038, "font": "Oswald", "weight": 700, "align": "left", "x": 0.07, "maxw": 0.68, "runs": [["HYDROGEN + MAGNESIUM + MINERALS", "#111111"]]},
                         {"y": 0.90, "size": 0.027, "font": "Montserrat", "weight": 500, "align": "left", "x": 0.07, "maxw": 0.62, "runs": [["The Glass That Changes Everything.", "#333333", 500]]},
                         {"y": 0.934, "size": 0.024, "font": "DejaVu", "align": "left", "x": 0.745, "runs": [["SHOP NOW →", "#FFFFFF"]]}]}},

# ---------------------------------------------------------------------------------------------------------------------------- S10
# compliance (deferred): 'LOSES WEIGHT ✅' belongs to the diet, Edenvia claims the jawline.
{'num': 10, 'tpl_abs': T + '10-11_c0376_MarsMen.webp',
 'angle': "A8 A8-F puffy face and soft jawline — dieting with Edenvia brings the jawline back",
 'why': "The same man drawn twice — hollow-eyed on the left holding his prescription, healthy on the right holding the brand — under 'FINASTERIDE | "
        "FINASTERIDE WITH MARS MEN': you keep your thing, we fix its side effect; the mirror: same face, two futures. Visual trick to copy literally: "
        "identical character, left degraded, right restored, each holding its product at the chest with the label out.",
 'dna': "man ~30 with hair-loss pills → a woman of 45–50 with a diet shake (the thing she keeps doing); dark circles / sunken → puffy face, soft double "
        "chin; healthy man with the Mars Men bottle → the same woman, jawline back, holding the Edenvia pouch; 'FINASTERIDE' → 'DIETING'; orange box → "
        "Edenvia blue box; hair lines → weight / puffy face / jawline lines.",
 'scene': "no scene; two half-length portraits on cream. Ours: the same woman twice, face and jawline visible because this is the face angle",
 'placement': "left: a plain 'DIET SHAKE' shaker bottle at the chest; right: the Edenvia pouch from Image 1 held at the chest with the fingers wrapped "
              "around it, label out, ~30 % width each — like the template",
 'inventory': ["SWAP person_left: man ~30, curly hair, dark circles, sunken, black T-shirt, holding a Finasteride bottle at the chest → woman 45–50, "
               "shoulder-length dark curly hair, puffy face, soft double chin, tired eyes, black T-shirt, holding a 'DIET SHAKE' bottle at the chest, label "
               "out (avatar + body part = the face (A11, C1); rival object = what she keeps doing)",
               "SWAP person_right: same man, healthy, holding Mars Men bottle → the same woman, jawline sharp, eyes rested, same hair and T-shirt, holding the "
               "Edenvia pouch at the chest, label out (before/after; gesture kept (A8))",
               "SWAP header_left: 'FINASTERIDE' → 'DIETING' (the thing she keeps)",
               "SWAP header_right: 'FINASTERIDE WITH' + 'MARS MEN' on orange box → 'DIETING WITH' + 'EDENVIA' on Edenvia accent blue box (copy formula X WITH BRAND; brand slot)",
               "SWAP left_lines: 'TREATS HAIRLOSS ✅' / 'KILLS TESTOSTERONE ❌' → 'LOSES WEIGHT ✅' / 'PUFFY FACE STAYS ❌' (formula: the thing works ✅, its side effect ❌)",
               "SWAP right_lines: 'KEEPS HAIR ✅' / 'NATURAL TESTOSTERONE ✅' → 'LOSES WEIGHT ✅' / 'JAWLINE BACK ✅' (both ✅; bank: 'My jawline FINALLY back')",
               "SWAP product_spot: left: rival bottle at chest, ~30 % width; right: brand bottle at chest, same size → left a plain DIET SHAKE shaker, right "
               "the EDENVIA pouch, real proportions (placement + gesture (A8, C11))",
               "KEEP background: flat cream (render style)",
               "KEEP logo: none beyond the product (no logo slot)"],
 'visual': ("Comic ink illustration with subtle shading, NOT photoreal, flat cream (#f1e9dc) background, exactly the template's layout: two half-length "
            "portraits side by side, a black bold condensed caps header above each, the right header's brand name highlighted in white on an Edenvia "
            "blue (#1468DB) box, two small caps lines with ✅ / ❌ under each portrait. The same woman twice, " + OLD_F + ": LEFT she looks tired, puffy "
            "face, soft double chin, dark circles, holding a plain white shaker bottle labelled DIET SHAKE at her chest with both hands, label out; "
            "RIGHT the same face de-puffed, the jawline sharp, eyes rested, same hair and black T-shirt, holding " + POUCH + " at her chest with her "
            "fingers wrapped around it, label out, real proportions. Do NOT draw: no man, no prescription bottle, no hair-loss reading, no young model "
            "face on the right — the same 45-year-old woman, only de-puffed; no glass; do NOT copy the template's person." + M916),
 'texts': ['Header_left: "DIETING"', 'Header_right: "DIETING WITH EDENVIA"', 'Left_1: "LOSES WEIGHT ✅"', 'Left_2: "PUFFY FACE STAYS ❌"',
           'Right_1: "LOSES WEIGHT ✅"', 'Right_2: "JAWLINE BACK ✅"'],
 'engine': 'openai', 'fallback': 'none', 'aspect': 'portrait_16_9'},
]
for _s in S: _s['visual'] = _s['visual'] + TRUTH   # C2 brand truth on every ad
