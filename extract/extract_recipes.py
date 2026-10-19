"""Index crafting + GT machine recipes by output id, from StarT KubeJS server scripts and GTCEu fork Java loaders."""
import json, os, re, sys, io
pass
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from extract_multis import find_close, split_top, strings_in, snake, CONST, SRC, BASE

SS = os.path.join(BASE, "kubejs", "server_scripts")

from idfix import PREFIX  # GT TagPrefix field -> item id format
TIERS = ["ULV", "LV", "MV", "HV", "EV", "IV", "LuV", "ZPM", "UV", "UHV", "UEV", "UIV", "UXV", "OpV", "MAX"]


def java_item(e):
    """Convert a Java ingredient expression to (id, count); junk constants are resolved by idfix.clean_id."""
    import idfix
    e = re.sub(r"_LuV(?![A-Za-z])", "_LUV", e.strip())  # GTBlocks.MACHINE_CASING_LuV: constants are upper case
    pre, pm = idfix.clean_id(e)
    if pre != e:  # Java constant expression already resolvable (X.get(TIER), tag constants, buzz saw heads)
        return pre, pm
    i, c = _java_item(e)
    i, mul = idfix.clean_id(i)
    return i, c * mul


def _java_item(e):
    e = e.strip()
    cnt = 1
    m = re.search(r"\.asStack\((\d+)\)", e)
    if m:
        cnt = int(m.group(1))
    if "casingsPerCraft" in e:
        cnt = 2
    m = re.search(r"CustomTags\.([A-Za-z]+)_CIRCUITS", e)
    if m:
        return f"#gtceu:circuits/{m.group(1).lower()}", cnt
    m = re.search(r"(?:new (?:Material|Unification)Entry\()?(?:TagPrefix\.)?([a-zA-Z]+),\s*(?:GTMaterials\.)?([A-Z][A-Za-z0-9]+)\)?(?:,\s*(\d+))?", e)
    if m and m.group(1) in PREFIX:
        if m.group(3):
            cnt = int(m.group(3))
        return "gtceu:" + PREFIX[m.group(1)].format(m=snake(m.group(2))), cnt
    m = re.search(r"GTMachines\.([A-Z_]+)\[(?:GTValues\.)?([A-Za-z]+)\]", e)
    if m:
        kind, tier = m.group(1), m.group(2).lower()
        base = {"HULL": "machine_hull", "ENERGY_INPUT_HATCH": "energy_input_hatch", "ITEM_IMPORT_BUS": "input_bus",
                "ITEM_EXPORT_BUS": "output_bus", "FLUID_IMPORT_HATCH": "input_hatch", "FLUID_EXPORT_HATCH": "output_hatch",
                "ELECTRIC_FURNACE": "electric_furnace", "ROTOR_HOLDER": "rotor_holder"}.get(kind, kind.lower())
        return f"gtceu:{tier}_{base}", cnt
    m = re.fullmatch(r"(?:GTItems\.)?([A-Z][A-Z0-9_]*?)_(ULV|LV|MV|HV|EV|IV|LuV|LUV|ZPM|UV|UHV)(?:\.asStack\(\d*\))?", e)
    if m:
        return f"gtceu:{m.group(2).lower()}_{m.group(1).lower()}", cnt
    m = re.search(r"GTItems\.([A-Z0-9_]+?)_(ULV|LV|MV|HV|EV|IV|LuV|LUV|ZPM|UV|UHV)\b", e)
    if m:
        return f"gtceu:{m.group(2).lower()}_{m.group(1).lower()}", cnt
    m = re.search(r"GTItems\.([A-Z0-9_]+)", e)
    if m:
        return "gtceu:" + m.group(1).lower(), cnt
    m = re.search(r"(?:GTBlocks|GCYMBlocks)\.([A-Z0-9_]+)", e) or re.fullmatch(r"([A-Z][A-Z0-9_]+)(?:\.asStack\(\d*\))?", e)
    if m:
        c = m.group(1)
        return CONST.get(c, "gtceu:" + c.lower()), cnt
    m = re.search(r"(?:GTMultiMachines|GCYMMachines|GTResearchMachines|GTMachines)\.([A-Z0-9_]+)", e)
    if m:
        return "gtceu:" + m.group(1).lower(), cnt
    m = re.search(r"(?:Blocks|Items)\.([A-Z_]+)", e)
    if m:
        return "minecraft:" + m.group(1).lower(), cnt
    m = re.search(r"Tags\.Items\.([A-Z_]+)", e)
    if m:
        return "#forge:" + m.group(1).lower(), cnt
    return e[:60], cnt


REC = {}


def add(out, rec):
    REC.setdefault(out, []).append(rec)


def shaped_counts(rows, keys):
    counts = {}
    for r in rows:
        for ch in r:
            if ch in keys:
                counts[keys[ch]] = counts.get(keys[ch], 0) + 1
    return counts


# ---------------- Java (GTCEu fork) ----------------
for fn in ("MetaTileEntityLoader.java", "MachineRecipeLoader.java"):
    t = open(os.path.join(SRC, fn), encoding="utf-8").read()
    for m in re.finditer(r"addShapedRecipe\(", t):
        st = m.end() - 1
        args = split_top(t[st + 1:find_close(t, st)])
        if len(args) < 4:
            continue
        i = 1 if args[1].strip() in ("true", "false") else 0
        i += 1  # skip provider
        if not args[i].strip().startswith('"'):
            continue
        out_id, out_cnt = java_item(args[i + 1])
        rest = args[i + 2:]
        rows = []
        while rest and re.fullmatch(r'\s*"[^"]*"\s*', rest[0]):
            rows.append(strings_in(rest.pop(0))[0])
        keys = {}
        while len(rest) >= 2:
            k = re.search(r"'(.)'", rest[0])
            if not k:
                break
            keys[k.group(1)] = java_item(rest[1])[0]
            rest = rest[2:]
        tools = set("hwfdsrxc")
        cnts = {k: v for k, v in shaped_counts(rows, keys).items()}
        add(out_id, {"src": "gt", "type": "crafting", "out": out_cnt, "grid": rows,
                     "keys": keys, "in": cnts})
    for m in re.finditer(r"([A-Z_]+_RECIPES)\.recipeBuilder\(\"([^\"]+)\"\)", t):
        st = m.start()
        en = t.find(".save(", st)
        chain = t[st:en]
        rtype = m.group(1).replace("_RECIPES", "").lower()
        ins, fins, outs = [], [], []
        for cm in re.finditer(r"\.(inputItems|outputItems|inputFluids|outputFluids)\(", chain):
            a = chain[cm.end() - 1:find_close(chain, cm.end() - 1) + 1][1:-1]
            if cm.group(1) in ("inputItems", "outputItems"):
                iid, c = java_item(a)
                (ins if cm.group(1) == "inputItems" else outs).append([iid, c])
            else:
                fm = re.match(r"\s*(?:GTMaterials\.)?([A-Z][A-Za-z0-9]+)(?:\.getFluid\()?[^,]*,?\s*(.*)", a)
                if fm:
                    amt = fm.group(2).strip().rstrip(")")
                    amt = {"GTValues.L": "144", "L": "144", "L * 2": "288", "L / 2": "72"}.get(amt, amt)
                    fins.append([snake(fm.group(1)), amt])
        eu = re.search(r"\.EUt\(([^)]*)\)", chain)
        dur = re.search(r"\.duration\((\d+)\)", chain)
        circ = re.search(r"\.circuitMeta\((\d+)\)", chain)
        for o, c in outs:
            add(o, {"src": "gt", "type": rtype, "out": c, "in": dict((i, n) for i, n in ins), "fluids": fins,
                    "eu": eu.group(1) if eu else None, "dur": int(dur.group(1)) if dur else None,
                    "circuit": int(circ.group(1)) if circ else None})

# ---------------- KubeJS (StarT) ----------------
REMOVED = set()


def kjs_item(s):
    s = s.strip()
    m = re.match(r"^(?:Item\.of\()?['\"`](?:(\d+)x\s+)?([^'\"`]+)['\"`](?:\s*,\s*(\d+))?", s)
    if m:
        return m.group(2), int(m.group(1) or m.group(3) or 1)
    return None, 0


def subst_consts(a, consts):
    """Inline file-level string constants: `'6x ' + t1Panel` and bare `t1Panel` arguments become literal strings."""
    if not consts:
        return a
    a = re.sub(r"(['\"])((?:\d+x\s+)?)\1\s*\+\s*(\w+)", lambda m: repr(m.group(2) + consts[m.group(3)]) if m.group(3) in consts else m.group(0), a)
    return re.sub(r"(?<![\w'\".$])(\w+)(?![\w'\"(])", lambda m: repr(consts[m.group(1)]) if m.group(1) in consts else m.group(0), a)


for root, _, files in os.walk(SS):
    for f in files:
        if not f.endswith(".js"):
            continue
        t = open(os.path.join(root, f), encoding="utf-8").read()
        rel = os.path.relpath(os.path.join(root, f), SS).replace("\\", "/")
        CONSTS = dict(re.findall(r"(?:const|let|var)\s+(\w+)\s*=\s*['\"]([^'\"]+)['\"]", t))
        for m in re.finditer(r"remove\(\s*\{([^}]*)\}", t):
            for o in re.findall(r"output:\s*['\"]([^'\"]+)['\"]", m.group(1)):
                REMOVED.add(o)
            for o in re.findall(r"output:\s*\[([^\]]*)\]", m.group(1)):
                for x in strings_in(o):
                    REMOVED.add(x)
        for m in re.finditer(r"\.shaped\(", t):
            st = m.end() - 1
            args = split_top(t[st + 1:find_close(t, st)])
            if len(args) < 3:
                continue
            oid, oc = kjs_item(args[0])
            if not oid or "$" in oid:
                continue
            rows = strings_in(args[1])
            km = args[2].strip()
            keys = {}
            if km.startswith("{"):
                for ent in split_top(km[1:-1]):
                    kk = re.match(r"\s*['\"]?(.)['\"]?\s*:\s*(.*)", ent, re.S)
                    if kk:
                        iid, _ = kjs_item(kk.group(2))
                        keys[kk.group(1)] = iid or kk.group(2).strip()[:50]
            add(oid, {"src": "kjs:" + rel, "type": "crafting", "out": oc, "grid": rows, "keys": keys,
                      "in": shaped_counts(rows, keys)})
        for m in re.finditer(r"\.recipes\.gtceu\s*\.\s*([a-z_]+)\(", t):
            st = m.end() - 1
            en = t.find(";", st)
            nxt = re.search(r"\.recipes\.gtceu\s*\.", t[st + 1:])
            if nxt and st + 1 + nxt.start() < en:
                en = st + 1 + nxt.start()
            chain = t[st:en]
            def args_of(fn):
                r = []
                for cm in re.finditer(r"\." + fn + r"\(", chain):
                    a = chain[cm.end() - 1:find_close(chain, cm.end() - 1) + 1][1:-1]
                    a = subst_consts(a, CONSTS)
                    r += strings_in(a)
                return r
            outs = args_of("itemOutputs")
            if not outs:
                continue
            ins = {}
            for s in args_of("itemInputs"):
                mm = re.match(r"(?:(\d+)x\s+)?(.+)", s)
                ins[mm.group(2)] = ins.get(mm.group(2), 0) + int(mm.group(1) or 1)
            fl = []
            for s in args_of("inputFluids"):
                mm = re.match(r"([^\s]+)\s*(\d*)", s)
                fl.append([mm.group(1), mm.group(2)])
            eu = re.search(r"\.EUt\(([^)]*)\)", chain)
            dur = re.search(r"\.duration\(([^)]*)\)", chain)
            circ = re.search(r"\.circuit\((\d+)\)", chain)
            for o in outs:
                mm = re.match(r"(?:(\d+)x\s+)?(.+)", o)
                if "$" in mm.group(2):
                    continue
                add(mm.group(2), {"src": "kjs:" + rel, "type": m.group(1), "out": int(mm.group(1) or 1), "in": ins,
                                  "fluids": fl, "eu": eu.group(1) if eu else None,
                                  "dur": dur.group(1) if dur else None,
                                  "circuit": int(circ.group(1)) if circ else None})

json.dump({"recipes": REC, "removed": sorted(REMOVED)}, open(os.path.join(HERE, "recipes.json"), "w", encoding="utf-8"), indent=0)
print(len(REC), "outputs indexed;", len(REMOVED), "removed outputs")
