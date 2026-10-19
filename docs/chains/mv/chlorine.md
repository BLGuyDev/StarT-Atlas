---
kind: chain
id: chlorine
order: 220
data:
  t: Chlorine, hydrogen & HCl
  inf: true
  "n":
    - [sw, Salt water, s, "gtceu:salt_water_bucket"]
    - [el, Electrolyzer, m, "gtceu:mv_electrolyzer"]
    - [cl, Chlorine, f, "gtceu:chlorine_bucket"]
    - [hy, Hydrogen, f, "gtceu:hydrogen_bucket"]
    - [na, Sodium hydroxide, o, "gtceu:sodium_hydroxide_dust"]
    - [cr, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [hcl, Hydrochloric Acid, o, "gtceu:hydrochloric_acid_bucket"]
  e: [[sw, el], [el, cl], [el, hy], [el, na], [cl, cr], [hy, cr], [cr, hcl]]
  tips:
    - |-
      Sea water: barrel with water + sand; salt from sea water processing.
    - Water electrolysis also gives H₂ + O₂.
  b: [["gtceu:mv_electrolyzer", 1], ["gtceu:mv_chemical_reactor", 1]]
---
# Chlorine, hydrogen &amp; HCl

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `chlorine` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-el">
<div class="gt-head"><span class="gt-mname">Electrolyzer</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Salt water (gtceu:salt_water_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__salt_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Salt Water Bucket</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Chlorine (gtceu:chlorine_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span></span><span class="gt-slot gt-outp" title="Sodium hydroxide (gtceu:sodium_hydroxide_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__sodium_hydroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sodium Hydroxide Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_electrolyzer</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Chlorine (gtceu:chlorine_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Hydrochloric Acid (gtceu:hydrochloric_acid_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrochloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrochloric Acid Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Electrolyzer](#m-el) → [Chem Reactor](#m-cr)

## Tips

- Sea water: barrel with water + sand; salt from sea water processing.
- Water electrolysis also gives H₂ + O₂.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_electrolyzer` | 1 |
| `gtceu:mv_chemical_reactor` | 1 |

## Needs / Feeds

- **Needs:** [Salt water](sea_water.md)
- **Main source for:** `gtceu:hydrogen_bucket`, `gtceu:chlorine_bucket`, `gtceu:hydrochloric_acid_bucket`
