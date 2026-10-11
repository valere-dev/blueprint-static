#!/usr/bin/env python3
"""D15 — output format of every ad (Adrien, Oct08 Loom): width is ALWAYS 1080.
  square template (1:1)      -> 1080 x 1080
  Story / TikTok (9:16)      -> 1080 x 1920 (stays a Story)
  4:5 feed                   -> 1080 x 1350
  any other ratio            -> 1080 x round(1080 * h / w)  (the template's own ratio)
A template within 3 % of a standard ratio snaps to it (1856x2304 = 0.806 -> 4:5; 1122x1402 -> 4:5).
usage:  python3 adformat.py check FILE...            -> prints size + target, exit 1 if any file is off
        python3 adformat.py fix FILE [TEMPLATE]      -> crop (least-content window) + resize in place
        python3 adformat.py target W H               -> prints the target size"""
import sys
W_OUT = 1080
STD = [(1, 1), (4, 5), (9, 16)]


def target_size(w, h):
    """(w, h) of a template or image -> the (1080, H) output size."""
    r = w / h
    for a, b in STD:
        if abs(r - a / b) / (a / b) <= 0.03:
            return W_OUT, round(W_OUT * b / a)
    return W_OUT, round(W_OUT * h / w)


def ratio_name(w, h):
    r = w / h
    for a, b in STD:
        if abs(r - a / b) / (a / b) <= 0.03:
            return f"{a}:{b}"
    return f"{w}:{h}"


def _smart_crop(im, tgt):
    """crop to ratio tgt (w/h) keeping the window that cuts the LEAST strong edges (text, objects)."""
    import numpy as np
    from PIL import ImageFilter, Image
    w, h = im.size
    if abs(w / h - tgt) <= 0.002:
        return im
    g = im.convert("L").resize((max(1, w // 4), max(1, h // 4)))
    e = (np.asarray(g.filter(ImageFilter.FIND_EDGES), dtype=float) > 70).astype(float)
    e[:2, :] = 0; e[-2:, :] = 0; e[:, :2] = 0; e[:, -2:] = 0
    e = np.asarray(Image.fromarray((e * 255).astype("uint8")).resize((w, h)), dtype=float)
    if w / h > tgt:
        nw = round(h * tgt); col = e.mean(axis=0); cs = np.concatenate([[0], np.cumsum(col)])
        best = min(range(0, w - nw + 1, 2), key=lambda x: cs[x] + (cs[-1] - cs[x + nw]))
        return im.crop((best, 0, best + nw, h))
    nh = round(w / tgt); row = e.mean(axis=1); cs = np.concatenate([[0], np.cumsum(row)])
    best = min(range(0, h - nh + 1, 2), key=lambda y: cs[y] + (cs[-1] - cs[y + nh]))
    return im.crop((0, best, w, best + nh))


def fit(im, size):
    """PIL image -> exactly `size` (crop to its ratio first, never stretch)."""
    from PIL import Image
    tw, th = size
    if im.size == (tw, th):
        return im
    return _smart_crop(im, tw / th).resize((tw, th), Image.LANCZOS)


def normalize(path, template=None):
    """Rewrite `path` in place at the D15 size of `template` (or of the image itself). Returns (old, new) sizes."""
    from PIL import Image
    im = Image.open(path); old = im.size
    ref = Image.open(template).size if template else old
    size = target_size(*ref)
    if old != size:
        mode = "RGBA" if im.mode in ("RGBA", "LA", "P") and path.lower().endswith(".png") else "RGB"
        fit(im.convert(mode), size).save(path)
    return old, size


if __name__ == "__main__":
    from PIL import Image
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "target":
        print(*target_size(int(sys.argv[2]), int(sys.argv[3])))
    elif cmd == "check":
        bad = 0
        for f in sys.argv[2:]:
            s = Image.open(f).size; t = target_size(*s); ok = s == t; bad += not ok
            print(f"{'OK ' if ok else 'BAD'} {s[0]}x{s[1]} target {t[0]}x{t[1]} ({ratio_name(*s)})  {f}")
        sys.exit(1 if bad else 0)
    elif cmd == "fix":
        print(normalize(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
    else:
        print(__doc__); sys.exit(2)
