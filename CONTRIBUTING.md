# Contributing

Thanks for helping. The most valuable contribution is a **verified correction** to the guide text.

## Rules
1. **Every fact must be checked against the pack itself**: its KubeJS scripts, its recipes, the GregTech fork sources,
   or in-game testing. Cite where you checked it in the pull request.
2. A fact you cannot verify is still welcome, but it must be written as `Unverified: ...` so readers know.
3. **Do not commit generated or third-party data**: `guia/data/recipes.js`, `icons.js`, `multis.js`, `quests.js`,
   `blocks3d.js`, `guia/img/atlas.png`, `blocks.png`, `guia/img/m/`, `extract/*.json` and `gtsrc/` are built locally
   from your own modpack and are git-ignored. Do not paste pack assets or mod code into the repo.
4. **Do not include private data**: no player names or chat logs from Discord or other private spaces, no personal
   paths, no tokens. Summarize findings in your own words.

## How to fix a page
The Markdown wiki in `docs/` is the source of truth. Edit the page (front matter and body) and run
`node tools/refresh_body.js`. Details: [docs/CONTRIBUTING-CONTENT.md](docs/CONTRIBUTING-CONTENT.md).

## Code changes
- `extract/*.py` and `extract/*.js` must stay ASCII-only and must not contain machine-specific paths. Use
  `extract/common.py` (`require_pack()`, `GT_SRC`, `GUIA`).
- Check scripts compile: `python -m py_compile extract/*.py`.
- Preview locally (see README) before opening a pull request.

## Pull requests
Keep them small and focused, describe what you verified and how, and be kind (see `CODE_OF_CONDUCT.md`).
By contributing you agree your contribution is released under the MIT license of this repository.
