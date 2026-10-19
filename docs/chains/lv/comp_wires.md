---
kind: chain
id: comp_wires
order: 790
data:
  t: "Parts row 2: wires, fine wire, cables"
  inf: true
  "n":
    - [cu, Copper, i, "minecraft:copper_ingot"]
    - [sn, Tin, i, "gtceu:tin_ingot"]
    - [ra, Red alloy, i, "gtceu:red_alloy_ingot"]
    - [lr, Liquid rubber, f, "gtceu:rubber_bucket"]
    - [w1, "Wiremill · copper circ 1", m, "gtceu:lv_wiremill"]
    - [w2, "Wiremill · copper circ 3", m, "gtceu:lv_wiremill"]
    - [w3, "Wiremill · tin", m, "gtceu:lv_wiremill"]
    - [w4, "Wiremill · red alloy", m, "gtceu:lv_wiremill"]
    - [ca, "Assembler · cables", m, "gtceu:lv_assembler"]
    - - dr
      - Parts drawers
      - g
      - functionalstorage:oak_1
      - - [Copper wire, "gtceu:copper_single_wire", "1 → 2"]
        - [Fine copper wire, "gtceu:fine_copper_wire", "1 → 8"]
        - [Tin cable, "gtceu:tin_single_cable", "+144 mB"]
        - [Red alloy wire, "gtceu:red_alloy_single_wire", "1 → 2"]
  e: [[cu, w1], [cu, w2], [sn, w3], [ra, w4], [w3, ca, tin wire], [lr, ca], [w1, dr], [w2, dr], [ca, dr], [w4, dr]]
  tips:
    - |-
      Wiremill: 1 ingot → 2 wires on circuit 1, or 8 fine wires on circuit 3. One wiremill per product keeps the circuits fixed.
    - |-
      Cable: 1 tin wire + 144 mB liquid rubber → 1 tin cable in 5 s (assembler, 7 EU/t). Every LV component needs 1–3.
  b:
    - ["gtceu:lv_wiremill", 4]
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["functionalstorage:oak_1", 5]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
  how:
    - i: ["gtceu:lv_wiremill", "gtceu:copper_single_wire"]
      t: |-
        Wiremill on copper, circuit 1: 1 copper → 2 copper wires (motors use 4, vacuum tubes 2).
    - i: ["gtceu:lv_wiremill", "gtceu:fine_copper_wire"]
      t: |-
        Second copper wiremill on circuit 3: 1 copper → 8 fine copper wires (resistors use 4).
    - i: ["gtceu:lv_wiremill", "gtceu:red_alloy_single_wire"]
      t: "Red alloy wiremill: wires for the LV circuits (2 per craft)."
    - i: ["gtceu:lv_assembler", "gtceu:rubber_bucket", "gtceu:tin_single_cable"]
      t: |-
        Tin wiremill feeds the cable assembler: 1 tin wire + 144 mB liquid rubber from the rubber line → 1 tin cable.
---
# Parts row 2: wires, fine wire, cables

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_wires` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Wires and cables](../../plan/p4.md#wires)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-w1">
<div class="gt-head"><span class="gt-mname">Wiremill · copper circ 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper (minecraft:copper_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Copper wire <i>1 → 2</i></span><span>Fine copper wire <i>1 → 8</i></span><span>Tin cable <i>+144 mB</i></span><span>Red alloy wire <i>1 → 2</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-w2">
<div class="gt-head"><span class="gt-mname">Wiremill · copper circ 3</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper (minecraft:copper_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Copper wire <i>1 → 2</i></span><span>Fine copper wire <i>1 → 8</i></span><span>Tin cable <i>+144 mB</i></span><span>Red alloy wire <i>1 → 2</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-w3">
<div class="gt-head"><span class="gt-mname">Wiremill · tin</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tin (gtceu:tin_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ca" title="Assembler · cables (gtceu:lv_assembler) - tin wire"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Assembler</span><span class="gt-note">Assembler · cables</span><b class="gt-q">tin wire</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-w4">
<div class="gt-head"><span class="gt-mname">Wiremill · red alloy</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Red alloy (gtceu:red_alloy_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__red_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Red Alloy Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Copper wire <i>1 → 2</i></span><span>Fine copper wire <i>1 → 8</i></span><span>Tin cable <i>+144 mB</i></span><span>Red alloy wire <i>1 → 2</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-ca">
<div class="gt-head"><span class="gt-mname">Assembler · cables</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-w3" title="Wiremill · tin (gtceu:lv_wiremill) - tin wire"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Wiremill</span><span class="gt-note">Wiremill · tin</span><b class="gt-q">tin wire</b></a><span class="gt-slot gt-fluid" title="Liquid rubber (gtceu:rubber_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><span class="gt-note">Liquid rubber</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Parts drawers (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Parts drawers</span><span class="gt-sub"><span>Copper wire <i>1 → 2</i></span><span>Fine copper wire <i>1 → 8</i></span><span>Tin cable <i>+144 mB</i></span><span>Red alloy wire <i>1 → 2</i></span></span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Wiremill · copper circ 1](#m-w1)
- [Wiremill · copper circ 3](#m-w2)
- [Wiremill · tin](#m-w3) → [Assembler · cables](#m-ca)
- [Wiremill · red alloy](#m-w4)

## How to build

1. Wiremill on copper, circuit 1: 1 copper → 2 copper wires (motors use 4, vacuum tubes 2). — `gtceu:lv_wiremill`, `gtceu:copper_single_wire`
2. Second copper wiremill on circuit 3: 1 copper → 8 fine copper wires (resistors use 4). — `gtceu:lv_wiremill`, `gtceu:fine_copper_wire`
3. Red alloy wiremill: wires for the LV circuits (2 per craft). — `gtceu:lv_wiremill`, `gtceu:red_alloy_single_wire`
4. Tin wiremill feeds the cable assembler: 1 tin wire + 144 mB liquid rubber from the rubber line → 1 tin cable. — `gtceu:lv_assembler`, `gtceu:rubber_bucket`, `gtceu:tin_single_cable`

## Tips

- Wiremill: 1 ingot → 2 wires on circuit 1, or 8 fine wires on circuit 3. One wiremill per product keeps the circuits fixed.
- Cable: 1 tin wire + 144 mB liquid rubber → 1 tin cable in 5 s (assembler, 7 EU/t). Every LV component needs 1–3.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_wiremill` | 4 |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `functionalstorage:oak_1` | 5 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md)
- **Feeds:** [LV Electric Motor line](comp_motor.md), [LV Electric Piston line](comp_piston.md), [LV Conveyor Module line](comp_conveyor.md), [LV Electric Pump line](comp_pump.md), [LV Robot Arm line](comp_robot_arm.md), [LV circuit line (Basic Electronic Circuit)](comp_circuit_lv.md), [First MV hull and the LV → MV transformer](../mv/mv_hull.md), [LV hull line (Create mechanical crafters)](lv_hull_line.md), [MV hull line (Create mechanical crafters)](../mv/mv_hull_line.md), [MV components on LV machines](../mv/comp_mv.md), [Diodes (gallium arsenide + glass + fine wire)](../mv/mv_diode.md), [MV circuit line (Good Electronic Circuit)](../mv/mv_circuit.md), [MV Robot Arm (uses the new circuits)](../mv/comp_mv_arm.md)
- **Main source for:** `gtceu:tin_single_cable`, `gtceu:copper_single_wire`, `gtceu:fine_copper_wire`, `gtceu:red_alloy_single_wire`, `gtceu:copper_single_cable`
