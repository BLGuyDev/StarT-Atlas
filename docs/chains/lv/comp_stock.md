---
kind: chain
id: comp_stock
order: 770
data:
  t: "Component wall: always a stock of every part (no AE2)"
  inf: true
  hero: false
  "n":
    - [in, "Ingots + liquid rubber (your farms)", s, "minecraft:iron_ingot"]
    - [sh, "Shaping row (lathe, wiremill, bender…)", m, "gtceu:lv_lathe"]
    - [pd, Parts drawers, x, "functionalstorage:oak_1"]
    - [as, One assembler per component, m, "gtceu:lv_assembler"]
    - [ra, "Robot Arm cover · Keep Exact", p, "gtceu:lv_robot_arm"]
    - [st, "Stock drawers (64 each)", o, "functionalstorage:oak_1"]
  e: [[in, sh, pipes], [sh, pd, Keep Exact], [pd, as, filtered pipes], [as, ra], [ra, st, tops up]]
  tips:
    - A GT machine with a full output slot just pauses and draws no power, so nothing is wasted while the stock is full.
    - |-
      Give every machine one job: set its ghost circuit once and only pipe in the items of that recipe, so its input slots never clog.
    - |-
      Simplest version without covers: the machine stops when its output drawer is full, so the drawer size is the stock.
    - |-
      Iron Downgrade (4 iron plates + 1 tin plate, crossed) cuts a drawer slot to 64 items: the easy way to cap a stock drawer.
  b:
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["functionalstorage:oak_1", 24]
    - ["pipez:item_pipe", 64]
    - ["pipez:fluid_pipe", 16]
  how:
    - i: ["functionalstorage:oak_1", "pipez:item_pipe"]
      t: |-
        Raw drawers at the start: iron, copper, tin, steel, red alloy ingots and charcoal dust, filled by your ore and alloy lines. A fluid cell (or tank) holds liquid rubber and glue.
    - i: ["gtceu:lv_lathe", "gtceu:lv_wiremill", "gtceu:lv_bender"]
      t: |-
        Shaping row: each machine does one part (rods, wires, cables, plates, foil, bolts, gears) and pushes it into its own parts drawer.
    - i: ["gtceu:lv_robot_arm", "gtceu:item_filter"]
      t: |-
        On the output face of every machine: a Robot Arm cover in Keep Exact mode with an Item Filter holding the part and the amount (e.g. 64). It stops pushing at 64; the machine fills its own output slot and pauses until you take some.
    - i: ["pipez:item_pipe", "gtceu:lv_assembler"]
      t: Pipez item pipes with a filter per ingredient carry parts from the drawers to the assembler that needs them. One assembler per component, each with its circuit set.
    - i: ["gtceu:lv_electric_motor", "gtceu:basic_electronic_circuit"]
      t: |-
        Stock drawers for the finished parts: motors, pistons, conveyors, pumps, robot arms and LV circuits. Take what you need and the wall rebuilds it on its own.
    - i: ["thermal:dynamo_lapidary"]
      t: |-
        Power: each LV machine uses 4–30 EU/t and only while working. With every machine busy at once the wall stays under about 350 EU/t, which two Lapidary Dynamos with LV kits cover.
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
# Component wall: always a stock of every part (no AE2)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_stock` · **Tags:** Infinite source, 3D scene

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-sh">
<div class="gt-head"><span class="gt-mname">Shaping row (lathe, wiremill, bender…)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Ingots + liquid rubber (your farms) (minecraft:iron_ingot) - pipes"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Ingots + liquid rubber (your farms)</span><span class="gt-tag">infinite</span><b class="gt-q">pipes</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Parts drawers (functionalstorage:oak_1) - Keep Exact"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><b class="gt-q">Keep Exact</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">One assembler per component</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Parts drawers (functionalstorage:oak_1) - filtered pipes"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><b class="gt-q">filtered pipes</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-ra" title="Robot Arm cover · Keep Exact (gtceu:lv_robot_arm)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Robot Arm</span><span class="gt-note">Robot Arm cover · Keep Exact</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-ra">
<div class="gt-head"><span class="gt-mname">Robot Arm cover · Keep Exact</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-as" title="One assembler per component (gtceu:lv_assembler)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Assembler</span><span class="gt-note">One assembler per component</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Stock drawers (64 each) (functionalstorage:oak_1) - tops up"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Stock drawers (64 each)</span><b class="gt-q">tops up</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_robot_arm</code></div>
</div>
</div>

## Flow

- [Shaping row (lathe, wiremill, bender…)](#m-sh) → [One assembler per component](#m-as) → [Robot Arm cover · Keep Exact](#m-ra)

## How to build

1. Raw drawers at the start: iron, copper, tin, steel, red alloy ingots and charcoal dust, filled by your ore and alloy lines. A fluid cell (or tank) holds liquid rubber and glue. — `functionalstorage:oak_1`, `pipez:item_pipe`
2. Shaping row: each machine does one part (rods, wires, cables, plates, foil, bolts, gears) and pushes it into its own parts drawer. — `gtceu:lv_lathe`, `gtceu:lv_wiremill`, `gtceu:lv_bender`
3. On the output face of every machine: a Robot Arm cover in Keep Exact mode with an Item Filter holding the part and the amount (e.g. 64). It stops pushing at 64; the machine fills its own output slot and pauses until you take some. — `gtceu:lv_robot_arm`, `gtceu:item_filter`
4. Pipez item pipes with a filter per ingredient carry parts from the drawers to the assembler that needs them. One assembler per component, each with its circuit set. — `pipez:item_pipe`, `gtceu:lv_assembler`
5. Stock drawers for the finished parts: motors, pistons, conveyors, pumps, robot arms and LV circuits. Take what you need and the wall rebuilds it on its own. — `gtceu:lv_electric_motor`, `gtceu:basic_electronic_circuit`
6. Power: each LV machine uses 4–30 EU/t and only while working. With every machine busy at once the wall stays under about 350 EU/t, which two Lapidary Dynamos with LV kits cover. — `thermal:dynamo_lapidary`

## Tips

- A GT machine with a full output slot just pauses and draws no power, so nothing is wasted while the stock is full.
- Give every machine one job: set its ghost circuit once and only pipe in the items of that recipe, so its input slots never clog.
- Simplest version without covers: the machine stops when its output drawer is full, so the drawer size is the stock.
- Iron Downgrade (4 iron plates + 1 tin plate, crossed) cuts a drawer slot to 64 items: the easy way to cap a stock drawer.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `functionalstorage:oak_1` | 24 |
| `pipez:item_pipe` | 64 |
| `pipez:fluid_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md)

## Extras

- 3D assembly scene with 38 blocks (open it in the Atlas page).
