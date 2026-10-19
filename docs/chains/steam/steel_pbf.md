---
kind: chain
id: steel_pbf
order: 730
data:
  t: "Steel: Primitive Blast Furnace"
  "n":
    - [fe, Iron ingot, i, "minecraft:iron_ingot"]
    - [ch, "2 Charcoal", i, "minecraft:charcoal"]
    - [pbf, Primitive Blast Furnace, m, "gtceu:primitive_blast_furnace"]
    - [st, Steel, o, "gtceu:steel_ingot"]
  e: [[fe, pbf], [ch, pbf], [pbf, st, "90 s"]]
  tips:
    - |-
      Only for your first steel: the Solid Blast Furnace needs steel to build and is 5.6× faster.
    - |-
      Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.
  b: [["gtceu:primitive_blast_furnace", 1]]
  how:
    - i: ["gtceu:primitive_blast_furnace", "gtceu:firebricks"]
      t: |-
        32 firebricks + controller (the controller uses wrought iron plates, rods and screws in this pack).
    - i: ["minecraft:iron_ingot", "minecraft:charcoal"]
      t: |-
        1 iron + 2 charcoal → 1 steel every 90 s, no power. A coke gem instead of 2 charcoal: 75 s.
---
# Steel: Primitive Blast Furnace

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `steel_pbf`

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Steel](../../plan/p3.md#steel)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-pbf">
<div class="gt-head"><span class="gt-mname">Primitive Blast Furnace</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron ingot (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span></span><span class="gt-slot" title="2 Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span><span class="gt-note">2 Charcoal</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__primitive_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Steel (gtceu:steel_ingot) - 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:primitive_blast_furnace</code></div>
</div>
</div>

## Flow

- [Primitive Blast Furnace](#m-pbf)

## How to build

1. 32 firebricks + controller (the controller uses wrought iron plates, rods and screws in this pack). — `gtceu:primitive_blast_furnace`, `gtceu:firebricks`
2. 1 iron + 2 charcoal → 1 steel every 90 s, no power. A coke gem instead of 2 charcoal: 75 s. — `minecraft:iron_ingot`, `minecraft:charcoal`

## Tips

- Only for your first steel: the Solid Blast Furnace needs steel to build and is 5.6× faster.
- Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:primitive_blast_furnace` | 1 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md), [Charcoal &amp; creosote: Coke Oven](charcoal.md)
