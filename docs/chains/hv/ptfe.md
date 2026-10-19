---
kind: chain
id: ptfe
order: 280
data:
  t: "PTFE: three HV Chemical Reactors"
  inf: true
  "n":
    - [me, Methane, f, "gtceu:methane_bucket"]
    - [cl, Chlorine, f, "gtceu:chlorine_bucket"]
    - [cr1, Chem Reactor, m, "gtceu:hv_chemical_reactor"]
    - [chf, Chloroform, f, "gtceu:chloroform_bucket"]
    - [hf, Hydrofluoric acid, f, "gtceu:hydrofluoric_acid_bucket"]
    - [cr2, Chem Reactor, m, "gtceu:hv_chemical_reactor"]
    - [tfe, Tetrafluoroethylene, f, "gtceu:tetrafluoroethylene_bucket"]
    - [o, Oxygen, f, "gtceu:oxygen_bucket"]
    - [cr3, Chem Reactor, m, "gtceu:hv_chemical_reactor"]
    - [pt, PTFE, o, "gtceu:polytetrafluoroethylene_bucket"]
  e: [[me, cr1], [cl, cr1, "6 B"], [cr1, chf], [chf, cr2], [hf, cr2], [cr2, tfe], [tfe, cr3], [o, cr3], [cr3, pt]]
  tips:
    - |-
      Per 1 B of tetrafluoroethylene: 2 B chloroform (= 12 B chlorine + 2 B methane) + 4 B hydrofluoric acid, giving 12 B hydrochloric acid back. Chlorine is the bottleneck: one LV electrolyzer makes 1.7 B a minute, an HV one about 6.7.
    - |-
      Oxygen route: 1 B oxygen + 144 mB TFE → 216 mB PTFE (1.5 B PTFE per B of TFE = 10.4 ingots). Air route: 1 B air + 144 mB TFE → 144 mB PTFE (6.9 ingots per B of TFE). Air needs no centrifuge, oxygen needs 69 B of air per B of TFE.
    - |-
      Hydrochloric acid goes back to chlorine: electrolyse it in the same electrolyzer as your salt water (output of this step not checked, read it in EMI).
    - |-
      Fluorine: no recipe in the pack scripts. It has to come from decomposing a fluorine mineral (topaz, blue topaz, lepidolite, bastnasite); check the electrolyzer recipe in EMI before you plan the line.
    - |-
      The LCR shortcuts (circuit 24) are what PTFE buys: methane from 6 B hydrogen + 1 B carbon monoxide (8 s, 30 EU/t), ammonia, phenol and diesel in one step.
  b:
    - ["gtceu:hv_chemical_reactor", 3]
    - ["gtceu:hv_fluid_solidifier", 1]
    - ["gtceu:steel_drum", 5]
    - ["pipez:fluid_pipe", 24]
  how:
    - i: ["gtceu:chlorine_bucket", "gtceu:methane_bucket", "gtceu:steel_drum"]
      t: |-
        Buffer first: one steel drum each for chlorine, methane and hydrofluoric acid, one for hydrochloric acid (outputs). Pipez fluid pipes with a filter, or GT pump covers on each reactor face, so a reactor never pulls the wrong fluid.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:chloroform_bucket"]
      t: |-
        Reactor 1, ghost circuit 1: 6 B chlorine + 1 B methane → 3 B hydrochloric acid + 1 B chloroform in 4 s at 30 EU/t. An HV reactor overclocks it twice (1 s, 480 EU/t), far faster than your chlorine supply, so reactor 1 mostly waits.
    - i: ["gtceu:hydrofluoric_acid_bucket", "gtceu:hydrogen_bucket"]
      t: |-
        Hydrofluoric acid: 1 B hydrogen + 1 B fluorine → 1 B acid in 3 s at 7 EU/t (any chemical reactor). You need 4 B of acid per B of TFE, so 4 B of fluorine. The pack has no fluorine recipe in its scripts (see the watch line): confirm your source first.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:tetrafluoroethylene_bucket"]
      t: |-
        Reactor 2 (no circuit): 2 B chloroform + 4 B hydrofluoric acid → 6 B hydrochloric acid + 1 B tetrafluoroethylene in 24 s at 240 EU/t. This recipe is HV tier and cannot overclock on a 512 V hatch, so one reactor = 2.5 B of TFE a minute. It is the speed limit of the whole line.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:polytetrafluoroethylene_bucket", "gtceu:oxygen_bucket"]
      t: |-
        Reactor 3, ghost circuit 1: 1 B oxygen + 144 mB TFE → 216 mB PTFE in 8 s at 30 EU/t (2 s at 480 EU/t on HV). With air instead of oxygen the output is 144 mB. Pipe the PTFE straight into a Fluid Solidifier (ingot mold, 144 mB per ingot) and from there into a drawer.
    - i: ["gtceu:large_chemical_reactor", "gtceu:ptfe_pipe_casing", "gtceu:inert_machine_casing"]
      t: |-
        Pay-off: Large Chemical Reactor = controller (4 HV circuits, stainless rotor, 2 large PTFE fluid pipes, HV motor, HV hull) + 24 chemically inert PTFE casings (10 minimum) + 1 PTFE pipe casing in the middle + exactly 1 heating coil of any tier. PTFE pipe casing = 4 PTFE plates + 4 normal PTFE pipes + 1 PTFE frame (makes 2). The inert casing is a solid machine casing + PTFE fluid. Check the BOM below: it is a lot of PTFE.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:hydrochloric_acid_bucket"]
      t: |-
        Easy to miss: each B of TFE returns 12 B of hydrochloric acid (6 B from the two chloroform runs, 6 B from the TFE run). Do not let the acid drum fill, or reactors 1 and 2 stop. Send it back to the electrolyzer line or fit a Fluid Voiding Cover (soft mallet) while you build that loop.
---
# PTFE: three HV Chemical Reactors

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `ptfe` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Polyethylene and PTFE](../../plan/p8.md#plastics)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-cr1">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Methane (gtceu:methane_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__methane_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Methane</span></span><span class="gt-slot gt-fluid" title="Chlorine (gtceu:chlorine_bucket) - 6 B"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><b class="gt-q">6 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Chloroform (gtceu:chloroform_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__chloroform_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chloroform</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-cr2">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Chloroform (gtceu:chloroform_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__chloroform_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chloroform</span></span><span class="gt-slot gt-fluid" title="Hydrofluoric acid (gtceu:hydrofluoric_acid_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrofluoric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrofluoric Acid</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Tetrafluoroethylene (gtceu:tetrafluoroethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__tetrafluoroethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tetrafluoroethylene</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-cr3">
<div class="gt-head"><span class="gt-mname">Chem Reactor</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Tetrafluoroethylene (gtceu:tetrafluoroethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__tetrafluoroethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tetrafluoroethylene</span></span><span class="gt-slot gt-fluid" title="Oxygen (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="PTFE (gtceu:polytetrafluoroethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__polytetrafluoroethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polytetrafluoroethylene Bucket</span><span class="gt-note">PTFE</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Chem Reactor](#m-cr1) → [Chem Reactor](#m-cr2) → [Chem Reactor](#m-cr3)

## How to build

1. Buffer first: one steel drum each for chlorine, methane and hydrofluoric acid, one for hydrochloric acid (outputs). Pipez fluid pipes with a filter, or GT pump covers on each reactor face, so a reactor never pulls the wrong fluid. — `gtceu:chlorine_bucket`, `gtceu:methane_bucket`, `gtceu:steel_drum`
2. Reactor 1, ghost circuit 1: 6 B chlorine + 1 B methane → 3 B hydrochloric acid + 1 B chloroform in 4 s at 30 EU/t. An HV reactor overclocks it twice (1 s, 480 EU/t), far faster than your chlorine supply, so reactor 1 mostly waits. — `gtceu:hv_chemical_reactor`, `gtceu:chloroform_bucket`
3. Hydrofluoric acid: 1 B hydrogen + 1 B fluorine → 1 B acid in 3 s at 7 EU/t (any chemical reactor). You need 4 B of acid per B of TFE, so 4 B of fluorine. The pack has no fluorine recipe in its scripts (see the watch line): confirm your source first. — `gtceu:hydrofluoric_acid_bucket`, `gtceu:hydrogen_bucket`
4. Reactor 2 (no circuit): 2 B chloroform + 4 B hydrofluoric acid → 6 B hydrochloric acid + 1 B tetrafluoroethylene in 24 s at 240 EU/t. This recipe is HV tier and cannot overclock on a 512 V hatch, so one reactor = 2.5 B of TFE a minute. It is the speed limit of the whole line. — `gtceu:hv_chemical_reactor`, `gtceu:tetrafluoroethylene_bucket`
5. Reactor 3, ghost circuit 1: 1 B oxygen + 144 mB TFE → 216 mB PTFE in 8 s at 30 EU/t (2 s at 480 EU/t on HV). With air instead of oxygen the output is 144 mB. Pipe the PTFE straight into a Fluid Solidifier (ingot mold, 144 mB per ingot) and from there into a drawer. — `gtceu:hv_chemical_reactor`, `gtceu:polytetrafluoroethylene_bucket`, `gtceu:oxygen_bucket`
6. Pay-off: Large Chemical Reactor = controller (4 HV circuits, stainless rotor, 2 large PTFE fluid pipes, HV motor, HV hull) + 24 chemically inert PTFE casings (10 minimum) + 1 PTFE pipe casing in the middle + exactly 1 heating coil of any tier. PTFE pipe casing = 4 PTFE plates + 4 normal PTFE pipes + 1 PTFE frame (makes 2). The inert casing is a solid machine casing + PTFE fluid. Check the BOM below: it is a lot of PTFE. — `gtceu:large_chemical_reactor`, `gtceu:ptfe_pipe_casing`, `gtceu:inert_machine_casing`
7. Easy to miss: each B of TFE returns 12 B of hydrochloric acid (6 B from the two chloroform runs, 6 B from the TFE run). Do not let the acid drum fill, or reactors 1 and 2 stop. Send it back to the electrolyzer line or fit a Fluid Voiding Cover (soft mallet) while you build that loop. — `gtceu:hv_chemical_reactor`, `gtceu:hydrochloric_acid_bucket`

## Tips

- Per 1 B of tetrafluoroethylene: 2 B chloroform (= 12 B chlorine + 2 B methane) + 4 B hydrofluoric acid, giving 12 B hydrochloric acid back. Chlorine is the bottleneck: one LV electrolyzer makes 1.7 B a minute, an HV one about 6.7.
- Oxygen route: 1 B oxygen + 144 mB TFE → 216 mB PTFE (1.5 B PTFE per B of TFE = 10.4 ingots). Air route: 1 B air + 144 mB TFE → 144 mB PTFE (6.9 ingots per B of TFE). Air needs no centrifuge, oxygen needs 69 B of air per B of TFE.
- Hydrochloric acid goes back to chlorine: electrolyse it in the same electrolyzer as your salt water (output of this step not checked, read it in EMI).
- Fluorine: no recipe in the pack scripts. It has to come from decomposing a fluorine mineral (topaz, blue topaz, lepidolite, bastnasite); check the electrolyzer recipe in EMI before you plan the line.
- The LCR shortcuts (circuit 24) are what PTFE buys: methane from 6 B hydrogen + 1 B carbon monoxide (8 s, 30 EU/t), ammonia, phenol and diesel in one step.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_chemical_reactor` | 3 |
| `gtceu:hv_fluid_solidifier` | 1 |
| `gtceu:steel_drum` | 5 |
| `pipez:fluid_pipe` | 24 |
