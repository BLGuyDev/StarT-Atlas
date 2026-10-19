---
kind: chain
id: radon
order: 350
data:
  t: Radon
  inf: true
  "n":
    - [lv, "Lava + redstone (LCR)", s, "minecraft:lava_bucket"]
    - [nr, Netherrack, x, "minecraft:netherrack"]
    - [na, Nether Air, f, "gtceu:nether_air_bucket"]
    - [es, "End Stone (LCR)", x, "minecraft:end_stone"]
    - [ea, Ender Air, f, "gtceu:ender_air_bucket"]
    - [vf, Vacuum Freezer, m, "gtceu:vacuum_freezer"]
    - [dt, Distillation Tower, m, "gtceu:distillation_tower"]
    - [rn, Radon, o, "gtceu:radon_bucket"]
  e: [[lv, nr, "32 per 32 B"], [nr, na, HV mixer], [na, ea], [es, ea], [ea, vf], [vf, dt, liquid], [dt, rn]]
  tips: ["Radon feeds quantum eyes/stars and the EV circuit assembler."]
  b:
    - ["gtceu:large_chemical_reactor", 1]
    - ["gtceu:hv_mixer", 2]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:distillation_tower", 1]
---
# Radon

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `radon` · **Tags:** Infinite source

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Refinery gases, liquid air, radon, epoxy](../../plan/p9.md#evfluids)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Ender Air (gtceu:ender_air_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ender_air_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender Air</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dt" title="Distillation Tower (gtceu:distillation_tower) - liquid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distillation Tower</span><b class="gt-q">liquid</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-dt">
<div class="gt-head"><span class="gt-mname">Distillation Tower</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-vf" title="Vacuum Freezer (gtceu:vacuum_freezer) - liquid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><b class="gt-q">liquid</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Radon (gtceu:radon_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__radon_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Radon Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
</div>

## Flow

- [Vacuum Freezer](#m-vf) → [Distillation Tower](#m-dt)

### Direct steps

- Lava + redstone (LCR) → Netherrack (32 per 32 B)
- Netherrack → Nether Air (HV mixer)
- Nether Air → Ender Air
- End Stone (LCR) → Ender Air

## Tips

- Radon feeds quantum eyes/stars and the EV circuit assembler.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 1 |
| `gtceu:hv_mixer` | 2 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:distillation_tower` | 1 |

## Needs / Feeds

- **Needs:** [Infinite lava, obsidian &amp; pebbles](../stone/inf_lava.md)
- **Main source for:** `minecraft:netherrack`
