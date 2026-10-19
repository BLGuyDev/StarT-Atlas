---
kind: chain
id: uev_components2
order: 2040
data:
  t: |-
    UEV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator
  inf: true
  "n":
    - - g0
      - |-
        Robot Arm: 4 long starium alloy rod · 1 uev precision drive mechanism · 1 uev transmission assembly · 1 uev electric motor · 1 uev electric piston · 2 uev computational matrix · 2 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [long starium alloy rod, "gtceu:long_starium_alloy_rod"]
        - [uev precision drive mechanism, "kubejs:uev_precision_drive_mechanism"]
        - [uev transmission assembly, "kubejs:uev_transmission_assembly"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [uev electric piston, "gtceu:uev_electric_piston"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
    - - g1
      - |-
        Field Generator: 1 starium alloy frame · 2 uev high strength panel · 1 uev catalyst core · 2 uev emitter · 1 uev computational matrix · 64 fine enriched pallarovium alloy wire · 2 uev micropower router · 9 216 mB naquadated soldering alloy · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [starium alloy frame, "gtceu:starium_alloy_frame"]
        - [uev high strength panel, "kubejs:uev_high_strength_panel"]
        - [uev catalyst core, "kubejs:uev_catalyst_core"]
        - [uev emitter, "gtceu:uev_emitter"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
        - [fine enriched pallarovium alloy wire, "gtceu:fine_enriched_pallarovium_alloy_wire"]
    - - g2
      - |-
        Emitter: 1 starium alloy frame · 1 uev electric motor · 4 long starium alloy rod · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [starium alloy frame, "gtceu:starium_alloy_frame"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [long starium alloy rod, "gtceu:long_starium_alloy_rod"]
        - [uev catalyst core, "kubejs:uev_catalyst_core"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
        - [mythrolic alloy foil, "gtceu:mythrolic_alloy_foil"]
    - - g3
      - |-
        Sensor: 1 starium alloy frame · 1 uev electric motor · 4 starium alloy plate · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [starium alloy frame, "gtceu:starium_alloy_frame"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [starium alloy plate, "gtceu:starium_alloy_plate"]
        - [uev catalyst core, "kubejs:uev_catalyst_core"]
        - [uev computational matrix, "kubejs:uev_computational_matrix"]
        - [mythrolic alloy foil, "gtceu:mythrolic_alloy_foil"]
    - [al, "Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part", m, "gtceu:assembly_line"]
    - [o0, UEV Robot Arm, x, "gtceu:uev_robot_arm"]
    - [o1, UEV Field Generator, x, "gtceu:uev_field_generator"]
    - [o2, UEV Emitter, x, "gtceu:uev_emitter"]
    - [o3, UEV Sensor, x, "gtceu:uev_sensor"]
    - - g9
      - |-
        Fluid regulator: 1 UEV electric pump + 2 UEV circuits (circuit 1)
      - g
      - functionalstorage:oak_1
      - [[UEV pump, "gtceu:uev_electric_pump"], [UEV circuit, "kubejs:uev_universal_circuit"]]
    - [as, "Assembler · 2.5 s · 7 864 320 EU/t", m, "gtceu:uev_assembler"]
    - [o9, UEV Fluid Regulator, o, "gtceu:uev_fluid_regulator"]
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
      Source: kjs additions/progression/components/uhv_to_uiv_components.js (components(), tier uev). Every component is an Assembly Line recipe (600 ticks = 30 s) at 1 966 080 EU/t with STATION research of the UHV component of the same kind (160 CWU/t; 176 for emitter, sensor and field generator). Amounts: exponential x32 (tier scaler 5), rubber x5.
    - |-
      Robot Arm: 4 long starium alloy rod · 1 uev precision drive mechanism · 1 uev transmission assembly · 1 uev electric motor · 1 uev electric piston · 2 uev computational matrix · 2 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Field Generator: 1 starium alloy frame · 2 uev high strength panel · 1 uev catalyst core · 2 uev emitter · 1 uev computational matrix · 64 fine enriched pallarovium alloy wire · 2 uev micropower router · 9 216 mB naquadated soldering alloy · 2 304 mB isovol [research 176 CWU/t]. Emitter: 1 starium alloy frame · 1 uev electric motor · 4 long starium alloy rod · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol [research 176 CWU/t]. Sensor: 1 starium alloy frame · 1 uev electric motor · 4 starium alloy plate · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol [research 176 CWU/t].
    - |-
      Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
    - |-
      Order inside the chain: emitter first (field generator takes 2), then sensor, then field generator, then robot arm needs a piston from components 1/2. The fluid regulator is a plain assembler recipe (50 ticks, 4 times the tier voltage) and feeds the next tier's microfluidic flow valve.
    - |-
      Sub-steps people skip: (1) research each component by scanning the UHV one; (2) the robot arm eats 2 computational matrices and 2 micropower routers; (3) one motor per component plus 2 for the conveyor: motor throughput is the limit; (4) keep drawers Keep Exact 4 on motors and parts.
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
    - i: ["functionalstorage:oak_1", "gtceu:uev_electric_motor"]
      t: Drawers first for every part of this chain (Robot Arm, Field Generator, Emitter, Sensor). Drums for naquadated soldering alloy, tungsten disulfide, isovol. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers.
    - i: ["gtceu:research_station", "gtceu:data_orb"]
      t: |-
        Research: scan the UHV version of each component (160 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product.
    - i: ["gtceu:assembly_line", "gtceu:uev_robot_arm"]
      t: |-
        Robot Arm first: 30 s, 1 966 080 EU/t. This is the item that every other product in this chain needs.
    - i: ["gtceu:assembly_line", "gtceu:uev_field_generator"]
      t: |-
        Then Field Generator, Emitter, Sensor one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once.
    - i: ["functionalstorage:oak_1", "gtceu:uev_sensor"]
      t: Output drawers Keep Exact 4 per component; regulator on its own assembler with the pump from the drawer.
    - i: ["functionalstorage:oak_1", "gtceu:uev_electric_motor"]
      t: |-
        These components go into: the UEV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks.
---
# UEV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Robot Arm: 4 long starium alloy rod · 1 uev precision drive mechanism · 1 uev transmission assembly · 1 uev electric motor · 1 uev electric piston · 2 uev computational matrix · 2 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Robot Arm: 4 long starium alloy rod · 1 uev precision drive mechanism · 1 uev transmission assembly · 1 uev electric motor · 1 uev electric piston · 2 uev computational matrix · 2 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>long starium alloy rod</span><span>uev precision drive mechanism</span><span>uev transmission assembly</span><span>uev electric motor</span><span>uev electric piston</span><span>uev computational matrix</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Field Generator: 1 starium alloy frame · 2 uev high strength panel · 1 uev catalyst core · 2 uev emitter · 1 uev computational matrix · 64 fine enriched pallarovium alloy wire · 2 uev micropower router · 9 216 mB naquadated soldering alloy · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Field Generator: 1 starium alloy frame · 2 uev high strength panel · 1 uev catalyst core · 2 uev emitter · 1 uev computational matrix · 64 fine enriched pallarovium alloy wire · 2 uev micropower router · 9 216 mB naquadated soldering alloy · 2 304 mB isovol</span><span class="gt-sub"><span>starium alloy frame</span><span>uev high strength panel</span><span>uev catalyst core</span><span>uev emitter</span><span>uev computational matrix</span><span>fine enriched pallarovium alloy wire</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Emitter: 1 starium alloy frame · 1 uev electric motor · 4 long starium alloy rod · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Emitter: 1 starium alloy frame · 1 uev electric motor · 4 long starium alloy rod · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>starium alloy frame</span><span>uev electric motor</span><span>long starium alloy rod</span><span>uev catalyst core</span><span>uev computational matrix</span><span>mythrolic alloy foil</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Sensor: 1 starium alloy frame · 1 uev electric motor · 4 starium alloy plate · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Sensor: 1 starium alloy frame · 1 uev electric motor · 4 starium alloy plate · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>starium alloy frame</span><span>uev electric motor</span><span>starium alloy plate</span><span>uev catalyst core</span><span>uev computational matrix</span><span>mythrolic alloy foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Robot Arm (gtceu:uev_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Robot Arm</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Field Generator (gtceu:uev_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Field Generator</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Emitter (gtceu:uev_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Emitter</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Sensor (gtceu:uev_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-uev" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 2.5 s · 7 864 320 EU/t</span><span class="gt-badge t-uev">UEV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Fluid regulator: 1 UEV electric pump + 2 UEV circuits (circuit 1) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Fluid regulator: 1 UEV electric pump + 2 UEV circuits (circuit 1)</span><span class="gt-sub"><span>UEV pump</span><span>UEV circuit</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 388 608 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UEV Fluid Regulator (gtceu:uev_fluid_regulator) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_fluid_regulator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Fluid Regulator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uev_assembler</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part](#m-al)
- [Assembler · 2.5 s · 7 864 320 EU/t](#m-as)

## How to build

1. Drawers first for every part of this chain (Robot Arm, Field Generator, Emitter, Sensor). Drums for naquadated soldering alloy, tungsten disulfide, isovol. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers. — `functionalstorage:oak_1`, `gtceu:uev_electric_motor`
2. Research: scan the UHV version of each component (160 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product. — `gtceu:research_station`, `gtceu:data_orb`
3. Robot Arm first: 30 s, 1 966 080 EU/t. This is the item that every other product in this chain needs. — `gtceu:assembly_line`, `gtceu:uev_robot_arm`
4. Then Field Generator, Emitter, Sensor one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once. — `gtceu:assembly_line`, `gtceu:uev_field_generator`
5. Output drawers Keep Exact 4 per component; regulator on its own assembler with the pump from the drawer. — `functionalstorage:oak_1`, `gtceu:uev_sensor`
6. These components go into: the UEV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks. — `functionalstorage:oak_1`, `gtceu:uev_electric_motor`

## Tips

- Source: kjs additions/progression/components/uhv\_to\_uiv\_components.js (components(), tier uev). Every component is an Assembly Line recipe (600 ticks = 30 s) at 1 966 080 EU/t with STATION research of the UHV component of the same kind (160 CWU/t; 176 for emitter, sensor and field generator). Amounts: exponential x32 (tier scaler 5), rubber x5.
- Robot Arm: 4 long starium alloy rod · 1 uev precision drive mechanism · 1 uev transmission assembly · 1 uev electric motor · 1 uev electric piston · 2 uev computational matrix · 2 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Field Generator: 1 starium alloy frame · 2 uev high strength panel · 1 uev catalyst core · 2 uev emitter · 1 uev computational matrix · 64 fine enriched pallarovium alloy wire · 2 uev micropower router · 9 216 mB naquadated soldering alloy · 2 304 mB isovol \[research 176 CWU/t\]. Emitter: 1 starium alloy frame · 1 uev electric motor · 4 long starium alloy rod · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol \[research 176 CWU/t\]. Sensor: 1 starium alloy frame · 1 uev electric motor · 4 starium alloy plate · 1 uev catalyst core · 1 uev computational matrix · 64 mythrolic alloy foil · 1 uev micropower router · 4 608 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol \[research 176 CWU/t\].
- Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
- Order inside the chain: emitter first (field generator takes 2), then sensor, then field generator, then robot arm needs a piston from components 1/2. The fluid regulator is a plain assembler recipe (50 ticks, 4 times the tier voltage) and feeds the next tier's microfluidic flow valve.
- Sub-steps people skip: (1) research each component by scanning the UHV one; (2) the robot arm eats 2 computational matrices and 2 micropower routers; (3) one motor per component plus 2 for the conveyor: motor throughput is the limit; (4) keep drawers Keep Exact 4 on motors and parts.
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

- **Main source for:** `gtceu:uev_robot_arm`, `gtceu:uev_field_generator`, `gtceu:uev_emitter`, `gtceu:uev_sensor`, `gtceu:uev_fluid_regulator`
