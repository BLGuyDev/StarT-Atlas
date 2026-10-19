---
kind: chain
id: uev_fusion
order: 2120
data:
  t: |-
    UEV fusion parts: borealic reflector panel and casing (tier 5), advanced fusion coil, fusion casing MK4 → UEV Fusion Reactor
  inf: true
  "n":
    - - g1
      - |-
        Borealic neutron reflector panel: 1 ancient netherite plate · 2 double void plate · 1 reinforced neutron reflector · 2 304 mB indium tin lead cadmium soldering alloy
      - g
      - functionalstorage:oak_1
      - - [ancient netherite plate, "gtceu:ancient_netherite_plate"]
        - [double void plate, "gtceu:double_void_plate"]
        - [reinforced neutron reflector, "kubejs:reinforced_neutron_reflector"]
    - [a1, "Assembler · sterile cleanroom · 50 s · 245 760 EU/t", m, "gtceu:uv_assembler"]
    - [p5, Borealic neutron reflector panel, x, "kubejs:borealic_neutron_reflector"]
    - - g2
      - |-
        2 borealic reflector casing: 2 reinforced reflector casing · 1 uhv field generator · 6 borealic neutron reflector · 4 cerium tritelluride single cable · 48 trinium foil · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [reinforced reflector casing, "kubejs:reinforced_reflector_casing"]
        - [uhv field generator, "gtceu:uhv_field_generator"]
        - [borealic neutron reflector, "kubejs:borealic_neutron_reflector"]
        - [cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]
        - [trinium foil, "gtceu:trinium_foil"]
    - [a2, "Assembler · sterile cleanroom · 20 s · 1 966 080 EU/t", m, "gtceu:uv_assembler"]
    - [rc, "2 Borealic reflector casing (tier 5)", x, "kubejs:borealic_reflector_casing"]
    - - g3
      - |-
        Advanced fusion coil: 1 fusion coil · 2 uv field generator · 1 uv electric pump · 4 reinforced neutron reflector · 4 UHV circuit · 1 mythrolic alloy normal fluid pipe · 4 magmada alloy plate · 576 mB cerium tritelluride
      - g
      - functionalstorage:oak_1
      - - [fusion coil, "gtceu:fusion_coil"]
        - [uv field generator, "gtceu:uv_field_generator"]
        - [uv electric pump, "gtceu:uv_electric_pump"]
        - [reinforced neutron reflector, "kubejs:reinforced_neutron_reflector"]
        - [UHV circuit, "kubejs:uhv_universal_circuit"]
        - [mythrolic alloy normal fluid pipe, "gtceu:mythrolic_alloy_normal_fluid_pipe"]
    - [a3, "Assembler · sterile cleanroom · 7.5 s · 7 864 320 EU/t", m, "gtceu:uev_assembler"]
    - [ac, Advanced Fusion Coil, x, "start_core:advanced_fusion_coil"]
    - - g4
      - |-
        2 fusion casing MK4: 1 uev machine hull · 1 advanced fusion coil · 2 uev voltage coil · 1 uhv field generator · 6 borealic neutron reflector · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [uev machine hull, "gtceu:uev_machine_hull"]
        - [advanced fusion coil, "start_core:advanced_fusion_coil"]
        - [uev voltage coil, "kubejs:uev_voltage_coil"]
        - [uhv field generator, "gtceu:uhv_field_generator"]
        - [borealic neutron reflector, "kubejs:borealic_neutron_reflector"]
    - [a4, "Assembler · cleanroom · 8 s · 30 720 EU/t", m, "gtceu:luv_assembler"]
    - [mk4, "2 Fusion Casing MK4", x, "start_core:fusion_casing_mk4"]
    - [fr, "UEV Fusion Reactor (needs 4 UIV circuits: see uiv_circuits)", o, "start_core:uev_fusion_reactor"]
  e:
    - [g1, a1, "1"]
    - [a1, p5, "1 / 50 s"]
    - [p5, g2, "6 panels"]
    - [g2, a2, "1"]
    - [a2, rc, "2 / 20 s"]
    - [p5, g4, "6 panels"]
    - [g3, a3, "1"]
    - [a3, ac, "1 / 7.5 s"]
    - [ac, g4, "1"]
    - [g4, a4, "1"]
    - [a4, mk4, "2 / 8 s"]
    - [mk4, fr, casings]
    - [rc, fr, reflector]
  tips:
    - |-
      Source: kjs systems/fusion/start_fusion_machines.js (reflectorPanel, reflectorBlock, fusionCoil, fusionCasing, reactor recipes) and fusion_scaling.js. Borealic panel (tier 5): 1 ancient netherite plate + 2 double void plates + 1 reinforced (tier 4) panel + 2304 mB indium tin lead cadmium soldering alloy, assembler 1000 ticks, VHA[UV] = 245 760 EU/t, sterile cleanroom. Borealic reflector casing: 2 reinforced reflector casings + 1 UHV field generator + 6 borealic panels + 4 cerium tritelluride single cables + 48 trinium foil + 288 mB PEDOT:PSS → 2 casings, 400 ticks, 1 966 080 EU/t, sterile cleanroom.
    - |-
      Advanced fusion coil: fusion coil + 2 UV field generators + 1 UV pump + 4 reinforced panels + 4 UHV circuits + 1 mythrolic alloy normal fluid pipe + 4 magmada alloy plates + 576 mB cerium tritelluride, 150 ticks, VA[UEV], sterile cleanroom. Fusion casing MK4 (2 per craft): UEV hull + advanced fusion coil + 2 UEV voltage coils + 1 UHV field generator + 6 borealic panels + 288 mB PEDOT:PSS, 160 ticks, VA[LuV] = 30 720 EU/t, plain cleanroom.
    - |-
      UEV Fusion Reactor (Assembly Line, 1800 ticks, VA[UEV]): advanced fusion coil + 4 UIV circuits + 1 decaying star + 1 double magmada plate + 2 UHV field generators + 160 UEPIC chips + 32 enriched pallarovium alloy single wire, 1152 mB naquadated soldering alloy + 1152 mB cerium tritelluride, station research of the UHV reactor (VHA[UEV], 160 CWU/t). So the reactor itself is a UIV-era item (the circuits); this chain only prepares the parts.
    - |-
      What tier 5 unlocks (fusion_scaling.js, reflector tier 5): aurourium (396 mB nether star concentrate + 108 mB seaborgium → 144 mB, 884 736 EU/t, 19.2 s, start 888 MEU), magmatic plasma (500 mB infernal concentrate + 288 mB iron plasma → 144 mB, 66 666 EU/t, 12.8 s, start 720 MEU; needed for magmada alloy), oganesson plasma (see uev_chiller) and borealic concentrate (135 mB stellarium + 9 mB aurourium, 1 023 948 EU/t, 3.6 s, start 1200 MEU). A recipe needs a reflector tier at least its own; a higher tier raises the reactor overclock cap by the difference in tiers (each overclock step doubles EU/t and halves the time), and all reflectors of a reactor must be the same tier (verified in start_core).
    - |-
      Sub-steps people skip: (1) check the reactor card for how many reflector casings it takes before you craft a stack; (2) trinium foil (48 per craft) is a lot of foil; (3) the sterile cleanroom is needed for the panel, casing and coil; (4) the UHV and UV field generators come from the UHV and UV pages.
    - |-
      Unverified: which fusion reactor (UHV, UEV) accepts tier 5 reflector casings and holds 720 to 1200 MEU of start energy; the reflector slot count.
  b:
    - ["gtceu:uv_assembler", 1]
    - ["gtceu:uev_assembler", 1]
    - ["gtceu:luv_assembler", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:ancient_netherite_plate
        - gtceu:double_void_plate
        - kubejs:reinforced_neutron_reflector
      t: |-
        Drawers first: ancient netherite plates, double void plates, tier 4 panels, UHV field generators, cerium tritelluride cables, trinium foil. Drum: soldering alloy 2304 mB per panel batch, PEDOT:PSS, cerium tritelluride. One dedicated assembler per product in the sterile cleanroom.
    - i: ["gtceu:uv_assembler", "kubejs:borealic_neutron_reflector"]
      t: |-
        Panels first (50 s each at 245 760 EU/t): 6 per casing craft, 6 per fusion casing MK4 and 4 more reinforced panels per coil. Output drawer Keep Exact 32.
    - i: ["gtceu:uv_assembler", "kubejs:borealic_reflector_casing"]
      t: |-
        Reflector casings: 20 s each craft (2 casings). Keep Exact 16.
    - i: ["gtceu:uev_assembler", "start_core:advanced_fusion_coil"]
      t: |-
        Advanced fusion coil: needs the mythrolic pipe and magmada plates from uev_alloys. 7.5 s.
    - i: ["gtceu:luv_assembler", "start_core:fusion_casing_mk4"]
      t: |-
        Fusion casing MK4: 8 s per 2 casings; needs the UEV hull and 2 UEV voltage coils per craft.
    - i: ["functionalstorage:oak_1", "start_core:uev_fusion_reactor"]
      t: Hold the casings and coil for the reactor controller (uiv_multis) and keep the 4 UIV circuits free.
---
# UEV fusion parts: borealic reflector panel and casing (tier 5), advanced fusion coil, fusion casing MK4 → UEV Fusion Reactor

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_fusion` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV fusion and plasma power](../../plan/p18.md#uevfusion)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-uv" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 50 s · 245 760 EU/t</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Borealic neutron reflector panel: 1 ancient netherite plate · 2 double void plate · 1 reinforced neutron reflector · 2 304 mB indium tin lead cadmium soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Borealic neutron reflector panel: 1 ancient netherite plate · 2 double void plate · 1 reinforced neutron reflector · 2 304 mB indium tin lead cadmium soldering alloy</span><span class="gt-sub"><span>ancient netherite plate</span><span>double void plate</span><span>reinforced neutron reflector</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Borealic neutron reflector panel (kubejs:borealic_neutron_reflector) - 1 / 50 s"><img class="gt-ico" src="../../assets/icons/kubejs__borealic_neutron_reflector.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borealic Neutron Reflector</span><span class="gt-note">Borealic neutron reflector panel</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_assembler</code></div>
</div>
<div class="gt-panel t-uv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 20 s · 1 966 080 EU/t</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 borealic reflector casing: 2 reinforced reflector casing · 1 uhv field generator · 6 borealic neutron reflector · 4 cerium tritelluride single cable · 48 trinium foil · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 borealic reflector casing: 2 reinforced reflector casing · 1 uhv field generator · 6 borealic neutron reflector · 4 cerium tritelluride single cable · 48 trinium foil · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>reinforced reflector casing</span><span>uhv field generator</span><span>borealic neutron reflector</span><span>cerium tritelluride single cable</span><span>trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Borealic reflector casing (tier 5) (kubejs:borealic_reflector_casing) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__borealic_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borealic Reflector Casing</span><span class="gt-note">2 Borealic reflector casing (tier 5)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_assembler</code></div>
</div>
<div class="gt-panel t-uev" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 7.5 s · 7 864 320 EU/t</span><span class="gt-badge t-uev">UEV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Advanced fusion coil: 1 fusion coil · 2 uv field generator · 1 uv electric pump · 4 reinforced neutron reflector · 4 UHV circuit · 1 mythrolic alloy normal fluid pipe · 4 magmada alloy plate · 576 mB cerium tritelluride (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Advanced fusion coil: 1 fusion coil · 2 uv field generator · 1 uv electric pump · 4 reinforced neutron reflector · 4 UHV circuit · 1 mythrolic alloy normal fluid pipe · 4 magmada alloy plate · 576 mB cerium tritelluride</span><span class="gt-sub"><span>fusion coil</span><span>uv field generator</span><span>uv electric pump</span><span>reinforced neutron reflector</span><span>UHV circuit</span><span>mythrolic alloy normal fluid pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 388 608 EU/t</span><span class="gt-stat">7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Advanced Fusion Coil (start_core:advanced_fusion_coil) - 1 / 7.5 s"><img class="gt-ico" src="../../assets/icons/start_core__advanced_fusion_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Fusion Coil</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uev_assembler</code></div>
</div>
<div class="gt-panel t-luv" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembler · cleanroom · 8 s · 30 720 EU/t</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 fusion casing MK4: 1 uev machine hull · 1 advanced fusion coil · 2 uev voltage coil · 1 uhv field generator · 6 borealic neutron reflector · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 fusion casing MK4: 1 uev machine hull · 1 advanced fusion coil · 2 uev voltage coil · 1 uhv field generator · 6 borealic neutron reflector · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>uev machine hull</span><span>advanced fusion coil</span><span>uev voltage coil</span><span>uhv field generator</span><span>borealic neutron reflector</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Fusion Casing MK4 (start_core:fusion_casing_mk4) - 2 / 8 s"><img class="gt-ico" src="../../assets/icons/start_core__fusion_casing_mk4.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fusion Casing Mk4</span><span class="gt-note">2 Fusion Casing MK4</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · sterile cleanroom · 50 s · 245 760 EU/t](#m-a1) → [Assembler · sterile cleanroom · 20 s · 1 966 080 EU/t](#m-a2) (also Assembler · sterile cleanroom · 50 s · 245 760 EU/t → [Assembler · cleanroom · 8 s · 30 720 EU/t](#m-a4))
- [Assembler · sterile cleanroom · 7.5 s · 7 864 320 EU/t](#m-a3) → [Assembler · cleanroom · 8 s · 30 720 EU/t](#m-a4)

### Direct steps

- Borealic neutron reflector panel → 2 borealic reflector casing: 2 reinforced reflector casing · 1 uhv field generator · 6 borealic neutron reflector · 4 cerium tritelluride single cable · 48 trinium foil · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (6 panels)
- Borealic neutron reflector panel → 2 fusion casing MK4: 1 uev machine hull · 1 advanced fusion coil · 2 uev voltage coil · 1 uhv field generator · 6 borealic neutron reflector · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (6 panels)
- Advanced Fusion Coil → 2 fusion casing MK4: 1 uev machine hull · 1 advanced fusion coil · 2 uev voltage coil · 1 uhv field generator · 6 borealic neutron reflector · 288 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (1)
- 2 Fusion Casing MK4 → UEV Fusion Reactor (needs 4 UIV circuits: see uiv\_circuits) (casings)
- 2 Borealic reflector casing (tier 5) → UEV Fusion Reactor (needs 4 UIV circuits: see uiv\_circuits) (reflector)

## How to build

1. Drawers first: ancient netherite plates, double void plates, tier 4 panels, UHV field generators, cerium tritelluride cables, trinium foil. Drum: soldering alloy 2304 mB per panel batch, PEDOT:PSS, cerium tritelluride. One dedicated assembler per product in the sterile cleanroom. — `functionalstorage:oak_1`, `gtceu:ancient_netherite_plate`, `gtceu:double_void_plate`, `kubejs:reinforced_neutron_reflector`
2. Panels first (50 s each at 245 760 EU/t): 6 per casing craft, 6 per fusion casing MK4 and 4 more reinforced panels per coil. Output drawer Keep Exact 32. — `gtceu:uv_assembler`, `kubejs:borealic_neutron_reflector`
3. Reflector casings: 20 s each craft (2 casings). Keep Exact 16. — `gtceu:uv_assembler`, `kubejs:borealic_reflector_casing`
4. Advanced fusion coil: needs the mythrolic pipe and magmada plates from uev\_alloys. 7.5 s. — `gtceu:uev_assembler`, `start_core:advanced_fusion_coil`
5. Fusion casing MK4: 8 s per 2 casings; needs the UEV hull and 2 UEV voltage coils per craft. — `gtceu:luv_assembler`, `start_core:fusion_casing_mk4`
6. Hold the casings and coil for the reactor controller (uiv\_multis) and keep the 4 UIV circuits free. — `functionalstorage:oak_1`, `start_core:uev_fusion_reactor`

## Tips

- Source: kjs systems/fusion/start\_fusion\_machines.js (reflectorPanel, reflectorBlock, fusionCoil, fusionCasing, reactor recipes) and fusion\_scaling.js. Borealic panel (tier 5): 1 ancient netherite plate + 2 double void plates + 1 reinforced (tier 4) panel + 2304 mB indium tin lead cadmium soldering alloy, assembler 1000 ticks, VHA\[UV\] = 245 760 EU/t, sterile cleanroom. Borealic reflector casing: 2 reinforced reflector casings + 1 UHV field generator + 6 borealic panels + 4 cerium tritelluride single cables + 48 trinium foil + 288 mB PEDOT:PSS → 2 casings, 400 ticks, 1 966 080 EU/t, sterile cleanroom.
- Advanced fusion coil: fusion coil + 2 UV field generators + 1 UV pump + 4 reinforced panels + 4 UHV circuits + 1 mythrolic alloy normal fluid pipe + 4 magmada alloy plates + 576 mB cerium tritelluride, 150 ticks, VA\[UEV\], sterile cleanroom. Fusion casing MK4 (2 per craft): UEV hull + advanced fusion coil + 2 UEV voltage coils + 1 UHV field generator + 6 borealic panels + 288 mB PEDOT:PSS, 160 ticks, VA\[LuV\] = 30 720 EU/t, plain cleanroom.
- UEV Fusion Reactor (Assembly Line, 1800 ticks, VA\[UEV\]): advanced fusion coil + 4 UIV circuits + 1 decaying star + 1 double magmada plate + 2 UHV field generators + 160 UEPIC chips + 32 enriched pallarovium alloy single wire, 1152 mB naquadated soldering alloy + 1152 mB cerium tritelluride, station research of the UHV reactor (VHA\[UEV\], 160 CWU/t). So the reactor itself is a UIV-era item (the circuits); this chain only prepares the parts.
- What tier 5 unlocks (fusion\_scaling.js, reflector tier 5): aurourium (396 mB nether star concentrate + 108 mB seaborgium → 144 mB, 884 736 EU/t, 19.2 s, start 888 MEU), magmatic plasma (500 mB infernal concentrate + 288 mB iron plasma → 144 mB, 66 666 EU/t, 12.8 s, start 720 MEU; needed for magmada alloy), oganesson plasma (see uev\_chiller) and borealic concentrate (135 mB stellarium + 9 mB aurourium, 1 023 948 EU/t, 3.6 s, start 1200 MEU). A recipe needs a reflector tier at least its own; a higher tier raises the reactor overclock cap by the difference in tiers (each overclock step doubles EU/t and halves the time), and all reflectors of a reactor must be the same tier (verified in start\_core).
- Sub-steps people skip: (1) check the reactor card for how many reflector casings it takes before you craft a stack; (2) trinium foil (48 per craft) is a lot of foil; (3) the sterile cleanroom is needed for the panel, casing and coil; (4) the UHV and UV field generators come from the UHV and UV pages.
- **Unverified** which fusion reactor (UHV, UEV) accepts tier 5 reflector casings and holds 720 to 1200 MEU of start energy; the reflector slot count.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:uv_assembler` | 1 |
| `gtceu:uev_assembler` | 1 |
| `gtceu:luv_assembler` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `kubejs:borealic_neutron_reflector`, `kubejs:borealic_reflector_casing`, `start_core:advanced_fusion_coil`, `start_core:fusion_casing_mk4`, `start_core:uev_fusion_reactor`
