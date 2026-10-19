---
kind: chain
id: uv_wetware2
order: 1580
data:
  t: |-
    Wetware circuits 2: QRAM chips → wetware processor assembly → Wetware Processor Computer (UV circuit, Assembly Line + 64 CWU/t research)
  inf: true
  "n":
    - [rw, RAM wafer, x, "gtceu:ram_wafer"]
    - - g0
      - "2 SiC over bismuth tritelluride dust · 500 mB radon"
      - g
      - functionalstorage:oak_1
      - [[SiC over BiTe dust, "gtceu:silicon_carbide_over_bismuth_tritelluride_dust"], [Radon, "gtceu:radon_bucket"]]
    - [qr, "ZPM Chemical Reactor · 60 s · 61 440 EU/t · Sterile Cleanroom", m, "gtceu:zpm_chemical_reactor"]
    - [qw, QRAM wafer, x, "kubejs:qram_wafer"]
    - [cu, "LuV Cutter · 45 s · 30 720 EU/t · Sterile Cleanroom", m, "gtceu:luv_cutter"]
    - [qc, QRAM chip x12, x, "kubejs:qram_chip"]
    - - g1
      - Wetware printed board · 2 wetware processor · 3 living inductor · 6 living capacitor · 6 QRAM chip · 16 fine YBCO wire
      - g
      - functionalstorage:oak_1
      - - [Printed board, "gtceu:wetware_printed_circuit_board"]
        - [Wetware processor, "gtceu:wetware_processor"]
        - [Living inductor, "kubejs:living_smd_inductor"]
        - [Living capacitor, "kubejs:living_smd_capacitor"]
    - [a1, "ZPM Circuit Assembler · 10 s · 38 400 EU/t · Cleanroom", m, "gtceu:zpm_circuit_assembler"]
    - [as, "Wetware processor assembly x2 (ZPM circuit)", x, "gtceu:wetware_processor_assembly"]
    - [rs, "Research Station · 64 CWU/t · 38 400 EU/t · assembly in the Object Holder", m, "gtceu:research_station"]
    - - g2
      - Printed board · 2 assembly · 4 living diode · 12 QRAM · 24 NOR · 48 NAND · 32 fine YBCO wire · 2 europium plate · 864 mB ITLC solder · 576 mB PBI
      - g
      - functionalstorage:oak_1
      - - [NOR chip, "gtceu:nor_memory_chip"]
        - [NAND chip, "gtceu:nand_memory_chip"]
        - [Living diode, "kubejs:living_smd_diode"]
        - [Europium plate, "gtceu:europium_plate"]
        - [PBI, "gtceu:polybenzimidazole_bucket"]
    - [al, "Assembly Line · 30 s · 64 000 EU/t (needs the orb)", m, "gtceu:assembly_line"]
    - [uc, "Wetware Processor Computer (UV circuit)", o, "gtceu:wetware_processor_computer"]
  e:
    - [rw, qr, "1"]
    - [g0, qr, "1"]
    - [qr, qw, "1 / 60 s"]
    - [qw, cu, "1"]
    - [cu, qc, "12 / 45 s"]
    - [qc, g1, "6"]
    - [g1, a1, "1"]
    - [a1, as, "2 / 10 s"]
    - [as, rs, "1 scan"]
    - [as, g2, "2"]
    - [rs, al, data orb]
    - [g2, al, "1"]
    - [al, uc, "1 / 30 s"]
  tips:
    - |-
      QRAM (kjs circuits.js): chemical reactor, Sterile Cleanroom, 1200 ticks at VHA[ZPM] (61 440 EU/t): 1 RAM wafer + 2 silicon carbide over bismuth tritelluride dust + 500 mB radon → 1 QRAM wafer; cutter, Sterile Cleanroom, 900 ticks at VA[LuV]: 1 wafer → 12 QRAM chips. The wafer needs a ZPM reactor (61 440 EU/t > LuV 32 768). Both machines sit in the STERILE cleanroom of bio line 1/2. Unverified: where silicon carbide over bismuth tritelluride dust comes from.
    - |-
      Wetware processor assembly (ZPM circuit; pack recipe, circuits.js): circuit assembler, Cleanroom, 200 ticks at 38 400 EU/t: 1 wetware printed circuit board + 2 wetware processors + 3 living inductors + 6 living capacitors + 6 QRAM chips + 16 fine YBCO wire → 2 assemblies. The GT recipe (wetware_processor_assembly_zpm) still exists too: 400 ticks, printed board + 2 processors + 6 advanced SMD inductors + 12 advanced SMD capacitors + 24 RAM chips + 16 fine YBCO wire with double solder → 2 assemblies; it needs no living SMDs and no QRAM.
    - |-
      Wetware Processor Computer (UV circuit; pack recipe, assemblyLineCircuitRS): printed board + 2 assemblies + 4 living diodes + 12 QRAM + 24 NOR chips + 48 NAND chips + 32 fine YBCO wire + 2 europium plates, fluids 864 mB indium tin lead cadmium soldering alloy + 576 mB PBI, 600 ticks at 64 000 EU/t, STATION research of the processor assembly at 64 CWU/t, 38 400 EU/t. The GT recipe (wetware_super_computer_uv) and its research are removed in the pack, so no scanner route. 64 000 EU/t is a ZPM-tier recipe (Assembly Line on a ZPM or 4A hatch).
    - |-
      CWU: 64 CWU/t is 4 HPCA advanced computation components at 16 each, and each of those makes 4 cooling units of heat; an HPCA has 9 component slots and an active cooler gives 2 cooling, so one HPCA tops out around 48 CWU/t (3 advanced + 6 active coolers). 64 CWU/t therefore needs two or three HPCAs with bridge components joined by a Network Switch (uv_research; the quest text confirms the switch routes several HPCAs into the Research Station).
    - |-
      Costs for ONE computer (an assembly craft gives 2 assemblies = exactly what the computer eats): 1 assembly craft (1 printed board, 2 processors = 1 processor craft = 1 neuro unit + 1 crystal CPU + 1 nano CPU chip, 3 living inductors, 6 living capacitors, 6 QRAM, 16 fine YBCO) + 1 computer craft (1 printed board, 4 living diodes, 12 QRAM, 24 NOR, 48 NAND, 32 fine YBCO, 2 europium plates). Totals per computer: 1 neuro unit (16 stem cells), 2 printed boards, 18 QRAM chips (1.5 wafers), 24 NOR + 48 NAND chips. So 4 UV circuits via this route are 4 neuro units, 8 printed boards (one board run of 16), 72 QRAM chips (6 wafers), 96 NOR and 192 NAND chips; compare the crystal mainframe route of zpm_uv_circuit.
    - |-
      Sub-steps people skip: (1) the research writes onto a data carrier (a data MODULE at 64 CWU/t, see uv_data; Unverified for the fork) that goes into the Assembly Line’s Data Access Hatch; (2) QRAM is made in the sterile cleanroom, the assemblers in the normal one; (3) keep Keep Exact 12 on the QRAM drawer and 48 on NAND; (4) 64 000 EU/t for 600 ticks is 38 MEU per computer, size the substation first.
    - |-
      Unverified: NOR/NAND chip routes at this volume; silicon carbide over bismuth tritelluride dust source.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:zpm_circuit_assembler", 1]
    - ["gtceu:zpm_chemical_reactor", 1]
    - ["gtceu:luv_cutter", 1]
    - ["gtceu:zpm_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 16]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 5]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:ram_wafer", "kubejs:qram_chip", "gtceu:nand_memory_chip"]
      t: |-
        Drawers first, one per input: RAM wafers, SiC over bismuth tritelluride dust, QRAM chips (Keep Exact 12), NOR chips (24), NAND chips (48), printed boards, processors, living SMDs, YBCO wire, europium plates. Drums: radon, ITLC soldering alloy, PBI.
    - i: ["gtceu:zpm_chemical_reactor", "kubejs:qram_wafer", "gtceu:luv_cutter"]
      t: |-
        Sterile corner: ZPM chemical reactor (wafer + 2 dust + 500 mB radon → QRAM wafer, 60 s), then a LuV cutter next to it (wafer → 12 chips, 45 s). A router or a Robot Arm cover moves the wafer; both machines inside the Sterile Cleanroom.
    - i: ["gtceu:zpm_circuit_assembler", "gtceu:wetware_processor_assembly"]
      t: |-
        Assembly assembler (ZPM circuit assembler, normal cleanroom): board + 2 processors + 3 living inductors + 6 living capacitors + 6 QRAM + 16 fine YBCO → 2 assemblies per 10 s.
    - i: ["gtceu:research_station", "gtceu:data_orb", "gtceu:wetware_processor_assembly"]
      t: |-
        Research: a data orb + 1 assembly in the Object Holder, 64 CWU/t at 38 400 EU/t, then the orb into the Assembly Line Data Access Hatch (zpm_data).
    - i: ["gtceu:assembly_line", "gtceu:wetware_processor_computer"]
      t: |-
        Computer: Assembly Line buses in recipe order, 864 mB solder + 576 mB PBI by hatches; 30 s at 64 000 EU/t. Output drawer Keep Exact 4.
    - i: ["gtceu:wetware_processor_computer", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: the computer is BOTH the UV circuit that the era multis ask for and the input of the UHV mainframe (2 per mainframe). Route the first ones to the multis, do not lock them in the mainframe line yet.
---
# Wetware circuits 2: QRAM chips → wetware processor assembly → Wetware Processor Computer (UV circuit, Assembly Line + 64 CWU/t research)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_wetware2` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Wetware circuits (UV and UHV circuit)](../../plan/p14.md#wetware)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-qr">
<div class="gt-head"><span class="gt-mname">ZPM Chemical Reactor · 60 s · 61 440 EU/t · Sterile Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="RAM wafer (gtceu:ram_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ram_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">RAM Wafer</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="2 SiC over bismuth tritelluride dust · 500 mB radon (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 SiC over bismuth tritelluride dust · 500 mB radon</span><span class="gt-sub"><span>SiC over BiTe dust</span><span>Radon</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="QRAM wafer (kubejs:qram_wafer) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/kubejs__qram_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">QRAM Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_chemical_reactor</code></div>
</div>
<div class="gt-panel t-luv" id="m-cu">
<div class="gt-head"><span class="gt-mname">LuV Cutter · 45 s · 30 720 EU/t · Sterile Cleanroom</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="QRAM wafer (kubejs:qram_wafer) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__qram_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">QRAM Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="QRAM chip x12 (kubejs:qram_chip) - 12 / 45 s"><img class="gt-ico" src="../../assets/icons/kubejs__qram_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">QRAM Chip</span><span class="gt-note">QRAM chip x12</span><b class="gt-q">12</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_cutter</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a1">
<div class="gt-head"><span class="gt-mname">ZPM Circuit Assembler · 10 s · 38 400 EU/t · Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Wetware printed board · 2 wetware processor · 3 living inductor · 6 living capacitor · 6 QRAM chip · 16 fine YBCO wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Wetware printed board · 2 wetware processor · 3 living inductor · 6 living capacitor · 6 QRAM chip · 16 fine YBCO wire</span><span class="gt-sub"><span>Printed board</span><span>Wetware processor</span><span>Living inductor</span><span>Living capacitor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Wetware processor assembly x2 (ZPM circuit) (gtceu:wetware_processor_assembly) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Processor Assembly</span><span class="gt-note">Wetware processor assembly x2 (ZPM circuit)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 64 CWU/t · 38 400 EU/t · assembly in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wetware processor assembly x2 (ZPM circuit) (gtceu:wetware_processor_assembly) - 1 scan"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_processor_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Processor Assembly</span><span class="gt-note">Wetware processor assembly x2 (ZPM circuit)</span><b class="gt-q">1 scan</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 30 s · 64 000 EU/t (needs the orb) (gtceu:assembly_line) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 30 s · 64 000 EU/t (needs the orb)</span><b class="gt-q">data orb</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 64 000 EU/t (needs the orb)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-rs" title="Research Station · 64 CWU/t · 38 400 EU/t · assembly in the Object Holder (gtceu:research_station) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station · 64 CWU/t · 38 400 EU/t · assembly in the Object Holder</span><b class="gt-q">data orb</b></a><span class="gt-slot gt-group" title="Printed board · 2 assembly · 4 living diode · 12 QRAM · 24 NOR · 48 NAND · 32 fine YBCO wire · 2 europium plate · 864 mB ITLC solder · 576 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Printed board · 2 assembly · 4 living diode · 12 QRAM · 24 NOR · 48 NAND · 32 fine YBCO wire · 2 europium plate · 864 mB ITLC solder · 576 mB PBI</span><span class="gt-sub"><span>NOR chip</span><span>NAND chip</span><span>Living diode</span><span>Europium plate</span><span>PBI</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Wetware Processor Computer (UV circuit) (gtceu:wetware_processor_computer) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__wetware_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wetware Processor Computer</span><span class="gt-note">Wetware Processor Computer (UV circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [ZPM Chemical Reactor · 60 s · 61 440 EU/t · Sterile Cleanroom](#m-qr) → [LuV Cutter · 45 s · 30 720 EU/t · Sterile Cleanroom](#m-cu) → [ZPM Circuit Assembler · 10 s · 38 400 EU/t · Cleanroom](#m-a1) → [Research Station · 64 CWU/t · 38 400 EU/t · assembly in the Object Holder](#m-rs) → [Assembly Line · 30 s · 64 000 EU/t (needs the orb)](#m-al) (also ZPM Circuit Assembler · 10 s · 38 400 EU/t · Cleanroom → [Assembly Line · 30 s · 64 000 EU/t (needs the orb)](#m-al))

### Direct steps

- QRAM chip x12 → Wetware printed board · 2 wetware processor · 3 living inductor · 6 living capacitor · 6 QRAM chip · 16 fine YBCO wire (6)
- Wetware processor assembly x2 (ZPM circuit) → Printed board · 2 assembly · 4 living diode · 12 QRAM · 24 NOR · 48 NAND · 32 fine YBCO wire · 2 europium plate · 864 mB ITLC solder · 576 mB PBI (2)

## How to build

1. Drawers first, one per input: RAM wafers, SiC over bismuth tritelluride dust, QRAM chips (Keep Exact 12), NOR chips (24), NAND chips (48), printed boards, processors, living SMDs, YBCO wire, europium plates. Drums: radon, ITLC soldering alloy, PBI. — `functionalstorage:oak_1`, `gtceu:ram_wafer`, `kubejs:qram_chip`, `gtceu:nand_memory_chip`
2. Sterile corner: ZPM chemical reactor (wafer + 2 dust + 500 mB radon → QRAM wafer, 60 s), then a LuV cutter next to it (wafer → 12 chips, 45 s). A router or a Robot Arm cover moves the wafer; both machines inside the Sterile Cleanroom. — `gtceu:zpm_chemical_reactor`, `kubejs:qram_wafer`, `gtceu:luv_cutter`
3. Assembly assembler (ZPM circuit assembler, normal cleanroom): board + 2 processors + 3 living inductors + 6 living capacitors + 6 QRAM + 16 fine YBCO → 2 assemblies per 10 s. — `gtceu:zpm_circuit_assembler`, `gtceu:wetware_processor_assembly`
4. Research: a data orb + 1 assembly in the Object Holder, 64 CWU/t at 38 400 EU/t, then the orb into the Assembly Line Data Access Hatch (zpm\_data). — `gtceu:research_station`, `gtceu:data_orb`, `gtceu:wetware_processor_assembly`
5. Computer: Assembly Line buses in recipe order, 864 mB solder + 576 mB PBI by hatches; 30 s at 64 000 EU/t. Output drawer Keep Exact 4. — `gtceu:assembly_line`, `gtceu:wetware_processor_computer`
6. Easy to miss: the computer is BOTH the UV circuit that the era multis ask for and the input of the UHV mainframe (2 per mainframe). Route the first ones to the multis, do not lock them in the mainframe line yet. — `gtceu:wetware_processor_computer`, `functionalstorage:oak_1`

## Tips

- QRAM (kjs circuits.js): chemical reactor, Sterile Cleanroom, 1200 ticks at VHA\[ZPM\] (61 440 EU/t): 1 RAM wafer + 2 silicon carbide over bismuth tritelluride dust + 500 mB radon → 1 QRAM wafer; cutter, Sterile Cleanroom, 900 ticks at VA\[LuV\]: 1 wafer → 12 QRAM chips. The wafer needs a ZPM reactor (61 440 EU/t &gt; LuV 32 768). Both machines sit in the STERILE cleanroom of bio line 1/2. Unverified: where silicon carbide over bismuth tritelluride dust comes from.
- Wetware processor assembly (ZPM circuit; pack recipe, circuits.js): circuit assembler, Cleanroom, 200 ticks at 38 400 EU/t: 1 wetware printed circuit board + 2 wetware processors + 3 living inductors + 6 living capacitors + 6 QRAM chips + 16 fine YBCO wire → 2 assemblies. The GT recipe (wetware\_processor\_assembly\_zpm) still exists too: 400 ticks, printed board + 2 processors + 6 advanced SMD inductors + 12 advanced SMD capacitors + 24 RAM chips + 16 fine YBCO wire with double solder → 2 assemblies; it needs no living SMDs and no QRAM.
- Wetware Processor Computer (UV circuit; pack recipe, assemblyLineCircuitRS): printed board + 2 assemblies + 4 living diodes + 12 QRAM + 24 NOR chips + 48 NAND chips + 32 fine YBCO wire + 2 europium plates, fluids 864 mB indium tin lead cadmium soldering alloy + 576 mB PBI, 600 ticks at 64 000 EU/t, STATION research of the processor assembly at 64 CWU/t, 38 400 EU/t. The GT recipe (wetware\_super\_computer\_uv) and its research are removed in the pack, so no scanner route. 64 000 EU/t is a ZPM-tier recipe (Assembly Line on a ZPM or 4A hatch).
- CWU: 64 CWU/t is 4 HPCA advanced computation components at 16 each, and each of those makes 4 cooling units of heat; an HPCA has 9 component slots and an active cooler gives 2 cooling, so one HPCA tops out around 48 CWU/t (3 advanced + 6 active coolers). 64 CWU/t therefore needs two or three HPCAs with bridge components joined by a Network Switch (uv\_research; the quest text confirms the switch routes several HPCAs into the Research Station).
- Costs for ONE computer (an assembly craft gives 2 assemblies = exactly what the computer eats): 1 assembly craft (1 printed board, 2 processors = 1 processor craft = 1 neuro unit + 1 crystal CPU + 1 nano CPU chip, 3 living inductors, 6 living capacitors, 6 QRAM, 16 fine YBCO) + 1 computer craft (1 printed board, 4 living diodes, 12 QRAM, 24 NOR, 48 NAND, 32 fine YBCO, 2 europium plates). Totals per computer: 1 neuro unit (16 stem cells), 2 printed boards, 18 QRAM chips (1.5 wafers), 24 NOR + 48 NAND chips. So 4 UV circuits via this route are 4 neuro units, 8 printed boards (one board run of 16), 72 QRAM chips (6 wafers), 96 NOR and 192 NAND chips; compare the crystal mainframe route of zpm\_uv\_circuit.
- Sub-steps people skip: (1) the research writes onto a data carrier (a data MODULE at 64 CWU/t, see uv\_data; Unverified for the fork) that goes into the Assembly Line’s Data Access Hatch; (2) QRAM is made in the sterile cleanroom, the assemblers in the normal one; (3) keep Keep Exact 12 on the QRAM drawer and 48 on NAND; (4) 64 000 EU/t for 600 ticks is 38 MEU per computer, size the substation first.
- **Unverified** NOR/NAND chip routes at this volume; silicon carbide over bismuth tritelluride dust source.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:zpm_circuit_assembler` | 1 |
| `gtceu:zpm_chemical_reactor` | 1 |
| `gtceu:luv_cutter` | 1 |
| `gtceu:zpm_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 16 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `gtceu:wetware_processor_assembly`, `gtceu:wetware_processor_computer`, `kubejs:qram_chip`, `kubejs:qram_wafer`
