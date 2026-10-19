---
kind: chain
id: uiv_parts
order: 2010
data:
  t: |-
    UIV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve
  inf: true
  "n":
    - - g0
      - |-
        Voltage Coil: 1 nyanium tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine rhenate w wire · 1 500 mB superstate helium 3
      - g
      - functionalstorage:oak_1
      - - [nyanium tiny fluid pipe, "gtceu:nyanium_tiny_fluid_pipe"]
        - [long magnetic zapolgium rod, "gtceu:long_magnetic_zapolgium_rod"]
        - [fine rhenate w wire, "gtceu:fine_rhenate_w_wire"]
    - - g1
      - |-
        Computational Matrix: 1 ohmderblux alloy frame · 1 UIV circuit · 2 UEV circuit · 3 UHV circuit · 4 polonium bismide single cable · 4 ohmderblux alloy bolt · 9 216 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy frame, "gtceu:ohmderblux_alloy_frame"]
        - [UIV circuit, "kubejs:uiv_universal_circuit"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
        - [ohmderblux alloy bolt, "gtceu:ohmderblux_alloy_bolt"]
    - - g2
      - |-
        Transmission Assembly: 1 chaotixic alloy frame · 1 uev electric motor · 2 ohmderblux alloy rod · 2 ohmderblux alloy ring · 4 ohmderblux alloy round · 16 fine xeproda wire · 8 000 mB tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [chaotixic alloy frame, "gtceu:chaotixic_alloy_frame"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [ohmderblux alloy rod, "gtceu:ohmderblux_alloy_rod"]
        - [ohmderblux alloy ring, "gtceu:ohmderblux_alloy_ring"]
        - [ohmderblux alloy round, "gtceu:ohmderblux_alloy_round"]
        - [fine xeproda wire, "gtceu:fine_xeproda_wire"]
    - - g3
      - |-
        Precision Drive Mechanism: 1 ohmderblux alloy frame · 1 uev electric motor · 1 UEV circuit · 1 abyssal alloy gear · 1 small ohmderblux alloy gear · 8 ohmderblux alloy round · 8 000 mB tungsten disulfide · 3 456 mB perfluoroelastomer rubber
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy frame, "gtceu:ohmderblux_alloy_frame"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [abyssal alloy gear, "gtceu:abyssal_alloy_gear"]
        - [small ohmderblux alloy gear, "gtceu:small_ohmderblux_alloy_gear"]
        - [ohmderblux alloy round, "gtceu:ohmderblux_alloy_round"]
    - - g4
      - |-
        Microfluidic Flow Valve: 1 uev fluid regulator · 1 nyanium small fluid pipe · 2 ohmderblux alloy plate · 4 ohmderblux alloy round · 4 perfluoroelastomer rubber ring · 2 ohmderblux alloy ring · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [uev fluid regulator, "gtceu:uev_fluid_regulator"]
        - [nyanium small fluid pipe, "gtceu:nyanium_small_fluid_pipe"]
        - [ohmderblux alloy plate, "gtceu:ohmderblux_alloy_plate"]
        - [ohmderblux alloy round, "gtceu:ohmderblux_alloy_round"]
        - [perfluoroelastomer rubber ring, "gtceu:perfluoroelastomer_rubber_ring"]
        - [ohmderblux alloy ring, "gtceu:ohmderblux_alloy_ring"]
    - - cpa
      - Component Part Assembly · 31 457 280 EU/t · station research of the UEV part
      - m
      - gtceu:component_part_assembly
    - [o0, UIV Voltage Coil, x, "kubejs:uiv_voltage_coil"]
    - [o1, UIV Computational Matrix, x, "kubejs:uiv_computational_matrix"]
    - [o2, UIV Transmission Assembly, x, "kubejs:uiv_transmission_assembly"]
    - [o3, UIV Precision Drive Mechanism, x, "kubejs:uiv_precision_drive_mechanism"]
    - [o4, UIV Microfluidic Flow Valve, o, "kubejs:uiv_microfluidic_flow_valve"]
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
      Source: kjs additions/progression/components/component_parts.js (componentPart(), tier uiv; materials in utils/tier_data.js). Every part is a Component Part Assembly recipe (gtceu:component_part_assembly) at 31 457 280 EU/t, with STATION research of the same part of the UEV tier at 7 864 320 EU/t and 192 CWU/t (208 for computational matrix and catalyst core). Amounts use the pack formulas: x6 for the scaled ones, x64 for the exponential ones.
    - |-
      Voltage Coil: 1 nyanium tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine rhenate w wire · 1 500 mB superstate helium 3; 10 s; 192 CWU/t. Computational Matrix: 1 ohmderblux alloy frame · 1 UIV circuit · 2 UEV circuit · 3 UHV circuit · 4 polonium bismide single cable · 4 ohmderblux alloy bolt · 9 216 mB naquadated soldering alloy; 20 s; 208 CWU/t. Transmission Assembly: 1 chaotixic alloy frame · 1 uev electric motor · 2 ohmderblux alloy rod · 2 ohmderblux alloy ring · 4 ohmderblux alloy round · 16 fine xeproda wire · 8 000 mB tungsten disulfide; 16 s; 192 CWU/t. Precision Drive Mechanism: 1 ohmderblux alloy frame · 1 uev electric motor · 1 UEV circuit · 1 abyssal alloy gear · 1 small ohmderblux alloy gear · 8 ohmderblux alloy round · 8 000 mB tungsten disulfide · 3 456 mB perfluoroelastomer rubber; 24 s; 192 CWU/t. Microfluidic Flow Valve: 1 uev fluid regulator · 1 nyanium small fluid pipe · 2 ohmderblux alloy plate · 4 ohmderblux alloy round · 4 perfluoroelastomer rubber ring · 2 ohmderblux alloy ring · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 16 s; 192 CWU/t.
    - The UIV circuit tag holds the draconic processor mainframe and the abyssal processor computer (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uiv_circuits) set the pace.
    - |-
      Parts 2/2 (Super Magnetic Core, Catalyst Core, High Strength Panel, Micropower Router) is the other half: the motor, pump, conveyor and piston lines need those.
    - |-
      Sub-steps people skip: (1) research first: one sample of every UEV part on a data item in the Research Station; (2) one product per input slice so a half-filled recipe does not block the bus; (3) UIV, UEV and UHV circuits are three separate drawers; (4) keep 2 spare of every part: the components chain eats 1 to 3 per craft.
    - |-
      Unverified: exact feed layout of the Component Part Assembly (see its multiblock card), fluid hatch counts, and the alloy and wire sources (uiv_alloys).
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
        Drawers first for every input of the products in this chain and the UEV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, calamatium, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact.
    - i: ["gtceu:research_station", "start_core:component_data_core"]
      t: |-
        Research first: every recipe needs station research of the UEV part (192 CWU/t, 208 for matrix and catalyst core). Scan one sample of each UEV part and keep the data item in the Data Access Hatch of the assembly.
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_voltage_coil"]
      t: |-
        Voltage Coil first: 10 s at 31 457 280 EU/t. Output drawer Keep Exact 16.
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_computational_matrix"]
      t: Computational Matrix next (20 s). Do not queue two products in one slice.
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_microfluidic_flow_valve"]
      t: |-
        Remaining products: Transmission Assembly, Precision Drive Mechanism, Microfluidic Flow Valve. One output drawer per part.
    - i: ["functionalstorage:oak_1", "kubejs:uiv_voltage_coil"]
      t: |-
        The parts feed uiv_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first.
---
# UIV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_parts` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV hull, parts, hatches and components](../../plan/p19.md#uivmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cpa">
<div class="gt-head"><span class="gt-mname">Component Part Assembly · 31 457 280 EU/t · station research of the UEV part</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Voltage Coil: 1 nyanium tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine rhenate w wire · 1 500 mB superstate helium 3 (functionalstorage:oak_1) - 10 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Voltage Coil: 1 nyanium tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine rhenate w wire · 1 500 mB superstate helium 3</span><span class="gt-sub"><span>nyanium tiny fluid pipe</span><span>long magnetic zapolgium rod</span><span>fine rhenate w wire</span></span></span><span class="gt-slot gt-group" title="Computational Matrix: 1 ohmderblux alloy frame · 1 UIV circuit · 2 UEV circuit · 3 UHV circuit · 4 polonium bismide single cable · 4 ohmderblux alloy bolt · 9 216 mB naquadated soldering alloy (functionalstorage:oak_1) - 20 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Computational Matrix: 1 ohmderblux alloy frame · 1 UIV circuit · 2 UEV circuit · 3 UHV circuit · 4 polonium bismide single cable · 4 ohmderblux alloy bolt · 9 216 mB naquadated soldering alloy</span><span class="gt-sub"><span>ohmderblux alloy frame</span><span>UIV circuit</span><span>UEV circuit</span><span>UHV circuit</span><span>polonium bismide single cable</span><span>ohmderblux alloy bolt</span></span></span><span class="gt-slot gt-group" title="Transmission Assembly: 1 chaotixic alloy frame · 1 uev electric motor · 2 ohmderblux alloy rod · 2 ohmderblux alloy ring · 4 ohmderblux alloy round · 16 fine xeproda wire · 8 000 mB tungsten disulfide (functionalstorage:oak_1) - 16 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Transmission Assembly: 1 chaotixic alloy frame · 1 uev electric motor · 2 ohmderblux alloy rod · 2 ohmderblux alloy ring · 4 ohmderblux alloy round · 16 fine xeproda wire · 8 000 mB tungsten disulfide</span><span class="gt-sub"><span>chaotixic alloy frame</span><span>uev electric motor</span><span>ohmderblux alloy rod</span><span>ohmderblux alloy ring</span><span>ohmderblux alloy round</span><span>fine xeproda wire</span></span></span><span class="gt-slot gt-group" title="Precision Drive Mechanism: 1 ohmderblux alloy frame · 1 uev electric motor · 1 UEV circuit · 1 abyssal alloy gear · 1 small ohmderblux alloy gear · 8 ohmderblux alloy round · 8 000 mB tungsten disulfide · 3 456 mB perfluoroelastomer rubber (functionalstorage:oak_1) - 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Precision Drive Mechanism: 1 ohmderblux alloy frame · 1 uev electric motor · 1 UEV circuit · 1 abyssal alloy gear · 1 small ohmderblux alloy gear · 8 ohmderblux alloy round · 8 000 mB tungsten disulfide · 3 456 mB perfluoroelastomer rubber</span><span class="gt-sub"><span>ohmderblux alloy frame</span><span>uev electric motor</span><span>UEV circuit</span><span>abyssal alloy gear</span><span>small ohmderblux alloy gear</span><span>ohmderblux alloy round</span></span></span><span class="gt-slot gt-group" title="Microfluidic Flow Valve: 1 uev fluid regulator · 1 nyanium small fluid pipe · 2 ohmderblux alloy plate · 4 ohmderblux alloy round · 4 perfluoroelastomer rubber ring · 2 ohmderblux alloy ring · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 16 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Microfluidic Flow Valve: 1 uev fluid regulator · 1 nyanium small fluid pipe · 2 ohmderblux alloy plate · 4 ohmderblux alloy round · 4 perfluoroelastomer rubber ring · 2 ohmderblux alloy ring · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>uev fluid regulator</span><span>nyanium small fluid pipe</span><span>ohmderblux alloy plate</span><span>ohmderblux alloy round</span><span>perfluoroelastomer rubber ring</span><span>ohmderblux alloy ring</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s · 20 s · 16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Voltage Coil (kubejs:uiv_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Voltage Coil</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Computational Matrix (kubejs:uiv_computational_matrix) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Computational Matrix</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Transmission Assembly (kubejs:uiv_transmission_assembly) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_transmission_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Transmission Assembly</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Precision Drive Mechanism (kubejs:uiv_precision_drive_mechanism) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_precision_drive_mechanism.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Precision Drive Mechanism</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="UIV Microfluidic Flow Valve (kubejs:uiv_microfluidic_flow_valve) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_microfluidic_flow_valve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Microfluidic Flow Valve</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [Component Part Assembly · 31 457 280 EU/t · station research of the UEV part](#m-cpa)

## How to build

1. Drawers first for every input of the products in this chain and the UEV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, calamatium, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:component_part_assembly`
2. Research first: every recipe needs station research of the UEV part (192 CWU/t, 208 for matrix and catalyst core). Scan one sample of each UEV part and keep the data item in the Data Access Hatch of the assembly. — `gtceu:research_station`, `start_core:component_data_core`
3. Voltage Coil first: 10 s at 31 457 280 EU/t. Output drawer Keep Exact 16. — `gtceu:component_part_assembly`, `kubejs:uiv_voltage_coil`
4. Computational Matrix next (20 s). Do not queue two products in one slice. — `gtceu:component_part_assembly`, `kubejs:uiv_computational_matrix`
5. Remaining products: Transmission Assembly, Precision Drive Mechanism, Microfluidic Flow Valve. One output drawer per part. — `gtceu:component_part_assembly`, `kubejs:uiv_microfluidic_flow_valve`
6. The parts feed uiv\_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first. — `functionalstorage:oak_1`, `kubejs:uiv_voltage_coil`

## Tips

- Source: kjs additions/progression/components/component\_parts.js (componentPart(), tier uiv; materials in utils/tier\_data.js). Every part is a Component Part Assembly recipe (gtceu:component\_part\_assembly) at 31 457 280 EU/t, with STATION research of the same part of the UEV tier at 7 864 320 EU/t and 192 CWU/t (208 for computational matrix and catalyst core). Amounts use the pack formulas: x6 for the scaled ones, x64 for the exponential ones.
- Voltage Coil: 1 nyanium tiny fluid pipe · 1 long magnetic zapolgium rod · 32 fine rhenate w wire · 1 500 mB superstate helium 3; 10 s; 192 CWU/t. Computational Matrix: 1 ohmderblux alloy frame · 1 UIV circuit · 2 UEV circuit · 3 UHV circuit · 4 polonium bismide single cable · 4 ohmderblux alloy bolt · 9 216 mB naquadated soldering alloy; 20 s; 208 CWU/t. Transmission Assembly: 1 chaotixic alloy frame · 1 uev electric motor · 2 ohmderblux alloy rod · 2 ohmderblux alloy ring · 4 ohmderblux alloy round · 16 fine xeproda wire · 8 000 mB tungsten disulfide; 16 s; 192 CWU/t. Precision Drive Mechanism: 1 ohmderblux alloy frame · 1 uev electric motor · 1 UEV circuit · 1 abyssal alloy gear · 1 small ohmderblux alloy gear · 8 ohmderblux alloy round · 8 000 mB tungsten disulfide · 3 456 mB perfluoroelastomer rubber; 24 s; 192 CWU/t. Microfluidic Flow Valve: 1 uev fluid regulator · 1 nyanium small fluid pipe · 2 ohmderblux alloy plate · 4 ohmderblux alloy round · 4 perfluoroelastomer rubber ring · 2 ohmderblux alloy ring · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 16 s; 192 CWU/t.
- The UIV circuit tag holds the draconic processor mainframe and the abyssal processor computer (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uiv\_circuits) set the pace.
- Parts 2/2 (Super Magnetic Core, Catalyst Core, High Strength Panel, Micropower Router) is the other half: the motor, pump, conveyor and piston lines need those.
- Sub-steps people skip: (1) research first: one sample of every UEV part on a data item in the Research Station; (2) one product per input slice so a half-filled recipe does not block the bus; (3) UIV, UEV and UHV circuits are three separate drawers; (4) keep 2 spare of every part: the components chain eats 1 to 3 per craft.
- **Unverified** exact feed layout of the Component Part Assembly (see its multiblock card), fluid hatch counts, and the alloy and wire sources (uiv\_alloys).

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

- **Main source for:** `kubejs:uiv_voltage_coil`, `kubejs:uiv_computational_matrix`, `kubejs:uiv_transmission_assembly`, `kubejs:uiv_precision_drive_mechanism`, `kubejs:uiv_microfluidic_flow_valve`
