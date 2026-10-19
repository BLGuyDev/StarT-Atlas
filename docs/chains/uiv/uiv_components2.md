---
kind: chain
id: uiv_components2
order: 2060
data:
  t: |-
    UIV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator
  inf: true
  "n":
    - - g0
      - |-
        Robot Arm: 4 long ohmderblux alloy rod · 1 uiv precision drive mechanism · 1 uiv transmission assembly · 1 uiv electric motor · 1 uiv electric piston · 2 uiv computational matrix · 2 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [long ohmderblux alloy rod, "gtceu:long_ohmderblux_alloy_rod"]
        - [uiv precision drive mechanism, "kubejs:uiv_precision_drive_mechanism"]
        - [uiv transmission assembly, "kubejs:uiv_transmission_assembly"]
        - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [uiv electric piston, "gtceu:uiv_electric_piston"]
        - [uiv computational matrix, "kubejs:uiv_computational_matrix"]
    - - g1
      - |-
        Field Generator: 1 ohmderblux alloy frame · 2 uiv high strength panel · 1 uiv catalyst core · 2 uiv emitter · 1 uiv computational matrix · 64 fine rhenium super composite alloy wire · 2 uiv micropower router · 18 432 mB naquadated soldering alloy · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy frame, "gtceu:ohmderblux_alloy_frame"]
        - [uiv high strength panel, "kubejs:uiv_high_strength_panel"]
        - [uiv catalyst core, "kubejs:uiv_catalyst_core"]
        - [uiv emitter, "gtceu:uiv_emitter"]
        - [uiv computational matrix, "kubejs:uiv_computational_matrix"]
        - [fine rhenium super composite alloy wire, "gtceu:fine_rhenium_super_composite_alloy_wire"]
    - - g2
      - |-
        Emitter: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 long ohmderblux alloy rod · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy frame, "gtceu:ohmderblux_alloy_frame"]
        - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [long ohmderblux alloy rod, "gtceu:long_ohmderblux_alloy_rod"]
        - [uiv catalyst core, "kubejs:uiv_catalyst_core"]
        - [uiv computational matrix, "kubejs:uiv_computational_matrix"]
        - [chaotixic alloy foil, "gtceu:chaotixic_alloy_foil"]
    - - g3
      - |-
        Sensor: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 ohmderblux alloy plate · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [ohmderblux alloy frame, "gtceu:ohmderblux_alloy_frame"]
        - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [ohmderblux alloy plate, "gtceu:ohmderblux_alloy_plate"]
        - [uiv catalyst core, "kubejs:uiv_catalyst_core"]
        - [uiv computational matrix, "kubejs:uiv_computational_matrix"]
        - [chaotixic alloy foil, "gtceu:chaotixic_alloy_foil"]
    - [al, "Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part", m, "gtceu:assembly_line"]
    - [o0, UIV Robot Arm, x, "gtceu:uiv_robot_arm"]
    - [o1, UIV Field Generator, x, "gtceu:uiv_field_generator"]
    - [o2, UIV Emitter, x, "gtceu:uiv_emitter"]
    - [o3, UIV Sensor, x, "gtceu:uiv_sensor"]
    - - g9
      - |-
        Fluid regulator: 1 UIV electric pump + 2 UIV circuits (circuit 1)
      - g
      - functionalstorage:oak_1
      - [[UIV pump, "gtceu:uiv_electric_pump"], [UIV circuit, "kubejs:uiv_universal_circuit"]]
    - [as, "Assembler · 2.5 s · 31 457 280 EU/t", m, "gtceu:uiv_assembler"]
    - [o9, UIV Fluid Regulator, o, "gtceu:uiv_fluid_regulator"]
  e:
    - [g0, al, "1"]
    - [g1, al, "1"]
    - [g2, al, "1"]
    - [g3, al, "1"]
    - [al, o0, "1 / 30 s"]
    - [al, o1, "1 / 30 s"]
    - [al, o2, "1 / 30 s"]
    - [al, o3, "1 / 30 s"]
    - [g9, as, "1"]
    - [as, o9, "1 / 2.5 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/uhv_to_uiv_components.js (components(), tier uiv). Every component is an Assembly Line recipe (600 ticks = 30 s) at 7 864 320 EU/t with STATION research of the UEV component of the same kind (192 CWU/t; 208 for emitter, sensor and field generator). Amounts: exponential x64 (tier scaler 6), rubber x6.
    - |-
      Robot Arm: 4 long ohmderblux alloy rod · 1 uiv precision drive mechanism · 1 uiv transmission assembly · 1 uiv electric motor · 1 uiv electric piston · 2 uiv computational matrix · 2 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Field Generator: 1 ohmderblux alloy frame · 2 uiv high strength panel · 1 uiv catalyst core · 2 uiv emitter · 1 uiv computational matrix · 64 fine rhenium super composite alloy wire · 2 uiv micropower router · 18 432 mB naquadated soldering alloy · 4 608 mB calamatium [research 208 CWU/t]. Emitter: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 long ohmderblux alloy rod · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium [research 208 CWU/t]. Sensor: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 ohmderblux alloy plate · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium [research 208 CWU/t].
    - |-
      Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
    - |-
      Order inside the chain: emitter first (field generator takes 2), then sensor, then field generator, then robot arm needs a piston from components 1/2. The fluid regulator is a plain assembler recipe (50 ticks, 4 times the tier voltage) and feeds the next tier's microfluidic flow valve.
    - |-
      Sub-steps people skip: (1) research each component by scanning the UEV one; (2) the robot arm eats 2 computational matrices and 2 micropower routers; (3) one motor per component plus 2 for the conveyor: motor throughput is the limit; (4) keep drawers Keep Exact 4 on motors and parts.
    - |-
      Unverified: Assembly Line input slot count (more than 16 stacks fit only with a big bus), and the alloy and wire sources.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 5]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uiv_electric_motor"]
      t: Drawers first for every part of this chain (Robot Arm, Field Generator, Emitter, Sensor). Drums for naquadated soldering alloy, tungsten disulfide, calamatium. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers.
    - i: ["gtceu:research_station", "gtceu:data_orb"]
      t: |-
        Research: scan the UEV version of each component (192 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product.
    - i: ["gtceu:assembly_line", "gtceu:uiv_robot_arm"]
      t: |-
        Robot Arm first: 30 s, 7 864 320 EU/t. This is the item that every other product in this chain needs.
    - i: ["gtceu:assembly_line", "gtceu:uiv_field_generator"]
      t: |-
        Then Field Generator, Emitter, Sensor one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once.
    - i: ["functionalstorage:oak_1", "gtceu:uiv_sensor"]
      t: Output drawers Keep Exact 4 per component; regulator on its own assembler with the pump from the drawer.
    - i: ["functionalstorage:oak_1", "gtceu:uiv_electric_motor"]
      t: |-
        These components go into: the UIV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks.
---
# UIV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV hull, parts, hatches and components](../../plan/p19.md#uivmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Robot Arm: 4 long ohmderblux alloy rod · 1 uiv precision drive mechanism · 1 uiv transmission assembly · 1 uiv electric motor · 1 uiv electric piston · 2 uiv computational matrix · 2 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Robot Arm: 4 long ohmderblux alloy rod · 1 uiv precision drive mechanism · 1 uiv transmission assembly · 1 uiv electric motor · 1 uiv electric piston · 2 uiv computational matrix · 2 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>long ohmderblux alloy rod</span><span>uiv precision drive mechanism</span><span>uiv transmission assembly</span><span>uiv electric motor</span><span>uiv electric piston</span><span>uiv computational matrix</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Field Generator: 1 ohmderblux alloy frame · 2 uiv high strength panel · 1 uiv catalyst core · 2 uiv emitter · 1 uiv computational matrix · 64 fine rhenium super composite alloy wire · 2 uiv micropower router · 18 432 mB naquadated soldering alloy · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Field Generator: 1 ohmderblux alloy frame · 2 uiv high strength panel · 1 uiv catalyst core · 2 uiv emitter · 1 uiv computational matrix · 64 fine rhenium super composite alloy wire · 2 uiv micropower router · 18 432 mB naquadated soldering alloy · 4 608 mB calamatium</span><span class="gt-sub"><span>ohmderblux alloy frame</span><span>uiv high strength panel</span><span>uiv catalyst core</span><span>uiv emitter</span><span>uiv computational matrix</span><span>fine rhenium super composite alloy wire</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Emitter: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 long ohmderblux alloy rod · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Emitter: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 long ohmderblux alloy rod · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>ohmderblux alloy frame</span><span>uiv electric motor</span><span>long ohmderblux alloy rod</span><span>uiv catalyst core</span><span>uiv computational matrix</span><span>chaotixic alloy foil</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Sensor: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 ohmderblux alloy plate · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Sensor: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 ohmderblux alloy plate · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>ohmderblux alloy frame</span><span>uiv electric motor</span><span>ohmderblux alloy plate</span><span>uiv catalyst core</span><span>uiv computational matrix</span><span>chaotixic alloy foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Robot Arm (gtceu:uiv_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Robot Arm</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Field Generator (gtceu:uiv_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Field Generator</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Emitter (gtceu:uiv_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Emitter</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Sensor (gtceu:uiv_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-uiv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 2.5 s · 31 457 280 EU/t</span><span class="gt-badge t-uiv">UIV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Fluid regulator: 1 UIV electric pump + 2 UIV circuits (circuit 1) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Fluid regulator: 1 UIV electric pump + 2 UIV circuits (circuit 1)</span><span class="gt-sub"><span>UIV pump</span><span>UIV circuit</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 33 554 432 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UIV Fluid Regulator (gtceu:uiv_fluid_regulator) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_fluid_regulator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Fluid Regulator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uiv_assembler</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part](#m-al)
- [Assembler · 2.5 s · 31 457 280 EU/t](#m-as)

## How to build

1. Drawers first for every part of this chain (Robot Arm, Field Generator, Emitter, Sensor). Drums for naquadated soldering alloy, tungsten disulfide, calamatium. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers. — `functionalstorage:oak_1`, `gtceu:uiv_electric_motor`
2. Research: scan the UEV version of each component (192 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product. — `gtceu:research_station`, `gtceu:data_orb`
3. Robot Arm first: 30 s, 7 864 320 EU/t. This is the item that every other product in this chain needs. — `gtceu:assembly_line`, `gtceu:uiv_robot_arm`
4. Then Field Generator, Emitter, Sensor one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once. — `gtceu:assembly_line`, `gtceu:uiv_field_generator`
5. Output drawers Keep Exact 4 per component; regulator on its own assembler with the pump from the drawer. — `functionalstorage:oak_1`, `gtceu:uiv_sensor`
6. These components go into: the UIV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks. — `functionalstorage:oak_1`, `gtceu:uiv_electric_motor`

## Tips

- Source: kjs additions/progression/components/uhv\_to\_uiv\_components.js (components(), tier uiv). Every component is an Assembly Line recipe (600 ticks = 30 s) at 7 864 320 EU/t with STATION research of the UEV component of the same kind (192 CWU/t; 208 for emitter, sensor and field generator). Amounts: exponential x64 (tier scaler 6), rubber x6.
- Robot Arm: 4 long ohmderblux alloy rod · 1 uiv precision drive mechanism · 1 uiv transmission assembly · 1 uiv electric motor · 1 uiv electric piston · 2 uiv computational matrix · 2 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Field Generator: 1 ohmderblux alloy frame · 2 uiv high strength panel · 1 uiv catalyst core · 2 uiv emitter · 1 uiv computational matrix · 64 fine rhenium super composite alloy wire · 2 uiv micropower router · 18 432 mB naquadated soldering alloy · 4 608 mB calamatium \[research 208 CWU/t\]. Emitter: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 long ohmderblux alloy rod · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium \[research 208 CWU/t\]. Sensor: 1 ohmderblux alloy frame · 1 uiv electric motor · 4 ohmderblux alloy plate · 1 uiv catalyst core · 1 uiv computational matrix · 64 chaotixic alloy foil · 1 uiv micropower router · 9 216 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium \[research 208 CWU/t\].
- Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
- Order inside the chain: emitter first (field generator takes 2), then sensor, then field generator, then robot arm needs a piston from components 1/2. The fluid regulator is a plain assembler recipe (50 ticks, 4 times the tier voltage) and feeds the next tier's microfluidic flow valve.
- Sub-steps people skip: (1) research each component by scanning the UEV one; (2) the robot arm eats 2 computational matrices and 2 micropower routers; (3) one motor per component plus 2 for the conveyor: motor throughput is the limit; (4) keep drawers Keep Exact 4 on motors and parts.
- **Unverified** Assembly Line input slot count (more than 16 stacks fit only with a big bus), and the alloy and wire sources.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `gtceu:uiv_robot_arm`, `gtceu:uiv_field_generator`, `gtceu:uiv_emitter`, `gtceu:uiv_sensor`, `gtceu:uiv_fluid_regulator`
