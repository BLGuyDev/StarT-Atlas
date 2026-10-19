# Viewing the 3D assembly lines

The interactive Atlas (`guia/`) can show any production line as a **3D scene**: machines as real blocks laid out
left to right, drawers as buffers, tanks for fluids, and pipes for every connection. This viewer is **not** part of the
published wiki site, because it needs textures taken from your own copy of the modpack. You run it locally, on your
own PC, from the files of your own Star Technology installation.

## Fast path (Windows, no terminal)

You do not need to type anything. You double-click one file.

```
+------------------+   +---------------------+   +----------------------+   +--------------------+   +----------------------+
| 1. Get the files |   | 2. Double-click     |   | 3. First run only:   |   | 4. Wait for the    |   | 5. PLAN tab ->       |
|    (Download ZIP |-->|    Start-Atlas.bat  |-->|    pick your Star    |-->|    build. Your     |-->|    open a module ->  |
|    or git clone) |   |    in that folder   |   |    Technology folder |   |    browser opens   |   |    green "3D         |
|                  |   |                     |   |    (has mods+kubejs) |   |    by itself       |   |    assembly line"    |
+------------------+   +---------------------+   +----------------------+   +--------------------+   +----------------------+
```

Install these **once** before you start (the launcher tells you if one is missing):

| Program | Download | Important |
|---|---|---|
| Python 3.10 or newer | <https://www.python.org/downloads/> | On the first installer screen tick **Add python.exe to PATH**. |
| Node.js (LTS) | <https://nodejs.org/> | Click Next through the installer. |

Prefer one line each in a terminal? `winget install -e --id Python.Python.3.12` and
`winget install -e --id OpenJS.NodeJS.LTS`.

### What you will see, step by step

| Step | What you do | What you will see |
|---|---|---|
| **1. Get the files** | On the GitHub page press the green **Code** button, then **Download ZIP**. Right-click the ZIP, choose **Extract All...**, and open the new folder. (Or use `git clone`; see *Advanced*.) | A normal Explorer window with `Start-Atlas.bat`, `README.md` and the folders `guia`, `scripts` and `docs`. |
| **2. Double-click `Start-Atlas.bat`** | Double-click it. If a blue **Windows protected your PC** box appears, press **More info**, then **Run anyway** (the file is plain text; you can open it in Notepad first). | A black console window titled *Star Technology Atlas* with a cyan header and numbered lines: `[1/6] Checking Python and Node.js...`, `[2/6] ...`. Green `OK` lines mean fine. |
| **3. Pick your Star Technology folder (first run only)** | If the launcher cannot find your game by itself, a window opens titled *Select your Star Technology instance folder (the one that contains mods and kubejs)*. Browse to your instance (for example `D:\Games\Star Technology`, or the CurseForge `Instances\Star Technology` folder) and press **OK**. | A standard Windows *Browse For Folder* window. If the folder has no `mods` and `kubejs`, the console says so and the window opens again. Your choice is saved in `extract\config.local.json`, so you are not asked again. |
| **4. Wait for the build (first run only)** | Do nothing and do not close the console. | `[4/6]` prints *This takes several minutes the first time*, then `== Step 1/10 ...` up to `Step 10/10` with the elapsed time. After it, `[5/6] Starting the local web server` and `[6/6] Opening your browser`, and your browser opens the Atlas. Later runs skip the build and start in seconds. |
| **5. Open a 3D view** | Click the **PLAN** tab, open a module card (expand *Diagram, step-by-step build and materials* if it is collapsed) and press the green **3D assembly line** button above the diagram. | The diagram is replaced by a 3D scene (the first time, the browser downloads three.js; wait a second). Press **Back to the diagram** to return. |

The console window must stay open while you use the Atlas: it is the small web server. **Close the window to stop it.**
Next time, just double-click `Start-Atlas.bat` again.

A second launcher exists: **`Rebuild-Atlas-Data.bat`** forces a full rebuild of the generated data (use it after the
modpack is updated, or if icons or 3D blocks look wrong). It does not start the server.

### Common mistakes

| What went wrong | Why it fails | What to do instead |
|---|---|---|
| Opened PowerShell in `C:\WINDOWS\System32` and typed a script name | A terminal looks for files in the folder it is *in*, and `System32` does not contain this project. | Skip the terminal: double-click `Start-Atlas.bat`. If you do use a terminal, first run `cd "D:\Games\StarT-Atlas"` (your own repo folder) and check with `dir`; see *Advanced*. |
| Typed `scripts/build_all` | PowerShell needs `.\` in front of a file in the current folder and the full file name with `.ps1`. `scripts/build_all` is not a command. | Type `.\scripts\build_all.ps1`, or simply double-click `Start-Atlas.bat` or `Rebuild-Atlas-Data.bat`. |
| Pasted two commands on one line | The second command became part of the first one, so both failed or did the wrong thing. | Paste **one command, press Enter, wait for it to finish**, then paste the next. The Advanced section has one command per block. |
| Double-clicked `guia\index.html` | The page opens as a local file (`file://`) and cannot load its data and textures, so the 3D view is empty or missing. | Open the Atlas through the launcher only. It opens `http://127.0.0.1:8765/index.html` for you. |
| *Python was not found* | Python is not installed, or it was installed without **Add python.exe to PATH**. | Install it from <https://www.python.org/downloads/> and tick **Add python.exe to PATH**. If it is already installed without the tick, run the installer again and choose **Modify**. Then double-click the launcher again (an already open window will not see the change). |
| *That folder has no "mods" and "kubejs"* | You picked a parent folder, a sub-folder, or another game. | Pick the instance folder itself: the one that shows `mods`, `kubejs` and `config` inside. In the CurseForge app: instance **...** menu > **Open Folder**. |
| The console closes instantly | You started the `.ps1` file or something other than the launcher. | Double-click `Start-Atlas.bat`. On an error it stays open and says *Press any key to continue*. |
| The browser says the site cannot be reached | The console window was closed, so the server stopped. | Double-click `Start-Atlas.bat` again and leave its window open. |
| 3D says *could not load (offline?)* | The viewer loads three.js from public CDNs the first time you use it. | Check your connection or ad blocker, then press the button again. |

## Advanced: the same thing from a terminal

Only needed on Linux/macOS, or if you want to see what the launcher does. Run **one command per step, press Enter,
and wait for it to finish** before pasting the next. On Windows, open **PowerShell** from the Start menu. It starts
in your user folder (or even `C:\WINDOWS\System32`), not in the project, so always begin with `cd`.

### 1. Get the repository and go into its folder

```bash
git clone https://github.com/BLGuyDev/StarT-Atlas.git
```

Replace the example with the folder where **you** unpacked or cloned it. Quote the path if it has spaces:

```powershell
cd "D:\Games\StarT-Atlas"
```

Check that you are in the right place. The list must show `README.md` and a `scripts` folder:

```powershell
dir
```

Install the two Python packages used by the extractor (Pillow and numpy):

```powershell
python -m pip install -r requirements-extract.txt
```

### 2. Point the scripts at your modpack

Set `STAR_PACK_DIR` to the instance folder (the one that contains `mods/` and `kubejs/`). The launcher does this for
you and saves it in `extract/config.local.json`; by hand you can use either way.

Windows PowerShell (lasts only for the current window):

```powershell
$env:STAR_PACK_DIR = 'D:\Games\Star Technology'
```

Linux / macOS / Git Bash:

```bash
export STAR_PACK_DIR="/path/to/Star Technology"
```

Or create the file `extract/config.local.json` (ignored by git):
`{"pack_dir": "D:/Games/Star Technology", "vanilla_jar": "D:/path/to/1.20.1.jar", "gt_src": "D:/path/to/gtsrc"}`.
Only `pack_dir` is required. Outside the CurseForge folder layout also set `STAR_VANILLA_JAR` (or `vanilla_jar`) to the
Minecraft 1.20.1 jar.

### 3. Build all the generated data (this also builds the 3D textures)

Windows PowerShell, from the repository folder. Note the leading `.\` and the `.ps1` ending:

```powershell
.\scripts\build_all.ps1
```

If PowerShell says *running scripts is disabled on this system*, allow it for this window only (first command), then
run the build line above again (second command):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Linux / macOS / Git Bash:

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

It can take several minutes. If a step fails, the message names the step; read the lines above it, fix the cause and run
the script again.

### 4. Start the local server

Windows PowerShell:

```powershell
.\scripts\serve.ps1
```

Linux / macOS / Git Bash:

```bash
scripts/serve.sh
```

Both do the same as `cd guia` followed by `python -m http.server 8765`. Open
**<http://127.0.0.1:8765/index.html>** in a browser. Use that address and not a `file://` path: the page loads its data
and textures over HTTP.

### 5. Launcher options

`Start-Atlas.bat` passes its arguments to `scripts/start_atlas.ps1`. Try `.\Start-Atlas.bat -Check` from the
repository folder to see what it would do without changing anything.

| Option | Effect |
|---|---|
| `-Check` | Only report what is installed, which pack folder it found and which generated files are missing. |
| `-Rebuild` | Rebuild the generated data even if it exists (same as `Rebuild-Atlas-Data.bat`). |
| `-NoBrowser` | Start the server but do not open the browser. |
| `-NoServer` | Do everything except starting the server. |
| `-Port 9000` | First port to try. The default is 8765; if it is busy the next free one is used. |

## Open a 3D view

1. Click the **PLAN** tab (or an era tab such as **LV**, **MV**, **HV**).
2. Open a module card (PLAN) or scroll to a setup (era tabs). In the PLAN, expand
   *Diagram, step-by-step build and materials* if the card is collapsed.
3. Press **3D assembly line** above the diagram. The first time, the browser downloads three.js, so wait a
   second. The diagram is replaced by the 3D scene.
4. Press **Back to the diagram** to return. Only one 3D view is live at a time; opening another closes the
   first.

You can also jump straight to a module with a link such as `index.html#plan-sieves`
(`#plan-<module id>` and `#phase-<phase id>` open the right phase and scroll to the card).

## Controls

| Action | How |
|---|---|
| Rotate | Drag with the left mouse button |
| Zoom | Mouse wheel |
| Pan | Drag with the right mouse button |
| Show the name of a block | Hover over it |
| Restore the camera | **Reset view** |
| Hide or show the floating labels | **Labels on/off** |
| Go back to the flat diagram | **Back to the diagram** |

## How to read a scene

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
| The scene is empty or all blocks are grey | `guia/data/blocks3d.js` or `guia/img/blocks.png` are missing or stale. Double-click `Rebuild-Atlas-Data.bat`. |
| Icons are letters on grey tiles | The icon atlas is missing. Double-click `Rebuild-Atlas-Data.bat`. |
| A block is missing from a hand-built scene | Its id has no texture in `blocks3d.js`. Check the id spelling in the chain's `s3d`, or rebuild with `Rebuild-Atlas-Data.bat`. |
| Nothing loads, console says `file://` or CORS errors | You opened `index.html` straight from disk. Use the launcher (`Start-Atlas.bat`). |
| The launcher or scripts complain about the pack folder | The folder is unset or wrong. It must contain `mods` and `kubejs`. Delete `extract\config.local.json` (and clear `STAR_PACK_DIR` if you set it), then double-click `Start-Atlas.bat` to pick the folder again. |
| The build stops at a step | The message names the step number and script. Read the lines just above it. A missing Minecraft jar is fixed by setting `vanilla_jar` in `extract\config.local.json`. |
| Everything works but the view is tiny on a phone | Use two fingers to pinch-zoom the scene. The viewer is meant for a laptop-sized screen; the diagrams above it also work on phones. |

## Why the wiki site does not show the 3D scenes

The public wiki (GitHub Pages) is rendered by MkDocs from the Markdown pages and shows each line as machine
panels. The 3D viewer needs the generated textures, which derive from the modpack and its mods and are therefore not
in this repository. Everybody who plays the pack can build them locally with the launcher.
