---
kind: chain
id: luv_research
order: 1280
data:
  t: |-
    Research: Data Bank (IV power), High Performance Computation Array and Research Station (both 100 000 EU/t, ZPM circuits)
  inf: true
  "n":
    - - ig
      - |-
        8 LuV circuit · computer casing · data orb · 64 fine cobalt + 64 fine copper wire · 4 optical pipe · 16 ITBTC double wire · 288 mB solder · 500 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [Nanoprocessor Mainframe, "gtceu:nano_processor_mainframe"]
        - [Data Orb, "gtceu:data_orb"]
        - [Fine ITBTC wire, "gtceu:fine_indium_tin_barium_titanium_cuprate_wire"]
        - [Soldering alloy, "gtceu:soldering_alloy_bucket"]
    - [a1, "Assembly Line · 60 s · 6000 EU/t (scan: Data Access Hatch)", m, "gtceu:assembly_line"]
    - [db, Data Bank, x, "gtceu:data_bank"]
    - - hg
      - Data Bank · 4 ZPM circuit · 8 LuV field generator · data orb · cover screen · 64 URD double wire · 16 optical pipe · 1152 mB solder + molten vanadium gallium · 4 B PCB coolant
      - g
      - functionalstorage:oak_1
      - - [LuV Field Generator, "gtceu:luv_field_generator"]
        - [Data Orb, "gtceu:data_orb"]
        - [PCB coolant, "gtceu:pcb_coolant_bucket"]
    - [a2, "Assembly Line · 60 s · 100 000 EU/t (scan: cover screen)", m, "gtceu:assembly_line"]
    - [hp, High Performance Computation Array, o, "gtceu:high_performance_computation_array"]
    - - rg
      - Data Bank · 8 LuV sensor · 8 ZPM circuit · 2 LuV field generator · 2 ZPM motor · 32 URD double wire · 32 trinium foil · 16 optical pipe · 1152 mB solder + vanadium gallium
      - g
      - functionalstorage:oak_1
      - - [LuV Sensor, "gtceu:luv_sensor"]
        - [LuV Field Generator, "gtceu:luv_field_generator"]
        - [ZPM Electric Motor, "gtceu:zpm_electric_motor"]
        - [Trinium foil, "gtceu:trinium_foil"]
    - [a3, "Assembly Line · 60 s · 100 000 EU/t (scan: LuV Scanner)", m, "gtceu:assembly_line"]
    - [rs, Research Station, o, "gtceu:research_station"]
  e:
    - [ig, a1, "1"]
    - [a1, db, "1 / 60 s"]
    - [db, a2, "1"]
    - [hg, a2, "1"]
    - [a2, hp, "1 / 60 s"]
    - [db, a3, "1"]
    - [rg, a3, "1"]
    - [a3, rs, "1 / 60 s"]
  tips:
    - |-
      Where this sits: only the Data Bank is LuV; the HPCA and Research Station (and computation hatches, Advanced Data Access Hatch) are ZPM-gated by 4-8 ZPM circuits (ComputerRecipes, not changed by the pack, verified). Research Station research is also required by ZPM sensor, emitter and field generator (kjs tier_data.js zpm row, CWU 4). Data Bank: computer casing + 8 LuV circuits + 1 data orb + 64 fine cobalt wire + 64 fine copper wire + 4 optical pipes + 16 ITBTC double wire, 288 mB soldering alloy + 500 mB lubricant, 1200 ticks at 6000 EU/t, scanner research of a Data Access Hatch (2400 ticks, 1920 EU/t): this one fits an IV hatch. HPCA: Data Bank + 4 ZPM circuits + 8 LuV field generators + data orb + cover screen + 64 uranium rhodium dinaquadide double wire + 16 optical pipes + 1152 mB solder + 1152 mB vanadium gallium + 4 B PCB coolant, 1200 ticks at 100 000 EU/t, scan of the cover screen. Research Station: Data Bank + 8 LuV sensors + 8 ZPM circuits + 2 LuV field generators + 2 ZPM motors + 32 URD double wire + 32 trinium foil + 16 optical pipes + 1152 mB solder + 1152 mB vanadium gallium, 1200 ticks at 100 000 EU/t, scan of a LuV Scanner (2400 ticks at 7680 EU/t).
    - |-
      100 000 EU/t is ZPM tier, so the HPCA and the Research Station need a ZPM-class energy source for the Assembly Line: a LuV 4A hatch (the quest: the 4A LuV hatch gives ZPM recipe speeds) or a ZPM hatch. Also the quest chapter puts both after the uranium rhodium dinaquadide ingot (URD) and the first ZPM circuit (quantum mainframe, which itself needs the quantum computer, the IV Circuit Assembler and crystal/quantum lines). So the order is: LuV circuits, hull, components, luv_hatches, naquadah, URD, ZPM circuit, then these.
    - |-
      HPCA: a computation provider, it needs a bridge or direct hatch and heat sinks. Component recipes (ComputerRecipes, cleanroom assembler, 200 ticks, 1 B PCB coolant each): empty = computer casing + IV circuit + data stick (7680 EU/t); heat sink = empty + 32 aluminium plates + 8 stainless screws; active cooler = advanced computer casing + 16 aluminium plates + 16 tiny stainless pipes + 8 stainless screws; computation component = empty + 4 ZPM circuits + LuV field generator (30 720 EU/t). Quest: 48 CWU/t is the max without a bridge, 36 with a bridge. The pack’s later components are in kjs systems/research.js. Unverified: how many CWU/t each component gives (read the HPCA tooltip).
    - |-
      Computer casing (ComputerRecipes computer_casing): iridium frame + 6 iridium plates + 1 LuV circuit + 32 fine cobalt wire + 32 fine copper wire + 2 vanadium gallium single wire, assembler 200 ticks at 30 720 EU/t, 2 per craft (casingsPerCraft 2): LuV power again, so the Large Assembler on a 4A hatch (luv_hatches). The advanced computer casing needs a ZPM circuit and 4 ITBTC single wire on top. Iridium: 7 per craft (frame + 6 plates), 3.5 per casing.
    - |-
      Optical pipe (ComputerRecipes): 8 fine borosilicate glass wire + 8 silver foil + 144 mB PTFE, assembler in the CLEANROOM, 100 ticks at 7680 EU/t. Data orb (CircuitRecipes): advanced circuit board + 2 HV circuits + 4 RAM + 32 NOR chips + 64 NAND chips + 32 fine platinum wire, circuit assembler in the cleanroom, 400 ticks at 1200 EU/t (EV Circuit Assembler); it eats 2 NOR wafers worth of chips, so the luv_chips line matters. Cover screen: a cover from the cover list, Unverified recipe.
    - |-
      Sub-steps people skip: (1) the Data Bank is NOT the Research Station’s data store only: it also sits inside both recipes, so build one first and keep it; (2) the scanner research of the HPCA is the COVER SCREEN, of the Research Station the LuV Scanner (4 ZPM circuits, so ZPM); (3) 60 s per craft at 100 000 EU/t is 120 MEU per machine, size the power for it; (4) cobalt wire: cobalt comes from the rare ore residue line; (5) the HPCA needs PCB coolant as a drum, 4 B at the assembly.
    - |-
      Unverified: URD ingot route (uranium 238 + rhodium + 2 naquadah dust, mixer 150 ticks at ZPM power per MixerRecipes), optical pipe recipe, cobalt wire counts, and everything past the first Data Bank is ZPM content you should re-check against the pack quest before planning.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:high_performance_computation_array", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:luv_scanner", 1]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["gtceu:data_bank", "gtceu:data_orb", "gtceu:nano_processor_mainframe"]
      t: |-
        Data Bank first (it is in both big recipes): scan a Data Access Hatch at the EV Scanner onto a stick, then the Assembly Line (IV hatch, 6000 EU/t): computer casing, 8 LuV circuits, data orb, 64 fine cobalt, 64 fine copper, 4 optical pipes, 16 ITBTC double wire; 288 mB solder + 500 mB lubricant. 60 s. Build the structure from the multis card (computer casings, heat vents, high power casings).
    - i: ["gtceu:luv_scanner", "gtceu:data_stick", "gtceu:research_station"]
      t: |-
        LuV Scanner: LuV hull + LuV emitter + LuV sensor + 4 ZPM circuits + 2 NbTi cables (same pattern as the IV scanner one tier up, derived): the research station recipe wants its scan. It is a ZPM-circuit machine, so it waits for the quantum mainframe.
    - i: ["gtceu:high_performance_computation_array", "gtceu:luv_field_generator", "gtceu:pcb_coolant_bucket"]
      t: |-
        HPCA: the Assembly Line with a 100 000 EU/t source (LuV 4A hatch, ZPM recipe speed), 8 LuV field generators among 13 ingredient types: the line needs 7 buses (data bank, ZPM circuits, field generators, orb, screen, wire, pipes). Fluids: 1152 mB solder, 1152 mB vanadium gallium, 4 B PCB coolant. 60 s.
    - i: ["gtceu:research_station", "gtceu:luv_sensor", "gtceu:zpm_electric_motor"]
      t: |-
        Research Station: 8 buses of ingredients incl. 8 LuV sensors, 8 ZPM circuits, 2 ZPM motors (ZPM motor is a pack-table Assembly Line part, kjs luv_to_uv_components.js zpm row). 60 s at 100 000 EU/t.
    - i: ["gtceu:high_performance_computation_array", "gtceu:research_station"]
      t: |-
        Connect: HPCA computation transmitter via a computation (optical) hatch to the Research Station’s receiver hatch; items to research go in the Object Holder. The era text: 48 CWU/t sustainable without a bridge.
    - i: ["functionalstorage:oak_1", "gtceu:data_orb"]
      t: |-
        Easy to miss: data orbs are chip-hungry (32 NOR + 64 NAND chips each) and you need one per Data Bank and one per HPCA, so start the NOR and NAND chip lines early.
---
# Research: Data Bank (IV power), High Performance Computation Array and Research Station (both 100 000 EU/t, ZPM circuits)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_research` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Research Station, HPCA and data](../../plan/p12.md#research)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 6000 EU/t (scan: Data Access Hatch)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="8 LuV circuit · computer casing · data orb · 64 fine cobalt + 64 fine copper wire · 4 optical pipe · 16 ITBTC double wire · 288 mB solder · 500 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 LuV circuit · computer casing · data orb · 64 fine cobalt + 64 fine copper wire · 4 optical pipe · 16 ITBTC double wire · 288 mB solder · 500 mB lubricant</span><span class="gt-sub"><span>Nanoprocessor Mainframe</span><span>Data Orb</span><span>Fine ITBTC wire</span><span>Soldering alloy</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data Bank (gtceu:data_bank) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__data_bank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Bank</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 100 000 EU/t (scan: cover screen)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Bank (gtceu:data_bank) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_bank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Bank</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Data Bank · 4 ZPM circuit · 8 LuV field generator · data orb · cover screen · 64 URD double wire · 16 optical pipe · 1152 mB solder + molten vanadium gallium · 4 B PCB coolant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Data Bank · 4 ZPM circuit · 8 LuV field generator · data orb · cover screen · 64 URD double wire · 16 optical pipe · 1152 mB solder + molten vanadium gallium · 4 B PCB coolant</span><span class="gt-sub"><span>LuV Field Generator</span><span>Data Orb</span><span>PCB coolant</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="High Performance Computation Array (gtceu:high_performance_computation_array) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__high_performance_computation_array.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">High Performance Computation Array</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 100 000 EU/t (scan: LuV Scanner)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Bank (gtceu:data_bank) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_bank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Bank</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Data Bank · 8 LuV sensor · 8 ZPM circuit · 2 LuV field generator · 2 ZPM motor · 32 URD double wire · 32 trinium foil · 16 optical pipe · 1152 mB solder + vanadium gallium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Data Bank · 8 LuV sensor · 8 ZPM circuit · 2 LuV field generator · 2 ZPM motor · 32 URD double wire · 32 trinium foil · 16 optical pipe · 1152 mB solder + vanadium gallium</span><span class="gt-sub"><span>LuV Sensor</span><span>LuV Field Generator</span><span>ZPM Electric Motor</span><span>Trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Research Station (gtceu:research_station) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 60 s · 6000 EU/t (scan: Data Access Hatch)](#m-a1) → [Assembly Line · 60 s · 100 000 EU/t (scan: cover screen)](#m-a2) (also Assembly Line · 60 s · 6000 EU/t (scan: Data Access Hatch) → [Assembly Line · 60 s · 100 000 EU/t (scan: LuV Scanner)](#m-a3))
- [Assembly Line · 60 s · 100 000 EU/t (scan: LuV Scanner)](#m-a3)

## How to build

1. Data Bank first (it is in both big recipes): scan a Data Access Hatch at the EV Scanner onto a stick, then the Assembly Line (IV hatch, 6000 EU/t): computer casing, 8 LuV circuits, data orb, 64 fine cobalt, 64 fine copper, 4 optical pipes, 16 ITBTC double wire; 288 mB solder + 500 mB lubricant. 60 s. Build the structure from the multis card (computer casings, heat vents, high power casings). — `gtceu:data_bank`, `gtceu:data_orb`, `gtceu:nano_processor_mainframe`
2. LuV Scanner: LuV hull + LuV emitter + LuV sensor + 4 ZPM circuits + 2 NbTi cables (same pattern as the IV scanner one tier up, derived): the research station recipe wants its scan. It is a ZPM-circuit machine, so it waits for the quantum mainframe. — `gtceu:luv_scanner`, `gtceu:data_stick`, `gtceu:research_station`
3. HPCA: the Assembly Line with a 100 000 EU/t source (LuV 4A hatch, ZPM recipe speed), 8 LuV field generators among 13 ingredient types: the line needs 7 buses (data bank, ZPM circuits, field generators, orb, screen, wire, pipes). Fluids: 1152 mB solder, 1152 mB vanadium gallium, 4 B PCB coolant. 60 s. — `gtceu:high_performance_computation_array`, `gtceu:luv_field_generator`, `gtceu:pcb_coolant_bucket`
4. Research Station: 8 buses of ingredients incl. 8 LuV sensors, 8 ZPM circuits, 2 ZPM motors (ZPM motor is a pack-table Assembly Line part, kjs luv\_to\_uv\_components.js zpm row). 60 s at 100 000 EU/t. — `gtceu:research_station`, `gtceu:luv_sensor`, `gtceu:zpm_electric_motor`
5. Connect: HPCA computation transmitter via a computation (optical) hatch to the Research Station’s receiver hatch; items to research go in the Object Holder. The era text: 48 CWU/t sustainable without a bridge. — `gtceu:high_performance_computation_array`, `gtceu:research_station`
6. Easy to miss: data orbs are chip-hungry (32 NOR + 64 NAND chips each) and you need one per Data Bank and one per HPCA, so start the NOR and NAND chip lines early. — `functionalstorage:oak_1`, `gtceu:data_orb`

## Tips

- Where this sits: only the Data Bank is LuV; the HPCA and Research Station (and computation hatches, Advanced Data Access Hatch) are ZPM-gated by 4-8 ZPM circuits (ComputerRecipes, not changed by the pack, verified). Research Station research is also required by ZPM sensor, emitter and field generator (kjs tier\_data.js zpm row, CWU 4). Data Bank: computer casing + 8 LuV circuits + 1 data orb + 64 fine cobalt wire + 64 fine copper wire + 4 optical pipes + 16 ITBTC double wire, 288 mB soldering alloy + 500 mB lubricant, 1200 ticks at 6000 EU/t, scanner research of a Data Access Hatch (2400 ticks, 1920 EU/t): this one fits an IV hatch. HPCA: Data Bank + 4 ZPM circuits + 8 LuV field generators + data orb + cover screen + 64 uranium rhodium dinaquadide double wire + 16 optical pipes + 1152 mB solder + 1152 mB vanadium gallium + 4 B PCB coolant, 1200 ticks at 100 000 EU/t, scan of the cover screen. Research Station: Data Bank + 8 LuV sensors + 8 ZPM circuits + 2 LuV field generators + 2 ZPM motors + 32 URD double wire + 32 trinium foil + 16 optical pipes + 1152 mB solder + 1152 mB vanadium gallium, 1200 ticks at 100 000 EU/t, scan of a LuV Scanner (2400 ticks at 7680 EU/t).
- 100 000 EU/t is ZPM tier, so the HPCA and the Research Station need a ZPM-class energy source for the Assembly Line: a LuV 4A hatch (the quest: the 4A LuV hatch gives ZPM recipe speeds) or a ZPM hatch. Also the quest chapter puts both after the uranium rhodium dinaquadide ingot (URD) and the first ZPM circuit (quantum mainframe, which itself needs the quantum computer, the IV Circuit Assembler and crystal/quantum lines). So the order is: LuV circuits, hull, components, luv\_hatches, naquadah, URD, ZPM circuit, then these.
- HPCA: a computation provider, it needs a bridge or direct hatch and heat sinks. Component recipes (ComputerRecipes, cleanroom assembler, 200 ticks, 1 B PCB coolant each): empty = computer casing + IV circuit + data stick (7680 EU/t); heat sink = empty + 32 aluminium plates + 8 stainless screws; active cooler = advanced computer casing + 16 aluminium plates + 16 tiny stainless pipes + 8 stainless screws; computation component = empty + 4 ZPM circuits + LuV field generator (30 720 EU/t). Quest: 48 CWU/t is the max without a bridge, 36 with a bridge. The pack’s later components are in kjs systems/research.js. Unverified: how many CWU/t each component gives (read the HPCA tooltip).
- Computer casing (ComputerRecipes computer\_casing): iridium frame + 6 iridium plates + 1 LuV circuit + 32 fine cobalt wire + 32 fine copper wire + 2 vanadium gallium single wire, assembler 200 ticks at 30 720 EU/t, 2 per craft (casingsPerCraft 2): LuV power again, so the Large Assembler on a 4A hatch (luv\_hatches). The advanced computer casing needs a ZPM circuit and 4 ITBTC single wire on top. Iridium: 7 per craft (frame + 6 plates), 3.5 per casing.
- Optical pipe (ComputerRecipes): 8 fine borosilicate glass wire + 8 silver foil + 144 mB PTFE, assembler in the CLEANROOM, 100 ticks at 7680 EU/t. Data orb (CircuitRecipes): advanced circuit board + 2 HV circuits + 4 RAM + 32 NOR chips + 64 NAND chips + 32 fine platinum wire, circuit assembler in the cleanroom, 400 ticks at 1200 EU/t (EV Circuit Assembler); it eats 2 NOR wafers worth of chips, so the luv\_chips line matters. Cover screen: a cover from the cover list, Unverified recipe.
- Sub-steps people skip: (1) the Data Bank is NOT the Research Station’s data store only: it also sits inside both recipes, so build one first and keep it; (2) the scanner research of the HPCA is the COVER SCREEN, of the Research Station the LuV Scanner (4 ZPM circuits, so ZPM); (3) 60 s per craft at 100 000 EU/t is 120 MEU per machine, size the power for it; (4) cobalt wire: cobalt comes from the rare ore residue line; (5) the HPCA needs PCB coolant as a drum, 4 B at the assembly.
- **Unverified** URD ingot route (uranium 238 + rhodium + 2 naquadah dust, mixer 150 ticks at ZPM power per MixerRecipes), optical pipe recipe, cobalt wire counts, and everything past the first Data Bank is ZPM content you should re-check against the pack quest before planning.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:high_performance_computation_array` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:luv_scanner` | 1 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:data_bank`, `gtceu:high_performance_computation_array`, `gtceu:research_station`
