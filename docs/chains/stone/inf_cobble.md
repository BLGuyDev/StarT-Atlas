---
kind: chain
id: inf_cobble
order: 20
data:
  t: Infinite cobble & blackstone
  inf: true
  "n":
    - [w, Water, f, "minecraft:water_bucket"]
    - [ww, Witch Water, f, "exnihilosequentia:witch_water_bucket"]
    - [lav, "Lava (kept)", s, "minecraft:lava_bucket"]
    - [sb1, "Stone Barrel · circ 0", m, "gtceu:stone_barrel"]
    - [sb2, "Stone Barrel · circ 0", m, "gtceu:stone_barrel"]
    - [c, Cobblestone, o, "minecraft:cobblestone"]
    - [b, Blackstone, o, "minecraft:blackstone"]
  e: [[w, sb1, "1 B"], [lav, sb1, not used], [sb1, c, "0.75 s"], [ww, sb2, "1 B"], [lav, sb2], [sb2, b, "0.75 s"]]
  tips:
    - Circuit 10, lava in + water inside = obsidian.
    - Glass + lava = tempered glass.
    - Large Stone Barrel does all of this much faster.
  store: ["functionalstorage:oak_1"]
  b:
    - ["gtceu:stone_barrel", 2]
    - ["minecraft:lava_bucket", 2]
    - ["pipez:fluid_pipe", 4]
    - ["functionalstorage:oak_1", 2]
  how:
    - i: ["gtceu:stone_barrel"]
      t: "Craft a Stone Barrel: stone, stone slabs and a bucket."
    - i: ["minecraft:lava_bucket"]
      t: Put one lava bucket into its fluid slot. It is a catalyst and never runs out.
    - i: ["thermal:device_water_gen", "pipez:fluid_pipe"]
      t: Pipe water in (1 B per craft); the Aqueous Accumulator keeps up with two barrels.
    - i: ["minecraft:cobblestone"]
      t: |-
        Ghost circuit 0: 1 cobble every 15 ticks (80/min per barrel). Witch water instead of water gives blackstone; circuit 10 with lava flowing in + water inside gives obsidian.
    - i: ["functionalstorage:oak_1"]
      t: Enable auto-output into a drawer (or hopper) so the barrel never fills.
---
# Infinite cobble &amp; blackstone

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `inf_cobble` · **Tags:** Infinite source

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Cobblestone and blackstone](../../plan/p0.md#cobble)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-sb1">
<div class="gt-head"><span class="gt-mname">Stone Barrel · circ 0</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-inf" title="Lava (kept) (minecraft:lava_bucket) - not used"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><span class="gt-note">Lava (kept)</span><span class="gt-tag">infinite</span><b class="gt-q">not used</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">0.75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Cobblestone (minecraft:cobblestone) - 0.75 s"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
<div class="gt-panel t-mod" id="m-sb2">
<div class="gt-head"><span class="gt-mname">Stone Barrel · circ 0</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Witch Water (exnihilosequentia:witch_water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__witch_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Witch Water</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-inf" title="Lava (kept) (minecraft:lava_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><span class="gt-note">Lava (kept)</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">0.75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Blackstone (minecraft:blackstone) - 0.75 s"><img class="gt-ico" src="../../assets/icons/minecraft__blackstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blackstone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
</div>

## Flow

- [Stone Barrel · circ 0](#m-sb1)
- [Stone Barrel · circ 0](#m-sb2)

## How to build

1. Craft a Stone Barrel: stone, stone slabs and a bucket. — `gtceu:stone_barrel`
2. Put one lava bucket into its fluid slot. It is a catalyst and never runs out. — `minecraft:lava_bucket`
3. Pipe water in (1 B per craft); the Aqueous Accumulator keeps up with two barrels. — `thermal:device_water_gen`, `pipez:fluid_pipe`
4. Ghost circuit 0: 1 cobble every 15 ticks (80/min per barrel). Witch water instead of water gives blackstone; circuit 10 with lava flowing in + water inside gives obsidian. — `minecraft:cobblestone`
5. Enable auto-output into a drawer (or hopper) so the barrel never fills. — `functionalstorage:oak_1`

## Tips

- Circuit 10, lava in + water inside = obsidian.
- Glass + lava = tempered glass.
- Large Stone Barrel does all of this much faster.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:stone_barrel` | 2 |
| `minecraft:lava_bucket` | 2 |
| `pipez:fluid_pipe` | 4 |
| `functionalstorage:oak_1` | 2 |

## Storage

`functionalstorage:oak_1`

## Needs / Feeds

- **Needs:** [Infinite lava, obsidian &amp; pebbles](inf_lava.md)
- **Feeds:** [Drilling fluid](../lv/drilling.md), [Sieve station (manual)](sieve_manual.md), [Infinite lava, obsidian &amp; pebbles](inf_lava.md), [Molten Ore Mixture](../ev/molten_mix.md), [Gravel, sand &amp; dust: Forge Hammers](../feeders/gravel_hammer.md), [Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer](../ev/titanium_line.md)
- **Main source for:** `minecraft:cobblestone`, `gtceu:stone_dust`, `minecraft:blackstone`
