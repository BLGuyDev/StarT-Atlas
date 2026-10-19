"""Parse multiblock patterns (KubeJS startup scripts + StarT GTCEu fork Java sources) into block counts."""
import json, os, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from common import GT_SRC, require_pack
SRC = GT_SRC
BASE = require_pack()
MB_DIR = os.path.join(BASE, r"kubejs/startup_scripts/machines/multiblocks")


def snake(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()


# ---- constant -> block id map from GTBlocks / GCYMBlocks ----
CONST = {}
for fn in ("GTBlocks.java", "GCYMBlocks.java"):
    t = open(os.path.join(SRC, fn), encoding="utf-8").read()
    for m in re.finditer(r"public static final [^=]+?\s([A-Z][A-Z0-9_]+)\s*=\s*([\s\S]{0,200}?);", t):
        name, rhs = m.group(1), m.group(2)
        s = re.search(r"\"([a-z0-9_]+)\"", rhs)
        if s:
            CONST[name] = "gtceu:" + s.group(1)
FIRE = {"FIREBOX_BRONZE": "gtceu:bronze_firebox_casing", "FIREBOX_STEEL": "gtceu:steel_firebox_casing",
        "FIREBOX_TITANIUM": "gtceu:titanium_firebox_casing", "FIREBOX_TUNGSTENSTEEL": "gtceu:tungstensteel_firebox_casing"}
CONST.update(FIRE)
CONST.setdefault("CASING_PUMP_DECK", "gtceu:pump_deck")
CONST.setdefault("TREATED_WOOD_PLANK", "gtceu:treated_wood_planks")


def find_close(t, i, open_ch="(", close_ch=")"):
    """i points at open_ch; return index of matching close (skips string literals)."""
    depth, j, n = 0, i, len(t)
    while j < n:
        c = t[j]
        if c in "'\"`":
            q = c
            j += 1
            while j < n and t[j] != q:
                if t[j] == "\\":
                    j += 1
                j += 1
        elif c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return n - 1


def strings_in(s):
    return [a or b for a, b in re.findall(r"'((?:[^'\\]|\\.)*)'|\"((?:[^\"\\]|\\.)*)\"", s)]


def split_top(s, sep=","):
    out, depth, cur, j = [], 0, [], 0
    while j < len(s):
        c = s[j]
        if c in "'\"`":
            q = c
            k = j + 1
            while k < len(s) and s[k] != q:
                if s[k] == "\\":
                    k += 1
                k += 1
            cur.append(s[j:k + 1])
            j = k + 1
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if c == sep and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(c)
        j += 1
    if "".join(cur).strip():
        out.append("".join(cur))
    return out


def analyse_pred(e):
    info = {"blocks": [], "abilities": [], "min": None, "special": []}
    if re.search(r"controller\(", e):
        info["special"].append("controller")
    for rx, pre in [(r"P\.block\('([^']+)'", ""), (r"P\.kjsBlock\('([^']+)'", "kubejs:"),
                    (r"P\.gtBlock\('([^']+)'", "gtceu:"), (r"P\.coreBlock\('([^']+)'", "start_core:"),
                    (r"Predicates\.blocks\('([^']+)'", ""), (r"Block\.getBlock\('([^']+)'", ""),
                    (r"blocks\(\"([^\"]+)\"", "")]:
        for m in re.finditer(rx, e):
            v = m.group(1)
            info["blocks"].append(pre + v if pre and ":" not in v else v)
    for m in re.finditer(r"(?:GTBlocks\.|GCYMBlocks\.|blocks\(|\.or\(blocks\()([A-Z][A-Z0-9_]+)(?:\.get\(\)|\[)", e):
        c = m.group(1)
        if c in CONST:
            info["blocks"].append(CONST[c])
        elif c == "MACHINE_CASING_ULV":
            info["blocks"].append("gtceu:ulv_machine_casing")
        elif c in ("ITEM_IMPORT_BUS", "ITEM_EXPORT_BUS", "FLUID_IMPORT_HATCH", "ENERGY_INPUT_HATCH"):
            info["abilities"].append(c)
        else:
            info["blocks"].append("gtceu:" + c.lower())
    for m in re.finditer(r"frames?\(\s*(?:GTMaterials\.)?(?!GTMaterials)([A-Z][A-Za-z0-9]+)", e):
        info["blocks"].append(f"gtceu:{snake(m.group(1))}_frame")
    for m in re.finditer(r"frameGt,\s*(?:GTMaterials\.)?(?!GTMaterials)([A-Z][A-Za-z0-9]+)", e):
        info["blocks"].append(f"gtceu:{snake(m.group(1))}_frame")
    for m in re.finditer(r"P\.frame\('([a-z0-9_]+)'", e):
        info["blocks"].append(f"gtceu:{m.group(1)}_frame")
    for m in re.finditer(r"Blocks\.([A-Z_]+)\b", e):
        if not re.search(r"(GT|GCYM)Blocks\." + m.group(1), e):
            info["blocks"].append("minecraft:" + m.group(1).lower())
    for m in re.finditer(r"P\.fluid\('([^']+)'", e):
        info["blocks"].append(m.group(1))
    bare = re.fullmatch(r"\s*'([a-z0-9_]+:[a-z0-9_/]+)'\s*", e)
    if bare:
        info["blocks"].append(bare.group(1))
    if re.search(r"threadingBlocks\(", e):
        info["special"].append("threading")
    if re.search(r"vacuumPumps\(", e):
        info["special"].append("vacuum_pump")
    if re.search(r"heatingCoils?\(", e):
        info["special"].append("coil")
    if re.search(r"cleanroomFilters?\(", e):
        info["special"].append("filter")
    if re.search(r"powerSubstationBatter", e):
        info["special"].append("battery")
    if re.search(r"P\.air\(\)|\bair\(\)", e) and not info["blocks"]:
        info["special"].append("air")
    if re.search(r"P\.any\(\)|\bany\(\)", e) and not info["blocks"]:
        info["special"].append("any")
    if re.search(r"autoAbilities", e):
        info["abilities"].append("auto")
    for m in re.finditer(r"(?:PA|PartAbility|\$StarTPartAbility)\.([A-Za-z0-9_]+)", e):
        if m.group(1) not in info["abilities"]:
            info["abilities"].append(m.group(1))
    m = re.search(r"setMinGlobalLimited\((\d+)|min:\s*(\d+)|setMinLayerLimited\((\d+)", e)
    if m:
        info["min"] = int(next(g for g in m.groups() if g))
    m = re.search(r"exact:\s*(\d+)|setExactLimit\((\d+)", e)
    if m:
        info["exact"] = int(next(g for g in m.groups() if g))
    info["blocks"] = list(dict.fromkeys(info["blocks"]))
    return info


def parse_segment(seg):
    """Return (aisles list[list[str]], mapping dict) for a machine definition segment."""
    aisles = []
    # newFactoryBlockPattern([ ... ], divider?)
    m = re.search(r"newFactoryBlockPattern\w*\([^\[]*\[", seg)
    if m:
        st = seg.index("[", m.start())
        en = find_close(seg, st, "[", "]")
        arr = seg[st + 1:en]
        div = "|"
        dm = re.match(r"\s*,\s*'(.)'", seg[en + 1:en + 10])
        if dm:
            div = dm.group(1)
        for s in strings_in(arr):
            aisles.append([x for x in s.split(div)])
    for m in re.finditer(r"\.aisle\(", seg):
        st = m.end() - 1
        en = find_close(seg, st)
        rows = strings_in(seg[st + 1:en])
        rep = 1
        rm = re.match(r"\s*\.setRepeatable\((\d+)", seg[en + 1:en + 60])
        if rm:
            rep = int(rm.group(1))
        for _ in range(max(rep, 1)):
            aisles.append(rows)
    mapping = {}
    m = re.search(r"\.whereDict\(\s*\{", seg)
    if m:
        st = seg.index("{", m.start())
        en = find_close(seg, st, "{", "}")
        for ent in split_top(seg[st + 1:en]):
            km = re.match(r"\s*(?:'(.)'|\"(.)\"|([A-Za-z0-9#]))\s*:", ent)
            if km:
                k = km.group(1) or km.group(2) or km.group(3)
                mapping[k] = ent[km.end():]
    for m in re.finditer(r"\.where\(\s*(?:'(.)'|\"(.)\")\s*,", seg):
        st = seg.index("(", m.start())
        en = find_close(seg, st)
        k = m.group(1) or m.group(2)
        mapping.setdefault(k, seg[m.end():en])
    return aisles, mapping


def collect(text, kind, fname):
    out = []
    rx = r"\.create\(\s*'([a-z0-9_]+)'" if kind == "js" else r"\.multiblock\(\"([a-z0-9_]+)\""
    starts = [(m.start(), m.group(1)) for m in re.finditer(rx, text)]
    for i, (pos, mid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        seg = text[pos:end]
        if ".pattern(" not in seg and "newFactoryBlockPattern" not in seg:
            continue
        if ".pattern(" in seg:
            ps = seg.find(".pattern(") + len(".pattern")
            pseg = seg[ps:find_close(seg, ps) + 1]
        else:
            pseg = seg
        aisles, mapping = parse_segment(pseg)
        if not aisles:
            continue
        counts = {}
        for a in aisles:
            for row in a:
                for ch in row:
                    counts[ch] = counts.get(ch, 0) + 1
        syms = {}
        for ch, n in counts.items():
            info = analyse_pred(mapping.get(ch, "")) if ch in mapping else {"blocks": [], "abilities": [], "min": None, "special": ["unmapped"]}
            if ch == " " and ch not in mapping:
                info["special"] = ["any"]
            info["count"] = n
            syms[ch] = info
        tooltip = []
        if re.search(r"exact_hatch_1|only.*single.*energy|maxGlobal.*euIn|euIn,\s*\{\s*max:\s*1", seg):
            tooltip.append("1 energy hatch")
        out.append({"id": ("gtceu:" if ":" not in mid else "") + mid, "file": fname,
                    "layers": len(aisles), "symbols": syms, "aisles": aisles})
    return out


def main():
    allm = []
    for root, _, files in os.walk(MB_DIR):
        if "deprecated" in root:
            continue
        for f in files:
            if f.endswith(".js"):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, MB_DIR).replace("\\", "/")
                allm += collect(open(p, encoding="utf-8").read(), "js", "kjs/" + rel)
    for f in ("GTMultiMachines.java", "GCYMMachines.java", "GTResearchMachines.java"):
        allm += collect(open(os.path.join(SRC, f), encoding="utf-8").read(), "java", "gt/" + f)
    # the StarT KubeJS can define machines with ids in other namespaces? keep as gtceu
    seen = {}
    for m in allm:
        seen.setdefault(m["id"], m)  # first definition wins (KubeJS before Java)
    json.dump(list(seen.values()), open(os.path.join(HERE, "multis.json"), "w", encoding="utf-8"), indent=1)
    print(len(seen), "multiblocks parsed")


if __name__ == "__main__":
    main()
