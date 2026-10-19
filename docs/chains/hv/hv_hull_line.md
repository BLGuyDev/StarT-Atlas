---
kind: chain
id: hv_hull_line
order: 2240
data:
  t: HV hull line (stainless casing + polyethylene)
  inf: true
  "n":
    - [sp, "8 stainless steel plates", i, "gtceu:stainless_steel_plate"]
    - [ca, HV Machine Casing, x, "gtceu:hv_machine_casing"]
    - [s1, "1 stainless steel plate", i, "gtceu:stainless_steel_plate"]
    - [pp, "2 polyethylene plates", i, "gtceu:polyethylene_plate"]
    - [gc, "2 gold cables", i, "gtceu:gold_single_cable"]
    - [mc, Mechanical Crafters, m, "create:mechanical_crafter"]
    - [hu, HV Machine Hull, o, "gtceu:hv_machine_hull"]
  e: [[sp, ca, "8"], [ca, mc], [s1, mc], [pp, mc, "2"], [gc, mc, "2"], [mc, hu]]
  tips:
    - |-
      Pack recipe: HV machine casing + 2 polyethylene plates + 1 stainless steel plate + 2 gold cables. The casing is 8 stainless steel plates around a wrench.
    - The HV Assembler is built from this hull; the assemblers that make the parts stay LV.
  b: [["create:mechanical_crafter", 6], ["modularrouters:modular_router", 2]]
---
# HV hull line (stainless casing + polyethylene)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `hv_hull_line` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [HV hulls](../../plan/p8.md#hvhull)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Mechanical Crafters</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HV Machine Casing (gtceu:hv_machine_casing)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Machine Casing</span></span><span class="gt-slot" title="1 stainless steel plate (gtceu:stainless_steel_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Plate</span><span class="gt-note">1 stainless steel plate</span></span><span class="gt-slot" title="2 polyethylene plates (gtceu:polyethylene_plate) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene Plate</span><span class="gt-note">2 polyethylene plates</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 gold cables (gtceu:gold_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">2 gold cables</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_crafter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Machine Hull (gtceu:hv_machine_hull)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Machine Hull</span></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_crafter</code></div>
</div>
</div>

## Flow

- [Mechanical Crafters](#m-mc)

### Direct steps

- 8 stainless steel plates → HV Machine Casing (8)

## Tips

- Pack recipe: HV machine casing + 2 polyethylene plates + 1 stainless steel plate + 2 gold cables. The casing is 8 stainless steel plates around a wrench.
- The HV Assembler is built from this hull; the assemblers that make the parts stay LV.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:mechanical_crafter` | 6 |
| `modularrouters:modular_router` | 2 |

## Needs / Feeds

- **Needs:** [HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers](hv_components2.md), [HV components 1/2: motor, pump, conveyor on LV assemblers](hv_components.md)
- **Main source for:** `gtceu:hv_machine_hull`, `gtceu:hv_machine_casing`
