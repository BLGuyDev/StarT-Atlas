---
kind: chain
id: comp_circuit_lv
order: 850
data:
  t: LV circuit line (Basic Electronic Circuit)
  inf: true
  "n":
    - [oak, "Oak tree extractor · resin", s, "start_core:large_arboreal_extractor"]
    - [chd, Charcoal dust, i, "gtceu:charcoal_dust"]
    - [mx, Mixer, m, "gtceu:lv_mixer"]
    - [gl, Glue, f, "gtceu:glue_bucket"]
    - [fo, "4 Copper foil", i, "gtceu:copper_foil"]
    - [wp, "Wood plate (3 slabs)", i, "gtceu:wood_plate"]
    - [a1, "Assembler · board", m, "gtceu:lv_assembler"]
    - [bd, Circuit board, x, "gtceu:resin_printed_circuit_board"]
    - [fw, "4 Fine copper wire", i, "gtceu:fine_copper_wire"]
    - [a2, "Assembler · resistors", m, "gtceu:lv_assembler"]
    - [rs, "2 Resistors", x, "gtceu:resistor"]
    - [gt, "Glass tube (6 panes → 2)", i, "gtceu:glass_tube"]
    - [bo, "Steel bolt + 2 copper wire", i, "gtceu:steel_bolt"]
    - [ra, "18 mB red alloy", f, "gtceu:red_alloy_bucket"]
    - [a3, "Assembler · tubes", m, "gtceu:lv_assembler"]
    - [vt, "3 Vacuum tubes", x, "gtceu:vacuum_tube"]
    - [rw, "2 Red alloy wire", i, "gtceu:red_alloy_single_wire"]
    - [ca, Circuit Assembler, m, "gtceu:lv_circuit_assembler"]
    - [out, "2 LV circuits / 10 s", o, "gtceu:basic_electronic_circuit"]
  e:
    - [oak, mx, resin]
    - [chd, mx]
    - [mx, gl, "500 mB"]
    - [fo, a1]
    - [wp, a1]
    - [gl, a1, "100 mB"]
    - [a1, bd]
    - [fw, a2]
    - [chd, a2]
    - [gl, a2, "100 mB"]
    - [a2, rs]
    - [gt, a3]
    - [bo, a3]
    - [ra, a3]
    - [a3, vt]
    - [bd, ca, "1"]
    - [rs, ca, "2"]
    - [vt, ca, "2"]
    - [rw, ca, "2"]
    - [ca, out]
  tips:
    - |-
      Circuit Assembler: 1 board + 2 resistors + 2 vacuum tubes + 2 red alloy wires → 2 circuits (crafting by hand gives 1 and costs a steel plate).
    - |-
      Glue is the only farmed input: about 100 mB per circuit. One oak extractor (300 mB resin per minute, 750 with fertilizer) feeds 3–7 circuits per minute.
    - Annealed copper later doubles resistors (4 per craft) and vacuum tubes (4).
  b:
    - ["start_core:large_arboreal_extractor", 1]
    - ["gtceu:lv_mixer", 1]
    - ["gtceu:lv_assembler", 3]
    - ["gtceu:lv_circuit_assembler", 1]
    - ["gtceu:lv_extractor", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["functionalstorage:oak_1", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
  how:
    - i: ["start_core:large_arboreal_extractor", "minecraft:oak_log"]
      t: |-
        Glue source: a Large Arboreal Extractor built with oak logs and leaves gives resin instead of latex (same 100 mB per 20 s, 250 with fertilizer and an iron screw).
    - i: ["gtceu:lv_mixer", "gtceu:charcoal_dust", "gtceu:glue_bucket"]
      t: |-
        LV Mixer: 500 mB resin + 1 charcoal dust → 500 mB glue (no power: a barrel gives only 200 mB). Charcoal dust: macerate charcoal.
    - i: ["gtceu:lv_bender", "gtceu:copper_foil", "gtceu:wood_plate"]
      t: |-
        Board assembler: 4 copper foil (bender: 1 copper → 4 foil) + 1 wood plate (3 wooden slabs in a crafting row) + 100 mB glue → 1 circuit board in 10 s.
    - i: ["gtceu:resistor", "gtceu:fine_copper_wire"]
      t: |-
        Resistor assembler: 1 charcoal dust + 4 fine copper wire (wiremill circuit 3: 1 copper → 8) + 100 mB glue → 2 resistors in 8 s.
    - i: ["gtceu:vacuum_tube", "gtceu:glass_tube", "gtceu:lv_extractor"]
      t: |-
        Tube assembler: 1 glass tube + 1 steel bolt + 2 copper wires + 18 mB molten red alloy (extractor: 1 red alloy ingot → 144 mB) → 3 vacuum tubes in 2 s. Glass tubes: 6 glass panes → 2 by hand, in big batches.
    - i: ["gtceu:lv_circuit_assembler", "gtceu:red_alloy_single_wire", "gtceu:basic_electronic_circuit"]
      t: |-
        Circuit Assembler: 1 board + 2 resistors + 2 vacuum tubes + 2 red alloy wires → 2 LV circuits every 10 s at 16 EU/t (12 per minute). Robot Arm cover on Keep Exact 64.
---
# LV circuit line (Basic Electronic Circuit)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_circuit_lv` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV circuits](../../plan/p4.md#lvcirc)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Oak tree extractor · resin (start_core:large_arboreal_extractor) - resin"><img class="gt-ico" src="../../assets/icons/start_core__large_arboreal_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Arboreal Extractor</span><span class="gt-note">Oak tree extractor · resin</span><span class="gt-tag">infinite</span><b class="gt-q">resin</b></span><span class="gt-slot" title="Charcoal dust (gtceu:charcoal_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__charcoal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Glue (gtceu:glue_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glue</span><b class="gt-q">500 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembler · board</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Copper foil (gtceu:copper_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Foil</span><span class="gt-note">4 Copper foil</span></span><span class="gt-slot" title="Wood plate (3 slabs) (gtceu:wood_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Plate</span><span class="gt-note">Wood plate (3 slabs)</span></span><span class="gt-slot gt-fluid" title="Glue (gtceu:glue_bucket) - 100 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glue</span><b class="gt-q">100 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Circuit board (gtceu:resin_printed_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__resin_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resin Printed Circuit Board</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembler · resistors</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Fine copper wire (gtceu:fine_copper_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__fine_copper_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Copper Wire</span><span class="gt-note">4 Fine copper wire</span></span><span class="gt-slot" title="Charcoal dust (gtceu:charcoal_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__charcoal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal Dust</span></span><span class="gt-slot gt-fluid" title="Glue (gtceu:glue_bucket) - 100 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glue</span><b class="gt-q">100 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Resistors (gtceu:resistor)"><img class="gt-ico" src="../../assets/icons/gtceu__resistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resistor</span><span class="gt-note">2 Resistors</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembler · tubes</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Glass tube (6 panes → 2) (gtceu:glass_tube)"><img class="gt-ico" src="../../assets/icons/gtceu__glass_tube.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass Tube</span><span class="gt-note">Glass tube (6 panes → 2)</span></span><span class="gt-slot" title="Steel bolt + 2 copper wire (gtceu:steel_bolt)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_bolt.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Bolt</span><span class="gt-note">Steel bolt + 2 copper wire</span></span><span class="gt-slot gt-fluid" title="18 mB red alloy (gtceu:red_alloy_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__red_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Red Alloy</span><span class="gt-note">18 mB red alloy</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="3 Vacuum tubes (gtceu:vacuum_tube)"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_tube.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Tube</span><span class="gt-note">3 Vacuum tubes</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-ca">
<div class="gt-head"><span class="gt-mname">Circuit Assembler</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Circuit board (gtceu:resin_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__resin_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resin Printed Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Resistors (gtceu:resistor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__resistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resistor</span><span class="gt-note">2 Resistors</span><b class="gt-q">2</b></span><span class="gt-slot" title="3 Vacuum tubes (gtceu:vacuum_tube) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_tube.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Tube</span><span class="gt-note">3 Vacuum tubes</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 Red alloy wire (gtceu:red_alloy_single_wire) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__red_alloy_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Red Alloy Single Wire</span><span class="gt-note">2 Red alloy wire</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 LV circuits / 10 s (gtceu:basic_electronic_circuit)"><img class="gt-ico" src="../../assets/icons/gtceu__basic_electronic_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basic Electronic Circuit</span><span class="gt-note">2 LV circuits / 10 s</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_circuit_assembler</code></div>
</div>
</div>

## Flow

- [Mixer](#m-mx) → [Assembler · board](#m-a1) → [Circuit Assembler](#m-ca) (also Mixer → [Assembler · resistors](#m-a2))
- [Assembler · tubes](#m-a3) → [Circuit Assembler](#m-ca)
- [Assembler · resistors](#m-a2) → [Circuit Assembler](#m-ca)

## How to build

1. Glue source: a Large Arboreal Extractor built with oak logs and leaves gives resin instead of latex (same 100 mB per 20 s, 250 with fertilizer and an iron screw). — `start_core:large_arboreal_extractor`, `minecraft:oak_log`
2. LV Mixer: 500 mB resin + 1 charcoal dust → 500 mB glue (no power: a barrel gives only 200 mB). Charcoal dust: macerate charcoal. — `gtceu:lv_mixer`, `gtceu:charcoal_dust`, `gtceu:glue_bucket`
3. Board assembler: 4 copper foil (bender: 1 copper → 4 foil) + 1 wood plate (3 wooden slabs in a crafting row) + 100 mB glue → 1 circuit board in 10 s. — `gtceu:lv_bender`, `gtceu:copper_foil`, `gtceu:wood_plate`
4. Resistor assembler: 1 charcoal dust + 4 fine copper wire (wiremill circuit 3: 1 copper → 8) + 100 mB glue → 2 resistors in 8 s. — `gtceu:resistor`, `gtceu:fine_copper_wire`
5. Tube assembler: 1 glass tube + 1 steel bolt + 2 copper wires + 18 mB molten red alloy (extractor: 1 red alloy ingot → 144 mB) → 3 vacuum tubes in 2 s. Glass tubes: 6 glass panes → 2 by hand, in big batches. — `gtceu:vacuum_tube`, `gtceu:glass_tube`, `gtceu:lv_extractor`
6. Circuit Assembler: 1 board + 2 resistors + 2 vacuum tubes + 2 red alloy wires → 2 LV circuits every 10 s at 16 EU/t (12 per minute). Robot Arm cover on Keep Exact 64. — `gtceu:lv_circuit_assembler`, `gtceu:red_alloy_single_wire`, `gtceu:basic_electronic_circuit`

## Tips

- Circuit Assembler: 1 board + 2 resistors + 2 vacuum tubes + 2 red alloy wires → 2 circuits (crafting by hand gives 1 and costs a steel plate).
- Glue is the only farmed input: about 100 mB per circuit. One oak extractor (300 mB resin per minute, 750 with fertilizer) feeds 3–7 circuits per minute.
- Annealed copper later doubles resistors (4 per craft) and vacuum tubes (4).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:large_arboreal_extractor` | 1 |
| `gtceu:lv_mixer` | 1 |
| `gtceu:lv_assembler` | 3 |
| `gtceu:lv_circuit_assembler` | 1 |
| `gtceu:lv_extractor` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `functionalstorage:oak_1` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md), [Parts row 2: wires, fine wire, cables](comp_wires.md), [Parts row 1: rods, plates, bolts, gears](comp_parts.md)
- **Feeds:** [LV Robot Arm line](comp_robot_arm.md), [MV circuit line (Good Electronic Circuit)](../mv/mv_circuit.md)
- **Main source for:** `gtceu:basic_electronic_circuit`
