"""Shared configuration for the static-ads scripts.

Every script imports this module instead of hard-coding brand paths.
Resolution order for each value: environment variable > brand.json > default.

  SAC_WORKDIR   working directory of the brand (out/, batch/, prompts/ live here). Default: current directory.
  SAC_BATCH     directory of the current batch (specs, templates/, prompts/, calls.jsonl, validated.json). Default: $SAC_WORKDIR/batch
  BRAND_JSON    path to the brand file. Default: $SAC_WORKDIR/brand.json if it exists, else the skill-root brand.json
                (../brand.json next to BRAND-KIT.md: blank template in static-ads, Wildhorn values in wildhorn-static-ads)
  SAC_PAGES     where review pages are written. Default: $SAC_WORKDIR/pages
  SAC_PUB       optional public folder that remix.py copies every output into (e.g. a Caddy-served gallery). Default: none
  OPENAI_KEY_FILE  default /etc/secrets/openai_api_key   (path only, never the value)
  KIE_KEY_FILE     default /etc/secrets/kie_api_key      (path only, never the value)
"""
import json, os

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.abspath(os.environ.get("SAC_WORKDIR", os.getcwd()))
BATCH = os.path.abspath(os.environ.get("SAC_BATCH", os.path.join(WORKDIR, "batch")))
SKILL_ROOT = os.path.dirname(SCRIPTS)
SKILL_BRAND_JSON = os.path.join(SKILL_ROOT, "brand.json")
if os.environ.get("BRAND_JSON"):
    BRAND_JSON = os.environ["BRAND_JSON"]
elif os.path.exists(os.path.join(WORKDIR, "brand.json")):
    BRAND_JSON = os.path.join(WORKDIR, "brand.json")
else:
    BRAND_JSON = SKILL_BRAND_JSON
PAGES = os.environ.get("SAC_PAGES", os.path.join(WORKDIR, "pages"))
PUB = os.environ.get("SAC_PUB", "")
OUT = os.path.join(WORKDIR, "out")
OPENAI_KEY_FILE = os.environ.get("OPENAI_KEY_FILE", "/etc/secrets/openai_api_key")
KIE_KEY_FILE = os.environ.get("KIE_KEY_FILE", "/etc/secrets/kie_api_key")


def _load_brand():
    try:
        with open(BRAND_JSON) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


BRAND = _load_brand()
if BRAND.get("_template"):
    import sys as _sys
    print(f"warning: {BRAND_JSON} is the BLANK brand template — copy it to $SAC_WORKDIR/brand.json and fill it (BRAND-KIT.md)", file=_sys.stderr)
NAME = BRAND.get("name", "BRAND")                      # e.g. "WILDHORN"
FILE_PREFIX = BRAND.get("file_prefix", NAME.title().replace(" ", ""))  # e.g. "Wildhorn" -> Wildhorn_S01.png
PRODUCT_NOUN = BRAND.get("product_noun", "jar")        # the word specs use for the product ("jar", "pouch", "bottle")
PRODUCT_PHOTO = BRAND.get("product_photo", os.path.join(WORKDIR, "product.jpg"))      # Image 1 of every generation
PRODUCT_CUTOUT = BRAND.get("product_cutout", os.path.join(WORKDIR, "product-cutout.png"))  # RGBA cutout for composite.py
PRODUCT_LOCK = BRAND.get("product_lock", f"the {NAME} {PRODUCT_NOUN}. Reproduce it exactly as in Image 1.")
WORDMARK = BRAND.get("wordmark", NAME)
ICON = BRAND.get("icon_description", "the brand icon only")
FONTS = BRAND.get("fonts_dir", os.path.join(SCRIPTS, "fonts"))


def key(path):
    """Read an API key from a secrets file (never print it)."""
    with open(path) as f:
        return f.read().strip()


def ensure_out():
    os.makedirs(OUT, exist_ok=True)
    return OUT
