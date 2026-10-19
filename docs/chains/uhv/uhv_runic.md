---
kind: chain
id: uhv_runic
order: 1940
data:
  t: |-
    Runic circuits: board → etched board → convergence unit → runic processor (ZPM) → runic assembly (UV) → runic computer (UHV); the pack adds them to the circuit tags
  inf: true
  "n":
    - - g1
      - |-
        32 wetware board · enriched naquadah fluid cell · ZPM pump · ZPM sensor · 2 LuV circuit · 16 naquadah alloy foil · 7.5 B infusion
      - g
      - functionalstorage:oak_1
      - - [Wetware circuit board, "gtceu:wetware_circuit_board"]
        - [Naquadah alloy foil, "gtceu:naquadah_alloy_foil"]
        - [Runic convergence infusion, "gtceu:runic_convergence_infusion_bucket"]
    - - a1
      - Circuit Assembler · 60 s · 122 880 EU/t · STERILE → 32 runic circuit board
      - m
      - gtceu:zpm_circuit_assembler
    - - pb
      - |-
        Runic printed circuit board (etched: sterile chemical reactor 105 s, 16 YBCO foil + 5 B cupric chloride)
      - x
      - kubejs:runic_printed_circuit_board
    - - g2
      - printed board · 4 UHPIC · 8 small PEEK pipe · 8 trinaquadalloy plate · 16 PBI foil · 8 zircalloy-4 bolt · 250 mB infusion
      - g
      - functionalstorage:oak_1
      - [[UHPIC chip, "gtceu:uhpic_chip"], [Trinaquadalloy plate, "gtceu:trinaquadalloy_plate"]]
    - [a2, "Circuit Assembler · 30 s · 491 520 EU/t · STERILE", m, "gtceu:uv_circuit_assembler"]
    - [cu, Runic convergence processing unit, x, "kubejs:runic_convergence_processing_unit"]
    - - g3
      - unit · crystal SoC · advanced SoC · 8 living capacitor · 8 living transistor · 8 fine europium wire
      - g
      - functionalstorage:oak_1
      - [[Crystal SoC, "gtceu:crystal_soc"], [Advanced SoC, "gtceu:advanced_soc"]]
    - [a3, "Circuit Assembler · 10 s · 120 000 EU/t · Cleanroom", m, "gtceu:zpm_circuit_assembler"]
    - [rp, "Runic processor (ZPM circuit)", x, "kubejs:runic_processor"]
    - - g4
      - board · 2 processor · 4 ancient runicalium bolt · 6 living inductor · 12 capacitor · 16 QRAM · 16 fine europium wire · 576 mB ITLC + 216 mB PEEK + 500 mB infusion
      - g
      - functionalstorage:oak_1
      - [[Ancient runicalium bolt, "gtceu:ancient_runicalium_bolt"]]
    - [a4, "Assembly Line · 20 s · 240 000 EU/t · 128 CWU/t", m, "gtceu:assembly_line"]
    - [ra, "Runic processor assembly (UV circuit)", x, "kubejs:runic_processor_assembly"]
    - - g5
      - board · 2 assembly · 8 living diode · 24 QRAM · 8 hyper NOR · 16 hyper NAND · 32 fine europium · 32 PEEK foil · 4 tiny pipe · 2 naquadah alloy plate · 1152 + 576 + 750 mB
      - g
      - functionalstorage:oak_1
      - - [Hyper NOR chip, "kubejs:hyper_nor_memory_chip"]
        - [Hyper NAND chip, "kubejs:hyper_nand_memory_chip"]
        - [PEEK foil, "gtceu:polyether_ether_ketone_foil"]
    - [a5, "Assembly Line · 40 s · 240 000 EU/t · 128 CWU/t", m, "gtceu:assembly_line"]
  e:
    - [g1, a1, "1"]
    - [a1, pb, "1 + etch"]
    - [pb, g2, "1"]
    - [g2, a2, "1"]
    - [a2, cu, "1"]
    - [cu, g3, "1"]
    - [g3, a3, "1"]
    - [a3, rp, "1"]
    - [pb, g4, "1"]
    - [rp, g4, "2"]
    - [g4, a4, "1"]
    - [a4, ra, "1"]
    - [ra, g5, "2"]
    - [g5, a5, "1"]
  tips:
    - |-
      Source: kjs circuits.js, circuit_etching.js, utils/tags.js (verified numbers). Tags: circuits/zpm gets kubejs:runic_processor, circuits/uv gets kubejs:runic_processor_assembly, circuits/uhv gets kubejs:runic_processor_computer and circuits/uev the mainframe, so the runic line is a full alternative to the quantum, crystal and wetware routes. Runic circuit board: circuit assembler, sterile cleanroom, 1200 ticks at VA[ZPM] = 122 880 EU/t, 32 wetware circuit boards + 1 enriched naquadah fluid cell + 1 ZPM pump + 1 ZPM sensor + 2 LuV circuits + 16 naquadah alloy foil + 7500 mB runic convergence infusion → 32 boards. Etching (sterile chemical reactor): board + 16 YBCO foil + 5000 mB cupric chloride (10 B iron III chloride, 20 B persulfate), 2100 ticks, 1920 EU/t.
    - |-
      Convergence processing unit (circuit assembler, sterile, 600 ticks at VA[UV]): printed board + 4 UHPIC chips + 8 small PEEK fluid pipes + 8 trinaquadalloy plates + 16 PBI foil + 8 zircalloy-4 bolts + 250 mB infusion. Runic processor (circuit assembler, cleanroom, 200 ticks at 120 000 EU/t, 3 per craft output): unit + crystal SoC + advanced SoC + 8 living capacitors + 8 living transistors + 8 fine europium wire. Runic assembly (Assembly Line, 400 ticks at 240 000 EU/t, station research of the processor at 128 CWU/t and 120 000 EU/t): printed board + 2 processors + 4 ancient runicalium bolts + 6 living inductors + 12 living capacitors + 16 QRAM + 16 fine europium wire, 576 mB ITLC + 216 mB PEEK + 500 mB infusion. Runic computer (800 ticks at 240 000 EU/t, research of the assembly at 128 CWU/t and 160 000 EU/t): board + 2 assemblies + 8 living diodes + 24 QRAM + 8 hyper NOR + 16 hyper NAND chips + 32 fine europium wire + 32 PEEK foil + 4 tiny enriched naquadah pipes + 2 naquadah alloy plates, 1152 mB ITLC + 576 mB PEEK + 750 mB infusion.
    - |-
      Comparison: the runic assembly is a UV circuit and the runic computer a UHV circuit with 2 assemblies each, but they cost the infusion line (uhv_runic_infusion), hyper NOR / NAND wafers (chemical reactor with strontium titanium oxide + carbon: kjs circuits.js, 1200 ticks) and ancient runicalium (a gate-line metal: Unverified). The wetware mainframe is also a UHV circuit, so the runic computer is only a substitute at UHV; but the runic MAINFRAME (the first UEV circuit, uev_circuits) is needed already in the UHV era: it requires no UEV machine (Assembly Line 600 000 EU/t, 1800 ticks, UHV 1A hatch is enough) and the UHV Fusion Reactor (4 UEV circuits), the Ancient Stargate Generator (about 96) and the Folding Akreyrium Stabiliser chain depend on it. The mainframe uses UHPIC chips (4), not UEPIC, and 24 of each living SMD type (32 capacitors).
    - |-
      Sub-steps people skip: (1) three different data items for research: the runic processor, the assembly and the computer must each be kept as scan items; (2) the etched board is a sterile recipe; (3) 7.5 B of infusion for 32 boards; (4) living SMDs again (uv_living_smd).
    - |-
      Unverified: ancient runicalium source, the hyper wafer line, UV circuit assembler recipe (one machine tier per recipe EU).
  b:
    - ["gtceu:zpm_circuit_assembler", 2]
    - ["gtceu:uv_circuit_assembler", 1]
    - ["gtceu:ev_chemical_reactor", 1]
    - ["gtceu:assembly_line", 2]
    - ["gtceu:research_station", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:wetware_circuit_board
        - gtceu:ancient_runicalium_bolt
        - kubejs:hyper_nor_memory_chip
      t: |-
        Drawers first, one per input: wetware boards (32), ZPM pumps / sensors, LuV circuits, foils, UHPIC chips, PEEK pipes and foil, SoCs, living SMDs, QRAM, hyper chips, europium wire. Drums: infusion, cupric chloride or iron III chloride, ITLC, PEEK.
    - i: ["gtceu:zpm_circuit_assembler", "kubejs:runic_printed_circuit_board"]
      t: Board assembler (sterile cleanroom) then the etching reactor (also sterile); 32 boards per run, one printed board per later step.
    - i: ["gtceu:uv_circuit_assembler", "kubejs:runic_convergence_processing_unit"]
      t: |-
        Unit assembler (sterile, UV tier), then the processor assembler in a normal cleanroom: 3 processors per run.
    - i: ["gtceu:assembly_line", "kubejs:runic_processor_assembly"]
      t: |-
        Assembly Line: research of the runic processor (128 CWU/t) then the assembly recipe.
    - i: ["gtceu:assembly_line", "kubejs:runic_processor_computer"]
      t: |-
        Second Assembly Line for the computer: 2 assemblies per craft, research of the assembly.
    - i: ["functionalstorage:oak_1", "kubejs:runic_processor_computer"]
      t: Output drawers Keep Exact 4; the UHV runic computer substitutes for a wetware mainframe in any UHV circuit slot.
---
# Runic circuits: board → etched board → convergence unit → runic processor (ZPM) → runic assembly (UV) → runic computer (UHV); the pack adds them to the circuit tags

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_runic` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Runic infusion and runic circuits](../../plan/p17.md#uhvcirc)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-a1">
<div class="gt-head"><span class="gt-mname">Circuit Assembler · 60 s · 122 880 EU/t · STERILE → 32 runic circuit board</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="32 wetware board · enriched naquadah fluid cell · ZPM pump · ZPM sensor · 2 LuV circuit · 16 naquadah alloy foil · 7.5 B infusion (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">32 wetware board · enriched naquadah fluid cell · ZPM pump · ZPM sensor · 2 LuV circuit · 16 naquadah alloy foil · 7.5 B infusion</span><span class="gt-sub"><span>Wetware circuit board</span><span>Naquadah alloy foil</span><span>Runic convergence infusion</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Runic printed circuit board (etched: sterile chemical reactor 105 s, 16 YBCO foil + 5 B cupric chloride) (kubejs:runic_printed_circuit_board) - 1 + etch"><img class="gt-ico" src="../../assets/icons/kubejs__runic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Printed Circuit Board</span><span class="gt-note">Runic printed circuit board (etched: sterile chemical reactor 105 s, 16 YBCO foil + 5 B cupric chloride)</span><b class="gt-q">1 + etch</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
<div class="gt-panel t-uv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Circuit Assembler · 30 s · 491 520 EU/t · STERILE</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="printed board · 4 UHPIC · 8 small PEEK pipe · 8 trinaquadalloy plate · 16 PBI foil · 8 zircalloy-4 bolt · 250 mB infusion (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">printed board · 4 UHPIC · 8 small PEEK pipe · 8 trinaquadalloy plate · 16 PBI foil · 8 zircalloy-4 bolt · 250 mB infusion</span><span class="gt-sub"><span>UHPIC chip</span><span>Trinaquadalloy plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Runic convergence processing unit (kubejs:runic_convergence_processing_unit) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__runic_convergence_processing_unit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Convergence Processing Unit</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a3">
<div class="gt-head"><span class="gt-mname">Circuit Assembler · 10 s · 120 000 EU/t · Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="unit · crystal SoC · advanced SoC · 8 living capacitor · 8 living transistor · 8 fine europium wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">unit · crystal SoC · advanced SoC · 8 living capacitor · 8 living transistor · 8 fine europium wire</span><span class="gt-sub"><span>Crystal SoC</span><span>Advanced SoC</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Runic processor (ZPM circuit) (kubejs:runic_processor) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__runic_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Processor</span><span class="gt-note">Runic processor (ZPM circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 240 000 EU/t · 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="board · 2 processor · 4 ancient runicalium bolt · 6 living inductor · 12 capacitor · 16 QRAM · 16 fine europium wire · 576 mB ITLC + 216 mB PEEK + 500 mB infusion (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">board · 2 processor · 4 ancient runicalium bolt · 6 living inductor · 12 capacitor · 16 QRAM · 16 fine europium wire · 576 mB ITLC + 216 mB PEEK + 500 mB infusion</span><span class="gt-sub"><span>Ancient runicalium bolt</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Runic processor assembly (UV circuit) (kubejs:runic_processor_assembly) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__runic_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Processor Assembly</span><span class="gt-note">Runic processor assembly (UV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a5">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s · 240 000 EU/t · 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="board · 2 assembly · 8 living diode · 24 QRAM · 8 hyper NOR · 16 hyper NAND · 32 fine europium · 32 PEEK foil · 4 tiny pipe · 2 naquadah alloy plate · 1152 + 576 + 750 mB (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">board · 2 assembly · 8 living diode · 24 QRAM · 8 hyper NOR · 16 hyper NAND · 32 fine europium · 32 PEEK foil · 4 tiny pipe · 2 naquadah alloy plate · 1152 + 576 + 750 mB</span><span class="gt-sub"><span>Hyper NOR chip</span><span>Hyper NAND chip</span><span>PEEK foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Circuit Assembler · 60 s · 122 880 EU/t · STERILE → 32 runic circuit board](#m-a1) → [Circuit Assembler · 30 s · 491 520 EU/t · STERILE](#m-a2) → [Circuit Assembler · 10 s · 120 000 EU/t · Cleanroom](#m-a3) → [Assembly Line · 20 s · 240 000 EU/t · 128 CWU/t](#m-a4) → [Assembly Line · 40 s · 240 000 EU/t · 128 CWU/t](#m-a5) (also Circuit Assembler · 60 s · 122 880 EU/t · STERILE → 32 runic circuit board → [Assembly Line · 20 s · 240 000 EU/t · 128 CWU/t](#m-a4))

### Direct steps

- Runic printed circuit board (etched: sterile chemical reactor 105 s, 16 YBCO foil + 5 B cupric chloride) → printed board · 4 UHPIC · 8 small PEEK pipe · 8 trinaquadalloy plate · 16 PBI foil · 8 zircalloy-4 bolt · 250 mB infusion (1)
- Runic convergence processing unit → unit · crystal SoC · advanced SoC · 8 living capacitor · 8 living transistor · 8 fine europium wire (1)
- Runic printed circuit board (etched: sterile chemical reactor 105 s, 16 YBCO foil + 5 B cupric chloride) → board · 2 processor · 4 ancient runicalium bolt · 6 living inductor · 12 capacitor · 16 QRAM · 16 fine europium wire · 576 mB ITLC + 216 mB PEEK + 500 mB infusion (1)
- Runic processor (ZPM circuit) → board · 2 processor · 4 ancient runicalium bolt · 6 living inductor · 12 capacitor · 16 QRAM · 16 fine europium wire · 576 mB ITLC + 216 mB PEEK + 500 mB infusion (2)
- Runic processor assembly (UV circuit) → board · 2 assembly · 8 living diode · 24 QRAM · 8 hyper NOR · 16 hyper NAND · 32 fine europium · 32 PEEK foil · 4 tiny pipe · 2 naquadah alloy plate · 1152 + 576 + 750 mB (2)

## How to build

1. Drawers first, one per input: wetware boards (32), ZPM pumps / sensors, LuV circuits, foils, UHPIC chips, PEEK pipes and foil, SoCs, living SMDs, QRAM, hyper chips, europium wire. Drums: infusion, cupric chloride or iron III chloride, ITLC, PEEK. — `functionalstorage:oak_1`, `gtceu:wetware_circuit_board`, `gtceu:ancient_runicalium_bolt`, `kubejs:hyper_nor_memory_chip`
2. Board assembler (sterile cleanroom) then the etching reactor (also sterile); 32 boards per run, one printed board per later step. — `gtceu:zpm_circuit_assembler`, `kubejs:runic_printed_circuit_board`
3. Unit assembler (sterile, UV tier), then the processor assembler in a normal cleanroom: 3 processors per run. — `gtceu:uv_circuit_assembler`, `kubejs:runic_convergence_processing_unit`
4. Assembly Line: research of the runic processor (128 CWU/t) then the assembly recipe. — `gtceu:assembly_line`, `kubejs:runic_processor_assembly`
5. Second Assembly Line for the computer: 2 assemblies per craft, research of the assembly. — `gtceu:assembly_line`, `kubejs:runic_processor_computer`
6. Output drawers Keep Exact 4; the UHV runic computer substitutes for a wetware mainframe in any UHV circuit slot. — `functionalstorage:oak_1`, `kubejs:runic_processor_computer`

## Tips

- Source: kjs circuits.js, circuit\_etching.js, utils/tags.js (verified numbers). Tags: circuits/zpm gets kubejs:runic\_processor, circuits/uv gets kubejs:runic\_processor\_assembly, circuits/uhv gets kubejs:runic\_processor\_computer and circuits/uev the mainframe, so the runic line is a full alternative to the quantum, crystal and wetware routes. Runic circuit board: circuit assembler, sterile cleanroom, 1200 ticks at VA\[ZPM\] = 122 880 EU/t, 32 wetware circuit boards + 1 enriched naquadah fluid cell + 1 ZPM pump + 1 ZPM sensor + 2 LuV circuits + 16 naquadah alloy foil + 7500 mB runic convergence infusion → 32 boards. Etching (sterile chemical reactor): board + 16 YBCO foil + 5000 mB cupric chloride (10 B iron III chloride, 20 B persulfate), 2100 ticks, 1920 EU/t.
- Convergence processing unit (circuit assembler, sterile, 600 ticks at VA\[UV\]): printed board + 4 UHPIC chips + 8 small PEEK fluid pipes + 8 trinaquadalloy plates + 16 PBI foil + 8 zircalloy-4 bolts + 250 mB infusion. Runic processor (circuit assembler, cleanroom, 200 ticks at 120 000 EU/t, 3 per craft output): unit + crystal SoC + advanced SoC + 8 living capacitors + 8 living transistors + 8 fine europium wire. Runic assembly (Assembly Line, 400 ticks at 240 000 EU/t, station research of the processor at 128 CWU/t and 120 000 EU/t): printed board + 2 processors + 4 ancient runicalium bolts + 6 living inductors + 12 living capacitors + 16 QRAM + 16 fine europium wire, 576 mB ITLC + 216 mB PEEK + 500 mB infusion. Runic computer (800 ticks at 240 000 EU/t, research of the assembly at 128 CWU/t and 160 000 EU/t): board + 2 assemblies + 8 living diodes + 24 QRAM + 8 hyper NOR + 16 hyper NAND chips + 32 fine europium wire + 32 PEEK foil + 4 tiny enriched naquadah pipes + 2 naquadah alloy plates, 1152 mB ITLC + 576 mB PEEK + 750 mB infusion.
- Comparison: the runic assembly is a UV circuit and the runic computer a UHV circuit with 2 assemblies each, but they cost the infusion line (uhv\_runic\_infusion), hyper NOR / NAND wafers (chemical reactor with strontium titanium oxide + carbon: kjs circuits.js, 1200 ticks) and ancient runicalium (a gate-line metal: Unverified). The wetware mainframe is also a UHV circuit, so the runic computer is only a substitute at UHV; but the runic MAINFRAME (the first UEV circuit, uev\_circuits) is needed already in the UHV era: it requires no UEV machine (Assembly Line 600 000 EU/t, 1800 ticks, UHV 1A hatch is enough) and the UHV Fusion Reactor (4 UEV circuits), the Ancient Stargate Generator (about 96) and the Folding Akreyrium Stabiliser chain depend on it. The mainframe uses UHPIC chips (4), not UEPIC, and 24 of each living SMD type (32 capacitors).
- Sub-steps people skip: (1) three different data items for research: the runic processor, the assembly and the computer must each be kept as scan items; (2) the etched board is a sterile recipe; (3) 7.5 B of infusion for 32 boards; (4) living SMDs again (uv\_living\_smd).
- **Unverified** ancient runicalium source, the hyper wafer line, UV circuit assembler recipe (one machine tier per recipe EU).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:zpm_circuit_assembler` | 2 |
| `gtceu:uv_circuit_assembler` | 1 |
| `gtceu:ev_chemical_reactor` | 1 |
| `gtceu:assembly_line` | 2 |
| `gtceu:research_station` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `kubejs:runic_processor`, `kubejs:runic_processor_assembly`, `kubejs:runic_processor_computer`, `kubejs:runic_printed_circuit_board`
