"""Index crafting recipes shipped inside mod jars + vanilla (data/<ns>/recipes/**.json), minus KubeJS removals by id."""
import json, os, re, sys, io, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
from common import require_pack, vanilla_jar
BASE = require_pack()
VANILLA = vanilla_jar()
SS = os.path.join(BASE, "kubejs", "server_scripts")

removed_ids, removed_out = set(), set()
for root, _, files in os.walk(SS):
    if "deprecated" in root:
        continue
    for f in files:
        if f.endswith(".js"):
            t = open(os.path.join(root, f), encoding="utf-8").read()
            for m in re.finditer(r"remove\(\s*\{([^}]*)\}", t):
                for x in re.findall(r"id:\s*['\"]([^'\"]+)['\"]", m.group(1)):
                    removed_ids.add(x)
                for x in re.findall(r"output:\s*['\"]([^'\"]+)['\"]", m.group(1)):
                    removed_out.add(x)
            for m in re.finditer(r"remove\(\s*\[([^\]]*)\]", t):
                pass


def ing(x):
    if isinstance(x, list):
        x = x[0] if x else {}
    if not isinstance(x, dict):
        return None
    if "item" in x:
        return x["item"]
    if "tag" in x:
        return "#" + x["tag"]
    return None


REC = {}


def add(out, r):
    REC.setdefault(out, []).append(r)


def handle(rid, j):
    ty = j.get("type", "")
    res = j.get("result")
    if isinstance(res, dict):
        out, cnt = res.get("item"), int(res.get("count", 1))
    elif isinstance(res, str):
        out, cnt = res, 1
    else:
        return
    if not out or rid in removed_ids or out in removed_out:
        return
    if ty in ("minecraft:crafting_shaped", "create:mechanical_crafting"):
        keys = {k: ing(v) for k, v in (j.get("key") or {}).items()}
        grid = j.get("pattern") or []
        cnts = {}
        for row in grid:
            for ch in row:
                if ch in keys and keys[ch]:
                    cnts[keys[ch]] = cnts.get(keys[ch], 0) + 1
        add(out, {"src": "jar", "id": rid, "type": "crafting" if ty == "minecraft:crafting_shaped" else "mechanical_crafting",
                  "out": cnt, "grid": grid, "keys": {k: v for k, v in keys.items() if v}, "in": cnts})
    elif ty == "minecraft:crafting_shapeless":
        cnts = {}
        for x in j.get("ingredients", []):
            i = ing(x)
            if i:
                cnts[i] = cnts.get(i, 0) + 1
        add(out, {"src": "jar", "id": rid, "type": "shapeless", "out": cnt, "in": cnts})
    elif ty in ("create:item_application", "create:deploying", "create:pressing", "create:mixing", "create:crushing", "create:milling"):
        cnts = {}
        for x in j.get("ingredients", []):
            i = ing(x)
            if i:
                cnts[i] = cnts.get(i, 0) + 1
        add(out, {"src": "jar", "id": rid, "type": ty.split(":")[1], "out": cnt, "in": cnts})


def scan(path):
    try:
        z = zipfile.ZipFile(path)
    except Exception:
        return
    for n in z.namelist():
        if n.startswith("META-INF/jarjar/") and n.endswith(".jar"):
            scan(io.BytesIO(z.read(n)))
            continue
        m = re.match(r"^data/([^/]+)/recipes?/(.+)\.json$", n)
        if not m:
            continue
        try:
            j = json.loads(z.read(n))
        except Exception:
            continue
        if isinstance(j, dict):
            res = j.get("results")
            if "result" not in j and isinstance(res, list) and res:
                j = dict(j, result=res[0])
            handle(f"{m.group(1)}:{m.group(2)}", j)


scan(VANILLA)
for jar in os.listdir(os.path.join(BASE, "mods")):
    if jar.endswith(".jar"):
        scan(os.path.join(BASE, "mods", jar))
json.dump(REC, open(os.path.join(HERE, "jar_recipes.json"), "w", encoding="utf-8"))
print(len(REC), "outputs;", len(removed_ids), "removed ids;", len(removed_out), "removed outputs")
for k in ["create:windmill_bearing", "create:mechanical_bearing", "create:white_sail", "create:sail_frame", "create:mechanical_saw", "create:deployer",
          "create:portable_storage_interface", "create:encased_fan", "create:crushing_wheel", "create:smart_chute", "create_new_age:generator_coil",
          "create_new_age:carbon_brushes", "create_new_age:redstone_magnet", "thermal:device_water_gen", "thermal:dynamo_stirling", "create:mechanical_drill"]:
    print(k, [(r["type"], r["in"]) for r in REC.get(k, [])][:2])
