"""Merge KubeJS / jar / GT recipes, pick one per item, and emit guia/data/recipes.js for the BOM closure."""
import json, os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from common import GUIA, require_pack
G = GUIA
BASE = require_pack()
SS = os.path.join(BASE, "kubejs", "server_scripts")

kj = json.load(open(os.path.join(HERE, "recipes.json"), encoding="utf-8"))
KREC, REMOVED = kj["recipes"], set(kj["removed"])
JAR = json.load(open(os.path.join(HERE, "jar_recipes.json"), encoding="utf-8"))
GTM = json.load(open(os.path.join(HERE, "gt_machine_recipes.json"), encoding="utf-8"))

# KubeJS replaceInput({id:'x'}, 'old', 'new')
REPL = {}
for root, _, files in os.walk(SS):
    if "deprecated" in root:
        continue
    for f in files:
        if f.endswith(".js"):
            t = open(os.path.join(root, f), encoding="utf-8").read()
            for m in re.finditer(r"replaceInput\(\s*\{\s*id:\s*['\"]([^'\"]+)['\"]\s*\}\s*,\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]", t):
                REPL.setdefault(m.group(1), []).append((m.group(2), m.group(3)))

MC_EXPAND = {"hopper", "chest", "furnace", "piston", "sticky_piston", "dispenser", "observer", "comparator", "repeater", "anvil",
             "campfire", "soul_campfire", "crafting_table", "barrel", "blast_furnace", "smoker", "cauldron", "bucket", "flint_and_steel",
             "glass_pane", "iron_bars", "redstone_block", "lever", "composter"}


def is_base(i):
    if not i or i.startswith("#") or ":" not in i:
        return True
    ns, p = i.split(":", 1)
    if ns == "gtceu":
        return bool(re.search(r"_(ingot|plate|dust|rod|bolt|screw|gear|foil|nugget|gem|wire|spring|ring|round|rotor|lens|bucket)$", p)) or p.startswith(("raw_", "crushed_"))
    if ns == "minecraft":
        return p not in MC_EXPAND
    if ns == "create":
        return p in ("andesite_alloy", "brass_ingot", "zinc_ingot", "iron_sheet", "copper_sheet", "brass_sheet", "golden_sheet", "polished_rose_quartz", "rose_quartz", "cinder_flour", "wheat_flour", "dough", "precision_mechanism", "sturdy_sheet", "experience_nugget")
    return False


def norm(r, src):
    import idfix
    o = {"t": r.get("type", "crafting"), "o": r.get("out", 1), "in": [[k, v] for k, v in idfix.clean_inputs(r.get("in", {})).items()]}
    if r.get("grid"):
        o["g"] = r["grid"]
        o["k"] = {kk: idfix.clean_id(vv)[0] for kk, vv in r.get("keys", {}).items()}
    if r.get("fluids"):
        o["fl"] = r["fluids"]
    for k in ("eu", "circuit"):
        if r.get(k):
            o[k] = r[k]
    o["s"] = src
    rid = r.get("id")
    key = None
    if rid:
        short = rid.split(":", 1)[1].split("/")[-1]
        key = next((k for k in REPL if k == rid or (k.split(":")[0] == rid.split(":")[0] and k.split(":", 1)[1] == short)), None)
    if key:
        def same(a, old):
            if a == old:
                return True
            mm = re.match(r"^[a-z_]+:([a-z_]+)_ingot$", old)
            return bool(mm) and a == f"#forge:ingots/{mm.group(1)}"
        for old, new in REPL[key]:
            o["in"] = [[new if same(a, old) else a, n] for a, n in o["in"]]
            if o.get("k"):
                o["k"] = {k: (new if same(v, old) else v) for k, v in o["k"].items()}
        merged = {}
        for a, n in o["in"]:
            merged[a] = merged.get(a, 0) + n
        o["in"] = [[a, n] for a, n in merged.items()]
    return o


# Recipes the indexer gets wrong (KubeJS regex removals such as /thermal:dynamo*/, template loops) - checked by hand.
OVERRIDE = {
    "thermal:dynamo_lapidary": {"t": "assembler", "o": 1, "eu": "30", "s": "kubejs (modifications/thermal.js)",
                                "in": [["thermal:rf_coil", 1], ["gtceu:cobalt_brass_gear", 1], ["gtceu:lv_machine_hull", 1]], "fl": [["tin_alloy", "288"]]},
    "kubejs:lv_upgrade_kit": {"t": "assembler", "o": 1, "eu": "30", "s": "kubejs (power/thermal_augments.js)",
                              "in": [["gtceu:silver_plate", 4], ["thermal_extra:soul_infused_glass", 1], ["gtceu:bronze_gear", 1], ["#gtceu:circuits/lv", 1]], "fl": [["tin", "720"]]},
    "gtceu:lp_steam_forge_hammer": {"t": "crafting", "o": 1, "s": "gt",
                                    "in": [["gtceu:bronze_small_fluid_pipe", 6], ["minecraft:piston", 1], ["gtceu:bronze_machine_casing", 1], ["minecraft:anvil", 1]]},
    "gtceu:hp_steam_forge_hammer": {"t": "crafting", "o": 1, "s": "gt",
                                    "in": [["gtceu:lp_steam_forge_hammer", 1], ["gtceu:steel_plate", 1], ["gtceu:tin_alloy_small_fluid_pipe", 2], ["gtceu:wrought_iron_plate", 5]]},
    "gtceu:lp_steam_solid_boiler": {"t": "crafting", "o": 1, "s": "gt",
                                    "in": [["gtceu:bronze_plate", 5], ["minecraft:furnace", 1], ["minecraft:bricks", 2]]},
    "gtceu:hp_steam_solid_boiler": {"t": "crafting", "o": 1, "s": "gt",
                                    "in": [["gtceu:steel_plate", 5], ["minecraft:furnace", 1], ["minecraft:bricks", 2]]},
}


OVERRIDE["start_core:large_arboreal_extractor"] = {"t": "crafting", "o": 1, "s": "kubejs (multiblock_recipes/large_arboreal_extractor.js)",
    "in": [["gtceu:iron_rod", 2], ["gtceu:lead_spring", 1], ["gtceu:iron_plate", 2], ["#forge:glass", 1], ["minecraft:bricks", 2], ["thermal:redstone_servo", 1]]}
OVERRIDE["gtceu:lp_steam_alloy_smelter"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:bronze_small_fluid_pipe", 6], ["minecraft:furnace", 2], ["gtceu:bronze_brick_casing", 1]]}
OVERRIDE["gtceu:hp_steam_alloy_smelter"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:lp_steam_alloy_smelter", 1], ["gtceu:steel_plate", 1], ["gtceu:wrought_iron_plate", 6], ["gtceu:tin_alloy_small_fluid_pipe", 1]]}
OVERRIDE["thermal_extra:soul_infused_glass"] = {"t": "fluid_solidifier", "o": 1, "eu": "30", "s": "kubejs (modifications/thermal.js)", "in": [["gtceu:tempered_glass", 1]], "fl": [["soul_infused", "144"]]}
OVERRIDE["thermal:energy_cell_frame"] = {"t": "crafting", "o": 1, "s": "kubejs (modifications/thermal.js)", "in": [["gtceu:lead_plate", 4], ["gtceu:electrum_plate", 4]]}
OVERRIDE["thermal:energy_cell"] = {"t": "alloy_smelter", "o": 1, "eu": "28", "s": "kubejs (modifications/thermal.js)", "in": [["thermal:energy_cell_frame", 1], ["minecraft:redstone_block", 1]]}
OVERRIDE["gtceu:treated_wood_planks"] = {"t": "crafting", "o": 8, "s": "gt", "in": [["#minecraft:planks", 8]], "fl": [["creosote", "1000"]]}
OVERRIDE["gtceu:firebricks"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:firebrick", 4]]}
OVERRIDE["kubejs:mesh_block"] = {"t": "crafting", "o": 1, "s": "kubejs (mechanical_sieve.js)", "in": [["exnihilosequentia:string_mesh", 5], ["gtceu:treated_wood_rod", 4]]}
OVERRIDE["gtceu:lv_battery_buffer_4x"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:lv_machine_hull", 1], ["gtceu:tin_quadruple_wire", 4], ["#forge:chests/wooden", 1]]}
for _t, (_pl, _gl, _gr, _c, _f) in {"mv": ("gold", "thermal:signalum_glass", "steel", "mv", ("redstone", "720")),
                                     "hv": ("electrum", "thermal:lumium_glass", "aluminium", "hv", ("glowstone", "720")),
                                     "ev": ("blue_alloy", "thermal:enderium_glass", "stainless_steel", "ev", ("ender", "750"))}.items():
    OVERRIDE[f"kubejs:{_t}_upgrade_kit"] = {"t": "assembler", "o": 1, "s": "kubejs (power/thermal_augments.js)",
        "in": [[f"gtceu:{_pl}_plate", 4], [_gl, 1], [f"gtceu:{_gr}_gear", 1], [f"#gtceu:circuits/{_c}", 1]], "fl": [list(_f)]}
for _t, (_pipe, _rotor) in {"mv": ("steel", "bronze"), "hv": ("stainless_steel", "steel"), "ev": ("titanium", "stainless_steel")}.items():
    OVERRIDE[f"gtceu:{_t}_muffler_hatch"] = {"t": "crafting", "o": 1, "s": "gt",
        "in": [[f"gtceu:{_t}_machine_hull", 1], [f"gtceu:{_t}_electric_motor", 1], [f"gtceu:{_pipe}_normal_fluid_pipe", 1], [f"gtceu:{_rotor}_rotor", 1]]}
for _g, _base, _fl in (("thermal:obsidian_glass", "tempered", ("lava", "250")), ("thermal:signalum_glass", "tempered", ("signalum", "144")),
                       ("thermal:lumium_glass", "tempered", ("lumium", "144")), ("thermal:enderium_glass", "tempered", ("enderium", "144")),
                       ("thermal_extra:shellite_glass", "laminated", ("shellite", "144"))):
    OVERRIDE[_g] = {"t": "fluid_solidifier", "o": 1, "s": "kubejs (modifications/thermal.js)", "in": [[f"gtceu:{_base}_glass", 1]], "fl": [list(_fl)]}
OVERRIDE["gtceu:item_filter"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:zinc_foil", 8], ["gtceu:steel_plate", 1]]}
OVERRIDE["gtceu:empty_mold"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:steel_plate", 4]]}
for _m in ("small_gear_casting_mold", "ingot_casting_mold", "ball_casting_mold", "plate_casting_mold", "ring_extruder_mold"):
    OVERRIDE[f"gtceu:{_m}"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:empty_mold", 1]]}
OVERRIDE["gtceu:lv_transformer_1a"] = {"t": "crafting", "o": 1, "s": "kubejs (tiered_machines/transformers.js)", "in": [["gtceu:lv_machine_hull", 1], ["gtceu:tin_single_cable", 4], ["gtceu:copper_single_cable", 1]]}
OVERRIDE["functionalstorage:oak_1"] = {"t": "crafting", "o": 1, "s": "mod", "in": [["minecraft:oak_planks", 8], ["#forge:chests/wooden", 1]]}
# GT generates these in loops (MetaTileEntityLoader / MetaTileEntityMachineRecipeLoader / AssemblerRecipeLoader of the StarT fork).
# Hull crafting "PLP"/"CHC": P hull plate, L tier plate, C cable, H casing. Buses/hatches: hull + crate/drum + the tier's cheapest glue/plastic.
_HULLS = {"lv": ("wrought_iron", "steel", "tin"), "mv": ("wrought_iron", "aluminium", "copper"),
          "hv": ("polyethylene", "stainless_steel", "gold"), "ev": ("polyethylene", "titanium", "aluminium")}
_IO = {"lv": (1, "wooden", "glue", 576), "mv": (2, "bronze", "polyethylene", 432), "hv": (3, "steel", "polyethylene", 576), "ev": (4, "aluminium", "polytetrafluoroethylene", 360)}
for _t, (_hp, _pl, _cb) in _HULLS.items():
    OVERRIDE[f"gtceu:{_t}_machine_hull"] = {"t": "crafting", "o": 1, "s": "gt",
        "in": [[f"gtceu:{_hp}_plate", 2], [f"gtceu:{_pl}_plate", 1], [f"gtceu:{_cb}_single_cable", 2], [f"gtceu:{_t}_machine_casing", 1]]}
    _tier, _mat, _fl, _amt = _IO[_t]
    for _io, _circ in (("input", 1), ("output", 2)):
        OVERRIDE[f"gtceu:{_t}_{_io}_bus"] = {"t": "assembler", "o": 1, "eu": "30", "circuit": _circ, "s": "gt",
            "in": [[f"gtceu:{_t}_machine_hull", 1], [f"gtceu:{_mat}_crate", 1]], "fl": [[_fl, str(_amt)]]}
        OVERRIDE[f"gtceu:{_t}_{_io}_hatch"] = {"t": "assembler", "o": 1, "eu": "30", "circuit": _circ, "s": "gt",
            "in": [[f"gtceu:{_t}_machine_hull", 1], [f"gtceu:{_mat}_drum", 1]], "fl": [[_fl, str(_amt)]]}
OVERRIDE["gtceu:ulv_machine_casing"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:wrought_iron_plate", 8]]}
OVERRIDE["gtceu:ulv_machine_hull"] = {"t": "crafting", "o": 1, "s": "gt",
    "in": [["gtceu:wood_plate", 2], ["gtceu:wrought_iron_plate", 1], ["gtceu:red_alloy_single_cable", 2], ["gtceu:ulv_machine_casing", 1]]}
for _io, _circ in (("input", 1), ("output", 2)):
    OVERRIDE[f"gtceu:ulv_{_io}_bus"] = {"t": "assembler", "o": 1, "eu": "7", "circuit": _circ, "s": "gt",
        "in": [["gtceu:ulv_machine_hull", 1], ["#forge:chests/wooden", 1]], "fl": [["glue", "288"]]}
    OVERRIDE[f"gtceu:ulv_{_io}_hatch"] = {"t": "assembler", "o": 1, "eu": "7", "circuit": _circ, "s": "gt",
        "in": [["gtceu:ulv_machine_hull", 1], ["#forge:glass", 1]], "fl": [["glue", "288"]]}
OVERRIDE["gtceu:lv_muffler_hatch"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:lv_machine_hull", 1], ["gtceu:lv_electric_motor", 1], ["gtceu:bronze_normal_fluid_pipe", 1], ["gtceu:tin_rotor", 1]]}
OVERRIDE["gtceu:lv_energy_input_hatch"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:lv_machine_hull", 1], ["gtceu:tin_single_cable", 2], ["gtceu:lv_voltage_coil", 1]]}
OVERRIDE["gtceu:mv_energy_input_hatch"] = {"t": "crafting", "o": 1, "s": "gt", "in": [["gtceu:mv_machine_hull", 1], ["gtceu:copper_single_cable", 2], ["gtceu:mv_voltage_coil", 1], ["gtceu:ulpic_chip", 1]]}
OVERRIDE["gtceu:lv_voltage_coil"] = {"t": "assembler", "o": 1, "eu": "30", "circuit": 1, "s": "gt", "in": [["gtceu:magnetic_iron_rod", 1], ["gtceu:fine_steel_wire", 16]]}
OVERRIDE["gtceu:mv_voltage_coil"] = {"t": "assembler", "o": 1, "eu": "120", "circuit": 1, "s": "gt", "in": [["gtceu:magnetic_steel_rod", 1], ["gtceu:fine_aluminium_wire", 16]]}


def pick(i):
    if i in OVERRIDE:
        return dict(OVERRIDE[i])
    kc = [r for r in KREC.get(i, []) if r["src"].startswith("kjs")]
    gtc = [r for r in KREC.get(i, []) if r["src"] == "gt"]
    jar = JAR.get(i, [])
    gtm = GTM.get(i, [])
    if i in REMOVED and kc:
        jar, gtm, gtc = [], [], []
    order = [(r, "kubejs") for r in kc if r["type"] == "crafting"] + \
            [(r, "mod") for r in jar if r["type"] in ("crafting", "shapeless", "mechanical_crafting")] + \
            [(r, "gt") for r in gtm] + [(r, "gt") for r in gtc if r["type"] == "crafting"] + \
            [(r, "kubejs") for r in kc] + [(r, "gt") for r in gtc] + [(r, "mod") for r in jar]
    for r, src in order:
        if r.get("in"):
            return norm(r, src)
    if i in MANUAL:
        return dict(MANUAL[i], s="kubejs/gt (generated)")
    m = re.match(r"^gtceu:([a-z0-9_]+)_frame$", i)
    if m:
        return {"t": "crafting", "o": 2, "s": "gt (generated)", "in": [[f"gtceu:{m.group(1)}_rod", 8]]}
    m = re.match(r"^gtceu:([a-z0-9_]+)_block$", i)
    if m and not re.search(r"(coil|casing|glass|ore|_raw)", m.group(1)):
        part = "gem" if f"gtceu:{m.group(1)}_gem" in NAMES else "ingot"
        return {"t": "crafting", "o": 1, "s": "gt (generated)", "in": [[f"gtceu:{m.group(1)}_{part}", 9]]}
    return None


# Recipes the pack builds in loops / templates (KubeJS converters.js, GT tiered components) - written out per tier.
MANUAL = {}
NAMES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "names.json"), encoding="utf-8")).get("names", {})
TIERMAT = {"lv": ("steel", "tin", "soul_infused", "wrought_iron", "bronze"), "mv": ("aluminium", "copper", "signalum", "wrought_iron", "steel"),
           "hv": ("stainless_steel", "gold", "lumium", "polyethylene", "stainless_steel"), "ev": ("titanium", "aluminium", "enderium", "polyethylene", "titanium"),
           "iv": ("tungsten_steel", "platinum", "shellite", "polytetrafluoroethylene", "tungsten_steel")}
for t, (plate, cable, sc, hullp, pipe) in TIERMAT.items():
    for amps, thick in ((1, "single"), (4, "quadruple"), (8, "octal"), (16, "hex")):
        MANUAL[f"gtceu:{t}_{amps}a_energy_converter"] = {"t": "crafting", "o": 1, "in": [[f"gtceu:{sc}_{thick}_wire", 4], [f"#gtceu:circuits/{t}", 1], [f"gtceu:{t}_machine_hull", 1]]}
    MANUAL[f"gtceu:{t}_machine_casing"] = {"t": "crafting", "o": 1, "in": [[f"gtceu:{plate}_plate", 8]]}
    MANUAL[f"gtceu:{t}_machine_hull"] = {"t": "crafting", "o": 1, "in": [[f"gtceu:{t}_machine_casing", 1], [f"gtceu:{cable}_single_cable", 2], [f"gtceu:{hullp}_plate", 2]]}
    MANUAL[f"gtceu:{t}_conveyor_module"] = {"t": "crafting", "o": 1, "in": [["gtceu:rubber_plate" if t in ("lv", "mv", "hv") else "gtceu:styrene_butadiene_rubber_plate", 6], [f"gtceu:{t}_electric_motor", 2], [f"gtceu:{cable}_single_cable", 1]]}
    MANUAL[f"gtceu:{t}_electric_pump"] = {"t": "crafting", "o": 1, "in": [[f"gtceu:{'tin' if t == 'lv' else plate}_screw", 1], [f"gtceu:{'tin' if t == 'lv' else plate}_rotor", 1], ["gtceu:rubber_ring", 2], [f"gtceu:{cable}_single_cable", 1], [f"gtceu:{pipe}_normal_fluid_pipe", 1], [f"gtceu:{t}_electric_motor", 1]]}


def load_js(fn):
    t = open(os.path.join(G, "data", fn), encoding="utf-8").read()
    return t


need = set()
import glob
for fn in sorted(os.path.basename(p) for p in glob.glob(os.path.join(G, "data", "guide*.js"))):
    p = os.path.join(G, "data", fn)
    if os.path.exists(p):
        need |= set(re.findall(r"'([a-z0-9_]+:[a-z0-9_./]+)'", open(p, encoding="utf-8").read()))
M = json.loads(load_js("multis.js").split("=", 1)[1].rstrip().rstrip(";"))
for m in M:
    need.add(m["id"])
    for s in m["s"]:
        if s.get("id"):
            need.add(s["id"])

need |= set(OVERRIDE)
OUT, seen = {}, set()
frontier = [(i, 0) for i in need]
while frontier:
    i, d = frontier.pop()
    if i in seen or d > 7:
        continue
    seen.add(i)
    if is_base(i) and i not in need:
        continue
    r = pick(i)
    if not r:
        continue
    OUT[i] = r
    for a, _ in r["in"]:
        if not is_base(a):
            frontier.append((a, d + 1))
with open(os.path.join(G, "data", "recipes.js"), "w", encoding="utf-8") as f:
    f.write("window.RECIPES=" + json.dumps(OUT, ensure_ascii=True, separators=(",", ":")) + ";\n")
print(len(need), "needed ids;", len(OUT), "recipes written;", len(REPL), "replaceInput ids")
for k in ["create:windmill_bearing", "create:mechanical_saw", "thermal:device_water_gen", "gtceu:lv_assembler", "gtceu:mechanical_sieve", "gtceu:heatproof_machine_casing", "create:andesite_casing"]:
    print(k, OUT.get(k, {}).get("in"), OUT.get(k, {}).get("s"))
