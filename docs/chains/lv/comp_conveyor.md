---
kind: chain
id: comp_conveyor
order: 820
data:
  t: LV Conveyor Module line
  inf: true
  "n":
    - [m, "2 Motors", i, "gtceu:lv_electric_motor"]
    - [c, "1 Tin cable", i, "gtceu:tin_single_cable"]
    - [lr, "864 mB liquid rubber", i, "gtceu:rubber_bucket"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [out, LV Conveyor Module, o, "gtceu:lv_conveyor_module"]
  e: [[m, as], [c, as], [lr, as], [as, out, "12 / min"]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["functionalstorage:oak_1", 1]
    - ["pipez:item_pipe", 8]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_conveyor_module"]
      t: |-
        Assembler, circuit 1: 2 motors + 1 tin cable + 864 mB liquid rubber → 1 conveyor in 5 s. Pipe the rubber in through an input hatch side (fluid pipe).
    - i: ["gtceu:rubber_bucket"]
      t: |-
        864 mB is 6 plates’ worth of rubber: the liquid route skips the solidifier.
---
# LV Conveyor Module line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_conveyor` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Motors (gtceu:lv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Motor</span><span class="gt-note">2 Motors</span></span><span class="gt-slot" title="1 Tin cable (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">1 Tin cable</span></span><span class="gt-slot" title="864 mB liquid rubber (gtceu:rubber_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber Bucket</span><span class="gt-note">864 mB liquid rubber</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Conveyor Module (gtceu:lv_conveyor_module) - 12 / min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Conveyor Module</span><b class="gt-q">12 / min</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Assembler, circuit 1: 2 motors + 1 tin cable + 864 mB liquid rubber → 1 conveyor in 5 s. Pipe the rubber in through an input hatch side (fluid pipe). — `gtceu:lv_assembler`, `gtceu:lv_conveyor_module`
2. 864 mB is 6 plates’ worth of rubber: the liquid route skips the solidifier. — `gtceu:rubber_bucket`

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `functionalstorage:oak_1` | 1 |
| `pipez:item_pipe` | 8 |

## Needs / Feeds

- **Needs:** [LV Electric Motor line](comp_motor.md), [Parts row 2: wires, fine wire, cables](comp_wires.md)
- **Main source for:** `gtceu:lv_conveyor_module`
