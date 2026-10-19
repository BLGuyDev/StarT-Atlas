# Viewing the 3D assembly lines

The interactive Atlas (`guia/`) can show any production line as a **3D scene**: machines as real blocks laid out
left to right, drawers as buffers, tanks for fluids, and pipes for every connection. This viewer is **not** part of the
published wiki site, because it needs textures taken from your own copy of the modpack. You run it locally, in
about ten minutes. The steps below assume nothing is installed yet.

## What you need

| Requirement | Why |
|---|---|
| A Star Technology instance (a CurseForge/Prism folder with `mods/` and `kubejs/`) | The block textures and item data are built from your own files. They are not distributed in this repository. |
| Python 3.10 or newer | Runs the extraction scripts. |
| Node.js (any recent LTS) | Builds the wiki data and one helper script. |
| Git | To clone the repository. |
| Internet access when you open a 3D view | The viewer loads three.js from public CDNs the first time you use it (see *Troubleshooting*). |

## Step by step

### 1. Get the repository

```bash
git clone https://github.com/BLGuyDev/StarT-Atlas.git
cd StarT-Atlas
pip install -r requirements-extract.txt   # Pillow and numpy
```

### 2. Point the scripts at your modpack

Set `STAR_PACK_DIR` to the instance folder (the one that contains `mods/` and `kubejs/`).

```powershell
# Windows PowerShell
$env:STAR_PACK_DIR = 'D:/path/to/Star Technology'
```
```bash
# Linux / macOS / Git Bash
export STAR_PACK_DIR="/path/to/Star Technology"
```

If you prefer a file, create `extract/config.local.json` (ignored by git):
`{"pack_dir": "...", "vanilla_jar": "...", "gt_src": "..."}`. If your launcher is not CurseForge, also set
`STAR_VANILLA_JAR` to the Minecraft 1.20.1 jar.

### 3. Build all the generated data (this also builds the 3D textures)

```powershell
./scripts/build_all.ps1
```
```bash
scripts/build_all.sh
```

The script downloads the StarT GregTech fork sources into `gtsrc/` the first time, then runs ten steps. The ones that
matter for 3D are:

| Step | Output | What it is for |
|---|---|---|
| 8 `extract/build_assets.py` | `guia/img/atlas.png`, `guia/data/icons.js` | Item icons (the drawers and labels in the scenes use them). |
| 9 `extract/build_3d.py` | `guia/img/blocks.png`, `guia/data/blocks3d.js` | The 3D block textures (top, side, front faces) and the multiblock structures. |
| 10 `tools/build_data.js` | `guia/data/wiki-data.js` | The chain, plan and era data read from `docs/`. |

It can take several minutes. If a step fails, the message names the missing path; fix it and run the script again.

### 4. Start the local server

```powershell
./scripts/serve.ps1
```
```bash
scripts/serve.sh      # same as: cd guia && python -m http.server 8765
```

Open **<http://127.0.0.1:8765/index.html>** in a browser. Use the address above and not a `file://` path: the page
loads its data and textures over HTTP.

### 5. Open a 3D view

1. Click the **PLAN** tab (or an era tab such as **LV**, **MV**, **HV**).
2. Open a module card (PLAN) or scroll to a setup (era tabs). In the PLAN, expand
   *Diagram, step-by-step build and materials* if the card is collapsed.
3. Press **▶ 3D assembly line** above the diagram. The first time, the browser downloads three.js, so wait a
   second. The diagram is replaced by the 3D scene.
4. Press **■ Back to the diagram** to return. Only one 3D view is live at a time; opening another closes the
   first.

You can also jump straight to a module with a link such as `index.html#plan-sieves`
(`#plan-<module id>` and `#phase-<phase id>` open the right phase and scroll to the card).

### 6. Controls

| Action | How |
|---|---|
| Rotate | Drag with the left mouse button |
| Zoom | Mouse wheel |
| Pan | Drag with the right mouse button |
| Show the name of a block | Hover over it |
| Restore the camera | **Reset view** |
| Hide or show the floating labels | **Labels on/off** |

### 7. How to read a scene

* **Blocks**: real machine and casing textures from your pack. Multiblocks are drawn at their real footprint.
* **Drawers** with an item icon are the buffer in front of each machine (the method used throughout this guide).
* **Tanks** are fluid buffers.
* **Pipes**: grey = items (`i`), blue = fluids (`f`), amber = power (`p`), brown = rotation / Create shafts (`r`).
* **Labels** carry the real numbers of the line (EU/t, seconds, rates). If two labels touch, use *Labels on/off* or
  zoom in.

## Which lines have a hand-built scene

Every chain gets an **automatic scene** (machines placed in columns by dependency, drawers and pipes generated from
the diagram data). Eight lines also have a **hand-built, to-scale layout**:

`power_steam_engine`, `rubber`, `sieve_block4`, `treated_wood`, `comp_stock` (and `comp_motor`, same scene),
`lv_hull_line` and `mv_hull_line`.

These live in the chain data as `s3d`, in the front matter of the chain pages under `docs/chains/`:

```yaml
s3d:
  b: [[block id, x, y, z, dx, dy, dz, "label"], ...]   # blocks; dx/dy/dz fill a box
  p: [[kind, [x, y, z], [x, y, z], ...], ...]          # pipe polylines (kind = i items, f fluids, p power, r rotation)
  l: [["text", x, y, z], ...]                          # floating labels
```

To add or fix a scene, edit that block in the chain page, run `node tools/build_data.js`, reload the browser and open
the 3D view. Keep labels at least 1.5 blocks apart, and use only block ids that have a texture in
`guia/data/blocks3d.js` (ids without a texture are skipped silently).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The button says **3D could not load (offline?)** | The viewer loads `three.js` r128 from `cdnjs.cloudflare.com` and `OrbitControls` from `cdn.jsdelivr.net`. Check your connection, a firewall or an ad blocker, then press the button again. |
| The scene is empty or all blocks are grey | `guia/data/blocks3d.js` or `guia/img/blocks.png` are missing or stale. Run step 9 (`python extract/build_3d.py`) again after step 8. |
| Icons are letters on grey tiles | The icon atlas is missing. Run step 8 (`python extract/build_assets.py`). |
| A block is missing from a hand-built scene | Its id has no texture in `blocks3d.js`. Check the id spelling in the chain's `s3d`, or rebuild step 9. |
| Nothing loads, console says `file://` or CORS errors | You opened `index.html` straight from disk. Use the local server in step 4. |
| `STAR_PACK_DIR` error from the scripts | The variable is unset or points to the wrong folder. It must contain `mods/` and `kubejs/`. |
| Everything works but the view is tiny on a phone | Use two fingers to pinch-zoom the scene. The viewer is meant for a laptop-sized screen; the diagrams above it also work on phones. |

## Why the wiki site does not show the 3D scenes

The public wiki (GitHub Pages) is rendered by MkDocs from the Markdown pages and shows each line as machine
panels. The 3D viewer needs the generated textures, which derive from the modpack and its mods and are therefore not
in this repository. Everybody who plays the pack can build them locally with the steps above.
