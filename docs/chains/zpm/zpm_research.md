---
kind: chain
id: zpm_research
order: 1310
data:
  t: |-
    Research Station parts: advanced computer casing, Object Holder, computation hatch, HPCA components (all need ZPM circuits)
  inf: true
  "n":
    - - g1
      - Computer casing · ZPM circuit · 64 fine cobalt wire · 64 fine electrum wire · 4 ITBTC single wire
      - g
      - functionalstorage:oak_1
      - - [Computer casing, "gtceu:computer_casing"]
        - [Fine cobalt wire, "gtceu:fine_cobalt_wire"]
        - [Fine electrum wire, "gtceu:fine_electrum_wire"]
        - [ITBTC single wire, "gtceu:indium_tin_barium_titanium_cuprate_single_wire"]
    - [a1, "Large Assembler on a 4A hatch · 10 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [ac, Advanced Computer Casing, x, "gtceu:advanced_computer_casing"]
    - - g2
      - ZPM input bus · 8 LuV emitter · ZPM circuit · 2 ZPM robot arm · 2 ZPM motor · 16 URD double wire · 2 optical pipe · 576 mB solder + 288 mB PBI
      - g
      - functionalstorage:oak_1
      - - [ZPM input bus, "gtceu:zpm_input_bus"]
        - [LuV emitter, "gtceu:luv_emitter"]
        - [ZPM robot arm, "gtceu:zpm_robot_arm"]
        - [ZPM motor, "gtceu:zpm_electric_motor"]
        - [URD double wire, "gtceu:uranium_rhodium_dinaquadide_double_wire"]
        - [Optical pipe, "gtceu:optical_pipe"]
    - [a2, "Assembly Line · 60 s · 100 000 EU/t (scan: ZPM input bus)", m, "gtceu:assembly_line"]
    - [oh, Object Holder, x, "gtceu:object_holder"]
    - - g3
      - Data receiver hatch · ZPM circuit · LuV sensor · 288 mB PBI
      - g
      - functionalstorage:oak_1
      - - [Data receiver hatch, "gtceu:data_receiver_hatch"]
        - [LuV sensor, "gtceu:luv_sensor"]
        - [PBI, "gtceu:polybenzimidazole_bucket"]
    - [a3, "Cleanroom Assembler · 10 s · 30 720 EU/t", m, "gtceu:luv_assembler"]
    - [ch, "Computation Data Reception Hatch (ZPM)", x, "gtceu:computation_receiver_hatch"]
    - - g4
      - Computer casing · IV circuit · data stick · 32 aluminium plate · 8 stainless screw · 4 ZPM circuit · LuV field generator · 1 B PCB coolant each
      - g
      - functionalstorage:oak_1
      - - [Data stick, "gtceu:data_stick"]
        - [Aluminium plate, "gtceu:aluminium_plate"]
        - [LuV field generator, "gtceu:luv_field_generator"]
        - [PCB coolant, "gtceu:pcb_coolant_bucket"]
    - [a4, "Cleanroom Assembler · 10 s · 7680 / 30 720 EU/t", m, "gtceu:iv_assembler"]
    - [hc, "HPCA empty, heat sink and computation components", x, "gtceu:hpca_computation_component"]
    - [rs, "Research Station + HPCA (luv_research chain, multis card)", o, "gtceu:research_station"]
  e:
    - [g1, a1, "1"]
    - [a1, ac, "1 / 10 s"]
    - [ac, rs, "23 + 13"]
    - [g2, a2, "1"]
    - [a2, oh, "1 / 60 s"]
    - [oh, rs, "1"]
    - [g3, a3, "1"]
    - [a3, ch, "1 / 10 s"]
    - [ch, rs, "1"]
    - [g4, a4, "1"]
    - [a4, hc, "10 s each"]
    - [hc, rs, HPCA]
  tips:
    - |-
      Why this chain: the Research Station and the HPCA are Assembly Line recipes (luv_research chain), but both multiblocks are built from parts that the base recipes only hint at. Verified from the multiblock card (GTResearchMachines patterns): the Research Station is 52 computer casings + 9 computer casing hatch spots (energy hatch 1 to 2, exactly 1 computation reception hatch) + 23 ADVANCED computer casings + 14 computer heat vents + exactly 1 Object Holder + controller; the HPCA is 13 advanced casings + 12 computer casings (min 5 hatch spots: energy, coolant fluid in, exactly 1 computation transmission hatch) + 15 heat vents + 9 component slots.
    - |-
      Advanced Computer Casing (ComputerRecipes advanced_computer_casing, not changed by the pack): 1 computer casing + 1 ZPM circuit + 64 fine cobalt wire + 64 fine electrum wire + 4 ITBTC single wire → 1 casing, assembler 200 ticks at VA[LuV] = 30 720 EU/t. 23 + 13 = 36 of them = 36 ZPM circuits and 36 computer casings before the machines even start. Computer casing: iridium frame + 6 iridium plates + 1 LuV circuit + 32 fine cobalt + 32 fine copper wire + 2 vanadium gallium single wire, 2 per craft (casingsPerCraft), 200 ticks at 30 720 EU/t. A Research Station + HPCA is about 110 computer casings = 55 crafts of 8 iridium ingots (1 frame = 2 ingots + 6 plates) = about 440 iridium. This is the real cost of research in this pack: start the iridium line early.
    - |-
      Heat vents (ComputerRecipes computer_heat_vent): stainless steel frame + 2 IV motors + 2 stainless steel rotors + 16 tiny stainless steel fluid pipes + 16 copper plates + 1 samarium iron arsenic oxide single wire → 2 vents, 100 ticks at 1920 EU/t (an EV assembler). 14 + 15 = 29 vents = 15 crafts = 30 IV motors. Samarium iron arsenic oxide wire is the IV superconductor of the rtm/iv chains.
    - |-
      Object Holder (ComputerRecipes object_holder, tier ZPM in GTResearchMachines): 1 ZPM input bus + 8 LuV emitters + 1 ZPM circuit + 2 ZPM robot arms + 2 ZPM motors + 16 URD double wire + 2 optical pipes + 576 mB soldering alloy + 288 mB PBI, Assembly Line 1200 ticks at 100 000 EU/t, scan of a ZPM input bus (2400 ticks, VA[IV]). It is a part that goes in the ‘H’ slot of the station; items you research are put into it together with a data orb. ZPM input bus (pack, io_hatches.js): ZPM hull + tungsten steel crate + 288 mB PBI, circuit 1, 300 ticks at 122 880 EU/t, so you need either a ZPM assembler or a Large Assembler on a LuV 4A hatch.
    - |-
      Computation hatches (ComputerRecipes, tier ZPM in GTResearchMachines): reception hatch = data receiver hatch + 1 ZPM circuit + 1 LuV sensor + 288 mB PBI, cleanroom assembler 200 ticks at 30 720 EU/t; transmission hatch = data transmitter hatch + 1 ZPM circuit + 1 LuV emitter + 288 mB PBI. Data receiver hatch = computer casing + LuV input bus + LuV circuit + IV sensor + 2 optical pipes + 288 mB PBI, same time and power. The optical data hatches are LuV tier, the computation ones ZPM tier, so the Data Bank link is available a tier earlier than the station link.
    - |-
      HPCA components (ComputerRecipes, cleanroom assembler, 200 ticks each, 1 B PCB coolant in every recipe): empty = computer casing + 1 IV circuit + data stick (7680 EU/t); heat sink = empty + 32 aluminium plates + 8 stainless screws (7680 EU/t); computation = empty + 4 ZPM circuits + 1 LuV field generator (30 720 EU/t). Tooltips (GTResearchMachines): computation component 4 CWU/t, needs 2 cooling, upkeep 1920 EU/t, max 30 720; heat sink 1 passive cooling; active cooler 2 cooling and uses PCB coolant (needs an advanced computer casing + 16 aluminium plates + 16 tiny stainless pipes + 8 stainless screws, 7680 EU/t); the 16 CWU/t advanced computation component needs 4 UV circuits and a ZPM field generator, so it is UV content. With 9 slots: 3 computation + 3 heat sinks + 3 active coolers = 12 CWU/t fully cooled. Unverified: the exact overheat rules, read the HPCA tooltip.
    - |-
      What the station needs for ZPM parts: the pack’s ZPM emitter, sensor and field generator recipes use STATION research of the LuV part at only 4 CWU/t (utils/tier_data.js zpm researchData special: cwuS 4, EUTS = VA[LuV]), so one computation component is enough for the whole era. Quest text: each overclock gives a 2.5 % additive discount on the CWU requirement of the research.
    - |-
      Sub-steps people skip: (1) the HPCA’s coolant needs a fluid hatch AND PCB coolant stock, one per component recipe; (2) exactly one computation hatch each (receiver on the station, transmitter on the HPCA), joined by an optical cable (Unverified: the optical pipe is a pipe block, place it between the two hatches); (3) every casing/vent block is a separate craft: check the multis card count, not the preview; (4) Keep Exact 4 on the ZPM circuit drawer, it feeds six different recipes here; (5) the advanced casing is made from a computer casing, so do not use those casings in the build first.
    - |-
      Unverified: whether the pack’s Large Assembler runs the cleanroom-tagged hatch and HPCA recipes (put a normal LuV Assembler inside the cleanroom if it does not), and the exact layout of the optical link between station and HPCA.
  b:
    - ["gtceu:research_station", 1]
    - ["gtceu:high_performance_computation_array", 1]
    - ["gtceu:object_holder", 1]
    - ["gtceu:computation_receiver_hatch", 1]
    - ["gtceu:computation_transmitter_hatch", 1]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:computer_casing", "gtceu:data_stick"]
      t: |-
        Drawers first, one per input: computer casings (a big stock), ZPM circuits (Keep Exact 4), fine cobalt wire, fine electrum wire, ITBTC single wire, aluminium plates, stainless screws, data sticks, IV circuits, optical pipes. PCB coolant, soldering alloy and PBI in drums. Every machine below gets its own input drawer behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:large_assembler", "gtceu:advanced_computer_casing", "gtceu:computer_casing"]
      t: |-
        Advanced casings: one dedicated Large Assembler on a LuV 4A hatch (or a LuV Assembler), computer casing + ZPM circuit + 64 fine cobalt + 64 fine electrum + 4 ITBTC single wire → 1 advanced casing in 10 s at 30 720 EU/t. Make 36 for the station and the HPCA. The output drawer feeds nothing else, so Keep Exact 64.
    - i: ["gtceu:assembly_line", "gtceu:object_holder", "gtceu:zpm_input_bus"]
      t: |-
        Object Holder: scan a ZPM input bus onto a data stick (120 s per scan at an IV Scanner, 7680 EU/t), put the stick in the Assembly Line’s Data Access Hatch. Buses in order: ZPM input bus, 8 LuV emitters, ZPM circuit, 2 ZPM robot arms, 2 ZPM motors, 16 URD double wire, 2 optical pipes; fluids 576 mB soldering alloy + 288 mB PBI. 60 s at 100 000 EU/t.
    - i: ["gtceu:luv_assembler", "gtceu:data_receiver_hatch", "gtceu:computation_receiver_hatch"]
      t: |-
        Computation hatches: a cleanroom assembler for each, data receiver or transmitter hatch + 1 ZPM circuit + 1 LuV sensor (reception) or emitter (transmission) + 288 mB PBI → hatch in 10 s at 30 720 EU/t. Both together cost 2 ZPM circuits.
    - i: ["gtceu:iv_assembler", "gtceu:hpca_computation_component", "gtceu:pcb_coolant_bucket"]
      t: |-
        HPCA parts, three assemblers in the cleanroom: empty component (computer casing + IV circuit + data stick + 1 B coolant), then heat sink (+ 32 aluminium plates + 8 stainless screws) and computation component (+ 4 ZPM circuits + LuV field generator, 30 720 EU/t). One empty component per output, so the empty-component assembler gets one drawer and two Keep Exact arms.
    - i: ["gtceu:research_station", "gtceu:high_performance_computation_array", "gtceu:advanced_computer_casing"]
      t: |-
        Build from the multis card: 52 + 9 computer casings, 23 advanced casings, 14 vents, Object Holder, computation reception hatch, 1 to 2 LuV energy hatches, maintenance. Then the HPCA: 13 advanced casings, 12 casings, 15 vents, the transmission hatch, a coolant fluid hatch and an energy hatch.
    - i: ["functionalstorage:oak_1", "gtceu:zpm_electric_motor"]
      t: |-
        Easy to miss: the whole chain waits for the ZPM motor and robot arm lines (zpm_components) and for URD wire (zpm_alloys); the order is: first ZPM circuit, ZPM motors, URD, then this chain, then the Research Station recipe itself in luv_research.
---
# Research Station parts: advanced computer casing, Object Holder, computation hatch, HPCA components (all need ZPM circuits)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_research` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Research Station, HPCA and data](../../plan/p12.md#research)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Large Assembler on a 4A hatch · 10 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Computer casing · ZPM circuit · 64 fine cobalt wire · 64 fine electrum wire · 4 ITBTC single wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Computer casing · ZPM circuit · 64 fine cobalt wire · 64 fine electrum wire · 4 ITBTC single wire</span><span class="gt-sub"><span>Computer casing</span><span>Fine cobalt wire</span><span>Fine electrum wire</span><span>ITBTC single wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Advanced Computer Casing (gtceu:advanced_computer_casing) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_computer_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Computer Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 100 000 EU/t (scan: ZPM input bus)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM input bus · 8 LuV emitter · ZPM circuit · 2 ZPM robot arm · 2 ZPM motor · 16 URD double wire · 2 optical pipe · 576 mB solder + 288 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM input bus · 8 LuV emitter · ZPM circuit · 2 ZPM robot arm · 2 ZPM motor · 16 URD double wire · 2 optical pipe · 576 mB solder + 288 mB PBI</span><span class="gt-sub"><span>ZPM input bus</span><span>LuV emitter</span><span>ZPM robot arm</span><span>ZPM motor</span><span>URD double wire</span><span>Optical pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Object Holder (gtceu:object_holder) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__object_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Object Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-luv" id="m-a3">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 10 s · 30 720 EU/t</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Data receiver hatch · ZPM circuit · LuV sensor · 288 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Data receiver hatch · ZPM circuit · LuV sensor · 288 mB PBI</span><span class="gt-sub"><span>Data receiver hatch</span><span>LuV sensor</span><span>PBI</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Computation Data Reception Hatch (ZPM) (gtceu:computation_receiver_hatch) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__computation_receiver_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Computation Receiver Hatch</span><span class="gt-note">Computation Data Reception Hatch (ZPM)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a4">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 10 s · 7680 / 30 720 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Computer casing · IV circuit · data stick · 32 aluminium plate · 8 stainless screw · 4 ZPM circuit · LuV field generator · 1 B PCB coolant each (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Computer casing · IV circuit · data stick · 32 aluminium plate · 8 stainless screw · 4 ZPM circuit · LuV field generator · 1 B PCB coolant each</span><span class="gt-sub"><span>Data stick</span><span>Aluminium plate</span><span>LuV field generator</span><span>PCB coolant</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HPCA empty, heat sink and computation components (gtceu:hpca_computation_component) - 10 s each"><img class="gt-ico" src="../../assets/icons/gtceu__hpca_computation_component.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hpca Computation Component</span><span class="gt-note">HPCA empty, heat sink and computation components</span><b class="gt-q">10 s each</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
</div>

## Flow

- [Large Assembler on a 4A hatch · 10 s · 30 720 EU/t](#m-a1)
- [Assembly Line · 60 s · 100 000 EU/t (scan: ZPM input bus)](#m-a2)
- [Cleanroom Assembler · 10 s · 30 720 EU/t](#m-a3)
- [Cleanroom Assembler · 10 s · 7680 / 30 720 EU/t](#m-a4)

### Direct steps

- Advanced Computer Casing → Research Station + HPCA (luv\_research chain, multis card) (23 + 13)
- Object Holder → Research Station + HPCA (luv\_research chain, multis card) (1)
- Computation Data Reception Hatch (ZPM) → Research Station + HPCA (luv\_research chain, multis card) (1)
- HPCA empty, heat sink and computation components → Research Station + HPCA (luv\_research chain, multis card) (HPCA)

## How to build

1. Drawers first, one per input: computer casings (a big stock), ZPM circuits (Keep Exact 4), fine cobalt wire, fine electrum wire, ITBTC single wire, aluminium plates, stainless screws, data sticks, IV circuits, optical pipes. PCB coolant, soldering alloy and PBI in drums. Every machine below gets its own input drawer behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:computer_casing`, `gtceu:data_stick`
2. Advanced casings: one dedicated Large Assembler on a LuV 4A hatch (or a LuV Assembler), computer casing + ZPM circuit + 64 fine cobalt + 64 fine electrum + 4 ITBTC single wire → 1 advanced casing in 10 s at 30 720 EU/t. Make 36 for the station and the HPCA. The output drawer feeds nothing else, so Keep Exact 64. — `gtceu:large_assembler`, `gtceu:advanced_computer_casing`, `gtceu:computer_casing`
3. Object Holder: scan a ZPM input bus onto a data stick (120 s per scan at an IV Scanner, 7680 EU/t), put the stick in the Assembly Line’s Data Access Hatch. Buses in order: ZPM input bus, 8 LuV emitters, ZPM circuit, 2 ZPM robot arms, 2 ZPM motors, 16 URD double wire, 2 optical pipes; fluids 576 mB soldering alloy + 288 mB PBI. 60 s at 100 000 EU/t. — `gtceu:assembly_line`, `gtceu:object_holder`, `gtceu:zpm_input_bus`
4. Computation hatches: a cleanroom assembler for each, data receiver or transmitter hatch + 1 ZPM circuit + 1 LuV sensor (reception) or emitter (transmission) + 288 mB PBI → hatch in 10 s at 30 720 EU/t. Both together cost 2 ZPM circuits. — `gtceu:luv_assembler`, `gtceu:data_receiver_hatch`, `gtceu:computation_receiver_hatch`
5. HPCA parts, three assemblers in the cleanroom: empty component (computer casing + IV circuit + data stick + 1 B coolant), then heat sink (+ 32 aluminium plates + 8 stainless screws) and computation component (+ 4 ZPM circuits + LuV field generator, 30 720 EU/t). One empty component per output, so the empty-component assembler gets one drawer and two Keep Exact arms. — `gtceu:iv_assembler`, `gtceu:hpca_computation_component`, `gtceu:pcb_coolant_bucket`
6. Build from the multis card: 52 + 9 computer casings, 23 advanced casings, 14 vents, Object Holder, computation reception hatch, 1 to 2 LuV energy hatches, maintenance. Then the HPCA: 13 advanced casings, 12 casings, 15 vents, the transmission hatch, a coolant fluid hatch and an energy hatch. — `gtceu:research_station`, `gtceu:high_performance_computation_array`, `gtceu:advanced_computer_casing`
7. Easy to miss: the whole chain waits for the ZPM motor and robot arm lines (zpm\_components) and for URD wire (zpm\_alloys); the order is: first ZPM circuit, ZPM motors, URD, then this chain, then the Research Station recipe itself in luv\_research. — `functionalstorage:oak_1`, `gtceu:zpm_electric_motor`

## Tips

- Why this chain: the Research Station and the HPCA are Assembly Line recipes (luv\_research chain), but both multiblocks are built from parts that the base recipes only hint at. Verified from the multiblock card (GTResearchMachines patterns): the Research Station is 52 computer casings + 9 computer casing hatch spots (energy hatch 1 to 2, exactly 1 computation reception hatch) + 23 ADVANCED computer casings + 14 computer heat vents + exactly 1 Object Holder + controller; the HPCA is 13 advanced casings + 12 computer casings (min 5 hatch spots: energy, coolant fluid in, exactly 1 computation transmission hatch) + 15 heat vents + 9 component slots.
- Advanced Computer Casing (ComputerRecipes advanced\_computer\_casing, not changed by the pack): 1 computer casing + 1 ZPM circuit + 64 fine cobalt wire + 64 fine electrum wire + 4 ITBTC single wire → 1 casing, assembler 200 ticks at VA\[LuV\] = 30 720 EU/t. 23 + 13 = 36 of them = 36 ZPM circuits and 36 computer casings before the machines even start. Computer casing: iridium frame + 6 iridium plates + 1 LuV circuit + 32 fine cobalt + 32 fine copper wire + 2 vanadium gallium single wire, 2 per craft (casingsPerCraft), 200 ticks at 30 720 EU/t. A Research Station + HPCA is about 110 computer casings = 55 crafts of 8 iridium ingots (1 frame = 2 ingots + 6 plates) = about 440 iridium. This is the real cost of research in this pack: start the iridium line early.
- Heat vents (ComputerRecipes computer\_heat\_vent): stainless steel frame + 2 IV motors + 2 stainless steel rotors + 16 tiny stainless steel fluid pipes + 16 copper plates + 1 samarium iron arsenic oxide single wire → 2 vents, 100 ticks at 1920 EU/t (an EV assembler). 14 + 15 = 29 vents = 15 crafts = 30 IV motors. Samarium iron arsenic oxide wire is the IV superconductor of the rtm/iv chains.
- Object Holder (ComputerRecipes object\_holder, tier ZPM in GTResearchMachines): 1 ZPM input bus + 8 LuV emitters + 1 ZPM circuit + 2 ZPM robot arms + 2 ZPM motors + 16 URD double wire + 2 optical pipes + 576 mB soldering alloy + 288 mB PBI, Assembly Line 1200 ticks at 100 000 EU/t, scan of a ZPM input bus (2400 ticks, VA\[IV\]). It is a part that goes in the ‘H’ slot of the station; items you research are put into it together with a data orb. ZPM input bus (pack, io\_hatches.js): ZPM hull + tungsten steel crate + 288 mB PBI, circuit 1, 300 ticks at 122 880 EU/t, so you need either a ZPM assembler or a Large Assembler on a LuV 4A hatch.
- Computation hatches (ComputerRecipes, tier ZPM in GTResearchMachines): reception hatch = data receiver hatch + 1 ZPM circuit + 1 LuV sensor + 288 mB PBI, cleanroom assembler 200 ticks at 30 720 EU/t; transmission hatch = data transmitter hatch + 1 ZPM circuit + 1 LuV emitter + 288 mB PBI. Data receiver hatch = computer casing + LuV input bus + LuV circuit + IV sensor + 2 optical pipes + 288 mB PBI, same time and power. The optical data hatches are LuV tier, the computation ones ZPM tier, so the Data Bank link is available a tier earlier than the station link.
- HPCA components (ComputerRecipes, cleanroom assembler, 200 ticks each, 1 B PCB coolant in every recipe): empty = computer casing + 1 IV circuit + data stick (7680 EU/t); heat sink = empty + 32 aluminium plates + 8 stainless screws (7680 EU/t); computation = empty + 4 ZPM circuits + 1 LuV field generator (30 720 EU/t). Tooltips (GTResearchMachines): computation component 4 CWU/t, needs 2 cooling, upkeep 1920 EU/t, max 30 720; heat sink 1 passive cooling; active cooler 2 cooling and uses PCB coolant (needs an advanced computer casing + 16 aluminium plates + 16 tiny stainless pipes + 8 stainless screws, 7680 EU/t); the 16 CWU/t advanced computation component needs 4 UV circuits and a ZPM field generator, so it is UV content. With 9 slots: 3 computation + 3 heat sinks + 3 active coolers = 12 CWU/t fully cooled. Unverified: the exact overheat rules, read the HPCA tooltip.
- What the station needs for ZPM parts: the pack’s ZPM emitter, sensor and field generator recipes use STATION research of the LuV part at only 4 CWU/t (utils/tier\_data.js zpm researchData special: cwuS 4, EUTS = VA\[LuV\]), so one computation component is enough for the whole era. Quest text: each overclock gives a 2.5 % additive discount on the CWU requirement of the research.
- Sub-steps people skip: (1) the HPCA’s coolant needs a fluid hatch AND PCB coolant stock, one per component recipe; (2) exactly one computation hatch each (receiver on the station, transmitter on the HPCA), joined by an optical cable (Unverified: the optical pipe is a pipe block, place it between the two hatches); (3) every casing/vent block is a separate craft: check the multis card count, not the preview; (4) Keep Exact 4 on the ZPM circuit drawer, it feeds six different recipes here; (5) the advanced casing is made from a computer casing, so do not use those casings in the build first.
- **Unverified** whether the pack’s Large Assembler runs the cleanroom-tagged hatch and HPCA recipes (put a normal LuV Assembler inside the cleanroom if it does not), and the exact layout of the optical link between station and HPCA.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:research_station` | 1 |
| `gtceu:high_performance_computation_array` | 1 |
| `gtceu:object_holder` | 1 |
| `gtceu:computation_receiver_hatch` | 1 |
| `gtceu:computation_transmitter_hatch` | 1 |
| `gtceu:large_assembler` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:advanced_computer_casing`, `gtceu:object_holder`, `gtceu:computation_receiver_hatch`, `gtceu:computation_transmitter_hatch`, `gtceu:hpca_computation_component`, `gtceu:hpca_heat_sink_component`, `gtceu:hpca_empty_component`
