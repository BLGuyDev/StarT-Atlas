---
kind: chain
id: uev_circuits
order: 1970
data:
  t: |-
    UEV circuit: Runic Processor Mainframe (2 Runic Processor Computers + 32 QRAM chips + 5 living SMDs + runic convergence infusion)
  inf: true
  "n":
    - - g1
      - |-
        2 ancient runicalium frame · 2 runic processor computer · 32 QRAM chip · 4 UHPIC chip
      - g
      - functionalstorage:oak_1
      - - [Ancient runicalium frame, "gtceu:ancient_runicalium_frame"]
        - [Runic processor computer, "kubejs:runic_processor_computer"]
        - [QRAM chip, "kubejs:qram_chip"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
    - - g2
      - |-
        Living SMDs: 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor
      - g
      - functionalstorage:oak_1
      - - [Living inductor, "kubejs:living_smd_inductor"]
        - [Living capacitor, "kubejs:living_smd_capacitor"]
        - [Living diode, "kubejs:living_smd_diode"]
        - [Living resistor, "kubejs:living_smd_resistor"]
        - [Living transistor, "kubejs:living_smd_transistor"]
    - - g3
      - |-
        24 europium single wire · 64 PEEK foil · 4 trinaquadalloy plate
      - g
      - functionalstorage:oak_1
      - - [Europium single wire, "gtceu:europium_single_wire"]
        - [PEEK foil, "gtceu:polyether_ether_ketone_foil"]
        - [Trinaquadalloy plate, "gtceu:trinaquadalloy_plate"]
    - - fl
      - |-
        2304 mB soldering alloy (indium tin lead cadmium) · 864 mB PEEK · 1000 mB runic convergence infusion
      - f
      - gtceu:runic_convergence_infusion_bucket
    - - rs
      - |-
        Research Station: data from the Runic Processor Computer · 160 CWU/t · 400 000 EU/t
      - m
      - gtceu:research_station
    - [al, "Assembly Line · 90 s · 600 000 EU/t", m, "gtceu:assembly_line"]
    - [o, "Runic Processor Mainframe (UEV circuit)", o, "kubejs:runic_processor_mainframe"]
  e:
    - [g1, al, "1 set"]
    - [g2, al, "1 set"]
    - [g3, al, "1 set"]
    - [fl, al, "3 fluids"]
    - [rs, al, data]
    - [al, o, "1 / 90 s"]
  tips:
    - |-
      Source: circuits.js (assemblyLineCircuitRS 'runic_processor_mainframe'): 2 ancient runicalium frames, 2 runic processor computers, 32 QRAM chips, 4 UHPIC chips, 24 living inductors, 32 living capacitors, 24 living diodes, 24 living resistors, 24 living transistors, 24 europium single wires, 64 PEEK foil and 4 trinaquadalloy plates, plus 2304 mB indium tin lead cadmium soldering alloy, 864 mB PEEK and 1000 mB runic convergence infusion; 1800 ticks (90 s) at 600 000 EU/t; research item = Runic Processor Computer, 160 CWU/t, 400 000 EU/t. 600 000 EU/t is above one UV hatch (524 288) and below a UHV hatch (2 097 152): a UHV 1A hatch (or UV 2A and up) feeds the Assembly Line; no UEV hardware is involved.
    - |-
      Which items are the UEV circuit: the tag gtceu:circuits/uev holds the Runic Processor Mainframe, the Draconic Processor Computer and the Abyssal Processor Assembly (utils/tags.js), plus the UEV universal circuit (universal_circuits.js). Only the runic mainframe is made without the Draco Circuit Assembler, so it is the first UEV circuit you can build. The other two need the UIV-era Draco Circuit Assembler (uiv_circuits).
    - One UEV circuit costs 2 Runic Processor Computers; each computer costs 2 Runic Processor Assemblies, each of those 2 Runic Processors (UHV/UV pieces, see the UV and UHV pages). So a mainframe = 8 Runic Processors, 32 QRAM chips and 24 of each of the 5 living SMD types (32 capacitors). The living SMD and QRAM lines are the real bottleneck, not the Assembly Line.
    - |-
      Timing (verified): the first UEV circuit needs nothing UEV: every input is UHV or lower (runic processor, assembly and computer, living SMDs at VHA[ZPM], QRAM, 4 UHPIC chips, the infusion of uhv_runic_infusion), so build it at the end of the UHV era. The UHV-era builds already ask for it: the UHV Fusion Reactor [AUX I] (4 UEV circuits + 96 UEPIC chips), the Ancient Stargate Generator (about 96 UEV circuits in the dimensional supercomputer and 64 UEPIC chips per computational matrix) and the Folding Akreyrium Stabiliser (48 UEPIC). Only the machines that need UEV hulls, UEV hatches and UEV parallel hatches are truly UEV-era.
    - |-
      UEV circuits are consumed in bulk by: Hell Forge, Cryostate Quantum Chiller and Mega ABS (12 each), Super Compact Heat Chamber (4), UEV hull-tier machines (1 to 12), every UEV catalyst, UEV energy hatch (1) and the sterile cleaning maintenance hatch (3). Keep a drawer with Keep Exact 16 per circuit type.
    - |-
      Sub-steps people skip: (1) the research must be done on a Runic Processor Computer first (Research Station writes it on a data item; the data item must sit in a Data Access Hatch or Data Bank before the Assembly Line); (2) fluids need a hatch that holds 2304 mB: use UHV or larger input hatches; (3) frames are made with the ancient runicalium frame box recipe; (4) the infusion is also the base for UV and UHV runic circuits: do not drain it.
    - |-
      Unverified: which data item the station uses for 160 CWU (the draco recipes say data module under 160, DNA disk at 160 and above for their own research recipes), and the QRAM/living SMD recipes (UV and UHV pages).
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uhv_input_bus", 3]
    - ["gtceu:uhv_input_hatch", 3]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:ancient_runicalium_frame", "kubejs:runic_processor_computer"]
      t: |-
        Drawers first (Keep Exact 2): ancient runicalium frame, runic processor computer. Drawers for QRAM chips (64), UHPIC chips (16), the five living SMD types (64 each), europium single wire, PEEK foil and trinaquadalloy plate.
    - i: ["gtceu:research_station", "gtceu:data_orb"]
      t: |-
        Research once: Research Station with a Runic Processor Computer scanned onto a data item (160 CWU/t, 400 000 EU/t). Put the data item in a Data Access Hatch of the Assembly Line.
    - i: ["gtceu:assembly_line", "kubejs:living_smd_capacitor", "kubejs:qram_chip"]
      t: |-
        Assembly Line item feed: one router or Pipez item pipe per drawer into its own bus slot, in recipe order; Robot Arm cover Keep Exact on each, Item Filter set to the single item.
    - i: ["gtceu:runic_convergence_infusion_bucket", "gtceu:polyether_ether_ketone_bucket"]
      t: |-
        Fluids: three drums (soldering alloy 2304 mB, PEEK 864 mB, runic convergence infusion 1000 mB), each on a Pipez fluid pipe with a pump cover into its own input hatch.
    - i: ["gtceu:assembly_line", "kubejs:runic_processor_mainframe"]
      t: |-
        Run: 90 s, 600 000 EU/t. Output bus to a drawer, Keep Exact 12 (the multiblock recipes ask for 12 circuits each).
---
# UEV circuit: Runic Processor Mainframe (2 Runic Processor Computers + 32 QRAM chips + 5 living SMDs + runic convergence infusion)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_circuits` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEPIC chip and UEV circuit](../../plan/p17.md#uevcirc)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station: data from the Runic Processor Computer · 160 CWU/t · 400 000 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 90 s · 600 000 EU/t (gtceu:assembly_line) - data"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 90 s · 600 000 EU/t</span><b class="gt-q">data</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 90 s · 600 000 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 ancient runicalium frame · 2 runic processor computer · 32 QRAM chip · 4 UHPIC chip (functionalstorage:oak_1) - 1 set"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 ancient runicalium frame · 2 runic processor computer · 32 QRAM chip · 4 UHPIC chip</span><span class="gt-sub"><span>Ancient runicalium frame</span><span>Runic processor computer</span><span>QRAM chip</span><span>UHPIC chip</span></span><b class="gt-q">1 set</b></span><span class="gt-slot gt-group" title="Living SMDs: 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor (functionalstorage:oak_1) - 1 set"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs: 24 inductor · 32 capacitor · 24 diode · 24 resistor · 24 transistor</span><span class="gt-sub"><span>Living inductor</span><span>Living capacitor</span><span>Living diode</span><span>Living resistor</span><span>Living transistor</span></span><b class="gt-q">1 set</b></span><span class="gt-slot gt-group" title="24 europium single wire · 64 PEEK foil · 4 trinaquadalloy plate (functionalstorage:oak_1) - 1 set"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">24 europium single wire · 64 PEEK foil · 4 trinaquadalloy plate</span><span class="gt-sub"><span>Europium single wire</span><span>PEEK foil</span><span>Trinaquadalloy plate</span></span><b class="gt-q">1 set</b></span><span class="gt-slot gt-fluid" title="2304 mB soldering alloy (indium tin lead cadmium) · 864 mB PEEK · 1000 mB runic convergence infusion (gtceu:runic_convergence_infusion_bucket) - 3 fluids"><img class="gt-ico" src="../../assets/icons/gtceu__runic_convergence_infusion_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Convergence Infusion</span><span class="gt-note">2304 mB soldering alloy (indium tin lead cadmium) · 864 mB PEEK · 1000 mB runic convergence infusion</span><b class="gt-q">3 fluids</b></span><a class="gt-slot gt-mach" href="#m-rs" title="Research Station: data from the Runic Processor Computer · 160 CWU/t · 400 000 EU/t (gtceu:research_station) - data"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station: data from the Runic Processor Computer · 160 CWU/t · 400 000 EU/t</span><b class="gt-q">data</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Runic Processor Mainframe (UEV circuit) (kubejs:runic_processor_mainframe) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/kubejs__runic_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Processor Mainframe</span><span class="gt-note">Runic Processor Mainframe (UEV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Research Station: data from the Runic Processor Computer · 160 CWU/t · 400 000 EU/t](#m-rs) → [Assembly Line · 90 s · 600 000 EU/t](#m-al)

## How to build

1. Drawers first (Keep Exact 2): ancient runicalium frame, runic processor computer. Drawers for QRAM chips (64), UHPIC chips (16), the five living SMD types (64 each), europium single wire, PEEK foil and trinaquadalloy plate. — `functionalstorage:oak_1`, `gtceu:ancient_runicalium_frame`, `kubejs:runic_processor_computer`
2. Research once: Research Station with a Runic Processor Computer scanned onto a data item (160 CWU/t, 400 000 EU/t). Put the data item in a Data Access Hatch of the Assembly Line. — `gtceu:research_station`, `gtceu:data_orb`
3. Assembly Line item feed: one router or Pipez item pipe per drawer into its own bus slot, in recipe order; Robot Arm cover Keep Exact on each, Item Filter set to the single item. — `gtceu:assembly_line`, `kubejs:living_smd_capacitor`, `kubejs:qram_chip`
4. Fluids: three drums (soldering alloy 2304 mB, PEEK 864 mB, runic convergence infusion 1000 mB), each on a Pipez fluid pipe with a pump cover into its own input hatch. — `gtceu:runic_convergence_infusion_bucket`, `gtceu:polyether_ether_ketone_bucket`
5. Run: 90 s, 600 000 EU/t. Output bus to a drawer, Keep Exact 12 (the multiblock recipes ask for 12 circuits each). — `gtceu:assembly_line`, `kubejs:runic_processor_mainframe`

## Tips

- Source: circuits.js (assemblyLineCircuitRS 'runic\_processor\_mainframe'): 2 ancient runicalium frames, 2 runic processor computers, 32 QRAM chips, 4 UHPIC chips, 24 living inductors, 32 living capacitors, 24 living diodes, 24 living resistors, 24 living transistors, 24 europium single wires, 64 PEEK foil and 4 trinaquadalloy plates, plus 2304 mB indium tin lead cadmium soldering alloy, 864 mB PEEK and 1000 mB runic convergence infusion; 1800 ticks (90 s) at 600 000 EU/t; research item = Runic Processor Computer, 160 CWU/t, 400 000 EU/t. 600 000 EU/t is above one UV hatch (524 288) and below a UHV hatch (2 097 152): a UHV 1A hatch (or UV 2A and up) feeds the Assembly Line; no UEV hardware is involved.
- Which items are the UEV circuit: the tag gtceu:circuits/uev holds the Runic Processor Mainframe, the Draconic Processor Computer and the Abyssal Processor Assembly (utils/tags.js), plus the UEV universal circuit (universal\_circuits.js). Only the runic mainframe is made without the Draco Circuit Assembler, so it is the first UEV circuit you can build. The other two need the UIV-era Draco Circuit Assembler (uiv\_circuits).
- One UEV circuit costs 2 Runic Processor Computers; each computer costs 2 Runic Processor Assemblies, each of those 2 Runic Processors (UHV/UV pieces, see the UV and UHV pages). So a mainframe = 8 Runic Processors, 32 QRAM chips and 24 of each of the 5 living SMD types (32 capacitors). The living SMD and QRAM lines are the real bottleneck, not the Assembly Line.
- Timing (verified): the first UEV circuit needs nothing UEV: every input is UHV or lower (runic processor, assembly and computer, living SMDs at VHA\[ZPM\], QRAM, 4 UHPIC chips, the infusion of uhv\_runic\_infusion), so build it at the end of the UHV era. The UHV-era builds already ask for it: the UHV Fusion Reactor \[AUX I\] (4 UEV circuits + 96 UEPIC chips), the Ancient Stargate Generator (about 96 UEV circuits in the dimensional supercomputer and 64 UEPIC chips per computational matrix) and the Folding Akreyrium Stabiliser (48 UEPIC). Only the machines that need UEV hulls, UEV hatches and UEV parallel hatches are truly UEV-era.
- UEV circuits are consumed in bulk by: Hell Forge, Cryostate Quantum Chiller and Mega ABS (12 each), Super Compact Heat Chamber (4), UEV hull-tier machines (1 to 12), every UEV catalyst, UEV energy hatch (1) and the sterile cleaning maintenance hatch (3). Keep a drawer with Keep Exact 16 per circuit type.
- Sub-steps people skip: (1) the research must be done on a Runic Processor Computer first (Research Station writes it on a data item; the data item must sit in a Data Access Hatch or Data Bank before the Assembly Line); (2) fluids need a hatch that holds 2304 mB: use UHV or larger input hatches; (3) frames are made with the ancient runicalium frame box recipe; (4) the infusion is also the base for UV and UHV runic circuits: do not drain it.
- **Unverified** which data item the station uses for 160 CWU (the draco recipes say data module under 160, DNA disk at 160 and above for their own research recipes), and the QRAM/living SMD recipes (UV and UHV pages).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uhv_input_bus` | 3 |
| `gtceu:uhv_input_hatch` | 3 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `kubejs:runic_processor_mainframe`
