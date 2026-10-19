---
kind: chain
id: zpm_argon
order: 2300
data:
  t: |-
    ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines
  inf: true
  power: true
  "n":
    - [dd, Diamond dust, i, "gtceu:diamond_dust"]
    - [el, "LV Electrolyzer · 768 ticks", m, "gtceu:lv_electrolyzer"]
    - [cd, "64 carbon dust", x, "gtceu:carbon_dust"]
    - [mg, Magnesium, i, "gtceu:magnesium_dust"]
    - [rf, "Tier 2 reflectors (all the same tier)", i, "kubejs:advanced_reflector_casing"]
    - [bf, "Buffer · 180 MEU start", x, "gtceu:power_substation"]
    - [fu, "Fusion MK II · 24 576 EU/t · 7.2 s", m, "start_core:zpm_fusion_reactor"]
    - [ap, "Argon plasma · 1000 mB", x, "gtceu:argon_plasma_bucket"]
    - [rh, "ZPM rotor holder (x4)", i, "gtceu:zpm_rotor_holder"]
    - [ro, "Prismalium rotor (power 1600)", i, "gtceu:prismalium_ingot"]
    - [pt, "Large Plasma Turbine (IV controller)", p, "gtceu:plasma_large_turbine"]
    - [dy, "ZPM dynamo hatch (16 A accepted)", x, "gtceu:zpm_energy_output_hatch"]
    - [out, ZPM grid, o, "gtceu:zpm_machine_hull"]
  e:
    - [dd, el, "1"]
    - [el, cd, "64"]
    - [cd, fu, "144 mB"]
    - [mg, fu, "144 mB"]
    - [rf, fu]
    - [bf, fu, once]
    - [fu, ap, "1000 mB / 7.2 s"]
    - [ap, pt, "5 mB per 116 ticks"]
    - [rh, pt]
    - [ro, pt]
    - [pt, dy, "up to 1 048 576 EU/t"]
    - [dy, out]
  tips:
    - |-
      Pack recipe (systems/fusion/fusion_scaling.js): reflector tier 2, 144 mB carbon + 144 mB magnesium → 1000 mB argon plasma, 144 ticks (7.2 s) at 24 576 EU/t, start energy 180 MEU. Fusion MK I holds at most 160 MEU, so argon needs Fusion MK II (320 MEU). All reflectors of one reactor must be the same tier.
    - |-
      Why argon (plasma_turbines.js: 5 mB per cycle at 2 048 EU/t): argon 116 ticks per 5 mB = 47 514 EU/mB, helium 27 ticks = 11 059 EU/mB. Net per 1000 mB after the reactor cost: argon about 44 MEU, helium about 10.5 MEU, about 4.2x more per mB and per reactor-second (both make 6.94 mB a tick).
    - |-
      Turbine (gtceu jar formula): the Large Plasma Turbine is an IV controller, base 2 x 8 192 = 16 384 EU/t, times 2^(holder tier - IV) times rotor power / 100. ZPM holder (x4) + prismalium rotor (1600) = 1 048 576 EU/t per turbine at full speed. A 16 A dynamo hatch is accepted (OUTPUT_ENERGY ability).
    - |-
      Fuel is the real limit: one MK II makes 6.94 mB/t of argon plasma, about 330 000 EU/t of turbine power (derived: 6.94 x 47 514); 50 reactors are about 16.5 M EU/t raw. A reflector above the recipe tier raises the overclock cap by the tier difference and each overclock doubles the flow. The community figure "400 MFE/t" does not match the formula: do not plan on it.
    - |-
      Carbon: 1 diamond dust → 64 carbon dust in an LV electrolyzer, 768 ticks (gtsrc SeparationRecipes, not removed by the pack). Diamonds: sand sieve 7.5 % or the Rock Filtrator diamond geode (35 %, lv_geodes).
    - |-
      Unverified: the recipe that turns carbon dust into the 144 mB fluid the reactor takes, and a magnesium source beyond the titanium line MgCl2 loop.
    - |-
      Later and bigger: the Supreme Plasma Turbine (UHV): 16 384 EU/t base, up to 6 parallels, x2 EU/t per rotor holder tier over IV, laser output (see uhv_power / uev_power).
  b:
    - ["start_core:zpm_fusion_reactor", 1]
    - ["gtceu:plasma_large_turbine", 1]
    - ["gtceu:zpm_rotor_holder", 1]
    - ["gtceu:zpm_energy_output_hatch", 1]
    - ["gtceu:lv_electrolyzer", 1]
    - ["gtceu:steel_drum", 4]
    - ["pipez:fluid_pipe", 16]
  how:
    - i: ["gtceu:diamond_dust", "gtceu:lv_electrolyzer", "gtceu:carbon_dust"]
      t: |-
        Carbon: a diamond dust drawer into one LV electrolyzer (64 carbon dust per diamond, 38 s). One electrolyzer gives about 100 carbon dust a minute, far more than one reactor needs.
    - i: ["start_core:zpm_fusion_reactor", "kubejs:advanced_reflector_casing", "gtceu:power_substation"]
      t: Fusion MK II with tier 2 reflectors everywhere (mixed tiers fail the structure). Charge 180 MEU from a Power Substation before the first run; carbon and magnesium in through fluid hatches (144 mB each), argon plasma out to a drum.
    - i: ["gtceu:plasma_large_turbine", "gtceu:zpm_rotor_holder", "gtceu:zpm_energy_output_hatch"]
      t: |-
        Large Plasma Turbine with a ZPM rotor holder and a prismalium rotor; plasma in from the drum, ZPM dynamo hatch (a 16 A one is allowed) out. One turbine can take far more than one reactor makes: match reactors to turbines by plasma flow, not by turbine count.
    - i: ["gtceu:argon_plasma_bucket"]
      t: |-
        Keep the helium line (zpm_power) only as a backup: per reactor the argon plasma gives about 4x the power. Add reactors, not turbines, when you need more.
---
# ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_argon` · **Tags:** Infinite source, Power, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Fusion MK II (darmstadtium)](../../plan/p13.md#fusion2)

**Tips:** 7, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-el">
<div class="gt-head"><span class="gt-mname">LV Electrolyzer · 768 ticks</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Diamond dust (gtceu:diamond_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__diamond_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="64 carbon dust (gtceu:carbon_dust) - 64"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dust</span><span class="gt-note">64 carbon dust</span><b class="gt-q">64</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electrolyzer</code></div>
</div>
<div class="gt-panel t-zpm" id="m-fu">
<div class="gt-head"><span class="gt-mname">Fusion MK II · 24 576 EU/t · 7.2 s</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="64 carbon dust (gtceu:carbon_dust) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dust</span><span class="gt-note">64 carbon dust</span><b class="gt-q">144 mB</b></span><span class="gt-slot" title="Magnesium (gtceu:magnesium_dust) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__magnesium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnesium Dust</span><b class="gt-q">144 mB</b></span><span class="gt-slot" title="Tier 2 reflectors (all the same tier) (kubejs:advanced_reflector_casing)"><img class="gt-ico" src="../../assets/icons/kubejs__advanced_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Reflector Casing</span><span class="gt-note">Tier 2 reflectors (all the same tier)</span></span><span class="gt-slot" title="Buffer · 180 MEU start (gtceu:power_substation) - once"><img class="gt-ico" src="../../assets/icons/gtceu__power_substation.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Power Substation</span><span class="gt-note">Buffer · 180 MEU start</span><b class="gt-q">once</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">7.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Argon plasma · 1000 mB (gtceu:argon_plasma_bucket) - 1000 mB / 7.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__argon_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Argon Plasma Bucket</span><span class="gt-note">Argon plasma · 1000 mB</span><b class="gt-q">1000 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-pt">
<div class="gt-head"><span class="gt-mname">Large Plasma Turbine (IV controller)</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Argon plasma · 1000 mB (gtceu:argon_plasma_bucket) - 5 mB per 116 ticks"><img class="gt-ico" src="../../assets/icons/gtceu__argon_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Argon Plasma Bucket</span><span class="gt-note">Argon plasma · 1000 mB</span><b class="gt-q">5 mB per 116 ticks</b></span><span class="gt-slot" title="ZPM rotor holder (x4) (gtceu:zpm_rotor_holder)"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Rotor Holder</span><span class="gt-note">ZPM rotor holder (x4)</span></span><span class="gt-slot" title="Prismalium rotor (power 1600) (gtceu:prismalium_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__prismalium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Prismalium Ingot</span><span class="gt-note">Prismalium rotor (power 1600)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__plasma_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM dynamo hatch (16 A accepted) (gtceu:zpm_energy_output_hatch) - up to 1 048 576 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Energy Output Hatch</span><span class="gt-note">ZPM dynamo hatch (16 A accepted)</span><b class="gt-q">up to 1 048 576 EU/t</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:plasma_large_turbine</code></div>
</div>
</div>

## Flow

- [LV Electrolyzer · 768 ticks](#m-el) → [Fusion MK II · 24 576 EU/t · 7.2 s](#m-fu) → [Large Plasma Turbine (IV controller)](#m-pt)

### Direct steps

- ZPM dynamo hatch (16 A accepted) → ZPM grid

## How to build

1. Carbon: a diamond dust drawer into one LV electrolyzer (64 carbon dust per diamond, 38 s). One electrolyzer gives about 100 carbon dust a minute, far more than one reactor needs. — `gtceu:diamond_dust`, `gtceu:lv_electrolyzer`, `gtceu:carbon_dust`
2. Fusion MK II with tier 2 reflectors everywhere (mixed tiers fail the structure). Charge 180 MEU from a Power Substation before the first run; carbon and magnesium in through fluid hatches (144 mB each), argon plasma out to a drum. — `start_core:zpm_fusion_reactor`, `kubejs:advanced_reflector_casing`, `gtceu:power_substation`
3. Large Plasma Turbine with a ZPM rotor holder and a prismalium rotor; plasma in from the drum, ZPM dynamo hatch (a 16 A one is allowed) out. One turbine can take far more than one reactor makes: match reactors to turbines by plasma flow, not by turbine count. — `gtceu:plasma_large_turbine`, `gtceu:zpm_rotor_holder`, `gtceu:zpm_energy_output_hatch`
4. Keep the helium line (zpm\_power) only as a backup: per reactor the argon plasma gives about 4x the power. Add reactors, not turbines, when you need more. — `gtceu:argon_plasma_bucket`

## Tips

- Pack recipe (systems/fusion/fusion\_scaling.js): reflector tier 2, 144 mB carbon + 144 mB magnesium → 1000 mB argon plasma, 144 ticks (7.2 s) at 24 576 EU/t, start energy 180 MEU. Fusion MK I holds at most 160 MEU, so argon needs Fusion MK II (320 MEU). All reflectors of one reactor must be the same tier.
- Why argon (plasma\_turbines.js: 5 mB per cycle at 2 048 EU/t): argon 116 ticks per 5 mB = 47 514 EU/mB, helium 27 ticks = 11 059 EU/mB. Net per 1000 mB after the reactor cost: argon about 44 MEU, helium about 10.5 MEU, about 4.2x more per mB and per reactor-second (both make 6.94 mB a tick).
- Turbine (gtceu jar formula): the Large Plasma Turbine is an IV controller, base 2 x 8 192 = 16 384 EU/t, times 2^(holder tier - IV) times rotor power / 100. ZPM holder (x4) + prismalium rotor (1600) = 1 048 576 EU/t per turbine at full speed. A 16 A dynamo hatch is accepted (OUTPUT\_ENERGY ability).
- Fuel is the real limit: one MK II makes 6.94 mB/t of argon plasma, about 330 000 EU/t of turbine power (derived: 6.94 x 47 514); 50 reactors are about 16.5 M EU/t raw. A reflector above the recipe tier raises the overclock cap by the tier difference and each overclock doubles the flow. The community figure "400 MFE/t" does not match the formula: do not plan on it.
- Carbon: 1 diamond dust → 64 carbon dust in an LV electrolyzer, 768 ticks (gtsrc SeparationRecipes, not removed by the pack). Diamonds: sand sieve 7.5 % or the Rock Filtrator diamond geode (35 %, lv\_geodes).
- **Unverified** the recipe that turns carbon dust into the 144 mB fluid the reactor takes, and a magnesium source beyond the titanium line MgCl2 loop.
- Later and bigger: the Supreme Plasma Turbine (UHV): 16 384 EU/t base, up to 6 parallels, x2 EU/t per rotor holder tier over IV, laser output (see uhv\_power / uev\_power).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:zpm_fusion_reactor` | 1 |
| `gtceu:plasma_large_turbine` | 1 |
| `gtceu:zpm_rotor_holder` | 1 |
| `gtceu:zpm_energy_output_hatch` | 1 |
| `gtceu:lv_electrolyzer` | 1 |
| `gtceu:steel_drum` | 4 |
| `pipez:fluid_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Raw Ore Slurry &amp; mineral mixtures](../mv/slurry.md), [Fusion MK II (ZPM): URD superconducting coil → fusion coil, advanced reflector casing, then the reactor (needs 4 UV circuits) and darmstadtium](zpm_fusion.md), [ZPM power: deuterium + tritium → helium plasma (MK I fusion) → Large Plasma Turbine with a ZPM rotor holder → ZPM dynamo hatch](../power/zpm_power.md)
- **Main source for:** `gtceu:argon_plasma_bucket`
