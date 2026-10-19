---
kind: chain
id: uhv_components
order: 1850
data:
  t: |-
    UHV components 1/2: motor, pump, conveyor module, piston and fluid regulator (Assembly Line, 30 s, 491 520 EU/t, research 128 CWU/t, component parts instead of raw metal)
  inf: true
  "n":
    - - g1
      - UHV super magnetic core · 2 long zalloy rod · UHV transmission assembly · 64 fine zirconium wire · micropower router · 1152 mB solder · 2000 mB lubricant · 1152 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Super magnetic core, "kubejs:uhv_super_magnetic_core"]
        - [Transmission assembly, "kubejs:uhv_transmission_assembly"]
        - [Micropower router, "kubejs:uhv_micropower_router"]
        - [Long zalloy rod, "gtceu:long_zalloy_rod"]
        - [Fine zirconium wire, "gtceu:fine_zirconium_wire"]
    - [a1, "Assembly Line · 30 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [mo, UHV Electric Motor, x, "gtceu:uhv_electric_motor"]
    - - g2
      - motor · zapolgium normal pipe · microfluidic flow valve · 8 SBR ring · zircalloy-4 rotor · router + fluids
      - g
      - functionalstorage:oak_1
      - - [Zapolgium normal fluid pipe, "gtceu:zapolgium_normal_fluid_pipe"]
        - [Microfluidic flow valve, "kubejs:uhv_microfluidic_flow_valve"]
        - [Zircalloy-4 rotor, "gtceu:zircalloy_4_rotor"]
    - [a2, "Assembly Line · 30 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [pu, UHV Electric Pump, x, "gtceu:uhv_electric_pump"]
    - - g3
      - |-
        2 motor · high strength panel · precision drive · 4 zalloy ring · router · 4608 mB perfluoroelastomer + fluids
      - g
      - functionalstorage:oak_1
      - - [High strength panel, "kubejs:uhv_high_strength_panel"]
        - [Precision drive mechanism, "kubejs:uhv_precision_drive_mechanism"]
    - [a3, "Assembly Line · 30 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [cv, UHV Conveyor Module, x, "gtceu:uhv_conveyor_module"]
    - - g4
      - motor · 2 panel · transmission assembly · zircalloy-4 gear · small zircalloy-4 gear · router + fluids
      - g
      - functionalstorage:oak_1
      - [[Zircalloy-4 gear, "gtceu:zircalloy_4_gear"], [Small zircalloy-4 gear, "gtceu:small_zircalloy_4_gear"]]
    - [a4, "Assembly Line · 30 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [pi, UHV Electric Piston, x, "gtceu:uhv_electric_piston"]
  e:
    - [g1, a1, "1"]
    - [a1, mo, "1 / 30 s"]
    - [mo, g2, "1"]
    - [mo, g3, "2"]
    - [mo, g4, "1"]
    - [g2, a2, "1"]
    - [a2, pu, "1 / 30 s"]
    - [g3, a3, "1"]
    - [a3, cv, "1 / 30 s"]
    - [g4, a4, "1"]
    - [a4, pi, "1 / 30 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/uhv_to_uiv_components.js (verified). Every UHV component is an Assembly Line recipe, 600 ticks at EU = VA[UV] = 491 520 EU/t, with STATION research of the UV item at 128 CWU/t (special ones 144) and 491 520 EU/t, and the fluids: 1152 mB ITLC solder (b2 = 72 x 2^4), 2000 mB lubricant (tungsten disulfide), 1152 mB naquadria (the tier fluid); the conveyor adds 4608 mB perfluoroelastomer rubber (1152 x 4). Instead of raw plates the recipes eat the component PARTS of uhv_parts / uhv_parts2.
    - |-
      Motor: 1 UHV super magnetic core + 2 long zalloy rods + 1 UHV transmission assembly + 64 fine zirconium wire + 1 UHV micropower router. Pump: 1 UHV motor + 1 zapolgium normal fluid pipe + 1 UHV microfluidic flow valve + 8 styrene butadiene rubber rings + 1 zircalloy-4 rotor + 1 router. Conveyor: 2 UHV motors + 1 high strength panel + 1 precision drive mechanism + 4 zalloy rings + 1 router. Piston: 1 UHV motor + 2 high strength panels + 1 transmission assembly + 1 zircalloy-4 gear + 1 small zircalloy-4 gear + 1 router. Fluid regulator: UHV pump + 2 UHV-tag circuits, assembler circuit 1, 50 ticks at EU x 4.
    - The Scanner and Station recipes from GT are replaced by the pack’s Component Synthesis Forge alternatives (research 320 CWU/t, 64 items per run, stabilized cleanroom, 48x inputs) which is the way to mass-produce these later.
    - |-
      Cost: 1 motor = 1 magnetic core + 1 transmission + 1 router + 64 fine zirconium wire (64 fine zirconium wire = 8 zirconium ingots = 64 titanite dust for the wire alone, see uhv_zirconium). A conveyor is 2 motors, a pump 1, a piston 1: expect 20 to 40 motors per full UHV machine set. The zirconium line is the bottleneck of the UHV era.
    - |-
      Sub-steps people skip: (1) the research item is the UV component, keep one UV motor/pump/conveyor/piston aside; (2) 128 CWU/t is more than the ZPM-era HPCA gives: Network Switch + 4 to 5 HPCAs; (3) motors first, they feed 7 of the other recipes; (4) tungsten disulfide as a fluid, 2000 mB each.
    - |-
      Unverified: tungsten disulfide fluid form, CWU total, UHV circuit tag for the regulator (any UHV tag circuit works).
  b:
    - ["gtceu:assembly_line", 4]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 2]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:uhv_super_magnetic_core
        - kubejs:uhv_micropower_router
        - gtceu:fine_zirconium_wire
      t: |-
        Drawers first, one per input: parts (magnetic cores, transmissions, routers, valves, panels, drive mechanisms), long zalloy rods, fine zirconium wire, SBR rings, zapolgium pipes, zircalloy rotors / gears, zalloy rings. Drums: ITLC solder, tungsten disulfide, naquadria, perfluoroelastomer.
    - i: ["gtceu:research_station", "gtceu:uv_electric_motor", "gtceu:data_module"]
      t: |-
        Research once per item: a UV motor / pump / conveyor / piston with a data module, 128 CWU/t at 491 520 EU/t. Modules into the matching Assembly Line.
    - i: ["gtceu:assembly_line", "gtceu:uhv_electric_motor"]
      t: |-
        Motor line first (30 s each, output drawer Keep Exact 8): every other UHV component and the machines take motors.
    - i: ["gtceu:assembly_line", "gtceu:uhv_electric_pump", "gtceu:uhv_conveyor_module"]
      t: |-
        Pump and conveyor lines: motors by router (1 and 2), parts by routers, rubber and fluids by hatches.
    - i: ["gtceu:assembly_line", "gtceu:uhv_electric_piston", "gtceu:uhv_fluid_regulator"]
      t: Piston line and the fluid regulator assembler (pump + 2 circuits).
    - i: ["functionalstorage:oak_1", "gtceu:uhv_electric_motor"]
      t: "Output drawers Keep Exact 4: motors 8."
---
# UHV components 1/2: motor, pump, conveyor module, piston and fluid regulator (Assembly Line, 30 s, 491 520 EU/t, research 128 CWU/t, component parts instead of raw metal)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_components` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV super magnetic core · 2 long zalloy rod · UHV transmission assembly · 64 fine zirconium wire · micropower router · 1152 mB solder · 2000 mB lubricant · 1152 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV super magnetic core · 2 long zalloy rod · UHV transmission assembly · 64 fine zirconium wire · micropower router · 1152 mB solder · 2000 mB lubricant · 1152 mB naquadria</span><span class="gt-sub"><span>Super magnetic core</span><span>Transmission assembly</span><span>Micropower router</span><span>Long zalloy rod</span><span>Fine zirconium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Electric Motor (gtceu:uhv_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="motor · zapolgium normal pipe · microfluidic flow valve · 8 SBR ring · zircalloy-4 rotor · router + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">motor · zapolgium normal pipe · microfluidic flow valve · 8 SBR ring · zircalloy-4 rotor · router + fluids</span><span class="gt-sub"><span>Zapolgium normal fluid pipe</span><span>Microfluidic flow valve</span><span>Zircalloy-4 rotor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Electric Pump (gtceu:uhv_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Electric Pump</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 motor · high strength panel · precision drive · 4 zalloy ring · router · 4608 mB perfluoroelastomer + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 motor · high strength panel · precision drive · 4 zalloy ring · router · 4608 mB perfluoroelastomer + fluids</span><span class="gt-sub"><span>High strength panel</span><span>Precision drive mechanism</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Conveyor Module (gtceu:uhv_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Conveyor Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="motor · 2 panel · transmission assembly · zircalloy-4 gear · small zircalloy-4 gear · router + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">motor · 2 panel · transmission assembly · zircalloy-4 gear · small zircalloy-4 gear · router + fluids</span><span class="gt-sub"><span>Zircalloy-4 gear</span><span>Small zircalloy-4 gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Electric Piston (gtceu:uhv_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 491 520 EU/t](#m-a1) → [Assembly Line · 30 s · 491 520 EU/t](#m-a2) (also Assembly Line · 30 s · 491 520 EU/t → [Assembly Line · 30 s · 491 520 EU/t](#m-a3), Assembly Line · 30 s · 491 520 EU/t → [Assembly Line · 30 s · 491 520 EU/t](#m-a4))
- [Assembly Line · 30 s · 491 520 EU/t](#m-a3)
- [Assembly Line · 30 s · 491 520 EU/t](#m-a4)

### Direct steps

- UHV Electric Motor → motor · zapolgium normal pipe · microfluidic flow valve · 8 SBR ring · zircalloy-4 rotor · router + fluids (1)
- UHV Electric Motor → 2 motor · high strength panel · precision drive · 4 zalloy ring · router · 4608 mB perfluoroelastomer + fluids (2)
- UHV Electric Motor → motor · 2 panel · transmission assembly · zircalloy-4 gear · small zircalloy-4 gear · router + fluids (1)

## How to build

1. Drawers first, one per input: parts (magnetic cores, transmissions, routers, valves, panels, drive mechanisms), long zalloy rods, fine zirconium wire, SBR rings, zapolgium pipes, zircalloy rotors / gears, zalloy rings. Drums: ITLC solder, tungsten disulfide, naquadria, perfluoroelastomer. — `functionalstorage:oak_1`, `kubejs:uhv_super_magnetic_core`, `kubejs:uhv_micropower_router`, `gtceu:fine_zirconium_wire`
2. Research once per item: a UV motor / pump / conveyor / piston with a data module, 128 CWU/t at 491 520 EU/t. Modules into the matching Assembly Line. — `gtceu:research_station`, `gtceu:uv_electric_motor`, `gtceu:data_module`
3. Motor line first (30 s each, output drawer Keep Exact 8): every other UHV component and the machines take motors. — `gtceu:assembly_line`, `gtceu:uhv_electric_motor`
4. Pump and conveyor lines: motors by router (1 and 2), parts by routers, rubber and fluids by hatches. — `gtceu:assembly_line`, `gtceu:uhv_electric_pump`, `gtceu:uhv_conveyor_module`
5. Piston line and the fluid regulator assembler (pump + 2 circuits). — `gtceu:assembly_line`, `gtceu:uhv_electric_piston`, `gtceu:uhv_fluid_regulator`
6. Output drawers Keep Exact 4: motors 8. — `functionalstorage:oak_1`, `gtceu:uhv_electric_motor`

## Tips

- Source: kjs additions/progression/components/uhv\_to\_uiv\_components.js (verified). Every UHV component is an Assembly Line recipe, 600 ticks at EU = VA\[UV\] = 491 520 EU/t, with STATION research of the UV item at 128 CWU/t (special ones 144) and 491 520 EU/t, and the fluids: 1152 mB ITLC solder (b2 = 72 x 2^4), 2000 mB lubricant (tungsten disulfide), 1152 mB naquadria (the tier fluid); the conveyor adds 4608 mB perfluoroelastomer rubber (1152 x 4). Instead of raw plates the recipes eat the component PARTS of uhv\_parts / uhv\_parts2.
- Motor: 1 UHV super magnetic core + 2 long zalloy rods + 1 UHV transmission assembly + 64 fine zirconium wire + 1 UHV micropower router. Pump: 1 UHV motor + 1 zapolgium normal fluid pipe + 1 UHV microfluidic flow valve + 8 styrene butadiene rubber rings + 1 zircalloy-4 rotor + 1 router. Conveyor: 2 UHV motors + 1 high strength panel + 1 precision drive mechanism + 4 zalloy rings + 1 router. Piston: 1 UHV motor + 2 high strength panels + 1 transmission assembly + 1 zircalloy-4 gear + 1 small zircalloy-4 gear + 1 router. Fluid regulator: UHV pump + 2 UHV-tag circuits, assembler circuit 1, 50 ticks at EU x 4.
- The Scanner and Station recipes from GT are replaced by the pack’s Component Synthesis Forge alternatives (research 320 CWU/t, 64 items per run, stabilized cleanroom, 48x inputs) which is the way to mass-produce these later.
- Cost: 1 motor = 1 magnetic core + 1 transmission + 1 router + 64 fine zirconium wire (64 fine zirconium wire = 8 zirconium ingots = 64 titanite dust for the wire alone, see uhv\_zirconium). A conveyor is 2 motors, a pump 1, a piston 1: expect 20 to 40 motors per full UHV machine set. The zirconium line is the bottleneck of the UHV era.
- Sub-steps people skip: (1) the research item is the UV component, keep one UV motor/pump/conveyor/piston aside; (2) 128 CWU/t is more than the ZPM-era HPCA gives: Network Switch + 4 to 5 HPCAs; (3) motors first, they feed 7 of the other recipes; (4) tungsten disulfide as a fluid, 2000 mB each.
- **Unverified** tungsten disulfide fluid form, CWU total, UHV circuit tag for the regulator (any UHV tag circuit works).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 4 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 2 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:uhv_electric_motor`, `gtceu:uhv_electric_pump`, `gtceu:uhv_conveyor_module`, `gtceu:uhv_electric_piston`, `gtceu:uhv_fluid_regulator`
