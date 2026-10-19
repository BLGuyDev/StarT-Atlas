---
kind: chain
id: sieve_blackstone
order: 500
data:
  t: Infinite lead, silver & antimony (blackstone sieve)
  inf: true
  "n":
    - [ww, Witch Water, s, "exnihilosequentia:witch_water_bucket"]
    - [sb, "Stone Barrel + lava", m, "gtceu:stone_barrel"]
    - [b, Blackstone, x, "minecraft:blackstone"]
    - [fh, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [cb, Crushed Blackstone, x, "exnihilosequentia:crushed_blackstone"]
    - [ms, Mechanical Sieve, m, "gtceu:mechanical_sieve"]
    - [o1, Crushed Galena, o, "gtceu:crushed_galena_ore"]
    - [o2, Crushed Stibnite, o, "gtceu:crushed_stibnite_ore"]
  e: [[ww, sb], [sb, b], [b, fh], [fh, cb], [cb, ms, "64"], [ms, o1, "×16"], [ms, o2, "×16"]]
  tips:
    - Galena → lead + silver (aqueous accumulator, signalum, lumium). Stibnite → antimony.
    - Create crushing wheels also turn blackstone into crushed blackstone.
  b:
    - ["gtceu:stone_barrel", 1]
    - ["gtceu:lv_forge_hammer", 1]
    - ["gtceu:mechanical_sieve", 1]
    - ["exnihilosequentia:string_mesh", 1]
    - ["gtceu:lv_super_chest", 1]
---
# Infinite lead, silver &amp; antimony (blackstone sieve)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_blackstone` · **Tags:** Infinite source

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-sb">
<div class="gt-head"><span class="gt-mname">Stone Barrel + lava</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Witch Water (exnihilosequentia:witch_water_bucket)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__witch_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Witch Water Bucket</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Blackstone (minecraft:blackstone)"><img class="gt-ico" src="../../assets/icons/minecraft__blackstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blackstone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-fh">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Blackstone (minecraft:blackstone)"><img class="gt-ico" src="../../assets/icons/minecraft__blackstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blackstone</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Crushed Blackstone (exnihilosequentia:crushed_blackstone)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__crushed_blackstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Blackstone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-ms">
<div class="gt-head"><span class="gt-mname">Mechanical Sieve</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crushed Blackstone (exnihilosequentia:crushed_blackstone) - 64"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__crushed_blackstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Blackstone</span><b class="gt-q">64</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Galena (gtceu:crushed_galena_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_galena_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Galena Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Stibnite (gtceu:crushed_stibnite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_stibnite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Stibnite Ore</span><b class="gt-q">×16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
</div>

## Flow

- [Stone Barrel + lava](#m-sb) → [Forge Hammer](#m-fh) → [Mechanical Sieve](#m-ms)

## Tips

- Galena → lead + silver (aqueous accumulator, signalum, lumium). Stibnite → antimony.
- Create crushing wheels also turn blackstone into crushed blackstone.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:stone_barrel` | 1 |
| `gtceu:lv_forge_hammer` | 1 |
| `gtceu:mechanical_sieve` | 1 |
| `exnihilosequentia:string_mesh` | 1 |
| `gtceu:lv_super_chest` | 1 |

## Needs / Feeds

- **Needs:** [Barrel transformations](../stone/barrel.md)
- **Main source for:** `gtceu:lead_ingot`
