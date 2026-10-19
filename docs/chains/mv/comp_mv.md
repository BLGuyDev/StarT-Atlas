---
kind: chain
id: comp_mv
order: 940
data:
  t: MV components on LV machines
  inf: true
  "n":
    - [al, Aluminium, i, "gtceu:aluminium_ingot"]
    - [la, Lathe, m, "gtceu:lv_lathe"]
    - [ar, Aluminium rods, x, "gtceu:aluminium_rod"]
    - [st, Steel rods, i, "gtceu:steel_rod"]
    - [po, Polarizer, m, "gtceu:lv_polarizer"]
    - [ms, Magnetic steel rod, x, "gtceu:magnetic_steel_rod"]
    - [cn, Cupronickel, i, "gtceu:cupronickel_ingot"]
    - [wm, "Wiremill · circuit 2", m, "gtceu:lv_wiremill"]
    - [dw, Cupronickel double wire, x, "gtceu:cupronickel_double_wire"]
    - [cc, Copper cables, i, "gtceu:copper_single_cable"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [mo, MV Electric Motor, o, "gtceu:mv_electric_motor"]
  e:
    - [al, la]
    - [la, ar, "1 → 2"]
    - [st, po]
    - [po, ms]
    - [cn, wm]
    - [wm, dw, "1 → 1"]
    - [ar, as, "2"]
    - [ms, as, "1"]
    - [dw, as, "4"]
    - [cc, as, "2"]
    - [as, mo]
  tips:
    - |-
      Every MV component recipe runs at 30 EU/t: your LV assemblers make them, no MV power needed.
    - |-
      MV piston: MV motor + 2 aluminium rods + 2 copper cables + 3 aluminium plates + 1 small aluminium gear. MV conveyor: 2 MV motors + 1 copper cable + 864 mB liquid rubber. MV pump: MV motor + copper cable + steel fluid pipe + bronze screw + bronze rotor + 2 rubber rings.
    - |-
      MV robot arms need MV circuits: those are the next real wall.
  b:
    - ["gtceu:lv_lathe", 1]
    - ["gtceu:lv_polarizer", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_alloy_smelter", 1]
    - ["gtceu:lv_assembler", 4]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["functionalstorage:oak_1", 8]
  how:
    - i: ["gtceu:lv_alloy_smelter", "gtceu:cupronickel_ingot"]
      t: |-
        Cupronickel: alloy smelter, 1 copper + 1 nickel → 2 cupronickel. Nickel comes from pentlandite (Void Extractor).
    - i: ["gtceu:lv_wiremill", "gtceu:cupronickel_double_wire"]
      t: |-
        Wiremill on circuit 2: 1 cupronickel ingot → 1 double wire (4 per MV motor).
    - i: ["gtceu:lv_lathe", "gtceu:aluminium_rod"]
      t: |-
        Lathe: 1 aluminium → 2 rods. Polarizer: steel rod → magnetic steel rod.
    - i: ["gtceu:lv_assembler", "gtceu:mv_electric_motor"]
      t: |-
        Assembler: 2 copper cables + 2 aluminium rods + 1 magnetic steel rod + 4 cupronickel double wires → 1 MV motor in 5 s at 30 EU/t.
    - i: ["gtceu:mv_electric_piston", "gtceu:mv_conveyor_module", "gtceu:mv_electric_pump"]
      t: One more assembler each for MV pistons, conveyors and pumps, pulling motors from the MV motor drawer, all with Robot Arm Keep Exact caps.
---
# MV components on LV machines

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_mv` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [MV components (on LV machines)](../../plan/p5.md#mvcomp)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-la">
<div class="gt-head"><span class="gt-mname">Lathe</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Aluminium (gtceu:aluminium_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Aluminium rods (gtceu:aluminium_rod) - 1 → 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Rod</span><span class="gt-note">Aluminium rods</span><b class="gt-q">1 → 2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-lv" id="m-po">
<div class="gt-head"><span class="gt-mname">Polarizer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Steel rods (gtceu:steel_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Rod</span><span class="gt-note">Steel rods</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Magnetic steel rod (gtceu:magnetic_steel_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Steel Rod</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_polarizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">Wiremill · circuit 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cupronickel (gtceu:cupronickel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Cupronickel double wire (gtceu:cupronickel_double_wire) - 1 → 1"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Double Wire</span><b class="gt-q">1 → 1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Aluminium rods (gtceu:aluminium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Rod</span><span class="gt-note">Aluminium rods</span><b class="gt-q">2</b></span><span class="gt-slot" title="Magnetic steel rod (gtceu:magnetic_steel_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Steel Rod</span><b class="gt-q">1</b></span><span class="gt-slot" title="Cupronickel double wire (gtceu:cupronickel_double_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Double Wire</span><b class="gt-q">4</b></span><span class="gt-slot" title="Copper cables (gtceu:copper_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Cable</span><span class="gt-note">Copper cables</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="MV Electric Motor (gtceu:mv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Electric Motor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Lathe](#m-la) → [Assembler · 5 s · 30 EU/t](#m-as)
- [Polarizer](#m-po) → [Assembler · 5 s · 30 EU/t](#m-as)
- [Wiremill · circuit 2](#m-wm) → [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Cupronickel: alloy smelter, 1 copper + 1 nickel → 2 cupronickel. Nickel comes from pentlandite (Void Extractor). — `gtceu:lv_alloy_smelter`, `gtceu:cupronickel_ingot`
2. Wiremill on circuit 2: 1 cupronickel ingot → 1 double wire (4 per MV motor). — `gtceu:lv_wiremill`, `gtceu:cupronickel_double_wire`
3. Lathe: 1 aluminium → 2 rods. Polarizer: steel rod → magnetic steel rod. — `gtceu:lv_lathe`, `gtceu:aluminium_rod`
4. Assembler: 2 copper cables + 2 aluminium rods + 1 magnetic steel rod + 4 cupronickel double wires → 1 MV motor in 5 s at 30 EU/t. — `gtceu:lv_assembler`, `gtceu:mv_electric_motor`
5. One more assembler each for MV pistons, conveyors and pumps, pulling motors from the MV motor drawer, all with Robot Arm Keep Exact caps. — `gtceu:mv_electric_piston`, `gtceu:mv_conveyor_module`, `gtceu:mv_electric_pump`

## Tips

- Every MV component recipe runs at 30 EU/t: your LV assemblers make them, no MV power needed.
- MV piston: MV motor + 2 aluminium rods + 2 copper cables + 3 aluminium plates + 1 small aluminium gear. MV conveyor: 2 MV motors + 1 copper cable + 864 mB liquid rubber. MV pump: MV motor + copper cable + steel fluid pipe + bronze screw + bronze rotor + 2 rubber rings.
- MV robot arms need MV circuits: those are the next real wall.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_lathe` | 1 |
| `gtceu:lv_polarizer` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_alloy_smelter` | 1 |
| `gtceu:lv_assembler` | 4 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `functionalstorage:oak_1` | 8 |

## Needs / Feeds

- **Needs:** [Infinite aluminium (clay)](aluminium.md), [Parts row 1: rods, plates, bolts, gears](../lv/comp_parts.md), [Cupronickel coils ×16](../lv/coils.md), [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md)
- **Feeds:** [MV Robot Arm (uses the new circuits)](comp_mv_arm.md)
- **Main source for:** `gtceu:mv_electric_motor`
