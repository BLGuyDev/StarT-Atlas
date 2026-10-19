---
kind: chain
id: uv_multis
order: 1720
data:
  t: |-
    UV multiblock controllers (Assembly Line): Mega Vacuum Freezer, Chemical Plant, Advanced Synthesis Plant, Titan Forge - all gated on UV circuits, UV components and 24 to 64 CWU/t research
  inf: true
  "n":
    - - g1
      - aluminium frame · 2 UV circuit · 4 dense rhodium plated palladium plate · 2 LuV field generator · 4 NbTi normal pipe · 32 fine ITBTC wire · 6 HSS-E screw · 1152 mB solder
      - g
      - functionalstorage:oak_1
      - - [Aluminium frame, "gtceu:aluminium_frame"]
        - [Dense Rh-Pd plate, "gtceu:dense_rhodium_plated_palladium_plate"]
        - [LuV field generator, "gtceu:luv_field_generator"]
        - [NbTi normal fluid pipe, "gtceu:niobium_titanium_normal_fluid_pipe"]
    - [a1, "Assembly Line · 20 s · 245 760 EU/t · research Super Vacuum Freezer 24 CWU/t", m, "gtceu:assembly_line"]
    - [o1, Mega Vacuum Freezer, o, "gtceu:mega_vacuum_freezer"]
    - - g2
      - ZPM hull · 4 ZPM motor · naquadah alloy rotor · 2 large NbTi pipe · 4 UV circuit · 1872 mB solder · 288 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [ZPM Machine Hull, "gtceu:zpm_machine_hull"]
        - [ZPM motor, "gtceu:zpm_electric_motor"]
        - [Naquadah alloy rotor, "gtceu:naquadah_alloy_rotor"]
        - [Large NbTi pipe, "gtceu:niobium_titanium_large_fluid_pipe"]
    - - a2
      - Assembly Line · 60 s · 983 040 EU/t · research Large Chemical Reactor 64 CWU/t
      - m
      - gtceu:assembly_line
    - [o2, Chemical Plant, o, "gtceu:chemical_plant"]
    - - g3
      - ZPM hull · 4 sensor · 4 arm · 4 fluid regulator · 2 naquadah alloy rotor · 6 large NbTi pipe · 6 UV circuit · 1872 mB solder · 288 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [ZPM sensor, "gtceu:zpm_sensor"]
        - [ZPM robot arm, "gtceu:zpm_robot_arm"]
        - [ZPM fluid regulator, "gtceu:zpm_fluid_regulator"]
    - [a3, "Assembly Line · 60 s · 983 040 EU/t · research ZPM Chemical Reactor 64 CWU/t", m, "gtceu:assembly_line"]
    - [o3, Advanced Synthesis Plant, o, "gtceu:advanced_synthesis_plant"]
    - - g4
      - UV hull · 12 UV circuit · 4 dense tritan steel plate · 64 UHPIC · 8 UV piston · 4 small pure netherite gear · 2 quadruple enriched naquadah pipe · 4 UV pump · 7200 mB solder · 5 B lubricant · 864 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [UV piston, "gtceu:uv_electric_piston"]
        - [UV pump, "gtceu:uv_electric_pump"]
        - [Dense tritan steel plate, "gtceu:dense_tritan_steel_plate"]
    - [a4, "Assembly Line · 80 s · 245 760 EU/t · research Large Extruder 64 CWU/t", m, "gtceu:assembly_line"]
    - [o4, Titan Forge, o, "gtceu:titan_forge"]
  e:
    - [g1, a1, "1"]
    - [a1, o1, "1 / 20 s"]
    - [g2, a2, "1"]
    - [a2, o2, "1 / 60 s"]
    - [g3, a3, "1"]
    - [a3, o3, "1 / 60 s"]
    - [g4, a4, "1"]
    - [a4, o4, "1 / 80 s"]
  tips:
    - |-
      Source: kjs additions/machines_and_parts/large_multis.js and additions/multiblock_recipes/abydos_multis.js (verified). Mega Vacuum Freezer = Bulk Blast Chiller [BBC] (UV, as the era says; a GCYM multi with parallel hatch and batch mode): AL 400 ticks at VHA[UV] = 245 760 EU/t, STATION research of the Super Vacuum Freezer at 24 CWU/t and VHA[ZPM] = 61 440 EU/t (so the Super Vacuum Freezer = Arctic Chilling Unit, an IV recipe, must be kept as the scan item). Chemical Plant: ZPM hull + 4 ZPM motors + naquadah alloy rotor + 2 NbTi large pipes + 4 UV circuits, 1872 mB soldering alloy + 288 mB naquadria, 1200 ticks at VHA[UHV] = 983 040 EU/t, research Large Chemical Reactor 64 CWU/t at VHA[UV]. Advanced Synthesis Plant: ZPM hull + 4 sensors + 4 robot arms + 4 fluid regulators + 2 rotors + 6 large pipes + 6 UV circuits, same fluids, same 1200 ticks / 983 040 EU/t, research ZPM Chemical Reactor 64 CWU/t. Titan Forge: UV hull + 12 UV circuits + 4 dense tritan steel plates + 64 UHPIC + 8 UV pistons + 4 small pure netherite gears + 2 quadruple enriched naquadah pipes + 4 UV pumps; 7200 mB solder + 5 B lubricant + 864 mB naquadria, 1600 ticks at VHA[UV], research Large Extruder 64 CWU/t at VA[ZPM].
    - |-
      Power gate: 983 040 EU/t is above one UV hatch (524 288 EU/t): the Assembly Line needs a UV 4A hatch (2 097 152 EU/t) for the Chemical Plant and the Advanced Synthesis Plant; the Mega Vacuum Freezer and the Titan Forge (245 760 EU/t) are UV-tier recipes (EUtVHA(UV) is above the ZPM voltage): a UV hatch, or a ZPM 4A hatch with the same total. The UV chemistry multis are therefore at the END of the UV era; do the Mega Vacuum Freezer first (it only needs 2 UV circuits).
    - |-
      Circuits: Mega Vacuum Freezer 2 UV, Chemical Plant 4, Advanced Synthesis Plant 6, Titan Forge 12 UV; with the crystal route (zpm_uv_circuit) each UV circuit is 2 crystal computers. Components: Chemical Plant 4 ZPM motors (zpm_components), Advanced Synthesis Plant 4 ZPM sensors + 4 robot arms + 4 ZPM fluid regulators (the regulator is a ZPM pump-like item: Unverified recipe), Titan Forge 8 UV pistons + 4 UV pumps (uv_components) - so the Titan Forge is the first UV-component customer.
    - |-
      What they do: the Chemical Plant and Advanced Synthesis Plant are the pack’s multi-step chemistry (ordered_chemistry / chemical_skip recipes in kjs multiblock_recipes/chemical_plant.js: several reactions in one operation, e.g. skip recipes for mutagen, silicon carbide, tungsten from scheelite); the Mega Vacuum Freezer is a bigger vacuum freezer for hot ingots; the Titan Forge is the large extruder for UV-tier shaping (Unverified recipes). The tooltips in game list their recipe types.
    - |-
      Sub-steps people skip: (1) the research item for the chemical plant is the large chemical reactor you already have: keep one aside; (2) naquadria is again a fluid input (288 mB); (3) UHPIC chips: 64 per Titan Forge; (4) build the UV 4A hatch before queuing the Chemical Plant; (5) the Network Hub (4 UHV circuits, 4 UV emitters + 4 UV sensors, 32 double RTAN wire) is the UHV research aggregator, not needed now.
    - |-
      Unverified: ZPM fluid regulator recipe, what each multi’s recipe types contain, and CWU totals.
  b:
    - ["gtceu:assembly_line", 4]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 1]
    - ["gtceu:zpm_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:aluminium_frame", "gtceu:uv_machine_hull", "gtceu:zpm_machine_hull"]
      t: |-
        Drawers first, one per input: frames, hulls, UV circuits (Keep Exact per recipe), field generators, motors, rotors, pipes, fine wire, screws, pistons, pumps, gears, UHPIC chips. Drums: soldering alloy, naquadria, lubricant. One Assembly Line per product, each with its own Data Access Hatch for its research orb.
    - i: ["gtceu:research_station", "gtceu:super_vacuum_freezer", "gtceu:data_orb"]
      t: |-
        Research per multi: orb + scan item in the Object Holder (Super Vacuum Freezer 24 CWU/t, Large Chemical Reactor 64, ZPM chemical reactor 64, Large Extruder 64). Check the CWU/t readout first (uv_research).
    - i: ["gtceu:assembly_line", "gtceu:mega_vacuum_freezer"]
      t: |-
        Mega Vacuum Freezer first: buses in recipe order (frame, 2 UV circuits, 4 dense plates, 2 LuV field generators, pipes, wire, screws), solder by hatch; 20 s at 245 760 EU/t.
    - i: ["gtceu:assembly_line", "gtceu:chemical_plant", "gtceu:advanced_synthesis_plant"]
      t: |-
        Chemical Plant and Advanced Synthesis Plant on a UV 4A hatch (983 040 EU/t, 60 s each): hull, motors/sensors/arms, rotors, large pipes, UV circuits; solder + naquadria by hatches.
    - i: ["gtceu:assembly_line", "gtceu:titan_forge"]
      t: |-
        Titan Forge: UV hull, 12 UV circuits, plates, 64 UHPIC, 8 pistons, gears, pipes, 4 pumps; 7200 mB solder, 5 B lubricant, 864 mB naquadria; 80 s at 245 760 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:chemical_plant"]
      t: |-
        Output drawers Keep Exact 1 per controller. These multis also take their recipe-casing blocks: read each controller’s structure preview before you craft casings.
---
# UV multiblock controllers (Assembly Line): Mega Vacuum Freezer, Chemical Plant, Advanced Synthesis Plant, Titan Forge - all gated on UV circuits, UV components and 24 to 64 CWU/t research

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_multis` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV multiblock controllers](../../plan/p16.md#uvmultis)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 245 760 EU/t · research Super Vacuum Freezer 24 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="aluminium frame · 2 UV circuit · 4 dense rhodium plated palladium plate · 2 LuV field generator · 4 NbTi normal pipe · 32 fine ITBTC wire · 6 HSS-E screw · 1152 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">aluminium frame · 2 UV circuit · 4 dense rhodium plated palladium plate · 2 LuV field generator · 4 NbTi normal pipe · 32 fine ITBTC wire · 6 HSS-E screw · 1152 mB solder</span><span class="gt-sub"><span>Aluminium frame</span><span>Dense Rh-Pd plate</span><span>LuV field generator</span><span>NbTi normal fluid pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mega Vacuum Freezer (gtceu:mega_vacuum_freezer) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__mega_vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mega Vacuum Freezer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 983 040 EU/t · research Large Chemical Reactor 64 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 4 ZPM motor · naquadah alloy rotor · 2 large NbTi pipe · 4 UV circuit · 1872 mB solder · 288 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 4 ZPM motor · naquadah alloy rotor · 2 large NbTi pipe · 4 UV circuit · 1872 mB solder · 288 mB naquadria</span><span class="gt-sub"><span>ZPM Machine Hull</span><span>ZPM motor</span><span>Naquadah alloy rotor</span><span>Large NbTi pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Chemical Plant (gtceu:chemical_plant) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__chemical_plant.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chemical Plant</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 983 040 EU/t · research ZPM Chemical Reactor 64 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 4 sensor · 4 arm · 4 fluid regulator · 2 naquadah alloy rotor · 6 large NbTi pipe · 6 UV circuit · 1872 mB solder · 288 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 4 sensor · 4 arm · 4 fluid regulator · 2 naquadah alloy rotor · 6 large NbTi pipe · 6 UV circuit · 1872 mB solder · 288 mB naquadria</span><span class="gt-sub"><span>ZPM sensor</span><span>ZPM robot arm</span><span>ZPM fluid regulator</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Advanced Synthesis Plant (gtceu:advanced_synthesis_plant) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_synthesis_plant.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Synthesis Plant</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 80 s · 245 760 EU/t · research Large Extruder 64 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · 12 UV circuit · 4 dense tritan steel plate · 64 UHPIC · 8 UV piston · 4 small pure netherite gear · 2 quadruple enriched naquadah pipe · 4 UV pump · 7200 mB solder · 5 B lubricant · 864 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · 12 UV circuit · 4 dense tritan steel plate · 64 UHPIC · 8 UV piston · 4 small pure netherite gear · 2 quadruple enriched naquadah pipe · 4 UV pump · 7200 mB solder · 5 B lubricant · 864 mB naquadria</span><span class="gt-sub"><span>UV Machine Hull</span><span>UV piston</span><span>UV pump</span><span>Dense tritan steel plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">80 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Titan Forge (gtceu:titan_forge) - 1 / 80 s"><img class="gt-ico" src="../../assets/icons/gtceu__titan_forge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titan Forge</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 245 760 EU/t · research Super Vacuum Freezer 24 CWU/t](#m-a1)
- [Assembly Line · 60 s · 983 040 EU/t · research Large Chemical Reactor 64 CWU/t](#m-a2)
- [Assembly Line · 60 s · 983 040 EU/t · research ZPM Chemical Reactor 64 CWU/t](#m-a3)
- [Assembly Line · 80 s · 245 760 EU/t · research Large Extruder 64 CWU/t](#m-a4)

## How to build

1. Drawers first, one per input: frames, hulls, UV circuits (Keep Exact per recipe), field generators, motors, rotors, pipes, fine wire, screws, pistons, pumps, gears, UHPIC chips. Drums: soldering alloy, naquadria, lubricant. One Assembly Line per product, each with its own Data Access Hatch for its research orb. — `functionalstorage:oak_1`, `gtceu:aluminium_frame`, `gtceu:uv_machine_hull`, `gtceu:zpm_machine_hull`
2. Research per multi: orb + scan item in the Object Holder (Super Vacuum Freezer 24 CWU/t, Large Chemical Reactor 64, ZPM chemical reactor 64, Large Extruder 64). Check the CWU/t readout first (uv\_research). — `gtceu:research_station`, `gtceu:super_vacuum_freezer`, `gtceu:data_orb`
3. Mega Vacuum Freezer first: buses in recipe order (frame, 2 UV circuits, 4 dense plates, 2 LuV field generators, pipes, wire, screws), solder by hatch; 20 s at 245 760 EU/t. — `gtceu:assembly_line`, `gtceu:mega_vacuum_freezer`
4. Chemical Plant and Advanced Synthesis Plant on a UV 4A hatch (983 040 EU/t, 60 s each): hull, motors/sensors/arms, rotors, large pipes, UV circuits; solder + naquadria by hatches. — `gtceu:assembly_line`, `gtceu:chemical_plant`, `gtceu:advanced_synthesis_plant`
5. Titan Forge: UV hull, 12 UV circuits, plates, 64 UHPIC, 8 pistons, gears, pipes, 4 pumps; 7200 mB solder, 5 B lubricant, 864 mB naquadria; 80 s at 245 760 EU/t. — `gtceu:assembly_line`, `gtceu:titan_forge`
6. Output drawers Keep Exact 1 per controller. These multis also take their recipe-casing blocks: read each controller’s structure preview before you craft casings. — `functionalstorage:oak_1`, `gtceu:chemical_plant`

## Tips

- Source: kjs additions/machines\_and\_parts/large\_multis.js and additions/multiblock\_recipes/abydos\_multis.js (verified). Mega Vacuum Freezer = Bulk Blast Chiller \[BBC\] (UV, as the era says; a GCYM multi with parallel hatch and batch mode): AL 400 ticks at VHA\[UV\] = 245 760 EU/t, STATION research of the Super Vacuum Freezer at 24 CWU/t and VHA\[ZPM\] = 61 440 EU/t (so the Super Vacuum Freezer = Arctic Chilling Unit, an IV recipe, must be kept as the scan item). Chemical Plant: ZPM hull + 4 ZPM motors + naquadah alloy rotor + 2 NbTi large pipes + 4 UV circuits, 1872 mB soldering alloy + 288 mB naquadria, 1200 ticks at VHA\[UHV\] = 983 040 EU/t, research Large Chemical Reactor 64 CWU/t at VHA\[UV\]. Advanced Synthesis Plant: ZPM hull + 4 sensors + 4 robot arms + 4 fluid regulators + 2 rotors + 6 large pipes + 6 UV circuits, same fluids, same 1200 ticks / 983 040 EU/t, research ZPM Chemical Reactor 64 CWU/t. Titan Forge: UV hull + 12 UV circuits + 4 dense tritan steel plates + 64 UHPIC + 8 UV pistons + 4 small pure netherite gears + 2 quadruple enriched naquadah pipes + 4 UV pumps; 7200 mB solder + 5 B lubricant + 864 mB naquadria, 1600 ticks at VHA\[UV\], research Large Extruder 64 CWU/t at VA\[ZPM\].
- Power gate: 983 040 EU/t is above one UV hatch (524 288 EU/t): the Assembly Line needs a UV 4A hatch (2 097 152 EU/t) for the Chemical Plant and the Advanced Synthesis Plant; the Mega Vacuum Freezer and the Titan Forge (245 760 EU/t) are UV-tier recipes (EUtVHA(UV) is above the ZPM voltage): a UV hatch, or a ZPM 4A hatch with the same total. The UV chemistry multis are therefore at the END of the UV era; do the Mega Vacuum Freezer first (it only needs 2 UV circuits).
- Circuits: Mega Vacuum Freezer 2 UV, Chemical Plant 4, Advanced Synthesis Plant 6, Titan Forge 12 UV; with the crystal route (zpm\_uv\_circuit) each UV circuit is 2 crystal computers. Components: Chemical Plant 4 ZPM motors (zpm\_components), Advanced Synthesis Plant 4 ZPM sensors + 4 robot arms + 4 ZPM fluid regulators (the regulator is a ZPM pump-like item: Unverified recipe), Titan Forge 8 UV pistons + 4 UV pumps (uv\_components) - so the Titan Forge is the first UV-component customer.
- What they do: the Chemical Plant and Advanced Synthesis Plant are the pack’s multi-step chemistry (ordered\_chemistry / chemical\_skip recipes in kjs multiblock\_recipes/chemical\_plant.js: several reactions in one operation, e.g. skip recipes for mutagen, silicon carbide, tungsten from scheelite); the Mega Vacuum Freezer is a bigger vacuum freezer for hot ingots; the Titan Forge is the large extruder for UV-tier shaping (Unverified recipes). The tooltips in game list their recipe types.
- Sub-steps people skip: (1) the research item for the chemical plant is the large chemical reactor you already have: keep one aside; (2) naquadria is again a fluid input (288 mB); (3) UHPIC chips: 64 per Titan Forge; (4) build the UV 4A hatch before queuing the Chemical Plant; (5) the Network Hub (4 UHV circuits, 4 UV emitters + 4 UV sensors, 32 double RTAN wire) is the UHV research aggregator, not needed now.
- **Unverified** ZPM fluid regulator recipe, what each multi’s recipe types contain, and CWU totals.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 4 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 1 |
| `gtceu:zpm_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:mega_vacuum_freezer`, `gtceu:chemical_plant`, `gtceu:advanced_synthesis_plant`, `gtceu:titan_forge`
