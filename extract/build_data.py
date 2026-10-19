"""Generate guia/data/quests.js and guia/data/multis.js from the pack (quests, multiblock patterns, recipes)."""
import json, os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from common import name, NAMES, GUIA, require_pack
BASE = require_pack()

OUT = os.path.join(GUIA, "data")
os.makedirs(OUT, exist_ok=True)
LANG = json.load(open(os.path.join(BASE, r"kubejs/assets/ftbquestlocalizer/lang/en_us.json"), encoding="utf-8"))


# ---------------- SNBT ----------------
def tok(s):
    i, n, out = 0, len(s), []
    while i < n:
        c = s[i]
        if c in " \t\r\n,\ufeff":
            i += 1; continue
        if c in "{}[]:;":
            out.append(c); i += 1; continue
        if c == '"':
            j, buf = i + 1, []
            while s[j] != '"':
                if s[j] == "\\":
                    buf.append(s[j + 1]); j += 2
                else:
                    buf.append(s[j]); j += 1
            out.append(("S", "".join(buf))); i = j + 1; continue
        j = i
        while j < n and s[j] not in ' \t\r\n,{}[]:;"':
            j += 1
        out.append(("W", s[i:j])); i = j
    return out


def parse(t, p=0):
    x = t[p]
    if x == "{":
        d = {}; p += 1
        while t[p] != "}":
            k = t[p][1]; p += 2
            v, p = parse(t, p); d[k] = v
        return d, p + 1
    if x == "[":
        l = []; p += 1
        if isinstance(t[p], tuple) and t[p + 1] == ";":
            p += 2
        while t[p] != "]":
            v, p = parse(t, p); l.append(v)
        return l, p + 1
    return x[1], p + 1


def L(k):
    if not k:
        return ""
    k = re.sub(r"\{([a-z0-9_.]+)\}", lambda m: LANG.get(m.group(1), m.group(0)), k)
    k = re.sub(r"[&\u00a7][0-9a-fk-or]", "", k)
    return k


def itm(x):
    if isinstance(x, dict):
        i = x.get("id", "?")
        tag = x.get("tag")
        if isinstance(tag, dict) and "items" in tag and i.startswith("itemfilters"):
            return [itm(y) for y in tag["items"]]
        return i
    return x


CHAPTERS = {}
QUESTS = {}
cdir = os.path.join(BASE, r"config/ftbquests/quests/chapters")
for f in os.listdir(cdir):
    d, _ = parse(tok(open(os.path.join(cdir, f), encoding="utf-8").read()))
    ch = f[:-5]
    CHAPTERS[ch] = {"title": L(d.get("title")), "group": d.get("group", ""), "order": int(d.get("order_index", 0))}
    for q in d.get("quests", []):
        tasks = []
        for tk in q.get("tasks", []):
            if tk.get("type") == "item":
                it = itm(tk.get("item"))
                cnt = int(str(tk.get("count", "1")).rstrip("L"))
                if isinstance(it, list):
                    tasks.append({"any": it, "n": cnt})
                elif it and not it.startswith("itemfilters"):
                    tasks.append({"id": it, "n": cnt})
        title = L(q.get("title"))
        if not title:
            for tk in q.get("tasks", []):
                if tk.get("title"):
                    title = L(tk["title"]); break
        if not title and tasks:
            t0 = tasks[0]
            title = name(t0["id"]) if "id" in t0 else name(t0["any"][0])
        if title and re.fullmatch(r"[a-z_]+:[a-z0-9_]+", title):
            title = name(title)
        desc = " ".join(L(x) for x in q.get("description", []) if x and x != "{@pagebreak}")
        desc = re.sub(r"\[\s*\"===>.*?\]\s*\]?", "", desc)
        desc = re.sub(r"\{image:[^}]*\}", "", desc)
        QUESTS[q["id"]] = {"ch": ch, "title": title or "?", "tasks": tasks, "deps": q.get("dependencies", []),
                           "opt": bool(q.get("optional")), "desc": desc.strip(), "inv": bool(q.get("invisible")),
                           "x": float(str(q.get("x", "0")).rstrip("d")), "y": float(str(q.get("y", "0")).rstrip("d"))}

# ---------------- eras ----------------
ERAS = ["stone", "steam", "lv", "mv", "hv", "ev", "iv", "luv", "zpm", "uv", "uhv", "uev", "uiv"]
TIERPFX = {"lv": 2, "mv": 3, "hv": 4, "ev": 5, "iv": 6, "luv": 7, "zpm": 8, "uv": 9, "uhv": 10, "uev": 11, "uiv": 12}
MATSEED = {"aluminium_ingot": 3, "signalum": 3, "good_electronic_circuit": 3, "stainless_steel_ingot": 4,
           "advanced_integrated_circuit": 4, "lumium": 4, "titanium_ingot": 5, "micro_processor_computer": 5,
           "enderium": 5, "vacuum_freezer": 5, "tungsten_steel_ingot": 6, "micro_processor_mainframe": 6,
           "shellite": 6, "rhodium_plated_palladium": 7, "nano_processor_mainframe": 7, "assembly_line": 7,
           "naquadah_alloy": 8, "quantum_processor_mainframe": 8, "darmstadtium": 9,
           "phosphorus": 5, "epoxy": 5, "mpic": 5, "nano_cpu": 5, "nor_memory": 5, "nand_memory": 5, "soc": 5,
           "carbon_fibers": 5, "borosilicate": 5, "hpic": 6, "graphene": 6, "hssg_ingot": 6, "alloy_blast_smelter": 6,
           "quantum_star": 6, "nuclear_reactor": 6, "ruridit": 7, "twinite": 7, "naquadah": 7,
           "superconducting_coil": 7, "uhpic": 7, "reflector": 7, "qbit": 7, "fiber_reinforced": 7, "data_orb": 7,
           "niobium_nitride": 7, "indium_tin_barium": 8, "dragonsteel": 8, "osthendah": 8, "emerald_gem": 8,
           "advanced_smd": 6, "hsse": 6, "hsss": 6}
BRONZE_TITLES = {"Primitive Steelworks", "Coke Oven", "Create Path", "Steam Age Path", "Bronze and Brass",
                 "Alloy Mixing", "Stressed Out", "Latex Extraction", "Red Alloy", "Invar", "Nickel", "Gold",
                 "Primitive Ore Factory", "Mixing Dusts", "Create: Vintage", "Large Farm", "Large Barrel",
                 "Large Stone Barrel"}
BASE_ERA = {"early_game": 0, "industrial_revolution": 2, "automation_age": 4, "futuristic_mechanisms": 6,
            "preparing_for_dimensional_travel": 8, "adventures_in_abydos": 9, "a_portal_of_lost_worlds": 10,
            "draconic_age_part_1": 11, "the_stars_await_greatness": 12}


def seed(q):
    s = BASE_ERA.get(q["ch"], 0)
    if q["title"] in BRONZE_TITLES:
        s = max(s, 1)
    ids = [t["id"] for t in q["tasks"] if "id" in t] + [x for t in q["tasks"] if "any" in t for x in t["any"][:1]]
    for i in ids:
        path = i.split(":")[1]
        m = re.match(r"^(lv|mv|hv|ev|iv|luv|zpm|uv|uhv|uev|uiv)_", path)
        if m and q["ch"] in BASE_ERA:
            s = max(s, TIERPFX[m.group(1)])
        for k, v in MATSEED.items():
            if k in path:
                s = max(s, v)
    return s


era = {}


def get_era(qid, stack=()):
    if qid in era:
        return era[qid]
    q = QUESTS.get(qid)
    if not q or qid in stack:
        return 0
    e = seed(q)
    for d in q["deps"]:
        if d in QUESTS and QUESTS[d]["ch"] in BASE_ERA:
            e = max(e, get_era(d, stack + (qid,)))
    era[qid] = e
    return e


for qid in QUESTS:
    get_era(qid)

# topological order within era (deps first), then by chapter order and position
MAIN_ORDER = ["early_game", "industrial_revolution", "automation_age", "futuristic_mechanisms",
              "preparing_for_dimensional_travel", "adventures_in_abydos", "a_portal_of_lost_worlds",
              "draconic_age_part_1", "the_stars_await_greatness"]
visited, ordered = set(), []


def visit(qid):
    if qid in visited or qid not in QUESTS:
        return
    visited.add(qid)
    for d in QUESTS[qid]["deps"]:
        if d in QUESTS and QUESTS[d]["ch"] == QUESTS[qid]["ch"]:
            visit(d)
    ordered.append(qid)


for ch in MAIN_ORDER:
    qs = sorted([k for k, v in QUESTS.items() if v["ch"] == ch], key=lambda k: (QUESTS[k]["x"], QUESTS[k]["y"]))
    for k in qs:
        visit(k)

quest_out = []
for qid in ordered:
    q = QUESTS[qid]
    if q["title"] in ("positioner", "?") or q["title"].startswith("{ftbquests"):
        continue
    if not q["tasks"] and not q["desc"]:
        continue
    quest_out.append({"id": qid, "ch": q["ch"], "era": ERAS[era[qid]], "t": q["title"], "opt": q["opt"],
                      "items": [{"id": t.get("id") or t["any"][0], "n": t["n"], "nm": name(t.get("id") or t["any"][0]),
                                 "any": len(t.get("any", [])) > 1} for t in q["tasks"]][:6],
                      "d": q["desc"][:600]})

with open(os.path.join(OUT, "quests.js"), "w", encoding="utf-8") as f:
    f.write("window.QUESTS=" + json.dumps(quest_out, ensure_ascii=True, separators=(",", ":")) + ";\n")
cnt = {}
for q in quest_out:
    cnt[q["era"]] = cnt.get(q["era"], 0) + 1
print("quests:", len(quest_out), cnt)

# controller -> era from quests
CTRL_ERA = {}
for qid in ordered:
    for t in QUESTS[qid]["tasks"]:
        for i in ([t["id"]] if "id" in t else t["any"]):
            CTRL_ERA.setdefault(i, ERAS[era[qid]])

# ---------------- multis ----------------
MS = json.load(open(os.path.join(HERE, "multis.json"), encoding="utf-8"))
RJ = json.load(open(os.path.join(HERE, "recipes.json"), encoding="utf-8"))
REC, REMOVED = RJ["recipes"], set(RJ["removed"])

AB = {  # ability -> Spanish label
    "itemIn": "Input Bus", "IMPORT_ITEMS": "Input Bus", "ITEM_IMPORT_BUS": "ULV Input Bus",
    "itemOut": "Output Bus", "EXPORT_ITEMS": "Output Bus",
    "fluidIn": "Input Hatch", "IMPORT_FLUIDS": "Input Hatch", "IMPORT_FLUIDS_1X": "Input Hatch",
    "IMPORT_FLUIDS_4X": "Quadruple Input Hatch", "IMPORT_FLUIDS_9X": "Nonuple Input Hatch",
    "fluidOut": "Output Hatch", "EXPORT_FLUIDS": "Output Hatch",
    "euIn": "Energy Hatch", "INPUT_ENERGY": "Energy Hatch", "euIn2a": "Energy Hatch (2A)", "euIn4a": "Energy Hatch 4A",
    "euIn16a": "Energy Hatch 16A", "maintenance": "Maintenance Hatch", "MAINTENANCE": "Maintenance Hatch",
    "muffler": "Muffler Hatch", "MUFFLER": "Muffler Hatch", "parallelHatch": "Parallel Hatch",
    "PARALLEL_HATCH": "Parallel Hatch", "steamIn": "Steam Input Bus", "STEAM_IMPORT_ITEMS": "Steam Input Bus",
    "steamOut": "Steam Output Bus", "STEAM_EXPORT_ITEMS": "Steam Output Bus", "steam": "Steam Hatch",
    "STEAM": "Steam Hatch", "rotorHolder": "Rotor Holder", "ROTOR_HOLDER": "Rotor Holder",
    "euOut": "Dynamo Hatch", "OUTPUT_ENERGY": "Dynamo Hatch", "PASSTHROUGH_HATCH": "Passthrough Hatch",
    "compIn": "Computation Data Reception", "optIn": "Optical Data Reception", "data": "Data Access Hatch",
    "OBJECT_HOLDER": "Object Holder", "auto": "auto",
}
AUTO = "Buses/Hatches + Energy + Maintenance"


def best_recipe(oid):
    rs = REC.get(oid, [])
    kjs = [r for r in rs if r["src"].startswith("kjs")]
    gt = [r for r in rs if r["src"] == "gt"]
    if oid in REMOVED and kjs:
        gt = []
    pick = (kjs or gt)
    craft = [r for r in pick if r["type"] == "crafting"]
    other = [r for r in pick if r["type"] != "crafting"]
    out = []
    if craft:
        out.append(craft[0])
    if other:
        out.append(other[0])
    return out


def slim(r):
    import idfix
    r = dict(r, **{"in": idfix.clean_inputs(r["in"])}, **({"keys": {kk: idfix.clean_id(vv)[0] for kk, vv in r["keys"].items()}} if r.get("keys") else {}))
    o = {"t": r["type"], "o": r["out"], "in": [[k, v, name(k)] for k, v in r["in"].items()]}
    if r.get("fluids"):
        o["fl"] = [[a, b, name(a + "_bucket") if ":" in a else name("gtceu:" + a + "_bucket")] for a, b in r["fluids"]]
    for k in ("eu", "dur", "circuit"):
        if r.get(k):
            o[k] = r[k]
    if r.get("grid"):
        o["g"] = r["grid"]
        o["k"] = {k: [v, name(v)] for k, v in r["keys"].items()}
    return o


CAT = {  # category from file path
    "primitives": "Primitive", "ore_factories": "Ore processing", "resource_production": "Resources",
    "intermediate_multiblocks": "Boosted", "power": "Power", "stargate_related_multiblocks": "Stargate",
    "very_late_game_multis": "Endgame", "ae2": "AE2", "GTMultiMachines.java": "GregTech", "GCYMMachines.java": "GCYM (Large)",
    "GTResearchMachines.java": "Research",
}
multi_out = []
for m in MS:
    mid = m["id"]
    if "display" in mid:
        continue
    struct, hatch = [], []
    for ch, s in sorted(m["symbols"].items(), key=lambda kv: -kv[1]["count"]):
        sp = s["special"]
        if "air" in sp or "any" in sp or "unmapped" in sp and not s["blocks"]:
            continue
        if "controller" in sp or s["blocks"] == ["minecraft:air"]:  # air is empty space inside the structure, not a part
            continue
        abil = [AB.get(a, a) for a in s["abilities"]]
        if "auto" in s["abilities"]:
            abil = [AUTO] + [a for a in abil if a != "auto"]
        if s["blocks"] or "coil" in sp or "filter" in sp or "battery" in sp or "threading" in sp or "vacuum_pump" in sp:
            if s["blocks"]:
                b0 = s["blocks"][0]
                nm = " / ".join(name(b) for b in s["blocks"][:3])
            else:
                b0 = None
                nm = {"coil": "Heating Coil (any tier)", "filter": "Filter Casing",
                      "battery": "Substation Capacitor (any)", "threading": "Threading block",
                      "vacuum_pump": "Vacuum Pump"}[sp[0] if sp else "coil"] if sp else "?"
            row = {"id": b0, "nm": nm, "n": s["count"]}
            if s.get("min"):
                row["min"] = s["min"]
            if abil:
                row["h"] = list(dict.fromkeys(abil))
            if b0:
                rr = best_recipe(b0)
                if rr:
                    row["r"] = [slim(x) for x in rr]
            struct.append(row)
        elif abil:
            hatch.append({"nm": " / ".join(dict.fromkeys(abil)), "n": s["count"]})
    folder = m["file"].split("/")[1] if m["file"].startswith("kjs/") else m["file"].split("/")[1]
    cat = CAT.get(folder, folder)
    if m["file"].startswith("kjs/") and "/" in m["file"][4:]:
        sub = m["file"].split("/")[1]
        cat = CAT.get(sub, sub)
    multi_out.append({"id": mid, "nm": name(mid), "cat": cat, "era": CTRL_ERA.get(mid, ""),
                      "s": struct, "hx": hatch, "r": [slim(x) for x in best_recipe(mid)], "layers": m["layers"]})

# Guide-side corrections (verified against GTMultiMachines + CraftingRecipeLoader):
# cleanroom ceiling = Filter Casings (parsed row had no id); LCR = 24 inert PTFE casings (10 min) + exactly 1 coil.
for m in multi_out:
    if m["id"] == "gtceu:cleanroom":
        for r in m["s"]:
            if not r.get("id") and "Filter" in (r.get("nm") or ""):
                r["id"] = "gtceu:filter_casing"
    elif m["id"] == "gtceu:large_chemical_reactor" and not any(r.get("id") == "gtceu:inert_machine_casing" for r in m["s"]):
        for r in m["s"]:
            if not r.get("id"):
                r["n"] = 1
                break
        m["s"].insert(0, {"id": "gtceu:inert_machine_casing", "nm": "Chemically Inert PTFE Machine Casing", "n": 24, "min": 10,
                          "h": ["Input Bus", "Output Bus", "Input Hatch", "Output Hatch", "Energy Hatch", "Maintenance Hatch"]})

with open(os.path.join(OUT, "multis.js"), "w", encoding="utf-8") as f:
    f.write("window.MULTIS=" + json.dumps(multi_out, ensure_ascii=True, separators=(",", ":")) + ";\n")
ec = {}
for x in multi_out:
    ec[x["era"] or "?"] = ec.get(x["era"] or "?", 0) + 1
print("multis:", len(multi_out), ec, "with ctrl recipe:", sum(1 for x in multi_out if x["r"]))
