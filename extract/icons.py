"""Render item icons and isometric multiblock previews from the pack's real textures."""
import io, json, os, re, zipfile, functools
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(__file__)
import sys
sys.path.insert(0, HERE)
from common import GT_SRC, require_pack, vanilla_jar
BASE = require_pack()
VANILLA = vanilla_jar()
SRC = GT_SRC

# ------------------------------------------------------------------ virtual asset FS
FS = {}  # 'ns/path' (after assets/) -> (zip or None, name or filepath)
_zips = {}


def _add_zip(path, prio):
    try:
        z = zipfile.ZipFile(path)
    except Exception:
        return
    _zips[str(path)] = z
    for n in z.namelist():
        if n.startswith("assets/") and not n.endswith("/"):
            k = n[7:]
            if k not in FS or FS[k][2] < prio:
                FS[k] = (z, n, prio)
        elif n.startswith("META-INF/jarjar/") and n.endswith(".jar"):
            _add_zip(io.BytesIO(z.read(n)), prio)


TEXIDX = {}  # 'ns/basename' -> texture key, for KubeJS items with nested texture folders


_add_zip(VANILLA, 0)
for j in os.listdir(os.path.join(BASE, "mods")):
    if j.endswith(".jar"):
        _add_zip(os.path.join(BASE, "mods", j), 1)
for root, _, files in os.walk(os.path.join(BASE, "kubejs", "assets")):
    for f in files:
        p = os.path.join(root, f)
        k = os.path.relpath(p, os.path.join(BASE, "kubejs", "assets")).replace("\\", "/")
        FS[k] = (None, p, 2)


for _k in list(FS):
    _m = re.match(r"^([a-z0-9_]+)/textures/(item|block)/(?:.*/)?([a-z0-9_]+)\.png$", _k)
    if _m:
        _key = f"{_m.group(1)}/{_m.group(3)}"
        _val = f"{_m.group(1)}:{_k.split('/textures/', 1)[1][:-4]}"
        if _key not in TEXIDX or _m.group(2) == "item":
            TEXIDX[_key] = _val


def read(k):
    e = FS.get(k)
    if not e:
        return None
    z, n, _ = e
    return z.read(n) if z else open(n, "rb").read()


def rl(s, default_ns="minecraft"):
    s = s.lstrip("#")
    return (s.split(":", 1) if ":" in s else (default_ns, s))


@functools.lru_cache(maxsize=None)
def tex(name):
    """Texture 'ns:block/x' -> RGBA 16x16-ish (first animation frame) or None."""
    ns, p = rl(name)
    b = read(f"{ns}/textures/{p}.png")
    if b is None:
        return None
    im = Image.open(io.BytesIO(b)).convert("RGBA")
    w, h = im.size
    if h > w:
        im = im.crop((0, 0, w, w))
    return im


@functools.lru_cache(maxsize=None)
def model(name, kind="block"):
    ns, p = rl(name)
    if "/" not in p:
        p = f"{kind}/{p}"
    b = read(f"{ns}/models/{p}.json")
    if b is None:
        return None
    try:
        return json.loads(b)
    except Exception:
        return None


def resolve(name, kind="item"):
    """Follow parents; return (textures dict merged child-wins, list of parent ids, raw)."""
    texs, chain, cur, first = {}, [], name, None
    for _ in range(12):
        m = model(cur, kind)
        if m is None:
            break
        if first is None:
            first = m
        if "variants" in m and m.get("loader") == "gtceu:machine":
            v = list(m["variants"].values())[0]
            v = v[0] if isinstance(v, list) else v
            mm = v.get("model", {}) if isinstance(v, dict) else {}
            if isinstance(mm, str):
                mm = {"parent": mm}
            for k, t in mm.get("textures", {}).items():
                texs.setdefault(k, t)
            if mm.get("parent"):
                chain.append(mm["parent"])
                cur = mm["parent"]
                kind = "block"
                continue
        for k, t in (m.get("textures") or {}).items():
            texs.setdefault(k, t)
        par = m.get("parent")
        if not par:
            break
        chain.append(par)
        cur = par
        kind = "block"
    # resolve #refs
    for _ in range(5):
        for k, v in list(texs.items()):
            if isinstance(v, str) and v.startswith("#"):
                texs[k] = texs.get(v[1:], v)
    return texs, chain, first


# ------------------------------------------------------------------ materials
MAT = {}


def _parse_materials():
    for fn in os.listdir(SRC):
        if not fn.endswith("Materials.java"):
            continue
        t = open(os.path.join(SRC, fn), encoding="utf-8").read()
        for m in re.finditer(r"new Material\.Builder\(GTCEu\.id\(\"([a-z0-9_]+)\"\)\)([\s\S]*?)\.buildAndRegister\(\)", t):
            body = m.group(2)
            c = re.search(r"\.colors?\(0x([0-9a-fA-F]{6})(?:,\s*0x([0-9a-fA-F]{6}))?", body)
            s2 = re.search(r"\.secondaryColor\(0x([0-9a-fA-F]{6})", body)
            ic = re.search(r"\.iconSet\((?:MaterialIconSet\.)?([A-Z_]+)\)", body)
            MAT[m.group(1)] = {"c": int(c.group(1), 16) if c else 0xFFFFFF,
                               "c2": int((c.group(2) if c and c.group(2) else (s2.group(1) if s2 else "0")), 16) or None,
                               "set": ic.group(1).lower() if ic else ("dull" if ".dust(" in body and ".ingot(" not in body else "metallic")}
    sets = "dull|metallic|shiny|bright|rough|fine|sand|gem_vertical|gem_horizontal|diamond|emerald|ruby|lapis|flint|certus|quartz|opal|glass|radioactive|magnetic|netherstar|lignite|wood|fluid|gas|lapis"
    for root, _, files in os.walk(os.path.join(BASE, r"kubejs/startup_scripts/elements_materials")):
        for f in files:
            if not f.endswith(".js"):
                continue
            t = open(os.path.join(root, f), encoding="utf-8").read()
            for m in re.finditer(r"(?:create|\w+)\(\s*(?:event\s*,\s*)?'([a-z0-9_]+)'", t):
                name = m.group(1)
                seg = t[m.end():m.end() + 900]
                end = re.search(r"\)\s*;", seg)
                seg = seg[:end.end()] if end else seg[:400]
                hx = re.findall(r"0x([0-9a-fA-F]{6})", seg)
                if not hx:
                    continue
                ic = re.search(r"\b(?:ICONSETS\.|GTMaterialIconSet\.)?(" + sets + r")\b", seg.replace("'", " "), re.I)
                d = MAT.setdefault(name, {"c": 0xFFFFFF, "c2": None, "set": "metallic"})
                d["c"] = int(hx[0], 16)
                if len(hx) > 1 and "SecColor" in t[max(0, m.start() - 40):m.start() + 40]:
                    d["c2"] = int(hx[1], 16)
                if ic:
                    d["set"] = ic.group(1).lower()


_parse_materials()


def _parse_class_materials():
    """Material colors compiled into the GTCEu fork jar (e.g. GCYMMaterials: hsla_steel, hastelloy_x, carbides): scan ldc constants."""
    import struct
    for j in os.listdir(os.path.join(BASE, "mods")):
        if not j.startswith("gtceu"):
            continue
        try:
            z = zipfile.ZipFile(os.path.join(BASE, "mods", j))
        except Exception:
            continue
        for n in z.namelist():
            if not (n.startswith("com/gregtechceu/gtceu/common/data/materials/") and n.endswith("Materials.class")):
                continue
            d = z.read(n)
            cnt = struct.unpack(">H", d[8:10])[0]
            cp, p, i = [None] * cnt, 10, 1
            try:
                while i < cnt:
                    tg = d[p]
                    if tg == 1:
                        ln = struct.unpack(">H", d[p + 1:p + 3])[0]
                        cp[i] = ("u", d[p + 3:p + 3 + ln].decode("utf8", "replace"))
                        p += 3 + ln
                    elif tg == 3:
                        cp[i] = ("i", struct.unpack(">i", d[p + 1:p + 5])[0])
                        p += 5
                    elif tg == 4:
                        p += 5
                    elif tg in (5, 6):
                        p += 9
                        i += 1
                    elif tg == 8:
                        cp[i] = ("r", struct.unpack(">H", d[p + 1:p + 3])[0])
                        p += 3
                    elif tg in (7, 16, 19, 20):
                        p += 3
                    elif tg in (9, 10, 11, 12, 17, 18):
                        p += 5
                    elif tg == 15:
                        p += 4
                    else:
                        raise ValueError(tg)
                    i += 1
            except Exception:
                continue
            seq = []
            for q in range(len(d) - 3):
                b = d[q]
                if b == 0x12:
                    idx = d[q + 1]
                elif b == 0x13:
                    idx = (d[q + 1] << 8) | d[q + 2]
                else:
                    continue
                e = cp[idx] if idx < cnt else None
                if not e:
                    continue
                if e[0] == "r" and cp[e[1]] and re.fullmatch(r"[a-z][a-z0-9_]{2,}", cp[e[1]][1]):
                    seq.append(("s", cp[e[1]][1]))
                elif e[0] == "i" and 0x8000 <= e[1] <= 0xFFFFFF:
                    seq.append(("i", e[1]))
            cur = None
            for kind, v in seq:
                if kind == "s":
                    cur = v
                elif cur:
                    if cur not in MAT:
                        MAT[cur] = {"c": v, "c2": None, "set": "metallic"}
                    cur = None


_parse_class_materials()
# materials whose colour is only computed at runtime (composites / AE2): rough manual colours
for _k, _c in (("fluix", 0x5B3F8C), ("gold_skystone_alloy", 0xB8A140), ("diamond_skystone_alloy", 0x4AC7C0), ("certus_quartz_skystone_alloy", 0x5A9FA0),
               ("netherite_gold_skystone_alloy", 0x978B2D), ("netherite_certus_quartz_skystone_alloy", 0x396A6C), ("niter", 0xD9C7C0)):
    MAT.setdefault(_k, {"c": _c, "c2": None, "set": "dull"})
try:
    _KNOWN = set(json.load(open(os.path.join(HERE, "names.json"), encoding="utf-8"))["materials"])
except Exception:
    _KNOWN = set()

SET_PARENT = {"metallic": "dull", "magnetic": "metallic", "shiny": "metallic", "bright": "shiny", "rough": "dull",
              "fine": "rough", "sand": "fine", "wood": "rough", "gem_vertical": "shiny", "gem_horizontal": "shiny",
              "emerald": "gem_vertical", "diamond": "gem_horizontal", "ruby": "gem_horizontal", "opal": "gem_horizontal",
              "glass": "gem_vertical", "lapis": "dull", "flint": "rough", "lignite": "rough", "quartz": "dull",
              "certus": "dull", "netherstar": "shiny", "radioactive": "metallic", "fluid": "dull", "gas": "dull"}


def set_chain(s):
    out = []
    while s and s not in out:
        out.append(s)
        s = SET_PARENT.get(s)
    if "dull" not in out:
        out.append("dull")
    return out


def tint(im, rgb):
    if im is None:
        return None
    a = np.asarray(im).astype(np.float32)
    r, g, b = ((rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255)
    a[..., 0] *= r / 255
    a[..., 1] *= g / 255
    a[..., 2] *= b / 255
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def comp(*ims):
    base = None
    for im in ims:
        if im is None:
            continue
        im = im.resize((16, 16), Image.NEAREST) if im.size != (16, 16) else im
        base = im.copy() if base is None else Image.alpha_composite(base, im)
    return base


def mat_tex(kind, mat, prefix):
    """kind: item/block. Compose material-set texture for prefix with tints."""
    info = MAT.get(mat, {"c": 0xBBBBBB, "c2": None, "set": "metallic"})
    for s in set_chain(info["set"]):
        p = f"gtceu:{kind}/material_sets/{s}/{prefix}"
        base = tex(p)
        if base is not None:
            sec = tex(p + "_secondary")
            ov = tex(p + "_overlay")
            return comp(tint(base, info["c"]), tint(sec, info["c2"] or info["c"]) if sec is not None else None, ov)
    return None


# ------------------------------------------------------------------ isometric cube
S = 32


def _face_map(size, face):
    """Return arrays (u,v,mask) mapping output pixels -> texture coords for a face of an iso cube in a size x size box."""
    h = size / 4.0
    ys, xs = np.mgrid[0:size, 0:size].astype(np.float32) + 0.5
    cx = size / 2
    if face == "top":
        # rhombus: (cx,0) (size,h) (cx,2h) (0,h); u along (cx,0)->(size,h), v along (cx,0)->(0,h)
        o = np.array([cx, 0.0]); U = np.array([cx, h]); V = np.array([-cx, h])
    elif face == "left":  # +z face (front)
        o = np.array([0.0, h]); U = np.array([cx, h]); V = np.array([0.0, 2 * h])
    else:  # right, +x face
        o = np.array([cx, 2 * h]); U = np.array([cx, -h]); V = np.array([0.0, 2 * h])
    M = np.array([[U[0], V[0]], [U[1], V[1]]])
    inv = np.linalg.inv(M)
    dx, dy = xs - o[0], ys - o[1]
    u = inv[0, 0] * dx + inv[0, 1] * dy
    v = inv[1, 0] * dx + inv[1, 1] * dy
    mask = (u >= 0) & (u < 1) & (v >= 0) & (v < 1)
    return u, v, mask


@functools.lru_cache(maxsize=8)
def _maps(size):
    return {f: _face_map(size, f) for f in ("top", "left", "right")}


def cube(top, front, side, size=S):
    out = np.zeros((size, size, 4), np.float32)
    shade = {"top": 1.0, "left": 0.82, "right": 0.64}
    for f, t in (("top", top), ("left", front), ("right", side)):
        if t is None:
            continue
        a = np.asarray(t.convert("RGBA").resize((16, 16), Image.NEAREST)).astype(np.float32)
        u, v, m = _maps(size)[f]
        ui = np.clip((u * 16).astype(int), 0, 15)
        vi = np.clip((v * 16).astype(int), 0, 15)
        px = a[vi, ui]
        px[..., :3] *= shade[f]
        sel = m & (px[..., 3] > 8)
        out[sel] = px[sel]
    return Image.fromarray(out.clip(0, 255).astype(np.uint8), "RGBA")


def faces_from(texs):
    """Pick top/front/side textures (+overlays) from a resolved texture dict."""
    g = lambda *ks: next((texs[k] for k in ks if k in texs and isinstance(texs[k], str) and not texs[k].startswith("#")), None)
    allt = g("all", "texture", "particle", "bot_all", "base")
    top = g("top", "up", "end", "all", "bot_all") or allt
    side = g("side", "east", "north", "all", "bot_all") or allt
    front = g("front", "north", "side", "all", "bot_all") or allt
    tl = lambda n: tex(n) if n else None
    T, F, Sd = tl(top), tl(front), tl(side)
    for k, base in (("overlay_front", "F"), ("overlay_top", "T"), ("overlay_side", "S")):
        if k in texs and "void" not in texs[k]:
            ov = tex(texs[k])
            if ov is not None:
                if base == "F":
                    F = comp(F, ov)
                elif base == "T":
                    T = comp(T, ov)
                else:
                    Sd = comp(Sd, ov)
    if "top_all" in texs and texs["top_all"]:
        ov = tex(texs["top_all"])
        T, F, Sd = comp(T, ov), comp(F, ov), comp(Sd, ov)
    if T is None and F is None and Sd is None:
        for k, v in texs.items():
            if isinstance(v, str) and not v.startswith("#") and "overlay" not in k and tex(v) is not None:
                t = tex(v)
                return t, t, t
    return T, F, Sd


# KubeJS-registered machines: workableCasingModel(casing, overlayFolder)
KJS_MODEL = {}
for root, _, files in os.walk(os.path.join(BASE, r"kubejs/startup_scripts")):
    for f in files:
        if f.endswith(".js"):
            t = open(os.path.join(root, f), encoding="utf-8").read()
            for m in re.finditer(r"\.create\(\s*'([a-z0-9_]+)'", t):
                seg = t[m.end():m.end() + 6000]
                nx = re.search(r"\.create\(\s*'", seg)
                if nx:
                    seg = seg[:nx.start()]
                w = re.search(r"\.workableCasingModel\(\s*'([^']+)'\s*,\s*'([^']+)'", seg)
                if w:
                    KJS_MODEL[m.group(1)] = (w.group(1), w.group(2))


# KubeJS items/blocks registered with .texture()/.textureAll()/.textureJson() (no model file on disk).
# Ids and textures may be JS template literals (`${tier}_chevron`), so keep templates and resolve per id.
KJS_REG = []
for root, _, files in os.walk(os.path.join(BASE, r"kubejs/startup_scripts")):
    for f in files:
        if not f.endswith(".js"):
            continue
        t = open(os.path.join(root, f), encoding="utf-8").read()
        for m in re.finditer(r"\.create\(\s*([`'])([^`']+)\1", t):
            seg = t[m.end():m.end() + 3000]
            nx = re.search(r"\.create\(\s*[`']", seg)
            if nx:
                seg = seg[:nx.start()]
            w = re.search(r"\.(?:texture|textureAll|textureSide)\(\s*([`'])((?:(?!\1).)*:(?:(?!\1).)+)\1", seg)
            lay = [x[1] for x in re.findall(r"layer\d\s*:\s*([`'])((?:(?!\1).)+)\1", seg)]
            fb = None
            if not w:
                w2 = re.search(r"\.firebox\(\s*'([^']+)'\s*,\s*'([^']+)'", seg)
                if w2:
                    fb = w2.group(2)
                else:
                    w2 = re.search(r"\.(?:simple|bloom)\(\s*'([^']+)'", seg)
                    fb = w2.group(1) if w2 else None
            tt = w.group(2) if w else fb
            if tt or lay:
                KJS_REG.append((m.group(2), tt, lay))
        # helper functions: function f(id, texture) { event.create(id)...textureAll(`..${texture}`) }  +  f('a', 'b') calls
        for fm in re.finditer(r"(?:function\s+(\w+)\s*\(([^)]*)\)|const\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>)", t):
            fname = fm.group(1) or fm.group(3)
            params = [p.strip() for p in (fm.group(2) if fm.group(1) else fm.group(4)).split(",") if p.strip()]
            body = t[fm.end():fm.end() + 2500]
            cm = re.search(r"\.create\(\s*(\w+)\s*[,)]", body)
            if not cm or cm.group(1) not in params:
                continue
            bseg = body[cm.end():]
            nx = re.search(r"\.create\(", bseg)
            bseg = bseg[:nx.start()] if nx else bseg
            wm = re.search(r"\.(?:texture|textureAll)\(\s*([`'])((?:(?!\1).)*:(?:(?!\1).)+)\1", bseg)
            if not wm:
                continue
            for call in re.finditer(r"\b" + fname + r"\(\s*([^)]*)\)", t[fm.end():]):
                args = [a.strip().strip("'`\"") for a in call.group(1).split(",")]
                if len(args) < len(params) or not args[params.index(cm.group(1))]:
                    continue
                vals = dict(zip(params, args))
                KJS_REG.append((vals[cm.group(1)], re.sub(r"\$\{(\w+)\}", lambda q: vals.get(q.group(1), q.group(0)), wm.group(2)), []))


def _tpl_eval(expr, vals):
    out = ""
    for part in expr.split("+"):
        part = part.strip()
        if len(part) >= 2 and part[0] in "'`" and part[-1] == part[0]:
            out += part[1:-1]
        elif part in vals:
            out += vals[part]
        else:
            return None
    return out


def kjs_tex(path):
    """-> (texture ref or None, [layer refs]) for a KubeJS-registered item/block id (path without namespace)."""
    for idtpl, ttpl, lay in KJS_REG:
        exprs, rx, last = [], "", 0
        for mm in re.finditer(r"\${([^}]+)}", idtpl):
            rx += re.escape(idtpl[last:mm.start()]) + f"(?P<v{len(exprs)}>[a-z0-9_]+?)"
            exprs.append(mm.group(1).strip())
            last = mm.end()
        rx += re.escape(idtpl[last:])
        mt = re.fullmatch(rx, path)
        if not mt:
            continue
        vals = {e: mt.group(f"v{i}") for i, e in enumerate(exprs)}

        def sub(s):
            if s is None:
                return None
            ok = [True]

            def r(mm):
                v = _tpl_eval(mm.group(1), vals)
                if v is None:
                    ok[0] = False
                return v or ""
            res = re.sub(r"\${([^}]+)}", r, s)
            return res if ok[0] else None
        ref = sub(ttpl)
        layers = [x for x in (sub(l) for l in lay) if x]
        if (ref and tex(ref) is not None) or any(tex(x) is not None for x in layers):
            return ref, layers
    return None, []


# ------------------------------------------------------------------ item icons
PREF = [
    (r"^(.+)_single_cable$", "cable"), (r"^(.+)_(double|quadruple|octal|hex)_cable$", "cable"),
    (r"^(.+)_(single|double|quadruple|octal|hex)_wire$", "wire"),
    (r"^fine_(.+)_wire$", "wire_fine"), (r"^double_(.+)_plate$", "plate_double"), (r"^dense_(.+)_plate$", "plate_dense"),
    (r"^small_(.+)_gear$", "gear_small"), (r"^small_(.+)_spring$", "spring_small"), (r"^long_(.+)_rod$", "rod_long"),
    (r"^small_(.+)_dust$", "dust_small"), (r"^tiny_(.+)_dust$", "dust_tiny"), (r"^crushed_(.+)_ore$", "crushed"),
    (r"^purified_(.+)_ore$", "crushed_purified"), (r"^refined_(.+)_ore$", "crushed_refined"),
    (r"^impure_(.+)_dust$", "dust_impure"), (r"^pure_(.+)_dust$", "dust_pure"), (r"^exquisite_(.+)_gem$", "gem_exquisite"),
    (r"^flawless_(.+)_gem$", "gem_flawless"), (r"^flawed_(.+)_gem$", "gem_flawed"), (r"^chipped_(.+)_gem$", "gem_chipped"),
    (r"^hot_(.+)_ingot$", "ingot_hot"), (r"^raw_(.+)$", "raw_ore"),
    (r"^(.+)_ultradense_plate$", "ultradense_plate"), (r"^(.+)_wire_spool$", "wire_spool"), (r"^(.+)_foil_ream$", "foil_ream"),
    (r"^(.+)_buzz_saw_blade$", "tool_head_buzz_saw"), (r"^(.+)_drill_head$", "tool_head_drill"), (r"^(.+)_chainsaw_head$", "tool_head_chainsaw"),
    (r"^(.+)_turbine_blade$", "turbine_blade"), (r"^(.+)_ball_bearing$", "ball_bearing"),
    (r"^(.+)_plate$", "plate"), (r"^(.+)_ingot$", "ingot"), (r"^(.+)_dust$", "dust"), (r"^(.+)_gear$", "gear"),
    (r"^(.+)_rod$", "rod"), (r"^(.+)_bolt$", "bolt"), (r"^(.+)_screw$", "screw"), (r"^(.+)_ring$", "ring"),
    (r"^(.+)_spring$", "spring"), (r"^(.+)_round$", "round"), (r"^(.+)_foil$", "foil"), (r"^(.+)_frame$", "frame"),
    (r"^(.+)_block$", "block"), (r"^(.+)_rotor$", "rotor"), (r"^(.+)_nugget$", "nugget"), (r"^(.+)_gem$", "gem"),
    (r"^(.+)_lens$", "lens"), (r"^(.+)_(tiny|small|normal|large|huge|quadruple|nonuple)_fluid_pipe$", "pipe"),
    (r"^(.+)_(small|normal|large|huge)_item_pipe$", "pipe"),
]


def up(im, size=S):
    return im.resize((size, size), Image.NEAREST) if im is not None else None


def fluid_icon(mat_or_id):
    ns, p = rl(mat_or_id, "gtceu")
    base = p[:-7] if p.endswith("_bucket") else p
    t = tex(f"{ns}:block/fluids/fluid.{base}") or tex(f"gtceu:block/fluids/fluid.{base}")
    if t is None and base.endswith("_plasma") and base[:-7] in MAT:
        pt = tex("gtceu:block/fluids/fluid.plasma") or tex("gtceu:block/material_sets/dull/plasma")
        t = tint(pt, MAT[base[:-7]]["c"]) if pt is not None else None
    if t is None:
        info = MAT.get(base)
        for pre in ("liquid_", "molten_", "gaseous_"):
            if info is None and base.startswith(pre):
                info = MAT.get(base[len(pre):])
        lt = tex("gtceu:block/material_sets/dull/liquid")
        if info and lt is not None:
            t = tint(lt, info["c"])
        elif base in ("water", "lava"):
            t = tex(f"minecraft:block/{base}_still")
            if base == "water" and t is not None:
                t = tint(t, 0x3F76E4)
    if t is None:
        return None
    t = t.resize((16, 16), Image.NEAREST)
    # droplet mask
    mask = Image.new("L", (32, 32), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((6, 11, 26, 31), fill=255)
    d.polygon([(16, 1), (7, 19), (25, 19)], fill=255)
    big = t.resize((32, 32), Image.NEAREST)
    out = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    out.paste(big, (0, 0), mask)
    ImageDraw.Draw(out).ellipse((10, 17, 15, 22), fill=(255, 255, 255, 110))
    return out


def wire_icon(mat, cable):
    info = MAT.get(mat, {"c": 0xAAAAAA})
    c = info["c"]
    col = ((c >> 16) & 255, (c >> 8) & 255, c & 255, 255)
    im = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if cable:
        d.line((5, 27, 27, 5), fill=(40, 40, 40, 255), width=11)
        d.line((5, 27, 27, 5), fill=(70, 70, 70, 255), width=7)
        d.ellipse((22, 1, 31, 10), fill=col)
    else:
        d.line((5, 27, 27, 5), fill=tuple(int(x * 0.6) for x in col[:3]) + (255,), width=7)
        d.line((5, 27, 27, 5), fill=col, width=4)
    return im


def gt_material_item(path):
    for rx, pre in PREF:
        m = re.match(rx, path)
        if not m:
            continue
        mat = m.group(1)
        if mat not in MAT:
            if mat not in _KNOWN:
                continue
            MAT[mat] = {"c": 0x9A9A9A, "c2": None, "set": "metallic"}  # registered material, colour unknown: neutral grey
        if pre in ("cable", "wire"):
            return wire_icon(mat, pre == "cable")
        if pre == "pipe":
            info = MAT[mat]
            im = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
            c = info["c"]
            ImageDraw.Draw(im).ellipse((5, 5, 27, 27), outline=((c >> 16) & 255, (c >> 8) & 255, c & 255, 255), width=6)
            return im
        if pre in ("block", "frame"):
            t = mat_tex("block", mat, "block" if pre == "block" else "frame_gt")
            return cube(t, t, t) if t is not None else None
        t = mat_tex("item", mat, pre)
        if t is not None:
            return up(t)
    return None


@functools.lru_cache(maxsize=None)
def icon(item_id):
    if not item_id or item_id.startswith("#"):
        return None
    ns, path = rl(item_id)
    if path.endswith("_bucket") and ns in ("gtceu", "minecraft", "thermal", "exnihilosequentia") and path not in ("wooden_bucket",):
        f = fluid_icon(item_id)
        if f is not None:
            return f
    m = re.fullmatch(r"(ancient|draconic)_stargate_(ring|base|chevron)_block", path) if ns == "kubejs" else None
    if m:  # gate_blocks.js builds the id from gate + type and textures each side separately
        g, ty = m.groups()
        tops = tex(f"kubejs:block/stargate/{g}_stargate_block_tops")
        side = tex(f"kubejs:block/stargate/{g}_stargate_block_{'chevron' if ty == 'chevron' else 'ring'}")
        front = tex(f"kubejs:block/stargate/{g}_stargate_block_{ty}")
        if tops is not None and side is not None:
            return cube(tops, front if front is not None else side, side)
    m = re.fullmatch(r"([a-z]+)_stabilization_module", path) if ns == "gtceu" else None
    if m:  # custom_hatches.js: tiered hull model + kubejs overlay
        cas = tex(f"gtceu:block/casings/voltage/{m.group(1)}/side")
        ov = tex("kubejs:block/machines/stabilization_core/overlay_front")
        if cas is not None and ov is not None:
            return cube(cas, comp(cas, ov), cas)
    if ns == "gtceu" and model(f"{ns}:item/{path}", "item") is None:
        g = gt_material_item(path)
        if g is not None:
            return g
    texs, chain, first = resolve(f"{ns}:item/{path}", "item")
    if first is None and ns in ("gtceu", "start_core") and path in KJS_MODEL:
        cas, ovf = KJS_MODEL[path]
        T = tex(cas)
        F = comp(T, tex(ovf + "/overlay_front"))
        return cube(T, F, T)
    OVR = {"functionalstorage:oak_1": ("functionalstorage:block/oak_side", "functionalstorage:block/oak_front_1"),
           "functionalstorage:oak_2": ("functionalstorage:block/oak_side", "functionalstorage:block/oak_front_2"),
           "functionalstorage:oak_4": ("functionalstorage:block/oak_side", "functionalstorage:block/oak_front_4"),
           "fluxnetworks:flux_plug": ("fluxnetworks:block/flux_plug_on", "fluxnetworks:block/flux_plug_on"),
           "fluxnetworks:flux_point": ("fluxnetworks:block/flux_point_on", "fluxnetworks:block/flux_point_on")}
    if item_id in OVR:
        a, b = OVR[item_id]
        return cube(tex(a), tex(b), tex(a))
    if first is None and ns == "gtceu":
        texs, chain, first = resolve(f"gtceu:block/machine/{path}", "block")
    if first is None:
        # block without item model: try blockstate
        bs = read(f"{ns}/blockstates/{path}.json")
        if bs:
            try:
                j = json.loads(bs)
                v = list(j.get("variants", {}).values())[0] if "variants" in j else None
                v = v[0] if isinstance(v, list) else v
                if v:
                    texs, chain, first = resolve(v["model"], "block")
            except Exception:
                pass
    if first is None:
        if ns == "gtceu":
            g = gt_material_item(path)
            if g is not None:
                return g
        for k in (f"{ns}:item/{path}", f"{ns}:block/{path}"):
            if tex(k) is not None:
                return up(tex(k)) if "item/" in k else cube(tex(k), tex(k), tex(k))
        k = TEXIDX.get(f"{ns}/{path}")
        if not k:
            cands = [key for key in TEXIDX if key.startswith(ns + "/") and path in key.split("/", 1)[1]]
            if cands:
                k = TEXIDX[min(cands, key=len)]
        if k:
            t = tex(k)
            if t is not None:
                return up(t) if ":item/" in k else cube(t, t, t)
        return None
    if "layer0" in texs and not any("block/" in c and "item/" not in c for c in chain[:1]):
        layers = [tex(texs[k]) for k in sorted(texs) if re.fullmatch(r"layer\d", k)]
        c = comp(*layers)
        if c is not None:
            return up(c)
    T, F, Sd = faces_from(texs)
    if T is None and F is None:
        if "layer0" in texs:
            return up(tex(texs["layer0"]))
        return None
    return cube(T, F or T, Sd or F or T)


def placeholder(label):
    im = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, 29, 29), 5, fill=(110, 118, 126, 255))
    txt = "".join(w[0] for w in re.split(r"[_\s]+", label) if w)[:3].upper()
    d.text((16, 16), txt, fill=(255, 255, 255, 255), anchor="mm")
    return im


# ------------------------------------------------------------------ block faces for multiblock renders
@functools.lru_cache(maxsize=None)
def block_faces(block_id):
    if block_id in ("coil",):
        t = tex("gtceu:block/casings/coils/machine_coil_cupronickel")
        return (t, t, t)
    ns, path = rl(block_id)
    if ns == "gtceu" and path.endswith("_frame"):
        t = mat_tex("block", path[:-6], "frame_gt")
        if t is not None:
            return (t, t, t)
    bs = read(f"{ns}/blockstates/{path}.json")
    texs = None
    if bs:
        try:
            j = json.loads(bs)
            if "variants" in j:
                v = list(j["variants"].values())[0]
            else:
                v = j["multipart"][0]["apply"]
            v = v[0] if isinstance(v, list) else v
            texs, _, _ = resolve(v["model"], "block")
        except Exception:
            texs = None
    if not texs:
        texs, _, first = resolve(f"{ns}:item/{path}", "item")
        if not first:
            texs = None
    if texs:
        T, F, Sd = faces_from(texs)
        if T is not None or F is not None:
            return (T or F, F or T, Sd or F or T)
        if "layer0" in texs:
            t = tex(texs["layer0"])
            return (t, t, t)
    if ns == "gtceu" and path.endswith("_block"):
        t = mat_tex("block", path[:-6], "block")
        if t is not None:
            return (t, t, t)
    if ns == "minecraft":
        t = tex(f"minecraft:block/{path}")
        if t is not None:
            return (t, t, t)
    return None


def controller_faces(mid):
    ns, path = rl(mid)
    if path in KJS_MODEL:
        cas, ovf = KJS_MODEL[path]
        T = tex(cas)
        return (T, comp(T, tex(ovf + "/overlay_front")), T)
    texs, _, first = resolve(f"gtceu:block/machine/{path}", "block")
    if first:
        T, F, Sd = faces_from(texs)
        return (T, F, Sd)
    return None


def render_multi(m, tile=24):
    """m: entry of multis.json (symbols + aisles). Returns PIL image or None."""
    aisles = m.get("aisles")
    if not aisles:
        return None
    sprites = {}
    for ch, s in m["symbols"].items():
        if "controller" in s["special"]:
            f = controller_faces(m["id"])
        elif s["blocks"]:
            f = None
            for b in s["blocks"]:
                f = block_faces(b)
                if f:
                    break
        elif "coil" in s["special"]:
            f = block_faces("coil")
        elif "filter" in s["special"]:
            f = block_faces("gtceu:filter_casing")
        else:
            f = None
        if f is None and s["abilities"] and not ("air" in s["special"] or "any" in s["special"]):
            t = tex("gtceu:block/casings/voltage/lv/side")
            f = (t, t, t)
        if f:
            sprites[ch] = cube(*f, size=tile)
    cells = []
    D = len(aisles)
    for z, a in enumerate(aisles):
        for y, row in enumerate(a):
            for x, ch in enumerate(row):
                if ch in sprites:
                    cells.append((x, y, z, ch))
    if not cells:
        return None
    W = max(c[0] for c in cells) + 1
    hw, hh = tile / 2, tile / 4
    pos = []
    for x, y, z, ch in cells:
        X = (W - 1 - x)
        sx = (X - z) * hw
        sy = (X + z) * hh - y * (tile / 2)
        pos.append((X + y + z, sx, sy, ch))
    minx = min(p[1] for p in pos); miny = min(p[2] for p in pos)
    maxx = max(p[1] for p in pos) + tile; maxy = max(p[2] for p in pos) + tile
    img = Image.new("RGBA", (int(maxx - minx) + 2, int(maxy - miny) + 2), (0, 0, 0, 0))
    for _, sx, sy, ch in sorted(pos, key=lambda p: p[0]):
        img.alpha_composite(sprites[ch], (int(round(sx - minx)) + 1, int(round(sy - miny)) + 1))
    return img
