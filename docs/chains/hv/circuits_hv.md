---
kind: chain
id: circuits_hv
order: 310
data:
  t: |-
    HV circuits: Advanced Integrated Circuit and Microprocessor Assembly
  "n":
    - [sw, Silicon wafers, i, "gtceu:silicon_wafer"]
    - [le, "3 MV Laser Engravers (red / green / light blue lens)", m, "gtceu:mv_laser_engraver"]
    - [ic, ILC chips, x, "gtceu:ilc_chip"]
    - [rm, RAM chips, x, "gtceu:ram_chip"]
    - [cp, CPU chips, x, "gtceu:cpu_chip"]
    - [tr, Transistors, x, "gtceu:transistor"]
    - [c1, "LV Circuit Assembler · basic integrated", m, "gtceu:lv_circuit_assembler"]
    - [c2, "LV Circuit Assembler · good integrated", m, "gtceu:lv_circuit_assembler"]
    - [c3, "LV Circuit Assembler · advanced", m, "gtceu:lv_circuit_assembler"]
    - [ai, Advanced Integrated Circuit, o, "gtceu:advanced_integrated_circuit"]
    - [pb, Plastic printed board, i, "gtceu:plastic_printed_circuit_board"]
    - [m1, "MV Circuit Assembler · processor", m, "gtceu:mv_circuit_assembler"]
    - [m2, "MV Circuit Assembler · assembly", m, "gtceu:mv_circuit_assembler"]
    - [pa, Microprocessor Assembly, o, "gtceu:micro_processor_assembly"]
  e:
    - [sw, le]
    - [le, ic, "8 per wafer"]
    - [le, rm, "32 per wafer"]
    - [le, cp, "8 per wafer"]
    - [ic, c1, "1"]
    - [c1, c2, "2"]
    - [c2, c3, "2"]
    - [ic, c3, "2"]
    - [rm, c3, "2"]
    - [tr, c3, "4"]
    - [c3, ai, "40 s"]
    - [cp, m1]
    - [pb, m1]
    - [m1, m2, "2"]
    - [pb, m2]
    - [rm, m2, "4"]
    - [m2, pa, "20 s"]
  tips:
    - |-
      First HV circuit = Advanced Integrated Circuit. Its recipe has no cleanroom tag and runs on an LV Circuit Assembler: 2 good integrated + 2 ILC + 2 RAM + 4 transistors + 8 fine electrum wire + 8 annealed copper bolts + 144 mB tin, 40 s at 30 EU/t. You need it to build the MV Circuit Assembler (2 HV circuits).
    - |-
      Microprocessor Assembly is the second HV circuit and needs the MV Circuit Assembler: 1 plastic printed board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire (+288 mB tin), 20 s at 120 EU/t, gives 2.
    - |-
      All three chips come from silicon wafers: no cleanroom until phosphorus wafers (HV, 480 EU/t) and SoCs (600 EU/t and up). Every circuit assembler recipe also takes solder: 144 mB tin, or 72 mB soldering alloy.
    - |-
      Stock 32 of one type first: HV Assembler, Chemical Reactor and Mixer each take 2 HV circuits, the LCR 4, the MV Circuit Assembler 2, the cleanroom 1.
  b:
    - ["gtceu:lv_circuit_assembler", 3]
    - ["gtceu:mv_laser_engraver", 3]
    - ["gtceu:mv_cutter", 1]
    - ["gtceu:mv_assembler", 1]
    - ["gtceu:mv_circuit_assembler", 2]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
  how:
    - i: ["gtceu:silicon_boule", "gtceu:mv_cutter", "gtceu:silicon_wafer"]
      t: |-
        Wafers: EBF (cupronickel, MV hatch) 32 silicon dust + 1 small gallium arsenide dust, circuit 2, 1784 K, 120 EU/t, 7.5 min → 1 boule. MV Cutter: 1 boule → 16 wafers in 20 s at 64 EU/t with 20 mB lubricant (water: 80 mB and 40 s, distilled: 60 mB and 30 s). One boule per 7.5 min is the real cap: 2.1 wafers a minute.
    - i: ["gtceu:mv_laser_engraver", "gtceu:red_glass_lens", "gtceu:ilc_wafer"]
      t: |-
        Three MV Laser Engravers, one lens each, never swapped: red lens → ILC wafer, green lens → RAM wafer, light blue lens → CPU wafer. Each takes 1 silicon wafer, 45 s, 120 EU/t. A Robot Arm cover (Keep Exact 8) per engraver pushes the wafer into a drawer for the cutter.
    - i: ["gtceu:mv_cutter", "gtceu:ilc_chip", "gtceu:ram_chip", "gtceu:cpu_chip"]
      t: |-
        Cutting, same MV Cutter with lubricant: ILC wafer → 8 ILC chips (45 s, 64 EU/t, 45 mB), RAM wafer → 32 RAM chips (45 s, 96 EU/t, 67 mB), CPU wafer → 8 CPU chips (45 s, 120 EU/t, 84 mB). Chips go to three drawers; one advanced circuit uses 3 ILC and 2 RAM, so even one wafer lasts long.
    - i: ["gtceu:mv_assembler", "gtceu:transistor"]
      t: |-
        Transistors, one MV Assembler: 1 silicon plate + 6 fine tin wire + 144 mB polyethylene → 8 transistors in 8 s at 120 EU/t (60 a minute). Polyethylene is the MV plastic line; keep a drum of it beside the assembler.
    - i: ["gtceu:lv_circuit_assembler", "gtceu:basic_integrated_circuit"]
      t: |-
        Circuit Assembler 1 (basic integrated): LV circuit board (the resin one) + 1 ILC + 2 resistors + 2 diodes + 2 fine copper wire + 2 tin bolts → 2 circuits in 10 s at 16 EU/t, plus solder.
    - i: ["gtceu:lv_circuit_assembler", "gtceu:good_integrated_circuit", "gtceu:phenolic_printed_circuit_board"]
      t: |-
        Circuit Assembler 2 (good integrated): phenolic printed board (the MV silver-foil board) + 2 basic integrated + 2 resistors + 2 diodes + 4 fine gold wire + 4 silver bolts → 2 circuits in 20 s at 24 EU/t.
    - i: ["gtceu:lv_circuit_assembler", "gtceu:advanced_integrated_circuit", "gtceu:electrum_ingot"]
      t: |-
        Circuit Assembler 3 (advanced integrated): 2 good integrated + 2 ILC + 2 RAM + 4 transistors + 8 fine electrum wire (1 electrum ingot in a wiremill, circuit 3) + 8 annealed copper bolts → 1 circuit in 40 s at 30 EU/t. One machine gives 1.5 a minute. Each machine gets its own input drawers and an output drawer, with Robot Arm Keep Exact 64 on its output.
    - i: ["gtceu:mv_circuit_assembler", "gtceu:micro_processor", "gtceu:plastic_printed_circuit_board"]
      t: |-
        Second route, once an MV Circuit Assembler stands: plastic printed board + 1 CPU + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire → 2 microprocessors in 10 s at 60 EU/t. Plastic board: 1 polyethylene plate + 4 copper foil + 250 mB sulfuric acid → 1 board (25 s, 10 EU/t, chemical reactor), then 1 board + 6 copper foil + 250 mB iron III chloride (30 s, 30 EU/t) → printed board.
    - i: ["gtceu:mv_circuit_assembler", "gtceu:micro_processor_assembly", "gtceu:inductor"]
      t: |-
        Microprocessor Assembly, a second MV Circuit Assembler: plastic printed board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire, 288 mB tin → 2 assemblies in 20 s at 120 EU/t. Inductor: 1 steel ring + 2 fine copper wire + 36 mB polyethylene → 2 (MV assembler 16 s, 120 EU/t); capacitor: 1 polyethylene foil + 2 aluminium foil + 144 mB polyethylene → 8 (16 s).
    - i: ["functionalstorage:oak_1", "gtceu:advanced_integrated_circuit"]
      t: |-
        Easy to miss: the hand-crafted good circuit board is removed in this pack, so boards only come from the chemical reactor etch. Every circuit recipe also wants solder fluid: keep a 144 mB tin drum on each assembler or it stalls with all items present. Do not build the cleanroom for this step.
---
# HV circuits: Advanced Integrated Circuit and Microprocessor Assembly

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `circuits_hv`

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [SMDs and HV circuits](../../plan/p8.md#hvcirc)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-le">
<div class="gt-head"><span class="gt-mname">3 MV Laser Engravers (red / green / light blue lens)</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silicon wafers (gtceu:silicon_wafer)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Wafer</span><span class="gt-note">Silicon wafers</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ILC chips (gtceu:ilc_chip) - 8 per wafer"><img class="gt-ico" src="../../assets/icons/gtceu__ilc_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilc Chip</span><span class="gt-note">ILC chips</span><b class="gt-q">8 per wafer</b></span><span class="gt-slot" title="RAM chips (gtceu:ram_chip) - 32 per wafer"><img class="gt-ico" src="../../assets/icons/gtceu__ram_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">RAM Chip</span><span class="gt-note">RAM chips</span><b class="gt-q">32 per wafer</b></span><span class="gt-slot" title="CPU chips (gtceu:cpu_chip) - 8 per wafer"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Chip</span><span class="gt-note">CPU chips</span><b class="gt-q">8 per wafer</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_laser_engraver</code></div>
</div>
<div class="gt-panel t-lv" id="m-c1">
<div class="gt-head"><span class="gt-mname">LV Circuit Assembler · basic integrated</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ILC chips (gtceu:ilc_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ilc_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilc Chip</span><span class="gt-note">ILC chips</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-c2" title="LV Circuit Assembler · good integrated (gtceu:lv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Circuit Assembler</span><span class="gt-note">LV Circuit Assembler · good integrated</span><b class="gt-q">2</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-c2">
<div class="gt-head"><span class="gt-mname">LV Circuit Assembler · good integrated</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-c1" title="LV Circuit Assembler · basic integrated (gtceu:lv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Circuit Assembler</span><span class="gt-note">LV Circuit Assembler · basic integrated</span><b class="gt-q">2</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-c3" title="LV Circuit Assembler · advanced (gtceu:lv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Circuit Assembler</span><span class="gt-note">LV Circuit Assembler · advanced</span><b class="gt-q">2</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-c3">
<div class="gt-head"><span class="gt-mname">LV Circuit Assembler · advanced</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-c2" title="LV Circuit Assembler · good integrated (gtceu:lv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Circuit Assembler</span><span class="gt-note">LV Circuit Assembler · good integrated</span><b class="gt-q">2</b></a><span class="gt-slot" title="ILC chips (gtceu:ilc_chip) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__ilc_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilc Chip</span><span class="gt-note">ILC chips</span><b class="gt-q">2</b></span><span class="gt-slot" title="RAM chips (gtceu:ram_chip) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__ram_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">RAM Chip</span><span class="gt-note">RAM chips</span><b class="gt-q">2</b></span><span class="gt-slot" title="Transistors (gtceu:transistor) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__transistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Transistor</span><span class="gt-note">Transistors</span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Advanced Integrated Circuit (gtceu:advanced_integrated_circuit) - 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_integrated_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Integrated Circuit</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-mv" id="m-m1">
<div class="gt-head"><span class="gt-mname">MV Circuit Assembler · processor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="CPU chips (gtceu:cpu_chip)"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Chip</span><span class="gt-note">CPU chips</span></span><span class="gt-slot" title="Plastic printed board (gtceu:plastic_printed_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__plastic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plastic Printed Circuit Board</span><span class="gt-note">Plastic printed board</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="MV Circuit Assembler · assembly (gtceu:mv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Circuit Assembler</span><span class="gt-note">MV Circuit Assembler · assembly</span><b class="gt-q">2</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-mv" id="m-m2">
<div class="gt-head"><span class="gt-mname">MV Circuit Assembler · assembly</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="MV Circuit Assembler · processor (gtceu:mv_circuit_assembler) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Circuit Assembler</span><span class="gt-note">MV Circuit Assembler · processor</span><b class="gt-q">2</b></a><span class="gt-slot" title="Plastic printed board (gtceu:plastic_printed_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__plastic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plastic Printed Circuit Board</span><span class="gt-note">Plastic printed board</span></span><span class="gt-slot" title="RAM chips (gtceu:ram_chip) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__ram_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">RAM Chip</span><span class="gt-note">RAM chips</span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Microprocessor Assembly (gtceu:micro_processor_assembly) - 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Assembly</span><span class="gt-note">Microprocessor Assembly</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
</div>

## Flow

- [3 MV Laser Engravers (red / green / light blue lens)](#m-le) → [LV Circuit Assembler · basic integrated](#m-c1) → [LV Circuit Assembler · good integrated](#m-c2) → [LV Circuit Assembler · advanced](#m-c3) (also 3 MV Laser Engravers (red / green / light blue lens) → [LV Circuit Assembler · advanced](#m-c3), 3 MV Laser Engravers (red / green / light blue lens) → [MV Circuit Assembler · assembly](#m-m2), 3 MV Laser Engravers (red / green / light blue lens) → [MV Circuit Assembler · processor](#m-m1))
- [MV Circuit Assembler · processor](#m-m1) → [MV Circuit Assembler · assembly](#m-m2)

## How to build

1. Wafers: EBF (cupronickel, MV hatch) 32 silicon dust + 1 small gallium arsenide dust, circuit 2, 1784 K, 120 EU/t, 7.5 min → 1 boule. MV Cutter: 1 boule → 16 wafers in 20 s at 64 EU/t with 20 mB lubricant (water: 80 mB and 40 s, distilled: 60 mB and 30 s). One boule per 7.5 min is the real cap: 2.1 wafers a minute. — `gtceu:silicon_boule`, `gtceu:mv_cutter`, `gtceu:silicon_wafer`
2. Three MV Laser Engravers, one lens each, never swapped: red lens → ILC wafer, green lens → RAM wafer, light blue lens → CPU wafer. Each takes 1 silicon wafer, 45 s, 120 EU/t. A Robot Arm cover (Keep Exact 8) per engraver pushes the wafer into a drawer for the cutter. — `gtceu:mv_laser_engraver`, `gtceu:red_glass_lens`, `gtceu:ilc_wafer`
3. Cutting, same MV Cutter with lubricant: ILC wafer → 8 ILC chips (45 s, 64 EU/t, 45 mB), RAM wafer → 32 RAM chips (45 s, 96 EU/t, 67 mB), CPU wafer → 8 CPU chips (45 s, 120 EU/t, 84 mB). Chips go to three drawers; one advanced circuit uses 3 ILC and 2 RAM, so even one wafer lasts long. — `gtceu:mv_cutter`, `gtceu:ilc_chip`, `gtceu:ram_chip`, `gtceu:cpu_chip`
4. Transistors, one MV Assembler: 1 silicon plate + 6 fine tin wire + 144 mB polyethylene → 8 transistors in 8 s at 120 EU/t (60 a minute). Polyethylene is the MV plastic line; keep a drum of it beside the assembler. — `gtceu:mv_assembler`, `gtceu:transistor`
5. Circuit Assembler 1 (basic integrated): LV circuit board (the resin one) + 1 ILC + 2 resistors + 2 diodes + 2 fine copper wire + 2 tin bolts → 2 circuits in 10 s at 16 EU/t, plus solder. — `gtceu:lv_circuit_assembler`, `gtceu:basic_integrated_circuit`
6. Circuit Assembler 2 (good integrated): phenolic printed board (the MV silver-foil board) + 2 basic integrated + 2 resistors + 2 diodes + 4 fine gold wire + 4 silver bolts → 2 circuits in 20 s at 24 EU/t. — `gtceu:lv_circuit_assembler`, `gtceu:good_integrated_circuit`, `gtceu:phenolic_printed_circuit_board`
7. Circuit Assembler 3 (advanced integrated): 2 good integrated + 2 ILC + 2 RAM + 4 transistors + 8 fine electrum wire (1 electrum ingot in a wiremill, circuit 3) + 8 annealed copper bolts → 1 circuit in 40 s at 30 EU/t. One machine gives 1.5 a minute. Each machine gets its own input drawers and an output drawer, with Robot Arm Keep Exact 64 on its output. — `gtceu:lv_circuit_assembler`, `gtceu:advanced_integrated_circuit`, `gtceu:electrum_ingot`
8. Second route, once an MV Circuit Assembler stands: plastic printed board + 1 CPU + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire → 2 microprocessors in 10 s at 60 EU/t. Plastic board: 1 polyethylene plate + 4 copper foil + 250 mB sulfuric acid → 1 board (25 s, 10 EU/t, chemical reactor), then 1 board + 6 copper foil + 250 mB iron III chloride (30 s, 30 EU/t) → printed board. — `gtceu:mv_circuit_assembler`, `gtceu:micro_processor`, `gtceu:plastic_printed_circuit_board`
9. Microprocessor Assembly, a second MV Circuit Assembler: plastic printed board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire, 288 mB tin → 2 assemblies in 20 s at 120 EU/t. Inductor: 1 steel ring + 2 fine copper wire + 36 mB polyethylene → 2 (MV assembler 16 s, 120 EU/t); capacitor: 1 polyethylene foil + 2 aluminium foil + 144 mB polyethylene → 8 (16 s). — `gtceu:mv_circuit_assembler`, `gtceu:micro_processor_assembly`, `gtceu:inductor`
10. Easy to miss: the hand-crafted good circuit board is removed in this pack, so boards only come from the chemical reactor etch. Every circuit recipe also wants solder fluid: keep a 144 mB tin drum on each assembler or it stalls with all items present. Do not build the cleanroom for this step. — `functionalstorage:oak_1`, `gtceu:advanced_integrated_circuit`

## Tips

- First HV circuit = Advanced Integrated Circuit. Its recipe has no cleanroom tag and runs on an LV Circuit Assembler: 2 good integrated + 2 ILC + 2 RAM + 4 transistors + 8 fine electrum wire + 8 annealed copper bolts + 144 mB tin, 40 s at 30 EU/t. You need it to build the MV Circuit Assembler (2 HV circuits).
- Microprocessor Assembly is the second HV circuit and needs the MV Circuit Assembler: 1 plastic printed board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire (+288 mB tin), 20 s at 120 EU/t, gives 2.
- All three chips come from silicon wafers: no cleanroom until phosphorus wafers (HV, 480 EU/t) and SoCs (600 EU/t and up). Every circuit assembler recipe also takes solder: 144 mB tin, or 72 mB soldering alloy.
- Stock 32 of one type first: HV Assembler, Chemical Reactor and Mixer each take 2 HV circuits, the LCR 4, the MV Circuit Assembler 2, the cleanroom 1.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_circuit_assembler` | 3 |
| `gtceu:mv_laser_engraver` | 3 |
| `gtceu:mv_cutter` | 1 |
| `gtceu:mv_assembler` | 1 |
| `gtceu:mv_circuit_assembler` | 2 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |

## Needs / Feeds

- **Needs:** [Polyethylene](../mv/polyethylene.md)
- **Feeds:** [HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers](hv_components2.md)
- **Main source for:** `gtceu:advanced_integrated_circuit`, `gtceu:micro_processor_assembly`
