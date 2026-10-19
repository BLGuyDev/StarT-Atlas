---
kind: chain
id: comp_piston
order: 810
data:
  t: LV Electric Piston line
  inf: true
  "n":
    - [m, "1 Motor", i, "gtceu:lv_electric_motor"]
    - [p, "3 Steel plates", i, "gtceu:steel_plate"]
    - [r, "2 Steel rods", i, "gtceu:steel_rod"]
    - [c, "2 Tin cable", i, "gtceu:tin_single_cable"]
    - [g, "1 Small steel gear", i, "gtceu:small_steel_gear"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [out, LV Electric Piston, o, "gtceu:lv_electric_piston"]
  e: [[m, as], [p, as], [r, as], [c, as], [g, as], [as, out, "12 / min"]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["functionalstorage:oak_1", 1]
    - ["pipez:item_pipe", 8]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_electric_piston"]
      t: |-
        Assembler: 1 motor + 3 steel plates + 2 steel rods + 2 tin cables + 1 small steel gear → 1 piston in 5 s.
    - i: ["gtceu:lv_robot_arm"]
      t: |-
        Keep 32: robot arms and many machines (sieve, forge hammer) use them.
---
# LV Electric Piston line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_piston` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Motor (gtceu:lv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Motor</span><span class="gt-note">1 Motor</span></span><span class="gt-slot" title="3 Steel plates (gtceu:steel_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Plate</span><span class="gt-note">3 Steel plates</span></span><span class="gt-slot" title="2 Steel rods (gtceu:steel_rod)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Rod</span><span class="gt-note">2 Steel rods</span></span><span class="gt-slot" title="2 Tin cable (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">2 Tin cable</span></span><span class="gt-slot" title="1 Small steel gear (gtceu:small_steel_gear)"><img class="gt-ico" src="../../assets/icons/gtceu__small_steel_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Steel Gear</span><span class="gt-note">1 Small steel gear</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Electric Piston (gtceu:lv_electric_piston) - 12 / min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Piston</span><b class="gt-q">12 / min</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Assembler: 1 motor + 3 steel plates + 2 steel rods + 2 tin cables + 1 small steel gear → 1 piston in 5 s. — `gtceu:lv_assembler`, `gtceu:lv_electric_piston`
2. Keep 32: robot arms and many machines (sieve, forge hammer) use them. — `gtceu:lv_robot_arm`

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `functionalstorage:oak_1` | 1 |
| `pipez:item_pipe` | 8 |

## Needs / Feeds

- **Needs:** [LV Electric Motor line](comp_motor.md), [Parts row 1: rods, plates, bolts, gears](comp_parts.md), [Parts row 2: wires, fine wire, cables](comp_wires.md)
- **Feeds:** [LV Robot Arm line](comp_robot_arm.md)
- **Main source for:** `gtceu:lv_electric_piston`
