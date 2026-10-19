---
kind: chain
id: barrel
order: 30
data:
  t: Barrel transformations
  inf: true
  "n":
    - [w, Water, f, "minecraft:water_bucket"]
    - [d, Dust, i, "exnihilosequentia:dust"]
    - [sp, Mycelium Spores, i, "exnihilosequentia:mycelium_spores"]
    - [b1, Barrel, m, "gtceu:barrel"]
    - [b2, Barrel, m, "gtceu:barrel"]
    - [b3, Barrel, m, "gtceu:barrel"]
    - [sa, Sand, i, "minecraft:sand"]
    - [cl, Clay, o, "minecraft:clay"]
    - [ww, Witch Water, f, "exnihilosequentia:witch_water_bucket"]
    - [ss, Soul Sand, o, "minecraft:soul_sand"]
  e: [[d, b1], [w, b1, "1 B"], [b1, cl], [sp, b2, kept], [w, b2], [b2, ww], [ww, b3, "1 B"], [sa, b3], [b3, ss]]
  tips: ["Cobble + witch water = blackstone · red mushroom block + witch water = slime block."]
  b: [["gtceu:barrel", 3]]
---
# Barrel transformations

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `barrel` · **Tags:** Infinite source

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Barrel transformations](../../plan/p0.md#barrels)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-b1">
<div class="gt-head"><span class="gt-mname">Barrel</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Dust (exnihilosequentia:dust)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dust</span></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Clay (minecraft:clay)"><img class="gt-ico" src="../../assets/icons/minecraft__clay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Clay</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:barrel</code></div>
</div>
<div class="gt-panel t-mod" id="m-b2">
<div class="gt-head"><span class="gt-mname">Barrel</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Mycelium Spores (exnihilosequentia:mycelium_spores) - kept"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__mycelium_spores.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mycelium Spores</span><b class="gt-q">kept</b></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Witch Water (exnihilosequentia:witch_water_bucket)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__witch_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Witch Water</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:barrel</code></div>
</div>
<div class="gt-panel t-mod" id="m-b3">
<div class="gt-head"><span class="gt-mname">Barrel</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Witch Water (exnihilosequentia:witch_water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__witch_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Witch Water</span><b class="gt-q">1 B</b></span><span class="gt-slot" title="Sand (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Soul Sand (minecraft:soul_sand)"><img class="gt-ico" src="../../assets/icons/minecraft__soul_sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Sand</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:barrel</code></div>
</div>
</div>

## Flow

- [Barrel](#m-b1)
- [Barrel](#m-b2) → [Barrel](#m-b3)

## Tips

- Cobble + witch water = blackstone · red mushroom block + witch water = slime block.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:barrel` | 3 |

## Needs / Feeds

- **Needs:** [Infinite redstone, sulfur &amp; pearls (dust sieve)](../feeders/sieve_dust.md), [Sieve station (manual)](sieve_manual.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
- **Feeds:** [Firebricks &amp; coke oven bricks](bricks.md), [Infinite lead, silver &amp; antimony (blackstone sieve)](../feeders/sieve_blackstone.md)
- **Main source for:** `minecraft:clay_ball`, `minecraft:clay`, `exnihilosequentia:witch_water_bucket`, `minecraft:brick`
