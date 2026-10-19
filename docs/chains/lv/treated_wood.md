---
kind: chain
id: treated_wood
order: 870
data:
  t: "Treated wood: cutter + spout"
  inf: true
  "n":
    - [lg, "Logs (tree farm)", i, "minecraft:oak_log"]
    - [wa, Water 4 mB, f, "minecraft:water_bucket"]
    - [cu, Cutter, m, "gtceu:lv_cutter"]
    - [pl, "6 Planks", x, "minecraft:oak_planks"]
    - [wp, "2 Wood pulp", o, "gtceu:wood_dust"]
    - [cr, Creosote 125 mB, f, "gtceu:creosote_bucket"]
    - [sp, "Belt + Spout", m, "create:spout"]
    - [tw, Treated wood planks, o, "gtceu:treated_wood_planks"]
  e: [[lg, cu], [wa, cu], [cu, pl], [cu, wp, to fertilizer], [pl, sp, brass funnel], [cr, sp], [sp, tw]]
  tips:
    - |-
      The cutter needs a fluid: with water a log takes 20 s, with distilled water 15 s, with lubricant 10 s.
    - |-
      125 mB creosote per plank: one log in the coke oven (250 mB) treats 2 planks.
    - "Keep the wood pulp: it is half of the fertilizer recipe."
  b:
    - ["gtceu:lv_cutter", 1]
    - ["create:belt_connector", 4]
    - ["create:brass_funnel", 2]
    - ["create:spout", 1]
    - ["functionalstorage:oak_1", 3]
    - ["modularrouters:modular_router", 1]
  how:
    - i: ["modularrouters:modular_router", "gtceu:lv_cutter"]
      t: |-
        A Modular Router sends logs from the tree farm drawer into an LV Cutter with a little water piped in: 1 log → 6 planks + 2 wood pulp (20 s, 7 EU/t).
    - i: ["create:brass_funnel", "create:belt_connector"]
      t: Output drawer → Brass Funnel filtered to planks → a Create belt, a few planks at a time.
    - i: ["create:spout", "gtceu:creosote_bucket"]
      t: A Spout over the belt, fed creosote from the coke ovens, fills each plank (125 mB) into a treated wood plank. The belt needs rotation from the steam engine line.
    - i: ["gtceu:treated_wood_planks", "functionalstorage:oak_1"]
      t: A funnel at the end stores them in a drawer. Treated planks become rods, frames and casings for the sieves, Large Farm and Large Barrel.
  s3d:
    b:
      - ["functionalstorage:oak_1", 0, 0, 0, 1, 1, 1, "Log drawer (tree farm)"]
      - ["modularrouters:modular_router", 2, 0, 0, 1, 1, 1, "Modular Router (logs → cutter)"]
      - ["gtceu:lv_cutter", 4, 0, 0, 1, 1, 1, "LV Cutter · 7 EU/t"]
      - ["thermal:device_water_gen", 4, 0, -3, 1, 1, 1, Aqueous Accumulator]
      - ["functionalstorage:oak_1", 4, 0, 3, 1, 1, 1, Wood pulp drawer]
      - ["functionalstorage:oak_1", 7, 0, 0, 1, 1, 1, Planks drawer]
      - ["create:brass_funnel", 8, 0, 0, 1, 1, 1, "Brass Funnel (filter: planks)"]
      - ["create:belt_connector", 9, 0, 0, 6, 1, 1, Create belt]
      - ["create:spout", 11, 1, 0, 1, 1, 1, "Spout (125 mB creosote per plank)"]
      - ["create:fluid_tank", 11, 2, 0, 1, 1, 1, Creosote tank]
      - ["create:shaft", 9, 0, 1, 1, 1, 3, "Shaft (belt rotation)"]
      - ["create:brass_funnel", 15, 0, 0, 1, 1, 1, "Brass Funnel (treated planks)"]
      - ["functionalstorage:oak_1", 16, 0, 0, 1, 1, 1, Treated planks drawer]
    p:
      - [i, [1, 0.5, 0.5], [2, 0.5, 0.5]]
      - [i, [3, 0.5, 0.5], [4, 0.5, 0.5]]
      - [i, [5, 0.5, 0.5], [7, 0.5, 0.5]]
      - [i, [4.5, 0.5, 1], [4.5, 0.5, 3]]
      - [f, [4.5, 0.5, -2], [4.5, 0.5, 0]]
      - [f, [11.5, 3, 0.5], [11.5, 4.4, 0.5], [11.5, 4.4, -4]]
      - [r, [9.5, 0.5, 4], [9.5, 0.5, 6.5]]
    l:
      - ["Log drawer · tree farm", 0.5, 1.9, 0.5]
      - [Modular Router, 2, 4.9, 0.5]
      - ["LV Cutter · 1 log → 6 planks + 2 pulp · 20 s", 4.5, 3.3, 0.5]
      - [Water 4 mB per log, 4.5, 1.9, -3.5]
      - ["2 wood pulp → fertilizer", 4.5, 1.9, 3.5]
      - [Planks drawer, 7.5, 1.9, 0.5]
      - ["Brass funnel → belt", 8.5, 3.4, 0.5]
      - ["Spout · 125 mB creosote per plank", 11.5, 4.9, 0.5]
      - [Creosote from the coke ovens, 11.5, 6.5, -4]
      - [Rotation from the steam engine line, 9.5, 1.9, 6.5]
      - ["Brass funnel → drawer", 15.5, 3.4, 0.5]
      - ["Treated planks · 18/min", 16.5, 1.9, 0.5]
---
# Treated wood: cutter + spout

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `treated_wood` · **Tags:** Infinite source, 3D scene

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Treated wood](../../plan/p3.md#treated)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-cu">
<div class="gt-head"><span class="gt-mname">Cutter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Logs (tree farm) (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs (tree farm)</span></span><span class="gt-slot gt-fluid" title="Water 4 mB (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><span class="gt-note">Water 4 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="6 Planks (minecraft:oak_planks)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_planks.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Planks</span><span class="gt-note">6 Planks</span></span><span class="gt-slot gt-outp" title="2 Wood pulp (gtceu:wood_dust) - to fertilizer"><img class="gt-ico" src="../../assets/icons/gtceu__wood_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Dust</span><span class="gt-note">2 Wood pulp</span><b class="gt-q">to fertilizer</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_cutter</code></div>
</div>
<div class="gt-panel t-mod" id="m-sp">
<div class="gt-head"><span class="gt-mname">Belt + Spout</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 Planks (minecraft:oak_planks) - brass funnel"><img class="gt-ico" src="../../assets/icons/minecraft__oak_planks.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Planks</span><span class="gt-note">6 Planks</span><b class="gt-q">brass funnel</b></span><span class="gt-slot gt-fluid" title="Creosote 125 mB (gtceu:creosote_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__creosote_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Creosote</span><span class="gt-note">Creosote 125 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__spout.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Treated wood planks (gtceu:treated_wood_planks)"><img class="gt-ico" src="../../assets/icons/gtceu__treated_wood_planks.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Treated Wood Planks</span></span></div>
</div>
<div class="gt-foot"><code>create:spout</code></div>
</div>
</div>

## Flow

- [Cutter](#m-cu) → [Belt + Spout](#m-sp)

## How to build

1. A Modular Router sends logs from the tree farm drawer into an LV Cutter with a little water piped in: 1 log → 6 planks + 2 wood pulp (20 s, 7 EU/t). — `modularrouters:modular_router`, `gtceu:lv_cutter`
2. Output drawer → Brass Funnel filtered to planks → a Create belt, a few planks at a time. — `create:brass_funnel`, `create:belt_connector`
3. A Spout over the belt, fed creosote from the coke ovens, fills each plank (125 mB) into a treated wood plank. The belt needs rotation from the steam engine line. — `create:spout`, `gtceu:creosote_bucket`
4. A funnel at the end stores them in a drawer. Treated planks become rods, frames and casings for the sieves, Large Farm and Large Barrel. — `gtceu:treated_wood_planks`, `functionalstorage:oak_1`

## Tips

- The cutter needs a fluid: with water a log takes 20 s, with distilled water 15 s, with lubricant 10 s.
- 125 mB creosote per plank: one log in the coke oven (250 mB) treats 2 planks.
- Keep the wood pulp: it is half of the fertilizer recipe.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_cutter` | 1 |
| `create:belt_connector` | 4 |
| `create:brass_funnel` | 2 |
| `create:spout` | 1 |
| `functionalstorage:oak_1` | 3 |
| `modularrouters:modular_router` | 1 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](../steam/tree_farm.md)
- **Feeds:** [Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff](../hv/oil_pyro.md), [Fertilizer (for the rubber extractor and greenhouses)](fertilizer.md), [Phenolic printed circuit board (silver foil + etching)](../mv/mv_board.md)
- **Main source for:** `gtceu:wood_dust`, `gtceu:treated_wood_planks`

## Extras

- 3D assembly scene with 13 blocks (open it in the Atlas page).
