---
kind: chain
id: luv_turbines
order: 2290
data:
  t: "LuV power: Large Gas Turbine with a LuV rotor holder"
  inf: true
  power: true
  "n":
    - [hu, LuV hull, i, "gtceu:luv_machine_hull"]
    - [gr, "4 HSS-S gears + 6 HSS-S rounds", i, "gtceu:hsss_gear"]
    - [mo, LuV electric motor, i, "gtceu:luv_electric_motor"]
    - [rp, "4 small RPP gears + 1 RPP ring", i, "gtceu:rhodium_plated_palladium_ingot"]
    - [pt, "PTFE · 288 mB", f, "gtceu:polytetrafluoroethylene_bucket"]
    - [as, "LuV-tier Assembler · circuit 3", m, "gtceu:luv_assembler"]
    - [rh, LuV rotor holder, x, "gtceu:luv_rotor_holder"]
    - [nb, "Nitrobenzene (EV line)", f, "gtceu:nitrobenzene_bucket"]
    - [lgt, Large Gas Turbine, p, "gtceu:gas_large_turbine"]
    - [out, LuV grid and Power Substation, o, "gtceu:power_substation"]
  e:
    - [hu, as]
    - [gr, as]
    - [mo, as]
    - [rp, as]
    - [pt, as]
    - [as, rh]
    - [rh, lgt, replaces the EV holder]
    - [nb, lgt, about 3.2x the fuel]
    - [lgt, out, about 4x the power]
  tips:
    - |-
      Rotor holder rule (pack quest + gtceu jar): each rotor holder tier above the turbine controller doubles the power (multiplier 2^(holder tier - controller tier)) and burns 1.8x the fuel, about 10 % better efficiency per tier. A LuV holder on the EV Large Gas Turbine is 2 tiers up: 4x power for about 3.2x fuel (derived).
    - |-
      LuV rotor holder (pack recipe): LuV hull + 4 HSS-S gears + 1 LuV electric motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 RPP ring + 288 mB PTFE, circuit 3, a LuV-tier assembler recipe.
    - |-
      Rotors: dragonsteel is a ZPM material (EBF 7 100 K, ZPM hatch, naquadah coils), so do not plan dragonsteel rotors in LuV; prismalium (rotor power 1600) is later still.
    - |-
      Rotor holders cannot be shared between turbines (gtceu jar: canShared = false): one holder per turbine. Walls, fluid hatches and dynamo hatches can be shared (see the Combos phase).
    - |-
      This is generation; the Power Substation (luv_power) only stores it. Community reports: LuV turbines on LuV rotor holders in 3 reported setups.
    - |-
      Unverified: the Large Gas Turbine base output and rotor stats, so the dynamo tier: read the turbine tooltip after fitting the LuV holder and use a dynamo hatch of that voltage.
  b:
    - ["gtceu:gas_large_turbine", 1]
    - ["gtceu:luv_rotor_holder", 1]
    - ["gtceu:steel_drum", 2]
    - ["pipez:fluid_pipe", 8]
  how:
    - i: ["gtceu:luv_assembler", "gtceu:luv_rotor_holder"]
      t: |-
        One holder per turbine: LuV hull, 4 HSS-S gears, 6 HSS-S rounds, 1 LuV motor, 4 small RPP gears, 1 RPP ring and 288 mB PTFE in a LuV-tier assembler (circuit 3). Make one, test it, then one per turbine.
    - i: ["gtceu:gas_large_turbine", "gtceu:luv_rotor_holder"]
      t: Swap the EV rotor holder of each Large Gas Turbine for the LuV one (the rotor moves over). Read the new output on the turbine and change the dynamo hatch to match.
    - i: ["gtceu:nitrobenzene_bucket", "gtceu:hv_chemical_reactor"]
      t: |-
        Fuel: each upgraded turbine eats about 3.2x as much nitrobenzene, so add chemical reactors to the EV nitrobenzene line before the swap, not after.
---
# LuV power: Large Gas Turbine with a LuV rotor holder

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_turbines` · **Tags:** Infinite source, Power, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [LuV power: turbines on LuV rotor holders](../../plan/p11.md#luvgen)

**Tips:** 6, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-luv" id="m-as">
<div class="gt-head"><span class="gt-mname">LuV-tier Assembler · circuit 3</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV hull (gtceu:luv_machine_hull)"><img class="gt-ico" src="../../assets/icons/gtceu__luv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Machine Hull</span><span class="gt-note">LuV hull</span></span><span class="gt-slot" title="4 HSS-S gears + 6 HSS-S rounds (gtceu:hsss_gear)"><img class="gt-ico" src="../../assets/icons/gtceu__hsss_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hsss Gear</span><span class="gt-note">4 HSS-S gears + 6 HSS-S rounds</span></span><span class="gt-slot" title="LuV electric motor (gtceu:luv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electric Motor</span></span><span class="gt-slot" title="4 small RPP gears + 1 RPP ring (gtceu:rhodium_plated_palladium_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Ingot</span><span class="gt-note">4 small RPP gears + 1 RPP ring</span></span><span class="gt-slot gt-fluid" title="PTFE · 288 mB (gtceu:polytetrafluoroethylene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__polytetrafluoroethylene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polytetrafluoroethylene</span><span class="gt-note">PTFE · 288 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LuV rotor holder (gtceu:luv_rotor_holder)"><img class="gt-ico" src="../../assets/icons/gtceu__luv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Rotor Holder</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_assembler</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-lgt">
<div class="gt-head"><span class="gt-mname">Large Gas Turbine</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV rotor holder (gtceu:luv_rotor_holder) - replaces the EV holder"><img class="gt-ico" src="../../assets/icons/gtceu__luv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Rotor Holder</span><b class="gt-q">replaces the EV holder</b></span><span class="gt-slot gt-fluid" title="Nitrobenzene (EV line) (gtceu:nitrobenzene_bucket) - about 3.2x the fuel"><img class="gt-ico" src="../../assets/icons/gtceu__nitrobenzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrobenzene</span><span class="gt-note">Nitrobenzene (EV line)</span><b class="gt-q">about 3.2x the fuel</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__gas_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV grid and Power Substation (gtceu:power_substation) - about 4x the power"><img class="gt-ico" src="../../assets/icons/gtceu__power_substation.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Power Substation</span><span class="gt-note">LuV grid and Power Substation</span><b class="gt-q">about 4x the power</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:gas_large_turbine</code></div>
</div>
</div>

## Flow

- [LuV-tier Assembler · circuit 3](#m-as) → [Large Gas Turbine](#m-lgt)

## How to build

1. One holder per turbine: LuV hull, 4 HSS-S gears, 6 HSS-S rounds, 1 LuV motor, 4 small RPP gears, 1 RPP ring and 288 mB PTFE in a LuV-tier assembler (circuit 3). Make one, test it, then one per turbine. — `gtceu:luv_assembler`, `gtceu:luv_rotor_holder`
2. Swap the EV rotor holder of each Large Gas Turbine for the LuV one (the rotor moves over). Read the new output on the turbine and change the dynamo hatch to match. — `gtceu:gas_large_turbine`, `gtceu:luv_rotor_holder`
3. Fuel: each upgraded turbine eats about 3.2x as much nitrobenzene, so add chemical reactors to the EV nitrobenzene line before the swap, not after. — `gtceu:nitrobenzene_bucket`, `gtceu:hv_chemical_reactor`

## Tips

- Rotor holder rule (pack quest + gtceu jar): each rotor holder tier above the turbine controller doubles the power (multiplier 2^(holder tier - controller tier)) and burns 1.8x the fuel, about 10 % better efficiency per tier. A LuV holder on the EV Large Gas Turbine is 2 tiers up: 4x power for about 3.2x fuel (derived).
- LuV rotor holder (pack recipe): LuV hull + 4 HSS-S gears + 1 LuV electric motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 RPP ring + 288 mB PTFE, circuit 3, a LuV-tier assembler recipe.
- Rotors: dragonsteel is a ZPM material (EBF 7 100 K, ZPM hatch, naquadah coils), so do not plan dragonsteel rotors in LuV; prismalium (rotor power 1600) is later still.
- Rotor holders cannot be shared between turbines (gtceu jar: canShared = false): one holder per turbine. Walls, fluid hatches and dynamo hatches can be shared (see the Combos phase).
- This is generation; the Power Substation (luv\_power) only stores it. Community reports: LuV turbines on LuV rotor holders in 3 reported setups.
- **Unverified** the Large Gas Turbine base output and rotor stats, so the dynamo tier: read the turbine tooltip after fitting the LuV holder and use a dynamo hatch of that voltage.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:gas_large_turbine` | 1 |
| `gtceu:luv_rotor_holder` | 1 |
| `gtceu:steel_drum` | 2 |
| `pipez:fluid_pipe` | 8 |

## Needs / Feeds

- **Needs:** [LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI](luv_hull.md), [HSS-S: HSS-G + iridium + osmium → EBF 5000 K (HSS-G coils) → Vacuum Freezer with liquid helium → the LuV component metal](luv_hsss.md), [LuV components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 7680 EU/t, HSS-S + ruridit + niobium titanium + palladium wire)](luv_components.md), [LuV alloys: rhodium plated palladium (hull), ruridit (gears, rotor) and niobium titanium (cables, pipes), all IV Mixer → EBF 4500 K (RTM coils) → Vacuum Freezer](luv_alloys.md)
- **Main source for:** `gtceu:luv_rotor_holder`
