---
kind: chain
id: uv_components2
order: 1670
data:
  t: |-
    UV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, gravi stars, 96 naquadria foil each, research 32 / 48 CWU/t)
  inf: true
  "n":
    - - g1
      - |-
        4 long tritan steel rod · gear · 3 small gear · 2 motor · piston · 1 UV + 2 ZPM + 4 LuV circuit · 4 YBCO cable · 1152 mB solder · 1000 mB lubricant · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [UV motor, "gtceu:uv_electric_motor"]
        - [UV piston, "gtceu:uv_electric_piston"]
        - [Tritan steel gear, "gtceu:tritan_steel_gear"]
        - [Small tritan steel gear, "gtceu:small_tritan_steel_gear"]
    - [a1, "Assembly Line · 30 s · 122 880 EU/t", m, "gtceu:assembly_line"]
    - [ar, UV Robot Arm, x, "gtceu:uv_robot_arm"]
    - - g2
      - tritan steel frame · motor · 4 long rod · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Tritan steel frame, "gtceu:tritan_steel_frame"]
        - [Gravi star, "gtceu:gravi_star"]
        - [Naquadria foil, "gtceu:naquadria_foil"]
    - [a2, "Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research", m, "gtceu:assembly_line"]
    - [em, UV Emitter, x, "gtceu:uv_emitter"]
    - - g3
      - tritan steel frame · motor · 4 plate · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - [[Tritan steel plate, "gtceu:tritan_steel_plate"]]
    - [a3, "Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research", m, "gtceu:assembly_line"]
    - [se, UV Sensor, x, "gtceu:uv_sensor"]
    - - g4
      - frame · 6 plate · gravi star · 2 UV emitter · 2 UV circuit · 128 fine ENTED wire · 4 YBCO cable · 2304 mB solder · 576 mB naquadria
      - g
      - functionalstorage:oak_1
      - [[Fine ENTED wire, "gtceu:fine_enriched_naquadah_trinium_europium_duranide_wire"]]
    - [a4, "Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research", m, "gtceu:assembly_line"]
    - [fg, UV Field Generator, o, "gtceu:uv_field_generator"]
  e:
    - [g1, a1, "1"]
    - [a1, ar, "1 / 30 s"]
    - [g2, a2, "1"]
    - [a2, em, "1 / 30 s"]
    - [g3, a3, "1"]
    - [a3, se, "1 / 30 s"]
    - [em, g4, "2"]
    - [g4, a4, "1"]
    - [a4, fg, "1 / 30 s"]
  tips:
    - |-
      Source: kjs luv_to_uv_components.js with the uv column of tier_data.js (verified). Robot arm: 4 long tritan steel rods + 1 tritan steel gear + 3 small gears + 2 UV motors + 1 UV piston + 1 UV circuit + 2 ZPM circuits + 4 LuV circuits (the arm asks for three circuit tiers: uv / zpm / luv) + 4 YBCO single cables; 1152 mB solder, 1000 mB lubricant, 576 mB naquadria. Emitter: 1 tritan steel frame + 1 UV motor + 4 long rods + 1 gravi star + 2 UV circuits + 96 naquadria foil (64 + 32) + 4 cables; 1152 mB solder + 576 mB naquadria. Sensor: same but 4 tritan steel plates instead of the long rods (frame, motor, 4 plates, gravi star, 2 circuits, 96 naquadria foil, 4 cables). Field generator: 1 frame + 6 plates + 1 gravi star + 2 UV emitters + 2 UV circuits + 128 fine ENTED wire (64 + 64) + 4 cables; 2304 mB solder + 576 mB naquadria.
    - |-
      Research: the arm is DEFAULT research (32 CWU/t, 122 880 EU/t, scanned from the ZPM arm). Emitter, sensor and field generator are SPECIAL research: 48 CWU/t at 491 520 EU/t (VA[UV]), scanned from the ZPM emitter / sensor / field generator. The recipes sit at 122 880 EU/t, so the Assembly Line only needs ZPM power, but the Research Station needs a UV-tier hatch for the research EU/t (491 520 EU/t: ZPM 4A hatch). 48 CWU/t is one HPCA fully populated with 3 advanced components (uv_research).
    - |-
      Circuits per component: robot arm 1 UV + 2 ZPM + 4 LuV; emitter 2 UV; sensor 2 UV; field generator 2 UV + 2 UV emitters = 6 UV circuits. A hull-based machine of the UV tier usually needs 1 to 2 emitters or sensors: UV circuits and naquadria foil are the real cost. Gravi star: quantum star + 288 mB neutronium in an IV autoclave (uv_gravi), so every emitter, sensor and field generator needs a neutronium feed.
    - |-
      Naquadria foil: 96 foil = 24 ingots (a plate gives 4 foil) per emitter or sensor: that is 3456 mB of naquadria per component and a naquadria line (zpm_naq_products) that runs at fusion-reactor scale (the neutronium run takes 288 mB of it as well).
    - |-
      Sub-steps people skip: (1) emitters first (2 per field generator), the field generator is the LAST item; (2) 128 fine ENTED wire = 16 ingots of the UV superconductor; (3) gravi stars from Keep Exact 4 drawers; (4) the arm needs a UV PISTON and 2 motors, so build the piston line of uv_components first; (5) one Data Bank holds all research orbs.
    - |-
      Unverified: nothing beyond the sources of americium, pure netherite, naquadria, dysprosium.
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
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uv_electric_motor", "gtceu:gravi_star", "gtceu:naquadria_foil"]
      t: |-
        Drawers first, one per input: motors (Keep Exact 4), piston, circuits (UV, ZPM, LuV), tritan steel frames / plates / rods / gears, gravi stars, naquadria foil (Keep Exact 64 × 2), fine ENTED wire, YBCO cables. Drums: ITLC solder, lubricant, naquadria.
    - i: ["gtceu:research_station", "gtceu:zpm_emitter", "gtceu:data_orb"]
      t: |-
        Research: ZPM emitter, sensor and field generator at 48 CWU/t / 491 520 EU/t each, the arm at 32 CWU/t / 122 880 EU/t. One orb per item; orbs into the matching line.
    - i: ["gtceu:assembly_line", "gtceu:uv_robot_arm", "gtceu:uv_emitter"]
      t: |-
        Arm line and emitter line: 30 s each. The arm’s three circuit tiers come from three different drawers (UV, ZPM, LuV): label them.
    - i: ["gtceu:assembly_line", "gtceu:uv_sensor"]
      t: |-
        Sensor line: frame, motor, 4 plates, gravi star, 2 circuits, 96 foil, 4 cables; fluid hatches for solder + naquadria.
    - i: ["gtceu:assembly_line", "gtceu:uv_field_generator"]
      t: |-
        Field generator line last: two emitters by router from the emitter drawer, 128 fine ENTED wire, 6 plates, frame, gravi star.
    - i: ["functionalstorage:oak_1", "gtceu:uv_field_generator"]
      t: Output drawers Keep Exact 2 (field generators 2). They feed the UV fusion reactor (2 ZPM ones, not UV) and the fusion casings (ZPM generator each).
---
# UV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, gravi stars, 96 naquadria foil each, research 32 / 48 CWU/t)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV components and hatches](../../plan/p16.md#uvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 long tritan steel rod · gear · 3 small gear · 2 motor · piston · 1 UV + 2 ZPM + 4 LuV circuit · 4 YBCO cable · 1152 mB solder · 1000 mB lubricant · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 long tritan steel rod · gear · 3 small gear · 2 motor · piston · 1 UV + 2 ZPM + 4 LuV circuit · 4 YBCO cable · 1152 mB solder · 1000 mB lubricant · 576 mB naquadria</span><span class="gt-sub"><span>UV motor</span><span>UV piston</span><span>Tritan steel gear</span><span>Small tritan steel gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Robot Arm (gtceu:uv_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="tritan steel frame · motor · 4 long rod · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">tritan steel frame · motor · 4 long rod · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria</span><span class="gt-sub"><span>Tritan steel frame</span><span>Gravi star</span><span>Naquadria foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Emitter (gtceu:uv_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Emitter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="tritan steel frame · motor · 4 plate · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">tritan steel frame · motor · 4 plate · gravi star · 2 UV circuit · 96 naquadria foil · 4 YBCO cable · 1152 mB solder · 576 mB naquadria</span><span class="gt-sub"><span>Tritan steel plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Sensor (gtceu:uv_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="frame · 6 plate · gravi star · 2 UV emitter · 2 UV circuit · 128 fine ENTED wire · 4 YBCO cable · 2304 mB solder · 576 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">frame · 6 plate · gravi star · 2 UV emitter · 2 UV circuit · 128 fine ENTED wire · 4 YBCO cable · 2304 mB solder · 576 mB naquadria</span><span class="gt-sub"><span>Fine ENTED wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Field Generator (gtceu:uv_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Field Generator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 122 880 EU/t](#m-a1)
- [Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research](#m-a2) → [Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research](#m-a4)
- [Assembly Line · 30 s · 122 880 EU/t · 48 CWU/t research](#m-a3)

### Direct steps

- UV Emitter → frame · 6 plate · gravi star · 2 UV emitter · 2 UV circuit · 128 fine ENTED wire · 4 YBCO cable · 2304 mB solder · 576 mB naquadria (2)

## How to build

1. Drawers first, one per input: motors (Keep Exact 4), piston, circuits (UV, ZPM, LuV), tritan steel frames / plates / rods / gears, gravi stars, naquadria foil (Keep Exact 64 × 2), fine ENTED wire, YBCO cables. Drums: ITLC solder, lubricant, naquadria. — `functionalstorage:oak_1`, `gtceu:uv_electric_motor`, `gtceu:gravi_star`, `gtceu:naquadria_foil`
2. Research: ZPM emitter, sensor and field generator at 48 CWU/t / 491 520 EU/t each, the arm at 32 CWU/t / 122 880 EU/t. One orb per item; orbs into the matching line. — `gtceu:research_station`, `gtceu:zpm_emitter`, `gtceu:data_orb`
3. Arm line and emitter line: 30 s each. The arm’s three circuit tiers come from three different drawers (UV, ZPM, LuV): label them. — `gtceu:assembly_line`, `gtceu:uv_robot_arm`, `gtceu:uv_emitter`
4. Sensor line: frame, motor, 4 plates, gravi star, 2 circuits, 96 foil, 4 cables; fluid hatches for solder + naquadria. — `gtceu:assembly_line`, `gtceu:uv_sensor`
5. Field generator line last: two emitters by router from the emitter drawer, 128 fine ENTED wire, 6 plates, frame, gravi star. — `gtceu:assembly_line`, `gtceu:uv_field_generator`
6. Output drawers Keep Exact 2 (field generators 2). They feed the UV fusion reactor (2 ZPM ones, not UV) and the fusion casings (ZPM generator each). — `functionalstorage:oak_1`, `gtceu:uv_field_generator`

## Tips

- Source: kjs luv\_to\_uv\_components.js with the uv column of tier\_data.js (verified). Robot arm: 4 long tritan steel rods + 1 tritan steel gear + 3 small gears + 2 UV motors + 1 UV piston + 1 UV circuit + 2 ZPM circuits + 4 LuV circuits (the arm asks for three circuit tiers: uv / zpm / luv) + 4 YBCO single cables; 1152 mB solder, 1000 mB lubricant, 576 mB naquadria. Emitter: 1 tritan steel frame + 1 UV motor + 4 long rods + 1 gravi star + 2 UV circuits + 96 naquadria foil (64 + 32) + 4 cables; 1152 mB solder + 576 mB naquadria. Sensor: same but 4 tritan steel plates instead of the long rods (frame, motor, 4 plates, gravi star, 2 circuits, 96 naquadria foil, 4 cables). Field generator: 1 frame + 6 plates + 1 gravi star + 2 UV emitters + 2 UV circuits + 128 fine ENTED wire (64 + 64) + 4 cables; 2304 mB solder + 576 mB naquadria.
- Research: the arm is DEFAULT research (32 CWU/t, 122 880 EU/t, scanned from the ZPM arm). Emitter, sensor and field generator are SPECIAL research: 48 CWU/t at 491 520 EU/t (VA\[UV\]), scanned from the ZPM emitter / sensor / field generator. The recipes sit at 122 880 EU/t, so the Assembly Line only needs ZPM power, but the Research Station needs a UV-tier hatch for the research EU/t (491 520 EU/t: ZPM 4A hatch). 48 CWU/t is one HPCA fully populated with 3 advanced components (uv\_research).
- Circuits per component: robot arm 1 UV + 2 ZPM + 4 LuV; emitter 2 UV; sensor 2 UV; field generator 2 UV + 2 UV emitters = 6 UV circuits. A hull-based machine of the UV tier usually needs 1 to 2 emitters or sensors: UV circuits and naquadria foil are the real cost. Gravi star: quantum star + 288 mB neutronium in an IV autoclave (uv\_gravi), so every emitter, sensor and field generator needs a neutronium feed.
- Naquadria foil: 96 foil = 24 ingots (a plate gives 4 foil) per emitter or sensor: that is 3456 mB of naquadria per component and a naquadria line (zpm\_naq\_products) that runs at fusion-reactor scale (the neutronium run takes 288 mB of it as well).
- Sub-steps people skip: (1) emitters first (2 per field generator), the field generator is the LAST item; (2) 128 fine ENTED wire = 16 ingots of the UV superconductor; (3) gravi stars from Keep Exact 4 drawers; (4) the arm needs a UV PISTON and 2 motors, so build the piston line of uv\_components first; (5) one Data Bank holds all research orbs.
- **Unverified** nothing beyond the sources of americium, pure netherite, naquadria, dysprosium.

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
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:uv_robot_arm`, `gtceu:uv_emitter`, `gtceu:uv_sensor`, `gtceu:uv_field_generator`
