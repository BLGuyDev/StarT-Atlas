---
kind: chain
id: power_lv
order: 90
data:
  t: LV power grid
  power: true
  "n":
    - [f1, "Charcoal / creosote", i, "minecraft:charcoal"]
    - [f2, "Diamonds (sieve)", i, "minecraft:diamond"]
    - [d1, Stirling Dynamo, p, "thermal:dynamo_stirling"]
    - [d2, Lapidary Dynamo, p, "thermal:dynamo_lapidary"]
    - [kit, LV Upgrade Kit, x, "kubejs:lv_upgrade_kit"]
    - [cell, Flux Cell, x, "thermal:energy_cell"]
    - [cv, LV 4A Converter, m, "gtceu:lv_4a_energy_converter"]
    - [w, Soul Infused wire, x, "gtceu:soul_infused_single_wire"]
    - [bb, Battery Buffer, x, "gtceu:lv_battery_buffer_4x"]
    - [mc, LV machines, o, "gtceu:lv_assembler"]
  e:
    - [f1, d1]
    - [f2, d2]
    - [kit, d1, "×6"]
    - [kit, d2, "×6"]
    - [d1, cell, FE]
    - [d2, cell, FE]
    - [cell, cv, FE]
    - [cv, w, "32 V · 4 A"]
    - [w, bb]
    - [bb, mc]
  tips:
    - |-
      4 FE = 1 EU. LV 4A converter = 128 EU/t = 4 machines at full speed.
    - |-
      ARC kit: more power, less efficiency. MCI kit: more efficiency.
    - Higher voltage on an LV machine makes it explode.
  b:
    - ["thermal:dynamo_stirling", 4]
    - ["thermal:dynamo_lapidary", 2]
    - ["kubejs:lv_upgrade_kit", 6]
    - ["thermal:energy_cell", 1]
    - ["gtceu:lv_4a_energy_converter", 1]
    - ["gtceu:soul_infused_quadruple_wire", 8]
    - ["gtceu:lv_battery_buffer_4x", 1]
  how:
    - i: ["thermal:dynamo_stirling", "minecraft:charcoal"]
      t: "4 Stirling Dynamos fed charcoal by a funnel or pipe."
    - i: ["thermal:dynamo_lapidary", "minecraft:diamond"]
      t: "2 Lapidary Dynamos fed diamonds from the sand sieve."
    - i: ["kubejs:lv_upgrade_kit"]
      t: |-
        One LV Upgrade Kit in each dynamo: ×6 to every stat. ARC kits raise power, MCI kits raise efficiency.
    - i: ["thermal:energy_cell", "gtceu:lv_4a_energy_converter"]
      t: |-
        Every dynamo feeds a Flux Cell, and the cell feeds an LV 4A converter: 128 EU/t, four LV machines at full speed.
    - i: ["gtceu:soul_infused_quadruple_wire", "gtceu:lv_battery_buffer_4x"]
      t: Soul infused wire (lossless) runs to a battery buffer, which feeds the machines.
---
# LV power grid

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_lv` · **Tags:** Power

**Tips:** 3

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod gt-gen" id="m-d1">
<div class="gt-head"><span class="gt-mname">Stirling Dynamo</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Charcoal / creosote (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span><span class="gt-note">Charcoal / creosote</span></span><span class="gt-slot" title="LV Upgrade Kit (kubejs:lv_upgrade_kit) - ×6"><img class="gt-ico" src="../../assets/icons/kubejs__lv_upgrade_kit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Upgrade Kit</span><b class="gt-q">×6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_stirling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Flux Cell (thermal:energy_cell) - FE"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energy Cell</span><span class="gt-note">Flux Cell</span><b class="gt-q">FE</b></span></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_stirling</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-d2">
<div class="gt-head"><span class="gt-mname">Lapidary Dynamo</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Diamonds (sieve) (minecraft:diamond)"><img class="gt-ico" src="../../assets/icons/minecraft__diamond.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond</span><span class="gt-note">Diamonds (sieve)</span></span><span class="gt-slot" title="LV Upgrade Kit (kubejs:lv_upgrade_kit) - ×6"><img class="gt-ico" src="../../assets/icons/kubejs__lv_upgrade_kit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Upgrade Kit</span><b class="gt-q">×6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Flux Cell (thermal:energy_cell) - FE"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energy Cell</span><span class="gt-note">Flux Cell</span><b class="gt-q">FE</b></span></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_lapidary</code></div>
</div>
<div class="gt-panel t-lv" id="m-cv">
<div class="gt-head"><span class="gt-mname">LV 4A Converter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Flux Cell (thermal:energy_cell) - FE"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energy Cell</span><span class="gt-note">Flux Cell</span><b class="gt-q">FE</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Soul Infused wire (gtceu:soul_infused_single_wire) - 32 V · 4 A"><img class="gt-ico" src="../../assets/icons/gtceu__soul_infused_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Infused Single Wire</span><span class="gt-note">Soul Infused wire</span><b class="gt-q">32 V · 4 A</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [Stirling Dynamo](#m-d1) → [LV 4A Converter](#m-cv)
- [Lapidary Dynamo](#m-d2) → [LV 4A Converter](#m-cv)

### Direct steps

- Soul Infused wire → Battery Buffer
- Battery Buffer → LV machines

## How to build

1. 4 Stirling Dynamos fed charcoal by a funnel or pipe. — `thermal:dynamo_stirling`, `minecraft:charcoal`
2. 2 Lapidary Dynamos fed diamonds from the sand sieve. — `thermal:dynamo_lapidary`, `minecraft:diamond`
3. One LV Upgrade Kit in each dynamo: ×6 to every stat. ARC kits raise power, MCI kits raise efficiency. — `kubejs:lv_upgrade_kit`
4. Every dynamo feeds a Flux Cell, and the cell feeds an LV 4A converter: 128 EU/t, four LV machines at full speed. — `thermal:energy_cell`, `gtceu:lv_4a_energy_converter`
5. Soul infused wire (lossless) runs to a battery buffer, which feeds the machines. — `gtceu:soul_infused_quadruple_wire`, `gtceu:lv_battery_buffer_4x`

## Tips

- 4 FE = 1 EU. LV 4A converter = 128 EU/t = 4 machines at full speed.
- ARC kit: more power, less efficiency. MCI kit: more efficiency.
- Higher voltage on an LV machine makes it explode.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:dynamo_stirling` | 4 |
| `thermal:dynamo_lapidary` | 2 |
| `kubejs:lv_upgrade_kit` | 6 |
| `thermal:energy_cell` | 1 |
| `gtceu:lv_4a_energy_converter` | 1 |
| `gtceu:soul_infused_quadruple_wire` | 8 |
| `gtceu:lv_battery_buffer_4x` | 1 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
