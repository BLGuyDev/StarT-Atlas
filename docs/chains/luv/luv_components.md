---
kind: chain
id: luv_components
order: 1230
data:
  t: |-
    LuV components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 7680 EU/t, HSS-S + ruridit + niobium titanium + palladium wire)
  inf: true
  "n":
    - - mg
      - |-
        Motor: 1 long magnetic samarium rod · 4 long HSS-S rod · 4 HSS-S ring · 8 HSS-S round · 64 fine palladium wire · 2 NbTi cable · 144 mB solder · 250 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [Long magnetic samarium rod, "gtceu:long_magnetic_samarium_rod"]
        - [Long HSS-S rod, "gtceu:long_hsss_rod"]
        - [HSS-S ring, "gtceu:hsss_ring"]
        - [HSS-S round, "gtceu:hsss_round"]
        - [Fine palladium wire, "gtceu:fine_palladium_wire"]
        - [NbTi single cable, "gtceu:niobium_titanium_single_cable"]
    - [a1, "Assembly Line · 30 s · 7680 EU/t", m, "gtceu:assembly_line"]
    - [mo, LuV Electric Motor, x, "gtceu:luv_electric_motor"]
    - - pg
      - |-
        Piston: 4 HSS-S plate · 4 ring · 16 round · 4 rod · 1 ruridit gear · 2 small ruridit gear · 2 NbTi cable
      - g
      - functionalstorage:oak_1
      - - [HSS-S plate, "gtceu:hsss_plate"]
        - [HSS-S rod, "gtceu:hsss_rod"]
        - [Ruridit gear, "gtceu:ruridit_gear"]
        - [Small ruridit gear, "gtceu:small_ruridit_gear"]
    - [a2, "Assembly Line (piston)", m, "gtceu:assembly_line"]
    - [pi, LuV Electric Piston, o, "gtceu:luv_electric_piston"]
    - - ug
      - |-
        Pump: NbTi normal fluid pipe · 2 HSS-S plate · 8 screw · 4 silicone rubber ring · 1 ruridit rotor · 2 NbTi cable
      - g
      - functionalstorage:oak_1
      - - [NbTi normal fluid pipe, "gtceu:niobium_titanium_normal_fluid_pipe"]
        - [HSS-S screw, "gtceu:hsss_screw"]
        - [Silicone rubber ring, "gtceu:silicone_rubber_ring"]
        - [Ruridit rotor, "gtceu:ruridit_rotor"]
    - [a3, "Assembly Line (pump)", m, "gtceu:assembly_line"]
    - [pm, LuV Electric Pump, o, "gtceu:luv_electric_pump"]
    - - cg
      - |-
        Conveyor: 2 HSS-S plate · 4 ring · 16 round · 4 screw · 2 NbTi cable · 1152 mB SBR
      - g
      - functionalstorage:oak_1
      - - [HSS-S plate, "gtceu:hsss_plate"]
        - [HSS-S screw, "gtceu:hsss_screw"]
        - [Styrene butadiene rubber, "gtceu:styrene_butadiene_rubber_bucket"]
    - [a4, "Assembly Line (conveyor)", m, "gtceu:assembly_line"]
    - [cv, LuV Conveyor Module, o, "gtceu:luv_conveyor_module"]
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
      All recipes come from the pack table (utils/tier_data.js, luv entry: primMaterial hsss, supMaterial ruridit, wireMechanical palladium, cable niobium titanium, pipe niobium titanium, supRubber silicone rubber, primRubber styrene butadiene rubber, primMagnet samarium, solder soldering alloy, lubricant) and luv_to_uv_components.js. Each is an Assembly Line recipe, 600 ticks at 7680 EU/t, scanner research of the IV version (90 s at 1920 EU/t). Fluids per craft: 144 mB soldering alloy + 250 mB lubricant for all four, and 1152 mB styrene butadiene rubber extra for the conveyor.
    - |-
      This differs from vanilla GregTech (vanilla motor uses ruridit wire, vanilla pump an HSS-S rotor): in this pack the pump uses a RURIDIT rotor and the piston a RURIDIT gear and two small ruridit gears, both new flags the pack adds to ruridit in startup_scripts/.../modifications.js. The vanilla motor (ruridit fine wire, 2 long HSS-S rods) and vanilla pump (HSS-S rotor) are removed, so a viewer still showing them is stale.
    - |-
      Raw cost per part in ingots (derived from material units, rod 1/2, long rod 1, ring 1/4, round 1/9, screw 1/9, plate 1, gear 4, small gear 1, rotor 4.25): motor ≈ 5.9 HSS-S + 1 samarium magnetic long rod + 8 palladium ingots (64 fine wire at 8 per ingot) + 2 NbTi cables. Piston ≈ 8.8 HSS-S + 6 ruridit + the motor. Pump ≈ 2.9 HSS-S + 3 NbTi (pipe, normal = 3 ingots) + 4.25 ruridit + 4 silicone rings + the motor. Conveyor ≈ 5.2 HSS-S + 2 motors + 1152 mB SBR. One LuV assembler-class machine eats 2 arms, 2 conveyors: the motor line is the one to scale (about 10 motors for a robot-arm-and-conveyor machine).
    - |-
      Motors needed: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3 (emitter and sensor 1 each, field generator 2 emitters = 2). So a robot arm costs 3 motors, a conveyor 2, a sensor 1: build the motor line first and biggest, 30 s per motor per Assembly Line.
    - |-
      HSS-S is the real bottleneck: iridium + osmium + HSS-G (see luv_hsss). Palladium: 8 ingots per motor from the platline line, again the platinum group. Fine palladium wire: 1 ingot → wire (foil/wire) in a wiremill, 4 or 8 wire per ingot depending on the form; Unverified exact count, check the wiremill in EMI.
    - |-
      Silicone rings: rubber ring made in an extruder/bender from silicone rubber; 4 per pump. Unverified: the ring recipe in this fork, check EMI. Ruridit rotor: extruder or forge from ruridit plates and ring (pack flag), Unverified machine.
    - |-
      Sub-steps people skip: (1) the scanned stick is from the IV part (IV motor, IV pump ...), not the LuV one; (2) the rhodium foil is NOT here, only in emitter and sensor; (3) the long samarium rod is magnetised: samarium is an element with magnetic variant, do not use a plain samarium rod; (4) the pump needs a NbTi PIPE, not wire; (5) soldering alloy, not tin, in this tier; (6) keep a motor stock drawer with Keep Exact 4 so the piston, pump and conveyor lines can all be fed from one motor line.
    - |-
      Unverified: the lathe/extruder times of HSS-S rings, rounds, screws and long rods (mass based), and the machine tiers they need above 5000 K materials (HSS-S is a hard material: check the extruder tier).
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:hv_extruder", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:hsss_plate", "gtceu:fine_palladium_wire", "gtceu:long_hsss_rod"]
      t: |-
        Drawers first, one per part: HSS-S plates, long rods, rods, rings, rounds, screws; ruridit gears, small gears, rotors; NbTi pipes and single cables; fine palladium wire; silicone rings; samarium magnetic long rods. Four drums (soldering alloy, lubricant, SBR) go to the Assembly Line hatches.
    - i: ["gtceu:lv_lathe", "gtceu:hsss_round", "gtceu:long_hsss_rod"]
      t: |-
        Part machines, one per product: LV Lathe for rods/long rods and rounds, LV Bender for plates, extruder for rings and gears, wiremill for fine palladium wire, screw cutter. Each behind its own router with a Keep Exact arm. Most HSS-S parts are cheap in time but heavy in metal.
    - i: ["gtceu:assembly_line", "gtceu:long_magnetic_samarium_rod", "gtceu:luv_electric_motor"]
      t: |-
        Motor: load buses in order: samarium magnetic long rod, 4 long HSS-S rods, 4 rings, 8 rounds, 64 fine palladium wire, 2 NbTi cables; solder + lubricant in the hatches. 30 s, 7680 EU/t → 1 LuV Electric Motor. Drawer with Keep Exact 8.
    - i: ["gtceu:assembly_line", "gtceu:luv_electric_motor", "gtceu:luv_electric_piston"]
      t: |-
        Piston: motor + 4 HSS-S plates + 4 rings + 16 rounds + 4 rods + 1 ruridit gear + 2 small ruridit gears + 2 NbTi cables (in that order), swap the data stick for the IV piston scan. 30 s.
    - i: ["gtceu:assembly_line", "gtceu:niobium_titanium_normal_fluid_pipe", "gtceu:luv_electric_pump"]
      t: |-
        Pump: motor + NbTi normal fluid pipe + 2 HSS-S plates + 8 screws + 4 silicone rings + 1 ruridit rotor + 2 NbTi cables. 30 s. The pipe is 3 niobium titanium ingots in an extruder (HV or above, Unverified tier).
    - i: ["gtceu:assembly_line", "gtceu:styrene_butadiene_rubber_bucket", "gtceu:luv_conveyor_module"]
      t: |-
        Conveyor: 2 motors + 2 HSS-S plates + 4 rings + 16 rounds + 4 screws + 2 NbTi cables and 1152 mB styrene butadiene rubber (a third drum) → LuV Conveyor Module in 30 s.
    - i: ["functionalstorage:oak_1", "gtceu:luv_electric_motor"]
      t: |-
        Easy to miss: the motors feed pistons, pumps, conveyors and every other LuV component. Three Keep Exact arms off one motor drawer, one for each of the other three Assembly Line setups, and a second Assembly Line for the robot arm line (see luv_components2).
---
# LuV components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 7680 EU/t, HSS-S + ruridit + niobium titanium + palladium wire)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_components` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Motor: 1 long magnetic samarium rod · 4 long HSS-S rod · 4 HSS-S ring · 8 HSS-S round · 64 fine palladium wire · 2 NbTi cable · 144 mB solder · 250 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Motor: 1 long magnetic samarium rod · 4 long HSS-S rod · 4 HSS-S ring · 8 HSS-S round · 64 fine palladium wire · 2 NbTi cable · 144 mB solder · 250 mB lubricant</span><span class="gt-sub"><span>Long magnetic samarium rod</span><span>Long HSS-S rod</span><span>HSS-S ring</span><span>HSS-S round</span><span>Fine palladium wire</span><span>NbTi single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LuV Electric Motor (gtceu:luv_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line (piston)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Electric Motor (gtceu:luv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Piston: 4 HSS-S plate · 4 ring · 16 round · 4 rod · 1 ruridit gear · 2 small ruridit gear · 2 NbTi cable (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Piston: 4 HSS-S plate · 4 ring · 16 round · 4 rod · 1 ruridit gear · 2 small ruridit gear · 2 NbTi cable</span><span class="gt-sub"><span>HSS-S plate</span><span>HSS-S rod</span><span>Ruridit gear</span><span>Small ruridit gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Electric Piston (gtceu:luv_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line (pump)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Electric Motor (gtceu:luv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Pump: NbTi normal fluid pipe · 2 HSS-S plate · 8 screw · 4 silicone rubber ring · 1 ruridit rotor · 2 NbTi cable (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Pump: NbTi normal fluid pipe · 2 HSS-S plate · 8 screw · 4 silicone rubber ring · 1 ruridit rotor · 2 NbTi cable</span><span class="gt-sub"><span>NbTi normal fluid pipe</span><span>HSS-S screw</span><span>Silicone rubber ring</span><span>Ruridit rotor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Electric Pump (gtceu:luv_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Pump</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line (conveyor)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Electric Motor (gtceu:luv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Conveyor: 2 HSS-S plate · 4 ring · 16 round · 4 screw · 2 NbTi cable · 1152 mB SBR (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Conveyor: 2 HSS-S plate · 4 ring · 16 round · 4 screw · 2 NbTi cable · 1152 mB SBR</span><span class="gt-sub"><span>HSS-S plate</span><span>HSS-S screw</span><span>Styrene butadiene rubber</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Conveyor Module (gtceu:luv_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Conveyor Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 7680 EU/t](#m-a1) → [Assembly Line (piston)](#m-a2) (also Assembly Line · 30 s · 7680 EU/t → [Assembly Line (pump)](#m-a3), Assembly Line · 30 s · 7680 EU/t → [Assembly Line (conveyor)](#m-a4))
- [Assembly Line (pump)](#m-a3)
- [Assembly Line (conveyor)](#m-a4)

## How to build

1. Drawers first, one per part: HSS-S plates, long rods, rods, rings, rounds, screws; ruridit gears, small gears, rotors; NbTi pipes and single cables; fine palladium wire; silicone rings; samarium magnetic long rods. Four drums (soldering alloy, lubricant, SBR) go to the Assembly Line hatches. — `functionalstorage:oak_1`, `gtceu:hsss_plate`, `gtceu:fine_palladium_wire`, `gtceu:long_hsss_rod`
2. Part machines, one per product: LV Lathe for rods/long rods and rounds, LV Bender for plates, extruder for rings and gears, wiremill for fine palladium wire, screw cutter. Each behind its own router with a Keep Exact arm. Most HSS-S parts are cheap in time but heavy in metal. — `gtceu:lv_lathe`, `gtceu:hsss_round`, `gtceu:long_hsss_rod`
3. Motor: load buses in order: samarium magnetic long rod, 4 long HSS-S rods, 4 rings, 8 rounds, 64 fine palladium wire, 2 NbTi cables; solder + lubricant in the hatches. 30 s, 7680 EU/t → 1 LuV Electric Motor. Drawer with Keep Exact 8. — `gtceu:assembly_line`, `gtceu:long_magnetic_samarium_rod`, `gtceu:luv_electric_motor`
4. Piston: motor + 4 HSS-S plates + 4 rings + 16 rounds + 4 rods + 1 ruridit gear + 2 small ruridit gears + 2 NbTi cables (in that order), swap the data stick for the IV piston scan. 30 s. — `gtceu:assembly_line`, `gtceu:luv_electric_motor`, `gtceu:luv_electric_piston`
5. Pump: motor + NbTi normal fluid pipe + 2 HSS-S plates + 8 screws + 4 silicone rings + 1 ruridit rotor + 2 NbTi cables. 30 s. The pipe is 3 niobium titanium ingots in an extruder (HV or above, Unverified tier). — `gtceu:assembly_line`, `gtceu:niobium_titanium_normal_fluid_pipe`, `gtceu:luv_electric_pump`
6. Conveyor: 2 motors + 2 HSS-S plates + 4 rings + 16 rounds + 4 screws + 2 NbTi cables and 1152 mB styrene butadiene rubber (a third drum) → LuV Conveyor Module in 30 s. — `gtceu:assembly_line`, `gtceu:styrene_butadiene_rubber_bucket`, `gtceu:luv_conveyor_module`
7. Easy to miss: the motors feed pistons, pumps, conveyors and every other LuV component. Three Keep Exact arms off one motor drawer, one for each of the other three Assembly Line setups, and a second Assembly Line for the robot arm line (see luv\_components2). — `functionalstorage:oak_1`, `gtceu:luv_electric_motor`

## Tips

- All recipes come from the pack table (utils/tier\_data.js, luv entry: primMaterial hsss, supMaterial ruridit, wireMechanical palladium, cable niobium titanium, pipe niobium titanium, supRubber silicone rubber, primRubber styrene butadiene rubber, primMagnet samarium, solder soldering alloy, lubricant) and luv\_to\_uv\_components.js. Each is an Assembly Line recipe, 600 ticks at 7680 EU/t, scanner research of the IV version (90 s at 1920 EU/t). Fluids per craft: 144 mB soldering alloy + 250 mB lubricant for all four, and 1152 mB styrene butadiene rubber extra for the conveyor.
- This differs from vanilla GregTech (vanilla motor uses ruridit wire, vanilla pump an HSS-S rotor): in this pack the pump uses a RURIDIT rotor and the piston a RURIDIT gear and two small ruridit gears, both new flags the pack adds to ruridit in startup\_scripts/.../modifications.js. The vanilla motor (ruridit fine wire, 2 long HSS-S rods) and vanilla pump (HSS-S rotor) are removed, so a viewer still showing them is stale.
- Raw cost per part in ingots (derived from material units, rod 1/2, long rod 1, ring 1/4, round 1/9, screw 1/9, plate 1, gear 4, small gear 1, rotor 4.25): motor ≈ 5.9 HSS-S + 1 samarium magnetic long rod + 8 palladium ingots (64 fine wire at 8 per ingot) + 2 NbTi cables. Piston ≈ 8.8 HSS-S + 6 ruridit + the motor. Pump ≈ 2.9 HSS-S + 3 NbTi (pipe, normal = 3 ingots) + 4.25 ruridit + 4 silicone rings + the motor. Conveyor ≈ 5.2 HSS-S + 2 motors + 1152 mB SBR. One LuV assembler-class machine eats 2 arms, 2 conveyors: the motor line is the one to scale (about 10 motors for a robot-arm-and-conveyor machine).
- Motors needed: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3 (emitter and sensor 1 each, field generator 2 emitters = 2). So a robot arm costs 3 motors, a conveyor 2, a sensor 1: build the motor line first and biggest, 30 s per motor per Assembly Line.
- HSS-S is the real bottleneck: iridium + osmium + HSS-G (see luv\_hsss). Palladium: 8 ingots per motor from the platline line, again the platinum group. Fine palladium wire: 1 ingot → wire (foil/wire) in a wiremill, 4 or 8 wire per ingot depending on the form; Unverified exact count, check the wiremill in EMI.
- Silicone rings: rubber ring made in an extruder/bender from silicone rubber; 4 per pump. Unverified: the ring recipe in this fork, check EMI. Ruridit rotor: extruder or forge from ruridit plates and ring (pack flag), Unverified machine.
- Sub-steps people skip: (1) the scanned stick is from the IV part (IV motor, IV pump ...), not the LuV one; (2) the rhodium foil is NOT here, only in emitter and sensor; (3) the long samarium rod is magnetised: samarium is an element with magnetic variant, do not use a plain samarium rod; (4) the pump needs a NbTi PIPE, not wire; (5) soldering alloy, not tin, in this tier; (6) keep a motor stock drawer with Keep Exact 4 so the piston, pump and conveyor lines can all be fed from one motor line.
- **Unverified** the lathe/extruder times of HSS-S rings, rounds, screws and long rods (mass based), and the machine tiers they need above 5000 K materials (HSS-S is a hard material: check the extruder tier).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:lv_lathe` | 2 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:hv_extruder` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Feeds:** [LuV power: Large Gas Turbine with a LuV rotor holder](luv_turbines.md)
- **Main source for:** `gtceu:luv_electric_motor`, `gtceu:luv_electric_piston`, `gtceu:luv_electric_pump`, `gtceu:luv_conveyor_module`
