"""MkDocs hooks for the Star Technology Atlas wiki (no extra pip packages).

1. on_config: builds the navigation from docs/ when mkdocs.yml has no explicit `nav`.
   The 277 generated pages are never listed by hand: titles come from each page's first
   Markdown heading and the order from the `order:` line of its front matter.
   To pin a custom nav, add a `nav:` key to mkdocs.yml and this hook steps aside.
2. on_page_content: finishes the optional icons of the machine panels (docs/assets/icons).
   tools/refresh_body.js writes <img class="gt-ico" src="../../assets/icons/<ns>__<path>.png">
   (a path that works when the Markdown is read on GitHub). Here the path is made relative to the
   built page, and the <img> is dropped when the PNG is not in docs/assets/icons, so a repo without
   icons makes no failing requests.
"""
import html
import os
import re

GROUPS = [  # (folder under docs/chains, nav label)
    ("stone", "Stone age"), ("steam", "Steam"), ("lv", "LV"), ("mv", "MV"), ("hv", "HV"), ("ev", "EV"),
    ("iv", "IV"), ("luv", "LuV"), ("zpm", "ZPM"), ("uv", "UV"), ("uhv", "UHV"), ("uev", "UEV"),
    ("uiv", "UIV"), ("power", "Power grids"), ("feeders", "Feeders"),
]
COMBOS = "combos"  # chain folder shown under the "Combos" section instead of "Chains"

_ORDER = re.compile(r"^order:\s*(-?\d+(?:\.\d+)?)\s*$", re.M)
_H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)
_IMG = re.compile(r'<img class="gt-ico" src="[^"]*?([^"/]+\.png)"[^>]*>')

_icons = set()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _page_info(docs, rel):
    """Return (order, title) for a docs-relative path."""
    text = _read(os.path.join(docs, rel)).replace("\r\n", "\n")
    head = ""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 3)
        head, text = text[:end], text[end + 5:]
    m = _ORDER.search(head)
    order = float(m.group(1)) if m else 0.0
    m = _H1.search(text)
    title = m.group(1) if m else os.path.splitext(os.path.basename(rel))[0]
    title = html.unescape(re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~])", r"\1", title))
    return order, title


def _pages(docs, folder):
    """Sorted [(title, rel_path)] of the .md files directly inside docs/<folder>."""
    base = os.path.join(docs, folder)
    out = []
    for name in os.listdir(base) if os.path.isdir(base) else []:
        if name.endswith(".md") and name != "index.md":
            rel = folder + "/" + name
            order, title = _page_info(docs, rel)
            out.append((order, name, title, rel))
    out.sort()
    return [(t, r) for _, _, t, r in out]


def _entries(pairs):
    return [{t: r} for t, r in pairs]


def build_nav(docs):
    used = set()

    def take(rel):
        used.add(rel)
        return rel

    nav = [{"Home": take("index.md")}]
    if os.path.exists(os.path.join(docs, "route.md")):
        nav.append({"Route": take("route.md")})

    plan = []
    for t, r in _pages(docs, "plan"):
        n = re.search(r"p(\d+)\.md$", r)
        plan.append({("%s. %s" % (n.group(1), t) if n else t): take(r)})
    nav.append({"Plan": plan})

    eras = []
    for t, r in _pages(docs, "eras"):
        eras.append({re.split(r"\s+[\u2014\u00b7]\s+", t)[0]: take(r)})
    nav.append({"Eras": eras})

    chains = [{"All chains": take("chains/index.md")}]
    known = [g for g, _ in GROUPS]
    folders = sorted(d for d in os.listdir(os.path.join(docs, "chains"))
                     if os.path.isdir(os.path.join(docs, "chains", d)))
    labels = dict(GROUPS)
    for g in known + [d for d in folders if d not in known and d != COMBOS]:
        if g not in folders:
            continue
        pages = _pages(docs, "chains/" + g)
        if pages:
            chains.append({labels.get(g, g.title()): [{t: take(r)} for t, r in pages]})
    nav.append({"Chains": chains})

    combos = [{"Overview": take("combos/index.md")}]
    combos += [{t: take(r)} for t, r in _pages(docs, "chains/" + COMBOS)]
    nav.append({"Combos": combos})

    nav.append({"Resources": take("resources.md")})
    nav.append({"Farms": take("farms.md")})
    ref = [{"Tiers and mechanics": take("reference.md")}]
    if os.path.exists(os.path.join(docs, "tools.md")):
        ref.append({"Calculators and planners": take("tools.md")})
    nav.append({"Reference": ref})
    nav.append({"Contributing": take("CONTRIBUTING-CONTENT.md")})

    # Any page added later and not listed above still gets a place.
    extra = []
    for root, dirs, files in os.walk(docs):
        dirs[:] = sorted(d for d in dirs if d not in ("_data", "assets", "stylesheets", "javascripts", "overrides"))
        for name in sorted(files):
            if name.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, name), docs).replace(os.sep, "/")
                if rel not in used:
                    extra.append({_page_info(docs, rel)[1]: rel})
    if extra:
        nav.append({"More": extra})
    return nav


def on_config(config, **kwargs):
    docs = config["docs_dir"]
    icons = os.path.join(docs, "assets", "icons")
    _icons.clear()
    if os.path.isdir(icons):
        _icons.update(f for f in os.listdir(icons) if f.lower().endswith(".png"))
    if not config.get("nav"):
        config["nav"] = build_nav(docs)
    return config


def on_page_content(content, page, config, files):
    if 'class="gt-ico"' not in content:
        return content
    prefix = "../" * page.url.count("/") + "assets/icons/"

    def fix(m):
        name = m.group(1)
        if name not in _icons:
            return ""
        return m.group(0).replace(re.search(r'src="([^"]*)"', m.group(0)).group(1), prefix + name, 1)

    return _IMG.sub(fix, content)
