---
kind: chain
id: ev_nitrobenzene
order: 2280
data:
  t: |-
    EV power: nitrobenzene in Large Gas Turbines (1 280 EU per mB)
  inf: true
  power: true
  "n":
    - [na, "Nitric acid · 1 B", f, "gtceu:nitric_acid_bucket"]
    - [sa, "Sulfuric acid · 1 B", f, "gtceu:sulfuric_acid_bucket"]
    - [mx, "Mixer · 2 EU/t · 25 s", m, "gtceu:mv_mixer"]
    - [nm, "Nitration mixture · 2 B", x, "gtceu:nitration_mixture_bucket"]
    - [bz, "Benzene · 5 B", f, "gtceu:benzene_bucket"]
    - [dw, "Distilled water · 2 B", f, "gtceu:distilled_water_bucket"]
    - [cr, "HV Chemical Reactor · 480 EU/t · 8 s", m, "gtceu:hv_chemical_reactor"]
    - [nb, "Nitrobenzene · 8 B (+1 B diluted sulfuric acid)", x, "gtceu:nitrobenzene_bucket"]
    - [dm, Fuel drums, x, "gtceu:steel_drum"]
    - [lgt, "Large Gas Turbine (EV controller)", p, "gtceu:gas_large_turbine"]
    - [dy, EV Dynamo Hatch, x, "gtceu:ev_energy_output_hatch"]
    - [out, EV machines and multiblocks, o, "gtceu:ev_assembler"]
  e:
    - [na, mx, "1 B"]
    - [sa, mx, "1 B"]
    - [mx, nm, "2 B"]
    - [nm, cr, "2 B"]
    - [bz, cr, "5 B"]
    - [dw, cr, "2 B"]
    - [cr, nb, "8 B / 8 s"]
    - [nb, dm]
    - [dm, lgt, "1 mB = 1 280 EU"]
    - [lgt, dy]
    - [dy, out, "2 048 V"]
  tips:
    - |-
      "NBZ" is the community shorthand for nitrobenzene (the gas turbine quest itself calls it the most popular choice). Fuel value (gtsrc FuelRecipes, no pack override): gas turbine fuel, 1 mB per 40 ticks at 32 EU/t = 1 280 EU per mB, 3.6x benzene (352 EU/mB). It is NOT a combustion fuel: the Large Combustion Engine does not burn it.
    - |-
      Recipes (gtsrc FuelRecipeChains, MixerRecipes): mixer, 1 B nitric acid + 1 B sulfuric acid → 2 B nitration mixture, 500 ticks at 2 EU/t; chemical reactor, 5 B benzene + 2 B nitration mixture + 2 B distilled water → 8 B nitrobenzene + 1 B diluted sulfuric acid, 160 ticks at 480 EU/t (HV). 5 B benzene (1.76 MEU burnt as gas) becomes 8 B nitrobenzene (10.24 MEU): 5.8x the energy.
    - |-
      Sizing: one HV chemical reactor makes 1 B a second = 20 mB/t = 25 600 EU/t of fuel at 100 % efficiency. Example: 240 A of EV (491 520 EU/t) burns 384 mB/t = 7.7 B/s, about 8 reactors.
    - |-
      Controllers (gtsrc MetaTileEntityLoader): Large Gas Turbine = EV hull + 2 EV circuits + 4 stainless steel gears + 2 stainless steel large fluid pipes (stainless turbine casings, stainless gearbox). The Large Combustion Engine needs 1 IV circuit and the Extreme Combustion Engine a LuV circuit, so the gas turbine is the EV option. A turbine rotor holder can never be shared between two turbines.
    - |-
      Alternative for combustion engines: high octane gasoline 3 200 EU/mB (gasoline 1 600): Large Chemical Reactor, 1 920 EU/t, 50 ticks, circuit 24: 20 B gasoline + 2 B octane + 2 B nitrous oxide + 1 B toluene + 1 B ETBE → 32 B. It burns in combustion generators and engines, not in gas turbines.
    - |-
      More EV amps (pack large_energy_hatches.js): EV 4A hatch = EV 1A transformer + EV energy hatch + 2 aluminium quadruple wire + 1 EV voltage coil + 2 titanium plates + 144 mB soldering alloy, 960 EU/t; EV 16A hatch = EV 4A transformer + EV 4A hatch + 2 aluminium quadruple wire + 2 EV voltage coils + 4 titanium plates + 288 mB soldering alloy, 1 440 EU/t, 200 ticks. Both need platinum (transformer cable) and MPIC chips.
    - |-
      Unverified: the nitric acid route in this pack (not traced; the platinum line uses it too), the Large Gas Turbine base output and the rotor to use: read the turbine tooltip. Community reports: 7 of 12 reported setups power EV-IV this way.
  b:
    - ["gtceu:gas_large_turbine", 1]
    - ["gtceu:hv_chemical_reactor", 2]
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:ev_energy_output_hatch", 1]
    - ["gtceu:steel_drum", 4]
    - ["pipez:fluid_pipe", 16]
  how:
    - i: ["gtceu:nitric_acid_bucket", "gtceu:sulfuric_acid_bucket", "gtceu:mv_mixer"]
      t: |-
        Acid mixer: one Mixer with two fluid inputs (nitric acid drum, sulfuric acid drum from the oil/sulfuric line) and a pump cover into a nitration mixture drum. 1 B + 1 B → 2 B in 25 s at 2 EU/t, so one mixer feeds one reactor with room to spare.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:benzene_bucket", "gtceu:distilled_water_bucket"]
      t: |-
        HV Chemical Reactor: benzene (oil_distill / refinery), nitration mixture and distilled water (drilling line) piped in; 8 B nitrobenzene + 1 B diluted sulfuric acid every 8 s. Lock each output to its fluid: nitrobenzene to the fuel drums, diluted sulfuric acid to its own drum.
    - i: ["gtceu:steel_drum", "gtceu:nitrobenzene_bucket"]
      t: |-
        Buffer: two or more fuel drums between the reactors and the turbine. A Robot Arm/pump cover with a fluid filter keeps the reactor off when the drums are full.
    - i: ["gtceu:gas_large_turbine", "gtceu:ev_energy_output_hatch"]
      t: |-
        Large Gas Turbine: stainless turbine casings, stainless gearbox, one rotor holder with a rotor, a fluid input hatch for nitrobenzene and an EV dynamo hatch. Feed it from the drums; the dynamo goes to an EV cable or to the 4A/16A EV hatches of your multis.
    - i: ["gtceu:ev_energy_input_hatch_16a"]
      t: |-
        Scale: add one reactor per 25 600 EU/t of target output and turbines to match; a 16A EV hatch per big consumer. Keep the acid and benzene lines running before adding turbines.
---
# EV power: nitrobenzene in Large Gas Turbines (1 280 EU per mB)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `ev_nitrobenzene` · **Tags:** Infinite source, Power, Unverified

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [EV power: nitrobenzene gas turbines](../../plan/p9.md#evpower)

**Tips:** 7, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer · 2 EU/t · 25 s</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Nitric acid · 1 B (gtceu:nitric_acid_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__nitric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitric Acid</span><span class="gt-note">Nitric acid · 1 B</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-fluid" title="Sulfuric acid · 1 B (gtceu:sulfuric_acid_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Acid</span><span class="gt-note">Sulfuric acid · 1 B</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nitration mixture · 2 B (gtceu:nitration_mixture_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__nitration_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitration Mixture Bucket</span><span class="gt-note">Nitration mixture · 2 B</span><b class="gt-q">2 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_mixer</code></div>
</div>
<div class="gt-panel t-hv" id="m-cr">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 480 EU/t · 8 s</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nitration mixture · 2 B (gtceu:nitration_mixture_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__nitration_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitration Mixture Bucket</span><span class="gt-note">Nitration mixture · 2 B</span><b class="gt-q">2 B</b></span><span class="gt-slot gt-fluid" title="Benzene · 5 B (gtceu:benzene_bucket) - 5 B"><img class="gt-ico" src="../../assets/icons/gtceu__benzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Benzene</span><span class="gt-note">Benzene · 5 B</span><b class="gt-q">5 B</b></span><span class="gt-slot gt-fluid" title="Distilled water · 2 B (gtceu:distilled_water_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water</span><span class="gt-note">Distilled water · 2 B</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nitrobenzene · 8 B (+1 B diluted sulfuric acid) (gtceu:nitrobenzene_bucket) - 8 B / 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__nitrobenzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrobenzene Bucket</span><span class="gt-note">Nitrobenzene · 8 B (+1 B diluted sulfuric acid)</span><b class="gt-q">8 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-lgt">
<div class="gt-head"><span class="gt-mname">Large Gas Turbine (EV controller)</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Fuel drums (gtceu:steel_drum) - 1 mB = 1 280 EU"><img class="gt-ico" src="../../assets/icons/gtceu__steel_drum.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Drum</span><span class="gt-note">Fuel drums</span><b class="gt-q">1 mB = 1 280 EU</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__gas_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="EV Dynamo Hatch (gtceu:ev_energy_output_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__ev_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Energy Output Hatch</span><span class="gt-note">EV Dynamo Hatch</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:gas_large_turbine</code></div>
</div>
</div>

## Flow

- [Mixer · 2 EU/t · 25 s](#m-mx) → [HV Chemical Reactor · 480 EU/t · 8 s](#m-cr) → [Large Gas Turbine (EV controller)](#m-lgt)

### Direct steps

- Nitrobenzene · 8 B (+1 B diluted sulfuric acid) → Fuel drums
- EV Dynamo Hatch → EV machines and multiblocks (2 048 V)

## How to build

1. Acid mixer: one Mixer with two fluid inputs (nitric acid drum, sulfuric acid drum from the oil/sulfuric line) and a pump cover into a nitration mixture drum. 1 B + 1 B → 2 B in 25 s at 2 EU/t, so one mixer feeds one reactor with room to spare. — `gtceu:nitric_acid_bucket`, `gtceu:sulfuric_acid_bucket`, `gtceu:mv_mixer`
2. HV Chemical Reactor: benzene (oil\_distill / refinery), nitration mixture and distilled water (drilling line) piped in; 8 B nitrobenzene + 1 B diluted sulfuric acid every 8 s. Lock each output to its fluid: nitrobenzene to the fuel drums, diluted sulfuric acid to its own drum. — `gtceu:hv_chemical_reactor`, `gtceu:benzene_bucket`, `gtceu:distilled_water_bucket`
3. Buffer: two or more fuel drums between the reactors and the turbine. A Robot Arm/pump cover with a fluid filter keeps the reactor off when the drums are full. — `gtceu:steel_drum`, `gtceu:nitrobenzene_bucket`
4. Large Gas Turbine: stainless turbine casings, stainless gearbox, one rotor holder with a rotor, a fluid input hatch for nitrobenzene and an EV dynamo hatch. Feed it from the drums; the dynamo goes to an EV cable or to the 4A/16A EV hatches of your multis. — `gtceu:gas_large_turbine`, `gtceu:ev_energy_output_hatch`
5. Scale: add one reactor per 25 600 EU/t of target output and turbines to match; a 16A EV hatch per big consumer. Keep the acid and benzene lines running before adding turbines. — `gtceu:ev_energy_input_hatch_16a`

## Tips

- "NBZ" is the community shorthand for nitrobenzene (the gas turbine quest itself calls it the most popular choice). Fuel value (gtsrc FuelRecipes, no pack override): gas turbine fuel, 1 mB per 40 ticks at 32 EU/t = 1 280 EU per mB, 3.6x benzene (352 EU/mB). It is NOT a combustion fuel: the Large Combustion Engine does not burn it.
- Recipes (gtsrc FuelRecipeChains, MixerRecipes): mixer, 1 B nitric acid + 1 B sulfuric acid → 2 B nitration mixture, 500 ticks at 2 EU/t; chemical reactor, 5 B benzene + 2 B nitration mixture + 2 B distilled water → 8 B nitrobenzene + 1 B diluted sulfuric acid, 160 ticks at 480 EU/t (HV). 5 B benzene (1.76 MEU burnt as gas) becomes 8 B nitrobenzene (10.24 MEU): 5.8x the energy.
- Sizing: one HV chemical reactor makes 1 B a second = 20 mB/t = 25 600 EU/t of fuel at 100 % efficiency. Example: 240 A of EV (491 520 EU/t) burns 384 mB/t = 7.7 B/s, about 8 reactors.
- Controllers (gtsrc MetaTileEntityLoader): Large Gas Turbine = EV hull + 2 EV circuits + 4 stainless steel gears + 2 stainless steel large fluid pipes (stainless turbine casings, stainless gearbox). The Large Combustion Engine needs 1 IV circuit and the Extreme Combustion Engine a LuV circuit, so the gas turbine is the EV option. A turbine rotor holder can never be shared between two turbines.
- Alternative for combustion engines: high octane gasoline 3 200 EU/mB (gasoline 1 600): Large Chemical Reactor, 1 920 EU/t, 50 ticks, circuit 24: 20 B gasoline + 2 B octane + 2 B nitrous oxide + 1 B toluene + 1 B ETBE → 32 B. It burns in combustion generators and engines, not in gas turbines.
- More EV amps (pack large\_energy\_hatches.js): EV 4A hatch = EV 1A transformer + EV energy hatch + 2 aluminium quadruple wire + 1 EV voltage coil + 2 titanium plates + 144 mB soldering alloy, 960 EU/t; EV 16A hatch = EV 4A transformer + EV 4A hatch + 2 aluminium quadruple wire + 2 EV voltage coils + 4 titanium plates + 288 mB soldering alloy, 1 440 EU/t, 200 ticks. Both need platinum (transformer cable) and MPIC chips.
- **Unverified** the nitric acid route in this pack (not traced; the platinum line uses it too), the Large Gas Turbine base output and the rotor to use: read the turbine tooltip. Community reports: 7 of 12 reported setups power EV-IV this way.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:gas_large_turbine` | 1 |
| `gtceu:hv_chemical_reactor` | 2 |
| `gtceu:mv_mixer` | 1 |
| `gtceu:ev_energy_output_hatch` | 1 |
| `gtceu:steel_drum` | 4 |
| `pipez:fluid_pipe` | 16 |

## Needs / Feeds

- **Main source for:** `gtceu:nitrobenzene_bucket`, `gtceu:nitration_mixture_bucket`, `gtceu:gas_large_turbine`
