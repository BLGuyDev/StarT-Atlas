#!/usr/bin/env bash
# Rebuild all generated Atlas data from YOUR Star Technology instance.
# Usage: STAR_PACK_DIR=/path/to/"Star Technology" scripts/build_all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8

if [ -z "${STAR_PACK_DIR:-}" ] && [ ! -f extract/config.local.json ]; then
  echo "ERROR: set STAR_PACK_DIR to your Star Technology instance folder (or create extract/config.local.json)." >&2
  exit 1
fi

if [ ! -d "${STAR_GT_SRC:-gtsrc}" ]; then
  echo "== gtsrc/ missing: fetching the StarT GregTech fork sources"
  python extract/fetch_gtsrc.py
fi

run() { echo; echo "== $*"; "$@"; }

run python extract/names.py             # 1 names.json
run python extract/extract_multis.py    # 2 multis.json
run python extract/extract_recipes.py   # 3 recipes.json
run python extract/jar_recipes.py       # 4 jar_recipes.json
run python extract/gt_machines.py       # 5 gt_machine_recipes.json
run python extract/build_data.py        # 6 guia/data/quests.js + multis.js
run python extract/build_recipes_js.py  # 7 guia/data/recipes.js
run python extract/build_assets.py      # 8 guia/img/atlas.png + data/icons.js + img/m/
run python extract/build_3d.py          # 9 guia/img/blocks.png + data/blocks3d.js

if [ -f tools/build_data.js ]; then
  run node tools/build_data.js          # 10 wiki data (tools/)
else
  echo "NOTE: tools/build_data.js not found - wiki data step NOT run."
fi
echo; echo "Done."
