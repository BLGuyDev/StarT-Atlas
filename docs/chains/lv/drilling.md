---
kind: chain
id: drilling
order: 120
data:
  t: Drilling fluid
  inf: true
  "n":
    - [cr, Creosote, f, "gtceu:creosote_bucket"]
    - [di, Distillery, m, "gtceu:lv_distillery"]
    - [lu, Lubricant, f, "gtceu:lubricant_bucket"]
    - [w, Water, f, "minecraft:water_bucket"]
    - [sd, Stone Dust, i, "gtceu:stone_dust"]
    - [mx, Mixer, m, "gtceu:lv_mixer"]
    - [df, Drilling Fluid, o, "gtceu:drilling_fluid_bucket"]
  e: [[cr, di], [di, lu], [lu, mx, "20 mB"], [w, mx, "4980 mB"], [sd, mx, "1"], [mx, df, "5 B · 3.2 s"]]
  tips: ["Distilled water: 2.4 s.", One Void Extractor cycle eats 5 B.]
  b: [["gtceu:lv_distillery", 1], ["gtceu:lv_mixer", 1], ["gtceu:lv_macerator", 1]]
  how:
    - i: ["gtceu:creosote_bucket", "gtceu:lv_distillery"]
      t: Creosote from the coke ovens → LV Distillery → lubricant.
    - i: ["gtceu:lv_macerator", "gtceu:stone_dust"]
      t: Macerate cobble from the stone barrels into stone dust.
    - i: ["gtceu:lv_mixer", "gtceu:drilling_fluid_bucket"]
      t: |-
        LV Mixer: 1 stone dust + 20 mB lubricant + 4 980 mB water → 5 B drilling fluid in 3.2 s (2.4 s with distilled water).
---
# Drilling fluid

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `drilling` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Drilling fluid and distilled water](../../plan/p2.md#drilling)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-di">
<div class="gt-head"><span class="gt-mname">Distillery</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Creosote (gtceu:creosote_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__creosote_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Creosote</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Lubricant (gtceu:lubricant_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__lubricant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lubricant</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Lubricant (gtceu:lubricant_bucket) - 20 mB"><img class="gt-ico" src="../../assets/icons/gtceu__lubricant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lubricant</span><b class="gt-q">20 mB</b></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket) - 4980 mB"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><b class="gt-q">4980 mB</b></span><span class="gt-slot" title="Stone Dust (gtceu:stone_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__stone_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">3.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Drilling Fluid (gtceu:drilling_fluid_bucket) - 5 B · 3.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__drilling_fluid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Drilling Fluid Bucket</span><b class="gt-q">5 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
</div>

## Flow

- [Distillery](#m-di) → [Mixer](#m-mx)

## How to build

1. Creosote from the coke ovens → LV Distillery → lubricant. — `gtceu:creosote_bucket`, `gtceu:lv_distillery`
2. Macerate cobble from the stone barrels into stone dust. — `gtceu:lv_macerator`, `gtceu:stone_dust`
3. LV Mixer: 1 stone dust + 20 mB lubricant + 4 980 mB water → 5 B drilling fluid in 3.2 s (2.4 s with distilled water). — `gtceu:lv_mixer`, `gtceu:drilling_fluid_bucket`

## Tips

- Distilled water: 2.4 s.
- One Void Extractor cycle eats 5 B.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_distillery` | 1 |
| `gtceu:lv_mixer` | 1 |
| `gtceu:lv_macerator` | 1 |

## Needs / Feeds

- **Needs:** [Infinite cobble &amp; blackstone](../stone/inf_cobble.md)
- **Main source for:** `gtceu:drilling_fluid_bucket`
