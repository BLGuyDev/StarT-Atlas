---
kind: chain
id: cobble_drill
order: 650
data:
  t: "Cobble: Create drill generator"
  inf: true
  "n":
    - [lv, Lava source, i, "minecraft:lava_bucket"]
    - [w, Water source, i, "minecraft:water_bucket"]
    - [cg, Cobble forms, x, "minecraft:cobblestone"]
    - [dr, Mechanical Drill, m, "create:mechanical_drill"]
    - [wm, Windmill, p, "create:windmill_bearing"]
    - [c, Cobblestone, o, "minecraft:cobblestone"]
  e: [[lv, cg], [w, cg], [cg, dr], [wm, dr, SU], [dr, c, chute]]
  tips: ["Vanilla cobble generator; the drill mines it as it forms. Faster with more RPM."]
  b:
    - ["create:mechanical_drill", 1]
    - ["create:shaft", 2]
    - ["create:chute", 1]
    - ["minecraft:lava_bucket", 1]
    - ["minecraft:water_bucket", 1]
  how:
    - i: ["minecraft:lava_bucket", "minecraft:water_bucket"]
      t: |-
        Vanilla cobble generator: lava flows into a channel where water meets it, forming cobble in one spot.
    - i: ["create:mechanical_drill"]
      t: A Mechanical Drill facing that spot mines the cobble as soon as it forms.
    - i: ["create:chute", "functionalstorage:oak_1"]
      t: Drops fall into a chute → drawer. Drill stress 4 SU/RPM; faster RPM = faster mining.
---
# Cobble: Create drill generator

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `cobble_drill` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-dr">
<div class="gt-head"><span class="gt-mname">Mechanical Drill</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cobble forms (minecraft:cobblestone)"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><span class="gt-note">Cobble forms</span></span><a class="gt-slot gt-power" href="#m-wm" title="Windmill (create:windmill_bearing) - SU"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Windmill Bearing</span><b class="gt-q">SU</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_drill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Cobblestone (minecraft:cobblestone) - chute"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><b class="gt-q">chute</b></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_drill</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dr" title="Mechanical Drill (create:mechanical_drill) - SU"><img class="gt-ico" src="../../assets/icons/create__mechanical_drill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Drill</span><b class="gt-q">SU</b></a></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
</div>

## Flow

- [Windmill](#m-wm) → [Mechanical Drill](#m-dr)

### Direct steps

- Lava source → Cobble forms
- Water source → Cobble forms

## How to build

1. Vanilla cobble generator: lava flows into a channel where water meets it, forming cobble in one spot. — `minecraft:lava_bucket`, `minecraft:water_bucket`
2. A Mechanical Drill facing that spot mines the cobble as soon as it forms. — `create:mechanical_drill`
3. Drops fall into a chute → drawer. Drill stress 4 SU/RPM; faster RPM = faster mining. — `create:chute`, `functionalstorage:oak_1`

## Tips

- Vanilla cobble generator; the drill mines it as it forms. Faster with more RPM.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:mechanical_drill` | 1 |
| `create:shaft` | 2 |
| `create:chute` | 1 |
| `minecraft:lava_bucket` | 1 |
| `minecraft:water_bucket` | 1 |

## Needs / Feeds

- **Needs:** [Infinite lava, obsidian &amp; pebbles](../stone/inf_lava.md), [Infinite water](../stone/inf_water.md)
