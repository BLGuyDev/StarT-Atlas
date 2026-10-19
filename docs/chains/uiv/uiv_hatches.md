---
kind: chain
id: uiv_hatches
order: 2080
data:
  t: |-
    UIV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches
  inf: true
  "n":
    - - g1
      - |-
        UIV energy input hatch: 1 uiv machine hull · 4 polonium bismide single cable · 2 uepic chip · 1 UIV circuit · 2 uiv voltage coil · 24 000 mB sodium potassium · 11 520 mB indium tin lead cadmium soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
        - [uepic chip, "kubejs:uepic_chip"]
        - [UIV circuit, "kubejs:uiv_universal_circuit"]
        - [uiv voltage coil, "kubejs:uiv_voltage_coil"]
    - [al, "Assembly Line · 40 s · 31 457 280 EU/t · research of the UEV hatch 256 CWU/t", m, "gtceu:assembly_line"]
    - [eh, "UIV Energy Input Hatch (output: 4 springs instead of cables)", x, "gtceu:uiv_energy_input_hatch"]
    - - g2
      - |-
        UIV transformer 1A: 1 uiv machine hull · 1 lepton resonant thallium antimonide single cable · 4 polonium bismide single cable · 2 uepic chip
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [lepton resonant thallium antimonide single cable, "gtceu:lepton_resonant_thallium_antimonide_single_cable"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
        - [uepic chip, "kubejs:uepic_chip"]
    - [a2, "Assembler · 5 ticks · 30 EU/t", m, "gtceu:lv_assembler"]
    - - tr
      - UIV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)
      - x
      - gtceu:uiv_transformer_1a
    - - g3
      - |-
        UIV 4A hatch: 1 uiv transformer 1a · 1 uiv energy input hatch · 2 polonium bismide quadruple wire · 1 uiv voltage coil · 2 chaotixic alloy plate · 864 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uiv transformer 1a, "gtceu:uiv_transformer_1a"]
        - [uiv energy input hatch, "gtceu:uiv_energy_input_hatch"]
        - [polonium bismide quadruple wire, "gtceu:polonium_bismide_quadruple_wire"]
        - [uiv voltage coil, "kubejs:uiv_voltage_coil"]
        - [chaotixic alloy plate, "gtceu:chaotixic_alloy_plate"]
    - [a3, "Assembler · 5 s / 10 s / 20 s · 15 728 640 to 31 457 280 EU/t", m, "gtceu:lv_assembler"]
    - [mh, "UIV 4A, 16A and 64A energy hatches", x, "gtceu:uiv_energy_input_hatch_4a"]
    - - g4
      - |-
        UIV 256A laser target hatch: 1 uiv substation input hatch 64a · 1 diamond lens · 1 uiv sensor · 1 uiv electric pump · 4 polonium bismide single cable · 3 456 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uiv substation input hatch 64a, "gtceu:uiv_substation_input_hatch_64a"]
        - [diamond lens, "gtceu:diamond_lens"]
        - [uiv sensor, "gtceu:uiv_sensor"]
        - [uiv electric pump, "gtceu:uiv_electric_pump"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
    - [a4, "Assembler · 30 s / 45 s / 60 s · 31 457 280 EU/t", m, "gtceu:lv_assembler"]
    - [lh, "UIV 256A, 1024A and 4096A laser hatches", o, "gtceu:uiv_256a_laser_target_hatch"]
  e:
    - [g1, al, "1"]
    - [al, eh, "1 / 40 s"]
    - [g2, a2, "1"]
    - [a2, tr, "1"]
    - [eh, a3, "1"]
    - [tr, a3, "1"]
    - [g3, a3, "1"]
    - [a3, mh, "1"]
    - [mh, a4, "1"]
    - [g4, a4, "1"]
    - [a4, lh, "1"]
  tips:
    - |-
      Source: kjs additions/machines_and_parts/tiered_machines/singleblocks.js (postUVMachines), transformers.js, large_energy_hatches.js, modular_power_hatches.js, parallel_hatches.js, hatches_and_busses.js. The pack removes all gtceu:uiv recipes (singleblocks.js top) and re-adds only a short list (hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder, fusion reactor), so anything else must come from a multiblock or the recipe browser. There are NO UIV input/output hatches or buses (io_hatches.js stops at UHV: the comment says UEV and above scale like UHV): use UHV item and fluid hatches, UHV dual hatches and the UHV 4x / 9x hatches on UIV multiblocks.
    - |-
      Energy hatch (assembly line, 800 ticks = 40 s): UIV hull + 4 polonium bismide single cables (the output hatch uses 4 springs) + 2 UEPIC chips + 1 UIV circuit + 2 UIV voltage coils + 24 000 mB sodium potassium + 11 520 mB indium tin lead cadmium soldering alloy, 31 457 280 EU/t, station research of the UEV energy hatch (7 864 320 EU/t, 256 CWU/t). Output hatch is the same with the spring and the output version of the research.
    - |-
      Transformer (assembler, 5 ticks, 30 EU/t, or crafting table with chips): UIV hull (1A) or the previous transformer + 1 lepton resonant thallium antimonide cable + 4 polonium bismide cables + 2 UEPIC chips; thickness single, double, quadruple, hex for 1A, 2A, 4A, 16A.
    - |-
      Multi-amp: 4A = transformer 1A + energy hatch + 2 polonium bismide quadruple wire + 1 voltage coil + 2 chaotixic alloy plates + 864 mB solder (100 ticks, 15 728 640 EU/t); 16A = transformer 4A + 4A hatch + 2 quadruple wire + 2 coils + 4 plates + 1728 mB (200 ticks, x3); 64A substation hatch = transformer 16A + 16A hatch + 2 hex wire + 3 coils + 6 plates + 2592 mB (400 ticks, x4). Lasers: 256A = 64A hatch + diamond lens + sensor/emitter + pump + 4 single cables + 3456 mB (600 ticks); 1024A doubles lens/parts, 4320 mB (900 ticks); 4096A quadruples them, 5184 mB (1200 ticks). Target hatch uses the sensor, source (output) hatch the emitter. All x4 EU of the scaling voltage 7 864 320.
    - |-
      Parallel hatches (parallel_hatches.js): shaped, sensor + emitter + 4 circuits of the NEXT tier (UXV, the abyssal processor mainframe) + UIV hull + 2 polonium bismide double cables, then the absolute parallel hatch = it + 4 sensors + 4 emitters + 2 next-tier circuits + 4 UIPIC chips + 576 mB calamatium, assembler 16 s at 7 864 320 EU/t. So the UIV parallel hatch is a UIV-era item that needs the abyssal mainframe. Modular conduit node/terminal hatches (modular_power_hatches.js) are hatch + sensor/emitter + 2 cables, circuit 2, 5 ticks.
    - |-
      Sub-steps people skip: (1) the energy hatch needs the voltage coil of THIS tier (part of uiv_parts); (2) the research item is the UEV energy hatch, scanned in the Research Station; (3) sodium potassium in bulk: 24 000 mB per hatch; (4) at UIV voltage a 4A hatch is cheaper than 4 plain ones.
    - |-
      Unverified: the recipes of the tier cables and wires themselves (polonium bismide is a superconductor-style material), the sodium potassium supply, and the sterile cleaning maintenance hatch (a UEV Assembly Line item: hull + 2 robot arms + emitter + 3 UEV circuits, listed in hatches_and_busses.js).
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:lv_assembler", 2]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uiv_machine_hull", "kubejs:uepic_chip"]
      t: |-
        Drawers first: UIV hull, UEPIC chips (Keep Exact 16), the UIV voltage coil, UIV circuits, polonium bismide single cables and springs. Drums: sodium potassium, soldering alloy. One dedicated machine per product, each behind its own router or Pipez item pipe with Item Filters and a Robot Arm Keep Exact.
    - i: ["gtceu:research_station", "gtceu:uev_energy_input_hatch"]
      t: |-
        Research once: scan the UEV energy input hatch (and the output hatch if you want dynamos), 256 CWU/t. Data item into the Assembly Line.
    - i: ["gtceu:assembly_line", "gtceu:uiv_energy_input_hatch"]
      t: |-
        Assembly Line: 40 s per hatch at 31 457 280 EU/t with the two fluids by Pipez fluid pipes. Output drawer Keep Exact 4.
    - i: ["gtceu:uiv_transformer_1a", "gtceu:lv_assembler"]
      t: |-
        Transformers on a plain assembler: hull (1A) or the previous transformer + cables + chips, 5 ticks. Build 1A, then 2A, 4A, 16A in order, each its own drawer.
    - i: ["gtceu:uiv_energy_input_hatch_4a", "gtceu:uiv_substation_input_hatch_64a"]
      t: |-
        Multi-amp hatches: transformer + the smaller hatch + wire + coils + plates + solder; 4A, 16A, 64A in order.
    - i: ["gtceu:uiv_256a_laser_target_hatch", "gtceu:diamond_lens"]
      t: |-
        Lasers last: 64A hatch + diamond lens + sensor/emitter + pump + cables; target hatch for consumers, source hatch for generators. Keep the sensor, emitter and pump from uiv_components.
---
# UIV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV hull, parts, hatches and components](../../plan/p19.md#uivmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s · 31 457 280 EU/t · research of the UEV hatch 256 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UIV energy input hatch: 1 uiv machine hull · 4 polonium bismide single cable · 2 uepic chip · 1 UIV circuit · 2 uiv voltage coil · 24 000 mB sodium potassium · 11 520 mB indium tin lead cadmium soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIV energy input hatch: 1 uiv machine hull · 4 polonium bismide single cable · 2 uepic chip · 1 UIV circuit · 2 uiv voltage coil · 24 000 mB sodium potassium · 11 520 mB indium tin lead cadmium soldering alloy</span><span class="gt-sub"><span>uiv machine hull</span><span>polonium bismide single cable</span><span>uepic chip</span><span>UIV circuit</span><span>uiv voltage coil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Energy Input Hatch (output: 4 springs instead of cables) (gtceu:uiv_energy_input_hatch) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Energy Input Hatch</span><span class="gt-note">UIV Energy Input Hatch (output: 4 springs instead of cables)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembler · 5 ticks · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UIV transformer 1A: 1 uiv machine hull · 1 lepton resonant thallium antimonide single cable · 4 polonium bismide single cable · 2 uepic chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIV transformer 1A: 1 uiv machine hull · 1 lepton resonant thallium antimonide single cable · 4 polonium bismide single cable · 2 uepic chip</span><span class="gt-sub"><span>uiv machine hull</span><span>lepton resonant thallium antimonide single cable</span><span>polonium bismide single cable</span><span>uepic chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer) (gtceu:uiv_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Transformer 1a</span><span class="gt-note">UIV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s / 10 s / 20 s · 15 728 640 to 31 457 280 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UIV Energy Input Hatch (output: 4 springs instead of cables) (gtceu:uiv_energy_input_hatch) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Energy Input Hatch</span><span class="gt-note">UIV Energy Input Hatch (output: 4 springs instead of cables)</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer) (gtceu:uiv_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Transformer 1a</span><span class="gt-note">UIV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="UIV 4A hatch: 1 uiv transformer 1a · 1 uiv energy input hatch · 2 polonium bismide quadruple wire · 1 uiv voltage coil · 2 chaotixic alloy plate · 864 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIV 4A hatch: 1 uiv transformer 1a · 1 uiv energy input hatch · 2 polonium bismide quadruple wire · 1 uiv voltage coil · 2 chaotixic alloy plate · 864 mB naquadated soldering alloy</span><span class="gt-sub"><span>uiv transformer 1a</span><span>uiv energy input hatch</span><span>polonium bismide quadruple wire</span><span>uiv voltage coil</span><span>chaotixic alloy plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV 4A, 16A and 64A energy hatches (gtceu:uiv_energy_input_hatch_4a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Energy Input Hatch 4a</span><span class="gt-note">UIV 4A, 16A and 64A energy hatches</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembler · 30 s / 45 s / 60 s · 31 457 280 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UIV 4A, 16A and 64A energy hatches (gtceu:uiv_energy_input_hatch_4a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Energy Input Hatch 4a</span><span class="gt-note">UIV 4A, 16A and 64A energy hatches</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="UIV 256A laser target hatch: 1 uiv substation input hatch 64a · 1 diamond lens · 1 uiv sensor · 1 uiv electric pump · 4 polonium bismide single cable · 3 456 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIV 256A laser target hatch: 1 uiv substation input hatch 64a · 1 diamond lens · 1 uiv sensor · 1 uiv electric pump · 4 polonium bismide single cable · 3 456 mB naquadated soldering alloy</span><span class="gt-sub"><span>uiv substation input hatch 64a</span><span>diamond lens</span><span>uiv sensor</span><span>uiv electric pump</span><span>polonium bismide single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UIV 256A, 1024A and 4096A laser hatches (gtceu:uiv_256a_laser_target_hatch) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_256a_laser_target_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV 256a Laser Target Hatch</span><span class="gt-note">UIV 256A, 1024A and 4096A laser hatches</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembly Line · 40 s · 31 457 280 EU/t · research of the UEV hatch 256 CWU/t](#m-al) → [Assembler · 5 s / 10 s / 20 s · 15 728 640 to 31 457 280 EU/t](#m-a3) → [Assembler · 30 s / 45 s / 60 s · 31 457 280 EU/t](#m-a4)
- [Assembler · 5 ticks · 30 EU/t](#m-a2) → [Assembler · 5 s / 10 s / 20 s · 15 728 640 to 31 457 280 EU/t](#m-a3)

## How to build

1. Drawers first: UIV hull, UEPIC chips (Keep Exact 16), the UIV voltage coil, UIV circuits, polonium bismide single cables and springs. Drums: sodium potassium, soldering alloy. One dedicated machine per product, each behind its own router or Pipez item pipe with Item Filters and a Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:uiv_machine_hull`, `kubejs:uepic_chip`
2. Research once: scan the UEV energy input hatch (and the output hatch if you want dynamos), 256 CWU/t. Data item into the Assembly Line. — `gtceu:research_station`, `gtceu:uev_energy_input_hatch`
3. Assembly Line: 40 s per hatch at 31 457 280 EU/t with the two fluids by Pipez fluid pipes. Output drawer Keep Exact 4. — `gtceu:assembly_line`, `gtceu:uiv_energy_input_hatch`
4. Transformers on a plain assembler: hull (1A) or the previous transformer + cables + chips, 5 ticks. Build 1A, then 2A, 4A, 16A in order, each its own drawer. — `gtceu:uiv_transformer_1a`, `gtceu:lv_assembler`
5. Multi-amp hatches: transformer + the smaller hatch + wire + coils + plates + solder; 4A, 16A, 64A in order. — `gtceu:uiv_energy_input_hatch_4a`, `gtceu:uiv_substation_input_hatch_64a`
6. Lasers last: 64A hatch + diamond lens + sensor/emitter + pump + cables; target hatch for consumers, source hatch for generators. Keep the sensor, emitter and pump from uiv\_components. — `gtceu:uiv_256a_laser_target_hatch`, `gtceu:diamond_lens`

## Tips

- Source: kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js (postUVMachines), transformers.js, large\_energy\_hatches.js, modular\_power\_hatches.js, parallel\_hatches.js, hatches\_and\_busses.js. The pack removes all gtceu:uiv recipes (singleblocks.js top) and re-adds only a short list (hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder, fusion reactor), so anything else must come from a multiblock or the recipe browser. There are NO UIV input/output hatches or buses (io\_hatches.js stops at UHV: the comment says UEV and above scale like UHV): use UHV item and fluid hatches, UHV dual hatches and the UHV 4x / 9x hatches on UIV multiblocks.
- Energy hatch (assembly line, 800 ticks = 40 s): UIV hull + 4 polonium bismide single cables (the output hatch uses 4 springs) + 2 UEPIC chips + 1 UIV circuit + 2 UIV voltage coils + 24 000 mB sodium potassium + 11 520 mB indium tin lead cadmium soldering alloy, 31 457 280 EU/t, station research of the UEV energy hatch (7 864 320 EU/t, 256 CWU/t). Output hatch is the same with the spring and the output version of the research.
- Transformer (assembler, 5 ticks, 30 EU/t, or crafting table with chips): UIV hull (1A) or the previous transformer + 1 lepton resonant thallium antimonide cable + 4 polonium bismide cables + 2 UEPIC chips; thickness single, double, quadruple, hex for 1A, 2A, 4A, 16A.
- Multi-amp: 4A = transformer 1A + energy hatch + 2 polonium bismide quadruple wire + 1 voltage coil + 2 chaotixic alloy plates + 864 mB solder (100 ticks, 15 728 640 EU/t); 16A = transformer 4A + 4A hatch + 2 quadruple wire + 2 coils + 4 plates + 1728 mB (200 ticks, x3); 64A substation hatch = transformer 16A + 16A hatch + 2 hex wire + 3 coils + 6 plates + 2592 mB (400 ticks, x4). Lasers: 256A = 64A hatch + diamond lens + sensor/emitter + pump + 4 single cables + 3456 mB (600 ticks); 1024A doubles lens/parts, 4320 mB (900 ticks); 4096A quadruples them, 5184 mB (1200 ticks). Target hatch uses the sensor, source (output) hatch the emitter. All x4 EU of the scaling voltage 7 864 320.
- Parallel hatches (parallel\_hatches.js): shaped, sensor + emitter + 4 circuits of the NEXT tier (UXV, the abyssal processor mainframe) + UIV hull + 2 polonium bismide double cables, then the absolute parallel hatch = it + 4 sensors + 4 emitters + 2 next-tier circuits + 4 UIPIC chips + 576 mB calamatium, assembler 16 s at 7 864 320 EU/t. So the UIV parallel hatch is a UIV-era item that needs the abyssal mainframe. Modular conduit node/terminal hatches (modular\_power\_hatches.js) are hatch + sensor/emitter + 2 cables, circuit 2, 5 ticks.
- Sub-steps people skip: (1) the energy hatch needs the voltage coil of THIS tier (part of uiv\_parts); (2) the research item is the UEV energy hatch, scanned in the Research Station; (3) sodium potassium in bulk: 24 000 mB per hatch; (4) at UIV voltage a 4A hatch is cheaper than 4 plain ones.
- **Unverified** the recipes of the tier cables and wires themselves (polonium bismide is a superconductor-style material), the sodium potassium supply, and the sterile cleaning maintenance hatch (a UEV Assembly Line item: hull + 2 robot arms + emitter + 3 UEV circuits, listed in hatches\_and\_busses.js).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:lv_assembler` | 2 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:uiv_energy_input_hatch`, `gtceu:uiv_energy_output_hatch`, `gtceu:uiv_transformer_1a`, `gtceu:uiv_transformer_2a`, `gtceu:uiv_transformer_4a`, `gtceu:uiv_transformer_16a`, `gtceu:uiv_energy_input_hatch_4a`, `gtceu:uiv_energy_input_hatch_16a`, `gtceu:uiv_substation_input_hatch_64a`, `gtceu:uiv_256a_laser_target_hatch`, `gtceu:uiv_1024a_laser_target_hatch`, `gtceu:uiv_4096a_laser_target_hatch`, `gtceu:uiv_256a_laser_source_hatch`, `gtceu:uiv_energy_output_hatch_4a`
