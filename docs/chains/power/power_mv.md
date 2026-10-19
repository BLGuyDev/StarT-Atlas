---
kind: chain
id: power_mv
order: 170
data:
  t: MV power grid
  power: true
  "n":
    - [dia, Sieve diamonds, i, "minecraft:diamond"]
    - [d2, "Lapidary + MV kits", p, "thermal:dynamo_lapidary"]
    - [bd, "Biodiesel / creosote", f, "gtceu:bio_diesel_bucket"]
    - [d3, Compression Dynamo, p, "thermal:dynamo_compression"]
    - [cv, MV 4A Converter, m, "gtceu:mv_4a_energy_converter"]
    - [w, Signalum wire, x, "gtceu:signalum_single_wire"]
    - [mc, MV machines, o, "gtceu:mv_assembler"]
  e: [[dia, d2], [bd, d3], [d2, cv, FE], [d3, cv, FE], [cv, w, "128 V"], [w, mc]]
  tips: ["Alt: dynamo + steam pipe = boiler → GT steam turbines."]
  b:
    - ["thermal:dynamo_lapidary", 4]
    - ["kubejs:mv_upgrade_kit", 4]
    - ["thermal:dynamo_compression", 2]
    - ["gtceu:mv_4a_energy_converter", 1]
    - ["gtceu:signalum_quadruple_wire", 8]
---
# MV power grid

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_mv` · **Tags:** Power

**Tips:** 1

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod gt-gen" id="m-d2">
<div class="gt-head"><span class="gt-mname">Lapidary + MV kits</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sieve diamonds (minecraft:diamond)"><img class="gt-ico" src="../../assets/icons/minecraft__diamond.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond</span><span class="gt-note">Sieve diamonds</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cv" title="MV 4A Converter (gtceu:mv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__mv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV 4a Energy Converter</span><span class="gt-note">MV 4A Converter</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_lapidary</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-d3">
<div class="gt-head"><span class="gt-mname">Compression Dynamo</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Biodiesel / creosote (gtceu:bio_diesel_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__bio_diesel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bio Diesel</span><span class="gt-note">Biodiesel / creosote</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_compression.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cv" title="MV 4A Converter (gtceu:mv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__mv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV 4a Energy Converter</span><span class="gt-note">MV 4A Converter</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_compression</code></div>
</div>
<div class="gt-panel t-mv" id="m-cv">
<div class="gt-head"><span class="gt-mname">MV 4A Converter</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-d2" title="Lapidary + MV kits (thermal:dynamo_lapidary) - FE"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">Lapidary + MV kits</span><b class="gt-q">FE</b></a><a class="gt-slot gt-power" href="#m-d3" title="Compression Dynamo (thermal:dynamo_compression) - FE"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_compression.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Compression</span><span class="gt-note">Compression Dynamo</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Signalum wire (gtceu:signalum_single_wire) - 128 V"><img class="gt-ico" src="../../assets/icons/gtceu__signalum_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Signalum Single Wire</span><span class="gt-note">Signalum wire</span><b class="gt-q">128 V</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [Lapidary + MV kits](#m-d2) → [MV 4A Converter](#m-cv)
- [Compression Dynamo](#m-d3) → [MV 4A Converter](#m-cv)

### Direct steps

- Signalum wire → MV machines

## Tips

- Alt: dynamo + steam pipe = boiler → GT steam turbines.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:dynamo_lapidary` | 4 |
| `kubejs:mv_upgrade_kit` | 4 |
| `thermal:dynamo_compression` | 2 |
| `gtceu:mv_4a_energy_converter` | 1 |
| `gtceu:signalum_quadruple_wire` | 8 |

## Needs / Feeds

- **Needs:** [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
