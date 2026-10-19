---
kind: chain
id: smd
order: 460
data:
  t: SMDs from HV Assemblers (one machine per part)
  inf: true
  "n":
    - [pe, Polyethylene, f, "gtceu:polyethylene_bucket"]
    - [ca, Carbon dust, i, "gtceu:carbon_dust"]
    - [ew, Fine electrum wire, i, "gtceu:fine_electrum_wire"]
    - [gf, Gallium foil, i, "gtceu:gallium_foil"]
    - [cw, Fine annealed copper wire, i, "gtceu:fine_annealed_copper_wire"]
    - [sf, Silicone rubber foil, i, "gtceu:silicone_rubber_foil"]
    - [af, Aluminium foil, i, "gtceu:aluminium_foil"]
    - [a1, "HV Assembler · resistor", m, "gtceu:hv_assembler"]
    - [a2, "HV Assembler · transistor", m, "gtceu:hv_assembler"]
    - [a3, "HV Assembler · capacitor", m, "gtceu:hv_assembler"]
    - [o1, "16 SMD Resistor", o, "gtceu:smd_resistor"]
    - [o2, "16 SMD Transistor", o, "gtceu:smd_transistor"]
    - [o3, "8 SMD Capacitor", o, "gtceu:smd_capacitor"]
  e:
    - [ca, a1]
    - [ew, a1, "4"]
    - [pe, a1, "288 mB"]
    - [gf, a2]
    - [cw, a2, "8"]
    - [pe, a2, "144 mB"]
    - [sf, a3]
    - [af, a3]
    - [pe, a3, "72 mB"]
    - [a1, o1, "8 s"]
    - [a2, o2, "8 s"]
    - [a3, o3, "4 s"]
  tips:
    - All SMD recipes run at 480 EU/t on an HV Assembler (fits a 512 V hatch exactly, no overclock).
    - |-
      SMDs count as the plain parts in every HV recipe (tag), but one craft gives twice as many: 16 transistors for 144 mB polyethylene vs 8.
    - |-
      Capacitor alternative: 2 PVC foil + 1 aluminium foil + 72 mB polyethylene → 12 in 4 s. Inductor: 1 nickel zinc ferrite ring + 4 fine cupronickel wire + 144 mB polyethylene → 16 (8 s). Diode: 1 gallium arsenide dust + 8 fine platinum wire + 288 mB polyethylene → 32 (10 s).
    - Sources of gallium foil, silicone rubber foil and nickel zinc ferrite were not traced; PVC foil is the other capacitor option.
  b:
    - ["gtceu:hv_assembler", 3]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 3]
    - ["gtceu:lv_robot_arm", 3]
    - ["gtceu:item_filter", 3]
    - ["pipez:fluid_pipe", 6]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:hv_assembler", "gtceu:smd_resistor", "gtceu:carbon_dust"]
      t: |-
        SMD Resistor, its own HV Assembler: 1 carbon dust + 4 fine electrum wire + 288 mB polyethylene → 16 resistors in 8 s at 480 EU/t (120 a minute). Tantalum wire instead of electrum gives 32.
    - i: ["gtceu:hv_assembler", "gtceu:smd_transistor", "gtceu:gallium_foil"]
      t: |-
        SMD Transistor, second HV Assembler: 1 gallium foil + 8 fine annealed copper wire + 144 mB polyethylene → 16 transistors in 8 s at 480 EU/t. The gallium comes from the gallium arsenide line, so this part is limited by sphalerite.
    - i: ["gtceu:hv_assembler", "gtceu:smd_capacitor", "gtceu:silicone_rubber_foil"]
      t: |-
        SMD Capacitor, third HV Assembler: 1 silicone rubber foil + 1 aluminium foil + 72 mB polyethylene → 8 capacitors in 4 s at 480 EU/t.
    - i: ["functionalstorage:oak_1", "modularrouters:modular_router"]
      t: Each assembler has input drawers for its items (Modular Router or Pipez item pipe + Item Filter) and a polyethylene drum on its fluid face. Output goes through a Robot Arm cover, Keep Exact 64, into its own stock drawer.
    - i: ["gtceu:advanced_integrated_circuit", "gtceu:smd_transistor"]
      t: |-
        Easy to miss: nothing in the first HV circuits needs SMDs. Build them once the plastic line runs steadily; they pay off for the EV nano processors (8 SMD each of resistor, capacitor and transistor) and the cleanroom circuits.
---
# SMDs from HV Assemblers (one machine per part)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `smd` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [SMDs and HV circuits](../../plan/p8.md#hvcirc)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-a1">
<div class="gt-head"><span class="gt-mname">HV Assembler · resistor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Carbon dust (gtceu:carbon_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dust</span></span><span class="gt-slot" title="Fine electrum wire (gtceu:fine_electrum_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__fine_electrum_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Electrum Wire</span><b class="gt-q">4</b></span><span class="gt-slot gt-fluid" title="Polyethylene (gtceu:polyethylene_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="16 SMD Resistor (gtceu:smd_resistor) - 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__smd_resistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">SMD Resistor</span><span class="gt-note">16 SMD Resistor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_assembler</code></div>
</div>
<div class="gt-panel t-hv" id="m-a2">
<div class="gt-head"><span class="gt-mname">HV Assembler · transistor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gallium foil (gtceu:gallium_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Foil</span></span><span class="gt-slot" title="Fine annealed copper wire (gtceu:fine_annealed_copper_wire) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__fine_annealed_copper_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Annealed Copper Wire</span><b class="gt-q">8</b></span><span class="gt-slot gt-fluid" title="Polyethylene (gtceu:polyethylene_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="16 SMD Transistor (gtceu:smd_transistor) - 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__smd_transistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">SMD Transistor</span><span class="gt-note">16 SMD Transistor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_assembler</code></div>
</div>
<div class="gt-panel t-hv" id="m-a3">
<div class="gt-head"><span class="gt-mname">HV Assembler · capacitor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silicone rubber foil (gtceu:silicone_rubber_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__silicone_rubber_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicone Rubber Foil</span></span><span class="gt-slot" title="Aluminium foil (gtceu:aluminium_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Foil</span></span><span class="gt-slot gt-fluid" title="Polyethylene (gtceu:polyethylene_bucket) - 72 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene</span><b class="gt-q">72 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="8 SMD Capacitor (gtceu:smd_capacitor) - 4 s"><img class="gt-ico" src="../../assets/icons/gtceu__smd_capacitor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">SMD Capacitor</span><span class="gt-note">8 SMD Capacitor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_assembler</code></div>
</div>
</div>

## Flow

- [HV Assembler · resistor](#m-a1)
- [HV Assembler · transistor](#m-a2)
- [HV Assembler · capacitor](#m-a3)

## How to build

1. SMD Resistor, its own HV Assembler: 1 carbon dust + 4 fine electrum wire + 288 mB polyethylene → 16 resistors in 8 s at 480 EU/t (120 a minute). Tantalum wire instead of electrum gives 32. — `gtceu:hv_assembler`, `gtceu:smd_resistor`, `gtceu:carbon_dust`
2. SMD Transistor, second HV Assembler: 1 gallium foil + 8 fine annealed copper wire + 144 mB polyethylene → 16 transistors in 8 s at 480 EU/t. The gallium comes from the gallium arsenide line, so this part is limited by sphalerite. — `gtceu:hv_assembler`, `gtceu:smd_transistor`, `gtceu:gallium_foil`
3. SMD Capacitor, third HV Assembler: 1 silicone rubber foil + 1 aluminium foil + 72 mB polyethylene → 8 capacitors in 4 s at 480 EU/t. — `gtceu:hv_assembler`, `gtceu:smd_capacitor`, `gtceu:silicone_rubber_foil`
4. Each assembler has input drawers for its items (Modular Router or Pipez item pipe + Item Filter) and a polyethylene drum on its fluid face. Output goes through a Robot Arm cover, Keep Exact 64, into its own stock drawer. — `functionalstorage:oak_1`, `modularrouters:modular_router`
5. Easy to miss: nothing in the first HV circuits needs SMDs. Build them once the plastic line runs steadily; they pay off for the EV nano processors (8 SMD each of resistor, capacitor and transistor) and the cleanroom circuits. — `gtceu:advanced_integrated_circuit`, `gtceu:smd_transistor`

## Tips

- All SMD recipes run at 480 EU/t on an HV Assembler (fits a 512 V hatch exactly, no overclock).
- SMDs count as the plain parts in every HV recipe (tag), but one craft gives twice as many: 16 transistors for 144 mB polyethylene vs 8.
- Capacitor alternative: 2 PVC foil + 1 aluminium foil + 72 mB polyethylene → 12 in 4 s. Inductor: 1 nickel zinc ferrite ring + 4 fine cupronickel wire + 144 mB polyethylene → 16 (8 s). Diode: 1 gallium arsenide dust + 8 fine platinum wire + 288 mB polyethylene → 32 (10 s).
- Sources of gallium foil, silicone rubber foil and nickel zinc ferrite were not traced; PVC foil is the other capacitor option.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_assembler` | 3 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 3 |
| `gtceu:lv_robot_arm` | 3 |
| `gtceu:item_filter` | 3 |
| `pipez:fluid_pipe` | 6 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md)
- **Main source for:** `gtceu:smd_transistor`, `gtceu:smd_resistor`, `gtceu:smd_capacitor`
