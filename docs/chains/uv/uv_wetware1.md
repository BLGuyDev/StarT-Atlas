---
kind: chain
id: uv_wetware1
order: 1570
data:
  t: |-
    Wetware circuits 1: wetware board → printed board → neuro processing unit → wetware processor (the LuV circuit of the wetware line)
  inf: true
  "n":
    - - g1
      - |-
        16 multilayer fiber board · petri dish · LuV pump · LuV sensor · 2 IV circuit · 16 osmiridium foil · 4 B sterile medium
      - g
      - functionalstorage:oak_1
      - - [Multilayer fiber board, "gtceu:multilayer_fiber_reinforced_circuit_board"]
        - [Petri dish, "gtceu:petri_dish"]
        - [LuV pump, "gtceu:luv_electric_pump"]
        - [LuV sensor, "gtceu:luv_sensor"]
        - [Osmiridium foil, "gtceu:osmiridium_foil"]
        - [Sterile medium, "gtceu:sterilized_growth_medium_bucket"]
    - [a1, "LuV Circuit Assembler · 60 s · 30 720 EU/t · Cleanroom", m, "gtceu:luv_circuit_assembler"]
    - [wb, Wetware circuit board x16, x, "gtceu:wetware_circuit_board"]
    - - g2
      - |-
        16 NbTi foil · 5 B iron III chloride (or 10 B sodium persulfate)
      - g
      - functionalstorage:oak_1
      - [[NbTi foil, "gtceu:niobium_titanium_foil"], [Iron III chloride, "gtceu:iron_iii_chloride_bucket"]]
    - [rx, "HV Chemical Reactor · 90 s · 480 EU/t · Cleanroom", m, "gtceu:hv_chemical_reactor"]
    - [pcb, Wetware printed circuit board, x, "gtceu:wetware_printed_circuit_board"]
    - - g3
      - |-
        16 stem cells · 8 small PBI pipe · 8 electrum plate · 16 silicone rubber foil · 8 HSS-E bolt · 250 mB sterile medium
      - g
      - functionalstorage:oak_1
      - - [Stem cells, "gtceu:stem_cells"]
        - [Small PBI pipe, "gtceu:polybenzimidazole_small_fluid_pipe"]
        - [Electrum plate, "gtceu:electrum_plate"]
        - [Silicone rubber foil, "gtceu:silicone_rubber_foil"]
        - [HSS-E bolt, "gtceu:hsse_bolt"]
    - [a2, "ZPM Circuit Assembler · 30 s · 80 000 EU/t · Cleanroom", m, "gtceu:zpm_circuit_assembler"]
    - [np, Neuro processing unit, x, "gtceu:neuro_processing_unit"]
    - - g4
      - Crystal CPU · nano CPU chip · 4 living capacitor · 4 living transistor · 8 fine YBCO wire
      - g
      - functionalstorage:oak_1
      - - [Crystal CPU, "gtceu:crystal_cpu"]
        - [Nano CPU chip, "gtceu:nano_cpu_chip"]
        - [Living capacitor, "kubejs:living_smd_capacitor"]
        - [Living transistor, "kubejs:living_smd_transistor"]
        - [Fine YBCO wire, "gtceu:fine_yttrium_barium_cuprate_wire"]
    - [a3, "ZPM Circuit Assembler · 5 s · 38 400 EU/t · Cleanroom", m, "gtceu:zpm_circuit_assembler"]
    - [wp, "Wetware processor x2 (LuV circuit)", o, "gtceu:wetware_processor"]
  e:
    - [g1, a1, "1"]
    - [a1, wb, "16 / 60 s"]
    - [wb, rx, "1"]
    - [g2, rx, "1"]
    - [rx, pcb, "1 / 90 s"]
    - [pcb, a2, "1"]
    - [g3, a2, "1"]
    - [a2, np, "1 / 30 s"]
    - [np, a3, "1"]
    - [g4, a3, "1"]
    - [a3, wp, "2 / 5 s"]
  tips:
    - |-
      Why this chain: wetware circuits are the pack’s route to the UV circuit (wetware computer) and the UHV circuit (wetware mainframe); the processor and the assembly are the LuV and ZPM steps (gtceu circuits tags: luv = wetware processor, zpm = wetware assembly, uv = wetware computer + crystal mainframe, uhv = wetware mainframe). Only the ZPM-era Quantum / crystal route is shorter, the wetware line is the one that feeds the UHV circuit.
    - |-
      Wetware circuit board (kjs circuits.js, the GT recipe gtceu:circuit_assembler/wetware_board is removed): circuit assembler in a normal Cleanroom, 1200 ticks at VA[LuV] = 30 720 EU/t, 16 multilayer fiber-reinforced circuit boards + 1 petri dish + 1 LuV electric pump + 1 LuV sensor + 2 IV circuits + 16 osmiridium foil + 4 B sterilized growth medium → 16 wetware circuit boards. Petri dish: GT fluid solidifier, 1/8 ingot of PBI (2 dishes) or 1/4 ingot PTFE (1 dish).
    - |-
      Printed board (kjs circuit_etching.js): chemical reactor in a Cleanroom, 1800 ticks (90 s) at 480 EU/t, 1 wetware circuit board + 16 niobium titanium foil + 5 B iron III chloride (or 10 B sodium persulfate) → 1 wetware printed circuit board. The script first adds a cupric chloride version (2.5 B) and then removes everything with this output before re-adding the two above, so use iron III chloride or persulfate (Unverified whether the cupric version survives).
    - |-
      Neuro processing unit (gtsrc CircuitRecipes neuro_processor, not touched by the pack): circuit assembler, Cleanroom, 600 ticks at 80 000 EU/t, 1 wetware printed circuit board + 16 stem cells + 8 small PBI fluid pipes + 8 electrum plates + 16 silicone rubber foil + 8 HSS-E bolts + 250 mB sterilized growth medium. 80 000 EU/t is above LuV (32 768), so this needs a ZPM circuit assembler (131 072 EU/t).
    - |-
      Wetware processor, two recipes: (a) pack (circuits.js): circuit assembler, 100 ticks at 38 400 EU/t, 1 neuro unit + 1 crystal CPU + 1 nano CPU chip + 4 living capacitors + 4 living transistors + 8 fine YBCO wire → 2 processors; (b) GT (CircuitRecipes wetware_processor_luv): 200 ticks, same neuro unit + crystal CPU + nano CPU but 8 advanced SMD capacitors + 8 advanced SMD transistors + 8 fine YBCO wire, output 1 or 2 (harder-circuit config); also a SoC route: neuro unit + highly advanced SoC + 8 fine YBCO wire + 8 naquadah bolts, 100 ticks at 150 000 EU/t. 38 400 EU/t is above 32 768 EU/t, so a ZPM circuit assembler is needed again.
    - |-
      Sub-steps people skip: (1) the board recipe consumes ONE petri dish, LuV pump and LuV sensor per 16 boards, keep them in drawers with Keep Exact 1; (2) only the sterile bio line (uv_bio1/uv_bio2) is Sterile Cleanroom; this chain runs in a NORMAL cleanroom, a sterile cleanroom would reject it; (3) an unprocessed wetware circuit board and a wetware PRINTED board are different items; (4) every neuro unit eats a whole printed board, a run of 16 boards leaves 15 spare for the assembly, computer and mainframe recipes (they each take one).
    - |-
      Unverified: whether a LuV circuit assembler can run the 38 400 EU/t recipes with an overclock cap (the recipe EU is above LuV voltage, so it will not start), the cleanroom size, and the output count of the GT processor recipe in this pack config.
  b:
    - ["gtceu:luv_circuit_assembler", 1]
    - ["gtceu:zpm_circuit_assembler", 2]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:multilayer_fiber_reinforced_circuit_board
        - gtceu:petri_dish
        - gtceu:osmiridium_foil
      t: |-
        Drawers first, one per input: multilayer fiber boards, petri dishes, LuV pumps, LuV sensors, IV circuits, osmiridium foil, niobium titanium foil, stem cells, small PBI pipes, electrum plates, silicone rubber foil, HSS-E bolts, crystal CPUs, nano CPU chips, living capacitors, living transistors, fine YBCO wire. Drums: sterile medium, iron III chloride. Circuit assemblers are inside the normal cleanroom.
    - i: ["gtceu:luv_circuit_assembler", "gtceu:wetware_circuit_board"]
      t: |-
        Board assembler (LuV Circuit Assembler): sixteen boards per run, one run per minute. Output drawer Keep Exact 16 so the reactor always has a full stack.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:wetware_printed_circuit_board"]
      t: |-
        Etching reactor: 1 board + 16 NbTi foil + 5 B iron III chloride → 1 printed board, 90 s. One reactor makes 40 printed boards per hour: build two if the chain feeds both the processors and the computer / mainframe lines.
    - i: ["gtceu:zpm_circuit_assembler", "gtceu:neuro_processing_unit"]
      t: |-
        Neuro unit assembler: its own ZPM circuit assembler, 80 000 EU/t for 30 s. Stem cells by router (Keep Exact 16), medium by Pipez.
    - i: ["gtceu:zpm_circuit_assembler", "gtceu:wetware_processor"]
      t: |-
        Processor assembler (second ZPM circuit assembler): neuro unit, crystal CPU, nano CPU chip, living SMDs, YBCO wire → 2 wetware processors in 5 s at 38 400 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:wetware_processor"]
      t: |-
        Output drawer Keep Exact 16. Remember: LuV circuits are used elsewhere too (robot arm, hatches), do not hoard them.
---
# Wetware circuits 1: wetware board → printed board → neuro processing unit → wetware processor (the LuV circuit of the wetware line)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_wetware1` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Wetware circuits (UV and UHV circuit)](../../plan/p14.md#wetware)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-luv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LuV Circuit Assembler · 60 s · 30 720 EU/t · Cleanroom</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="16 multilayer fiber board · petri dish · LuV pump · LuV sensor · 2 IV circuit · 16 osmiridium foil · 4 B sterile medium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 multilayer fiber board · petri dish · LuV pump · LuV sensor · 2 IV circuit · 16 osmiridium foil · 4 B sterile medium</span><span class="gt-sub"><span>Multilayer fiber board</span><span>Petri dish</span><span>LuV pump</span><span>LuV sensor</span><span>Osmiridium foil</span><span>Sterile medium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Wetware circuit board x16 (gtceu:wetware_circuit_board) - 16 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Circuit Board</span><span class="gt-note">Wetware circuit board x16</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_circuit_assembler</code></div>
</div>
<div class="gt-panel t-hv" id="m-rx">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 90 s · 480 EU/t · Cleanroom</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wetware circuit board x16 (gtceu:wetware_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Circuit Board</span><span class="gt-note">Wetware circuit board x16</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="16 NbTi foil · 5 B iron III chloride (or 10 B sodium persulfate) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 NbTi foil · 5 B iron III chloride (or 10 B sodium persulfate)</span><span class="gt-sub"><span>NbTi foil</span><span>Iron III chloride</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Wetware printed circuit board (gtceu:wetware_printed_circuit_board) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Printed Circuit Board</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a2">
<div class="gt-head"><span class="gt-mname">ZPM Circuit Assembler · 30 s · 80 000 EU/t · Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wetware printed circuit board (gtceu:wetware_printed_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Printed Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="16 stem cells · 8 small PBI pipe · 8 electrum plate · 16 silicone rubber foil · 8 HSS-E bolt · 250 mB sterile medium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 stem cells · 8 small PBI pipe · 8 electrum plate · 16 silicone rubber foil · 8 HSS-E bolt · 250 mB sterile medium</span><span class="gt-sub"><span>Stem cells</span><span>Small PBI pipe</span><span>Electrum plate</span><span>Silicone rubber foil</span><span>HSS-E bolt</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Neuro processing unit (gtceu:neuro_processing_unit) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__neuro_processing_unit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neuro Processing Unit</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a3">
<div class="gt-head"><span class="gt-mname">ZPM Circuit Assembler · 5 s · 38 400 EU/t · Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Neuro processing unit (gtceu:neuro_processing_unit) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__neuro_processing_unit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neuro Processing Unit</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Crystal CPU · nano CPU chip · 4 living capacitor · 4 living transistor · 8 fine YBCO wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Crystal CPU · nano CPU chip · 4 living capacitor · 4 living transistor · 8 fine YBCO wire</span><span class="gt-sub"><span>Crystal CPU</span><span>Nano CPU chip</span><span>Living capacitor</span><span>Living transistor</span><span>Fine YBCO wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Wetware processor x2 (LuV circuit) (gtceu:wetware_processor) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_processor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Processor</span><span class="gt-note">Wetware processor x2 (LuV circuit)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
</div>

## Flow

- [LuV Circuit Assembler · 60 s · 30 720 EU/t · Cleanroom](#m-a1) → [HV Chemical Reactor · 90 s · 480 EU/t · Cleanroom](#m-rx) → [ZPM Circuit Assembler · 30 s · 80 000 EU/t · Cleanroom](#m-a2) → [ZPM Circuit Assembler · 5 s · 38 400 EU/t · Cleanroom](#m-a3)

## How to build

1. Drawers first, one per input: multilayer fiber boards, petri dishes, LuV pumps, LuV sensors, IV circuits, osmiridium foil, niobium titanium foil, stem cells, small PBI pipes, electrum plates, silicone rubber foil, HSS-E bolts, crystal CPUs, nano CPU chips, living capacitors, living transistors, fine YBCO wire. Drums: sterile medium, iron III chloride. Circuit assemblers are inside the normal cleanroom. — `functionalstorage:oak_1`, `gtceu:multilayer_fiber_reinforced_circuit_board`, `gtceu:petri_dish`, `gtceu:osmiridium_foil`
2. Board assembler (LuV Circuit Assembler): sixteen boards per run, one run per minute. Output drawer Keep Exact 16 so the reactor always has a full stack. — `gtceu:luv_circuit_assembler`, `gtceu:wetware_circuit_board`
3. Etching reactor: 1 board + 16 NbTi foil + 5 B iron III chloride → 1 printed board, 90 s. One reactor makes 40 printed boards per hour: build two if the chain feeds both the processors and the computer / mainframe lines. — `gtceu:hv_chemical_reactor`, `gtceu:wetware_printed_circuit_board`
4. Neuro unit assembler: its own ZPM circuit assembler, 80 000 EU/t for 30 s. Stem cells by router (Keep Exact 16), medium by Pipez. — `gtceu:zpm_circuit_assembler`, `gtceu:neuro_processing_unit`
5. Processor assembler (second ZPM circuit assembler): neuro unit, crystal CPU, nano CPU chip, living SMDs, YBCO wire → 2 wetware processors in 5 s at 38 400 EU/t. — `gtceu:zpm_circuit_assembler`, `gtceu:wetware_processor`
6. Output drawer Keep Exact 16. Remember: LuV circuits are used elsewhere too (robot arm, hatches), do not hoard them. — `functionalstorage:oak_1`, `gtceu:wetware_processor`

## Tips

- Why this chain: wetware circuits are the pack’s route to the UV circuit (wetware computer) and the UHV circuit (wetware mainframe); the processor and the assembly are the LuV and ZPM steps (gtceu circuits tags: luv = wetware processor, zpm = wetware assembly, uv = wetware computer + crystal mainframe, uhv = wetware mainframe). Only the ZPM-era Quantum / crystal route is shorter, the wetware line is the one that feeds the UHV circuit.
- Wetware circuit board (kjs circuits.js, the GT recipe gtceu:circuit\_assembler/wetware\_board is removed): circuit assembler in a normal Cleanroom, 1200 ticks at VA\[LuV\] = 30 720 EU/t, 16 multilayer fiber-reinforced circuit boards + 1 petri dish + 1 LuV electric pump + 1 LuV sensor + 2 IV circuits + 16 osmiridium foil + 4 B sterilized growth medium → 16 wetware circuit boards. Petri dish: GT fluid solidifier, 1/8 ingot of PBI (2 dishes) or 1/4 ingot PTFE (1 dish).
- Printed board (kjs circuit\_etching.js): chemical reactor in a Cleanroom, 1800 ticks (90 s) at 480 EU/t, 1 wetware circuit board + 16 niobium titanium foil + 5 B iron III chloride (or 10 B sodium persulfate) → 1 wetware printed circuit board. The script first adds a cupric chloride version (2.5 B) and then removes everything with this output before re-adding the two above, so use iron III chloride or persulfate (Unverified whether the cupric version survives).
- Neuro processing unit (gtsrc CircuitRecipes neuro\_processor, not touched by the pack): circuit assembler, Cleanroom, 600 ticks at 80 000 EU/t, 1 wetware printed circuit board + 16 stem cells + 8 small PBI fluid pipes + 8 electrum plates + 16 silicone rubber foil + 8 HSS-E bolts + 250 mB sterilized growth medium. 80 000 EU/t is above LuV (32 768), so this needs a ZPM circuit assembler (131 072 EU/t).
- Wetware processor, two recipes: (a) pack (circuits.js): circuit assembler, 100 ticks at 38 400 EU/t, 1 neuro unit + 1 crystal CPU + 1 nano CPU chip + 4 living capacitors + 4 living transistors + 8 fine YBCO wire → 2 processors; (b) GT (CircuitRecipes wetware\_processor\_luv): 200 ticks, same neuro unit + crystal CPU + nano CPU but 8 advanced SMD capacitors + 8 advanced SMD transistors + 8 fine YBCO wire, output 1 or 2 (harder-circuit config); also a SoC route: neuro unit + highly advanced SoC + 8 fine YBCO wire + 8 naquadah bolts, 100 ticks at 150 000 EU/t. 38 400 EU/t is above 32 768 EU/t, so a ZPM circuit assembler is needed again.
- Sub-steps people skip: (1) the board recipe consumes ONE petri dish, LuV pump and LuV sensor per 16 boards, keep them in drawers with Keep Exact 1; (2) only the sterile bio line (uv\_bio1/uv\_bio2) is Sterile Cleanroom; this chain runs in a NORMAL cleanroom, a sterile cleanroom would reject it; (3) an unprocessed wetware circuit board and a wetware PRINTED board are different items; (4) every neuro unit eats a whole printed board, a run of 16 boards leaves 15 spare for the assembly, computer and mainframe recipes (they each take one).
- **Unverified** whether a LuV circuit assembler can run the 38 400 EU/t recipes with an overclock cap (the recipe EU is above LuV voltage, so it will not start), the cleanroom size, and the output count of the GT processor recipe in this pack config.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:luv_circuit_assembler` | 1 |
| `gtceu:zpm_circuit_assembler` | 2 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:wetware_processor`, `gtceu:neuro_processing_unit`, `gtceu:wetware_printed_circuit_board`, `gtceu:wetware_circuit_board`, `gtceu:petri_dish`
