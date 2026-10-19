---
kind: chain
id: etchant
order: 230
data:
  t: Board etching
  "n":
    - [fe, Iron dust, i, "gtceu:iron_dust"]
    - [hcl, Hydrochloric Acid, f, "gtceu:hydrochloric_acid_bucket"]
    - [cr, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [fc, Iron III Chloride, f, "gtceu:iron_iii_chloride_bucket"]
    - [bd, "Board + copper foil", i, "gtceu:phenolic_circuit_board"]
    - [cr2, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [pb, Printed board, o, "gtceu:phenolic_printed_circuit_board"]
  e: [[fe, cr], [hcl, cr, "3 B"], [cr, fc], [fc, cr2], [bd, cr2], [cr2, pb]]
  tips: ["Sodium persulfate works too; cupric chloride in EV."]
  b: [["gtceu:mv_chemical_reactor", 2]]
---
# Board etching

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `etchant`

**Era setup:** [MV](../../eras/mv.md)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-cr">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron dust (gtceu:iron_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span></span><span class="gt-slot gt-fluid" title="Hydrochloric Acid (gtceu:hydrochloric_acid_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrochloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrochloric Acid</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Iron III Chloride (gtceu:iron_iii_chloride_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_iii_chloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Iii Chloride</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr2">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Iron III Chloride (gtceu:iron_iii_chloride_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_iii_chloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Iii Chloride</span></span><span class="gt-slot" title="Board + copper foil (gtceu:phenolic_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Circuit Board</span><span class="gt-note">Board + copper foil</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Printed board (gtceu:phenolic_printed_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Printed Circuit Board</span><span class="gt-note">Printed board</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Chem Reactor](#m-cr) → [Chem Reactor](#m-cr2)

## Tips

- Sodium persulfate works too; cupric chloride in EV.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_chemical_reactor` | 2 |

## Needs / Feeds

- **Needs:** [Ore processing](../lv/ores.md), [Phenolic printed circuit board (silver foil + etching)](mv_board.md)
