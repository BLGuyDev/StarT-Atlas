---
kind: chain
id: mv_circuit
order: 1000
data:
  t: MV circuit line (Good Electronic Circuit)
  inf: true
  "n":
    - [bc, "2 LV circuits", i, "gtceu:basic_electronic_circuit"]
    - [pb, Phenolic printed circuit board, i, "gtceu:phenolic_printed_circuit_board"]
    - [di, "2 Diodes", i, "gtceu:diode"]
    - [cw, "2 Copper wire", i, "gtceu:copper_single_wire"]
    - [ca, "LV Circuit Assembler · 15 s", m, "gtceu:lv_circuit_assembler"]
    - [ra, "Robot Arm cover · Keep Exact 64", p, "gtceu:lv_robot_arm"]
    - [out, Good Electronic Circuit, o, "gtceu:good_electronic_circuit"]
  e: [[bc, ca, "2"], [pb, ca, "1"], [di, ca, "2"], [cw, ca, "2"], [ca, out, "1 / 15 s"], [ra, out, caps stock]]
  tips:
    - |-
      Recipe (circuit assembler, 30 EU/t, 15 s): 1 phenolic printed circuit board + 2 LV circuits + 2 diodes + 2 copper wires → 1 Good Electronic Circuit. It runs on LV power.
    - |-
      Per circuit: 1 silver ingot, 1 wood dust, 50 mB glue, 100 mB iron III chloride, 0.25 gallium + 0.25 arsenic, 2 glass blocks, 2 copper ingots (8 fine wire for the diodes + 2 wires) and 2 LV circuits.
    - The MV Circuit Assembler itself needs two HV circuits to build, so stay on the LV one for now.
  b:
    - ["gtceu:lv_circuit_assembler", 1]
    - ["gtceu:lv_robot_arm", 2]
    - ["gtceu:item_filter", 2]
    - ["functionalstorage:oak_1", 5]
    - ["pipez:item_pipe", 16]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:basic_electronic_circuit
        - gtceu:phenolic_printed_circuit_board
        - gtceu:diode
      t: |-
        Four input drawers in front of the assembler (LV circuits, printed boards, diodes, copper wire), each filled by routers from the stock drawers of the lines above. A circuit assembler dedicated to this recipe: keep your LV circuit assembler on its own recipe.
    - i: ["gtceu:lv_circuit_assembler", "gtceu:good_electronic_circuit"]
      t: |-
        LV Circuit Assembler: 1 phenolic printed circuit board + 2 LV circuits + 2 diodes + 2 copper wires → 1 Good Electronic Circuit in 15 s at 30 EU/t, so 4 a minute.
    - i: ["gtceu:lv_robot_arm", "gtceu:item_filter", "gtceu:good_electronic_circuit"]
      t: Output drawer with a Robot Arm cover on Keep Exact 64 and an Item Filter holding the circuit. A full output slot pauses the machine at zero draw.
---
# MV circuit line (Good Electronic Circuit)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_circuit` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [MV circuits (Good Electronic Circuit)](../../plan/p6.md#mvcirc)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-ca">
<div class="gt-head"><span class="gt-mname">LV Circuit Assembler · 15 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 LV circuits (gtceu:basic_electronic_circuit) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__basic_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basic Electronic Circuit</span><span class="gt-note">2 LV circuits</span><b class="gt-q">2</b></span><span class="gt-slot" title="Phenolic printed circuit board (gtceu:phenolic_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Printed Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Diodes (gtceu:diode) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__diode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diode</span><span class="gt-note">2 Diodes</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 Copper wire (gtceu:copper_single_wire) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Wire</span><span class="gt-note">2 Copper wire</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Good Electronic Circuit (gtceu:good_electronic_circuit) - 1 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__good_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Good Electronic Circuit</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-ra">
<div class="gt-head"><span class="gt-mname">Robot Arm cover · Keep Exact 64</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Good Electronic Circuit (gtceu:good_electronic_circuit) - caps stock"><img class="gt-ico" src="../../assets/icons/gtceu__good_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Good Electronic Circuit</span><b class="gt-q">caps stock</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_robot_arm</code></div>
</div>
</div>

## Flow

- [LV Circuit Assembler · 15 s](#m-ca)
- [Robot Arm cover · Keep Exact 64](#m-ra)

## How to build

1. Four input drawers in front of the assembler (LV circuits, printed boards, diodes, copper wire), each filled by routers from the stock drawers of the lines above. A circuit assembler dedicated to this recipe: keep your LV circuit assembler on its own recipe. — `functionalstorage:oak_1`, `gtceu:basic_electronic_circuit`, `gtceu:phenolic_printed_circuit_board`, `gtceu:diode`
2. LV Circuit Assembler: 1 phenolic printed circuit board + 2 LV circuits + 2 diodes + 2 copper wires → 1 Good Electronic Circuit in 15 s at 30 EU/t, so 4 a minute. — `gtceu:lv_circuit_assembler`, `gtceu:good_electronic_circuit`
3. Output drawer with a Robot Arm cover on Keep Exact 64 and an Item Filter holding the circuit. A full output slot pauses the machine at zero draw. — `gtceu:lv_robot_arm`, `gtceu:item_filter`, `gtceu:good_electronic_circuit`

## Tips

- Recipe (circuit assembler, 30 EU/t, 15 s): 1 phenolic printed circuit board + 2 LV circuits + 2 diodes + 2 copper wires → 1 Good Electronic Circuit. It runs on LV power.
- Per circuit: 1 silver ingot, 1 wood dust, 50 mB glue, 100 mB iron III chloride, 0.25 gallium + 0.25 arsenic, 2 glass blocks, 2 copper ingots (8 fine wire for the diodes + 2 wires) and 2 LV circuits.
- The MV Circuit Assembler itself needs two HV circuits to build, so stay on the LV one for now.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_circuit_assembler` | 1 |
| `gtceu:lv_robot_arm` | 2 |
| `gtceu:item_filter` | 2 |
| `functionalstorage:oak_1` | 5 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [LV circuit line (Basic Electronic Circuit)](../lv/comp_circuit_lv.md), [Phenolic printed circuit board (silver foil + etching)](mv_board.md), [Diodes (gallium arsenide + glass + fine wire)](mv_diode.md), [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md)
- **Feeds:** [MV Robot Arm (uses the new circuits)](comp_mv_arm.md)
- **Main source for:** `gtceu:good_electronic_circuit`
