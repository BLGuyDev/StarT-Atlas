---
kind: chain
id: geodes
order: 140
data:
  t: Rock Filtrator (gems)
  inf: true
  "n":
    - [g, "32 Gravel", i, "minecraft:gravel"]
    - [dw, Distilled Water, f, "gtceu:distilled_water_bucket"]
    - [rf, Rock Filtrator, m, "gtceu:rock_filtrator"]
    - [o1, Diamond geode, o, "kubejs:diamond_geode"]
    - [o2, Emerald geode, o, "kubejs:emerald_geode"]
    - [o3, Ruby geode, o, "kubejs:ruby_geode"]
    - [o4, Sapphire geode, o, "kubejs:sapphire_geode"]
    - [o5, Quartzite geode, o, "kubejs:quartzite_geode"]
  e: [[g, rf], [dw, rf, "1 B"], [rf, o1], [rf, o2], [rf, o3], [rf, o4], [rf, o5]]
  tips:
    - |-
      Circuit 1: diamond/emerald/ruby · 2: sapphires · 3: quartzite/realgar — half the time, +20 %.
    - |-
      The controller is LV (4 LV circuits + 4 LV motors + steel casing). MV recipe, 32 sand + 1 B distilled water, 48 s: topaz, apatite, spessartine, monazite, certus (certus geode 45 %; the certus sieve is disabled in this pack). Cutter turns a certus geode into raw certus.
  b: [["gtceu:rock_filtrator", 1], ["gtceu:lv_distillery", 1], ["gtceu:lv_macerator", 1]]
  how:
    - i: ["gtceu:rock_filtrator"]
      t: |-
        Rock Filtrator: solid casings, tempered glass, a cupronickel coil and 2 mesh blocks. One energy hatch, two output buses.
    - i: ["minecraft:gravel", "gtceu:distilled_water_bucket"]
      t: "32 gravel + 1 B distilled water per 60 s run."
    - i: ["kubejs:diamond_geode", "gtceu:lv_macerator"]
      t: Geodes → macerator / forge hammer → crushed gem ores. Use circuit 1-3 to target specific gems.
---
# Rock Filtrator (gems)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `geodes` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Geodes (Rock Filtrator)](../../plan/p2.md#geodes)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-rf">
<div class="gt-head"><span class="gt-mname">Rock Filtrator</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="32 Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span><span class="gt-note">32 Gravel</span></span><span class="gt-slot gt-fluid" title="Distilled Water (gtceu:distilled_water_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__rock_filtrator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Diamond geode (kubejs:diamond_geode)"><img class="gt-ico" src="../../assets/icons/kubejs__diamond_geode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond Geode</span></span><span class="gt-slot gt-outp" title="Emerald geode (kubejs:emerald_geode)"><img class="gt-ico" src="../../assets/icons/kubejs__emerald_geode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Emerald Geode</span></span><span class="gt-slot gt-outp" title="Ruby geode (kubejs:ruby_geode)"><img class="gt-ico" src="../../assets/icons/kubejs__ruby_geode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruby Geode</span></span><span class="gt-slot gt-outp" title="Sapphire geode (kubejs:sapphire_geode)"><img class="gt-ico" src="../../assets/icons/kubejs__sapphire_geode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sapphire Geode</span></span><span class="gt-slot gt-outp" title="Quartzite geode (kubejs:quartzite_geode)"><img class="gt-ico" src="../../assets/icons/kubejs__quartzite_geode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quartzite Geode</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:rock_filtrator</code></div>
</div>
</div>

## Flow

- [Rock Filtrator](#m-rf)

## How to build

1. Rock Filtrator: solid casings, tempered glass, a cupronickel coil and 2 mesh blocks. One energy hatch, two output buses. — `gtceu:rock_filtrator`
2. 32 gravel + 1 B distilled water per 60 s run. — `minecraft:gravel`, `gtceu:distilled_water_bucket`
3. Geodes → macerator / forge hammer → crushed gem ores. Use circuit 1-3 to target specific gems. — `kubejs:diamond_geode`, `gtceu:lv_macerator`

## Tips

- Circuit 1: diamond/emerald/ruby · 2: sapphires · 3: quartzite/realgar — half the time, +20 %.
- The controller is LV (4 LV circuits + 4 LV motors + steel casing). MV recipe, 32 sand + 1 B distilled water, 48 s: topaz, apatite, spessartine, monazite, certus (certus geode 45 %; the certus sieve is disabled in this pack). Cutter turns a certus geode into raw certus.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:rock_filtrator` | 1 |
| `gtceu:lv_distillery` | 1 |
| `gtceu:lv_macerator` | 1 |

## Needs / Feeds

- **Needs:** [Gravel, sand &amp; dust: Forge Hammers](../feeders/gravel_hammer.md)
