---
kind: chain
id: uv_components
order: 1660
data:
  t: |-
    UV components 1/2: electric motor, pump, conveyor module and piston (Assembly Line, 30 s, 122 880 EU/t, research 32 CWU/t, 576 mB naquadria each)
  inf: true
  "n":
    - - g1
      - |-
        1 long magnetic dysprosium rod · 4 long tritan steel rod · 4 tritan steel ring · 8 tritan steel round · 64 fine americium wire · 2 YBCO cable · 576 mB solder · 1000 mB lubricant · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Long magnetic dysprosium rod, "gtceu:long_magnetic_dysprosium_rod"]
        - [Long tritan steel rod, "gtceu:long_tritan_steel_rod"]
        - [Tritan steel ring, "gtceu:tritan_steel_ring"]
        - [Tritan steel round, "gtceu:tritan_steel_round"]
        - [Fine americium wire, "gtceu:fine_americium_wire"]
        - [YBCO cable, "gtceu:yttrium_barium_cuprate_single_cable"]
        - [Naquadria, "gtceu:naquadria_bucket"]
    - [a1, "Assembly Line · 30 s · 122 880 EU/t", m, "gtceu:assembly_line"]
    - [mo, UV Electric Motor, x, "gtceu:uv_electric_motor"]
    - - g2
      - |-
        1 motor · naquadah pipe · 2 tritan steel plate · 8 screw · 8 SBR ring · pure netherite rotor · 2 YBCO cable + fluids
      - g
      - functionalstorage:oak_1
      - - [Naquadah normal fluid pipe, "gtceu:naquadah_normal_fluid_pipe"]
        - [Tritan steel plate, "gtceu:tritan_steel_plate"]
        - [Tritan steel screw, "gtceu:tritan_steel_screw"]
        - [SBR ring, "gtceu:styrene_butadiene_rubber_ring"]
        - [Pure netherite rotor, "gtceu:pure_netherite_rotor"]
    - [a2, "Assembly Line · 30 s · 122 880 EU/t", m, "gtceu:assembly_line"]
    - [pu, UV Electric Pump, x, "gtceu:uv_electric_pump"]
    - - g3
      - |-
        2 motor · 2 plate · 4 ring · 16 round · 4 screw · 2 YBCO cable · 3456 mB SBR + fluids
      - g
      - functionalstorage:oak_1
      - [[Styrene butadiene rubber, "gtceu:styrene_butadiene_rubber_bucket"]]
    - [a3, "Assembly Line · 30 s · 122 880 EU/t", m, "gtceu:assembly_line"]
    - [cv, UV Conveyor Module, x, "gtceu:uv_conveyor_module"]
    - - g4
      - |-
        1 motor · 4 plate · 4 ring · 16 round · 4 rod · pure netherite gear · 2 small netherite gear · 2 YBCO cable + fluids
      - g
      - functionalstorage:oak_1
      - - [Pure netherite gear, "gtceu:pure_netherite_gear"]
        - [Small pure netherite gear, "gtceu:small_pure_netherite_gear"]
        - [Tritan steel rod, "gtceu:tritan_steel_rod"]
    - [a4, "Assembly Line · 30 s · 122 880 EU/t", m, "gtceu:assembly_line"]
    - [pi, UV Electric Piston, x, "gtceu:uv_electric_piston"]
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
      Source: kjs additions/progression/components/luv_to_uv_components.js with the UV values of utils/tier_data.js (verified): tritan steel (primary), pure netherite (secondary: rotor, gears), americium fine wire, YBCO cables, naquadah pipes, dysprosium magnets, SBR rubber, solder = indium tin lead cadmium soldering alloy, scaler 3 (fluids x 8). Every UV component is an Assembly Line recipe, 600 ticks (30 s), at VA[ZPM] = 122 880 EU/t, plus 576 mB MOLTEN NAQUADRIA (tier fluid, UV only), and a scanner-free STATION research of the ZPM version of the item at 32 CWU/t (122 880 EU/t) for motor, pump, conveyor, piston and robot arm; emitter, sensor and field generator need 48 CWU/t at 491 520 EU/t. The scanner recipes are removed.
    - |-
      Motor: 1 long magnetic dysprosium rod, 4 long tritan steel rods, 4 tritan steel rings, 8 tritan steel rounds, 64 fine americium wire (8 ingots), 2 YBCO single cables; fluids 576 mB solder, 1000 mB lubricant, 576 mB naquadria. Pump: 1 UV motor, 1 naquadah normal fluid pipe, 2 tritan steel plates, 8 tritan steel screws, 8 SBR rings, 1 pure netherite rotor, 2 YBCO cables; same fluids. Conveyor: 2 UV motors, 2 plates, 4 rings, 16 rounds, 4 screws, 2 cables; same fluids + 3456 mB styrene butadiene rubber. Piston: 1 UV motor, 4 plates, 4 rings, 16 rounds, 4 rods, 1 pure netherite gear, 2 small pure netherite gears, 2 cables; same fluids.
    - |-
      Alternatives with the same inputs: the Component Nexus (UHV multiblock, 300 ticks = half the time, stabilized cleanroom) and the Component Synthesis Forge (64 items per run from 48 times the inputs, needs a research of 320 CWU/t and a component data core; component_part_synthesis for the SMDs). Both are UHV-era; the Assembly Line is the UV way.
    - |-
      Cost (ingot equivalents): motor = 8 americium ingots + about 6 tritan steel ingots + 2 YBCO cables; pump adds 1 motor + a pure netherite rotor; conveyor is 2 motors; piston 1 motor. Americium comes from fusion (uv_fusion_mats), pure netherite from the netherite line (nether lines; Unverified route), tritan steel from the ABS (uv_alloys). A single machine of a tier needs 2 motors, 1 pump, 1 conveyor or so: the americium bill alone makes the UV machines a fusion-reactor project.
    - |-
      Sub-steps people skip: (1) naquadria is a FLUID input 576 mB on every recipe (it is also the neutronium feed); (2) one dedicated Assembly Line per product, motors made first and kept in a drawer Keep Exact 4 (the pump needs 1, conveyor 2, piston 1, every other component 1 to 2); (3) the four research items (ZPM motor, pump, conveyor, piston) are scanned in the Research Station: keep one ZPM version of each; (4) a second pair of Data Access Hatches or one Data Bank stores the orbs.
    - |-
      Unverified: pure netherite and dysprosium sources; whether the Assembly Line at 122 880 EU/t needs a ZPM hatch exactly (a ZPM energy hatch runs it).
  b:
    - ["gtceu:assembly_line", 4]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:zpm_energy_input_hatch", 2]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:tritan_steel_ring
        - gtceu:fine_americium_wire
        - gtceu:pure_netherite_rotor
      t: |-
        Drawers first, one per input: long magnetic dysprosium rods, long rods, rings, rounds, plates, screws, rods, fine americium wire, YBCO cables, naquadah pipes, SBR rings, pure netherite rotors / gears / small gears, motors. Drums: ITLC solder, lubricant, naquadria, SBR. One Assembly Line per product, each with its own Data Access Hatch loaded with the matching research orb.
    - i: ["gtceu:research_station", "gtceu:zpm_electric_motor", "gtceu:data_orb"]
      t: |-
        Research each ZPM item once: orb + ZPM motor in the Object Holder, 32 CWU/t at 122 880 EU/t; repeat for the pump, conveyor and piston. Orbs into the matching Assembly Line’s hatch (or a Data Bank).
    - i: ["gtceu:assembly_line", "gtceu:uv_electric_motor"]
      t: |-
        Motor line first: buses in recipe order (rod, long rods, rings, rounds, fine wire, cables), fluids by hatches. 30 s each; output drawer Keep Exact 8: every other component eats motors.
    - i: ["gtceu:assembly_line", "gtceu:uv_electric_pump", "gtceu:uv_conveyor_module"]
      t: |-
        Pump and conveyor lines: motors by router from the drawer (1 and 2), their own parts by routers; conveyor also needs 3456 mB SBR on its own fluid hatch.
    - i: ["gtceu:assembly_line", "gtceu:uv_electric_piston"]
      t: |-
        Piston line: motor + plates + rings + rounds + rods + the pure netherite gear and two small gears. All four share the naquadria drum through Pipez pipes with valves.
    - i: ["functionalstorage:oak_1", "gtceu:uv_electric_motor"]
      t: |-
        Output drawers Keep Exact 4: motors 8. Machines, hatches and every UV multiblock take them from here.
---
# UV components 1/2: electric motor, pump, conveyor module and piston (Assembly Line, 30 s, 122 880 EU/t, research 32 CWU/t, 576 mB naquadria each)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_components` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV components and hatches](../../plan/p16.md#uvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 long magnetic dysprosium rod · 4 long tritan steel rod · 4 tritan steel ring · 8 tritan steel round · 64 fine americium wire · 2 YBCO cable · 576 mB solder · 1000 mB lubricant · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 long magnetic dysprosium rod · 4 long tritan steel rod · 4 tritan steel ring · 8 tritan steel round · 64 fine americium wire · 2 YBCO cable · 576 mB solder · 1000 mB lubricant · 576 mB naquadria</span><span class="gt-sub"><span>Long magnetic dysprosium rod</span><span>Long tritan steel rod</span><span>Tritan steel ring</span><span>Tritan steel round</span><span>Fine americium wire</span><span>YBCO cable</span><span>Naquadria</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Electric Motor (gtceu:uv_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Electric Motor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 motor · naquadah pipe · 2 tritan steel plate · 8 screw · 8 SBR ring · pure netherite rotor · 2 YBCO cable + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 motor · naquadah pipe · 2 tritan steel plate · 8 screw · 8 SBR ring · pure netherite rotor · 2 YBCO cable + fluids</span><span class="gt-sub"><span>Naquadah normal fluid pipe</span><span>Tritan steel plate</span><span>Tritan steel screw</span><span>SBR ring</span><span>Pure netherite rotor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Electric Pump (gtceu:uv_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Electric Pump</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 motor · 2 plate · 4 ring · 16 round · 4 screw · 2 YBCO cable · 3456 mB SBR + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 motor · 2 plate · 4 ring · 16 round · 4 screw · 2 YBCO cable · 3456 mB SBR + fluids</span><span class="gt-sub"><span>Styrene butadiene rubber</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Conveyor Module (gtceu:uv_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Conveyor Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 motor · 4 plate · 4 ring · 16 round · 4 rod · pure netherite gear · 2 small netherite gear · 2 YBCO cable + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 motor · 4 plate · 4 ring · 16 round · 4 rod · pure netherite gear · 2 small netherite gear · 2 YBCO cable + fluids</span><span class="gt-sub"><span>Pure netherite gear</span><span>Small pure netherite gear</span><span>Tritan steel rod</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Electric Piston (gtceu:uv_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 122 880 EU/t](#m-a1) → [Assembly Line · 30 s · 122 880 EU/t](#m-a2) (also Assembly Line · 30 s · 122 880 EU/t → [Assembly Line · 30 s · 122 880 EU/t](#m-a3), Assembly Line · 30 s · 122 880 EU/t → [Assembly Line · 30 s · 122 880 EU/t](#m-a4))
- [Assembly Line · 30 s · 122 880 EU/t](#m-a3)
- [Assembly Line · 30 s · 122 880 EU/t](#m-a4)

### Direct steps

- UV Electric Motor → 1 motor · naquadah pipe · 2 tritan steel plate · 8 screw · 8 SBR ring · pure netherite rotor · 2 YBCO cable + fluids (1)
- UV Electric Motor → 2 motor · 2 plate · 4 ring · 16 round · 4 screw · 2 YBCO cable · 3456 mB SBR + fluids (2)
- UV Electric Motor → 1 motor · 4 plate · 4 ring · 16 round · 4 rod · pure netherite gear · 2 small netherite gear · 2 YBCO cable + fluids (1)

## How to build

1. Drawers first, one per input: long magnetic dysprosium rods, long rods, rings, rounds, plates, screws, rods, fine americium wire, YBCO cables, naquadah pipes, SBR rings, pure netherite rotors / gears / small gears, motors. Drums: ITLC solder, lubricant, naquadria, SBR. One Assembly Line per product, each with its own Data Access Hatch loaded with the matching research orb. — `functionalstorage:oak_1`, `gtceu:tritan_steel_ring`, `gtceu:fine_americium_wire`, `gtceu:pure_netherite_rotor`
2. Research each ZPM item once: orb + ZPM motor in the Object Holder, 32 CWU/t at 122 880 EU/t; repeat for the pump, conveyor and piston. Orbs into the matching Assembly Line’s hatch (or a Data Bank). — `gtceu:research_station`, `gtceu:zpm_electric_motor`, `gtceu:data_orb`
3. Motor line first: buses in recipe order (rod, long rods, rings, rounds, fine wire, cables), fluids by hatches. 30 s each; output drawer Keep Exact 8: every other component eats motors. — `gtceu:assembly_line`, `gtceu:uv_electric_motor`
4. Pump and conveyor lines: motors by router from the drawer (1 and 2), their own parts by routers; conveyor also needs 3456 mB SBR on its own fluid hatch. — `gtceu:assembly_line`, `gtceu:uv_electric_pump`, `gtceu:uv_conveyor_module`
5. Piston line: motor + plates + rings + rounds + rods + the pure netherite gear and two small gears. All four share the naquadria drum through Pipez pipes with valves. — `gtceu:assembly_line`, `gtceu:uv_electric_piston`
6. Output drawers Keep Exact 4: motors 8. Machines, hatches and every UV multiblock take them from here. — `functionalstorage:oak_1`, `gtceu:uv_electric_motor`

## Tips

- Source: kjs additions/progression/components/luv\_to\_uv\_components.js with the UV values of utils/tier\_data.js (verified): tritan steel (primary), pure netherite (secondary: rotor, gears), americium fine wire, YBCO cables, naquadah pipes, dysprosium magnets, SBR rubber, solder = indium tin lead cadmium soldering alloy, scaler 3 (fluids x 8). Every UV component is an Assembly Line recipe, 600 ticks (30 s), at VA\[ZPM\] = 122 880 EU/t, plus 576 mB MOLTEN NAQUADRIA (tier fluid, UV only), and a scanner-free STATION research of the ZPM version of the item at 32 CWU/t (122 880 EU/t) for motor, pump, conveyor, piston and robot arm; emitter, sensor and field generator need 48 CWU/t at 491 520 EU/t. The scanner recipes are removed.
- Motor: 1 long magnetic dysprosium rod, 4 long tritan steel rods, 4 tritan steel rings, 8 tritan steel rounds, 64 fine americium wire (8 ingots), 2 YBCO single cables; fluids 576 mB solder, 1000 mB lubricant, 576 mB naquadria. Pump: 1 UV motor, 1 naquadah normal fluid pipe, 2 tritan steel plates, 8 tritan steel screws, 8 SBR rings, 1 pure netherite rotor, 2 YBCO cables; same fluids. Conveyor: 2 UV motors, 2 plates, 4 rings, 16 rounds, 4 screws, 2 cables; same fluids + 3456 mB styrene butadiene rubber. Piston: 1 UV motor, 4 plates, 4 rings, 16 rounds, 4 rods, 1 pure netherite gear, 2 small pure netherite gears, 2 cables; same fluids.
- Alternatives with the same inputs: the Component Nexus (UHV multiblock, 300 ticks = half the time, stabilized cleanroom) and the Component Synthesis Forge (64 items per run from 48 times the inputs, needs a research of 320 CWU/t and a component data core; component\_part\_synthesis for the SMDs). Both are UHV-era; the Assembly Line is the UV way.
- Cost (ingot equivalents): motor = 8 americium ingots + about 6 tritan steel ingots + 2 YBCO cables; pump adds 1 motor + a pure netherite rotor; conveyor is 2 motors; piston 1 motor. Americium comes from fusion (uv\_fusion\_mats), pure netherite from the netherite line (nether lines; Unverified route), tritan steel from the ABS (uv\_alloys). A single machine of a tier needs 2 motors, 1 pump, 1 conveyor or so: the americium bill alone makes the UV machines a fusion-reactor project.
- Sub-steps people skip: (1) naquadria is a FLUID input 576 mB on every recipe (it is also the neutronium feed); (2) one dedicated Assembly Line per product, motors made first and kept in a drawer Keep Exact 4 (the pump needs 1, conveyor 2, piston 1, every other component 1 to 2); (3) the four research items (ZPM motor, pump, conveyor, piston) are scanned in the Research Station: keep one ZPM version of each; (4) a second pair of Data Access Hatches or one Data Bank stores the orbs.
- **Unverified** pure netherite and dysprosium sources; whether the Assembly Line at 122 880 EU/t needs a ZPM hatch exactly (a ZPM energy hatch runs it).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 4 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:zpm_energy_input_hatch` | 2 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:uv_electric_motor`, `gtceu:uv_electric_pump`, `gtceu:uv_conveyor_module`, `gtceu:uv_electric_piston`, `gtceu:fine_americium_wire`
