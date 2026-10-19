---
kind: chain
id: uv_fusion
order: 1700
data:
  t: |-
    UV Fusion Reactor: complex reflector panel → complex reflector casing → fusion casing MK3 → reactor (4 UHV circuits, 128 UHPIC chips, research 96 CWU/t)
  inf: true
  "n":
    - - g1
      - |-
        1 trinaquadalloy plate · 2 double zirconium plate · 1 advanced neutron reflector · 2304 mB solder
      - g
      - functionalstorage:oak_1
      - - [Trinaquadalloy plate, "gtceu:trinaquadalloy_plate"]
        - [Double zirconium plate, "gtceu:double_zirconium_plate"]
        - [Advanced neutron reflector, "kubejs:advanced_neutron_reflector"]
    - [a1, "Cleanroom Assembler · 50 s · 15 360 EU/t", m, "gtceu:large_assembler"]
    - [cp, Complex Neutron Reflector panel, x, "kubejs:complex_neutron_reflector"]
    - - g2
      - |-
        2 advanced reflector casing · ZPM field generator · 6 complex panel · 4 YBCO cable · 24 trinium foil · 288 mB PEEK
      - g
      - functionalstorage:oak_1
      - - [Advanced reflector casing, "kubejs:advanced_reflector_casing"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [Trinium foil, "gtceu:trinium_foil"]
    - [a2, "Cleanroom Assembler · 20 s · 122 880 EU/t", m, "gtceu:large_assembler"]
    - [rc, "2 Complex Reflector Casing (tier 3)", x, "kubejs:complex_reflector_casing"]
    - - g3
      - UV hull · fusion coil · 2 UV voltage coil · ZPM field generator · 6 complex panel · 288 mB PEEK
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [Fusion coil, "gtceu:fusion_coil"]
        - [UV voltage coil, "gtceu:uv_voltage_coil"]
    - [a3, "Cleanroom Assembler · 8 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [mk, "2 Fusion Casing MK3", x, "gtceu:fusion_casing_mk3"]
    - - g4
      - fusion coil · 4 UHV circuit · quantum star · double americium plate · 2 ZPM field generator · 128 UHPIC chip · 32 ENTED single wire · 1152 mB ITLC solder + 1152 mB YBCO
      - g
      - functionalstorage:oak_1
      - - ["Wetware mainframe (UHV)", "gtceu:wetware_processor_mainframe"]
        - [Quantum star, "gtceu:quantum_star"]
        - [Double americium plate, "gtceu:double_americium_plate"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [ENTED single wire, "gtceu:enriched_naquadah_trinium_europium_duranide_single_wire"]
    - - rs
      - Research Station · 96 CWU/t · 245 760 EU/t · ZPM fusion reactor in the Object Holder
      - m
      - gtceu:research_station
    - [al, "Assembly Line · 75 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [fr, "UV Fusion Reactor (MK III)", o, "start_core:uv_fusion_reactor"]
  e:
    - [g1, a1, "1"]
    - [a1, cp, "1 / 50 s"]
    - [cp, g2, "6"]
    - [cp, g3, "6"]
    - [g2, a2, "1"]
    - [a2, rc, "2 / 20 s"]
    - [g3, a3, "1"]
    - [a3, mk, "2 / 8 s"]
    - [g4, al, "1"]
    - [rs, al, data orb]
    - [al, fr, "1 / 75 s"]
  tips:
    - |-
      Reactor (kjs systems/fusion/start_fusion_machines.js, uv_fusion_reactor; GT mk3 recipe removed): 1 fusion coil + 4 circuits of the UHV tag + 1 quantum star + 1 double americium plate + 2 ZPM field generators + 128 UHPIC chips (64 + 64) + 32 ENTED single wire; 1152 mB ITLC soldering alloy + 1152 mB molten YBCO; Assembly Line 1500 ticks (75 s) at VA[UV] = 491 520 EU/t; STATION research of the ZPM fusion reactor at 96 CWU/t and VHA[UV] = 245 760 EU/t. THE FOUR UHV CIRCUITS ARE WETWARE MAINFRAMES (uv_wetware3), not UV circuits: the UV fusion reactor is gated on the UHV circuit.
    - |-
      Fusion coil: the same cleanroom assembler recipe as for the ZPM reactor (zpm_fusion: 1 superconducting coil + 2 IV field generators + IV pump + 4 basic panels + 4 LuV circuits + naquadah pipe + 4 europium plates + 576 mB VG). 128 UHPIC chips = 64 wafers (luv_fusion chip line); the ENTED single wire is 4 ingots of the UV superconductor (uv_alloys). The reactor consumes the quantum star (uv_gravi shows the bath).
    - |-
      Complex reflector panel (reflectorPanel tier 3): 1 trinaquadalloy plate + 2 double zirconium plates + 1 advanced neutron reflector panel + 2304 mB soldering alloy, cleanroom assembler, 1000 ticks at VHA[LuV]. Complex reflector casing (reflectorBlock tier 3): 2 advanced reflector casings + 1 ZPM field generator + 6 complex panels + 4 YBCO single cables + 24 trinium foil + 288 mB PEEK → 2 casings, cleanroom, 400 ticks at VA[EV] x 4^3 = 122 880 EU/t. Fusion casing MK3: UV hull + fusion coil + 2 UV voltage coils + 1 ZPM field generator + 6 complex panels + 288 mB PEEK → 2 casings, cleanroom, 160 ticks at VA[LuV] = 30 720 EU/t. Reinforced fusion glass (kubejs): fusion glass + ZPM emitter + 6 complex panels + 432 mB PEEK → 2 glass at VA[UV].
    - |-
      What it unlocks (fusion_scaling.js): neutronium (600 MEU start) and the 480 MEU nickel plasma of uv_power. Americium, tritanium and duranium (200 MEU or less) already run on the MK II with tier-3 reflectors (uv_fusion_mats). Verified buffers (start_core reactor descriptions): MK I 160 MEU, MK II 320 MEU, MK III 640 MEU, so the 600 MEU neutronium run only fits this MK III. The casing and coil counts of the structure are not in the extracted multis: read the controller’s structure preview (Unverified).
    - |-
      Sub-steps people skip: (1) the research item is the ZPM fusion reactor: do not recycle it; (2) tier 3 reflectors need the tier 2 casings as ingredients, so keep the advanced casing line running; (3) 6 complex panels per casing and per MK3 casing: 12 panels per pair, each panel eats an advanced panel; (4) 24 trinium foil per complex casing craft; (5) YBCO fluid 1152 mB: a YBCO ingot line; (6) PEEK for every casing (uv_peek).
    - |-
      Unverified: casing counts and 128 UHPIC chip throughput. Verified: buffer 640 MEU, FRC III research 96 CWU/t, Assembly Line VA[UV].
  b:
    - ["start_core:uv_fusion_reactor", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:large_assembler", 3]
    - ["gtceu:power_substation", 2]
    - ["kubejs:complex_reflector_casing", 16]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 5]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:advanced_neutron_reflector
        - gtceu:trinaquadalloy_plate
        - gtceu:double_zirconium_plate
      t: |-
        Drawers first, one per input: advanced panels, trinaquadalloy plates, double zirconium plates, advanced casings (2), ZPM field generators (1 + 1 + 2), trinium foil (24), YBCO cables (4), UV hulls, voltage coils, fusion coils, quantum stars, double americium plates, UHPIC chips, ENTED single wire. Drums: soldering alloy, ITLC solder, PEEK, YBCO.
    - i: ["gtceu:large_assembler", "kubejs:complex_neutron_reflector"]
      t: |-
        Panels: cleanroom assembler, 50 s at 15 360 EU/t, one per craft; 12 panels per pair of casings and pair of MK3 casings, so a second assembler is worth it. Output drawer Keep Exact 12.
    - i: ["gtceu:large_assembler", "kubejs:complex_reflector_casing"]
      t: |-
        Complex casings: cleanroom assembler at 122 880 EU/t (20 s): 2 advanced casings + ZPM field generator + 6 panels + 4 cables + 24 trinium foil + 288 mB PEEK → 2. 16 casings for the reflector shell of uv_fusion_mats.
    - i: ["gtceu:large_assembler", "gtceu:fusion_casing_mk3"]
      t: |-
        Fusion casing MK3: 8 s at 30 720 EU/t, UV hull + coil + 2 voltage coils + field generator + 6 panels + PEEK → 2. Make the number your structure preview asks for.
    - i: ["gtceu:research_station", "start_core:zpm_fusion_reactor", "gtceu:data_orb"]
      t: |-
        Research: a ZPM fusion reactor in the Object Holder, 96 CWU/t at 245 760 EU/t, orb into the Assembly Line.
    - i: ["gtceu:assembly_line", "start_core:uv_fusion_reactor"]
      t: |-
        Reactor: Assembly Line buses in recipe order (coil, 4 mainframes, star, plate, 2 field generators, chips, wire); fluids by hatches; 75 s at 491 520 EU/t. Needs the ZPM 4A hatch or a UV hatch.
---
# UV Fusion Reactor: complex reflector panel → complex reflector casing → fusion casing MK3 → reactor (4 UHV circuits, 128 UHPIC chips, research 96 CWU/t)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_fusion` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV Fusion Reactor and fusion metals](../../plan/p15.md#uvfusion)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 50 s · 15 360 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 trinaquadalloy plate · 2 double zirconium plate · 1 advanced neutron reflector · 2304 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 trinaquadalloy plate · 2 double zirconium plate · 1 advanced neutron reflector · 2304 mB solder</span><span class="gt-sub"><span>Trinaquadalloy plate</span><span>Double zirconium plate</span><span>Advanced neutron reflector</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Complex Neutron Reflector panel (kubejs:complex_neutron_reflector) - 1 / 50 s"><img class="gt-ico" src="../../assets/icons/kubejs__complex_neutron_reflector.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Complex Neutron Reflector</span><span class="gt-note">Complex Neutron Reflector panel</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 20 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 advanced reflector casing · ZPM field generator · 6 complex panel · 4 YBCO cable · 24 trinium foil · 288 mB PEEK (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 advanced reflector casing · ZPM field generator · 6 complex panel · 4 YBCO cable · 24 trinium foil · 288 mB PEEK</span><span class="gt-sub"><span>Advanced reflector casing</span><span>ZPM field generator</span><span>Trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Complex Reflector Casing (tier 3) (kubejs:complex_reflector_casing) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__complex_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Complex Reflector Casing</span><span class="gt-note">2 Complex Reflector Casing (tier 3)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 8 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · fusion coil · 2 UV voltage coil · ZPM field generator · 6 complex panel · 288 mB PEEK (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · fusion coil · 2 UV voltage coil · ZPM field generator · 6 complex panel · 288 mB PEEK</span><span class="gt-sub"><span>UV Machine Hull</span><span>Fusion coil</span><span>UV voltage coil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Fusion Casing MK3 (gtceu:fusion_casing_mk3) - 2 / 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__fusion_casing_mk3.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fusion Casing Mk3</span><span class="gt-note">2 Fusion Casing MK3</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 96 CWU/t · 245 760 EU/t · ZPM fusion reactor in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 75 s · 491 520 EU/t (gtceu:assembly_line) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 75 s · 491 520 EU/t</span><b class="gt-q">data orb</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 75 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="fusion coil · 4 UHV circuit · quantum star · double americium plate · 2 ZPM field generator · 128 UHPIC chip · 32 ENTED single wire · 1152 mB ITLC solder + 1152 mB YBCO (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">fusion coil · 4 UHV circuit · quantum star · double americium plate · 2 ZPM field generator · 128 UHPIC chip · 32 ENTED single wire · 1152 mB ITLC solder + 1152 mB YBCO</span><span class="gt-sub"><span>Wetware mainframe (UHV)</span><span>Quantum star</span><span>Double americium plate</span><span>UHPIC chip</span><span>ENTED single wire</span></span><b class="gt-q">1</b></span><a class="gt-slot gt-mach" href="#m-rs" title="Research Station · 96 CWU/t · 245 760 EU/t · ZPM fusion reactor in the Object Holder (gtceu:research_station) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station · 96 CWU/t · 245 760 EU/t · ZPM fusion reactor in the Object Holder</span><b class="gt-q">data orb</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Fusion Reactor (MK III) (start_core:uv_fusion_reactor) - 1 / 75 s"><img class="gt-ico" src="../../assets/icons/start_core__uv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Fusion Reactor</span><span class="gt-note">UV Fusion Reactor (MK III)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Cleanroom Assembler · 50 s · 15 360 EU/t](#m-a1) → [Cleanroom Assembler · 20 s · 122 880 EU/t](#m-a2) (also Cleanroom Assembler · 50 s · 15 360 EU/t → [Cleanroom Assembler · 8 s · 30 720 EU/t](#m-a3))
- [Research Station · 96 CWU/t · 245 760 EU/t · ZPM fusion reactor in the Object Holder](#m-rs) → [Assembly Line · 75 s · 491 520 EU/t](#m-al)
- [Cleanroom Assembler · 8 s · 30 720 EU/t](#m-a3)

### Direct steps

- Complex Neutron Reflector panel → 2 advanced reflector casing · ZPM field generator · 6 complex panel · 4 YBCO cable · 24 trinium foil · 288 mB PEEK (6)
- Complex Neutron Reflector panel → UV hull · fusion coil · 2 UV voltage coil · ZPM field generator · 6 complex panel · 288 mB PEEK (6)

## How to build

1. Drawers first, one per input: advanced panels, trinaquadalloy plates, double zirconium plates, advanced casings (2), ZPM field generators (1 + 1 + 2), trinium foil (24), YBCO cables (4), UV hulls, voltage coils, fusion coils, quantum stars, double americium plates, UHPIC chips, ENTED single wire. Drums: soldering alloy, ITLC solder, PEEK, YBCO. — `functionalstorage:oak_1`, `kubejs:advanced_neutron_reflector`, `gtceu:trinaquadalloy_plate`, `gtceu:double_zirconium_plate`
2. Panels: cleanroom assembler, 50 s at 15 360 EU/t, one per craft; 12 panels per pair of casings and pair of MK3 casings, so a second assembler is worth it. Output drawer Keep Exact 12. — `gtceu:large_assembler`, `kubejs:complex_neutron_reflector`
3. Complex casings: cleanroom assembler at 122 880 EU/t (20 s): 2 advanced casings + ZPM field generator + 6 panels + 4 cables + 24 trinium foil + 288 mB PEEK → 2. 16 casings for the reflector shell of uv\_fusion\_mats. — `gtceu:large_assembler`, `kubejs:complex_reflector_casing`
4. Fusion casing MK3: 8 s at 30 720 EU/t, UV hull + coil + 2 voltage coils + field generator + 6 panels + PEEK → 2. Make the number your structure preview asks for. — `gtceu:large_assembler`, `gtceu:fusion_casing_mk3`
5. Research: a ZPM fusion reactor in the Object Holder, 96 CWU/t at 245 760 EU/t, orb into the Assembly Line. — `gtceu:research_station`, `start_core:zpm_fusion_reactor`, `gtceu:data_orb`
6. Reactor: Assembly Line buses in recipe order (coil, 4 mainframes, star, plate, 2 field generators, chips, wire); fluids by hatches; 75 s at 491 520 EU/t. Needs the ZPM 4A hatch or a UV hatch. — `gtceu:assembly_line`, `start_core:uv_fusion_reactor`

## Tips

- Reactor (kjs systems/fusion/start\_fusion\_machines.js, uv\_fusion\_reactor; GT mk3 recipe removed): 1 fusion coil + 4 circuits of the UHV tag + 1 quantum star + 1 double americium plate + 2 ZPM field generators + 128 UHPIC chips (64 + 64) + 32 ENTED single wire; 1152 mB ITLC soldering alloy + 1152 mB molten YBCO; Assembly Line 1500 ticks (75 s) at VA\[UV\] = 491 520 EU/t; STATION research of the ZPM fusion reactor at 96 CWU/t and VHA\[UV\] = 245 760 EU/t. THE FOUR UHV CIRCUITS ARE WETWARE MAINFRAMES (uv\_wetware3), not UV circuits: the UV fusion reactor is gated on the UHV circuit.
- Fusion coil: the same cleanroom assembler recipe as for the ZPM reactor (zpm\_fusion: 1 superconducting coil + 2 IV field generators + IV pump + 4 basic panels + 4 LuV circuits + naquadah pipe + 4 europium plates + 576 mB VG). 128 UHPIC chips = 64 wafers (luv\_fusion chip line); the ENTED single wire is 4 ingots of the UV superconductor (uv\_alloys). The reactor consumes the quantum star (uv\_gravi shows the bath).
- Complex reflector panel (reflectorPanel tier 3): 1 trinaquadalloy plate + 2 double zirconium plates + 1 advanced neutron reflector panel + 2304 mB soldering alloy, cleanroom assembler, 1000 ticks at VHA\[LuV\]. Complex reflector casing (reflectorBlock tier 3): 2 advanced reflector casings + 1 ZPM field generator + 6 complex panels + 4 YBCO single cables + 24 trinium foil + 288 mB PEEK → 2 casings, cleanroom, 400 ticks at VA\[EV\] x 4^3 = 122 880 EU/t. Fusion casing MK3: UV hull + fusion coil + 2 UV voltage coils + 1 ZPM field generator + 6 complex panels + 288 mB PEEK → 2 casings, cleanroom, 160 ticks at VA\[LuV\] = 30 720 EU/t. Reinforced fusion glass (kubejs): fusion glass + ZPM emitter + 6 complex panels + 432 mB PEEK → 2 glass at VA\[UV\].
- What it unlocks (fusion\_scaling.js): neutronium (600 MEU start) and the 480 MEU nickel plasma of uv\_power. Americium, tritanium and duranium (200 MEU or less) already run on the MK II with tier-3 reflectors (uv\_fusion\_mats). Verified buffers (start\_core reactor descriptions): MK I 160 MEU, MK II 320 MEU, MK III 640 MEU, so the 600 MEU neutronium run only fits this MK III. The casing and coil counts of the structure are not in the extracted multis: read the controller’s structure preview (Unverified).
- Sub-steps people skip: (1) the research item is the ZPM fusion reactor: do not recycle it; (2) tier 3 reflectors need the tier 2 casings as ingredients, so keep the advanced casing line running; (3) 6 complex panels per casing and per MK3 casing: 12 panels per pair, each panel eats an advanced panel; (4) 24 trinium foil per complex casing craft; (5) YBCO fluid 1152 mB: a YBCO ingot line; (6) PEEK for every casing (uv\_peek).
- **Unverified** casing counts and 128 UHPIC chip throughput. Verified: buffer 640 MEU, FRC III research 96 CWU/t, Assembly Line VA\[UV\].

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:uv_fusion_reactor` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:large_assembler` | 3 |
| `gtceu:power_substation` | 2 |
| `kubejs:complex_reflector_casing` | 16 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `start_core:uv_fusion_reactor`, `gtceu:fusion_casing_mk3`, `kubejs:complex_neutron_reflector`, `kubejs:reinforced_fusion_glass`
