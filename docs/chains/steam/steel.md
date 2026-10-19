---
kind: chain
id: steel
order: 80
data:
  t: "Steel: Solid Blast Furnace"
  inf: true
  "n":
    - [fe, Iron, i, "minecraft:iron_ingot"]
    - [cf, "Kiln / Campfire", m, "gtceu:kiln"]
    - [wi, Wrought Iron, x, "gtceu:wrought_iron_ingot"]
    - [ch, Charcoal, x, "minecraft:charcoal"]
    - [sbf, Solid Blast Furnace, m, "gtceu:solid_blast_furnace"]
    - [st, Steel, o, "gtceu:steel_ingot"]
  e: [[fe, cf], [cf, wi], [wi, sbf, "1"], [ch, sbf, "2"], [sbf, st, "16 s"]]
  tips:
    - |-
      Wrought iron is 2.25× faster than plain iron (16 s vs 36 s). Coke: 1 coke instead of 2 charcoal and 12 s.
    - |-
      Block mode: 1 wrought iron block + 2 charcoal blocks → 1 steel block in 144 s, the same speed with 9× fewer items to move.
    - One furnace makes 3.75 steel and burns 7.5 charcoal per minute.
    - |-
      Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.
  store: ["functionalstorage:oak_1"]
  b: [["gtceu:solid_blast_furnace", 1], ["gtceu:kiln", 1], ["pipez:item_pipe", 4]]
  how:
    - i: ["gtceu:kiln", "minecraft:iron_ingot", "gtceu:wrought_iron_ingot"]
      t: |-
        Kiln (mud bricks, stripped jungle wood, a campfire): iron → wrought iron in 2 s, no fuel. A plain campfire takes 20 s.
    - i: ["gtceu:solid_blast_furnace", "kubejs:high_steam_machine_casing", "gtceu:steel_firebox_casing"]
      t: |-
        Solid Blast Furnace: 23 high pressure steam casings (min 15) + 9 steel firebox casings + controller (steel rods, screws and plate). The first steel comes from the Primitive Blast Furnace.
    - i: ["gtceu:wrought_iron_ingot", "minecraft:charcoal"]
      t: |-
        Input bus: wrought iron + charcoal 1:2 → steel every 16 s, no power. Feed it from the kiln and the charcoal drawer with Pipez item pipes.
    - i: ["gtceu:coke_gem"]
      t: |-
        Coke (coal from the Void Extractor in a coke oven) is better fuel: 1 per steel and 12 s.
    - i: ["gtceu:steel_block"]
      t: |-
        For bulk, compress wrought iron and charcoal into blocks: 144 s per steel block, nine times fewer transfers.
---
# Steel: Solid Blast Furnace

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `steel` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Steel](../../plan/p3.md#steel)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cf">
<div class="gt-head"><span class="gt-mname">Kiln / Campfire</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__kiln.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Wrought Iron (gtceu:wrought_iron_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:kiln</code></div>
</div>
<div class="gt-panel t-mod" id="m-sbf">
<div class="gt-head"><span class="gt-mname">Solid Blast Furnace</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wrought Iron (gtceu:wrought_iron_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Ingot</span><b class="gt-q">1</b></span><span class="gt-slot" title="Charcoal (minecraft:charcoal) - 2"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__solid_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Steel (gtceu:steel_ingot) - 16 s"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:solid_blast_furnace</code></div>
</div>
</div>

## Flow

- [Kiln / Campfire](#m-cf) → [Solid Blast Furnace](#m-sbf)

## How to build

1. Kiln (mud bricks, stripped jungle wood, a campfire): iron → wrought iron in 2 s, no fuel. A plain campfire takes 20 s. — `gtceu:kiln`, `minecraft:iron_ingot`, `gtceu:wrought_iron_ingot`
2. Solid Blast Furnace: 23 high pressure steam casings (min 15) + 9 steel firebox casings + controller (steel rods, screws and plate). The first steel comes from the Primitive Blast Furnace. — `gtceu:solid_blast_furnace`, `kubejs:high_steam_machine_casing`, `gtceu:steel_firebox_casing`
3. Input bus: wrought iron + charcoal 1:2 → steel every 16 s, no power. Feed it from the kiln and the charcoal drawer with Pipez item pipes. — `gtceu:wrought_iron_ingot`, `minecraft:charcoal`
4. Coke (coal from the Void Extractor in a coke oven) is better fuel: 1 per steel and 12 s. — `gtceu:coke_gem`
5. For bulk, compress wrought iron and charcoal into blocks: 144 s per steel block, nine times fewer transfers. — `gtceu:steel_block`

## Tips

- Wrought iron is 2.25× faster than plain iron (16 s vs 36 s). Coke: 1 coke instead of 2 charcoal and 12 s.
- Block mode: 1 wrought iron block + 2 charcoal blocks → 1 steel block in 144 s, the same speed with 9× fewer items to move.
- One furnace makes 3.75 steel and burns 7.5 charcoal per minute.
- Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:solid_blast_furnace` | 1 |
| `gtceu:kiln` | 1 |
| `pipez:item_pipe` | 4 |

## Storage

`functionalstorage:oak_1`

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md)
- **Feeds:** [LV circuit parts from earlier lines](../feeders/circuit_parts.md), [Parts row 1: rods, plates, bolts, gears](../lv/comp_parts.md)
- **Main source for:** `gtceu:steel_ingot`
