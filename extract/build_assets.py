"""Build icon atlas (guia/img/atlas.png + data/icons.js) and multiblock renders (guia/img/m/<id>.png)."""
import json, os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
import icons
import icons_model
from common import name, GUIA
from PIL import Image

G = GUIA
os.makedirs(os.path.join(G, "img", "m"), exist_ok=True)


def load_js(fn, var):
    t = open(os.path.join(G, "data", fn), encoding="utf-8").read()
    return json.loads(t[t.index("=") + 1:].rstrip().rstrip(";"))


Q = load_js("quests.js", "QUESTS")
M = load_js("multis.js", "MULTIS")
import glob
guide = "".join(open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(G, "data", "guide*.js"))))

ids = set(re.findall(r"'([a-z0-9_]+:[a-z0-9_./]+)'", guide))
for _fn in ("app2.js", "route.js", "view3d.js"):  # ids written literally in the page scripts (e.g. the magnet table in app2.js)
    ids |= set(re.findall(r"'([a-z0-9_]+:[a-z0-9_./]+)'", open(os.path.join(G, "data", _fn), encoding="utf-8").read()))
import subprocess
try:
    ids |= set(json.loads(subprocess.run(["node", os.path.join(HERE, "guide_ids.js")], capture_output=True, text=True, encoding="utf-8", check=True).stdout))
except Exception as e:
    print("guide_ids.js failed", e)
for q in Q:
    for it in q["items"]:
        ids.add(it["id"])
for m in M:
    ids.add(m["id"])
    for s in m["s"]:
        if s.get("id"):
            ids.add(s["id"])
        for r in s.get("r", []):
            for a in r["in"]:
                ids.add(a[0])
    for r in m["r"]:
        for a in r["in"]:
            ids.add(a[0])
        for k, v in (r.get("k") or {}).items():
            ids.add(v[0])
for h in ["gtceu:lv_muffler_hatch", "gtceu:maintenance_hatch", "gtceu:lv_energy_input_hatch", "gtceu:lv_input_bus", "gtceu:lv_output_bus", "gtceu:lv_input_hatch", "gtceu:lv_output_hatch", "gtceu:iv_parallel_hatch", "gtceu:hv_rotor_holder", "gtceu:lv_energy_output_hatch", "gtceu:steam_input_bus", "gtceu:steam_output_bus", "gtceu:steam_hatch", "gtceu:data_access_hatch", "gtceu:computation_data_reception_hatch", "gtceu:object_holder", "gtceu:passthrough_hatch_item"]:
    ids.add(h)
# ids referenced by the merged recipe set + tag aliases
RJS = json.loads(open(os.path.join(G, "data", "recipes.js"), encoding="utf-8").read().split("=", 1)[1].rstrip().rstrip(";"))
tags = set()
for k, r in RJS.items():
    ids.add(k)
    for a, _ in r["in"]:
        (tags if a.startswith("#") else ids).add(a)
    for v in (r.get("k") or {}).values():
        (tags if v.startswith("#") else ids).add(v)
for m in M:
    for s in m["s"]:
        for r in s.get("r", []):
            for a in r["in"]:
                if a[0].startswith("#"):
                    tags.add(a[0])
VAN = {"iron", "copper", "gold", "netherite"}
FIXED = {"#thermal:glass/hardened": "thermal:obsidian_glass",  # tag members: obsidian / signalum / lumium / enderium glass (TCoreTagsProvider)
         "#forge:rods/wooden": "minecraft:stick", "#forge:dusts/redstone": "minecraft:redstone", "#forge:dusts/glowstone": "minecraft:glowstone_dust",
         "#minecraft:planks": "minecraft:oak_planks", "#minecraft:logs": "minecraft:oak_log", "#minecraft:logs_that_burn": "minecraft:oak_log",
         "#minecraft:wooden_slabs": "minecraft:oak_slab", "#forge:stone": "minecraft:stone", "#forge:cobblestone": "minecraft:cobblestone",
         "#minecraft:wool": "minecraft:white_wool", "#forge:glass": "minecraft:glass", "#forge:glass_panes": "minecraft:glass_pane",
         "#forge:stripped_logs": "minecraft:stripped_oak_log", "#exnihilosequentia:sieves": "exnihilosequentia:oak_sieve",
         "#forge:string": "minecraft:string", "#forge:chests": "minecraft:chest", "#forge:chests/wooden": "minecraft:chest",
         "#minecraft:stone_crafting_materials": "minecraft:cobblestone", "#forge:sand": "minecraft:sand", "#forge:gravel": "minecraft:gravel",
         "#forge:slimeballs": "minecraft:slime_ball", "#forge:obsidian": "minecraft:obsidian", "#forge:ender_pearls": "minecraft:ender_pearl",
         "#forge:gunpowder": "minecraft:gunpowder", "#minecraft:coals": "minecraft:coal", "#forge:dusts/coal": "gtceu:coal_dust",
         "#forge:gems/diamond": "minecraft:diamond", "#forge:gems/emerald": "minecraft:emerald", "#forge:gems/quartz": "minecraft:quartz",
         "#forge:gems/lapis": "minecraft:lapis_lazuli", "#minecraft:wooden_buttons": "minecraft:oak_button", "#forge:rods/blaze": "minecraft:blaze_rod",
         "#minecraft:sand": "minecraft:sand", "#forge:feathers": "minecraft:feather", "#forge:leather": "minecraft:leather",
         "#sgjourney:refined_naquadah": "sgjourney:refined_naquadah", "#sgjourney:naquadah_alloy": "sgjourney:naquadah_alloy",
         "#ae2:all_certus_quartz": "ae2:certus_quartz_crystal", "#ae2:all_fluix": "ae2:fluix_crystal", "#ae2:all_nether_quartz": "minecraft:quartz",
         "#ae2:all_quartz_dust": "ae2:certus_quartz_dust", "#ae2:pattern_provider": "ae2:pattern_provider", "#forge:crops/flax": "thermal:flax",
         "#gtceu:diodes": "gtceu:diode", "#gtceu:pistons": "minecraft:piston", "#minecraft:coral_plants": "minecraft:tube_coral", "#minecraft:coral_blocks": "minecraft:tube_coral_block", "#minecraft:fishes": "minecraft:cod", "#minecraft:saplings": "minecraft:oak_sapling", "#forge:slag": "thermal:slag", "#ae2:illuminated_panel": "ae2:monitor", "#minecraft:logs_that_burn": "minecraft:oak_log",
         "#forge:mushrooms": "minecraft:red_mushroom", "#minecraft:oak_logs": "minecraft:oak_log", "#minecraft:soul_fire_base_blocks": "minecraft:soul_sand",
         "#minecraft:smelts_to_glass": "minecraft:sand", "#minecraft:convertable_to_mud": "minecraft:dirt", "#forge:rods": "minecraft:stick"}
ALIAS = {}
for t in tags:
    a = FIXED.get(t)
    m = re.match(r"^#gtceu:circuits/([a-z]+)$", t)
    if m:
        a = f"kubejs:{m.group(1)}_universal_circuit"
    m = re.match(r"^#forge:(ingots|plates|rods|gears|dusts|nuggets|gems|storage_blocks|wires|foils|screws|bolts|rings|springs)/([a-z_]+)$", t)
    if not a and m:
        kind, mat = m.groups()
        if mat in VAN and kind in ("ingots", "nuggets", "storage_blocks"):
            a = f"minecraft:{mat}_" + {"ingots": "ingot", "nuggets": "nugget", "storage_blocks": "block"}[kind]
        else:
            a = "gtceu:" + {"ingots": f"{mat}_ingot", "plates": f"{mat}_plate", "rods": f"{mat}_rod", "gears": f"{mat}_gear", "dusts": f"{mat}_dust",
                            "nuggets": f"{mat}_nugget", "gems": f"{mat}_gem", "storage_blocks": f"{mat}_block", "wires": f"{mat}_single_wire",
                            "foils": f"{mat}_foil", "screws": f"{mat}_screw", "bolts": f"{mat}_bolt", "rings": f"{mat}_ring", "springs": f"{mat}_spring"}[kind]
    if not a and "tools/" not in t:
        a = "minecraft:" + t.split("/")[-1].split(":")[-1]
        if icons_model.icon64(a) is None:
            a = None  # guessed id does not exist: leave the tag without alias instead of inventing an item
    if a:
        ALIAS[t] = a
        ids.add(a)
for t in ["ulv", "lv", "mv", "hv", "ev", "iv", "luv", "zpm", "uv", "uhv", "uev", "uiv", "uxv"]:
    ids.add(f"kubejs:{t}_universal_circuit")
# app2.js hatchesOf() builds energy / muffler hatch ids per era tier at runtime
for t in ["lv", "mv", "hv", "ev", "iv", "luv", "zpm", "uv", "uhv", "uev", "uiv"]:
    for k in ("energy_input_hatch", "muffler_hatch"):
        ids.add(f"gtceu:{t}_{k}")
ids = sorted(i for i in ids if isinstance(i, str) and ":" in i and not i.startswith(("#", "http")) and " " not in i)
print(len(ids), "ids")

raw = {m["id"]: m for m in json.load(open(os.path.join(HERE, "multis.json"), encoding="utf-8"))}
RENDERS = {}
for m in M:
    r = raw.get(m["id"])
    try:
        im = icons.render_multi(r) if r else None
    except Exception as e:
        print("render fail", m["id"], e)
        im = None
    if im is not None:
        RENDERS[m["id"]] = im


def thumb(im):
    w, h = im.size
    s = 64 / max(w, h)
    t = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    out = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    out.alpha_composite(t, ((64 - t.width) // 2, (64 - t.height) // 2))
    return out


# GT steam machines have no static models (built at runtime): bronze/steel steam casing + the machine's own overlay.
for _pre, _cas in (("lp_steam_", "bronze"), ("hp_steam_", "steel")):
    for _m, _ov in (("forge_hammer", "machines/forge_hammer"), ("solid_boiler", "generators/boiler/coal"), ("liquid_boiler", "generators/boiler/lava"),
                    ("alloy_smelter", "machines/alloy_smelter"), ("macerator", "machines/macerator"), ("compressor", "machines/compressor"),
                    ("extractor", "machines/extractor"), ("furnace", "machines/furnace"), ("rock_crusher", "machines/rock_crusher"), ("miner", "machines/miner")):
        icons.KJS_MODEL.setdefault(_pre + _m, (f"gtceu:block/casings/steam/{_cas}/side", f"gtceu:block/{_ov}"))

icons.KJS_MODEL.setdefault('lv_pulverizer', ('gtceu:block/casings/voltage/lv/side', 'gtceu:block/machines/pulverizer'))
COLS = 32
imgs, idx, miss = [], {}, []
for i in ids:
    try:
        im = icons_model.icon64(i)
    except Exception as e:
        im = None
    if im is None and i in RENDERS:
        im = thumb(RENDERS[i])
    if im is None:
        miss.append(i)
        continue
    idx[i] = len(imgs)
    imgs.append(im.convert("RGBA").resize((64, 64), Image.NEAREST))
rows = (len(imgs) + COLS - 1) // COLS
atlas = Image.new("RGBA", (COLS * 64, rows * 64), (0, 0, 0, 0))
for n, im in enumerate(imgs):
    atlas.alpha_composite(im, ((n % COLS) * 64, (n // COLS) * 64))
atlas.save(os.path.join(G, "img", "atlas.png"), optimize=True)
names = {i: name(i) for i in ids}
# tags drawn directly (e.g. in small recipe views) share the icon of their representative item
for _t, _a in ALIAS.items():
    if _a in idx and _t not in idx:
        idx[_t] = idx[_a]
with open(os.path.join(G, "data", "icons.js"), "w", encoding="utf-8") as f:
    f.write("window.ICONS=" + json.dumps({"cols": COLS, "px": 64, "i": idx, "n": names, "alias": ALIAS}, ensure_ascii=True, separators=(",", ":")) + ";\n")
print("atlas", atlas.size, "icons", len(imgs), "missing", len(miss))
print("missing all:", miss)
print("aliased ids:", icons_model.ALIAS_HITS)

# renders
done = 0
for m in M:
    im = RENDERS.get(m["id"])
    if im is None:
        continue
    im.save(os.path.join(G, "img", "m", m["id"].split(":")[1] + ".png"), optimize=True)
    m["img"] = 1
    m["w"], m["h"] = im.size
    done += 1
with open(os.path.join(G, "data", "multis.js"), "w", encoding="utf-8") as f:
    f.write("window.MULTIS=" + json.dumps(M, ensure_ascii=True, separators=(",", ":")) + ";\n")
print("renders", done)
