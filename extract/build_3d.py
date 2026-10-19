"""Build 3D assets for the guide's line viewer.
- img/blocks.png: 32 px face atlas (top, side, front per block) for every machine/structure block the guide places.
- data/blocks3d.js: window.BLOCKS3D = {cols, px, f: {id: [top, side, front]}, s: {multi_id: {d:[w,h,l], b:[[x,y,z,key],...], k:{key: block_id}}}}
Faces come from the pack's own block models (icons.block_faces / controller_faces); items without a block model fall back to their icon.
Run after build_assets.py (needs guide*.js, multis.json)."""
import json, os, re, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
import icons, icons_model
from common import GUIA

HERE = os.path.dirname(os.path.abspath(__file__))
G = GUIA
PX = 32

import glob
guide = "".join(open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(G, "data", "guide*.js"))))
# machine-ish nodes: ['key', 'label', 'm'|'p'|'s', 'id'] plus every id the BOMs mention
node_ids = set(re.findall(r"\['[a-z0-9_]+',\s*'[^']*',\s*'[mps]',\s*'([a-z0-9_]+:[a-z0-9_./]+)'", guide))
# ids placed in hand-built scenes: ['mod:id', x, y, z, ...]
node_ids |= set(re.findall(r"\['([a-z0-9_]+:[a-z0-9_./]+)',\s*-?\d", guide))
EXTRA = ["functionalstorage:oak_1", "create:fluid_tank", "minecraft:smooth_stone", "pipez:item_pipe", "pipez:fluid_pipe", "gtceu:tin_single_cable",
         "create:shaft", "create:belt_connector", "minecraft:water", "minecraft:lava", "gtceu:lv_machine_casing", "create:andesite_casing"]
raw = {m["id"]: m for m in json.load(open(os.path.join(HERE, "multis.json"), encoding="utf-8"))}

structs, need = {}, set(node_ids) | set(EXTRA)
for mid in sorted(node_ids):
    m = raw.get(mid)
    if not m or not m.get("aisles"):
        continue
    keys, cells = {}, []
    for ch, sym in m["symbols"].items():
        if "controller" in sym["special"]:
            keys[ch] = mid
        elif sym["blocks"]:
            keys[ch] = sym["blocks"][0]
        elif "coil" in sym["special"]:
            keys[ch] = "gtceu:cupronickel_coil_block"
        elif sym["abilities"] and not ("air" in sym["special"] or "any" in sym["special"]):
            keys[ch] = "gtceu:lv_machine_casing"
    W = max(len(r) for a in m["aisles"] for r in a)
    for z, a in enumerate(m["aisles"]):
        for y, row in enumerate(a):
            for x, ch in enumerate(row):
                if ch in keys and keys[ch] not in ("minecraft:air",):
                    cells.append([W - 1 - x, y, z, ch])
    if not cells:
        continue
    structs[mid] = {"d": [W, max(c[1] for c in cells) + 1, len(m["aisles"])], "b": cells, "k": keys}
    need |= set(keys.values())


# KubeJS blocks: .create('name') ... .textureAll('tex'); KubeJS machines: workableCasingModel(casing, overlays)
KJS_TEX = {}
for root, _, files in os.walk(os.path.join(HERE, "..", "..", "kubejs", "startup_scripts")):
    for fn in files:
        if not fn.endswith(".js"):
            continue
        src = open(os.path.join(root, fn), encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r"\.create\(\s*'([a-z0-9_]+)'[^;]*?\.textureAll\(\s*'([^']+)'", src, re.S):
            KJS_TEX.setdefault(m.group(1), m.group(2))
        for m in re.finditer(r"\.create\(\s*'([a-z0-9_]+)'[^;]*?\.workableCasingModel\(\s*'([^']+)'\s*,\s*'([^']+)'", src, re.S):
            icons.KJS_MODEL.setdefault(m.group(1), (m.group(2), m.group(3)))
for _pre, _cas in (("lp_steam_", "bronze"), ("hp_steam_", "steel")):
    for _m, _ov in (("forge_hammer", "machines/forge_hammer"), ("solid_boiler", "generators/boiler/coal"), ("alloy_smelter", "machines/alloy_smelter")):
        icons.KJS_MODEL.setdefault(_pre + _m, (f"gtceu:block/casings/steam/{_cas}/side", f"gtceu:block/{_ov}"))


icons.KJS_MODEL.setdefault('lv_pulverizer', ('gtceu:block/casings/voltage/lv/side', 'gtceu:block/machines/pulverizer'))
icons.KJS_MODEL.setdefault('kiln', ('minecraft:block/mud_bricks', 'gtceu:block/multiblock/primitive_blast_furnace'))
KJS_TEX.setdefault('mesh_block', KJS_TEX.get('meshblock', 'kubejs:block/misc/meshblock'))


def faces(bid):
    ns0, p0 = icons.rl(bid)
    if ns0 == "kubejs" and p0 in KJS_TEX:
        t = icons.tex(KJS_TEX[p0])
        if t is not None:
            return t, t, t
    for fn in (icons.block_faces, icons.controller_faces):
        try:
            f = fn(bid)
        except Exception:
            f = None
        if f and any(x is not None for x in f):
            T, F, S = f
            return T or F or S, S or T or F, F or S or T
    ns, path = icons.rl(bid)
    if path in icons.KJS_MODEL:
        cas, ovf = icons.KJS_MODEL[path]
        C = icons.tex(cas)
        return C, icons.comp(C, icons.tex(ovf + "/overlay_side")) or C, icons.comp(C, icons.tex(ovf + "/overlay_front")) or C
    try:
        im = icons_model.icon64(bid)
    except Exception:
        im = None
    if im is not None:
        return im, im, im
    return None


def sq(im):
    im = im.convert("RGBA")
    if im.size != (PX, PX):
        im = im.resize((PX, PX), Image.NEAREST)
    return im


cells, index, miss = [], {}, []
for bid in sorted(need):
    f = faces(bid)
    if not f:
        miss.append(bid)
        continue
    index[bid] = [len(cells), len(cells) + 1, len(cells) + 2]
    cells += [sq(f[0]), sq(f[1]), sq(f[2])]
COLS = 32
rows = (len(cells) + COLS - 1) // COLS
atlas = Image.new("RGBA", (COLS * PX, max(1, rows) * PX), (0, 0, 0, 0))
for n, im in enumerate(cells):
    atlas.alpha_composite(im, ((n % COLS) * PX, (n // COLS) * PX))
atlas.save(os.path.join(G, "img", "blocks.png"), optimize=True)
with open(os.path.join(G, "data", "blocks3d.js"), "w", encoding="utf-8") as fh:
    fh.write("window.BLOCKS3D=" + json.dumps({"cols": COLS, "px": PX, "rows": rows, "f": index, "s": structs}, ensure_ascii=True, separators=(",", ":")) + ";\n")
print(len(index), "blocks;", len(structs), "structures; atlas", atlas.size, "; no faces:", miss[:20])
