---
kind: chain
id: zpm_data
order: 1320
data:
  t: |-
    Research data: data stick (IV Scanner: ZPM motor, pump, piston, conveyor, arm) and data orb (Research Station: emitter, sensor, field generator, hatches)
  inf: true
  "n":
    - - p1
      - Plastic board · 2 CPU · 32 NAND chip · 4 RAM · 16 fine red alloy wire · 4 polyethylene plate
      - g
      - functionalstorage:oak_1
      - - [Plastic circuit board, "gtceu:plastic_circuit_board"]
        - [CPU, "gtceu:cpu_chip"]
        - [NAND chip, "gtceu:nand_memory_chip"]
        - [RAM chip, "gtceu:ram_chip"]
    - [m1, "Circuit Assembler in the cleanroom · 20 s · 90 EU/t", m, "gtceu:mv_circuit_assembler"]
    - [ds, Data Stick, x, "gtceu:data_stick"]
    - - p2
      - Advanced board · 2 HV circuit · 4 RAM · 32 NOR chip · 64 NAND chip · 32 fine platinum wire
      - g
      - functionalstorage:oak_1
      - - [Advanced circuit board, "gtceu:epoxy_printed_circuit_board"]
        - [NOR chip, "gtceu:nor_memory_chip"]
        - [NAND chip, "gtceu:nand_memory_chip"]
        - [RAM chip, "gtceu:ram_chip"]
    - [m2, "EV Circuit Assembler in the cleanroom · 20 s · 1200 EU/t", m, "gtceu:ev_circuit_assembler"]
    - [do, Data Orb, x, "gtceu:data_orb"]
    - [s1, "IV Scanner · 90 s · 7680 EU/t · LuV motor, pump, piston, conveyor, robot arm", m, "gtceu:iv_scanner"]
    - - s2
      - Research Station · 4 CWU/t · 30 720 EU/t · LuV emitter, sensor, field generator
      - m
      - gtceu:research_station
    - [dh, "Data Access Hatch (EV) or Data Bank", m, "gtceu:data_access_hatch"]
    - [al, "Assembly Line · ZPM part recipe", m, "gtceu:assembly_line"]
    - [zc, "ZPM components (zpm_components chains)", o, "gtceu:zpm_electric_motor"]
  e:
    - [p1, m1, "1"]
    - [m1, ds, "1 / 20 s"]
    - [p2, m2, "1"]
    - [m2, do, "1 / 20 s"]
    - [ds, s1, stick per part type]
    - [do, s2, orb per research]
    - [s1, dh, stick with scan]
    - [s2, dh, orb with research]
    - [dh, al, data]
    - [al, zc, "1 / 30 s"]
  tips:
    - |-
      Two kinds of data. The Research Station tooltip (GT lang file): it scans onto DATA ORBS and DATA MODULES; the scanner writes onto data STICKS. So every scanner research of this era (ZPM motor, pump, piston, conveyor, robot arm, quantum mainframe, crystal computer, Object Holder) needs a stick and every station research (emitter, sensor, field generator, ZPM hatches, Advanced Data Access Hatch, MK II reactor, crystal mainframe and the era multis) needs an ORB. In the pack’s own gate recipes (recipe_helpers.js getDataItem) the data item grows with the CWU/t: below 32 a data orb, 32 to 159 a data module, 160 to 319 a data DNA disk, 320 and more a component data core; all ZPM-era researches in this guide are below 32 CWU/t, so orbs.
    - |-
      Which research each ZPM-era recipe wants (verified: utils/tier_data.js zpm row, luv_to_uv_components.js, ComputerRecipes, MetaTileEntityMachineRecipeLoader, circuits.js, start_fusion_machines.js, misc.js, vacuum_chemical_reactor.js). SCANNER, a stick: LuV motor, pump, piston, conveyor module, robot arm for the ZPM ones, 1800 ticks (90 s) at 7680 EU/t (an IV Scanner); quantum computer for the quantum mainframe (1200 ticks, 7680); crystal assembly for the crystal computer (800 ticks); superconducting coil for the LuV fusion reactor; ZPM input bus for the Object Holder (2400 ticks). STATION, an orb: LuV emitter, sensor, field generator, 4 CWU/t at 30 720 EU/t; LuV energy and dynamo hatch, 8 CWU/t; the Data Bank, 4 CWU/t (Advanced Data Access Hatch); LuV fusion reactor, 16 CWU/t (ZPM Fusion); crystal computer, 16 CWU/t (crystal mainframe); ZPM assembler, electric furnace, lathe, laser engraver, 16 CWU/t (Component Part Assembly, Heat Chamber, Large Rotor Machine, runic engraver); ZPM gas collector, activated rod, coordinate crystal 24 CWU/t.
    - |-
      Data Stick (CircuitRecipes data_stick): plastic circuit board + 2 CPU chips + 32 NAND chips + 4 RAM chips + 16 fine red alloy wire + 4 polyethylene plates, circuit assembler in a CLEANROOM, 400 ticks at 90 EU/t, soldering x2 (an MV Circuit Assembler). Data Orb (data_orb): advanced circuit board (epoxy printed) + 2 HV circuits + 4 RAM + 32 NOR chips + 64 NAND chips + 32 fine platinum wire, cleanroom circuit assembler, 400 ticks at 1200 EU/t (an EV Circuit Assembler). One orb is 32 NOR + 64 NAND + 4 RAM chips; a station research per recipe type needs its own orb, so expect 10 or more orbs over the era (about 1000 chips). A used stick or orb is cleared by crafting it alone (data_stick_nbt, data_orb_nbt shapeless recipes in MachineRecipeLoader).
    - |-
      Reading data: an Assembly Line needs the research in a Data Access Hatch (slots for ‘Data Items’, both sticks and orbs) or in a Data Bank linked by optical data hatches (LuV tier; the Data Bank shares them between Assembly Lines and other Data Banks, and costs EU/t per hatch). Hatches (ComputerRecipes): Basic Data Access Hatch (HV) = HV input bus + 4 data sticks + 4 HV circuits + 288 mB polyethylene; Data Access Hatch (EV) = EV input bus + 4 data sticks + 4 EV circuits + 288 mB PTFE; Advanced Data Access Hatch (LuV) = LuV input bus + 4 data orbs + 4 ZPM circuits + 576 mB soldering alloy + 576 mB PBI, Assembly Line 400 ticks at 6000 EU/t with station research of the Data Bank at 4 CWU/t. Unverified: the slot count of each hatch (read the tooltip).
    - |-
      Scanner vs station: the pack gives the five mechanical parts a plain scan because no CWU is needed, so you can make ZPM motors, pumps, pistons, conveyors and arms BEFORE the Research Station exists. Only emitter, sensor, field generator (and with them the field generator machines, the fusion coil, the ZPM hatches) are gated by the station. The station also runs faster with more computation (research station tooltip) and the quest gives a 2.5 % additive CWU discount per overclock. Scanner recipes at 7680 EU/t need an IV Scanner; the LuV Scanner of the luv_research chain is only for the Research Station’s own Assembly Line scan.
    - |-
      Sub-steps people skip: (1) clear a used stick or orb before scanning a new part (shapeless crafting of the data item alone); (2) station research needs the item inside the Object Holder AND an orb, so the Object Holder must exist before the field-generator line starts; (3) a scan result is per recipe: the LuV motor scan works for the ZPM motor recipe only; (4) keep one spare of every LuV part, scans need the real item; (5) the stick or orb that goes into the Data Access Hatch stays there while the line runs; (6) the chips for orbs (NOR and NAND) come from the same wafer lines as the circuits: start them early.
    - |-
      Unverified: that the scanned or researched item is not consumed (GT default; check on the first scan), the total CWU of a default station research (the pack sets its own totalCWU only on its own recipes: for the gate parts 24 CWU/t x 600 ticks, for the data-core ones 320 CWU/t x 1200 ticks), and the slot counts of the hatches.
  b:
    - ["gtceu:mv_circuit_assembler", 1]
    - ["gtceu:ev_circuit_assembler", 1]
    - ["gtceu:iv_scanner", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_access_hatch", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 1]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:nand_memory_chip", "gtceu:ram_chip", "gtceu:plastic_circuit_board"]
      t: |-
        Drawers first, one per part: plastic boards, CPU chips, NAND chips, NOR chips, RAM chips, advanced boards, HV circuits, polyethylene plates, fine red alloy wire, fine platinum wire. Each circuit assembler gets its own input drawers behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:mv_circuit_assembler", "gtceu:data_stick"]
      t: |-
        Sticks: an MV Circuit Assembler in the cleanroom, plastic board + 2 CPU + 32 NAND + 4 RAM + 16 fine red alloy wire + 4 polyethylene plates → 1 stick in 20 s at 90 EU/t. Make about 8: one per scanned part type.
    - i: ["gtceu:ev_circuit_assembler", "gtceu:data_orb"]
      t: |-
        Orbs: an EV Circuit Assembler in the cleanroom, advanced board + 2 HV circuits + 4 RAM + 32 NOR + 64 NAND + 32 fine platinum wire → 1 orb in 20 s at 1200 EU/t. One for the Data Bank, one for the HPCA, one per station research.
    - i: ["gtceu:iv_scanner", "gtceu:luv_electric_motor", "gtceu:data_stick"]
      t: |-
        Scan: put a stick and a LuV motor in an IV Scanner (90 s, 7680 EU/t); the stick now holds the ZPM motor research. Repeat for pump, piston, conveyor module and robot arm, one stick each. Wire the scanner to an IV line, not the LV network.
    - i: ["gtceu:research_station", "gtceu:luv_emitter", "gtceu:data_orb"]
      t: |-
        Station research (after zpm_research): an orb in the Object Holder with the LuV emitter, 4 CWU/t for the run, 30 720 EU/t. One orb each for emitter, sensor and field generator. Keep the computation hatch fed: the HPCA must be on.
    - i: ["gtceu:data_access_hatch", "gtceu:assembly_line", "gtceu:data_orb"]
      t: |-
        Load: sticks and orbs into the Data Access Hatch of the Assembly Line that makes the part (one line per part family, or a Data Bank with optical hatches for all of them). Buses must match the recipe order; the data item lets the recipe show up.
    - i: ["functionalstorage:oak_1", "gtceu:data_orb"]
      t: |-
        Easy to miss: sticks are cheap but orbs are not; the NAND/NOR load of 10 orbs is the same as 4 Nanoprocessor mainframes. Do not scan before the Assembly Line and its ingredients exist, a data item you wait on is one you cannot reuse.
---
# Research data: data stick (IV Scanner: ZPM motor, pump, piston, conveyor, arm) and data orb (Research Station: emitter, sensor, field generator, hatches)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_data` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Research Station, HPCA and data](../../plan/p12.md#research)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-m1">
<div class="gt-head"><span class="gt-mname">Circuit Assembler in the cleanroom · 20 s · 90 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Plastic board · 2 CPU · 32 NAND chip · 4 RAM · 16 fine red alloy wire · 4 polyethylene plate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Plastic board · 2 CPU · 32 NAND chip · 4 RAM · 16 fine red alloy wire · 4 polyethylene plate</span><span class="gt-sub"><span>Plastic circuit board</span><span>CPU</span><span>NAND chip</span><span>RAM chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data Stick (gtceu:data_stick) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__data_stick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Stick</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-ev" id="m-m2">
<div class="gt-head"><span class="gt-mname">EV Circuit Assembler in the cleanroom · 20 s · 1200 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Advanced board · 2 HV circuit · 4 RAM · 32 NOR chip · 64 NAND chip · 32 fine platinum wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Advanced board · 2 HV circuit · 4 RAM · 32 NOR chip · 64 NAND chip · 32 fine platinum wire</span><span class="gt-sub"><span>Advanced circuit board</span><span>NOR chip</span><span>NAND chip</span><span>RAM chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data Orb (gtceu:data_orb) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_circuit_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-s1">
<div class="gt-head"><span class="gt-mname">IV Scanner · 90 s · 7680 EU/t · LuV motor, pump, piston, conveyor, robot arm</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Stick (gtceu:data_stick) - stick per part type"><img class="gt-ico" src="../../assets/icons/gtceu__data_stick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Stick</span><b class="gt-q">stick per part type</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_scanner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dh" title="Data Access Hatch (EV) or Data Bank (gtceu:data_access_hatch) - stick with scan"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Access Hatch</span><span class="gt-note">Data Access Hatch (EV) or Data Bank</span><b class="gt-q">stick with scan</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_scanner</code></div>
</div>
<div class="gt-panel t-mod" id="m-s2">
<div class="gt-head"><span class="gt-mname">Research Station · 4 CWU/t · 30 720 EU/t · LuV emitter, sensor, field generator</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Orb (gtceu:data_orb) - orb per research"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><b class="gt-q">orb per research</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dh" title="Data Access Hatch (EV) or Data Bank (gtceu:data_access_hatch) - orb with research"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Access Hatch</span><span class="gt-note">Data Access Hatch (EV) or Data Bank</span><b class="gt-q">orb with research</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-mod" id="m-dh">
<div class="gt-head"><span class="gt-mname">Data Access Hatch (EV) or Data Bank</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-s1" title="IV Scanner · 90 s · 7680 EU/t · LuV motor, pump, piston, conveyor, robot arm (gtceu:iv_scanner) - stick with scan"><img class="gt-ico" src="../../assets/icons/gtceu__iv_scanner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Scanner</span><span class="gt-note">IV Scanner · 90 s · 7680 EU/t · LuV motor, pump, piston, conveyor, robot arm</span><b class="gt-q">stick with scan</b></a><a class="gt-slot gt-mach" href="#m-s2" title="Research Station · 4 CWU/t · 30 720 EU/t · LuV emitter, sensor, field generator (gtceu:research_station) - orb with research"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station · 4 CWU/t · 30 720 EU/t · LuV emitter, sensor, field generator</span><b class="gt-q">orb with research</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · ZPM part recipe (gtceu:assembly_line) - data"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · ZPM part recipe</span><b class="gt-q">data</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:data_access_hatch</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · ZPM part recipe</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-dh" title="Data Access Hatch (EV) or Data Bank (gtceu:data_access_hatch) - data"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Access Hatch</span><span class="gt-note">Data Access Hatch (EV) or Data Bank</span><b class="gt-q">data</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM components (zpm_components chains) (gtceu:zpm_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Motor</span><span class="gt-note">ZPM components (zpm_components chains)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Circuit Assembler in the cleanroom · 20 s · 90 EU/t](#m-m1) → [IV Scanner · 90 s · 7680 EU/t · LuV motor, pump, piston, conveyor, robot arm](#m-s1) → [Data Access Hatch (EV) or Data Bank](#m-dh) → [Assembly Line · ZPM part recipe](#m-al)
- [EV Circuit Assembler in the cleanroom · 20 s · 1200 EU/t](#m-m2) → [Research Station · 4 CWU/t · 30 720 EU/t · LuV emitter, sensor, field generator](#m-s2) → [Data Access Hatch (EV) or Data Bank](#m-dh)

## How to build

1. Drawers first, one per part: plastic boards, CPU chips, NAND chips, NOR chips, RAM chips, advanced boards, HV circuits, polyethylene plates, fine red alloy wire, fine platinum wire. Each circuit assembler gets its own input drawers behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:nand_memory_chip`, `gtceu:ram_chip`, `gtceu:plastic_circuit_board`
2. Sticks: an MV Circuit Assembler in the cleanroom, plastic board + 2 CPU + 32 NAND + 4 RAM + 16 fine red alloy wire + 4 polyethylene plates → 1 stick in 20 s at 90 EU/t. Make about 8: one per scanned part type. — `gtceu:mv_circuit_assembler`, `gtceu:data_stick`
3. Orbs: an EV Circuit Assembler in the cleanroom, advanced board + 2 HV circuits + 4 RAM + 32 NOR + 64 NAND + 32 fine platinum wire → 1 orb in 20 s at 1200 EU/t. One for the Data Bank, one for the HPCA, one per station research. — `gtceu:ev_circuit_assembler`, `gtceu:data_orb`
4. Scan: put a stick and a LuV motor in an IV Scanner (90 s, 7680 EU/t); the stick now holds the ZPM motor research. Repeat for pump, piston, conveyor module and robot arm, one stick each. Wire the scanner to an IV line, not the LV network. — `gtceu:iv_scanner`, `gtceu:luv_electric_motor`, `gtceu:data_stick`
5. Station research (after zpm\_research): an orb in the Object Holder with the LuV emitter, 4 CWU/t for the run, 30 720 EU/t. One orb each for emitter, sensor and field generator. Keep the computation hatch fed: the HPCA must be on. — `gtceu:research_station`, `gtceu:luv_emitter`, `gtceu:data_orb`
6. Load: sticks and orbs into the Data Access Hatch of the Assembly Line that makes the part (one line per part family, or a Data Bank with optical hatches for all of them). Buses must match the recipe order; the data item lets the recipe show up. — `gtceu:data_access_hatch`, `gtceu:assembly_line`, `gtceu:data_orb`
7. Easy to miss: sticks are cheap but orbs are not; the NAND/NOR load of 10 orbs is the same as 4 Nanoprocessor mainframes. Do not scan before the Assembly Line and its ingredients exist, a data item you wait on is one you cannot reuse. — `functionalstorage:oak_1`, `gtceu:data_orb`

## Tips

- Two kinds of data. The Research Station tooltip (GT lang file): it scans onto DATA ORBS and DATA MODULES; the scanner writes onto data STICKS. So every scanner research of this era (ZPM motor, pump, piston, conveyor, robot arm, quantum mainframe, crystal computer, Object Holder) needs a stick and every station research (emitter, sensor, field generator, ZPM hatches, Advanced Data Access Hatch, MK II reactor, crystal mainframe and the era multis) needs an ORB. In the pack’s own gate recipes (recipe\_helpers.js getDataItem) the data item grows with the CWU/t: below 32 a data orb, 32 to 159 a data module, 160 to 319 a data DNA disk, 320 and more a component data core; all ZPM-era researches in this guide are below 32 CWU/t, so orbs.
- Which research each ZPM-era recipe wants (verified: utils/tier\_data.js zpm row, luv\_to\_uv\_components.js, ComputerRecipes, MetaTileEntityMachineRecipeLoader, circuits.js, start\_fusion\_machines.js, misc.js, vacuum\_chemical\_reactor.js). SCANNER, a stick: LuV motor, pump, piston, conveyor module, robot arm for the ZPM ones, 1800 ticks (90 s) at 7680 EU/t (an IV Scanner); quantum computer for the quantum mainframe (1200 ticks, 7680); crystal assembly for the crystal computer (800 ticks); superconducting coil for the LuV fusion reactor; ZPM input bus for the Object Holder (2400 ticks). STATION, an orb: LuV emitter, sensor, field generator, 4 CWU/t at 30 720 EU/t; LuV energy and dynamo hatch, 8 CWU/t; the Data Bank, 4 CWU/t (Advanced Data Access Hatch); LuV fusion reactor, 16 CWU/t (ZPM Fusion); crystal computer, 16 CWU/t (crystal mainframe); ZPM assembler, electric furnace, lathe, laser engraver, 16 CWU/t (Component Part Assembly, Heat Chamber, Large Rotor Machine, runic engraver); ZPM gas collector, activated rod, coordinate crystal 24 CWU/t.
- Data Stick (CircuitRecipes data\_stick): plastic circuit board + 2 CPU chips + 32 NAND chips + 4 RAM chips + 16 fine red alloy wire + 4 polyethylene plates, circuit assembler in a CLEANROOM, 400 ticks at 90 EU/t, soldering x2 (an MV Circuit Assembler). Data Orb (data\_orb): advanced circuit board (epoxy printed) + 2 HV circuits + 4 RAM + 32 NOR chips + 64 NAND chips + 32 fine platinum wire, cleanroom circuit assembler, 400 ticks at 1200 EU/t (an EV Circuit Assembler). One orb is 32 NOR + 64 NAND + 4 RAM chips; a station research per recipe type needs its own orb, so expect 10 or more orbs over the era (about 1000 chips). A used stick or orb is cleared by crafting it alone (data\_stick\_nbt, data\_orb\_nbt shapeless recipes in MachineRecipeLoader).
- Reading data: an Assembly Line needs the research in a Data Access Hatch (slots for ‘Data Items’, both sticks and orbs) or in a Data Bank linked by optical data hatches (LuV tier; the Data Bank shares them between Assembly Lines and other Data Banks, and costs EU/t per hatch). Hatches (ComputerRecipes): Basic Data Access Hatch (HV) = HV input bus + 4 data sticks + 4 HV circuits + 288 mB polyethylene; Data Access Hatch (EV) = EV input bus + 4 data sticks + 4 EV circuits + 288 mB PTFE; Advanced Data Access Hatch (LuV) = LuV input bus + 4 data orbs + 4 ZPM circuits + 576 mB soldering alloy + 576 mB PBI, Assembly Line 400 ticks at 6000 EU/t with station research of the Data Bank at 4 CWU/t. Unverified: the slot count of each hatch (read the tooltip).
- Scanner vs station: the pack gives the five mechanical parts a plain scan because no CWU is needed, so you can make ZPM motors, pumps, pistons, conveyors and arms BEFORE the Research Station exists. Only emitter, sensor, field generator (and with them the field generator machines, the fusion coil, the ZPM hatches) are gated by the station. The station also runs faster with more computation (research station tooltip) and the quest gives a 2.5 % additive CWU discount per overclock. Scanner recipes at 7680 EU/t need an IV Scanner; the LuV Scanner of the luv\_research chain is only for the Research Station’s own Assembly Line scan.
- Sub-steps people skip: (1) clear a used stick or orb before scanning a new part (shapeless crafting of the data item alone); (2) station research needs the item inside the Object Holder AND an orb, so the Object Holder must exist before the field-generator line starts; (3) a scan result is per recipe: the LuV motor scan works for the ZPM motor recipe only; (4) keep one spare of every LuV part, scans need the real item; (5) the stick or orb that goes into the Data Access Hatch stays there while the line runs; (6) the chips for orbs (NOR and NAND) come from the same wafer lines as the circuits: start them early.
- **Unverified** that the scanned or researched item is not consumed (GT default; check on the first scan), the total CWU of a default station research (the pack sets its own totalCWU only on its own recipes: for the gate parts 24 CWU/t x 600 ticks, for the data-core ones 320 CWU/t x 1200 ticks), and the slot counts of the hatches.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_circuit_assembler` | 1 |
| `gtceu:ev_circuit_assembler` | 1 |
| `gtceu:iv_scanner` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:data_access_hatch` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 1 |

## Needs / Feeds

- **Main source for:** `gtceu:data_orb`
