---
kind: chain
id: cobble_rb
order: 640
data:
  t: "Cobble: Rock Breaker (LV)"
  inf: true
  "n":
    - [lv, "Lava (adjacent)", i, "minecraft:lava_bucket"]
    - [w, "Water (adjacent)", i, "minecraft:water_bucket"]
    - [rb, Rock Breaker, m, "gtceu:lv_rock_crusher"]
    - [c, Cobblestone, o, "minecraft:cobblestone"]
  e: [[lv, rb, not used], [w, rb, not used], [rb, c]]
  tips: ["Lava and water just sit next to the machine. Higher tiers also make stone, basalt, obsidian."]
  b: [["gtceu:lv_rock_crusher", 1], ["minecraft:lava_bucket", 1], ["minecraft:water_bucket", 1]]
  how:
    - i: ["gtceu:lv_rock_crusher"]
      t: LV Rock Breaker with a lava source and a water source touching it (neither is consumed).
    - i: ["minecraft:cobblestone"]
      t: Cobble with no input; higher tiers unlock stone, basalt and obsidian.
---
# Cobble: Rock Breaker (LV)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `cobble_rb` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-rb">
<div class="gt-head"><span class="gt-mname">Rock Breaker</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Lava (adjacent) (minecraft:lava_bucket) - not used"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava Bucket</span><span class="gt-note">Lava (adjacent)</span><b class="gt-q">not used</b></span><span class="gt-slot" title="Water (adjacent) (minecraft:water_bucket) - not used"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span><span class="gt-note">Water (adjacent)</span><b class="gt-q">not used</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_rock_crusher.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Cobblestone (minecraft:cobblestone)"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_rock_crusher</code></div>
</div>
</div>

## Flow

- [Rock Breaker](#m-rb)

## How to build

1. LV Rock Breaker with a lava source and a water source touching it (neither is consumed). — `gtceu:lv_rock_crusher`
2. Cobble with no input; higher tiers unlock stone, basalt and obsidian. — `minecraft:cobblestone`

## Tips

- Lava and water just sit next to the machine. Higher tiers also make stone, basalt, obsidian.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_rock_crusher` | 1 |
| `minecraft:lava_bucket` | 1 |
| `minecraft:water_bucket` | 1 |

## Needs / Feeds

- **Needs:** [Infinite lava, obsidian &amp; pebbles](../stone/inf_lava.md), [Infinite water](../stone/inf_water.md)
