---
kind: chain
id: uhv_parts
order: 1830
data:
  t: |-
    UHV component parts 1/2 (Component Part Assembly, 1 966 080 EU/t): voltage coil, computational matrix, transmission assembly, precision drive mechanism - first unlocked by researching RUINED parts looted in Abydos
  inf: true
  "n":
    - - rp
      - Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data
      - x
      - kubejs:ruined_computational_matrix
    - - g1
      - neutronium tiny pipe · long magnetic dysprosium rod · 32 fine TPD 241 wire · 1 B liquid helium
      - g
      - functionalstorage:oak_1
      - - [Neutronium tiny fluid pipe, "gtceu:neutronium_tiny_fluid_pipe"]
        - [Long magnetic dysprosium rod, "gtceu:long_magnetic_dysprosium_rod"]
        - [Fine TPD 241 wire, "gtceu:fine_thorium_plut_duranide_241_wire"]
        - [Liquid helium, "gtceu:liquid_helium_bucket"]
    - [a1, "CPA · 10 s", m, "gtceu:component_part_assembly"]
    - [p1, UHV Voltage Coil, x, "kubejs:uhv_voltage_coil"]
    - - g2
      - zalloy frame · UHV circuit · 2 UV circuit · 3 ZPM circuit · 4 europium cable · 4 zalloy bolt · 2304 mB ITLC solder
      - g
      - functionalstorage:oak_1
      - - [Zalloy frame, "gtceu:zalloy_frame"]
        - [Zalloy bolt, "gtceu:zalloy_bolt"]
        - [Europium cable, "gtceu:europium_single_cable"]
    - [a2, "CPA · 20 s", m, "gtceu:component_part_assembly"]
    - [p2, UHV Computational Matrix, x, "kubejs:uhv_computational_matrix"]
    - - g3
      - neutronium frame · UV motor · 2 zalloy rod · 2 ring · 4 round · 16 fine zirconium wire · 2 B tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [Neutronium frame, "gtceu:neutronium_frame"]
        - [UV motor, "gtceu:uv_electric_motor"]
        - [Fine zirconium wire, "gtceu:fine_zirconium_wire"]
    - [a3, "CPA · 16 s", m, "gtceu:component_part_assembly"]
    - [p3, UHV Transmission Assembly, x, "kubejs:uhv_transmission_assembly"]
    - - g4
      - zalloy frame · UV motor · UV circuit · zircalloy-4 gear · small zalloy gear · 8 round · 2 B tungsten disulfide · 2304 mB perfluoroelastomer
      - g
      - functionalstorage:oak_1
      - - [Zircalloy-4 gear, "gtceu:zircalloy_4_gear"]
        - [Small zalloy gear, "gtceu:small_zalloy_gear"]
        - [Perfluoroelastomer rubber, "gtceu:perfluoroelastomer_rubber_bucket"]
    - [a4, "CPA · 24 s", m, "gtceu:component_part_assembly"]
    - [p4, UHV Precision Drive Mechanism, x, "kubejs:uhv_precision_drive_mechanism"]
  e:
    - [rp, a1, research]
    - [rp, a2, research]
    - [rp, a3, research]
    - [rp, a4, research]
    - [g1, a1, "1"]
    - [a1, p1, "1 / 10 s"]
    - [g2, a2, "1"]
    - [a2, p2, "1 / 20 s"]
    - [g3, a3, "1"]
    - [a3, p3, "1 / 16 s"]
    - [g4, a4, "1"]
    - [a4, p4, "1 / 24 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/component_parts.js with the uhv column of tier_data.js (verified numbers). The Component Part Assembly (ZPM-era multi, zpm_multis) runs each part as a recipe of EU x 4 = 4 x VA[UV] = 1 966 080 EU/t (a UHV-tier recipe: UV 4A hatch or UHV hatch) with a station research: for UHV the research item is the RUINED part (`ruined_<part>`, Abydos structure loot: quest ‘Ruined Component Parts’), for UEV the UHV part and so on. Research CWU: 128 CWU/t for the default parts (voltage coil, transmission, drive, valve, magnetic core, panel, router) and 144 CWU/t for the special ones (computational matrix, catalyst core), EU VA[UV]. Ruined parts can be duplicated first (assembler, 1200 ticks at VA[UHV]: 1 ruined part + 4 dense enriched naquadah plates + 1 fine ancient runicalium wire + 1440 mB naquadria → 2 ruined parts).
    - |-
      Recipes: voltage coil: 1 neutronium TINY fluid pipe + 1 long magnetic dysprosium rod + 32 fine thorium plutonium duranide 241 wire + 1000 mB liquid helium, 200 ticks, research uv_voltage_coil (not a ruined part). Computational matrix: 1 zalloy frame + 1 UHV + 2 UV + 3 ZPM circuits + 4 europium single cables + 4 zalloy bolts + 2304 mB ITLC solder, 400 ticks. Transmission assembly: 1 neutronium frame + 1 UV motor + 2 zalloy rods + 2 zalloy rings + 4 zalloy rounds + 16 fine zirconium wire + 2000 mB tungsten disulfide, 320 ticks. Precision drive: 1 zalloy frame + 1 UV motor + 1 UV circuit + 1 zircalloy-4 gear + 1 small zalloy gear + 8 zalloy rounds + 2000 mB tungsten disulfide + 2304 mB perfluoroelastomer rubber, 480 ticks.
    - |-
      Where each part goes (uhv_components): transmission assembly: motor, piston, arm; micropower router in every component; computational matrix: arm, emitter, sensor, field generator; precision drive: conveyor, arm. Each part is one item per recipe (the router several), so a complete UHV machine-component set is roughly 20 parts.
    - |-
      Tungsten disulfide (kjs misc_materials.js: LCR 4 tungsten trioxide + 3 B hydrogen sulfide → 3 dust, 480 ticks, VHA[ZPM]) must be a fluid for the lubricant slot: Unverified how it is liquefied (melting in an extractor/fluid solidifier chain). Perfluoroelastomer rubber: the pack line kjs lines/polymers/perfluoroelastomer.js (Unverified here).
    - |-
      Sub-steps people skip: (1) UHV tier hatches before the CPA: 1 966 080 EU/t; (2) the research needs ruined parts which are LOOT: duplicate them at 2:1 before research; (3) liquid helium: a gas line (1 B per coil); (4) every part consumes UV motors and UV circuits, so the UV era lines have to keep running.
    - |-
      Unverified: tungsten disulfide liquefaction, perfluoroelastomer route, the exact data carrier.
  b:
    - ["gtceu:component_part_assembly", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 18]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:ruined_computational_matrix
        - gtceu:zalloy_frame
        - gtceu:uv_electric_motor
      t: |-
        Drawers first, one per input: ruined parts, tiny pipes, magnetic rods, TPD wire, zalloy frames / bolts / rods / rings / rounds, circuits (4 tiers), cables, motors, zircalloy gears, wire. Drums: liquid helium, ITLC solder, tungsten disulfide, perfluoroelastomer.
    - i: ["gtceu:research_station", "kubejs:ruined_computational_matrix", "gtceu:data_module"]
      t: |-
        Research each part once: ruined part (or the UV voltage coil) + a data module in the Object Holder, 128 or 144 CWU/t at 491 520 EU/t. Needs the Network Switch + 4 to 5 HPCAs (uv_research).
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_voltage_coil"]
      t: |-
        Voltage coil recipe first (no loot needed): helium by Pipez fluid pipe, wire and rod by one router.
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_computational_matrix", "kubejs:uhv_transmission_assembly"]
      t: |-
        Matrix and transmission: in the same CPA only one recipe runs at a time: use two CPAs or switch drawers; output drawers Keep Exact 4 each.
    - i: ["gtceu:component_part_assembly", "kubejs:uhv_precision_drive_mechanism"]
      t: |-
        Precision drive: the lubricant and rubber from drums with valves; 24 s per part.
    - i: ["functionalstorage:oak_1", "kubejs:uhv_voltage_coil"]
      t: |-
        Output drawers: Keep Exact 2 to 4 per part; routers feed uhv_components.
---
# UHV component parts 1/2 (Component Part Assembly, 1 966 080 EU/t): voltage coil, computational matrix, transmission assembly, precision drive mechanism - first unlocked by researching RUINED parts looted in Abydos

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_parts` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-a1">
<div class="gt-head"><span class="gt-mname">CPA · 10 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data (kubejs:ruined_computational_matrix) - research"><img class="gt-ico" src="../../assets/icons/kubejs__ruined_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruined Computational Matrix</span><span class="gt-note">Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data</span><b class="gt-q">research</b></span><span class="gt-slot gt-group" title="neutronium tiny pipe · long magnetic dysprosium rod · 32 fine TPD 241 wire · 1 B liquid helium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">neutronium tiny pipe · long magnetic dysprosium rod · 32 fine TPD 241 wire · 1 B liquid helium</span><span class="gt-sub"><span>Neutronium tiny fluid pipe</span><span>Long magnetic dysprosium rod</span><span>Fine TPD 241 wire</span><span>Liquid helium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Voltage Coil (kubejs:uhv_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/kubejs__uhv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Voltage Coil</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a2">
<div class="gt-head"><span class="gt-mname">CPA · 20 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data (kubejs:ruined_computational_matrix) - research"><img class="gt-ico" src="../../assets/icons/kubejs__ruined_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruined Computational Matrix</span><span class="gt-note">Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data</span><b class="gt-q">research</b></span><span class="gt-slot gt-group" title="zalloy frame · UHV circuit · 2 UV circuit · 3 ZPM circuit · 4 europium cable · 4 zalloy bolt · 2304 mB ITLC solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">zalloy frame · UHV circuit · 2 UV circuit · 3 ZPM circuit · 4 europium cable · 4 zalloy bolt · 2304 mB ITLC solder</span><span class="gt-sub"><span>Zalloy frame</span><span>Zalloy bolt</span><span>Europium cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Computational Matrix (kubejs:uhv_computational_matrix) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__uhv_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Computational Matrix</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a3">
<div class="gt-head"><span class="gt-mname">CPA · 16 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data (kubejs:ruined_computational_matrix) - research"><img class="gt-ico" src="../../assets/icons/kubejs__ruined_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruined Computational Matrix</span><span class="gt-note">Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data</span><b class="gt-q">research</b></span><span class="gt-slot gt-group" title="neutronium frame · UV motor · 2 zalloy rod · 2 ring · 4 round · 16 fine zirconium wire · 2 B tungsten disulfide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">neutronium frame · UV motor · 2 zalloy rod · 2 ring · 4 round · 16 fine zirconium wire · 2 B tungsten disulfide</span><span class="gt-sub"><span>Neutronium frame</span><span>UV motor</span><span>Fine zirconium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Transmission Assembly (kubejs:uhv_transmission_assembly) - 1 / 16 s"><img class="gt-ico" src="../../assets/icons/kubejs__uhv_transmission_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Transmission Assembly</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a4">
<div class="gt-head"><span class="gt-mname">CPA · 24 s</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data (kubejs:ruined_computational_matrix) - research"><img class="gt-ico" src="../../assets/icons/kubejs__ruined_computational_matrix.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruined Computational Matrix</span><span class="gt-note">Ruined component parts (Abydos loot) → Research Station 128 to 144 CWU/t → data</span><b class="gt-q">research</b></span><span class="gt-slot gt-group" title="zalloy frame · UV motor · UV circuit · zircalloy-4 gear · small zalloy gear · 8 round · 2 B tungsten disulfide · 2304 mB perfluoroelastomer (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">zalloy frame · UV motor · UV circuit · zircalloy-4 gear · small zalloy gear · 8 round · 2 B tungsten disulfide · 2304 mB perfluoroelastomer</span><span class="gt-sub"><span>Zircalloy-4 gear</span><span>Small zalloy gear</span><span>Perfluoroelastomer rubber</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__component_part_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">24 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Precision Drive Mechanism (kubejs:uhv_precision_drive_mechanism) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/kubejs__uhv_precision_drive_mechanism.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Precision Drive Mechanism</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:component_part_assembly</code></div>
</div>
</div>

## Flow

- [CPA · 10 s](#m-a1)
- [CPA · 20 s](#m-a2)
- [CPA · 16 s](#m-a3)
- [CPA · 24 s](#m-a4)

## How to build

1. Drawers first, one per input: ruined parts, tiny pipes, magnetic rods, TPD wire, zalloy frames / bolts / rods / rings / rounds, circuits (4 tiers), cables, motors, zircalloy gears, wire. Drums: liquid helium, ITLC solder, tungsten disulfide, perfluoroelastomer. — `functionalstorage:oak_1`, `kubejs:ruined_computational_matrix`, `gtceu:zalloy_frame`, `gtceu:uv_electric_motor`
2. Research each part once: ruined part (or the UV voltage coil) + a data module in the Object Holder, 128 or 144 CWU/t at 491 520 EU/t. Needs the Network Switch + 4 to 5 HPCAs (uv\_research). — `gtceu:research_station`, `kubejs:ruined_computational_matrix`, `gtceu:data_module`
3. Voltage coil recipe first (no loot needed): helium by Pipez fluid pipe, wire and rod by one router. — `gtceu:component_part_assembly`, `kubejs:uhv_voltage_coil`
4. Matrix and transmission: in the same CPA only one recipe runs at a time: use two CPAs or switch drawers; output drawers Keep Exact 4 each. — `gtceu:component_part_assembly`, `kubejs:uhv_computational_matrix`, `kubejs:uhv_transmission_assembly`
5. Precision drive: the lubricant and rubber from drums with valves; 24 s per part. — `gtceu:component_part_assembly`, `kubejs:uhv_precision_drive_mechanism`
6. Output drawers: Keep Exact 2 to 4 per part; routers feed uhv\_components. — `functionalstorage:oak_1`, `kubejs:uhv_voltage_coil`

## Tips

- Source: kjs additions/progression/components/component\_parts.js with the uhv column of tier\_data.js (verified numbers). The Component Part Assembly (ZPM-era multi, zpm\_multis) runs each part as a recipe of EU x 4 = 4 x VA\[UV\] = 1 966 080 EU/t (a UHV-tier recipe: UV 4A hatch or UHV hatch) with a station research: for UHV the research item is the RUINED part (\`ruined\_&lt;part&gt;\`, Abydos structure loot: quest ‘Ruined Component Parts’), for UEV the UHV part and so on. Research CWU: 128 CWU/t for the default parts (voltage coil, transmission, drive, valve, magnetic core, panel, router) and 144 CWU/t for the special ones (computational matrix, catalyst core), EU VA\[UV\]. Ruined parts can be duplicated first (assembler, 1200 ticks at VA\[UHV\]: 1 ruined part + 4 dense enriched naquadah plates + 1 fine ancient runicalium wire + 1440 mB naquadria → 2 ruined parts).
- Recipes: voltage coil: 1 neutronium TINY fluid pipe + 1 long magnetic dysprosium rod + 32 fine thorium plutonium duranide 241 wire + 1000 mB liquid helium, 200 ticks, research uv\_voltage\_coil (not a ruined part). Computational matrix: 1 zalloy frame + 1 UHV + 2 UV + 3 ZPM circuits + 4 europium single cables + 4 zalloy bolts + 2304 mB ITLC solder, 400 ticks. Transmission assembly: 1 neutronium frame + 1 UV motor + 2 zalloy rods + 2 zalloy rings + 4 zalloy rounds + 16 fine zirconium wire + 2000 mB tungsten disulfide, 320 ticks. Precision drive: 1 zalloy frame + 1 UV motor + 1 UV circuit + 1 zircalloy-4 gear + 1 small zalloy gear + 8 zalloy rounds + 2000 mB tungsten disulfide + 2304 mB perfluoroelastomer rubber, 480 ticks.
- Where each part goes (uhv\_components): transmission assembly: motor, piston, arm; micropower router in every component; computational matrix: arm, emitter, sensor, field generator; precision drive: conveyor, arm. Each part is one item per recipe (the router several), so a complete UHV machine-component set is roughly 20 parts.
- Tungsten disulfide (kjs misc\_materials.js: LCR 4 tungsten trioxide + 3 B hydrogen sulfide → 3 dust, 480 ticks, VHA\[ZPM\]) must be a fluid for the lubricant slot: Unverified how it is liquefied (melting in an extractor/fluid solidifier chain). Perfluoroelastomer rubber: the pack line kjs lines/polymers/perfluoroelastomer.js (Unverified here).
- Sub-steps people skip: (1) UHV tier hatches before the CPA: 1 966 080 EU/t; (2) the research needs ruined parts which are LOOT: duplicate them at 2:1 before research; (3) liquid helium: a gas line (1 B per coil); (4) every part consumes UV motors and UV circuits, so the UV era lines have to keep running.
- **Unverified** tungsten disulfide liquefaction, perfluoroelastomer route, the exact data carrier.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 18 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `kubejs:uhv_voltage_coil`, `kubejs:uhv_computational_matrix`, `kubejs:uhv_transmission_assembly`, `kubejs:uhv_precision_drive_mechanism`
