---
kind: chain
id: uhv_power
order: 1920
data:
  t: |-
    UHV power: UHV rotor holder + Supreme Plasma Turbine (Assembly Line) burning nickel / iron plasma (UV reactor) or americium plasma (tier-4 reflectors, UHV reactor) into a UHV dynamo hatch
  inf: true
  "n":
    - - g1
      - UHV hull · 4 zalloy gear · 2 UHV motor · 6 small neutronium gear · 8 zircalloy-4 round · neutronium ring · 2 transmission assembly · UHV circuit · 12 fine zirconium wire · 288 mB PEEK · 5 B lubricant
      - g
      - functionalstorage:oak_1
      - - [UHV Machine Hull, "gtceu:uhv_machine_hull"]
        - [Zalloy gear, "gtceu:zalloy_gear"]
        - [Small neutronium gear, "gtceu:small_neutronium_gear"]
        - [Transmission assembly, "kubejs:uhv_transmission_assembly"]
    - [a1, "Assembly Line · 20 s · 1 966 080 EU/t · research UV rotor holder 128 CWU/t", m, "gtceu:assembly_line"]
    - [rh, UHV Rotor Holder, x, "gtceu:uhv_rotor_holder"]
    - - g2
      - UHV hull · 6 dense enriched naquadah plate · 4 neutronium gear · 6 small naquadah alloy gear · 8 huge enriched naquadah pipe · 6 UHV circuit · 64 fine RTAN wire · 64 UHPIC · 4320 mB PEEK + 5 B naquadria + 2500 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [Dense enriched naquadah plate, "gtceu:dense_enriched_naquadah_plate"]
        - [Neutronium gear, "gtceu:neutronium_gear"]
        - [Huge enriched naquadah pipe, "gtceu:enriched_naquadah_huge_fluid_pipe"]
    - - a2
      - Assembly Line · 30 s · 983 040 EU/t · research Plasma Large Turbine 128 CWU/t
      - m
      - gtceu:assembly_line
    - [tb, Supreme Plasma Turbine, x, "gtceu:supreme_plasma_turbine"]
    - - pl
      - |-
        Plasma: nickel (UV reactor) · 180 ticks per mB at 2048 EU/t base · americium 984 ticks (needs tier-4 reflectors)
      - f
      - gtceu:nickel_plasma_bucket
    - [eu, "UHV Dynamo Hatch → UHV power line", o, "gtceu:uhv_energy_output_hatch"]
  e:
    - [g1, a1, "1"]
    - [a1, rh, "1 / 20 s"]
    - [g2, a2, "1"]
    - [a2, tb, "1 / 30 s"]
    - [rh, tb, "1"]
    - [pl, tb, plasma]
    - [tb, eu, EU]
  tips:
    - |-
      Source: kjs systems/fusion/plasma_turbines.js (verified). UHV rotor holder (Assembly Line, 400 ticks at VA[UHV], research of the UV rotor holder at 128 CWU/t and VA[UV]): UHV hull + 4 zalloy gears + 2 UHV motors + 6 small neutronium gears + 8 zircalloy-4 rounds + 1 neutronium ring + 2 UHV transmission assemblies + 1 UHV-tag circuit + 12 fine zirconium wire; 288 mB PEEK + 5000 mB lubricant. Supreme Plasma Turbine (Assembly Line, 600 ticks at VHA[UHV] = 983 040 EU/t, research of the Plasma Large Turbine at 128 CWU/t and VHA[UHV]): UHV hull + 6 dense enriched naquadah plates + 4 neutronium gears + 6 small naquadah alloy gears + 8 enriched naquadah huge fluid pipes + 6 UHV circuits + 64 fine RTAN wire + 64 UHPIC chips; 4320 mB PEEK + 5000 mB naquadria + 2500 mB lubricant.
    - |-
      Fuel table (plasma_generator recipes rewritten by the pack, EU/t base 2048, same for the Large Plasma Turbine): nickel 180 ticks per 1 mB, iron 135, tin 84, americium 984, magmatic plasma (EU/t 8192) 748 ticks per 1 mB → infernal concentrate (UEV), oxygen 98 / nitrogen 110 / argon 116 / helium 27 ticks per 5 mB. Americium plasma = 144 mB plutonium 238 + 3.5 B hydrogen, tier-4 reflectors, 98 304 EU/t, 15.6 s, start 760 MEU; it needs a reactor with a 760 MEU buffer (the UHV Fusion Reactor [AUX I] needs 4 UEV circuits and 96 UEPIC chips; the first UEV circuit needs no UEV machine, so AUX I is a late-UHV build, see uhv_multis and uhv_runic) → for the UHV era the fuel is nickel / iron plasma from the UV reactor (uv_power). Per 144 mB americium plasma: 984 x 2048 x 144 = 290 MEU of base energy.
    - |-
      What the UHV turbine adds: the Supreme controller replaces the Large Plasma Turbine structure with the UHV tier (hull, naquadah/neutronium parts) and requires the UHV rotor holder; the fuel recipes stay the same, the turbine multiplier is Unverified (read the controller tooltip). The UHV dynamo hatch (uhv_hatches: 4 europium springs instead of cables, research of the UV dynamo hatch) carries it out.
    - |-
      Dream-Link wireless power (wireless_power.js, verified): the Dream-Link Node is a UHV-tier item: Assembly Line EUtVHA(UHV) = 983 040 EU/t, 600 ticks, UV hull + 8 UHV circuits + 12 UV field generators + 8 UV emitters + 192 UHPIC chips, research active transformer 128 CWU/t. Later nodes: Oneiric Relay (UHV hull, 8 UEV circuits, 160 UEPIC, VHA[UEV]) and Daydream Spire (UEV hull, 8 UIV circuits, VHA[UIV]). Dream-Link energy hatches exist for UV, UHV, UEV and UIV at 2 / 4 / 16 / 64 / 256 A. Reach between dimensions is not documented in the scripts.
    - The Nyinsane Plasma Turbine (UIV) and the UEV / UIV rotor holders belong to later pages.
    - |-
      Sub-steps people skip: (1) 5 B naquadria for one controller: the naquadria line (zpm_naq_products) again; (2) RTAN fine wire 64 = 8 ingots; (3) the UHV rotor holder has two transmission assemblies (uhv_parts); (4) keep the old Large Plasma Turbine running until the Supreme one exists.
    - |-
      Unverified: Supreme turbine output multiplier and structure counts.
  b:
    - ["gtceu:supreme_plasma_turbine", 1]
    - ["gtceu:uhv_rotor_holder", 1]
    - ["gtceu:uhv_energy_output_hatch", 1]
    - ["gtceu:assembly_line", 2]
    - ["gtceu:research_station", 1]
    - ["gtceu:power_substation", 2]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 5]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:zalloy_gear
        - gtceu:small_neutronium_gear
        - gtceu:fine_ruthenium_trinium_americium_neutronate_wire
      t: |-
        Drawers first, one per input: hulls, gears (zalloy, neutronium, small naquadah), rounds, ring, transmission assemblies, plates, huge pipes, UHV circuits, RTAN fine wire, UHPIC chips. Drums: PEEK, lubricant, naquadria, plasma.
    - i: ["gtceu:research_station", "gtceu:uv_rotor_holder", "gtceu:data_module"]
      t: Research the UV rotor holder (128 CWU/t) and the Plasma Large Turbine (128 CWU/t at 983 040 EU/t) once each.
    - i: ["gtceu:assembly_line", "gtceu:uhv_rotor_holder"]
      t: |-
        Rotor holder: Assembly Line, 20 s at 1 966 080 EU/t (UV 4A hatch).
    - i: ["gtceu:assembly_line", "gtceu:supreme_plasma_turbine"]
      t: "Turbine controller: Assembly Line, 30 s at 983 040 EU/t."
    - i: ["gtceu:supreme_plasma_turbine", "gtceu:uhv_energy_output_hatch", "gtceu:nickel_plasma_bucket"]
      t: |-
        Run: plasma into the input hatch, spent fluid out, dynamo hatch to the Power Substation.
    - i: ["start_core:uv_fusion_reactor", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: nickel plasma comes from the UV reactor (uv_power): size fluorine and potassium first.
---
# UHV power: UHV rotor holder + Supreme Plasma Turbine (Assembly Line) burning nickel / iron plasma (UV reactor) or americium plasma (tier-4 reflectors, UHV reactor) into a UHV dynamo hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_power` · **Tags:** Infinite source, Unverified

**Plan modules:** [Akreyrium refining, UHV controllers](../../plan/p17.md#uhvmulti)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 1 966 080 EU/t · research UV rotor holder 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 4 zalloy gear · 2 UHV motor · 6 small neutronium gear · 8 zircalloy-4 round · neutronium ring · 2 transmission assembly · UHV circuit · 12 fine zirconium wire · 288 mB PEEK · 5 B lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 4 zalloy gear · 2 UHV motor · 6 small neutronium gear · 8 zircalloy-4 round · neutronium ring · 2 transmission assembly · UHV circuit · 12 fine zirconium wire · 288 mB PEEK · 5 B lubricant</span><span class="gt-sub"><span>UHV Machine Hull</span><span>Zalloy gear</span><span>Small neutronium gear</span><span>Transmission assembly</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Rotor Holder (gtceu:uhv_rotor_holder) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Rotor Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 983 040 EU/t · research Plasma Large Turbine 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 6 dense enriched naquadah plate · 4 neutronium gear · 6 small naquadah alloy gear · 8 huge enriched naquadah pipe · 6 UHV circuit · 64 fine RTAN wire · 64 UHPIC · 4320 mB PEEK + 5 B naquadria + 2500 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 6 dense enriched naquadah plate · 4 neutronium gear · 6 small naquadah alloy gear · 8 huge enriched naquadah pipe · 6 UHV circuit · 64 fine RTAN wire · 64 UHPIC · 4320 mB PEEK + 5 B naquadria + 2500 mB lubricant</span><span class="gt-sub"><span>Dense enriched naquadah plate</span><span>Neutronium gear</span><span>Huge enriched naquadah pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Supreme Plasma Turbine (gtceu:supreme_plasma_turbine) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__supreme_plasma_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Supreme Plasma Turbine</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 1 966 080 EU/t · research UV rotor holder 128 CWU/t](#m-a1)
- [Assembly Line · 30 s · 983 040 EU/t · research Plasma Large Turbine 128 CWU/t](#m-a2)

### Direct steps

- UHV Rotor Holder → Supreme Plasma Turbine (1)
- Plasma: nickel (UV reactor) · 180 ticks per mB at 2048 EU/t base · americium 984 ticks (needs tier-4 reflectors) → Supreme Plasma Turbine (plasma)
- Supreme Plasma Turbine → UHV Dynamo Hatch → UHV power line (EU)

## How to build

1. Drawers first, one per input: hulls, gears (zalloy, neutronium, small naquadah), rounds, ring, transmission assemblies, plates, huge pipes, UHV circuits, RTAN fine wire, UHPIC chips. Drums: PEEK, lubricant, naquadria, plasma. — `functionalstorage:oak_1`, `gtceu:zalloy_gear`, `gtceu:small_neutronium_gear`, `gtceu:fine_ruthenium_trinium_americium_neutronate_wire`
2. Research the UV rotor holder (128 CWU/t) and the Plasma Large Turbine (128 CWU/t at 983 040 EU/t) once each. — `gtceu:research_station`, `gtceu:uv_rotor_holder`, `gtceu:data_module`
3. Rotor holder: Assembly Line, 20 s at 1 966 080 EU/t (UV 4A hatch). — `gtceu:assembly_line`, `gtceu:uhv_rotor_holder`
4. Turbine controller: Assembly Line, 30 s at 983 040 EU/t. — `gtceu:assembly_line`, `gtceu:supreme_plasma_turbine`
5. Run: plasma into the input hatch, spent fluid out, dynamo hatch to the Power Substation. — `gtceu:supreme_plasma_turbine`, `gtceu:uhv_energy_output_hatch`, `gtceu:nickel_plasma_bucket`
6. Easy to miss: nickel plasma comes from the UV reactor (uv\_power): size fluorine and potassium first. — `start_core:uv_fusion_reactor`, `functionalstorage:oak_1`

## Tips

- Source: kjs systems/fusion/plasma\_turbines.js (verified). UHV rotor holder (Assembly Line, 400 ticks at VA\[UHV\], research of the UV rotor holder at 128 CWU/t and VA\[UV\]): UHV hull + 4 zalloy gears + 2 UHV motors + 6 small neutronium gears + 8 zircalloy-4 rounds + 1 neutronium ring + 2 UHV transmission assemblies + 1 UHV-tag circuit + 12 fine zirconium wire; 288 mB PEEK + 5000 mB lubricant. Supreme Plasma Turbine (Assembly Line, 600 ticks at VHA\[UHV\] = 983 040 EU/t, research of the Plasma Large Turbine at 128 CWU/t and VHA\[UHV\]): UHV hull + 6 dense enriched naquadah plates + 4 neutronium gears + 6 small naquadah alloy gears + 8 enriched naquadah huge fluid pipes + 6 UHV circuits + 64 fine RTAN wire + 64 UHPIC chips; 4320 mB PEEK + 5000 mB naquadria + 2500 mB lubricant.
- Fuel table (plasma\_generator recipes rewritten by the pack, EU/t base 2048, same for the Large Plasma Turbine): nickel 180 ticks per 1 mB, iron 135, tin 84, americium 984, magmatic plasma (EU/t 8192) 748 ticks per 1 mB → infernal concentrate (UEV), oxygen 98 / nitrogen 110 / argon 116 / helium 27 ticks per 5 mB. Americium plasma = 144 mB plutonium 238 + 3.5 B hydrogen, tier-4 reflectors, 98 304 EU/t, 15.6 s, start 760 MEU; it needs a reactor with a 760 MEU buffer (the UHV Fusion Reactor \[AUX I\] needs 4 UEV circuits and 96 UEPIC chips; the first UEV circuit needs no UEV machine, so AUX I is a late-UHV build, see uhv\_multis and uhv\_runic) → for the UHV era the fuel is nickel / iron plasma from the UV reactor (uv\_power). Per 144 mB americium plasma: 984 x 2048 x 144 = 290 MEU of base energy.
- What the UHV turbine adds: the Supreme controller replaces the Large Plasma Turbine structure with the UHV tier (hull, naquadah/neutronium parts) and requires the UHV rotor holder; the fuel recipes stay the same, the turbine multiplier is Unverified (read the controller tooltip). The UHV dynamo hatch (uhv\_hatches: 4 europium springs instead of cables, research of the UV dynamo hatch) carries it out.
- Dream-Link wireless power (wireless\_power.js, verified): the Dream-Link Node is a UHV-tier item: Assembly Line EUtVHA(UHV) = 983 040 EU/t, 600 ticks, UV hull + 8 UHV circuits + 12 UV field generators + 8 UV emitters + 192 UHPIC chips, research active transformer 128 CWU/t. Later nodes: Oneiric Relay (UHV hull, 8 UEV circuits, 160 UEPIC, VHA\[UEV\]) and Daydream Spire (UEV hull, 8 UIV circuits, VHA\[UIV\]). Dream-Link energy hatches exist for UV, UHV, UEV and UIV at 2 / 4 / 16 / 64 / 256 A. Reach between dimensions is not documented in the scripts.
- The Nyinsane Plasma Turbine (UIV) and the UEV / UIV rotor holders belong to later pages.
- Sub-steps people skip: (1) 5 B naquadria for one controller: the naquadria line (zpm\_naq\_products) again; (2) RTAN fine wire 64 = 8 ingots; (3) the UHV rotor holder has two transmission assemblies (uhv\_parts); (4) keep the old Large Plasma Turbine running until the Supreme one exists.
- **Unverified** Supreme turbine output multiplier and structure counts.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:supreme_plasma_turbine` | 1 |
| `gtceu:uhv_rotor_holder` | 1 |
| `gtceu:uhv_energy_output_hatch` | 1 |
| `gtceu:assembly_line` | 2 |
| `gtceu:research_station` | 1 |
| `gtceu:power_substation` | 2 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `gtceu:supreme_plasma_turbine`, `gtceu:uhv_rotor_holder`
