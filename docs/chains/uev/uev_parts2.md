---
kind: chain
id: uev_parts2
order: 2000
data:
  t: |-
    UEV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router
  inf: true
  "n":
    - - g0
      - |-
        Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 starium alloy rod · 16 fine adamantine wire · 2 mythrolic alloy tiny fluid pipe · 2 500 mB superstate helium 3
      - g
      - functionalstorage:oak_1
      - - [long magnetic zapolgium rod, "gtceu:long_magnetic_zapolgium_rod"]
        - [magnetic dysprosium rod, "gtceu:magnetic_dysprosium_rod"]
        - [starium alloy rod, "gtceu:starium_alloy_rod"]
        - [fine adamantine wire, "gtceu:fine_adamantine_wire"]
        - [mythrolic alloy tiny fluid pipe, "gtceu:mythrolic_alloy_tiny_fluid_pipe"]
    - - g1
      - |-
        Catalyst Core: 4 starium alloy rod · 1 reinforced fusion glass · 2 decaying star · 32 fine enriched pallarovium alloy wire · 1 uhv emitter · 4 magmada alloy ring · 1 152 mB isovol
      - g
      - functionalstorage:oak_1
      - - [starium alloy rod, "gtceu:starium_alloy_rod"]
        - [reinforced fusion glass, "kubejs:reinforced_fusion_glass"]
        - [decaying star, "kubejs:decaying_star"]
        - [fine enriched pallarovium alloy wire, "gtceu:fine_enriched_pallarovium_alloy_wire"]
        - [uhv emitter, "gtceu:uhv_emitter"]
        - [magmada alloy ring, "gtceu:magmada_alloy_ring"]
    - - g2
      - |-
        High Strength Panel: 1 dense starium alloy plate · 1 UV circuit · 4 magmada alloy screw · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [dense starium alloy plate, "gtceu:dense_starium_alloy_plate"]
        - [UV circuit, "kubejs:uv_universal_circuit"]
        - [magmada alloy screw, "gtceu:magmada_alloy_screw"]
    - - g3
      - |-
        Micropower Router: 4 cerium tritelluride double cable · 2 starium alloy plate · 1 UHV circuit · 4 starium alloy bolt · 720 mB perfluoroelastomer rubber
      - g
      - functionalstorage:oak_1
      - - [cerium tritelluride double cable, "gtceu:cerium_tritelluride_double_cable"]
        - [starium alloy plate, "gtceu:starium_alloy_plate"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [starium alloy bolt, "gtceu:starium_alloy_bolt"]
    - - cpa
      - Component Part Assembly · 7 864 320 EU/t · station research of the UHV part
      - m
      - gtceu:component_part_assembly
    - [o0, UEV Super Magnetic Core, x, "kubejs:uev_super_magnetic_core"]
    - [o1, UEV Catalyst Core, x, "kubejs:uev_catalyst_core"]
    - [o2, UEV High Strength Panel, x, "kubejs:uev_high_strength_panel"]
    - [o3, UEV Micropower Router, o, "kubejs:uev_micropower_router"]
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
      Source: kjs additions/progression/components/component_parts.js (componentPart(), tier uev; materials in utils/tier_data.js). Every part is a Component Part Assembly recipe (gtceu:component_part_assembly) at 7 864 320 EU/t, with STATION research of the same part of the UHV tier at 1 966 080 EU/t and 160 CWU/t (176 for computational matrix and catalyst core). Amounts use the pack formulas: x5 for the scaled ones, x32 for the exponential ones.
    - |-
      Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 starium alloy rod · 16 fine adamantine wire · 2 mythrolic alloy tiny fluid pipe · 2 500 mB superstate helium 3; 15 s; 160 CWU/t. Catalyst Core: 4 starium alloy rod · 1 reinforced fusion glass · 2 decaying star · 32 fine enriched pallarovium alloy wire · 1 uhv emitter · 4 magmada alloy ring · 1 152 mB isovol; 24 s; 176 CWU/t. High Strength Panel: 1 dense starium alloy plate · 1 UV circuit · 4 magmada alloy screw · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 10 s; 160 CWU/t. Micropower Router: 4 cerium tritelluride double cable · 2 starium alloy plate · 1 UHV circuit · 4 starium alloy bolt · 720 mB perfluoroelastomer rubber; 12 s; 160 CWU/t.
    - The UEV circuit tag holds the runic processor mainframe, the draconic processor computer and the abyssal processor assembly (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uev_circuits) set the pace.
    - |-
      Quirk in the pack script: the High Strength Panel lists its alloy fluid as the id 'gtceu:mythrolic_alloy 288' and the builder appends the amount again. Whether KubeJS reads that as 288 mB of molten mythrolic alloy is Unverified: open the recipe in the Recipe Browser before building the line.
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
    - i: ["gtceu:component_part_assembly", "kubejs:uev_super_magnetic_core"]
      t: |-
        Super Magnetic Core first: 15 s at 7 864 320 EU/t. Output drawer Keep Exact 16.
    - i: ["gtceu:component_part_assembly", "kubejs:uev_catalyst_core"]
      t: Catalyst Core next (24 s). Do not queue two products in one slice.
    - i: ["gtceu:component_part_assembly", "kubejs:uev_micropower_router"]
      t: |-
        Remaining products: High Strength Panel, Micropower Router. One output drawer per part.
    - i: ["functionalstorage:oak_1", "kubejs:uev_super_magnetic_core"]
      t: |-
        The parts feed uev_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first.
---
# UEV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_parts2` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cpa">
<div class="gt-head"><span class="gt-mname">Component Part Assembly · 7 864 320 EU/t · station research of the UHV part</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 starium alloy rod · 16 fine adamantine wire · 2 mythrolic alloy tiny fluid pipe · 2 500 mB superstate helium 3 (functionalstorage:oak_1) - 15 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 starium alloy rod · 16 fine adamantine wire · 2 mythrolic alloy tiny fluid pipe · 2 500 mB superstate helium 3</span><span class="gt-sub"><span>long magnetic zapolgium rod</span><span>magnetic dysprosium rod</span><span>starium alloy rod</span><span>fine adamantine wire</span><span>mythrolic alloy tiny fluid pipe</span></span></span><span class="gt-slot gt-group" title="Catalyst Core: 4 starium alloy rod · 1 reinforced fusion glass · 2 decaying star · 32 fine enriched pallarovium alloy wire · 1 uhv emitter · 4 magmada alloy ring · 1 152 mB isovol (functionalstorage:oak_1) - 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Catalyst Core: 4 starium alloy rod · 1 reinforced fusion glass · 2 decaying star · 32 fine enriched pallarovium alloy wire · 1 uhv emitter · 4 magmada alloy ring · 1 152 mB isovol</span><span class="gt-sub"><span>starium alloy rod</span><span>reinforced fusion glass</span><span>decaying star</span><span>fine enriched pallarovium alloy wire</span><span>uhv emitter</span><span>magmada alloy ring</span></span></span><span class="gt-slot gt-group" title="High Strength Panel: 1 dense starium alloy plate · 1 UV circuit · 4 magmada alloy screw · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 10 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">High Strength Panel: 1 dense starium alloy plate · 1 UV circuit · 4 magmada alloy screw · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>dense starium alloy plate</span><span>UV circuit</span><span>magmada alloy screw</span></span></span><span class="gt-slot gt-group" title="Micropower Router: 4 cerium tritelluride double cable · 2 starium alloy plate · 1 UHV circuit · 4 starium alloy bolt · 720 mB perfluoroelastomer rubber (functionalstorage:oak_1) - 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Micropower Router: 4 cerium tritelluride double cable · 2 starium alloy plate · 1 UHV circuit · 4 starium alloy bolt · 720 mB perfluoroelastomer rubber</span><span class="gt-sub"><span>cerium tritelluride double cable</span><span>starium alloy plate</span><span>UHV circuit</span><span>starium alloy bolt</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s · 24 s · 10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Super Magnetic Core (kubejs:uev_super_magnetic_core) - 1 / 15 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_super_magnetic_core.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Super Magnetic Core</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Catalyst Core (kubejs:uev_catalyst_core) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_catalyst_core.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Catalyst Core</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV High Strength Panel (kubejs:uev_high_strength_panel) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_high_strength_panel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV High Strength Panel</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="UEV Micropower Router (kubejs:uev_micropower_router) - 1 / 12 s"><img class="gt-ico" src="../../assets/icons/kubejs__uev_micropower_router.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Micropower Router</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [Component Part Assembly · 7 864 320 EU/t · station research of the UHV part](#m-cpa)

## How to build

1. Drawers first for every input of the products in this chain and the UHV sample of each part. Drums for naquadated soldering alloy, tungsten disulfide, superstate helium 3, isovol, perfluoroelastomer rubber and PEDOT:PSS plastic. The Component Part Assembly is one multiblock: give each product its own input slice, one router or Pipez item pipe per drawer with Item Filters and Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:component_part_assembly`
2. Research first: every recipe needs station research of the UHV part (160 CWU/t, 176 for matrix and catalyst core). Scan one sample of each UHV part and keep the data item in the Data Access Hatch of the assembly. — `gtceu:research_station`, `start_core:component_data_core`
3. Super Magnetic Core first: 15 s at 7 864 320 EU/t. Output drawer Keep Exact 16. — `gtceu:component_part_assembly`, `kubejs:uev_super_magnetic_core`
4. Catalyst Core next (24 s). Do not queue two products in one slice. — `gtceu:component_part_assembly`, `kubejs:uev_catalyst_core`
5. Remaining products: High Strength Panel, Micropower Router. One output drawer per part. — `gtceu:component_part_assembly`, `kubejs:uev_micropower_router`
6. The parts feed uev\_components. Each recipe also has a 64-at-once Component Part Synthesis Forge variant (needs a stabilized cleanroom and station research of the part, 320 CWU/t): Unverified which multiblock you will use first. — `functionalstorage:oak_1`, `kubejs:uev_super_magnetic_core`

## Tips

- Source: kjs additions/progression/components/component\_parts.js (componentPart(), tier uev; materials in utils/tier\_data.js). Every part is a Component Part Assembly recipe (gtceu:component\_part\_assembly) at 7 864 320 EU/t, with STATION research of the same part of the UHV tier at 1 966 080 EU/t and 160 CWU/t (176 for computational matrix and catalyst core). Amounts use the pack formulas: x5 for the scaled ones, x32 for the exponential ones.
- Super Magnetic Core: 1 long magnetic zapolgium rod · 2 magnetic dysprosium rod · 3 starium alloy rod · 16 fine adamantine wire · 2 mythrolic alloy tiny fluid pipe · 2 500 mB superstate helium 3; 15 s; 160 CWU/t. Catalyst Core: 4 starium alloy rod · 1 reinforced fusion glass · 2 decaying star · 32 fine enriched pallarovium alloy wire · 1 uhv emitter · 4 magmada alloy ring · 1 152 mB isovol; 24 s; 176 CWU/t. High Strength Panel: 1 dense starium alloy plate · 1 UV circuit · 4 magmada alloy screw · 720 mB poly 34 ethylenedioxythiophene polystyrene sulfonate; 10 s; 160 CWU/t. Micropower Router: 4 cerium tritelluride double cable · 2 starium alloy plate · 1 UHV circuit · 4 starium alloy bolt · 720 mB perfluoroelastomer rubber; 12 s; 160 CWU/t.
- The UEV circuit tag holds the runic processor mainframe, the draconic processor computer and the abyssal processor assembly (utils/tags.js; the tag also holds the tier universal circuit). Each computational matrix eats 6 circuits of three tiers, so the circuit lines (uev\_circuits) set the pace.
- Quirk in the pack script: the High Strength Panel lists its alloy fluid as the id 'gtceu:mythrolic\_alloy 288' and the builder appends the amount again. Whether KubeJS reads that as 288 mB of molten mythrolic alloy is Unverified: open the recipe in the Recipe Browser before building the line.
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

- **Main source for:** `kubejs:uev_super_magnetic_core`, `kubejs:uev_catalyst_core`, `kubejs:uev_high_strength_panel`, `kubejs:uev_micropower_router`
