---
kind: chain
id: void
order: 130
data:
  t: Void Extractor
  inf: true
  "n":
    - [df, Drilling Fluid, f, "gtceu:drilling_fluid_bucket"]
    - [ve, Void Extractor, m, "gtceu:void_extractor"]
    - [o1, Coal, o, "gtceu:raw_coal"]
    - [o2, Gold, o, "minecraft:raw_gold"]
    - [o3, Silver, o, "gtceu:raw_silver"]
    - [o4, Sodalite, o, "gtceu:raw_sodalite"]
    - [o5, Pentlandite, o, "gtceu:raw_pentlandite"]
    - [o6, Realgar, o, "gtceu:raw_realgar"]
    - [rr, Rare Ore Residue, f, "gtceu:rare_ore_residue_bucket"]
    - [rs, Raw Ore Slurry, f, "gtceu:raw_ore_slurry_bucket"]
  e:
    - [df, ve, "5 B"]
    - [ve, o1]
    - [ve, o2]
    - [ve, o3]
    - [ve, o4]
    - [ve, o5]
    - [ve, o6]
    - [ve, rr, "400 mB"]
    - [ve, rs, "600 mB"]
  tips:
    - Two output buses + two output hatches or it jams.
    - Keep both fluids from day one.
    - Build and run it on LV (30 EU/t, 32 s per cycle); only the residue processing needs an MV centrifuge and, for mixed mineral residue, HV.
    - |-
      5 B drilling fluid = stone dust + 20 mB lubricant + water in a mixer (16 EU/t): you need lubricant first.
  store: ["gtceu:lv_super_chest", "gtceu:lv_super_tank"]
  b: [["gtceu:void_extractor", 1], ["gtceu:lv_super_tank", 2], ["gtceu:lv_super_chest", 6]]
  how:
    - i: ["gtceu:void_extractor"]
      t: |-
        Void Extractor: 11 steel frames + 8 solid casings + 2 steel gearbox casings (see render). One energy hatch only.
    - i: ["gtceu:lv_input_hatch", "gtceu:drilling_fluid_bucket"]
      t: |-
        Input hatch: 5 B drilling fluid per 32 s cycle, straight from the mixer.
    - i: ["gtceu:lv_output_bus", "gtceu:lv_output_hatch"]
      t: Two output buses (raw ores) and two output hatches (rare ore residue + raw ore slurry), or it jams.
---
# Void Extractor

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `void` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Void Extractor](../../plan/p2.md#void)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-ve">
<div class="gt-head"><span class="gt-mname">Void Extractor</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Drilling Fluid (gtceu:drilling_fluid_bucket) - 5 B"><img class="gt-ico" src="../../assets/icons/gtceu__drilling_fluid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Drilling Fluid</span><b class="gt-q">5 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__void_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Coal (gtceu:raw_coal)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_coal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Coal</span></span><span class="gt-slot gt-outp" title="Gold (minecraft:raw_gold)"><img class="gt-ico" src="../../assets/icons/minecraft__raw_gold.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Gold</span></span><span class="gt-slot gt-outp" title="Silver (gtceu:raw_silver)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_silver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Silver</span></span><span class="gt-slot gt-outp" title="Sodalite (gtceu:raw_sodalite)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_sodalite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Sodalite</span></span><span class="gt-slot gt-outp" title="Pentlandite (gtceu:raw_pentlandite)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_pentlandite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Pentlandite</span></span><span class="gt-slot gt-outp" title="Realgar (gtceu:raw_realgar)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_realgar.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Realgar</span></span><span class="gt-slot gt-fluid" title="Rare Ore Residue (gtceu:rare_ore_residue_bucket) - 400 mB"><img class="gt-ico" src="../../assets/icons/gtceu__rare_ore_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Ore Residue</span><b class="gt-q">400 mB</b></span><span class="gt-slot gt-fluid" title="Raw Ore Slurry (gtceu:raw_ore_slurry_bucket) - 600 mB"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ore_slurry_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ore Slurry</span><b class="gt-q">600 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:void_extractor</code></div>
</div>
</div>

## Flow

- [Void Extractor](#m-ve)

## How to build

1. Void Extractor: 11 steel frames + 8 solid casings + 2 steel gearbox casings (see render). One energy hatch only. — `gtceu:void_extractor`
2. Input hatch: 5 B drilling fluid per 32 s cycle, straight from the mixer. — `gtceu:lv_input_hatch`, `gtceu:drilling_fluid_bucket`
3. Two output buses (raw ores) and two output hatches (rare ore residue + raw ore slurry), or it jams. — `gtceu:lv_output_bus`, `gtceu:lv_output_hatch`

## Tips

- Two output buses + two output hatches or it jams.
- Keep both fluids from day one.
- Build and run it on LV (30 EU/t, 32 s per cycle); only the residue processing needs an MV centrifuge and, for mixed mineral residue, HV.
- 5 B drilling fluid = stone dust + 20 mB lubricant + water in a mixer (16 EU/t): you need lubricant first.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:void_extractor` | 1 |
| `gtceu:lv_super_tank` | 2 |
| `gtceu:lv_super_chest` | 6 |

## Storage

`gtceu:lv_super_chest`, `gtceu:lv_super_tank`

## Needs / Feeds

- **Feeds:** [Rare Ore Residue](../mv/rare_residue.md), [Raw Ore Slurry &amp; mineral mixtures](../mv/slurry.md)
- **Main source for:** `gtceu:rare_ore_residue_bucket`, `gtceu:raw_ore_slurry_bucket`
