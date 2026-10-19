---
kind: chain
id: luv_lcaf
order: 1260
data:
  t: |-
    What LuV circuits unlock first: IV Circuit Assembler (2 LuV circuits), IV Parallel Hatch (4), Large Circuit Assembling Facility
  inf: true
  "n":
    - [nm, "Nanoprocessor Mainframe (LuV circuit) · 2 + 4", i, "gtceu:nano_processor_mainframe"]
    - - p1
      - IV robot arm · IV emitter · 2 IV conveyor · IV hull · 2 platinum cable
      - g
      - functionalstorage:oak_1
      - - [IV Robot Arm, "gtceu:iv_robot_arm"]
        - [IV Emitter, "gtceu:iv_emitter"]
        - [IV Conveyor Module, "gtceu:iv_conveyor_module"]
        - [IV Machine Hull, "gtceu:iv_machine_hull"]
        - [Platinum single cable, "gtceu:platinum_single_cable"]
    - [ic, "IV Circuit Assembler (crafting table)", x, "gtceu:iv_circuit_assembler"]
    - - p2
      - IV sensor · IV emitter · IV hull · 2 platinum double cable
      - g
      - functionalstorage:oak_1
      - - [IV Sensor, "gtceu:iv_sensor"]
        - [IV Emitter, "gtceu:iv_emitter"]
        - [IV Machine Hull, "gtceu:iv_machine_hull"]
        - [Platinum double cable, "gtceu:platinum_double_cable"]
    - [ph, "IV Parallel Hatch · 4x (crafting table)", x, "gtceu:iv_parallel_hatch"]
    - - p3
      - |-
        2 IV robot arm · 2 IV conveyor · 2 IV circuit · 2 platinum cable
      - g
      - functionalstorage:oak_1
      - - [IV Robot Arm, "gtceu:iv_robot_arm"]
        - [IV Conveyor Module, "gtceu:iv_conveyor_module"]
        - ["Mainframe (IV circuit)", "gtceu:micro_processor_mainframe"]
    - - cs
      - |-
        65 large scale assembler casing · 10 grating · 6 tungstensteel pipe casing · 4 tempered glass
      - g
      - functionalstorage:oak_1
      - - [Large scale assembler casing, "gtceu:large_scale_assembler_casing"]
        - [Tungstensteel pipe casing, "gtceu:tungstensteel_pipe_casing"]
        - [Assembly line grating, "gtceu:assembly_line_grating"]
    - [lc, "Large Circuit Assembling Facility (crafting table)", m, "gtceu:large_circuit_assembler"]
    - [eh, "LuV Energy Input Hatch · exactly 1", m, "gtceu:luv_energy_input_hatch"]
    - [ou, "Circuit recipes up to LuV power, parallel", o, "gtceu:nano_processor_mainframe"]
  e:
    - [nm, ic, "2"]
    - [p1, ic]
    - [nm, ph, "4"]
    - [p2, ph]
    - [ic, lc, "1"]
    - [p3, lc]
    - [cs, lc]
    - [eh, lc]
    - [ph, lc, parallel]
    - [lc, ou]
  tips:
    - |-
      Recipes (verified in the extracted recipes and GCYMRecipes; the pack does not touch them): IV Circuit Assembler = IV robot arm + 2 LuV circuits + IV emitter + 2 IV conveyor modules + IV hull + 2 platinum single cables, crafting table. IV Parallel Hatch (GCYMRecipes parallel_hatch_mk1) = IV sensor + IV emitter + 4 LuV circuits + IV hull + 2 platinum DOUBLE cables, crafting table; it runs up to 4 recipes in parallel (the tooltip in the mod jar says 4; the pack quest subtitle says 8x, the jar wins). LuV Parallel Hatch (16x) = LuV sensor + LuV emitter + 4 ZPM circuits + LuV hull + 2 niobium titanium double cables, so it is a ZPM-circuit item; ZPM one is 64x.
    - |-
      So a single LuV circuit unlocks 2 + 4 = 6 circuits worth of use: build 6 nanoprocessor mainframes before you plan anything else. The quest says the IV Circuit Assembler is the last circuit assembler you will make; it is also what the quantum recipes (2400 EU/t) need and what the Large Circuit Assembling Facility is crafted from.
    - |-
      Large Circuit Assembling Facility (GCYMMachines, large_circuit_assembler): crafting table, 2 IV robot arms + 2 IV conveyor modules + 2 IV circuits + an IV Circuit Assembler + 2 platinum cables. It runs circuit assembler recipes, accepts a Parallel Hatch and batch mode, and takes exactly ONE energy hatch of any tier, so with a LuV hatch every LuV-power circuit recipe (crystal assembly at 9600 EU/t, advanced SoC recipes) runs. Structure: at least 55 Large Scale Assembler Casings (65 with hatches), 10 assembly line gratings, 6 tungstensteel pipe casings, 4 tempered glass. Casing: 6 Stellite-100 plates + 1 tungsten frame, assembler circuit 6, 50 ticks, 16 EU/t, 2 per craft, so about 168 plates. Unverified: where Stellite-100 comes from in this pack (alloy dust; check the mixer in EMI).
    - |-
      Use: put the nano line (luv_circuits) on one LCAF with an IV parallel hatch (4x). The nano recipes carry the cleanroom tag, so plan the LCAF inside a Cleanroom (Unverified: the GCYM multi has no built-in clean air, check the controller tooltip; the footprint is 7 x 5 x 3 plus the controller wall). The four single EV Circuit Assemblers of luv_circuits can then be retired: one LCAF with the 4x parallel hatch does all four stages in turn.
    - |-
      The LuV Energy Input Hatch needs LuV voltage to build (see luv_hatches); until then the LCAF runs on an IV or EV hatch and recipes above that tier simply do not start. The pack quest chapter describes it this way: the LuV hatch on the LCAF gives LuV circuit assembler recipes at once, the 4A one ZPM speeds, the 16A one UV speeds.
    - |-
      Order and tiers: the Large Assembling Factory (large_assembler) is an IV craft with no LuV part (2 IV robot arms + 2 IV conveyors + 2 IV circuits + an IV Assembler + 2 platinum cables) and takes exactly one energy hatch; the IV 16A hatch exists (pack assembler recipe, see iv_hatches). Only the 4x parallel needs 4 LuV circuits, so a Large ME Assembler or Large Assembler with 4x parallel comes after the nano line. The real recipe order is IV hull, LuV circuits, IV Circuit Assembler, LCAF: quests do not lock recipes, and the Large Machines quest depends only on the IV machine hull quest.
    - |-
      Other IV machines that already need LuV circuits: Extreme Combustion Engine (1), Thermal Decomposition Array / super_pyrolyse (2 LuV circuits + pyrolyse oven + 2 IV pistons + 2 IV pumps), super cracker (2 LuV circuits + HSS-G coil). The Tree Synthesizer is IV only (2 IV circuits, IV motor, greenhouse, 2 IV conveyors, IV pump, IV field generator). Large Extractor (IV, extractor + canner) runs the AE2 co-processors, which are canner recipes in this pack.
    - |-
      Sub-steps people skip: (1) the first IV circuit assembler is a crafting-table item, not an assembler recipe; (2) 2 LuV circuits there, 4 in the parallel hatch: do not spend them on anything else; (3) tempered glass is the stone barrel recipe (glass + 1 B lava), already used in the HV chain; (4) the LCAF has no recipe viewer shortcut: copy the grating, pipe casing and glass counts from the multis card.
  b:
    - ["gtceu:large_circuit_assembler", 1]
    - ["gtceu:iv_circuit_assembler", 1]
    - ["gtceu:iv_parallel_hatch", 1]
    - ["gtceu:luv_energy_input_hatch", 1]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:lv_assembler", 2]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 5]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 1]
  how:
    - i: ["gtceu:nano_processor_mainframe", "gtceu:iv_robot_arm", "gtceu:iv_emitter"]
      t: |-
        Stock first: 6 Nanoprocessor Mainframes, 3 IV robot arms, 2 IV emitters, 1 IV sensor, 2 IV hulls (the iv_components chain), 4 IV conveyor modules, 2 more IV circuits, 4 platinum single cables and 2 platinum double cables. Drawers for each, then craft by hand.
    - i: ["gtceu:iv_circuit_assembler", "gtceu:nano_processor_mainframe"]
      t: |-
        IV Circuit Assembler: crafting table, RIE / CHC / WIW: robot arm top-left, 2 LuV circuits (I) in the top-middle and bottom-middle, emitter top-right, 2 conveyors left and right of the hull, platinum cables bottom corners. One machine is all you need; it is also the base item of the LCAF.
    - i: ["gtceu:iv_parallel_hatch", "gtceu:iv_sensor", "gtceu:platinum_double_cable"]
      t: |-
        IV Parallel Hatch: crafting table SZE / ZHZ / CZC: IV sensor and emitter on top, LuV circuits in the plus shape around the hull, 2 platinum double cables on the bottom corners. It is a multiblock hatch: it goes in a free slot of an LCAF or any Large multi that lists it.
    - i: ["gtceu:large_scale_assembler_casing", "gtceu:assembly_line_grating", "gtceu:tungstensteel_pipe_casing"]
      t: |-
        LCAF structure: casing 6 Stellite-100 plates + tungsten frame (2 per craft, circuit 6), 6 pipe casings (4 tungsten steel plates + 4 normal pipes + frame), 10 gratings (IV assembler recipe from steel), 4 tempered glass. Hatches replace casings: 1 energy hatch, the item buses and fluid hatches the recipes need, maintenance.
    - i: ["gtceu:large_circuit_assembler", "gtceu:iv_circuit_assembler"]
      t: |-
        LCAF controller: crafting table RKR / CXC / MKM with 2 IV robot arms, 2 IV circuits, the IV Circuit Assembler in the centre, 2 conveyors, 2 platinum cables. Set the Parallel Hatch in a free spot, one dedicated input bus per part drawer as in the IV chain.
    - i: ["gtceu:cleanroom", "gtceu:large_circuit_assembler"]
      t: |-
        Cleanroom: size the room of the luv_circuits chain for the LCAF (7 x 5 x 3 footprint) from the start, or build a second one; the machine must stand inside to run the cleanroom-tagged recipes (Unverified for the GCYM multi).
    - i: ["gtceu:luv_energy_input_hatch", "gtceu:large_circuit_assembler"]
      t: |-
        Easy to miss: the LCAF takes exactly one energy hatch. Start with the IV hatch you have, swap to the LuV one when luv_hatches is done; do not put two.
---
# What LuV circuits unlock first: IV Circuit Assembler (2 LuV circuits), IV Parallel Hatch (4), Large Circuit Assembling Facility

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_lcaf` · **Tags:** Infinite source

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [LuV circuit (Nanoprocessor Mainframe)](../../plan/p11.md#luvcirc)

**Tips:** 8

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lc">
<div class="gt-head"><span class="gt-mname">Large Circuit Assembling Facility (crafting table)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Circuit Assembler (crafting table) (gtceu:iv_circuit_assembler) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Circuit Assembler</span><span class="gt-note">IV Circuit Assembler (crafting table)</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="2 IV robot arm · 2 IV conveyor · 2 IV circuit · 2 platinum cable (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 IV robot arm · 2 IV conveyor · 2 IV circuit · 2 platinum cable</span><span class="gt-sub"><span>IV Robot Arm</span><span>IV Conveyor Module</span><span>Mainframe (IV circuit)</span></span></span><span class="gt-slot gt-group" title="65 large scale assembler casing · 10 grating · 6 tungstensteel pipe casing · 4 tempered glass (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">65 large scale assembler casing · 10 grating · 6 tungstensteel pipe casing · 4 tempered glass</span><span class="gt-sub"><span>Large scale assembler casing</span><span>Tungstensteel pipe casing</span><span>Assembly line grating</span></span></span><a class="gt-slot gt-mach" href="#m-eh" title="LuV Energy Input Hatch · exactly 1 (gtceu:luv_energy_input_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__luv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Energy Input Hatch</span><span class="gt-note">LuV Energy Input Hatch · exactly 1</span></a><span class="gt-slot" title="IV Parallel Hatch · 4x (crafting table) (gtceu:iv_parallel_hatch) - parallel"><img class="gt-ico" src="../../assets/icons/gtceu__iv_parallel_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Parallel Hatch</span><span class="gt-note">IV Parallel Hatch · 4x (crafting table)</span><b class="gt-q">parallel</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Circuit recipes up to LuV power, parallel (gtceu:nano_processor_mainframe)"><img class="gt-ico" src="../../assets/icons/gtceu__nano_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano Processor Mainframe</span><span class="gt-note">Circuit recipes up to LuV power, parallel</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_circuit_assembler</code></div>
</div>
<div class="gt-panel t-luv" id="m-eh">
<div class="gt-head"><span class="gt-mname">LuV Energy Input Hatch · exactly 1</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-lc" title="Large Circuit Assembling Facility (crafting table) (gtceu:large_circuit_assembler)"><img class="gt-ico" src="../../assets/icons/gtceu__large_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Circuit Assembler</span><span class="gt-note">Large Circuit Assembling Facility (crafting table)</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:luv_energy_input_hatch</code></div>
</div>
</div>

## Flow

- [LuV Energy Input Hatch · exactly 1](#m-eh) → [Large Circuit Assembling Facility (crafting table)](#m-lc)

### Direct steps

- Nanoprocessor Mainframe (LuV circuit) · 2 + 4 → IV Circuit Assembler (crafting table) (2)
- IV robot arm · IV emitter · 2 IV conveyor · IV hull · 2 platinum cable → IV Circuit Assembler (crafting table)
- Nanoprocessor Mainframe (LuV circuit) · 2 + 4 → IV Parallel Hatch · 4x (crafting table) (4)
- IV sensor · IV emitter · IV hull · 2 platinum double cable → IV Parallel Hatch · 4x (crafting table)

## How to build

1. Stock first: 6 Nanoprocessor Mainframes, 3 IV robot arms, 2 IV emitters, 1 IV sensor, 2 IV hulls (the iv\_components chain), 4 IV conveyor modules, 2 more IV circuits, 4 platinum single cables and 2 platinum double cables. Drawers for each, then craft by hand. — `gtceu:nano_processor_mainframe`, `gtceu:iv_robot_arm`, `gtceu:iv_emitter`
2. IV Circuit Assembler: crafting table, RIE / CHC / WIW: robot arm top-left, 2 LuV circuits (I) in the top-middle and bottom-middle, emitter top-right, 2 conveyors left and right of the hull, platinum cables bottom corners. One machine is all you need; it is also the base item of the LCAF. — `gtceu:iv_circuit_assembler`, `gtceu:nano_processor_mainframe`
3. IV Parallel Hatch: crafting table SZE / ZHZ / CZC: IV sensor and emitter on top, LuV circuits in the plus shape around the hull, 2 platinum double cables on the bottom corners. It is a multiblock hatch: it goes in a free slot of an LCAF or any Large multi that lists it. — `gtceu:iv_parallel_hatch`, `gtceu:iv_sensor`, `gtceu:platinum_double_cable`
4. LCAF structure: casing 6 Stellite-100 plates + tungsten frame (2 per craft, circuit 6), 6 pipe casings (4 tungsten steel plates + 4 normal pipes + frame), 10 gratings (IV assembler recipe from steel), 4 tempered glass. Hatches replace casings: 1 energy hatch, the item buses and fluid hatches the recipes need, maintenance. — `gtceu:large_scale_assembler_casing`, `gtceu:assembly_line_grating`, `gtceu:tungstensteel_pipe_casing`
5. LCAF controller: crafting table RKR / CXC / MKM with 2 IV robot arms, 2 IV circuits, the IV Circuit Assembler in the centre, 2 conveyors, 2 platinum cables. Set the Parallel Hatch in a free spot, one dedicated input bus per part drawer as in the IV chain. — `gtceu:large_circuit_assembler`, `gtceu:iv_circuit_assembler`
6. Cleanroom: size the room of the luv\_circuits chain for the LCAF (7 x 5 x 3 footprint) from the start, or build a second one; the machine must stand inside to run the cleanroom-tagged recipes (Unverified for the GCYM multi). — `gtceu:cleanroom`, `gtceu:large_circuit_assembler`
7. Easy to miss: the LCAF takes exactly one energy hatch. Start with the IV hatch you have, swap to the LuV one when luv\_hatches is done; do not put two. — `gtceu:luv_energy_input_hatch`, `gtceu:large_circuit_assembler`

## Tips

- Recipes (verified in the extracted recipes and GCYMRecipes; the pack does not touch them): IV Circuit Assembler = IV robot arm + 2 LuV circuits + IV emitter + 2 IV conveyor modules + IV hull + 2 platinum single cables, crafting table. IV Parallel Hatch (GCYMRecipes parallel\_hatch\_mk1) = IV sensor + IV emitter + 4 LuV circuits + IV hull + 2 platinum DOUBLE cables, crafting table; it runs up to 4 recipes in parallel (the tooltip in the mod jar says 4; the pack quest subtitle says 8x, the jar wins). LuV Parallel Hatch (16x) = LuV sensor + LuV emitter + 4 ZPM circuits + LuV hull + 2 niobium titanium double cables, so it is a ZPM-circuit item; ZPM one is 64x.
- So a single LuV circuit unlocks 2 + 4 = 6 circuits worth of use: build 6 nanoprocessor mainframes before you plan anything else. The quest says the IV Circuit Assembler is the last circuit assembler you will make; it is also what the quantum recipes (2400 EU/t) need and what the Large Circuit Assembling Facility is crafted from.
- Large Circuit Assembling Facility (GCYMMachines, large\_circuit\_assembler): crafting table, 2 IV robot arms + 2 IV conveyor modules + 2 IV circuits + an IV Circuit Assembler + 2 platinum cables. It runs circuit assembler recipes, accepts a Parallel Hatch and batch mode, and takes exactly ONE energy hatch of any tier, so with a LuV hatch every LuV-power circuit recipe (crystal assembly at 9600 EU/t, advanced SoC recipes) runs. Structure: at least 55 Large Scale Assembler Casings (65 with hatches), 10 assembly line gratings, 6 tungstensteel pipe casings, 4 tempered glass. Casing: 6 Stellite-100 plates + 1 tungsten frame, assembler circuit 6, 50 ticks, 16 EU/t, 2 per craft, so about 168 plates. Unverified: where Stellite-100 comes from in this pack (alloy dust; check the mixer in EMI).
- Use: put the nano line (luv\_circuits) on one LCAF with an IV parallel hatch (4x). The nano recipes carry the cleanroom tag, so plan the LCAF inside a Cleanroom (Unverified: the GCYM multi has no built-in clean air, check the controller tooltip; the footprint is 7 x 5 x 3 plus the controller wall). The four single EV Circuit Assemblers of luv\_circuits can then be retired: one LCAF with the 4x parallel hatch does all four stages in turn.
- The LuV Energy Input Hatch needs LuV voltage to build (see luv\_hatches); until then the LCAF runs on an IV or EV hatch and recipes above that tier simply do not start. The pack quest chapter describes it this way: the LuV hatch on the LCAF gives LuV circuit assembler recipes at once, the 4A one ZPM speeds, the 16A one UV speeds.
- Order and tiers: the Large Assembling Factory (large\_assembler) is an IV craft with no LuV part (2 IV robot arms + 2 IV conveyors + 2 IV circuits + an IV Assembler + 2 platinum cables) and takes exactly one energy hatch; the IV 16A hatch exists (pack assembler recipe, see iv\_hatches). Only the 4x parallel needs 4 LuV circuits, so a Large ME Assembler or Large Assembler with 4x parallel comes after the nano line. The real recipe order is IV hull, LuV circuits, IV Circuit Assembler, LCAF: quests do not lock recipes, and the Large Machines quest depends only on the IV machine hull quest.
- Other IV machines that already need LuV circuits: Extreme Combustion Engine (1), Thermal Decomposition Array / super\_pyrolyse (2 LuV circuits + pyrolyse oven + 2 IV pistons + 2 IV pumps), super cracker (2 LuV circuits + HSS-G coil). The Tree Synthesizer is IV only (2 IV circuits, IV motor, greenhouse, 2 IV conveyors, IV pump, IV field generator). Large Extractor (IV, extractor + canner) runs the AE2 co-processors, which are canner recipes in this pack.
- Sub-steps people skip: (1) the first IV circuit assembler is a crafting-table item, not an assembler recipe; (2) 2 LuV circuits there, 4 in the parallel hatch: do not spend them on anything else; (3) tempered glass is the stone barrel recipe (glass + 1 B lava), already used in the HV chain; (4) the LCAF has no recipe viewer shortcut: copy the grating, pipe casing and glass counts from the multis card.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_circuit_assembler` | 1 |
| `gtceu:iv_circuit_assembler` | 1 |
| `gtceu:iv_parallel_hatch` | 1 |
| `gtceu:luv_energy_input_hatch` | 1 |
| `gtceu:cleanroom` | 1 |
| `gtceu:lv_assembler` | 2 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 5 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 1 |

## Needs / Feeds

- **Needs:** [LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)](luv_circuits.md)
- **Main source for:** `gtceu:iv_circuit_assembler`, `gtceu:iv_parallel_hatch`, `gtceu:large_circuit_assembler`
