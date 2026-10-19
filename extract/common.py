"""Shared helpers: configuration (pack / source paths) and display-name resolution for item ids.

Configuration
- PACK_DIR: root of YOUR Star Technology instance (contains mods/, kubejs/, config/).
  Set env STAR_PACK_DIR, or create extract/config.local.json (git-ignored):
      {"pack_dir": "/path/to/Star Technology", "vanilla_jar": "/path/to/1.20.1.jar", "gt_src": "/path/to/gtsrc"}
- VANILLA_JAR: env STAR_VANILLA_JAR / config "vanilla_jar"; default <pack>/../../Install/versions/1.20.1/1.20.1.jar
  (CurseForge layout).
- GT_SRC: env STAR_GT_SRC / config "gt_src"; default <repo>/gtsrc (see fetch_gtsrc.py).
- Outputs: <repo>/guia/data and <repo>/guia/img.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GUIA = os.path.join(REPO, "guia")
DATA_DIR = os.path.join(GUIA, "data")
IMG_DIR = os.path.join(GUIA, "img")


def _local_cfg():
    p = os.path.join(HERE, "config.local.json")
    if os.path.isfile(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except ValueError as e:
            sys.exit("ERROR: extract/config.local.json is not valid JSON: %s" % e)
    return {}


_CFG = _local_cfg()


def _abs(p):
    return os.path.abspath(os.path.expanduser(p)) if p else None


PACK_DIR = _abs(os.environ.get("STAR_PACK_DIR") or _CFG.get("pack_dir"))
GT_SRC = _abs(os.environ.get("STAR_GT_SRC") or _CFG.get("gt_src")) or os.path.join(REPO, "gtsrc")


def require_pack():
    """Return PACK_DIR or exit with a clear message when it is unset / wrong."""
    if not PACK_DIR:
        sys.exit("ERROR: STAR_PACK_DIR is not set.\n"
                 "Point it at your Star Technology instance folder (the one containing mods/ and kubejs/), e.g.\n"
                 "  PowerShell: $env:STAR_PACK_DIR = 'D:/path/to/Star Technology'\n"
                 "  bash:       export STAR_PACK_DIR=/path/to/'Star Technology'\n"
                 "or put {\"pack_dir\": \"...\"} in extract/config.local.json.")
    missing = [d for d in ("mods", "kubejs") if not os.path.isdir(os.path.join(PACK_DIR, d))]
    if missing:
        sys.exit("ERROR: STAR_PACK_DIR=%r does not look like a Star Technology instance (missing: %s)."
                 % (PACK_DIR, ", ".join(missing)))
    return PACK_DIR


def vanilla_jar():
    p = _abs(os.environ.get("STAR_VANILLA_JAR") or _CFG.get("vanilla_jar"))
    if not p:
        p = os.path.abspath(os.path.join(require_pack(), "..", "..", "Install", "versions", "1.20.1", "1.20.1.jar"))
    if not os.path.isfile(p):
        sys.exit("ERROR: vanilla Minecraft 1.20.1 jar not found at %r.\n"
                 "Set STAR_VANILLA_JAR (or \"vanilla_jar\" in extract/config.local.json)." % p)
    return p


_ID_RX = re.compile(r"^[a-z0-9_]+:[a-z0-9_./]+$")


def load_guide():
    """window.GUIDE from guia/data/wiki-data.js (built by tools/build_data.js from docs/); {} if the file is missing."""
    p = os.path.join(DATA_DIR, "wiki-data.js")
    if not os.path.isfile(p):
        return {}
    t = open(p, encoding="utf-8").read()
    i = t.index("window.GUIDE")
    t = t[t.index("=", i) + 1:].lstrip()
    return json.JSONDecoder().raw_decode(t)[0]


def guide_ids():
    """(all_ids, node_ids): every item id mentioned anywhere in the guide data, and the ids of its machine nodes
    (type m/p/s) plus every ['mod:id', number, ...] entry (BOMs and the blocks of hand-built 3D scenes)."""
    allids, nodes = set(), set()

    def walk(o):
        if isinstance(o, str):
            if _ID_RX.match(o):
                allids.add(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                if _ID_RX.match(k):
                    allids.add(k)
                walk(v)
        elif isinstance(o, list):
            # ['mod:id', 4, ...]: BOM entries and hand-built scene blocks (the 3D viewer needs faces for them too)
            if len(o) > 1 and isinstance(o[0], str) and _ID_RX.match(o[0]) and isinstance(o[1], (int, float)):
                nodes.add(o[0])
            for v in o:
                walk(v)
    G = load_guide()
    walk(G)
    for c in (G.get("chains") or {}).values():
        for n in c.get("n", []):
            if len(n) > 3 and n[2] in ("m", "p", "s") and _ID_RX.match(n[3]):
                nodes.add(n[3])
        for b in (c.get("s3d") or {}).get("b", []):
            if b and isinstance(b[0], str) and _ID_RX.match(b[0]):
                nodes.add(b[0])
    return allids, nodes


BASE = PACK_DIR  # may be None; scripts that need the pack call require_pack()
_NF = os.path.join(HERE, "names.json")
_D = json.load(open(_NF, encoding="utf-8")) if os.path.isfile(_NF) else {"names": {}, "materials": {}, "prefixes": {}}
NAMES, MATS, PREF = _D["names"], _D["materials"], _D["prefixes"]

# (regex on gtceu item path, tagprefix key)
_PATTERNS = [
    (r"^(.+)_single_cable$", "cable_gt_single"), (r"^(.+)_double_cable$", "cable_gt_double"),
    (r"^(.+)_quadruple_cable$", "cable_gt_quadruple"), (r"^(.+)_octal_cable$", "cable_gt_octal"),
    (r"^(.+)_hex_cable$", "cable_gt_hex"),
    (r"^(.+)_single_wire$", "wire_gt_single"), (r"^(.+)_double_wire$", "wire_gt_double"),
    (r"^(.+)_quadruple_wire$", "wire_gt_quadruple"), (r"^(.+)_octal_wire$", "wire_gt_octal"),
    (r"^(.+)_hex_wire$", "wire_gt_hex"),
    (r"^fine_(.+)_wire$", "fine_wire"), (r"^double_(.+)_plate$", "double_plate"),
    (r"^dense_(.+)_plate$", "dense_plate"), (r"^small_(.+)_gear$", "small_gear"),
    (r"^small_(.+)_spring$", "small_spring"), (r"^long_(.+)_rod$", "long_rod"),
    (r"^small_(.+)_dust$", "small_dust"), (r"^tiny_(.+)_dust$", "tiny_dust"),
    (r"^crushed_(.+)_ore$", "crushed_ore"), (r"^purified_(.+)_ore$", "purified_ore"),
    (r"^refined_(.+)_ore$", "refined_ore"), (r"^impure_(.+)_dust$", "impure_dust"),
    (r"^pure_(.+)_dust$", "pure_dust"), (r"^exquisite_(.+)_gem$", "exquisite_gem"),
    (r"^flawless_(.+)_gem$", "flawless_gem"), (r"^flawed_(.+)_gem$", "flawed_gem"),
    (r"^chipped_(.+)_gem$", "chipped_gem"), (r"^hot_(.+)_ingot$", "hot_ingot"),
    (r"^raw_(.+)$", "raw"),
    (r"^(.+)_plate$", "plate"), (r"^(.+)_ingot$", "ingot"), (r"^(.+)_dust$", "dust"),
    (r"^(.+)_gear$", "gear"), (r"^(.+)_rod$", "rod"), (r"^(.+)_bolt$", "bolt"),
    (r"^(.+)_screw$", "screw"), (r"^(.+)_ring$", "ring"), (r"^(.+)_spring$", "spring"),
    (r"^(.+)_round$", "round"), (r"^(.+)_foil$", "foil"), (r"^(.+)_frame$", "frame"),
    (r"^(.+)_block$", "block"), (r"^(.+)_rotor$", "rotor"), (r"^(.+)_nugget$", "nugget"),
    (r"^(.+)_gem$", "gem"), (r"^(.+)_lens$", "lens"), (r"^(.+)_buzz_saw_blade$", "buzz_saw_blade"),
    (r"^(.+)_normal_fluid_pipe$", "pipe_normal_fluid"), (r"^(.+)_small_fluid_pipe$", "pipe_small_fluid"),
    (r"^(.+)_large_fluid_pipe$", "pipe_large_fluid"),
]


def _clean(s):
    return re.sub(r"\u00a7.", "", s).strip()


def mat_name(m):
    return MATS.get(m) or m.replace("_", " ").title()


def name(item_id):
    """Best-effort English display name for an id like 'gtceu:steel_plate' or '#forge:plates/steel'."""
    if not item_id:
        return ""
    if item_id.startswith("#"):
        tag = item_id[1:]
        m = re.match(r"^gtceu:circuits/([a-z]+)$", tag)
        if m:
            return f"Any {m.group(1).upper()} Circuit"
        parts = tag.split(":")[-1].split("/")
        if len(parts) == 2:
            return f"{mat_name(parts[1])} {parts[0].rstrip('s').replace('_', ' ')} (tag)"
        return f"[{tag}]"
    if item_id in NAMES:
        return _clean(NAMES[item_id])
    ns, _, path = item_id.partition(":")
    if path.endswith("_bucket"):
        base = path[:-7]
        for k in (f"{ns}:{base}", f"gtceu:{base}"):
            if k in NAMES:
                return _clean(NAMES[k])
        return f"{mat_name(base)}"
    if ns == "gtceu":
        for rx, pref in _PATTERNS:
            m = re.match(rx, path)
            if m and pref in PREF and m.group(1) in MATS:
                return _clean(PREF[pref].replace("%s", MATS[m.group(1)]))
        for rx, pref in _PATTERNS:
            m = re.match(rx, path)
            if m and pref in PREF:
                return _clean(PREF[pref].replace("%s", mat_name(m.group(1))))
    return path.replace("_", " ").title()


if __name__ == "__main__":
    for t in ["gtceu:steel_plate", "gtceu:tin_single_cable", "gtceu:fine_copper_wire", "gtceu:small_steel_gear",
              "gtceu:hot_kanthal_ingot", "gtceu:sulfuric_acid_bucket", "#gtceu:circuits/lv", "gtceu:lv_electric_motor",
              "gtceu:crushed_tin_ore", "gtceu:treated_wood_rod", "gtceu:steel_frame", "kubejs:lv_upgrade_kit"]:
        print(t, "=>", name(t))
