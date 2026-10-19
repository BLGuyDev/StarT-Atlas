---
kind: chain
id: ingots
order: 890
data:
  t: Ingots, wrought iron, wires and foil from the sieve
  inf: true
  "n":
    - [co, "Crushed ores (gravel sieve)", s, "gtceu:crushed_copper_ore"]
    - [fu, "Furnace / fan blasting", m, "minecraft:furnace"]
    - [ig, "Copper, tin, iron ingots", x, "minecraft:iron_ingot"]
    - [ki, Kiln, m, "gtceu:kiln"]
    - [wi, Wrought iron, o, "gtceu:wrought_iron_ingot"]
    - [wm, "Wiremills (copper, tin)", m, "gtceu:lv_wiremill"]
    - [wr, "Copper & tin wire", o, "gtceu:copper_single_wire"]
    - [be, Bender, m, "gtceu:lv_bender"]
    - [fo, "Plates & copper foil", o, "gtceu:copper_foil"]
  e: [[co, fu, "1 → 1 ingot"], [fu, ig], [ig, ki, iron], [ki, wi, "2 s"], [ig, wm], [wm, wr], [ig, be], [be, fo]]
  tips:
    - Crushed ore smelts straight into 1 ingot in a furnace or by Create fan blasting; the full GT ore line only adds byproducts.
    - |-
      Bender: 1 ingot → 1 plate, or 1 copper → 4 foil on circuit 10 (circuit boards use 4 foil each).
    - One wiremill per metal so nobody changes circuits.
  b: [["gtceu:kiln", 1], ["gtceu:lv_wiremill", 2], ["gtceu:lv_bender", 1], ["functionalstorage:oak_1", 8]]
  how:
    - i: ["gtceu:crushed_copper_ore", "gtceu:crushed_tin_ore", "gtceu:crushed_iron_ore"]
      t: |-
        One drawer per crushed ore after the sieve; a router feeds them to furnaces (or a Create fan through lava): 1 crushed ore = 1 ingot.
    - i: ["gtceu:kiln", "gtceu:wrought_iron_ingot"]
      t: |-
        Iron to the Kiln: wrought iron in 2 s, no fuel. Wrought iron is the steel furnace input and hull plates.
    - i: ["gtceu:lv_wiremill", "gtceu:copper_single_wire", "gtceu:tin_single_wire"]
      t: |-
        Copper and tin each into their own wiremill: 1 ingot → 2 single wires, stocked in drawers.
    - i: ["gtceu:lv_bender", "gtceu:copper_foil"]
      t: |-
        Bender: plates for parts and copper foil (circuit 10) for the LV circuit boards.
---
# Ingots, wrought iron, wires and foil from the sieve

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `ingots` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Smelting: ingots and wrought iron](../../plan/p2.md#ingots)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-fu">
<div class="gt-head"><span class="gt-mname">Furnace / fan blasting</span><span class="gt-badge t-mod">Vanilla</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Crushed ores (gravel sieve) (gtceu:crushed_copper_ore) - 1 → 1 ingot"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_copper_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Copper Ore</span><span class="gt-note">Crushed ores (gravel sieve)</span><span class="gt-tag">infinite</span><b class="gt-q">1 → 1 ingot</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/minecraft__furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Copper, tin, iron ingots (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Copper, tin, iron ingots</span></span></div>
</div>
<div class="gt-foot"><code>minecraft:furnace</code></div>
</div>
<div class="gt-panel t-mod" id="m-ki">
<div class="gt-head"><span class="gt-mname">Kiln</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper, tin, iron ingots (minecraft:iron_ingot) - iron"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Copper, tin, iron ingots</span><b class="gt-q">iron</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__kiln.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Wrought iron (gtceu:wrought_iron_ingot) - 2 s"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:kiln</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">Wiremills (copper, tin)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper, tin, iron ingots (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Copper, tin, iron ingots</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Copper &amp; tin wire (gtceu:copper_single_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Wire</span><span class="gt-note">Copper &amp; tin wire</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper, tin, iron ingots (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Copper, tin, iron ingots</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Plates &amp; copper foil (gtceu:copper_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Foil</span><span class="gt-note">Plates &amp; copper foil</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
</div>

## Flow

- [Furnace / fan blasting](#m-fu) → [Kiln](#m-ki) (also Furnace / fan blasting → [Wiremills (copper, tin)](#m-wm), Furnace / fan blasting → [Bender](#m-be))
- [Wiremills (copper, tin)](#m-wm)
- [Bender](#m-be)

## How to build

1. One drawer per crushed ore after the sieve; a router feeds them to furnaces (or a Create fan through lava): 1 crushed ore = 1 ingot. — `gtceu:crushed_copper_ore`, `gtceu:crushed_tin_ore`, `gtceu:crushed_iron_ore`
2. Iron to the Kiln: wrought iron in 2 s, no fuel. Wrought iron is the steel furnace input and hull plates. — `gtceu:kiln`, `gtceu:wrought_iron_ingot`
3. Copper and tin each into their own wiremill: 1 ingot → 2 single wires, stocked in drawers. — `gtceu:lv_wiremill`, `gtceu:copper_single_wire`, `gtceu:tin_single_wire`
4. Bender: plates for parts and copper foil (circuit 10) for the LV circuit boards. — `gtceu:lv_bender`, `gtceu:copper_foil`

## Tips

- Crushed ore smelts straight into 1 ingot in a furnace or by Create fan blasting; the full GT ore line only adds byproducts.
- Bender: 1 ingot → 1 plate, or 1 copper → 4 foil on circuit 10 (circuit boards use 4 foil each).
- One wiremill per metal so nobody changes circuits.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:kiln` | 1 |
| `gtceu:lv_wiremill` | 2 |
| `gtceu:lv_bender` | 1 |
| `functionalstorage:oak_1` | 8 |

## Needs / Feeds

- **Feeds:** [Alloys: Create heated mixer](../steam/alloys.md), [Steel: Solid Blast Furnace](../steam/steel.md), [Cupronickel coils ×16](coils.md), [LV circuit parts from earlier lines](../feeders/circuit_parts.md), [Steel: Primitive Blast Furnace](../steam/steel_pbf.md), [Steel: Electric Blast Furnace + oxygen](../mv/steel_ebf.md), [Alloys: Steam / LV Alloy Smelter (more per ingot)](../steam/alloys_smelter.md), [Component wall: always a stock of every part (no AE2)](comp_stock.md), [Parts row 1: rods, plates, bolts, gears](comp_parts.md), [Parts row 2: wires, fine wire, cables](comp_wires.md), [LV circuit line (Basic Electronic Circuit)](comp_circuit_lv.md), [Magnets: from magnetite block to Fluxuated Magnetite](magnets.md), [Etching fluid (iron III chloride)](../mv/mv_fecl3.md), [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](../hv/kanthal.md)
- **Main source for:** `minecraft:iron_ingot`, `minecraft:copper_ingot`, `gtceu:tin_ingot`, `gtceu:wrought_iron_ingot`, `gtceu:copper_foil`
