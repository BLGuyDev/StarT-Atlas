---
kind: chain
id: power_lapidary
order: 700
data:
  t: Diamond power (Lapidary Dynamos)
  inf: true
  power: true
  "n":
    - [sb, "2 Stone Barrels", s, "gtceu:stone_barrel"]
    - [hm, "2 Forge Hammers", m, "gtceu:lv_forge_hammer"]
    - [ms, "Mechanical Sieve · sand", m, "gtceu:mechanical_sieve"]
    - [gm, "Quartz, lapis, amethyst, emerald", o, "minecraft:emerald"]
    - [ld, "5 Lapidary Dynamos + LV kits", p, "thermal:dynamo_lapidary"]
    - [fc, Flux Cell, p, "thermal:energy_cell"]
    - [cv, Energy Converters, p, "gtceu:lv_4a_energy_converter"]
    - [out, "≈ 1 440 EU/t spare", o, "gtceu:soul_infused_quadruple_wire"]
  e:
    - [sb, hm, cobble]
    - [hm, ms, "sand 96/min"]
    - [ms, gm, "×16"]
    - [ms, ld, "24 diamonds/min"]
    - [ld, fc, "6 000 RF/t"]
    - [fc, cv, FE]
    - [cv, out, EU]
  tips:
    - |-
      16 diamonds every 40 s = 24 per minute = 7.2 million RF per minute: exactly enough for 5 dynamos with LV kits running flat out.
    - The sieve and its two hammers use about 55 EU/t of that themselves.
    - MV/HV Upgrade Kits multiply the dynamos further; diatron gems (750 000 RF) are the next fuel.
  b:
    - ["gtceu:stone_barrel", 2]
    - ["minecraft:lava_bucket", 2]
    - ["gtceu:lv_forge_hammer", 2]
    - ["gtceu:mechanical_sieve", 1]
    - ["exnihilosequentia:string_mesh", 1]
    - ["thermal:dynamo_lapidary", 5]
    - ["kubejs:lv_upgrade_kit", 5]
    - ["thermal:energy_cell", 1]
    - ["gtceu:lv_4a_energy_converter", 4]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:stone_barrel", "gtceu:lv_forge_hammer"]
      t: |-
        2 Stone Barrels (160 cobble per minute) into 2 Forge Hammers: cobble to gravel, then gravel to sand, 96 sand per minute for the sieve.
    - i: ["gtceu:mechanical_sieve"]
      t: |-
        One Mechanical Sieve on sand with a string mesh: 16 diamonds every 40 s, plus quartz, lapis, amethyst and emerald.
    - i: ["thermal:dynamo_lapidary", "kubejs:lv_upgrade_kit"]
      t: |-
        Lapidary Dynamo: assembler, RF coil + cobalt brass gear + LV hull + 288 mB tin alloy. Each gets one LV Upgrade Kit (4 silver plates + soul infused glass + bronze gear + LV circuit + 720 mB tin): 200 → 1 200 RF/t.
    - i: ["minecraft:diamond", "pipez:item_pipe"]
      t: An item pipe filtered to diamonds feeds the dynamos in round-robin. A diamond is 300 000 RF in this pack, so each dynamo burns one every 12.5 s at full power (4.8 per minute).
    - i: ["thermal:energy_cell", "gtceu:lv_4a_energy_converter"]
      t: Dynamos fill a Flux Cell; Energy Converters of the tier you need turn FE into EU (4 FE = 1 EU). LV 4A = 128 EU/t each; for MV machines use MV converters (512 EU/t each).
    - i: ["gtceu:cobalt_brass_gear"]
      t: |-
        Cobalt brass = 7 brass + 1 aluminium + 1 cobalt dust in the mixer. Cobalt: hand-sieve crushed blackstone with an iron mesh (cobaltite). Aluminium dust: LV electrolyzer on sodalite from the Void Extractor.
---
# Diamond power (Lapidary Dynamos)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_lapidary` · **Tags:** Infinite source, Power

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Diamond power](../../plan/p2.md#diamond)

**Tips:** 3

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-hm">
<div class="gt-head"><span class="gt-mname">2 Forge Hammers</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="2 Stone Barrels (gtceu:stone_barrel) - cobble"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Barrel</span><span class="gt-note">2 Stone Barrels</span><span class="gt-tag">infinite</span><b class="gt-q">cobble</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ms" title="Mechanical Sieve · sand (gtceu:mechanical_sieve) - sand 96/min"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Mechanical Sieve · sand</span><b class="gt-q">sand 96/min</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-ms">
<div class="gt-head"><span class="gt-mname">Mechanical Sieve · sand</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-hm" title="2 Forge Hammers (gtceu:lv_forge_hammer) - sand 96/min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">2 Forge Hammers</span><b class="gt-q">sand 96/min</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Quartz, lapis, amethyst, emerald (minecraft:emerald) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__emerald.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Emerald</span><span class="gt-note">Quartz, lapis, amethyst, emerald</span><b class="gt-q">×16</b></span><a class="gt-slot gt-power" href="#m-ld" title="5 Lapidary Dynamos + LV kits (thermal:dynamo_lapidary) - 24 diamonds/min"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">5 Lapidary Dynamos + LV kits</span><b class="gt-q">24 diamonds/min</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-ld">
<div class="gt-head"><span class="gt-mname">5 Lapidary Dynamos + LV kits</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ms" title="Mechanical Sieve · sand (gtceu:mechanical_sieve) - 24 diamonds/min"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Mechanical Sieve · sand</span><b class="gt-q">24 diamonds/min</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-fc" title="Flux Cell (thermal:energy_cell) - 6 000 RF/t"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energy Cell</span><span class="gt-note">Flux Cell</span><b class="gt-q">6 000 RF/t</b></a></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_lapidary</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-fc">
<div class="gt-head"><span class="gt-mname">Flux Cell</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-ld" title="5 Lapidary Dynamos + LV kits (thermal:dynamo_lapidary) - 6 000 RF/t"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">5 Lapidary Dynamos + LV kits</span><b class="gt-q">6 000 RF/t</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-cv" title="Energy Converters (gtceu:lv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 4a Energy Converter</span><span class="gt-note">Energy Converters</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>thermal:energy_cell</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-cv">
<div class="gt-head"><span class="gt-mname">Energy Converters</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-fc" title="Flux Cell (thermal:energy_cell) - FE"><img class="gt-ico" src="../../assets/icons/thermal__energy_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energy Cell</span><span class="gt-note">Flux Cell</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="≈ 1 440 EU/t spare (gtceu:soul_infused_quadruple_wire) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__soul_infused_quadruple_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Infused Quadruple Wire</span><span class="gt-note">≈ 1 440 EU/t spare</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [2 Forge Hammers](#m-hm) → [Mechanical Sieve · sand](#m-ms) → [5 Lapidary Dynamos + LV kits](#m-ld) → [Flux Cell](#m-fc) → [Energy Converters](#m-cv)

## How to build

1. 2 Stone Barrels (160 cobble per minute) into 2 Forge Hammers: cobble to gravel, then gravel to sand, 96 sand per minute for the sieve. — `gtceu:stone_barrel`, `gtceu:lv_forge_hammer`
2. One Mechanical Sieve on sand with a string mesh: 16 diamonds every 40 s, plus quartz, lapis, amethyst and emerald. — `gtceu:mechanical_sieve`
3. Lapidary Dynamo: assembler, RF coil + cobalt brass gear + LV hull + 288 mB tin alloy. Each gets one LV Upgrade Kit (4 silver plates + soul infused glass + bronze gear + LV circuit + 720 mB tin): 200 → 1 200 RF/t. — `thermal:dynamo_lapidary`, `kubejs:lv_upgrade_kit`
4. An item pipe filtered to diamonds feeds the dynamos in round-robin. A diamond is 300 000 RF in this pack, so each dynamo burns one every 12.5 s at full power (4.8 per minute). — `minecraft:diamond`, `pipez:item_pipe`
5. Dynamos fill a Flux Cell; Energy Converters of the tier you need turn FE into EU (4 FE = 1 EU). LV 4A = 128 EU/t each; for MV machines use MV converters (512 EU/t each). — `thermal:energy_cell`, `gtceu:lv_4a_energy_converter`
6. Cobalt brass = 7 brass + 1 aluminium + 1 cobalt dust in the mixer. Cobalt: hand-sieve crushed blackstone with an iron mesh (cobaltite). Aluminium dust: LV electrolyzer on sodalite from the Void Extractor. — `gtceu:cobalt_brass_gear`

## Tips

- 16 diamonds every 40 s = 24 per minute = 7.2 million RF per minute: exactly enough for 5 dynamos with LV kits running flat out.
- The sieve and its two hammers use about 55 EU/t of that themselves.
- MV/HV Upgrade Kits multiply the dynamos further; diatron gems (750 000 RF) are the next fuel.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:stone_barrel` | 2 |
| `minecraft:lava_bucket` | 2 |
| `gtceu:lv_forge_hammer` | 2 |
| `gtceu:mechanical_sieve` | 1 |
| `exnihilosequentia:string_mesh` | 1 |
| `thermal:dynamo_lapidary` | 5 |
| `kubejs:lv_upgrade_kit` | 5 |
| `thermal:energy_cell` | 1 |
| `gtceu:lv_4a_energy_converter` | 4 |
| `pipez:item_pipe` | 16 |
