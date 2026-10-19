---
kind: chain
id: comp_robot_arm
order: 840
data:
  t: LV Robot Arm line
  inf: true
  "n":
    - [m, "2 Motors", i, "gtceu:lv_electric_motor"]
    - [p, "1 Piston", i, "gtceu:lv_electric_piston"]
    - [c, "3 Tin cable", i, "gtceu:tin_single_cable"]
    - [r, "2 Steel rods", i, "gtceu:steel_rod"]
    - [ci, "1 LV circuit", i, "gtceu:basic_electronic_circuit"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [out, LV Robot Arm, o, "gtceu:lv_robot_arm"]
  e: [[m, as], [p, as], [c, as], [r, as], [ci, as], [as, out, "12 / min"]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["functionalstorage:oak_1", 1]
    - ["pipez:item_pipe", 8]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_robot_arm"]
      t: |-
        Assembler: 2 motors + 1 piston + 3 tin cables + 2 steel rods + 1 LV circuit → 1 robot arm in 5 s.
    - i: ["gtceu:lv_robot_arm"]
      t: |-
        The wall’s own covers are robot arms: craft the first dozen by hand, then this line supplies the rest.
---
# LV Robot Arm line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_robot_arm` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Motors (gtceu:lv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Motor</span><span class="gt-note">2 Motors</span></span><span class="gt-slot" title="1 Piston (gtceu:lv_electric_piston)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Piston</span><span class="gt-note">1 Piston</span></span><span class="gt-slot" title="3 Tin cable (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">3 Tin cable</span></span><span class="gt-slot" title="2 Steel rods (gtceu:steel_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Rod</span><span class="gt-note">2 Steel rods</span></span><span class="gt-slot" title="1 LV circuit (gtceu:basic_electronic_circuit)"><img class="gt-ico" src="../../assets/icons/gtceu__basic_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basic Electronic Circuit</span><span class="gt-note">1 LV circuit</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Robot Arm (gtceu:lv_robot_arm) - 12 / min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Robot Arm</span><b class="gt-q">12 / min</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Assembler: 2 motors + 1 piston + 3 tin cables + 2 steel rods + 1 LV circuit → 1 robot arm in 5 s. — `gtceu:lv_assembler`, `gtceu:lv_robot_arm`
2. The wall’s own covers are robot arms: craft the first dozen by hand, then this line supplies the rest. — `gtceu:lv_robot_arm`

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `functionalstorage:oak_1` | 1 |
| `pipez:item_pipe` | 8 |

## Needs / Feeds

- **Needs:** [LV Electric Motor line](comp_motor.md), [LV Electric Piston line](comp_piston.md), [Parts row 2: wires, fine wire, cables](comp_wires.md), [Parts row 1: rods, plates, bolts, gears](comp_parts.md), [LV circuit line (Basic Electronic Circuit)](comp_circuit_lv.md)
- **Main source for:** `gtceu:lv_robot_arm`
