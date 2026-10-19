---
kind: chain
id: zpm_multis2
order: 1500
data:
  t: |-
    Era multiblocks 2: Runic Engraver (RCAS), Stargate Component Assembly, Dimensional Finder with coordinate crystals
  inf: true
  "n":
    - - g1
      - Lumium frame · 4 UV circuit · 2 ZPM field gen · 4 ZPM emitter · 8 quantum star · 48 blue alloy screw · 256 UHPIC chip · 5184 mB ITLC + naquadria + duranium
      - g
      - functionalstorage:oak_1
      - - [Lumium frame, "gtceu:lumium_frame"]
        - [ZPM emitter, "gtceu:zpm_emitter"]
        - [Quantum star, "gtceu:quantum_star"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
    - [a1, "Assembly Line · 5 min · ZPM power (scan: ZPM laser engraver, 16 CWU/t)", m, "gtceu:assembly_line"]
    - [o1, Runic Circuitry Assembling Station, o, "gtceu:runic_circuitry_assembling_station"]
    - - g2
      - Prismalium frame · 16 UV circuit · 12 ZPM field gen · 64 quantum star · 16 arm, motor, conveyor, piston · 256 UHPIC chip · 56 dragonsteel screw · 18 432 mB prismalium + 256 B PCB coolant + 3456 mB nether star concentrate
      - g
      - functionalstorage:oak_1
      - - [Prismalium frame, "gtceu:prismalium_frame"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [ZPM robot arm, "gtceu:zpm_robot_arm"]
        - [Dragonsteel screw, "gtceu:dragonsteel_screw"]
    - [a2, "Assembly Line · 5.3 min · ZPM power (scan: activated stargate rod, 24 CWU/t)", m, "gtceu:assembly_line"]
    - [o2, Stargate Component Assembly, o, "gtceu:stargate_component_assembly"]
    - - g3
      - ZPM scanner · 12 sensor, emitter, field gen, voltage coil · 128 fine trinaquadalloy wire · 8 UV circuit · 34 992 mB naquadria + 13 248 mB europium + 11 520 mB prismalium
      - g
      - functionalstorage:oak_1
      - - [ZPM scanner, "gtceu:zpm_scanner"]
        - [ZPM sensor, "gtceu:zpm_sensor"]
        - [ZPM voltage coil, "gtceu:zpm_voltage_coil"]
    - [a3, "Assembly Line · 3 min · ZPM power (scan: coordinate crystal, 24 CWU/t)", m, "gtceu:assembly_line"]
    - [o3, Dimensional Finder, o, "gtceu:dimensional_finder"]
    - - cc
      - |-
        Coordinate crystal: exquisite purified naquadah gem + nether star lens (laser engraver)
      - x
      - kubejs:coordinate_crystal
    - - df
      - Dimensional Finder run · 48 CWU/t · 230 400 CWU · 5 % · crystal + 64 sand + 16 ZPM sensor + 7200 mB naquadria
      - m
      - gtceu:dimensional_finder
    - [ac, Abydos Coordinate Crystal, o, "kubejs:abydos_coordinate_crystal"]
  e:
    - [g1, a1, "1"]
    - [a1, o1, "1 / 5 min"]
    - [g2, a2, "1"]
    - [a2, o2, "1 / 5.3 min"]
    - [g3, a3, "1"]
    - [a3, o3, "1 / 3 min"]
    - [cc, df, "1"]
    - [o3, df, controller]
    - [df, ac, "5 %"]
  tips:
    - |-
      Recipes (kjs systems/gate_based/misc.js, dimensional_pinging.js; all Assembly Line at VHA[ZPM] with STATION research). Runic Circuitry Assembling Station (‘runic engraver’): lumium frame + 4 UV circuits + double tantalum carbide plate + double titanium carbide plate + 2 ZPM field generators + 4 ZPM emitters + 48 blue alloy screws + 8 quantum stars + 4 stacks of UHPIC chips (256), 5184 mB each of ITLC soldering alloy, naquadria and duranium, 6000 ticks; research ZPM laser engraver at 16 CWU/t. Stargate Component Assembly: prismalium frame + 16 UV circuits + 12 ZPM field generators + 64 quantum stars + 16 ZPM robot arms, motors, conveyors and pistons each + 256 UHPIC chips + 56 dragonsteel screws + 32 prismalium single wire; 18 432 mB prismalium + 256 000 mB PCB coolant + 3456 mB nether star concentrate, 6400 ticks; research: the ACTIVATED stargate rod (zpm_rods) at 24 CWU/t. Dimensional Finder: ZPM scanner + 12 ZPM sensors + 12 emitters + 12 field generators + 12 voltage coils + 128 fine trinaquadalloy wire + 8 UV circuits, 34 992 mB naquadria + 13 248 mB europium + 11 520 mB prismalium, 3600 ticks; research: a coordinate crystal at 24 CWU/t.
    - |-
      Structures (multis card, counts only): the RCAS is 148 enriched naquadah machine casings + 187 lumium casings (hatch spots) + 80 trinaquadalloy frames + 72 fusion glass + 40 assembly line gratings + 28 advanced computer casings + 13 naquadah coil blocks + the pack’s laser casing (laser casing = 6 double prismalium plates + prismalium frame + a runic wave generator, 7200 ticks Assembly Line with 96 energy modules, 16 advanced reflector panels, 8 ZPM emitters, 16 ZPM voltage coils, 4 x 64 UHPIC wafers: Unverified source of the energy module and the exquisite runic laser source gem). The Stargate Component Assembly is 648 enderium casings + 540 prismalium casings + 450 atomic casings + 355 TRINIUM COIL BLOCKS + 275 dragonsteel casings + 96 machine casings + 78 fusion glass: 355 trinium coil blocks alone are 2840 trinium ingots. The Dimensional Finder is 97 pipe casings + 92 high temperature smelting casings + 84 sturdy casings + 48 trinaquadalloy frames + 26 superconducting coils + 16 fusion coils + 38 + 27 + 20 further pack casings.
    - |-
      Coordinate crystals (verified): a blank coordinate crystal = laser engraver (VHA[ZPM], 240 ticks) with 1 exquisite purified naquadah gem and a NON-consumed nether star lens. Abydos coordinate crystal (dimensional_finder recipe type, run in the OVERWORLD): crystal + 64 sand + 16 ZPM sensors + 7200 mB naquadria → 5 % chance (chancedOutput 500 of 10 000) of the Abydos crystal, 48 CWU/t, 230 400 total CWU, EUtVHA(UV). Duplicate: a scanner recipe, crystal + Abydos crystal → 2 Abydos crystals, 3000 ticks at VHA[ZPM] x 4^0, so the first lucky crystal becomes any number. A finder run lasts 4800 ticks (48 CWU/t x 4 min) and gives a crystal 5 % of the time: about 20 runs (80 min) on average, and 30 runs (2 h) is simply bad luck, so keep a copy as soon as one succeeds. Later crystals (verified): the Nether crystal takes 16 UV sensors + 50 000 mB lava (192 CWU/t, VHA[UEV], run inside Abydos); the End crystal takes 16 UHV sensors + 7200 mB echo fluid (384 CWU/t, VA[UIV] = 31 457 280 EU/t, run in the Nether); see the UEV page. Coordinates are read by right-clicking a crystal (quest: ‘absorb the crystal’s power’: make a copy first), and the gate takes them in the crystal interface.
    - |-
      Vacuum Chemical Reaction Chamber (era list, kjs vacuum_chemical_reactor.js), cheaper than the three above: 8 enriched naquadah frames + 1 extreme chemical reactor (ZPM) + 4 ZPM circuits + 4 ZPM pumps + 4 enriched naquadah quadruple fluid pipes + 4 polycarbonate huge pipes + 4 polycarbonate large pipes, 1152 mB polycarbonate + 2304 mB ITLC, 2000 ticks, EUtVHA(ZPM), research: ZPM gas collector at 24 CWU/t. Structure: 117 palladium substation casings (hatch spots), 76 polycarbonate casings, 28 tungsten carbide frames, 26 pallaridium firebox casings. It needs no UV circuit. The pack’s ZPM vacuum pump block (shaped): 2 + 2 double enriched naquadah plates around 2 dragonsteel rotors, 2 ZPM pumps and a ZPM rotor holder.
    - |-
      What 1 UV circuit + ZPM parts cost across this chain: the RCAS needs 4 UV circuits, the Component Assembly 16, the Finder 8. With the Component Part Assembly, Heat Chamber and Large Rotor Machine (zpm_multis, 4 each) that is 40 UV circuits before the gate itself. Plan the crystal line (zpm_crystal, zpm_crystal2, zpm_uv_circuit) as the main project of the second half of the era.
    - |-
      Sub-steps people skip: (1) every multi has a different research item (laser engraver, activated rod, coordinate crystal): do the three station researches in a row; (2) coolant: 256 B of PCB coolant for the Component Assembly is a whole PCB coolant plant (pcb_coolant chain), not a drum; (3) the Dimensional Finder runs on CWU like the station: it needs a second computation hatch/HPCA slice; (4) naquadria per recipe is 5184 to 34 992 mB: the 9000 K furnace (zpm_naq_products) must be running.
    - |-
      Unverified: the CWU duration of the research steps, the blue alloy screw and advanced power thruster sources, the laser casing chain and where the HPCA connects to the Dimensional Finder (compIn hatch).
  b:
    - ["gtceu:runic_circuitry_assembling_station", 1]
    - ["gtceu:stargate_component_assembly", 1]
    - ["gtceu:dimensional_finder", 1]
    - ["gtceu:assembly_line", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 2]
    - ["functionalstorage:oak_1", 30]
    - ["modularrouters:modular_router", 16]
    - ["gtceu:lv_robot_arm", 16]
    - ["gtceu:item_filter", 16]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uhpic_chip", "gtceu:quantum_star", "gtceu:zpm_field_generator"]
      t: |-
        Drawers first, one per input: UHPIC chips (Keep Exact 64), quantum stars (Keep Exact 64), ZPM parts (field generators, emitters, sensors, voltage coils, arms, motors, conveyors, pistons), UV circuits, frames, screws, plates. Drums: ITLC soldering alloy, naquadria, duranium, prismalium, PCB coolant, europium, nether star concentrate. Each Assembly Line input bus has its own router and Item Filter; each product its own line.
    - i: ["gtceu:research_station", "gtceu:zpm_laser_engraver", "gtceu:data_orb"]
      t: |-
        Research first (zpm_data): a ZPM laser engraver (16 CWU/t), an activated stargate rod (24 CWU/t) and a coordinate crystal (24 CWU/t), each on its own data orb. The orbs go into the Assembly Lines’ Data Access Hatches.
    - i: ["gtceu:assembly_line", "gtceu:runic_circuitry_assembling_station"]
      t: |-
        RCAS (the rune maker): buses in recipe order, fluids 5184 mB ITLC, 5184 mB naquadria, 5184 mB duranium; 5 min. Then 148 + 187 + 80 + ... casings and the laser casing from the multis card.
    - i: ["gtceu:assembly_line", "gtceu:stargate_component_assembly"]
      t: |-
        Stargate Component Assembly: prismalium frame, 16 UV circuits, 12 field generators, 64 quantum stars, 16 each of arm, motor, conveyor, piston, 256 UHPIC chips; fluids 18 432 mB prismalium + 256 000 mB PCB coolant + 3456 mB nether star concentrate. 5.3 min. The structure needs 355 trinium coil blocks: start collecting trinium for it now.
    - i: ["gtceu:assembly_line", "gtceu:dimensional_finder", "gtceu:zpm_scanner"]
      t: |-
        Dimensional Finder: ZPM scanner + 12 sensors, emitters, field generators, voltage coils + 128 fine trinaquadalloy wire + 8 UV circuits; naquadria 34 992 + europium 13 248 + prismalium 11 520 mB. 3 min.
    - i: ["gtceu:dimensional_finder", "kubejs:coordinate_crystal", "kubejs:abydos_coordinate_crystal"]
      t: |-
        First crystal: blank crystal (exquisite purified naquadah gem + nether star lens in a laser engraver), then the Finder in the Overworld with 64 sand + 16 ZPM sensors + 7200 mB naquadria; 5 % chance. Keep the crystal and duplicate it in a scanner (crystal + the new one → 2).
    - i: ["functionalstorage:oak_1", "gtceu:zpm_sensor"]
      t: |-
        Easy to miss: each Finder run takes 16 ZPM sensors (24 trinium ingots each) as plain item inputs and has a 5 % chance, so on average 320 sensors per crystal unless the pack’s sensors are returned (Unverified: check the first run); duplication in a scanner means you only need ONE success. Do one run first and see what comes back.
---
# Era multiblocks 2: Runic Engraver (RCAS), Stargate Component Assembly, Dimensional Finder with coordinate crystals

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_multis2` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Era multiblocks and the Classic Stargate](../../plan/p13.md#zpmmultis)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 5 min · ZPM power (scan: ZPM laser engraver, 16 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Lumium frame · 4 UV circuit · 2 ZPM field gen · 4 ZPM emitter · 8 quantum star · 48 blue alloy screw · 256 UHPIC chip · 5184 mB ITLC + naquadria + duranium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Lumium frame · 4 UV circuit · 2 ZPM field gen · 4 ZPM emitter · 8 quantum star · 48 blue alloy screw · 256 UHPIC chip · 5184 mB ITLC + naquadria + duranium</span><span class="gt-sub"><span>Lumium frame</span><span>ZPM emitter</span><span>Quantum star</span><span>UHPIC chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Runic Circuitry Assembling Station (gtceu:runic_circuitry_assembling_station) - 1 / 5 min"><img class="gt-ico" src="../../assets/icons/gtceu__runic_circuitry_assembling_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Circuitry Assembling Station</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 5.3 min · ZPM power (scan: activated stargate rod, 24 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Prismalium frame · 16 UV circuit · 12 ZPM field gen · 64 quantum star · 16 arm, motor, conveyor, piston · 256 UHPIC chip · 56 dragonsteel screw · 18 432 mB prismalium + 256 B PCB coolant + 3456 mB nether star concentrate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Prismalium frame · 16 UV circuit · 12 ZPM field gen · 64 quantum star · 16 arm, motor, conveyor, piston · 256 UHPIC chip · 56 dragonsteel screw · 18 432 mB prismalium + 256 B PCB coolant + 3456 mB nether star concentrate</span><span class="gt-sub"><span>Prismalium frame</span><span>ZPM field generator</span><span>ZPM robot arm</span><span>Dragonsteel screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5.3 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Stargate Component Assembly (gtceu:stargate_component_assembly) - 1 / 5.3 min"><img class="gt-ico" src="../../assets/icons/gtceu__stargate_component_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stargate Component Assembly</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 3 min · ZPM power (scan: coordinate crystal, 24 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM scanner · 12 sensor, emitter, field gen, voltage coil · 128 fine trinaquadalloy wire · 8 UV circuit · 34 992 mB naquadria + 13 248 mB europium + 11 520 mB prismalium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM scanner · 12 sensor, emitter, field gen, voltage coil · 128 fine trinaquadalloy wire · 8 UV circuit · 34 992 mB naquadria + 13 248 mB europium + 11 520 mB prismalium</span><span class="gt-sub"><span>ZPM scanner</span><span>ZPM sensor</span><span>ZPM voltage coil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">3 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Dimensional Finder (gtceu:dimensional_finder) - 1 / 3 min"><img class="gt-ico" src="../../assets/icons/gtceu__dimensional_finder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dimensional Finder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-mod" id="m-df">
<div class="gt-head"><span class="gt-mname">Dimensional Finder run · 48 CWU/t · 230 400 CWU · 5 % · crystal + 64 sand + 16 ZPM sensor + 7200 mB naquadria</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Coordinate crystal: exquisite purified naquadah gem + nether star lens (laser engraver) (kubejs:coordinate_crystal) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__coordinate_crystal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Coordinate Crystal</span><span class="gt-note">Coordinate crystal: exquisite purified naquadah gem + nether star lens (laser engraver)</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Dimensional Finder (gtceu:dimensional_finder) - controller"><img class="gt-ico" src="../../assets/icons/gtceu__dimensional_finder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dimensional Finder</span><b class="gt-q">controller</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__dimensional_finder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Abydos Coordinate Crystal (kubejs:abydos_coordinate_crystal) - 5 %"><img class="gt-ico" src="../../assets/icons/kubejs__abydos_coordinate_crystal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Abydos Coordinate Crystal</span><b class="gt-q">5 %</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:dimensional_finder</code></div>
</div>
</div>

## Flow

- [Assembly Line · 5 min · ZPM power (scan: ZPM laser engraver, 16 CWU/t)](#m-a1)
- [Assembly Line · 5.3 min · ZPM power (scan: activated stargate rod, 24 CWU/t)](#m-a2)
- [Assembly Line · 3 min · ZPM power (scan: coordinate crystal, 24 CWU/t)](#m-a3) → [Dimensional Finder run · 48 CWU/t · 230 400 CWU · 5 % · crystal + 64 sand + 16 ZPM sensor + 7200 mB naquadria](#m-df)

## How to build

1. Drawers first, one per input: UHPIC chips (Keep Exact 64), quantum stars (Keep Exact 64), ZPM parts (field generators, emitters, sensors, voltage coils, arms, motors, conveyors, pistons), UV circuits, frames, screws, plates. Drums: ITLC soldering alloy, naquadria, duranium, prismalium, PCB coolant, europium, nether star concentrate. Each Assembly Line input bus has its own router and Item Filter; each product its own line. — `functionalstorage:oak_1`, `gtceu:uhpic_chip`, `gtceu:quantum_star`, `gtceu:zpm_field_generator`
2. Research first (zpm\_data): a ZPM laser engraver (16 CWU/t), an activated stargate rod (24 CWU/t) and a coordinate crystal (24 CWU/t), each on its own data orb. The orbs go into the Assembly Lines’ Data Access Hatches. — `gtceu:research_station`, `gtceu:zpm_laser_engraver`, `gtceu:data_orb`
3. RCAS (the rune maker): buses in recipe order, fluids 5184 mB ITLC, 5184 mB naquadria, 5184 mB duranium; 5 min. Then 148 + 187 + 80 + ... casings and the laser casing from the multis card. — `gtceu:assembly_line`, `gtceu:runic_circuitry_assembling_station`
4. Stargate Component Assembly: prismalium frame, 16 UV circuits, 12 field generators, 64 quantum stars, 16 each of arm, motor, conveyor, piston, 256 UHPIC chips; fluids 18 432 mB prismalium + 256 000 mB PCB coolant + 3456 mB nether star concentrate. 5.3 min. The structure needs 355 trinium coil blocks: start collecting trinium for it now. — `gtceu:assembly_line`, `gtceu:stargate_component_assembly`
5. Dimensional Finder: ZPM scanner + 12 sensors, emitters, field generators, voltage coils + 128 fine trinaquadalloy wire + 8 UV circuits; naquadria 34 992 + europium 13 248 + prismalium 11 520 mB. 3 min. — `gtceu:assembly_line`, `gtceu:dimensional_finder`, `gtceu:zpm_scanner`
6. First crystal: blank crystal (exquisite purified naquadah gem + nether star lens in a laser engraver), then the Finder in the Overworld with 64 sand + 16 ZPM sensors + 7200 mB naquadria; 5 % chance. Keep the crystal and duplicate it in a scanner (crystal + the new one → 2). — `gtceu:dimensional_finder`, `kubejs:coordinate_crystal`, `kubejs:abydos_coordinate_crystal`
7. Easy to miss: each Finder run takes 16 ZPM sensors (24 trinium ingots each) as plain item inputs and has a 5 % chance, so on average 320 sensors per crystal unless the pack’s sensors are returned (Unverified: check the first run); duplication in a scanner means you only need ONE success. Do one run first and see what comes back. — `functionalstorage:oak_1`, `gtceu:zpm_sensor`

## Tips

- Recipes (kjs systems/gate\_based/misc.js, dimensional\_pinging.js; all Assembly Line at VHA\[ZPM\] with STATION research). Runic Circuitry Assembling Station (‘runic engraver’): lumium frame + 4 UV circuits + double tantalum carbide plate + double titanium carbide plate + 2 ZPM field generators + 4 ZPM emitters + 48 blue alloy screws + 8 quantum stars + 4 stacks of UHPIC chips (256), 5184 mB each of ITLC soldering alloy, naquadria and duranium, 6000 ticks; research ZPM laser engraver at 16 CWU/t. Stargate Component Assembly: prismalium frame + 16 UV circuits + 12 ZPM field generators + 64 quantum stars + 16 ZPM robot arms, motors, conveyors and pistons each + 256 UHPIC chips + 56 dragonsteel screws + 32 prismalium single wire; 18 432 mB prismalium + 256 000 mB PCB coolant + 3456 mB nether star concentrate, 6400 ticks; research: the ACTIVATED stargate rod (zpm\_rods) at 24 CWU/t. Dimensional Finder: ZPM scanner + 12 ZPM sensors + 12 emitters + 12 field generators + 12 voltage coils + 128 fine trinaquadalloy wire + 8 UV circuits, 34 992 mB naquadria + 13 248 mB europium + 11 520 mB prismalium, 3600 ticks; research: a coordinate crystal at 24 CWU/t.
- Structures (multis card, counts only): the RCAS is 148 enriched naquadah machine casings + 187 lumium casings (hatch spots) + 80 trinaquadalloy frames + 72 fusion glass + 40 assembly line gratings + 28 advanced computer casings + 13 naquadah coil blocks + the pack’s laser casing (laser casing = 6 double prismalium plates + prismalium frame + a runic wave generator, 7200 ticks Assembly Line with 96 energy modules, 16 advanced reflector panels, 8 ZPM emitters, 16 ZPM voltage coils, 4 x 64 UHPIC wafers: Unverified source of the energy module and the exquisite runic laser source gem). The Stargate Component Assembly is 648 enderium casings + 540 prismalium casings + 450 atomic casings + 355 TRINIUM COIL BLOCKS + 275 dragonsteel casings + 96 machine casings + 78 fusion glass: 355 trinium coil blocks alone are 2840 trinium ingots. The Dimensional Finder is 97 pipe casings + 92 high temperature smelting casings + 84 sturdy casings + 48 trinaquadalloy frames + 26 superconducting coils + 16 fusion coils + 38 + 27 + 20 further pack casings.
- Coordinate crystals (verified): a blank coordinate crystal = laser engraver (VHA\[ZPM\], 240 ticks) with 1 exquisite purified naquadah gem and a NON-consumed nether star lens. Abydos coordinate crystal (dimensional\_finder recipe type, run in the OVERWORLD): crystal + 64 sand + 16 ZPM sensors + 7200 mB naquadria → 5 % chance (chancedOutput 500 of 10 000) of the Abydos crystal, 48 CWU/t, 230 400 total CWU, EUtVHA(UV). Duplicate: a scanner recipe, crystal + Abydos crystal → 2 Abydos crystals, 3000 ticks at VHA\[ZPM\] x 4^0, so the first lucky crystal becomes any number. A finder run lasts 4800 ticks (48 CWU/t x 4 min) and gives a crystal 5 % of the time: about 20 runs (80 min) on average, and 30 runs (2 h) is simply bad luck, so keep a copy as soon as one succeeds. Later crystals (verified): the Nether crystal takes 16 UV sensors + 50 000 mB lava (192 CWU/t, VHA\[UEV\], run inside Abydos); the End crystal takes 16 UHV sensors + 7200 mB echo fluid (384 CWU/t, VA\[UIV\] = 31 457 280 EU/t, run in the Nether); see the UEV page. Coordinates are read by right-clicking a crystal (quest: ‘absorb the crystal’s power’: make a copy first), and the gate takes them in the crystal interface.
- Vacuum Chemical Reaction Chamber (era list, kjs vacuum\_chemical\_reactor.js), cheaper than the three above: 8 enriched naquadah frames + 1 extreme chemical reactor (ZPM) + 4 ZPM circuits + 4 ZPM pumps + 4 enriched naquadah quadruple fluid pipes + 4 polycarbonate huge pipes + 4 polycarbonate large pipes, 1152 mB polycarbonate + 2304 mB ITLC, 2000 ticks, EUtVHA(ZPM), research: ZPM gas collector at 24 CWU/t. Structure: 117 palladium substation casings (hatch spots), 76 polycarbonate casings, 28 tungsten carbide frames, 26 pallaridium firebox casings. It needs no UV circuit. The pack’s ZPM vacuum pump block (shaped): 2 + 2 double enriched naquadah plates around 2 dragonsteel rotors, 2 ZPM pumps and a ZPM rotor holder.
- What 1 UV circuit + ZPM parts cost across this chain: the RCAS needs 4 UV circuits, the Component Assembly 16, the Finder 8. With the Component Part Assembly, Heat Chamber and Large Rotor Machine (zpm\_multis, 4 each) that is 40 UV circuits before the gate itself. Plan the crystal line (zpm\_crystal, zpm\_crystal2, zpm\_uv\_circuit) as the main project of the second half of the era.
- Sub-steps people skip: (1) every multi has a different research item (laser engraver, activated rod, coordinate crystal): do the three station researches in a row; (2) coolant: 256 B of PCB coolant for the Component Assembly is a whole PCB coolant plant (pcb\_coolant chain), not a drum; (3) the Dimensional Finder runs on CWU like the station: it needs a second computation hatch/HPCA slice; (4) naquadria per recipe is 5184 to 34 992 mB: the 9000 K furnace (zpm\_naq\_products) must be running.
- **Unverified** the CWU duration of the research steps, the blue alloy screw and advanced power thruster sources, the laser casing chain and where the HPCA connects to the Dimensional Finder (compIn hatch).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:runic_circuitry_assembling_station` | 1 |
| `gtceu:stargate_component_assembly` | 1 |
| `gtceu:dimensional_finder` | 1 |
| `gtceu:assembly_line` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 2 |
| `functionalstorage:oak_1` | 30 |
| `modularrouters:modular_router` | 16 |
| `gtceu:lv_robot_arm` | 16 |
| `gtceu:item_filter` | 16 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:runic_circuitry_assembling_station`, `gtceu:stargate_component_assembly`, `gtceu:dimensional_finder`, `kubejs:abydos_coordinate_crystal`, `kubejs:coordinate_crystal`, `gtceu:vacuum_chemical_reaction_chamber`
