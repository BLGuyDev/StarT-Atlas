"""Real block-model renderer (inventory/GUI view) on top of icons.py: elements, UVs, face rotation, GUI transform."""
import json, re, functools
import numpy as np
from PIL import Image
import icons
from icons import tex, model, read, rl, comp, faces_from, KJS_MODEL, kjs_tex, fluid_icon, gt_material_item


def _full_model(name, kind="item"):
    texs, chain, cur, elements, gui = {}, [], name, None, None
    for _ in range(14):
        m = model(cur, kind)
        if m is None:
            break
        if "variants" in m and m.get("loader") == "gtceu:machine":
            v = list(m["variants"].values())[0]
            v = v[0] if isinstance(v, list) else v
            mm = v.get("model", {}) if isinstance(v, dict) else {}
            if isinstance(mm, str):
                mm = {"parent": mm}
            m = dict(mm)
        for k, t in (m.get("textures") or {}).items():
            texs.setdefault(k, t)
        if elements is None and m.get("elements"):
            elements = m["elements"]
        if gui is None and isinstance(m.get("display"), dict) and "gui" in m["display"]:
            gui = m["display"]["gui"]
        par = m.get("parent")
        if not par:
            break
        chain.append(par)
        cur = par
        kind = "block"
    return texs, elements, gui, chain


def _res_tex(texs, ref):
    n = 0
    while isinstance(ref, str) and ref.startswith("#") and n < 8:
        ref = texs.get(ref[1:])
        n += 1
    if not isinstance(ref, str) or ref.startswith("#") or "void" in ref or "missing" in ref:
        return None
    return tex(ref)


def _rot(axis, deg):
    a = np.radians(deg)
    c, s = np.cos(a), np.sin(a)
    if axis == "x":
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    if axis == "y":
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


FACE_SHADE = {"up": 1.0, "down": 0.5, "north": 0.8, "south": 0.8, "east": 0.6, "west": 0.6}


def _face_quad(f, t, d):
    x1, y1, z1 = f
    x2, y2, z2 = t
    if d == "north":
        return [(x2, y2, z1), (x1, y2, z1), (x1, y1, z1), (x2, y1, z1)], (16 - x2, 16 - y2, 16 - x1, 16 - y1)
    if d == "south":
        return [(x1, y2, z2), (x2, y2, z2), (x2, y1, z2), (x1, y1, z2)], (x1, 16 - y2, x2, 16 - y1)
    if d == "west":
        return [(x1, y2, z1), (x1, y2, z2), (x1, y1, z2), (x1, y1, z1)], (z1, 16 - y2, z2, 16 - y1)
    if d == "east":
        return [(x2, y2, z2), (x2, y2, z1), (x2, y1, z1), (x2, y1, z2)], (16 - z2, 16 - y2, 16 - z1, 16 - y1)
    if d == "up":
        return [(x1, y2, z1), (x2, y2, z1), (x2, y2, z2), (x1, y2, z2)], (x1, z1, x2, z2)
    return [(x1, y1, z2), (x2, y1, z2), (x2, y1, z1), (x1, y1, z1)], (x1, 16 - z2, x2, 16 - z1)


def render_elements(texs, elements, gui=None, size=64, face_tex=None):
    rot = (gui or {}).get("rotation", [30, 225, 0])
    scl = (gui or {}).get("scale", [0.625, 0.625, 0.625])
    trn = (gui or {}).get("translation", [0, 0, 0])
    R = _rot("x", rot[0]) @ _rot("y", rot[1]) @ _rot("z", rot[2])
    img = np.zeros((size, size, 4), np.float32)
    zbuf = np.full((size, size), -1e9, np.float32)
    k = size / 16.0
    for el in elements:
        f, t = el.get("from"), el.get("to")
        if not f or not t:
            continue
        er = el.get("rotation")
        for d, fc in (el.get("faces") or {}).items():
            timg = face_tex.get(d) if face_tex is not None else _res_tex(texs, fc.get("texture"))
            if timg is None:
                continue
            ta = np.asarray(timg.convert("RGBA")).astype(np.float32)
            th, tw = ta.shape[:2]
            quad, duv = _face_quad(f, t, d)
            u1, v1, u2, v2 = fc.get("uv") or duv
            uvs = [(u1, v1), (u2, v1), (u2, v2), (u1, v2)]
            r = int(fc.get("rotation", 0)) // 90 % 4
            uvs = uvs[r:] + uvs[:r]
            P = np.array(quad, np.float64)
            if er:
                o = np.array(er.get("origin", [8, 8, 8]), np.float64)
                P = (P - o) @ _rot(er.get("axis", "y"), float(er.get("angle", 0))).T + o
            P = (P - 8.0) * np.array(scl) + np.array(trn)
            P = P @ R.T
            sx = size / 2 + P[:, 0] * k
            sy = size / 2 - P[:, 1] * k
            sz = P[:, 2]
            shade = FACE_SHADE.get(d, 0.8) if el.get("shade", True) else 1.0
            tint = None
            if "tintindex" in fc and any(w in str(fc.get("texture")) + str(texs.get("top", "")) + str(texs.get("all", "")) for w in ("grass", "leaves", "vine", "top")):
                if any(w in str(texs) for w in ("grass_block", "leaves", "vine")):
                    tint = np.array([0x7F / 255, 0xB2 / 255, 0x38 / 255])
            for tri in ((0, 1, 2), (0, 2, 3)):
                xs, ys, zs = sx[list(tri)], sy[list(tri)], sz[list(tri)]
                us = np.array([uvs[i][0] for i in tri]); vs = np.array([uvs[i][1] for i in tri])
                x0, x1_ = int(max(0, np.floor(xs.min()))), int(min(size - 1, np.ceil(xs.max())))
                y0, y1_ = int(max(0, np.floor(ys.min()))), int(min(size - 1, np.ceil(ys.max())))
                if x1_ < x0 or y1_ < y0:
                    continue
                den = (ys[1] - ys[2]) * (xs[0] - xs[2]) + (xs[2] - xs[1]) * (ys[0] - ys[2])
                if abs(den) < 1e-6:
                    continue
                gy, gx = np.mgrid[y0:y1_ + 1, x0:x1_ + 1].astype(np.float64) + 0.5
                a = ((ys[1] - ys[2]) * (gx - xs[2]) + (xs[2] - xs[1]) * (gy - ys[2])) / den
                b = ((ys[2] - ys[0]) * (gx - xs[2]) + (xs[0] - xs[2]) * (gy - ys[2])) / den
                c = 1 - a - b
                inside = (a >= -1e-4) & (b >= -1e-4) & (c >= -1e-4)
                if not inside.any():
                    continue
                uu = a * us[0] + b * us[1] + c * us[2]
                vv = a * vs[0] + b * vs[1] + c * vs[2]
                zz = a * zs[0] + b * zs[1] + c * zs[2]
                ti = np.clip((uu / 16.0 * tw).astype(int), 0, tw - 1)
                tj = np.clip((vv / 16.0 * th).astype(int), 0, th - 1)
                px = ta[tj, ti]
                zsub = zbuf[y0:y1_ + 1, x0:x1_ + 1]
                ok = inside & (px[..., 3] > 16) & (zz >= zsub - 1e-3)
                if not ok.any():
                    continue
                col = px[..., :3] * shade
                if tint is not None:
                    col = col * tint
                sub = img[y0:y1_ + 1, x0:x1_ + 1]
                sub[ok, :3] = col[ok]
                sub[ok, 3] = 255
                zsub[ok] = zz[ok]
    if img[..., 3].max() == 0:
        return None
    return Image.fromarray(img.clip(0, 255).astype(np.uint8), "RGBA")


FULL = [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": {d: {} for d in ("north", "south", "east", "west", "up", "down")}}]


def cube_faces(faces, size=64):
    return render_elements({}, FULL, None, size, face_tex=faces)


def kjs_machine_icon(path, size=64):
    cas, ovf = KJS_MODEL[path]
    C = tex(cas)
    ov = lambda n: tex(f"{ovf}/{n}")
    side = comp(C, ov("overlay_side"))
    back = comp(C, ov("overlay_back")) if ov("overlay_back") is not None else side
    return cube_faces({"north": comp(C, ov("overlay_front")), "south": back, "east": side, "west": side,
                       "up": comp(C, ov("overlay_top")), "down": C}, size)


def up64(im):
    return im.resize((64, 64), Image.NEAREST) if im is not None else None


# ids produced by the data pipeline (Java constant names -> snake case) that differ from the real registry ids.
# Used only to pick the right icon; build_assets prints every alias hit so the source data can be fixed.
ID_ALIAS = {
    "gtceu:steam_hatch": "gtceu:steam_input_hatch",
    "gtceu:passthrough_hatch_item": "gtceu:lv_item_passthrough_hatch",
    "gtceu:computation_data_reception_hatch": "gtceu:computation_receiver_hatch",
    "gtceu:fluid_export_hatch": "gtceu:lv_output_hatch",
    "gtceu:cover_screen": "gtceu:computer_monitor_cover",
    "gtceu:wooden_drum": "gtceu:wood_drum",
    "gtceu:iron_axe": "minecraft:iron_axe",
    "gtceu:power_integrated_circuit": "gtceu:mpic_chip",
    "gtceu:high_power_integrated_circuit": "gtceu:hpic_chip",
    "gtceu:steel_magnetic_rod": "gtceu:magnetic_steel_rod",
    "gtceu:hermetic_casing_lv": "gtceu:lv_hermetic_casing",
    "gtceu:hermetic_casing_mv": "gtceu:mv_hermetic_casing",
    "gtceu:machine_casing_uhv": "gtceu:uhv_machine_casing",
    "gtceu:machine_casing_uv": "gtceu:uv_machine_casing",
    "gtceu:machine_casing_zpm": "gtceu:zpm_machine_casing",
    "kubejs:mesh_block": "kubejs:meshblock",
}
ALIAS_HITS = {}


def canon(item_id):
    a = ID_ALIAS.get(item_id)
    if a is None:
        ns, _, p = item_id.partition(":")
        q = re.sub(r"(?<![a-z0-9])((?:[a-z]_){1,}[a-z])(?![a-z0-9])", lambda mm: mm.group(1).replace("_", ""), p) if ns == "gtceu" else p
        a = f"{ns}:{q}" if q != p else None
    if a:
        ALIAS_HITS[item_id] = a
    return a or item_id


@functools.lru_cache(maxsize=None)
def icon64(item_id):
    if not item_id or item_id.startswith("#"):
        return None
    item_id = canon(item_id)
    ns, path = rl(item_id)
    if path == "normal_optical_pipe":
        s, i_ = tex("gtceu:block/pipe/pipe_optical_side"), tex("gtceu:block/pipe/pipe_optical_in")
        if s is not None:
            return cube_faces({"north": i_ or s, "south": i_ or s, "east": s, "west": s, "up": s, "down": s})
    if path.endswith("_bucket") and path != "wooden_bucket":
        f = fluid_icon(item_id)
        if f is not None:
            return f.resize((64, 64), Image.NEAREST)
    has_item_model = model(f"{ns}:item/{path}", "item") is not None
    if ns == "gtceu" and not has_item_model:
        g = gt_material_item(path)
        if g is not None:
            return g.resize((64, 64), Image.NEAREST)
    if ns in ("gtceu", "start_core") and not has_item_model and path in KJS_MODEL:
        return kjs_machine_icon(path)
    if ns == "kubejs" and not has_item_model and read(f"kubejs/blockstates/{path}.json") is None:
        ref, layers = kjs_tex(path)
        tt = tex(ref) if ref else None
        if tt is None or (ref and "/item/" not in ref):
            ls = [tex(x) for x in layers]
            if any(x is not None for x in ls):
                return up64(comp(*ls))
        if tt is not None:
            if "/item/" in ref or ":item/" in ref:
                return up64(tt)
            return cube_faces({d: tt for d in ("north", "south", "east", "west", "up", "down")})
    cands = []
    if has_item_model:
        cands.append((f"{ns}:item/{path}", "item"))
    bs = read(f"{ns}/blockstates/{path}.json")
    if bs:
        try:
            j = json.loads(bs)
            v = list(j["variants"].values())[0] if "variants" in j else j["multipart"][0]["apply"]
            v = v[0] if isinstance(v, list) else v
            cands.append((v["model"], "block"))
        except Exception:
            pass
    if ns == "gtceu":
        cands.append((f"gtceu:block/machine/{path}", "block"))
    for name_, kind in cands:
        texs, elements, gui, chain = _full_model(name_, kind)
        if not texs and not elements:
            continue
        flat = any(c.split(":")[-1] in ("item/generated", "item/handheld", "builtin/generated", "item/handheld_rod") for c in chain) or (not elements and "layer0" in texs)
        if flat and "layer0" in texs:
            layers = [_res_tex(texs, texs[k]) for k in sorted(texs) if re.fullmatch(r"layer\d", k)]
            c = comp(*[l for l in layers if l is not None])
            if c is not None:
                return up64(c)
        if elements:
            im = render_elements(texs, elements, gui)
            if im is not None:
                return im
        T, F, Sd = faces_from(texs)
        if T is not None or F is not None:
            return cube_faces({"north": F or T, "south": Sd or T, "east": Sd or T, "west": Sd or T, "up": T or F, "down": T or F})
    if path in KJS_MODEL:
        return kjs_machine_icon(path)
    old = icons.icon(item_id)
    return old.resize((64, 64), Image.NEAREST) if old is not None else None
