---
kind: chain
id: rubber
order: 720
data:
  t: "Rubber: Large Arboreal Extractor"
  inf: true
  "n":
    - [sc, "Screw (kept)", i, "gtceu:iron_screw"]
    - [fz, "Fertilizer (25 % used)", i, "gtceu:fertilizer"]
    - [ae, Large Arboreal Extractor, m, "start_core:large_arboreal_extractor"]
    - [lx, Latex, f, "thermal:latex_bucket"]
    - [fs, "Fluid Solidifier · ball mold", m, "gtceu:lv_fluid_solidifier"]
    - [rb, Rubber, x, "thermal:rubber"]
    - [s, Sulfur, i, "gtceu:sulfur_dust"]
    - [cr, Chemical Reactor, m, "gtceu:lv_chemical_reactor"]
    - [lr, Liquid Rubber, f, "gtceu:rubber_bucket"]
    - [so, "Fluid Solidifier · plate mold", m, "gtceu:lv_fluid_solidifier"]
    - [rp, Rubber Plates, o, "gtceu:rubber_plate"]
  e:
    - [sc, ae]
    - [fz, ae, optional]
    - [ae, lx, "100-250 mB / 20 s"]
    - [lx, fs, "250 mB"]
    - [fs, rb]
    - [rb, cr, "3"]
    - [s, cr, "1"]
    - [cr, lr, "576 mB"]
    - [lr, so, "144 mB"]
    - [so, rp]
  tips:
    - |-
      No power at all: the extractor is a brick multiblock built around a small jungle tree you place yourself (5 logs, 5 leaves).
    - |-
      Chemical reactor route: 3 rubber + 1 sulfur = 576 mB = 4 plates. The Create mixer + press gives only 3 plates for the same rubber.
    - |-
      Thermal’s small Arboreal Extractor only reads rubberwood trees, and rubberwood saplings are hidden in this pack: it gives nothing here.
    - |-
      Needs fertilizer from the LV fertilizer line (optional: it only raises the yield).
  b:
    - ["start_core:large_arboreal_extractor", 1]
    - ["minecraft:bricks", 10]
    - ["minecraft:brick_slab", 6]
    - ["minecraft:jungle_log", 5]
    - ["minecraft:jungle_leaves", 5]
    - ["minecraft:dirt", 1]
    - ["gtceu:ulv_input_bus", 1]
    - ["gtceu:ulv_output_hatch", 1]
    - ["gtceu:iron_screw", 1]
    - ["gtceu:lv_fluid_solidifier", 2]
    - ["gtceu:lv_chemical_reactor", 1]
  how:
    - i: ["start_core:large_arboreal_extractor", "minecraft:bricks", "minecraft:jungle_log"]
      t: |-
        Large Arboreal Extractor: a 3 × 3 brick base with dirt in the middle, a 5-log jungle trunk on it, jungle leaves on top and brick slabs as the rim. The controller sits in the second brick layer; a ULV input bus and a ULV fluid output hatch replace two base bricks.
    - i: ["gtceu:wood_screw", "gtceu:iron_screw"]
      t: |-
        A screw in the input bus is the tap and is never used up. Wood screw: 100 mB latex every 20 s (300 mB per minute).
    - i: ["minecraft:bone_meal", "thermal:compost", "gtceu:fertilizer"]
      t: |-
        With an iron screw plus fertilizer in the bus, output rises: bone meal 150, compost 200, fertilizer 250 mB per 20 s. Each run uses the fertilizer only 25 % of the time (fertilizer: 0.75 per minute for 750 mB latex).
    - i: ["gtceu:lv_fluid_solidifier", "gtceu:ball_casting_mold"]
      t: |-
        Latex to an LV Fluid Solidifier with a ball mold: 250 mB = 1 rubber in 6 s (8 EU/t). One extractor on fertilizer = 3 rubber per minute; build more extractors side by side to scale.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:sulfur_dust"]
      t: |-
        LV Chemical Reactor: 3 rubber + 1 sulfur dust → 576 mB liquid rubber (12 s). A second solidifier with a plate mold makes 144 mB = 1 rubber plate, so 3 rubber become 4 plates. Liquid rubber also coats cables directly in the assembler.
    - i: ["create:mechanical_mixer", "create:mechanical_press"]
      t: |-
        Before LV: heated Create mixer (3 rubber + sulfur → 3 cured rubber) then a press (cured rubber → rubber plate). Works, but 25 % less rubber per plate.
  s3d:
    b:
      - ["minecraft:bricks", 0, 0, 0, 3, 1, 1, Bricks]
      - ["minecraft:bricks", 0, 0, 2, 3, 1, 1, Bricks]
      - ["gtceu:ulv_input_bus", 0, 0, 1, 1, 1, 1, "ULV Input Bus (iron screw + fertilizer)"]
      - ["minecraft:bricks", 1, 0, 1, 1, 1, 1, Bricks]
      - ["gtceu:ulv_output_hatch", 2, 0, 1, 1, 1, 1, "ULV Output Hatch (latex)"]
      - ["minecraft:bricks", 0, 1, 0, 3, 1, 1, Bricks]
      - ["minecraft:bricks", 0, 1, 1, 1, 1, 1, Bricks]
      - ["minecraft:bricks", 2, 1, 1, 1, 1, 1, Bricks]
      - ["minecraft:bricks", 0, 1, 2, 1, 1, 1, Bricks]
      - ["start_core:large_arboreal_extractor", 1, 1, 2, 1, 1, 1, "Large Arboreal Extractor (controller)"]
      - ["minecraft:bricks", 2, 1, 2, 1, 1, 1, Bricks]
      - ["minecraft:dirt", 1, 1, 1, 1, 1, 1, Dirt]
      - ["minecraft:brick_slab", 0, 2, 0, 1, 1, 3, Brick Slab]
      - ["minecraft:brick_slab", 2, 2, 0, 1, 1, 3, Brick Slab]
      - ["minecraft:jungle_log", 1, 2, 1, 1, 5, 1, "Jungle Log (trunk)"]
      - ["minecraft:jungle_leaves", 0, 5, 0, 3, 2, 1, Jungle Leaves]
      - ["minecraft:jungle_leaves", 0, 5, 2, 3, 2, 1, Jungle Leaves]
      - ["minecraft:jungle_leaves", 0, 5, 1, 1, 2, 1, Jungle Leaves]
      - ["minecraft:jungle_leaves", 2, 5, 1, 1, 2, 1, Jungle Leaves]
      - ["minecraft:jungle_leaves", 0, 7, 0, 3, 1, 3, Jungle Leaves]
      - ["functionalstorage:oak_1", -4, 0, 1, 1, 1, 1, Fertilizer drawer]
      - ["modularrouters:modular_router", -2, 0, 1, 1, 1, 1, Modular Router]
      - ["thermal:fluid_cell", 4, 0, 1, 1, 1, 1, "Latex buffer (fluid cell)"]
      - ["gtceu:lv_fluid_solidifier", 6, 0, 1, 1, 1, 1, "LV Fluid Solidifier · ball mold"]
      - ["functionalstorage:oak_1", 8, 0, 1, 1, 1, 1, Rubber drawer]
      - ["gtceu:lv_chemical_reactor", 10, 0, 1, 1, 1, 1, LV Chemical Reactor]
      - ["functionalstorage:oak_1", 10, 0, 4, 1, 1, 1, Sulfur drawer]
      - ["thermal:fluid_cell", 12, 0, 1, 1, 1, 1, "Liquid rubber buffer (fluid cell)"]
      - ["gtceu:lv_fluid_solidifier", 14, 0, 1, 1, 1, 1, "LV Fluid Solidifier · plate mold"]
      - ["functionalstorage:oak_1", 16, 0, 1, 1, 1, 1, Rubber plates drawer]
    p:
      - [i, [-3, 0.5, 1.5], [-2, 0.5, 1.5]]
      - [i, [-1, 0.5, 1.5], [0, 0.5, 1.5]]
      - [f, [3, 0.5, 1.5], [4, 0.5, 1.5]]
      - [f, [5, 0.5, 1.5], [6, 0.5, 1.5]]
      - [i, [7, 0.5, 1.5], [8, 0.5, 1.5]]
      - [i, [9, 0.5, 1.5], [10, 0.5, 1.5]]
      - [i, [10.5, 0.5, 4], [10.5, 0.5, 2]]
      - [f, [11, 0.5, 1.5], [12, 0.5, 1.5]]
      - [f, [13, 0.5, 1.5], [14, 0.5, 1.5]]
      - [i, [15, 0.5, 1.5], [16, 0.5, 1.5]]
    l:
      - ["Large Arboreal Extractor · no power", 1.5, 9.2, 1.5]
      - ["Iron screw (kept) + fertilizer: 250 mB / 20 s", 1.5, 10.9, 1.5]
      - ["Fertilizer · optional (25 % used)", -3.5, 1.9, 1.5]
      - [Router, -1.5, 3.4, 1.5]
      - ["Latex 750 mB/min", 4.5, 1.9, 1.5]
      - ["250 mB → 1 rubber · 6 s", 6.5, 3.6, 1.5]
      - ["Rubber · 3/min", 8.5, 1.9, 1.5]
      - ["3 rubber + 1 sulfur → 576 mB", 10.5, 5.4, 1.5]
      - [Sulfur, 10.5, 1.9, 4.5]
      - [Liquid rubber, 12.5, 1.9, 1.5]
      - ["144 mB → 1 plate", 14.5, 3.6, 1.5]
      - [Rubber plates, 16.5, 1.9, 1.5]
---
# Rubber: Large Arboreal Extractor

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `rubber` · **Tags:** Infinite source, 3D scene

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Rubber and liquid rubber](../../plan/p3.md#rubber)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-ae">
<div class="gt-head"><span class="gt-mname">Large Arboreal Extractor</span><span class="gt-badge t-mod">StarT</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Screw (kept) (gtceu:iron_screw)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_screw.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Screw</span><span class="gt-note">Screw (kept)</span></span><span class="gt-slot" title="Fertilizer (25 % used) (gtceu:fertilizer) - optional"><img class="gt-ico" src="../../assets/icons/gtceu__fertilizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fertilizer</span><span class="gt-note">Fertilizer (25 % used)</span><b class="gt-q">optional</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__large_arboreal_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Latex (thermal:latex_bucket) - 100-250 mB / 20 s"><img class="gt-ico" src="../../assets/icons/thermal__latex_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Latex</span><b class="gt-q">100-250 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:large_arboreal_extractor</code></div>
</div>
<div class="gt-panel t-lv" id="m-fs">
<div class="gt-head"><span class="gt-mname">Fluid Solidifier · ball mold</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Latex (thermal:latex_bucket) - 250 mB"><img class="gt-ico" src="../../assets/icons/thermal__latex_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Latex</span><b class="gt-q">250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_fluid_solidifier.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Rubber (thermal:rubber)"><img class="gt-ico" src="../../assets/icons/thermal__rubber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_fluid_solidifier</code></div>
</div>
<div class="gt-panel t-lv" id="m-cr">
<div class="gt-head"><span class="gt-mname">Chemical Reactor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Rubber (thermal:rubber) - 3"><img class="gt-ico" src="../../assets/icons/thermal__rubber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><b class="gt-q">3</b></span><span class="gt-slot" title="Sulfur (gtceu:sulfur_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Liquid Rubber (gtceu:rubber_bucket) - 576 mB"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><span class="gt-note">Liquid Rubber</span><b class="gt-q">576 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-so">
<div class="gt-head"><span class="gt-mname">Fluid Solidifier · plate mold</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Liquid Rubber (gtceu:rubber_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><span class="gt-note">Liquid Rubber</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_fluid_solidifier.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Rubber Plates (gtceu:rubber_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber Plate</span><span class="gt-note">Rubber Plates</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_fluid_solidifier</code></div>
</div>
</div>

## Flow

- [Large Arboreal Extractor](#m-ae) → [Fluid Solidifier · ball mold](#m-fs) → [Chemical Reactor](#m-cr) → [Fluid Solidifier · plate mold](#m-so)

## How to build

1. Large Arboreal Extractor: a 3 × 3 brick base with dirt in the middle, a 5-log jungle trunk on it, jungle leaves on top and brick slabs as the rim. The controller sits in the second brick layer; a ULV input bus and a ULV fluid output hatch replace two base bricks. — `start_core:large_arboreal_extractor`, `minecraft:bricks`, `minecraft:jungle_log`
2. A screw in the input bus is the tap and is never used up. Wood screw: 100 mB latex every 20 s (300 mB per minute). — `gtceu:wood_screw`, `gtceu:iron_screw`
3. With an iron screw plus fertilizer in the bus, output rises: bone meal 150, compost 200, fertilizer 250 mB per 20 s. Each run uses the fertilizer only 25 % of the time (fertilizer: 0.75 per minute for 750 mB latex). — `minecraft:bone_meal`, `thermal:compost`, `gtceu:fertilizer`
4. Latex to an LV Fluid Solidifier with a ball mold: 250 mB = 1 rubber in 6 s (8 EU/t). One extractor on fertilizer = 3 rubber per minute; build more extractors side by side to scale. — `gtceu:lv_fluid_solidifier`, `gtceu:ball_casting_mold`
5. LV Chemical Reactor: 3 rubber + 1 sulfur dust → 576 mB liquid rubber (12 s). A second solidifier with a plate mold makes 144 mB = 1 rubber plate, so 3 rubber become 4 plates. Liquid rubber also coats cables directly in the assembler. — `gtceu:lv_chemical_reactor`, `gtceu:sulfur_dust`
6. Before LV: heated Create mixer (3 rubber + sulfur → 3 cured rubber) then a press (cured rubber → rubber plate). Works, but 25 % less rubber per plate. — `create:mechanical_mixer`, `create:mechanical_press`

## Tips

- No power at all: the extractor is a brick multiblock built around a small jungle tree you place yourself (5 logs, 5 leaves).
- Chemical reactor route: 3 rubber + 1 sulfur = 576 mB = 4 plates. The Create mixer + press gives only 3 plates for the same rubber.
- Thermal’s small Arboreal Extractor only reads rubberwood trees, and rubberwood saplings are hidden in this pack: it gives nothing here.
- Needs fertilizer from the LV fertilizer line (optional: it only raises the yield).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:large_arboreal_extractor` | 1 |
| `minecraft:bricks` | 10 |
| `minecraft:brick_slab` | 6 |
| `minecraft:jungle_log` | 5 |
| `minecraft:jungle_leaves` | 5 |
| `minecraft:dirt` | 1 |
| `gtceu:ulv_input_bus` | 1 |
| `gtceu:ulv_output_hatch` | 1 |
| `gtceu:iron_screw` | 1 |
| `gtceu:lv_fluid_solidifier` | 2 |
| `gtceu:lv_chemical_reactor` | 1 |

## Needs / Feeds

- **Needs:** [Fertilizer (for the rubber extractor and greenhouses)](../lv/fertilizer.md), [Infinite redstone, sulfur &amp; pearls (dust sieve)](../feeders/sieve_dust.md)
- **Main source for:** `thermal:latex_bucket`, `thermal:rubber`

## Extras

- 3D assembly scene with 30 blocks (open it in the Atlas page).
