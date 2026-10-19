---
kind: chain
id: power_newage
order: 100
data:
  t: Fuel-free LV power (Create New Age)
  inf: true
  power: true
  "n":
    - [wm, Windmill, p, "create:windmill_bearing"]
    - [gc, Generator Coil, m, "create_new_age:generator_coil"]
    - [mg, Magnets, x, "create_new_age:redstone_magnet"]
    - [cb, Carbon Brushes, m, "create_new_age:carbon_brushes"]
    - [cv, LV Converter, m, "gtceu:lv_4a_energy_converter"]
    - [w, Soul Infused wire, x, "gtceu:soul_infused_single_wire"]
    - [ms, Mechanical Sieve, o, "gtceu:mechanical_sieve"]
  e: [[wm, gc, RPM], [mg, gc, field], [gc, cb], [cb, cv, FE], [cv, w, EU], [w, ms]]
  tips:
    - FE/t = RPM × magnet strength / 20 · SU = RPM × (strength + 24).
    - "Stronger magnets: layered, fluxuated magnetite, netherite."
  b:
    - ["create:windmill_bearing", 1]
    - ["create:white_sail", 32]
    - ["create_new_age:generator_coil", 4]
    - ["create_new_age:redstone_magnet", 8]
    - ["create_new_age:carbon_brushes", 1]
    - ["gtceu:lv_4a_energy_converter", 1]
  how:
    - i: ["create_new_age:generator_coil"]
      t: Generator Coils sit on a shaft line. One set of Carbon Brushes can collect from up to 8 coils (pack config).
    - i: ["create_new_age:magnetite_block", "create_new_age:redstone_magnet", "create_new_age:layered_magnet"]
      t: Magnets around each coil add up their magnetic force (tooltip “Magnetic Force”). FE/t = RPM × force / 20.
    - i: ["create:windmill_bearing"]
      t: Each coil costs RPM × (force + 24) SU. Use the calculator below to size windmills against RPM.
    - i: ["gtceu:lv_4a_energy_converter"]
      t: Brushes → LV converter (4 FE = 1 EU). Below 128 FE/t use a 1A converter; above, a 4A one.
  calc:
    rpm: 140
    windmills: 1
    sails: 128
    mag:
      magnetite: 6
      redstone: 6
      layered: 0
      fluxuated: 0
      netherite: 0
    wheels: 0
    coils: 1
    euNeed: 30
---
# Fuel-free LV power (Create New Age)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_newage` · **Tags:** Infinite source, Power

**Tips:** 2

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-gc" title="Generator Coil (create_new_age:generator_coil) - RPM"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Generator Coil</span><b class="gt-q">RPM</b></a></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
<div class="gt-panel t-mod" id="m-gc">
<div class="gt-head"><span class="gt-mname">Generator Coil</span><span class="gt-badge t-mod">New Age</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-wm" title="Windmill (create:windmill_bearing) - RPM"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Windmill Bearing</span><b class="gt-q">RPM</b></a><span class="gt-slot" title="Magnets (create_new_age:redstone_magnet) - field"><img class="gt-ico" src="../../assets/icons/create_new_age__redstone_magnet.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Redstone Magnet</span><span class="gt-note">Magnets</span><b class="gt-q">field</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cb" title="Carbon Brushes (create_new_age:carbon_brushes)"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Brushes</span></a></div>
</div>
<div class="gt-foot"><code>create_new_age:generator_coil</code></div>
</div>
<div class="gt-panel t-mod" id="m-cb">
<div class="gt-head"><span class="gt-mname">Carbon Brushes</span><span class="gt-badge t-mod">New Age</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-gc" title="Generator Coil (create_new_age:generator_coil)"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Generator Coil</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cv" title="LV Converter (gtceu:lv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 4a Energy Converter</span><span class="gt-note">LV Converter</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>create_new_age:carbon_brushes</code></div>
</div>
<div class="gt-panel t-lv" id="m-cv">
<div class="gt-head"><span class="gt-mname">LV Converter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-cb" title="Carbon Brushes (create_new_age:carbon_brushes) - FE"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Brushes</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Soul Infused wire (gtceu:soul_infused_single_wire) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__soul_infused_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Infused Single Wire</span><span class="gt-note">Soul Infused wire</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [Windmill](#m-wm) → [Generator Coil](#m-gc) → [Carbon Brushes](#m-cb) → [LV Converter](#m-cv)

### Direct steps

- Soul Infused wire → Mechanical Sieve

## How to build

1. Generator Coils sit on a shaft line. One set of Carbon Brushes can collect from up to 8 coils (pack config). — `create_new_age:generator_coil`
2. Magnets around each coil add up their magnetic force (tooltip “Magnetic Force”). FE/t = RPM × force / 20. — `create_new_age:magnetite_block`, `create_new_age:redstone_magnet`, `create_new_age:layered_magnet`
3. Each coil costs RPM × (force + 24) SU. Use the calculator below to size windmills against RPM. — `create:windmill_bearing`
4. Brushes → LV converter (4 FE = 1 EU). Below 128 FE/t use a 1A converter; above, a 4A one. — `gtceu:lv_4a_energy_converter`

## Tips

- FE/t = RPM × magnet strength / 20 · SU = RPM × (strength + 24).
- Stronger magnets: layered, fluxuated magnetite, netherite.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:windmill_bearing` | 1 |
| `create:white_sail` | 32 |
| `create_new_age:generator_coil` | 4 |
| `create_new_age:redstone_magnet` | 8 |
| `create_new_age:carbon_brushes` | 1 |
| `gtceu:lv_4a_energy_converter` | 1 |

## Extras

- Power calculator defaults are stored in the front matter (`calc`).
