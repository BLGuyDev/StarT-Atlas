---
kind: chain
id: refinery
order: 330
data:
  t: Oil refinery
  inf: true
  "n":
    - [ho, Heavy Oil, i, "gtceu:oil_heavy_bucket"]
    - [dt1, Distillation Tower, m, "gtceu:distillation_tower"]
    - [sf, Sulfuric fuels, f, "gtceu:sulfuric_heavy_fuel_bucket"]
    - [hy, Hydrogen, f, "gtceu:hydrogen_bucket"]
    - [cr, "Desulfurize (LCR)", m, "gtceu:large_chemical_reactor"]
    - [fu, "Fuels · naphtha · gas", f, "gtceu:naphtha_bucket"]
    - [ck, Cracker, m, "gtceu:cracker"]
    - [dt2, Distillation Tower, m, "gtceu:distillation_tower"]
    - [o1, Ethylene, o, "gtceu:ethylene_bucket"]
    - [o2, Propene, o, "gtceu:propene_bucket"]
    - [o3, Benzene, o, "gtceu:benzene_bucket"]
    - [o4, Toluene, o, "gtceu:toluene_bucket"]
  e:
    - [ho, dt1]
    - [dt1, sf]
    - [sf, cr]
    - [hy, cr]
    - [cr, fu]
    - [fu, ck, "steam / H₂"]
    - [ck, dt2]
    - [dt2, o1]
    - [dt2, o2]
    - [dt2, o3]
    - [dt2, o4]
  tips: [Lock each output hatch to its fluid., "H₂S from desulfurizing → sulfur back into acid."]
  b: [["gtceu:distillation_tower", 2], ["gtceu:large_chemical_reactor", 1], ["gtceu:cracker", 1]]
---
# Oil refinery

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `refinery` · **Tags:** Infinite source

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Refinery gases, liquid air, radon, epoxy](../../plan/p9.md#evfluids)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-dt1">
<div class="gt-head"><span class="gt-mname">Distillation Tower</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Heavy Oil (gtceu:oil_heavy_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oil_heavy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Heavy Bucket</span><span class="gt-note">Heavy Oil</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sulfuric fuels (gtceu:sulfuric_heavy_fuel_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Heavy Fuel</span><span class="gt-note">Sulfuric fuels</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
<div class="gt-panel t-multi" id="m-cr">
<div class="gt-head"><span class="gt-mname">Desulfurize (LCR)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfuric fuels (gtceu:sulfuric_heavy_fuel_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Heavy Fuel</span><span class="gt-note">Sulfuric fuels</span></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Fuels · naphtha · gas (gtceu:naphtha_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__naphtha_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naphtha</span><span class="gt-note">Fuels · naphtha · gas</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-ck">
<div class="gt-head"><span class="gt-mname">Cracker</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Fuels · naphtha · gas (gtceu:naphtha_bucket) - steam / H₂"><img class="gt-ico" src="../../assets/icons/gtceu__naphtha_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naphtha</span><span class="gt-note">Fuels · naphtha · gas</span><b class="gt-q">steam / H₂</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cracker.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dt2" title="Distillation Tower (gtceu:distillation_tower)"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distillation Tower</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:cracker</code></div>
</div>
<div class="gt-panel t-multi" id="m-dt2">
<div class="gt-head"><span class="gt-mname">Distillation Tower</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ck" title="Cracker (gtceu:cracker)"><img class="gt-ico" src="../../assets/icons/gtceu__cracker.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cracker</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Ethylene (gtceu:ethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethylene Bucket</span></span><span class="gt-slot gt-outp" title="Propene (gtceu:propene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__propene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Propene Bucket</span></span><span class="gt-slot gt-outp" title="Benzene (gtceu:benzene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__benzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Benzene Bucket</span></span><span class="gt-slot gt-outp" title="Toluene (gtceu:toluene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__toluene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Toluene Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
</div>

## Flow

- [Distillation Tower](#m-dt1) → [Desulfurize (LCR)](#m-cr) → [Cracker](#m-ck) → [Distillation Tower](#m-dt2)

## Tips

- Lock each output hatch to its fluid.
- H₂S from desulfurizing → sulfur back into acid.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:distillation_tower` | 2 |
| `gtceu:large_chemical_reactor` | 1 |
| `gtceu:cracker` | 1 |

## Needs / Feeds

- **Needs:** [Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff](../hv/oil_pyro.md)
- **Main source for:** `gtceu:propene_bucket`, `gtceu:benzene_bucket`, `gtceu:diesel_bucket`, `gtceu:high_octane_gasoline_bucket`
