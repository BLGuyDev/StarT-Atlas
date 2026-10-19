"""Build an item/block/fluid id -> English display name map from mod jars and KubeJS assets."""
import json, os, re, sys, zipfile, io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import require_pack
BASE = require_pack()
OUT = os.path.join(os.path.dirname(__file__), "names.json")


def load_lang(data, names, mats):
    for k, v in data.items():
        if not isinstance(v, str):
            continue
        m = re.match(r"^(item|block|fluid)\.([a-z0-9_]+)\.([a-z0-9_./]+)$", k)
        if m:
            names.setdefault(f"{m.group(2)}:{m.group(3)}", v)
            continue
        m = re.match(r"^material\.([a-z0-9_]+)\.([a-z0-9_]+)$", k)
        if m:
            mats[m.group(2)] = v


def main():
    names, mats, prefixes = {}, {}, {}
    # KubeJS assets first (pack overrides)
    for root, _, files in os.walk(os.path.join(BASE, "kubejs", "assets")):
        for f in files:
            if f == "en_us.json":
                try:
                    data = json.load(open(os.path.join(root, f), encoding="utf-8"))
                except Exception:
                    continue
                load_lang(data, names, mats)
    for jar in os.listdir(os.path.join(BASE, "mods")):
        if not jar.endswith(".jar"):
            continue
        try:
            z = zipfile.ZipFile(os.path.join(BASE, "mods", jar))
        except Exception:
            continue
        for n in z.namelist():
            if re.match(r"^assets/[^/]+/lang/en_us\.json$", n):
                try:
                    data = json.loads(z.read(n).decode("utf-8"))
                except Exception:
                    continue
                load_lang(data, names, mats)
                for k, v in data.items():
                    m = re.match(r"^tagprefix\.([a-z0-9_]+)$", k)
                    if m and isinstance(v, str):
                        prefixes[m.group(1)] = v
    json.dump({"names": names, "materials": mats, "prefixes": prefixes}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(len(names), "names,", len(mats), "materials,", len(prefixes), "prefixes")


if __name__ == "__main__":
    main()
