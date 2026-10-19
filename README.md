# Star Technology Atlas

An unofficial progression guide for the Minecraft modpack **Star Technology** (GregTech CEu fork "StarT" by the
StarT Dev Team; official wiki: <https://start-dev-team.github.io/StarT-Wiki/>). It is a fan project and is not
affiliated with the pack authors (see [NOTICE.md](NOTICE.md)).

The project has two parts:

| Part | Folder | What it is |
|------|--------|------------|
| Markdown wiki | `docs/` | Source of truth for the guide text. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) (`mkdocs.yml`) and published to GitHub Pages by `.github/workflows/docs.yml`. |
| Interactive Atlas | `guia/` | Static HTML/JS app: phased plan, per-module bills of materials, crafting trees, multiblock cards, 3D assembly-line viewer and a quest checklist. |

Helper code lives in `extract/` (Python pipeline that reads your own modpack), `tools/` (wiki/data tooling) and
`scripts/` (build and preview scripts).

## Data policy

The Atlas needs data generated from the modpack and from mod assets. Those files derive from third-party work, so
they are **not in this repository** and are git-ignored: `guia/data/recipes.js`, `icons.js`, `multis.js`,
`quests.js`, `blocks3d.js`, `guia/img/atlas.png`, `blocks.png`, `guia/img/m/`, `extract/*.json` and `gtsrc/`.
You generate them locally from your own installation (below). Nothing from Discord or other private spaces is stored.

**Verification rule:** every fact is checked against the pack's own scripts and recipes (KubeJS, configs, the
GregTech fork sources). A fact that could not be verified is tagged `Unverified:`.

## Contributing a correction

1. Edit the relevant page in `docs/` (front matter and body).
2. Run `node tools/refresh_body.js`.
3. Open a pull request, saying where you verified the fact.

Details: [docs/CONTRIBUTING-CONTENT.md](docs/CONTRIBUTING-CONTENT.md). General rules: [CONTRIBUTING.md](CONTRIBUTING.md).

## Build the Atlas data from your own pack

Requirements: Python 3.10+ with `pip install -r requirements-extract.txt` (Pillow, numpy), Node.js (used by
`tools/build_data.js`), and a Star Technology instance (e.g. a CurseForge instance folder containing `mods/` and
`kubejs/`). The vanilla 1.20.1 jar is looked up in the CurseForge layout (`../../Install/versions/1.20.1/1.20.1.jar`
relative to the instance); otherwise set `STAR_VANILLA_JAR`.

```powershell
# PowerShell, from the repo folder (or just double-click Start-Atlas.bat)
$env:STAR_PACK_DIR = 'D:/path/to/Star Technology'
.\scripts\build_all.ps1
```
```bash
# bash
export STAR_PACK_DIR="/path/to/Star Technology"
scripts/build_all.sh
```

Instead of the environment variable you can create `extract/config.local.json` (git-ignored):
`{"pack_dir": "...", "vanilla_jar": "...", "gt_src": "..."}`.

The scripts first fetch the StarT GregTech fork sources into `gtsrc/` if missing
(`python extract/fetch_gtsrc.py`, from <https://github.com/StarT-Dev-Team/GTM-StarT-Fork>, branch `main`), then run,
from the repo root:

1. `extract/names.py` - `names.json`: display names from every mod jar and the KubeJS lang files.
2. `extract/extract_multis.py` - `multis.json`: multiblock block counts (KubeJS startup scripts + GT Java patterns).
3. `extract/extract_recipes.py` - `recipes.json`: KubeJS server-script and GT Java recipes, plus removals.
4. `extract/jar_recipes.py` - `jar_recipes.json`: data recipes inside all jars (including nested jars).
5. `extract/gt_machines.py` - `gt_machine_recipes.json`: tiered GT machine recipes.
6. `extract/build_data.py` - `guia/data/quests.js` and `multis.js`.
7. `extract/build_recipes_js.py` - `guia/data/recipes.js` (one recipe per item, BOM closure).
8. `extract/build_assets.py` - `guia/img/atlas.png`, `guia/data/icons.js`, `guia/img/m/*.png`.
9. `extract/build_3d.py` - `guia/img/blocks.png` and `guia/data/blocks3d.js`. Rerun after any change to
   the chain data (`docs/`) that adds machines.
0. (runs first) `tools/build_data.js` - `guia/data/wiki-data.js` from `docs/`; steps 7-9 read the item ids it lists.

After hand-editing `guia/data/*.js` keep them ASCII (non-ASCII as `\uXXXX`); in `index.html` use `&#N;` entities.

## Local preview

**Windows: double-click `Start-Atlas.bat`.** It checks Python and Node.js, finds (or asks for) your Star Technology
folder, builds the data the first time, starts the web server and opens the Atlas in your browser. Use
`Rebuild-Atlas-Data.bat` to force a full data rebuild. No terminal needed; see
[docs/atlas-3d.md](docs/atlas-3d.md) for the picture-by-picture guide, common mistakes and the 3D controls.

From a terminal instead (Linux/macOS/Git Bash, or PowerShell after `cd` to the repo folder):

```bash
scripts/serve.sh          # or .\scripts\serve.ps1 ; same as: cd guia && python -m http.server 8765
# open http://127.0.0.1:8765/index.html
```

Wiki site preview:

```bash
pip install -r requirements.txt
mkdocs serve              # wiki at http://127.0.0.1:8000
```

## License

Code and original text: MIT (see [LICENSE](LICENSE)). Third-party names and content: see [NOTICE.md](NOTICE.md).
Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).
