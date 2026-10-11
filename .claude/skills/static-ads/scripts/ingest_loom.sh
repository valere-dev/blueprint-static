#!/usr/bin/env bash
# Download a review Loom and transcribe it (OpenAI Whisper API via scripts/transcribe.py — never local whisper; R15).
# usage: ingest_loom.sh <loom-url> <id>      e.g.  ingest_loom.sh https://www.loom.com/share/xxxx s5
# Output: $SAC_WORKDIR/feedback/loom-<id>.mp4 + loom-<id>.txt (timecoded). Then follow 3-improve/feedback-loop.md.
set -euo pipefail
URL="$1"; ID="$2"; W="${SAC_WORKDIR:-$PWD}"; D="$W/feedback"; mkdir -p "$D"
yt-dlp -q -o "$D/loom-$ID.%(ext)s" --merge-output-format mp4 "$URL"
python3 "$(dirname "$0")/transcribe.py" "$D/loom-$ID.mp4" --out "$D"
ls -la "$D/loom-$ID".*
echo "Next: read $D/loom-$ID.txt in full, build the verdict table (3-improve/feedback-loop.md step 2)."
