---
kind: chain
id: power_steam
order: 670
data:
  t: "LV power: boilers + steam turbines"
  power: true
  "n":
    - [ch, Charcoal, i, "minecraft:charcoal"]
    - [bo, "Stirling Boiler (dynamo + boiler pipe)", m, "systeams:boiler_pipe"]
    - [w, Water, i, "minecraft:water_bucket"]
    - [st, Steam, f, "gtceu:steam_bucket"]
    - [tu, "LV Steam Turbine ×2", p, "gtceu:lv_steam_turbine"]
    - [mc, LV machines, o, "gtceu:lv_assembler"]
  e: [[ch, bo], [w, bo], [bo, st], [st, tu], [tu, mc, EU directly]]
  tips:
    - Right-click a Thermal dynamo with a Steam Pipe to turn it into a boiler.
    - "GT turbines output EU directly: no converter needed."
  b:
    - ["thermal:dynamo_stirling", 2]
    - ["systeams:boiler_pipe", 2]
    - ["gtceu:lv_steam_turbine", 2]
    - ["pipez:fluid_pipe", 6]
  how:
    - i: ["thermal:dynamo_stirling", "systeams:boiler_pipe"]
      t: Right-click a Stirling Dynamo with a Steam Pipe to make it a boiler; feed charcoal and water.
    - i: ["gtceu:lv_steam_turbine"]
      t: |-
        Pipe the steam into LV Steam Turbines: they output EU directly, so no converter is needed.
    - i: ["gtceu:soul_infused_single_wire"]
      t: Turbine → soul infused wire → machines.
---
# LV power: boilers + steam turbines

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_steam` · **Tags:** Power

**Tips:** 2

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-bo">
<div class="gt-head"><span class="gt-mname">Stirling Boiler (dynamo + boiler pipe)</span><span class="gt-badge t-mod">Systeams</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span><span class="gt-slot" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/systeams__boiler_pipe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Steam (gtceu:steam_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__steam_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam</span></span></div>
</div>
<div class="gt-foot"><code>systeams:boiler_pipe</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-tu">
<div class="gt-head"><span class="gt-mname">LV Steam Turbine ×2</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Steam (gtceu:steam_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__steam_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_steam_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV machines (gtceu:lv_assembler) - EU directly"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Assembler</span><span class="gt-note">LV machines</span><b class="gt-q">EU directly</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_steam_turbine</code></div>
</div>
</div>

## Flow

- [Stirling Boiler (dynamo + boiler pipe)](#m-bo) → [LV Steam Turbine ×2](#m-tu)

## How to build

1. Right-click a Stirling Dynamo with a Steam Pipe to make it a boiler; feed charcoal and water. — `thermal:dynamo_stirling`, `systeams:boiler_pipe`
2. Pipe the steam into LV Steam Turbines: they output EU directly, so no converter is needed. — `gtceu:lv_steam_turbine`
3. Turbine → soul infused wire → machines. — `gtceu:soul_infused_single_wire`

## Tips

- Right-click a Thermal dynamo with a Steam Pipe to turn it into a boiler.
- GT turbines output EU directly: no converter needed.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:dynamo_stirling` | 2 |
| `systeams:boiler_pipe` | 2 |
| `gtceu:lv_steam_turbine` | 2 |
| `pipez:fluid_pipe` | 6 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md), [Infinite water](../stone/inf_water.md)
