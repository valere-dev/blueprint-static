# Edenvia — round 1 QC redos (S1, S4, S8, S10). 2026-10-11. Loaded after s1specs.py (same num overrides, pages show every try).
# QC log (2-make/qc-checklist.md): the D15 crop from the 2:3 OpenAI canvas cut the headline (S1, S8) or the side text (S4, S10) because the
# model ignored the margin note; S10 also drew the pouch label without the Edenvia wordmark/icon (C6). Fix = explicit LETTERBOX / PILLARBOX
# bands in the prompt + the label named element by element; everything else unchanged (A20: only what QC named).
import os, sys, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_sp = importlib.util.spec_from_file_location("s1", os.path.join(os.path.dirname(os.path.abspath(__file__)), "s1specs.py"))
_s1 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_s1)
from s1specs import M45, M34, M916, TRUTH

LB45 = (" LETTERBOX (mandatory): the canvas is 2:3 but the finished ad is 4:5. Paint a solid band of the same dark navy across the TOP 9% and the "
        "BOTTOM 9% of the canvas and put NOTHING in those two bands — no text, no badge, no banner, no element. The whole ad, from the small red badge "
        "at the top down to the gold banner at the bottom, fits entirely inside the middle 82% of the canvas height, with visible empty navy above the "
        "badge and below the banner.")
LB34 = (" LETTERBOX (mandatory): the canvas is 2:3 but the finished ad is 3:4. Paint a solid dark band across the TOP 7% and the BOTTOM 7% of the "
        "canvas and put NOTHING in those bands. The whole ad, from the first word of the headline at the top to the blue button at the bottom, fits "
        "entirely inside the middle 86% of the canvas height, with visible empty background above the headline and below the button.")
PB916 = (" PILLARBOX (mandatory): the canvas is 2:3 but the finished ad is a 9:16 Story. Keep the LEFT 10% and the RIGHT 10% of the canvas as plain "
         "background of the half they belong to (black / blue, or cream) with NOTHING in them. Every text line is short, centred in its half, and "
         "ends well before the edge: all text and both characters fit entirely inside the central 80% of the canvas width.")

def redo(num, qc, framing_old, framing_new, extra=""):
    s = dict(next(x for x in _s1.S if x["num"] == num))
    s["why"] = f"QC round 1: {qc} " + s["why"]
    s["visual"] = s["visual"].replace(framing_old, "") + extra + framing_new
    return s

S = [
    redo(1, "the top crop cut the badge and the first headline line (D15).", M45, LB45),
    redo(4, "the side crop cut the first/last letters of the body lines (D15).", M916, PB916),
    redo(8, "the top crop cut the first headline line; the button touched the bottom edge (D15).", M34, LB34),
    redo(10, "the side crop clipped 'PUFFY FACE STAYS'; the pouch label lost the Edenvia wordmark and atom icon (C6).", M916, PB916,
         extra=(" The pouch she holds is an EXACT replica of Image 1, label complete and readable: at the top the small atom icon next to the bold "
                "italic word Edenvia in dark navy, then MOLECULAR, then the large HYDROGEN, then GENERATES 8PPM OF HYDROGEN PER TABLET, the two "
                "CONSUME DAILY lines, DIETARY SUPPLEMENT and 30 TABLETS | 30 DAY SUPPLY — nothing missing, nothing re-lettered.")),
]
