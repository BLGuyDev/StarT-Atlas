---
kind: chain
id: uiv_circuits
order: 2170
data:
  t: |-
    Draco Circuit Assembler (controller) and its UEV and UIV circuits: draconic computer and mainframe, abyssal assembly and computer
  inf: true
  "n":
    - - g0
      - |-
        Draco Circuit Assembler: 1 void frame · 6 draco ware casing · 6 uev computational matrix · 4 uev sensor · 8 uev robot arm · 4 uev conveyor module · 32 fine enriched pallarovium alloy wire · 8 calamatium screw · 125 000 mB indium tin lead cadmium soldering alloy · 75 000 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 50 000 mB sterilized growth medium · 28 800 mB isovol
      - g
      - functionalstorage:oak_1
      - - [void frame, "gtceu:void_frame"]
        - [draco ware casing, "kubejs:draco_ware_casing"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
        - [uev sensor, "gtceu:uev_sensor"]
        - [uev robot arm, "gtceu:uev_robot_arm"]
        - [uev conveyor module, "gtceu:uev_conveyor_module"]
    - - al
      - Assembly Line · 4 min · 15 728 640 EU/t · research Large Circuit Assembler 192 CWU/t
      - m
      - gtceu:assembly_line
    - [dc, Draco Circuit Assembler, x, "gtceu:draco_circuit_assembler"]
    - - g1
      - |-
        Draconic processor computer: draconic board · 2 draconic processor assembly · 8 qmd diode · 48 QRAM · 16 hyper NOR · 32 hyper NAND · 16 void foil · 32 PEDOT foil · 32 fine polonium bismide wire · 2 aurourium plate · 1152 / 576 / 250 mB
      - g
      - functionalstorage:oak_1
      - - [Draconic circuit board, "kubejs:draconic_printed_circuit_board"]
        - [Draconic processor assembly, "kubejs:draconic_processor_assembly"]
        - [QRAM chip, "kubejs:qram_chip"]
        - [Aurourium plate, "gtceu:aurourium_plate"]
    - - g2
      - |-
        Draconic processor mainframe: 2 void frame · 2 draconic computer · 64 QRAM · 2 UEPIC chip · 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor (qmd) · 32 void foil · energy module · 64 aerogel foil · 32 polonium bismide wire · 4 aurourium plate
      - g
      - functionalstorage:oak_1
      - - [Void frame, "gtceu:void_frame"]
        - [Draconic processor computer, "kubejs:draconic_processor_computer"]
        - [UEPIC chip, "kubejs:uepic_chip"]
        - [Energy module, "gtceu:energy_module"]
    - - g3
      - |-
        Abyssal processor assembly: abyssal board · 2 abyssal processor · 4 hvga steel bolt · 16 stellar RAM chip · 12 inductor · 24 capacitor · 16 fine lepton wire · draco abyssal plate
      - g
      - functionalstorage:oak_1
      - - [Abyssal circuit board, "kubejs:abyssal_printed_circuit_board"]
        - [Abyssal processor, "kubejs:abyssal_processor"]
        - [Stellar RAM chip, "kubejs:stellar_ram_chip"]
        - [Draco abyssal plate, "gtceu:draco_abyssal_plate"]
    - - g4
      - |-
        Abyssal processor computer: abyssal board · 2 abyssal assembly · 16 diode · 24 stellar RAM · 32 hyper NOR · 64 hyper NAND · 8 hvga bolt · 32 draconyallium foil · 4 nyanium tiny pipe · 64 PEDOT foil · 32 fine lepton wire · 2 draco abyssal plate
      - g
      - functionalstorage:oak_1
      - - [Abyssal processor assembly, "kubejs:abyssal_processor_assembly"]
        - [Draconyallium foil, "gtceu:draconyallium_foil"]
        - [Nyanium tiny pipe, "gtceu:nyanium_tiny_fluid_pipe"]
    - [o1, "Draconic Processor Computer (UEV circuit)", o, "kubejs:draconic_processor_computer"]
    - [o2, "Draconic Processor Mainframe (UIV circuit)", o, "kubejs:draconic_processor_mainframe"]
    - [o3, "Abyssal Processor Assembly (UEV circuit)", o, "kubejs:abyssal_processor_assembly"]
    - [o4, "Abyssal Processor Computer (UIV circuit)", o, "kubejs:abyssal_processor_computer"]
  e:
    - [g0, al, "1"]
    - [al, dc, "1 / 4 min"]
    - [dc, g1, recipe]
    - [dc, g2, recipe]
    - [dc, g3, recipe]
    - [dc, g4, recipe]
    - [g1, o1, "1 / 60 s"]
    - [g2, o2, "1 / 90 s"]
    - [g3, o3, "2 / 40 s"]
    - [g4, o4, "1 / 60 s"]
  tips:
    - |-
      Source: kjs additions/progression/circuitry/{draco_circuit_assembly,circuits}.js and utils/tags.js. Controller: Assembly Line 4800 ticks, VHA[UIV] = 15 728 640 EU/t, station research Large Circuit Assembler (VA[UEV], 192 CWU/t); void frame + 6 draco ware casings + 6 UEV computational matrices + 4 UEV sensors + 8 UEV robot arms + 4 UEV conveyor modules + 32 fine enriched pallarovium alloy wire + 8 calamatium screws; 125 000 mB indium tin lead cadmium soldering alloy + 75 000 mB PEDOT:PSS + 50 000 mB sterilized growth medium + 28 800 mB isovol. Draco ware casing: Assembly Line 400 ticks, VHA[UIV], research High Power Casing (216 CWU/t): trikoductive neutro steel frame + 6 draconic brain matter cells + 2 UEV circuits + UEV sensor + 32 fine aurourium wire + 32 fine magmada alloy wire, 1008 mB PEDOT:PSS + 2250 mB dragon breath.
    - |-
      The machine runs two recipe types (startup draco_circuit_assembly.js): draco_circuit_assembler (the circuits below, each with station research of the previous item) and draco_bulk_circuiter (8 to 24 universal circuits per run from boards and SoCs, EU/3.5 of a high tier: for example 8 LuV universal circuits at VA[UHV] / 3.5). Circuit tags: UEV = runic processor mainframe, draconic processor computer, abyssal processor assembly; UIV = draconic processor mainframe, abyssal processor computer; UXV = abyssal processor mainframe (utils/tags.js).
    - |-
      Recipes (all with naquadated soldering alloy, PEDOT:PSS and dragon breath or draconic enrichment serum = DES): draconic processor computer (UEV): 1200 ticks, VA[UHV] = 1 966 080 EU/t, research draconic processor assembly 176 CWU/t, 1152 mB solder + 576 mB PEDOT:PSS + 250 mB dragon breath. Draconic processor mainframe (UIV): 1800 ticks, VA[UEV] = 7 864 320 EU/t, research draconic processor computer 192 CWU/t, 2304 + 1152 mB + 500 mB dragon breath. Abyssal processor assembly (UEV, 2 per run): 800 ticks, VA[UEV], research abyssal processor 216 CWU/t, 1152 + 576 mB + 250 mB DES. Abyssal processor computer (UIV): 1200 ticks, VA[UEV], 240 CWU/t, 2304 + 1152 mB + 500 mB DES.
    - |-
      Prerequisites you must already have (UV and UHV pages): draconic processing unit, draconic microchip processor, draconic processor, draconic processor assembly, abyssal processing unit, abyssal processor, QRAM chips (+ stellar RAM chips for the abyssal ones), hyper NAND and NOR memory chips, void foil, aerogel foil, qmd SMDs (draconic qmd transistor, resistor, capacitor, diode, inductor). Boards (circuits.js): draconic circuit board = 48 runic circuit boards + neutronium drum + UV pump + UV sensor + 2 ZPM circuits + 16 aurourium foil + 2000 mB dragon breath, circuit assembler, sterile cleanroom, VA[UV], 1200 ticks, 48 boards; abyssal circuit board = 64 draconic circuit boards + blank injection catalyst + UHV pump + UHV sensor + 2 UV circuits + 16 draco abyssal foil + 6000 mB draconic enrichment serum, VHA[UEV], 1200 ticks, 64 boards, in the Abyssal Containment Room (the printed-board step between them: Unverified). That room is a UXV-voltage Assembly Line recipe (start_core:abyssal_containment_room: draco abyssal frame + 8 draco ware casings + 4 abyssal inductors + 12 UIV computational matrices + 2 UIV micropower routers + 8 UIV microfluidic flow valves + 64 fine rhenium super composite alloy wire + 4 UIV field generators + 224 UEPIC chips, 46 080 mB solder + 8640 mB PEDOT:PSS + 5760 mB perfluoroelastomer rubber, research abyssal inductor hull 224 CWU/t).
    - |-
      Consumption: the draconic mainframe needs 2 draconic computers = 4 draconic assemblies = 8 draconic processors; with 2 UEPIC chips, 64 QRAM chips, 24 qmd SMDs per type and 1 energy module. The abyssal computer needs 2 abyssal assemblies = 4 abyssal processors, 24 stellar RAM chips and 32 draconyallium foil. The UEV circuits for the Hell Forge, Chiller and heat chambers (uev_multis) are the first customers; UIV circuits go into the UIV hull-tier machines, fusion reactor (4 UIV circuits for UEV; 4 UXV for UIV), Ultimate EBF (8) and atomic materialization plant (12).
    - |-
      Draco Circuit Assembler facts (verified): it is ONE multiblock with two recipe types (draco_circuit_assembler and draco_bulk_circuiter), not separate machines; Assembly Line VHA[UIV] = 15 728 640 EU/t. Its recipes carry no cleanroom requirement (the normal circuit assembler recipes ask for a cleanroom or sterile room), which is why it replaces the cleanroom circuit assemblers in UEV and UIV; the controller recipe burns 50 000 mB sterilized growth medium (SGM, uv_bio2), and each ASG computational matrix 5000 mB. Parallel hatches: the UEV absolute parallel hatch asks for UIV circuits (4 + 2) and the UIV one for UXV circuits (abyssal mainframe). Draconic computer VA[UHV], mainframe VA[UEV] with 2 UEPIC chips.
    - |-
      Sub-steps people skip: (1) research chain: the station research item of each recipe must be made and scanned in order (processor assembly → computer → mainframe); (2) the recipe EU/t is above a single UEV hatch for the mainframe: use laser target hatches or 4A/16A hatches; (3) abyssal circuits need the Abyssal Containment Room, not a plain cleanroom; (4) keep 2 drawers of draconic brain matter cells and a spare draconic eye for the abyssal mainframe (UXV, next era).
    - |-
      Unverified: the draconic board and unit recipes in detail (UV and UHV pages), the qmd SMD lines, hatch minimums of the Draco Circuit Assembler, and how the abyssal room attaches to the multiblock.
  b:
    - ["gtceu:draco_circuit_assembler", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uhv_input_bus", 6]
    - ["gtceu:uhv_input_hatch", 4]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:draco_ware_casing", "kubejs:uev_computational_matrix"]
      t: |-
        Controller first: draco ware casings (6) need UEV circuits, brain matter cells, aurourium and magmada wire; matrices, sensors, arms and conveyors from uev_parts and uev_components. Drums: soldering alloy 125 000 mB, PEDOT:PSS, sterilized growth medium, isovol.
    - i: ["gtceu:draco_circuit_assembler", "kubejs:draconic_processor_computer"]
      t: |-
        First product: draconic processor computer (UEV circuit). Its research item is the draconic processor assembly. One router or Pipez item pipe per drawer, Item Filters, Robot Arm Keep Exact; fluids by Pipez fluid pipes with pump covers.
    - i: ["gtceu:draco_circuit_assembler", "kubejs:draconic_processor_mainframe"]
      t: Then the mainframe (2 computers + 2 void frames + 64 QRAM + chips + SMDs). 90 s at 7 864 320 EU/t. Needs the energy module and aerogel foil in drawers.
    - i: ["gtceu:draco_circuit_assembler", "kubejs:abyssal_processor_assembly"]
      t: |-
        Abyssal assembly and computer: same machine, other drums (draconic enrichment serum instead of dragon breath) and the Abyssal Containment Room for the boards.
    - i: ["functionalstorage:oak_1", "kubejs:draconic_processor_mainframe", "kubejs:abyssal_processor_computer"]
      t: Output drawers Keep Exact 12 for each circuit; every UIV multiblock recipe eats 4 to 12.
---
# Draco Circuit Assembler (controller) and its UEV and UIV circuits: draconic computer and mainframe, abyssal assembly and computer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_circuits` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [Draco Infusion, UIPIC chip, UIV circuits](../../plan/p19.md#uivdraco)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 4 min · 15 728 640 EU/t · research Large Circuit Assembler 192 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Draco Circuit Assembler: 1 void frame · 6 draco ware casing · 6 uev computational matrix · 4 uev sensor · 8 uev robot arm · 4 uev conveyor module · 32 fine enriched pallarovium alloy wire · 8 calamatium screw · 125 000 mB indium tin lead cadmium soldering alloy · 75 000 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 50 000 mB sterilized growth medium · 28 800 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Draco Circuit Assembler: 1 void frame · 6 draco ware casing · 6 uev computational matrix · 4 uev sensor · 8 uev robot arm · 4 uev conveyor module · 32 fine enriched pallarovium alloy wire · 8 calamatium screw · 125 000 mB indium tin lead cadmium soldering alloy · 75 000 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 50 000 mB sterilized growth medium · 28 800 mB isovol</span><span class="gt-sub"><span>void frame</span><span>draco ware casing</span><span>uev computational matrix</span><span>uev sensor</span><span>uev robot arm</span><span>uev conveyor module</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">4 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Draco Circuit Assembler (gtceu:draco_circuit_assembler) - 1 / 4 min"><img class="gt-ico" src="../../assets/icons/gtceu__draco_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Draco Circuit Assembler</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 4 min · 15 728 640 EU/t · research Large Circuit Assembler 192 CWU/t](#m-al)

### Direct steps

- Draco Circuit Assembler → Draconic processor computer: draconic board · 2 draconic processor assembly · 8 qmd diode · 48 QRAM · 16 hyper NOR · 32 hyper NAND · 16 void foil · 32 PEDOT foil · 32 fine polonium bismide wire · 2 aurourium plate · 1152 / 576 / 250 mB (recipe)
- Draco Circuit Assembler → Draconic processor mainframe: 2 void frame · 2 draconic computer · 64 QRAM · 2 UEPIC chip · 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor (qmd) · 32 void foil · energy module · 64 aerogel foil · 32 polonium bismide wire · 4 aurourium plate (recipe)
- Draco Circuit Assembler → Abyssal processor assembly: abyssal board · 2 abyssal processor · 4 hvga steel bolt · 16 stellar RAM chip · 12 inductor · 24 capacitor · 16 fine lepton wire · draco abyssal plate (recipe)
- Draco Circuit Assembler → Abyssal processor computer: abyssal board · 2 abyssal assembly · 16 diode · 24 stellar RAM · 32 hyper NOR · 64 hyper NAND · 8 hvga bolt · 32 draconyallium foil · 4 nyanium tiny pipe · 64 PEDOT foil · 32 fine lepton wire · 2 draco abyssal plate (recipe)
- Draconic processor computer: draconic board · 2 draconic processor assembly · 8 qmd diode · 48 QRAM · 16 hyper NOR · 32 hyper NAND · 16 void foil · 32 PEDOT foil · 32 fine polonium bismide wire · 2 aurourium plate · 1152 / 576 / 250 mB → Draconic Processor Computer (UEV circuit) (1 / 60 s)
- Draconic processor mainframe: 2 void frame · 2 draconic computer · 64 QRAM · 2 UEPIC chip · 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor (qmd) · 32 void foil · energy module · 64 aerogel foil · 32 polonium bismide wire · 4 aurourium plate → Draconic Processor Mainframe (UIV circuit) (1 / 90 s)
- Abyssal processor assembly: abyssal board · 2 abyssal processor · 4 hvga steel bolt · 16 stellar RAM chip · 12 inductor · 24 capacitor · 16 fine lepton wire · draco abyssal plate → Abyssal Processor Assembly (UEV circuit) (2 / 40 s)
- Abyssal processor computer: abyssal board · 2 abyssal assembly · 16 diode · 24 stellar RAM · 32 hyper NOR · 64 hyper NAND · 8 hvga bolt · 32 draconyallium foil · 4 nyanium tiny pipe · 64 PEDOT foil · 32 fine lepton wire · 2 draco abyssal plate → Abyssal Processor Computer (UIV circuit) (1 / 60 s)

## How to build

1. Controller first: draco ware casings (6) need UEV circuits, brain matter cells, aurourium and magmada wire; matrices, sensors, arms and conveyors from uev\_parts and uev\_components. Drums: soldering alloy 125 000 mB, PEDOT:PSS, sterilized growth medium, isovol. — `functionalstorage:oak_1`, `kubejs:draco_ware_casing`, `kubejs:uev_computational_matrix`
2. First product: draconic processor computer (UEV circuit). Its research item is the draconic processor assembly. One router or Pipez item pipe per drawer, Item Filters, Robot Arm Keep Exact; fluids by Pipez fluid pipes with pump covers. — `gtceu:draco_circuit_assembler`, `kubejs:draconic_processor_computer`
3. Then the mainframe (2 computers + 2 void frames + 64 QRAM + chips + SMDs). 90 s at 7 864 320 EU/t. Needs the energy module and aerogel foil in drawers. — `gtceu:draco_circuit_assembler`, `kubejs:draconic_processor_mainframe`
4. Abyssal assembly and computer: same machine, other drums (draconic enrichment serum instead of dragon breath) and the Abyssal Containment Room for the boards. — `gtceu:draco_circuit_assembler`, `kubejs:abyssal_processor_assembly`
5. Output drawers Keep Exact 12 for each circuit; every UIV multiblock recipe eats 4 to 12. — `functionalstorage:oak_1`, `kubejs:draconic_processor_mainframe`, `kubejs:abyssal_processor_computer`

## Tips

- Source: kjs additions/progression/circuitry/{draco\_circuit\_assembly,circuits}.js and utils/tags.js. Controller: Assembly Line 4800 ticks, VHA\[UIV\] = 15 728 640 EU/t, station research Large Circuit Assembler (VA\[UEV\], 192 CWU/t); void frame + 6 draco ware casings + 6 UEV computational matrices + 4 UEV sensors + 8 UEV robot arms + 4 UEV conveyor modules + 32 fine enriched pallarovium alloy wire + 8 calamatium screws; 125 000 mB indium tin lead cadmium soldering alloy + 75 000 mB PEDOT:PSS + 50 000 mB sterilized growth medium + 28 800 mB isovol. Draco ware casing: Assembly Line 400 ticks, VHA\[UIV\], research High Power Casing (216 CWU/t): trikoductive neutro steel frame + 6 draconic brain matter cells + 2 UEV circuits + UEV sensor + 32 fine aurourium wire + 32 fine magmada alloy wire, 1008 mB PEDOT:PSS + 2250 mB dragon breath.
- The machine runs two recipe types (startup draco\_circuit\_assembly.js): draco\_circuit\_assembler (the circuits below, each with station research of the previous item) and draco\_bulk\_circuiter (8 to 24 universal circuits per run from boards and SoCs, EU/3.5 of a high tier: for example 8 LuV universal circuits at VA\[UHV\] / 3.5). Circuit tags: UEV = runic processor mainframe, draconic processor computer, abyssal processor assembly; UIV = draconic processor mainframe, abyssal processor computer; UXV = abyssal processor mainframe (utils/tags.js).
- Recipes (all with naquadated soldering alloy, PEDOT:PSS and dragon breath or draconic enrichment serum = DES): draconic processor computer (UEV): 1200 ticks, VA\[UHV\] = 1 966 080 EU/t, research draconic processor assembly 176 CWU/t, 1152 mB solder + 576 mB PEDOT:PSS + 250 mB dragon breath. Draconic processor mainframe (UIV): 1800 ticks, VA\[UEV\] = 7 864 320 EU/t, research draconic processor computer 192 CWU/t, 2304 + 1152 mB + 500 mB dragon breath. Abyssal processor assembly (UEV, 2 per run): 800 ticks, VA\[UEV\], research abyssal processor 216 CWU/t, 1152 + 576 mB + 250 mB DES. Abyssal processor computer (UIV): 1200 ticks, VA\[UEV\], 240 CWU/t, 2304 + 1152 mB + 500 mB DES.
- Prerequisites you must already have (UV and UHV pages): draconic processing unit, draconic microchip processor, draconic processor, draconic processor assembly, abyssal processing unit, abyssal processor, QRAM chips (+ stellar RAM chips for the abyssal ones), hyper NAND and NOR memory chips, void foil, aerogel foil, qmd SMDs (draconic qmd transistor, resistor, capacitor, diode, inductor). Boards (circuits.js): draconic circuit board = 48 runic circuit boards + neutronium drum + UV pump + UV sensor + 2 ZPM circuits + 16 aurourium foil + 2000 mB dragon breath, circuit assembler, sterile cleanroom, VA\[UV\], 1200 ticks, 48 boards; abyssal circuit board = 64 draconic circuit boards + blank injection catalyst + UHV pump + UHV sensor + 2 UV circuits + 16 draco abyssal foil + 6000 mB draconic enrichment serum, VHA\[UEV\], 1200 ticks, 64 boards, in the Abyssal Containment Room (the printed-board step between them: Unverified). That room is a UXV-voltage Assembly Line recipe (start\_core:abyssal\_containment\_room: draco abyssal frame + 8 draco ware casings + 4 abyssal inductors + 12 UIV computational matrices + 2 UIV micropower routers + 8 UIV microfluidic flow valves + 64 fine rhenium super composite alloy wire + 4 UIV field generators + 224 UEPIC chips, 46 080 mB solder + 8640 mB PEDOT:PSS + 5760 mB perfluoroelastomer rubber, research abyssal inductor hull 224 CWU/t).
- Consumption: the draconic mainframe needs 2 draconic computers = 4 draconic assemblies = 8 draconic processors; with 2 UEPIC chips, 64 QRAM chips, 24 qmd SMDs per type and 1 energy module. The abyssal computer needs 2 abyssal assemblies = 4 abyssal processors, 24 stellar RAM chips and 32 draconyallium foil. The UEV circuits for the Hell Forge, Chiller and heat chambers (uev\_multis) are the first customers; UIV circuits go into the UIV hull-tier machines, fusion reactor (4 UIV circuits for UEV; 4 UXV for UIV), Ultimate EBF (8) and atomic materialization plant (12).
- Draco Circuit Assembler facts (verified): it is ONE multiblock with two recipe types (draco\_circuit\_assembler and draco\_bulk\_circuiter), not separate machines; Assembly Line VHA\[UIV\] = 15 728 640 EU/t. Its recipes carry no cleanroom requirement (the normal circuit assembler recipes ask for a cleanroom or sterile room), which is why it replaces the cleanroom circuit assemblers in UEV and UIV; the controller recipe burns 50 000 mB sterilized growth medium (SGM, uv\_bio2), and each ASG computational matrix 5000 mB. Parallel hatches: the UEV absolute parallel hatch asks for UIV circuits (4 + 2) and the UIV one for UXV circuits (abyssal mainframe). Draconic computer VA\[UHV\], mainframe VA\[UEV\] with 2 UEPIC chips.
- Sub-steps people skip: (1) research chain: the station research item of each recipe must be made and scanned in order (processor assembly → computer → mainframe); (2) the recipe EU/t is above a single UEV hatch for the mainframe: use laser target hatches or 4A/16A hatches; (3) abyssal circuits need the Abyssal Containment Room, not a plain cleanroom; (4) keep 2 drawers of draconic brain matter cells and a spare draconic eye for the abyssal mainframe (UXV, next era).
- **Unverified** the draconic board and unit recipes in detail (UV and UHV pages), the qmd SMD lines, hatch minimums of the Draco Circuit Assembler, and how the abyssal room attaches to the multiblock.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:draco_circuit_assembler` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uhv_input_bus` | 6 |
| `gtceu:uhv_input_hatch` | 4 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:draco_circuit_assembler`, `kubejs:draconic_processor_computer`, `kubejs:draconic_processor_mainframe`, `kubejs:abyssal_processor_assembly`, `kubejs:abyssal_processor_computer`, `kubejs:draco_ware_casing`
