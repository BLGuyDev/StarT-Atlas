---
kind: chain
id: polyethylene
order: 210
data:
  t: Polyethylene
  inf: true
  "n":
    - [bm, "Plant balls / biomass", s, "gtceu:plant_ball"]
    - [br, "Brewery + Fermenter", m, "gtceu:lv_fermenter"]
    - [et, Ethanol, f, "gtceu:ethanol_bucket"]
    - [h, Sulfuric acid, f, "gtceu:sulfuric_acid_bucket"]
    - [cr, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [eth, Ethylene, f, "gtceu:ethylene_bucket"]
    - [air, Oxygen, f, "gtceu:oxygen_bucket"]
    - [cr2, Chem Reactor, m, "gtceu:mv_chemical_reactor"]
    - [pe, Polyethylene, o, "gtceu:polyethylene_bucket"]
  e: [[bm, br], [br, et], [et, cr], [h, cr, catalyst], [cr, eth], [eth, cr2], [air, cr2], [cr2, pe]]
  tips:
    - Oxygen gives 1.5× the polymer of air.
    - "Diluted acid comes back: re-concentrate it."
    - "Later: ethylene from oil cracking."
    - |-
      No oil needed: distil biomass (600 mB ethanol per B, 400 EU/t, so an HV distillery) + 1 B sulfuric acid per B ethanol → 1 B ethylene in a chemical reactor (120 EU/t, 60 s, diluted acid returns). 144 mB ethylene + 1 B air → 144 mB polyethylene; with 1 B oxygen → 216 mB. In the LCR, 100 mB titanium tetrachloride per 2.16 B ethylene gives ×1.5 on air or ×2 on oxygen.
    - Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.
  b:
    - ["gtceu:lv_brewery", 1]
    - ["gtceu:lv_fermenter", 1]
    - ["gtceu:lv_distillery", 1]
    - ["gtceu:mv_chemical_reactor", 2]
---
# Polyethylene

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `polyethylene` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Polyethylene and PTFE](../../plan/p8.md#plastics)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-br">
<div class="gt-head"><span class="gt-mname">Brewery + Fermenter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Plant balls / biomass (gtceu:plant_ball)"><img class="gt-ico" src="../../assets/icons/gtceu__plant_ball.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plant Ball</span><span class="gt-note">Plant balls / biomass</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_fermenter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Ethanol (gtceu:ethanol_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ethanol_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethanol</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_fermenter</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Ethanol (gtceu:ethanol_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ethanol_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethanol</span></span><span class="gt-slot gt-fluid" title="Sulfuric acid (gtceu:sulfuric_acid_bucket) - catalyst"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Acid</span><b class="gt-q">catalyst</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Ethylene (gtceu:ethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethylene</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-cr2">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Ethylene (gtceu:ethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__ethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethylene</span></span><span class="gt-slot gt-fluid" title="Oxygen (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Polyethylene (gtceu:polyethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Brewery + Fermenter](#m-br) → [Chem Reactor](#m-cr) → [Chem Reactor](#m-cr2)

## Tips

- Oxygen gives 1.5× the polymer of air.
- Diluted acid comes back: re-concentrate it.
- Later: ethylene from oil cracking.
- No oil needed: distil biomass (600 mB ethanol per B, 400 EU/t, so an HV distillery) + 1 B sulfuric acid per B ethanol → 1 B ethylene in a chemical reactor (120 EU/t, 60 s, diluted acid returns). 144 mB ethylene + 1 B air → 144 mB polyethylene; with 1 B oxygen → 216 mB. In the LCR, 100 mB titanium tetrachloride per 2.16 B ethylene gives ×1.5 on air or ×2 on oxygen.
- Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_brewery` | 1 |
| `gtceu:lv_fermenter` | 1 |
| `gtceu:lv_distillery` | 1 |
| `gtceu:mv_chemical_reactor` | 2 |

## Needs / Feeds

- **Needs:** [Crops: Large Farm (no power)](../steam/crop_farm.md)
- **Feeds:** [HV circuits: Advanced Integrated Circuit and Microprocessor Assembly](../hv/circuits_hv.md), [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../iv/iv_circuits.md)
- **Main source for:** `gtceu:ethanol_bucket`, `gtceu:plastic_printed_circuit_board`, `gtceu:polyethylene_bucket`
