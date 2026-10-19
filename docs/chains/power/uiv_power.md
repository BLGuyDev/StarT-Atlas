---
kind: chain
id: uiv_power
order: 2230
data:
  t: |-
    UIV power: plasma → Nyinsane Plasma Turbine with a UIV rotor holder (tungsten disulfide + BEC oganesson boost) → laser hatch
  inf: true
  "n":
    - - pl
      - Plasma (magmatic, nickel, americium ...) from the tier 5 and tier 6 reactors
      - f
      - gtceu:magmatic_plasma_bucket
    - - g1
      - |-
        UIV rotor holder: 1 uiv machine hull · 4 ohmderblux alloy gear · 2 uiv electric motor · 6 small chaotixic alloy gear · 8 abyssal alloy round · 1 chaotixic alloy ring · 2 uiv transmission assembly · 1 uiv precision drive mechanism · 1 UIV circuit · 1 uiv field generator · 16 fine xeproda wire · 432 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [ohmderblux alloy gear, "gtceu:ohmderblux_alloy_gear"]
        - [uiv electric motor, "gtceu:uiv_electric_motor"]
        - [small chaotixic alloy gear, "gtceu:small_chaotixic_alloy_gear"]
        - [abyssal alloy round, "gtceu:abyssal_alloy_round"]
        - [chaotixic alloy ring, "gtceu:chaotixic_alloy_ring"]
    - - al
      - Assembly Line · 20 s · 31 457 280 EU/t · research of the UEV holder 192 CWU/t
      - m
      - gtceu:assembly_line
    - [rh, UIV Rotor Holder, x, "gtceu:uiv_rotor_holder"]
    - - g2
      - |-
        Nyinsane Plasma Turbine: 1 uiv machine hull · 6 dense nyanium plate · 4 chaotixic alloy gear · 6 small nyanium gear · 8 nyanium huge fluid pipe · 6 UIV circuit · 64 fine rhenium super composite alloy wire · 160 uepic chip · 4 320 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 000 mB calamatium · 2 500 mB tungsten disulfide
      - g
      - functionalstorage:oak_1
      - - [uiv machine hull, "gtceu:uiv_machine_hull"]
        - [dense nyanium plate, "gtceu:dense_nyanium_plate"]
        - [chaotixic alloy gear, "gtceu:chaotixic_alloy_gear"]
        - [small nyanium gear, "gtceu:small_nyanium_gear"]
        - [nyanium huge fluid pipe, "gtceu:nyanium_huge_fluid_pipe"]
        - [UIV circuit, "kubejs:uiv_universal_circuit"]
    - - a2
      - Assembly Line · 30 s · 15 728 640 EU/t · research Supreme Plasma Turbine 192 CWU/t
      - m
      - gtceu:assembly_line
    - [np, "Nyinsane Plasma Turbine · 12 parallels", x, "gtceu:nyinsane_plasma_turbine"]
    - [bo, "Per hour: 2500 B tungsten disulfide (+50 %) and 800 B BEC oganesson (+150 %)", f, "gtceu:bec_og_bucket"]
    - [lh, "UIV 256A laser source hatch (uiv_hatches)", o, "gtceu:uiv_256a_laser_source_hatch"]
  e:
    - [g1, al, "1"]
    - [al, rh, "1 / 20 s"]
    - [rh, np, "1"]
    - [g2, a2, "1"]
    - [a2, np, "1 / 30 s"]
    - [pl, np, plasma]
    - [bo, np, boost]
    - [np, lh, EU]
  tips:
    - |-
      Verified from the pack lang file (assets/gtceu/lang/en_us.json) and kjs systems/fusion/plasma_turbines.js + startup more_plasma_turbine.js: the Nyinsane Plasma Turbine is the UIV boosted turbine (BoostedPlasmaTurbine tier UIV); up to 12x the parallels of a standard Large Plasma Turbine; lubricant boosting: 2500 B tungsten disulfide per hour for +50 % EU/t, skipping it costs -20 %; coolant boosting: 800 B oganesson stabilized Bose-Einstein condensate (BEC oganesson, uev_chiller) per hour for +150 %, only while lubricant boosting is active; uses laser hatches. The base production line of the tooltip is not in the lang file for this machine (the Supreme says 16 384 EU/t; each rotor holder above IV doubles EU/t and adds 10 % efficiency): Unverified for the Nyinsane.
    - |-
      UIV rotor holder: Assembly Line 400 ticks, VA[UIV] = 31 457 280 EU/t, station research of the UEV rotor holder (VA[UEV], 192 CWU/t): UIV hull + 4 ohmderblux gears + 2 UIV motors + 6 small chaotixic gears + 8 abyssal alloy rounds + 1 chaotixic ring + 2 UIV transmission assemblies + 1 UIV precision drive + 1 UIV circuit + 1 UIV field generator + 16 fine xeproda wire, 432 mB PEDOT:PSS + 10 000 mB tungsten disulfide. Nyinsane Plasma Turbine: 600 ticks, VHA[UIV], research Supreme Plasma Turbine (192 CWU/t): UIV hull + 6 dense nyanium plates + 4 chaotixic gears + 6 small nyanium gears + 8 nyanium huge fluid pipes + 6 UIV circuits + 64 fine rhenium super composite alloy wire + 160 UEPIC chips, 4320 mB PEDOT:PSS + 5000 mB calamatium + 2500 mB tungsten disulfide.
    - |-
      Draco abyssal rotor (plasma_turbines.js): turbine blade = assembler, 5 double draco abyssal plates + 8 draco abyssal foil + 2 draco abyssal screws + 720 mB void, 50 ticks, VHA[UEV]; rotor = Assembly Line, void frame + UIV transmission assembly + 8 blades + 16 fine rhenium super composite alloy wire, 15 000 mB tungsten disulfide + 1080 mB PEDOT:PSS, 600 ticks, VA[UEV], research Draco Abyssal Rotor (192 CWU/t). The same rotor goes 12 times into the Atomic Materialization Plant controller. Draco abyssal alloy is a Hell Forge recipe at VHA[UXV] (hellforge.js: 9 ingots, preon plasma, abyssal catalyst), so the best rotor is a UXV-priced item: Unverified whether another rotor material works in the holder.
    - |-
      Fuel: the plasma_generator recipes listed in uev_power (nickel, iron, oxygen, nitrogen, argon, helium, americium, tin at -2048 EU/t base, magmatic at -8192 EU/t base returning infernal concentrate). Tier 6 plasma (paradox, voidic, preon) has no turbine recipe in the file: they are alloy inputs, not turbine fuel.
    - |-
      Sub-steps people skip: (1) BEC oganesson is consumed here AND by the alloy chiller: size the oganesson loop (uev_chiller) for both; (2) a turbine without lubricant loses 20 %: keep tungsten disulfide piped in; (3) 160 UEPIC chips per turbine = 80 wafers (uev_chips); (4) the output is a laser source hatch: both ends need laser cables.
    - |-
      Unverified: Nyinsane base output, the effect of the rotor holder tier here, and plasma input rate.
  b:
    - ["gtceu:nyinsane_plasma_turbine", 1]
    - ["gtceu:uiv_rotor_holder", 1]
    - ["gtceu:uiv_256a_laser_source_hatch", 1]
    - ["gtceu:assembly_line", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uiv_machine_hull", "kubejs:uiv_transmission_assembly"]
      t: |-
        Holder parts first: hull, ohmderblux gears, UIV motors, small chaotixic gears, abyssal rounds, ring, transmissions, precision drive, circuit, field generator, xeproda wire. Drums: PEDOT:PSS, tungsten disulfide.
    - i: ["gtceu:assembly_line", "gtceu:uiv_rotor_holder"]
      t: Research the UEV rotor holder, then 20 s per UIV holder at 31 457 280 EU/t. Output Keep Exact 2.
    - i: ["gtceu:assembly_line", "gtceu:nyinsane_plasma_turbine"]
      t: |-
        Controller: 160 UEPIC chips and 6 UIV circuits in drawers; 30 s at 15 728 640 EU/t. Research the Supreme Plasma Turbine first.
    - i: ["gtceu:nyinsane_plasma_turbine", "gtceu:uiv_rotor_holder"]
      t: Put the UIV holder in the turbine's rotor holder slot with a rotor; plasma in, plain gas out, both on Pipez fluid pipes.
    - i: ["gtceu:bec_og_bucket", "gtceu:tungsten_disulfide_bucket"]
      t: |-
        Boost drums: tungsten disulfide 2500 B and BEC oganesson 800 B per hour, each Keep Exact so the turbine never runs without lubricant.
    - i: ["gtceu:uiv_256a_laser_source_hatch"]
      t: Output through the UIV 256A laser source hatch into the line.
---
# UIV power: plasma → Nyinsane Plasma Turbine with a UIV rotor holder (tungsten disulfide + BEC oganesson boost) → laser hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_power` · **Tags:** Infinite source, Unverified

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 31 457 280 EU/t · research of the UEV holder 192 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UIV rotor holder: 1 uiv machine hull · 4 ohmderblux alloy gear · 2 uiv electric motor · 6 small chaotixic alloy gear · 8 abyssal alloy round · 1 chaotixic alloy ring · 2 uiv transmission assembly · 1 uiv precision drive mechanism · 1 UIV circuit · 1 uiv field generator · 16 fine xeproda wire · 432 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB tungsten disulfide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIV rotor holder: 1 uiv machine hull · 4 ohmderblux alloy gear · 2 uiv electric motor · 6 small chaotixic alloy gear · 8 abyssal alloy round · 1 chaotixic alloy ring · 2 uiv transmission assembly · 1 uiv precision drive mechanism · 1 UIV circuit · 1 uiv field generator · 16 fine xeproda wire · 432 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 10 000 mB tungsten disulfide</span><span class="gt-sub"><span>uiv machine hull</span><span>ohmderblux alloy gear</span><span>uiv electric motor</span><span>small chaotixic alloy gear</span><span>abyssal alloy round</span><span>chaotixic alloy ring</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIV Rotor Holder (gtceu:uiv_rotor_holder) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__uiv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UIV Rotor Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 15 728 640 EU/t · research Supreme Plasma Turbine 192 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Nyinsane Plasma Turbine: 1 uiv machine hull · 6 dense nyanium plate · 4 chaotixic alloy gear · 6 small nyanium gear · 8 nyanium huge fluid pipe · 6 UIV circuit · 64 fine rhenium super composite alloy wire · 160 uepic chip · 4 320 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 000 mB calamatium · 2 500 mB tungsten disulfide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Nyinsane Plasma Turbine: 1 uiv machine hull · 6 dense nyanium plate · 4 chaotixic alloy gear · 6 small nyanium gear · 8 nyanium huge fluid pipe · 6 UIV circuit · 64 fine rhenium super composite alloy wire · 160 uepic chip · 4 320 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 5 000 mB calamatium · 2 500 mB tungsten disulfide</span><span class="gt-sub"><span>uiv machine hull</span><span>dense nyanium plate</span><span>chaotixic alloy gear</span><span>small nyanium gear</span><span>nyanium huge fluid pipe</span><span>UIV circuit</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nyinsane Plasma Turbine · 12 parallels (gtceu:nyinsane_plasma_turbine) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__nyinsane_plasma_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nyinsane Plasma Turbine</span><span class="gt-note">Nyinsane Plasma Turbine · 12 parallels</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 31 457 280 EU/t · research of the UEV holder 192 CWU/t](#m-al)
- [Assembly Line · 30 s · 15 728 640 EU/t · research Supreme Plasma Turbine 192 CWU/t](#m-a2)

### Direct steps

- UIV Rotor Holder → Nyinsane Plasma Turbine · 12 parallels (1)
- Plasma (magmatic, nickel, americium ...) from the tier 5 and tier 6 reactors → Nyinsane Plasma Turbine · 12 parallels (plasma)
- Per hour: 2500 B tungsten disulfide (+50 %) and 800 B BEC oganesson (+150 %) → Nyinsane Plasma Turbine · 12 parallels (boost)
- Nyinsane Plasma Turbine · 12 parallels → UIV 256A laser source hatch (uiv\_hatches) (EU)

## How to build

1. Holder parts first: hull, ohmderblux gears, UIV motors, small chaotixic gears, abyssal rounds, ring, transmissions, precision drive, circuit, field generator, xeproda wire. Drums: PEDOT:PSS, tungsten disulfide. — `functionalstorage:oak_1`, `gtceu:uiv_machine_hull`, `kubejs:uiv_transmission_assembly`
2. Research the UEV rotor holder, then 20 s per UIV holder at 31 457 280 EU/t. Output Keep Exact 2. — `gtceu:assembly_line`, `gtceu:uiv_rotor_holder`
3. Controller: 160 UEPIC chips and 6 UIV circuits in drawers; 30 s at 15 728 640 EU/t. Research the Supreme Plasma Turbine first. — `gtceu:assembly_line`, `gtceu:nyinsane_plasma_turbine`
4. Put the UIV holder in the turbine's rotor holder slot with a rotor; plasma in, plain gas out, both on Pipez fluid pipes. — `gtceu:nyinsane_plasma_turbine`, `gtceu:uiv_rotor_holder`
5. Boost drums: tungsten disulfide 2500 B and BEC oganesson 800 B per hour, each Keep Exact so the turbine never runs without lubricant. — `gtceu:bec_og_bucket`, `gtceu:tungsten_disulfide_bucket`
6. Output through the UIV 256A laser source hatch into the line. — `gtceu:uiv_256a_laser_source_hatch`

## Tips

- Verified from the pack lang file (assets/gtceu/lang/en\_us.json) and kjs systems/fusion/plasma\_turbines.js + startup more\_plasma\_turbine.js: the Nyinsane Plasma Turbine is the UIV boosted turbine (BoostedPlasmaTurbine tier UIV); up to 12x the parallels of a standard Large Plasma Turbine; lubricant boosting: 2500 B tungsten disulfide per hour for +50 % EU/t, skipping it costs -20 %; coolant boosting: 800 B oganesson stabilized Bose-Einstein condensate (BEC oganesson, uev\_chiller) per hour for +150 %, only while lubricant boosting is active; uses laser hatches. The base production line of the tooltip is not in the lang file for this machine (the Supreme says 16 384 EU/t; each rotor holder above IV doubles EU/t and adds 10 % efficiency): Unverified for the Nyinsane.
- UIV rotor holder: Assembly Line 400 ticks, VA\[UIV\] = 31 457 280 EU/t, station research of the UEV rotor holder (VA\[UEV\], 192 CWU/t): UIV hull + 4 ohmderblux gears + 2 UIV motors + 6 small chaotixic gears + 8 abyssal alloy rounds + 1 chaotixic ring + 2 UIV transmission assemblies + 1 UIV precision drive + 1 UIV circuit + 1 UIV field generator + 16 fine xeproda wire, 432 mB PEDOT:PSS + 10 000 mB tungsten disulfide. Nyinsane Plasma Turbine: 600 ticks, VHA\[UIV\], research Supreme Plasma Turbine (192 CWU/t): UIV hull + 6 dense nyanium plates + 4 chaotixic gears + 6 small nyanium gears + 8 nyanium huge fluid pipes + 6 UIV circuits + 64 fine rhenium super composite alloy wire + 160 UEPIC chips, 4320 mB PEDOT:PSS + 5000 mB calamatium + 2500 mB tungsten disulfide.
- Draco abyssal rotor (plasma\_turbines.js): turbine blade = assembler, 5 double draco abyssal plates + 8 draco abyssal foil + 2 draco abyssal screws + 720 mB void, 50 ticks, VHA\[UEV\]; rotor = Assembly Line, void frame + UIV transmission assembly + 8 blades + 16 fine rhenium super composite alloy wire, 15 000 mB tungsten disulfide + 1080 mB PEDOT:PSS, 600 ticks, VA\[UEV\], research Draco Abyssal Rotor (192 CWU/t). The same rotor goes 12 times into the Atomic Materialization Plant controller. Draco abyssal alloy is a Hell Forge recipe at VHA\[UXV\] (hellforge.js: 9 ingots, preon plasma, abyssal catalyst), so the best rotor is a UXV-priced item: Unverified whether another rotor material works in the holder.
- Fuel: the plasma\_generator recipes listed in uev\_power (nickel, iron, oxygen, nitrogen, argon, helium, americium, tin at -2048 EU/t base, magmatic at -8192 EU/t base returning infernal concentrate). Tier 6 plasma (paradox, voidic, preon) has no turbine recipe in the file: they are alloy inputs, not turbine fuel.
- Sub-steps people skip: (1) BEC oganesson is consumed here AND by the alloy chiller: size the oganesson loop (uev\_chiller) for both; (2) a turbine without lubricant loses 20 %: keep tungsten disulfide piped in; (3) 160 UEPIC chips per turbine = 80 wafers (uev\_chips); (4) the output is a laser source hatch: both ends need laser cables.
- **Unverified** Nyinsane base output, the effect of the rotor holder tier here, and plasma input rate.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:nyinsane_plasma_turbine` | 1 |
| `gtceu:uiv_rotor_holder` | 1 |
| `gtceu:uiv_256a_laser_source_hatch` | 1 |
| `gtceu:assembly_line` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:uiv_rotor_holder`, `gtceu:nyinsane_plasma_turbine`
