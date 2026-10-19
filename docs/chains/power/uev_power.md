---
kind: chain
id: uev_power
order: 2150
data:
  t: |-
    UEV power: plasma → Supreme Plasma Turbine with a UEV rotor holder (tungsten disulfide + superstate helium 3 boost) → laser or dynamo hatch
  inf: true
  "n":
    - - pl
      - |-
        Plasma: magmatic (tier 5 fusion) · nickel · iron · oxygen · nitrogen · argon · helium · americium · tin
      - f
      - gtceu:magmatic_plasma_bucket
    - - g1
      - |-
        UEV rotor holder: 1 uev machine hull · 4 starium alloy gear · 2 uev electric motor · 6 small mythrolic alloy gear · 8 magmada alloy round · 1 mythrolic alloy ring · 2 uev transmission assembly · 1 uev precision drive mechanism · 1 UEV circuit · 12 fine adamantine wire · 576 mB polyether ether ketone · 5 000 mB tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [uev machine hull, "gtceu:uev_machine_hull"]
        - [starium alloy gear, "gtceu:starium_alloy_gear"]
        - [uev electric motor, "gtceu:uev_electric_motor"]
        - [small mythrolic alloy gear, "gtceu:small_mythrolic_alloy_gear"]
        - [magmada alloy round, "gtceu:magmada_alloy_round"]
        - [mythrolic alloy ring, "gtceu:mythrolic_alloy_ring"]
    - - al
      - Assembly Line · 20 s · 7 864 320 EU/t · research of the UHV rotor holder 160 CWU/t
      - m
      - gtceu:assembly_line
    - [rh, UEV Rotor Holder, x, "gtceu:uev_rotor_holder"]
    - - sp
      - |-
        Supreme Plasma Turbine (UHV controller: UHV page) · base 16 384 EU/t · 6 parallels
      - m
      - gtceu:supreme_plasma_turbine
    - - bo
      - |-
        Boost per hour: 1000 B tungsten disulfide (+25 %), 2500 B superstate helium 3 (+75 %)
      - f
      - gtceu:superstate_helium_3_bucket
    - [lh, "UEV 256A laser source hatch (uev_hatches) → UEV power line", o, "gtceu:uev_256a_laser_source_hatch"]
  e: [[g1, al, "1"], [al, rh, "1 / 20 s"], [rh, sp, "1"], [pl, sp, plasma], [bo, sp, boost], [sp, lh, EU]]
  tips:
    - |-
      Verified from the pack lang file (assets/gtceu/lang/en_us.json) and kjs systems/fusion/plasma_turbines.js: Supreme Plasma Turbine = boosted Large Plasma Turbine, base production 16 384 EU/t; each rotor holder above IV multiplies EU/t by 2 and adds 10 % efficiency; up to 6x the parallels of a standard Large Plasma Turbine; lubricant boosting: 1000 B tungsten disulfide per hour for +25 % EU/t, skipping it costs -10 %; coolant boosting: 2500 B superstate helium 3 per hour for +75 %, only while lubricant boosting is active; accepts laser hatches. By the first rule a UEV rotor holder (LuV, ZPM, UV, UHV, UEV = 5 steps above IV) gives 16 384 x 32 = 524 288 EU/t and +50 % efficiency per turbine (verified from the lang formula); the final total with the 6 parallels and the lubricant / coolant boosts is applied by the mod code (BoostedPlasmaTurbine) and could not be read, so treat 524 288 EU/t as the base figure.
    - |-
      Plasma recipes (plasma_turbines.js, plasma_generator): 5 mB (gases) or 1 mB (metals) per run at -2048 EU/t base: nickel 180 ticks, iron 135, oxygen 98, nitrogen 110, argon 116, helium 27, americium 984, tin 84; magmatic plasma is the one special case: 1 mB → 1 mB infernal concentrate over 748 ticks at -8192 EU/t base. Infernal concentrate is also the input of the tier 5 magmatic plasma fusion recipe (500 mB + 288 mB iron plasma → 144 mB, uev_fusion), so the loop is: burn magmatic plasma, return concentrate to the reactor.
    - |-
      UEV rotor holder: Assembly Line, 400 ticks, VA[UEV] = 7 864 320 EU/t, station research of the UHV rotor holder (VA[UHV], 160 CWU/t): UEV hull, 4 starium gears, 2 UEV motors, 6 small mythrolic gears, 8 magmada rounds, 1 mythrolic ring, 2 UEV transmission assemblies, 1 UEV precision drive mechanism, 1 UEV circuit, 12 fine adamantine wire, 576 mB PEEK, 5000 mB tungsten disulfide. The Ultimate EBF of the UIV page ALSO uses one UEV rotor holder in its pattern.
    - |-
      Controller: Supreme Plasma Turbine = UHV hull + 6 dense enriched naquadah plates + 4 neutronium gears + 6 small naquadah alloy gears + 8 enriched naquadah huge pipes + 6 UHV circuits + 64 fine RTA neutronate wire + 64 UHPIC chips, 4320 mB PEEK + 5000 mB naquadria + 2500 mB lubricant, 600 ticks, VHA[UHV], research Large Plasma Turbine (128 CWU/t). The Nyinsane Plasma Turbine (UIV page) is the 12x version that boosts with oganesson stabilized BEC.
    - |-
      Sub-steps people skip: (1) the holder is a hatch of the turbine structure, not a casing: it replaces the rotor holder slot (R in the pattern); (2) the boost fluids are per HOUR of runtime: put 1000 B and 2500 B in drums with a pump cover, a missing lubricant reduces output by 10 %; (3) the 256A laser hatch (not a dynamo) is the output: both ends need a laser cable; (4) fusion output (magmatic plasma needs tier 5 reflectors) is the real limit.
    - |-
      Unverified: exact output of the UEV setup, which rotor material, and whether the plasma is gated by the reactor tier.
  b:
    - ["gtceu:supreme_plasma_turbine", 1]
    - ["gtceu:uev_rotor_holder", 1]
    - ["gtceu:uev_256a_laser_source_hatch", 1]
    - ["gtceu:assembly_line", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uev_machine_hull", "kubejs:uev_transmission_assembly"]
      t: |-
        Rotor holder parts first: hull, starium gears, UEV motors, small mythrolic gears, magmada rounds, ring, transmission assemblies, precision drive, circuit, adamantine wire. Drums: PEEK and tungsten disulfide.
    - i: ["gtceu:assembly_line", "gtceu:uev_rotor_holder"]
      t: |-
        Assembly Line: station research of the UHV rotor holder, then 20 s per holder at 7 864 320 EU/t. Output drawer Keep Exact 2.
    - i: ["gtceu:supreme_plasma_turbine", "gtceu:uev_rotor_holder"]
      t: Swap the UEV rotor holder into the Supreme Plasma Turbine's holder slot; fluid input and output hatches are UHV ones.
    - i: ["gtceu:magmatic_plasma_bucket", "gtceu:infernal_concentrate_bucket"]
      t: Plasma by a Pipez fluid pipe with a pump cover from the reactor drum; returned gas or concentrate by a second pipe into its own drum.
    - i: ["gtceu:superstate_helium_3_bucket", "gtceu:tungsten_disulfide_bucket"]
      t: |-
        Boost drums: tungsten disulfide first, then superstate helium 3; each with Keep Exact 2500 so the turbine does not lose 10 %.
    - i: ["gtceu:uev_256a_laser_source_hatch", "gtceu:uev_energy_output_hatch"]
      t: |-
        Output: UEV 256A laser source hatch into the grid, or UEV dynamo hatches for a short run.
---
# UEV power: plasma → Supreme Plasma Turbine with a UEV rotor holder (tungsten disulfide + superstate helium 3 boost) → laser or dynamo hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_power` · **Tags:** Infinite source, Unverified

**Plan modules:** [UEV fusion and plasma power](../../plan/p18.md#uevfusion)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 7 864 320 EU/t · research of the UHV rotor holder 160 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UEV rotor holder: 1 uev machine hull · 4 starium alloy gear · 2 uev electric motor · 6 small mythrolic alloy gear · 8 magmada alloy round · 1 mythrolic alloy ring · 2 uev transmission assembly · 1 uev precision drive mechanism · 1 UEV circuit · 12 fine adamantine wire · 576 mB polyether ether ketone · 5 000 mB tungsten disulfide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UEV rotor holder: 1 uev machine hull · 4 starium alloy gear · 2 uev electric motor · 6 small mythrolic alloy gear · 8 magmada alloy round · 1 mythrolic alloy ring · 2 uev transmission assembly · 1 uev precision drive mechanism · 1 UEV circuit · 12 fine adamantine wire · 576 mB polyether ether ketone · 5 000 mB tungsten disulfide</span><span class="gt-sub"><span>uev machine hull</span><span>starium alloy gear</span><span>uev electric motor</span><span>small mythrolic alloy gear</span><span>magmada alloy round</span><span>mythrolic alloy ring</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Rotor Holder (gtceu:uev_rotor_holder) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Rotor Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-mod" id="m-sp">
<div class="gt-head"><span class="gt-mname">Supreme Plasma Turbine (UHV controller: UHV page) · base 16 384 EU/t · 6 parallels</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UEV Rotor Holder (gtceu:uev_rotor_holder) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Rotor Holder</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Plasma: magmatic (tier 5 fusion) · nickel · iron · oxygen · nitrogen · argon · helium · americium · tin (gtceu:magmatic_plasma_bucket) - plasma"><img class="gt-ico" src="../../assets/icons/gtceu__magmatic_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magmatic Plasma</span><span class="gt-note">Plasma: magmatic (tier 5 fusion) · nickel · iron · oxygen · nitrogen · argon · helium · americium · tin</span><b class="gt-q">plasma</b></span><span class="gt-slot gt-fluid" title="Boost per hour: 1000 B tungsten disulfide (+25 %), 2500 B superstate helium 3 (+75 %) (gtceu:superstate_helium_3_bucket) - boost"><img class="gt-ico" src="../../assets/icons/gtceu__superstate_helium_3_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superstate Helium 3</span><span class="gt-note">Boost per hour: 1000 B tungsten disulfide (+25 %), 2500 B superstate helium 3 (+75 %)</span><b class="gt-q">boost</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__supreme_plasma_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UEV 256A laser source hatch (uev_hatches) → UEV power line (gtceu:uev_256a_laser_source_hatch) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__uev_256a_laser_source_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV 256a Laser Source Hatch</span><span class="gt-note">UEV 256A laser source hatch (uev_hatches) → UEV power line</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:supreme_plasma_turbine</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 7 864 320 EU/t · research of the UHV rotor holder 160 CWU/t](#m-al) → [Supreme Plasma Turbine (UHV controller: UHV page) · base 16 384 EU/t · 6 parallels](#m-sp)

## How to build

1. Rotor holder parts first: hull, starium gears, UEV motors, small mythrolic gears, magmada rounds, ring, transmission assemblies, precision drive, circuit, adamantine wire. Drums: PEEK and tungsten disulfide. — `functionalstorage:oak_1`, `gtceu:uev_machine_hull`, `kubejs:uev_transmission_assembly`
2. Assembly Line: station research of the UHV rotor holder, then 20 s per holder at 7 864 320 EU/t. Output drawer Keep Exact 2. — `gtceu:assembly_line`, `gtceu:uev_rotor_holder`
3. Swap the UEV rotor holder into the Supreme Plasma Turbine's holder slot; fluid input and output hatches are UHV ones. — `gtceu:supreme_plasma_turbine`, `gtceu:uev_rotor_holder`
4. Plasma by a Pipez fluid pipe with a pump cover from the reactor drum; returned gas or concentrate by a second pipe into its own drum. — `gtceu:magmatic_plasma_bucket`, `gtceu:infernal_concentrate_bucket`
5. Boost drums: tungsten disulfide first, then superstate helium 3; each with Keep Exact 2500 so the turbine does not lose 10 %. — `gtceu:superstate_helium_3_bucket`, `gtceu:tungsten_disulfide_bucket`
6. Output: UEV 256A laser source hatch into the grid, or UEV dynamo hatches for a short run. — `gtceu:uev_256a_laser_source_hatch`, `gtceu:uev_energy_output_hatch`

## Tips

- Verified from the pack lang file (assets/gtceu/lang/en\_us.json) and kjs systems/fusion/plasma\_turbines.js: Supreme Plasma Turbine = boosted Large Plasma Turbine, base production 16 384 EU/t; each rotor holder above IV multiplies EU/t by 2 and adds 10 % efficiency; up to 6x the parallels of a standard Large Plasma Turbine; lubricant boosting: 1000 B tungsten disulfide per hour for +25 % EU/t, skipping it costs -10 %; coolant boosting: 2500 B superstate helium 3 per hour for +75 %, only while lubricant boosting is active; accepts laser hatches. By the first rule a UEV rotor holder (LuV, ZPM, UV, UHV, UEV = 5 steps above IV) gives 16 384 x 32 = 524 288 EU/t and +50 % efficiency per turbine (verified from the lang formula); the final total with the 6 parallels and the lubricant / coolant boosts is applied by the mod code (BoostedPlasmaTurbine) and could not be read, so treat 524 288 EU/t as the base figure.
- Plasma recipes (plasma\_turbines.js, plasma\_generator): 5 mB (gases) or 1 mB (metals) per run at -2048 EU/t base: nickel 180 ticks, iron 135, oxygen 98, nitrogen 110, argon 116, helium 27, americium 984, tin 84; magmatic plasma is the one special case: 1 mB → 1 mB infernal concentrate over 748 ticks at -8192 EU/t base. Infernal concentrate is also the input of the tier 5 magmatic plasma fusion recipe (500 mB + 288 mB iron plasma → 144 mB, uev\_fusion), so the loop is: burn magmatic plasma, return concentrate to the reactor.
- UEV rotor holder: Assembly Line, 400 ticks, VA\[UEV\] = 7 864 320 EU/t, station research of the UHV rotor holder (VA\[UHV\], 160 CWU/t): UEV hull, 4 starium gears, 2 UEV motors, 6 small mythrolic gears, 8 magmada rounds, 1 mythrolic ring, 2 UEV transmission assemblies, 1 UEV precision drive mechanism, 1 UEV circuit, 12 fine adamantine wire, 576 mB PEEK, 5000 mB tungsten disulfide. The Ultimate EBF of the UIV page ALSO uses one UEV rotor holder in its pattern.
- Controller: Supreme Plasma Turbine = UHV hull + 6 dense enriched naquadah plates + 4 neutronium gears + 6 small naquadah alloy gears + 8 enriched naquadah huge pipes + 6 UHV circuits + 64 fine RTA neutronate wire + 64 UHPIC chips, 4320 mB PEEK + 5000 mB naquadria + 2500 mB lubricant, 600 ticks, VHA\[UHV\], research Large Plasma Turbine (128 CWU/t). The Nyinsane Plasma Turbine (UIV page) is the 12x version that boosts with oganesson stabilized BEC.
- Sub-steps people skip: (1) the holder is a hatch of the turbine structure, not a casing: it replaces the rotor holder slot (R in the pattern); (2) the boost fluids are per HOUR of runtime: put 1000 B and 2500 B in drums with a pump cover, a missing lubricant reduces output by 10 %; (3) the 256A laser hatch (not a dynamo) is the output: both ends need a laser cable; (4) fusion output (magmatic plasma needs tier 5 reflectors) is the real limit.
- **Unverified** exact output of the UEV setup, which rotor material, and whether the plasma is gated by the reactor tier.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:supreme_plasma_turbine` | 1 |
| `gtceu:uev_rotor_holder` | 1 |
| `gtceu:uev_256a_laser_source_hatch` | 1 |
| `gtceu:assembly_line` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:uev_rotor_holder`
