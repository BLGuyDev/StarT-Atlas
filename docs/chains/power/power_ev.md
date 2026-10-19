---
kind: chain
id: power_ev
order: 320
data:
  t: EV power
  power: true
  "n":
    - [oil, Refined fuels, f, "gtceu:diesel_bucket"]
    - [lce, Large Combustion Engine, p, "gtceu:large_combustion_engine"]
    - [nb, "Nitrobenzene / benzene", f, "gtceu:nitrobenzene_bucket"]
    - [lgt, Large Gas Turbine, p, "gtceu:gas_large_turbine"]
    - [dy, EV Dynamo Hatch, x, "gtceu:ev_energy_output_hatch"]
    - [w, Enderium wire, x, "gtceu:enderium_single_wire"]
    - [bat, Lapotron batteries, x, "gtceu:ev_lapotronic_battery"]
    - [mc, EV multis, o, "gtceu:ev_assembler"]
  e: [[oil, lce], [nb, lgt], [lce, dy], [lgt, dy], [dy, w, "2048 V"], [w, bat], [bat, mc]]
  tips: ["Each rotor holder tier: 2× power for 1.8× fuel.", Oxygen boosts combustion engines.]
  b:
    - ["gtceu:large_combustion_engine", 1]
    - ["gtceu:gas_large_turbine", 1]
    - ["gtceu:ev_energy_output_hatch", 2]
    - ["gtceu:enderium_quadruple_wire", 8]
---
# EV power

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_ev` · **Tags:** Power

**Plan modules:** [EV power: nitrobenzene gas turbines](../../plan/p9.md#evpower)

**Tips:** 2

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi gt-gen" id="m-lce">
<div class="gt-head"><span class="gt-mname">Large Combustion Engine</span><span class="gt-badge t-multi">Multiblock</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Refined fuels (gtceu:diesel_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__diesel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diesel</span><span class="gt-note">Refined fuels</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_combustion_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Dynamo Hatch (gtceu:ev_energy_output_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__ev_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Energy Output Hatch</span><span class="gt-note">EV Dynamo Hatch</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_combustion_engine</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-lgt">
<div class="gt-head"><span class="gt-mname">Large Gas Turbine</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Nitrobenzene / benzene (gtceu:nitrobenzene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__nitrobenzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrobenzene</span><span class="gt-note">Nitrobenzene / benzene</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__gas_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Dynamo Hatch (gtceu:ev_energy_output_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__ev_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Energy Output Hatch</span><span class="gt-note">EV Dynamo Hatch</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:gas_large_turbine</code></div>
</div>
</div>

## Flow

- [Large Combustion Engine](#m-lce)
- [Large Gas Turbine](#m-lgt)

### Direct steps

- EV Dynamo Hatch → Enderium wire (2048 V)
- Enderium wire → Lapotron batteries
- Lapotron batteries → EV multis

## Tips

- Each rotor holder tier: 2× power for 1.8× fuel.
- Oxygen boosts combustion engines.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_combustion_engine` | 1 |
| `gtceu:gas_large_turbine` | 1 |
| `gtceu:ev_energy_output_hatch` | 2 |
| `gtceu:enderium_quadruple_wire` | 8 |
