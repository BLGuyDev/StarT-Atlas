---
kind: chain
id: distilled
order: 160
data:
  t: Distilled water
  inf: true
  "n":
    - [w, Water, s, "minecraft:water_bucket"]
    - [di, "Distillery · circ 5", m, "gtceu:lv_distillery"]
    - [dw, Distilled Water, o, "gtceu:distilled_water_bucket"]
  e: [[w, di], [di, dw]]
  tips: [Feeds the Rock Filtrator and drilling fluid.]
  b: [["gtceu:lv_distillery", 1]]
---
# Distilled water

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `distilled` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Drilling fluid and distilled water](../../plan/p2.md#drilling)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-di">
<div class="gt-head"><span class="gt-mname">Distillery · circ 5</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Distilled Water (gtceu:distilled_water_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_distillery</code></div>
</div>
</div>

## Flow

- [Distillery · circ 5](#m-di)

## Tips

- Feeds the Rock Filtrator and drilling fluid.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_distillery` | 1 |

## Needs / Feeds

- **Needs:** [Infinite water](../stone/inf_water.md)
- **Main source for:** `gtceu:distilled_water_bucket`
