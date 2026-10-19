"""Resolve GTCEu tiered machine recipes (registerMachineRecipe + CraftingComponent tables) and component recipes."""
import json, os, re, sys, io
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from extract_multis import find_close, split_top, strings_in, SRC
from extract_recipes import java_item, shaped_counts

TIERS = ["ULV", "LV", "MV", "HV", "EV", "IV", "LuV", "ZPM", "UV", "UHV"]
comp_src = open(os.path.join(SRC, "GTCraftingComponents.java"), encoding="utf-8").read()

COMP = {}  # name -> {tier: id}
for m in re.finditer(r"\b([A-Z][A-Z0-9_]+)\s*(?:=\s*CraftingComponent\.of\(|\.add\()", comp_src):
    name = m.group(1)
    st = m.start()
    # walk the chained .add( ... ) calls after this point until ';'
    end = comp_src.find(";", st)
    seg = comp_src[st:end]
    for a in re.finditer(r"\.add\(\s*(ULV|LV|MV|HV|EV|IV|LuV|ZPM|UV|UHV)\s*,", seg):
        cst = a.end()
        cen = find_close(seg, a.start() + len(".add"))
        expr = seg[cst:cen]
        iid, _ = java_item(expr)
        if "Tags.Items.GLASS" in expr:
            iid = "#forge:glass"
        COMP.setdefault(name, {})[a.group(1)] = iid
json.dump({k: {t.lower(): v for t, v in d.items()} for k, d in COMP.items()}, open(os.path.join(HERE, "component_table.json"), "w", encoding="utf-8"))
print(len(COMP), "components; CABLE LV =", COMP.get("CABLE", {}).get("LV"), "MOTOR MV =", COMP.get("MOTOR", {}).get("MV"))

MACH_ID = {"HULL": "machine_hull"}
mt = open(os.path.join(SRC, "MetaTileEntityLoader.java"), encoding="utf-8").read()
OUT = {}
for m in re.finditer(r"registerMachineRecipe\(", mt):
    st = m.end() - 1
    args = split_top(mt[st + 1:find_close(mt, st)])
    if len(args) < 4:
        continue
    mm = re.search(r"GTMachines\.([A-Z0-9_]+)", args[1])
    if not mm:
        continue
    mname = mm.group(1).lower()
    rest = args[2:]
    rows = []
    while rest and re.fullmatch(r'\s*"[^"]*"\s*', rest[0]):
        rows.append(strings_in(rest.pop(0))[0])
    keys = {}
    while len(rest) >= 2:
        k = re.search(r"'(.)'", rest[0])
        if not k:
            break
        keys[k.group(1)] = rest[1].strip()
        rest = rest[2:]
    for tier in TIERS[1:6]:
        kk, ok = {}, True
        for k, expr in keys.items():
            e = expr.replace("GTCraftingComponents.", "")
            if re.fullmatch(r"[A-Z][A-Z0-9_]+", e) and e in COMP:
                v = COMP[e].get(tier)
                if not v:
                    ok = False
                    break
                kk[k] = v
            else:
                kk[k] = java_item(expr)[0]
        if not ok:
            continue
        oid = f"gtceu:{tier.lower()}_{mname}"
        OUT.setdefault(oid, []).append({"src": "gt", "type": "crafting", "out": 1, "grid": rows, "keys": kk, "in": shaped_counts(rows, kk)})

# component recipes (motors, pistons, pumps, conveyors, robot arms ...)
ct = open(os.path.join(SRC, "ComponentRecipes.java"), encoding="utf-8").read()
for m in re.finditer(r"addShapedRecipe\(", ct):
    st = m.end() - 1
    args = split_top(ct[st + 1:find_close(ct, st)])
    i = 1 if args[1].strip() in ("true", "false") else 0
    i += 1
    if len(args) <= i + 1 or not args[i].strip().startswith('"'):
        continue
    oid, oc = java_item(args[i + 1])
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
    OUT.setdefault(oid, []).append({"src": "gt", "type": "crafting", "out": oc, "grid": rows, "keys": keys, "in": shaped_counts(rows, keys)})

json.dump(OUT, open(os.path.join(HERE, "gt_machine_recipes.json"), "w", encoding="utf-8"))
print(len(OUT), "outputs")
for k in ["gtceu:lv_assembler", "gtceu:mv_electrolyzer", "gtceu:lv_electric_motor", "gtceu:lv_conveyor_module", "gtceu:lv_forge_hammer", "gtceu:lv_machine_hull"]:
    print(k, [r["in"] for r in OUT.get(k, [])][:1])
