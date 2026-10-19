---
kind: chain
id: uiv_components
order: 2050
data:
  t: |-
    UIV components 1/2: electric motor, electric pump, conveyor module, electric piston
  inf: true
  "n":
    - - g0
      - |-
        Electric Motor: 1 uiv super magnetic core · 2 long ohmderblux alloy rod · 1 uiv transmission assembly · 64 fine xeproda wire · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [uiv super magnetic core, "kubejs:uiv_super_magnetic_core"]
        - [long ohmderblux alloy rod, "gtceu:long_ohmderblux_alloy_rod"]
        - [uiv transmission assembly, "kubejs:uiv_transmission_assembly"]
        - [fine xeproda wire, "gtceu:fine_xeproda_wire"]
        - [uiv micropower router, "kubejs:uiv_micropower_router"]
    - - g1
      - |-
        Electric Pump: 1 uiv electric motor · 1 nyanium normal fluid pipe · 1 uiv microfluidic flow valve · 8 perfluoroelastomer rubber ring · 1 abyssal alloy rotor · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [nyanium normal fluid pipe, "gtceu:nyanium_normal_fluid_pipe"]
        - [uiv microfluidic flow valve, "kubejs:uiv_microfluidic_flow_valve"]
        - [perfluoroelastomer rubber ring, "gtceu:perfluoroelastomer_rubber_ring"]
        - [abyssal alloy rotor, "gtceu:abyssal_alloy_rotor"]
        - [uiv micropower router, "kubejs:uiv_micropower_router"]
    - - g2
      - |-
        Conveyor Module: 2 uiv electric motor · 1 uiv high strength panel · 1 uiv precision drive mechanism · 4 ohmderblux alloy ring · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 6 912 mB perfluoroelastomer rubber · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [uiv high strength panel, "kubejs:uiv_high_strength_panel"]
        - [uiv precision drive mechanism, "kubejs:uiv_precision_drive_mechanism"]
        - [ohmderblux alloy ring, "gtceu:ohmderblux_alloy_ring"]
        - [uiv micropower router, "kubejs:uiv_micropower_router"]
    - - g3
      - |-
        Electric Piston: 1 uiv electric motor · 2 uiv high strength panel · 1 uiv transmission assembly · 1 abyssal alloy gear · 1 small abyssal alloy gear · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium
      - g
      - functionalstorage:oak_1
      - - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [uiv high strength panel, "kubejs:uiv_high_strength_panel"]
        - [uiv transmission assembly, "kubejs:uiv_transmission_assembly"]
        - [abyssal alloy gear, "gtceu:abyssal_alloy_gear"]
        - [small abyssal alloy gear, "gtceu:small_abyssal_alloy_gear"]
        - [uiv micropower router, "kubejs:uiv_micropower_router"]
    - [al, "Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part", m, "gtceu:assembly_line"]
    - [o0, UIV Electric Motor, x, "gtceu:uiv_electric_motor"]
    - [o1, UIV Electric Pump, x, "gtceu:uiv_electric_pump"]
    - [o2, UIV Conveyor Module, x, "gtceu:uiv_conveyor_module"]
    - [o3, UIV Electric Piston, x, "gtceu:uiv_electric_piston"]
  e:
    - [g0, al, "1"]
    - [g1, al, "1"]
    - [g2, al, "1"]
    - [g3, al, "1"]
    - [al, o0, "1 / 30 s"]
    - [al, o1, "1 / 30 s"]
    - [al, o2, "1 / 30 s"]
    - [al, o3, "1 / 30 s"]
  tips:
    - |-
      Source: kjs additions/progression/components/uhv_to_uiv_components.js (components(), tier uiv). Every component is an Assembly Line recipe (600 ticks = 30 s) at 7 864 320 EU/t with STATION research of the UEV component of the same kind (192 CWU/t; 208 for emitter, sensor and field generator). Amounts: exponential x64 (tier scaler 6), rubber x6.
    - |-
      Electric Motor: 1 uiv super magnetic core · 2 long ohmderblux alloy rod · 1 uiv transmission assembly · 64 fine xeproda wire · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Electric Pump: 1 uiv electric motor · 1 nyanium normal fluid pipe · 1 uiv microfluidic flow valve · 8 perfluoroelastomer rubber ring · 1 abyssal alloy rotor · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Conveyor Module: 2 uiv electric motor · 1 uiv high strength panel · 1 uiv precision drive mechanism · 4 ohmderblux alloy ring · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 6 912 mB perfluoroelastomer rubber · 4 608 mB calamatium. Electric Piston: 1 uiv electric motor · 2 uiv high strength panel · 1 uiv transmission assembly · 1 abyssal alloy gear · 1 small abyssal alloy gear · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium.
    - |-
      Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
    - |-
      Motor first: pump, conveyor, piston, robot arm and the three laser parts all take it. The pump needs the microfluidic flow valve, which needs the UEV fluid regulator (made from the UEV pump): that is why the UEV component line must stay alive. The conveyor and piston need two and one high strength panels, so build parts 2/2 before this chain.
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
      t: Drawers first for every part of this chain (Electric Motor, Electric Pump, Conveyor Module, Electric Piston). Drums for naquadated soldering alloy, tungsten disulfide, calamatium and perfluoroelastomer rubber. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers.
    - i: ["gtceu:research_station", "gtceu:data_orb"]
      t: |-
        Research: scan the UEV version of each component (192 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product.
    - i: ["gtceu:assembly_line", "gtceu:uiv_electric_motor"]
      t: |-
        Electric Motor first: 30 s, 7 864 320 EU/t. This is the item that every other product in this chain needs.
    - i: ["gtceu:assembly_line", "gtceu:uiv_electric_pump"]
      t: |-
        Then Electric Pump, Conveyor Module, Electric Piston one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once.
    - i: ["functionalstorage:oak_1", "gtceu:uiv_electric_piston"]
      t: Output drawers Keep Exact 4 per component; the pump also leaves a copy for the fluid regulator in components 2/2.
    - i: ["functionalstorage:oak_1", "gtceu:uiv_electric_motor"]
      t: |-
        These components go into: the UIV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks.
---
# UIV components 1/2: electric motor, electric pump, conveyor module, electric piston

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_components` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV hull, parts, hatches and components](../../plan/p19.md#uivmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Electric Motor: 1 uiv super magnetic core · 2 long ohmderblux alloy rod · 1 uiv transmission assembly · 64 fine xeproda wire · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Motor: 1 uiv super magnetic core · 2 long ohmderblux alloy rod · 1 uiv transmission assembly · 64 fine xeproda wire · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>uiv super magnetic core</span><span>long ohmderblux alloy rod</span><span>uiv transmission assembly</span><span>fine xeproda wire</span><span>uiv micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Electric Pump: 1 uiv electric motor · 1 nyanium normal fluid pipe · 1 uiv microfluidic flow valve · 8 perfluoroelastomer rubber ring · 1 abyssal alloy rotor · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Pump: 1 uiv electric motor · 1 nyanium normal fluid pipe · 1 uiv microfluidic flow valve · 8 perfluoroelastomer rubber ring · 1 abyssal alloy rotor · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>uiv electric motor</span><span>nyanium normal fluid pipe</span><span>uiv microfluidic flow valve</span><span>perfluoroelastomer rubber ring</span><span>abyssal alloy rotor</span><span>uiv micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Conveyor Module: 2 uiv electric motor · 1 uiv high strength panel · 1 uiv precision drive mechanism · 4 ohmderblux alloy ring · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 6 912 mB perfluoroelastomer rubber · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Conveyor Module: 2 uiv electric motor · 1 uiv high strength panel · 1 uiv precision drive mechanism · 4 ohmderblux alloy ring · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 6 912 mB perfluoroelastomer rubber · 4 608 mB calamatium</span><span class="gt-sub"><span>uiv electric motor</span><span>uiv high strength panel</span><span>uiv precision drive mechanism</span><span>ohmderblux alloy ring</span><span>uiv micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Electric Piston: 1 uiv electric motor · 2 uiv high strength panel · 1 uiv transmission assembly · 1 abyssal alloy gear · 1 small abyssal alloy gear · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Piston: 1 uiv electric motor · 2 uiv high strength panel · 1 uiv transmission assembly · 1 abyssal alloy gear · 1 small abyssal alloy gear · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium</span><span class="gt-sub"><span>uiv electric motor</span><span>uiv high strength panel</span><span>uiv transmission assembly</span><span>abyssal alloy gear</span><span>small abyssal alloy gear</span><span>uiv micropower router</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Electric Motor (gtceu:uiv_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Electric Pump (gtceu:uiv_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Electric Pump</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Conveyor Module (gtceu:uiv_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Conveyor Module</span><b class="gt-q">1</b></span><span class="gt-slot" title="UIV Electric Piston (gtceu:uiv_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 7 864 320 EU/t · station research of the UEV part](#m-al)

## How to build

1. Drawers first for every part of this chain (Electric Motor, Electric Pump, Conveyor Module, Electric Piston). Drums for naquadated soldering alloy, tungsten disulfide, calamatium and perfluoroelastomer rubber. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers. — `functionalstorage:oak_1`, `gtceu:uiv_electric_motor`
2. Research: scan the UEV version of each component (192 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product. — `gtceu:research_station`, `gtceu:data_orb`
3. Electric Motor first: 30 s, 7 864 320 EU/t. This is the item that every other product in this chain needs. — `gtceu:assembly_line`, `gtceu:uiv_electric_motor`
4. Then Electric Pump, Conveyor Module, Electric Piston one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once. — `gtceu:assembly_line`, `gtceu:uiv_electric_pump`
5. Output drawers Keep Exact 4 per component; the pump also leaves a copy for the fluid regulator in components 2/2. — `functionalstorage:oak_1`, `gtceu:uiv_electric_piston`
6. These components go into: the UIV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks. — `functionalstorage:oak_1`, `gtceu:uiv_electric_motor`

## Tips

- Source: kjs additions/progression/components/uhv\_to\_uiv\_components.js (components(), tier uiv). Every component is an Assembly Line recipe (600 ticks = 30 s) at 7 864 320 EU/t with STATION research of the UEV component of the same kind (192 CWU/t; 208 for emitter, sensor and field generator). Amounts: exponential x64 (tier scaler 6), rubber x6.
- Electric Motor: 1 uiv super magnetic core · 2 long ohmderblux alloy rod · 1 uiv transmission assembly · 64 fine xeproda wire · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Electric Pump: 1 uiv electric motor · 1 nyanium normal fluid pipe · 1 uiv microfluidic flow valve · 8 perfluoroelastomer rubber ring · 1 abyssal alloy rotor · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium. Conveyor Module: 2 uiv electric motor · 1 uiv high strength panel · 1 uiv precision drive mechanism · 4 ohmderblux alloy ring · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 6 912 mB perfluoroelastomer rubber · 4 608 mB calamatium. Electric Piston: 1 uiv electric motor · 2 uiv high strength panel · 1 uiv transmission assembly · 1 abyssal alloy gear · 1 small abyssal alloy gear · 1 uiv micropower router · 4 608 mB naquadated soldering alloy · 8 000 mB tungsten disulfide · 4 608 mB calamatium.
- Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
- Motor first: pump, conveyor, piston, robot arm and the three laser parts all take it. The pump needs the microfluidic flow valve, which needs the UEV fluid regulator (made from the UEV pump): that is why the UEV component line must stay alive. The conveyor and piston need two and one high strength panels, so build parts 2/2 before this chain.
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

- **Main source for:** `gtceu:uiv_electric_motor`, `gtceu:uiv_electric_pump`, `gtceu:uiv_conveyor_module`, `gtceu:uiv_electric_piston`
