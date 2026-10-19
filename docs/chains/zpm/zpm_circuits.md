---
kind: chain
id: zpm_circuits
order: 1350
data:
  t: |-
    ZPM circuit: Quantum Processor Mainframe (processor → assembly → supercomputer in IV Circuit Assemblers, mainframe in the Assembly Line)
  inf: true
  "n":
    - - p1
      - Extreme board · qubit CPU chip · nano CPU chip · 12 SMD capacitor · 12 SMD transistor · 12 fine platinum wire
      - g
      - functionalstorage:oak_1
      - - [Extreme board, "gtceu:fiber_reinforced_printed_circuit_board"]
        - [Qubit CPU chip, "gtceu:qbit_cpu_chip"]
        - [Nano CPU chip, "gtceu:nano_cpu_chip"]
        - [Fine platinum wire, "gtceu:fine_platinum_wire"]
    - [m1, "IV Circuit Assembler in the cleanroom · 10 s · 2400 EU/t", m, "gtceu:iv_circuit_assembler"]
    - [qp, "Quantum Processor (EV) · 2 per craft", x, "gtceu:quantum_processor"]
    - - p2
      - Extreme board · 8 SMD inductor · 16 SMD capacitor · 4 RAM · 16 fine platinum wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [SMD inductor, "gtceu:smd_inductor"]
        - [SMD capacitor, "gtceu:smd_capacitor"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Tin, "gtceu:tin_bucket"]
    - [m2, "IV Circuit Assembler · 20 s · 2400 EU/t", m, "gtceu:iv_circuit_assembler"]
    - [qa, "Quantum Processor Assembly (IV) · 2 per craft", x, "gtceu:quantum_processor_assembly"]
    - - p3
      - Extreme board · 8 SMD diode · 4 NOR chip · 16 RAM · 32 fine platinum wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [SMD diode, "gtceu:smd_diode"]
        - [NOR memory chip, "gtceu:nor_memory_chip"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Fine platinum wire, "gtceu:fine_platinum_wire"]
    - [m3, "IV Circuit Assembler · 20 s · 2400 EU/t", m, "gtceu:iv_circuit_assembler"]
    - [qm, "Quantum Processor Supercomputer (LuV circuit)", x, "gtceu:quantum_processor_computer"]
    - - p4
      - |-
        2 HSS-G frame · 24 RAM · 2 HPIC chip · 8 ASMD inductor · 16 ASMD capacitor · 8 ASMD diode · 8 platinum single wire · 576 mB soldering alloy
      - g
      - functionalstorage:oak_1
      - - [HSS-G frame, "gtceu:hssg_frame"]
        - [HPIC chip, "gtceu:hpic_chip"]
        - [ASMD inductor, "gtceu:advanced_smd_inductor"]
        - [ASMD capacitor, "gtceu:advanced_smd_capacitor"]
        - [ASMD diode, "gtceu:advanced_smd_diode"]
    - [m4, "Assembly Line · 30 s · 30 720 EU/t (scan: quantum supercomputer)", m, "gtceu:assembly_line"]
    - [mf, "Quantum Processor Mainframe (ZPM circuit)", o, "gtceu:quantum_processor_mainframe"]
  e:
    - [p1, m1, "1"]
    - [m1, qp, "2 / 10 s"]
    - [qp, m2, "2"]
    - [p2, m2, "1"]
    - [m2, qa, "2 / 20 s"]
    - [qa, m3, "2"]
    - [p3, m3, "1"]
    - [m3, qm, "1 / 20 s"]
    - [qm, m4, "2"]
    - [p4, m4, "1"]
    - [m4, mf, "1 / 30 s"]
  tips:
    - |-
      What the era wants: the quest chapter calls the Quantum Processor Mainframe the FIRST ZPM circuit and the crystal processor computer the second (zpm_crystal); wetware processor assembly, runic processor and draconic microchip processor are the third to fifth. They are all in the #gtceu:circuits/zpm tag (kjs utils/tags.js adds the runic and draconic ones), so ONE route is enough for every recipe that says ZPM circuit. The quantum route needs no exotic ingredient and no sterile room: radon, plain boards, platinum wire.
    - |-
      The pack changed the last step: it REMOVES the circuit-assembler recipes quantum_mainframe_zpm (plain and asmd variants, with and without soldering alloy) and the crystal_computer_zpm ones (kjs circuits.js) and replaces the mainframe by an Assembly Line recipe: 2 HSS-G frames + 2 quantum processor supercomputers + 24 RAM chips + 2 HPIC chips + 8 advanced SMD inductors + 16 advanced SMD capacitors + 8 advanced SMD diodes + 8 platinum single wire, 576 mB soldering alloy, 600 ticks (30 s) at 30 720 EU/t, with SCANNER research of the quantum supercomputer (1200 ticks at 7680 EU/t). It needs an Assembly Line with the 4A hatch route (luv_hatches) and the data stick of the supercomputer.
    - |-
      The first three stages are the vanilla recipes (CircuitRecipes; harderCircuitRecipes is false so each craft of the first two stages gives 2): Quantum Processor (EV) = extreme board + 1 qubit CPU chip + 1 nano CPU chip + 12 SMD capacitors + 12 SMD transistors + 12 fine platinum wire → 2, 200 ticks at 2400 EU/t. Assembly (IV) = extreme board + 2 processors + 8 SMD inductors + 16 SMD capacitors + 4 RAM + 16 fine platinum wire + solder x2 → 2, 400 ticks at 2400 EU/t. Supercomputer (LuV, a LuV circuit as well) = extreme board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire + solder x2 → 1, 400 ticks. ALL carry the CLEANROOM tag. 2400 EU/t is above the EV cap (2048), so every stage needs the IV Circuit Assembler (the luv_lcaf chain), not the four EV ones of the nano line.
    - |-
      Cost of ONE mainframe: 2 supercomputers = 4 assemblies = 4 processors, i.e. 2 + 2 + 2 crafts: 6 extreme boards, 2 qubit CPU chips, 2 nano CPU chips, 56 SMD capacitors + 24 SMD transistors + 16 inductors + 16 diodes (plain), 64 RAM chips (2 wafers), 8 NOR chips, 120 fine platinum wire (15 platinum ingots), 2 HPIC chips, 2 HSS-G frames, 8 + 16 + 8 advanced SMDs, about 1 B tin in the three stages. Time per mainframe if nothing waits: 2 x 10 s + 2 x 20 s + 2 x 20 s + 30 s = 130 s, plus 6 min of extreme-board reactor time: boards are the bottleneck, not the assemblers.
    - |-
      Faster variants: the _asmd recipes of the three circuit-assembler stages swap SMDs for advanced SMDs (processor: 3 + 3 at 100 ticks; assembly: 2 inductors + 4 capacitors at 200 ticks; computer: 2 diodes at 200 ticks), halving the time and cutting the SMD load by 3/4. Since you build the zpm_asmd line anyway for the mainframe, use these variants as your normal routes.
    - |-
      RAM: 64 chips = 2 RAM wafers per mainframe (32 chips per wafer) plus 4 NOR chips per supercomputer; use the same chip lines as the luv_circuits chain and keep a RAM drawer with Keep Exact 64. HSS-G frames: one frame is 2 HSS-G ingots (the IV coil alloy line, abs_super_ebf chain); HPIC chips: iv_hatches chain.
    - |-
      Sub-steps people skip: (1) build the IV Circuit Assembler FIRST (2 LuV circuits) and the data stick scan of the supercomputer BEFORE the mainframe line; (2) the supercomputer is itself a LuV circuit and counts for every LuV recipe, so make extra and keep them apart from the stock reserved for mainframes; (3) three different extreme-board drawers are one drawer with three routers; (4) the Assembly Line must have the research stick in its Data Access Hatch AND the 4A power hatch; (5) soldering alloy 576 mB sits on a drum; tin 288 mB per stage on a separate one.
    - |-
      Unverified: that the pack leaves the quantum supercomputer recipes untouched (circuits.js removes only the ZPM and later ones and re-adds the mainframe; the earlier stages are not in its removal list), and the real throughput of one IV Circuit Assembler across three stages (use one machine per stage).
  b:
    - ["gtceu:iv_circuit_assembler", 3]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:iv_scanner", 1]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:iv_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:ram_chip
        - gtceu:fiber_reinforced_printed_circuit_board
        - gtceu:fine_platinum_wire
      t: |-
        Drawers first, one per input: extreme boards, qubit and nano CPU chips, RAM, NOR chips, SMD capacitors, transistors, inductors, diodes, fine platinum wire, HSS-G frames, HPIC chips, advanced SMDs. Two drums: tin (stage solder) and soldering alloy (mainframe). Each stage has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output so a stalled stage does not flood the next.
    - i: ["gtceu:iv_circuit_assembler", "gtceu:quantum_processor"]
      t: |-
        Stage 1, its own IV Circuit Assembler in the cleanroom: extreme board + qubit chip + nano chip + 12 SMD capacitors + 12 SMD transistors + 12 fine platinum wire → 2 quantum processors in 10 s at 2400 EU/t. 2 per craft, 4 per mainframe.
    - i: ["gtceu:iv_circuit_assembler", "gtceu:quantum_processor_assembly", "gtceu:smd_inductor"]
      t: |-
        Stage 2, its own machine: extreme board + 2 processors + 8 inductors + 16 capacitors + 4 RAM + 16 fine platinum wire + 288 mB tin → 2 assemblies in 20 s at 2400 EU/t (this is the IV circuit).
    - i: ["gtceu:iv_circuit_assembler", "gtceu:quantum_processor_computer", "gtceu:nor_memory_chip"]
      t: |-
        Stage 3, its own machine: extreme board + 2 assemblies + 8 diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire + 288 mB tin → 1 supercomputer in 20 s. This is the LuV circuit; drawer it with Keep Exact 8, two per mainframe.
    - i: ["gtceu:iv_scanner", "gtceu:quantum_processor_computer", "gtceu:data_stick"]
      t: |-
        Scan: a stick and one supercomputer in an IV Scanner (1200 ticks at 7680 EU/t) and the stick goes into the Assembly Line’s Data Access Hatch (zpm_data chain). You can scan with the first supercomputer you make.
    - i: ["gtceu:assembly_line", "gtceu:quantum_processor_mainframe", "gtceu:hssg_frame"]
      t: |-
        Mainframe: Assembly Line buses in recipe order: 2 HSS-G frames, 2 supercomputers, 24 RAM, 2 HPIC chips, 8 ASMD inductors, 16 ASMD capacitors, 8 ASMD diodes, 8 platinum single wire; 576 mB soldering alloy in the hatch. 30 s at 30 720 EU/t → 1 ZPM circuit.
    - i: ["functionalstorage:oak_1", "gtceu:quantum_processor_mainframe"]
      t: |-
        Easy to miss: the station needs about 50 ZPM circuits (zpm_research), hatches 1 each, field generators 2 each, ZPM Fusion MK I 4. Stock them before you plan anything, and start the boards and the RAM wafers of the second and third mainframe while the first one runs.
---
# ZPM circuit: Quantum Processor Mainframe (processor → assembly → supercomputer in IV Circuit Assemblers, mainframe in the Assembly Line)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_circuits` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM circuit (Quantum Mainframe)](../../plan/p12.md#zpmcirc)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-m1">
<div class="gt-head"><span class="gt-mname">IV Circuit Assembler in the cleanroom · 10 s · 2400 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Extreme board · qubit CPU chip · nano CPU chip · 12 SMD capacitor · 12 SMD transistor · 12 fine platinum wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Extreme board · qubit CPU chip · nano CPU chip · 12 SMD capacitor · 12 SMD transistor · 12 fine platinum wire</span><span class="gt-sub"><span>Extreme board</span><span>Qubit CPU chip</span><span>Nano CPU chip</span><span>Fine platinum wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Quantum Processor (EV) · 2 per craft (gtceu:quantum_processor) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor</span><span class="gt-note">Quantum Processor (EV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-m2">
<div class="gt-head"><span class="gt-mname">IV Circuit Assembler · 20 s · 2400 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Quantum Processor (EV) · 2 per craft (gtceu:quantum_processor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor</span><span class="gt-note">Quantum Processor (EV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Extreme board · 8 SMD inductor · 16 SMD capacitor · 4 RAM · 16 fine platinum wire · 288 mB tin (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Extreme board · 8 SMD inductor · 16 SMD capacitor · 4 RAM · 16 fine platinum wire · 288 mB tin</span><span class="gt-sub"><span>SMD inductor</span><span>SMD capacitor</span><span>RAM chip</span><span>Tin</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Quantum Processor Assembly (IV) · 2 per craft (gtceu:quantum_processor_assembly) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor Assembly</span><span class="gt-note">Quantum Processor Assembly (IV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-m3">
<div class="gt-head"><span class="gt-mname">IV Circuit Assembler · 20 s · 2400 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Quantum Processor Assembly (IV) · 2 per craft (gtceu:quantum_processor_assembly) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor Assembly</span><span class="gt-note">Quantum Processor Assembly (IV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Extreme board · 8 SMD diode · 4 NOR chip · 16 RAM · 32 fine platinum wire · 288 mB tin (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Extreme board · 8 SMD diode · 4 NOR chip · 16 RAM · 32 fine platinum wire · 288 mB tin</span><span class="gt-sub"><span>SMD diode</span><span>NOR memory chip</span><span>RAM chip</span><span>Fine platinum wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Quantum Processor Supercomputer (LuV circuit) (gtceu:quantum_processor_computer) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor Computer</span><span class="gt-note">Quantum Processor Supercomputer (LuV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (scan: quantum supercomputer)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Quantum Processor Supercomputer (LuV circuit) (gtceu:quantum_processor_computer) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor Computer</span><span class="gt-note">Quantum Processor Supercomputer (LuV circuit)</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="2 HSS-G frame · 24 RAM · 2 HPIC chip · 8 ASMD inductor · 16 ASMD capacitor · 8 ASMD diode · 8 platinum single wire · 576 mB soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 HSS-G frame · 24 RAM · 2 HPIC chip · 8 ASMD inductor · 16 ASMD capacitor · 8 ASMD diode · 8 platinum single wire · 576 mB soldering alloy</span><span class="gt-sub"><span>HSS-G frame</span><span>HPIC chip</span><span>ASMD inductor</span><span>ASMD capacitor</span><span>ASMD diode</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Quantum Processor Mainframe (ZPM circuit) (gtceu:quantum_processor_mainframe) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Processor Mainframe</span><span class="gt-note">Quantum Processor Mainframe (ZPM circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [IV Circuit Assembler in the cleanroom · 10 s · 2400 EU/t](#m-m1) → [IV Circuit Assembler · 20 s · 2400 EU/t](#m-m2) → [IV Circuit Assembler · 20 s · 2400 EU/t](#m-m3) → [Assembly Line · 30 s · 30 720 EU/t (scan: quantum supercomputer)](#m-m4)

## How to build

1. Drawers first, one per input: extreme boards, qubit and nano CPU chips, RAM, NOR chips, SMD capacitors, transistors, inductors, diodes, fine platinum wire, HSS-G frames, HPIC chips, advanced SMDs. Two drums: tin (stage solder) and soldering alloy (mainframe). Each stage has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output so a stalled stage does not flood the next. — `functionalstorage:oak_1`, `gtceu:ram_chip`, `gtceu:fiber_reinforced_printed_circuit_board`, `gtceu:fine_platinum_wire`
2. Stage 1, its own IV Circuit Assembler in the cleanroom: extreme board + qubit chip + nano chip + 12 SMD capacitors + 12 SMD transistors + 12 fine platinum wire → 2 quantum processors in 10 s at 2400 EU/t. 2 per craft, 4 per mainframe. — `gtceu:iv_circuit_assembler`, `gtceu:quantum_processor`
3. Stage 2, its own machine: extreme board + 2 processors + 8 inductors + 16 capacitors + 4 RAM + 16 fine platinum wire + 288 mB tin → 2 assemblies in 20 s at 2400 EU/t (this is the IV circuit). — `gtceu:iv_circuit_assembler`, `gtceu:quantum_processor_assembly`, `gtceu:smd_inductor`
4. Stage 3, its own machine: extreme board + 2 assemblies + 8 diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire + 288 mB tin → 1 supercomputer in 20 s. This is the LuV circuit; drawer it with Keep Exact 8, two per mainframe. — `gtceu:iv_circuit_assembler`, `gtceu:quantum_processor_computer`, `gtceu:nor_memory_chip`
5. Scan: a stick and one supercomputer in an IV Scanner (1200 ticks at 7680 EU/t) and the stick goes into the Assembly Line’s Data Access Hatch (zpm\_data chain). You can scan with the first supercomputer you make. — `gtceu:iv_scanner`, `gtceu:quantum_processor_computer`, `gtceu:data_stick`
6. Mainframe: Assembly Line buses in recipe order: 2 HSS-G frames, 2 supercomputers, 24 RAM, 2 HPIC chips, 8 ASMD inductors, 16 ASMD capacitors, 8 ASMD diodes, 8 platinum single wire; 576 mB soldering alloy in the hatch. 30 s at 30 720 EU/t → 1 ZPM circuit. — `gtceu:assembly_line`, `gtceu:quantum_processor_mainframe`, `gtceu:hssg_frame`
7. Easy to miss: the station needs about 50 ZPM circuits (zpm\_research), hatches 1 each, field generators 2 each, ZPM Fusion MK I 4. Stock them before you plan anything, and start the boards and the RAM wafers of the second and third mainframe while the first one runs. — `functionalstorage:oak_1`, `gtceu:quantum_processor_mainframe`

## Tips

- What the era wants: the quest chapter calls the Quantum Processor Mainframe the FIRST ZPM circuit and the crystal processor computer the second (zpm\_crystal); wetware processor assembly, runic processor and draconic microchip processor are the third to fifth. They are all in the #gtceu:circuits/zpm tag (kjs utils/tags.js adds the runic and draconic ones), so ONE route is enough for every recipe that says ZPM circuit. The quantum route needs no exotic ingredient and no sterile room: radon, plain boards, platinum wire.
- The pack changed the last step: it REMOVES the circuit-assembler recipes quantum\_mainframe\_zpm (plain and asmd variants, with and without soldering alloy) and the crystal\_computer\_zpm ones (kjs circuits.js) and replaces the mainframe by an Assembly Line recipe: 2 HSS-G frames + 2 quantum processor supercomputers + 24 RAM chips + 2 HPIC chips + 8 advanced SMD inductors + 16 advanced SMD capacitors + 8 advanced SMD diodes + 8 platinum single wire, 576 mB soldering alloy, 600 ticks (30 s) at 30 720 EU/t, with SCANNER research of the quantum supercomputer (1200 ticks at 7680 EU/t). It needs an Assembly Line with the 4A hatch route (luv\_hatches) and the data stick of the supercomputer.
- The first three stages are the vanilla recipes (CircuitRecipes; harderCircuitRecipes is false so each craft of the first two stages gives 2): Quantum Processor (EV) = extreme board + 1 qubit CPU chip + 1 nano CPU chip + 12 SMD capacitors + 12 SMD transistors + 12 fine platinum wire → 2, 200 ticks at 2400 EU/t. Assembly (IV) = extreme board + 2 processors + 8 SMD inductors + 16 SMD capacitors + 4 RAM + 16 fine platinum wire + solder x2 → 2, 400 ticks at 2400 EU/t. Supercomputer (LuV, a LuV circuit as well) = extreme board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire + solder x2 → 1, 400 ticks. ALL carry the CLEANROOM tag. 2400 EU/t is above the EV cap (2048), so every stage needs the IV Circuit Assembler (the luv\_lcaf chain), not the four EV ones of the nano line.
- Cost of ONE mainframe: 2 supercomputers = 4 assemblies = 4 processors, i.e. 2 + 2 + 2 crafts: 6 extreme boards, 2 qubit CPU chips, 2 nano CPU chips, 56 SMD capacitors + 24 SMD transistors + 16 inductors + 16 diodes (plain), 64 RAM chips (2 wafers), 8 NOR chips, 120 fine platinum wire (15 platinum ingots), 2 HPIC chips, 2 HSS-G frames, 8 + 16 + 8 advanced SMDs, about 1 B tin in the three stages. Time per mainframe if nothing waits: 2 x 10 s + 2 x 20 s + 2 x 20 s + 30 s = 130 s, plus 6 min of extreme-board reactor time: boards are the bottleneck, not the assemblers.
- Faster variants: the \_asmd recipes of the three circuit-assembler stages swap SMDs for advanced SMDs (processor: 3 + 3 at 100 ticks; assembly: 2 inductors + 4 capacitors at 200 ticks; computer: 2 diodes at 200 ticks), halving the time and cutting the SMD load by 3/4. Since you build the zpm\_asmd line anyway for the mainframe, use these variants as your normal routes.
- RAM: 64 chips = 2 RAM wafers per mainframe (32 chips per wafer) plus 4 NOR chips per supercomputer; use the same chip lines as the luv\_circuits chain and keep a RAM drawer with Keep Exact 64. HSS-G frames: one frame is 2 HSS-G ingots (the IV coil alloy line, abs\_super\_ebf chain); HPIC chips: iv\_hatches chain.
- Sub-steps people skip: (1) build the IV Circuit Assembler FIRST (2 LuV circuits) and the data stick scan of the supercomputer BEFORE the mainframe line; (2) the supercomputer is itself a LuV circuit and counts for every LuV recipe, so make extra and keep them apart from the stock reserved for mainframes; (3) three different extreme-board drawers are one drawer with three routers; (4) the Assembly Line must have the research stick in its Data Access Hatch AND the 4A power hatch; (5) soldering alloy 576 mB sits on a drum; tin 288 mB per stage on a separate one.
- **Unverified** that the pack leaves the quantum supercomputer recipes untouched (circuits.js removes only the ZPM and later ones and re-adds the mainframe; the earlier stages are not in its removal list), and the real throughput of one IV Circuit Assembler across three stages (use one machine per stage).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_circuit_assembler` | 3 |
| `gtceu:assembly_line` | 1 |
| `gtceu:iv_scanner` | 1 |
| `gtceu:cleanroom` | 1 |
| `gtceu:iv_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:quantum_processor_mainframe`, `gtceu:quantum_processor_computer`, `gtceu:quantum_processor_assembly`, `gtceu:quantum_processor`
