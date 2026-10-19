"""Normalise junk ingredient ids produced by the Java/KubeJS recipe extractors into real registry ids / tag ids.
java_item() (extract_recipes.py) wraps its result with clean_id(); build_recipes_js.py applies it again as a safety net."""
import json, os, re

TIERS = ["ULV", "LV", "MV", "HV", "EV", "IV", "LuV", "ZPM", "UV", "UHV", "UEV", "UIV", "UXV", "OpV", "MAX"]
_T = {t.lower(): t.lower() for t in TIERS}
_COMP = None

TAGS = {  # Java tag constant -> tag id
    "ItemTags.PLANKS": "#minecraft:planks", "ItemTags.LOGS_THAT_BURN": "#minecraft:logs_that_burn", "ItemTags.SAPLINGS": "#minecraft:saplings",
    "ItemTags.FISHES": "#minecraft:fishes", "ItemTags.LOGS": "#minecraft:logs", "ItemTags.WOOL": "#minecraft:wool", "ItemTags.SAND": "#forge:sand",
    "CustomTags.DIODES": "#gtceu:diodes", "CustomTags.PISTONS": "#gtceu:pistons", "CustomTags.CORAL_ITEMS": "#minecraft:coral_plants",
    "CustomTags.CORAL_BLOCK_ITEMS": "#minecraft:coral_blocks",
    "minecraft:chests_wooden": "#forge:chests/wooden", "Chests Wooden": "#forge:chests/wooden",
}
# real registry names that differ from the generator's derivation
PAT = [
    (r"^gtceu:machine_casing_([a-z]+)$", r"gtceu:\1_machine_casing"),
    (r"^gtceu:hermetic_casing_([a-z]+)$", r"gtceu:\1_hermetic_casing"),
    (r"^gtceu:([a-z0-9_]+)_magnetic_rod$", r"gtceu:magnetic_\1_rod"),
    (r"^gtceu:g_t_materials_(.+)$", None),  # unresolved GTMaterials.<X> constant: drop to generic
]


def _comp():
    """CraftingComponent tables (name -> tier -> id), dumped by gt_machines.py into component_table.json."""
    global _COMP
    if _COMP is None:
        try:
            _COMP = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "component_table.json"), encoding="utf-8"))
        except Exception:
            _COMP = {}
    return _COMP


def clean_id(i):
    """Return (id, count_multiplier)."""
    if not isinstance(i, str):
        return i, 1
    s = i.strip(); n = 1
    m = re.fullmatch(r"(.*\S),\s*(\d+)", s)  # 'ItemTags.PLANKS, 4' -> count suffix
    if m and "toolHead" not in s:
        s, n = m.group(1), int(m.group(2))
    if s in TAGS:
        return TAGS[s], n
    m = re.fullmatch(r"CustomTags\.([A-Za-z]+)_CIRCUITS", s)
    if m:
        return f"#gtceu:circuits/{m.group(1).lower()}", n
    m = re.fullmatch(r"CustomTags\.([A-Za-z]+)", s)
    if m and m.group(1).lower() in _T:
        return f"#gtceu:circuits/{m.group(1).lower()}", n
    m = re.fullmatch(r"toolHeadBuzzSaw,\s*([A-Za-z0-9]+)", s)  # TagPrefix.toolHeadBuzzSaw, Material
    if m:
        mat = re.sub(r"(?<!^)([A-Z])", r"_\1", m.group(1)).lower()
        return f"gtceu:{mat}_buzz_saw_blade", n
    m = re.fullmatch(r"(?:GTCraftingComponents\.|GTValues\.)?([A-Z][A-Z0-9_]+)\.get\((?:GTValues\.)?([A-Za-z]+)\)", s)
    if m:
        name, tier = m.group(1), m.group(2).lower()
        if name == "HULL":
            return f"gtceu:{tier}_machine_hull", n
        v = _comp().get(name, {}).get(tier)
        if v:
            return v, n
        return f"gtceu:{tier}_{name.lower()}", n
    m = re.fullmatch(r"([a-z][A-Za-z]+),\s*(?:GTMaterials\.)?([A-Z][A-Za-z0-9]+)(?:,\s*(\d+))?", s)  # 'cableGtSingle, Platinum'
    if m and m.group(1) in PREFIX:
        mat = re.sub(r"(?<!^)(?=[A-Z])", "_", m.group(2)).lower()
        return "gtceu:" + PREFIX[m.group(1)].format(m=mat), int(m.group(3) or 1) * n
    for rx, rep in PAT:
        if re.match(rx, s):
            if rep is None:
                return s, n
            return re.sub(rx, rep, s), n
    return s, n


def clean_inputs(d):
    """dict id->count (or list of [id,count]) -> same shape with cleaned ids (counts merged)."""
    items = d.items() if isinstance(d, dict) else d
    out = {}
    for k, v in items:
        k2, mul = clean_id(k)
        try:
            out[k2] = out.get(k2, 0) + v * mul
        except TypeError:
            out[k2] = v
    return out


# GT TagPrefix field -> item id format (single source of truth, imported by extract_recipes)
PREFIX = {
    "plate": "{m}_plate", "plateDouble": "double_{m}_plate", "plateDense": "dense_{m}_plate",
    "ingot": "{m}_ingot", "dust": "{m}_dust", "dustSmall": "small_{m}_dust", "dustTiny": "tiny_{m}_dust",
    "gear": "{m}_gear", "gearSmall": "small_{m}_gear", "rod": "{m}_rod", "rodLong": "long_{m}_rod",
    "bolt": "{m}_bolt", "screw": "{m}_screw", "ring": "{m}_ring", "spring": "{m}_spring",
    "springSmall": "small_{m}_spring", "round": "{m}_round", "foil": "{m}_foil", "wireFine": "fine_{m}_wire",
    "frameGt": "{m}_frame", "block": "{m}_block", "rotor": "{m}_rotor", "gem": "{m}_gem",
    "gemExquisite": "exquisite_{m}_gem", "gemFlawless": "flawless_{m}_gem", "lens": "{m}_lens",
    "cableGtSingle": "{m}_single_cable", "cableGtDouble": "{m}_double_cable", "cableGtQuadruple": "{m}_quadruple_cable",
    "cableGtOctal": "{m}_octal_cable", "cableGtHex": "{m}_hex_cable",
    "wireGtSingle": "{m}_single_wire", "wireGtDouble": "{m}_double_wire", "wireGtQuadruple": "{m}_quadruple_wire",
    "wireGtOctal": "{m}_octal_wire", "wireGtHex": "{m}_hex_wire",
    "pipeSmallFluid": "{m}_small_fluid_pipe", "pipeNormalFluid": "{m}_normal_fluid_pipe",
    "pipeLargeFluid": "{m}_large_fluid_pipe", "pipeHugeFluid": "{m}_huge_fluid_pipe",
    "pipeNormalItem": "{m}_normal_item_pipe", "toolHeadBuzzSaw": "{m}_buzz_saw_blade", "rock": "{m}_dust", "nugget": "{m}_nugget",
}
