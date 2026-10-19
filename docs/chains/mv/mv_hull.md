---
kind: chain
id: mv_hull
order: 900
data:
  t: First MV hull and the LV → MV transformer
  "n":
    - [al, "9 Aluminium", i, "gtceu:aluminium_ingot"]
    - [be, Bender, m, "gtceu:lv_bender"]
    - [ap, Aluminium plates, x, "gtceu:aluminium_plate"]
    - [ca, "MV Machine Casing (8 plates + wrench)", x, "gtceu:mv_machine_casing"]
    - [wi, "2 Wrought iron plates", i, "gtceu:wrought_iron_plate"]
    - [cw, Copper wire, i, "gtceu:copper_single_wire"]
    - [lr, "144 mB liquid rubber", f, "gtceu:rubber_bucket"]
    - [as, Assembler, m, "gtceu:lv_assembler"]
    - [cc, "2 Copper cables", x, "gtceu:copper_single_cable"]
    - [hu, MV Machine Hull, o, "gtceu:mv_machine_hull"]
    - [lh, "LV hull + 4 tin cables", i, "gtceu:lv_machine_hull"]
    - [tr, LV Transformer, o, "gtceu:lv_transformer_1a"]
  e:
    - [al, be]
    - [be, ap]
    - [ap, ca, "8"]
    - [ap, hu, "1"]
    - [ca, hu]
    - [wi, hu]
    - [cw, as]
    - [lr, as]
    - [as, cc]
    - [cc, hu, "2"]
    - [cc, tr, "1"]
    - [lh, tr]
  tips:
    - |-
      Crafting grid, top row: wrought iron plate, aluminium plate, wrought iron plate. Bottom row: copper cable, MV machine casing, copper cable.
    - |-
      Copper is an MV cable: it has NO hand recipe with rubber plates (tin does). Make it in the assembler: 1 copper wire + 144 mB liquid rubber.
    - |-
      Per MV hull: 9 aluminium, 2 iron, 1 copper and 288 mB liquid rubber. The assembler hull recipe needs polyethylene (MV chemistry), so craft it by hand.
  b:
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_chemical_reactor", 1]
    - ["gtceu:lv_transformer_1a", 1]
  how:
    - i: ["gtceu:lv_bender", "gtceu:aluminium_plate"]
      t: |-
        LV Bender: 1 aluminium → 1 plate at 24 EU/t, so it works on LV power. 9 plates per hull.
    - i: ["gtceu:mv_machine_casing"]
      t: |-
        MV Machine Casing: 8 aluminium plates around a wrench (or LV assembler, circuit 8).
    - i: ["gtceu:lv_chemical_reactor", "gtceu:rubber_bucket", "gtceu:copper_single_cable"]
      t: |-
        Copper cable: LV Chemical Reactor 3 rubber + 1 sulfur → 576 mB liquid rubber (4 cables), then assembler 1 copper wire + 144 mB → 1 copper cable.
    - i: ["gtceu:mv_machine_hull"]
      t: Craft the hull by hand with the layout above.
    - i: ["gtceu:lv_transformer_1a", "gtceu:lv_machine_hull", "gtceu:tin_single_cable"]
      t: |-
        To run MV machines from LV power you do not need an MV hull: LV Transformer = LV hull + 4 tin cables + 1 copper cable. Switch it to step-up (check its tooltip for the tool): 4 A of LV in, 1 A of MV (128 EU/t) out.
    - i: ["thermal:dynamo_lapidary", "create_new_age:generator_coil"]
      t: An MV machine at full speed needs 128 EU/t, i.e. 512 FE/t from your coils or 4 A of LV.
---
# First MV hull and the LV → MV transformer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_hull`

**Era setup:** [MV](../../eras/mv.md)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="9 Aluminium (gtceu:aluminium_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Ingot</span><span class="gt-note">9 Aluminium</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Aluminium plates (gtceu:aluminium_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Plate</span><span class="gt-note">Aluminium plates</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper wire (gtceu:copper_single_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Wire</span><span class="gt-note">Copper wire</span></span><span class="gt-slot gt-fluid" title="144 mB liquid rubber (gtceu:rubber_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><span class="gt-note">144 mB liquid rubber</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Copper cables (gtceu:copper_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Single Cable</span><span class="gt-note">2 Copper cables</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Bender](#m-be)
- [Assembler](#m-as)

### Direct steps

- Aluminium plates → MV Machine Casing (8 plates + wrench) (8)
- Aluminium plates → MV Machine Hull (1)
- MV Machine Casing (8 plates + wrench) → MV Machine Hull
- 2 Wrought iron plates → MV Machine Hull
- 2 Copper cables → MV Machine Hull (2)
- 2 Copper cables → LV Transformer (1)
- LV hull + 4 tin cables → LV Transformer

## How to build

1. LV Bender: 1 aluminium → 1 plate at 24 EU/t, so it works on LV power. 9 plates per hull. — `gtceu:lv_bender`, `gtceu:aluminium_plate`
2. MV Machine Casing: 8 aluminium plates around a wrench (or LV assembler, circuit 8). — `gtceu:mv_machine_casing`
3. Copper cable: LV Chemical Reactor 3 rubber + 1 sulfur → 576 mB liquid rubber (4 cables), then assembler 1 copper wire + 144 mB → 1 copper cable. — `gtceu:lv_chemical_reactor`, `gtceu:rubber_bucket`, `gtceu:copper_single_cable`
4. Craft the hull by hand with the layout above. — `gtceu:mv_machine_hull`
5. To run MV machines from LV power you do not need an MV hull: LV Transformer = LV hull + 4 tin cables + 1 copper cable. Switch it to step-up (check its tooltip for the tool): 4 A of LV in, 1 A of MV (128 EU/t) out. — `gtceu:lv_transformer_1a`, `gtceu:lv_machine_hull`, `gtceu:tin_single_cable`
6. An MV machine at full speed needs 128 EU/t, i.e. 512 FE/t from your coils or 4 A of LV. — `thermal:dynamo_lapidary`, `create_new_age:generator_coil`

## Tips

- Crafting grid, top row: wrought iron plate, aluminium plate, wrought iron plate. Bottom row: copper cable, MV machine casing, copper cable.
- Copper is an MV cable: it has NO hand recipe with rubber plates (tin does). Make it in the assembler: 1 copper wire + 144 mB liquid rubber.
- Per MV hull: 9 aluminium, 2 iron, 1 copper and 288 mB liquid rubber. The assembler hull recipe needs polyethylene (MV chemistry), so craft it by hand.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_chemical_reactor` | 1 |
| `gtceu:lv_transformer_1a` | 1 |

## Needs / Feeds

- **Needs:** [Infinite aluminium (clay)](aluminium.md), [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md), [LV hull line (Create mechanical crafters)](../lv/lv_hull_line.md)
