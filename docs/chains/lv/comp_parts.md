---
kind: chain
id: comp_parts
order: 780
data:
  t: "Parts row 1: rods, plates, bolts, gears"
  inf: true
  "n":
    - [fe, Iron, i, "minecraft:iron_ingot"]
    - [st, Steel, i, "gtceu:steel_ingot"]
    - [l1, "Lathe (iron)", m, "gtceu:lv_lathe"]
    - [l2, "Lathe (steel)", m, "gtceu:lv_lathe"]
    - [be, Bender, m, "gtceu:lv_bender"]
    - [al, "Alloy Smelter · mold", m, "gtceu:lv_alloy_smelter"]
    - [po, Polarizer, m, "gtceu:lv_polarizer"]
    - [cu, Cutter, m, "gtceu:lv_cutter"]
    - - dr
      - Parts drawers
      - g
      - functionalstorage:oak_1
      - - [Iron rods, "gtceu:iron_rod", "1 → 2"]
        - [Magnetic iron rods, "gtceu:magnetic_iron_rod"]
        - [Steel rods, "gtceu:steel_rod", "1 → 2"]
        - [Steel bolts, "gtceu:steel_bolt", "rod → 4"]
        - [Steel plates, "gtceu:steel_plate", "1 → 1"]
        - [Small steel gear, "gtceu:small_steel_gear", "2 → 1"]
  e:
    - [fe, l1]
    - [st, l2]
    - [st, be]
    - [st, al]
    - [l1, po]
    - [l2, cu]
    - [l1, dr]
    - [po, dr]
    - [l2, dr]
    - [cu, dr]
    - [be, dr]
    - [al, dr]
  tips:
    - |-
      Two lathes (one per metal) so neither ever switches recipe. Lathe: 1 ingot → 2 rods (harder rods are off in this pack).
    - Each machine pushes into its own drawer through a Robot Arm cover on Keep Exact.
  b:
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:lv_polarizer", 1]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_cutter", 1]
    - ["gtceu:lv_alloy_smelter", 1]
    - ["gtceu:small_gear_casting_mold", 1]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["functionalstorage:oak_1", 6]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:lv_lathe", "gtceu:iron_rod", "gtceu:steel_rod"]
      t: |-
        Lathe A on iron: 1 iron → 2 iron rods. Lathe B on steel: 1 steel → 2 steel rods. Both 16 EU/t.
    - i: ["gtceu:lv_polarizer", "gtceu:magnetic_iron_rod"]
      t: Polarizer takes iron rods from lathe A and makes magnetic iron rods (one per motor).
    - i: ["gtceu:lv_cutter", "gtceu:steel_bolt"]
      t: |-
        Cutter takes steel rods from lathe B: 1 rod → 4 steel bolts (vacuum tubes).
    - i: ["gtceu:lv_bender", "gtceu:steel_plate"]
      t: "Bender: 1 steel → 1 steel plate at 24 EU/t (pistons use 3)."
    - i: ["gtceu:lv_alloy_smelter", "gtceu:small_gear_casting_mold", "gtceu:small_steel_gear"]
      t: |-
        Alloy smelter with a small gear casting mold (empty mold + hammer): 2 steel → 1 small steel gear (pistons).
---
# Parts row 1: rods, plates, bolts, gears

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_parts` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Metal parts](../../plan/p4.md#parts)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-l1">
<div class="gt-head"><span class="gt-mname">Lathe (iron)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-po" title="Polarizer (gtceu:lv_polarizer)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Polarizer</span></a><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-lv" id="m-l2">
<div class="gt-head"><span class="gt-mname">Lathe (steel)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Steel (gtceu:steel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cu" title="Cutter (gtceu:lv_cutter)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Cutter</span></a><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Steel (gtceu:steel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-al">
<div class="gt-head"><span class="gt-mname">Alloy Smelter · mold</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Steel (gtceu:steel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_alloy_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_alloy_smelter</code></div>
</div>
<div class="gt-panel t-lv" id="m-po">
<div class="gt-head"><span class="gt-mname">Polarizer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-l1" title="Lathe (iron) (gtceu:lv_lathe)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Lathe</span><span class="gt-note">Lathe (iron)</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_polarizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-cu">
<div class="gt-head"><span class="gt-mname">Cutter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-l2" title="Lathe (steel) (gtceu:lv_lathe)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Lathe</span><span class="gt-note">Lathe (steel)</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Iron rods <i>1 → 2</i></span><span>Magnetic iron rods</span><span>Steel rods <i>1 → 2</i></span><span>Steel bolts <i>rod → 4</i></span><span>Steel plates <i>1 → 1</i></span><span>Small steel gear <i>2 → 1</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_cutter</code></div>
</div>
</div>

## Flow

- [Lathe (iron)](#m-l1) → [Polarizer](#m-po)
- [Lathe (steel)](#m-l2) → [Cutter](#m-cu)
- [Bender](#m-be)
- [Alloy Smelter · mold](#m-al)

## How to build

1. Lathe A on iron: 1 iron → 2 iron rods. Lathe B on steel: 1 steel → 2 steel rods. Both 16 EU/t. — `gtceu:lv_lathe`, `gtceu:iron_rod`, `gtceu:steel_rod`
2. Polarizer takes iron rods from lathe A and makes magnetic iron rods (one per motor). — `gtceu:lv_polarizer`, `gtceu:magnetic_iron_rod`
3. Cutter takes steel rods from lathe B: 1 rod → 4 steel bolts (vacuum tubes). — `gtceu:lv_cutter`, `gtceu:steel_bolt`
4. Bender: 1 steel → 1 steel plate at 24 EU/t (pistons use 3). — `gtceu:lv_bender`, `gtceu:steel_plate`
5. Alloy smelter with a small gear casting mold (empty mold + hammer): 2 steel → 1 small steel gear (pistons). — `gtceu:lv_alloy_smelter`, `gtceu:small_gear_casting_mold`, `gtceu:small_steel_gear`

## Tips

- Two lathes (one per metal) so neither ever switches recipe. Lathe: 1 ingot → 2 rods (harder rods are off in this pack).
- Each machine pushes into its own drawer through a Robot Arm cover on Keep Exact.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_lathe` | 2 |
| `gtceu:lv_polarizer` | 1 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_cutter` | 1 |
| `gtceu:lv_alloy_smelter` | 1 |
| `gtceu:small_gear_casting_mold` | 1 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `functionalstorage:oak_1` | 6 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md), [Steel: Solid Blast Furnace](../steam/steel.md)
- **Feeds:** [LV Electric Motor line](comp_motor.md), [LV Electric Piston line](comp_piston.md), [LV Robot Arm line](comp_robot_arm.md), [LV circuit line (Basic Electronic Circuit)](comp_circuit_lv.md), [LV hull line (Create mechanical crafters)](lv_hull_line.md), [MV components on LV machines](../mv/comp_mv.md)
- **Main source for:** `gtceu:iron_rod`, `gtceu:magnetic_iron_rod`, `gtceu:steel_plate`, `gtceu:steel_rod`, `gtceu:steel_bolt`, `gtceu:small_steel_gear`
