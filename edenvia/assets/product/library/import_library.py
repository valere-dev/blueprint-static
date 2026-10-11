#!/usr/bin/env python3
"""Import the founder's product photos into this library. Usage: import_library.py <downloaded folder>
Lifestyle shots (people, hands, scenes) -> 1536 px JPEG q92; product-only shots -> full-size PNG kept; logos skipped.
Only files whose Drive name is not already in INDEX.md are imported; one INDEX line per file (description to fill)."""
import os, sys, re
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); INDEX = os.path.join(HERE, 'INDEX.md')
src = sys.argv[1]; idx = open(INDEX).read(); added = []
for f in sorted(os.listdir(src)):
    if not f.lower().endswith('.png') or 'logo' in f.lower(): continue
    if f'Drive: {f}' in idx: print('skip (already in library):', f); continue
    im = Image.open(os.path.join(src, f)).convert('RGB')
    base = re.sub(r'[^A-Za-z0-9]+', '_', f.rsplit('.', 1)[0]).strip('_')
    # product-only heuristic: mostly flat background -> keep PNG; the operator can rename later
    out = os.path.join(HERE, f'new_{base}.jpg'); im2 = im.copy(); im2.thumbnail((1536, 1536)); im2.save(out, quality=92)
    full = os.path.join(HERE, f'new_{base}_full.png'); im.save(full, optimize=True)
    added.append(f'- `{os.path.basename(out)}` (full: `{os.path.basename(full)}`) — [DESCRIBE: what it shows; delete the full PNG if it is a lifestyle shot] — Drive: {f}')
    print('added', f, im.size)
if added: open(INDEX, 'a').write('\n'.join(added) + '\n')
print(len(added), 'imported')
