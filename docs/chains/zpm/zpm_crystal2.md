---
kind: chain
id: zpm_crystal2
order: 1370
data:
  t: |-
    ZPM circuit 2: Crystal Processor Supercomputer (elite board, crystal processor → assembly in the LCAF, computer in the Assembly Line)
  inf: true
  "n":
    - - f1
      - "2 fiber board · 8 palladium foil · 500 mB sulfuric acid"
      - g
      - functionalstorage:oak_1
      - - [Fiber board, "gtceu:fiber_reinforced_circuit_board"]
        - [Palladium foil, "gtceu:palladium_foil"]
        - [Sulfuric acid, "gtceu:sulfuric_acid_bucket"]
    - [m1, "HV Chemical Reactor in the cleanroom · 25 s · 480 EU/t", m, "gtceu:hv_chemical_reactor"]
    - - m2
      - MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride
      - m
      - gtceu:mv_chemical_reactor
    - [eb, Elite Circuit Board, x, "gtceu:multilayer_fiber_reinforced_printed_circuit_board"]
    - - p1
      - Crystal CPU · 2 nano CPU chip · 6 ASMD capacitor · 6 ASMD transistor · 8 fine NbTi wire
      - g
      - functionalstorage:oak_1
      - - [Crystal CPU, "gtceu:crystal_cpu"]
        - [Nano CPU chip, "gtceu:nano_cpu_chip"]
        - [ASMD capacitor, "gtceu:advanced_smd_capacitor"]
        - [ASMD transistor, "gtceu:advanced_smd_transistor"]
    - [m3, "LCAF + LuV hatch · 10 s · 9600 EU/t", m, "gtceu:large_circuit_assembler"]
    - [cp, "Crystal Processor (IV) · 2 per craft", x, "gtceu:crystal_processor"]
    - - p2
      - |-
        4 ASMD inductor · 8 ASMD capacitor · 24 RAM · 16 fine NbTi wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [ASMD inductor, "gtceu:advanced_smd_inductor"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Fine NbTi wire, "gtceu:fine_niobium_titanium_wire"]
    - [m4, "LCAF + LuV hatch · 20 s · 9600 EU/t", m, "gtceu:large_circuit_assembler"]
    - [ca, "Crystal Processor Assembly (LuV) · 2 per craft", x, "gtceu:crystal_processor_assembly"]
    - - p3
      - |-
        4 ASMD diode · 24 RAM · 16 NOR chip · 32 NAND chip · 24 fine NbTi wire · 576 mB soldering alloy
      - g
      - functionalstorage:oak_1
      - - [ASMD diode, "gtceu:advanced_smd_diode"]
        - [NOR memory chip, "gtceu:nor_memory_chip"]
        - [NAND memory chip, "gtceu:nand_memory_chip"]
    - [m5, "Assembly Line · 20 s · 30 720 EU/t (scan: crystal assembly)", m, "gtceu:assembly_line"]
    - [cz, "Crystal Processor Supercomputer (ZPM circuit)", o, "gtceu:crystal_processor_computer"]
  e:
    - [f1, m1, "1"]
    - [m1, m2, multilayer board]
    - [m2, eb, "1 / 75 s"]
    - [eb, m3, "1"]
    - [eb, m4, "1"]
    - [eb, m5, "1"]
    - [p1, m3, "1"]
    - [m3, cp, "2 / 10 s"]
    - [cp, m4, "2"]
    - [p2, m4, "1"]
    - [m4, ca, "2 / 20 s"]
    - [ca, m5, "2"]
    - [p3, m5, "1"]
    - [m5, cz, "1 / 20 s"]
  tips:
    - |-
      Why it is the SECOND ZPM circuit (quest subtitle) and not the first: it needs the crystal CPU (zpm_crystal, a 10 minute autoclave clock), advanced SMDs (zpm_asmd) and three elite boards, and a LuV-power circuit assembler. What it buys you: the same ZPM tag, and the UV crystal mainframe (2 crystal computers per mainframe + station research of the computer at 16 CWU/t) that the later gate chains eat. If you only need ZPM circuits for hatches and components, the quantum route (zpm_circuits) is cheaper.
    - |-
      Elite board (CircuitRecipes, not changed by the pack): multi-layer fiber board = 2 fiber boards + 8 palladium foil + 500 mB sulfuric acid, chemical reactor, CLEANROOM, 500 ticks at VA[HV] = 480 EU/t; elite circuit board = that + 8 platinum foil + 2000 mB iron III chloride (or 4000 mB sodium persulfate), cleanroom, 1500 ticks at VA[MV] = 120 EU/t. Fiber board is the same item as the first step of the extreme board in zpm_quantum. Per crystal computer you need 3 elite boards = 6 fiber boards + 24 palladium foil + 24 platinum foil + 6 B iron III chloride.
    - |-
      The three stages (CircuitRecipes, cleanroom, outputAmount 2 for the processor): Crystal Processor (IV) = elite board + 1 crystal CPU + 2 nano CPU chips + 6 advanced SMD capacitors + 6 advanced SMD transistors + 8 fine NbTi wire → 2, 200 ticks at 9600 EU/t. Crystal Assembly (LuV) = elite board + 2 processors + 4 advanced SMD inductors + 8 advanced SMD capacitors + 24 RAM + 16 fine NbTi wire + solder x2 → 2, 400 ticks at 9600 EU/t. 9600 EU/t is above an IV machine, so these two stages run in the Large Circuit Assembling Facility with a LuV energy hatch (luv_lcaf chain), or in a LuV circuit assembler if you build one.
    - |-
      The last step is a PACK recipe: kjs circuits.js removes the GT circuit-assembler recipe crystal_computer_zpm and the crystal mainframe, and adds crystal_processor_computer as an Assembly Line recipe: multi-layer fiber PRINTED board (the elite board) + 2 crystal processor assemblies + 4 advanced SMD diodes + 24 RAM + 16 NOR chips + 32 NAND chips + 24 fine niobium titanium wire, 576 mB soldering alloy, 400 ticks at 30 720 EU/t, scanner research of the crystal assembly (800 ticks at 7680 EU/t). Compare vanilla: 4 RAM + 32 NOR + 64 NAND + 32 NbTi: the pack trades chips for RAM and ASMDs.
    - |-
      Per ONE crystal computer (one ZPM circuit): 1 crystal CPU, 2 nano CPU chips, 3 elite boards, 6 ASMD capacitors + 6 transistors (processor craft), 4 inductors + 8 capacitors (assembly craft), 4 diodes (computer), 48 RAM chips, 16 NOR + 32 NAND chips, 48 fine niobium titanium wire (6 ingots) and about 288 mB tin + 576 mB soldering alloy. Compared with the quantum mainframe (64 RAM, 6 extreme boards, 120 platinum wire) it is lighter on chips but needs the slow crystal CPU.
    - |-
      Sub-steps people skip: (1) three machines again: LCAF twice (stages 1 and 2 are separate recipes, use two input drawer sets and a Parallel Hatch if you have one) and the Assembly Line for the computer; (2) the scan stick holds the crystal ASSEMBLY, not the processor; (3) elite board drawer feeds three recipes: Keep Exact 12, three routers; (4) NAND chips come 32 per wafer after cutting, so 1 wafer per computer, NOR 16 per wafer; (5) the nano CPU chips come from the luv_chips chain: 2 per computer.
    - |-
      Unverified: the Parallel Hatch accepting these recipes in the LCAF, the exact tin amount per stage (144 mB x2 per craft by the solder multiplier), and the wiremill yield of fine NbTi wire.
  b:
    - ["gtceu:large_circuit_assembler", 1]
    - ["gtceu:luv_energy_input_hatch", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:mv_chemical_reactor", 1]
    - ["gtceu:iv_scanner", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 20]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:crystal_cpu", "gtceu:advanced_smd_capacitor", "gtceu:palladium_foil"]
      t: |-
        Drawers first, one per input: fiber boards, palladium foil, platinum foil, crystal CPUs, nano CPU chips, ASMD capacitors, transistors, inductors, diodes, RAM, NOR, NAND, fine NbTi wire. Drums: sulfuric acid, iron III chloride, tin, soldering alloy. Every machine behind its own router with Item Filters, a Robot Arm cover in Keep Exact mode on each output.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:multilayer_fiber_reinforced_circuit_board"]
      t: |-
        Multilayer board (cleanroom): 2 fiber boards + 8 palladium foil + 500 mB sulfuric acid → 1 board in 25 s at 480 EU/t; one reactor, one product.
    - i:
        - gtceu:mv_chemical_reactor
        - gtceu:multilayer_fiber_reinforced_printed_circuit_board
        - gtceu:iron_iii_chloride_bucket
      t: |-
        Elite board (cleanroom): multilayer board + 8 platinum foil + 2 B iron III chloride → 1 elite board in 75 s at 120 EU/t. This is the slow step: 3 boards per computer, so a second reactor is worth it.
    - i: ["gtceu:large_circuit_assembler", "gtceu:crystal_processor", "gtceu:crystal_cpu"]
      t: |-
        Stage 1 in the LCAF (LuV hatch, cleanroom): elite board + crystal CPU + 2 nano CPU + 6 ASMD capacitors + 6 ASMD transistors + 8 fine NbTi wire → 2 processors in 10 s at 9600 EU/t.
    - i: ["gtceu:large_circuit_assembler", "gtceu:crystal_processor_assembly", "gtceu:ram_chip"]
      t: |-
        Stage 2: elite board + 2 processors + 4 ASMD inductors + 8 ASMD capacitors + 24 RAM + 16 fine NbTi wire + 288 mB tin → 2 assemblies in 20 s at 9600 EU/t. A second LCAF input set, or the same LCAF with an output filter between stages.
    - i: ["gtceu:iv_scanner", "gtceu:crystal_processor_assembly", "gtceu:data_stick"]
      t: Scan one crystal assembly at an IV Scanner (800 ticks, 7680 EU/t); the stick goes to the Assembly Line’s Data Access Hatch (zpm_data).
    - i: ["gtceu:assembly_line", "gtceu:crystal_processor_computer", "gtceu:nand_memory_chip"]
      t: |-
        Computer: Assembly Line buses in order: elite board, 2 assemblies, 4 ASMD diodes, 24 RAM, 16 NOR, 32 NAND, 24 fine NbTi wire; 576 mB soldering alloy → 1 crystal processor supercomputer in 20 s at 30 720 EU/t (the 4A hatch).
---
# ZPM circuit 2: Crystal Processor Supercomputer (elite board, crystal processor → assembly in the LCAF, computer in the Assembly Line)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_crystal2` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Crystal circuits and the UV circuit](../../plan/p12.md#zpmcrystal)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-m1">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor in the cleanroom · 25 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 fiber board · 8 palladium foil · 500 mB sulfuric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 fiber board · 8 palladium foil · 500 mB sulfuric acid</span><span class="gt-sub"><span>Fiber board</span><span>Palladium foil</span><span>Sulfuric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride (gtceu:mv_chemical_reactor) - multilayer board"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Chemical Reactor</span><span class="gt-note">MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride</span><b class="gt-q">multilayer board</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-m2">
<div class="gt-head"><span class="gt-mname">MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="HV Chemical Reactor in the cleanroom · 25 s · 480 EU/t (gtceu:hv_chemical_reactor) - multilayer board"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Chemical Reactor</span><span class="gt-note">HV Chemical Reactor in the cleanroom · 25 s · 480 EU/t</span><b class="gt-q">multilayer board</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Elite Circuit Board (gtceu:multilayer_fiber_reinforced_printed_circuit_board) - 1 / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__multilayer_fiber_reinforced_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multilayer Fiber Reinforced Printed Circuit Board</span><span class="gt-note">Elite Circuit Board</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">LCAF + LuV hatch · 10 s · 9600 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Elite Circuit Board (gtceu:multilayer_fiber_reinforced_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__multilayer_fiber_reinforced_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multilayer Fiber Reinforced Printed Circuit Board</span><span class="gt-note">Elite Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Crystal CPU · 2 nano CPU chip · 6 ASMD capacitor · 6 ASMD transistor · 8 fine NbTi wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Crystal CPU · 2 nano CPU chip · 6 ASMD capacitor · 6 ASMD transistor · 8 fine NbTi wire</span><span class="gt-sub"><span>Crystal CPU</span><span>Nano CPU chip</span><span>ASMD capacitor</span><span>ASMD transistor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Crystal Processor (IV) · 2 per craft (gtceu:crystal_processor) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor</span><span class="gt-note">Crystal Processor (IV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_circuit_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">LCAF + LuV hatch · 20 s · 9600 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Elite Circuit Board (gtceu:multilayer_fiber_reinforced_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__multilayer_fiber_reinforced_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multilayer Fiber Reinforced Printed Circuit Board</span><span class="gt-note">Elite Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot" title="Crystal Processor (IV) · 2 per craft (gtceu:crystal_processor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor</span><span class="gt-note">Crystal Processor (IV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="4 ASMD inductor · 8 ASMD capacitor · 24 RAM · 16 fine NbTi wire · 288 mB tin (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 ASMD inductor · 8 ASMD capacitor · 24 RAM · 16 fine NbTi wire · 288 mB tin</span><span class="gt-sub"><span>ASMD inductor</span><span>RAM chip</span><span>Fine NbTi wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Crystal Processor Assembly (LuV) · 2 per craft (gtceu:crystal_processor_assembly) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Assembly</span><span class="gt-note">Crystal Processor Assembly (LuV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_circuit_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 30 720 EU/t (scan: crystal assembly)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Elite Circuit Board (gtceu:multilayer_fiber_reinforced_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__multilayer_fiber_reinforced_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multilayer Fiber Reinforced Printed Circuit Board</span><span class="gt-note">Elite Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot" title="Crystal Processor Assembly (LuV) · 2 per craft (gtceu:crystal_processor_assembly) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Assembly</span><span class="gt-note">Crystal Processor Assembly (LuV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="4 ASMD diode · 24 RAM · 16 NOR chip · 32 NAND chip · 24 fine NbTi wire · 576 mB soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 ASMD diode · 24 RAM · 16 NOR chip · 32 NAND chip · 24 fine NbTi wire · 576 mB soldering alloy</span><span class="gt-sub"><span>ASMD diode</span><span>NOR memory chip</span><span>NAND memory chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crystal Processor Supercomputer (ZPM circuit) (gtceu:crystal_processor_computer) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Computer</span><span class="gt-note">Crystal Processor Supercomputer (ZPM circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [HV Chemical Reactor in the cleanroom · 25 s · 480 EU/t](#m-m1) → [MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride](#m-m2) → [LCAF + LuV hatch · 10 s · 9600 EU/t](#m-m3) → [LCAF + LuV hatch · 20 s · 9600 EU/t](#m-m4) → [Assembly Line · 20 s · 30 720 EU/t (scan: crystal assembly)](#m-m5) (also MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride → [LCAF + LuV hatch · 20 s · 9600 EU/t](#m-m4), MV Chemical Reactor in the cleanroom · 75 s · 120 EU/t · 8 platinum foil + 2 B iron III chloride → [Assembly Line · 20 s · 30 720 EU/t (scan: crystal assembly)](#m-m5))

## How to build

1. Drawers first, one per input: fiber boards, palladium foil, platinum foil, crystal CPUs, nano CPU chips, ASMD capacitors, transistors, inductors, diodes, RAM, NOR, NAND, fine NbTi wire. Drums: sulfuric acid, iron III chloride, tin, soldering alloy. Every machine behind its own router with Item Filters, a Robot Arm cover in Keep Exact mode on each output. — `functionalstorage:oak_1`, `gtceu:crystal_cpu`, `gtceu:advanced_smd_capacitor`, `gtceu:palladium_foil`
2. Multilayer board (cleanroom): 2 fiber boards + 8 palladium foil + 500 mB sulfuric acid → 1 board in 25 s at 480 EU/t; one reactor, one product. — `gtceu:hv_chemical_reactor`, `gtceu:multilayer_fiber_reinforced_circuit_board`
3. Elite board (cleanroom): multilayer board + 8 platinum foil + 2 B iron III chloride → 1 elite board in 75 s at 120 EU/t. This is the slow step: 3 boards per computer, so a second reactor is worth it. — `gtceu:mv_chemical_reactor`, `gtceu:multilayer_fiber_reinforced_printed_circuit_board`, `gtceu:iron_iii_chloride_bucket`
4. Stage 1 in the LCAF (LuV hatch, cleanroom): elite board + crystal CPU + 2 nano CPU + 6 ASMD capacitors + 6 ASMD transistors + 8 fine NbTi wire → 2 processors in 10 s at 9600 EU/t. — `gtceu:large_circuit_assembler`, `gtceu:crystal_processor`, `gtceu:crystal_cpu`
5. Stage 2: elite board + 2 processors + 4 ASMD inductors + 8 ASMD capacitors + 24 RAM + 16 fine NbTi wire + 288 mB tin → 2 assemblies in 20 s at 9600 EU/t. A second LCAF input set, or the same LCAF with an output filter between stages. — `gtceu:large_circuit_assembler`, `gtceu:crystal_processor_assembly`, `gtceu:ram_chip`
6. Scan one crystal assembly at an IV Scanner (800 ticks, 7680 EU/t); the stick goes to the Assembly Line’s Data Access Hatch (zpm\_data). — `gtceu:iv_scanner`, `gtceu:crystal_processor_assembly`, `gtceu:data_stick`
7. Computer: Assembly Line buses in order: elite board, 2 assemblies, 4 ASMD diodes, 24 RAM, 16 NOR, 32 NAND, 24 fine NbTi wire; 576 mB soldering alloy → 1 crystal processor supercomputer in 20 s at 30 720 EU/t (the 4A hatch). — `gtceu:assembly_line`, `gtceu:crystal_processor_computer`, `gtceu:nand_memory_chip`

## Tips

- Why it is the SECOND ZPM circuit (quest subtitle) and not the first: it needs the crystal CPU (zpm\_crystal, a 10 minute autoclave clock), advanced SMDs (zpm\_asmd) and three elite boards, and a LuV-power circuit assembler. What it buys you: the same ZPM tag, and the UV crystal mainframe (2 crystal computers per mainframe + station research of the computer at 16 CWU/t) that the later gate chains eat. If you only need ZPM circuits for hatches and components, the quantum route (zpm\_circuits) is cheaper.
- Elite board (CircuitRecipes, not changed by the pack): multi-layer fiber board = 2 fiber boards + 8 palladium foil + 500 mB sulfuric acid, chemical reactor, CLEANROOM, 500 ticks at VA\[HV\] = 480 EU/t; elite circuit board = that + 8 platinum foil + 2000 mB iron III chloride (or 4000 mB sodium persulfate), cleanroom, 1500 ticks at VA\[MV\] = 120 EU/t. Fiber board is the same item as the first step of the extreme board in zpm\_quantum. Per crystal computer you need 3 elite boards = 6 fiber boards + 24 palladium foil + 24 platinum foil + 6 B iron III chloride.
- The three stages (CircuitRecipes, cleanroom, outputAmount 2 for the processor): Crystal Processor (IV) = elite board + 1 crystal CPU + 2 nano CPU chips + 6 advanced SMD capacitors + 6 advanced SMD transistors + 8 fine NbTi wire → 2, 200 ticks at 9600 EU/t. Crystal Assembly (LuV) = elite board + 2 processors + 4 advanced SMD inductors + 8 advanced SMD capacitors + 24 RAM + 16 fine NbTi wire + solder x2 → 2, 400 ticks at 9600 EU/t. 9600 EU/t is above an IV machine, so these two stages run in the Large Circuit Assembling Facility with a LuV energy hatch (luv\_lcaf chain), or in a LuV circuit assembler if you build one.
- The last step is a PACK recipe: kjs circuits.js removes the GT circuit-assembler recipe crystal\_computer\_zpm and the crystal mainframe, and adds crystal\_processor\_computer as an Assembly Line recipe: multi-layer fiber PRINTED board (the elite board) + 2 crystal processor assemblies + 4 advanced SMD diodes + 24 RAM + 16 NOR chips + 32 NAND chips + 24 fine niobium titanium wire, 576 mB soldering alloy, 400 ticks at 30 720 EU/t, scanner research of the crystal assembly (800 ticks at 7680 EU/t). Compare vanilla: 4 RAM + 32 NOR + 64 NAND + 32 NbTi: the pack trades chips for RAM and ASMDs.
- Per ONE crystal computer (one ZPM circuit): 1 crystal CPU, 2 nano CPU chips, 3 elite boards, 6 ASMD capacitors + 6 transistors (processor craft), 4 inductors + 8 capacitors (assembly craft), 4 diodes (computer), 48 RAM chips, 16 NOR + 32 NAND chips, 48 fine niobium titanium wire (6 ingots) and about 288 mB tin + 576 mB soldering alloy. Compared with the quantum mainframe (64 RAM, 6 extreme boards, 120 platinum wire) it is lighter on chips but needs the slow crystal CPU.
- Sub-steps people skip: (1) three machines again: LCAF twice (stages 1 and 2 are separate recipes, use two input drawer sets and a Parallel Hatch if you have one) and the Assembly Line for the computer; (2) the scan stick holds the crystal ASSEMBLY, not the processor; (3) elite board drawer feeds three recipes: Keep Exact 12, three routers; (4) NAND chips come 32 per wafer after cutting, so 1 wafer per computer, NOR 16 per wafer; (5) the nano CPU chips come from the luv\_chips chain: 2 per computer.
- **Unverified** the Parallel Hatch accepting these recipes in the LCAF, the exact tin amount per stage (144 mB x2 per craft by the solder multiplier), and the wiremill yield of fine NbTi wire.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_circuit_assembler` | 1 |
| `gtceu:luv_energy_input_hatch` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:mv_chemical_reactor` | 1 |
| `gtceu:iv_scanner` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 20 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Feeds:** [UV circuit: Crystal Processor Mainframe (2 crystal computers + advanced SMDs in the Assembly Line, station research 16 CWU/t) - 4 of them gate every ZPM multiblock](zpm_uv_circuit.md)
- **Main source for:** `gtceu:crystal_processor_computer`, `gtceu:crystal_processor_assembly`, `gtceu:crystal_processor`, `gtceu:multilayer_fiber_reinforced_printed_circuit_board`
