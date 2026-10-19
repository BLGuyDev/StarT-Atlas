---
kind: chain
id: mv_hull_line
order: 930
data:
  t: MV hull line (Create mechanical crafters)
  inf: true
  "n":
    - [pl, "8 Aluminium plates", i, "gtceu:aluminium_plate"]
    - [as, "Assembler · circuit 8", m, "gtceu:lv_assembler"]
    - [ca, MV Machine Casing, x, "gtceu:mv_machine_casing"]
    - [hp, "2 Wrought iron plates", i, "gtceu:wrought_iron_plate"]
    - [pp, "1 Aluminium plate", i, "gtceu:aluminium_plate"]
    - [cb, "2 Copper cables", i, "gtceu:copper_single_cable"]
    - [mc, "Mechanical Crafters 3×2", m, "create:mechanical_crafter"]
    - [hu, MV Machine Hull, o, "gtceu:mv_machine_hull"]
  e: [[pl, as], [as, ca, "2.5 s"], [ca, mc], [hp, mc], [pp, mc], [cb, mc], [mc, hu]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["create:mechanical_crafter", 6]
    - ["modularrouters:modular_router", 2]
    - ["functionalstorage:oak_1", 5]
  tips:
    - |-
      Hull layout (2 rows): wrought iron plate, aluminium plate, wrought iron plate / copper cable, MV casing, copper cable.
    - |-
      Copper cable has no hand recipe: assembler, 1 copper wire + 144 mB liquid rubber. The assembler hull recipe needs polyethylene, so the crafters are the LV-power way.
  how:
    - i: ["gtceu:lv_bender", "gtceu:aluminium_plate"]
      t: "LV Bender: 1 aluminium → 1 plate (24 EU/t). 9 per hull."
    - i: ["gtceu:lv_assembler", "gtceu:mv_machine_casing"]
      t: |-
        Assembler on circuit 8: 8 aluminium plates → 1 MV Machine Casing in 2.5 s.
    - i: ["gtceu:copper_single_cable", "gtceu:rubber_bucket"]
      t: Copper cables from the cable assembler (wire + 144 mB liquid rubber).
    - i: ["create:mechanical_crafter", "gtceu:mv_machine_hull"]
      t: Same 3×2 Mechanical Crafter grid as the LV hull line, fed by routers. Keep 8 MV hulls.
    - i: ["gtceu:lv_transformer_1a"]
      t: |-
        Power for MV machines without MV generation: LV Transformer (LV hull + 4 tin cables + 1 copper cable) on step-up: 4 A LV in, 1 A MV out.
  s3d:
    b:
      - ["functionalstorage:oak_1", 0, 0, 1, 1, 1, 1, Aluminium ingot drawer]
      - ["gtceu:lv_bender", 2, 0, 1, 1, 1, 1, "LV Bender · 1 ingot → 1 plate · 24 EU/t"]
      - ["functionalstorage:oak_1", 4, 0, 1, 1, 1, 1, Aluminium plate drawer]
      - ["gtceu:lv_assembler", 6, 0, 1, 1, 1, 1, "LV Assembler · circuit 8 · 8 plates → MV casing"]
      - ["modularrouters:modular_router", 11, 0, 1, 1, 1, 1, "Modular Router (casing → feed drawer)"]
      - ["functionalstorage:oak_1", 13, 1, 0, 1, 1, 1, "Feed drawer · Wrought iron plate"]
      - ["functionalstorage:oak_1", 13, 1, 1, 1, 1, 1, "Feed drawer · Aluminium plate"]
      - ["functionalstorage:oak_1", 13, 1, 2, 1, 1, 1, "Feed drawer · Wrought iron plate"]
      - ["functionalstorage:oak_1", 13, 0, 0, 1, 1, 1, "Feed drawer · Copper cable"]
      - ["functionalstorage:oak_1", 13, 0, 1, 1, 1, 1, "Feed drawer · MV Machine Casing"]
      - ["functionalstorage:oak_1", 13, 0, 2, 1, 1, 1, "Feed drawer · Copper cable"]
      - ["create:mechanical_crafter", 16, 0, 0, 1, 2, 3, "Mechanical Crafter (3×2 grid, hull recipe)"]
      - ["create:shaft", 16, 2, 0, 1, 1, 3, "Shaft (steam engine rotation)"]
      - ["functionalstorage:oak_1", 18, 0, 2, 1, 1, 1, MV Machine Hull drawer]
      - ["gtceu:lv_robot_arm", 19, 0, 2, 1, 1, 1, "Robot Arm cover · Keep Exact 16"]
    p:
      - [i, [1, 0.5, 1.5], [2, 0.5, 1.5]]
      - [i, [3, 0.5, 1.5], [4, 0.5, 1.5]]
      - [i, [5, 0.5, 1.5], [6, 0.5, 1.5]]
      - [i, [7, 0.5, 1.5], [11, 0.5, 1.5]]
      - [i, [12, 0.5, 1.5], [13, 0.5, 1.5]]
      - [i, [14, 1.5, 0.5], [16, 1.5, 0.5]]
      - [i, [14, 1.5, 1.5], [16, 1.5, 1.5]]
      - [i, [14, 1.5, 2.5], [16, 1.5, 2.5]]
      - [i, [14, 0.5, 0.5], [16, 0.5, 0.5]]
      - [i, [14, 0.5, 1.5], [16, 0.5, 1.5]]
      - [i, [14, 0.5, 2.5], [16, 0.5, 2.5]]
      - [i, [17, 0.5, 2.5], [18, 0.5, 2.5]]
      - [r, [16.5, 2.5, 3], [16.5, 2.5, 6.5]]
    l:
      - [Aluminium ingots, 0.5, 1.9, 1.5]
      - ["Bender · 9 plates per hull", 2.5, 3.4, 1.5]
      - [Aluminium plates, 4.5, 1.4, 1.5]
      - ["Assembler · circuit 8 · 2.5 s", 6.5, 2.4, 1.5]
      - ["Router → feed", 11.5, 1.9, 1.5]
      - ["6 feed drawers", 13.5, 3.6, 1.5]
      - ["6 Mechanical Crafters 3×2", 16.5, 4.4, 1.5]
      - ["Top row: 3 plates", 16.5, 6.2, 1.5]
      - ["Bottom row: cable + casing", 16.5, 8, 1.5]
      - [MV hull stock 16, 18.5, 1.9, 2.5]
      - [Shaft from the steam engine line, 16.5, 3.3, 6.5]
---
# MV hull line (Create mechanical crafters)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_hull_line` · **Tags:** Infinite source, 3D scene

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [MV hulls + transformer](../../plan/p5.md#mvhull)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · circuit 8</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Aluminium plates (gtceu:aluminium_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Plate</span><span class="gt-note">8 Aluminium plates</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="MV Machine Casing (gtceu:mv_machine_casing) - 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__mv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Machine Casing</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Mechanical Crafters 3×2</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="MV Machine Casing (gtceu:mv_machine_casing)"><img class="gt-ico" src="../../assets/icons/gtceu__mv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Machine Casing</span></span><span class="gt-slot" title="2 Wrought iron plates (gtceu:wrought_iron_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Plate</span><span class="gt-note">2 Wrought iron plates</span></span><span class="gt-slot" title="1 Aluminium plate (gtceu:aluminium_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Plate</span><span class="gt-note">1 Aluminium plate</span></span><span class="gt-slot" title="2 Copper cables (gtceu:copper_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Cable</span><span class="gt-note">2 Copper cables</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_crafter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="MV Machine Hull (gtceu:mv_machine_hull)"><img class="gt-ico" src="../../assets/icons/gtceu__mv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">MV Machine Hull</span></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_crafter</code></div>
</div>
</div>

## Flow

- [Assembler · circuit 8](#m-as) → [Mechanical Crafters 3×2](#m-mc)

## How to build

1. LV Bender: 1 aluminium → 1 plate (24 EU/t). 9 per hull. — `gtceu:lv_bender`, `gtceu:aluminium_plate`
2. Assembler on circuit 8: 8 aluminium plates → 1 MV Machine Casing in 2.5 s. — `gtceu:lv_assembler`, `gtceu:mv_machine_casing`
3. Copper cables from the cable assembler (wire + 144 mB liquid rubber). — `gtceu:copper_single_cable`, `gtceu:rubber_bucket`
4. Same 3×2 Mechanical Crafter grid as the LV hull line, fed by routers. Keep 8 MV hulls. — `create:mechanical_crafter`, `gtceu:mv_machine_hull`
5. Power for MV machines without MV generation: LV Transformer (LV hull + 4 tin cables + 1 copper cable) on step-up: 4 A LV in, 1 A MV out. — `gtceu:lv_transformer_1a`

## Tips

- Hull layout (2 rows): wrought iron plate, aluminium plate, wrought iron plate / copper cable, MV casing, copper cable.
- Copper cable has no hand recipe: assembler, 1 copper wire + 144 mB liquid rubber. The assembler hull recipe needs polyethylene, so the crafters are the LV-power way.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `create:mechanical_crafter` | 6 |
| `modularrouters:modular_router` | 2 |
| `functionalstorage:oak_1` | 5 |

## Needs / Feeds

- **Needs:** [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md)
- **Main source for:** `gtceu:mv_machine_hull`

## Extras

- 3D assembly scene with 15 blocks (open it in the Atlas page).
