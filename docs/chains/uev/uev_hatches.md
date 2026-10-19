---
kind: chain
id: uev_hatches
order: 2070
data:
  t: |-
    UEV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches
  inf: true
  "n":
    - - g1
      - |-
        UEV energy input hatch: 1 uev machine hull · 4 cerium tritelluride single cable · 2 uepic chip · 1 UEV circuit · 2 uev voltage coil · 20 000 mB sodium potassium · 5 760 mB indium tin lead cadmium soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uev machine hull, "gtceu:uev_machine_hull"]
        - [cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]
        - [uepic chip, "kubejs:uepic_chip"]
        - [UEV circuit, "kubejs:uev_universal_circuit"]
        - [uev voltage coil, "kubejs:uev_voltage_coil"]
    - [al, "Assembly Line · 40 s · 7 864 320 EU/t · research of the UHV hatch 192 CWU/t", m, "gtceu:assembly_line"]
    - [eh, "UEV Energy Input Hatch (output: 4 springs instead of cables)", x, "gtceu:uev_energy_input_hatch"]
    - - g2
      - |-
        UEV transformer 1A: 1 uev machine hull · 1 polonium bismide single cable · 4 cerium tritelluride single cable · 2 uepic chip
      - g
      - functionalstorage:oak_1
      - - [uev machine hull, "gtceu:uev_machine_hull"]
        - [polonium bismide single cable, "gtceu:polonium_bismide_single_cable"]
        - [cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]
        - [uepic chip, "kubejs:uepic_chip"]
    - [a2, "Assembler · 5 ticks · 30 EU/t", m, "gtceu:lv_assembler"]
    - - tr
      - UEV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)
      - x
      - gtceu:uev_transformer_1a
    - - g3
      - |-
        UEV 4A hatch: 1 uev transformer 1a · 1 uev energy input hatch · 2 cerium tritelluride quadruple wire · 1 uev voltage coil · 2 mythrolic alloy plate · 720 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uev transformer 1a, "gtceu:uev_transformer_1a"]
        - [uev energy input hatch, "gtceu:uev_energy_input_hatch"]
        - [cerium tritelluride quadruple wire, "gtceu:cerium_tritelluride_quadruple_wire"]
        - [uev voltage coil, "kubejs:uev_voltage_coil"]
        - [mythrolic alloy plate, "gtceu:mythrolic_alloy_plate"]
    - [a3, "Assembler · 5 s / 10 s / 20 s · 3 932 160 to 7 864 320 EU/t", m, "gtceu:lv_assembler"]
    - [mh, "UEV 4A, 16A and 64A energy hatches", x, "gtceu:uev_energy_input_hatch_4a"]
    - - g4
      - |-
        UEV 256A laser target hatch: 1 uev substation input hatch 64a · 1 diamond lens · 1 uev sensor · 1 uev electric pump · 4 cerium tritelluride single cable · 2 880 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [uev substation input hatch 64a, "gtceu:uev_substation_input_hatch_64a"]
        - [diamond lens, "gtceu:diamond_lens"]
        - [uev sensor, "gtceu:uev_sensor"]
        - [uev electric pump, "gtceu:uev_electric_pump"]
        - [cerium tritelluride single cable, "gtceu:cerium_tritelluride_single_cable"]
    - [a4, "Assembler · 30 s / 45 s / 60 s · 7 864 320 EU/t", m, "gtceu:lv_assembler"]
    - [lh, "UEV 256A, 1024A and 4096A laser hatches", o, "gtceu:uev_256a_laser_target_hatch"]
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
      Source: kjs additions/machines_and_parts/tiered_machines/singleblocks.js (postUVMachines), transformers.js, large_energy_hatches.js, modular_power_hatches.js, parallel_hatches.js, hatches_and_busses.js. The pack removes all gtceu:uev recipes (singleblocks.js top) and re-adds only a short list (hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder, fusion reactor), so anything else must come from a multiblock or the recipe browser. There are NO UEV input/output hatches or buses (io_hatches.js stops at UHV: the comment says UEV and above scale like UHV): use UHV item and fluid hatches, UHV dual hatches and the UHV 4x / 9x hatches on UEV multiblocks.
    - |-
      Energy hatch (assembly line, 800 ticks = 40 s): UEV hull + 4 cerium tritelluride single cables (the output hatch uses 4 springs) + 2 UEPIC chips + 1 UEV circuit + 2 UEV voltage coils + 20 000 mB sodium potassium + 5 760 mB indium tin lead cadmium soldering alloy, 7 864 320 EU/t, station research of the UHV energy hatch (1 966 080 EU/t, 192 CWU/t). Output hatch is the same with the spring and the output version of the research.
    - |-
      Transformer (assembler, 5 ticks, 30 EU/t, or crafting table with chips): UEV hull (1A) or the previous transformer + 1 polonium bismide cable + 4 cerium tritelluride cables + 2 UEPIC chips; thickness single, double, quadruple, hex for 1A, 2A, 4A, 16A.
    - |-
      Multi-amp: 4A = transformer 1A + energy hatch + 2 cerium tritelluride quadruple wire + 1 voltage coil + 2 mythrolic alloy plates + 720 mB solder (100 ticks, 3 932 160 EU/t); 16A = transformer 4A + 4A hatch + 2 quadruple wire + 2 coils + 4 plates + 1440 mB (200 ticks, x3); 64A substation hatch = transformer 16A + 16A hatch + 2 hex wire + 3 coils + 6 plates + 2160 mB (400 ticks, x4). Lasers: 256A = 64A hatch + diamond lens + sensor/emitter + pump + 4 single cables + 2880 mB (600 ticks); 1024A doubles lens/parts, 3600 mB (900 ticks); 4096A quadruples them, 4320 mB (1200 ticks). Target hatch uses the sensor, source (output) hatch the emitter. All x4 EU of the scaling voltage 1 966 080.
    - |-
      Parallel hatches (parallel_hatches.js): shaped, sensor + emitter + 4 circuits of the NEXT tier (UIV) + UEV hull + 2 cerium tritelluride double cables, then the absolute parallel hatch = it + 4 sensors + 4 emitters + 2 next-tier circuits + 4 UEPIC chips + 576 mB isovol, assembler 16 s at 1 966 080 EU/t. So the UEV parallel hatch is a UIV-era item. Modular conduit node/terminal hatches (modular_power_hatches.js) are hatch + sensor/emitter + 2 cables, circuit 2, 5 ticks.
    - |-
      Sub-steps people skip: (1) the energy hatch needs the voltage coil of THIS tier (part of uev_parts); (2) the research item is the UHV energy hatch, scanned in the Research Station; (3) sodium potassium in bulk: 20 000 mB per hatch; (4) at UEV voltage a 4A hatch is cheaper than 4 plain ones.
    - |-
      Unverified: the recipes of the tier cables and wires themselves (cerium tritelluride is a superconductor-style material), the sodium potassium supply, and the sterile cleaning maintenance hatch (a UEV Assembly Line item: hull + 2 robot arms + emitter + 3 UEV circuits, listed in hatches_and_busses.js).
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
    - i: ["functionalstorage:oak_1", "gtceu:uev_machine_hull", "kubejs:uepic_chip"]
      t: |-
        Drawers first: UEV hull, UEPIC chips (Keep Exact 16), the UEV voltage coil, UEV circuits, cerium tritelluride single cables and springs. Drums: sodium potassium, soldering alloy. One dedicated machine per product, each behind its own router or Pipez item pipe with Item Filters and a Robot Arm Keep Exact.
    - i: ["gtceu:research_station", "gtceu:uhv_energy_input_hatch"]
      t: |-
        Research once: scan the UHV energy input hatch (and the output hatch if you want dynamos), 192 CWU/t. Data item into the Assembly Line.
    - i: ["gtceu:assembly_line", "gtceu:uev_energy_input_hatch"]
      t: |-
        Assembly Line: 40 s per hatch at 7 864 320 EU/t with the two fluids by Pipez fluid pipes. Output drawer Keep Exact 4.
    - i: ["gtceu:uev_transformer_1a", "gtceu:lv_assembler"]
      t: |-
        Transformers on a plain assembler: hull (1A) or the previous transformer + cables + chips, 5 ticks. Build 1A, then 2A, 4A, 16A in order, each its own drawer.
    - i: ["gtceu:uev_energy_input_hatch_4a", "gtceu:uev_substation_input_hatch_64a"]
      t: |-
        Multi-amp hatches: transformer + the smaller hatch + wire + coils + plates + solder; 4A, 16A, 64A in order.
    - i: ["gtceu:uev_256a_laser_target_hatch", "gtceu:diamond_lens"]
      t: |-
        Lasers last: 64A hatch + diamond lens + sensor/emitter + pump + cables; target hatch for consumers, source hatch for generators. Keep the sensor, emitter and pump from uev_components.
---
# UEV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 40 s · 7 864 320 EU/t · research of the UHV hatch 192 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UEV energy input hatch: 1 uev machine hull · 4 cerium tritelluride single cable · 2 uepic chip · 1 UEV circuit · 2 uev voltage coil · 20 000 mB sodium potassium · 5 760 mB indium tin lead cadmium soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UEV energy input hatch: 1 uev machine hull · 4 cerium tritelluride single cable · 2 uepic chip · 1 UEV circuit · 2 uev voltage coil · 20 000 mB sodium potassium · 5 760 mB indium tin lead cadmium soldering alloy</span><span class="gt-sub"><span>uev machine hull</span><span>cerium tritelluride single cable</span><span>uepic chip</span><span>UEV circuit</span><span>uev voltage coil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Energy Input Hatch (output: 4 springs instead of cables) (gtceu:uev_energy_input_hatch) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Energy Input Hatch</span><span class="gt-note">UEV Energy Input Hatch (output: 4 springs instead of cables)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembler · 5 ticks · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UEV transformer 1A: 1 uev machine hull · 1 polonium bismide single cable · 4 cerium tritelluride single cable · 2 uepic chip (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UEV transformer 1A: 1 uev machine hull · 1 polonium bismide single cable · 4 cerium tritelluride single cable · 2 uepic chip</span><span class="gt-sub"><span>uev machine hull</span><span>polonium bismide single cable</span><span>cerium tritelluride single cable</span><span>uepic chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer) (gtceu:uev_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Transformer 1a</span><span class="gt-note">UEV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s / 10 s / 20 s · 3 932 160 to 7 864 320 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UEV Energy Input Hatch (output: 4 springs instead of cables) (gtceu:uev_energy_input_hatch) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Energy Input Hatch</span><span class="gt-note">UEV Energy Input Hatch (output: 4 springs instead of cables)</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer) (gtceu:uev_transformer_1a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_transformer_1a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Transformer 1a</span><span class="gt-note">UEV Transformer 1A (2A, 4A, 16A repeat the recipe with the previous transformer)</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="UEV 4A hatch: 1 uev transformer 1a · 1 uev energy input hatch · 2 cerium tritelluride quadruple wire · 1 uev voltage coil · 2 mythrolic alloy plate · 720 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UEV 4A hatch: 1 uev transformer 1a · 1 uev energy input hatch · 2 cerium tritelluride quadruple wire · 1 uev voltage coil · 2 mythrolic alloy plate · 720 mB naquadated soldering alloy</span><span class="gt-sub"><span>uev transformer 1a</span><span>uev energy input hatch</span><span>cerium tritelluride quadruple wire</span><span>uev voltage coil</span><span>mythrolic alloy plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV 4A, 16A and 64A energy hatches (gtceu:uev_energy_input_hatch_4a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Energy Input Hatch 4a</span><span class="gt-note">UEV 4A, 16A and 64A energy hatches</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembler · 30 s / 45 s / 60 s · 7 864 320 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UEV 4A, 16A and 64A energy hatches (gtceu:uev_energy_input_hatch_4a) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Energy Input Hatch 4a</span><span class="gt-note">UEV 4A, 16A and 64A energy hatches</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="UEV 256A laser target hatch: 1 uev substation input hatch 64a · 1 diamond lens · 1 uev sensor · 1 uev electric pump · 4 cerium tritelluride single cable · 2 880 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UEV 256A laser target hatch: 1 uev substation input hatch 64a · 1 diamond lens · 1 uev sensor · 1 uev electric pump · 4 cerium tritelluride single cable · 2 880 mB naquadated soldering alloy</span><span class="gt-sub"><span>uev substation input hatch 64a</span><span>diamond lens</span><span>uev sensor</span><span>uev electric pump</span><span>cerium tritelluride single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UEV 256A, 1024A and 4096A laser hatches (gtceu:uev_256a_laser_target_hatch) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_256a_laser_target_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV 256a Laser Target Hatch</span><span class="gt-note">UEV 256A, 1024A and 4096A laser hatches</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembly Line · 40 s · 7 864 320 EU/t · research of the UHV hatch 192 CWU/t](#m-al) → [Assembler · 5 s / 10 s / 20 s · 3 932 160 to 7 864 320 EU/t](#m-a3) → [Assembler · 30 s / 45 s / 60 s · 7 864 320 EU/t](#m-a4)
- [Assembler · 5 ticks · 30 EU/t](#m-a2) → [Assembler · 5 s / 10 s / 20 s · 3 932 160 to 7 864 320 EU/t](#m-a3)

## How to build

1. Drawers first: UEV hull, UEPIC chips (Keep Exact 16), the UEV voltage coil, UEV circuits, cerium tritelluride single cables and springs. Drums: sodium potassium, soldering alloy. One dedicated machine per product, each behind its own router or Pipez item pipe with Item Filters and a Robot Arm Keep Exact. — `functionalstorage:oak_1`, `gtceu:uev_machine_hull`, `kubejs:uepic_chip`
2. Research once: scan the UHV energy input hatch (and the output hatch if you want dynamos), 192 CWU/t. Data item into the Assembly Line. — `gtceu:research_station`, `gtceu:uhv_energy_input_hatch`
3. Assembly Line: 40 s per hatch at 7 864 320 EU/t with the two fluids by Pipez fluid pipes. Output drawer Keep Exact 4. — `gtceu:assembly_line`, `gtceu:uev_energy_input_hatch`
4. Transformers on a plain assembler: hull (1A) or the previous transformer + cables + chips, 5 ticks. Build 1A, then 2A, 4A, 16A in order, each its own drawer. — `gtceu:uev_transformer_1a`, `gtceu:lv_assembler`
5. Multi-amp hatches: transformer + the smaller hatch + wire + coils + plates + solder; 4A, 16A, 64A in order. — `gtceu:uev_energy_input_hatch_4a`, `gtceu:uev_substation_input_hatch_64a`
6. Lasers last: 64A hatch + diamond lens + sensor/emitter + pump + cables; target hatch for consumers, source hatch for generators. Keep the sensor, emitter and pump from uev\_components. — `gtceu:uev_256a_laser_target_hatch`, `gtceu:diamond_lens`

## Tips

- Source: kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js (postUVMachines), transformers.js, large\_energy\_hatches.js, modular\_power\_hatches.js, parallel\_hatches.js, hatches\_and\_busses.js. The pack removes all gtceu:uev recipes (singleblocks.js top) and re-adds only a short list (hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder, fusion reactor), so anything else must come from a multiblock or the recipe browser. There are NO UEV input/output hatches or buses (io\_hatches.js stops at UHV: the comment says UEV and above scale like UHV): use UHV item and fluid hatches, UHV dual hatches and the UHV 4x / 9x hatches on UEV multiblocks.
- Energy hatch (assembly line, 800 ticks = 40 s): UEV hull + 4 cerium tritelluride single cables (the output hatch uses 4 springs) + 2 UEPIC chips + 1 UEV circuit + 2 UEV voltage coils + 20 000 mB sodium potassium + 5 760 mB indium tin lead cadmium soldering alloy, 7 864 320 EU/t, station research of the UHV energy hatch (1 966 080 EU/t, 192 CWU/t). Output hatch is the same with the spring and the output version of the research.
- Transformer (assembler, 5 ticks, 30 EU/t, or crafting table with chips): UEV hull (1A) or the previous transformer + 1 polonium bismide cable + 4 cerium tritelluride cables + 2 UEPIC chips; thickness single, double, quadruple, hex for 1A, 2A, 4A, 16A.
- Multi-amp: 4A = transformer 1A + energy hatch + 2 cerium tritelluride quadruple wire + 1 voltage coil + 2 mythrolic alloy plates + 720 mB solder (100 ticks, 3 932 160 EU/t); 16A = transformer 4A + 4A hatch + 2 quadruple wire + 2 coils + 4 plates + 1440 mB (200 ticks, x3); 64A substation hatch = transformer 16A + 16A hatch + 2 hex wire + 3 coils + 6 plates + 2160 mB (400 ticks, x4). Lasers: 256A = 64A hatch + diamond lens + sensor/emitter + pump + 4 single cables + 2880 mB (600 ticks); 1024A doubles lens/parts, 3600 mB (900 ticks); 4096A quadruples them, 4320 mB (1200 ticks). Target hatch uses the sensor, source (output) hatch the emitter. All x4 EU of the scaling voltage 1 966 080.
- Parallel hatches (parallel\_hatches.js): shaped, sensor + emitter + 4 circuits of the NEXT tier (UIV) + UEV hull + 2 cerium tritelluride double cables, then the absolute parallel hatch = it + 4 sensors + 4 emitters + 2 next-tier circuits + 4 UEPIC chips + 576 mB isovol, assembler 16 s at 1 966 080 EU/t. So the UEV parallel hatch is a UIV-era item. Modular conduit node/terminal hatches (modular\_power\_hatches.js) are hatch + sensor/emitter + 2 cables, circuit 2, 5 ticks.
- Sub-steps people skip: (1) the energy hatch needs the voltage coil of THIS tier (part of uev\_parts); (2) the research item is the UHV energy hatch, scanned in the Research Station; (3) sodium potassium in bulk: 20 000 mB per hatch; (4) at UEV voltage a 4A hatch is cheaper than 4 plain ones.
- **Unverified** the recipes of the tier cables and wires themselves (cerium tritelluride is a superconductor-style material), the sodium potassium supply, and the sterile cleaning maintenance hatch (a UEV Assembly Line item: hull + 2 robot arms + emitter + 3 UEV circuits, listed in hatches\_and\_busses.js).

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

- **Main source for:** `gtceu:uev_energy_input_hatch`, `gtceu:uev_energy_output_hatch`, `gtceu:uev_transformer_1a`, `gtceu:uev_transformer_2a`, `gtceu:uev_transformer_4a`, `gtceu:uev_transformer_16a`, `gtceu:uev_energy_input_hatch_4a`, `gtceu:uev_energy_input_hatch_16a`, `gtceu:uev_substation_input_hatch_64a`, `gtceu:uev_256a_laser_target_hatch`, `gtceu:uev_1024a_laser_target_hatch`, `gtceu:uev_4096a_laser_target_hatch`, `gtceu:uev_256a_laser_source_hatch`, `gtceu:uev_energy_output_hatch_4a`
