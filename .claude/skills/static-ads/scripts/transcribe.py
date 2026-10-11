#!/usr/bin/env python3
"""Transcribe a review Loom (or any video/audio) through the OpenAI Whisper API — replacement for `mr-transcribe`
on hosts that don't have it (nutraflow1, 2026-10-11; VPS-SETUP.md §5, system rule R15).

usage: transcribe.py <media file> [--out DIR] [--dry-run]
Output: <DIR>/<stem>.txt — one timecoded line per segment ("MM:SS  text"), same shape as the mr-transcribe
transcripts quoted in 3-improve/rules.md (e.g. Loom O1 [02:52]). DIR defaults to the media file's folder.

Key: read from OPENAI_KEY_FILE (default /etc/secrets/openai_api_key, see sac_config.py) — never printed, never an env var.
Never local whisper on the VPS (feedback-loop.md §1). Cost ≈ $0.006/min.
The audio is extracted with ffmpeg (mono 16 kHz mp3, 48 kb/s) and cut into 20-minute chunks so every upload stays
under Whisper's 25 MB limit; chunk timestamps are offset so the final file is continuous.
"""
import argparse, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sac_config as C

CHUNK_S = 20 * 60          # seconds per upload


def mmss(t):
    t = int(t); return f"{t // 60:02d}:{t % 60:02d}"


def extract_chunks(src, tmp):
    """ffmpeg → mono 16 kHz mp3 chunks of CHUNK_S seconds. Returns [(offset_seconds, path), …]."""
    pat = os.path.join(tmp, "chunk_%03d.mp3")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k",
                    "-f", "segment", "-segment_time", str(CHUNK_S), "-reset_timestamps", "1", pat], check=True)
    files = sorted(f for f in os.listdir(tmp) if f.startswith("chunk_"))
    return [(i * CHUNK_S, os.path.join(tmp, f)) for i, f in enumerate(files)]


def transcribe(chunks):
    from openai import OpenAI
    client = OpenAI(api_key=C.key(C.OPENAI_KEY_FILE))
    lines = []
    for off, path in chunks:
        with open(path, "rb") as f:
            r = client.audio.transcriptions.create(model="whisper-1", file=f, response_format="verbose_json")
        for s in r.segments or []:
            text = (s.text if hasattr(s, "text") else s["text"]).strip()
            start = s.start if hasattr(s, "start") else s["start"]
            if text: lines.append(f"{mmss(off + start)}  {text}")
    return lines


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("media"); p.add_argument("--out", default=None)
    p.add_argument("--dry-run", action="store_true", help="extract the audio chunks, print their sizes, call no API")
    a = p.parse_args()
    if not os.path.exists(a.media): sys.exit(f"no such file: {a.media}")
    out_dir = a.out or os.path.dirname(os.path.abspath(a.media)); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, os.path.splitext(os.path.basename(a.media))[0] + ".txt")
    with tempfile.TemporaryDirectory() as tmp:
        chunks = extract_chunks(a.media, tmp)
        if not chunks: sys.exit("ffmpeg produced no audio — is there an audio track?")
        for off, path in chunks: print(f"chunk @{mmss(off)}  {os.path.getsize(path) / 1e6:.1f} MB", file=sys.stderr)
        if a.dry_run: print(f"dry run: {len(chunks)} chunk(s), would write {out}"); return
        if not os.path.exists(C.OPENAI_KEY_FILE): sys.exit(f"key file missing: {C.OPENAI_KEY_FILE}")
        lines = transcribe(chunks)
    with open(out, "w") as f: f.write("\n".join(lines) + "\n")
    print(f"{out}  ({len(lines)} segments, {mmss(chunks[-1][0] + CHUNK_S) if len(chunks) > 1 else 'single chunk'})")
    print("Next: read the transcript in full, build the verdict table (3-improve/feedback-loop.md step 2).")


if __name__ == "__main__":
    main()
