---
kind: chain
id: gravel_steam
order: 710
data:
  t: "Gravel, sand & dust: Steam Forge Hammer"
  inf: true
  "n":
    - [ch, Charcoal, i, "minecraft:charcoal"]
    - [w, Water, f, "minecraft:water_bucket"]
    - [bo, HP Solid Boiler, m, "gtceu:hp_steam_solid_boiler"]
    - [st, Steam, f, "gtceu:steam_bucket"]
    - [sb, Stone Barrel, s, "gtceu:stone_barrel"]
    - [hm, HP Steam Forge Hammer, m, "gtceu:hp_steam_forge_hammer"]
    - [g, Gravel, o, "minecraft:gravel"]
  e: [[ch, bo], [w, bo], [bo, st, "15 mB/t"], [st, hm, "32 mB/t"], [sb, hm, cobble], [hm, g, "0.5 s"]]
  tips:
    - |-
      Steam machines run any recipe up to LV: the same cobble → gravel → sand → dust and blackstone → crushed blackstone as the LV hammer.
    - |-
      High pressure: 0.5 s per block. Low pressure: 1 s. Both cost 320 mB of steam per block.
  b:
    - ["gtceu:hp_steam_solid_boiler", 2]
    - ["gtceu:hp_steam_forge_hammer", 1]
    - ["gtceu:stone_barrel", 1]
    - ["minecraft:lava_bucket", 1]
    - ["pipez:fluid_pipe", 4]
  how:
    - i: ["gtceu:hp_steam_forge_hammer"]
      t: |-
        High Pressure Steam Forge Hammer (bronze hammer + steel plate + tin alloy pipes + wrought iron plates). It runs the 16 EU/t hammer recipes on steam at 2 mB per EU: 32 mB/t while working, 0.5 s per block.
    - i: ["gtceu:hp_steam_solid_boiler", "minecraft:charcoal"]
      t: High Pressure Solid Boilers make 300 mB of steam per second (15 mB/t) when hot. Two keep one hammer running nonstop; feed them charcoal and water.
    - i: ["gtceu:stone_barrel"]
      t: |-
        A Stone Barrel auto-outputs cobble into the hammer (80 per minute; the hammer can do 120). Vent side clear: steam machines stop if their exhaust is blocked.
    - i: ["create:crushing_wheel"]
      t: |-
        Versus crushing wheels: no windmill or SU at all, one block instead of two wheels, and it also makes sand and dust.
---
# Gravel, sand &amp; dust: Steam Forge Hammer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `gravel_steam` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Sieve block (4 sieves)](../../plan/p2.md#sieves)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-bo">
<div class="gt-head"><span class="gt-mname">HP Solid Boiler</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hp_steam_solid_boiler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Steam (gtceu:steam_bucket) - 15 mB/t"><img class="gt-ico" src="../../assets/icons/gtceu__steam_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam</span><b class="gt-q">15 mB/t</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hp_steam_solid_boiler</code></div>
</div>
<div class="gt-panel t-mod" id="m-hm">
<div class="gt-head"><span class="gt-mname">HP Steam Forge Hammer</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Steam (gtceu:steam_bucket) - 32 mB/t"><img class="gt-ico" src="../../assets/icons/gtceu__steam_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam</span><b class="gt-q">32 mB/t</b></span><span class="gt-slot gt-inf" title="Stone Barrel (gtceu:stone_barrel) - cobble"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Barrel</span><span class="gt-tag">infinite</span><b class="gt-q">cobble</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hp_steam_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">0.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Gravel (minecraft:gravel) - 0.5 s"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hp_steam_forge_hammer</code></div>
</div>
</div>

## Flow

- [HP Solid Boiler](#m-bo) → [HP Steam Forge Hammer](#m-hm)

## How to build

1. High Pressure Steam Forge Hammer (bronze hammer + steel plate + tin alloy pipes + wrought iron plates). It runs the 16 EU/t hammer recipes on steam at 2 mB per EU: 32 mB/t while working, 0.5 s per block. — `gtceu:hp_steam_forge_hammer`
2. High Pressure Solid Boilers make 300 mB of steam per second (15 mB/t) when hot. Two keep one hammer running nonstop; feed them charcoal and water. — `gtceu:hp_steam_solid_boiler`, `minecraft:charcoal`
3. A Stone Barrel auto-outputs cobble into the hammer (80 per minute; the hammer can do 120). Vent side clear: steam machines stop if their exhaust is blocked. — `gtceu:stone_barrel`
4. Versus crushing wheels: no windmill or SU at all, one block instead of two wheels, and it also makes sand and dust. — `create:crushing_wheel`

## Tips

- Steam machines run any recipe up to LV: the same cobble → gravel → sand → dust and blackstone → crushed blackstone as the LV hammer.
- High pressure: 0.5 s per block. Low pressure: 1 s. Both cost 320 mB of steam per block.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hp_steam_solid_boiler` | 2 |
| `gtceu:hp_steam_forge_hammer` | 1 |
| `gtceu:stone_barrel` | 1 |
| `minecraft:lava_bucket` | 1 |
| `pipez:fluid_pipe` | 4 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](charcoal.md)
