---
kind: chain
id: uv_power
order: 1710
data:
  t: |-
    UV power: potassium + fluorine → nickel plasma (UV Fusion Reactor, tier-3 reflectors) → Large Plasma Turbine with a UV rotor holder → UV dynamo hatch
  inf: true
  "n":
    - - g1
      - "144 mB potassium · 1 B fluorine"
      - g
      - functionalstorage:oak_1
      - [[Potassium, "gtceu:potassium_bucket"], [Fluorine, "gtceu:fluorine_bucket"]]
    - - fr
      - UV Fusion Reactor · 7.2 s · 30 720 EU/t · start 480 MEU · reflector tier 3
      - m
      - start_core:uv_fusion_reactor
    - [np, "144 mB nickel plasma", x, "gtceu:nickel_plasma_bucket"]
    - - g2
      - UV hull · 4 tritan steel gear · 2 UV motor · 4 small darmstadtium gear · 6 tritan steel round · darmstadtium ring · UV circuit · 8 fine americium wire · 288 mB PBI
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [Tritan steel gear, "gtceu:tritan_steel_gear"]
        - [UV motor, "gtceu:uv_electric_motor"]
        - [Small darmstadtium gear, "gtceu:small_darmstadtium_gear"]
        - [Darmstadtium ring, "gtceu:darmstadtium_ring"]
    - [ra, "UV Assembler · circuit 3 · 5 s · 245 760 EU/t", m, "gtceu:large_assembler"]
    - [rh, UV Rotor Holder, x, "gtceu:uv_rotor_holder"]
    - - tb
      - |-
        Large Plasma Turbine + rotor (nickel: 1 mB per 180 ticks at 2048 EU/t base)
      - m
      - gtceu:plasma_large_turbine
    - [eu, "UV Dynamo Hatch → UV power line", o, "gtceu:uv_energy_output_hatch"]
    - - g3
      - |-
        Alt: 144 mB silicon · 144 mB magnesium → iron plasma (tier 3, 7680 EU/t, 10.8 s, start 360 MEU)
      - g
      - functionalstorage:oak_1
      - [[Silicon, "gtceu:silicon_bucket"], [Magnesium, "gtceu:magnesium_bucket"]]
  e:
    - [g1, fr, "1 B + 144 mB"]
    - [fr, np, "144 mB / 7.2 s"]
    - [np, tb, "1 mB / 180 ticks"]
    - [g3, fr, alt]
    - [g2, ra, "1"]
    - [ra, rh, "1 / 5 s"]
    - [rh, tb, "1"]
    - [tb, eu, EU]
  tips:
    - |-
      Fuel (kjs systems/fusion/fusion_scaling.js + plasma_turbines.js, verified): tier-3 reflector recipes of the UV reactor: nickel plasma = 144 mB potassium + 1 B fluorine → 144 mB, 30 720 EU/t, 7.2 s, start 480 MEU; iron plasma = 144 mB silicon + 144 mB magnesium → 144 mB, 7680 EU/t, 10.8 s, start 360 MEU. The pack replaces every plasma generator recipe: metal plasmas burn 1 mB per recipe, 2048 EU/t base: nickel 180 ticks, iron 135 ticks, tin 84, americium 984 (americium plasma needs tier-4 reflectors, the UHV page); gas plasmas burn 5 mB (helium 27 ticks, oxygen 98, nitrogen 110, argon 116).
    - |-
      Energy bookkeeping (base figures before rotor efficiency): 1 mB nickel plasma = 180 x 2048 = 368 640 EU, so one 144 mB run = 53 MEU against 0.22 MEU of reactor power plus the 480 MEU start buffer; 1 mB iron plasma = 276 480 EU (39.8 MEU per 144 mB). Nickel is the better fuel; the real limits are fluorine and potassium supply, not the reactor. The start energy has to be in a Power Substation or a laser source before each recipe (not refunded: Unverified).
    - |-
      UV rotor holder (plasma_turbines.js; the pack removes every GT holder recipe): assembler, circuit 3, 100 ticks, VHA[UV] = 245 760 EU/t: UV hull + 4 tritan steel gears + 2 UV motors + 4 small darmstadtium gears + 6 tritan steel rounds + 1 darmstadtium ring + 1 UV-tag circuit + 8 fine americium wire + 288 mB PBI. The Large Plasma Turbine controller is still the old LuV one (crafting table, LuV hull + 2 LuV circuits + 4 tungsten steel gears + 2 large tungsten steel pipes), see zpm_power; the UHV page upgrades to the Supreme Plasma Turbine (needs 6 UHV circuits).
    - |-
      Output: a UV dynamo hatch (UV hull + 4 YBCO springs + 2 UHPIC + circuit + 2 voltage coils + 10 B sodium potassium, station research of the ZPM dynamo hatch at 64 CWU/t, see uv_hatches). Cables: UV 4A / 16A laser hatches (large_energy_hatches.js: 256A laser hatch = substation hatch + diamond lens + UV sensor/emitter + pump + 4 YBCO cables) move the power to the substation.
    - |-
      Fluorine and dimension air (verified): no KubeJS recipe turns topaz into fluorine (a topaz gCrop exists, tier 3, but its processing lives in the mod jar, so do not count on it). Fluorine comes from the HF electrolysis, the naquadah chemical-plant skip (14 000 mB, ZPM) or the uraninite skip (40 000 mB, LuV). Nether-air and ender-air gCrops exist (tier 4); without them use HV mixers: 3 netherrack dust + 32 000 mB air -> 24 000 mB nether air, then 3 endstone dust + 32 000 mB nether air -> 24 000 mB ender air (netherrack and endstone dust from the LCR recipes easy_netherrack / easy_endstone).
    - |-
      Sub-steps people skip: (1) the 480 MEU start energy is more than a MK II needed; (2) fluorine and potassium: each run of nickel plasma uses 1 B fluorine, so a fluorine line (HF electrolysis, the uv_peek chain uses it too) must scale; (3) keep two plasma drums: a full turbine blocks the reactor; (4) the rotor: any GT turbine rotor fits (Unverified efficiency), tritan steel is the pack’s UV-tier rotor metal; (5) do not mix nickel and iron plasma in one input hatch.
    - |-
      Unverified: turbine output multiplier with the UV holder, start-energy handling, rotor choice.
  b:
    - ["gtceu:plasma_large_turbine", 1]
    - ["gtceu:uv_rotor_holder", 1]
    - ["start_core:uv_fusion_reactor", 1]
    - ["gtceu:uv_energy_output_hatch", 1]
    - ["gtceu:power_substation", 2]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 5]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:nickel_plasma_bucket", "gtceu:fluorine_bucket"]
      t: |-
        Drums first: potassium, fluorine, nickel plasma, spent nickel. Each machine on its own Pipez fluid pipe from its drum with a pump cover; a Keep Exact valve on the plasma drum so a full turbine does not stall the reactor.
    - i: ["start_core:uv_fusion_reactor", "gtceu:nickel_plasma_bucket"]
      t: |-
        Reactor: tier-3 reflectors, 144 mB potassium + 1 B fluorine → 144 mB nickel plasma every 7.2 s at 30 720 EU/t, 480 MEU start from the Power Substation. Share it with neutronium runs by emptying the hatches between recipes, or build a second reactor.
    - i: ["gtceu:large_assembler", "gtceu:uv_rotor_holder", "gtceu:uv_electric_motor"]
      t: |-
        Rotor holder: ghost circuit 3, UV hull + 4 tritan steel gears + 2 UV motors + small darmstadtium gears + rounds + ring + circuit + americium wire + 288 mB PBI → holder in 5 s. Output drawer Keep Exact 2.
    - i: ["gtceu:plasma_large_turbine", "gtceu:uv_rotor_holder", "gtceu:tritan_steel_ingot"]
      t: |-
        Turbine: controller (zpm_power), structure, a UV rotor holder, a turbine rotor. Plasma in by a Pipez fluid pipe with a valve, spent nickel out into a drum.
    - i: ["gtceu:plasma_large_turbine", "gtceu:uv_energy_output_hatch"]
      t: |-
        Dynamo hatch: UV; output into the Power Substation (luv_power) and from there into the line. Read the turbine tooltip for real EU/t; Unverified here.
    - i: ["functionalstorage:oak_1", "gtceu:fluorine_bucket"]
      t: |-
        Easy to miss: size the fluorine line first. The reactor eats 1 B per 7.2 s run, 500 B per hour.
---
# UV power: potassium + fluorine → nickel plasma (UV Fusion Reactor, tier-3 reflectors) → Large Plasma Turbine with a UV rotor holder → UV dynamo hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_power` · **Tags:** Infinite source, Unverified

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-uv" id="m-fr">
<div class="gt-head"><span class="gt-mname">UV Fusion Reactor · 7.2 s · 30 720 EU/t · start 480 MEU · reflector tier 3</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="144 mB potassium · 1 B fluorine (functionalstorage:oak_1) - 1 B + 144 mB"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">144 mB potassium · 1 B fluorine</span><span class="gt-sub"><span>Potassium</span><span>Fluorine</span></span><b class="gt-q">1 B + 144 mB</b></span><span class="gt-slot gt-group" title="Alt: 144 mB silicon · 144 mB magnesium → iron plasma (tier 3, 7680 EU/t, 10.8 s, start 360 MEU) (functionalstorage:oak_1) - alt"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Alt: 144 mB silicon · 144 mB magnesium → iron plasma (tier 3, 7680 EU/t, 10.8 s, start 360 MEU)</span><span class="gt-sub"><span>Silicon</span><span>Magnesium</span></span><b class="gt-q">alt</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__uv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">7.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="144 mB nickel plasma (gtceu:nickel_plasma_bucket) - 144 mB / 7.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Plasma Bucket</span><span class="gt-note">144 mB nickel plasma</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:uv_fusion_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-ra">
<div class="gt-head"><span class="gt-mname">UV Assembler · circuit 3 · 5 s · 245 760 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · 4 tritan steel gear · 2 UV motor · 4 small darmstadtium gear · 6 tritan steel round · darmstadtium ring · UV circuit · 8 fine americium wire · 288 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · 4 tritan steel gear · 2 UV motor · 4 small darmstadtium gear · 6 tritan steel round · darmstadtium ring · UV circuit · 8 fine americium wire · 288 mB PBI</span><span class="gt-sub"><span>UV Machine Hull</span><span>Tritan steel gear</span><span>UV motor</span><span>Small darmstadtium gear</span><span>Darmstadtium ring</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Rotor Holder (gtceu:uv_rotor_holder) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Rotor Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-tb">
<div class="gt-head"><span class="gt-mname">Large Plasma Turbine + rotor (nickel: 1 mB per 180 ticks at 2048 EU/t base)</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="144 mB nickel plasma (gtceu:nickel_plasma_bucket) - 1 mB / 180 ticks"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Plasma Bucket</span><span class="gt-note">144 mB nickel plasma</span><b class="gt-q">1 mB</b></span><span class="gt-slot" title="UV Rotor Holder (gtceu:uv_rotor_holder) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Rotor Holder</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__plasma_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">180 ticks</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Dynamo Hatch → UV power line (gtceu:uv_energy_output_hatch) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__uv_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Energy Output Hatch</span><span class="gt-note">UV Dynamo Hatch → UV power line</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:plasma_large_turbine</code></div>
</div>
</div>

## Flow

- [UV Fusion Reactor · 7.2 s · 30 720 EU/t · start 480 MEU · reflector tier 3](#m-fr) → [Large Plasma Turbine + rotor (nickel: 1 mB per 180 ticks at 2048 EU/t base)](#m-tb)
- [UV Assembler · circuit 3 · 5 s · 245 760 EU/t](#m-ra) → [Large Plasma Turbine + rotor (nickel: 1 mB per 180 ticks at 2048 EU/t base)](#m-tb)

## How to build

1. Drums first: potassium, fluorine, nickel plasma, spent nickel. Each machine on its own Pipez fluid pipe from its drum with a pump cover; a Keep Exact valve on the plasma drum so a full turbine does not stall the reactor. — `functionalstorage:oak_1`, `gtceu:nickel_plasma_bucket`, `gtceu:fluorine_bucket`
2. Reactor: tier-3 reflectors, 144 mB potassium + 1 B fluorine → 144 mB nickel plasma every 7.2 s at 30 720 EU/t, 480 MEU start from the Power Substation. Share it with neutronium runs by emptying the hatches between recipes, or build a second reactor. — `start_core:uv_fusion_reactor`, `gtceu:nickel_plasma_bucket`
3. Rotor holder: ghost circuit 3, UV hull + 4 tritan steel gears + 2 UV motors + small darmstadtium gears + rounds + ring + circuit + americium wire + 288 mB PBI → holder in 5 s. Output drawer Keep Exact 2. — `gtceu:large_assembler`, `gtceu:uv_rotor_holder`, `gtceu:uv_electric_motor`
4. Turbine: controller (zpm\_power), structure, a UV rotor holder, a turbine rotor. Plasma in by a Pipez fluid pipe with a valve, spent nickel out into a drum. — `gtceu:plasma_large_turbine`, `gtceu:uv_rotor_holder`, `gtceu:tritan_steel_ingot`
5. Dynamo hatch: UV; output into the Power Substation (luv\_power) and from there into the line. Read the turbine tooltip for real EU/t; Unverified here. — `gtceu:plasma_large_turbine`, `gtceu:uv_energy_output_hatch`
6. Easy to miss: size the fluorine line first. The reactor eats 1 B per 7.2 s run, 500 B per hour. — `functionalstorage:oak_1`, `gtceu:fluorine_bucket`

## Tips

- Fuel (kjs systems/fusion/fusion\_scaling.js + plasma\_turbines.js, verified): tier-3 reflector recipes of the UV reactor: nickel plasma = 144 mB potassium + 1 B fluorine → 144 mB, 30 720 EU/t, 7.2 s, start 480 MEU; iron plasma = 144 mB silicon + 144 mB magnesium → 144 mB, 7680 EU/t, 10.8 s, start 360 MEU. The pack replaces every plasma generator recipe: metal plasmas burn 1 mB per recipe, 2048 EU/t base: nickel 180 ticks, iron 135 ticks, tin 84, americium 984 (americium plasma needs tier-4 reflectors, the UHV page); gas plasmas burn 5 mB (helium 27 ticks, oxygen 98, nitrogen 110, argon 116).
- Energy bookkeeping (base figures before rotor efficiency): 1 mB nickel plasma = 180 x 2048 = 368 640 EU, so one 144 mB run = 53 MEU against 0.22 MEU of reactor power plus the 480 MEU start buffer; 1 mB iron plasma = 276 480 EU (39.8 MEU per 144 mB). Nickel is the better fuel; the real limits are fluorine and potassium supply, not the reactor. The start energy has to be in a Power Substation or a laser source before each recipe (not refunded: Unverified).
- UV rotor holder (plasma\_turbines.js; the pack removes every GT holder recipe): assembler, circuit 3, 100 ticks, VHA\[UV\] = 245 760 EU/t: UV hull + 4 tritan steel gears + 2 UV motors + 4 small darmstadtium gears + 6 tritan steel rounds + 1 darmstadtium ring + 1 UV-tag circuit + 8 fine americium wire + 288 mB PBI. The Large Plasma Turbine controller is still the old LuV one (crafting table, LuV hull + 2 LuV circuits + 4 tungsten steel gears + 2 large tungsten steel pipes), see zpm\_power; the UHV page upgrades to the Supreme Plasma Turbine (needs 6 UHV circuits).
- Output: a UV dynamo hatch (UV hull + 4 YBCO springs + 2 UHPIC + circuit + 2 voltage coils + 10 B sodium potassium, station research of the ZPM dynamo hatch at 64 CWU/t, see uv\_hatches). Cables: UV 4A / 16A laser hatches (large\_energy\_hatches.js: 256A laser hatch = substation hatch + diamond lens + UV sensor/emitter + pump + 4 YBCO cables) move the power to the substation.
- Fluorine and dimension air (verified): no KubeJS recipe turns topaz into fluorine (a topaz gCrop exists, tier 3, but its processing lives in the mod jar, so do not count on it). Fluorine comes from the HF electrolysis, the naquadah chemical-plant skip (14 000 mB, ZPM) or the uraninite skip (40 000 mB, LuV). Nether-air and ender-air gCrops exist (tier 4); without them use HV mixers: 3 netherrack dust + 32 000 mB air -&gt; 24 000 mB nether air, then 3 endstone dust + 32 000 mB nether air -&gt; 24 000 mB ender air (netherrack and endstone dust from the LCR recipes easy\_netherrack / easy\_endstone).
- Sub-steps people skip: (1) the 480 MEU start energy is more than a MK II needed; (2) fluorine and potassium: each run of nickel plasma uses 1 B fluorine, so a fluorine line (HF electrolysis, the uv\_peek chain uses it too) must scale; (3) keep two plasma drums: a full turbine blocks the reactor; (4) the rotor: any GT turbine rotor fits (Unverified efficiency), tritan steel is the pack’s UV-tier rotor metal; (5) do not mix nickel and iron plasma in one input hatch.
- **Unverified** turbine output multiplier with the UV holder, start-energy handling, rotor choice.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:plasma_large_turbine` | 1 |
| `gtceu:uv_rotor_holder` | 1 |
| `start_core:uv_fusion_reactor` | 1 |
| `gtceu:uv_energy_output_hatch` | 1 |
| `gtceu:power_substation` | 2 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `gtceu:uv_rotor_holder`, `gtceu:nickel_plasma_bucket`
