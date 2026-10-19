#!/usr/bin/env bash
# Serve the Atlas (guia/) at http://127.0.0.1:8765/index.html
set -euo pipefail
cd "$(dirname "$0")/../guia"
echo "Atlas: http://127.0.0.1:8765/index.html"
exec python -m http.server 8765 --bind 127.0.0.1
