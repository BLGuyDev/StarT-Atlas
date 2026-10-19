---
kind: chain
id: uv_research
order: 1680
data:
  t: |-
    More CWU for UV research: advanced HPCA computation component (16 CWU/t), active cooler, bridge component and the Network Switch that joins several HPCAs
  inf: true
  "n":
    - - g1
      - HPCA computation component · 4 UV circuit · ZPM field generator · 1 B PCB coolant
      - g
      - functionalstorage:oak_1
      - - [HPCA computation component, "gtceu:hpca_computation_component"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [PCB coolant, "gtceu:pcb_coolant_bucket"]
    - [a1, "ZPM Cleanroom Assembler · 10 s · 122 880 EU/t", m, "gtceu:zpm_assembler"]
    - - ac
      - HPCA Advanced Computation Component (16 CWU/t, cooling 4)
      - x
      - gtceu:hpca_advanced_computation_component
    - - g2
      - Advanced computer casing · 16 aluminium plate · 16 tiny stainless pipe · 8 stainless screw · 1 B PCB coolant
      - g
      - functionalstorage:oak_1
      - - [Advanced computer casing, "gtceu:advanced_computer_casing"]
        - [Aluminium plate, "gtceu:aluminium_plate"]
        - [Tiny stainless steel pipe, "gtceu:stainless_steel_tiny_fluid_pipe"]
        - [Stainless steel screw, "gtceu:stainless_steel_screw"]
    - [a2, "IV Cleanroom Assembler · 10 s · 7680 EU/t", m, "gtceu:iv_assembler"]
    - [co, "HPCA Active Cooling Component (cooling 2)", x, "gtceu:hpca_active_cooler_component"]
    - - g3
      - Advanced computer casing · UV circuit · ZPM emitter · 2 optical pipe · 1 B PCB coolant
      - g
      - functionalstorage:oak_1
      - [[ZPM emitter, "gtceu:zpm_emitter"], [Optical pipe, "gtceu:optical_pipe"]]
    - [a3, "LuV Cleanroom Assembler · 10 s · 30 720 EU/t", m, "gtceu:luv_assembler"]
    - [br, HPCA Bridge Component, x, "gtceu:hpca_bridge_component"]
    - - g4
      - Computer casing · 4 ZPM emitter · 4 ZPM sensor · 4 UV circuit · 32 double ENTED wire · 128 tritanium foil · 8 optical pipe · 576 mB solder · 576 mB PBI
      - g
      - functionalstorage:oak_1
      - - [ZPM sensor, "gtceu:zpm_sensor"]
        - [Double ENTED wire, "gtceu:enriched_naquadah_trinium_europium_duranide_double_wire"]
        - [Tritanium foil, "gtceu:tritanium_foil"]
    - [a4, "Assembly Line · 60 s · 100 000 EU/t · research 32 CWU/t", m, "gtceu:assembly_line"]
    - [sw, "Network Switch (joins HPCAs with bridges)", o, "gtceu:network_switch"]
  e:
    - [g1, a1, "1"]
    - [a1, ac, "1 / 10 s"]
    - [g2, a2, "1"]
    - [a2, co, "1 / 10 s"]
    - [g3, a3, "1"]
    - [a3, br, "1 / 10 s"]
    - [g4, a4, "1"]
    - [a4, sw, "1 / 60 s"]
    - [br, sw, bridges]
  tips:
    - |-
      Why: UV recipes ask for 32 to 96 CWU/t of Research Station power (UV hatch 64, UV components 32 / 48, wetware computer 64, wetware mainframe 96, UV fusion reactor 96). A ZPM-era HPCA with basic components gives 4 CWU/t per component (9 slots). Verified tooltips (gtsrc GTResearchMachines): computation component 4 CWU/t, cooling 2, upkeep VA[EV], max VA[LuV]; ADVANCED component 16 CWU/t, cooling 4, upkeep VA[IV], max VA[ZPM]; heat sink cooling 1 (passive); active cooler cooling 2, uses PCB coolant, max VA[IV]. Research Station = exactly 1 computation reception hatch, so only ONE HPCA can feed it directly.
    - |-
      Recipes (gtsrc ComputerRecipes, assembler, cleanroom, 200 ticks, 1000 mB PCB coolant each): advanced computation component = HPCA computation component + 4 UV circuits + 1 ZPM field generator at VA[ZPM] = 122 880 EU/t; active cooler = advanced computer casing + 16 aluminium plates + 16 tiny stainless steel fluid pipes + 8 stainless steel screws at VA[IV]; bridge component = advanced computer casing + 1 UV circuit + 1 ZPM emitter + 2 optical pipes at VA[LuV]. Each advanced component costs 4 UV circuits, so a 3-advanced HPCA costs 12 UV circuits.
    - |-
      How much CWU: an HPCA has 9 slots. Cooling needed by components must be covered by coolers or the array overheats (GT rule; Unverified in this fork). One advanced component needs 4 cooling = 2 active coolers, so the best single HPCA is 3 advanced + 6 active coolers = 48 CWU/t, enough for the 32 and 48 CWU/t recipes of the UV components but not for 64 or 96.
    - |-
      More than 48 CWU/t (quest text, ftbquests abydos.network_switch): the Research Station only accepts one HPCA, but a Network Switch (multiblock: 25 computer casings + 1 advanced computer casing + controller, 7 spots for energy / computation hatches) routes the computation of several HPCAs with a BRIDGE component each into it. Network Switch recipe (ComputerRecipes, Assembly Line, 1200 ticks at 100 000 EU/t, station research of an optical pipe at 32 CWU/t): computer casing + 4 ZPM emitters + 4 ZPM sensors + 4 UV circuits + 32 ENTED DOUBLE wire + 128 tritanium foil + 8 optical pipes, 576 mB soldering alloy + 576 mB PBI. Three bridged HPCAs of 2 advanced + 1 basic + 4 active + 1 bridge each give about 36 CWU/t, so 96 CWU/t needs three of them (Unverified slot balance).
    - |-
      Sub-steps people skip: (1) PCB coolant: 1 B per component (and per active cooler tick), so the pcb_coolant chain must run at scale; (2) advanced casings are the ZPM research hardware again: 1 per cooler and 1 per bridge; (3) computation hatch tiers: the transmitter and receiver hatches in zpm_research are enough, the optical pipes carry any amount; (4) the 64 and 96 CWU/t recipes simply do not start with less: check the Research Station’s CWU/t readout before spending UV circuits.
    - |-
      Unverified: slot and cooling balance, total CWU research time, optical pipe throughput.
  b:
    - ["gtceu:high_performance_computation_array", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:network_switch", 1]
    - ["gtceu:zpm_assembler", 1]
    - ["gtceu:iv_assembler", 1]
    - ["gtceu:luv_assembler", 1]
    - ["gtceu:assembly_line", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 4]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:hpca_computation_component
        - gtceu:advanced_computer_casing
        - gtceu:zpm_field_generator
      t: |-
        Drawers first, one per input: HPCA computation components, UV circuits (4 per craft), ZPM field generators, advanced computer casings, aluminium plates, tiny stainless pipes, stainless screws, ZPM emitters and sensors, optical pipes. Drum: PCB coolant (a pipe per assembler).
    - i: ["gtceu:zpm_assembler", "gtceu:hpca_advanced_computation_component"]
      t: |-
        Advanced component: cleanroom assembler at 122 880 EU/t (10 s): computation component + 4 UV circuits + ZPM field generator + 1 B coolant. Output drawer Keep Exact 3.
    - i: ["gtceu:iv_assembler", "gtceu:hpca_active_cooler_component"]
      t: |-
        Active coolers: IV cleanroom assembler, 6 per HPCA. Output drawer Keep Exact 6.
    - i: ["gtceu:luv_assembler", "gtceu:hpca_bridge_component"]
      t: |-
        Bridge components: LuV cleanroom assembler, 1 per extra HPCA.
    - i: ["gtceu:assembly_line", "gtceu:network_switch"]
      t: |-
        Network Switch: station research of an optical pipe (32 CWU/t) into an orb, then the Assembly Line (60 s at 100 000 EU/t).
    - i: ["gtceu:high_performance_computation_array", "gtceu:research_station"]
      t: |-
        Build: each HPCA gets 2 advanced + 4 active coolers + 1 bridge (+ 1 basic + 1 active if a slot is free); their transmission hatches go to the Network Switch, one switch output hatch to the Research Station’s reception hatch. Read the CWU/t readout.
---
# More CWU for UV research: advanced HPCA computation component (16 CWU/t), active cooler, bridge component and the Network Switch that joins several HPCAs

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_research` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Research data and CWU power](../../plan/p14.md#uvdata)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-a1">
<div class="gt-head"><span class="gt-mname">ZPM Cleanroom Assembler · 10 s · 122 880 EU/t</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="HPCA computation component · 4 UV circuit · ZPM field generator · 1 B PCB coolant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">HPCA computation component · 4 UV circuit · ZPM field generator · 1 B PCB coolant</span><span class="gt-sub"><span>HPCA computation component</span><span>ZPM field generator</span><span>PCB coolant</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HPCA Advanced Computation Component (16 CWU/t, cooling 4) (gtceu:hpca_advanced_computation_component) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__hpca_advanced_computation_component.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hpca Advanced Computation Component</span><span class="gt-note">HPCA Advanced Computation Component (16 CWU/t, cooling 4)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a2">
<div class="gt-head"><span class="gt-mname">IV Cleanroom Assembler · 10 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Advanced computer casing · 16 aluminium plate · 16 tiny stainless pipe · 8 stainless screw · 1 B PCB coolant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Advanced computer casing · 16 aluminium plate · 16 tiny stainless pipe · 8 stainless screw · 1 B PCB coolant</span><span class="gt-sub"><span>Advanced computer casing</span><span>Aluminium plate</span><span>Tiny stainless steel pipe</span><span>Stainless steel screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HPCA Active Cooling Component (cooling 2) (gtceu:hpca_active_cooler_component) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__hpca_active_cooler_component.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hpca Active Cooler Component</span><span class="gt-note">HPCA Active Cooling Component (cooling 2)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-luv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LuV Cleanroom Assembler · 10 s · 30 720 EU/t</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Advanced computer casing · UV circuit · ZPM emitter · 2 optical pipe · 1 B PCB coolant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Advanced computer casing · UV circuit · ZPM emitter · 2 optical pipe · 1 B PCB coolant</span><span class="gt-sub"><span>ZPM emitter</span><span>Optical pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HPCA Bridge Component (gtceu:hpca_bridge_component) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__hpca_bridge_component.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hpca Bridge Component</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 100 000 EU/t · research 32 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Computer casing · 4 ZPM emitter · 4 ZPM sensor · 4 UV circuit · 32 double ENTED wire · 128 tritanium foil · 8 optical pipe · 576 mB solder · 576 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Computer casing · 4 ZPM emitter · 4 ZPM sensor · 4 UV circuit · 32 double ENTED wire · 128 tritanium foil · 8 optical pipe · 576 mB solder · 576 mB PBI</span><span class="gt-sub"><span>ZPM sensor</span><span>Double ENTED wire</span><span>Tritanium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Network Switch (joins HPCAs with bridges) (gtceu:network_switch) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__network_switch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Network Switch</span><span class="gt-note">Network Switch (joins HPCAs with bridges)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [ZPM Cleanroom Assembler · 10 s · 122 880 EU/t](#m-a1)
- [IV Cleanroom Assembler · 10 s · 7680 EU/t](#m-a2)
- [LuV Cleanroom Assembler · 10 s · 30 720 EU/t](#m-a3)
- [Assembly Line · 60 s · 100 000 EU/t · research 32 CWU/t](#m-a4)

### Direct steps

- HPCA Bridge Component → Network Switch (joins HPCAs with bridges) (bridges)

## How to build

1. Drawers first, one per input: HPCA computation components, UV circuits (4 per craft), ZPM field generators, advanced computer casings, aluminium plates, tiny stainless pipes, stainless screws, ZPM emitters and sensors, optical pipes. Drum: PCB coolant (a pipe per assembler). — `functionalstorage:oak_1`, `gtceu:hpca_computation_component`, `gtceu:advanced_computer_casing`, `gtceu:zpm_field_generator`
2. Advanced component: cleanroom assembler at 122 880 EU/t (10 s): computation component + 4 UV circuits + ZPM field generator + 1 B coolant. Output drawer Keep Exact 3. — `gtceu:zpm_assembler`, `gtceu:hpca_advanced_computation_component`
3. Active coolers: IV cleanroom assembler, 6 per HPCA. Output drawer Keep Exact 6. — `gtceu:iv_assembler`, `gtceu:hpca_active_cooler_component`
4. Bridge components: LuV cleanroom assembler, 1 per extra HPCA. — `gtceu:luv_assembler`, `gtceu:hpca_bridge_component`
5. Network Switch: station research of an optical pipe (32 CWU/t) into an orb, then the Assembly Line (60 s at 100 000 EU/t). — `gtceu:assembly_line`, `gtceu:network_switch`
6. Build: each HPCA gets 2 advanced + 4 active coolers + 1 bridge (+ 1 basic + 1 active if a slot is free); their transmission hatches go to the Network Switch, one switch output hatch to the Research Station’s reception hatch. Read the CWU/t readout. — `gtceu:high_performance_computation_array`, `gtceu:research_station`

## Tips

- Why: UV recipes ask for 32 to 96 CWU/t of Research Station power (UV hatch 64, UV components 32 / 48, wetware computer 64, wetware mainframe 96, UV fusion reactor 96). A ZPM-era HPCA with basic components gives 4 CWU/t per component (9 slots). Verified tooltips (gtsrc GTResearchMachines): computation component 4 CWU/t, cooling 2, upkeep VA\[EV\], max VA\[LuV\]; ADVANCED component 16 CWU/t, cooling 4, upkeep VA\[IV\], max VA\[ZPM\]; heat sink cooling 1 (passive); active cooler cooling 2, uses PCB coolant, max VA\[IV\]. Research Station = exactly 1 computation reception hatch, so only ONE HPCA can feed it directly.
- Recipes (gtsrc ComputerRecipes, assembler, cleanroom, 200 ticks, 1000 mB PCB coolant each): advanced computation component = HPCA computation component + 4 UV circuits + 1 ZPM field generator at VA\[ZPM\] = 122 880 EU/t; active cooler = advanced computer casing + 16 aluminium plates + 16 tiny stainless steel fluid pipes + 8 stainless steel screws at VA\[IV\]; bridge component = advanced computer casing + 1 UV circuit + 1 ZPM emitter + 2 optical pipes at VA\[LuV\]. Each advanced component costs 4 UV circuits, so a 3-advanced HPCA costs 12 UV circuits.
- How much CWU: an HPCA has 9 slots. Cooling needed by components must be covered by coolers or the array overheats (GT rule; Unverified in this fork). One advanced component needs 4 cooling = 2 active coolers, so the best single HPCA is 3 advanced + 6 active coolers = 48 CWU/t, enough for the 32 and 48 CWU/t recipes of the UV components but not for 64 or 96.
- More than 48 CWU/t (quest text, ftbquests abydos.network\_switch): the Research Station only accepts one HPCA, but a Network Switch (multiblock: 25 computer casings + 1 advanced computer casing + controller, 7 spots for energy / computation hatches) routes the computation of several HPCAs with a BRIDGE component each into it. Network Switch recipe (ComputerRecipes, Assembly Line, 1200 ticks at 100 000 EU/t, station research of an optical pipe at 32 CWU/t): computer casing + 4 ZPM emitters + 4 ZPM sensors + 4 UV circuits + 32 ENTED DOUBLE wire + 128 tritanium foil + 8 optical pipes, 576 mB soldering alloy + 576 mB PBI. Three bridged HPCAs of 2 advanced + 1 basic + 4 active + 1 bridge each give about 36 CWU/t, so 96 CWU/t needs three of them (Unverified slot balance).
- Sub-steps people skip: (1) PCB coolant: 1 B per component (and per active cooler tick), so the pcb\_coolant chain must run at scale; (2) advanced casings are the ZPM research hardware again: 1 per cooler and 1 per bridge; (3) computation hatch tiers: the transmitter and receiver hatches in zpm\_research are enough, the optical pipes carry any amount; (4) the 64 and 96 CWU/t recipes simply do not start with less: check the Research Station’s CWU/t readout before spending UV circuits.
- **Unverified** slot and cooling balance, total CWU research time, optical pipe throughput.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:high_performance_computation_array` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:network_switch` | 1 |
| `gtceu:zpm_assembler` | 1 |
| `gtceu:iv_assembler` | 1 |
| `gtceu:luv_assembler` | 1 |
| `gtceu:assembly_line` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:hpca_advanced_computation_component`, `gtceu:hpca_active_cooler_component`, `gtceu:hpca_bridge_component`, `gtceu:network_switch`
