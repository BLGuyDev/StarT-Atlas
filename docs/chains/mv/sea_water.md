---
kind: chain
id: sea_water
order: 530
data:
  t: Salt water
  inf: true
  "n":
    - [w, Water, s, "minecraft:water_bucket"]
    - [b, "Large Barrel / Barrel", m, "gtceu:large_barrel"]
    - [sw, Sea Water, f, "exnihilosequentia:sea_water_bucket"]
    - [ce, LV Centrifuge, m, "gtceu:lv_centrifuge"]
    - [o, Salt Water, o, "gtceu:salt_water_bucket"]
    - [o2, Crushed Saltpeter, o, "gtceu:crushed_saltpeter_ore"]
    - [o3, Crushed Rock Salt, o, "gtceu:crushed_rock_salt_ore"]
  e: [[w, b, "1 B"], [b, sw], [sw, ce, "1250 mB"], [ce, o, "1 B"], [ce, o2], [ce, o3]]
  tips:
    - "Small barrel: water + any sand-type block kept inside."
    - Salt water electrolysis → chlorine + hydrogen + sodium hydroxide.
  b: [["gtceu:large_barrel", 1], ["gtceu:lv_centrifuge", 1]]
---
# Salt water

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sea_water` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Chlorine and hydrochloric acid](../../plan/p6.md#chlor)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-b">
<div class="gt-head"><span class="gt-mname">Large Barrel / Barrel</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Water (minecraft:water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span><span class="gt-tag">infinite</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sea Water (exnihilosequentia:sea_water_bucket)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__sea_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sea Water</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-ce">
<div class="gt-head"><span class="gt-mname">LV Centrifuge</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sea Water (exnihilosequentia:sea_water_bucket) - 1250 mB"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__sea_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sea Water</span><b class="gt-q">1250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Salt Water (gtceu:salt_water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__salt_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Salt Water Bucket</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-outp" title="Crushed Saltpeter (gtceu:crushed_saltpeter_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_saltpeter_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Saltpeter Ore</span></span><span class="gt-slot gt-outp" title="Crushed Rock Salt (gtceu:crushed_rock_salt_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_rock_salt_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Rock Salt Ore</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_centrifuge</code></div>
</div>
</div>

## Flow

- [Large Barrel / Barrel](#m-b) → [LV Centrifuge](#m-ce)

## Tips

- Small barrel: water + any sand-type block kept inside.
- Salt water electrolysis → chlorine + hydrogen + sodium hydroxide.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_barrel` | 1 |
| `gtceu:lv_centrifuge` | 1 |

## Needs / Feeds

- **Needs:** [Infinite water](../stone/inf_water.md)
- **Feeds:** [Chlorine, hydrogen &amp; HCl](chlorine.md)
- **Main source for:** `gtceu:salt_water_bucket`
