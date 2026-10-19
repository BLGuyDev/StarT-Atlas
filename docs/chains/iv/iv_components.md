---
kind: chain
id: iv_components
order: 1110
data:
  t: |-
    IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers
  inf: true
  "n":
    - [ts, Tungsten steel ingot, i, "gtceu:tungsten_steel_ingot"]
    - [be, "LV Bender · circuit 1 · about 6 s · 24 EU/t", m, "gtceu:lv_bender"]
    - [pl, Tungsten steel plate, x, "gtceu:tungsten_steel_plate"]
    - [la, "LV Lathe · about 12 s · 16 EU/t", m, "gtceu:lv_lathe"]
    - [tr, Tungsten steel rod, x, "gtceu:tungsten_steel_rod"]
    - [as, "LV Alloy Smelter · small gear mold · 30 EU/t", m, "gtceu:lv_alloy_smelter"]
    - [sg, Small tungsten steel gear, x, "gtceu:small_tungsten_steel_gear"]
    - [nd, Neodymium magnetic rod, i, "gtceu:magnetic_neodymium_rod"]
    - [tc, "2 Tungsten double cable", i, "gtceu:tungsten_double_cable"]
    - [gw, "4 Graphene double wire", i, "gtceu:graphene_double_wire"]
    - [a1, "LV Assembler · 5 s · 30 EU/t (motor)", m, "gtceu:lv_assembler"]
    - [mo, IV Electric Motor, x, "gtceu:iv_electric_motor"]
    - [sc, Tungsten single cable, i, "gtceu:tungsten_single_cable"]
    - [a2, "LV Assembler (piston)", m, "gtceu:lv_assembler"]
    - [pi, IV Electric Piston, x, "gtceu:iv_electric_piston"]
    - - pp
      - Pump parts
      - g
      - functionalstorage:oak_1
      - - [Tungsten steel fluid pipe, "gtceu:tungsten_steel_normal_fluid_pipe"]
        - [Tungsten steel screw, "gtceu:tungsten_steel_screw"]
        - [Tungsten steel rotor, "gtceu:tungsten_steel_rotor"]
        - ["2 Silicone rubber rings", "gtceu:silicone_rubber_ring"]
    - [a3, "LV Assembler (pump)", m, "gtceu:lv_assembler"]
    - [pm, IV Electric Pump, o, "gtceu:iv_electric_pump"]
    - [sr, "864 mB silicone rubber (or SBR)", f, "gtceu:silicone_rubber_bucket"]
    - [a4, "LV Assembler · circuit 1 (conveyor)", m, "gtceu:lv_assembler"]
    - [cv, IV Conveyor Module, o, "gtceu:iv_conveyor_module"]
    - [ic, IV circuit, i, "gtceu:micro_processor_mainframe"]
    - [a5, "LV Assembler (robot arm)", m, "gtceu:lv_assembler"]
    - [ra, IV Robot Arm, o, "gtceu:iv_robot_arm"]
    - [ir, Iridium rod, i, "gtceu:iridium_rod"]
    - [qs, Quantum star, i, "gtceu:quantum_star"]
    - [a6, "LV Assembler · circuit 1 (emitter)", m, "gtceu:lv_assembler"]
    - [em, IV Emitter, o, "gtceu:iv_emitter"]
    - [a7, "LV Assembler (sensor)", m, "gtceu:lv_assembler"]
    - [se, IV Sensor, o, "gtceu:iv_sensor"]
    - [a8, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, IV Machine Casing, x, "gtceu:iv_machine_casing"]
    - [pt, "2 Platinum single cable", i, "gtceu:platinum_single_cable"]
    - [pf, "288 mB PTFE", f, "gtceu:polytetrafluoroethylene_bucket"]
    - [a9, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, IV Machine Hull, o, "gtceu:iv_machine_hull"]
  e:
    - [ts, be, "1"]
    - [be, pl, "1 / about 6 s"]
    - [ts, la, "1"]
    - [la, tr, "1 → 2"]
    - [ts, as, "2"]
    - [as, sg, "1"]
    - [tr, a1, "2"]
    - [nd, a1, "1"]
    - [tc, a1, "2"]
    - [gw, a1, "4"]
    - [a1, mo, "1 / 5 s"]
    - [mo, a2, "1"]
    - [pl, a2, "3"]
    - [tr, a2, "2"]
    - [sg, a2, "1"]
    - [sc, a2, "2"]
    - [a2, pi, "1 / 5 s"]
    - [mo, a3, "1"]
    - [pp, a3]
    - [sc, a3, "1"]
    - [a3, pm, "1 / 5 s"]
    - [mo, a4, "2"]
    - [sr, a4, "864 mB"]
    - [sc, a4, "1"]
    - [a4, cv, "1 / 5 s"]
    - [mo, a5, "2"]
    - [pi, a5, "1"]
    - [tr, a5, "2"]
    - [sc, a5, "3"]
    - [ic, a5, "1"]
    - [a5, ra, "1 / 5 s"]
    - [ir, a6, "4"]
    - [sc, a6, "2"]
    - [ic, a6, "2"]
    - [qs, a6, "1"]
    - [a6, em, "1 / 5 s"]
    - [ir, a7, "1"]
    - [pl, a7, "4"]
    - [ic, a7, "1"]
    - [qs, a7, "1"]
    - [a7, se, "1 / 5 s"]
    - [pl, a8, "8"]
    - [a8, mc, "1"]
    - [mc, a9, "1"]
    - [pt, a9, "2"]
    - [pf, a9, "288 mB"]
    - [a9, hu, "1"]
  tips:
    - |-
      Every IV component recipe in this fork is an assembler recipe of 100 ticks at VA[LV] = 30 EU/t (ComponentRecipes). An LV Assembler runs all of them: no IV power, no cleanroom. The tier is only in the inputs. You still need the IV circuits and the tungsten steel line first.
    - |-
      The new problem at IV is cables. Tungsten and platinum cables are IV rated, so plain rubber no longer works. WireRecipeHandler: 1 wire (single or double) + 1 PVC foil + 72 mB silicone rubber, or 36 mB styrene butadiene rubber (SBR), in an assembler, 5 s at 7 EU/t. The IV conveyor and pump recipes also exist only for silicone rubber and SBR (ComponentRecipes skips plain Rubber for IV). Nothing in the pack scripts changes these recipes.
    - |-
      Motors needed: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3. An IV Assembler = 2 arms + 2 conveyors = 10 motors, plus 2 IV circuits in the recipe and 2 in the arms (4 in all), a hull and 2 platinum cables (gt_machine_recipes). Build the motor line first and biggest: 12 a minute per assembler.
    - |-
      Raw cost per motor: 2 tungsten ingots (the double cables), 1 tungsten steel ingot (2 rods), 1 magnetic neodymium rod and 4 graphene ingots (4 double wires). Graphene dust is made in the HV Mixer: 1 graphite + 1 silicon + 4 carbon dust, circuit 1, 100 ticks, 480 EU/t (MixerRecipes), so one motor eats 4 graphite, 4 silicon and 16 carbon dust. Carbon dust: 1 coal dust → 2 carbon in a centrifuge (36 ticks, 30 EU/t). Graphite is a by-product of the Electric Ore Factory on coal and diamond ore (kjs ore_factory_processing.js).
    - |-
      Piston: 6 tungsten steel ingots (3 plates, 1 for the 2 rods, 2 for the small gear) + 1 tungsten ingot (2 single wires) + the motor. Robot arm: 3 single cables + 2 rods + 2 motors + 1 piston + 1 IV circuit. Pump: 1 single cable + fluid pipe (3 ingots) + screw + rotor (4 ingots) + 2 silicone rings + 1 motor.
    - |-
      Pipe and rotor in an extruder (PartsRecipeHandler, PipeRecipeHandler): tungsten steel is 3000 K, so both use the hard-metal power: rotor 4 ingots, 256 EU/t, mass x 4 ticks; normal pipe 3 ingots, 180 EU/t, mass x 3 ticks. Both are above the MV 120 EU/t limit, so they need an HV Extruder. The small gear in the extruder is also 256 EU/t; the LV Alloy Smelter route (2 ingots + gear mold, 30 EU/t) avoids that.
    - |-
      Emitter and sensor need a Quantum Star where the HV ones took an ender eye: 1 nether star + 1250 mB radon in the HV Chemical Bath, 1920 ticks (96 s) at 480 EU/t (CircuitRecipes quantum_star). The star comes from the nether star loop in this era, the radon from the radon chain: an LCR with 8 plutonium-239 ingots (HV) or liquid ender air in a Vacuum Freezer and Distillation Tower (both IV, 7680 EU/t); see the ev_components tips. Emitter: 4 iridium rods + 2 tungsten single cables + 2 IV circuits + 1 star (ghost circuit 1). Sensor: 1 iridium rod + 4 tungsten steel plates + 1 IV circuit + 1 star.
    - |-
      Iridium rods are why this era needs RTM coils: iridium dust is an EBF recipe at 4500 K (ElementMaterials: VA[IV] = 7680 EU/t, 1100 ticks, gas tier argon) and RTM coils are exactly 4500 K (jar CoilType). The hot ingot needs the Vacuum Freezer (250 ticks = 12.5 s at 1920 EU/t, a freezer on an EV hatch), then a lathe makes 2 rods per ingot (about 19 s at 16 EU/t). See the rtm_coil chain and the platinum group chain.
    - |-
      IV Machine Hull: 8 tungsten steel plates → IV machine casing (ghost circuit 8, 50 ticks, 16 EU/t), then casing + 2 platinum single cables + 288 mB PTFE (pack recipe data). PTFE is the pack’s large chemical reactor line from HV; platinum cable also needs PVC foil and silicone rubber.
    - |-
      Field generator: recipe known (1 quantum star + 2 double tungsten steel plates + 2 IV circuits + 4 samarium iron arsenic oxide quadruple wire, 5 s at 30 EU/t), but no IV machine in this guide needs it. Only the IV World Accelerator, the LuV hull line and the battery recipes use it. Unverified: where the samarium iron arsenic oxide wire comes from, check EMI before you plan it.
    - |-
      Sub-steps people skip: (1) PVC foil in every cable, not only the rubber; (2) the screw is rod → bolt (cutter) → screw (lathe), three machines; (3) the neodymium rod must be the POLARIZED magnetic one; (4) emitters and conveyors need ghost circuit 1, the casing circuit 8, motor and piston none, so never share a machine; (5) graphene needs an ingot, not the dust, before the wiremill.
    - |-
      Unverified: the exact seconds of the tungsten steel parts (they are mass-based; the average component mass is assumed to be about 120, so about 6 s plate, 12 s rod, 6 s gear, 18 s pipe, 24 s rotor) and the PVC foil press time.
  b:
    - ["gtceu:lv_assembler", 11]
    - ["gtceu:lv_wiremill", 2]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_lathe", 3]
    - ["gtceu:lv_cutter", 1]
    - ["gtceu:lv_alloy_smelter", 1]
    - ["gtceu:lv_extruder", 1]
    - ["gtceu:hv_extruder", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:tungsten_steel_ingot", "gtceu:tungsten_ingot", "gtceu:graphene_dust"]
      t: |-
        Input drawers first, one per item: tungsten steel ingots, tungsten ingots, graphene dust (or ingots), iridium ingots, magnetic neodymium rods, PVC foil, platinum ingots, and IV circuits. A steel drum each for silicone rubber and for PTFE. From every drawer a Modular Router or Pipez item pipe with an Item Filter feeds exactly one machine; every output drawer gets a Robot Arm cover in Keep Exact mode so one hungry assembler cannot drain the rest.
    - i: ["gtceu:lv_bender", "gtceu:tungsten_steel_plate", "gtceu:lv_lathe", "gtceu:tungsten_steel_rod"]
      t: |-
        Tungsten steel parts, one machine each. Bender with ghost circuit 1: 1 ingot → 1 plate (24 EU/t). Lathe: 1 ingot → 2 rods (16 EU/t, about 12 s; harder rods are off in this pack). Alloy Smelter with the small gear mold: 2 ingots → 1 small gear (30 EU/t, so an LV machine; the extruder version needs 256 EU/t, an HV extruder). Never put two molds or two circuits in one machine.
    - i:
        - gtceu:lv_wiremill
        - gtceu:tungsten_double_cable
        - gtceu:tungsten_single_cable
        - gtceu:polyvinyl_chloride_foil
      t: |-
        Tungsten wire and cable. LV Wiremill circuit 1: 1 tungsten ingot → 2 single wires; a second wiremill on circuit 2: 1 ingot → 1 double wire (30 EU/t because tungsten is 3600 K, so LV is enough). Then two cable assemblers: wire + 1 PVC foil + 72 mB silicone rubber → cable, 5 s at 7 EU/t. One assembler per wire type, each with a PVC foil drawer and a fluid hatch from the rubber drum.
    - i: ["gtceu:graphene_dust", "gtceu:graphene_double_wire", "gtceu:hv_mixer"]
      t: |-
        Graphene for the motors. HV Mixer circuit 1: 1 graphite + 1 silicon + 4 carbon dust → 1 graphene dust (5 s, 480 EU/t). Furnace the dust into an ingot, then LV Wiremill circuit 2 → 1 double wire. Keep a carbon drawer fed by a centrifuge on coal dust and a graphite drawer from the ore factory; the mixer stalls silently when one of the three is empty.
    - i: ["gtceu:lv_assembler", "gtceu:iv_electric_motor", "gtceu:magnetic_neodymium_rod"]
      t: |-
        Motor assembler (own LV Assembler): 2 tungsten double cables + 2 tungsten steel rods + 1 magnetic neodymium rod + 4 graphene double wires in its input bus, 5 s at 30 EU/t. Cap its output drawer at 32 with a Keep Exact arm: pistons, pumps, conveyors and arms all pull from it, and it is the first machine to build.
    - i: ["gtceu:lv_assembler", "gtceu:iv_electric_piston", "gtceu:small_tungsten_steel_gear"]
      t: |-
        Piston assembler: 1 motor + 3 tungsten steel plates + 2 rods + 2 tungsten single cables + 1 small tungsten steel gear → 1 piston, 5 s. Plates, rods and gear arrive through three separate Item Filters, never one unfiltered pipe.
    - i:
        - gtceu:hv_extruder
        - gtceu:tungsten_steel_rotor
        - gtceu:tungsten_steel_normal_fluid_pipe
        - gtceu:tungsten_steel_screw
      t: |-
        Pump parts. HV Extruder with the rotor shape: 4 ingots → 1 rotor (256 EU/t); with the normal pipe shape: 3 ingots → 1 pipe (180 EU/t). Screw: LV Cutter rod → 4 bolts, then LV Lathe bolt → screw. LV Extruder with the ring shape: 1 silicone rubber ingot → 4 rings (24 EU/t). Each shape sits alone in its own extruder bus, and the shape never leaves the bus slot.
    - i: ["gtceu:lv_assembler", "gtceu:iv_electric_pump", "gtceu:iv_conveyor_module", "gtceu:silicone_rubber_bucket"]
      t: |-
        Pump assembler: 1 motor + 1 tungsten single cable + 1 pipe + 1 screw + 1 rotor + 2 silicone rubber rings → 1 pump, 5 s. Conveyor assembler on ghost circuit 1: 1 tungsten single cable + 2 motors + 864 mB silicone rubber (or SBR) → 1 conveyor, 5 s. The conveyor’s fluid goes in through a hatch; keep its drum separate from the cable assemblers’ drum so one empty tank does not stall both.
    - i: ["gtceu:lv_assembler", "gtceu:iv_robot_arm", "gtceu:micro_processor_mainframe"]
      t: |-
        Robot arm assembler: 3 tungsten single cables + 2 rods + 2 motors + 1 piston + 1 IV circuit → 1 arm, 5 s. The IV circuit is the scarce input (the first IV circuit is the Microprocessor Mainframe, see the IV circuits chain); stock 8 in its own drawer before you start arms, emitters and sensors.
    - i: ["gtceu:lv_assembler", "gtceu:iv_emitter", "gtceu:iv_sensor", "gtceu:quantum_star"]
      t: |-
        Emitter (ghost circuit 1): 4 iridium rods + 2 tungsten single cables + 2 IV circuits + 1 quantum star → 1 emitter. Sensor: 1 iridium rod + 4 tungsten steel plates + 1 IV circuit + 1 quantum star → 1 sensor. Both 5 s. Keep a quantum star drawer capped at 4 and never share it with another machine; a star is 96 s of chemical bath and a whole nether star.
    - i: ["gtceu:iv_machine_casing", "gtceu:iv_machine_hull", "gtceu:platinum_single_cable"]
      t: |-
        Hull line: assembler with ghost circuit 8, 8 tungsten steel plates → 1 IV machine casing (2.5 s at 16 EU/t). A second assembler: casing + 2 platinum single cables + 288 mB PTFE → IV Machine Hull (2.5 s at 16 EU/t). Hulls go straight into storage; every IV single machine and hatch uses one.
    - i: ["gtceu:iv_assembler", "gtceu:iv_robot_arm", "gtceu:iv_conveyor_module"]
      t: |-
        Easy to miss: the IV Assembler is the first big use of this line (2 arms, 2 conveyors, 2 circuits, hull, 2 platinum cables), and the pack quest says it makes the higher coils and the energy hatches. Craft the first set by hand and keep the line for every IV single machine (most need 1 pump or 2 pistons or 1 to 4 motors).
---
# IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `iv_components` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [IV components, RTM coil, Shellite](../../plan/p10.md#ivmach)

**Tips:** 12, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1 · about 6 s · 24 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten steel ingot (gtceu:tungsten_steel_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Tungsten steel plate (gtceu:tungsten_steel_plate) - 1 / about 6 s"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Plate</span><b class="gt-q">1 / about 6 s</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-la">
<div class="gt-head"><span class="gt-mname">LV Lathe · about 12 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten steel ingot (gtceu:tungsten_steel_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Tungsten steel rod (gtceu:tungsten_steel_rod) - 1 → 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Rod</span><b class="gt-q">1 → 2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">LV Alloy Smelter · small gear mold · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten steel ingot (gtceu:tungsten_steel_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Ingot</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_alloy_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Small tungsten steel gear (gtceu:small_tungsten_steel_gear) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__small_tungsten_steel_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Tungsten Steel Gear</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_alloy_smelter</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 30 EU/t (motor)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten steel rod (gtceu:tungsten_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="Neodymium magnetic rod (gtceu:magnetic_neodymium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_neodymium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Neodymium Rod</span><span class="gt-note">Neodymium magnetic rod</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Tungsten double cable (gtceu:tungsten_double_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_double_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Double Cable</span><span class="gt-note">2 Tungsten double cable</span><b class="gt-q">2</b></span><span class="gt-slot" title="4 Graphene double wire (gtceu:graphene_double_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__graphene_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Graphene Double Wire</span><span class="gt-note">4 Graphene double wire</span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="IV Electric Motor (gtceu:iv_electric_motor) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler (piston)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Electric Motor (gtceu:iv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot" title="Tungsten steel plate (gtceu:tungsten_steel_plate) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Plate</span><b class="gt-q">3</b></span><span class="gt-slot" title="Tungsten steel rod (gtceu:tungsten_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="Small tungsten steel gear (gtceu:small_tungsten_steel_gear) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__small_tungsten_steel_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Tungsten Steel Gear</span><b class="gt-q">1</b></span><span class="gt-slot" title="Tungsten single cable (gtceu:tungsten_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="IV Electric Piston (gtceu:iv_electric_piston) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler (pump)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Electric Motor (gtceu:iv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Pump parts (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Pump parts</span><span class="gt-sub"><span>Tungsten steel fluid pipe</span><span>Tungsten steel screw</span><span>Tungsten steel rotor</span><span>2 Silicone rubber rings</span></span></span><span class="gt-slot" title="Tungsten single cable (gtceu:tungsten_single_cable) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Electric Pump (gtceu:iv_electric_pump) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Pump</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a4">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 1 (conveyor)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Electric Motor (gtceu:iv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="864 mB silicone rubber (or SBR) (gtceu:silicone_rubber_bucket) - 864 mB"><img class="gt-ico" src="../../assets/icons/gtceu__silicone_rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicone Rubber</span><span class="gt-note">864 mB silicone rubber (or SBR)</span><b class="gt-q">864 mB</b></span><span class="gt-slot" title="Tungsten single cable (gtceu:tungsten_single_cable) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Conveyor Module (gtceu:iv_conveyor_module) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Conveyor Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a5">
<div class="gt-head"><span class="gt-mname">LV Assembler (robot arm)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Electric Motor (gtceu:iv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot" title="IV Electric Piston (gtceu:iv_electric_piston) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electric Piston</span><b class="gt-q">1</b></span><span class="gt-slot" title="Tungsten steel rod (gtceu:tungsten_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="Tungsten single cable (gtceu:tungsten_single_cable) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><b class="gt-q">3</b></span><span class="gt-slot" title="IV circuit (gtceu:micro_processor_mainframe) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Mainframe</span><span class="gt-note">IV circuit</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Robot Arm (gtceu:iv_robot_arm) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a6">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 1 (emitter)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iridium rod (gtceu:iridium_rod) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Rod</span><b class="gt-q">4</b></span><span class="gt-slot" title="Tungsten single cable (gtceu:tungsten_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><b class="gt-q">2</b></span><span class="gt-slot" title="IV circuit (gtceu:micro_processor_mainframe) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Mainframe</span><span class="gt-note">IV circuit</span><b class="gt-q">2</b></span><span class="gt-slot" title="Quantum star (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Emitter (gtceu:iv_emitter) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Emitter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a7">
<div class="gt-head"><span class="gt-mname">LV Assembler (sensor)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iridium rod (gtceu:iridium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Rod</span><b class="gt-q">1</b></span><span class="gt-slot" title="Tungsten steel plate (gtceu:tungsten_steel_plate) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Plate</span><b class="gt-q">4</b></span><span class="gt-slot" title="IV circuit (gtceu:micro_processor_mainframe) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Mainframe</span><span class="gt-note">IV circuit</span><b class="gt-q">1</b></span><span class="gt-slot" title="Quantum star (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Sensor (gtceu:iv_sensor) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a8">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten steel plate (gtceu:tungsten_steel_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="IV Machine Casing (gtceu:iv_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a9">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Machine Casing (gtceu:iv_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Platinum single cable (gtceu:platinum_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Single Cable</span><span class="gt-note">2 Platinum single cable</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PTFE (gtceu:polytetrafluoroethylene_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polytetrafluoroethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polytetrafluoroethylene</span><span class="gt-note">288 mB PTFE</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Machine Hull (gtceu:iv_machine_hull) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1 · about 6 s · 24 EU/t](#m-be) → [LV Assembler (piston)](#m-a2) → [LV Assembler (robot arm)](#m-a5) (also LV Bender · circuit 1 · about 6 s · 24 EU/t → [LV Assembler (sensor)](#m-a7), LV Bender · circuit 1 · about 6 s · 24 EU/t → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a8))
- [LV Lathe · about 12 s · 16 EU/t](#m-la) → [LV Assembler · 5 s · 30 EU/t (motor)](#m-a1) → [LV Assembler (pump)](#m-a3) (also LV Lathe · about 12 s · 16 EU/t → [LV Assembler (piston)](#m-a2), LV Lathe · about 12 s · 16 EU/t → [LV Assembler (robot arm)](#m-a5), LV Assembler · 5 s · 30 EU/t (motor) → [LV Assembler (piston)](#m-a2), LV Assembler · 5 s · 30 EU/t (motor) → [LV Assembler · circuit 1 (conveyor)](#m-a4), LV Assembler · 5 s · 30 EU/t (motor) → [LV Assembler (robot arm)](#m-a5))
- [LV Alloy Smelter · small gear mold · 30 EU/t](#m-as) → [LV Assembler (piston)](#m-a2)
- [LV Assembler · circuit 1 (emitter)](#m-a6)
- [LV Assembler · circuit 1 (conveyor)](#m-a4)
- [LV Assembler (sensor)](#m-a7)
- [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a8) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a9)

## How to build

1. Input drawers first, one per item: tungsten steel ingots, tungsten ingots, graphene dust (or ingots), iridium ingots, magnetic neodymium rods, PVC foil, platinum ingots, and IV circuits. A steel drum each for silicone rubber and for PTFE. From every drawer a Modular Router or Pipez item pipe with an Item Filter feeds exactly one machine; every output drawer gets a Robot Arm cover in Keep Exact mode so one hungry assembler cannot drain the rest. — `functionalstorage:oak_1`, `gtceu:tungsten_steel_ingot`, `gtceu:tungsten_ingot`, `gtceu:graphene_dust`
2. Tungsten steel parts, one machine each. Bender with ghost circuit 1: 1 ingot → 1 plate (24 EU/t). Lathe: 1 ingot → 2 rods (16 EU/t, about 12 s; harder rods are off in this pack). Alloy Smelter with the small gear mold: 2 ingots → 1 small gear (30 EU/t, so an LV machine; the extruder version needs 256 EU/t, an HV extruder). Never put two molds or two circuits in one machine. — `gtceu:lv_bender`, `gtceu:tungsten_steel_plate`, `gtceu:lv_lathe`, `gtceu:tungsten_steel_rod`
3. Tungsten wire and cable. LV Wiremill circuit 1: 1 tungsten ingot → 2 single wires; a second wiremill on circuit 2: 1 ingot → 1 double wire (30 EU/t because tungsten is 3600 K, so LV is enough). Then two cable assemblers: wire + 1 PVC foil + 72 mB silicone rubber → cable, 5 s at 7 EU/t. One assembler per wire type, each with a PVC foil drawer and a fluid hatch from the rubber drum. — `gtceu:lv_wiremill`, `gtceu:tungsten_double_cable`, `gtceu:tungsten_single_cable`, `gtceu:polyvinyl_chloride_foil`
4. Graphene for the motors. HV Mixer circuit 1: 1 graphite + 1 silicon + 4 carbon dust → 1 graphene dust (5 s, 480 EU/t). Furnace the dust into an ingot, then LV Wiremill circuit 2 → 1 double wire. Keep a carbon drawer fed by a centrifuge on coal dust and a graphite drawer from the ore factory; the mixer stalls silently when one of the three is empty. — `gtceu:graphene_dust`, `gtceu:graphene_double_wire`, `gtceu:hv_mixer`
5. Motor assembler (own LV Assembler): 2 tungsten double cables + 2 tungsten steel rods + 1 magnetic neodymium rod + 4 graphene double wires in its input bus, 5 s at 30 EU/t. Cap its output drawer at 32 with a Keep Exact arm: pistons, pumps, conveyors and arms all pull from it, and it is the first machine to build. — `gtceu:lv_assembler`, `gtceu:iv_electric_motor`, `gtceu:magnetic_neodymium_rod`
6. Piston assembler: 1 motor + 3 tungsten steel plates + 2 rods + 2 tungsten single cables + 1 small tungsten steel gear → 1 piston, 5 s. Plates, rods and gear arrive through three separate Item Filters, never one unfiltered pipe. — `gtceu:lv_assembler`, `gtceu:iv_electric_piston`, `gtceu:small_tungsten_steel_gear`
7. Pump parts. HV Extruder with the rotor shape: 4 ingots → 1 rotor (256 EU/t); with the normal pipe shape: 3 ingots → 1 pipe (180 EU/t). Screw: LV Cutter rod → 4 bolts, then LV Lathe bolt → screw. LV Extruder with the ring shape: 1 silicone rubber ingot → 4 rings (24 EU/t). Each shape sits alone in its own extruder bus, and the shape never leaves the bus slot. — `gtceu:hv_extruder`, `gtceu:tungsten_steel_rotor`, `gtceu:tungsten_steel_normal_fluid_pipe`, `gtceu:tungsten_steel_screw`
8. Pump assembler: 1 motor + 1 tungsten single cable + 1 pipe + 1 screw + 1 rotor + 2 silicone rubber rings → 1 pump, 5 s. Conveyor assembler on ghost circuit 1: 1 tungsten single cable + 2 motors + 864 mB silicone rubber (or SBR) → 1 conveyor, 5 s. The conveyor’s fluid goes in through a hatch; keep its drum separate from the cable assemblers’ drum so one empty tank does not stall both. — `gtceu:lv_assembler`, `gtceu:iv_electric_pump`, `gtceu:iv_conveyor_module`, `gtceu:silicone_rubber_bucket`
9. Robot arm assembler: 3 tungsten single cables + 2 rods + 2 motors + 1 piston + 1 IV circuit → 1 arm, 5 s. The IV circuit is the scarce input (the first IV circuit is the Microprocessor Mainframe, see the IV circuits chain); stock 8 in its own drawer before you start arms, emitters and sensors. — `gtceu:lv_assembler`, `gtceu:iv_robot_arm`, `gtceu:micro_processor_mainframe`
10. Emitter (ghost circuit 1): 4 iridium rods + 2 tungsten single cables + 2 IV circuits + 1 quantum star → 1 emitter. Sensor: 1 iridium rod + 4 tungsten steel plates + 1 IV circuit + 1 quantum star → 1 sensor. Both 5 s. Keep a quantum star drawer capped at 4 and never share it with another machine; a star is 96 s of chemical bath and a whole nether star. — `gtceu:lv_assembler`, `gtceu:iv_emitter`, `gtceu:iv_sensor`, `gtceu:quantum_star`
11. Hull line: assembler with ghost circuit 8, 8 tungsten steel plates → 1 IV machine casing (2.5 s at 16 EU/t). A second assembler: casing + 2 platinum single cables + 288 mB PTFE → IV Machine Hull (2.5 s at 16 EU/t). Hulls go straight into storage; every IV single machine and hatch uses one. — `gtceu:iv_machine_casing`, `gtceu:iv_machine_hull`, `gtceu:platinum_single_cable`
12. Easy to miss: the IV Assembler is the first big use of this line (2 arms, 2 conveyors, 2 circuits, hull, 2 platinum cables), and the pack quest says it makes the higher coils and the energy hatches. Craft the first set by hand and keep the line for every IV single machine (most need 1 pump or 2 pistons or 1 to 4 motors). — `gtceu:iv_assembler`, `gtceu:iv_robot_arm`, `gtceu:iv_conveyor_module`

## Tips

- Every IV component recipe in this fork is an assembler recipe of 100 ticks at VA\[LV\] = 30 EU/t (ComponentRecipes). An LV Assembler runs all of them: no IV power, no cleanroom. The tier is only in the inputs. You still need the IV circuits and the tungsten steel line first.
- The new problem at IV is cables. Tungsten and platinum cables are IV rated, so plain rubber no longer works. WireRecipeHandler: 1 wire (single or double) + 1 PVC foil + 72 mB silicone rubber, or 36 mB styrene butadiene rubber (SBR), in an assembler, 5 s at 7 EU/t. The IV conveyor and pump recipes also exist only for silicone rubber and SBR (ComponentRecipes skips plain Rubber for IV). Nothing in the pack scripts changes these recipes.
- Motors needed: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3. An IV Assembler = 2 arms + 2 conveyors = 10 motors, plus 2 IV circuits in the recipe and 2 in the arms (4 in all), a hull and 2 platinum cables (gt\_machine\_recipes). Build the motor line first and biggest: 12 a minute per assembler.
- Raw cost per motor: 2 tungsten ingots (the double cables), 1 tungsten steel ingot (2 rods), 1 magnetic neodymium rod and 4 graphene ingots (4 double wires). Graphene dust is made in the HV Mixer: 1 graphite + 1 silicon + 4 carbon dust, circuit 1, 100 ticks, 480 EU/t (MixerRecipes), so one motor eats 4 graphite, 4 silicon and 16 carbon dust. Carbon dust: 1 coal dust → 2 carbon in a centrifuge (36 ticks, 30 EU/t). Graphite is a by-product of the Electric Ore Factory on coal and diamond ore (kjs ore\_factory\_processing.js).
- Piston: 6 tungsten steel ingots (3 plates, 1 for the 2 rods, 2 for the small gear) + 1 tungsten ingot (2 single wires) + the motor. Robot arm: 3 single cables + 2 rods + 2 motors + 1 piston + 1 IV circuit. Pump: 1 single cable + fluid pipe (3 ingots) + screw + rotor (4 ingots) + 2 silicone rings + 1 motor.
- Pipe and rotor in an extruder (PartsRecipeHandler, PipeRecipeHandler): tungsten steel is 3000 K, so both use the hard-metal power: rotor 4 ingots, 256 EU/t, mass x 4 ticks; normal pipe 3 ingots, 180 EU/t, mass x 3 ticks. Both are above the MV 120 EU/t limit, so they need an HV Extruder. The small gear in the extruder is also 256 EU/t; the LV Alloy Smelter route (2 ingots + gear mold, 30 EU/t) avoids that.
- Emitter and sensor need a Quantum Star where the HV ones took an ender eye: 1 nether star + 1250 mB radon in the HV Chemical Bath, 1920 ticks (96 s) at 480 EU/t (CircuitRecipes quantum\_star). The star comes from the nether star loop in this era, the radon from the radon chain: an LCR with 8 plutonium-239 ingots (HV) or liquid ender air in a Vacuum Freezer and Distillation Tower (both IV, 7680 EU/t); see the ev\_components tips. Emitter: 4 iridium rods + 2 tungsten single cables + 2 IV circuits + 1 star (ghost circuit 1). Sensor: 1 iridium rod + 4 tungsten steel plates + 1 IV circuit + 1 star.
- Iridium rods are why this era needs RTM coils: iridium dust is an EBF recipe at 4500 K (ElementMaterials: VA\[IV\] = 7680 EU/t, 1100 ticks, gas tier argon) and RTM coils are exactly 4500 K (jar CoilType). The hot ingot needs the Vacuum Freezer (250 ticks = 12.5 s at 1920 EU/t, a freezer on an EV hatch), then a lathe makes 2 rods per ingot (about 19 s at 16 EU/t). See the rtm\_coil chain and the platinum group chain.
- IV Machine Hull: 8 tungsten steel plates → IV machine casing (ghost circuit 8, 50 ticks, 16 EU/t), then casing + 2 platinum single cables + 288 mB PTFE (pack recipe data). PTFE is the pack’s large chemical reactor line from HV; platinum cable also needs PVC foil and silicone rubber.
- Field generator: recipe known (1 quantum star + 2 double tungsten steel plates + 2 IV circuits + 4 samarium iron arsenic oxide quadruple wire, 5 s at 30 EU/t), but no IV machine in this guide needs it. Only the IV World Accelerator, the LuV hull line and the battery recipes use it. Unverified: where the samarium iron arsenic oxide wire comes from, check EMI before you plan it.
- Sub-steps people skip: (1) PVC foil in every cable, not only the rubber; (2) the screw is rod → bolt (cutter) → screw (lathe), three machines; (3) the neodymium rod must be the POLARIZED magnetic one; (4) emitters and conveyors need ghost circuit 1, the casing circuit 8, motor and piston none, so never share a machine; (5) graphene needs an ingot, not the dust, before the wiremill.
- **Unverified** the exact seconds of the tungsten steel parts (they are mass-based; the average component mass is assumed to be about 120, so about 6 s plate, 12 s rod, 6 s gear, 18 s pipe, 24 s rotor) and the PVC foil press time.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 11 |
| `gtceu:lv_wiremill` | 2 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_lathe` | 3 |
| `gtceu:lv_cutter` | 1 |
| `gtceu:lv_alloy_smelter` | 1 |
| `gtceu:lv_extruder` | 1 |
| `gtceu:hv_extruder` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](iv_circuits.md)
- **Feeds:** [IV Energy and Dynamo Hatch: phosphorus wafer → MPIC wafer → HPIC wafer → 2 HPIC chips, IV voltage coil, IV Assembler](iv_hatches.md), [Shellite: signalum + black bronze → EV Mixer → EBF 4400 K (RTM coils, IV hatch) → wire → IV converters](shellite_line.md), [Assembly Line: scan the IV part on a data stick, put it in a Data Access Hatch, one ULV bus per ingredient, IV energy hatch](../luv/luv_assembly_line.md), [LuV components 2: robot arm, emitter, sensor, field generator (Assembly Line, 30 s, 7680 EU/t, LuV circuits, quantum stars, rhodium foil)](../luv/luv_components2.md), [Combo: Extreme Chemical Reactor with a parallel hatch](../combos/combo_ecr.md)
- **Main source for:** `gtceu:iv_electric_motor`, `gtceu:iv_electric_piston`, `gtceu:iv_electric_pump`, `gtceu:iv_conveyor_module`, `gtceu:iv_robot_arm`, `gtceu:iv_emitter`, `gtceu:iv_sensor`, `gtceu:iv_machine_hull`, `gtceu:iv_machine_casing`, `gtceu:tungsten_steel_plate`, `gtceu:tungsten_steel_rod`, `gtceu:small_tungsten_steel_gear`, `gtceu:tungsten_single_cable`, `gtceu:tungsten_double_cable`, `gtceu:graphene_double_wire`, `gtceu:quantum_star`
