---
kind: chain
id: luv_circuits
order: 1190
data:
  t: |-
    LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)
  inf: true
  "n":
    - [ab, "Advanced Circuit Board · 6 per mainframe", i, "gtceu:epoxy_printed_circuit_board"]
    - [nc, "Nano CPU chip · 2 per mainframe", i, "gtceu:nano_cpu_chip"]
    - - p1
      - |-
        8 SMD resistor · 8 capacitor · 8 transistor · 8 fine electrum wire
      - g
      - functionalstorage:oak_1
      - - [SMD resistor, "gtceu:smd_resistor"]
        - [SMD capacitor, "gtceu:smd_capacitor"]
        - [SMD transistor, "gtceu:smd_transistor"]
        - [Fine electrum wire, "gtceu:fine_electrum_wire"]
    - [m1, "EV Circuit Assembler in the cleanroom · 10 s · 600 EU/t", m, "gtceu:ev_circuit_assembler"]
    - [np, "Nanoprocessor (HV) · 2 per craft", x, "gtceu:nano_processor"]
    - - p2
      - |-
        4 SMD inductor · 8 SMD capacitor · 8 RAM · 16 fine electrum wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [SMD inductor, "gtceu:smd_inductor"]
        - [SMD capacitor, "gtceu:smd_capacitor"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Tin, "gtceu:tin_bucket"]
    - [m2, "EV Circuit Assembler · 20 s · 600 EU/t", m, "gtceu:ev_circuit_assembler"]
    - [na, "Nanoprocessor Assembly (EV) · 2 per craft", x, "gtceu:nano_processor_assembly"]
    - - p3
      - |-
        8 SMD diode · 4 NOR chip · 16 RAM · 16 fine electrum wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [SMD diode, "gtceu:smd_diode"]
        - [NOR memory chip, "gtceu:nor_memory_chip"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Fine electrum wire, "gtceu:fine_electrum_wire"]
    - [m3, "EV Circuit Assembler · 20 s · 600 EU/t", m, "gtceu:ev_circuit_assembler"]
    - [nm, "Nanoprocessor Supercomputer (IV)", x, "gtceu:nano_processor_computer"]
    - - p4
      - |-
        2 Aluminium frame · 16 SMD inductor · 32 SMD capacitor · 16 RAM · 32 annealed copper wire · 576 mB tin
      - g
      - functionalstorage:oak_1
      - - [Aluminium frame, "gtceu:aluminium_frame"]
        - [SMD inductor, "gtceu:smd_inductor"]
        - [SMD capacitor, "gtceu:smd_capacitor"]
        - [Annealed copper wire, "gtceu:annealed_copper_single_wire"]
    - [m4, "EV Circuit Assembler · 40 s · 1920 EU/t", m, "gtceu:ev_circuit_assembler"]
    - [mf, "Nanoprocessor Mainframe (LuV circuit)", o, "gtceu:nano_processor_mainframe"]
  e:
    - [ab, m1, "1"]
    - [nc, m1, "1"]
    - [p1, m1]
    - [m1, np, "2 / 10 s"]
    - [np, m2, "2"]
    - [ab, m2, "1"]
    - [p2, m2]
    - [m2, na, "2 / 20 s"]
    - [na, m3, "2"]
    - [ab, m3, "1"]
    - [p3, m3]
    - [m3, nm, "1 / 20 s"]
    - [nm, m4, "2"]
    - [p4, m4]
    - [m4, mf, "1 / 40 s"]
  tips:
    - |-
      What the era needs: the first LuV circuit in the pack quest is the Nanoprocessor Mainframe (nano_processor_mainframe); the second is the Quantum Processor Supercomputer, the third the Crystal Processor Assembly. All three count as #gtceu:circuits/luv, so ONE route is enough. The Nanoprocessor line is the cheapest: no quantum eye, no crystal chip, only silicon, phosphorus and carbon fibers. Item ids: nano_processor (HV), nano_processor_assembly (EV), nano_processor_computer (IV), nano_processor_mainframe (LuV).
    - |-
      Recipes (CircuitRecipes, not changed by the pack; harderCircuitRecipes is false so each craft gives 2 for the first two stages): Nanoprocessor = advanced board + 1 nano CPU + 8 SMD resistors + 8 SMD capacitors + 8 SMD transistors + 8 fine electrum wire → 2, 200 ticks at 600 EU/t. Assembly = advanced board + 2 nanoprocessors + 4 SMD inductors + 8 SMD capacitors + 8 RAM + 16 fine electrum wire + solder x2 → 2, 400 ticks at 600 EU/t. Supercomputer = advanced board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 16 fine electrum wire + solder x2 → 1, 400 ticks at 600 EU/t. Mainframe = 2 aluminium frames + 2 supercomputers + 16 SMD inductors + 32 SMD capacitors + 16 RAM + 32 annealed copper single wire + solder x4 → 1, 800 ticks at 1920 EU/t. ALL FOUR carry the CLEANROOM tag.
    - |-
      Why EV machines: 600 EU/t is above the HV 512 V cap, so the first three stages need the EV Circuit Assembler, and the 1920 EU/t mainframe fits an EV machine exactly. The EV Circuit Assembler is the crafting-table machine: EV robot arm + EV emitter + 2 EV conveyor modules + EV hull + 2 aluminium single cables + 2 IV circuits (gt_machine_recipes). That is why the IV mainframe comes first: you cannot build even the first nanoprocessor machine without 2 IV circuits. Four machines (one per stage) = 8 IV circuits.
    - |-
      Solder per craft: the base is 144 mB tin (or 72 mB soldering alloy); the assembly and supercomputer take x2 (288 mB), the mainframe x4 (576 mB), the nanoprocessor x1 (144 mB). Total about 2 B tin per mainframe. One tin drum on EVERY assembler.
    - |-
      Raw cost of one mainframe (2 supercomputer crafts, 2 assembly crafts, 2 nanoprocessor crafts): 6 advanced boards, 2 nano CPU chips, 8 NOR chips, 64 RAM chips (2 RAM wafers), 16 SMD resistors, 16 SMD transistors, 64 SMD capacitors, 24 SMD inductors, 16 SMD diodes, 80 fine electrum wire (10 electrum ingots), 32 annealed copper wire, 2 aluminium frames, about 2 B tin. SMDs are the HV Assembler recipes of the smd chain (480 EU/t): basic SMDs are enough.
    - |-
      Machines and time: one machine per stage keeps it 1 : 1 : 1 : 1 and the 40 s mainframe is the slow step (1.5 a minute); the supercomputer stage needs 2 crafts of 20 s per mainframe = 40 s, the assembly stage 2 crafts of 20 s = 40 s, the nanoprocessor stage 2 crafts of 10 s = 20 s. All four idle between runs, so three would also keep up if you share one: not recommended, the tin and the cleanroom feeders get messy.
    - |-
      The faster variants (_asmd recipes) use Advanced SMDs (graphene, platinum, HSS-G, HSS-S, PBI): they halve the time and the part counts, but their parts need 3840 EU/t (IV Assembler) and HSS-S, so they are not a starting route. The SoC variants (advanced system on chip from naquadah wafers) are ZPM tier ingredients.
    - |-
      Sub-steps people skip: (1) build the EV Circuit Assemblers from IV circuits BEFORE you plan the line, and the cleanroom first; (2) RAM: 64 chips = 2 wafers per mainframe, the biggest chip load, keep a RAM drawer with Keep Exact 64; (3) NOR chips only exist from phosphorus wafers (luv_chips chain); (4) annealed copper SINGLE wire (not fine) for the mainframe, fine electrum wire for the other three; (5) set Keep Exact 16 on every stage output so a stalled stage does not flood the next; (6) the advanced board drawer feeds three stages: one drawer, three routers.
    - |-
      The other two LuV circuits, for later: Quantum Processor Supercomputer = extreme board + 2 quantum assemblies (IV) + 8 SMD diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire, 400 ticks at 2400 EU/t (needs an IV Circuit Assembler, which itself needs 2 LuV circuits); Crystal Processor Assembly = elite board + 2 crystal processors + 4 advanced SMD inductors + 8 advanced SMD capacitors + 24 RAM + 16 fine niobium titanium wire, 400 ticks at 9600 EU/t (a LuV-power machine). Not needed to reach ZPM hulls through the nano route alone, but the quest chapter asks for the quantum one.
    - |-
      Unverified: whether the circuit assemblers need the SMD tag items or accept only the exact SMD ids shown (the tag should accept both plain and advanced SMDs), and the exact range of the Cleanroom filter for four EV machines (size the room to four 3 x 3 machines plus the passthrough hatches).
  b:
    - ["gtceu:ev_circuit_assembler", 4]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:hv_assembler", 3]
    - ["gtceu:mv_wiremill", 1]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:ram_chip", "gtceu:nano_cpu_chip", "gtceu:epoxy_printed_circuit_board"]
      t: |-
        Drawers first, one per part: advanced boards, nano CPU chips, NOR chips, RAM chips, SMD resistors, capacitors, transistors, inductors and diodes, fine electrum wire, annealed copper single wire, aluminium frames. A tin drum for every assembler. Each assembler has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output, so the next stage only takes what it needs.
    - i: ["gtceu:ev_circuit_assembler", "gtceu:cleanroom", "gtceu:ev_robot_arm"]
      t: |-
        First the machines: four EV Circuit Assemblers, each from an EV robot arm, an EV emitter, 2 EV conveyor modules, an EV hull, 2 aluminium cables and 2 IV circuits (the IV mainframes you made in the IV era). Put all four inside the Cleanroom before you close the walls, with passthrough hatches for items and fluids (see the hv_cleanroom chain).
    - i: ["gtceu:ev_circuit_assembler", "gtceu:nano_processor"]
      t: |-
        Stage 1: advanced board + 1 nano CPU + 8 SMD resistors + 8 SMD capacitors + 8 SMD transistors + 8 fine electrum wire → 2 Nanoprocessors in 10 s at 600 EU/t, 144 mB tin. 2 per mainframe.
    - i: ["gtceu:ev_circuit_assembler", "gtceu:nano_processor_assembly", "gtceu:smd_inductor"]
      t: |-
        Stage 2, its own machine: advanced board + 2 nanoprocessors + 4 SMD inductors + 8 SMD capacitors + 8 RAM + 16 fine electrum wire + 288 mB tin → 2 Nanoprocessor Assemblies in 20 s at 600 EU/t. This is the EV circuit.
    - i: ["gtceu:ev_circuit_assembler", "gtceu:nano_processor_computer", "gtceu:nor_memory_chip"]
      t: |-
        Stage 3, its own machine: advanced board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 16 fine electrum wire + 288 mB tin → 1 Nanoprocessor Supercomputer (the IV nano circuit) in 20 s at 600 EU/t.
    - i: ["gtceu:ev_circuit_assembler", "gtceu:nano_processor_mainframe", "gtceu:aluminium_frame"]
      t: |-
        Stage 4: 2 aluminium frames + 2 supercomputers + 16 SMD inductors + 32 SMD capacitors + 16 RAM + 32 annealed copper single wire + 576 mB tin → 1 Nanoprocessor Mainframe, 40 s at 1920 EU/t. That is the LuV circuit. The EV hatch/cable must carry 1920 EU/t: wire this assembler to its own EV line.
    - i: ["gtceu:ram_chip", "gtceu:silicon_wafer", "gtceu:mv_laser_engraver"]
      t: |-
        RAM comes from the same silicon wafer line as the HV chain (green lens, cutter: 32 RAM per wafer). 64 per mainframe = 2 wafers; the boule (about 7.5 min) is the limit.
    - i: ["gtceu:hv_assembler", "gtceu:smd_capacitor", "gtceu:smd_inductor", "gtceu:smd_diode"]
      t: |-
        SMDs: the smd chain’s HV Assemblers, one per part. Per mainframe you use 64 capacitors, 24 inductors, 16 each of resistor, transistor and diode, so the capacitor machine and its foil drawers are the busiest. Diodes use platinum fine wire and gallium arsenide, inductors a nickel zinc ferrite ring (Unverified source, see the smd chain).
    - i: ["functionalstorage:oak_1", "gtceu:nano_processor_mainframe"]
      t: |-
        Easy to miss: stock two mainframes before you use one. The IV Circuit Assembler wants 2 LuV circuits, the IV Parallel Hatch 4, and then the LuV machine hull line, the LuV components (2 circuits per emitter, sensor and field generator, 1 per robot arm) and the Assembly Line hatches all take more. Keep Exact 8 on the output and a second drawer behind it.
---
# LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_circuits` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [LuV circuit (Nanoprocessor Mainframe)](../../plan/p11.md#luvcirc)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-m1">
<div class="gt-head"><span class="gt-mname">EV Circuit Assembler in the cleanroom · 10 s · 600 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Advanced Circuit Board · 6 per mainframe (gtceu:epoxy_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Printed Circuit Board</span><span class="gt-note">Advanced Circuit Board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot" title="Nano CPU chip · 2 per mainframe (gtceu:nano_cpu_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nano_cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano CPU Chip</span><span class="gt-note">Nano CPU chip · 2 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="8 SMD resistor · 8 capacitor · 8 transistor · 8 fine electrum wire (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 SMD resistor · 8 capacitor · 8 transistor · 8 fine electrum wire</span><span class="gt-sub"><span>SMD resistor</span><span>SMD capacitor</span><span>SMD transistor</span><span>Fine electrum wire</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nanoprocessor (HV) · 2 per craft (gtceu:nano_processor) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor</span><span class="gt-note">Nanoprocessor (HV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_circuit_assembler</code></div>
</div>
<div class="gt-panel t-ev" id="m-m2">
<div class="gt-head"><span class="gt-mname">EV Circuit Assembler · 20 s · 600 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nanoprocessor (HV) · 2 per craft (gtceu:nano_processor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor</span><span class="gt-note">Nanoprocessor (HV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot" title="Advanced Circuit Board · 6 per mainframe (gtceu:epoxy_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Printed Circuit Board</span><span class="gt-note">Advanced Circuit Board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="4 SMD inductor · 8 SMD capacitor · 8 RAM · 16 fine electrum wire · 288 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 SMD inductor · 8 SMD capacitor · 8 RAM · 16 fine electrum wire · 288 mB tin</span><span class="gt-sub"><span>SMD inductor</span><span>SMD capacitor</span><span>RAM chip</span><span>Tin</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nanoprocessor Assembly (EV) · 2 per craft (gtceu:nano_processor_assembly) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Assembly</span><span class="gt-note">Nanoprocessor Assembly (EV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_circuit_assembler</code></div>
</div>
<div class="gt-panel t-ev" id="m-m3">
<div class="gt-head"><span class="gt-mname">EV Circuit Assembler · 20 s · 600 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nanoprocessor Assembly (EV) · 2 per craft (gtceu:nano_processor_assembly) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Assembly</span><span class="gt-note">Nanoprocessor Assembly (EV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot" title="Advanced Circuit Board · 6 per mainframe (gtceu:epoxy_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Printed Circuit Board</span><span class="gt-note">Advanced Circuit Board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="8 SMD diode · 4 NOR chip · 16 RAM · 16 fine electrum wire · 288 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 SMD diode · 4 NOR chip · 16 RAM · 16 fine electrum wire · 288 mB tin</span><span class="gt-sub"><span>SMD diode</span><span>NOR memory chip</span><span>RAM chip</span><span>Fine electrum wire</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nanoprocessor Supercomputer (IV) (gtceu:nano_processor_computer) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Computer</span><span class="gt-note">Nanoprocessor Supercomputer (IV)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_circuit_assembler</code></div>
</div>
<div class="gt-panel t-ev" id="m-m4">
<div class="gt-head"><span class="gt-mname">EV Circuit Assembler · 40 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nanoprocessor Supercomputer (IV) (gtceu:nano_processor_computer) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Computer</span><span class="gt-note">Nanoprocessor Supercomputer (IV)</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="2 Aluminium frame · 16 SMD inductor · 32 SMD capacitor · 16 RAM · 32 annealed copper wire · 576 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 Aluminium frame · 16 SMD inductor · 32 SMD capacitor · 16 RAM · 32 annealed copper wire · 576 mB tin</span><span class="gt-sub"><span>Aluminium frame</span><span>SMD inductor</span><span>SMD capacitor</span><span>Annealed copper wire</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Nanoprocessor Mainframe (LuV circuit) (gtceu:nano_processor_mainframe) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Mainframe</span><span class="gt-note">Nanoprocessor Mainframe (LuV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_circuit_assembler</code></div>
</div>
</div>

## Flow

- [EV Circuit Assembler in the cleanroom · 10 s · 600 EU/t](#m-m1) → [EV Circuit Assembler · 20 s · 600 EU/t](#m-m2) → [EV Circuit Assembler · 20 s · 600 EU/t](#m-m3) → [EV Circuit Assembler · 40 s · 1920 EU/t](#m-m4)

## How to build

1. Drawers first, one per part: advanced boards, nano CPU chips, NOR chips, RAM chips, SMD resistors, capacitors, transistors, inductors and diodes, fine electrum wire, annealed copper single wire, aluminium frames. A tin drum for every assembler. Each assembler has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output, so the next stage only takes what it needs. — `functionalstorage:oak_1`, `gtceu:ram_chip`, `gtceu:nano_cpu_chip`, `gtceu:epoxy_printed_circuit_board`
2. First the machines: four EV Circuit Assemblers, each from an EV robot arm, an EV emitter, 2 EV conveyor modules, an EV hull, 2 aluminium cables and 2 IV circuits (the IV mainframes you made in the IV era). Put all four inside the Cleanroom before you close the walls, with passthrough hatches for items and fluids (see the hv\_cleanroom chain). — `gtceu:ev_circuit_assembler`, `gtceu:cleanroom`, `gtceu:ev_robot_arm`
3. Stage 1: advanced board + 1 nano CPU + 8 SMD resistors + 8 SMD capacitors + 8 SMD transistors + 8 fine electrum wire → 2 Nanoprocessors in 10 s at 600 EU/t, 144 mB tin. 2 per mainframe. — `gtceu:ev_circuit_assembler`, `gtceu:nano_processor`
4. Stage 2, its own machine: advanced board + 2 nanoprocessors + 4 SMD inductors + 8 SMD capacitors + 8 RAM + 16 fine electrum wire + 288 mB tin → 2 Nanoprocessor Assemblies in 20 s at 600 EU/t. This is the EV circuit. — `gtceu:ev_circuit_assembler`, `gtceu:nano_processor_assembly`, `gtceu:smd_inductor`
5. Stage 3, its own machine: advanced board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 16 fine electrum wire + 288 mB tin → 1 Nanoprocessor Supercomputer (the IV nano circuit) in 20 s at 600 EU/t. — `gtceu:ev_circuit_assembler`, `gtceu:nano_processor_computer`, `gtceu:nor_memory_chip`
6. Stage 4: 2 aluminium frames + 2 supercomputers + 16 SMD inductors + 32 SMD capacitors + 16 RAM + 32 annealed copper single wire + 576 mB tin → 1 Nanoprocessor Mainframe, 40 s at 1920 EU/t. That is the LuV circuit. The EV hatch/cable must carry 1920 EU/t: wire this assembler to its own EV line. — `gtceu:ev_circuit_assembler`, `gtceu:nano_processor_mainframe`, `gtceu:aluminium_frame`
7. RAM comes from the same silicon wafer line as the HV chain (green lens, cutter: 32 RAM per wafer). 64 per mainframe = 2 wafers; the boule (about 7.5 min) is the limit. — `gtceu:ram_chip`, `gtceu:silicon_wafer`, `gtceu:mv_laser_engraver`
8. SMDs: the smd chain’s HV Assemblers, one per part. Per mainframe you use 64 capacitors, 24 inductors, 16 each of resistor, transistor and diode, so the capacitor machine and its foil drawers are the busiest. Diodes use platinum fine wire and gallium arsenide, inductors a nickel zinc ferrite ring (Unverified source, see the smd chain). — `gtceu:hv_assembler`, `gtceu:smd_capacitor`, `gtceu:smd_inductor`, `gtceu:smd_diode`
9. Easy to miss: stock two mainframes before you use one. The IV Circuit Assembler wants 2 LuV circuits, the IV Parallel Hatch 4, and then the LuV machine hull line, the LuV components (2 circuits per emitter, sensor and field generator, 1 per robot arm) and the Assembly Line hatches all take more. Keep Exact 8 on the output and a second drawer behind it. — `functionalstorage:oak_1`, `gtceu:nano_processor_mainframe`

## Tips

- What the era needs: the first LuV circuit in the pack quest is the Nanoprocessor Mainframe (nano\_processor\_mainframe); the second is the Quantum Processor Supercomputer, the third the Crystal Processor Assembly. All three count as #gtceu:circuits/luv, so ONE route is enough. The Nanoprocessor line is the cheapest: no quantum eye, no crystal chip, only silicon, phosphorus and carbon fibers. Item ids: nano\_processor (HV), nano\_processor\_assembly (EV), nano\_processor\_computer (IV), nano\_processor\_mainframe (LuV).
- Recipes (CircuitRecipes, not changed by the pack; harderCircuitRecipes is false so each craft gives 2 for the first two stages): Nanoprocessor = advanced board + 1 nano CPU + 8 SMD resistors + 8 SMD capacitors + 8 SMD transistors + 8 fine electrum wire → 2, 200 ticks at 600 EU/t. Assembly = advanced board + 2 nanoprocessors + 4 SMD inductors + 8 SMD capacitors + 8 RAM + 16 fine electrum wire + solder x2 → 2, 400 ticks at 600 EU/t. Supercomputer = advanced board + 2 assemblies + 8 SMD diodes + 4 NOR chips + 16 RAM + 16 fine electrum wire + solder x2 → 1, 400 ticks at 600 EU/t. Mainframe = 2 aluminium frames + 2 supercomputers + 16 SMD inductors + 32 SMD capacitors + 16 RAM + 32 annealed copper single wire + solder x4 → 1, 800 ticks at 1920 EU/t. ALL FOUR carry the CLEANROOM tag.
- Why EV machines: 600 EU/t is above the HV 512 V cap, so the first three stages need the EV Circuit Assembler, and the 1920 EU/t mainframe fits an EV machine exactly. The EV Circuit Assembler is the crafting-table machine: EV robot arm + EV emitter + 2 EV conveyor modules + EV hull + 2 aluminium single cables + 2 IV circuits (gt\_machine\_recipes). That is why the IV mainframe comes first: you cannot build even the first nanoprocessor machine without 2 IV circuits. Four machines (one per stage) = 8 IV circuits.
- Solder per craft: the base is 144 mB tin (or 72 mB soldering alloy); the assembly and supercomputer take x2 (288 mB), the mainframe x4 (576 mB), the nanoprocessor x1 (144 mB). Total about 2 B tin per mainframe. One tin drum on EVERY assembler.
- Raw cost of one mainframe (2 supercomputer crafts, 2 assembly crafts, 2 nanoprocessor crafts): 6 advanced boards, 2 nano CPU chips, 8 NOR chips, 64 RAM chips (2 RAM wafers), 16 SMD resistors, 16 SMD transistors, 64 SMD capacitors, 24 SMD inductors, 16 SMD diodes, 80 fine electrum wire (10 electrum ingots), 32 annealed copper wire, 2 aluminium frames, about 2 B tin. SMDs are the HV Assembler recipes of the smd chain (480 EU/t): basic SMDs are enough.
- Machines and time: one machine per stage keeps it 1 : 1 : 1 : 1 and the 40 s mainframe is the slow step (1.5 a minute); the supercomputer stage needs 2 crafts of 20 s per mainframe = 40 s, the assembly stage 2 crafts of 20 s = 40 s, the nanoprocessor stage 2 crafts of 10 s = 20 s. All four idle between runs, so three would also keep up if you share one: not recommended, the tin and the cleanroom feeders get messy.
- The faster variants (\_asmd recipes) use Advanced SMDs (graphene, platinum, HSS-G, HSS-S, PBI): they halve the time and the part counts, but their parts need 3840 EU/t (IV Assembler) and HSS-S, so they are not a starting route. The SoC variants (advanced system on chip from naquadah wafers) are ZPM tier ingredients.
- Sub-steps people skip: (1) build the EV Circuit Assemblers from IV circuits BEFORE you plan the line, and the cleanroom first; (2) RAM: 64 chips = 2 wafers per mainframe, the biggest chip load, keep a RAM drawer with Keep Exact 64; (3) NOR chips only exist from phosphorus wafers (luv\_chips chain); (4) annealed copper SINGLE wire (not fine) for the mainframe, fine electrum wire for the other three; (5) set Keep Exact 16 on every stage output so a stalled stage does not flood the next; (6) the advanced board drawer feeds three stages: one drawer, three routers.
- The other two LuV circuits, for later: Quantum Processor Supercomputer = extreme board + 2 quantum assemblies (IV) + 8 SMD diodes + 4 NOR chips + 16 RAM + 32 fine platinum wire, 400 ticks at 2400 EU/t (needs an IV Circuit Assembler, which itself needs 2 LuV circuits); Crystal Processor Assembly = elite board + 2 crystal processors + 4 advanced SMD inductors + 8 advanced SMD capacitors + 24 RAM + 16 fine niobium titanium wire, 400 ticks at 9600 EU/t (a LuV-power machine). Not needed to reach ZPM hulls through the nano route alone, but the quest chapter asks for the quantum one.
- **Unverified** whether the circuit assemblers need the SMD tag items or accept only the exact SMD ids shown (the tag should accept both plain and advanced SMDs), and the exact range of the Cleanroom filter for four EV machines (size the room to four 3 x 3 machines plus the passthrough hatches).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:ev_circuit_assembler` | 4 |
| `gtceu:cleanroom` | 1 |
| `gtceu:hv_assembler` | 3 |
| `gtceu:mv_wiremill` | 1 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Needs:** [Advanced Circuit Board: epoxy plate + gold foil → advanced board → electrum foil + iron III chloride → 6 per Nanoprocessor Mainframe](luv_boards.md), [LuV chips: Nano CPU chip (CPU wafer + carbon fibers + molten glowstone) and NOR memory chip (phosphorus wafer)](luv_chips.md)
- **Feeds:** [What LuV circuits unlock first: IV Circuit Assembler (2 LuV circuits), IV Parallel Hatch (4), Large Circuit Assembling Facility](luv_lcaf.md)
- **Main source for:** `gtceu:nano_processor`, `gtceu:nano_processor_assembly`, `gtceu:nano_processor_computer`, `gtceu:nano_processor_mainframe`
