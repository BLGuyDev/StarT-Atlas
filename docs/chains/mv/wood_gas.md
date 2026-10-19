---
kind: chain
id: wood_gas
order: 440
data:
  t: Methane & wood chemicals
  inf: true
  "n":
    - [lg, "Logs (tree farm)", s, "minecraft:oak_log"]
    - [po, Pyrolyse Oven, m, "gtceu:pyrolyse_oven"]
    - [wg, Wood Gas, f, "gtceu:wood_gas_bucket"]
    - [wt, Wood Tar, f, "gtceu:wood_tar_bucket"]
    - [wv, Wood Vinegar, f, "gtceu:wood_vinegar_bucket"]
    - [dt, "Distillery / Tower", m, "gtceu:distillation_tower"]
    - [me, Methane, o, "gtceu:methane_bucket"]
    - [ph, "Phenol / Benzene", o, "gtceu:phenol_bucket"]
    - [ac, "Acetone / Acetic acid", o, "gtceu:acetone_bucket"]
  e: [[lg, po], [po, wg], [po, wt], [po, wv], [wg, dt], [wt, dt], [wv, dt], [dt, me], [dt, ph], [dt, ac]]
  tips:
    - Pick the output fluid with the pyrolyse oven circuit.
    - Before the distillation tower, single-block distilleries pick one product per circuit.
  b: [["gtceu:pyrolyse_oven", 1], ["gtceu:lv_distillery", 3]]
---
# Methane &amp; wood chemicals

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `wood_gas` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Oil without wells (pyrolyse + distillery)](../../plan/p8.md#oil)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-po">
<div class="gt-head"><span class="gt-mname">Pyrolyse Oven</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Logs (tree farm) (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs (tree farm)</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__pyrolyse_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Wood Gas (gtceu:wood_gas_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Gas</span></span><span class="gt-slot gt-fluid" title="Wood Tar (gtceu:wood_tar_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_tar_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Tar</span></span><span class="gt-slot gt-fluid" title="Wood Vinegar (gtceu:wood_vinegar_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_vinegar_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Vinegar</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:pyrolyse_oven</code></div>
</div>
<div class="gt-panel t-multi" id="m-dt">
<div class="gt-head"><span class="gt-mname">Distillery / Tower</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Wood Gas (gtceu:wood_gas_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Gas</span></span><span class="gt-slot gt-fluid" title="Wood Tar (gtceu:wood_tar_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_tar_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Tar</span></span><span class="gt-slot gt-fluid" title="Wood Vinegar (gtceu:wood_vinegar_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_vinegar_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Vinegar</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Methane (gtceu:methane_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__methane_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Methane Bucket</span></span><span class="gt-slot gt-outp" title="Phenol / Benzene (gtceu:phenol_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__phenol_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenol Bucket</span><span class="gt-note">Phenol / Benzene</span></span><span class="gt-slot gt-outp" title="Acetone / Acetic acid (gtceu:acetone_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__acetone_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Acetone Bucket</span><span class="gt-note">Acetone / Acetic acid</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
</div>

## Flow

- [Pyrolyse Oven](#m-po) → [Distillery / Tower](#m-dt)

## Tips

- Pick the output fluid with the pyrolyse oven circuit.
- Before the distillation tower, single-block distilleries pick one product per circuit.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:pyrolyse_oven` | 1 |
| `gtceu:lv_distillery` | 3 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](../steam/tree_farm.md)
- **Main source for:** `gtceu:methane_bucket`, `gtceu:phenol_bucket`, `gtceu:acetone_bucket`
