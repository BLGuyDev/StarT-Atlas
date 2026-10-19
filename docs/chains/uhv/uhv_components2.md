---
kind: chain
id: uhv_components2
order: 1860
data:
  t: |-
    UHV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, catalyst cores, computational matrices, research 128 / 144 CWU/t)
  inf: true
  "n":
    - - g1
      - |-
        4 long zalloy rod · precision drive · transmission assembly · motor · piston · 2 computational matrix · 2 router · 2304 mB solder · 2000 mB lubricant · 1152 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [UHV motor, "gtceu:uhv_electric_motor"]
        - [UHV piston, "gtceu:uhv_electric_piston"]
        - [Computational matrix, "kubejs:uhv_computational_matrix"]
    - [a1, "Assembly Line · 30 s · 491 520 EU/t · 128 CWU/t", m, "gtceu:assembly_line"]
    - [ar, UHV Robot Arm, x, "gtceu:uhv_robot_arm"]
    - - g2
      - zalloy frame · motor · 4 long zalloy rod · catalyst core · matrix · 64 neutronium foil · router + 2304 mB solder + 2000 mB lubricant + 1152 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Zalloy frame, "gtceu:zalloy_frame"]
        - [Catalyst core, "kubejs:uhv_catalyst_core"]
        - [Neutronium foil, "gtceu:neutronium_foil"]
    - [a2, "Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - [em, UHV Emitter, x, "gtceu:uhv_emitter"]
    - - g3
      - zalloy frame · motor · 4 zalloy plate · catalyst core · matrix · 64 neutronium foil · router + fluids
      - g
      - functionalstorage:oak_1
      - [[Zalloy plate, "gtceu:zalloy_plate"]]
    - [a3, "Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - [se, UHV Sensor, x, "gtceu:uhv_sensor"]
    - - g4
      - zalloy frame · 2 panel · catalyst core · 2 UHV emitter · matrix · 64 fine RTAN wire · 2 router + 4608 mB solder + 1152 mB naquadria
      - g
      - functionalstorage:oak_1
      - [[Fine RTAN wire, "gtceu:fine_ruthenium_trinium_americium_neutronate_wire"]]
    - [a4, "Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - [fg, UHV Field Generator, o, "gtceu:uhv_field_generator"]
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
      Source: kjs uhv_to_uiv_components.js (verified). Robot arm: 4 long zalloy rods + 1 precision drive mechanism + 1 transmission assembly + 1 UHV motor + 1 UHV piston + 2 computational matrices + 2 micropower routers; solder 2304 + lubricant 2000 + naquadria 1152. Emitter: zalloy frame + UHV motor + 4 long zalloy rods + 1 catalyst core + 1 computational matrix + 64 neutronium foil + 1 router; same fluids. Sensor: same but 4 zalloy plates instead of the rods. Field generator: zalloy frame + 2 high strength panels + 1 catalyst core + 2 UHV emitters + 1 computational matrix + 64 fine RTAN wire + 2 routers; solder 4608 + naquadria 1152. Research (all of the UV items): 128 CWU/t for the arm, 144 CWU/t for emitter, sensor and field generator, 491 520 EU/t.
    - |-
      Neutronium foil: 64 foil per emitter or sensor = 16 neutronium ingots (4 foils per plate/ingot), i.e. 2304 mB of neutronium, or 16 UV-reactor runs of 72 s: a sensor and an emitter cost about 5 reactor-hours with one reactor. RTAN fine wire: the pack adds the fine-wire flag to RTAN (kjs modifications.js); 64 fine wire = 8 ingots. The UHV fusion reactor and the UEV page use these.
    - |-
      UHV circuit count: only the pieces already built by uhv_parts need UHV circuits (1 per matrix) plus UV and ZPM tags; the AL recipes themselves have no circuit inputs. A robot arm needs 2 matrices = 2 UHV + 4 UV + 6 ZPM circuits through the matrix parts, a field generator 3 matrices (its own plus one per emitter).
    - |-
      Where the UHV set is consumed: UHV hatches, the UHV fusion reactor (field generators), the Compact Assembly Line (robot arms), the Super Pressure Heat Chamber (field generator), the Component Nexus, the folding stabiliser, the bacteria synthesizer and every UHV machine.
    - |-
      Sub-steps people skip: (1) emitters first (2 per field generator), the field generator is last; (2) check the CWU/t of the Research Station before you start a 144 CWU/t research; (3) 64 neutronium foil is a foil from a bender, not a ream; (4) one dedicated Assembly Line per product.
    - |-
      Unverified: neutronium foil bender recipe (standard GT foil), CWU totals.
  b:
    - ["gtceu:assembly_line", 4]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 2]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:uhv_computational_matrix
        - kubejs:uhv_catalyst_core
        - gtceu:neutronium_foil
      t: |-
        Drawers first, one per input: motors, piston, matrices, routers, catalyst cores, frames, rods, plates, neutronium foil (Keep Exact 64 x2), fine RTAN wire, panels. Drums: ITLC solder, lubricant, naquadria.
    - i: ["gtceu:research_station", "gtceu:uv_emitter", "gtceu:data_module"]
      t: |-
        Research per item: the UV emitter / sensor / field generator at 144 CWU/t, the UV arm at 128 CWU/t, with a data module (or a DNA disk: uv_data).
    - i: ["gtceu:assembly_line", "gtceu:uhv_robot_arm", "gtceu:uhv_emitter"]
      t: Arm and emitter lines, 30 s each.
    - i: ["gtceu:assembly_line", "gtceu:uhv_sensor"]
      t: Sensor line with its own neutronium foil drawer.
    - i: ["gtceu:assembly_line", "gtceu:uhv_field_generator"]
      t: |-
        Field generator last: two emitters by router, 64 fine RTAN wire, panels, catalyst core, matrix.
    - i: ["functionalstorage:oak_1", "gtceu:uhv_field_generator"]
      t: Output drawers Keep Exact 2.
---
# UHV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, catalyst cores, computational matrices, research 128 / 144 CWU/t)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t · 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 long zalloy rod · precision drive · transmission assembly · motor · piston · 2 computational matrix · 2 router · 2304 mB solder · 2000 mB lubricant · 1152 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 long zalloy rod · precision drive · transmission assembly · motor · piston · 2 computational matrix · 2 router · 2304 mB solder · 2000 mB lubricant · 1152 mB naquadria</span><span class="gt-sub"><span>UHV motor</span><span>UHV piston</span><span>Computational matrix</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Robot Arm (gtceu:uhv_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="zalloy frame · motor · 4 long zalloy rod · catalyst core · matrix · 64 neutronium foil · router + 2304 mB solder + 2000 mB lubricant + 1152 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">zalloy frame · motor · 4 long zalloy rod · catalyst core · matrix · 64 neutronium foil · router + 2304 mB solder + 2000 mB lubricant + 1152 mB naquadria</span><span class="gt-sub"><span>Zalloy frame</span><span>Catalyst core</span><span>Neutronium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Emitter (gtceu:uhv_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Emitter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="zalloy frame · motor · 4 zalloy plate · catalyst core · matrix · 64 neutronium foil · router + fluids (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">zalloy frame · motor · 4 zalloy plate · catalyst core · matrix · 64 neutronium foil · router + fluids</span><span class="gt-sub"><span>Zalloy plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Sensor (gtceu:uhv_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="zalloy frame · 2 panel · catalyst core · 2 UHV emitter · matrix · 64 fine RTAN wire · 2 router + 4608 mB solder + 1152 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">zalloy frame · 2 panel · catalyst core · 2 UHV emitter · matrix · 64 fine RTAN wire · 2 router + 4608 mB solder + 1152 mB naquadria</span><span class="gt-sub"><span>Fine RTAN wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UHV Field Generator (gtceu:uhv_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Field Generator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 491 520 EU/t · 128 CWU/t](#m-a1)
- [Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t](#m-a2) → [Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t](#m-a4)
- [Assembly Line · 30 s · 491 520 EU/t · 144 CWU/t](#m-a3)

### Direct steps

- UHV Emitter → zalloy frame · 2 panel · catalyst core · 2 UHV emitter · matrix · 64 fine RTAN wire · 2 router + 4608 mB solder + 1152 mB naquadria (2)

## How to build

1. Drawers first, one per input: motors, piston, matrices, routers, catalyst cores, frames, rods, plates, neutronium foil (Keep Exact 64 x2), fine RTAN wire, panels. Drums: ITLC solder, lubricant, naquadria. — `functionalstorage:oak_1`, `kubejs:uhv_computational_matrix`, `kubejs:uhv_catalyst_core`, `gtceu:neutronium_foil`
2. Research per item: the UV emitter / sensor / field generator at 144 CWU/t, the UV arm at 128 CWU/t, with a data module (or a DNA disk: uv\_data). — `gtceu:research_station`, `gtceu:uv_emitter`, `gtceu:data_module`
3. Arm and emitter lines, 30 s each. — `gtceu:assembly_line`, `gtceu:uhv_robot_arm`, `gtceu:uhv_emitter`
4. Sensor line with its own neutronium foil drawer. — `gtceu:assembly_line`, `gtceu:uhv_sensor`
5. Field generator last: two emitters by router, 64 fine RTAN wire, panels, catalyst core, matrix. — `gtceu:assembly_line`, `gtceu:uhv_field_generator`
6. Output drawers Keep Exact 2. — `functionalstorage:oak_1`, `gtceu:uhv_field_generator`

## Tips

- Source: kjs uhv\_to\_uiv\_components.js (verified). Robot arm: 4 long zalloy rods + 1 precision drive mechanism + 1 transmission assembly + 1 UHV motor + 1 UHV piston + 2 computational matrices + 2 micropower routers; solder 2304 + lubricant 2000 + naquadria 1152. Emitter: zalloy frame + UHV motor + 4 long zalloy rods + 1 catalyst core + 1 computational matrix + 64 neutronium foil + 1 router; same fluids. Sensor: same but 4 zalloy plates instead of the rods. Field generator: zalloy frame + 2 high strength panels + 1 catalyst core + 2 UHV emitters + 1 computational matrix + 64 fine RTAN wire + 2 routers; solder 4608 + naquadria 1152. Research (all of the UV items): 128 CWU/t for the arm, 144 CWU/t for emitter, sensor and field generator, 491 520 EU/t.
- Neutronium foil: 64 foil per emitter or sensor = 16 neutronium ingots (4 foils per plate/ingot), i.e. 2304 mB of neutronium, or 16 UV-reactor runs of 72 s: a sensor and an emitter cost about 5 reactor-hours with one reactor. RTAN fine wire: the pack adds the fine-wire flag to RTAN (kjs modifications.js); 64 fine wire = 8 ingots. The UHV fusion reactor and the UEV page use these.
- UHV circuit count: only the pieces already built by uhv\_parts need UHV circuits (1 per matrix) plus UV and ZPM tags; the AL recipes themselves have no circuit inputs. A robot arm needs 2 matrices = 2 UHV + 4 UV + 6 ZPM circuits through the matrix parts, a field generator 3 matrices (its own plus one per emitter).
- Where the UHV set is consumed: UHV hatches, the UHV fusion reactor (field generators), the Compact Assembly Line (robot arms), the Super Pressure Heat Chamber (field generator), the Component Nexus, the folding stabiliser, the bacteria synthesizer and every UHV machine.
- Sub-steps people skip: (1) emitters first (2 per field generator), the field generator is last; (2) check the CWU/t of the Research Station before you start a 144 CWU/t research; (3) 64 neutronium foil is a foil from a bender, not a ream; (4) one dedicated Assembly Line per product.
- **Unverified** neutronium foil bender recipe (standard GT foil), CWU totals.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 4 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 2 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:uhv_robot_arm`, `gtceu:uhv_emitter`, `gtceu:uhv_sensor`, `gtceu:uhv_field_generator`
