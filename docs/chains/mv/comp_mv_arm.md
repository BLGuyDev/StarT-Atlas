---
kind: chain
id: comp_mv_arm
order: 1010
data:
  t: MV Robot Arm (uses the new circuits)
  inf: true
  "n":
    - [gc, Good Electronic Circuit, i, "gtceu:good_electronic_circuit"]
    - [mo, "2 MV motors", i, "gtceu:mv_electric_motor"]
    - [pi, MV piston, i, "gtceu:mv_electric_piston"]
    - [ro, "2 Aluminium rods", i, "gtceu:aluminium_rod"]
    - [cb, "3 Copper cables", i, "gtceu:copper_single_cable"]
    - [as, "Assembler · 5 s", m, "gtceu:lv_assembler"]
    - [out, MV Robot Arm, o, "gtceu:mv_robot_arm"]
  e: [[gc, as, "1"], [mo, as, "2"], [pi, as, "1"], [ro, as, "2"], [cb, as, "3"], [as, out]]
  tips:
    - |-
      Recipe (assembler, 30 EU/t, 5 s): 3 copper cables + 2 aluminium rods + 2 MV motors + 1 MV piston + 1 Good Electronic Circuit. An LV assembler runs it.
    - |-
      Every MV machine needs 2 MV robot arms or circuits: MV assembler = 2 arms + 2 circuits + 2 conveyors + hull + 2 copper cables; MV chemical reactor = 2 circuits + MV motor + MV hull + bronze rotor + 2 glass + 2 copper cables.
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 2]
    - ["gtceu:item_filter", 2]
    - ["functionalstorage:oak_1", 6]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:mv_robot_arm"]
      t: |-
        LV Assembler: 3 copper cables + 2 aluminium rods (lathe) + 2 MV motors + 1 MV piston + 1 Good Electronic Circuit → 1 MV robot arm in 5 s. Motors and pistons come from the MV component line, the circuit from the drawer above.
---
# MV Robot Arm (uses the new circuits)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_mv_arm` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [MV circuits (Good Electronic Circuit)](../../plan/p6.md#mvcirc)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Good Electronic Circuit (gtceu:good_electronic_circuit) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__good_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Good Electronic Circuit</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 MV motors (gtceu:mv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Electric Motor</span><span class="gt-note">2 MV motors</span><b class="gt-q">2</b></span><span class="gt-slot" title="MV piston (gtceu:mv_electric_piston) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Electric Piston</span><span class="gt-note">MV piston</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Aluminium rods (gtceu:aluminium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Rod</span><span class="gt-note">2 Aluminium rods</span><b class="gt-q">2</b></span><span class="gt-slot" title="3 Copper cables (gtceu:copper_single_cable) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Cable</span><span class="gt-note">3 Copper cables</span><b class="gt-q">3</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="MV Robot Arm (gtceu:mv_robot_arm)"><img class="gt-ico" src="../../assets/icons/gtceu__mv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Robot Arm</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s](#m-as)

## How to build

1. LV Assembler: 3 copper cables + 2 aluminium rods (lathe) + 2 MV motors + 1 MV piston + 1 Good Electronic Circuit → 1 MV robot arm in 5 s. Motors and pistons come from the MV component line, the circuit from the drawer above. — `gtceu:lv_assembler`, `gtceu:mv_robot_arm`

## Tips

- Recipe (assembler, 30 EU/t, 5 s): 3 copper cables + 2 aluminium rods + 2 MV motors + 1 MV piston + 1 Good Electronic Circuit. An LV assembler runs it.
- Every MV machine needs 2 MV robot arms or circuits: MV assembler = 2 arms + 2 circuits + 2 conveyors + hull + 2 copper cables; MV chemical reactor = 2 circuits + MV motor + MV hull + bronze rotor + 2 glass + 2 copper cables.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 2 |
| `gtceu:item_filter` | 2 |
| `functionalstorage:oak_1` | 6 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [MV circuit line (Good Electronic Circuit)](mv_circuit.md), [MV components on LV machines](comp_mv.md), [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md)
- **Main source for:** `gtceu:mv_robot_arm`
