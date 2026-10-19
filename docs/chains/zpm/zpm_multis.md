---
kind: chain
id: zpm_multis
order: 1490
data:
  t: |-
    Era multiblocks 1: Component Part Assembly, Heat Chamber, Large Rotor Machine (Assembly Line, ZPM power, 4 UV circuits each, station research 16 CWU/t)
  inf: true
  "n":
    - - g1
      - ZPM assembler · 8 ZPM robot arm · 8 conveyor · 8 pump · 4 UV + 6 ZPM + 8 LuV circuit · 12 528 mB ITLC solder + 2500 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [ZPM Assembler, "gtceu:zpm_assembler"]
        - [ZPM robot arm, "gtceu:zpm_robot_arm"]
        - [ZPM conveyor, "gtceu:zpm_conveyor_module"]
        - [ZPM pump, "gtceu:zpm_electric_pump"]
        - ["Crystal mainframe (UV)", "gtceu:crystal_processor_mainframe"]
    - [a1, "Assembly Line · 90 s · ZPM power (scan: ZPM assembler, 16 CWU/t)", m, "gtceu:assembly_line"]
    - [o1, Component Part Assembly, o, "gtceu:component_part_assembly"]
    - - g2
      - Europium frame · 4 UV circuit · double trinaquadalloy plate · double duranium plate · ZPM field generator · 96 UHPIC chip · 48 dragonsteel single wire · 6912 mB HSS-S + 1728 mB NbN
      - g
      - functionalstorage:oak_1
      - - [Europium frame, "gtceu:europium_frame"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [Dragonsteel single wire, "gtceu:dragonsteel_single_wire"]
    - [a2, "Assembly Line · 120 s · ZPM power (scan: ZPM electric furnace)", m, "gtceu:assembly_line"]
    - [o2, Heat Chamber, o, "gtceu:heat_chamber"]
    - - g3
      - Shellite frame · 4 UV circuit · 12 ZPM field generator · 8 ZPM motor · 32 advanced power thruster · 4 HSS-G spring · 96 UHPIC chip · 3456 mB ITLC + 5184 mB YBCO
      - g
      - functionalstorage:oak_1
      - - [Shellite frame, "gtceu:shellite_frame"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [ZPM motor, "gtceu:zpm_electric_motor"]
        - [Advanced power thruster, "gtceu:advanced_power_thruster"]
    - [a3, "Assembly Line · 180 s · ZPM power (scan: ZPM lathe)", m, "gtceu:assembly_line"]
    - [o3, Large Rotor Machine, o, "gtceu:large_rotor_machine"]
  e:
    - [g1, a1, "1"]
    - [a1, o1, "1 / 90 s"]
    - [g2, a2, "1"]
    - [a2, o2, "1 / 120 s"]
    - [g3, a3, "1"]
    - [a3, o3, "1 / 180 s"]
  tips:
    - |-
      Recipes (kjs additions/multiblock_recipes/pre_gate_multis.js and systems/gate_based/misc.js). Component Part Assembly: 1 ZPM assembler + 8 ZPM robot arms + 8 ZPM conveyors + 8 ZPM pumps + 4 UV circuits + 6 ZPM circuits + 8 LuV circuits + 12 528 mB indium tin lead cadmium (ITLC) soldering alloy + 2500 mB lubricant, 1800 ticks, VHA[ZPM]; station research of the ZPM assembler at 16 CWU/t. Heat Chamber: 1 europium frame + 4 UV circuits + 1 double trinaquadalloy plate + 1 double duranium plate + 1 ZPM field generator + 96 UHPIC chips + 48 dragonsteel single wire, 6912 mB molten HSS-S + 1728 mB molten niobium nitride, 2400 ticks; research ZPM electric furnace, 16 CWU/t. Large Rotor Machine: 1 shellite frame + 4 UV circuits + 1 double vanadium gallium plate + 1 double red steel plate + 12 ZPM field generators + 8 ZPM motors + 32 advanced power thrusters + 4 HSS-G springs + 96 UHPIC chips, 3456 mB ITLC + 5184 mB molten YBCO, 3600 ticks; research ZPM lathe, 16 CWU/t.
    - |-
      The research items are ordinary ZPM single machines: ZPM Assembler = 2 ZPM robot arms + 2 ZPM circuits + 2 ZPM conveyors + ZPM hull + 2 cables (MetaTileEntityLoader pattern ACA/VMV/WCW, same loop as the IV one: 6 + 4 motors, i.e. 10 ZPM motors = 80 europium ingots); ZPM Lathe = hull + 2 circuits + motor + piston + grinding component + 3 cables; ZPM Electric Furnace = hull + 2 circuits + 4 coil-material double wire + 2 cables; the laser engraver and others follow the same loop (Unverified: the ZPM materials of the coil wire and grinder, check EMI). Each scan needs one of these machines in the Object Holder: build them as normal machines first.
    - |-
      Structures (multis card): Component Part Assembly 36 enriched naquadah machine casings (hatch spots: 1 energy hatch, fluid input, maintenance, optical hatch) + 6 ULV input buses + 8 sturdy casings + 8 assembly line gratings + 16 fusion glass + 5 assembly line units + 10 FUSION COILS + 1 output bus. Heat Chamber 328 enderium casings + 95 high temperature smelting casings (parallel hatch, maintenance) + 77 enriched naquadah pipe casings + 48 RPP frames + 40 heat vents + 36 NAQUADAH COIL BLOCKS + 32 firebox + 24 intake + 16 machine casings. Large Rotor Machine 116 enriched naquadah machine casings (hatches, parallel hatch) + 14 gearboxes + 12 pipe casings + 10 + 10 intake and heat-escape casings + 8 trinaquadalloy frames + assembly line parts + lumium/twinite/shellite casings. Those pack casings are crafted in the casings.js and startup scripts: Unverified recipes.
    - |-
      The ZPM-power Assembly Line: all three recipes run at VHA[ZPM] = 61 440 EU/t (VHA is half of VA; VA[ZPM] = 122 880): the LuV 4A hatch (131 072 EU/t) is more than enough, the quest says it ‘gives ZPM recipe speeds’. ITLC soldering alloy (14 indium + 3 tin + 2 lead + 1 cadmium as dust, startup solders.js) is the new fluid: 12 528 mB is 87 ingots of 144 mB. Unverified: the dust mixer recipe and the indium and cadmium sources.
    - |-
      Mega Vacuum Freezer (era list; kjs additions/machines_and_parts/large_multis.js): aluminium frame + 2 UV circuits + 4 dense rhodium plated palladium plates + 2 LuV field generators + 4 NbTi normal fluid pipes + 32 fine ITBTC wire + 6 HSS-E screws, 1152 mB soldering alloy, 400 ticks, but EUtVHA(UV): a UV-power Assembly Line recipe, so it is NOT a ZPM-era build (needs a LuV 16A or a UV hatch). Its research item is the super vacuum freezer (the Arctic Chilling Unit, itself an IV recipe) at 24 CWU/t. The Bulk Blast Chiller [BBC] is a GCYM multi (parallel hatch, batch mode) and, verified, a UV build: 2 UV circuits and VHA[UV] = 245 760 EU/t, so make it at the END of this era, after your first UV hatch and UV circuits, not in the middle. The structure is 161 frostproof casings, 74 tungsten steel pipe casings, 36 clean casings, 26 heat vents.
    - |-
      Chambered Alloy Transmuter [CAT] (gtceu:super_abs, the Boosted Alloy Blast Smelter; verified, intermediate_multis.js and super_abs.js): Assembly Line with a ZPM alloy smelter + 2 ZPM circuits + 2 double naquadah plates + 2 ZPM emitters + 4 europium springs + 8 vanadium gallium cables + 4 naquadria screws, 1008 mB soldering alloy + 432 mB PBI, 400 ticks, VHA[ZPM] = 61 440 EU/t, research alloy blast smelter 12 CWU/t. It runs the same alloy_blast_smelter recipes as the ABS with throughput boosting and batch mode, takes ONE energy hatch and heating coils, and has no special coolant slot: it replaces the ABS for bulk alloys but needs no better cooling. The Stargate Component Assembly, Runic Circuitry Assembly Station and Component Part Assembly are also built at VHA[ZPM] but ask for 16 / 4 / 4 UV circuits, which is why they close the era.
    - |-
      Order of priority for the era: Component Part Assembly (every later component is a CPA recipe: it assembles parts like the living SMDs, quest ‘components are getting complex’), then the Large Rotor Machine (the stargate rod line), then the Heat Chamber (nether star concentrate, the activated rods). Each needs 4 UV circuits = 4 crystal mainframes (zpm_uv_circuit) and 96 UHPIC chips (48 UHPIC wafers) for two of them.
    - |-
      Sub-steps people skip: (1) three different research machines to build and scan (ZPM assembler, lathe, electric furnace); (2) ZPM field generators 1, 12 and 1 respectively (Large Rotor Machine: 12 field generators = 72 stars + 72 ZPM circuits via emitters); (3) advanced power thrusters: an item of the pack (32 per rotor machine), Unverified recipe; (4) 96 UHPIC chips = the UHPIC wafer line (luv_fusion): start it before anything else; (5) the Large Rotor Machine needs 116 casings plus gearboxes: crafted in advance.
    - |-
      Unverified: the recipes of the pack casings (enriched naquadah machine casing etc.), advanced power thrusters and the fusion-coil-heavy structure of the Component Part Assembly.
  b:
    - ["gtceu:component_part_assembly", 1]
    - ["gtceu:heat_chamber", 1]
    - ["gtceu:large_rotor_machine", 1]
    - ["gtceu:assembly_line", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 2]
    - ["functionalstorage:oak_1", 28]
    - ["modularrouters:modular_router", 16]
    - ["gtceu:lv_robot_arm", 16]
    - ["gtceu:item_filter", 16]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 6]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:uhpic_chip
        - gtceu:zpm_field_generator
        - gtceu:crystal_processor_mainframe
      t: |-
        Drawers first, one per input: ZPM field generators, motors, arms, conveyors, pumps, UV circuits (Keep Exact 4), ZPM and LuV circuits, UHPIC chips (Keep Exact 64), frames, plates, dragonsteel wire. Drums: ITLC soldering alloy, YBCO, HSS-S, niobium nitride, lubricant. One Assembly Line per multi, each input bus behind its own router with an Item Filter.
    - i: ["gtceu:zpm_assembler", "gtceu:zpm_lathe", "gtceu:zpm_electric_furnace"]
      t: |-
        Build the research machines first: a ZPM Assembler (2 arms + 2 conveyors + 2 circuits + hull + 2 cables), a ZPM Lathe and a ZPM Electric Furnace by their crafting-table patterns, one each, then station research on each (16 CWU/t each) onto three data orbs (zpm_data).
    - i: ["gtceu:assembly_line", "gtceu:component_part_assembly"]
      t: |-
        Component Part Assembly: Assembly Line buses in recipe order (assembler, 8 arms, 8 conveyors, 8 pumps, 4 UV, 6 ZPM, 8 LuV circuits); hatches 12 528 mB ITLC solder + 2500 mB lubricant. 90 s. Then the structure from the multis card: 36 + 6 + 8 + 8 + 16 + 5 + 10 blocks.
    - i: ["gtceu:assembly_line", "gtceu:heat_chamber", "gtceu:europium_frame"]
      t: |-
        Heat Chamber: europium frame, 4 UV circuits, double trinaquadalloy and duranium plates, ZPM field generator, 96 UHPIC chips, 48 dragonsteel single wire; fluids 6912 mB HSS-S and 1728 mB niobium nitride. 120 s. The structure is huge (328 enderium casings, 36 naquadah coils).
    - i: ["gtceu:assembly_line", "gtceu:large_rotor_machine", "gtceu:advanced_power_thruster"]
      t: |-
        Large Rotor Machine: shellite frame, 4 UV circuits, double VG and red steel plates, 12 field generators, 8 motors, 32 advanced power thrusters, 4 HSS-G springs, 96 UHPIC chips; 3456 mB ITLC + 5184 mB YBCO. 180 s.
    - i: ["functionalstorage:oak_1", "gtceu:uhpic_chip"]
      t: |-
        Easy to miss: UHPIC chips are 96 per multi for two of them: 96 chips = 48 wafers; you want a dedicated HPIC → UHPIC wafer line and Keep Exact 64 on the chip drawer.
---
# Era multiblocks 1: Component Part Assembly, Heat Chamber, Large Rotor Machine (Assembly Line, ZPM power, 4 UV circuits each, station research 16 CWU/t)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_multis` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Era multiblocks and the Classic Stargate](../../plan/p13.md#zpmmultis)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 90 s · ZPM power (scan: ZPM assembler, 16 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM assembler · 8 ZPM robot arm · 8 conveyor · 8 pump · 4 UV + 6 ZPM + 8 LuV circuit · 12 528 mB ITLC solder + 2500 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM assembler · 8 ZPM robot arm · 8 conveyor · 8 pump · 4 UV + 6 ZPM + 8 LuV circuit · 12 528 mB ITLC solder + 2500 mB lubricant</span><span class="gt-sub"><span>ZPM Assembler</span><span>ZPM robot arm</span><span>ZPM conveyor</span><span>ZPM pump</span><span>Crystal mainframe (UV)</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Component Part Assembly (gtceu:component_part_assembly) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Component Part Assembly</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 120 s · ZPM power (scan: ZPM electric furnace)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Europium frame · 4 UV circuit · double trinaquadalloy plate · double duranium plate · ZPM field generator · 96 UHPIC chip · 48 dragonsteel single wire · 6912 mB HSS-S + 1728 mB NbN (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Europium frame · 4 UV circuit · double trinaquadalloy plate · double duranium plate · ZPM field generator · 96 UHPIC chip · 48 dragonsteel single wire · 6912 mB HSS-S + 1728 mB NbN</span><span class="gt-sub"><span>Europium frame</span><span>ZPM field generator</span><span>UHPIC chip</span><span>Dragonsteel single wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">120 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Heat Chamber (gtceu:heat_chamber) - 1 / 120 s"><img class="gt-ico" src="../../assets/icons/gtceu__heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Heat Chamber</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 180 s · ZPM power (scan: ZPM lathe)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Shellite frame · 4 UV circuit · 12 ZPM field generator · 8 ZPM motor · 32 advanced power thruster · 4 HSS-G spring · 96 UHPIC chip · 3456 mB ITLC + 5184 mB YBCO (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Shellite frame · 4 UV circuit · 12 ZPM field generator · 8 ZPM motor · 32 advanced power thruster · 4 HSS-G spring · 96 UHPIC chip · 3456 mB ITLC + 5184 mB YBCO</span><span class="gt-sub"><span>Shellite frame</span><span>ZPM field generator</span><span>ZPM motor</span><span>Advanced power thruster</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">180 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Large Rotor Machine (gtceu:large_rotor_machine) - 1 / 180 s"><img class="gt-ico" src="../../assets/icons/gtceu__large_rotor_machine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Rotor Machine</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 90 s · ZPM power (scan: ZPM assembler, 16 CWU/t)](#m-a1)
- [Assembly Line · 120 s · ZPM power (scan: ZPM electric furnace)](#m-a2)
- [Assembly Line · 180 s · ZPM power (scan: ZPM lathe)](#m-a3)

## How to build

1. Drawers first, one per input: ZPM field generators, motors, arms, conveyors, pumps, UV circuits (Keep Exact 4), ZPM and LuV circuits, UHPIC chips (Keep Exact 64), frames, plates, dragonsteel wire. Drums: ITLC soldering alloy, YBCO, HSS-S, niobium nitride, lubricant. One Assembly Line per multi, each input bus behind its own router with an Item Filter. — `functionalstorage:oak_1`, `gtceu:uhpic_chip`, `gtceu:zpm_field_generator`, `gtceu:crystal_processor_mainframe`
2. Build the research machines first: a ZPM Assembler (2 arms + 2 conveyors + 2 circuits + hull + 2 cables), a ZPM Lathe and a ZPM Electric Furnace by their crafting-table patterns, one each, then station research on each (16 CWU/t each) onto three data orbs (zpm\_data). — `gtceu:zpm_assembler`, `gtceu:zpm_lathe`, `gtceu:zpm_electric_furnace`
3. Component Part Assembly: Assembly Line buses in recipe order (assembler, 8 arms, 8 conveyors, 8 pumps, 4 UV, 6 ZPM, 8 LuV circuits); hatches 12 528 mB ITLC solder + 2500 mB lubricant. 90 s. Then the structure from the multis card: 36 + 6 + 8 + 8 + 16 + 5 + 10 blocks. — `gtceu:assembly_line`, `gtceu:component_part_assembly`
4. Heat Chamber: europium frame, 4 UV circuits, double trinaquadalloy and duranium plates, ZPM field generator, 96 UHPIC chips, 48 dragonsteel single wire; fluids 6912 mB HSS-S and 1728 mB niobium nitride. 120 s. The structure is huge (328 enderium casings, 36 naquadah coils). — `gtceu:assembly_line`, `gtceu:heat_chamber`, `gtceu:europium_frame`
5. Large Rotor Machine: shellite frame, 4 UV circuits, double VG and red steel plates, 12 field generators, 8 motors, 32 advanced power thrusters, 4 HSS-G springs, 96 UHPIC chips; 3456 mB ITLC + 5184 mB YBCO. 180 s. — `gtceu:assembly_line`, `gtceu:large_rotor_machine`, `gtceu:advanced_power_thruster`
6. Easy to miss: UHPIC chips are 96 per multi for two of them: 96 chips = 48 wafers; you want a dedicated HPIC → UHPIC wafer line and Keep Exact 64 on the chip drawer. — `functionalstorage:oak_1`, `gtceu:uhpic_chip`

## Tips

- Recipes (kjs additions/multiblock\_recipes/pre\_gate\_multis.js and systems/gate\_based/misc.js). Component Part Assembly: 1 ZPM assembler + 8 ZPM robot arms + 8 ZPM conveyors + 8 ZPM pumps + 4 UV circuits + 6 ZPM circuits + 8 LuV circuits + 12 528 mB indium tin lead cadmium (ITLC) soldering alloy + 2500 mB lubricant, 1800 ticks, VHA\[ZPM\]; station research of the ZPM assembler at 16 CWU/t. Heat Chamber: 1 europium frame + 4 UV circuits + 1 double trinaquadalloy plate + 1 double duranium plate + 1 ZPM field generator + 96 UHPIC chips + 48 dragonsteel single wire, 6912 mB molten HSS-S + 1728 mB molten niobium nitride, 2400 ticks; research ZPM electric furnace, 16 CWU/t. Large Rotor Machine: 1 shellite frame + 4 UV circuits + 1 double vanadium gallium plate + 1 double red steel plate + 12 ZPM field generators + 8 ZPM motors + 32 advanced power thrusters + 4 HSS-G springs + 96 UHPIC chips, 3456 mB ITLC + 5184 mB molten YBCO, 3600 ticks; research ZPM lathe, 16 CWU/t.
- The research items are ordinary ZPM single machines: ZPM Assembler = 2 ZPM robot arms + 2 ZPM circuits + 2 ZPM conveyors + ZPM hull + 2 cables (MetaTileEntityLoader pattern ACA/VMV/WCW, same loop as the IV one: 6 + 4 motors, i.e. 10 ZPM motors = 80 europium ingots); ZPM Lathe = hull + 2 circuits + motor + piston + grinding component + 3 cables; ZPM Electric Furnace = hull + 2 circuits + 4 coil-material double wire + 2 cables; the laser engraver and others follow the same loop (Unverified: the ZPM materials of the coil wire and grinder, check EMI). Each scan needs one of these machines in the Object Holder: build them as normal machines first.
- Structures (multis card): Component Part Assembly 36 enriched naquadah machine casings (hatch spots: 1 energy hatch, fluid input, maintenance, optical hatch) + 6 ULV input buses + 8 sturdy casings + 8 assembly line gratings + 16 fusion glass + 5 assembly line units + 10 FUSION COILS + 1 output bus. Heat Chamber 328 enderium casings + 95 high temperature smelting casings (parallel hatch, maintenance) + 77 enriched naquadah pipe casings + 48 RPP frames + 40 heat vents + 36 NAQUADAH COIL BLOCKS + 32 firebox + 24 intake + 16 machine casings. Large Rotor Machine 116 enriched naquadah machine casings (hatches, parallel hatch) + 14 gearboxes + 12 pipe casings + 10 + 10 intake and heat-escape casings + 8 trinaquadalloy frames + assembly line parts + lumium/twinite/shellite casings. Those pack casings are crafted in the casings.js and startup scripts: Unverified recipes.
- The ZPM-power Assembly Line: all three recipes run at VHA\[ZPM\] = 61 440 EU/t (VHA is half of VA; VA\[ZPM\] = 122 880): the LuV 4A hatch (131 072 EU/t) is more than enough, the quest says it ‘gives ZPM recipe speeds’. ITLC soldering alloy (14 indium + 3 tin + 2 lead + 1 cadmium as dust, startup solders.js) is the new fluid: 12 528 mB is 87 ingots of 144 mB. Unverified: the dust mixer recipe and the indium and cadmium sources.
- Mega Vacuum Freezer (era list; kjs additions/machines\_and\_parts/large\_multis.js): aluminium frame + 2 UV circuits + 4 dense rhodium plated palladium plates + 2 LuV field generators + 4 NbTi normal fluid pipes + 32 fine ITBTC wire + 6 HSS-E screws, 1152 mB soldering alloy, 400 ticks, but EUtVHA(UV): a UV-power Assembly Line recipe, so it is NOT a ZPM-era build (needs a LuV 16A or a UV hatch). Its research item is the super vacuum freezer (the Arctic Chilling Unit, itself an IV recipe) at 24 CWU/t. The Bulk Blast Chiller \[BBC\] is a GCYM multi (parallel hatch, batch mode) and, verified, a UV build: 2 UV circuits and VHA\[UV\] = 245 760 EU/t, so make it at the END of this era, after your first UV hatch and UV circuits, not in the middle. The structure is 161 frostproof casings, 74 tungsten steel pipe casings, 36 clean casings, 26 heat vents.
- Chambered Alloy Transmuter \[CAT\] (gtceu:super\_abs, the Boosted Alloy Blast Smelter; verified, intermediate\_multis.js and super\_abs.js): Assembly Line with a ZPM alloy smelter + 2 ZPM circuits + 2 double naquadah plates + 2 ZPM emitters + 4 europium springs + 8 vanadium gallium cables + 4 naquadria screws, 1008 mB soldering alloy + 432 mB PBI, 400 ticks, VHA\[ZPM\] = 61 440 EU/t, research alloy blast smelter 12 CWU/t. It runs the same alloy\_blast\_smelter recipes as the ABS with throughput boosting and batch mode, takes ONE energy hatch and heating coils, and has no special coolant slot: it replaces the ABS for bulk alloys but needs no better cooling. The Stargate Component Assembly, Runic Circuitry Assembly Station and Component Part Assembly are also built at VHA\[ZPM\] but ask for 16 / 4 / 4 UV circuits, which is why they close the era.
- Order of priority for the era: Component Part Assembly (every later component is a CPA recipe: it assembles parts like the living SMDs, quest ‘components are getting complex’), then the Large Rotor Machine (the stargate rod line), then the Heat Chamber (nether star concentrate, the activated rods). Each needs 4 UV circuits = 4 crystal mainframes (zpm\_uv\_circuit) and 96 UHPIC chips (48 UHPIC wafers) for two of them.
- Sub-steps people skip: (1) three different research machines to build and scan (ZPM assembler, lathe, electric furnace); (2) ZPM field generators 1, 12 and 1 respectively (Large Rotor Machine: 12 field generators = 72 stars + 72 ZPM circuits via emitters); (3) advanced power thrusters: an item of the pack (32 per rotor machine), Unverified recipe; (4) 96 UHPIC chips = the UHPIC wafer line (luv\_fusion): start it before anything else; (5) the Large Rotor Machine needs 116 casings plus gearboxes: crafted in advance.
- **Unverified** the recipes of the pack casings (enriched naquadah machine casing etc.), advanced power thrusters and the fusion-coil-heavy structure of the Component Part Assembly.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:heat_chamber` | 1 |
| `gtceu:large_rotor_machine` | 1 |
| `gtceu:assembly_line` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 2 |
| `functionalstorage:oak_1` | 28 |
| `modularrouters:modular_router` | 16 |
| `gtceu:lv_robot_arm` | 16 |
| `gtceu:item_filter` | 16 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:component_part_assembly`, `gtceu:heat_chamber`, `gtceu:large_rotor_machine`
