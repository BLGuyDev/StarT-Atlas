"""Lookup recipes: python rq.py <id-or-substring> [...]  (outputs matching; prefix 'in:' to search inputs)"""
import json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(__file__))
from common import name
d = json.load(open(os.path.join(os.path.dirname(__file__), "recipes.json"), encoding="utf-8"))
R = d["recipes"]
for q in sys.argv[1:]:
    inp = q.startswith("in:")
    q = q[3:] if inp else q
    hits = 0
    for out, rs in R.items():
        for r in rs:
            ok = any(q == k or q in k for k in r["in"]) if inp else (q == out or (q.endswith("*") and q[:-1] in out))
            if not ok:
                continue
            hits += 1
            if hits > 25:
                break
            ins = ", ".join(f"{v}x {name(k)}" for k, v in r["in"].items())
            fl = " +fl " + ", ".join(f"{a} {b}" for a, b in r.get("fluids") or []) if r.get("fluids") else ""
            extra = " ".join(x for x in [f"EU {r.get('eu')}" if r.get("eu") else "", f"t {r.get('dur')}" if r.get("dur") else "", f"circ {r['circuit']}" if r.get("circuit") else ""] if x)
            print(f"[{q}] {name(out)} x{r['out']} <= {r['type']}: {ins}{fl} {extra}  ({r['src']})")
    if hits == 0:
        print(f"[{q}] no recipes indexed")
