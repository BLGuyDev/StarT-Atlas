---
kind: chain
id: luv_assembly_line
order: 1220
data:
  t: |-
    Assembly Line: scan the IV part on a data stick, put it in a Data Access Hatch, one ULV bus per ingredient, IV energy hatch
  inf: true
  "n":
    - [ds, Blank Data Stick, i, "gtceu:data_stick"]
    - [it, "The IV part to scan (IV motor, piston, pump ...)", i, "gtceu:iv_electric_motor"]
    - - sc
      - EV Scanner · 90 s · 1920 EU/t (IV Scanner · 3 s · 7680 EU/t for emitter, sensor, field generator)
      - m
      - gtceu:ev_scanner
    - [rs, Data Stick with research, x, "gtceu:data_stick"]
    - [dh, Data Access Hatch in a grating spot of the line, m, "gtceu:data_access_hatch"]
    - - bu
      - ULV Input Buses, one per ingredient, in recipe order
      - g
      - functionalstorage:oak_1
      - [[ULV Input Bus, "gtceu:ulv_input_bus"], ["Input Hatch (fluids)", "gtceu:ev_input_hatch"]]
    - [eh, "IV Energy Input Hatch · 7680 EU/t", m, "gtceu:iv_energy_input_hatch"]
    - [al, "Assembly Line · 5 slices minimum, +1 slice per extra ingredient", m, "gtceu:assembly_line"]
    - [ob, Output Bus, m, "gtceu:ulv_output_bus"]
    - [pr, LuV component, o, "gtceu:luv_electric_motor"]
  e:
    - [ds, sc, "1"]
    - [it, sc, "1"]
    - [sc, rs, "1"]
    - [rs, dh, "1"]
    - [dh, al, research]
    - [bu, al, ordered]
    - [eh, al]
    - [al, ob]
    - [ob, pr, "1 / 30 s"]
  tips:
    - |-
      Tier check: the Assembly Line controller is an IV craft (4 control casings + 2 IV robot arms + 2 IV circuits + IV hull), so it can be built before any LuV part. The LuV hull does not use it (see luv_hull); the line is for the LuV components (motor, piston, pump, conveyor, robot arm, emitter, sensor, field generator; the LuV fluid regulator is a plain assembler recipe). Its casings need HPIC chips and ruridit gears (unit: 2 ruridit gears + 2 IV robot arms; control casing: 4 EV circuits + HPIC chip + IV sensor + emitter + motor), so the platinum group line must already run.
    - |-
      Blank Data Stick (CircuitRecipes data_stick): plastic circuit board + 2 CPU chips + 32 NAND memory chips + 4 RAM + 16 fine red alloy wire + 4 polyethylene plates + solder x2, circuit assembler in the CLEANROOM, 400 ticks at 90 EU/t (an MV Circuit Assembler). You need one stick per product, so a drawer of 8.
    - |-
      Why the line: all LuV components are Assembly Line recipes in this pack. The pack script luv_to_uv_components.js removes the vanilla recipes (gtceu:assembly_line/<part>_luv) and rebuilds motor, pump, conveyor, piston, robot arm, field generator, emitter and sensor from the table in utils/tier_data.js: 600 ticks (30 s) at VA[IV] = 7680 EU/t each, with a data-stick (scanner) research of the IV part. The quest also says: get used to making all components in an Assembly Line.
    - |-
      Research (scanner): the five basic parts (motor, pump, conveyor, piston, robot arm) need a stick scanned from the IV version: 1800 ticks (90 s) at 1920 EU/t, so an EV Scanner. Emitter, sensor and field generator need an IV scan: 60 ticks (3 s) at 7680 EU/t, so an IV Scanner. The vanilla scanner recipes are removed and regenerated from the pack table. Scanner machine recipe (MetaTileEntityLoader): hull + emitter + sensor of its own tier + 4 circuits one tier up + 2 cables, so the EV Scanner eats 4 IV circuits and the IV Scanner 4 LuV circuits (4 nano mainframes) plus an IV emitter and IV sensor. The LuV Scanner (only for the research station) 4 ZPM circuits: not needed here.
    - |-
      Structure (multis card, vanilla pattern with the pack’s block names): every slice is steel solid casing, one ULV Input Bus, laminated glass, an assembly line unit, a control casing and a grating; the last slice has the Output Bus instead of the bus; the energy hatch goes in the casing row at the bottom, input hatches in the steel casing at the corners. The pattern repeats 3 to 15 times, so a line can have 4 to 16 item buses; the minimum line (5 slices) holds only 4 buses. A motor has 6 ingredients, an emitter 8 (rhodium foil as two stacks), a robot arm 9, a field generator 8: build the line with at least 10 slices, the repeatable middle slices simply get longer.
    - |-
      Assembly Line Unit (crafting, 2 per craft): 4 steel plates + 2 ruridit gears + 2 IV robot arms + 1 tungsten steel frame. Control casing: 4 EV circuits + 1 HPIC chip + 1 IV sensor + 1 IV emitter + 1 IV motor + 1 tungsten steel frame → 2. Grating: 6 iron bars + 1 steel rotor + 1 steel frame + 1 MV motor → 2. Controller: IV hull + 4 control casings + 2 IV robot arms + 2 IV circuits. A minimal line is 5 units, 5 control casings (3 crafts), 9 gratings, 10 laminated glass, 15 steel casings, 4 ULV buses; more slices cost 1 unit, 1 control casing, 1 grating, 2 glass and a bus each.
    - |-
      Ordered inputs: orderedAssemblyLineItems is true, orderedAssemblyLineFluids is false (config/gtceu.yaml). Items must sit in the buses in the exact order of the recipe (look at the recipe in EMI; the first ingredient goes into the first bus, starting at the controller end). Fluids can go in any input hatch. A ULV bus holds one stack, so 64 fine palladium wire is one stack and the 96 rhodium foil of an emitter is TWO stacks (64 and 32) in two buses. A forming press with a rename tag separates identical-looking items (the quest tip).
    - |-
      Data Access Hatch (EV version): EV item input bus + 4 data sticks + 4 EV circuits + 288 mB PTFE, assembler in the cleanroom, 200 ticks at 1920 EU/t (ComputerRecipes). It replaces a grating block in the back row of a repeatable slice. Unverified: whether the cheaper HV Basic Data Access Hatch (4 HV circuits, 288 mB polyethylene) is accepted by the line; the Java predicate is dataHatchPredicate, so a data bank link or an optical one also counts.
    - |-
      Power: 7680 EU/t per recipe, so one IV Energy Hatch is enough (1 A, 8192 V); a second hatch only helps with overclocking. The line does not parallelise: a parallel hatch is not an option for the Assembly Line.
    - |-
      Sub-steps people skip: (1) scan each IV part separately: one stick per product, label them; (2) the IV field generator is not a machine part you already have, craft one first (see the iv_components tip); (3) a stick scanned at the EV scanner does NOT work for the emitter, sensor and field generator (their research has a higher EU/t); (4) the output bus is the last slice only, do not put an energy hatch there; (5) never mix two recipes in one line at once.
    - |-
      Unverified: whether the scanned IV part is consumed by the scanner (the extractor does not list research recipes), the best bus order direction (read the tooltip on the Assembly Line), and whether the data stick can sit in a Data Bank instead of a hatch (a data bank is an LuV-era multi; its link is an optical pipe).
    - The Blank Data Stick recipe is described above (circuit assembler in the cleanroom); the ZPM data chain only reuses it.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:ev_scanner", 1]
    - ["gtceu:iv_scanner", 1]
    - ["gtceu:data_access_hatch", 1]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["gtceu:ulv_input_bus", 12]
    - ["gtceu:ev_input_hatch", 2]
    - ["gtceu:ulv_output_bus", 1]
    - ["gtceu:data_stick", 8]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["gtceu:assembly_line", "gtceu:iv_machine_hull", "gtceu:iv_robot_arm"]
      t: |-
        Controller first: IV machine hull + 4 control casings + 2 IV robot arms + 2 IV circuits (crafting table). Then the casings: assembly line units (ruridit gears, IV robot arms) and control casings (EV circuits, HPIC chip, IV sensor, IV emitter, IV motor) all come from the IV component chain, so build a stock of IV arms and sensors first.
    - i: ["gtceu:ulv_input_bus", "gtceu:ulv_output_bus", "gtceu:ev_input_hatch"]
      t: |-
        Layout: stand the line at least 10 slices long on one wall so the buses are in one row of ULV Input Buses (one ingredient each) and the output bus is at the far end. Put 2 input hatches (fluids) on the steel casing corners and the IV Energy Hatch in the casing row on the floor.
    - i: ["gtceu:ev_scanner", "gtceu:data_stick", "gtceu:iv_electric_motor"]
      t: |-
        Scan: blank Data Stick + the IV part in the EV Scanner (90 s, 1920 EU/t) for motor, pump, conveyor, piston and robot arm; the IV Scanner (3 s, 7680 EU/t) for emitter, sensor and field generator. One stick per product; rename them with an anvil so you can tell them apart.
    - i: ["gtceu:data_access_hatch", "gtceu:data_stick"]
      t: Put the Data Access Hatch in a grating spot in the back row of a repeatable slice, drop the stick into it before you load the buses. The line only starts a recipe whose research the hatch holds.
    - i: ["functionalstorage:oak_1", "gtceu:ulv_input_bus", "modularrouters:modular_router"]
      t: |-
        Feed each bus from its own drawer by a Modular Router (or Pipez item pipe + Item Filter): drawer 1 → bus 1, and so on in recipe order. Fluids: one drum each for soldering alloy and lubricant (and styrene butadiene rubber for the conveyor), by Pipez fluid pipes to the input hatches.
    - i: ["gtceu:ulv_output_bus", "gtceu:lv_robot_arm", "gtceu:luv_electric_motor"]
      t: |-
        Output: the Output Bus at the end into a drawer with a Robot Arm cover in Keep Exact mode (Keep Exact 4 for motors, they are fed to three other products). One product at a time: clear the buses and swap the stick before you change recipe.
    - i: ["gtceu:iv_energy_input_hatch", "gtceu:assembly_line"]
      t: |-
        Easy to miss: the IV Energy Hatch is the one from the iv_hatches chain (HPIC chip line); with only an EV hatch the 7680 EU/t recipes will not start. Build that chain before the line.
---
# Assembly Line: scan the IV part on a data stick, put it in a Data Access Hatch, one ULV bus per ingredient, IV energy hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_assembly_line` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 12, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-sc">
<div class="gt-head"><span class="gt-mname">EV Scanner · 90 s · 1920 EU/t (IV Scanner · 3 s · 7680 EU/t for emitter, sensor, field generator)</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Blank Data Stick (gtceu:data_stick) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_stick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Stick</span><span class="gt-note">Blank Data Stick</span><b class="gt-q">1</b></span><span class="gt-slot" title="The IV part to scan (IV motor, piston, pump ...) (gtceu:iv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><span class="gt-note">The IV part to scan (IV motor, piston, pump ...)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_scanner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data Stick with research (gtceu:data_stick) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_stick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Stick</span><span class="gt-note">Data Stick with research</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_scanner</code></div>
</div>
<div class="gt-panel t-mod" id="m-dh">
<div class="gt-head"><span class="gt-mname">Data Access Hatch in a grating spot of the line</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Stick with research (gtceu:data_stick) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_stick.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Stick</span><span class="gt-note">Data Stick with research</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 5 slices minimum, +1 slice per extra ingredient (gtceu:assembly_line) - research"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 5 slices minimum, +1 slice per extra ingredient</span><b class="gt-q">research</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:data_access_hatch</code></div>
</div>
<div class="gt-panel t-iv" id="m-eh">
<div class="gt-head"><span class="gt-mname">IV Energy Input Hatch · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 5 slices minimum, +1 slice per extra ingredient (gtceu:assembly_line)"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 5 slices minimum, +1 slice per extra ingredient</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_energy_input_hatch</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 5 slices minimum, +1 slice per extra ingredient</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-dh" title="Data Access Hatch in a grating spot of the line (gtceu:data_access_hatch) - research"><img class="gt-ico" src="../../assets/icons/gtceu__data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Access Hatch</span><span class="gt-note">Data Access Hatch in a grating spot of the line</span><b class="gt-q">research</b></a><span class="gt-slot gt-group" title="ULV Input Buses, one per ingredient, in recipe order (functionalstorage:oak_1) - ordered"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ULV Input Buses, one per ingredient, in recipe order</span><span class="gt-sub"><span>ULV Input Bus</span><span>Input Hatch (fluids)</span></span><b class="gt-q">ordered</b></span><a class="gt-slot gt-mach" href="#m-eh" title="IV Energy Input Hatch · 7680 EU/t (gtceu:iv_energy_input_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Input Hatch</span><span class="gt-note">IV Energy Input Hatch · 7680 EU/t</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ob" title="Output Bus (gtceu:ulv_output_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__ulv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ULV Output Bus</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-ulv" id="m-ob">
<div class="gt-head"><span class="gt-mname">Output Bus</span><span class="gt-badge t-ulv">ULV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 5 slices minimum, +1 slice per extra ingredient (gtceu:assembly_line)"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 5 slices minimum, +1 slice per extra ingredient</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ulv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV component (gtceu:luv_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span><span class="gt-note">LuV component</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ulv_output_bus</code></div>
</div>
</div>

## Flow

- [EV Scanner · 90 s · 1920 EU/t (IV Scanner · 3 s · 7680 EU/t for emitter, sensor, field generator)](#m-sc) → [Data Access Hatch in a grating spot of the line](#m-dh) → [Assembly Line · 5 slices minimum, +1 slice per extra ingredient](#m-al) → [Output Bus](#m-ob)
- [IV Energy Input Hatch · 7680 EU/t](#m-eh) → [Assembly Line · 5 slices minimum, +1 slice per extra ingredient](#m-al)

## How to build

1. Controller first: IV machine hull + 4 control casings + 2 IV robot arms + 2 IV circuits (crafting table). Then the casings: assembly line units (ruridit gears, IV robot arms) and control casings (EV circuits, HPIC chip, IV sensor, IV emitter, IV motor) all come from the IV component chain, so build a stock of IV arms and sensors first. — `gtceu:assembly_line`, `gtceu:iv_machine_hull`, `gtceu:iv_robot_arm`
2. Layout: stand the line at least 10 slices long on one wall so the buses are in one row of ULV Input Buses (one ingredient each) and the output bus is at the far end. Put 2 input hatches (fluids) on the steel casing corners and the IV Energy Hatch in the casing row on the floor. — `gtceu:ulv_input_bus`, `gtceu:ulv_output_bus`, `gtceu:ev_input_hatch`
3. Scan: blank Data Stick + the IV part in the EV Scanner (90 s, 1920 EU/t) for motor, pump, conveyor, piston and robot arm; the IV Scanner (3 s, 7680 EU/t) for emitter, sensor and field generator. One stick per product; rename them with an anvil so you can tell them apart. — `gtceu:ev_scanner`, `gtceu:data_stick`, `gtceu:iv_electric_motor`
4. Put the Data Access Hatch in a grating spot in the back row of a repeatable slice, drop the stick into it before you load the buses. The line only starts a recipe whose research the hatch holds. — `gtceu:data_access_hatch`, `gtceu:data_stick`
5. Feed each bus from its own drawer by a Modular Router (or Pipez item pipe + Item Filter): drawer 1 → bus 1, and so on in recipe order. Fluids: one drum each for soldering alloy and lubricant (and styrene butadiene rubber for the conveyor), by Pipez fluid pipes to the input hatches. — `functionalstorage:oak_1`, `gtceu:ulv_input_bus`, `modularrouters:modular_router`
6. Output: the Output Bus at the end into a drawer with a Robot Arm cover in Keep Exact mode (Keep Exact 4 for motors, they are fed to three other products). One product at a time: clear the buses and swap the stick before you change recipe. — `gtceu:ulv_output_bus`, `gtceu:lv_robot_arm`, `gtceu:luv_electric_motor`
7. Easy to miss: the IV Energy Hatch is the one from the iv\_hatches chain (HPIC chip line); with only an EV hatch the 7680 EU/t recipes will not start. Build that chain before the line. — `gtceu:iv_energy_input_hatch`, `gtceu:assembly_line`

## Tips

- Tier check: the Assembly Line controller is an IV craft (4 control casings + 2 IV robot arms + 2 IV circuits + IV hull), so it can be built before any LuV part. The LuV hull does not use it (see luv\_hull); the line is for the LuV components (motor, piston, pump, conveyor, robot arm, emitter, sensor, field generator; the LuV fluid regulator is a plain assembler recipe). Its casings need HPIC chips and ruridit gears (unit: 2 ruridit gears + 2 IV robot arms; control casing: 4 EV circuits + HPIC chip + IV sensor + emitter + motor), so the platinum group line must already run.
- Blank Data Stick (CircuitRecipes data\_stick): plastic circuit board + 2 CPU chips + 32 NAND memory chips + 4 RAM + 16 fine red alloy wire + 4 polyethylene plates + solder x2, circuit assembler in the CLEANROOM, 400 ticks at 90 EU/t (an MV Circuit Assembler). You need one stick per product, so a drawer of 8.
- Why the line: all LuV components are Assembly Line recipes in this pack. The pack script luv\_to\_uv\_components.js removes the vanilla recipes (gtceu:assembly\_line/&lt;part&gt;\_luv) and rebuilds motor, pump, conveyor, piston, robot arm, field generator, emitter and sensor from the table in utils/tier\_data.js: 600 ticks (30 s) at VA\[IV\] = 7680 EU/t each, with a data-stick (scanner) research of the IV part. The quest also says: get used to making all components in an Assembly Line.
- Research (scanner): the five basic parts (motor, pump, conveyor, piston, robot arm) need a stick scanned from the IV version: 1800 ticks (90 s) at 1920 EU/t, so an EV Scanner. Emitter, sensor and field generator need an IV scan: 60 ticks (3 s) at 7680 EU/t, so an IV Scanner. The vanilla scanner recipes are removed and regenerated from the pack table. Scanner machine recipe (MetaTileEntityLoader): hull + emitter + sensor of its own tier + 4 circuits one tier up + 2 cables, so the EV Scanner eats 4 IV circuits and the IV Scanner 4 LuV circuits (4 nano mainframes) plus an IV emitter and IV sensor. The LuV Scanner (only for the research station) 4 ZPM circuits: not needed here.
- Structure (multis card, vanilla pattern with the pack’s block names): every slice is steel solid casing, one ULV Input Bus, laminated glass, an assembly line unit, a control casing and a grating; the last slice has the Output Bus instead of the bus; the energy hatch goes in the casing row at the bottom, input hatches in the steel casing at the corners. The pattern repeats 3 to 15 times, so a line can have 4 to 16 item buses; the minimum line (5 slices) holds only 4 buses. A motor has 6 ingredients, an emitter 8 (rhodium foil as two stacks), a robot arm 9, a field generator 8: build the line with at least 10 slices, the repeatable middle slices simply get longer.
- Assembly Line Unit (crafting, 2 per craft): 4 steel plates + 2 ruridit gears + 2 IV robot arms + 1 tungsten steel frame. Control casing: 4 EV circuits + 1 HPIC chip + 1 IV sensor + 1 IV emitter + 1 IV motor + 1 tungsten steel frame → 2. Grating: 6 iron bars + 1 steel rotor + 1 steel frame + 1 MV motor → 2. Controller: IV hull + 4 control casings + 2 IV robot arms + 2 IV circuits. A minimal line is 5 units, 5 control casings (3 crafts), 9 gratings, 10 laminated glass, 15 steel casings, 4 ULV buses; more slices cost 1 unit, 1 control casing, 1 grating, 2 glass and a bus each.
- Ordered inputs: orderedAssemblyLineItems is true, orderedAssemblyLineFluids is false (config/gtceu.yaml). Items must sit in the buses in the exact order of the recipe (look at the recipe in EMI; the first ingredient goes into the first bus, starting at the controller end). Fluids can go in any input hatch. A ULV bus holds one stack, so 64 fine palladium wire is one stack and the 96 rhodium foil of an emitter is TWO stacks (64 and 32) in two buses. A forming press with a rename tag separates identical-looking items (the quest tip).
- Data Access Hatch (EV version): EV item input bus + 4 data sticks + 4 EV circuits + 288 mB PTFE, assembler in the cleanroom, 200 ticks at 1920 EU/t (ComputerRecipes). It replaces a grating block in the back row of a repeatable slice. Unverified: whether the cheaper HV Basic Data Access Hatch (4 HV circuits, 288 mB polyethylene) is accepted by the line; the Java predicate is dataHatchPredicate, so a data bank link or an optical one also counts.
- Power: 7680 EU/t per recipe, so one IV Energy Hatch is enough (1 A, 8192 V); a second hatch only helps with overclocking. The line does not parallelise: a parallel hatch is not an option for the Assembly Line.
- Sub-steps people skip: (1) scan each IV part separately: one stick per product, label them; (2) the IV field generator is not a machine part you already have, craft one first (see the iv\_components tip); (3) a stick scanned at the EV scanner does NOT work for the emitter, sensor and field generator (their research has a higher EU/t); (4) the output bus is the last slice only, do not put an energy hatch there; (5) never mix two recipes in one line at once.
- **Unverified** whether the scanned IV part is consumed by the scanner (the extractor does not list research recipes), the best bus order direction (read the tooltip on the Assembly Line), and whether the data stick can sit in a Data Bank instead of a hatch (a data bank is an LuV-era multi; its link is an optical pipe).
- The Blank Data Stick recipe is described above (circuit assembler in the cleanroom); the ZPM data chain only reuses it.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:ev_scanner` | 1 |
| `gtceu:iv_scanner` | 1 |
| `gtceu:data_access_hatch` | 1 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `gtceu:ulv_input_bus` | 12 |
| `gtceu:ev_input_hatch` | 2 |
| `gtceu:ulv_output_bus` | 1 |
| `gtceu:data_stick` | 8 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Needs:** [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](../iv/iv_components.md)
- **Main source for:** `gtceu:assembly_line`, `gtceu:data_access_hatch`, `gtceu:data_stick`
