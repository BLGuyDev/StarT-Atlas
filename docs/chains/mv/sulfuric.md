---
kind: chain
id: sulfuric
order: 200
data:
  t: Sulfuric acid
  inf: true
  "n":
    - [s, Sulfur, i, "gtceu:sulfur_dust"]
    - [o, Oxygen, f, "gtceu:oxygen_bucket"]
    - [cr1, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [so2, Sulfur Dioxide, f, "gtceu:sulfur_dioxide_bucket"]
    - [cr2, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [so3, Sulfur Trioxide, f, "gtceu:sulfur_trioxide_bucket"]
    - [w, Water, f, "minecraft:water_bucket"]
    - [cr3, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [h, Sulfuric Acid, o, "gtceu:sulfuric_acid_bucket"]
  e:
    - [s, cr1]
    - [o, cr1, "2 B"]
    - [cr1, so2]
    - [so2, cr2]
    - [o, cr2, "1 B"]
    - [cr2, so3]
    - [so3, cr3]
    - [w, cr3]
    - [cr3, h]
  tips:
    - "LCR circuit 24: one step."
    - "Sulfur: sieve dust, ore byproducts, desulfurized oil."
    - Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.
  b: [["gtceu:mv_chemical_reactor", 3]]
---
# Sulfuric acid

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sulfuric` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Oil without wells (pyrolyse + distillery)](../../plan/p8.md#oil)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-cr1">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sulfur (gtceu:sulfur_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dust</span></span><span class="gt-slot gt-fluid" title="Oxygen (gtceu:oxygen_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sulfur Dioxide (gtceu:sulfur_dioxide_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dioxide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dioxide</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr2">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfur Dioxide (gtceu:sulfur_dioxide_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dioxide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dioxide</span></span><span class="gt-slot gt-fluid" title="Oxygen (gtceu:oxygen_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sulfur Trioxide (gtceu:sulfur_trioxide_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_trioxide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Trioxide</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr3">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfur Trioxide (gtceu:sulfur_trioxide_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_trioxide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Trioxide</span></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Sulfuric Acid (gtceu:sulfuric_acid_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Acid Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Chem Reactor](#m-cr1) → [Chem Reactor](#m-cr2) → [Chem Reactor](#m-cr3)

## Tips

- LCR circuit 24: one step.
- Sulfur: sieve dust, ore byproducts, desulfurized oil.
- Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_chemical_reactor` | 3 |

## Needs / Feeds

- **Needs:** [Infinite redstone, sulfur &amp; pearls (dust sieve)](../feeders/sieve_dust.md)
- **Main source for:** `gtceu:sulfuric_acid_bucket`
