---
kind: chain
id: inf_lava
order: 520
data:
  t: Infinite lava, obsidian & pebbles
  inf: true
  "n":
    - [c, Cobblestone, s, "minecraft:cobblestone"]
    - [sc, "Soul Campfire (kept)", i, "minecraft:soul_campfire"]
    - [lsb, Large Stone Barrel, m, "gtceu:large_stone_barrel"]
    - [lv, Lava, o, "minecraft:lava_bucket"]
    - [lsb2, Large Stone Barrel, m, "gtceu:large_stone_barrel"]
    - [ob, Obsidian, o, "minecraft:obsidian"]
    - [pb, Pebbles, o, "exnihilosequentia:stone_pebble"]
  e:
    - [c, lsb, "1"]
    - [sc, lsb]
    - [lsb, lv, "500 mB · 10 s"]
    - [lv, lsb2, water kept]
    - [lsb2, ob, "1 B → 1"]
    - [lsb2, pb, pebble kept]
  tips:
    - |-
      Before the multi: Fired Crucible over a campfire melts cobble.
    - Obsidian mode keeps 1 obsidian + water inside; pebble mode keeps 1 pebble + lava + water.
  b: [["gtceu:large_stone_barrel", 1], ["minecraft:soul_campfire", 1], ["gtceu:stone_barrel", 1]]
  how:
    - i: ["gtceu:large_stone_barrel"]
      t: |-
        Large Stone Barrel: 23 stone + 9 stone bricks + controller (see render).
    - i: ["minecraft:soul_campfire", "minecraft:cobblestone"]
      t: Soul Campfire in an input bus (kept) + cobble from the stone barrels → 500 mB lava every 10 s per cobble.
    - i: ["gtceu:lv_output_hatch"]
      t: Output hatch → fluid pipe → wherever lava is needed (stone barrels, LCR netherrack recipe, fuel).
    - i: ["minecraft:obsidian", "exnihilosequentia:stone_pebble"]
      t: |-
        Other modes: 1 obsidian + water kept inside turns 1 B lava into obsidian; 1 pebble + lava + water kept → pebbles of that stone.
---
# Infinite lava, obsidian &amp; pebbles

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `inf_lava` · **Tags:** Infinite source

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Lava and obsidian](../../plan/p2.md#lava)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lsb">
<div class="gt-head"><span class="gt-mname">Large Stone Barrel</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Cobblestone (minecraft:cobblestone) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><span class="gt-tag">infinite</span><b class="gt-q">1</b></span><span class="gt-slot" title="Soul Campfire (kept) (minecraft:soul_campfire)"><img class="gt-ico" src="../../assets/icons/minecraft__soul_campfire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Campfire</span><span class="gt-note">Soul Campfire (kept)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Lava (minecraft:lava_bucket) - 500 mB · 10 s"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><b class="gt-q">500 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_stone_barrel</code></div>
</div>
<div class="gt-panel t-multi" id="m-lsb2">
<div class="gt-head"><span class="gt-mname">Large Stone Barrel</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="Lava (minecraft:lava_bucket) - water kept"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><b class="gt-q">water kept</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Obsidian (minecraft:obsidian) - 1 B → 1"><img class="gt-ico" src="../../assets/icons/minecraft__obsidian.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Obsidian</span><b class="gt-q">1 B → 1</b></span><span class="gt-slot gt-outp" title="Pebbles (exnihilosequentia:stone_pebble) - pebble kept"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__stone_pebble.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Pebble</span><span class="gt-note">Pebbles</span><b class="gt-q">pebble kept</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_stone_barrel</code></div>
</div>
</div>

## Flow

- [Large Stone Barrel](#m-lsb) → [Large Stone Barrel](#m-lsb2)

## How to build

1. Large Stone Barrel: 23 stone + 9 stone bricks + controller (see render). — `gtceu:large_stone_barrel`
2. Soul Campfire in an input bus (kept) + cobble from the stone barrels → 500 mB lava every 10 s per cobble. — `minecraft:soul_campfire`, `minecraft:cobblestone`
3. Output hatch → fluid pipe → wherever lava is needed (stone barrels, LCR netherrack recipe, fuel). — `gtceu:lv_output_hatch`
4. Other modes: 1 obsidian + water kept inside turns 1 B lava into obsidian; 1 pebble + lava + water kept → pebbles of that stone. — `minecraft:obsidian`, `exnihilosequentia:stone_pebble`

## Tips

- Before the multi: Fired Crucible over a campfire melts cobble.
- Obsidian mode keeps 1 obsidian + water inside; pebble mode keeps 1 pebble + lava + water.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_stone_barrel` | 1 |
| `minecraft:soul_campfire` | 1 |
| `gtceu:stone_barrel` | 1 |

## Needs / Feeds

- **Needs:** [Infinite cobble &amp; blackstone](inf_cobble.md)
- **Feeds:** [Infinite cobble &amp; blackstone](inf_cobble.md), [Radon](../ev/radon.md), [Charcoal: Create fan smelting](../steam/charcoal_fan.md), [Cobble: Rock Breaker (LV)](../feeders/cobble_rb.md), [Cobble: Create drill generator](../feeders/cobble_drill.md)
- **Main source for:** `minecraft:lava_bucket`, `minecraft:end_stone`
