#!/usr/bin/env python3
"""Write one short kie prompt per template with a vision LLM (OpenAI gpt-5.4-mini), in the exact format that worked on batch T.
usage: write_prompts.py TEMPLATES_DIR PROMPTS_DIR [--workers 16]   (skips prompts that already exist)"""
import base64, concurrent.futures as cf, os, sys
from openai import OpenAI
sys.path.insert(0, "/home/adanalysis/workspace/blueprint-static/.claude/skills/static-ads/scripts"); import sac_config as C
T, P = sys.argv[1], sys.argv[2]; W = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 16
client = OpenAI(api_key=C.key(C.OPENAI_KEY_FILE)); os.makedirs(P, exist_ok=True)
BRIEF = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "BRIEF-for-prompts.md")).read()
EX = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts/kie-T/t_05.txt")).read()
SYS = f"""You write ONE image-generation prompt for gpt-image-2 that clones a Meta static ad template for the brand Edenvia. Output ONLY the prompt text, nothing else.
{BRIEF}
FORMAT (copy it exactly; this one produced an accepted ad):
---
{EX}
---
Rules: start with the Image 1 / Image 2 sentences as in the example (drop the Image 2 sentence only if the template shows no product at all, then write "No product (the template has none)."). Then "Changes:" — what is swapped for Edenvia (their product → our pouch same spot and size; their body part/symbol → our avatar's; their colour → Edenvia blue where their brand colour is; persons → our avatar). Then "Text, exactly and nothing else:" — one line per text slot of the template, same count, same length, same mechanic (a % stays a %, a price stays a price from the allowed list, a star count stays a star count), rewritten for the avatar; copy the template's words when they already fit. Finish with what NOT to draw. Keep it under 220 words. Never name a competitor, a disease, a drug, or a capsule/pill/powder for Edenvia."""

def one(f):
    out = os.path.join(P, os.path.splitext(f)[0].split("_")[0].lower() + ".txt")
    if os.path.exists(out): return f, "skip"
    b = base64.b64encode(open(os.path.join(T, f), "rb").read()).decode(); ext = f.rsplit(".", 1)[1].lower().replace("jpg", "jpeg")
    r = client.chat.completions.create(model="gpt-5.4-mini", messages=[{"role": "system", "content": SYS},
        {"role": "user", "content": [{"type": "text", "text": f"Template file: {f}. Write the prompt."}, {"type": "image_url", "image_url": {"url": f"data:image/{ext};base64,{b}", "detail": "high"}}]}])
    open(out, "w").write(r.choices[0].message.content.strip() + "\n"); return f, r.usage.total_tokens

files = sorted(x for x in os.listdir(T) if x.lower().endswith((".webp", ".jpg", ".png")))
with cf.ThreadPoolExecutor(W) as ex:
    for f, t in ex.map(one, files): print(f, t, flush=True)
