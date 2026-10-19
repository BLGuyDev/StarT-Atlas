---
kind: chain
id: uev_parts
order: 1990
data:
  t: |-
    UEV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve
  inf: true
  "n":
    - - g0
      - |-
        Voltage Coil: 1 mythrolic alloy tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine aurourium wire · 1 250 mB superstate helium 3
      - g
      - functionalstorage:oak_1
      - - [mythrolic alloy tiny fluid pipe, "gtceu:mythrolic_alloy_tiny_fluid_pipe"]
        - [long magnetic zapolgium rod, "gtceu:long_magnetic_zapolgium_rod"]
        - [fine aurourium wire, "gtceu:fine_aurourium_wire"]
    - - g1
      - |-
        Computational Matrix: 1 starium alloy frame · 1 UEV circuit · 2 UHV circuit · 3 UV circuit · 4 cerium tritelluride single cable · 4 starium alloy bolt · 4 608 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [starium alloy frame, "gtceu:starium_alloy_frame"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [UV circuit, "kubejs:uv_universal_circuit"]
        - [cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]
        - [starium alloy bolt, "gtceu:starium_alloy_bolt"]
    - - g2
      - |-
        Transmission Assembly: 1 mythrolic alloy frame · 1 uhv electric motor · 2 starium alloy rod · 2 starium alloy ring · 4 starium alloy round · 16 fine adamantine wire · 4 000 mB tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [mythrolic alloy frame, "gtceu:mythrolic_alloy_frame"]
        - [uhv electric motor, "gtceu:uhv_electric_motor"]
        - [starium alloy rod, "gtceu:starium_alloy_rod"]
        - [starium alloy ring, "gtceu:starium_alloy_ring"]
        - [starium alloy round, "gtceu:starium_alloy_round"]
        - [fine adamantine wire, "gtceu:fine_adamantine_wire"]
    - - g3
      - |-
        Precision Drive Mechanism: 1 starium alloy frame · 1 uhv electric motor · 1 UHV circuit · 1 magmada alloy gear · 1 small starium alloy gear · 8 starium alloy round · 4 000 mB tungsten disulfide · 2 880 mB perfluoroelastomer rubber
      - g
      - functionalstorage:oak_1
      - - [starium alloy frame, "gtceu:starium_alloy_frame"]
        - [uhv electric motor, "gtceu:uhv_electric_motor"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [magmada alloy gear, "gtceu:magmada_alloy_gear"]
        - [small starium alloy gear, "gtceu:small_starium_alloy_gear"]
        - [starium alloy round, "gtceu:starium_alloy_round"]
    - - g4
      - |-
        Microfluidic Flow Valve: 1 uhv fluid regulator · 1 mythrolic alloy small fluid pipe · 2 starium alloy plate · 4 starium alloy round · 4 styrene butadiene rubber ring · 2 starium alloy ring · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [uhv fluid regulator, "gtceu:uhv_fluid_regulator"]
        - [mythrolic alloy small fluid pipe, "gtceu:mythrolic_alloy_small_fluid_pipe"]
        - [starium alloy plate, "gtceu:starium_alloy_plate"]
        - [starium alloy round, "gtceu:starium_alloy_round"]
        - [styrene butadiene rubber ring, "gtceu:styrene_butadiene_rubber_ring"]
        - [starium alloy ring, "gtceu:starium_alloy_ring"]
    - - cpa
      - Component Part Assembly · 7 864 320 EU/t · station research of the UHV part
      - m
      - gtceu:component_part_assembly
    - [o0, UEV Voltage Coil, x, "kubejs:uev_voltage_coil"]
    - [o1, UEV Computational Matrix, x, "kubejs:uev_computational_matrix"]
    - [o2, UEV Transmission Assembly, x, "kubejs:uev_transmission_assembly"]
    - [o3, UEV Precision Drive Mechanism, x, "kubejs:uev_precision_drive_mechanism"]
    - [o4, UEV Microfluidic Flow Valve, o, "kubejs:uev_microfluidic_flow_valve"]
  e:
    - [g0, cpa, "10 s"]
    - [g1, cpa, "20 s"]
    - [g2, cpa, "16 s"]
    - [g3, cpa, "24 s"]
    - [g4, cpa, "16 s"]
    - [cpa, o0, "1 / 10 s"]
    - [cpa, o1, "1 / 20 s"]
    - [cpa, o2, "1 / 16 s"]
    - [cpa, o3, "1 / 24 s"]
    - [cpa, o4, "1 / 16 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/component_parts.js (componentPart(), tier uev; materials in utils/tier_data.js). Every part is a Component Part Assembly recipe (gtceu:component_part_assembly) at 7 864 320 EU/t, with STATION research of the same part of the UHV tier at 1 966 080 EU/t and 160 CWU/t (176 for computational matrix and catalyst core). Amounts use the pack formulas: x5 for the scaled ones, x32 for the exponential ones.
    - |-
      Voltage Coil: 1 mythrolic alloy tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine aurourium wire · 1 250 mB superstate helium 3; 10 s; 160 CWU/t. Computational Matrix: 1 starium alloy frame · 1 UEV circuit · 2 UHV circuit · 3 UV circuit · 4 cerium tritelluride single cable · 4 starium alloy bolt · 4 608 mB naquadated soldering alloy; 20 s; 176 CWU/t. Transmission Assembly: 1 mythrolic alloy frame · 1 uhv electric motor · 2 starium alloy rod · 2 starium alloy ring · 4 starium alloy round · 16 fine adamantine wire · 4 000 mB tungsten disulfide; 16 s; 160 CWU/t. Precision Drive Mechanism: 1 starium alloy frame · 1 uhv electric motor · 1 UHV circuit · 1 magmada alloy gear · 1 small starium alloy gear · 8 starium alloy round · 4 000 mB tungsten disulfide · 2 880 mB perfluoroelastomer rubber; 24 s; 160 CWU/t. Microfluidic Flow Valve: 1 uhv fluid regulator · 1 mythrolic alloy small fluid pipe · 2 starium alloy plate · 4 starium alloy round · 4 styrene butadiene rubber ring · 2 starium alloy ring · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 16 s; 160 CWU/t.
    - The UEV circuit tag holds the runic processor mainframe, the draconic processor computer and the abyssal processor assembly (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uev_circuits) set the pace.
    - |-
      Parts 2/2 (Super Magnetic Core, Catalyst Core, High Strength Panel, Micropower Router) is the other half: the motor, pump, conveyor and piston lines need those.
    - |-
      Sub-steps people skip: (1) research first: one sample of every UHV part on a data item in the Research Station; (2) one product per input slice so a half-filled recipe does not block the bus; (3) UEV, UHV and UV circuits are three separate drawers; (4) keep 2 spare of every part: the components chain eats 1 to 3 per craft.
    - |-
      Unverified: exact feed layout of the Component Part Assembly (see its multiblock card), fluid hatch counts, and the alloy and wire sources (uev_alloys).
  b:
    - ["gtceu:component_part_assembly", 1]
    - ["gtceu:research_station", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:component_part_assembly"]
      t: |-
        Drawers first for every input of the products in this chain and the UHV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, isovol, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact.
    - i: ["gtceu:research_station", "start_core:component_data_core"]
      t: |-
        Research first: every recipe needs station research of the UHV part (160 CWU/t, 176 for matrix and catalyst core). Scan one sample of each UHV part and keep the data item in the Data Access Hatch of the assembly.
    - i: ["gtceu:component_part_assembly", "kubejs:uev_voltage_coil"]
      t: |-
        Voltage Coil first: 10 s at 7 864 320 EU/t. Output drawer Keep Exact 16.
    - i: ["gtceu:component_part_assembly", "kubejs:uev_computational_matrix"]
      t: Computational Matrix next (20 s). Do not queue two products in one slice.
    - i: ["gtceu:component_part_assembly", "kubejs:uev_microfluidic_flow_valve"]
      t: |-
        Remaining products: Transmission Assembly, Precision Drive Mechanism, Microfluidic Flow Valve. One output drawer per part.
    - i: ["functionalstorage:oak_1", "kubejs:uev_voltage_coil"]
      t: |-
        The parts feed uev_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first.
---
# UEV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_parts` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cpa">
<div class="gt-head"><span class="gt-mname">Component Part Assembly · 7 864 320 EU/t · station research of the UHV part</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Voltage Coil: 1 mythrolic alloy tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine aurourium wire · 1 250 mB superstate helium 3 (functionalstorage:oak_1) - 10 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Voltage Coil: 1 mythrolic alloy tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine aurourium wire · 1 250 mB superstate helium 3</span><span class="gt-sub"><span>mythrolic alloy tiny fluid pipe</span><span>long magnetic zapolgium rod</span><span>fine aurourium wire</span></span></span><span class="gt-slot gt-group" title="Computational Matrix: 1 starium alloy frame · 1 UEV circuit · 2 UHV circuit · 3 UV circuit · 4 cerium tritelluride single cable · 4 starium alloy bolt · 4 608 mB naquadated soldering alloy (functionalstorage:oak_1) - 20 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Computational Matrix: 1 starium alloy frame · 1 UEV circuit · 2 UHV circuit · 3 UV circuit · 4 cerium tritelluride single cable · 4 starium alloy bolt · 4 608 mB naquadated soldering alloy</span><span class="gt-sub"><span>starium alloy frame</span><span>UEV circuit</span><span>UHV circuit</span><span>UV circuit</span><span>cerium tritelluride single cable</span><span>starium alloy bolt</span></span></span><span class="gt-slot gt-group" title="Transmission Assembly: 1 mythrolic alloy frame · 1 uhv electric motor · 2 starium alloy rod · 2 starium alloy ring · 4 starium alloy round · 16 fine adamantine wire · 4 000 mB tungsten disulfide (functionalstorage:oak_1) - 16 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Transmission Assembly: 1 mythrolic alloy frame · 1 uhv electric motor · 2 starium alloy rod · 2 starium alloy ring · 4 starium alloy round · 16 fine adamantine wire · 4 000 mB tungsten disulfide</span><span class="gt-sub"><span>mythrolic alloy frame</span><span>uhv electric motor</span><span>starium alloy rod</span><span>starium alloy ring</span><span>starium alloy round</span><span>fine adamantine wire</span></span></span><span class="gt-slot gt-group" title="Precision Drive Mechanism: 1 starium alloy frame · 1 uhv electric motor · 1 UHV circuit · 1 magmada alloy gear · 1 small starium alloy gear · 8 starium alloy round · 4 000 mB tungsten disulfide · 2 880 mB perfluoroelastomer rubber (functionalstorage:oak_1) - 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Precision Drive Mechanism: 1 starium alloy frame · 1 uhv electric motor · 1 UHV circuit · 1 magmada alloy gear · 1 small starium alloy gear · 8 starium alloy round · 4 000 mB tungsten disulfide · 2 880 mB perfluoroelastomer rubber</span><span class="gt-sub"><span>starium alloy frame</span><span>uhv electric motor</span><span>UHV circuit</span><span>magmada alloy gear</span><span>small starium alloy gear</span><span>starium alloy round</span></span></span><span class="gt-slot gt-group" title="Microfluidic Flow Valve: 1 uhv fluid regulator · 1 mythrolic alloy small fluid pipe · 2 starium alloy plate · 4 starium alloy round · 4 styrene butadiene rubber ring · 2 starium alloy ring · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 16 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Microfluidic Flow Valve: 1 uhv fluid regulator · 1 mythrolic alloy small fluid pipe · 2 starium alloy plate · 4 starium alloy round · 4 styrene butadiene rubber ring · 2 starium alloy ring · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>uhv fluid regulator</span><span>mythrolic alloy small fluid pipe</span><span>starium alloy plate</span><span>starium alloy round</span><span>styrene butadiene rubber ring</span><span>starium alloy ring</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s · 20 s · 16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Voltage Coil (kubejs:uev_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Voltage Coil</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Computational Matrix (kubejs:uev_computational_matrix) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Computational Matrix</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Transmission Assembly (kubejs:uev_transmission_assembly) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_transmission_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Transmission Assembly</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Precision Drive Mechanism (kubejs:uev_precision_drive_mechanism) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_precision_drive_mechanism.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Precision Drive Mechanism</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="UEV Microfluidic Flow Valve (kubejs:uev_microfluidic_flow_valve) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_microfluidic_flow_valve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Microfluidic Flow Valve</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [Component Part Assembly · 7 864 320 EU/t · station research of the UHV part](#m-cpa)

## How to build

1. Drawers first for every input of the products in this chain and the UHV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, isovol, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:component_part_assembly`
2. Research first: every recipe needs station research of the UHV part (160 CWU/t, 176 for matrix and catalyst core). Scan one sample of each UHV part and keep the data item in the Data Access Hatch of the assembly. — `gtceu:research_station`, `start_core:component_data_core`
3. Voltage Coil first: 10 s at 7 864 320 EU/t. Output drawer Keep Exact 16. — `gtceu:component_part_assembly`, `kubejs:uev_voltage_coil`
4. Computational Matrix next (20 s). Do not queue two products in one slice. — `gtceu:component_part_assembly`, `kubejs:uev_computational_matrix`
5. Remaining products: Transmission Assembly, Precision Drive Mechanism, Microfluidic Flow Valve. One output drawer per part. — `gtceu:component_part_assembly`, `kubejs:uev_microfluidic_flow_valve`
6. The parts feed uev\_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first. — `functionalstorage:oak_1`, `kubejs:uev_voltage_coil`

## Tips

- Source: kjs additions/progression/components/component\_parts.js (componentPart(), tier uev; materials in utils/tier\_data.js). Every part is a Component Part Assembly recipe (gtceu:component\_part\_assembly) at 7 864 320 EU/t, with STATION research of the same part of the UHV tier at 1 966 080 EU/t and 160 CWU/t (176 for computational matrix and catalyst core). Amounts use the pack formulas: x5 for the scaled ones, x32 for the exponential ones.
- Voltage Coil: 1 mythrolic alloy tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine aurourium wire · 1 250 mB superstate helium 3; 10 s; 160 CWU/t. Computational Matrix: 1 starium alloy frame · 1 UEV circuit · 2 UHV circuit · 3 UV circuit · 4 cerium tritelluride single cable · 4 starium alloy bolt · 4 608 mB naquadated soldering alloy; 20 s; 176 CWU/t. Transmission Assembly: 1 mythrolic alloy frame · 1 uhv electric motor · 2 starium alloy rod · 2 starium alloy ring · 4 starium alloy round · 16 fine adamantine wire · 4 000 mB tungsten disulfide; 16 s; 160 CWU/t. Precision Drive Mechanism: 1 starium alloy frame · 1 uhv electric motor · 1 UHV circuit · 1 magmada alloy gear · 1 small starium alloy gear · 8 starium alloy round · 4 000 mB tungsten disulfide · 2 880 mB perfluoroelastomer rubber; 24 s; 160 CWU/t. Microfluidic Flow Valve: 1 uhv fluid regulator · 1 mythrolic alloy small fluid pipe · 2 starium alloy plate · 4 starium alloy round · 4 styrene butadiene rubber ring · 2 starium alloy ring · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 16 s; 160 CWU/t.
- The UEV circuit tag holds the runic processor mainframe, the draconic processor computer and the abyssal processor assembly (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uev\_circuits) set the pace.
- Parts 2/2 (Super Magnetic Core, Catalyst Core, High Strength Panel, Micropower Router) is the other half: the motor, pump, conveyor and piston lines need those.
- Sub-steps people skip: (1) research first: one sample of every UHV part on a data item in the Research Station; (2) one product per input slice so a half-filled recipe does not block the bus; (3) UEV, UHV and UV circuits are three separate drawers; (4) keep 2 spare of every part: the components chain eats 1 to 3 per craft.
- **Unverified** exact feed layout of the Component Part Assembly (see its multiblock card), fluid hatch counts, and the alloy and wire sources (uev\_alloys).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:research_station` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `kubejs:uev_voltage_coil`, `kubejs:uev_computational_matrix`, `kubejs:uev_transmission_assembly`, `kubejs:uev_precision_drive_mechanism`, `kubejs:uev_microfluidic_flow_valve`
