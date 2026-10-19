---
kind: chain
id: zpm_asmd
order: 1340
data:
  t: |-
    Advanced SMDs (IV Assembler, 3840 EU/t): inductor, capacitor, diode, transistor, all with polybenzimidazole
  inf: true
  "n":
    - [pb, "Polybenzimidazole (zpm_pbi)", f, "gtceu:polybenzimidazole_bucket"]
    - - g1
      - "1 HSS-E ring · 4 fine palladium wire"
      - g
      - functionalstorage:oak_1
      - [[HSS-E ring, "gtceu:hsse_ring"], [Fine palladium wire, "gtceu:fine_palladium_wire"]]
    - [a1, "IV Assembler · 8 s · 3840 EU/t · 144 mB PBI", m, "gtceu:iv_assembler"]
    - [o1, "16 Advanced SMD inductor", x, "gtceu:advanced_smd_inductor"]
    - - g2
      - "2 PBI foil · 1 HSS-S foil"
      - g
      - functionalstorage:oak_1
      - [[PBI foil, "gtceu:polybenzimidazole_foil"], [HSS-S foil, "gtceu:hsss_foil"]]
    - [a2, "IV Assembler · 4 s · 3840 EU/t · 36 mB PBI", m, "gtceu:iv_assembler"]
    - [o2, "16 Advanced SMD capacitor", x, "gtceu:advanced_smd_capacitor"]
    - - g3
      - "1 indium gallium phosphide dust · 16 fine NbTi wire"
      - g
      - functionalstorage:oak_1
      - - [Indium gallium phosphide dust, "gtceu:indium_gallium_phosphide_dust"]
        - [Fine NbTi wire, "gtceu:fine_niobium_titanium_wire"]
    - [a3, "IV Assembler · 32 s · 3840 EU/t · 288 mB PBI", m, "gtceu:iv_assembler"]
    - [o3, "64 Advanced SMD diode", x, "gtceu:advanced_smd_diode"]
    - - g4
      - "1 vanadium gallium foil · 8 fine HSS-G wire"
      - g
      - functionalstorage:oak_1
      - [[Vanadium gallium foil, "gtceu:vanadium_gallium_foil"], [Fine HSS-G wire, "gtceu:fine_hssg_wire"]]
    - [a4, "IV Assembler · 8 s · 3840 EU/t · 144 mB PBI", m, "gtceu:iv_assembler"]
    - [o4, "16 Advanced SMD transistor", x, "gtceu:advanced_smd_transistor"]
  e:
    - [pb, a1, "144 mB"]
    - [pb, a2, "36 mB"]
    - [pb, a3, "288 mB"]
    - [pb, a4, "144 mB"]
    - [g1, a1, "1"]
    - [a1, o1, "16 / 8 s"]
    - [g2, a2, "1"]
    - [a2, o2, "16 / 4 s"]
    - [g3, a3, "1"]
    - [a3, o3, "64 / 32 s"]
    - [g4, a4, "1"]
    - [a4, o4, "16 / 8 s"]
  tips:
    - |-
      Recipes (CircuitRecipes, not changed by the pack; circuit_parts.js only adds the living and draconic SMDs): all four are IV-Assembler recipes at 3840 EU/t (above the EV cap of 2048). Inductor = 1 HSS-E ring + 4 fine palladium wire + 144 mB PBI → 16, 160 ticks. Capacitor = 2 PBI foil + 1 HSS-S foil + 36 mB PBI → 16, 80 ticks. Diode = 1 indium gallium phosphide dust + 16 fine niobium titanium wire + 288 mB PBI → 64, 640 ticks. Transistor = 1 vanadium gallium foil + 8 fine HSS-G wire + 144 mB PBI → 16, 160 ticks. The resistor (1 graphene dust + 4 fine platinum wire + 288 mB PBI → 16, 160 ticks) is not used by any ZPM recipe in this guide.
    - |-
      Where they are used: the quantum mainframe (Assembly Line: 8 inductors + 16 capacitors + 8 diodes), the crystal processor (6 capacitors + 6 transistors), crystal assembly (4 inductors + 8 capacitors), crystal computer (4 diodes) and the UV crystal mainframe (8 + 16 + 8). The quantum processor, assembly and computer also have _asmd circuit-assembler variants that use far fewer parts and half the time (processor 3 + 3 ASMD at 100 ticks, assembly 2 inductors + 4 capacitors at 200 ticks, computer 2 diodes at 200 ticks) so one batch of ASMDs goes a long way.
    - |-
      One mainframe needs only 8 + 16 + 8 ASMDs, so ONE craft of each product covers 2 mainframes (inductor, capacitor) and 8 (diode): this chain is small. The expensive inputs are HSS-S foil (luv_hsss) and the fine wires; PBI is the only fluid (zpm_pbi). The plain SMD line (smd chain) is still needed for the quantum processor, assembly and computer craft that use plain SMDs.
    - |-
      HSS-E rings and HSS-S foil: HSS-E is the IV era alloy (abs_super_ebf chain), HSS-S the LuV one; ring = extruder or lathe from a rod, foil = bender from a plate. Fine HSS-G wire and fine NbTi wire: wiremill. Vanadium gallium foil: the pack gives vanadium gallium a fine-wire flag; the foil itself is a bender product of the vanadium gallium plate. Unverified: the exact wiremill and bender times, and the vanadium gallium source (see zpm_alloys).
    - |-
      Sub-steps people skip: (1) each product needs its OWN assembler, because four different 3840 EU/t recipes in one machine would fight over the same input drawers; (2) PBI foil is a different item from the PBI plate and from the bucket; (3) diodes come 64 per craft but need the longest time (32 s), so they are the first stock to build; (4) circuit 0, no ghost circuit: do not leave a circuit in the bus.
    - |-
      Unverified: that the Advanced SMD resistor is never needed before UV (no ZPM recipe here uses it), and the graphene source for it.
  b:
    - ["gtceu:iv_assembler", 4]
    - ["gtceu:platinum_single_cable", 8]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:hsse_ring", "gtceu:fine_hssg_wire", "gtceu:polybenzimidazole_foil"]
      t: |-
        Drawers first, one per input: HSS-E rings, fine palladium wire, PBI foil, HSS-S foil, indium gallium phosphide dust, fine NbTi wire, vanadium gallium foil, fine HSS-G wire. One PBI drum shared by a Pipez fluid pipe with four branches. Four assemblers, one per product, each behind its own router with an Item Filter.
    - i: ["gtceu:iv_assembler", "gtceu:advanced_smd_inductor"]
      t: |-
        Inductor assembler: 1 HSS-E ring + 4 fine palladium wire + 144 mB PBI → 16 inductors in 8 s at 3840 EU/t. An IV Assembler on an IV hatch; no circuit in the bus. Output drawer Keep Exact 32.
    - i: ["gtceu:iv_assembler", "gtceu:advanced_smd_capacitor", "gtceu:polybenzimidazole_foil"]
      t: |-
        Capacitor assembler: 2 PBI foil + 1 HSS-S foil + 36 mB PBI → 16 capacitors in 4 s. The fastest recipe and the most used (the crystal line eats 8 + 6 per craft), so give it the biggest PBI foil drawer.
    - i: ["gtceu:iv_assembler", "gtceu:advanced_smd_diode", "gtceu:indium_gallium_phosphide_dust"]
      t: |-
        Diode assembler: 1 indium gallium phosphide dust + 16 fine NbTi wire + 288 mB PBI → 64 diodes in 32 s. Start it first and let it fill a drawer to 256.
    - i: ["gtceu:iv_assembler", "gtceu:advanced_smd_transistor", "gtceu:vanadium_gallium_foil"]
      t: |-
        Transistor assembler: 1 vanadium gallium foil + 8 fine HSS-G wire + 144 mB PBI → 16 transistors in 8 s. Needed by the crystal processor (6 per craft) and the draco lines later.
    - i: ["gtceu:iv_assembler", "gtceu:platinum_single_cable"]
      t: |-
        Power: each assembler is a single block that takes at most 3840 EU/t from an IV-rated cable run (an IV machine accepts up to 8192 V, an EV one only 2048, so an EV Assembler cannot run these). Easy to miss: they idle most of the time, so one cable run feeding all four is enough, and the capacitor/inductor machines can share a drawer queue if you are short of IV assemblers.
---
# Advanced SMDs (IV Assembler, 3840 EU/t): inductor, capacitor, diode, transistor, all with polybenzimidazole

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_asmd` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM circuit (Quantum Mainframe)](../../plan/p12.md#zpmcirc)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-a1">
<div class="gt-head"><span class="gt-mname">IV Assembler · 8 s · 3840 EU/t · 144 mB PBI</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Polybenzimidazole (zpm_pbi) (gtceu:polybenzimidazole_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">Polybenzimidazole (zpm_pbi)</span><b class="gt-q">144 mB</b></span><span class="gt-slot gt-group" title="1 HSS-E ring · 4 fine palladium wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 HSS-E ring · 4 fine palladium wire</span><span class="gt-sub"><span>HSS-E ring</span><span>Fine palladium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="16 Advanced SMD inductor (gtceu:advanced_smd_inductor) - 16 / 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_smd_inductor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced SMD Inductor</span><span class="gt-note">16 Advanced SMD inductor</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a2">
<div class="gt-head"><span class="gt-mname">IV Assembler · 4 s · 3840 EU/t · 36 mB PBI</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Polybenzimidazole (zpm_pbi) (gtceu:polybenzimidazole_bucket) - 36 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">Polybenzimidazole (zpm_pbi)</span><b class="gt-q">36 mB</b></span><span class="gt-slot gt-group" title="2 PBI foil · 1 HSS-S foil (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 PBI foil · 1 HSS-S foil</span><span class="gt-sub"><span>PBI foil</span><span>HSS-S foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="16 Advanced SMD capacitor (gtceu:advanced_smd_capacitor) - 16 / 4 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_smd_capacitor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced SMD Capacitor</span><span class="gt-note">16 Advanced SMD capacitor</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a3">
<div class="gt-head"><span class="gt-mname">IV Assembler · 32 s · 3840 EU/t · 288 mB PBI</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Polybenzimidazole (zpm_pbi) (gtceu:polybenzimidazole_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">Polybenzimidazole (zpm_pbi)</span><b class="gt-q">288 mB</b></span><span class="gt-slot gt-group" title="1 indium gallium phosphide dust · 16 fine NbTi wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 indium gallium phosphide dust · 16 fine NbTi wire</span><span class="gt-sub"><span>Indium gallium phosphide dust</span><span>Fine NbTi wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">32 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="64 Advanced SMD diode (gtceu:advanced_smd_diode) - 64 / 32 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_smd_diode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced SMD Diode</span><span class="gt-note">64 Advanced SMD diode</span><b class="gt-q">64</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a4">
<div class="gt-head"><span class="gt-mname">IV Assembler · 8 s · 3840 EU/t · 144 mB PBI</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Polybenzimidazole (zpm_pbi) (gtceu:polybenzimidazole_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">Polybenzimidazole (zpm_pbi)</span><b class="gt-q">144 mB</b></span><span class="gt-slot gt-group" title="1 vanadium gallium foil · 8 fine HSS-G wire (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 vanadium gallium foil · 8 fine HSS-G wire</span><span class="gt-sub"><span>Vanadium gallium foil</span><span>Fine HSS-G wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="16 Advanced SMD transistor (gtceu:advanced_smd_transistor) - 16 / 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_smd_transistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced SMD Transistor</span><span class="gt-note">16 Advanced SMD transistor</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
</div>

## Flow

- [IV Assembler · 8 s · 3840 EU/t · 144 mB PBI](#m-a1)
- [IV Assembler · 4 s · 3840 EU/t · 36 mB PBI](#m-a2)
- [IV Assembler · 32 s · 3840 EU/t · 288 mB PBI](#m-a3)
- [IV Assembler · 8 s · 3840 EU/t · 144 mB PBI](#m-a4)

## How to build

1. Drawers first, one per input: HSS-E rings, fine palladium wire, PBI foil, HSS-S foil, indium gallium phosphide dust, fine NbTi wire, vanadium gallium foil, fine HSS-G wire. One PBI drum shared by a Pipez fluid pipe with four branches. Four assemblers, one per product, each behind its own router with an Item Filter. — `functionalstorage:oak_1`, `gtceu:hsse_ring`, `gtceu:fine_hssg_wire`, `gtceu:polybenzimidazole_foil`
2. Inductor assembler: 1 HSS-E ring + 4 fine palladium wire + 144 mB PBI → 16 inductors in 8 s at 3840 EU/t. An IV Assembler on an IV hatch; no circuit in the bus. Output drawer Keep Exact 32. — `gtceu:iv_assembler`, `gtceu:advanced_smd_inductor`
3. Capacitor assembler: 2 PBI foil + 1 HSS-S foil + 36 mB PBI → 16 capacitors in 4 s. The fastest recipe and the most used (the crystal line eats 8 + 6 per craft), so give it the biggest PBI foil drawer. — `gtceu:iv_assembler`, `gtceu:advanced_smd_capacitor`, `gtceu:polybenzimidazole_foil`
4. Diode assembler: 1 indium gallium phosphide dust + 16 fine NbTi wire + 288 mB PBI → 64 diodes in 32 s. Start it first and let it fill a drawer to 256. — `gtceu:iv_assembler`, `gtceu:advanced_smd_diode`, `gtceu:indium_gallium_phosphide_dust`
5. Transistor assembler: 1 vanadium gallium foil + 8 fine HSS-G wire + 144 mB PBI → 16 transistors in 8 s. Needed by the crystal processor (6 per craft) and the draco lines later. — `gtceu:iv_assembler`, `gtceu:advanced_smd_transistor`, `gtceu:vanadium_gallium_foil`
6. Power: each assembler is a single block that takes at most 3840 EU/t from an IV-rated cable run (an IV machine accepts up to 8192 V, an EV one only 2048, so an EV Assembler cannot run these). Easy to miss: they idle most of the time, so one cable run feeding all four is enough, and the capacitor/inductor machines can share a drawer queue if you are short of IV assemblers. — `gtceu:iv_assembler`, `gtceu:platinum_single_cable`

## Tips

- Recipes (CircuitRecipes, not changed by the pack; circuit\_parts.js only adds the living and draconic SMDs): all four are IV-Assembler recipes at 3840 EU/t (above the EV cap of 2048). Inductor = 1 HSS-E ring + 4 fine palladium wire + 144 mB PBI → 16, 160 ticks. Capacitor = 2 PBI foil + 1 HSS-S foil + 36 mB PBI → 16, 80 ticks. Diode = 1 indium gallium phosphide dust + 16 fine niobium titanium wire + 288 mB PBI → 64, 640 ticks. Transistor = 1 vanadium gallium foil + 8 fine HSS-G wire + 144 mB PBI → 16, 160 ticks. The resistor (1 graphene dust + 4 fine platinum wire + 288 mB PBI → 16, 160 ticks) is not used by any ZPM recipe in this guide.
- Where they are used: the quantum mainframe (Assembly Line: 8 inductors + 16 capacitors + 8 diodes), the crystal processor (6 capacitors + 6 transistors), crystal assembly (4 inductors + 8 capacitors), crystal computer (4 diodes) and the UV crystal mainframe (8 + 16 + 8). The quantum processor, assembly and computer also have \_asmd circuit-assembler variants that use far fewer parts and half the time (processor 3 + 3 ASMD at 100 ticks, assembly 2 inductors + 4 capacitors at 200 ticks, computer 2 diodes at 200 ticks) so one batch of ASMDs goes a long way.
- One mainframe needs only 8 + 16 + 8 ASMDs, so ONE craft of each product covers 2 mainframes (inductor, capacitor) and 8 (diode): this chain is small. The expensive inputs are HSS-S foil (luv\_hsss) and the fine wires; PBI is the only fluid (zpm\_pbi). The plain SMD line (smd chain) is still needed for the quantum processor, assembly and computer craft that use plain SMDs.
- HSS-E rings and HSS-S foil: HSS-E is the IV era alloy (abs\_super\_ebf chain), HSS-S the LuV one; ring = extruder or lathe from a rod, foil = bender from a plate. Fine HSS-G wire and fine NbTi wire: wiremill. Vanadium gallium foil: the pack gives vanadium gallium a fine-wire flag; the foil itself is a bender product of the vanadium gallium plate. Unverified: the exact wiremill and bender times, and the vanadium gallium source (see zpm\_alloys).
- Sub-steps people skip: (1) each product needs its OWN assembler, because four different 3840 EU/t recipes in one machine would fight over the same input drawers; (2) PBI foil is a different item from the PBI plate and from the bucket; (3) diodes come 64 per craft but need the longest time (32 s), so they are the first stock to build; (4) circuit 0, no ghost circuit: do not leave a circuit in the bus.
- **Unverified** that the Advanced SMD resistor is never needed before UV (no ZPM recipe here uses it), and the graphene source for it.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_assembler` | 4 |
| `gtceu:platinum_single_cable` | 8 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `gtceu:advanced_smd_inductor`, `gtceu:advanced_smd_capacitor`, `gtceu:advanced_smd_diode`, `gtceu:advanced_smd_transistor`, `gtceu:advanced_smd_resistor`
