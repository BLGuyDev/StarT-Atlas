---
kind: chain
id: uiv_parts2
order: 2020
data:
  t: |-
    UIV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router
  inf: true
  "n":
    - - g0
      - |-
        Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 ohmderblux alloy rod · 16 fine xeproda wire · 2 nyanium tiny fluid pipe · 3 000 mB superstate helium 3
      - g
      - functionalstorage:oak_1
      - - [long magnetic zapolgium rod, "gtceu:long_magnetic_zapolgium_rod"]
        - [magnetic dysprosium rod, "gtceu:magnetic_dysprosium_rod"]
        - [ohmderblux alloy rod, "gtceu:ohmderblux_alloy_rod"]
        - [fine xeproda wire, "gtceu:fine_xeproda_wire"]
        - [nyanium tiny fluid pipe, "gtceu:nyanium_tiny_fluid_pipe"]
    - - g1
      - |-
        Catalyst Core: 4 ohmderblux alloy rod · 1 draco resilient fusion glass · 1 draconic eye · 32 fine rhenium super composite alloy wire · 1 uev emitter · 4 abyssal alloy ring · 2 304 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy rod, "gtceu:ohmderblux_alloy_rod"]
        - [draco resilient fusion glass, "kubejs:draco_resilient_fusion_glass"]
        - [draconic eye, "kubejs:draconic_eye"]
        - [fine rhenium super composite alloy wire, "gtceu:fine_rhenium_super_composite_alloy_wire"]
        - [uev emitter, "gtceu:uev_emitter"]
        - [abyssal alloy ring, "gtceu:abyssal_alloy_ring"]
    - - g2
      - |-
        High Strength Panel: 1 dense ohmderblux alloy plate · 1 UHV circuit · 4 abyssal alloy screw · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [dense ohmderblux alloy plate, "gtceu:dense_ohmderblux_alloy_plate"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [abyssal alloy screw, "gtceu:abyssal_alloy_screw"]
    - - g3
      - |-
        Micropower Router: 4 polonium bismide double cable · 2 ohmderblux alloy plate · 1 UEV circuit · 4 ohmderblux alloy bolt · 864 mB perfluoroelastomer rubber
      - g
      - functionalstorage:oak_1
      - - [polonium bismide double cable, "gtceu:polonium_bismide_double_cable"]
        - [ohmderblux alloy plate, "gtceu:ohmderblux_alloy_plate"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [ohmderblux alloy bolt, "gtceu:ohmderblux_alloy_bolt"]
    - - cpa
      - Component Part Assembly · 31 457 280 EU/t · station research of the UEV part
      - m
      - gtceu:component_part_assembly
    - [o0, UIV Super Magnetic Core, x, "kubejs:uiv_super_magnetic_core"]
    - [o1, UIV Catalyst Core, x, "kubejs:uiv_catalyst_core"]
    - [o2, UIV High Strength Panel, x, "kubejs:uiv_high_strength_panel"]
    - [o3, UIV Micropower Router, o, "kubejs:uiv_micropower_router"]
  e:
    - [g0, cpa, "15 s"]
    - [g1, cpa, "24 s"]
    - [g2, cpa, "10 s"]
    - [g3, cpa, "12 s"]
    - [cpa, o0, "1 / 15 s"]
    - [cpa, o1, "1 / 24 s"]
    - [cpa, o2, "1 / 10 s"]
    - [cpa, o3, "1 / 12 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/component_parts.js (componentPart(), tier uiv; materials in utils/tier_data.js). Every part is a Component Part Assembly recipe (gtceu:component_part_assembly) at 31 457 280 EU/t, with STATION research of the same part of the UEV tier at 7 864 320 EU/t and 192 CWU/t (208 for computational matrix and catalyst core). Amounts use the pack formulas: x6 for the scaled ones, x64 for the exponential ones.
    - |-
      Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 ohmderblux alloy rod · 16 fine xeproda wire · 2 nyanium tiny fluid pipe · 3 000 mB superstate helium 3; 15 s; 192 CWU/t. Catalyst Core: 4 ohmderblux alloy rod · 1 draco resilient fusion glass · 1 draconic eye · 32 fine rhenium super composite alloy wire · 1 uev emitter · 4 abyssal alloy ring · 2 304 mB calamatium; 24 s; 208 CWU/t. High Strength Panel: 1 dense ohmderblux alloy plate · 1 UHV circuit · 4 abyssal alloy screw · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 10 s; 192 CWU/t. Micropower Router: 4 polonium bismide double cable · 2 ohmderblux alloy plate · 1 UEV circuit · 4 ohmderblux alloy bolt · 864 mB perfluoroelastomer rubber; 12 s; 192 CWU/t.
    - The UIV circuit tag holds the draconic processor mainframe and the abyssal processor computer (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uiv_circuits) set the pace.
    - |-
      Quirk in the pack script: the High Strength Panel lists its alloy fluid as the id 'gtceu:chaotixic_alloy 288' and the builder appends the amount again. Whether KubeJS reads that as 288 mB of molten chaotixic alloy is Unverified: open the recipe in the Recipe Browser before building the line.
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
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_super_magnetic_core"]
      t: |-
        Super Magnetic Core first: 15 s at 31 457 280 EU/t. Output drawer Keep Exact 16.
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_catalyst_core"]
      t: Catalyst Core next (24 s). Do not queue two products in one slice.
    - i: ["gtceu:component_part_assembly", "kubejs:uiv_micropower_router"]
      t: |-
        Remaining products: High Strength Panel, Micropower Router. One output drawer per part.
    - i: ["functionalstorage:oak_1", "kubejs:uiv_super_magnetic_core"]
      t: |-
        The parts feed uiv_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first.
---
# UIV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_parts2` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV hull, parts, hatches and components](../../plan/p19.md#uivmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cpa">
<div class="gt-head"><span class="gt-mname">Component Part Assembly · 31 457 280 EU/t · station research of the UEV part</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 ohmderblux alloy rod · 16 fine xeproda wire · 2 nyanium tiny fluid pipe · 3 000 mB superstate helium 3 (functionalstorage:oak_1) - 15 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 ohmderblux alloy rod · 16 fine xeproda wire · 2 nyanium tiny fluid pipe · 3 000 mB superstate helium 3</span><span class="gt-sub"><span>long magnetic zapolgium rod</span><span>magnetic dysprosium rod</span><span>ohmderblux alloy rod</span><span>fine xeproda wire</span><span>nyanium tiny fluid pipe</span></span></span><span class="gt-slot gt-group" title="Catalyst Core: 4 ohmderblux alloy rod · 1 draco resilient fusion glass · 1 draconic eye · 32 fine rhenium super composite alloy wire · 1 uev emitter · 4 abyssal alloy ring · 2 304 mB calamatium (functionalstorage:oak_1) - 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Catalyst Core: 4 ohmderblux alloy rod · 1 draco resilient fusion glass · 1 draconic eye · 32 fine rhenium super composite alloy wire · 1 uev emitter · 4 abyssal alloy ring · 2 304 mB calamatium</span><span class="gt-sub"><span>ohmderblux alloy rod</span><span>draco resilient fusion glass</span><span>draconic eye</span><span>fine rhenium super composite alloy wire</span><span>uev emitter</span><span>abyssal alloy ring</span></span></span><span class="gt-slot gt-group" title="High Strength Panel: 1 dense ohmderblux alloy plate · 1 UHV circuit · 4 abyssal alloy screw · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 10 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">High Strength Panel: 1 dense ohmderblux alloy plate · 1 UHV circuit · 4 abyssal alloy screw · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>dense ohmderblux alloy plate</span><span>UHV circuit</span><span>abyssal alloy screw</span></span></span><span class="gt-slot gt-group" title="Micropower Router: 4 polonium bismide double cable · 2 ohmderblux alloy plate · 1 UEV circuit · 4 ohmderblux alloy bolt · 864 mB perfluoroelastomer rubber (functionalstorage:oak_1) - 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Micropower Router: 4 polonium bismide double cable · 2 ohmderblux alloy plate · 1 UEV circuit · 4 ohmderblux alloy bolt · 864 mB perfluoroelastomer rubber</span><span class="gt-sub"><span>polonium bismide double cable</span><span>ohmderblux alloy plate</span><span>UEV circuit</span><span>ohmderblux alloy bolt</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s · 24 s · 10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Super Magnetic Core (kubejs:uiv_super_magnetic_core) - 1 / 15 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_super_magnetic_core.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Super Magnetic Core</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Catalyst Core (kubejs:uiv_catalyst_core) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_catalyst_core.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Catalyst Core</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV High Strength Panel (kubejs:uiv_high_strength_panel) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_high_strength_panel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV High Strength Panel</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="UIV Micropower Router (kubejs:uiv_micropower_router) - 1 / 12 s"><img class="gt-ico" src="../../assets/icons/kubejs__uiv_micropower_router.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Micropower Router</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [Component Part Assembly · 31 457 280 EU/t · station research of the UEV part](#m-cpa)

## How to build

1. Drawers first for every input of the products in this chain and the UEV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, calamatium, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:component_part_assembly`
2. Research first: every recipe needs station research of the UEV part (192 CWU/t, 208 for matrix and catalyst core). Scan one sample of each UEV part and keep the data item in the Data Access Hatch of the assembly. — `gtceu:research_station`, `start_core:component_data_core`
3. Super Magnetic Core first: 15 s at 31 457 280 EU/t. Output drawer Keep Exact 16. — `gtceu:component_part_assembly`, `kubejs:uiv_super_magnetic_core`
4. Catalyst Core next (24 s). Do not queue two products in one slice. — `gtceu:component_part_assembly`, `kubejs:uiv_catalyst_core`
5. Remaining products: High Strength Panel, Micropower Router. One output drawer per part. — `gtceu:component_part_assembly`, `kubejs:uiv_micropower_router`
6. The parts feed uiv\_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first. — `functionalstorage:oak_1`, `kubejs:uiv_super_magnetic_core`

## Tips

- Source: kjs additions/progression/components/component\_parts.js (componentPart(), tier uiv; materials in utils/tier\_data.js). Every part is a Component Part Assembly recipe (gtceu:component\_part\_assembly) at 31 457 280 EU/t, with STATION research of the same part of the UEV tier at 7 864 320 EU/t and 192 CWU/t (208 for computational matrix and catalyst core). Amounts use the pack formulas: x6 for the scaled ones, x64 for the exponential ones.
- Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 ohmderblux alloy rod · 16 fine xeproda wire · 2 nyanium tiny fluid pipe · 3 000 mB superstate helium 3; 15 s; 192 CWU/t. Catalyst Core: 4 ohmderblux alloy rod · 1 draco resilient fusion glass · 1 draconic eye · 32 fine rhenium super composite alloy wire · 1 uev emitter · 4 abyssal alloy ring · 2 304 mB calamatium; 24 s; 208 CWU/t. High Strength Panel: 1 dense ohmderblux alloy plate · 1 UHV circuit · 4 abyssal alloy screw · 864 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 10 s; 192 CWU/t. Micropower Router: 4 polonium bismide double cable · 2 ohmderblux alloy plate · 1 UEV circuit · 4 ohmderblux alloy bolt · 864 mB perfluoroelastomer rubber; 12 s; 192 CWU/t.
- The UIV circuit tag holds the draconic processor mainframe and the abyssal processor computer (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uiv\_circuits) set the pace.
- Quirk in the pack script: the High Strength Panel lists its alloy fluid as the id 'gtceu:chaotixic\_alloy 288' and the builder appends the amount again. Whether KubeJS reads that as 288 mB of molten chaotixic alloy is Unverified: open the recipe in the Recipe Browser before building the line.
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

- **Main source for:** `kubejs:uiv_super_magnetic_core`, `kubejs:uiv_catalyst_core`, `kubejs:uiv_high_strength_panel`, `kubejs:uiv_micropower_router`
