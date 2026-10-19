---
kind: chain
id: uiv_multis
order: 2220
data:
  t: |-
    UIV multiblock controllers: Abyssal Containment Room, Ultimate EBF, Atomic Materialization Plant, Component Part Hub (all Assembly Line + station research)
  inf: true
  "n":
    - - g1
      - |-
        Abyssal Containment Room: 1 draco abyssal frame · 8 draco ware casing · 4 abyssal inductor · 12 uiv computational matrix · 2 uiv micropower router · 8 uiv microfluidic flow valve · 64 fine rhenium super composite alloy wire · 4 uiv field generator · 224 uepic chip · 46 080 mB indium tin lead cadmium soldering alloy · 8 640 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 760 mB perfluoroelastomer rubber
      - g
      - functionalstorage:oak_1
      - - [draco abyssal frame, "gtceu:draco_abyssal_frame"]
        - [draco ware casing, "kubejs:draco_ware_casing"]
        - [abyssal inductor, "kubejs:abyssal_inductor"]
        - [uiv computational matrix, "kubejs:uiv_computational_matrix"]
        - [uiv micropower router, "kubejs:uiv_micropower_router"]
        - [uiv microfluidic flow valve, "kubejs:uiv_microfluidic_flow_valve"]
    - - g2
      - |-
        Ultimate EBF: 1 abyssal alloy frame · 8 UIV circuit · 4 dense draco abyssal plate · 6 uiv field generator · 4 uiv conveyor module · 8 borealic steel gear · 4 uiv electric motor · 18 small ultispestalloy cmsh gear · 4 lepton resonant thallium antimonide spring · 4 uiv microfluidic flow valve · 32 fine rhenium super composite alloy wire · 16 zeroidic trinate steel screw · 24 768 mB naquadated soldering alloy · 19 008 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 100 000 mB corefire nectar · 12 500 mB dragon breath
      - g
      - functionalstorage:oak_1
      - - [abyssal alloy frame, "gtceu:abyssal_alloy_frame"]
        - [UIV circuit, "kubejs:uiv_universal_circuit"]
        - [dense draco abyssal plate, "gtceu:dense_draco_abyssal_plate"]
        - [uiv field generator, "gtceu:uiv_field_generator"]
        - [uiv conveyor module, "gtceu:uiv_conveyor_module"]
        - [borealic steel gear, "gtceu:borealic_steel_gear"]
    - - g3
      - |-
        Atomic Materialization Plant: 1 uiv machine hull · 6 rhenotax coil · 8 uiv field generator · 12 UIV circuit · 6 uiv electric motor · 4 nyanium gear · 12 draco abyssal rotor · 6 small draconyallium gear · 2 uiv robot arm · 6 poly 34 ethylenedioxythiophene polystyrene sulfonate huge fluid pipe · 4 uiv fluid regulator · 96 fine rhenium super composite alloy wire · 18 720 mB naquadated soldering alloy · 15 696 mB perfluoroelastomer rubber · 10 080 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 040 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [rhenotax coil, "kubejs:rhenotax_coil"]
        - [uiv field generator, "gtceu:uiv_field_generator"]
        - [UIV circuit, "kubejs:uiv_universal_circuit"]
        - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [nyanium gear, "gtceu:nyanium_gear"]
    - - g4
      - |-
        Component Part Hub: 8 component part assembly · 6 uev computational matrix · 4 draco ware casing · 8 uev high strength panel · 4 uev robot arm · 4 uev field generator · 24 void screw · 64 uepic chip · 14 400 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB utopian akreyrium · 7 200 mB tungsten disulfide · 5 600 mB indium tin lead cadmium soldering alloy
      - g
      - functionalstorage:oak_1
      - - [component part assembly, "gtceu:component_part_assembly"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
        - [draco ware casing, "kubejs:draco_ware_casing"]
        - [uev high strength panel, "kubejs:uev_high_strength_panel"]
        - [uev robot arm, "gtceu:uev_robot_arm"]
        - [uev field generator, "gtceu:uev_field_generator"]
    - [al, "Assembly Line · 40 s / 90 s / 60 s / 2 min · 15 728 640 to 62 914 560 EU/t", m, "gtceu:assembly_line"]
    - [o1, Abyssal Containment Room, o, "start_core:abyssal_containment_room"]
    - [o2, Ultimate EBF, o, "gtceu:ultimate_ebf"]
    - [o3, Atomic Materialization Plant, o, "gtceu:atomic_materialization_plant"]
    - [o4, Component Part Hub, o, "gtceu:component_part_hub"]
  e:
    - [g1, al, "1"]
    - [g2, al, "1"]
    - [g3, al, "1"]
    - [g4, al, "1"]
    - [al, o1, "1 / 40 s"]
    - [al, o2, "1 / 90 s"]
    - [al, o3, "1 / 60 s"]
    - [al, o4, "1 / 2 min"]
  tips:
    - |-
      Source: kjs additions/multiblock_recipes/end_multis.js. Abyssal Containment Room: 800 ticks, EU = VA[UXV] (125 829 120), research Abyssal Inductor Hull (VHA[UIV], 224 CWU/t). Ultimate EBF: 1800 ticks, VHA[UXV] = 62 914 560 EU/t, research Mega Blast Furnace (VHA[UIV], 192 CWU/t). Atomic Materialization Plant: 1200 ticks, VHA[UXV], research Chemical Plant (VA[UIV], 216 CWU/t). Component Part Hub: 2400 ticks, VHA[UIV] = 15 728 640 EU/t, research Component Part Assembly (VHA[UEV], 192 CWU/t). Also here (not charted): Incomprehensible Chemical Reactor (UIV hull + 4 UIV motors + abyssal rotor + 2 nyanium large pipes + 4 UIV circuits, 1200 ticks, VHA[UIV], research Extreme Chemical Reactor 192 CWU/t), True Synthesis Array (UIV hull + 4 sensors + 4 arms + 4 regulators + 2 abyssal rotors + 6 nyanium large pipes + 6 UIV circuits + 2 lepton springs, VHA[UXV], research Advanced Synthesis Plant 256 CWU/t) and the Abyssal Akreyriadix Stabiliser (UIV hull + 12 UIV circuits + 192 UEPIC chips + 16 nether star and 16 echo shard lenses + 32 nyanium pipes + 4 field generators etc., 75 000 mB dragon breath).
    - |-
      EU/t reality: the Ultimate EBF, Atomic Materialization Plant, Abyssal Containment Room and True Synthesis Array recipes are priced at UXV voltage (about 63 M EU/t, the Containment Room 126 M; one UIV hatch is 33.5 M): the controller has to be fed through 4A or larger UIV hatches (uev/uiv_hatches) or a 256A laser target hatch: Unverified whether the Assembly Line accepts that voltage with UIV hatches (GT multi-amp hatches combine their amperage; the quest or recipe viewer will tell).
    - |-
      Multiblock sizes (from the pack patterns): Ultimate EBF about 3 400 blocks: 1092 extreme temperature smelting casings (item/fluid/energy hatches, max 8 each, 2 energy), 840 reinforced brimstone casings, 468 nyanium pipe casings, 436 abyssal alloy frames, 212 heating coils, 148 heat vents, 124 intake, 92 firebox, 8 machine casings, 4 UEV rotor holders and 4 mufflers (the rotor holders are uev_power). Atomic Materialization Plant about 500 blocks: 210 cattomolymer casings (hatches), 72 draco abyssal frames, 58 heat vents, 36 rhenotax coils, 32 noble mixing casings, 32 PTFE pipe casings, 24 draco resilient fusion glass, 21 pipe casings, 16 intake, 10 abyssal inductor hulls, 7 coils, 1 UEV rotor holder. Component Part Hub about 340 blocks: 120 advanced assembly casings (hatches), 48 draco resilient fusion glass, 35 draco ware casings, 35 superdense assembly machine casings, 26 draco assembly gratings, 24 firebox, 16 advanced fusion coils, 12 nyanium machine casings, 10 control casings, 9 trinium coils and a UHV rotor holder. The Draco Circuit Assembler itself is tiny (37 enriched naquadah casings + 3 ware casings + 3 glass + 3 control + 2 gratings).
    - |-
      Casings in this list without their own chain: draco assembly grating, draco ware casing (uiv_circuits has it), draco resilient fusion glass and the abyssal inductor and its hull are specialUltimateCasing recipes in casings.js (Assembly Line, 400 ticks, VHA[UIV], research 216 CWU/t, with UIV components and circuits); the rhenotax coil, cattomolymer casing, noble mixing casing, superdense assembly casings and corefire nectar were not traced (Unverified). Casing counts of this size are the real cost of the era.
    - |-
      Sub-steps people skip: (1) research chain: Mega Blast Furnace, Chemical Plant, Abyssal Inductor Hull and Component Part Assembly must be scanned before the AL runs; (2) the Component Part Hub eats 8 Component Part Assembly controllers: build those first (uev_parts); (3) draconic eyes and UXV circuits come from uiv_infusion and uiv_circuits; (4) the Abyssal Containment Room unlocks abyssal circuits, tier 7 reflectors and the prismalic helix core.
    - |-
      Unverified: UXV voltage handling, hatch minimums, corefire nectar supply (heat chamber with the flamewake loop), and the abyssal inductor hull route.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uhv_input_bus", 8]
    - ["gtceu:uhv_input_hatch", 6]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:uepic_chip", "kubejs:uiv_universal_circuit"]
      t: |-
        Drawers first: UEPIC chips (224 for the room, 64 for the hub), UIV circuits (8 for the EBF, 12 for the plant), UIV field generators, UIV motors, UIV microfluidic flow valves and micropower routers, rhenium composite wire, frames, gears. Drums: soldering alloy, PEDOT:PSS, perfluoroelastomer rubber, corefire nectar, dragon breath, calamatium, utopian akreyrium, tungsten disulfide.
    - i: ["start_core:abyssal_containment_room", "kubejs:abyssal_inductor_hull"]
      t: |-
        Abyssal Containment Room first: it opens the abyssal circuit boards and the tier 7 parts. Needs abyssal inductor hull research (224 CWU/t).
    - i: ["gtceu:component_part_hub", "gtceu:component_part_assembly"]
      t: |-
        Component Part Hub next: it replaces 8 Component Part Assembly controllers and gives the parts at scale (uev_parts and uiv_parts).
    - i: ["gtceu:ultimate_ebf", "gtceu:mega_blast_furnace"]
      t: |-
        Ultimate EBF: research the Mega Blast Furnace first, then the AL run. Build the huge pattern with enough heating coils; place 4 UEV rotor holders.
    - i: ["gtceu:atomic_materialization_plant", "kubejs:rhenotax_coil"]
      t: |-
        Atomic Materialization Plant: 6 rhenotax coils in the recipe, 36 in the pattern; research the Chemical Plant first.
    - i: ["functionalstorage:oak_1", "gtceu:atomic_materialization_plant"]
      t: |-
        Hatches for all of them are UHV item and fluid hatches plus UIV energy hatches: from uiv_hatches.
---
# UIV multiblock controllers: Abyssal Containment Room, Ultimate EBF, Atomic Materialization Plant, Component Part Hub (all Assembly Line + station research)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_multis` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV controllers, threading, fusion](../../plan/p19.md#uivmulti)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s / 90 s / 60 s / 2 min · 15 728 640 to 62 914 560 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Abyssal Containment Room: 1 draco abyssal frame · 8 draco ware casing · 4 abyssal inductor · 12 uiv computational matrix · 2 uiv micropower router · 8 uiv microfluidic flow valve · 64 fine rhenium super composite alloy wire · 4 uiv field generator · 224 uepic chip · 46 080 mB indium tin lead cadmium soldering alloy · 8 640 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 760 mB perfluoroelastomer rubber (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Abyssal Containment Room: 1 draco abyssal frame · 8 draco ware casing · 4 abyssal inductor · 12 uiv computational matrix · 2 uiv micropower router · 8 uiv microfluidic flow valve · 64 fine rhenium super composite alloy wire · 4 uiv field generator · 224 uepic chip · 46 080 mB indium tin lead cadmium soldering alloy · 8 640 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 760 mB perfluoroelastomer rubber</span><span class="gt-sub"><span>draco abyssal frame</span><span>draco ware casing</span><span>abyssal inductor</span><span>uiv computational matrix</span><span>uiv micropower router</span><span>uiv microfluidic flow valve</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Ultimate EBF: 1 abyssal alloy frame · 8 UIV circuit · 4 dense draco abyssal plate · 6 uiv field generator · 4 uiv conveyor module · 8 borealic steel gear · 4 uiv electric motor · 18 small ultispestalloy cmsh gear · 4 lepton resonant thallium antimonide spring · 4 uiv microfluidic flow valve · 32 fine rhenium super composite alloy wire · 16 zeroidic trinate steel screw · 24 768 mB naquadated soldering alloy · 19 008 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 100 000 mB corefire nectar · 12 500 mB dragon breath (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Ultimate EBF: 1 abyssal alloy frame · 8 UIV circuit · 4 dense draco abyssal plate · 6 uiv field generator · 4 uiv conveyor module · 8 borealic steel gear · 4 uiv electric motor · 18 small ultispestalloy cmsh gear · 4 lepton resonant thallium antimonide spring · 4 uiv microfluidic flow valve · 32 fine rhenium super composite alloy wire · 16 zeroidic trinate steel screw · 24 768 mB naquadated soldering alloy · 19 008 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 100 000 mB corefire nectar · 12 500 mB dragon breath</span><span class="gt-sub"><span>abyssal alloy frame</span><span>UIV circuit</span><span>dense draco abyssal plate</span><span>uiv field generator</span><span>uiv conveyor module</span><span>borealic steel gear</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Atomic Materialization Plant: 1 uiv machine hull · 6 rhenotax coil · 8 uiv field generator · 12 UIV circuit · 6 uiv electric motor · 4 nyanium gear · 12 draco abyssal rotor · 6 small draconyallium gear · 2 uiv robot arm · 6 poly 34 ethylenedioxythiophene polystyrene sulfonate huge fluid pipe · 4 uiv fluid regulator · 96 fine rhenium super composite alloy wire · 18 720 mB naquadated soldering alloy · 15 696 mB perfluoroelastomer rubber · 10 080 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 040 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Atomic Materialization Plant: 1 uiv machine hull · 6 rhenotax coil · 8 uiv field generator · 12 UIV circuit · 6 uiv electric motor · 4 nyanium gear · 12 draco abyssal rotor · 6 small draconyallium gear · 2 uiv robot arm · 6 poly 34 ethylenedioxythiophene polystyrene sulfonate huge fluid pipe · 4 uiv fluid regulator · 96 fine rhenium super composite alloy wire · 18 720 mB naquadated soldering alloy · 15 696 mB perfluoroelastomer rubber · 10 080 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 040 mB calamatium</span><span class="gt-sub"><span>uiv machine hull</span><span>rhenotax coil</span><span>uiv field generator</span><span>UIV circuit</span><span>uiv electric motor</span><span>nyanium gear</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Component Part Hub: 8 component part assembly · 6 uev computational matrix · 4 draco ware casing · 8 uev high strength panel · 4 uev robot arm · 4 uev field generator · 24 void screw · 64 uepic chip · 14 400 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB utopian akreyrium · 7 200 mB tungsten disulfide · 5 600 mB indium tin lead cadmium soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Component Part Hub: 8 component part assembly · 6 uev computational matrix · 4 draco ware casing · 8 uev high strength panel · 4 uev robot arm · 4 uev field generator · 24 void screw · 64 uepic chip · 14 400 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB utopian akreyrium · 7 200 mB tungsten disulfide · 5 600 mB indium tin lead cadmium soldering alloy</span><span class="gt-sub"><span>component part assembly</span><span>uev computational matrix</span><span>draco ware casing</span><span>uev high strength panel</span><span>uev robot arm</span><span>uev field generator</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s · 90 s · 60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Abyssal Containment Room (start_core:abyssal_containment_room) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/start_core__abyssal_containment_room.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Abyssal Containment Room</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Ultimate EBF (gtceu:ultimate_ebf) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__ultimate_ebf.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ultimate EBF</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Atomic Materialization Plant (gtceu:atomic_materialization_plant) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__atomic_materialization_plant.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Atomic Materialization Plant</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Component Part Hub (gtceu:component_part_hub) - 1 / 2 min"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_hub.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Component Part Hub</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 40 s / 90 s / 60 s / 2 min · 15 728 640 to 62 914 560 EU/t](#m-al)

## How to build

1. Drawers first: UEPIC chips (224 for the room, 64 for the hub), UIV circuits (8 for the EBF, 12 for the plant), UIV field generators, UIV motors, UIV microfluidic flow valves and micropower routers, rhenium composite wire, frames, gears. Drums: soldering alloy, PEDOT:PSS, perfluoroelastomer rubber, corefire nectar, dragon breath, calamatium, utopian akreyrium, tungsten disulfide. — `functionalstorage:oak_1`, `kubejs:uepic_chip`, `kubejs:uiv_universal_circuit`
2. Abyssal Containment Room first: it opens the abyssal circuit boards and the tier 7 parts. Needs abyssal inductor hull research (224 CWU/t). — `start_core:abyssal_containment_room`, `kubejs:abyssal_inductor_hull`
3. Component Part Hub next: it replaces 8 Component Part Assembly controllers and gives the parts at scale (uev\_parts and uiv\_parts). — `gtceu:component_part_hub`, `gtceu:component_part_assembly`
4. Ultimate EBF: research the Mega Blast Furnace first, then the AL run. Build the huge pattern with enough heating coils; place 4 UEV rotor holders. — `gtceu:ultimate_ebf`, `gtceu:mega_blast_furnace`
5. Atomic Materialization Plant: 6 rhenotax coils in the recipe, 36 in the pattern; research the Chemical Plant first. — `gtceu:atomic_materialization_plant`, `kubejs:rhenotax_coil`
6. Hatches for all of them are UHV item and fluid hatches plus UIV energy hatches: from uiv\_hatches. — `functionalstorage:oak_1`, `gtceu:atomic_materialization_plant`

## Tips

- Source: kjs additions/multiblock\_recipes/end\_multis.js. Abyssal Containment Room: 800 ticks, EU = VA\[UXV\] (125 829 120), research Abyssal Inductor Hull (VHA\[UIV\], 224 CWU/t). Ultimate EBF: 1800 ticks, VHA\[UXV\] = 62 914 560 EU/t, research Mega Blast Furnace (VHA\[UIV\], 192 CWU/t). Atomic Materialization Plant: 1200 ticks, VHA\[UXV\], research Chemical Plant (VA\[UIV\], 216 CWU/t). Component Part Hub: 2400 ticks, VHA\[UIV\] = 15 728 640 EU/t, research Component Part Assembly (VHA\[UEV\], 192 CWU/t). Also here (not charted): Incomprehensible Chemical Reactor (UIV hull + 4 UIV motors + abyssal rotor + 2 nyanium large pipes + 4 UIV circuits, 1200 ticks, VHA\[UIV\], research Extreme Chemical Reactor 192 CWU/t), True Synthesis Array (UIV hull + 4 sensors + 4 arms + 4 regulators + 2 abyssal rotors + 6 nyanium large pipes + 6 UIV circuits + 2 lepton springs, VHA\[UXV\], research Advanced Synthesis Plant 256 CWU/t) and the Abyssal Akreyriadix Stabiliser (UIV hull + 12 UIV circuits + 192 UEPIC chips + 16 nether star and 16 echo shard lenses + 32 nyanium pipes + 4 field generators etc., 75 000 mB dragon breath).
- EU/t reality: the Ultimate EBF, Atomic Materialization Plant, Abyssal Containment Room and True Synthesis Array recipes are priced at UXV voltage (about 63 M EU/t, the Containment Room 126 M; one UIV hatch is 33.5 M): the controller has to be fed through 4A or larger UIV hatches (uev/uiv\_hatches) or a 256A laser target hatch: Unverified whether the Assembly Line accepts that voltage with UIV hatches (GT multi-amp hatches combine their amperage; the quest or recipe viewer will tell).
- Multiblock sizes (from the pack patterns): Ultimate EBF about 3 400 blocks: 1092 extreme temperature smelting casings (item/fluid/energy hatches, max 8 each, 2 energy), 840 reinforced brimstone casings, 468 nyanium pipe casings, 436 abyssal alloy frames, 212 heating coils, 148 heat vents, 124 intake, 92 firebox, 8 machine casings, 4 UEV rotor holders and 4 mufflers (the rotor holders are uev\_power). Atomic Materialization Plant about 500 blocks: 210 cattomolymer casings (hatches), 72 draco abyssal frames, 58 heat vents, 36 rhenotax coils, 32 noble mixing casings, 32 PTFE pipe casings, 24 draco resilient fusion glass, 21 pipe casings, 16 intake, 10 abyssal inductor hulls, 7 coils, 1 UEV rotor holder. Component Part Hub about 340 blocks: 120 advanced assembly casings (hatches), 48 draco resilient fusion glass, 35 draco ware casings, 35 superdense assembly machine casings, 26 draco assembly gratings, 24 firebox, 16 advanced fusion coils, 12 nyanium machine casings, 10 control casings, 9 trinium coils and a UHV rotor holder. The Draco Circuit Assembler itself is tiny (37 enriched naquadah casings + 3 ware casings + 3 glass + 3 control + 2 gratings).
- Casings in this list without their own chain: draco assembly grating, draco ware casing (uiv\_circuits has it), draco resilient fusion glass and the abyssal inductor and its hull are specialUltimateCasing recipes in casings.js (Assembly Line, 400 ticks, VHA\[UIV\], research 216 CWU/t, with UIV components and circuits); the rhenotax coil, cattomolymer casing, noble mixing casing, superdense assembly casings and corefire nectar were not traced (Unverified). Casing counts of this size are the real cost of the era.
- Sub-steps people skip: (1) research chain: Mega Blast Furnace, Chemical Plant, Abyssal Inductor Hull and Component Part Assembly must be scanned before the AL runs; (2) the Component Part Hub eats 8 Component Part Assembly controllers: build those first (uev\_parts); (3) draconic eyes and UXV circuits come from uiv\_infusion and uiv\_circuits; (4) the Abyssal Containment Room unlocks abyssal circuits, tier 7 reflectors and the prismalic helix core.
- **Unverified** UXV voltage handling, hatch minimums, corefire nectar supply (heat chamber with the flamewake loop), and the abyssal inductor hull route.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uhv_input_bus` | 8 |
| `gtceu:uhv_input_hatch` | 6 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Main source for:** `start_core:abyssal_containment_room`, `gtceu:ultimate_ebf`, `gtceu:atomic_materialization_plant`, `gtceu:component_part_hub`
