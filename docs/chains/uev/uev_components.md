---
kind: chain
id: uev_components
order: 2030
data:
  t: |-
    UEV components 1/2: electric motor, electric pump, conveyor module, electric piston
  inf: true
  "n":
    - - g0
      - |-
        Electric Motor: 1 uev super magnetic core · 2 long starium alloy rod · 1 uev transmission assembly · 64 fine adamantine wire · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [uev super magnetic core, "kubejs:uev_super_magnetic_core"]
        - [long starium alloy rod, "gtceu:long_starium_alloy_rod"]
        - [uev transmission assembly, "kubejs:uev_transmission_assembly"]
        - [fine adamantine wire, "gtceu:fine_adamantine_wire"]
        - [uev micropower router, "kubejs:uev_micropower_router"]
    - - g1
      - |-
        Electric Pump: 1 uev electric motor · 1 mythrolic alloy normal fluid pipe · 1 uev microfluidic flow valve · 8 styrene butadiene rubber ring · 1 magmada alloy rotor · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [uev electric motor, "gtceu:uev_electric_motor"]
        - [mythrolic alloy normal fluid pipe, "gtceu:mythrolic_alloy_normal_fluid_pipe"]
        - [uev microfluidic flow valve, "kubejs:uev_microfluidic_flow_valve"]
        - [styrene butadiene rubber ring, "gtceu:styrene_butadiene_rubber_ring"]
        - [magmada alloy rotor, "gtceu:magmada_alloy_rotor"]
        - [uev micropower router, "kubejs:uev_micropower_router"]
    - - g2
      - |-
        Conveyor Module: 2 uev electric motor · 1 uev high strength panel · 1 uev precision drive mechanism · 4 starium alloy ring · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 5 760 mB perfluoroelastomer rubber · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [uev electric motor, "gtceu:uev_electric_motor"]
        - [uev high strength panel, "kubejs:uev_high_strength_panel"]
        - [uev precision drive mechanism, "kubejs:uev_precision_drive_mechanism"]
        - [starium alloy ring, "gtceu:starium_alloy_ring"]
        - [uev micropower router, "kubejs:uev_micropower_router"]
    - - g3
      - |-
        Electric Piston: 1 uev electric motor · 2 uev high strength panel · 1 uev transmission assembly · 1 magmada alloy gear · 1 small magmada alloy gear · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol
      - g
      - functionalstorage:oak_1
      - - [uev electric motor, "gtceu:uev_electric_motor"]
        - [uev high strength panel, "kubejs:uev_high_strength_panel"]
        - [uev transmission assembly, "kubejs:uev_transmission_assembly"]
        - [magmada alloy gear, "gtceu:magmada_alloy_gear"]
        - [small magmada alloy gear, "gtceu:small_magmada_alloy_gear"]
        - [uev micropower router, "kubejs:uev_micropower_router"]
    - [al, "Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part", m, "gtceu:assembly_line"]
    - [o0, UEV Electric Motor, x, "gtceu:uev_electric_motor"]
    - [o1, UEV Electric Pump, x, "gtceu:uev_electric_pump"]
    - [o2, UEV Conveyor Module, x, "gtceu:uev_conveyor_module"]
    - [o3, UEV Electric Piston, x, "gtceu:uev_electric_piston"]
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
      Source: kjs additions/progression/components/uhv_to_uiv_components.js (components(), tier uev). Every component is an Assembly Line recipe (600 ticks = 30 s) at 1 966 080 EU/t with STATION research of the UHV component of the same kind (160 CWU/t; 176 for emitter, sensor and field generator). Amounts: exponential x32 (tier scaler 5), rubber x5.
    - |-
      Electric Motor: 1 uev super magnetic core · 2 long starium alloy rod · 1 uev transmission assembly · 64 fine adamantine wire · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Electric Pump: 1 uev electric motor · 1 mythrolic alloy normal fluid pipe · 1 uev microfluidic flow valve · 8 styrene butadiene rubber ring · 1 magmada alloy rotor · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Conveyor Module: 2 uev electric motor · 1 uev high strength panel · 1 uev precision drive mechanism · 4 starium alloy ring · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 5 760 mB perfluoroelastomer rubber · 2 304 mB isovol. Electric Piston: 1 uev electric motor · 2 uev high strength panel · 1 uev transmission assembly · 1 magmada alloy gear · 1 small magmada alloy gear · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol.
    - |-
      Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
    - |-
      Motor first: pump, conveyor, piston, robot arm and the three laser parts all take it. The pump needs the microfluidic flow valve, which needs the UHV fluid regulator (made from the UHV pump): that is why the UHV component line must stay alive. The conveyor and piston need two and one high strength panels, so build parts 2/2 before this chain.
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
      t: Drawers first for every part of this chain (Electric Motor, Electric Pump, Conveyor Module, Electric Piston). Drums for naquadated soldering alloy, tungsten disulfide, isovol and perfluoroelastomer rubber. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers.
    - i: ["gtceu:research_station", "gtceu:data_orb"]
      t: |-
        Research: scan the UHV version of each component (160 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product.
    - i: ["gtceu:assembly_line", "gtceu:uev_electric_motor"]
      t: |-
        Electric Motor first: 30 s, 1 966 080 EU/t. This is the item that every other product in this chain needs.
    - i: ["gtceu:assembly_line", "gtceu:uev_electric_pump"]
      t: |-
        Then Electric Pump, Conveyor Module, Electric Piston one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once.
    - i: ["functionalstorage:oak_1", "gtceu:uev_electric_piston"]
      t: Output drawers Keep Exact 4 per component; the pump also leaves a copy for the fluid regulator in components 2/2.
    - i: ["functionalstorage:oak_1", "gtceu:uev_electric_motor"]
      t: |-
        These components go into: the UEV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks.
---
# UEV components 1/2: electric motor, electric pump, conveyor module, electric piston

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_components` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Electric Motor: 1 uev super magnetic core · 2 long starium alloy rod · 1 uev transmission assembly · 64 fine adamantine wire · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Motor: 1 uev super magnetic core · 2 long starium alloy rod · 1 uev transmission assembly · 64 fine adamantine wire · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>uev super magnetic core</span><span>long starium alloy rod</span><span>uev transmission assembly</span><span>fine adamantine wire</span><span>uev micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Electric Pump: 1 uev electric motor · 1 mythrolic alloy normal fluid pipe · 1 uev microfluidic flow valve · 8 styrene butadiene rubber ring · 1 magmada alloy rotor · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Pump: 1 uev electric motor · 1 mythrolic alloy normal fluid pipe · 1 uev microfluidic flow valve · 8 styrene butadiene rubber ring · 1 magmada alloy rotor · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>uev electric motor</span><span>mythrolic alloy normal fluid pipe</span><span>uev microfluidic flow valve</span><span>styrene butadiene rubber ring</span><span>magmada alloy rotor</span><span>uev micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Conveyor Module: 2 uev electric motor · 1 uev high strength panel · 1 uev precision drive mechanism · 4 starium alloy ring · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 5 760 mB perfluoroelastomer rubber · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Conveyor Module: 2 uev electric motor · 1 uev high strength panel · 1 uev precision drive mechanism · 4 starium alloy ring · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 5 760 mB perfluoroelastomer rubber · 2 304 mB isovol</span><span class="gt-sub"><span>uev electric motor</span><span>uev high strength panel</span><span>uev precision drive mechanism</span><span>starium alloy ring</span><span>uev micropower router</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Electric Piston: 1 uev electric motor · 2 uev high strength panel · 1 uev transmission assembly · 1 magmada alloy gear · 1 small magmada alloy gear · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Electric Piston: 1 uev electric motor · 2 uev high strength panel · 1 uev transmission assembly · 1 magmada alloy gear · 1 small magmada alloy gear · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol</span><span class="gt-sub"><span>uev electric motor</span><span>uev high strength panel</span><span>uev transmission assembly</span><span>magmada alloy gear</span><span>small magmada alloy gear</span><span>uev micropower router</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Electric Motor (gtceu:uev_electric_motor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Electric Pump (gtceu:uev_electric_pump) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Electric Pump</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Conveyor Module (gtceu:uev_conveyor_module) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Conveyor Module</span><b class="gt-q">1</b></span><span class="gt-slot" title="UEV Electric Piston (gtceu:uev_electric_piston) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Electric Piston</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 1 966 080 EU/t · station research of the UHV part](#m-al)

## How to build

1. Drawers first for every part of this chain (Electric Motor, Electric Pump, Conveyor Module, Electric Piston). Drums for naquadated soldering alloy, tungsten disulfide, isovol and perfluoroelastomer rubber. Items by router or Pipez item pipe with Item Filters and Robot Arm Keep Exact into the Assembly Line bus; fluids by Pipez fluid pipes with pump covers. — `functionalstorage:oak_1`, `gtceu:uev_electric_motor`
2. Research: scan the UHV version of each component (160 CWU/t). The data item goes into the Data Access Hatch of the Assembly Line; one item per product. — `gtceu:research_station`, `gtceu:data_orb`
3. Electric Motor first: 30 s, 1 966 080 EU/t. This is the item that every other product in this chain needs. — `gtceu:assembly_line`, `gtceu:uev_electric_motor`
4. Then Electric Pump, Conveyor Module, Electric Piston one after another: the Assembly Line takes one recipe at a time, so queue by the drawers you fill, not all at once. — `gtceu:assembly_line`, `gtceu:uev_electric_pump`
5. Output drawers Keep Exact 4 per component; the pump also leaves a copy for the fluid regulator in components 2/2. — `functionalstorage:oak_1`, `gtceu:uev_electric_piston`
6. These components go into: the UEV hatches and transformers (hull + chips), the rotor holder and fusion reactor (field generator), and the era multiblocks. — `functionalstorage:oak_1`, `gtceu:uev_electric_motor`

## Tips

- Source: kjs additions/progression/components/uhv\_to\_uiv\_components.js (components(), tier uev). Every component is an Assembly Line recipe (600 ticks = 30 s) at 1 966 080 EU/t with STATION research of the UHV component of the same kind (160 CWU/t; 176 for emitter, sensor and field generator). Amounts: exponential x32 (tier scaler 5), rubber x5.
- Electric Motor: 1 uev super magnetic core · 2 long starium alloy rod · 1 uev transmission assembly · 64 fine adamantine wire · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Electric Pump: 1 uev electric motor · 1 mythrolic alloy normal fluid pipe · 1 uev microfluidic flow valve · 8 styrene butadiene rubber ring · 1 magmada alloy rotor · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol. Conveyor Module: 2 uev electric motor · 1 uev high strength panel · 1 uev precision drive mechanism · 4 starium alloy ring · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 5 760 mB perfluoroelastomer rubber · 2 304 mB isovol. Electric Piston: 1 uev electric motor · 2 uev high strength panel · 1 uev transmission assembly · 1 magmada alloy gear · 1 small magmada alloy gear · 1 uev micropower router · 2 304 mB naquadated soldering alloy · 4 000 mB tungsten disulfide · 2 304 mB isovol.
- Each recipe also exists as a Component Synthesis Forge recipe giving 64 at once for 48 times the inputs (count x 64 x 0.75, wires as spools, foils as reams), 64 x 600 ticks, stabilized cleanroom, station research of the item itself at 320 CWU/t. Unverified: which multiblock builds it and when (the Multithreaded Component Synthesis Forge is listed on the UIV page).
- Motor first: pump, conveyor, piston, robot arm and the three laser parts all take it. The pump needs the microfluidic flow valve, which needs the UHV fluid regulator (made from the UHV pump): that is why the UHV component line must stay alive. The conveyor and piston need two and one high strength panels, so build parts 2/2 before this chain.
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

- **Main source for:** `gtceu:uev_electric_motor`, `gtceu:uev_electric_pump`, `gtceu:uev_conveyor_module`, `gtceu:uev_electric_piston`
