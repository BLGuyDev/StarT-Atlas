---
kind: chain
id: uv_hatches
order: 1650
data:
  t: |-
    UV Energy Input Hatch: dysprosium voltage coils → Assembly Line (station research 64 CWU/t), then the UV transformer and 4A hatch
  inf: true
  "n":
    - - vg
      - "1 magnetic dysprosium rod · 16 fine tritanium wire"
      - g
      - functionalstorage:oak_1
      - - [Magnetic dysprosium rod, "gtceu:magnetic_dysprosium_rod"]
        - [Fine tritanium wire, "gtceu:fine_tritanium_wire"]
    - [vm, "Large Assembler on a ZPM 4A hatch · circuit 1 · 10 s · 491 520 EU/t", m, "gtceu:large_assembler"]
    - [vc, "UV Voltage Coil · 2 per hatch", x, "gtceu:uv_voltage_coil"]
    - - hg
      - UV hull · 4 YBCO cable · 2 UHPIC chip · 1 UV circuit · 2 voltage coil · 10 B sodium potassium · 2880 mB solder
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [YBCO single cable, "gtceu:yttrium_barium_cuprate_single_cable"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [Sodium potassium, "gtceu:sodium_potassium_bucket"]
        - [UV circuit, "gtceu:wetware_processor_computer"]
    - - rs
      - Research Station · 64 CWU/t · 122 880 EU/t · ZPM hatch in the Object Holder
      - m
      - gtceu:research_station
    - [al, "Assembly Line · 40 s · 491 520 EU/t", m, "gtceu:assembly_line"]
    - [eh, "UV Energy Input Hatch (1A)", o, "gtceu:uv_energy_input_hatch"]
    - - tg
      - UV hull · 1 europium cable · 4 YBCO cable · 2 UHPIC chip
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [Europium single cable, "gtceu:europium_single_cable"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
    - [ta, "LV Assembler · 5 ticks · 30 EU/t", m, "gtceu:lv_assembler"]
    - [tr, UV Transformer 1A, x, "gtceu:uv_transformer_1a"]
    - - g4
      - transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder
      - g
      - functionalstorage:oak_1
      - - [YBCO quadruple wire, "gtceu:yttrium_barium_cuprate_quadruple_wire"]
        - [Darmstadtium plate, "gtceu:darmstadtium_plate"]
    - [a4, "Large Assembler on a ZPM 4A hatch · 5 s · 245 760 EU/t", m, "gtceu:large_assembler"]
    - [o4, UV Energy Input Hatch 4A, o, "gtceu:uv_energy_input_hatch_4a"]
  e:
    - [vg, vm, "1"]
    - [vm, vc, "1 / 10 s"]
    - [vc, hg, "2"]
    - [hg, al, "1"]
    - [rs, al, data orb]
    - [al, eh, "1 / 40 s"]
    - [tg, ta, "1"]
    - [ta, tr, "1"]
    - [tr, g4, "1"]
    - [eh, g4, "1"]
    - [vc, g4, "1"]
    - [g4, a4, "1"]
    - [a4, o4, "1 / 5 s"]
  tips:
    - |-
      Voltage coil (pack, kjs additions/recipe_changes.js; the GT recipe is removed): assembler, circuit 1, 1 magnetic dysprosium rod + 16 fine TRITANIUM wire, 200 ticks at VA[UV] = 491 520 EU/t, which is above 131 072 V: the machine must be a UV assembler or the Large Assembler on a ZPM 4A hatch. Two coils per hatch (4 tritanium ingots). The ZPM coil used europium; this one needs the fusion-made tritanium (uv_fusion_mats) and a magnetized dysprosium rod (dysprosium source Unverified: the rare earth line of the Abydos pages).
    - |-
      UV Energy Input Hatch (gtsrc MetaTileEntityMachineRecipeLoader energy_hatch_uv, not changed by the pack): UV hull + 4 YBCO single cables + 2 UHPIC chips + 1 circuit of the UV tag + 2 UV voltage coils + 10 B sodium potassium + 2880 mB soldering alloy (20 x 144, the PLAIN soldering alloy), Assembly Line, 800 ticks (40 s) at 491 520 EU/t, STATION research of the ZPM energy input hatch at 64 CWU/t and 122 880 EU/t. Dynamo (output) hatch: same with 4 YBCO SPRINGS instead of cables, research of the ZPM dynamo hatch.
    - |-
      Transformer and 4A (pack, transformers.js and large_energy_hatches.js): UV Transformer 1A = UV hull + 1 europium single cable + 4 YBCO single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t, or the shaped craft). UV 4A hatch = transformer 1A + UV energy input hatch + 2 YBCO quadruple wire + 1 UV voltage coil + 2 darmstadtium plates + 432 mB indium tin lead cadmium soldering alloy, assembler 100 ticks at 245 760 EU/t (EU x 2 with EU = VA[ZPM]). 16A hatch: 4A transformer + 4A hatch + 2 YBCO quadruple wire + 2 coils + 4 plates + 864 mB solder, 200 ticks at 368 640 EU/t. 64A substation hatch: 16A transformer + 16A hatch + 2 YBCO HEX wire + 3 coils + 6 plates + 1296 mB solder, 400 ticks at 491 520 EU/t.
    - |-
      UV I/O hatches and buses (kjs tiered_machines/io_hatches.js, the GT recipes are removed): bus = UV hull + 1 enriched naquadah crate (start_core) + 324 mB PEEK, assembler, 300 ticks at 491 520 EU/t, circuit 1 input / 2 output; hatch = UV hull + 1 enriched naquadah drum + 324 mB PEEK, same numbers; dual hatch = bus + hatch + 1 naquadah NONUPLE fluid pipe + 3 darmstadtium frames + 1296 mB PEEK. All 491 520 EU/t, so a UV assembler or the Large Assembler on a ZPM 4A hatch again.
    - |-
      UV circuit here: the crystal mainframe (zpm_uv_circuit) or the wetware computer (uv_wetware2) both count; so does the runic assembly / draconic processor (Unverified, never needed). 64 CWU/t research: 4 advanced HPCA components; one HPCA only gives about 48 CWU/t, so several HPCAs with bridges through a Network Switch (uv_research).
    - |-
      Sub-steps people skip: (1) the scan item is the ZPM HATCH: keep one ZPM energy input hatch and one dynamo hatch aside, never use them in a machine; (2) 4 YBCO cables per hatch + 2 per hull: the YBCO cable line (uv_hull) runs for hours; (3) 10 B sodium potassium per hatch: a full drum before the craft; (4) the 4A hatch eats the 1A hatch, so make one more 1A hatch than you need; (5) the first UV assembler is built from the hull with a Large Assembler on a ZPM 4A hatch because it is its own prerequisite.
    - |-
      Unverified: dysprosium source, the CWU duration of the 64 CWU/t research, and whether a ZPM 4A hatch really runs UV recipes (quest text says so).
  b:
    - ["gtceu:large_assembler", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:zpm_energy_input_hatch_4a", 2]
    - ["gtceu:lv_assembler", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:magnetic_dysprosium_rod", "gtceu:fine_tritanium_wire", "gtceu:uhpic_chip"]
      t: |-
        Drawers first, one per input: magnetic dysprosium rods, fine tritanium wire, UHPIC chips, UV circuits, YBCO single cables, UV hulls, europium cables. Drums: sodium potassium, soldering alloy, ITLC soldering alloy, PEEK. Every machine gets its own drawers behind Modular Routers or Pipez pipes with Item Filters and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:large_assembler", "gtceu:uv_voltage_coil"]
      t: |-
        Voltage coils: Large Assembler on a ZPM 4A hatch, circuit 1, magnetic dysprosium rod + 16 fine tritanium wire → 1 coil in 10 s at 491 520 EU/t. Output drawer Keep Exact 4.
    - i: ["gtceu:research_station", "gtceu:zpm_energy_input_hatch", "gtceu:data_orb"]
      t: |-
        Station research: a data orb + a ZPM energy input hatch in the Object Holder, 64 CWU/t at 122 880 EU/t, then the orb into the Assembly Line’s Data Access Hatch. Repeat with a ZPM dynamo hatch for the dynamo recipe.
    - i: ["gtceu:assembly_line", "gtceu:uv_machine_hull", "gtceu:uv_energy_input_hatch"]
      t: |-
        Hatch: Assembly Line buses in recipe order: UV hull, 4 YBCO cables, 2 UHPIC chips, 1 UV circuit, 2 voltage coils; hatches: 10 B sodium potassium + 2880 mB soldering alloy. 40 s at 491 520 EU/t → UV Energy Input Hatch.
    - i: ["gtceu:lv_assembler", "gtceu:uv_transformer_1a"]
      t: |-
        Transformer: hull + 1 europium cable + 4 YBCO cables + 2 UHPIC chips in an LV Assembler (5 ticks at 30 EU/t) or by hand; it is only the carrier for the 4A hatch.
    - i: ["gtceu:large_assembler", "gtceu:uv_energy_input_hatch_4a"]
      t: |-
        4A hatch: Large Assembler, transformer + UV energy input hatch + 2 YBCO quadruple wire + voltage coil + 2 darmstadtium plates + 432 mB solder → 4A hatch in 5 s at 245 760 EU/t. Needed for the hungry UV multis and the polyimide reactors.
    - i: ["functionalstorage:oak_1", "gtceu:uv_energy_input_hatch"]
      t: |-
        Easy to miss: a UV hatch only supplies the machine it is built into; the line still needs UV-rated cables (YBCO) or superconductors and a transformer from your ZPM net.
---
# UV Energy Input Hatch: dysprosium voltage coils → Assembly Line (station research 64 CWU/t), then the UV transformer and 4A hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV components and hatches](../../plan/p16.md#uvmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-vm">
<div class="gt-head"><span class="gt-mname">Large Assembler on a ZPM 4A hatch · circuit 1 · 10 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 magnetic dysprosium rod · 16 fine tritanium wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 magnetic dysprosium rod · 16 fine tritanium wire</span><span class="gt-sub"><span>Magnetic dysprosium rod</span><span>Fine tritanium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Voltage Coil · 2 per hatch (gtceu:uv_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Voltage Coil</span><span class="gt-note">UV Voltage Coil · 2 per hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 64 CWU/t · 122 880 EU/t · ZPM hatch in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 40 s · 491 520 EU/t (gtceu:assembly_line) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 40 s · 491 520 EU/t</span><b class="gt-q">data orb</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · 4 YBCO cable · 2 UHPIC chip · 1 UV circuit · 2 voltage coil · 10 B sodium potassium · 2880 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · 4 YBCO cable · 2 UHPIC chip · 1 UV circuit · 2 voltage coil · 10 B sodium potassium · 2880 mB solder</span><span class="gt-sub"><span>UV Machine Hull</span><span>YBCO single cable</span><span>UHPIC chip</span><span>Sodium potassium</span><span>UV circuit</span></span><b class="gt-q">1</b></span><a class="gt-slot gt-mach" href="#m-rs" title="Research Station · 64 CWU/t · 122 880 EU/t · ZPM hatch in the Object Holder (gtceu:research_station) - data orb"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station · 64 CWU/t · 122 880 EU/t · ZPM hatch in the Object Holder</span><b class="gt-q">data orb</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Energy Input Hatch (1A) (gtceu:uv_energy_input_hatch) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Energy Input Hatch</span><span class="gt-note">UV Energy Input Hatch (1A)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-lv" id="m-ta">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 ticks · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · 1 europium cable · 4 YBCO cable · 2 UHPIC chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · 1 europium cable · 4 YBCO cable · 2 UHPIC chip</span><span class="gt-sub"><span>UV Machine Hull</span><span>Europium single cable</span><span>UHPIC chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Transformer 1A (gtceu:uv_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uv_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Transformer 1a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Large Assembler on a ZPM 4A hatch · 5 s · 245 760 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder</span><span class="gt-sub"><span>YBCO quadruple wire</span><span>Darmstadtium plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Energy Input Hatch 4A (gtceu:uv_energy_input_hatch_4a) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Energy Input Hatch 4a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
</div>

## Flow

- [Large Assembler on a ZPM 4A hatch · circuit 1 · 10 s · 491 520 EU/t](#m-vm) → [Assembly Line · 40 s · 491 520 EU/t](#m-al) → [Large Assembler on a ZPM 4A hatch · 5 s · 245 760 EU/t](#m-a4) (also Large Assembler on a ZPM 4A hatch · circuit 1 · 10 s · 491 520 EU/t → [Large Assembler on a ZPM 4A hatch · 5 s · 245 760 EU/t](#m-a4))
- [Research Station · 64 CWU/t · 122 880 EU/t · ZPM hatch in the Object Holder](#m-rs) → [Assembly Line · 40 s · 491 520 EU/t](#m-al)
- [LV Assembler · 5 ticks · 30 EU/t](#m-ta) → [Large Assembler on a ZPM 4A hatch · 5 s · 245 760 EU/t](#m-a4)

### Direct steps

- UV Voltage Coil · 2 per hatch → UV hull · 4 YBCO cable · 2 UHPIC chip · 1 UV circuit · 2 voltage coil · 10 B sodium potassium · 2880 mB solder (2)
- UV Transformer 1A → transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder (1)
- UV Energy Input Hatch (1A) → transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder (1)
- UV Voltage Coil · 2 per hatch → transformer · UV hatch · 2 YBCO quadruple wire · 1 voltage coil · 2 darmstadtium plate · 432 mB ITLC solder (1)

## How to build

1. Drawers first, one per input: magnetic dysprosium rods, fine tritanium wire, UHPIC chips, UV circuits, YBCO single cables, UV hulls, europium cables. Drums: sodium potassium, soldering alloy, ITLC soldering alloy, PEEK. Every machine gets its own drawers behind Modular Routers or Pipez pipes with Item Filters and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:magnetic_dysprosium_rod`, `gtceu:fine_tritanium_wire`, `gtceu:uhpic_chip`
2. Voltage coils: Large Assembler on a ZPM 4A hatch, circuit 1, magnetic dysprosium rod + 16 fine tritanium wire → 1 coil in 10 s at 491 520 EU/t. Output drawer Keep Exact 4. — `gtceu:large_assembler`, `gtceu:uv_voltage_coil`
3. Station research: a data orb + a ZPM energy input hatch in the Object Holder, 64 CWU/t at 122 880 EU/t, then the orb into the Assembly Line’s Data Access Hatch. Repeat with a ZPM dynamo hatch for the dynamo recipe. — `gtceu:research_station`, `gtceu:zpm_energy_input_hatch`, `gtceu:data_orb`
4. Hatch: Assembly Line buses in recipe order: UV hull, 4 YBCO cables, 2 UHPIC chips, 1 UV circuit, 2 voltage coils; hatches: 10 B sodium potassium + 2880 mB soldering alloy. 40 s at 491 520 EU/t → UV Energy Input Hatch. — `gtceu:assembly_line`, `gtceu:uv_machine_hull`, `gtceu:uv_energy_input_hatch`
5. Transformer: hull + 1 europium cable + 4 YBCO cables + 2 UHPIC chips in an LV Assembler (5 ticks at 30 EU/t) or by hand; it is only the carrier for the 4A hatch. — `gtceu:lv_assembler`, `gtceu:uv_transformer_1a`
6. 4A hatch: Large Assembler, transformer + UV energy input hatch + 2 YBCO quadruple wire + voltage coil + 2 darmstadtium plates + 432 mB solder → 4A hatch in 5 s at 245 760 EU/t. Needed for the hungry UV multis and the polyimide reactors. — `gtceu:large_assembler`, `gtceu:uv_energy_input_hatch_4a`
7. Easy to miss: a UV hatch only supplies the machine it is built into; the line still needs UV-rated cables (YBCO) or superconductors and a transformer from your ZPM net. — `functionalstorage:oak_1`, `gtceu:uv_energy_input_hatch`

## Tips

- Voltage coil (pack, kjs additions/recipe\_changes.js; the GT recipe is removed): assembler, circuit 1, 1 magnetic dysprosium rod + 16 fine TRITANIUM wire, 200 ticks at VA\[UV\] = 491 520 EU/t, which is above 131 072 V: the machine must be a UV assembler or the Large Assembler on a ZPM 4A hatch. Two coils per hatch (4 tritanium ingots). The ZPM coil used europium; this one needs the fusion-made tritanium (uv\_fusion\_mats) and a magnetized dysprosium rod (dysprosium source Unverified: the rare earth line of the Abydos pages).
- UV Energy Input Hatch (gtsrc MetaTileEntityMachineRecipeLoader energy\_hatch\_uv, not changed by the pack): UV hull + 4 YBCO single cables + 2 UHPIC chips + 1 circuit of the UV tag + 2 UV voltage coils + 10 B sodium potassium + 2880 mB soldering alloy (20 x 144, the PLAIN soldering alloy), Assembly Line, 800 ticks (40 s) at 491 520 EU/t, STATION research of the ZPM energy input hatch at 64 CWU/t and 122 880 EU/t. Dynamo (output) hatch: same with 4 YBCO SPRINGS instead of cables, research of the ZPM dynamo hatch.
- Transformer and 4A (pack, transformers.js and large\_energy\_hatches.js): UV Transformer 1A = UV hull + 1 europium single cable + 4 YBCO single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t, or the shaped craft). UV 4A hatch = transformer 1A + UV energy input hatch + 2 YBCO quadruple wire + 1 UV voltage coil + 2 darmstadtium plates + 432 mB indium tin lead cadmium soldering alloy, assembler 100 ticks at 245 760 EU/t (EU x 2 with EU = VA\[ZPM\]). 16A hatch: 4A transformer + 4A hatch + 2 YBCO quadruple wire + 2 coils + 4 plates + 864 mB solder, 200 ticks at 368 640 EU/t. 64A substation hatch: 16A transformer + 16A hatch + 2 YBCO HEX wire + 3 coils + 6 plates + 1296 mB solder, 400 ticks at 491 520 EU/t.
- UV I/O hatches and buses (kjs tiered\_machines/io\_hatches.js, the GT recipes are removed): bus = UV hull + 1 enriched naquadah crate (start\_core) + 324 mB PEEK, assembler, 300 ticks at 491 520 EU/t, circuit 1 input / 2 output; hatch = UV hull + 1 enriched naquadah drum + 324 mB PEEK, same numbers; dual hatch = bus + hatch + 1 naquadah NONUPLE fluid pipe + 3 darmstadtium frames + 1296 mB PEEK. All 491 520 EU/t, so a UV assembler or the Large Assembler on a ZPM 4A hatch again.
- UV circuit here: the crystal mainframe (zpm\_uv\_circuit) or the wetware computer (uv\_wetware2) both count; so does the runic assembly / draconic processor (Unverified, never needed). 64 CWU/t research: 4 advanced HPCA components; one HPCA only gives about 48 CWU/t, so several HPCAs with bridges through a Network Switch (uv\_research).
- Sub-steps people skip: (1) the scan item is the ZPM HATCH: keep one ZPM energy input hatch and one dynamo hatch aside, never use them in a machine; (2) 4 YBCO cables per hatch + 2 per hull: the YBCO cable line (uv\_hull) runs for hours; (3) 10 B sodium potassium per hatch: a full drum before the craft; (4) the 4A hatch eats the 1A hatch, so make one more 1A hatch than you need; (5) the first UV assembler is built from the hull with a Large Assembler on a ZPM 4A hatch because it is its own prerequisite.
- **Unverified** dysprosium source, the CWU duration of the 64 CWU/t research, and whether a ZPM 4A hatch really runs UV recipes (quest text says so).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_assembler` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:zpm_energy_input_hatch_4a` | 2 |
| `gtceu:lv_assembler` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:uv_energy_input_hatch`, `gtceu:uv_voltage_coil`, `gtceu:uv_energy_input_hatch_4a`, `gtceu:uv_transformer_1a`, `gtceu:uv_energy_output_hatch`
