---
kind: chain
id: coils
order: 110
data:
  t: Cupronickel coils ×16
  "n":
    - [cu, Copper, i, "minecraft:copper_ingot"]
    - [ni, Nickel, i, "gtceu:nickel_ingot"]
    - [cn, Cupronickel, x, "gtceu:cupronickel_ingot"]
    - [wm, Wiremill, m, "gtceu:lv_wiremill"]
    - [dw, "8× double wire", x, "gtceu:cupronickel_double_wire"]
    - [bz, Bronze, i, "gtceu:bronze_ingot"]
    - [bd, Bender, m, "gtceu:lv_bender"]
    - [bf, "8× bronze foil", x, "gtceu:bronze_foil"]
    - [ta, "144 mB Tin Alloy", f, "gtceu:tin_alloy_bucket"]
    - [as, Assembler, m, "gtceu:lv_assembler"]
    - [co, Cupronickel Coil, o, "gtceu:cupronickel_coil_block"]
  e: [[cu, cn], [ni, cn], [cn, wm], [wm, dw], [bz, bd], [bd, bf], [dw, as], [bf, as], [ta, as], [as, co]]
  tips: ["16 coils = 128 double wires + 128 foils + 2304 mB tin alloy."]
  b:
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_extractor", 1]
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_mixer", 1]
---
# Cupronickel coils ×16

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `coils`

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Cupronickel coils](../../plan/p5.md#coils)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">Wiremill</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cupronickel (gtceu:cupronickel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8× double wire (gtceu:cupronickel_double_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Double Wire</span><span class="gt-note">8× double wire</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-bd">
<div class="gt-head"><span class="gt-mname">Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Bronze (gtceu:bronze_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8× bronze foil (gtceu:bronze_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Foil</span><span class="gt-note">8× bronze foil</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8× double wire (gtceu:cupronickel_double_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Double Wire</span><span class="gt-note">8× double wire</span></span><span class="gt-slot" title="8× bronze foil (gtceu:bronze_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Foil</span><span class="gt-note">8× bronze foil</span></span><span class="gt-slot gt-fluid" title="144 mB Tin Alloy (gtceu:tin_alloy_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Alloy</span><span class="gt-note">144 mB Tin Alloy</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Cupronickel Coil (gtceu:cupronickel_coil_block)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Coil Block</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Wiremill](#m-wm) → [Assembler](#m-as)
- [Bender](#m-bd) → [Assembler](#m-as)

### Direct steps

- Copper → Cupronickel
- Nickel → Cupronickel

## Tips

- 16 coils = 128 double wires + 128 foils + 2304 mB tin alloy.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_extractor` | 1 |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_mixer` | 1 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md), [Ore processing](ores.md), [Alloys: Steam / LV Alloy Smelter (more per ingot)](../steam/alloys_smelter.md)
- **Feeds:** [MV components on LV machines](../mv/comp_mv.md)
- **Main source for:** `gtceu:cupronickel_ingot`
