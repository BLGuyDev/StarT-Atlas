---
kind: chain
id: iv_circuits
order: 1120
data:
  t: |-
    IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)
  inf: true
  "n":
    - [cp, CPU chip, i, "gtceu:cpu_chip"]
    - [pb, "Plastic printed board · 6 per mainframe", i, "gtceu:plastic_printed_circuit_board"]
    - - p1
      - |-
        4 Resistors · 4 capacitors · 4 transistors · 4 fine red alloy wire
      - g
      - functionalstorage:oak_1
      - - [Resistor, "gtceu:resistor"]
        - [Capacitor, "gtceu:capacitor"]
        - [Transistor, "gtceu:transistor"]
        - [Fine red alloy wire, "gtceu:fine_red_alloy_wire"]
    - [m1, "MV Circuit Assembler · 10 s · 60 EU/t", m, "gtceu:mv_circuit_assembler"]
    - [mp, "Microprocessor (MV) · 2 per craft", x, "gtceu:micro_processor"]
    - - p2
      - |-
        4 Inductors · 8 capacitors · 4 RAM · 8 fine red alloy wire · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [Inductor, "gtceu:inductor"]
        - [Capacitor, "gtceu:capacitor"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Tin, "gtceu:tin_bucket"]
    - [m2, "MV Circuit Assembler · 20 s · 120 EU/t", m, "gtceu:mv_circuit_assembler"]
    - [pa, "Microprocessor Assembly (HV) · 2 per craft", x, "gtceu:micro_processor_assembly"]
    - - p3
      - |-
        4 Diodes · 4 RAM · 16 fine electrum wire · 16 blue alloy bolts · 288 mB tin
      - g
      - functionalstorage:oak_1
      - - [Diode, "gtceu:diode"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Fine electrum wire, "gtceu:fine_electrum_wire"]
        - [Blue alloy bolt, "gtceu:blue_alloy_bolt"]
    - [cr, "Cleanroom (95 % or more)", m, "gtceu:cleanroom"]
    - [m3, "MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t", m, "gtceu:mv_circuit_assembler"]
    - [pc, "Microprocessor Supercomputer (EV)", x, "gtceu:micro_processor_computer"]
    - - p4
      - |-
        8 Inductors · 16 capacitors · 16 RAM · 16 annealed copper wire · 576 mB tin
      - g
      - functionalstorage:oak_1
      - - [Inductor, "gtceu:inductor"]
        - [Capacitor, "gtceu:capacitor"]
        - [RAM chip, "gtceu:ram_chip"]
        - [Annealed copper wire, "gtceu:annealed_copper_single_wire"]
    - [af, "2 Aluminium frames", i, "gtceu:aluminium_frame"]
    - [m4, "HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t", m, "gtceu:hv_circuit_assembler"]
    - [mf, "Microprocessor Mainframe (IV circuit)", o, "gtceu:micro_processor_mainframe"]
  e:
    - [cp, m1, "1"]
    - [pb, m1, "1"]
    - [p1, m1]
    - [m1, mp, "2 / 10 s"]
    - [mp, m2, "2"]
    - [pb, m2, "1"]
    - [p2, m2]
    - [m2, pa, "2 / 20 s"]
    - [pa, m3, "2"]
    - [pb, m3, "1"]
    - [p3, m3]
    - [cr, m3, clean air]
    - [m3, pc, "1 / 20 s"]
    - [pc, m4, "2"]
    - [p4, m4]
    - [af, m4, "2"]
    - [cr, m4, clean air]
    - [m4, mf, "1 / 40 s"]
  tips:
    - |-
      What the era needs: the first IV circuit is the Microprocessor Mainframe (pack quest: first IV circuit; second is the Nanoprocessor Supercomputer). The same line up from the HV chain: Microchip (LV) → Microprocessor (MV) → Microprocessor Assembly (HV) → Microprocessor Supercomputer (EV) → Mainframe (IV). Item ids: micro_processor, micro_processor_assembly, micro_processor_computer, micro_processor_mainframe.
    - |-
      It is the cheap route on purpose: only silicon wafers (RAM, CPU), plain boards and no laser lens beyond the HV chain. The Nanoprocessor Supercomputer needs NOR chips from phosphorus wafers and 600 EU/t (an EV Circuit Assembler); the Quantum Processor Assembly needs 2400 EU/t, i.e. an IV Circuit Assembler, which itself needs 2 LuV circuits; the Crystal Processor needs a 5000 K crystal chip. None of them is an IV starting point.
    - |-
      Recipes (CircuitRecipes, not changed by the pack): Microprocessor = plastic printed board + CPU + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire, 200 ticks at 60 EU/t, gives 2. Assembly = board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire + solder, 400 ticks at 120 EU/t, gives 2, no cleanroom. Supercomputer (workstation_ev) = board + 2 assemblies + 4 diodes + 4 RAM + 16 fine electrum wire + 16 blue alloy bolts + solder, 400 ticks at 120 EU/t, CLEANROOM. Mainframe (mainframe_iv) = 2 aluminium frames + 2 supercomputers + 8 inductors + 16 capacitors + 16 RAM + 16 annealed copper single wire + solder x4, 800 ticks at 480 EU/t, CLEANROOM.
    - |-
      Solder: the assembly and supercomputer recipes take 288 mB tin (or 144 mB soldering alloy); the mainframe takes 576 mB tin (or 288 mB soldering alloy). Every circuit assembler recipe also carries solder (jar GTRecipeTypes: 144 mB tin or 72 mB soldering alloy, times the multiplier), so even the plain microprocessor takes 144 mB. A recipe with all items present but an empty solder drum just sits there: one tin drum per assembler.
    - |-
      Raw cost of one mainframe: 6 plastic printed boards, 2 CPU chips, 32 RAM chips (one RAM wafer gives 32), 16 inductors, 40 capacitors, 8 diodes, 8 resistors, 8 transistors, 32 fine electrum wire (4 electrum ingots), 32 blue alloy bolts (4 blue alloy ingots in an extruder, 8 bolts each), 24 fine red alloy wire, 16 annealed copper wire, 2 aluminium frames and roughly 2 B tin of solder in all. Micro 2 crafts, assembly 2 crafts, supercomputer 2 crafts per mainframe.
    - |-
      Machines: one MV Circuit Assembler per stage (micro, assembly, supercomputer) and one HV Circuit Assembler for the mainframe keep the line 1:1:1:1 at 1.5 mainframes a minute (the 40 s mainframe is the slow step, 2 supercomputers = 40 s of one MV machine). The HV Circuit Assembler needs 2 EV circuits to build, so make the first supercomputers on the MV machine, then the HV machine from them.
    - |-
      Cleanroom: only the supercomputer and mainframe recipes carry the cleanroom tag, so only those two assemblers go inside. A standard (not sterile) Cleanroom is enough; it runs the recipe only while the clean amount is 95 % or more (see the hv_cleanroom chain).
    - |-
      Blue alloy: 1 silver dust + 4 electrotine dust in a mixer (circuit 2, 100 ticks, 7 EU/t) and the dust goes to a furnace; electrotine = redstone + electrum dust in a mixer (circuit 1, 200 ticks). Annealed copper wire comes from annealed copper ingots; the only recipe found is the arc furnace recycling rule for copper items (RecyclingRecipes). Unverified: its oxygen and time, and whether a plain copper ingot is accepted: read the arc furnace in EMI first.
    - |-
      Sub-steps people skip: (1) the HV Circuit Assembler cannot be built before the supercomputers, so keep 2 aside; (2) inductors and capacitors are the real bulk (56 per mainframe), build 2 MV assemblers for them; (3) put the tin drum on every assembler, not only the cleanroom ones; (4) RAM is the shared part: 32 of 32 RAM chips in a wafer go into one mainframe, so keep a RAM drawer with Keep Exact 64 on the cutter; (5) never mix the plain and the printed board.
    - |-
      Unverified: the annealed copper wire source above, how a cable reaches a machine inside the room, and the exact yield of blue alloy dust from the mixer (1 dust is assumed from the output line).
  b:
    - ["gtceu:mv_circuit_assembler", 3]
    - ["gtceu:hv_circuit_assembler", 1]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:mv_assembler", 2]
    - ["gtceu:mv_extruder", 1]
    - ["gtceu:lv_wiremill", 2]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:ram_chip", "gtceu:cpu_chip", "gtceu:plastic_printed_circuit_board"]
      t: |-
        Drawers first, one per part: RAM chips, CPU chips, plastic printed boards, resistors, capacitors, inductors, transistors, diodes, fine red alloy wire, fine electrum wire, blue alloy bolts, annealed copper wire, aluminium frames. A tin drum for every assembler. Each assembler has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output, so the next stage only takes what it needs.
    - i: ["gtceu:mv_circuit_assembler", "gtceu:micro_processor"]
      t: |-
        Stage 1, MV Circuit Assembler: plastic printed board + 1 CPU chip + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire → 2 Microprocessors in 10 s at 60 EU/t. Keep it as its own machine; it is the same machine as the HV chain’s second route.
    - i: ["gtceu:mv_circuit_assembler", "gtceu:micro_processor_assembly", "gtceu:inductor"]
      t: |-
        Stage 2, a second MV Circuit Assembler: board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire + 288 mB tin → 2 Microprocessor Assemblies in 20 s at 120 EU/t. No cleanroom here. Inductors: MV Assembler, steel ring + 2 fine copper wire + 36 mB polyethylene → 2 (16 s); capacitors: polyethylene foil + 2 aluminium foil + 144 mB polyethylene → 8 (16 s).
    - i: ["gtceu:cleanroom", "gtceu:mv_circuit_assembler", "gtceu:micro_processor_computer"]
      t: |-
        Stage 3 inside the Cleanroom: a third MV Circuit Assembler. Board + 2 assemblies + 4 diodes + 4 RAM + 16 fine electrum wire + 16 blue alloy bolts + 288 mB tin → 1 Microprocessor Supercomputer (the first EV circuit), 20 s at 120 EU/t. Place the assembler inside the room before you close the walls (machines standing in the room join it), and bring items and fluids in through passthrough hatches in the wall (see the cleanroom chain).
    - i: ["gtceu:hv_circuit_assembler", "gtceu:micro_processor_mainframe", "gtceu:aluminium_frame"]
      t: |-
        Stage 4 inside the Cleanroom: HV Circuit Assembler (build it from 2 supercomputers first). 2 aluminium frames + 2 supercomputers + 8 inductors + 16 capacitors + 16 RAM + 16 annealed copper single wire + 576 mB tin → 1 Microprocessor Mainframe, 40 s at 480 EU/t. That is the IV circuit the robot arms, emitters, sensors, IV assembler and almost every IV machine ask for.
    - i: ["gtceu:ram_chip", "gtceu:silicon_wafer", "gtceu:mv_laser_engraver"]
      t: |-
        RAM and CPU are the same wafer line as the HV circuits: boule, cutter, MV Laser Engraver with the green (RAM) and light blue (CPU) lens, then the cutter again (32 RAM chips or 8 CPU chips per wafer). One mainframe uses 32 RAM, so one RAM wafer per mainframe and 2 CPU chips from a quarter of a CPU wafer; the boule (7.5 min) is the real limit, about 2 wafers a minute.
    - i: ["gtceu:blue_alloy_ingot", "gtceu:blue_alloy_bolt", "gtceu:fine_electrum_wire"]
      t: |-
        Supercomputer parts: blue alloy bolts via MV Extruder (1 ingot → 8 bolts, 15 ticks, 120 EU/t) from blue alloy ingots (mixer dust, then furnace); fine electrum wire: wiremill circuit 3, 1 electrum ingot → 8. 16 of each per supercomputer, so a drawer of 32 of each covers a mainframe.
    - i: ["gtceu:diode", "gtceu:annealed_copper_single_wire"]
      t: Diodes (4 per supercomputer) come from the MV diode line (gallium arsenide small dust + glass or polyethylene + fine copper wire, 20 s at 30 EU/t, 4 diodes with annealed fine wire and polyethylene). Annealed copper single wire from annealed copper ingots in a wiremill; one mainframe takes 16.
    - i: ["functionalstorage:oak_1", "gtceu:micro_processor_mainframe"]
      t: |-
        Easy to miss: the mainframe is built from the HV tin, so the whole line is one big stock problem, not a power problem (peak 480 EU/t). Build stage 1 and 2 first and let them stock 8 assemblies before you start the cleanroom stages; set Keep Exact on every stage output to 16 so nothing floods the cleanroom feeders.
---
# IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `iv_circuits` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [IV circuit and IV hatches](../../plan/p10.md#ivcirc)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-m1">
<div class="gt-head"><span class="gt-mname">MV Circuit Assembler · 10 s · 60 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="CPU chip (gtceu:cpu_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Chip</span><b class="gt-q">1</b></span><span class="gt-slot" title="Plastic printed board · 6 per mainframe (gtceu:plastic_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__plastic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plastic Printed Circuit Board</span><span class="gt-note">Plastic printed board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="4 Resistors · 4 capacitors · 4 transistors · 4 fine red alloy wire (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 Resistors · 4 capacitors · 4 transistors · 4 fine red alloy wire</span><span class="gt-sub"><span>Resistor</span><span>Capacitor</span><span>Transistor</span><span>Fine red alloy wire</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Microprocessor (MV) · 2 per craft (gtceu:micro_processor) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor</span><span class="gt-note">Microprocessor (MV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-mv" id="m-m2">
<div class="gt-head"><span class="gt-mname">MV Circuit Assembler · 20 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Microprocessor (MV) · 2 per craft (gtceu:micro_processor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor</span><span class="gt-note">Microprocessor (MV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot" title="Plastic printed board · 6 per mainframe (gtceu:plastic_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__plastic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plastic Printed Circuit Board</span><span class="gt-note">Plastic printed board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="4 Inductors · 8 capacitors · 4 RAM · 8 fine red alloy wire · 288 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 Inductors · 8 capacitors · 4 RAM · 8 fine red alloy wire · 288 mB tin</span><span class="gt-sub"><span>Inductor</span><span>Capacitor</span><span>RAM chip</span><span>Tin</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Microprocessor Assembly (HV) · 2 per craft (gtceu:micro_processor_assembly) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Assembly</span><span class="gt-note">Microprocessor Assembly (HV) · 2 per craft</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-cr">
<div class="gt-head"><span class="gt-mname">Cleanroom (95 % or more)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t (gtceu:mv_circuit_assembler) - clean air"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Circuit Assembler</span><span class="gt-note">MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t</span><b class="gt-q">clean air</b></a><a class="gt-slot gt-mach" href="#m-m4" title="HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t (gtceu:hv_circuit_assembler) - clean air"><img class="gt-ico" src="../../assets/icons/gtceu__hv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Circuit Assembler</span><span class="gt-note">HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t</span><b class="gt-q">clean air</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:cleanroom</code></div>
</div>
<div class="gt-panel t-mv" id="m-m3">
<div class="gt-head"><span class="gt-mname">MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Microprocessor Assembly (HV) · 2 per craft (gtceu:micro_processor_assembly) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Assembly</span><span class="gt-note">Microprocessor Assembly (HV) · 2 per craft</span><b class="gt-q">2</b></span><span class="gt-slot" title="Plastic printed board · 6 per mainframe (gtceu:plastic_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__plastic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plastic Printed Circuit Board</span><span class="gt-note">Plastic printed board · 6 per mainframe</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="4 Diodes · 4 RAM · 16 fine electrum wire · 16 blue alloy bolts · 288 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 Diodes · 4 RAM · 16 fine electrum wire · 16 blue alloy bolts · 288 mB tin</span><span class="gt-sub"><span>Diode</span><span>RAM chip</span><span>Fine electrum wire</span><span>Blue alloy bolt</span></span></span><a class="gt-slot gt-mach" href="#m-cr" title="Cleanroom (95 % or more) (gtceu:cleanroom) - clean air"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cleanroom</span><span class="gt-note">Cleanroom (95 % or more)</span><b class="gt-q">clean air</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Microprocessor Supercomputer (EV) (gtceu:micro_processor_computer) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Computer</span><span class="gt-note">Microprocessor Supercomputer (EV)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-hv" id="m-m4">
<div class="gt-head"><span class="gt-mname">HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Microprocessor Supercomputer (EV) (gtceu:micro_processor_computer) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Computer</span><span class="gt-note">Microprocessor Supercomputer (EV)</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="8 Inductors · 16 capacitors · 16 RAM · 16 annealed copper wire · 576 mB tin (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 Inductors · 16 capacitors · 16 RAM · 16 annealed copper wire · 576 mB tin</span><span class="gt-sub"><span>Inductor</span><span>Capacitor</span><span>RAM chip</span><span>Annealed copper wire</span></span></span><span class="gt-slot" title="2 Aluminium frames (gtceu:aluminium_frame) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Frame</span><span class="gt-note">2 Aluminium frames</span><b class="gt-q">2</b></span><a class="gt-slot gt-mach" href="#m-cr" title="Cleanroom (95 % or more) (gtceu:cleanroom) - clean air"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cleanroom</span><span class="gt-note">Cleanroom (95 % or more)</span><b class="gt-q">clean air</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Microprocessor Mainframe (IV circuit) (gtceu:micro_processor_mainframe) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Mainframe</span><span class="gt-note">Microprocessor Mainframe (IV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_circuit_assembler</code></div>
</div>
</div>

## Flow

- [MV Circuit Assembler · 10 s · 60 EU/t](#m-m1) → [MV Circuit Assembler · 20 s · 120 EU/t](#m-m2) → [MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t](#m-m3) → [HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t](#m-m4)
- [Cleanroom (95 % or more)](#m-cr) → [MV Circuit Assembler in the cleanroom · 20 s · 120 EU/t](#m-m3), [HV Circuit Assembler in the cleanroom · 40 s · 480 EU/t](#m-m4)

## How to build

1. Drawers first, one per part: RAM chips, CPU chips, plastic printed boards, resistors, capacitors, inductors, transistors, diodes, fine red alloy wire, fine electrum wire, blue alloy bolts, annealed copper wire, aluminium frames. A tin drum for every assembler. Each assembler has its own input drawers behind Modular Routers or Pipez item pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output, so the next stage only takes what it needs. — `functionalstorage:oak_1`, `gtceu:ram_chip`, `gtceu:cpu_chip`, `gtceu:plastic_printed_circuit_board`
2. Stage 1, MV Circuit Assembler: plastic printed board + 1 CPU chip + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire → 2 Microprocessors in 10 s at 60 EU/t. Keep it as its own machine; it is the same machine as the HV chain’s second route. — `gtceu:mv_circuit_assembler`, `gtceu:micro_processor`
3. Stage 2, a second MV Circuit Assembler: board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire + 288 mB tin → 2 Microprocessor Assemblies in 20 s at 120 EU/t. No cleanroom here. Inductors: MV Assembler, steel ring + 2 fine copper wire + 36 mB polyethylene → 2 (16 s); capacitors: polyethylene foil + 2 aluminium foil + 144 mB polyethylene → 8 (16 s). — `gtceu:mv_circuit_assembler`, `gtceu:micro_processor_assembly`, `gtceu:inductor`
4. Stage 3 inside the Cleanroom: a third MV Circuit Assembler. Board + 2 assemblies + 4 diodes + 4 RAM + 16 fine electrum wire + 16 blue alloy bolts + 288 mB tin → 1 Microprocessor Supercomputer (the first EV circuit), 20 s at 120 EU/t. Place the assembler inside the room before you close the walls (machines standing in the room join it), and bring items and fluids in through passthrough hatches in the wall (see the cleanroom chain). — `gtceu:cleanroom`, `gtceu:mv_circuit_assembler`, `gtceu:micro_processor_computer`
5. Stage 4 inside the Cleanroom: HV Circuit Assembler (build it from 2 supercomputers first). 2 aluminium frames + 2 supercomputers + 8 inductors + 16 capacitors + 16 RAM + 16 annealed copper single wire + 576 mB tin → 1 Microprocessor Mainframe, 40 s at 480 EU/t. That is the IV circuit the robot arms, emitters, sensors, IV assembler and almost every IV machine ask for. — `gtceu:hv_circuit_assembler`, `gtceu:micro_processor_mainframe`, `gtceu:aluminium_frame`
6. RAM and CPU are the same wafer line as the HV circuits: boule, cutter, MV Laser Engraver with the green (RAM) and light blue (CPU) lens, then the cutter again (32 RAM chips or 8 CPU chips per wafer). One mainframe uses 32 RAM, so one RAM wafer per mainframe and 2 CPU chips from a quarter of a CPU wafer; the boule (7.5 min) is the real limit, about 2 wafers a minute. — `gtceu:ram_chip`, `gtceu:silicon_wafer`, `gtceu:mv_laser_engraver`
7. Supercomputer parts: blue alloy bolts via MV Extruder (1 ingot → 8 bolts, 15 ticks, 120 EU/t) from blue alloy ingots (mixer dust, then furnace); fine electrum wire: wiremill circuit 3, 1 electrum ingot → 8. 16 of each per supercomputer, so a drawer of 32 of each covers a mainframe. — `gtceu:blue_alloy_ingot`, `gtceu:blue_alloy_bolt`, `gtceu:fine_electrum_wire`
8. Diodes (4 per supercomputer) come from the MV diode line (gallium arsenide small dust + glass or polyethylene + fine copper wire, 20 s at 30 EU/t, 4 diodes with annealed fine wire and polyethylene). Annealed copper single wire from annealed copper ingots in a wiremill; one mainframe takes 16. — `gtceu:diode`, `gtceu:annealed_copper_single_wire`
9. Easy to miss: the mainframe is built from the HV tin, so the whole line is one big stock problem, not a power problem (peak 480 EU/t). Build stage 1 and 2 first and let them stock 8 assemblies before you start the cleanroom stages; set Keep Exact on every stage output to 16 so nothing floods the cleanroom feeders. — `functionalstorage:oak_1`, `gtceu:micro_processor_mainframe`

## Tips

- What the era needs: the first IV circuit is the Microprocessor Mainframe (pack quest: first IV circuit; second is the Nanoprocessor Supercomputer). The same line up from the HV chain: Microchip (LV) → Microprocessor (MV) → Microprocessor Assembly (HV) → Microprocessor Supercomputer (EV) → Mainframe (IV). Item ids: micro\_processor, micro\_processor\_assembly, micro\_processor\_computer, micro\_processor\_mainframe.
- It is the cheap route on purpose: only silicon wafers (RAM, CPU), plain boards and no laser lens beyond the HV chain. The Nanoprocessor Supercomputer needs NOR chips from phosphorus wafers and 600 EU/t (an EV Circuit Assembler); the Quantum Processor Assembly needs 2400 EU/t, i.e. an IV Circuit Assembler, which itself needs 2 LuV circuits; the Crystal Processor needs a 5000 K crystal chip. None of them is an IV starting point.
- Recipes (CircuitRecipes, not changed by the pack): Microprocessor = plastic printed board + CPU + 4 resistors + 4 capacitors + 4 transistors + 4 fine red alloy wire, 200 ticks at 60 EU/t, gives 2. Assembly = board + 2 microprocessors + 4 inductors + 8 capacitors + 4 RAM + 8 fine red alloy wire + solder, 400 ticks at 120 EU/t, gives 2, no cleanroom. Supercomputer (workstation\_ev) = board + 2 assemblies + 4 diodes + 4 RAM + 16 fine electrum wire + 16 blue alloy bolts + solder, 400 ticks at 120 EU/t, CLEANROOM. Mainframe (mainframe\_iv) = 2 aluminium frames + 2 supercomputers + 8 inductors + 16 capacitors + 16 RAM + 16 annealed copper single wire + solder x4, 800 ticks at 480 EU/t, CLEANROOM.
- Solder: the assembly and supercomputer recipes take 288 mB tin (or 144 mB soldering alloy); the mainframe takes 576 mB tin (or 288 mB soldering alloy). Every circuit assembler recipe also carries solder (jar GTRecipeTypes: 144 mB tin or 72 mB soldering alloy, times the multiplier), so even the plain microprocessor takes 144 mB. A recipe with all items present but an empty solder drum just sits there: one tin drum per assembler.
- Raw cost of one mainframe: 6 plastic printed boards, 2 CPU chips, 32 RAM chips (one RAM wafer gives 32), 16 inductors, 40 capacitors, 8 diodes, 8 resistors, 8 transistors, 32 fine electrum wire (4 electrum ingots), 32 blue alloy bolts (4 blue alloy ingots in an extruder, 8 bolts each), 24 fine red alloy wire, 16 annealed copper wire, 2 aluminium frames and roughly 2 B tin of solder in all. Micro 2 crafts, assembly 2 crafts, supercomputer 2 crafts per mainframe.
- Machines: one MV Circuit Assembler per stage (micro, assembly, supercomputer) and one HV Circuit Assembler for the mainframe keep the line 1:1:1:1 at 1.5 mainframes a minute (the 40 s mainframe is the slow step, 2 supercomputers = 40 s of one MV machine). The HV Circuit Assembler needs 2 EV circuits to build, so make the first supercomputers on the MV machine, then the HV machine from them.
- Cleanroom: only the supercomputer and mainframe recipes carry the cleanroom tag, so only those two assemblers go inside. A standard (not sterile) Cleanroom is enough; it runs the recipe only while the clean amount is 95 % or more (see the hv\_cleanroom chain).
- Blue alloy: 1 silver dust + 4 electrotine dust in a mixer (circuit 2, 100 ticks, 7 EU/t) and the dust goes to a furnace; electrotine = redstone + electrum dust in a mixer (circuit 1, 200 ticks). Annealed copper wire comes from annealed copper ingots; the only recipe found is the arc furnace recycling rule for copper items (RecyclingRecipes). Unverified: its oxygen and time, and whether a plain copper ingot is accepted: read the arc furnace in EMI first.
- Sub-steps people skip: (1) the HV Circuit Assembler cannot be built before the supercomputers, so keep 2 aside; (2) inductors and capacitors are the real bulk (56 per mainframe), build 2 MV assemblers for them; (3) put the tin drum on every assembler, not only the cleanroom ones; (4) RAM is the shared part: 32 of 32 RAM chips in a wafer go into one mainframe, so keep a RAM drawer with Keep Exact 64 on the cutter; (5) never mix the plain and the printed board.
- **Unverified** the annealed copper wire source above, how a cable reaches a machine inside the room, and the exact yield of blue alloy dust from the mixer (1 dust is assumed from the output line).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_circuit_assembler` | 3 |
| `gtceu:hv_circuit_assembler` | 1 |
| `gtceu:cleanroom` | 1 |
| `gtceu:mv_assembler` | 2 |
| `gtceu:mv_extruder` | 1 |
| `gtceu:lv_wiremill` | 2 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [Silicon wafers &amp; chips](../mv/wafer.md), [Polyethylene](../mv/polyethylene.md)
- **Feeds:** [EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull](../ev/ev_components.md), [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](iv_components.md), [Combo: Perfect-OC cubes (Multiblock Upgrade Kit) built as a quad](../combos/combo_cubes.md), [Combo: Extreme Chemical Reactor with a parallel hatch](../combos/combo_ecr.md)
- **Main source for:** `gtceu:micro_processor_mainframe`, `gtceu:micro_processor_computer`
