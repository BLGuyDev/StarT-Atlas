---
kind: chain
id: comp_motor
order: 800
data:
  t: LV Electric Motor line
  inf: true
  "n":
    - [c, "2 Tin cable", i, "gtceu:tin_single_cable"]
    - [r, "2 Iron rods", i, "gtceu:iron_rod"]
    - [m, "1 Magnetic iron rod", i, "gtceu:magnetic_iron_rod"]
    - [w, "4 Copper wire", i, "gtceu:copper_single_wire"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [out, LV Electric Motor, o, "gtceu:lv_electric_motor"]
  e: [[c, as], [r, as], [m, as], [w, as], [as, out, "12 / min"]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["functionalstorage:oak_1", 1]
    - ["pipez:item_pipe", 8]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_electric_motor"]
      t: |-
        Assembler: 2 tin cables + 2 iron rods + 1 magnetic iron rod + 4 copper wires → 1 motor in 5 s at 30 EU/t (12 per minute). The iron version is as good as the steel one and needs no steel.
    - i: ["minecraft:iron_ingot", "minecraft:copper_ingot", "gtceu:tin_ingot"]
      t: |-
        Raw cost per motor: 1.5 iron, 2 copper, 1 tin and 288 mB liquid rubber (1.5 rubber). The gravel sieve alone gives 24 of each ore per minute.
    - i: ["gtceu:lv_robot_arm"]
      t: |-
        Keep 64 motors: every other component line pulls from this drawer.
  tips:
    - |-
      Motors are inside every other part: pistons (1), conveyors (2), pumps (1), robot arms (2). Make this line first and biggest.
  s3d:
    b:
      - ["functionalstorage:oak_1", 0, 0, 0, 1, 1, 1, "Input drawer · 2 Tin cable"]
      - ["functionalstorage:oak_1", 1, 0, 0, 1, 1, 1, "Input drawer · 2 Iron rod"]
      - ["functionalstorage:oak_1", 2, 0, 0, 1, 1, 1, "Input drawer · 1 Magnetic rod"]
      - ["functionalstorage:oak_1", 3, 0, 0, 1, 1, 1, "Input drawer · 4 Copper wire"]
      - ["gtceu:lv_assembler", 2, 0, 2, 1, 1, 1, "LV Assembler · LV Electric Motor"]
      - ["gtceu:lv_robot_arm", 2, 0, 3, 1, 1, 1, "Robot Arm cover · Keep Exact + Item Filter"]
      - ["functionalstorage:oak_1", 2, 0, 4, 1, 1, 1, "Stock drawer · LV Electric Motor"]
      - ["functionalstorage:oak_1", 7, 0, 0, 1, 1, 1, "Input drawer · 1 Motor"]
      - ["functionalstorage:oak_1", 8, 0, 0, 1, 1, 1, "Input drawer · 3 Steel plate"]
      - ["functionalstorage:oak_1", 9, 0, 0, 1, 1, 1, "Input drawer · 2 Steel rod"]
      - ["functionalstorage:oak_1", 10, 0, 0, 1, 1, 1, "Input drawer · 2 Tin cable"]
      - ["functionalstorage:oak_1", 11, 0, 0, 1, 1, 1, "Input drawer · 1 Small steel gear"]
      - ["gtceu:lv_assembler", 9, 0, 2, 1, 1, 1, "LV Assembler · LV Electric Piston"]
      - ["gtceu:lv_robot_arm", 9, 0, 3, 1, 1, 1, "Robot Arm cover · Keep Exact + Item Filter"]
      - ["functionalstorage:oak_1", 9, 0, 4, 1, 1, 1, "Stock drawer · LV Electric Piston"]
      - ["functionalstorage:oak_1", 15, 0, 0, 1, 1, 1, "Input drawer · 2 Motor"]
      - ["functionalstorage:oak_1", 16, 0, 0, 1, 1, 1, "Input drawer · 1 Tin cable"]
      - ["thermal:fluid_cell", 17, 0, 0, 1, 1, 1, "Liquid rubber (fluid cell)"]
      - ["gtceu:lv_assembler", 16, 0, 2, 1, 1, 1, "LV Assembler · LV Conveyor Module"]
      - ["gtceu:lv_robot_arm", 16, 0, 3, 1, 1, 1, "Robot Arm cover · Keep Exact + Item Filter"]
      - ["functionalstorage:oak_1", 16, 0, 4, 1, 1, 1, "Stock drawer · LV Conveyor Module"]
      - ["functionalstorage:oak_1", 21, 0, 0, 1, 1, 1, "Input drawer · 1 Motor"]
      - ["functionalstorage:oak_1", 22, 0, 0, 1, 1, 1, "Input drawer · 1 Tin cable"]
      - ["functionalstorage:oak_1", 23, 0, 0, 1, 1, 1, "Input drawer · 1 Bronze pipe"]
      - ["functionalstorage:oak_1", 24, 0, 0, 1, 1, 1, "Input drawer · 1 Tin screw"]
      - ["functionalstorage:oak_1", 25, 0, 0, 1, 1, 1, "Input drawer · 1 Tin rotor"]
      - ["functionalstorage:oak_1", 26, 0, 0, 1, 1, 1, "Input drawer · 2 Rubber ring"]
      - ["gtceu:lv_assembler", 24, 0, 2, 1, 1, 1, "LV Assembler · LV Electric Pump"]
      - ["gtceu:lv_robot_arm", 24, 0, 3, 1, 1, 1, "Robot Arm cover · Keep Exact + Item Filter"]
      - ["functionalstorage:oak_1", 24, 0, 4, 1, 1, 1, "Stock drawer · LV Electric Pump"]
      - ["functionalstorage:oak_1", 30, 0, 0, 1, 1, 1, "Input drawer · 2 Motor"]
      - ["functionalstorage:oak_1", 31, 0, 0, 1, 1, 1, "Input drawer · 1 Piston"]
      - ["functionalstorage:oak_1", 32, 0, 0, 1, 1, 1, "Input drawer · 3 Tin cable"]
      - ["functionalstorage:oak_1", 33, 0, 0, 1, 1, 1, "Input drawer · 2 Steel rod"]
      - ["functionalstorage:oak_1", 34, 0, 0, 1, 1, 1, "Input drawer · 1 LV circuit"]
      - ["gtceu:lv_assembler", 32, 0, 2, 1, 1, 1, "LV Assembler · LV Robot Arm"]
      - ["gtceu:lv_robot_arm", 32, 0, 3, 1, 1, 1, "Robot Arm cover · Keep Exact + Item Filter"]
      - ["functionalstorage:oak_1", 32, 0, 4, 1, 1, 1, "Stock drawer · LV Robot Arm"]
    p:
      - [i, [0.5, 0.5, 1], [0.5, 0.5, 1.5]]
      - [i, [1.5, 0.5, 1], [1.5, 0.5, 1.5]]
      - [i, [2.5, 0.5, 1], [2.5, 0.5, 1.5]]
      - [i, [3.5, 0.5, 1], [3.5, 0.5, 1.5]]
      - [i, [0.5, 0.5, 1.5], [3.5, 0.5, 1.5]]
      - [i, [2.5, 0.5, 1.5], [2.5, 0.5, 2]]
      - [i, [7.5, 0.5, 1], [7.5, 0.5, 1.5]]
      - [i, [8.5, 0.5, 1], [8.5, 0.5, 1.5]]
      - [i, [9.5, 0.5, 1], [9.5, 0.5, 1.5]]
      - [i, [10.5, 0.5, 1], [10.5, 0.5, 1.5]]
      - [i, [11.5, 0.5, 1], [11.5, 0.5, 1.5]]
      - [i, [7.5, 0.5, 1.5], [11.5, 0.5, 1.5]]
      - [i, [9.5, 0.5, 1.5], [9.5, 0.5, 2]]
      - [i, [15.5, 0.5, 1], [15.5, 0.5, 1.5]]
      - [i, [16.5, 0.5, 1], [16.5, 0.5, 1.5]]
      - [i, [15.5, 0.5, 1.5], [16.5, 0.5, 1.5]]
      - [i, [16.5, 0.5, 1.5], [16.5, 0.5, 2]]
      - [f, [17.5, 0.25, -3.5], [17.5, 0.25, 0]]
      - [i, [21.5, 0.5, 1], [21.5, 0.5, 1.5]]
      - [i, [22.5, 0.5, 1], [22.5, 0.5, 1.5]]
      - [i, [23.5, 0.5, 1], [23.5, 0.5, 1.5]]
      - [i, [24.5, 0.5, 1], [24.5, 0.5, 1.5]]
      - [i, [25.5, 0.5, 1], [25.5, 0.5, 1.5]]
      - [i, [26.5, 0.5, 1], [26.5, 0.5, 1.5]]
      - [i, [21.5, 0.5, 1.5], [26.5, 0.5, 1.5]]
      - [i, [24.5, 0.5, 1.5], [24.5, 0.5, 2]]
      - [i, [30.5, 0.5, 1], [30.5, 0.5, 1.5]]
      - [i, [31.5, 0.5, 1], [31.5, 0.5, 1.5]]
      - [i, [32.5, 0.5, 1], [32.5, 0.5, 1.5]]
      - [i, [33.5, 0.5, 1], [33.5, 0.5, 1.5]]
      - [i, [34.5, 0.5, 1], [34.5, 0.5, 1.5]]
      - [i, [30.5, 0.5, 1.5], [34.5, 0.5, 1.5]]
      - [i, [32.5, 0.5, 1.5], [32.5, 0.5, 2]]
      - [i, [2.5, 0.5, 5], [2.5, 0.5, 6.5], [-1.5, 0.5, 6.5], [-1.5, 0.5, -1.5], [30.5, 0.5, -1.5]]
      - [i, [7.5, 0.5, -1.5], [7.5, 0.5, 0]]
      - [i, [15.5, 0.5, -1.5], [15.5, 0.5, 0]]
      - [i, [21.5, 0.5, -1.5], [21.5, 0.5, 0]]
      - [i, [30.5, 0.5, -1.5], [30.5, 0.5, 0]]
      - [i, [9.5, 0.9, 5], [9.5, 0.9, 7.5], [-2.5, 0.9, 7.5], [-2.5, 0.9, -2.5], [31.5, 0.9, -2.5], [31.5, 0.9, 0]]
    l:
      - ["Electric Motor · 5 s · stock 64 (12 / min)", 2.5, 2.7, 4]
      - ["4 input drawers", 2, 1.5, -0.5]
      - ["Electric Piston · 5 s · stock 64 (12 / min)", 8.5, 3.5, 4.5]
      - ["5 input drawers", 9.5, 1.5, -0.5]
      - ["Conveyor Module · 5 s · stock 64 (864 mB rubber)", 16.5, 2.7, 4]
      - ["3 input drawers", 16.5, 1.5, -0.5]
      - [Liquid rubber in, 17.5, 2.8, -3.5]
      - ["Electric Pump · 5 s · stock 64 (12 / min)", 24.5, 5.5, 3]
      - ["6 input drawers", 24, 1.5, -0.5]
      - ["Robot Arm · 5 s · stock 64 (12 / min)", 32, 2.7, 4]
      - ["5 input drawers", 32.5, 1.5, -0.5]
      - [Motors go to every other lane, -0.5, 3.1, -1.5]
      - ["Pistons → robot arm lane", 2, 3.6, 7.5]
      - [Parts drawers filled by the shaping rows, 8, 1.6, -3.5]
---
# LV Electric Motor line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_motor` · **Tags:** Infinite source, 3D scene

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Tin cable (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">2 Tin cable</span></span><span class="gt-slot" title="2 Iron rods (gtceu:iron_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Rod</span><span class="gt-note">2 Iron rods</span></span><span class="gt-slot" title="1 Magnetic iron rod (gtceu:magnetic_iron_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_iron_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Iron Rod</span><span class="gt-note">1 Magnetic iron rod</span></span><span class="gt-slot" title="4 Copper wire (gtceu:copper_single_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Wire</span><span class="gt-note">4 Copper wire</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Electric Motor (gtceu:lv_electric_motor) - 12 / min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Motor</span><b class="gt-q">12 / min</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Assembler: 2 tin cables + 2 iron rods + 1 magnetic iron rod + 4 copper wires → 1 motor in 5 s at 30 EU/t (12 per minute). The iron version is as good as the steel one and needs no steel. — `gtceu:lv_assembler`, `gtceu:lv_electric_motor`
2. Raw cost per motor: 1.5 iron, 2 copper, 1 tin and 288 mB liquid rubber (1.5 rubber). The gravel sieve alone gives 24 of each ore per minute. — `minecraft:iron_ingot`, `minecraft:copper_ingot`, `gtceu:tin_ingot`
3. Keep 64 motors: every other component line pulls from this drawer. — `gtceu:lv_robot_arm`

## Tips

- Motors are inside every other part: pistons (1), conveyors (2), pumps (1), robot arms (2). Make this line first and biggest.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `functionalstorage:oak_1` | 1 |
| `pipez:item_pipe` | 8 |

## Needs / Feeds

- **Needs:** [Parts row 2: wires, fine wire, cables](comp_wires.md), [Parts row 1: rods, plates, bolts, gears](comp_parts.md)
- **Feeds:** [LV Electric Piston line](comp_piston.md), [LV Conveyor Module line](comp_conveyor.md), [LV Electric Pump line](comp_pump.md), [LV Robot Arm line](comp_robot_arm.md)
- **Main source for:** `gtceu:lv_electric_motor`

## Extras

- 3D assembly scene with 38 blocks (open it in the Atlas page).
