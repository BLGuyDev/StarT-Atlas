---
kind: chain
id: charcoal_fan
order: 600
data:
  t: "Charcoal: Create fan smelting"
  inf: true
  "n":
    - [lg, "Logs (tree farm)", s, "minecraft:oak_log"]
    - [bl, Mechanical Belt, m, "create:belt_connector"]
    - [fn, Encased Fan, m, "create:encased_fan"]
    - [lv, Lava block in front, i, "minecraft:lava_bucket"]
    - [ch, Charcoal, o, "minecraft:charcoal"]
    - [dr, Drawer, o, "functionalstorage:oak_1"]
  e: [[lg, bl], [bl, fn, items pass], [lv, fn, bulk blasting], [fn, ch], [ch, dr, funnel]]
  tips:
    - |-
      Fan blows through lava onto the belt: logs smelt into charcoal on the move, a stack at a time.
    - Only rotation needed (windmill). No creosote.
    - Needs only rotation (your steam engines already make plenty) and a lava block. 1 log → 1 charcoal = 80 s of burner fuel.
  b:
    - ["create:encased_fan", 1]
    - ["create:belt_connector", 4]
    - ["create:shaft", 4]
    - ["create:andesite_funnel", 2]
    - ["minecraft:lava_bucket", 1]
    - ["functionalstorage:oak_1", 1]
  how:
    - i: ["functionalstorage:oak_1", "create:andesite_funnel"]
      t: An Andesite Funnel takes logs from the tree-farm drawer onto a Mechanical Belt.
    - i: ["create:encased_fan", "minecraft:lava_bucket"]
      t: An Encased Fan blows across the belt through a lava source block (lava in front of the fan = bulk blasting). Logs on that stretch smelt into charcoal.
    - i: ["create:belt_connector"]
      t: Belts are made from rubber plates in this pack (3 plates → 3 belts). A 4–6 block belt is plenty.
    - i: ["create:andesite_funnel", "functionalstorage:oak_1"]
      t: A funnel at the end of the belt puts the charcoal into a drawer. A faster fan has a longer reach and processes more at once.
---
# Charcoal: Create fan smelting

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `charcoal_fan` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Charcoal and creosote](../../plan/p1.md#fuel)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-bl">
<div class="gt-head"><span class="gt-mname">Mechanical Belt</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Logs (tree farm) (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs (tree farm)</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__belt_connector.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-fn" title="Encased Fan (create:encased_fan) - items pass"><img class="gt-ico" src="../../assets/icons/create__encased_fan.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Encased Fan</span><b class="gt-q">items pass</b></a></div>
</div>
<div class="gt-foot"><code>create:belt_connector</code></div>
</div>
<div class="gt-panel t-mod" id="m-fn">
<div class="gt-head"><span class="gt-mname">Encased Fan</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-bl" title="Mechanical Belt (create:belt_connector) - items pass"><img class="gt-ico" src="../../assets/icons/create__belt_connector.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Belt Connector</span><span class="gt-note">Mechanical Belt</span><b class="gt-q">items pass</b></a><span class="gt-slot" title="Lava block in front (minecraft:lava_bucket) - bulk blasting"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><span class="gt-note">Lava block in front</span><b class="gt-q">bulk blasting</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__encased_fan.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span></div>
</div>
<div class="gt-foot"><code>create:encased_fan</code></div>
</div>
</div>

## Flow

- [Mechanical Belt](#m-bl) → [Encased Fan](#m-fn)

### Direct steps

- Charcoal → Drawer (funnel)

## How to build

1. An Andesite Funnel takes logs from the tree-farm drawer onto a Mechanical Belt. — `functionalstorage:oak_1`, `create:andesite_funnel`
2. An Encased Fan blows across the belt through a lava source block (lava in front of the fan = bulk blasting). Logs on that stretch smelt into charcoal. — `create:encased_fan`, `minecraft:lava_bucket`
3. Belts are made from rubber plates in this pack (3 plates → 3 belts). A 4–6 block belt is plenty. — `create:belt_connector`
4. A funnel at the end of the belt puts the charcoal into a drawer. A faster fan has a longer reach and processes more at once. — `create:andesite_funnel`, `functionalstorage:oak_1`

## Tips

- Fan blows through lava onto the belt: logs smelt into charcoal on the move, a stack at a time.
- Only rotation needed (windmill). No creosote.
- Needs only rotation (your steam engines already make plenty) and a lava block. 1 log → 1 charcoal = 80 s of burner fuel.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:encased_fan` | 1 |
| `create:belt_connector` | 4 |
| `create:shaft` | 4 |
| `create:andesite_funnel` | 2 |
| `minecraft:lava_bucket` | 1 |
| `functionalstorage:oak_1` | 1 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](tree_farm.md), [Infinite lava, obsidian &amp; pebbles](../stone/inf_lava.md)
