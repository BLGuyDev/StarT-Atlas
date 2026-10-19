---
kind: chain
id: zpm_uv_circuit
order: 1480
data:
  t: |-
    UV circuit: Crystal Processor Mainframe (2 crystal computers + advanced SMDs in the Assembly Line, station research 16 CWU/t) - 4 of them gate every ZPM multiblock
  inf: true
  "n":
    - [cc, "2 Crystal Processor Supercomputer (zpm_crystal2)", i, "gtceu:crystal_processor_computer"]
    - - g2
      - |-
        2 HSS-E frame · 32 RAM · 4 HPIC chip · 12 ASMD inductor · 24 ASMD capacitor · 12 ASMD diode · 16 ASMD transistor · 12 NbTi single wire · 4 YBCO plate · 1152 mB soldering alloy
      - g
      - functionalstorage:oak_1
      - - [HSS-E frame, "gtceu:hsse_frame"]
        - [RAM chip, "gtceu:ram_chip"]
        - [HPIC chip, "gtceu:hpic_chip"]
        - [ASMD inductor, "gtceu:advanced_smd_inductor"]
        - [ASMD capacitor, "gtceu:advanced_smd_capacitor"]
        - [ASMD diode, "gtceu:advanced_smd_diode"]
        - [ASMD transistor, "gtceu:advanced_smd_transistor"]
        - [YBCO plate, "gtceu:yttrium_barium_cuprate_plate"]
    - - rs
      - Research Station · 16 CWU/t · 38 400 EU/t · crystal computer in the Object Holder
      - m
      - gtceu:research_station
    - [dd, Data orb with the crystal computer research, x, "gtceu:data_orb"]
    - [al, "Assembly Line · 50 s · 61 440 EU/t", m, "gtceu:assembly_line"]
    - [mf, "Crystal Processor Mainframe (UV circuit)", o, "gtceu:crystal_processor_mainframe"]
  e: [[cc, rs, "1 scan"], [rs, dd, research], [dd, al, data], [cc, al, "2"], [g2, al, "1"], [al, mf, "1 / 50 s"]]
  tips:
    - |-
      Why this chain exists: nearly every ZPM-era multiblock recipe in the pack asks for UV circuits (#gtceu:circuits/uv): Component Part Assembly 4, Heat Chamber 4, Large Rotor Machine 4, Runic Engraver 4, Stargate Component Assembly 16, Dimensional Finder 8, Mega Vacuum Freezer 2, ZPM Fusion Reactor 4 and the Classic Stargate parts (csg_reinforced_plating 1, dimensional supercomputer 64). The tag holds the crystal mainframe, the wetware processor computer (guide19), kubejs:runic_processor_assembly and kubejs:draconic_processor (kjs utils/tags.js). The crystal mainframe is the only one reachable in the ZPM era without the runic and draconic lines.
    - |-
      Recipe (kjs additions/progression/circuitry/circuits.js, assemblyLineCircuitRS; the GT mainframe recipe is removed): 2 HSS-E frames + 2 crystal processor supercomputers + 32 RAM chips + 4 HPIC chips + 12 advanced SMD inductors + 24 advanced SMD capacitors + 12 advanced SMD diodes + 16 advanced SMD transistors + 12 niobium titanium single wire + 4 yttrium barium cuprate plates, 1152 mB soldering alloy, 1000 ticks (50 s) at 61 440 EU/t, STATION research of the crystal computer at 16 CWU/t and 38 400 EU/t. 61 440 EU/t is a ZPM-tier recipe: the LuV 4A hatch on the Assembly Line.
    - |-
      Cost per mainframe: 2 crystal computers (2 ZPM circuits worth: 2 crystal CPUs, 4 nano CPU chips, 6 elite boards, 96 RAM, 32 NOR, 64 NAND chips, 96 fine NbTi wire, see zpm_crystal2) + 32 RAM + 4 HPIC + 64 advanced SMDs. So 4 UV circuits = 8 crystal computers = 8 crystal CPUs (about 80 minutes of autoclave clock on a single autoclave in the part loop), 24 elite boards and 512 RAM chips in total. The ASMD part is cheap (zpm_asmd); the RAM, boards and CPUs are the time.
    - |-
      YBCO plate: yttrium barium cuprate ingot (4500 K EBF, VA[IV], 1000 ticks, freezer 150 ticks at VA[EV]) from the mixer 1 yttrium + 2 barium + 3 copper dust + 7 B oxygen (Unverified: the exact mixer recipe and the yttrium source). 12 NbTi single wire = 6 NbTi ingots. HSS-E frame: 2 HSS-E ingots. HPIC chip: iv_hatches chain.
    - |-
      Data: put one crystal computer in the Object Holder with a data orb; the Research Station needs 16 CWU/t (4 computation components, i.e. 16 CWU/t when all are cooled) - the zpm_research HPCA with 4 computation components just reaches it. Scanning does not consume the computer (Unverified, GT default).
    - |-
      Sub-steps people skip: (1) the research is station research, not a scanner: the Station and HPCA must stand first; (2) the Assembly Line must have the LuV 4A hatch (61 440 EU/t); (3) keep Keep Exact 2 on the crystal computer drawer (2 per craft) and Keep Exact 12 on the capacitors; (4) every UV circuit also feeds the next tier chain, so do not hoard fewer than 8 once you start the multis.
    - |-
      Unverified: the YBCO mixer recipe, the yttrium source and the exact CWU the station needs for a 16 CWU/t recipe at your overclock.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 1]
    - ["gtceu:iv_scanner", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:crystal_processor_computer", "gtceu:ram_chip", "gtceu:hsse_frame"]
      t: |-
        Drawers first, one per input: crystal computers (Keep Exact 2), HSS-E frames, RAM chips, HPIC chips, ASMD inductors, capacitors, diodes, transistors, NbTi single wire, YBCO plates. A soldering alloy drum. The Assembly Line gets its inputs by routers or Pipez pipes with Item Filters, one per bus.
    - i: ["gtceu:research_station", "gtceu:crystal_processor_computer", "gtceu:data_orb"]
      t: |-
        Research: a data orb + 1 crystal computer in the Object Holder, 16 CWU/t from the HPCA at 38 400 EU/t → an orb with the research. Then the orb goes into the Assembly Line’s Data Access Hatch (zpm_data).
    - i: ["gtceu:assembly_line", "gtceu:crystal_processor_mainframe", "gtceu:advanced_smd_transistor"]
      t: |-
        Mainframe: Assembly Line buses in recipe order: 2 HSS-E frames, 2 crystal computers, 32 RAM, 4 HPIC, 12 inductors, 24 capacitors, 12 diodes, 16 transistors, 12 NbTi single wire, 4 YBCO plates; 1152 mB soldering alloy. 50 s at 61 440 EU/t.
    - i: ["gtceu:luv_energy_input_hatch_4a", "gtceu:assembly_line"]
      t: |-
        Power: LuV 4A hatch (4 x 32 768 = 131 072 EU/t). 61 440 EU/t for 1000 ticks is 61 MEU per mainframe: a Power Substation buffer or a big battery bank before the first craft.
    - i: ["functionalstorage:oak_1", "gtceu:crystal_processor_mainframe"]
      t: Output drawer Keep Exact 8. Routers send them straight to the multiblock lines that need 4 each.
    - i: ["gtceu:ram_chip", "gtceu:crystal_cpu"]
      t: |-
        Easy to miss: start the crystal chip loop (zpm_crystal) and the RAM wafer lines two sessions before you want the mainframes, they are the real clock: 8 crystal computers per 4 mainframes.
---
# UV circuit: Crystal Processor Mainframe (2 crystal computers + advanced SMDs in the Assembly Line, station research 16 CWU/t) - 4 of them gate every ZPM multiblock

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_uv_circuit` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Crystal circuits and the UV circuit](../../plan/p12.md#zpmcrystal)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 16 CWU/t · 38 400 EU/t · crystal computer in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Crystal Processor Supercomputer (zpm_crystal2) (gtceu:crystal_processor_computer) - 1 scan"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Computer</span><span class="gt-note">2 Crystal Processor Supercomputer (zpm_crystal2)</span><b class="gt-q">1 scan</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data orb with the crystal computer research (gtceu:data_orb) - research"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><span class="gt-note">Data orb with the crystal computer research</span><b class="gt-q">research</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 50 s · 61 440 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data orb with the crystal computer research (gtceu:data_orb) - data"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><span class="gt-note">Data orb with the crystal computer research</span><b class="gt-q">data</b></span><span class="gt-slot" title="2 Crystal Processor Supercomputer (zpm_crystal2) (gtceu:crystal_processor_computer) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Computer</span><span class="gt-note">2 Crystal Processor Supercomputer (zpm_crystal2)</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="2 HSS-E frame · 32 RAM · 4 HPIC chip · 12 ASMD inductor · 24 ASMD capacitor · 12 ASMD diode · 16 ASMD transistor · 12 NbTi single wire · 4 YBCO plate · 1152 mB soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 HSS-E frame · 32 RAM · 4 HPIC chip · 12 ASMD inductor · 24 ASMD capacitor · 12 ASMD diode · 16 ASMD transistor · 12 NbTi single wire · 4 YBCO plate · 1152 mB soldering alloy</span><span class="gt-sub"><span>HSS-E frame</span><span>RAM chip</span><span>HPIC chip</span><span>ASMD inductor</span><span>ASMD capacitor</span><span>ASMD diode</span><span>ASMD transistor</span><span>YBCO plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crystal Processor Mainframe (UV circuit) (gtceu:crystal_processor_mainframe) - 1 / 50 s"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal Processor Mainframe</span><span class="gt-note">Crystal Processor Mainframe (UV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Research Station · 16 CWU/t · 38 400 EU/t · crystal computer in the Object Holder](#m-rs) → [Assembly Line · 50 s · 61 440 EU/t](#m-al)

## How to build

1. Drawers first, one per input: crystal computers (Keep Exact 2), HSS-E frames, RAM chips, HPIC chips, ASMD inductors, capacitors, diodes, transistors, NbTi single wire, YBCO plates. A soldering alloy drum. The Assembly Line gets its inputs by routers or Pipez pipes with Item Filters, one per bus. — `functionalstorage:oak_1`, `gtceu:crystal_processor_computer`, `gtceu:ram_chip`, `gtceu:hsse_frame`
2. Research: a data orb + 1 crystal computer in the Object Holder, 16 CWU/t from the HPCA at 38 400 EU/t → an orb with the research. Then the orb goes into the Assembly Line’s Data Access Hatch (zpm\_data). — `gtceu:research_station`, `gtceu:crystal_processor_computer`, `gtceu:data_orb`
3. Mainframe: Assembly Line buses in recipe order: 2 HSS-E frames, 2 crystal computers, 32 RAM, 4 HPIC, 12 inductors, 24 capacitors, 12 diodes, 16 transistors, 12 NbTi single wire, 4 YBCO plates; 1152 mB soldering alloy. 50 s at 61 440 EU/t. — `gtceu:assembly_line`, `gtceu:crystal_processor_mainframe`, `gtceu:advanced_smd_transistor`
4. Power: LuV 4A hatch (4 x 32 768 = 131 072 EU/t). 61 440 EU/t for 1000 ticks is 61 MEU per mainframe: a Power Substation buffer or a big battery bank before the first craft. — `gtceu:luv_energy_input_hatch_4a`, `gtceu:assembly_line`
5. Output drawer Keep Exact 8. Routers send them straight to the multiblock lines that need 4 each. — `functionalstorage:oak_1`, `gtceu:crystal_processor_mainframe`
6. Easy to miss: start the crystal chip loop (zpm\_crystal) and the RAM wafer lines two sessions before you want the mainframes, they are the real clock: 8 crystal computers per 4 mainframes. — `gtceu:ram_chip`, `gtceu:crystal_cpu`

## Tips

- Why this chain exists: nearly every ZPM-era multiblock recipe in the pack asks for UV circuits (#gtceu:circuits/uv): Component Part Assembly 4, Heat Chamber 4, Large Rotor Machine 4, Runic Engraver 4, Stargate Component Assembly 16, Dimensional Finder 8, Mega Vacuum Freezer 2, ZPM Fusion Reactor 4 and the Classic Stargate parts (csg\_reinforced\_plating 1, dimensional supercomputer 64). The tag holds the crystal mainframe, the wetware processor computer (guide19), kubejs:runic\_processor\_assembly and kubejs:draconic\_processor (kjs utils/tags.js). The crystal mainframe is the only one reachable in the ZPM era without the runic and draconic lines.
- Recipe (kjs additions/progression/circuitry/circuits.js, assemblyLineCircuitRS; the GT mainframe recipe is removed): 2 HSS-E frames + 2 crystal processor supercomputers + 32 RAM chips + 4 HPIC chips + 12 advanced SMD inductors + 24 advanced SMD capacitors + 12 advanced SMD diodes + 16 advanced SMD transistors + 12 niobium titanium single wire + 4 yttrium barium cuprate plates, 1152 mB soldering alloy, 1000 ticks (50 s) at 61 440 EU/t, STATION research of the crystal computer at 16 CWU/t and 38 400 EU/t. 61 440 EU/t is a ZPM-tier recipe: the LuV 4A hatch on the Assembly Line.
- Cost per mainframe: 2 crystal computers (2 ZPM circuits worth: 2 crystal CPUs, 4 nano CPU chips, 6 elite boards, 96 RAM, 32 NOR, 64 NAND chips, 96 fine NbTi wire, see zpm\_crystal2) + 32 RAM + 4 HPIC + 64 advanced SMDs. So 4 UV circuits = 8 crystal computers = 8 crystal CPUs (about 80 minutes of autoclave clock on a single autoclave in the part loop), 24 elite boards and 512 RAM chips in total. The ASMD part is cheap (zpm\_asmd); the RAM, boards and CPUs are the time.
- YBCO plate: yttrium barium cuprate ingot (4500 K EBF, VA\[IV\], 1000 ticks, freezer 150 ticks at VA\[EV\]) from the mixer 1 yttrium + 2 barium + 3 copper dust + 7 B oxygen (Unverified: the exact mixer recipe and the yttrium source). 12 NbTi single wire = 6 NbTi ingots. HSS-E frame: 2 HSS-E ingots. HPIC chip: iv\_hatches chain.
- Data: put one crystal computer in the Object Holder with a data orb; the Research Station needs 16 CWU/t (4 computation components, i.e. 16 CWU/t when all are cooled) - the zpm\_research HPCA with 4 computation components just reaches it. Scanning does not consume the computer (Unverified, GT default).
- Sub-steps people skip: (1) the research is station research, not a scanner: the Station and HPCA must stand first; (2) the Assembly Line must have the LuV 4A hatch (61 440 EU/t); (3) keep Keep Exact 2 on the crystal computer drawer (2 per craft) and Keep Exact 12 on the capacitors; (4) every UV circuit also feeds the next tier chain, so do not hoard fewer than 8 once you start the multis.
- **Unverified** the YBCO mixer recipe, the yttrium source and the exact CWU the station needs for a 16 CWU/t recipe at your overclock.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 1 |
| `gtceu:iv_scanner` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [ZPM circuit 2: Crystal Processor Supercomputer (elite board, crystal processor → assembly in the LCAF, computer in the Assembly Line)](zpm_crystal2.md)
- **Main source for:** `gtceu:crystal_processor_mainframe`
