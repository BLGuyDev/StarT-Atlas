---
kind: chain
id: ev_components
order: 1100
data:
  t: |-
    EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull
  inf: true
  "n":
    - [ti, Titanium ingot, i, "gtceu:titanium_ingot"]
    - [be, LV Bender, m, "gtceu:lv_bender"]
    - [pl, Titanium plate, x, "gtceu:titanium_plate"]
    - [la, "LV Lathe · 1 → 2", m, "gtceu:lv_lathe"]
    - [tr, Titanium rod, x, "gtceu:titanium_rod"]
    - [ex, "MV Extruder · small gear shape", m, "gtceu:mv_extruder"]
    - [sg, Titanium small gear, x, "gtceu:small_titanium_gear"]
    - [nd, "Neodymium rod (polarized)", i, "gtceu:magnetic_neodymium_rod"]
    - [kw, "4 Kanthal double wire", i, "gtceu:kanthal_double_wire"]
    - [ac, "2 Aluminium double cable", i, "gtceu:aluminium_double_cable"]
    - [am, "LV Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [mo, EV Electric Motor, x, "gtceu:ev_electric_motor"]
    - [ap, "LV Assembler · 5 s", m, "gtceu:lv_assembler"]
    - [pi, EV Electric Piston, x, "gtceu:ev_electric_piston"]
    - [ec, "EV circuit (#gtceu:circuits/ev)", i, "gtceu:micro_processor_computer"]
    - [ar, "LV Assembler · 5 s", m, "gtceu:lv_assembler"]
    - [ra, EV Robot Arm, o, "gtceu:ev_robot_arm"]
    - [ah, "LV Assembler · circuit 8 · 2.5 s", m, "gtceu:lv_assembler"]
    - [mc, EV Machine Casing, x, "gtceu:ev_machine_casing"]
    - [hu, EV Machine Hull, o, "gtceu:ev_machine_hull"]
  e:
    - [ti, be, "1"]
    - [be, pl, "1"]
    - [ti, la, "1"]
    - [la, tr, "2"]
    - [ti, ex, "1"]
    - [ex, sg, "1 / 2.4 s"]
    - [tr, am, "2"]
    - [nd, am, "1"]
    - [kw, am, "4"]
    - [ac, am, "2"]
    - [am, mo, "1 / 5 s"]
    - [mo, ap, "1"]
    - [tr, ap, "2"]
    - [pl, ap, "3"]
    - [sg, ap, "1"]
    - [ap, pi, "1 / 5 s"]
    - [pi, ar, "1"]
    - [mo, ar, "2"]
    - [tr, ar, "2"]
    - [ec, ar, "1"]
    - [ar, ra, "1 / 5 s"]
    - [pl, ah, "8"]
    - [ah, mc, "1"]
    - [mc, hu, "+ 2 cable"]
  tips:
    - |-
      EV Electric Motor (assembler 100 ticks, 30 EU/t, LV machine is enough): 2 aluminium double cable + 2 titanium rod + 1 magnetic neodymium rod + 4 kanthal double wire. Piston: 2 titanium rod + 2 aluminium cable + 3 titanium plate + 1 small titanium gear + 1 motor. Robot arm: 3 aluminium cable + 2 titanium rod + 2 motors + 1 piston + 1 EV circuit. All source: ComponentRecipes (not changed by the pack scripts).
    - |-
      EV Electric Pump: 1 aluminium cable + 1 titanium normal fluid pipe + 1 stainless steel screw + 1 stainless steel rotor + 2 rubber rings + 1 motor. EV Conveyor Module: 1 aluminium cable + 2 motors + 864 mB molten rubber, ghost circuit 1. Both 100 ticks at 30 EU/t. The pipe is 3 titanium ingots in an extruder (HV pipe recipe from the previous era, same pattern).
    - |-
      Count the titanium: motor 1 ingot (the rods), piston 6, robot arm 9, pump 4, conveyor 2, hull 8 plates. A full set of EV single machines eats dozens of ingots, so the titanium line (about 1 ingot per 10 B of molten ore mixture) sets the pace of this whole era.
    - |-
      Magnetic neodymium rod: neodymium dust → EBF 1297 K (neodymium blast, MV default 120 EU/t, mass 144 x 1297 / 50 is about 3735 ticks, 3 min, derived) → lathe → rod → Polarizer → magnetic rod. Neodymium dust comes from bastnasite: the same Distillation Tower run as titanium gives 1 B molten bastnasite (2 raw bastnasite), and the EV tier of the Electric Ore Factory gives neodymium 25 % + 12.5 % per crushed bastnasite (ore_factory_processing.js).
    - |-
      Emitter and Sensor at EV need a Quantum Eye instead of an ender eye: HV Chemical Bath, 1 ender eye + 250 mB radon → 1 quantum eye in 24 s (480 EU/t). Emitter: 4 platinum rods + 2 aluminium cables + 2 EV circuits + 1 quantum eye (ghost circuit 1). Sensor: 1 platinum rod + 4 titanium plates + 1 EV circuit + 1 quantum eye. Radon is the catch: there is no cheap source. The only routes are an LCR with 8 plutonium-239 ingots + 1 uranium-238 dust + 10 B air (HV, 480 EU/t, 4000 ticks, 1 B radon; the plutonium comes from the uranium-238 centrifuge) or liquid ender air in a Vacuum Freezer plus the Distillation Tower (both IV, 7680 EU/t, 200 B liquid ender air per 1 B radon). So the EV emitter and sensor, and the EV circuit assembler that carries an EV emitter, need the plutonium route or wait for IV. A Field Generator needs a nether star and uranium triplatinum wire: not an EV target.
    - |-
      Platinum is an EV material, not an IV one: besides the emitter (4 rods) and sensor (1 rod) it is the cable of the EV transformers (hence the 4A and 16A EV hatches), the fine platinum wire of the SMD diodes for the nano line and the cable of the IV hull. Platinum and palladium need only the HV centrifuge and MV electrolysis, rhodium and ruthenium an EV Chemical Reactor (1920 EU/t), and only iridium and osmium need IV (platinum group chain).
    - |-
      EV Machine Hull: 8 titanium plates → EV machine casing (assembler, ghost circuit 8, 50 ticks at 16 EU/t), then casing + 2 aluminium cables + 288 mB polyethylene → hull (50 ticks, 16 EU/t). Source: extract/recipes.json.
    - |-
      EV cables: aluminium is an EV rated cable, so WireRecipeHandler adds 1 PVC foil per single or double cable (2 per quadruple) on top of the insulation: assembler, wire + 1 PVC foil + 144 mB rubber, or + 72 mB silicone rubber, or + 36 mB SBR, 100 ticks at 7 EU/t. Plain rubber alone no longer works for aluminium. Unverified: the PVC foil press recipe and time (read EMI).
    - |-
      Sub-steps people skip: one assembler per part (the circuit-less motor recipe must not share a machine with the circuit-1 conveyor); the neodymium rod must be POLARIZED, a plain neodymium rod is a different item that the motor does not accept; the small gear needs the small gear extruder shape in the extruder, not the big gear shape.
    - |-
      Unverified: Polarizer power and time for neodymium (recipe voltage is a high-amp HV value in the source, read EMI), neodymium EBF time, whether the bastnasite step in the Electric Ore Factory needs an EV hatch or accepts MV (read EMI).
    - The EV circuit (Microprocessor Supercomputer) is made inside the IV circuit line (iv_circuits, IV era, second stage); build those first stages before the EV robot arm.
  b:
    - ["gtceu:lv_assembler", 6]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:mv_extruder", 1]
    - ["gtceu:hv_polarizer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
  how:
    - i: ["gtceu:titanium_ingot", "gtceu:titanium_plate", "gtceu:titanium_rod"]
      t: |-
        One titanium drawer fed from the Vacuum Freezer output (titanium line). From it a Modular Router or Pipez filter feeds three single-purpose machines: LV Bender (ghost circuit 1, ingot → plate), LV Lathe (ingot → 2 rods) and the extruder (ingot → small gear). Each output goes into its own drawer. Keep Exact at 16 on every part drawer so one hungry assembler cannot drain the others.
    - i: ["gtceu:mv_extruder", "gtceu:small_titanium_gear"]
      t: |-
        MV Extruder with the small gear extruder shape in a bus slot: 1 titanium ingot → 1 small gear, 2.4 s at 64 EU/t (above the LV limit, hence MV). The same extruder with a pipe shape is the one that makes the titanium fluid pipe for the pump. Never put two shapes in the same bus.
    - i: ["gtceu:magnetic_neodymium_rod", "gtceu:hv_polarizer"]
      t: |-
        Neodymium chain: crushed bastnasite → Electric Ore Factory (EV) → neodymium dust → EBF (1297 K, circuit 1, cupronickel is enough) → neodymium ingot → lathe → neodymium rod → Polarizer → magnetic neodymium rod. Drawer of magnetic rods capped at 16: one rod per motor.
    - i: ["gtceu:lv_assembler", "gtceu:ev_electric_motor"]
      t: |-
        Motor assembler (own LV Assembler): 2 aluminium double cable, 2 titanium rods, 1 magnetic neodymium rod, 4 kanthal double wire in its input bus, 5 s at 30 EU/t. This is the part everything else uses, so cap its output drawer at 16 and make it the first machine you build.
    - i: ["gtceu:lv_assembler", "gtceu:ev_electric_piston"]
      t: |-
        Piston assembler (own machine): 2 titanium rods + 2 aluminium cables + 3 titanium plates + 1 small gear + 1 motor, 5 s at 30 EU/t. Plates, rods and gears come through three separate Item Filters, never a single unfiltered pipe.
    - i: ["gtceu:lv_assembler", "gtceu:ev_robot_arm", "gtceu:micro_processor_computer"]
      t: |-
        Robot arm assembler (own machine): 3 aluminium cables + 2 titanium rods + 2 motors + 1 piston + 1 EV circuit per arm (ComponentRecipes uses the EV circuit tag: Microprocessor Computer, Nanoprocessor Assembly or Quantum Processor, any of them; the Microprocessor Computer is the one the IV circuits chain builds first; the Nanoprocessor itself is an HV circuit and does not fit), 5 s at 30 EU/t. The circuit drawer is the scarce one; mark it so you do not drain the circuit assembler for hatches.
    - i: ["gtceu:lv_assembler", "gtceu:ev_electric_pump", "gtceu:ev_conveyor_module"]
      t: |-
        Pump assembler: 1 aluminium cable + titanium fluid pipe + stainless screw + stainless rotor + 2 rubber rings + 1 motor. Conveyor assembler with ghost circuit 1: 1 aluminium cable + 2 motors + 864 mB molten rubber (rubber chain, extractor). Pumps feed hatches and the Distillation Tower, conveyors go into every EV machine, so build 2 conveyor assemblers if you plan a machine row.
    - i: ["gtceu:lv_assembler", "gtceu:ev_machine_casing", "gtceu:ev_machine_hull"]
      t: |-
        Hull line: assembler with ghost circuit 8, 8 titanium plates → 1 EV machine casing (2.5 s at 16 EU/t). A second assembler: casing + 2 aluminium cables + 288 mB polyethylene → EV Machine Hull (2.5 s). Hulls go straight into storage; every EV single machine and hatch uses one.
    - i: ["gtceu:hv_chemical_bath", "gtceu:quantum_eye", "gtceu:ev_emitter", "gtceu:ev_sensor"]
      t: |-
        Emitters and sensors last: HV Chemical Bath makes quantum eyes (ender eye + 250 mB radon, 24 s, 480 EU/t), then one assembler each for the emitter (ghost circuit 1, 4 platinum rods) and the sensor (1 platinum rod, 4 titanium plates). Keep a quantum eye drawer capped at 8 and keep the radon drum off anything else. Radon gates this step: see the radon tip above.
---
# EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `ev_components` · **Tags:** Infinite source, Unverified

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [EV components and hull](../../plan/p9.md#evcomp)

**Tips:** 11, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Titanium ingot (gtceu:titanium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Titanium plate (gtceu:titanium_plate) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Plate</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-la">
<div class="gt-head"><span class="gt-mname">LV Lathe · 1 → 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Titanium ingot (gtceu:titanium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Titanium rod (gtceu:titanium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Rod</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
<div class="gt-panel t-mv" id="m-ex">
<div class="gt-head"><span class="gt-mname">MV Extruder · small gear shape</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Titanium ingot (gtceu:titanium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_extruder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">2.4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Titanium small gear (gtceu:small_titanium_gear) - 1 / 2.4 s"><img class="gt-ico" src="../../assets/icons/gtceu__small_titanium_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Titanium Gear</span><span class="gt-note">Titanium small gear</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_extruder</code></div>
</div>
<div class="gt-panel t-lv" id="m-am">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Titanium rod (gtceu:titanium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="Neodymium rod (polarized) (gtceu:magnetic_neodymium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_neodymium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Neodymium Rod</span><span class="gt-note">Neodymium rod (polarized)</span><b class="gt-q">1</b></span><span class="gt-slot" title="4 Kanthal double wire (gtceu:kanthal_double_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Double Wire</span><span class="gt-note">4 Kanthal double wire</span><b class="gt-q">4</b></span><span class="gt-slot" title="2 Aluminium double cable (gtceu:aluminium_double_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_double_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Double Cable</span><span class="gt-note">2 Aluminium double cable</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Electric Motor (gtceu:ev_electric_motor) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-ap">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="EV Electric Motor (gtceu:ev_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot" title="Titanium rod (gtceu:titanium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="Titanium plate (gtceu:titanium_plate) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Plate</span><b class="gt-q">3</b></span><span class="gt-slot" title="Titanium small gear (gtceu:small_titanium_gear) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__small_titanium_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Titanium Gear</span><span class="gt-note">Titanium small gear</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Electric Piston (gtceu:ev_electric_piston) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-ar">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="EV Electric Piston (gtceu:ev_electric_piston) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electric Piston</span><b class="gt-q">1</b></span><span class="gt-slot" title="EV Electric Motor (gtceu:ev_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot" title="Titanium rod (gtceu:titanium_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Rod</span><b class="gt-q">2</b></span><span class="gt-slot" title="EV circuit (#gtceu:circuits/ev) (gtceu:micro_processor_computer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Computer</span><span class="gt-note">EV circuit (#gtceu:circuits/ev)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="EV Robot Arm (gtceu:ev_robot_arm) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__ev_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-ah">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Titanium plate (gtceu:titanium_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Machine Casing (gtceu:ev_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ev_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender](#m-be) → [LV Assembler · 5 s](#m-ap) → [LV Assembler · 5 s](#m-ar) (also LV Bender → [LV Assembler · circuit 8 · 2.5 s](#m-ah))
- [LV Lathe · 1 → 2](#m-la) → [LV Assembler · 5 s · 30 EU/t](#m-am) → [LV Assembler · 5 s](#m-ap), [LV Assembler · 5 s](#m-ar) (also LV Lathe · 1 → 2 → [LV Assembler · 5 s](#m-ap), LV Lathe · 1 → 2 → [LV Assembler · 5 s](#m-ar))
- [MV Extruder · small gear shape](#m-ex) → [LV Assembler · 5 s](#m-ap)
- [LV Assembler · circuit 8 · 2.5 s](#m-ah)

### Direct steps

- EV Machine Casing → EV Machine Hull (+ 2 cable)

## How to build

1. One titanium drawer fed from the Vacuum Freezer output (titanium line). From it a Modular Router or Pipez filter feeds three single-purpose machines: LV Bender (ghost circuit 1, ingot → plate), LV Lathe (ingot → 2 rods) and the extruder (ingot → small gear). Each output goes into its own drawer. Keep Exact at 16 on every part drawer so one hungry assembler cannot drain the others. — `gtceu:titanium_ingot`, `gtceu:titanium_plate`, `gtceu:titanium_rod`
2. MV Extruder with the small gear extruder shape in a bus slot: 1 titanium ingot → 1 small gear, 2.4 s at 64 EU/t (above the LV limit, hence MV). The same extruder with a pipe shape is the one that makes the titanium fluid pipe for the pump. Never put two shapes in the same bus. — `gtceu:mv_extruder`, `gtceu:small_titanium_gear`
3. Neodymium chain: crushed bastnasite → Electric Ore Factory (EV) → neodymium dust → EBF (1297 K, circuit 1, cupronickel is enough) → neodymium ingot → lathe → neodymium rod → Polarizer → magnetic neodymium rod. Drawer of magnetic rods capped at 16: one rod per motor. — `gtceu:magnetic_neodymium_rod`, `gtceu:hv_polarizer`
4. Motor assembler (own LV Assembler): 2 aluminium double cable, 2 titanium rods, 1 magnetic neodymium rod, 4 kanthal double wire in its input bus, 5 s at 30 EU/t. This is the part everything else uses, so cap its output drawer at 16 and make it the first machine you build. — `gtceu:lv_assembler`, `gtceu:ev_electric_motor`
5. Piston assembler (own machine): 2 titanium rods + 2 aluminium cables + 3 titanium plates + 1 small gear + 1 motor, 5 s at 30 EU/t. Plates, rods and gears come through three separate Item Filters, never a single unfiltered pipe. — `gtceu:lv_assembler`, `gtceu:ev_electric_piston`
6. Robot arm assembler (own machine): 3 aluminium cables + 2 titanium rods + 2 motors + 1 piston + 1 EV circuit per arm (ComponentRecipes uses the EV circuit tag: Microprocessor Computer, Nanoprocessor Assembly or Quantum Processor, any of them; the Microprocessor Computer is the one the IV circuits chain builds first; the Nanoprocessor itself is an HV circuit and does not fit), 5 s at 30 EU/t. The circuit drawer is the scarce one; mark it so you do not drain the circuit assembler for hatches. — `gtceu:lv_assembler`, `gtceu:ev_robot_arm`, `gtceu:micro_processor_computer`
7. Pump assembler: 1 aluminium cable + titanium fluid pipe + stainless screw + stainless rotor + 2 rubber rings + 1 motor. Conveyor assembler with ghost circuit 1: 1 aluminium cable + 2 motors + 864 mB molten rubber (rubber chain, extractor). Pumps feed hatches and the Distillation Tower, conveyors go into every EV machine, so build 2 conveyor assemblers if you plan a machine row. — `gtceu:lv_assembler`, `gtceu:ev_electric_pump`, `gtceu:ev_conveyor_module`
8. Hull line: assembler with ghost circuit 8, 8 titanium plates → 1 EV machine casing (2.5 s at 16 EU/t). A second assembler: casing + 2 aluminium cables + 288 mB polyethylene → EV Machine Hull (2.5 s). Hulls go straight into storage; every EV single machine and hatch uses one. — `gtceu:lv_assembler`, `gtceu:ev_machine_casing`, `gtceu:ev_machine_hull`
9. Emitters and sensors last: HV Chemical Bath makes quantum eyes (ender eye + 250 mB radon, 24 s, 480 EU/t), then one assembler each for the emitter (ghost circuit 1, 4 platinum rods) and the sensor (1 platinum rod, 4 titanium plates). Keep a quantum eye drawer capped at 8 and keep the radon drum off anything else. Radon gates this step: see the radon tip above. — `gtceu:hv_chemical_bath`, `gtceu:quantum_eye`, `gtceu:ev_emitter`, `gtceu:ev_sensor`

## Tips

- EV Electric Motor (assembler 100 ticks, 30 EU/t, LV machine is enough): 2 aluminium double cable + 2 titanium rod + 1 magnetic neodymium rod + 4 kanthal double wire. Piston: 2 titanium rod + 2 aluminium cable + 3 titanium plate + 1 small titanium gear + 1 motor. Robot arm: 3 aluminium cable + 2 titanium rod + 2 motors + 1 piston + 1 EV circuit. All source: ComponentRecipes (not changed by the pack scripts).
- EV Electric Pump: 1 aluminium cable + 1 titanium normal fluid pipe + 1 stainless steel screw + 1 stainless steel rotor + 2 rubber rings + 1 motor. EV Conveyor Module: 1 aluminium cable + 2 motors + 864 mB molten rubber, ghost circuit 1. Both 100 ticks at 30 EU/t. The pipe is 3 titanium ingots in an extruder (HV pipe recipe from the previous era, same pattern).
- Count the titanium: motor 1 ingot (the rods), piston 6, robot arm 9, pump 4, conveyor 2, hull 8 plates. A full set of EV single machines eats dozens of ingots, so the titanium line (about 1 ingot per 10 B of molten ore mixture) sets the pace of this whole era.
- Magnetic neodymium rod: neodymium dust → EBF 1297 K (neodymium blast, MV default 120 EU/t, mass 144 x 1297 / 50 is about 3735 ticks, 3 min, derived) → lathe → rod → Polarizer → magnetic rod. Neodymium dust comes from bastnasite: the same Distillation Tower run as titanium gives 1 B molten bastnasite (2 raw bastnasite), and the EV tier of the Electric Ore Factory gives neodymium 25 % + 12.5 % per crushed bastnasite (ore\_factory\_processing.js).
- Emitter and Sensor at EV need a Quantum Eye instead of an ender eye: HV Chemical Bath, 1 ender eye + 250 mB radon → 1 quantum eye in 24 s (480 EU/t). Emitter: 4 platinum rods + 2 aluminium cables + 2 EV circuits + 1 quantum eye (ghost circuit 1). Sensor: 1 platinum rod + 4 titanium plates + 1 EV circuit + 1 quantum eye. Radon is the catch: there is no cheap source. The only routes are an LCR with 8 plutonium-239 ingots + 1 uranium-238 dust + 10 B air (HV, 480 EU/t, 4000 ticks, 1 B radon; the plutonium comes from the uranium-238 centrifuge) or liquid ender air in a Vacuum Freezer plus the Distillation Tower (both IV, 7680 EU/t, 200 B liquid ender air per 1 B radon). So the EV emitter and sensor, and the EV circuit assembler that carries an EV emitter, need the plutonium route or wait for IV. A Field Generator needs a nether star and uranium triplatinum wire: not an EV target.
- Platinum is an EV material, not an IV one: besides the emitter (4 rods) and sensor (1 rod) it is the cable of the EV transformers (hence the 4A and 16A EV hatches), the fine platinum wire of the SMD diodes for the nano line and the cable of the IV hull. Platinum and palladium need only the HV centrifuge and MV electrolysis, rhodium and ruthenium an EV Chemical Reactor (1920 EU/t), and only iridium and osmium need IV (platinum group chain).
- EV Machine Hull: 8 titanium plates → EV machine casing (assembler, ghost circuit 8, 50 ticks at 16 EU/t), then casing + 2 aluminium cables + 288 mB polyethylene → hull (50 ticks, 16 EU/t). Source: extract/recipes.json.
- EV cables: aluminium is an EV rated cable, so WireRecipeHandler adds 1 PVC foil per single or double cable (2 per quadruple) on top of the insulation: assembler, wire + 1 PVC foil + 144 mB rubber, or + 72 mB silicone rubber, or + 36 mB SBR, 100 ticks at 7 EU/t. Plain rubber alone no longer works for aluminium. Unverified: the PVC foil press recipe and time (read EMI).
- Sub-steps people skip: one assembler per part (the circuit-less motor recipe must not share a machine with the circuit-1 conveyor); the neodymium rod must be POLARIZED, a plain neodymium rod is a different item that the motor does not accept; the small gear needs the small gear extruder shape in the extruder, not the big gear shape.
- **Unverified** Polarizer power and time for neodymium (recipe voltage is a high-amp HV value in the source, read EMI), neodymium EBF time, whether the bastnasite step in the Electric Ore Factory needs an EV hatch or accepts MV (read EMI).
- The EV circuit (Microprocessor Supercomputer) is made inside the IV circuit line (iv\_circuits, IV era, second stage); build those first stages before the EV robot arm.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 6 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_lathe` | 2 |
| `gtceu:mv_extruder` | 1 |
| `gtceu:hv_polarizer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |

## Needs / Feeds

- **Needs:** [Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer](titanium_line.md), [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](../hv/kanthal.md), [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../iv/iv_circuits.md)
