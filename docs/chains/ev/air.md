---
kind: chain
id: air
order: 340
data:
  t: Liquid air distillation
  inf: true
  "n":
    - [gc, Gas Collectors, s, "gtceu:hv_gas_collector"]
    - [air, Air, f, "gtceu:air_bucket"]
    - [vf, Vacuum Freezer, m, "gtceu:vacuum_freezer"]
    - [la, Liquid Air, f, "gtceu:liquid_air_bucket"]
    - [dt, Distillation Tower, m, "gtceu:distillation_tower"]
    - ["n", Nitrogen, o, "gtceu:nitrogen_bucket"]
    - [o, Oxygen, o, "gtceu:oxygen_bucket"]
    - [ar, Argon, o, "gtceu:argon_bucket"]
    - [he, Helium, o, "gtceu:helium_bucket"]
  e: [[gc, air], [air, vf], [vf, la], [la, dt], [dt, "n"], [dt, o], [dt, ar], [dt, he]]
  tips: ["Nether air: 3 netherrack dust + 32 B air (HV mixer). Ender air: 3 end stone dust + 32 B nether air."]
  b: [["gtceu:hv_gas_collector", 4], ["gtceu:vacuum_freezer", 1], ["gtceu:distillation_tower", 1]]
---
# Liquid air distillation

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `air` · **Tags:** Infinite source

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Refinery gases, liquid air, radon, epoxy](../../plan/p9.md#evfluids)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Air (gtceu:air_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__air_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Air</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Liquid Air (gtceu:liquid_air_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__liquid_air_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Liquid Air</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-dt">
<div class="gt-head"><span class="gt-mname">Distillation Tower</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Liquid Air (gtceu:liquid_air_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__liquid_air_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Liquid Air</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Nitrogen (gtceu:nitrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__nitrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrogen Bucket</span></span><span class="gt-slot gt-outp" title="Oxygen (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen Bucket</span></span><span class="gt-slot gt-outp" title="Argon (gtceu:argon_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__argon_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Argon Bucket</span></span><span class="gt-slot gt-outp" title="Helium (gtceu:helium_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
</div>

## Flow

- [Vacuum Freezer](#m-vf) → [Distillation Tower](#m-dt)

### Direct steps

- Gas Collectors → Air

## Tips

- Nether air: 3 netherrack dust + 32 B air (HV mixer). Ender air: 3 end stone dust + 32 B nether air.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_gas_collector` | 4 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:distillation_tower` | 1 |

## Needs / Feeds

- **Main source for:** `gtceu:helium_bucket`
