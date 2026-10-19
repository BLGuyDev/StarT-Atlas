---
kind: chain
id: crop_farm
order: 430
data:
  t: "Crops: Large Farm (no power)"
  inf: true
  "n":
    - [sd, "Seeds (rooted dirt sieve)", s, "minecraft:wheat_seeds"]
    - [lf, Large Farm, m, "gtceu:large_farm"]
    - [cr, Crops, x, "minecraft:wheat"]
    - [cp, "Compressor ×8", m, "gtceu:lv_compressor"]
    - [pb, Plant Ball, o, "gtceu:plant_ball"]
    - [br, Brewery, m, "gtceu:lv_brewery"]
    - [bm, Biomass, o, "gtceu:biomass_bucket"]
  e: [[sd, lf], [lf, cr], [cr, cp, "8"], [cp, pb], [cr, br], [br, bm]]
  tips:
    - |-
      No power and cheap, but it stops at night: about 12 crops per minute averaged over a day.
    - |-
      Sugar cane in the coke oven: 8 → 1 charcoal + 50 mB creosote.
  store: ["functionalstorage:oak_1"]
  b: [["gtceu:large_farm", 1], ["gtceu:lv_compressor", 1], ["gtceu:lv_brewery", 1]]
  how:
    - i: ["gtceu:large_farm", "gtceu:treated_wood_frame", "gtceu:treated_wood_planks"]
      t: |-
        Large Farm: 20 treated wood frames, 15 treated wood planks, 8 farmland and 1 water inside, controller from treated wood and bone meal. Buses replace planks.
    - i: ["minecraft:wheat_seeds"]
      t: |-
        8 seeds in the input bus (kept): 16 crops every 40 s, plus 8 seeds back half the time. Daytime only.
    - i: ["gtceu:lv_compressor", "gtceu:plant_ball"]
      t: "Compressor: 8 crops → plant ball. Brewery: crops → biomass."
---
# Crops: Large Farm (no power)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `crop_farm` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lf">
<div class="gt-head"><span class="gt-mname">Large Farm</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Seeds (rooted dirt sieve) (minecraft:wheat_seeds)"><img class="gt-ico" src="../../assets/icons/minecraft__wheat_seeds.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat Seeds</span><span class="gt-note">Seeds (rooted dirt sieve)</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_farm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Crops (minecraft:wheat)"><img class="gt-ico" src="../../assets/icons/minecraft__wheat.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat</span><span class="gt-note">Crops</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_farm</code></div>
</div>
<div class="gt-panel t-lv" id="m-cp">
<div class="gt-head"><span class="gt-mname">Compressor ×8</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crops (minecraft:wheat) - 8"><img class="gt-ico" src="../../assets/icons/minecraft__wheat.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat</span><span class="gt-note">Crops</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_compressor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Plant Ball (gtceu:plant_ball)"><img class="gt-ico" src="../../assets/icons/gtceu__plant_ball.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plant Ball</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_compressor</code></div>
</div>
<div class="gt-panel t-lv" id="m-br">
<div class="gt-head"><span class="gt-mname">Brewery</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crops (minecraft:wheat)"><img class="gt-ico" src="../../assets/icons/minecraft__wheat.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat</span><span class="gt-note">Crops</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_brewery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Biomass (gtceu:biomass_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__biomass_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Biomass Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_brewery</code></div>
</div>
</div>

## Flow

- [Large Farm](#m-lf) → [Compressor ×8](#m-cp) (also Large Farm → [Brewery](#m-br))
- [Brewery](#m-br)

## How to build

1. Large Farm: 20 treated wood frames, 15 treated wood planks, 8 farmland and 1 water inside, controller from treated wood and bone meal. Buses replace planks. — `gtceu:large_farm`, `gtceu:treated_wood_frame`, `gtceu:treated_wood_planks`
2. 8 seeds in the input bus (kept): 16 crops every 40 s, plus 8 seeds back half the time. Daytime only. — `minecraft:wheat_seeds`
3. Compressor: 8 crops → plant ball. Brewery: crops → biomass. — `gtceu:lv_compressor`, `gtceu:plant_ball`

## Tips

- No power and cheap, but it stops at night: about 12 crops per minute averaged over a day.
- Sugar cane in the coke oven: 8 → 1 charcoal + 50 mB creosote.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_farm` | 1 |
| `gtceu:lv_compressor` | 1 |
| `gtceu:lv_brewery` | 1 |

## Storage

`functionalstorage:oak_1`

## Needs / Feeds

- **Feeds:** [Polyethylene](../mv/polyethylene.md), [Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff](../hv/oil_pyro.md)
- **Main source for:** `gtceu:plant_ball`, `gtceu:bio_diesel_bucket`
