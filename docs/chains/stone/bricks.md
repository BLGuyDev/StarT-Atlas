---
kind: chain
id: bricks
order: 40
data:
  t: Firebricks & coke oven bricks
  "n":
    - [cl, Clay Ball, i, "minecraft:clay_ball"]
    - [br, "Brick (smelted clay)", i, "minecraft:brick"]
    - [cd, Clay Dust, x, "gtceu:clay_dust"]
    - [bd, Brick Dust, x, "gtceu:brick_dust"]
    - [fd, Fireclay Dust, x, "gtceu:fireclay_dust"]
    - [fm, Brick Form, m, "gtceu:brick_wooden_form"]
    - [cf, Compressed Fireclay, x, "gtceu:compressed_fireclay"]
    - [fu, Furnace, m, "minecraft:furnace"]
    - [fb, Firebrick, o, "gtceu:firebrick"]
    - [sa, Sand, i, "minecraft:sand"]
    - [cc, Compressed Coke Clay, x, "gtceu:compressed_coke_clay"]
    - [cob, Coke Oven Brick, o, "gtceu:coke_oven_brick"]
  e:
    - [cl, cd, mortar]
    - [br, bd, mortar]
    - [cd, fd]
    - [bd, fd]
    - [fd, fm, "8"]
    - [fm, cf, "8"]
    - [cf, fu]
    - [fu, fb]
    - [cl, cc]
    - [sa, cc]
    - [cc, fu]
    - [fu, cob]
  tips:
    - "Create press: fireclay dust → compressed fireclay 1:1."
    - PBF 32 firebricks · POF 64 · Coke Oven 25 coke bricks.
  b: [["gtceu:brick_wooden_form", 1], ["minecraft:furnace", 2]]
---
# Firebricks &amp; coke oven bricks

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `bricks`

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Firebricks and coke oven bricks](../../plan/p0.md#bricks)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-fm">
<div class="gt-head"><span class="gt-mname">Brick Form</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Fireclay Dust (gtceu:fireclay_dust) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__fireclay_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fireclay Dust</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__brick_wooden_form.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Compressed Fireclay (gtceu:compressed_fireclay) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__compressed_fireclay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Compressed Fireclay</span><b class="gt-q">8</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:brick_wooden_form</code></div>
</div>
<div class="gt-panel t-mod" id="m-fu">
<div class="gt-head"><span class="gt-mname">Furnace</span><span class="gt-badge t-mod">Vanilla</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Compressed Fireclay (gtceu:compressed_fireclay)"><img class="gt-ico" src="../../assets/icons/gtceu__compressed_fireclay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Compressed Fireclay</span></span><span class="gt-slot" title="Compressed Coke Clay (gtceu:compressed_coke_clay)"><img class="gt-ico" src="../../assets/icons/gtceu__compressed_coke_clay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Compressed Coke Clay</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/minecraft__furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Firebrick (gtceu:firebrick)"><img class="gt-ico" src="../../assets/icons/gtceu__firebrick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Firebrick</span></span><span class="gt-slot gt-outp" title="Coke Oven Brick (gtceu:coke_oven_brick)"><img class="gt-ico" src="../../assets/icons/gtceu__coke_oven_brick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Coke Oven Brick</span></span></div>
</div>
<div class="gt-foot"><code>minecraft:furnace</code></div>
</div>
</div>

## Flow

- [Brick Form](#m-fm) → [Furnace](#m-fu)

### Direct steps

- Clay Ball → Clay Dust (mortar)
- Brick (smelted clay) → Brick Dust (mortar)
- Clay Dust → Fireclay Dust
- Brick Dust → Fireclay Dust
- Clay Ball → Compressed Coke Clay
- Sand → Compressed Coke Clay

## Tips

- Create press: fireclay dust → compressed fireclay 1:1.
- PBF 32 firebricks · POF 64 · Coke Oven 25 coke bricks.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:brick_wooden_form` | 1 |
| `minecraft:furnace` | 2 |

## Needs / Feeds

- **Needs:** [Barrel transformations](barrel.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
