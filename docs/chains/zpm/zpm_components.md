---
kind: chain
id: zpm_components
order: 1440
data:
  t: |-
    ZPM components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 30 720 EU/t, osthendah + osmiridium + europium wire)
  inf: true
  "n":
    - - mg
      - |-
        Motor: 1 long magnetic samarium rod · 4 long osthendah rod · 4 ring · 8 round · 64 fine europium wire · 2 VG cable · 288 mB solder + 500 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [Long magnetic samarium rod, "gtceu:long_magnetic_samarium_rod"]
        - [Long osthendah rod, "gtceu:long_osthendah_rod"]
        - [Osthendah ring, "gtceu:osthendah_ring"]
        - [Osthendah round, "gtceu:osthendah_round"]
        - [Fine europium wire, "gtceu:fine_europium_wire"]
        - [VG single cable, "gtceu:vanadium_gallium_single_cable"]
    - [a1, "Assembly Line · 30 s · 30 720 EU/t (scan: LuV motor)", m, "gtceu:assembly_line"]
    - [mo, ZPM Electric Motor, x, "gtceu:zpm_electric_motor"]
    - - pg
      - |-
        Piston: 4 plate · 4 ring · 16 round · 4 rod · 1 osmiridium gear · 2 small osmiridium gear · 2 VG cable
      - g
      - functionalstorage:oak_1
      - - [Osthendah plate, "gtceu:osthendah_plate"]
        - [Osthendah rod, "gtceu:osthendah_rod"]
        - [Osmiridium gear, "gtceu:osmiridium_gear"]
        - [Small osmiridium gear, "gtceu:small_osmiridium_gear"]
    - [a2, "Assembly Line (piston; scan: LuV piston)", m, "gtceu:assembly_line"]
    - [pi, ZPM Electric Piston, o, "gtceu:zpm_electric_piston"]
    - - ug
      - |-
        Pump: PBI normal fluid pipe · 2 plate · 8 screw · 6 silicone rubber ring · 1 osmiridium rotor · 2 VG cable
      - g
      - functionalstorage:oak_1
      - - [PBI normal fluid pipe, "gtceu:polybenzimidazole_normal_fluid_pipe"]
        - [Osthendah screw, "gtceu:osthendah_screw"]
        - [Silicone rubber ring, "gtceu:silicone_rubber_ring"]
        - [Osmiridium rotor, "gtceu:osmiridium_rotor"]
    - [a3, "Assembly Line (pump; scan: LuV pump)", m, "gtceu:assembly_line"]
    - [pm, ZPM Electric Pump, o, "gtceu:zpm_electric_pump"]
    - - cg
      - |-
        Conveyor: 2 plate · 4 ring · 16 round · 4 screw · 2 VG cable · 2304 mB SBR
      - g
      - functionalstorage:oak_1
      - - [Osthendah plate, "gtceu:osthendah_plate"]
        - [Osthendah screw, "gtceu:osthendah_screw"]
        - [Styrene butadiene rubber, "gtceu:styrene_butadiene_rubber_bucket"]
    - [a4, "Assembly Line (conveyor; scan: LuV conveyor)", m, "gtceu:assembly_line"]
    - [cv, ZPM Conveyor Module, o, "gtceu:zpm_conveyor_module"]
  e:
    - [mg, a1, "1"]
    - [a1, mo, "1 / 30 s"]
    - [mo, a2, "1"]
    - [pg, a2, "1"]
    - [a2, pi, "1 / 30 s"]
    - [mo, a3, "1"]
    - [ug, a3, "1"]
    - [a3, pm, "1 / 30 s"]
    - [mo, a4, "2"]
    - [cg, a4, "1"]
    - [a4, cv, "1 / 30 s"]
  tips:
    - |-
      All four come from the pack table (utils/tier_data.js zpm row: primMaterial osthendah, supMaterial osmiridium, wireMechanical europium, cable vanadium gallium, pipe polybenzimidazole, primRubber styrene butadiene rubber, supRubber silicone rubber, primMagnet samarium, scaler 2, EU = VA[LuV]) and luv_to_uv_components.js. Each is an Assembly Line recipe, 600 ticks at 30 720 EU/t, with SCANNER research of the LuV part (1800 ticks at 7680 EU/t, an IV Scanner, zpm_data chain): motor, piston, pump and conveyor all scan their LuV namesake. The vanilla ZPM versions are removed. Fluids per craft (base x 2^scaler = x 4): 288 mB soldering alloy + 500 mB lubricant for all four, plus 2304 mB styrene butadiene rubber for the conveyor.
    - |-
      Ingredient counts (verified from the componentTypesAssemblyLine calls): motor = 1 long magnetic samarium rod + 4 long osthendah rods + 4 osthendah rings + 8 osthendah rounds + 64 fine europium wire + 2 VG single cables. Piston = 1 motor + 4 osthendah plates + 4 rings + 16 rounds + 4 rods + 1 osmiridium gear + 2 small osmiridium gears + 2 cables. Pump = 1 motor + 1 PBI normal fluid pipe + 2 plates + 8 screws + 6 silicone rubber rings (scaled 2 + 2) + 1 osmiridium rotor + 2 cables. Conveyor = 2 motors + 2 plates + 4 rings + 16 rounds + 4 screws + 2 cables.
    - |-
      Raw metal per part (mass: long rod 1 ingot, rod 1/2, ring 1/4, round 1/9, screw 1/9, plate 1, gear 4, small gear 1, rotor about 4.25, wire: 64 fine wire = 8 ingots): motor about 5.9 osthendah + 8 EUROPIUM + 1 VG + 1 magnetic samarium rod; piston about 8.8 osthendah + 6 osmiridium + the motor; pump about 2.9 osthendah + 4.25 osmiridium + 3 PBI (pipe) + the motor; conveyor about 5.2 osthendah + 2 motors. EUROPIUM is the bottleneck: a motor is 8 ingots = 8 fusion runs of the LuV reactor at 144 mB each (28.8 s each: about 4 minutes). A conveyor (2 motors) is 16 ingots, a piston, pump or motor 8. Plan the MK II reactor (zpm_fusion) early: it overclocks the same recipe.
    - |-
      Motors needed downstream: pump 1, piston 1, conveyor 2, robot arm 2 + a piston (so 3), emitter 1, sensor 1, field generator 2 (through 2 emitters), Research Station 2, Object Holder 2. A machine that takes 2 arms and 2 conveyors (the usual assembler-class pattern, Unverified for ZPM) needs 10 motors = 80 europium ingots. Build the motor line first and make it big: 30 s per motor per Assembly Line.
    - |-
      Samarium: magnetic samarium rod = polarised samarium ingot (the long rod from it): the same rod the LuV motor and the voltage coils use; Unverified source of samarium (rare earth line, see luv_alloys). Europium fine wire: wiremill on a europium ingot, 8 wire per ingot (Unverified exact yield). Silicone rubber ring: bender/extruder from silicone rubber (Unverified). PBI normal fluid pipe: extruder with the pipe mold from PBI ingots (Unverified machine tier and whether PBI forms an ingot at all: the pack’s pipeMaterial entry says yes).
    - |-
      Sub-steps people skip: (1) the scan stick is the LuV part (LuV motor for the motor, LuV pump for the pump): four sticks, four Data Access slots or a Data Bank; (2) the pump uses an OSMIRIDIUM rotor and the piston osmiridium gears (supMaterial), not osthendah; (3) the conveyor needs SBR, 2304 mB: a third drum; (4) soldering alloy AND lubricant on all four: two drums on every line; (5) keep a motor stock drawer with Keep Exact 4, three Keep Exact arms off it; (6) 30 s per craft means a 20 minute wait for 40 motors: use more than one Assembly Line.
    - |-
      Unverified: the lathe/extruder/wiremill times for osthendah parts and which machine tier the 4-ingot gear needs; the liquid helium need for osthendah only appears at the freezer.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:hv_extruder", 1]
    - ["gtceu:luv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:osthendah_plate", "gtceu:fine_europium_wire", "gtceu:long_osthendah_rod"]
      t: |-
        Drawers first, one per part: osthendah plates, rods, long rods, rings, rounds, screws; osmiridium gears, small gears, rotors; PBI pipes; VG single cables; fine europium wire; silicone rings; magnetic samarium long rods. Drums: soldering alloy, lubricant, SBR on the Assembly Line hatches. Each Assembly Line input bus has its own drawer behind a router, with an Item Filter.
    - i: ["gtceu:lv_lathe", "gtceu:osthendah_round", "gtceu:long_osthendah_rod"]
      t: |-
        Part machines, one per product: LV Lathe for rods/long rods and rounds, LV Bender for plates, extruder for rings and gears, wiremill for fine europium wire, screw cutter. Each behind its own router with a Keep Exact arm.
    - i: ["gtceu:assembly_line", "gtceu:long_magnetic_samarium_rod", "gtceu:zpm_electric_motor"]
      t: |-
        Motor: load the buses in order: magnetic samarium long rod, 4 long osthendah rods, 4 rings, 8 rounds, 64 fine europium wire, 2 VG cables; fluids 288 mB soldering alloy + 500 mB lubricant. 30 s at 30 720 EU/t → 1 ZPM Electric Motor. The scan stick: LuV motor. Drawer Keep Exact 8.
    - i: ["gtceu:assembly_line", "gtceu:zpm_electric_motor", "gtceu:zpm_electric_piston"]
      t: |-
        Piston: motor + 4 plates + 4 rings + 16 rounds + 4 rods + 1 osmiridium gear + 2 small osmiridium gears + 2 cables, scan stick: LuV piston. 30 s.
    - i: ["gtceu:assembly_line", "gtceu:polybenzimidazole_normal_fluid_pipe", "gtceu:zpm_electric_pump"]
      t: |-
        Pump: motor + PBI normal fluid pipe + 2 plates + 8 screws + 6 silicone rings + 1 osmiridium rotor + 2 cables; scan stick: LuV pump. 30 s.
    - i: ["gtceu:assembly_line", "gtceu:styrene_butadiene_rubber_bucket", "gtceu:zpm_conveyor_module"]
      t: |-
        Conveyor: 2 motors + 2 plates + 4 rings + 16 rounds + 4 screws + 2 cables and 2304 mB SBR (a third drum) → ZPM Conveyor Module in 30 s; scan stick: LuV conveyor.
    - i: ["functionalstorage:oak_1", "gtceu:zpm_electric_motor"]
      t: |-
        Easy to miss: motors feed everything else. Three Keep Exact arms off one motor drawer, one for each other Assembly Line setup, and a second Assembly Line for the robot arm line (zpm_components2). Europium decides how many you can make: check the europium drum before each batch.
---
# ZPM components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 30 720 EU/t, osthendah + osmiridium + europium wire)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_components` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM hull, hatch and components](../../plan/p12.md#zpmmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (scan: LuV motor)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Motor: 1 long magnetic samarium rod · 4 long osthendah rod · 4 ring · 8 round · 64 fine europium wire · 2 VG cable · 288 mB solder + 500 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Motor: 1 long magnetic samarium rod · 4 long osthendah rod · 4 ring · 8 round · 64 fine europium wire · 2 VG cable · 288 mB solder + 500 mB lubricant</span><span class="gt-sub"><span>Long magnetic samarium rod</span><span>Long osthendah rod</span><span>Osthendah ring</span><span>Osthendah round</span><span>Fine europium wire</span><span>VG single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Electric Motor (gtceu:zpm_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line (piston; scan: LuV piston)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ZPM Electric Motor (gtceu:zpm_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Piston: 4 plate · 4 ring · 16 round · 4 rod · 1 osmiridium gear · 2 small osmiridium gear · 2 VG cable (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Piston: 4 plate · 4 ring · 16 round · 4 rod · 1 osmiridium gear · 2 small osmiridium gear · 2 VG cable</span><span class="gt-sub"><span>Osthendah plate</span><span>Osthendah rod</span><span>Osmiridium gear</span><span>Small osmiridium gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Electric Piston (gtceu:zpm_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line (pump; scan: LuV pump)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ZPM Electric Motor (gtceu:zpm_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Pump: PBI normal fluid pipe · 2 plate · 8 screw · 6 silicone rubber ring · 1 osmiridium rotor · 2 VG cable (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Pump: PBI normal fluid pipe · 2 plate · 8 screw · 6 silicone rubber ring · 1 osmiridium rotor · 2 VG cable</span><span class="gt-sub"><span>PBI normal fluid pipe</span><span>Osthendah screw</span><span>Silicone rubber ring</span><span>Osmiridium rotor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Electric Pump (gtceu:zpm_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Pump</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line (conveyor; scan: LuV conveyor)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ZPM Electric Motor (gtceu:zpm_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Conveyor: 2 plate · 4 ring · 16 round · 4 screw · 2 VG cable · 2304 mB SBR (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Conveyor: 2 plate · 4 ring · 16 round · 4 screw · 2 VG cable · 2304 mB SBR</span><span class="gt-sub"><span>Osthendah plate</span><span>Osthendah screw</span><span>Styrene butadiene rubber</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Conveyor Module (gtceu:zpm_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Conveyor Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 30 720 EU/t (scan: LuV motor)](#m-a1) → [Assembly Line (piston; scan: LuV piston)](#m-a2) (also Assembly Line · 30 s · 30 720 EU/t (scan: LuV motor) → [Assembly Line (pump; scan: LuV pump)](#m-a3), Assembly Line · 30 s · 30 720 EU/t (scan: LuV motor) → [Assembly Line (conveyor; scan: LuV conveyor)](#m-a4))
- [Assembly Line (pump; scan: LuV pump)](#m-a3)
- [Assembly Line (conveyor; scan: LuV conveyor)](#m-a4)

## How to build

1. Drawers first, one per part: osthendah plates, rods, long rods, rings, rounds, screws; osmiridium gears, small gears, rotors; PBI pipes; VG single cables; fine europium wire; silicone rings; magnetic samarium long rods. Drums: soldering alloy, lubricant, SBR on the Assembly Line hatches. Each Assembly Line input bus has its own drawer behind a router, with an Item Filter. — `functionalstorage:oak_1`, `gtceu:osthendah_plate`, `gtceu:fine_europium_wire`, `gtceu:long_osthendah_rod`
2. Part machines, one per product: LV Lathe for rods/long rods and rounds, LV Bender for plates, extruder for rings and gears, wiremill for fine europium wire, screw cutter. Each behind its own router with a Keep Exact arm. — `gtceu:lv_lathe`, `gtceu:osthendah_round`, `gtceu:long_osthendah_rod`
3. Motor: load the buses in order: magnetic samarium long rod, 4 long osthendah rods, 4 rings, 8 rounds, 64 fine europium wire, 2 VG cables; fluids 288 mB soldering alloy + 500 mB lubricant. 30 s at 30 720 EU/t → 1 ZPM Electric Motor. The scan stick: LuV motor. Drawer Keep Exact 8. — `gtceu:assembly_line`, `gtceu:long_magnetic_samarium_rod`, `gtceu:zpm_electric_motor`
4. Piston: motor + 4 plates + 4 rings + 16 rounds + 4 rods + 1 osmiridium gear + 2 small osmiridium gears + 2 cables, scan stick: LuV piston. 30 s. — `gtceu:assembly_line`, `gtceu:zpm_electric_motor`, `gtceu:zpm_electric_piston`
5. Pump: motor + PBI normal fluid pipe + 2 plates + 8 screws + 6 silicone rings + 1 osmiridium rotor + 2 cables; scan stick: LuV pump. 30 s. — `gtceu:assembly_line`, `gtceu:polybenzimidazole_normal_fluid_pipe`, `gtceu:zpm_electric_pump`
6. Conveyor: 2 motors + 2 plates + 4 rings + 16 rounds + 4 screws + 2 cables and 2304 mB SBR (a third drum) → ZPM Conveyor Module in 30 s; scan stick: LuV conveyor. — `gtceu:assembly_line`, `gtceu:styrene_butadiene_rubber_bucket`, `gtceu:zpm_conveyor_module`
7. Easy to miss: motors feed everything else. Three Keep Exact arms off one motor drawer, one for each other Assembly Line setup, and a second Assembly Line for the robot arm line (zpm\_components2). Europium decides how many you can make: check the europium drum before each batch. — `functionalstorage:oak_1`, `gtceu:zpm_electric_motor`

## Tips

- All four come from the pack table (utils/tier\_data.js zpm row: primMaterial osthendah, supMaterial osmiridium, wireMechanical europium, cable vanadium gallium, pipe polybenzimidazole, primRubber styrene butadiene rubber, supRubber silicone rubber, primMagnet samarium, scaler 2, EU = VA\[LuV\]) and luv\_to\_uv\_components.js. Each is an Assembly Line recipe, 600 ticks at 30 720 EU/t, with SCANNER research of the LuV part (1800 ticks at 7680 EU/t, an IV Scanner, zpm\_data chain): motor, piston, pump and conveyor all scan their LuV namesake. The vanilla ZPM versions are removed. Fluids per craft (base x 2^scaler = x 4): 288 mB soldering alloy + 500 mB lubricant for all four, plus 2304 mB styrene butadiene rubber for the conveyor.
- Ingredient counts (verified from the componentTypesAssemblyLine calls): motor = 1 long magnetic samarium rod + 4 long osthendah rods + 4 osthendah rings + 8 osthendah rounds + 64 fine europium wire + 2 VG single cables. Piston = 1 motor + 4 osthendah plates + 4 rings + 16 rounds + 4 rods + 1 osmiridium gear + 2 small osmiridium gears + 2 cables. Pump = 1 motor + 1 PBI normal fluid pipe + 2 plates + 8 screws + 6 silicone rubber rings (scaled 2 + 2) + 1 osmiridium rotor + 2 cables. Conveyor = 2 motors + 2 plates + 4 rings + 16 rounds + 4 screws + 2 cables.
- Raw metal per part (mass: long rod 1 ingot, rod 1/2, ring 1/4, round 1/9, screw 1/9, plate 1, gear 4, small gear 1, rotor about 4.25, wire: 64 fine wire = 8 ingots): motor about 5.9 osthendah + 8 EUROPIUM + 1 VG + 1 magnetic samarium rod; piston about 8.8 osthendah + 6 osmiridium + the motor; pump about 2.9 osthendah + 4.25 osmiridium + 3 PBI (pipe) + the motor; conveyor about 5.2 osthendah + 2 motors. EUROPIUM is the bottleneck: a motor is 8 ingots = 8 fusion runs of the LuV reactor at 144 mB each (28.8 s each: about 4 minutes). A conveyor (2 motors) is 16 ingots, a piston, pump or motor 8. Plan the MK II reactor (zpm\_fusion) early: it overclocks the same recipe.
- Motors needed downstream: pump 1, piston 1, conveyor 2, robot arm 2 + a piston (so 3), emitter 1, sensor 1, field generator 2 (through 2 emitters), Research Station 2, Object Holder 2. A machine that takes 2 arms and 2 conveyors (the usual assembler-class pattern, Unverified for ZPM) needs 10 motors = 80 europium ingots. Build the motor line first and make it big: 30 s per motor per Assembly Line.
- Samarium: magnetic samarium rod = polarised samarium ingot (the long rod from it): the same rod the LuV motor and the voltage coils use; Unverified source of samarium (rare earth line, see luv\_alloys). Europium fine wire: wiremill on a europium ingot, 8 wire per ingot (Unverified exact yield). Silicone rubber ring: bender/extruder from silicone rubber (Unverified). PBI normal fluid pipe: extruder with the pipe mold from PBI ingots (Unverified machine tier and whether PBI forms an ingot at all: the pack’s pipeMaterial entry says yes).
- Sub-steps people skip: (1) the scan stick is the LuV part (LuV motor for the motor, LuV pump for the pump): four sticks, four Data Access slots or a Data Bank; (2) the pump uses an OSMIRIDIUM rotor and the piston osmiridium gears (supMaterial), not osthendah; (3) the conveyor needs SBR, 2304 mB: a third drum; (4) soldering alloy AND lubricant on all four: two drums on every line; (5) keep a motor stock drawer with Keep Exact 4, three Keep Exact arms off it; (6) 30 s per craft means a 20 minute wait for 40 motors: use more than one Assembly Line.
- **Unverified** the lathe/extruder/wiremill times for osthendah parts and which machine tier the 4-ingot gear needs; the liquid helium need for osthendah only appears at the freezer.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:lv_lathe` | 2 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:hv_extruder` | 1 |
| `gtceu:luv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:zpm_electric_motor`, `gtceu:zpm_electric_piston`, `gtceu:zpm_electric_pump`, `gtceu:zpm_conveyor_module`
