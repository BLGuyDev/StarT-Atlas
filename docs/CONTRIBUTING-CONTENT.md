# Contributing content to the Atlas wiki

The `docs/` folder is the **source of truth** for the guide data shown by `guia/index.html`.
The page no longer loads hand-written `guide*.js` files; it loads `guia/data/wiki-data.js`,
which is generated from `docs/` by `tools/build_data.js`.

## How a page is built

Every data page has two parts:

1. **YAML front matter** between the first two `---` lines. This is the editable truth. It holds
   the complete object exactly as the page code reads it (`window.GUIDE`): nothing is dropped.
2. **A Markdown body** below it (title, tags, flow table, numbered steps, tips, bill of materials,
   Needs / Feeds links...). The body is **generated** from the front matter and is overwritten by
   `node tools/refresh_body.js`. Do not edit it by hand: change the front matter and refresh.

Front matter is standard YAML, so MkDocs (Material) and other renderers read it as page metadata
and do not show it.

| Path | Front matter | Becomes |
| --- | --- | --- |
| `docs/eras/<era>.md` | `kind: era`, `id`, `order`, `data` (the era object) | `GUIDE.eras[]`, sorted by `order` |
| `docs/chains/<group>/<chain_id>.md` | `kind: chain`, `id`, `order`, `data` (the chain object: `t`, `n` nodes, `e` edges, `b` BOM, `how`, `tips`, `store`, `s3d`, ...) | `GUIDE.chains[id]`, in `order` |
| `docs/plan/<phase>.md` | `kind: phase`, `id`, `order`, `data` (the phase), `modules` (list of plan modules, in order) | `GUIDE.phases[]` and `GUIDE.plan[]` (phases by `order`, modules in list order) |
| `docs/_data/meta.yml` | `pack`, `flagship`, `key_order` (key order of `window.GUIDE`) | top-level scalars |
| `docs/_data/<name>.yml` | `value:` holding `GUIDE.<name>` | `tiers`, `mechanics`, `legend`, `resources`, `src`, `once`, `options`, `route` |
| `docs/index.md`, `chains/index.md`, `resources.md`, `farms.md`, `route.md`, `reference.md`, `combos/index.md` | `kind: view` | nothing (overview pages, body generated) |

`GUIDE.optOf` is not stored: `wiki-data.js` rebuilds it from `options` at load time.
The chain folder (`steam`, `lv`, `power`, `combos`, `feeders`...) is only for browsing; the build
reads every page, so moving a file between folders changes nothing in the data.

## Rules

- **Ids are stable.** Chain ids, era ids, phase ids and plan module ids are keys used by the page
  (plan module ids are the Done-checkbox keys `plan:<id>` saved in players' browsers). Never rename
  or delete a module id; move it to another phase page instead (and update its `ph`).
- File names are the lowercase id, no spaces: `docs/chains/<group>/<chain_id>.md`.
- `order` is a number; pages are sorted by it (gaps of 10 leave room to insert).
- Mark facts you could not confirm by starting the text with `Unverified:`; confirmed ones may start
  with `Verified:`. The body shows them as tags.
- YAML tips: quote strings that contain `: ` or ` #`, or start with a symbol, digit, `[`, `{`, `'`
  or `"` (or use a `|-` block on the next line). Use `true` / `false`, not `yes` / `no`.
  Comments (`#`), `|`, `|-`, `>`, `>-` blocks and flow lists that wrap over several lines are fine.
  Anchors/aliases (`&`, `*`) are not supported.
- Docs may contain UTF-8 text. `tools/*.js` stay ASCII-only.

## Commands (Node only, no packages)

```sh
node tools/refresh_body.js     # rebuild every Markdown body from its front matter
node tools/build_data.js       # docs/ -> guia/data/wiki-data.js
node tools/build_data.js --check   # exit 1 if wiki-data.js is stale
ORIGINAL_GUIDE_DIR=/path/to/legacy node tools/test_roundtrip.js [--build]
                               # legacy guide*.js vs wiki-data.js, prints ROUNDTRIP OK
ORIGINAL_GUIDE_DIR=/path/to/legacy node tools/export_wiki.js --force
                               # one-time migration legacy guide*.js -> docs/ (overwrites docs/)
```

Typical edit: change the front matter, run `refresh_body.js` and `build_data.js`, open
`guia/index.html` to check, commit both `docs/` and `guia/data/wiki-data.js`.

`test_roundtrip.js` only makes sense against the legacy files (kept outside the repo after the
migration); once content has been edited in `docs/` it will report the first difference, which is expected.

If a future data field ever needs a function (YAML cannot hold code), put it in
`tools/runtime-patches.js`; the round-trip test loads that file after `wiki-data.js` when it exists,
and it must then be added as a `<script>` right after `wiki-data.js` in `guia/index.html`.
