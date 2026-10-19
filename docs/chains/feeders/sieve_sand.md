---
kind: chain
id: sieve_sand
order: 480
data:
  t: Infinite gems (sand sieve)
  inf: true
  "n":
    - [g, "Gravel (ore sieve line)", s, "minecraft:gravel"]
    - [fh, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [s, Sand, x, "minecraft:sand"]
    - [ms, Mechanical Sieve, m, "gtceu:mechanical_sieve"]
    - [o1, Diamond, o, "minecraft:diamond"]
    - [o2, Emerald, o, "minecraft:emerald"]
    - [o3, Nether Quartz, o, "minecraft:quartz"]
    - [o4, Lapis, o, "minecraft:lapis_lazuli"]
    - [o5, Amethyst, o, "minecraft:amethyst_shard"]
  e:
    - [g, fh]
    - [fh, s]
    - [s, ms, "64"]
    - [ms, o1, "×16"]
    - [ms, o2, "×16"]
    - [ms, o3, "×16"]
    - [ms, o4, "×16"]
    - [ms, o5, "×16"]
  tips: ["16 diamonds every 40 s: free fuel for the lapidary dynamos."]
  store: ["gtceu:lv_super_chest"]
  b:
    - ["gtceu:lv_forge_hammer", 1]
    - ["gtceu:mechanical_sieve", 1]
    - ["exnihilosequentia:string_mesh", 1]
    - ["gtceu:lv_super_chest", 2]
---
# Infinite gems (sand sieve)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_sand` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-fh">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Gravel (ore sieve line) (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span><span class="gt-note">Gravel (ore sieve line)</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Sand (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-ms">
<div class="gt-head"><span class="gt-mname">Mechanical Sieve</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sand (minecraft:sand) - 64"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span><b class="gt-q">64</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Diamond (minecraft:diamond) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__diamond.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Emerald (minecraft:emerald) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__emerald.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Emerald</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Nether Quartz (minecraft:quartz) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__quartz.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quartz</span><span class="gt-note">Nether Quartz</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Lapis (minecraft:lapis_lazuli) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__lapis_lazuli.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lapis Lazuli</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Amethyst (minecraft:amethyst_shard) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__amethyst_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Amethyst Shard</span><b class="gt-q">×16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
</div>

## Flow

- [Forge Hammer](#m-fh) → [Mechanical Sieve](#m-ms)

## Tips

- 16 diamonds every 40 s: free fuel for the lapidary dynamos.

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

- **Needs:** [Gravel, sand &amp; dust: Forge Hammers](gravel_hammer.md)
- **Feeds:** [Barrel transformations](../stone/barrel.md), [Firebricks &amp; coke oven bricks](../stone/bricks.md), [LV power grid](../power/power_lv.md), [MV power grid](../power/power_mv.md), [LV circuit parts from earlier lines](circuit_parts.md), [Infinite redstone, sulfur &amp; pearls (dust sieve)](sieve_dust.md), [Magnets: from magnetite block to Fluxuated Magnetite](../lv/magnets.md), [Fertilizer (for the rubber extractor and greenhouses)](../lv/fertilizer.md), [Chlorine and hydrochloric acid (water → salt water → acid)](../mv/mv_chlorine.md), [Diodes (gallium arsenide + glass + fine wire)](../mv/mv_diode.md), [Soul infused ingots (LV superconductor): sand → soul sand → dust + invar](../lv/soul_infused.md)
- **Main source for:** `minecraft:sand`, `minecraft:diamond`, `gtceu:diatron_gem`, `minecraft:glass`, `minecraft:quartz`
