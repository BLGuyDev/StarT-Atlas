---
kind: chain
id: uiv_fusion
order: 2200
data:
  t: |-
    UIV fusion parts: draconic reflector panel and casing (tier 6), auxiliary fusion coil MK2, boosted fusion casing MK2 → UEV and UIV Fusion Reactors
  inf: true
  "n":
    - - g1
      - |-
        Draconic neutron reflector panel: 1 rhenate w plate · 2 double mythrotight carbide steel plate · 1 borealic neutron reflector · 1 152 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [rhenate w plate, "gtceu:rhenate_w_plate"]
        - [double mythrotight carbide steel plate, "gtceu:double_mythrotight_carbide_steel_plate"]
        - [borealic neutron reflector, "kubejs:borealic_neutron_reflector"]
    - [a1, "Assembler · sterile cleanroom · 50 s · 983 040 EU/t", m, "gtceu:uhv_assembler"]
    - [p6, Draconic neutron reflector panel, x, "kubejs:draconic_neutron_reflector"]
    - - g2
      - |-
        2 draconic reflector casing: 2 borealic reflector casing · 1 uev field generator · 6 draconic neutron reflector · 4 polonium bismide single cable · 64 trinium foil · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [borealic reflector casing, "kubejs:borealic_reflector_casing"]
        - [uev field generator, "gtceu:uev_field_generator"]
        - [draconic neutron reflector, "kubejs:draconic_neutron_reflector"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
        - [trinium foil, "gtceu:trinium_foil"]
    - [a2, "Assembler · sterile cleanroom · 20 s · 7 864 320 EU/t", m, "gtceu:uev_assembler"]
    - [rc, "2 Draconic reflector casing (tier 6)", x, "kubejs:draconic_reflector_casing"]
    - - g3
      - |-
        3 auxiliary fusion coil MK2: 3 auxiliary fusion coil mk1 · 4 uhv field generator · 2 uhv electric pump · 8 borealic neutron reflector · 8 UEV circuit · 2 nyanium normal fluid pipe · 8 abyssal alloy plate · 1 152 mB polonium bismide
      - g
      - functionalstorage:oak_1
      - - [auxiliary fusion coil mk1, "start_core:auxiliary_fusion_coil_mk1"]
        - [uhv field generator, "gtceu:uhv_field_generator"]
        - [uhv electric pump, "gtceu:uhv_electric_pump"]
        - [borealic neutron reflector, "kubejs:borealic_neutron_reflector"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [nyanium normal fluid pipe, "gtceu:nyanium_normal_fluid_pipe"]
    - [a3, "Assembler · sterile cleanroom · 15 s · 31 457 280 EU/t", m, "gtceu:uiv_assembler"]
    - [ac, Auxiliary Fusion Coil MK2, x, "start_core:auxiliary_fusion_coil_mk2"]
    - - g4
      - |-
        2 boosted fusion casing MK2: 1 uiv machine hull · 1 auxiliary fusion coil mk2 · 2 uiv voltage coil · 1 uev field generator · 6 draconic neutron reflector · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [auxiliary fusion coil mk2, "start_core:auxiliary_fusion_coil_mk2"]
        - [uiv voltage coil, "kubejs:uiv_voltage_coil"]
        - [uev field generator, "gtceu:uev_field_generator"]
        - [draconic neutron reflector, "kubejs:draconic_neutron_reflector"]
    - [a4, "Assembler · cleanroom · 8 s · 30 720 EU/t", m, "gtceu:luv_assembler"]
    - [mk2, "2 Auxiliary Boosted Fusion Casing MK2", x, "start_core:auxiliary_boosted_fusion_casing_mk2"]
    - - fr
      - UIV Fusion Reactor (Assembly Line 97.5 s · 4 UXV circuits, draconic eye, 96 UIPIC)
      - o
      - start_core:uiv_fusion_reactor
  e:
    - [g1, a1, "1"]
    - [a1, p6, "1 / 50 s"]
    - [p6, g2, "6"]
    - [g2, a2, "1"]
    - [a2, rc, "2 / 20 s"]
    - [p6, g4, "6"]
    - [g3, a3, "1"]
    - [a3, ac, "3 / 15 s"]
    - [ac, g4, "1"]
    - [g4, a4, "1"]
    - [a4, mk2, "2 / 8 s"]
    - [mk2, fr, casings]
    - [rc, fr, reflector]
  tips:
    - |-
      Source: kjs systems/fusion/start_fusion_machines.js. Draconic panel (tier 6): 1 rhenate w plate + 2 double mythrotight carbide steel plates + 1 borealic panel + 1152 mB naquadated soldering alloy, 1000 ticks, VHA[UHV] = 983 040 EU/t, sterile cleanroom. Draconic reflector casing: 2 borealic reflector casings + 1 UEV field generator + 6 draconic panels + 4 polonium bismide single cables + 64 trinium foil + 576 mB PEDOT:PSS → 2 casings, 400 ticks, VA[EV] x 4^6 = 7 864 320 EU/t, sterile cleanroom. Prismalic (tier 7) casings need the Abyssal Containment Room and are the next era.
    - |-
      Auxiliary fusion coil MK2 (3 per craft): 3 auxiliary coils MK1 + 4 UHV field generators + 2 UHV pumps + 8 borealic panels + 8 UEV circuits + 2 nyanium normal fluid pipes + 8 abyssal alloy plates + 1152 mB polonium bismide, 300 ticks, VA[UIV] = 31 457 280 EU/t, sterile cleanroom. Boosted casing MK2 (2 per craft): UIV hull + coil MK2 + 2 UIV voltage coils + 1 UEV field generator + 6 draconic panels + 576 mB PEDOT:PSS, 160 ticks, VA[LuV], plain cleanroom.
    - |-
      UIV Fusion Reactor (Assembly Line, 1950 ticks, VA[UIV], station research of the UEV reactor VHA[UIV] / 192 CWU/t): auxiliary coil MK2 + 4 UXV circuits (abyssal processor mainframes) + draconic eye + double abyssal alloy plate + 2 UEV field generators + 96 UIPIC chips (64 + 32) + 32 rhenium super composite alloy single wire, 1152 mB naquadated soldering alloy + 1152 mB polonium bismide. So the reactor is a UXV-circuit item: not buildable inside this era; what this era delivers is the UEV reactor (uev_fusion; its 4 UIV circuits come from uiv_circuits) and the tier 6 reflector parts.
    - |-
      Plasma with tier 6 reflectors: paradox, voidic and preon plasma (uiv_alloys). The UEV reactor with tier 5 reflectors only covers magmatic, oganesson and aurourium fusion; the tier 6 recipes above start at 900 to 1160 MEU: Unverified which reactor holds that start energy (the quest text says a higher reflector than required doubles speed and power).
    - |-
      Sub-steps people skip: (1) rhenate w (33 ingots, tin plasma) and mythrotight carbide steel (19 ingots, iron plasma, ascendant catalyst, heat 966) are both Hell Forge alloys at VA[UIV] (hellforge.js); (2) 64 trinium foil per craft; (3) the borealic panels are used in the coil MK2 too (8 per craft); (4) sterile cleanroom for panel, reflector casing and coil.
    - |-
      Unverified: reflector slots per reactor, the mythrotight carbide steel and rhenate w production, the UXV circuit timing.
  b:
    - ["gtceu:uhv_assembler", 1]
    - ["gtceu:uev_assembler", 1]
    - ["gtceu:uiv_assembler", 1]
    - ["gtceu:luv_assembler", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:rhenate_w_plate
        - gtceu:double_mythrotight_carbide_steel_plate
        - kubejs:borealic_neutron_reflector
      t: |-
        Drawers first: rhenate w plates, double mythrotight carbide steel plates, borealic panels (from uev_fusion), UEV field generators, polonium bismide cables, trinium foil. Drum: naquadated soldering alloy, PEDOT:PSS, polonium bismide. One dedicated assembler per product in the sterile cleanroom.
    - i: ["gtceu:uhv_assembler", "kubejs:draconic_neutron_reflector"]
      t: |-
        Draconic panels first (50 s each). 6 per reflector casing craft and 6 per boosted casing craft: Keep Exact 32.
    - i: ["gtceu:uev_assembler", "kubejs:draconic_reflector_casing"]
      t: |-
        Reflector casings: 20 s per craft (2 casings). Keep Exact 16.
    - i: ["gtceu:uiv_assembler", "start_core:auxiliary_fusion_coil_mk2"]
      t: |-
        Auxiliary coil MK2: three coil MK1 (UHV page) per craft, 3 coils out. 15 s at 31 457 280 EU/t.
    - i: ["gtceu:luv_assembler", "start_core:auxiliary_boosted_fusion_casing_mk2"]
      t: |-
        Boosted casing MK2: UIV hull + coil + 2 voltage coils + field generator + panels. 8 s per 2 casings.
---
# UIV fusion parts: draconic reflector panel and casing (tier 6), auxiliary fusion coil MK2, boosted fusion casing MK2 → UEV and UIV Fusion Reactors

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_fusion` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV controllers, threading, fusion](../../plan/p19.md#uivmulti)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-uhv" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 50 s · 983 040 EU/t</span><span class="gt-badge t-uhv">UHV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Draconic neutron reflector panel: 1 rhenate w plate · 2 double mythrotight carbide steel plate · 1 borealic neutron reflector · 1 152 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Draconic neutron reflector panel: 1 rhenate w plate · 2 double mythrotight carbide steel plate · 1 borealic neutron reflector · 1 152 mB naquadated soldering alloy</span><span class="gt-sub"><span>rhenate w plate</span><span>double mythrotight carbide steel plate</span><span>borealic neutron reflector</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 097 152 EU/t</span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Draconic neutron reflector panel (kubejs:draconic_neutron_reflector) - 1 / 50 s"><img class="gt-ico" src="../../assets/icons/kubejs__draconic_neutron_reflector.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Draconic Neutron Reflector</span><span class="gt-note">Draconic neutron reflector panel</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uhv_assembler</code></div>
</div>
<div class="gt-panel t-uev" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 20 s · 7 864 320 EU/t</span><span class="gt-badge t-uev">UEV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 draconic reflector casing: 2 borealic reflector casing · 1 uev field generator · 6 draconic neutron reflector · 4 polonium bismide single cable · 64 trinium foil · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 draconic reflector casing: 2 borealic reflector casing · 1 uev field generator · 6 draconic neutron reflector · 4 polonium bismide single cable · 64 trinium foil · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>borealic reflector casing</span><span>uev field generator</span><span>draconic neutron reflector</span><span>polonium bismide single cable</span><span>trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 388 608 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Draconic reflector casing (tier 6) (kubejs:draconic_reflector_casing) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__draconic_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Draconic Reflector Casing</span><span class="gt-note">2 Draconic reflector casing (tier 6)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uev_assembler</code></div>
</div>
<div class="gt-panel t-uiv" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembler · sterile cleanroom · 15 s · 31 457 280 EU/t</span><span class="gt-badge t-uiv">UIV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="3 auxiliary fusion coil MK2: 3 auxiliary fusion coil mk1 · 4 uhv field generator · 2 uhv electric pump · 8 borealic neutron reflector · 8 UEV circuit · 2 nyanium normal fluid pipe · 8 abyssal alloy plate · 1 152 mB polonium bismide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">3 auxiliary fusion coil MK2: 3 auxiliary fusion coil mk1 · 4 uhv field generator · 2 uhv electric pump · 8 borealic neutron reflector · 8 UEV circuit · 2 nyanium normal fluid pipe · 8 abyssal alloy plate · 1 152 mB polonium bismide</span><span class="gt-sub"><span>auxiliary fusion coil mk1</span><span>uhv field generator</span><span>uhv electric pump</span><span>borealic neutron reflector</span><span>UEV circuit</span><span>nyanium normal fluid pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 33 554 432 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Auxiliary Fusion Coil MK2 (start_core:auxiliary_fusion_coil_mk2) - 3 / 15 s"><img class="gt-ico" src="../../assets/icons/start_core__auxiliary_fusion_coil_mk2.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Auxiliary Fusion Coil Mk2</span><b class="gt-q">3</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uiv_assembler</code></div>
</div>
<div class="gt-panel t-luv" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembler · cleanroom · 8 s · 30 720 EU/t</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 boosted fusion casing MK2: 1 uiv machine hull · 1 auxiliary fusion coil mk2 · 2 uiv voltage coil · 1 uev field generator · 6 draconic neutron reflector · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 boosted fusion casing MK2: 1 uiv machine hull · 1 auxiliary fusion coil mk2 · 2 uiv voltage coil · 1 uev field generator · 6 draconic neutron reflector · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate</span><span class="gt-sub"><span>uiv machine hull</span><span>auxiliary fusion coil mk2</span><span>uiv voltage coil</span><span>uev field generator</span><span>draconic neutron reflector</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Auxiliary Boosted Fusion Casing MK2 (start_core:auxiliary_boosted_fusion_casing_mk2) - 2 / 8 s"><img class="gt-ico" src="../../assets/icons/start_core__auxiliary_boosted_fusion_casing_mk2.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Auxiliary Boosted Fusion Casing Mk2</span><span class="gt-note">2 Auxiliary Boosted Fusion Casing MK2</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · sterile cleanroom · 50 s · 983 040 EU/t](#m-a1) → [Assembler · sterile cleanroom · 20 s · 7 864 320 EU/t](#m-a2) (also Assembler · sterile cleanroom · 50 s · 983 040 EU/t → [Assembler · cleanroom · 8 s · 30 720 EU/t](#m-a4))
- [Assembler · sterile cleanroom · 15 s · 31 457 280 EU/t](#m-a3) → [Assembler · cleanroom · 8 s · 30 720 EU/t](#m-a4)

### Direct steps

- Draconic neutron reflector panel → 2 draconic reflector casing: 2 borealic reflector casing · 1 uev field generator · 6 draconic neutron reflector · 4 polonium bismide single cable · 64 trinium foil · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (6)
- Draconic neutron reflector panel → 2 boosted fusion casing MK2: 1 uiv machine hull · 1 auxiliary fusion coil mk2 · 2 uiv voltage coil · 1 uev field generator · 6 draconic neutron reflector · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (6)
- Auxiliary Fusion Coil MK2 → 2 boosted fusion casing MK2: 1 uiv machine hull · 1 auxiliary fusion coil mk2 · 2 uiv voltage coil · 1 uev field generator · 6 draconic neutron reflector · 576 mB poly 34 ethylenedioxythiophene polystyrene sulfonate (1)
- 2 Auxiliary Boosted Fusion Casing MK2 → UIV Fusion Reactor (Assembly Line 97.5 s · 4 UXV circuits, draconic eye, 96 UIPIC) (casings)
- 2 Draconic reflector casing (tier 6) → UIV Fusion Reactor (Assembly Line 97.5 s · 4 UXV circuits, draconic eye, 96 UIPIC) (reflector)

## How to build

1. Drawers first: rhenate w plates, double mythrotight carbide steel plates, borealic panels (from uev\_fusion), UEV field generators, polonium bismide cables, trinium foil. Drum: naquadated soldering alloy, PEDOT:PSS, polonium bismide. One dedicated assembler per product in the sterile cleanroom. — `functionalstorage:oak_1`, `gtceu:rhenate_w_plate`, `gtceu:double_mythrotight_carbide_steel_plate`, `kubejs:borealic_neutron_reflector`
2. Draconic panels first (50 s each). 6 per reflector casing craft and 6 per boosted casing craft: Keep Exact 32. — `gtceu:uhv_assembler`, `kubejs:draconic_neutron_reflector`
3. Reflector casings: 20 s per craft (2 casings). Keep Exact 16. — `gtceu:uev_assembler`, `kubejs:draconic_reflector_casing`
4. Auxiliary coil MK2: three coil MK1 (UHV page) per craft, 3 coils out. 15 s at 31 457 280 EU/t. — `gtceu:uiv_assembler`, `start_core:auxiliary_fusion_coil_mk2`
5. Boosted casing MK2: UIV hull + coil + 2 voltage coils + field generator + panels. 8 s per 2 casings. — `gtceu:luv_assembler`, `start_core:auxiliary_boosted_fusion_casing_mk2`

## Tips

- Source: kjs systems/fusion/start\_fusion\_machines.js. Draconic panel (tier 6): 1 rhenate w plate + 2 double mythrotight carbide steel plates + 1 borealic panel + 1152 mB naquadated soldering alloy, 1000 ticks, VHA\[UHV\] = 983 040 EU/t, sterile cleanroom. Draconic reflector casing: 2 borealic reflector casings + 1 UEV field generator + 6 draconic panels + 4 polonium bismide single cables + 64 trinium foil + 576 mB PEDOT:PSS → 2 casings, 400 ticks, VA\[EV\] x 4^6 = 7 864 320 EU/t, sterile cleanroom. Prismalic (tier 7) casings need the Abyssal Containment Room and are the next era.
- Auxiliary fusion coil MK2 (3 per craft): 3 auxiliary coils MK1 + 4 UHV field generators + 2 UHV pumps + 8 borealic panels + 8 UEV circuits + 2 nyanium normal fluid pipes + 8 abyssal alloy plates + 1152 mB polonium bismide, 300 ticks, VA\[UIV\] = 31 457 280 EU/t, sterile cleanroom. Boosted casing MK2 (2 per craft): UIV hull + coil MK2 + 2 UIV voltage coils + 1 UEV field generator + 6 draconic panels + 576 mB PEDOT:PSS, 160 ticks, VA\[LuV\], plain cleanroom.
- UIV Fusion Reactor (Assembly Line, 1950 ticks, VA\[UIV\], station research of the UEV reactor VHA\[UIV\] / 192 CWU/t): auxiliary coil MK2 + 4 UXV circuits (abyssal processor mainframes) + draconic eye + double abyssal alloy plate + 2 UEV field generators + 96 UIPIC chips (64 + 32) + 32 rhenium super composite alloy single wire, 1152 mB naquadated soldering alloy + 1152 mB polonium bismide. So the reactor is a UXV-circuit item: not buildable inside this era; what this era delivers is the UEV reactor (uev\_fusion; its 4 UIV circuits come from uiv\_circuits) and the tier 6 reflector parts.
- Plasma with tier 6 reflectors: paradox, voidic and preon plasma (uiv\_alloys). The UEV reactor with tier 5 reflectors only covers magmatic, oganesson and aurourium fusion; the tier 6 recipes above start at 900 to 1160 MEU: Unverified which reactor holds that start energy (the quest text says a higher reflector than required doubles speed and power).
- Sub-steps people skip: (1) rhenate w (33 ingots, tin plasma) and mythrotight carbide steel (19 ingots, iron plasma, ascendant catalyst, heat 966) are both Hell Forge alloys at VA\[UIV\] (hellforge.js); (2) 64 trinium foil per craft; (3) the borealic panels are used in the coil MK2 too (8 per craft); (4) sterile cleanroom for panel, reflector casing and coil.
- **Unverified** reflector slots per reactor, the mythrotight carbide steel and rhenate w production, the UXV circuit timing.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:uhv_assembler` | 1 |
| `gtceu:uev_assembler` | 1 |
| `gtceu:uiv_assembler` | 1 |
| `gtceu:luv_assembler` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `kubejs:draconic_neutron_reflector`, `kubejs:draconic_reflector_casing`, `start_core:auxiliary_fusion_coil_mk2`, `start_core:auxiliary_boosted_fusion_casing_mk2`, `start_core:uiv_fusion_reactor`
