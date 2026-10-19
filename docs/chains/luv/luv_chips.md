---
kind: chain
id: luv_chips
order: 1180
data:
  t: |-
    LuV chips: Nano CPU chip (CPU wafer + carbon fibers + molten glowstone) and NOR memory chip (phosphorus wafer)
  inf: true
  "n":
    - [sw, Silicon wafer, i, "gtceu:silicon_wafer"]
    - [l1, "MV Laser Engraver · light blue lens · 45 s · 120 EU/t", m, "gtceu:mv_laser_engraver"]
    - [cw, CPU wafer, x, "gtceu:cpu_wafer"]
    - - cf
      - "16 Raw carbon fibers · 576 mB molten glowstone"
      - g
      - functionalstorage:oak_1
      - [[Raw carbon fibers, "gtceu:carbon_fibers"], [Molten glowstone, "gtceu:glowstone_bucket"]]
    - [cr, "EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t", m, "gtceu:ev_chemical_reactor"]
    - [nw, Nano CPU wafer, x, "gtceu:nano_cpu_wafer"]
    - [c1, "HV Cutter in the cleanroom · 45 s · 480 EU/t", m, "gtceu:hv_cutter"]
    - [nc, "8 Nano CPU chips", o, "gtceu:nano_cpu_chip"]
    - [pw, Phosphorus wafer, i, "gtceu:phosphorus_wafer"]
    - [l2, "HV Laser Engraver in the cleanroom · pink lens · 45 s · 480 EU/t", m, "gtceu:hv_laser_engraver"]
    - [nr, NOR memory wafer, x, "gtceu:nor_memory_wafer"]
    - [c2, "HV Cutter in the cleanroom · 45 s · 192 EU/t", m, "gtceu:hv_cutter"]
    - ["no", "16 NOR memory chips", o, "gtceu:nor_memory_chip"]
  e:
    - [sw, l1, "1"]
    - [l1, cw, "1 / 45 s"]
    - [cw, cr, "1"]
    - [cf, cr]
    - [cr, nw, "1 / 60 s"]
    - [nw, c1, "1"]
    - [c1, nc, "8 / 45 s"]
    - [pw, l2, "1"]
    - [l2, nr, "1 / 45 s"]
    - [nr, c2, "1"]
    - [c2, "no", "16 / 45 s"]
  tips:
    - |-
      Recipes (CircuitRecipes, the pack does not change them): CPU wafer = silicon wafer + light blue lens in a laser engraver, 900 ticks at 120 EU/t, no cleanroom (the same wafer as the HV circuit line). Nano CPU wafer = 1 CPU wafer + 16 raw carbon fibers + 576 mB molten glowstone, chemical reactor, CLEANROOM, 1200 ticks at 1920 EU/t (EV). Nano CPU chips: 1 wafer → 8 chips, cutter, CLEANROOM, 900 ticks at 480 EU/t.
    - |-
      NOR memory chip: NO silicon recipe exists. It needs a phosphorus-doped wafer: HV Laser Engraver, pink lens, CLEANROOM, 900 ticks at 480 EU/t → 1 NOR memory wafer; cutter, CLEANROOM, 900 ticks at 192 EU/t → 16 chips. The phosphorus boule → 32 wafers line is the one in the iv_hatches chain (EBF 2484 K, 10 minutes), so build that first. Naquadah wafers give 4 NOR wafers per wafer but need a naquadah boule (ZPM quest tier).
    - |-
      Raw carbon fibers: autoclave, 4 carbon dust + 36 mB polyethylene → 1 fiber, 37 ticks at 30 EU/t (an LV Autoclave runs it); the PTFE version (4 carbon + 18 mB PTFE → 2) needs MV. So one nano CPU wafer = 64 carbon dust + 576 mB polyethylene. Molten glowstone: glowstone dust (the dust sieve) melted in an extractor/fluid heater, 4 dust per 576 mB (144 mB each). Unverified: which machine the pack leaves for melting glowstone dust (check EMI).
    - |-
      How much you need: one Nanoprocessor Mainframe eats 2 nano CPU chips (a quarter of one wafer) and 8 NOR chips (half of one NOR wafer). One CPU wafer → one nano wafer → 8 chips is therefore 4 mainframes; one phosphorus wafer → 16 NOR chips is 2 mainframes. The chips are not the bottleneck, the phosphorus boule (10 min) and the RAM are.
    - |-
      Cleanroom: three machines here sit inside the room (EV chemical reactor, both HV cutters) plus the HV laser engraver for NOR: four machines. The wafer engraving for the plain CPU wafer (MV laser engraver) can stay outside. A cleanroom machine runs only while the room is 95 % clean.
    - |-
      Sub-steps people skip: (1) the lens is pink for NOR, light blue for CPU; (2) the cutter needs a coolant fluid (water or lubricant) in this GT version: Unverified, copy the amount the HV circuit chain uses; (3) the NOR cutter is 192 EU/t, not 480; (4) never let a wafer drawer feed two machines, the CPU wafer goes ONLY to the chemical reactor; (5) the carbon fibers are the slow input, build the autoclave first.
  b:
    - ["gtceu:mv_laser_engraver", 1]
    - ["gtceu:hv_laser_engraver", 1]
    - ["gtceu:ev_chemical_reactor", 1]
    - ["gtceu:hv_cutter", 2]
    - ["gtceu:lv_autoclave", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:silicon_wafer", "gtceu:phosphorus_wafer", "gtceu:carbon_fibers"]
      t: |-
        Drawers first: silicon wafers, phosphorus wafers, CPU wafers, raw carbon fibers, and one drum of molten glowstone and one of polyethylene. One dedicated machine per product: the CPU engraver, the nano reactor, the nano cutter, the NOR engraver and the NOR cutter never share a bus. Pipez item pipes with Item Filters and Robot Arm covers in Keep Exact mode, as in the other chains.
    - i: ["gtceu:mv_laser_engraver", "gtceu:light_blue_glass_lens", "gtceu:cpu_wafer"]
      t: |-
        CPU wafer: MV Laser Engraver with the light blue lens in its bus slot (the lens is not consumed), silicon wafer in, 45 s at 120 EU/t. This is the same machine as the HV circuit chain, so reuse that wafer drawer if it already exists.
    - i: ["gtceu:lv_autoclave", "gtceu:carbon_dust", "gtceu:carbon_fibers"]
      t: |-
        Carbon fibers: LV Autoclave, 4 carbon dust + 36 mB polyethylene, 37 ticks. 16 fibers per nano wafer, so keep a drawer of 64 carbon dust feeding it. Carbon dust: coal dust → centrifuge (see the IV motor tip).
    - i: ["gtceu:ev_chemical_reactor", "gtceu:cleanroom", "gtceu:nano_cpu_wafer"]
      t: |-
        Nano wafer: EV Chemical Reactor inside the Cleanroom. 1 CPU wafer + 16 fibers + 576 mB molten glowstone, 60 s at 1920 EU/t (an EV cable, no hatch). Pipe the glowstone from its drum through the wall by a passthrough hatch.
    - i: ["gtceu:hv_cutter", "gtceu:nano_cpu_chip"]
      t: |-
        HV Cutter inside the room: nano wafer → 8 Nano CPU chips, 45 s at 480 EU/t. Output into a drawer with Keep Exact 16; the mainframe line takes 2 per mainframe.
    - i: ["gtceu:hv_laser_engraver", "gtceu:pink_glass_lens", "gtceu:nor_memory_wafer"]
      t: |-
        NOR wafer: HV Laser Engraver inside the room with the pink lens, 1 phosphorus wafer → 1 NOR memory wafer, 45 s at 480 EU/t. The phosphorus wafer drawer is filled by the cutter of the iv_hatches chain.
    - i: ["gtceu:hv_cutter", "gtceu:nor_memory_chip"]
      t: |-
        Second HV Cutter: 1 NOR wafer → 16 NOR memory chips, 45 s at 192 EU/t. Output drawer with Keep Exact 16 (the supercomputer stage takes 4 per craft, 8 per mainframe).
---
# LuV chips: Nano CPU chip (CPU wafer + carbon fibers + molten glowstone) and NOR memory chip (phosphorus wafer)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_chips` · **Tags:** Infinite source

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Advanced boards and nano chips](../../plan/p11.md#luvboards)

**Tips:** 6

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-l1">
<div class="gt-head"><span class="gt-mname">MV Laser Engraver · light blue lens · 45 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silicon wafer (gtceu:silicon_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="CPU wafer (gtceu:cpu_wafer) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_laser_engraver</code></div>
</div>
<div class="gt-panel t-ev" id="m-cr">
<div class="gt-head"><span class="gt-mname">EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="CPU wafer (gtceu:cpu_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Wafer</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="16 Raw carbon fibers · 576 mB molten glowstone (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 Raw carbon fibers · 576 mB molten glowstone</span><span class="gt-sub"><span>Raw carbon fibers</span><span>Molten glowstone</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nano CPU wafer (gtceu:nano_cpu_wafer) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano CPU Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-c1">
<div class="gt-head"><span class="gt-mname">HV Cutter in the cleanroom · 45 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nano CPU wafer (gtceu:nano_cpu_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nano_cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano CPU Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="8 Nano CPU chips (gtceu:nano_cpu_chip) - 8 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__nano_cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano CPU Chip</span><span class="gt-note">8 Nano CPU chips</span><b class="gt-q">8</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_cutter</code></div>
</div>
<div class="gt-panel t-hv" id="m-l2">
<div class="gt-head"><span class="gt-mname">HV Laser Engraver in the cleanroom · pink lens · 45 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Phosphorus wafer (gtceu:phosphorus_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__phosphorus_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phosphorus Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="NOR memory wafer (gtceu:nor_memory_wafer) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__nor_memory_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">NOR Memory Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_laser_engraver</code></div>
</div>
<div class="gt-panel t-hv" id="m-c2">
<div class="gt-head"><span class="gt-mname">HV Cutter in the cleanroom · 45 s · 192 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="NOR memory wafer (gtceu:nor_memory_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nor_memory_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">NOR Memory Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="16 NOR memory chips (gtceu:nor_memory_chip) - 16 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__nor_memory_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">NOR Memory Chip</span><span class="gt-note">16 NOR memory chips</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_cutter</code></div>
</div>
</div>

## Flow

- [MV Laser Engraver · light blue lens · 45 s · 120 EU/t](#m-l1) → [EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t](#m-cr) → [HV Cutter in the cleanroom · 45 s · 480 EU/t](#m-c1)
- [HV Laser Engraver in the cleanroom · pink lens · 45 s · 480 EU/t](#m-l2) → [HV Cutter in the cleanroom · 45 s · 192 EU/t](#m-c2)

## How to build

1. Drawers first: silicon wafers, phosphorus wafers, CPU wafers, raw carbon fibers, and one drum of molten glowstone and one of polyethylene. One dedicated machine per product: the CPU engraver, the nano reactor, the nano cutter, the NOR engraver and the NOR cutter never share a bus. Pipez item pipes with Item Filters and Robot Arm covers in Keep Exact mode, as in the other chains. — `functionalstorage:oak_1`, `gtceu:silicon_wafer`, `gtceu:phosphorus_wafer`, `gtceu:carbon_fibers`
2. CPU wafer: MV Laser Engraver with the light blue lens in its bus slot (the lens is not consumed), silicon wafer in, 45 s at 120 EU/t. This is the same machine as the HV circuit chain, so reuse that wafer drawer if it already exists. — `gtceu:mv_laser_engraver`, `gtceu:light_blue_glass_lens`, `gtceu:cpu_wafer`
3. Carbon fibers: LV Autoclave, 4 carbon dust + 36 mB polyethylene, 37 ticks. 16 fibers per nano wafer, so keep a drawer of 64 carbon dust feeding it. Carbon dust: coal dust → centrifuge (see the IV motor tip). — `gtceu:lv_autoclave`, `gtceu:carbon_dust`, `gtceu:carbon_fibers`
4. Nano wafer: EV Chemical Reactor inside the Cleanroom. 1 CPU wafer + 16 fibers + 576 mB molten glowstone, 60 s at 1920 EU/t (an EV cable, no hatch). Pipe the glowstone from its drum through the wall by a passthrough hatch. — `gtceu:ev_chemical_reactor`, `gtceu:cleanroom`, `gtceu:nano_cpu_wafer`
5. HV Cutter inside the room: nano wafer → 8 Nano CPU chips, 45 s at 480 EU/t. Output into a drawer with Keep Exact 16; the mainframe line takes 2 per mainframe. — `gtceu:hv_cutter`, `gtceu:nano_cpu_chip`
6. NOR wafer: HV Laser Engraver inside the room with the pink lens, 1 phosphorus wafer → 1 NOR memory wafer, 45 s at 480 EU/t. The phosphorus wafer drawer is filled by the cutter of the iv\_hatches chain. — `gtceu:hv_laser_engraver`, `gtceu:pink_glass_lens`, `gtceu:nor_memory_wafer`
7. Second HV Cutter: 1 NOR wafer → 16 NOR memory chips, 45 s at 192 EU/t. Output drawer with Keep Exact 16 (the supercomputer stage takes 4 per craft, 8 per mainframe). — `gtceu:hv_cutter`, `gtceu:nor_memory_chip`

## Tips

- Recipes (CircuitRecipes, the pack does not change them): CPU wafer = silicon wafer + light blue lens in a laser engraver, 900 ticks at 120 EU/t, no cleanroom (the same wafer as the HV circuit line). Nano CPU wafer = 1 CPU wafer + 16 raw carbon fibers + 576 mB molten glowstone, chemical reactor, CLEANROOM, 1200 ticks at 1920 EU/t (EV). Nano CPU chips: 1 wafer → 8 chips, cutter, CLEANROOM, 900 ticks at 480 EU/t.
- NOR memory chip: NO silicon recipe exists. It needs a phosphorus-doped wafer: HV Laser Engraver, pink lens, CLEANROOM, 900 ticks at 480 EU/t → 1 NOR memory wafer; cutter, CLEANROOM, 900 ticks at 192 EU/t → 16 chips. The phosphorus boule → 32 wafers line is the one in the iv\_hatches chain (EBF 2484 K, 10 minutes), so build that first. Naquadah wafers give 4 NOR wafers per wafer but need a naquadah boule (ZPM quest tier).
- Raw carbon fibers: autoclave, 4 carbon dust + 36 mB polyethylene → 1 fiber, 37 ticks at 30 EU/t (an LV Autoclave runs it); the PTFE version (4 carbon + 18 mB PTFE → 2) needs MV. So one nano CPU wafer = 64 carbon dust + 576 mB polyethylene. Molten glowstone: glowstone dust (the dust sieve) melted in an extractor/fluid heater, 4 dust per 576 mB (144 mB each). Unverified: which machine the pack leaves for melting glowstone dust (check EMI).
- How much you need: one Nanoprocessor Mainframe eats 2 nano CPU chips (a quarter of one wafer) and 8 NOR chips (half of one NOR wafer). One CPU wafer → one nano wafer → 8 chips is therefore 4 mainframes; one phosphorus wafer → 16 NOR chips is 2 mainframes. The chips are not the bottleneck, the phosphorus boule (10 min) and the RAM are.
- Cleanroom: three machines here sit inside the room (EV chemical reactor, both HV cutters) plus the HV laser engraver for NOR: four machines. The wafer engraving for the plain CPU wafer (MV laser engraver) can stay outside. A cleanroom machine runs only while the room is 95 % clean.
- Sub-steps people skip: (1) the lens is pink for NOR, light blue for CPU; (2) the cutter needs a coolant fluid (water or lubricant) in this GT version: Unverified, copy the amount the HV circuit chain uses; (3) the NOR cutter is 192 EU/t, not 480; (4) never let a wafer drawer feed two machines, the CPU wafer goes ONLY to the chemical reactor; (5) the carbon fibers are the slow input, build the autoclave first.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_laser_engraver` | 1 |
| `gtceu:hv_laser_engraver` | 1 |
| `gtceu:ev_chemical_reactor` | 1 |
| `gtceu:hv_cutter` | 2 |
| `gtceu:lv_autoclave` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Feeds:** [LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)](luv_circuits.md), [Quantum chips: nano CPU wafer + radon → qubit CPU wafer → 4 chips, and the extreme circuit board (reinforced epoxy → fiber board → extreme board)](../zpm/zpm_quantum.md)
- **Main source for:** `gtceu:nano_cpu_chip`, `gtceu:nano_cpu_wafer`, `gtceu:nor_memory_chip`, `gtceu:nor_memory_wafer`
