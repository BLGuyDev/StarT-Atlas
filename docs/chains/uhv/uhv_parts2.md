---
kind: chain
id: uhv_parts2
order: 1840
data:
  t: |-
    UHV component parts 2/2 (Component Part Assembly): microfluidic flow valve, super magnetic core, catalyst core, high strength panel, micropower router
  inf: true
  "n":
    - - g1
      - UV fluid regulator · zapolgium small pipe · 2 zalloy plate · 4 round · 4 SBR ring · 2 zalloy ring · 576 mB PEEK
      - g
      - functionalstorage:oak_1
      - - [UV fluid regulator, "gtceu:uv_fluid_regulator"]
        - [Zapolgium small fluid pipe, "gtceu:zapolgium_small_fluid_pipe"]
        - [SBR ring, "gtceu:styrene_butadiene_rubber_ring"]
    - [a1, "CPA · 16 s", m, "gtceu:component_part_assembly"]
    - - g2
      - long magnetic dysprosium rod · 2 magnetic samarium rod · 3 zalloy rod · 16 fine zirconium wire · 2 zapolgium tiny pipe · 2 B liquid helium
      - g
      - functionalstorage:oak_1
      - - [Magnetic samarium rod, "gtceu:magnetic_samarium_rod"]
        - [Zapolgium tiny fluid pipe, "gtceu:zapolgium_tiny_fluid_pipe"]
    - [a2, "CPA · 15 s", m, "gtceu:component_part_assembly"]
    - - g3
      - |-
        4 zalloy rod · reinforced fusion glass · 2 gravi star · 32 fine RTAN wire · UV emitter · 4 zircalloy-4 ring · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Reinforced fusion glass, "kubejs:reinforced_fusion_glass"]
        - [Gravi star, "gtceu:gravi_star"]
        - [UV emitter, "gtceu:uv_emitter"]
        - [Zircalloy-4 ring, "gtceu:zircalloy_4_ring"]
    - [a3, "CPA · 24 s", m, "gtceu:component_part_assembly"]
    - - g4
      - dense zalloy plate · ZPM circuit · 4 zircalloy-4 screw · 288 mB neutronium · 576 mB PEEK
      - g
      - functionalstorage:oak_1
      - [[Dense zalloy plate, "gtceu:dense_zalloy_plate"], [Zircalloy-4 screw, "gtceu:zircalloy_4_screw"]]
    - [a4, "CPA · 10 s", m, "gtceu:component_part_assembly"]
    - - g5
      - |-
        4 europium double cable · 2 zalloy plate · UV circuit · 4 zalloy bolt · 576 mB perfluoroelastomer
      - g
      - functionalstorage:oak_1
      - [[Europium double cable, "gtceu:europium_double_cable"]]
    - [a5, "CPA · 12 s", m, "gtceu:component_part_assembly"]
    - - out
      - |-
        UHV parts: valve, magnetic core, catalyst core, panel, router
      - g
      - functionalstorage:oak_1
      - - [Flow valve, "kubejs:uhv_microfluidic_flow_valve"]
        - [Super magnetic core, "kubejs:uhv_super_magnetic_core"]
        - [Catalyst core, "kubejs:uhv_catalyst_core"]
        - [High strength panel, "kubejs:uhv_high_strength_panel"]
        - [Micropower router, "kubejs:uhv_micropower_router"]
  e:
    - [g1, a1, "1"]
    - [a1, out, "1 / 16 s"]
    - [g2, a2, "1"]
    - [a2, out, "1 / 15 s"]
    - [g3, a3, "1"]
    - [a3, out, "1 / 24 s"]
    - [g4, a4, "1"]
    - [a4, out, "1 / 10 s"]
    - [g5, a5, "1"]
    - [a5, out, "1 / 12 s"]
  tips:
    - |-
      Source: component_parts.js, uhv column (verified; the same CPA EU x 4 = 1 966 080 EU/t, research of the ruined part at 128 CWU/t, catalyst core 144 CWU/t). Microfluidic flow valve: 1 UV fluid regulator (a GT item made from a UV pump; the pack’s own regulator recipe, pump + 2 circuits, is written for UHV and up: Unverified for UV) + 1 zapolgium small fluid pipe + 2 zalloy plates + 4 zalloy rounds + 4 SBR rings + 2 zalloy rings + 576 mB PEEK, 320 ticks. Super magnetic core: 1 long magnetic dysprosium rod + 2 magnetic SAMARIUM rods + 3 zalloy rods + 16 fine zirconium wire + 2 zapolgium tiny pipes + 2000 mB liquid helium, 300 ticks. Catalyst core: 4 zalloy rods + 1 reinforced fusion glass + 2 gravi stars + 32 fine RTAN wire + 1 UV emitter + 4 zircalloy-4 rings + 576 mB naquadria, 480 ticks. High strength panel: 1 dense zalloy plate + 1 ZPM-tag circuit + 4 zircalloy-4 screws + 288 mB molten neutronium + 576 mB PEEK, 200 ticks (the script writes the neutronium fluid string twice, so the amount may differ in game: Unverified). Micropower router: 4 europium double cables + 2 zalloy plates + 1 UV-tag circuit + 4 zalloy bolts + 576 mB perfluoroelastomer rubber, 240 ticks.
    - |-
      Per UHV component (uhv_components): the micropower router is in every one (arm and field generator 2), the super magnetic core in the motor, the microfluidic valve in the pump, the high strength panel in the conveyor, piston and field generator, the catalyst core in the field generator, emitter and sensor. The reinforced fusion glass of the catalyst core is the uv_fusion glass recipe (fusion glass + ZPM emitter + 6 complex panels + 432 mB PEEK, 2 per craft); the gravi stars (2 each) come from uv_gravi.
    - |-
      Magnetic samarium rod: standard GT polarizer on a samarium rod; samarium is a rare earth (uv_rare_earth, ZPM-era sieves). Zapolgium pipes: a pipe from zapolgium ingots (uhv_zapolgium) in a pipe extruder; fine wires from wiremill; zircalloy-4 and zalloy parts from uhv_alloys.
    - |-
      Sub-steps people skip: (1) catalyst core is a 144 CWU/t research (data module or DNA disk): schedule it with the bridged HPCAs; (2) four different data modules are needed for the matrix, catalyst core, and the rest; (3) 2 gravi stars per catalyst core: neutronium 576 mB per core; (4) the CPA takes one recipe at a time, so make the router first (it is in all the others).
    - |-
      Unverified: neutronium fluid amount in the panel recipe, fluid regulator tier, the polarized samarium route.
  b:
    - ["gtceu:component_part_assembly", 2]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 22]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uv_fluid_regulator", "gtceu:dense_zalloy_plate", "gtceu:gravi_star"]
      t: |-
        Drawers first, one per input: fluid regulators, small / tiny zapolgium pipes, zalloy plates / rods / rings / rounds / bolts, SBR rings, magnetic rods (dysprosium long, samarium), fine wires (zirconium, RTAN), reinforced glass, gravi stars (Keep Exact 2), UV emitters, zircalloy rings and screws, europium double cables, circuits. Drums: PEEK, perfluoroelastomer, liquid helium, naquadria, neutronium.
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_micropower_router"]
      t: |-
        Router first (it is in every component): 12 s per router in a CPA; output drawer Keep Exact 8.
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_microfluidic_flow_valve", "kubejs:uhv_super_magnetic_core"]
      t: |-
        Valve and core: two CPA runs, or one CPA with drawer swaps. Helium by a Pipez fluid pipe with a valve.
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_catalyst_core", "kubejs:uhv_high_strength_panel"]
      t: Catalyst core (24 s, 2 gravi stars) and high strength panel (10 s, 288 mB neutronium + 576 mB PEEK).
    - i: ["gtceu:research_station", "kubejs:ruined_catalyst_core", "gtceu:data_module"]
      t: |-
        Research before each CPA recipe: the ruined version of the part in the Object Holder with a data module.
    - i: ["functionalstorage:oak_1", "kubejs:uhv_catalyst_core"]
      t: Output drawers Keep Exact 2 to 4; routers to uhv_components.
---
# UHV component parts 2/2 (Component Part Assembly): microfluidic flow valve, super magnetic core, catalyst core, high strength panel, micropower router

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_parts2` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-a1">
<div class="gt-head"><span class="gt-mname">CPA · 16 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV fluid regulator · zapolgium small pipe · 2 zalloy plate · 4 round · 4 SBR ring · 2 zalloy ring · 576 mB PEEK (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV fluid regulator · zapolgium small pipe · 2 zalloy plate · 4 round · 4 SBR ring · 2 zalloy ring · 576 mB PEEK</span><span class="gt-sub"><span>UV fluid regulator</span><span>Zapolgium small fluid pipe</span><span>SBR ring</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="UHV parts: valve, magnetic core, catalyst core, panel, router (functionalstorage:oak_1) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV parts: valve, magnetic core, catalyst core, panel, router</span><span class="gt-sub"><span>Flow valve</span><span>Super magnetic core</span><span>Catalyst core</span><span>High strength panel</span><span>Micropower router</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a2">
<div class="gt-head"><span class="gt-mname">CPA · 15 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="long magnetic dysprosium rod · 2 magnetic samarium rod · 3 zalloy rod · 16 fine zirconium wire · 2 zapolgium tiny pipe · 2 B liquid helium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">long magnetic dysprosium rod · 2 magnetic samarium rod · 3 zalloy rod · 16 fine zirconium wire · 2 zapolgium tiny pipe · 2 B liquid helium</span><span class="gt-sub"><span>Magnetic samarium rod</span><span>Zapolgium tiny fluid pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="UHV parts: valve, magnetic core, catalyst core, panel, router (functionalstorage:oak_1) - 1 / 15 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV parts: valve, magnetic core, catalyst core, panel, router</span><span class="gt-sub"><span>Flow valve</span><span>Super magnetic core</span><span>Catalyst core</span><span>High strength panel</span><span>Micropower router</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a3">
<div class="gt-head"><span class="gt-mname">CPA · 24 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 zalloy rod · reinforced fusion glass · 2 gravi star · 32 fine RTAN wire · UV emitter · 4 zircalloy-4 ring · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 zalloy rod · reinforced fusion glass · 2 gravi star · 32 fine RTAN wire · UV emitter · 4 zircalloy-4 ring · 576 mB naquadria</span><span class="gt-sub"><span>Reinforced fusion glass</span><span>Gravi star</span><span>UV emitter</span><span>Zircalloy-4 ring</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">24 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="UHV parts: valve, magnetic core, catalyst core, panel, router (functionalstorage:oak_1) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV parts: valve, magnetic core, catalyst core, panel, router</span><span class="gt-sub"><span>Flow valve</span><span>Super magnetic core</span><span>Catalyst core</span><span>High strength panel</span><span>Micropower router</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a4">
<div class="gt-head"><span class="gt-mname">CPA · 10 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="dense zalloy plate · ZPM circuit · 4 zircalloy-4 screw · 288 mB neutronium · 576 mB PEEK (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">dense zalloy plate · ZPM circuit · 4 zircalloy-4 screw · 288 mB neutronium · 576 mB PEEK</span><span class="gt-sub"><span>Dense zalloy plate</span><span>Zircalloy-4 screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="UHV parts: valve, magnetic core, catalyst core, panel, router (functionalstorage:oak_1) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV parts: valve, magnetic core, catalyst core, panel, router</span><span class="gt-sub"><span>Flow valve</span><span>Super magnetic core</span><span>Catalyst core</span><span>High strength panel</span><span>Micropower router</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a5">
<div class="gt-head"><span class="gt-mname">CPA · 12 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 europium double cable · 2 zalloy plate · UV circuit · 4 zalloy bolt · 576 mB perfluoroelastomer (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 europium double cable · 2 zalloy plate · UV circuit · 4 zalloy bolt · 576 mB perfluoroelastomer</span><span class="gt-sub"><span>Europium double cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="UHV parts: valve, magnetic core, catalyst core, panel, router (functionalstorage:oak_1) - 1 / 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV parts: valve, magnetic core, catalyst core, panel, router</span><span class="gt-sub"><span>Flow valve</span><span>Super magnetic core</span><span>Catalyst core</span><span>High strength panel</span><span>Micropower router</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [CPA · 16 s](#m-a1)
- [CPA · 15 s](#m-a2)
- [CPA · 24 s](#m-a3)
- [CPA · 10 s](#m-a4)
- [CPA · 12 s](#m-a5)

## How to build

1. Drawers first, one per input: fluid regulators, small / tiny zapolgium pipes, zalloy plates / rods / rings / rounds / bolts, SBR rings, magnetic rods (dysprosium long, samarium), fine wires (zirconium, RTAN), reinforced glass, gravi stars (Keep Exact 2), UV emitters, zircalloy rings and screws, europium double cables, circuits. Drums: PEEK, perfluoroelastomer, liquid helium, naquadria, neutronium. — `functionalstorage:oak_1`, `gtceu:uv_fluid_regulator`, `gtceu:dense_zalloy_plate`, `gtceu:gravi_star`
2. Router first (it is in every component): 12 s per router in a CPA; output drawer Keep Exact 8. — `gtceu:component_part_assembly`, `kubejs:uhv_micropower_router`
3. Valve and core: two CPA runs, or one CPA with drawer swaps. Helium by a Pipez fluid pipe with a valve. — `gtceu:component_part_assembly`, `kubejs:uhv_microfluidic_flow_valve`, `kubejs:uhv_super_magnetic_core`
4. Catalyst core (24 s, 2 gravi stars) and high strength panel (10 s, 288 mB neutronium + 576 mB PEEK). — `gtceu:component_part_assembly`, `kubejs:uhv_catalyst_core`, `kubejs:uhv_high_strength_panel`
5. Research before each CPA recipe: the ruined version of the part in the Object Holder with a data module. — `gtceu:research_station`, `kubejs:ruined_catalyst_core`, `gtceu:data_module`
6. Output drawers Keep Exact 2 to 4; routers to uhv\_components. — `functionalstorage:oak_1`, `kubejs:uhv_catalyst_core`

## Tips

- Source: component\_parts.js, uhv column (verified; the same CPA EU x 4 = 1 966 080 EU/t, research of the ruined part at 128 CWU/t, catalyst core 144 CWU/t). Microfluidic flow valve: 1 UV fluid regulator (a GT item made from a UV pump; the pack’s own regulator recipe, pump + 2 circuits, is written for UHV and up: Unverified for UV) + 1 zapolgium small fluid pipe + 2 zalloy plates + 4 zalloy rounds + 4 SBR rings + 2 zalloy rings + 576 mB PEEK, 320 ticks. Super magnetic core: 1 long magnetic dysprosium rod + 2 magnetic SAMARIUM rods + 3 zalloy rods + 16 fine zirconium wire + 2 zapolgium tiny pipes + 2000 mB liquid helium, 300 ticks. Catalyst core: 4 zalloy rods + 1 reinforced fusion glass + 2 gravi stars + 32 fine RTAN wire + 1 UV emitter + 4 zircalloy-4 rings + 576 mB naquadria, 480 ticks. High strength panel: 1 dense zalloy plate + 1 ZPM-tag circuit + 4 zircalloy-4 screws + 288 mB molten neutronium + 576 mB PEEK, 200 ticks (the script writes the neutronium fluid string twice, so the amount may differ in game: Unverified). Micropower router: 4 europium double cables + 2 zalloy plates + 1 UV-tag circuit + 4 zalloy bolts + 576 mB perfluoroelastomer rubber, 240 ticks.
- Per UHV component (uhv\_components): the micropower router is in every one (arm and field generator 2), the super magnetic core in the motor, the microfluidic valve in the pump, the high strength panel in the conveyor, piston and field generator, the catalyst core in the field generator, emitter and sensor. The reinforced fusion glass of the catalyst core is the uv\_fusion glass recipe (fusion glass + ZPM emitter + 6 complex panels + 432 mB PEEK, 2 per craft); the gravi stars (2 each) come from uv\_gravi.
- Magnetic samarium rod: standard GT polarizer on a samarium rod; samarium is a rare earth (uv\_rare\_earth, ZPM-era sieves). Zapolgium pipes: a pipe from zapolgium ingots (uhv\_zapolgium) in a pipe extruder; fine wires from wiremill; zircalloy-4 and zalloy parts from uhv\_alloys.
- Sub-steps people skip: (1) catalyst core is a 144 CWU/t research (data module or DNA disk): schedule it with the bridged HPCAs; (2) four different data modules are needed for the matrix, catalyst core, and the rest; (3) 2 gravi stars per catalyst core: neutronium 576 mB per core; (4) the CPA takes one recipe at a time, so make the router first (it is in all the others).
- **Unverified** neutronium fluid amount in the panel recipe, fluid regulator tier, the polarized samarium route.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:component_part_assembly` | 2 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 22 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `kubejs:uhv_microfluidic_flow_valve`, `kubejs:uhv_super_magnetic_core`, `kubejs:uhv_catalyst_core`, `kubejs:uhv_high_strength_panel`, `kubejs:uhv_micropower_router`, `gtceu:uv_fluid_regulator`
