---
kind: chain
id: sieve_dust
order: 490
data:
  t: Infinite redstone, sulfur & pearls (dust sieve)
  inf: true
  "n":
    - [s, Sand, s, "minecraft:sand"]
    - [fh, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [d, Dust, x, "exnihilosequentia:dust"]
    - [ms, Mechanical Sieve, m, "gtceu:mechanical_sieve"]
    - [o1, Redstone, o, "minecraft:redstone"]
    - [o2, Glowstone Dust, o, "minecraft:glowstone_dust"]
    - [o3, Sulfur Dust, o, "gtceu:sulfur_dust"]
    - [o4, Ender Pearl, o, "minecraft:ender_pearl"]
  e: [[s, fh], [fh, d], [d, ms, "64"], [ms, o1, "×16"], [ms, o2, "×16"], [ms, o3, "×4"], [ms, o4, "×4"]]
  tips: ["Part of the dust can go to barrels for clay (aluminium line)."]
  store: ["gtceu:lv_super_chest"]
  b:
    - ["gtceu:lv_forge_hammer", 1]
    - ["gtceu:mechanical_sieve", 1]
    - ["exnihilosequentia:string_mesh", 1]
    - ["gtceu:lv_super_chest", 2]
---
# Infinite redstone, sulfur &amp; pearls (dust sieve)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_dust` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-fh">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Sand (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Dust (exnihilosequentia:dust)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-ms">
<div class="gt-head"><span class="gt-mname">Mechanical Sieve</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Dust (exnihilosequentia:dust) - 64"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dust</span><b class="gt-q">64</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Redstone (minecraft:redstone) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__redstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Redstone</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Glowstone Dust (minecraft:glowstone_dust) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__glowstone_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glowstone Dust</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Sulfur Dust (gtceu:sulfur_dust) - ×4"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dust</span><b class="gt-q">×4</b></span><span class="gt-slot gt-outp" title="Ender Pearl (minecraft:ender_pearl) - ×4"><img class="gt-ico" src="../../assets/icons/minecraft__ender_pearl.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender Pearl</span><b class="gt-q">×4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
</div>

## Flow

- [Forge Hammer](#m-fh) → [Mechanical Sieve](#m-ms)

## Tips

- Part of the dust can go to barrels for clay (aluminium line).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_forge_hammer` | 1 |
| `gtceu:mechanical_sieve` | 1 |
| `exnihilosequentia:string_mesh` | 1 |
| `gtceu:lv_super_chest` | 2 |

## Storage

`gtceu:lv_super_chest`

## Needs / Feeds

- **Needs:** [Infinite gems (sand sieve)](sieve_sand.md)
- **Feeds:** [Barrel transformations](../stone/barrel.md), [Alloys: Create heated mixer](../steam/alloys.md), [Infinite aluminium (clay)](../mv/aluminium.md), [Sulfuric acid](../mv/sulfuric.md), [Rubber: Large Arboreal Extractor](../steam/rubber.md)
- **Main source for:** `exnihilosequentia:dust`, `minecraft:redstone`, `gtceu:sulfur_dust`, `gtceu:tiny_sulfur_dust`, `thermal:ender_bucket`, `minecraft:ender_pearl`, `minecraft:glowstone_dust`
