---
kind: chain
id: zpm_hatches
order: 1460
data:
  t: |-
    ZPM Energy Input Hatch: europium voltage coils → Assembly Line (station research 8 CWU/t), then the ZPM transformer and 4A hatch
  inf: true
  "n":
    - - vg
      - "1 magnetic samarium rod · 16 fine europium wire"
      - g
      - functionalstorage:oak_1
      - [[Magnetic samarium rod, "gtceu:magnetic_samarium_rod"], [Fine europium wire, "gtceu:fine_europium_wire"]]
    - [vm, "Large Assembler on a LuV 4A hatch · circuit 1 · 10 s · 122 880 EU/t", m, "gtceu:large_assembler"]
    - [vc, "ZPM Voltage Coil · 2 per hatch", x, "gtceu:zpm_voltage_coil"]
    - - hg
      - ZPM hull · 4 VG cable · 2 UHPIC chip · 1 ZPM circuit · 2 voltage coil · 8 B sodium potassium · 1440 mB solder
      - g
      - functionalstorage:oak_1
      - - [ZPM Machine Hull, "gtceu:zpm_machine_hull"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [Sodium potassium, "gtceu:sodium_potassium_bucket"]
        - [VG single cable, "gtceu:vanadium_gallium_single_cable"]
    - [al, "Assembly Line · 30 s · 122 880 EU/t (station: LuV hatch, 8 CWU/t)", m, "gtceu:assembly_line"]
    - [eh, "ZPM Energy Input Hatch (1A)", o, "gtceu:zpm_energy_input_hatch"]
    - - tg
      - ZPM hull · 1 YBCO cable · 4 VG cable · 2 UHPIC chip
      - g
      - functionalstorage:oak_1
      - - [ZPM Machine Hull, "gtceu:zpm_machine_hull"]
        - [YBCO single cable, "gtceu:yttrium_barium_cuprate_single_cable"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
    - [ta, "LV Assembler · 5 ticks · 30 EU/t", m, "gtceu:lv_assembler"]
    - [tr, ZPM Transformer 1A, x, "gtceu:zpm_transformer_1a"]
    - - g4
      - transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder
      - g
      - functionalstorage:oak_1
      - - [VG quadruple wire, "gtceu:vanadium_gallium_quadruple_wire"]
        - [Naquadah alloy plate, "gtceu:naquadah_alloy_plate"]
    - [a4, "Large Assembler on a LuV 4A hatch · 5 s · 61 440 EU/t", m, "gtceu:large_assembler"]
    - [o4, ZPM Energy Input Hatch 4A, o, "gtceu:zpm_energy_input_hatch_4a"]
  e:
    - [vg, vm, "1"]
    - [vm, vc, "1 / 10 s"]
    - [vc, hg, "2"]
    - [hg, al, "1"]
    - [al, eh, "1 / 30 s"]
    - [tg, ta, "1"]
    - [ta, tr, "1"]
    - [tr, g4, "1"]
    - [eh, g4, "1"]
    - [vc, g4, "1"]
    - [g4, a4, "1"]
    - [a4, o4, "1 / 5 s"]
  tips:
    - |-
      Voltage coil (AssemblerRecipeLoader voltage_coil_zpm, not changed by the pack): 1 magnetic samarium rod + 16 fine EUROPIUM wire, circuit 1, 200 ticks at VA[ZPM] = 122 880 EU/t. Two per hatch (2 x 2 ingots of europium). The LuV coil was osmiridium, the IV one iridium; the ZPM one is europium, so the fusion reactor is again the source. 122 880 EU/t means the Large Assembler on a LuV 4A hatch (4 x 32 768 = 131 072 EU/t) or a ZPM assembler.
    - |-
      ZPM Energy Input Hatch (MetaTileEntityMachineRecipeLoader energy_hatch_zpm): ZPM hull + 4 vanadium gallium single cables + 2 UHPIC chips + 1 ZPM circuit + 2 ZPM voltage coils + 8 B sodium potassium + 1440 mB soldering alloy, Assembly Line, 600 ticks (30 s) at 122 880 EU/t, STATION research of the LuV energy input hatch at 8 CWU/t (the LuV hatch must be kept as the scan item). Dynamo (output) hatch: same but 4 vanadium gallium SPRINGS instead of cables, station research of the LuV dynamo hatch. The quest: the 4A LuV hatch gives ZPM recipe speeds; this hatch is the first real ZPM power.
    - |-
      UHPIC chip: HPIC wafer + 8 indium gallium phosphide dust + 576 mB molten naquadah, chemical reactor in the cleanroom, 1200 ticks at 30 720 EU/t, then a cutter (LuV, 900 ticks, 2 chips per wafer) — the luv_fusion chain has the numbers. 2 per hatch, 2 per transformer, 64 per LuV fusion reactor, 96 per ZPM fusion reactor. Sodium potassium: 1 sodium + 1 potassium dust → 1 B in a chemical reactor (iv_hatches chain).
    - |-
      Transformer and 4A (pack, tiered_machines/transformers.js and large_energy_hatches.js): ZPM Transformer 1A = ZPM hull + 1 yttrium barium cuprate single cable + 4 VG single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t, or a shaped craft). ZPM 4A hatch = transformer 1A + ZPM energy input hatch + 2 VG quadruple wire + 1 ZPM voltage coil + 2 naquadah alloy plates + 288 mB soldering alloy, assembler 100 ticks at 61 440 EU/t (EU x 2). The 16A hatch: 4A transformer + 4A hatch + 2 VG quadruple wire + 2 voltage coils + 4 plates + 576 mB solder, 200 ticks at 92 160 EU/t. Yttrium barium cuprate single cable needs the same PPS + PVC foil + silicone wrap as every cable above LuV; YBCO from the pack route is Unverified (check EMI).
    - |-
      Order: you need the ZPM hull first (zpm_hull), the Research Station running (the hatch recipe is STATION research, 8 CWU/t, zpm_data) and a ZPM circuit. With the hull and the research done, the hatch itself is one Assembly Line craft, so the whole chain waits on the circuits, europium and UHPIC chips, not on a new machine.
    - |-
      Sub-steps people skip: (1) the scan item is the LuV HATCH, so keep one LuV energy input hatch aside; (2) two voltage coils per hatch, four for a hatch + 4A; (3) 8 B sodium potassium is a lot: a full drum before the craft; (4) the 4A hatch consumes the 1A hatch, so make one 1A hatch more than you need machines; (5) the Assembly Line itself needs the LuV 4A hatch (zpm tier for the 122 880 EU/t recipe), not a ZPM one, because the ZPM one is the product.
    - |-
      Unverified: the CWU duration of the 8 CWU/t research, the YBCO cable source, and the efficiency of a LuV 4A hatch on this Assembly Line recipe (the luv_hatches chain says it should work, quest text says ZPM speeds).
  b:
    - ["gtceu:large_assembler", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 2]
    - ["gtceu:lv_assembler", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:magnetic_samarium_rod", "gtceu:fine_europium_wire", "gtceu:uhpic_chip"]
      t: |-
        Drawers first, one per input: magnetic samarium rods, fine europium wire, UHPIC chips, ZPM circuits, VG single cables, ZPM hulls. Drums: sodium potassium, soldering alloy. Every machine gets its own drawers behind Modular Routers or Pipez pipes with Item Filters and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:large_assembler", "gtceu:zpm_voltage_coil"]
      t: |-
        Voltage coils: the Large Assembler on a LuV 4A hatch, circuit 1, 1 magnetic samarium rod + 16 fine europium wire → 1 coil in 10 s at 122 880 EU/t. Output drawer Keep Exact 4.
    - i: ["gtceu:research_station", "gtceu:luv_energy_input_hatch", "gtceu:data_orb"]
      t: |-
        Station research: a data orb + a LuV energy input hatch in the Object Holder, 8 CWU/t, then the orb into the Assembly Line’s Data Access Hatch (zpm_data). Do the same with a LuV dynamo hatch for the dynamo recipe.
    - i: ["gtceu:assembly_line", "gtceu:zpm_machine_hull", "gtceu:zpm_energy_input_hatch"]
      t: |-
        Hatch: Assembly Line buses in recipe order: ZPM hull, 4 VG cables, 2 UHPIC chips, 1 ZPM circuit, 2 voltage coils; hatches: 8 B sodium potassium + 1440 mB soldering alloy. 30 s at 122 880 EU/t on the LuV 4A hatch → ZPM Energy Input Hatch.
    - i: ["gtceu:lv_assembler", "gtceu:zpm_transformer_1a"]
      t: |-
        Transformer: hull + 1 YBCO cable + 4 VG cables + 2 UHPIC chips in an LV Assembler (5 ticks at 30 EU/t) or by hand: that is only the carrier for the 4A hatch.
    - i: ["gtceu:large_assembler", "gtceu:zpm_energy_input_hatch_4a"]
      t: |-
        4A hatch: Large Assembler, transformer + ZPM energy input hatch + 2 VG quadruple wire + voltage coil + 2 naquadah alloy plates + 288 mB solder → 4A hatch in 5 s at 61 440 EU/t. Needed for the hungry multis (EBF at 9000 K, Large Mixer).
    - i: ["functionalstorage:oak_1", "gtceu:zpm_energy_input_hatch"]
      t: |-
        Easy to miss: a ZPM hatch only supplies the machine it is built into; the line still needs ZPM-rated cables (dragonsteel superconductor in zpm_urd, or YBCO/VG cables) and a transformer from your IV/LuV net.
---
# ZPM Energy Input Hatch: europium voltage coils → Assembly Line (station research 8 CWU/t), then the ZPM transformer and 4A hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM hull, hatch and components](../../plan/p12.md#zpmmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-vm">
<div class="gt-head"><span class="gt-mname">Large Assembler on a LuV 4A hatch · circuit 1 · 10 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 magnetic samarium rod · 16 fine europium wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 magnetic samarium rod · 16 fine europium wire</span><span class="gt-sub"><span>Magnetic samarium rod</span><span>Fine europium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Voltage Coil · 2 per hatch (gtceu:zpm_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Voltage Coil</span><span class="gt-note">ZPM Voltage Coil · 2 per hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 122 880 EU/t (station: LuV hatch, 8 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 4 VG cable · 2 UHPIC chip · 1 ZPM circuit · 2 voltage coil · 8 B sodium potassium · 1440 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 4 VG cable · 2 UHPIC chip · 1 ZPM circuit · 2 voltage coil · 8 B sodium potassium · 1440 mB solder</span><span class="gt-sub"><span>ZPM Machine Hull</span><span>UHPIC chip</span><span>Sodium potassium</span><span>VG single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Energy Input Hatch (1A) (gtceu:zpm_energy_input_hatch) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Energy Input Hatch</span><span class="gt-note">ZPM Energy Input Hatch (1A)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-lv" id="m-ta">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 ticks · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 1 YBCO cable · 4 VG cable · 2 UHPIC chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 1 YBCO cable · 4 VG cable · 2 UHPIC chip</span><span class="gt-sub"><span>ZPM Machine Hull</span><span>YBCO single cable</span><span>UHPIC chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Transformer 1A (gtceu:zpm_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Transformer 1a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Large Assembler on a LuV 4A hatch · 5 s · 61 440 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder</span><span class="gt-sub"><span>VG quadruple wire</span><span>Naquadah alloy plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Energy Input Hatch 4A (gtceu:zpm_energy_input_hatch_4a) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Energy Input Hatch 4a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
</div>

## Flow

- [Large Assembler on a LuV 4A hatch · circuit 1 · 10 s · 122 880 EU/t](#m-vm) → [Assembly Line · 30 s · 122 880 EU/t (station: LuV hatch, 8 CWU/t)](#m-al) → [Large Assembler on a LuV 4A hatch · 5 s · 61 440 EU/t](#m-a4) (also Large Assembler on a LuV 4A hatch · circuit 1 · 10 s · 122 880 EU/t → [Large Assembler on a LuV 4A hatch · 5 s · 61 440 EU/t](#m-a4))
- [LV Assembler · 5 ticks · 30 EU/t](#m-ta) → [Large Assembler on a LuV 4A hatch · 5 s · 61 440 EU/t](#m-a4)

### Direct steps

- ZPM Voltage Coil · 2 per hatch → ZPM hull · 4 VG cable · 2 UHPIC chip · 1 ZPM circuit · 2 voltage coil · 8 B sodium potassium · 1440 mB solder (2)
- ZPM Transformer 1A → transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder (1)
- ZPM Energy Input Hatch (1A) → transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder (1)
- ZPM Voltage Coil · 2 per hatch → transformer · ZPM hatch · 2 VG quadruple wire · 1 voltage coil · 2 naquadah alloy plate · 288 mB solder (1)

## How to build

1. Drawers first, one per input: magnetic samarium rods, fine europium wire, UHPIC chips, ZPM circuits, VG single cables, ZPM hulls. Drums: sodium potassium, soldering alloy. Every machine gets its own drawers behind Modular Routers or Pipez pipes with Item Filters and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:magnetic_samarium_rod`, `gtceu:fine_europium_wire`, `gtceu:uhpic_chip`
2. Voltage coils: the Large Assembler on a LuV 4A hatch, circuit 1, 1 magnetic samarium rod + 16 fine europium wire → 1 coil in 10 s at 122 880 EU/t. Output drawer Keep Exact 4. — `gtceu:large_assembler`, `gtceu:zpm_voltage_coil`
3. Station research: a data orb + a LuV energy input hatch in the Object Holder, 8 CWU/t, then the orb into the Assembly Line’s Data Access Hatch (zpm\_data). Do the same with a LuV dynamo hatch for the dynamo recipe. — `gtceu:research_station`, `gtceu:luv_energy_input_hatch`, `gtceu:data_orb`
4. Hatch: Assembly Line buses in recipe order: ZPM hull, 4 VG cables, 2 UHPIC chips, 1 ZPM circuit, 2 voltage coils; hatches: 8 B sodium potassium + 1440 mB soldering alloy. 30 s at 122 880 EU/t on the LuV 4A hatch → ZPM Energy Input Hatch. — `gtceu:assembly_line`, `gtceu:zpm_machine_hull`, `gtceu:zpm_energy_input_hatch`
5. Transformer: hull + 1 YBCO cable + 4 VG cables + 2 UHPIC chips in an LV Assembler (5 ticks at 30 EU/t) or by hand: that is only the carrier for the 4A hatch. — `gtceu:lv_assembler`, `gtceu:zpm_transformer_1a`
6. 4A hatch: Large Assembler, transformer + ZPM energy input hatch + 2 VG quadruple wire + voltage coil + 2 naquadah alloy plates + 288 mB solder → 4A hatch in 5 s at 61 440 EU/t. Needed for the hungry multis (EBF at 9000 K, Large Mixer). — `gtceu:large_assembler`, `gtceu:zpm_energy_input_hatch_4a`
7. Easy to miss: a ZPM hatch only supplies the machine it is built into; the line still needs ZPM-rated cables (dragonsteel superconductor in zpm\_urd, or YBCO/VG cables) and a transformer from your IV/LuV net. — `functionalstorage:oak_1`, `gtceu:zpm_energy_input_hatch`

## Tips

- Voltage coil (AssemblerRecipeLoader voltage\_coil\_zpm, not changed by the pack): 1 magnetic samarium rod + 16 fine EUROPIUM wire, circuit 1, 200 ticks at VA\[ZPM\] = 122 880 EU/t. Two per hatch (2 x 2 ingots of europium). The LuV coil was osmiridium, the IV one iridium; the ZPM one is europium, so the fusion reactor is again the source. 122 880 EU/t means the Large Assembler on a LuV 4A hatch (4 x 32 768 = 131 072 EU/t) or a ZPM assembler.
- ZPM Energy Input Hatch (MetaTileEntityMachineRecipeLoader energy\_hatch\_zpm): ZPM hull + 4 vanadium gallium single cables + 2 UHPIC chips + 1 ZPM circuit + 2 ZPM voltage coils + 8 B sodium potassium + 1440 mB soldering alloy, Assembly Line, 600 ticks (30 s) at 122 880 EU/t, STATION research of the LuV energy input hatch at 8 CWU/t (the LuV hatch must be kept as the scan item). Dynamo (output) hatch: same but 4 vanadium gallium SPRINGS instead of cables, station research of the LuV dynamo hatch. The quest: the 4A LuV hatch gives ZPM recipe speeds; this hatch is the first real ZPM power.
- UHPIC chip: HPIC wafer + 8 indium gallium phosphide dust + 576 mB molten naquadah, chemical reactor in the cleanroom, 1200 ticks at 30 720 EU/t, then a cutter (LuV, 900 ticks, 2 chips per wafer) — the luv\_fusion chain has the numbers. 2 per hatch, 2 per transformer, 64 per LuV fusion reactor, 96 per ZPM fusion reactor. Sodium potassium: 1 sodium + 1 potassium dust → 1 B in a chemical reactor (iv\_hatches chain).
- Transformer and 4A (pack, tiered\_machines/transformers.js and large\_energy\_hatches.js): ZPM Transformer 1A = ZPM hull + 1 yttrium barium cuprate single cable + 4 VG single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t, or a shaped craft). ZPM 4A hatch = transformer 1A + ZPM energy input hatch + 2 VG quadruple wire + 1 ZPM voltage coil + 2 naquadah alloy plates + 288 mB soldering alloy, assembler 100 ticks at 61 440 EU/t (EU x 2). The 16A hatch: 4A transformer + 4A hatch + 2 VG quadruple wire + 2 voltage coils + 4 plates + 576 mB solder, 200 ticks at 92 160 EU/t. Yttrium barium cuprate single cable needs the same PPS + PVC foil + silicone wrap as every cable above LuV; YBCO from the pack route is Unverified (check EMI).
- Order: you need the ZPM hull first (zpm\_hull), the Research Station running (the hatch recipe is STATION research, 8 CWU/t, zpm\_data) and a ZPM circuit. With the hull and the research done, the hatch itself is one Assembly Line craft, so the whole chain waits on the circuits, europium and UHPIC chips, not on a new machine.
- Sub-steps people skip: (1) the scan item is the LuV HATCH, so keep one LuV energy input hatch aside; (2) two voltage coils per hatch, four for a hatch + 4A; (3) 8 B sodium potassium is a lot: a full drum before the craft; (4) the 4A hatch consumes the 1A hatch, so make one 1A hatch more than you need machines; (5) the Assembly Line itself needs the LuV 4A hatch (zpm tier for the 122 880 EU/t recipe), not a ZPM one, because the ZPM one is the product.
- **Unverified** the CWU duration of the 8 CWU/t research, the YBCO cable source, and the efficiency of a LuV 4A hatch on this Assembly Line recipe (the luv\_hatches chain says it should work, quest text says ZPM speeds).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_assembler` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 2 |
| `gtceu:lv_assembler` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:zpm_energy_input_hatch`, `gtceu:zpm_voltage_coil`, `gtceu:zpm_energy_input_hatch_4a`, `gtceu:zpm_transformer_1a`, `gtceu:uhpic_chip`
