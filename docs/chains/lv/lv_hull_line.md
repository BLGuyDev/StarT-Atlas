---
kind: chain
id: lv_hull_line
order: 920
data:
  t: LV hull line (Create mechanical crafters)
  inf: true
  "n":
    - [pl, "8 Steel plates", i, "gtceu:steel_plate"]
    - [as, "Assembler · circuit 8", m, "gtceu:lv_assembler"]
    - [ca, LV Machine Casing, x, "gtceu:lv_machine_casing"]
    - [hp, "2 Wrought iron plates", i, "gtceu:wrought_iron_plate"]
    - [pp, "1 Steel plate", i, "gtceu:steel_plate"]
    - [cb, "2 Tin cables", i, "gtceu:tin_single_cable"]
    - [mc, "Mechanical Crafters 3×2", m, "create:mechanical_crafter"]
    - [hu, LV Machine Hull, o, "gtceu:lv_machine_hull"]
  e: [[pl, as], [as, ca, "2.5 s"], [ca, mc], [hp, mc], [pp, mc], [cb, mc], [mc, hu]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["create:mechanical_crafter", 6]
    - ["modularrouters:modular_router", 2]
    - ["functionalstorage:oak_1", 5]
  tips:
    - |-
      Hull layout (2 rows): wrought iron plate, steel plate, wrought iron plate / tin cable, LV casing, tin cable.
    - |-
      Every GT machine, transformer, bus and hatch starts from a hull: keep 16 in stock.
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_machine_casing"]
      t: |-
        Assembler on circuit 8: 8 steel plates → 1 LV Machine Casing in 2.5 s (16 EU/t), no wrench needed.
    - i: ["create:mechanical_crafter"]
      t: Six Create Mechanical Crafters in a 3×2 grid facing the same way, rotation from the steam engine shaft. Routers put the six parts into the matching crafters; the hull drops out of the last crafter.
    - i: ["gtceu:lv_machine_hull", "gtceu:lv_robot_arm"]
      t: Output into a drawer with a cap (robot arm on Keep Exact 16, or a small drawer).
  s3d:
    b:
      - ["functionalstorage:oak_1", 0, 0, 1, 1, 1, 1, Steel plate drawer]
      - ["gtceu:lv_assembler", 2, 0, 1, 1, 1, 1, "LV Assembler · circuit 8 · 8 plates → LV casing"]
      - ["modularrouters:modular_router", 7, 0, 1, 1, 1, 1, "Modular Router (casing → feed drawer)"]
      - ["functionalstorage:oak_1", 9, 1, 0, 1, 1, 1, "Feed drawer · Wrought iron plate"]
      - ["functionalstorage:oak_1", 9, 1, 1, 1, 1, 1, "Feed drawer · Steel plate"]
      - ["functionalstorage:oak_1", 9, 1, 2, 1, 1, 1, "Feed drawer · Wrought iron plate"]
      - ["functionalstorage:oak_1", 9, 0, 0, 1, 1, 1, "Feed drawer · Tin cable"]
      - ["functionalstorage:oak_1", 9, 0, 1, 1, 1, 1, "Feed drawer · LV Machine Casing"]
      - ["functionalstorage:oak_1", 9, 0, 2, 1, 1, 1, "Feed drawer · Tin cable"]
      - ["create:mechanical_crafter", 12, 0, 0, 1, 2, 3, "Mechanical Crafter (3×2 grid, hull recipe)"]
      - ["create:shaft", 12, 2, 0, 1, 1, 3, "Shaft (steam engine rotation)"]
      - ["functionalstorage:oak_1", 14, 0, 2, 1, 1, 1, LV Machine Hull drawer]
      - ["gtceu:lv_robot_arm", 15, 0, 2, 1, 1, 1, "Robot Arm cover · Keep Exact 16"]
    p:
      - [i, [1, 0.5, 1.5], [2, 0.5, 1.5]]
      - [i, [3, 0.5, 1.5], [7, 0.5, 1.5]]
      - [i, [8, 0.5, 1.5], [9, 0.5, 1.5]]
      - [i, [10, 1.5, 0.5], [12, 1.5, 0.5]]
      - [i, [10, 1.5, 1.5], [12, 1.5, 1.5]]
      - [i, [10, 1.5, 2.5], [12, 1.5, 2.5]]
      - [i, [10, 0.5, 0.5], [12, 0.5, 0.5]]
      - [i, [10, 0.5, 1.5], [12, 0.5, 1.5]]
      - [i, [10, 0.5, 2.5], [12, 0.5, 2.5]]
      - [i, [13, 0.5, 2.5], [14, 0.5, 2.5]]
      - [r, [12.5, 2.5, 3], [12.5, 2.5, 6.5]]
    l:
      - [Steel plates, 0, 1.9, 1.5]
      - ["Assembler · circuit 8 · 2.5 s · 16 EU/t", 2.5, 2.4, 1.5]
      - ["Router → feed", 7.5, 1.9, 1.5]
      - ["6 feed drawers", 9.5, 3.6, 1.5]
      - ["6 Mechanical Crafters 3×2", 12.5, 4.4, 1.5]
      - ["Top row: 3 plates", 12.5, 6.2, 1.5]
      - ["Bottom row: cable + casing", 12.5, 8, 1.5]
      - [LV hull stock 16, 14.5, 1.9, 2.5]
      - [Shaft from the steam engine line, 12.5, 3.3, 6.5]
---
# LV hull line (Create mechanical crafters)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `lv_hull_line` · **Tags:** Infinite source, 3D scene

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV hulls](../../plan/p4.md#lvhull)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · circuit 8</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Steel plates (gtceu:steel_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Plate</span><span class="gt-note">8 Steel plates</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LV Machine Casing (gtceu:lv_machine_casing) - 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__lv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Machine Casing</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Mechanical Crafters 3×2</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LV Machine Casing (gtceu:lv_machine_casing)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Machine Casing</span></span><span class="gt-slot" title="2 Wrought iron plates (gtceu:wrought_iron_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Plate</span><span class="gt-note">2 Wrought iron plates</span></span><span class="gt-slot" title="1 Steel plate (gtceu:steel_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Plate</span><span class="gt-note">1 Steel plate</span></span><span class="gt-slot" title="2 Tin cables (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">2 Tin cables</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_crafter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Machine Hull (gtceu:lv_machine_hull)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Machine Hull</span></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_crafter</code></div>
</div>
</div>

## Flow

- [Assembler · circuit 8](#m-as) → [Mechanical Crafters 3×2](#m-mc)

## How to build

1. Assembler on circuit 8: 8 steel plates → 1 LV Machine Casing in 2.5 s (16 EU/t), no wrench needed. — `gtceu:lv_assembler`, `gtceu:lv_machine_casing`
2. Six Create Mechanical Crafters in a 3×2 grid facing the same way, rotation from the steam engine shaft. Routers put the six parts into the matching crafters; the hull drops out of the last crafter. — `create:mechanical_crafter`
3. Output into a drawer with a cap (robot arm on Keep Exact 16, or a small drawer). — `gtceu:lv_machine_hull`, `gtceu:lv_robot_arm`

## Tips

- Hull layout (2 rows): wrought iron plate, steel plate, wrought iron plate / tin cable, LV casing, tin cable.
- Every GT machine, transformer, bus and hatch starts from a hull: keep 16 in stock.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `create:mechanical_crafter` | 6 |
| `modularrouters:modular_router` | 2 |
| `functionalstorage:oak_1` | 5 |

## Needs / Feeds

- **Needs:** [Parts row 1: rods, plates, bolts, gears](comp_parts.md), [Parts row 2: wires, fine wire, cables](comp_wires.md)
- **Feeds:** [First MV hull and the LV → MV transformer](../mv/mv_hull.md)
- **Main source for:** `gtceu:lv_machine_hull`

## Extras

- 3D assembly scene with 13 blocks (open it in the Atlas page).
