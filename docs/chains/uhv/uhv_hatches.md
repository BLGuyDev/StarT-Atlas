---
kind: chain
id: uhv_hatches
order: 1870
data:
  t: |-
    UHV Energy Input Hatch: UHV voltage coils (Component Part Assembly) → Assembly Line (research 128 CWU/t, 1 966 080 EU/t), then transformer, 4A hatch and I/O hatches
  inf: true
  "n":
    - [vc, "2 UHV voltage coil (uhv_parts)", x, "kubejs:uhv_voltage_coil"]
    - - hg
      - UHV hull · 4 europium cable · 2 UHPIC chip · UHV circuit · 2 voltage coil · 16 B sodium potassium · 2880 mB ITLC solder
      - g
      - functionalstorage:oak_1
      - - [UHV Machine Hull, "gtceu:uhv_machine_hull"]
        - [Europium single cable, "gtceu:europium_single_cable"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [Sodium potassium, "gtceu:sodium_potassium_bucket"]
        - [UHV circuit, "gtceu:wetware_processor_mainframe"]
    - - rs
      - Research Station · 128 CWU/t · 491 520 EU/t · UV hatch in the Object Holder
      - m
      - gtceu:research_station
    - [al, "Assembly Line · 40 s · 1 966 080 EU/t", m, "gtceu:assembly_line"]
    - [eh, "UHV Energy Input Hatch (1A)", o, "gtceu:uhv_energy_input_hatch"]
    - - tg
      - UHV hull · cerium tritelluride cable · 4 europium cable · 2 UHPIC chip
      - g
      - functionalstorage:oak_1
      - [[Cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]]
    - [ta, "LV Assembler · 5 ticks · 30 EU/t", m, "gtceu:lv_assembler"]
    - [tr, UHV Transformer 1A, x, "gtceu:uhv_transformer_1a"]
    - - g4
      - transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder
      - g
      - functionalstorage:oak_1
      - [[Europium quadruple wire, "gtceu:europium_quadruple_wire"], [Neutronium plate, "gtceu:neutronium_plate"]]
    - [a4, "UV Assembler · 5 s · 983 040 EU/t", m, "gtceu:large_assembler"]
    - [o4, UHV Energy Input Hatch 4A, o, "gtceu:uhv_energy_input_hatch_4a"]
    - - io
      - UHV hull · neutronium crate or drum · 360 mB PEEK → UHV input/output bus and hatch (assembler 15 s, 1 966 080 EU/t)
      - o
      - gtceu:uhv_input_bus
  e:
    - [vc, hg, "2"]
    - [hg, al, "1"]
    - [rs, al, data]
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
      UHV Energy Input Hatch (kjs tiered_machines/singleblocks.js postUVMachines energy hatch, math = scaler - 3 = 1; the GT recipe is removed): UHV hull + 4 EUROPIUM single cables + 2 UHPIC chips + 1 circuit of the UHV tag + 2 UHV voltage coils (kubejs) + 16 B sodium potassium (4000 x math + 12000) + 2880 mB ITLC soldering alloy (1440 x 2^math), Assembly Line, 800 ticks (40 s) at 491 520 x 4 = 1 966 080 EU/t, STATION research of the UV energy input hatch at 128 CWU/t (64 x math + 64) and 491 520 EU/t. Dynamo (output) hatch: 4 europium SPRINGS instead of cables, research of the UV dynamo hatch. The UHV voltage coil is the Component Part Assembly recipe of uhv_parts (liquid helium 1 B, TPD 241 wire).
    - |-
      Transformer and 4A (pack, transformers.js, large_energy_hatches.js): UHV Transformer 1A = UHV hull + 1 CERIUM TRITELLURIDE single cable + 4 europium single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t). UHV 4A hatch = transformer 1A + UHV energy input hatch + 2 europium quadruple wire + 1 UHV voltage coil (kubejs) + 2 neutronium plates + 576 mB ITLC solder, assembler 100 ticks at EU x 2 = 983 040 EU/t. 16A: 4A transformer + 4A hatch + 2 europium quadruple wire + 2 coils + 4 plates + 1152 mB solder, 200 ticks at 1 474 560 EU/t. 64A: hex wire, 3 coils, 6 plates, 1728 mB, 400 ticks at 1 966 080 EU/t. Cerium tritelluride: mixer, circuit 4, 1 cerium + 3 tellurium dust → 4 dust, 900 ticks at VHA[UHV] (kjs misc_materials.js); blast data 11 699 K, so its EBF needs ZALLOY coils (13 499 K, kubejs zalloy_coil_block: neutronium frame + 8 zalloy double wire + 8 zirconium foil + 32 fine RTAN wire + 16 neutronium silicon carbide foil + 144 mB tritanium, assembler 1000 ticks at 1 966 080 EU/t).
    - |-
      UHV I/O (kjs io_hatches.js, scaler 4): bus = UHV hull + 1 neutronium crate (start_core:neutronium_crate) + 360 mB PEEK (216 + 4 x 36), assembler 300 ticks at VA[IV] x 4^4 = 1 966 080 EU/t, circuit 1 input / 2 output; hatch = hull + neutronium drum + 360 mB PEEK; dual hatch = bus + hatch + 1 zapolgium NONUPLE fluid pipe + 3 neutronium frames + 1440 mB PEEK; plus UHV 4x / 9x input and output hatches (hatch + zapolgium quadruple / nonuple pipe, crafting table).
    - |-
      Power gate: the Assembly Line recipe is 1 966 080 EU/t (UHV tier): it needs a UV 4A hatch (2 097 152 EU/t) or a UHV hatch. The 4A step makes the UV 4A hatch the real UHV gateway; build 2 UV 4A hatches early (uv_hatches).
    - |-
      Sub-steps people skip: (1) the research item is the UV energy hatch: keep one UV hatch and one UV dynamo hatch aside; (2) 16 B sodium potassium per hatch; (3) a CPA recipe per voltage coil (200 ticks) and a helium line; (4) UHPIC chips 2 per hatch, 2 per transformer; (5) a cerium tritelluride cable needs zalloy coils: do not forget the coil line (uhv_alloys makes tritanium coils only).
    - |-
      Unverified: the zalloy-coil EBF gas, cerium and tellurium sources, 128 CWU/t data carrier.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 2]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:lv_assembler", 1]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:uhv_voltage_coil", "gtceu:europium_single_cable", "gtceu:uhpic_chip"]
      t: |-
        Drawers first, one per input: UHV voltage coils, europium cables / springs / quadruple wire, UHPIC chips, UHV circuits, hulls, cerium tritelluride cables, neutronium plates. Drums: sodium potassium, ITLC solder, PEEK.
    - i: ["gtceu:research_station", "gtceu:uv_energy_input_hatch", "gtceu:data_module"]
      t: |-
        Station research: a data module + a UV energy input hatch in the Object Holder, 128 CWU/t at 491 520 EU/t; repeat with the UV dynamo hatch.
    - i: ["gtceu:assembly_line", "gtceu:uhv_machine_hull", "gtceu:uhv_energy_input_hatch"]
      t: |-
        Hatch: Assembly Line on a UV 4A hatch: hull, 4 cables, 2 UHPIC chips, circuit, 2 voltage coils; 16 B sodium potassium + 2880 mB solder; 40 s.
    - i: ["gtceu:lv_assembler", "gtceu:uhv_transformer_1a"]
      t: |-
        Transformer (needs one cerium tritelluride cable) in an LV assembler: 5 ticks, 30 EU/t.
    - i: ["gtceu:large_assembler", "gtceu:uhv_energy_input_hatch_4a"]
      t: |-
        4A hatch: Large Assembler: transformer + 1A hatch + 2 quadruple wire + coil + 2 plates + 576 mB solder; 5 s at 983 040 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:uhv_energy_input_hatch"]
      t: |-
        Easy to miss: the 4A hatch eats the 1A hatch and a transformer: make 3 hatches per 4A hatch.
---
# UHV Energy Input Hatch: UHV voltage coils (Component Part Assembly) → Assembly Line (research 128 CWU/t, 1 966 080 EU/t), then transformer, 4A hatch and I/O hatches

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 128 CWU/t · 491 520 EU/t · UV hatch in the Object Holder</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · 40 s · 1 966 080 EU/t (gtceu:assembly_line) - data"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · 40 s · 1 966 080 EU/t</span><b class="gt-q">data</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s · 1 966 080 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 4 europium cable · 2 UHPIC chip · UHV circuit · 2 voltage coil · 16 B sodium potassium · 2880 mB ITLC solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 4 europium cable · 2 UHPIC chip · UHV circuit · 2 voltage coil · 16 B sodium potassium · 2880 mB ITLC solder</span><span class="gt-sub"><span>UHV Machine Hull</span><span>Europium single cable</span><span>UHPIC chip</span><span>Sodium potassium</span><span>UHV circuit</span></span><b class="gt-q">1</b></span><a class="gt-slot gt-mach" href="#m-rs" title="Research Station · 128 CWU/t · 491 520 EU/t · UV hatch in the Object Holder (gtceu:research_station) - data"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Research Station</span><span class="gt-note">Research Station · 128 CWU/t · 491 520 EU/t · UV hatch in the Object Holder</span><b class="gt-q">data</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UHV Energy Input Hatch (1A) (gtceu:uhv_energy_input_hatch) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Energy Input Hatch</span><span class="gt-note">UHV Energy Input Hatch (1A)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-lv" id="m-ta">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 ticks · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · cerium tritelluride cable · 4 europium cable · 2 UHPIC chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · cerium tritelluride cable · 4 europium cable · 2 UHPIC chip</span><span class="gt-sub"><span>Cerium tritelluride single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Transformer 1A (gtceu:uhv_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Transformer 1a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">UV Assembler · 5 s · 983 040 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder</span><span class="gt-sub"><span>Europium quadruple wire</span><span>Neutronium plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UHV Energy Input Hatch 4A (gtceu:uhv_energy_input_hatch_4a) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Energy Input Hatch 4a</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
</div>

## Flow

- [Research Station · 128 CWU/t · 491 520 EU/t · UV hatch in the Object Holder](#m-rs) → [Assembly Line · 40 s · 1 966 080 EU/t](#m-al) → [UV Assembler · 5 s · 983 040 EU/t](#m-a4)
- [LV Assembler · 5 ticks · 30 EU/t](#m-ta) → [UV Assembler · 5 s · 983 040 EU/t](#m-a4)

### Direct steps

- 2 UHV voltage coil (uhv\_parts) → UHV hull · 4 europium cable · 2 UHPIC chip · UHV circuit · 2 voltage coil · 16 B sodium potassium · 2880 mB ITLC solder (2)
- UHV Transformer 1A → transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder (1)
- UHV Energy Input Hatch (1A) → transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder (1)
- 2 UHV voltage coil (uhv\_parts) → transformer · UHV hatch · 2 europium quadruple wire · UHV voltage coil · 2 neutronium plate · 576 mB ITLC solder (1)

### Other items

UHV hull · neutronium crate or drum · 360 mB PEEK → UHV input/output bus and hatch (assembler 15 s, 1 966 080 EU/t)

## How to build

1. Drawers first, one per input: UHV voltage coils, europium cables / springs / quadruple wire, UHPIC chips, UHV circuits, hulls, cerium tritelluride cables, neutronium plates. Drums: sodium potassium, ITLC solder, PEEK. — `functionalstorage:oak_1`, `kubejs:uhv_voltage_coil`, `gtceu:europium_single_cable`, `gtceu:uhpic_chip`
2. Station research: a data module + a UV energy input hatch in the Object Holder, 128 CWU/t at 491 520 EU/t; repeat with the UV dynamo hatch. — `gtceu:research_station`, `gtceu:uv_energy_input_hatch`, `gtceu:data_module`
3. Hatch: Assembly Line on a UV 4A hatch: hull, 4 cables, 2 UHPIC chips, circuit, 2 voltage coils; 16 B sodium potassium + 2880 mB solder; 40 s. — `gtceu:assembly_line`, `gtceu:uhv_machine_hull`, `gtceu:uhv_energy_input_hatch`
4. Transformer (needs one cerium tritelluride cable) in an LV assembler: 5 ticks, 30 EU/t. — `gtceu:lv_assembler`, `gtceu:uhv_transformer_1a`
5. 4A hatch: Large Assembler: transformer + 1A hatch + 2 quadruple wire + coil + 2 plates + 576 mB solder; 5 s at 983 040 EU/t. — `gtceu:large_assembler`, `gtceu:uhv_energy_input_hatch_4a`
6. Easy to miss: the 4A hatch eats the 1A hatch and a transformer: make 3 hatches per 4A hatch. — `functionalstorage:oak_1`, `gtceu:uhv_energy_input_hatch`

## Tips

- UHV Energy Input Hatch (kjs tiered\_machines/singleblocks.js postUVMachines energy hatch, math = scaler - 3 = 1; the GT recipe is removed): UHV hull + 4 EUROPIUM single cables + 2 UHPIC chips + 1 circuit of the UHV tag + 2 UHV voltage coils (kubejs) + 16 B sodium potassium (4000 x math + 12000) + 2880 mB ITLC soldering alloy (1440 x 2^math), Assembly Line, 800 ticks (40 s) at 491 520 x 4 = 1 966 080 EU/t, STATION research of the UV energy input hatch at 128 CWU/t (64 x math + 64) and 491 520 EU/t. Dynamo (output) hatch: 4 europium SPRINGS instead of cables, research of the UV dynamo hatch. The UHV voltage coil is the Component Part Assembly recipe of uhv\_parts (liquid helium 1 B, TPD 241 wire).
- Transformer and 4A (pack, transformers.js, large\_energy\_hatches.js): UHV Transformer 1A = UHV hull + 1 CERIUM TRITELLURIDE single cable + 4 europium single cables + 2 UHPIC chips (assembler 5 ticks at 30 EU/t). UHV 4A hatch = transformer 1A + UHV energy input hatch + 2 europium quadruple wire + 1 UHV voltage coil (kubejs) + 2 neutronium plates + 576 mB ITLC solder, assembler 100 ticks at EU x 2 = 983 040 EU/t. 16A: 4A transformer + 4A hatch + 2 europium quadruple wire + 2 coils + 4 plates + 1152 mB solder, 200 ticks at 1 474 560 EU/t. 64A: hex wire, 3 coils, 6 plates, 1728 mB, 400 ticks at 1 966 080 EU/t. Cerium tritelluride: mixer, circuit 4, 1 cerium + 3 tellurium dust → 4 dust, 900 ticks at VHA\[UHV\] (kjs misc\_materials.js); blast data 11 699 K, so its EBF needs ZALLOY coils (13 499 K, kubejs zalloy\_coil\_block: neutronium frame + 8 zalloy double wire + 8 zirconium foil + 32 fine RTAN wire + 16 neutronium silicon carbide foil + 144 mB tritanium, assembler 1000 ticks at 1 966 080 EU/t).
- UHV I/O (kjs io\_hatches.js, scaler 4): bus = UHV hull + 1 neutronium crate (start\_core:neutronium\_crate) + 360 mB PEEK (216 + 4 x 36), assembler 300 ticks at VA\[IV\] x 4^4 = 1 966 080 EU/t, circuit 1 input / 2 output; hatch = hull + neutronium drum + 360 mB PEEK; dual hatch = bus + hatch + 1 zapolgium NONUPLE fluid pipe + 3 neutronium frames + 1440 mB PEEK; plus UHV 4x / 9x input and output hatches (hatch + zapolgium quadruple / nonuple pipe, crafting table).
- Power gate: the Assembly Line recipe is 1 966 080 EU/t (UHV tier): it needs a UV 4A hatch (2 097 152 EU/t) or a UHV hatch. The 4A step makes the UV 4A hatch the real UHV gateway; build 2 UV 4A hatches early (uv\_hatches).
- Sub-steps people skip: (1) the research item is the UV energy hatch: keep one UV hatch and one UV dynamo hatch aside; (2) 16 B sodium potassium per hatch; (3) a CPA recipe per voltage coil (200 ticks) and a helium line; (4) UHPIC chips 2 per hatch, 2 per transformer; (5) a cerium tritelluride cable needs zalloy coils: do not forget the coil line (uhv\_alloys makes tritanium coils only).
- **Unverified** the zalloy-coil EBF gas, cerium and tellurium sources, 128 CWU/t data carrier.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 2 |
| `gtceu:large_assembler` | 1 |
| `gtceu:lv_assembler` | 1 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:uhv_energy_input_hatch`, `gtceu:uhv_energy_input_hatch_4a`, `gtceu:uhv_transformer_1a`, `gtceu:cerium_tritelluride_single_cable`, `gtceu:uhv_energy_output_hatch`, `gtceu:uhv_input_bus`
