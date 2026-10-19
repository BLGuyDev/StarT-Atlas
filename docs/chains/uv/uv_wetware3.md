---
kind: chain
id: uv_wetware3
order: 1620
data:
  t: |-
    UHV circuit: Wetware Processor Mainframe (2 computers + living SMDs, 70 s at 300 000 EU/t, station research 96 CWU/t) - the UV fusion reactor and the UHV hatches ask for it
  inf: true
  "n":
    - [tf, "2 tritanium frame (tritanium ingots from fusion, see uv_fusion_mats)", x, "gtceu:tritanium_frame"]
    - - g1
      - |-
        2 wetware computer (uv_wetware2) · 24 QRAM chip · 2 UHPIC chip
      - g
      - functionalstorage:oak_1
      - - [Wetware computer, "gtceu:wetware_processor_computer"]
        - [QRAM chip, "kubejs:qram_chip"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
    - - g2
      - |-
        12 living inductor · 12 capacitor · 12 diode · 12 resistor · 12 transistor
      - g
      - functionalstorage:oak_1
      - - [Living inductor, "kubejs:living_smd_inductor"]
        - [Living capacitor, "kubejs:living_smd_capacitor"]
        - [Living diode, "kubejs:living_smd_diode"]
        - [Living resistor, "kubejs:living_smd_resistor"]
        - [Living transistor, "kubejs:living_smd_transistor"]
    - - g3
      - |-
        16 YBCO single wire · 4 europium plate · 1728 mB ITLC solder · 1152 mB PBI
      - g
      - functionalstorage:oak_1
      - - [YBCO single wire, "gtceu:yttrium_barium_cuprate_single_wire"]
        - [Europium plate, "gtceu:europium_plate"]
        - [PBI, "gtceu:polybenzimidazole_bucket"]
    - - rs
      - Research Station · 96 CWU/t · 64 000 EU/t · wetware computer in the Object Holder
      - m
      - gtceu:research_station
    - [od, Data orb with the computer research, x, "gtceu:data_orb"]
    - [al, "Assembly Line · 70 s · 300 000 EU/t", m, "gtceu:assembly_line"]
    - [mf, "Wetware Processor Mainframe (UHV circuit)", o, "gtceu:wetware_processor_mainframe"]
  e:
    - [rs, od, research]
    - [od, al, data]
    - [tf, al, "2"]
    - [g1, al, "1"]
    - [g2, al, "1"]
    - [g3, al, "1"]
    - [al, mf, "1 / 70 s"]
  tips:
    - |-
      Recipe (kjs circuits.js, assemblyLineCircuitRS; the GT recipe wetware_mainframe_uhv and its research are removed): 2 tritanium frames + 2 wetware processor computers + 24 QRAM chips + 2 UHPIC chips + 12 each of living inductor / capacitor / diode / resistor / transistor + 16 YBCO single wire + 4 europium plates; 1728 mB indium tin lead cadmium soldering alloy + 1152 mB PBI; 1400 ticks (70 s) at 300 000 EU/t; STATION research of the wetware computer at 96 CWU/t and 64 000 EU/t. The circuits tag (GTCEu jar tags/items/circuits/uhv.json) holds ONLY this mainframe from GT; the pack adds the runic computer, draconic assembly and abyssal processor to the tag (utils/tags.js).
    - |-
      Why it matters in the UV era: the UV Fusion Reactor takes 4 UHV circuits (see uv_fusion), the UHV energy hatch and the UHV machines 1 to 3 each, HPCA optimized components 4 each, and several late multis 4 to 24. Four mainframes cost 8 wetware computers, which is about 8 neuro units and 144 QRAM chips (12 wafers) on top of 240 living SMDs: this is the biggest circuit bill of the era. 300 000 EU/t for 70 s is 21 MEU per mainframe.
    - |-
      CWU: 96 CWU/t is 6 HPCA advanced computation components at 16 CWU/t each. One HPCA has 9 slots and each advanced component needs 4 cooling units (active cooler 2, heat sink 1), so one HPCA gives about 48 CWU/t; 96 CWU/t needs three bridged HPCAs through a Network Switch (uv_research). Unverified: the exact overheat rule in this fork.
    - |-
      Power: 300 000 EU/t is a UV-tier recipe (above 131 072 V ZPM), so the Assembly Line needs a ZPM 4A hatch (524 288 EU/t) or better; the pack quest text says the next-tier 4A hatch gives the next tier’s recipe speed.
    - |-
      Sub-steps people skip: (1) the research item is the COMPUTER, not the assembly: keep 1 spare computer for the Object Holder, it is not consumed (Unverified GT default); (2) frames are tritanium, made in a Fusion MK II with tier-3 reflectors (200 MEU, uv_fusion_mats): no Abydos and no UV reactor needed, and the wetware circuits themselves (living SMDs, wetware PCB, qram wafer with SiC over bismuth tritelluride in a sterile chamber) have no Abydos ingredient; (3) 60 living SMDs per mainframe: build the five SMD assemblers (uv_living_smd) twice over; (4) UHPIC chip drawer Keep Exact 2.
    - "Unverified: the NOR / NAND chip volume."
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:zpm_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:tritanium_frame", "gtceu:wetware_processor_computer", "kubejs:qram_chip"]
      t: |-
        Drawers first, one per input: tritanium frames (Keep Exact 2), wetware computers (2), QRAM chips (24), UHPIC chips (2), five living SMD drawers (12 each), YBCO single wire (16), europium plates (4). Drums: ITLC soldering alloy and PBI.
    - i: ["gtceu:research_station", "gtceu:wetware_processor_computer", "gtceu:data_orb"]
      t: |-
        Research: a data orb + 1 wetware computer in the Object Holder, 96 CWU/t at 64 000 EU/t → an orb with the recipe. The orb goes into the Assembly Line’s Data Access Hatch (zpm_data).
    - i: ["gtceu:assembly_line", "gtceu:wetware_processor_mainframe"]
      t: |-
        Assembly Line buses in recipe order: frames, computers, QRAM, UHPIC chips, the five SMD stacks, wire, plates; solder + PBI by hatches. 70 s at 300 000 EU/t.
    - i: ["gtceu:zpm_energy_input_hatch_4a", "gtceu:assembly_line"]
      t: |-
        Power: a ZPM 4A hatch is 4 x 131 072 = 524 288 EU/t, enough. Put a Power Substation buffer first: 21 MEU per mainframe.
    - i: ["functionalstorage:oak_1", "gtceu:wetware_processor_mainframe"]
      t: |-
        Output drawer Keep Exact 4: routers send them straight to the UV fusion reactor (4), HPCA optimized components, UHV hatches.
    - i: ["gtceu:wetware_processor_computer", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: two computers per mainframe, so the computer line (uv_wetware2) must run at twice the speed you need for UV circuits alone.
---
# UHV circuit: Wetware Processor Mainframe (2 computers + living SMDs, 70 s at 300 000 EU/t, station research 96 CWU/t) - the UV fusion reactor and the UHV hatches ask for it

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_wetware3` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Wetware circuits (UV and UHV circuit)](../../plan/p14.md#wetware)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 96 CWU/t · 64 000 EU/t · wetware computer in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data orb with the computer research (gtceu:data_orb) - research"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><span class="gt-note">Data orb with the computer research</span><b class="gt-q">research</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 70 s · 300 000 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data orb with the computer research (gtceu:data_orb) - data"><img class="gt-ico" src="../../assets/icons/gtceu__data_orb.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Orb</span><span class="gt-note">Data orb with the computer research</span><b class="gt-q">data</b></span><span class="gt-slot" title="2 tritanium frame (tritanium ingots from fusion, see uv_fusion_mats) (gtceu:tritanium_frame) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tritanium_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritanium Frame</span><span class="gt-note">2 tritanium frame (tritanium ingots from fusion, see uv_fusion_mats)</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="2 wetware computer (uv_wetware2) · 24 QRAM chip · 2 UHPIC chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 wetware computer (uv_wetware2) · 24 QRAM chip · 2 UHPIC chip</span><span class="gt-sub"><span>Wetware computer</span><span>QRAM chip</span><span>UHPIC chip</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="12 living inductor · 12 capacitor · 12 diode · 12 resistor · 12 transistor (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">12 living inductor · 12 capacitor · 12 diode · 12 resistor · 12 transistor</span><span class="gt-sub"><span>Living inductor</span><span>Living capacitor</span><span>Living diode</span><span>Living resistor</span><span>Living transistor</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="16 YBCO single wire · 4 europium plate · 1728 mB ITLC solder · 1152 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 YBCO single wire · 4 europium plate · 1728 mB ITLC solder · 1152 mB PBI</span><span class="gt-sub"><span>YBCO single wire</span><span>Europium plate</span><span>PBI</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">70 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Wetware Processor Mainframe (UHV circuit) (gtceu:wetware_processor_mainframe) - 1 / 70 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Processor Mainframe</span><span class="gt-note">Wetware Processor Mainframe (UHV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Research Station · 96 CWU/t · 64 000 EU/t · wetware computer in the Object Holder](#m-rs) → [Assembly Line · 70 s · 300 000 EU/t](#m-al)

## How to build

1. Drawers first, one per input: tritanium frames (Keep Exact 2), wetware computers (2), QRAM chips (24), UHPIC chips (2), five living SMD drawers (12 each), YBCO single wire (16), europium plates (4). Drums: ITLC soldering alloy and PBI. — `functionalstorage:oak_1`, `gtceu:tritanium_frame`, `gtceu:wetware_processor_computer`, `kubejs:qram_chip`
2. Research: a data orb + 1 wetware computer in the Object Holder, 96 CWU/t at 64 000 EU/t → an orb with the recipe. The orb goes into the Assembly Line’s Data Access Hatch (zpm\_data). — `gtceu:research_station`, `gtceu:wetware_processor_computer`, `gtceu:data_orb`
3. Assembly Line buses in recipe order: frames, computers, QRAM, UHPIC chips, the five SMD stacks, wire, plates; solder + PBI by hatches. 70 s at 300 000 EU/t. — `gtceu:assembly_line`, `gtceu:wetware_processor_mainframe`
4. Power: a ZPM 4A hatch is 4 x 131 072 = 524 288 EU/t, enough. Put a Power Substation buffer first: 21 MEU per mainframe. — `gtceu:zpm_energy_input_hatch_4a`, `gtceu:assembly_line`
5. Output drawer Keep Exact 4: routers send them straight to the UV fusion reactor (4), HPCA optimized components, UHV hatches. — `functionalstorage:oak_1`, `gtceu:wetware_processor_mainframe`
6. Easy to miss: two computers per mainframe, so the computer line (uv\_wetware2) must run at twice the speed you need for UV circuits alone. — `gtceu:wetware_processor_computer`, `functionalstorage:oak_1`

## Tips

- Recipe (kjs circuits.js, assemblyLineCircuitRS; the GT recipe wetware\_mainframe\_uhv and its research are removed): 2 tritanium frames + 2 wetware processor computers + 24 QRAM chips + 2 UHPIC chips + 12 each of living inductor / capacitor / diode / resistor / transistor + 16 YBCO single wire + 4 europium plates; 1728 mB indium tin lead cadmium soldering alloy + 1152 mB PBI; 1400 ticks (70 s) at 300 000 EU/t; STATION research of the wetware computer at 96 CWU/t and 64 000 EU/t. The circuits tag (GTCEu jar tags/items/circuits/uhv.json) holds ONLY this mainframe from GT; the pack adds the runic computer, draconic assembly and abyssal processor to the tag (utils/tags.js).
- Why it matters in the UV era: the UV Fusion Reactor takes 4 UHV circuits (see uv\_fusion), the UHV energy hatch and the UHV machines 1 to 3 each, HPCA optimized components 4 each, and several late multis 4 to 24. Four mainframes cost 8 wetware computers, which is about 8 neuro units and 144 QRAM chips (12 wafers) on top of 240 living SMDs: this is the biggest circuit bill of the era. 300 000 EU/t for 70 s is 21 MEU per mainframe.
- CWU: 96 CWU/t is 6 HPCA advanced computation components at 16 CWU/t each. One HPCA has 9 slots and each advanced component needs 4 cooling units (active cooler 2, heat sink 1), so one HPCA gives about 48 CWU/t; 96 CWU/t needs three bridged HPCAs through a Network Switch (uv\_research). Unverified: the exact overheat rule in this fork.
- Power: 300 000 EU/t is a UV-tier recipe (above 131 072 V ZPM), so the Assembly Line needs a ZPM 4A hatch (524 288 EU/t) or better; the pack quest text says the next-tier 4A hatch gives the next tier’s recipe speed.
- Sub-steps people skip: (1) the research item is the COMPUTER, not the assembly: keep 1 spare computer for the Object Holder, it is not consumed (Unverified GT default); (2) frames are tritanium, made in a Fusion MK II with tier-3 reflectors (200 MEU, uv\_fusion\_mats): no Abydos and no UV reactor needed, and the wetware circuits themselves (living SMDs, wetware PCB, qram wafer with SiC over bismuth tritelluride in a sterile chamber) have no Abydos ingredient; (3) 60 living SMDs per mainframe: build the five SMD assemblers (uv\_living\_smd) twice over; (4) UHPIC chip drawer Keep Exact 2.
- **Unverified** the NOR / NAND chip volume.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:zpm_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:wetware_processor_mainframe`
