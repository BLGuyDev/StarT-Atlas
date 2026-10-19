"""Print a compact view of parsed multiblocks: python show_multis.py [id-substring ...]"""
import json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(__file__))
from common import name

ms = json.load(open(os.path.join(os.path.dirname(__file__), "multis.json"), encoding="utf-8"))
flt = sys.argv[1:]
for m in ms:
    if flt and not any(f == m["id"].split(":")[1] or (f.endswith("*") and f[:-1] in m["id"]) for f in flt):
        continue
    parts = []
    for ch, s in sorted(m["symbols"].items(), key=lambda kv: -kv[1]["count"]):
        if "air" in s["special"] or "any" in s["special"]:
            continue
        what = ", ".join(name(b) for b in s["blocks"]) or "/".join(s["special"]) or "?"
        ab = ("+[" + ",".join(s["abilities"]) + "]") if s["abilities"] else ""
        mn = f" min{s['min']}" if s.get("min") else ""
        parts.append(f"{ch}={s['count']}x {what}{mn}{ab}")
    print(f"{m['id']} ({m['file']}, {m['layers']} layers): " + " | ".join(parts))
