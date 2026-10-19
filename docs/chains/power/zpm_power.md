---
kind: chain
id: zpm_power
order: 1530
data:
  t: |-
    ZPM power: deuterium + tritium → helium plasma (MK I fusion) → Large Plasma Turbine with a ZPM rotor holder → ZPM dynamo hatch
  inf: true
  "n":
    - - dt
      - "1 B deuterium + 1 B tritium"
      - g
      - functionalstorage:oak_1
      - [[Deuterium, "gtceu:deuterium_bucket"], [Tritium, "gtceu:tritium_bucket"]]
    - - fr
      - LuV Fusion Reactor · 7.2 s · 4096 EU/t · start 40 MEU · reflector tier 1
      - m
      - start_core:luv_fusion_reactor
    - [hp, "1 B helium plasma", x, "gtceu:helium_plasma_bucket"]
    - - rg
      - ZPM hull · 4 trinium gear · ZPM motor · 4 small osthendah gear · 6 osmiridium round · osthendah ring · 8 fine europium wire · 144 mB PBI
      - g
      - functionalstorage:oak_1
      - - [ZPM Machine Hull, "gtceu:zpm_machine_hull"]
        - [Trinium gear, "gtceu:trinium_gear"]
        - [ZPM motor, "gtceu:zpm_electric_motor"]
        - [Small osthendah gear, "gtceu:small_osthendah_gear"]
    - [ra, "Assembler · circuit 3 · 5 s · ZPM power", m, "gtceu:large_assembler"]
    - [rh, ZPM Rotor Holder, x, "gtceu:zpm_rotor_holder"]
    - - tg
      - |-
        Controller: LuV hull + 2 LuV circuit + 4 tungsten steel gear + 2 large tungsten steel pipe (crafting table)
      - g
      - functionalstorage:oak_1
      - - [LuV Machine Hull, "gtceu:luv_machine_hull"]
        - [Tungsten steel gear, "gtceu:tungsten_steel_gear"]
        - [Nanoprocessor mainframe, "gtceu:nano_processor_mainframe"]
    - - tb
      - Large Plasma Turbine + rotor + dynamo hatch (5 mB helium plasma / 27 ticks or argon plasma / 116 ticks, base 2048 EU/t)
      - m
      - gtceu:plasma_large_turbine
    - [eu, "ZPM Dynamo Hatch → ZPM power line", o, "gtceu:zpm_energy_output_hatch"]
    - - ci
      - "144 mB carbon + 144 mB magnesium (argon route)"
      - g
      - functionalstorage:oak_1
      - [[Carbon dust, "gtceu:carbon_dust"], [Magnesium, "gtceu:magnesium_bucket"]]
    - - fa
      - ZPM Fusion Reactor (MK II) · 7.2 s · 24 576 EU/t · start 180 MEU · reflector tier 2
      - m
      - start_core:zpm_fusion_reactor
    - [ap, "1 B argon plasma", x, "gtceu:argon_plasma_bucket"]
  e:
    - [dt, fr, "1 + 1 B"]
    - [fr, hp, "1 B / 7.2 s"]
    - [hp, tb, "5 mB / 27 ticks"]
    - [rg, ra, "1"]
    - [ra, rh, "1 / 5 s"]
    - [rh, tb, "1"]
    - [tg, tb, controller]
    - [tb, eu, EU]
    - [ci, fa, "144 + 144 mB"]
    - [fa, ap, "1 B / 7.2 s"]
    - [ap, tb, "5 mB / 116 ticks"]
  tips:
    - |-
      Fuel (kjs systems/fusion/fusion_scaling.js + plasma_turbines.js): the MK I reactor makes 1000 mB helium plasma from 1000 mB deuterium + 1000 mB tritium in 7.2 s at 4096 EU/t, start energy 40 MEU, reflector tier 1. The pack replaces every plasma_generator recipe: helium plasma is burned in 5 mB batches, 27 ticks each, at 2048 EU/t base (other fuels: oxygen 98, nitrogen 110, argon 116, iron 135, nickel 180, tin 84 and americium 984 ticks per batch; oxygen, nitrogen, argon and helium in 5 mB batches, the metals in 1 mB). So 1000 mB helium plasma = 200 batches x 27 ticks x 2048 EU/t = about 11 MEU of base turbine output against 0.6 MEU of reactor power: roughly 18 to 1 before efficiency, plus the 40 MEU start buffer (Unverified how fast it drains when the reactor idles). The 2048 EU/t is only the recipe base; the real output per turbine follows the holder tier and rotor power formula in the tips below.
    - |-
      Argon plasma (fusion_scaling.js, verified): 144 mB carbon + 144 mB magnesium -> 1000 mB argon plasma, 24 576 EU/t, 7.2 s (144 ticks), start 180 MEU, reflector tier 2. It needs the MK II reactor (zpm_fusion): the MK I buffer caps at 160 MEU, below the 180 MEU start, and the MK II holds 320 MEU. 24 576 EU/t fits a LuV or ZPM hatch. Turbine side (plasma_turbines.js): argon burns in 5 mB batches of 116 ticks at 2048 EU/t = 47 514 EU per mB, helium (27 ticks) only 11 059 EU per mB. Net per 1000 mB of plasma: argon about 44.0 MEU (47.5 MEU minus 3.5 MEU of reactor power), helium about 10.5 MEU, so argon is about 4.2 times better per mB and per reactor-second, and it spends carbon and magnesium instead of deuterium and tritium.
    - |-
      Carbon for argon: electrolyzer (LV, 768 ticks) 1 diamond dust -> 64 carbon dust (SeparationRecipes diamond_electrolysis, not removed by the pack). Diamonds come from the sieves (7.5 % in the sieve table) and from the Rock Filtrator diamond geode (lv_geodes: 32 gravel + 1000 mB distilled water -> diamond geode 35 %, then cutter or macerator -> raw diamond / crushed diamond ore). Unverified: how the liquid carbon (gtceu:carbon) that the fusion recipe takes is made from carbon dust.
    - |-
      Real turbine output (formula from the fork jar, verified): Large Plasma Turbine (tier IV) output = 16 384 EU/t x (2^(holder tier - IV) x rotor power %) / 100 at full speed. A ZPM holder is two tiers above IV (x4) and a prismalium rotor has power 1600 (rotorStats in superconductors.js), so one turbine makes 16 384 x 4 x 1600 / 100 = 1 048 576 EU/t. 96 such turbines would be about 100 M EU/t, not the 400 MFE/t that has been quoted; that figure does not follow from the jar data, so do not plan with it. The real limit is the fuel: 50 MK II reactors make 50 x 6.94 mB/tick = 347 mB/tick of argon plasma = about 16.5 M EU/t raw, and each reflector overclock step above the recipe tier doubles that flow. A ZPM 16A dynamo (2.1 M EU/t) is not the cap.
    - |-
      Controller (MetaTileEntityLoader large_plasma_turbine, registerLargeTurbine tier IV, shaped): 2 LuV circuits + 4 tungsten steel gears + 1 LuV Machine Hull + 2 large tungsten steel fluid pipes; the pack removes every rotor holder recipe and re-adds them (plasma_turbines.js): LuV = LuV hull + 4 HSS-S gears + LuV motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 rhodium plated palladium ring + 288 mB PTFE (circuit 3, 100 ticks, VHA[LuV]); ZPM = ZPM hull + 4 trinium gears + ZPM motor + 4 small osthendah gears + 6 osmiridium rounds + 1 osthendah ring + 8 fine europium wire + 144 mB PBI (circuit 3, 100 ticks, VHA[ZPM]). Build the LuV holder first: it is enough for the turbine’s own tier; the ZPM holder is the upgrade once ZPM motors exist. Structure (tungsten steel turbine casings, tungstensteel gearbox blocks, the holder, dynamo/energy output hatch): Unverified counts.
    - |-
      Where deuterium and tritium come from: distillation of liquid ender air (200 B → 50 B deuterium + 10 B tritium + others, IV Distillation Tower, DistillationRecipes) or the Exotic Gas Siphon in the End (50 B deuterium + 10 B tritium per run) or Abydos (9 B deuterium + 4.5 B tritium per run), VA[ZPM]; deuterium also from the hydrogen electrolysis chain (earlier eras, Unverified). Tritium is the scarce one: 1 B per 11 MEU, so the reactor, not the turbine, is the limit.
    - |-
      ZPM dynamo hatch (zpm_hatches): ZPM hull + 4 vanadium gallium springs + 2 UHPIC chips + ZPM circuit + 2 voltage coils + 8 B sodium potassium + 1440 mB solder, station research of the LuV dynamo hatch, 8 CWU/t. Until it exists, a LuV dynamo hatch (30 720 EU/t) on the turbine caps the output; a 4A or laser dynamo would need more. The cables after it: dragonsteel superconductor (zpm_urd) or the tier cables.
    - |-
      Alternative power, modular combustion (kjs additions/progression/power/modular_combustion.js, verified): the Modular Combustion Frame [MCF] is an Assembly Line recipe (LuV hull + 2 LuV circuits + lapotronic orb cluster + LuV emitter, sensor and regulator, VHA[LuV], research iridium frame) and holds up to 8 modules. Supreme Combustion Module [SCM]: ZPM hull + 6 ZPM circuits, VHA[ZPM], research = the Unreal Combustion Module (24 CWU/t); base V[ZPM] = 131 072 EU/t per module, up to V[ZPM] x 6 = 786 432 EU/t with red fuming nitric acid (120 mB/s, double fuel use). Supreme Rocket Module [SRM]: 8 UV circuits + 6 UV regulators, VHA[UV], research = the SCM (64 CWU/t); up to V[UV] x 8 = 4 194 304 EU/t per module at 200 mB/s. Frame coolant: distilled water +20 %, deionized water +40 %, none -10 % (500 B/h per module). Oxidizer tiers (WFNA, RFNA, dioxygen difluoride, ferrocenium superoxide) multiply by 5 / 6 / 8 / 12. Theoretical maximum with 8 modules: SCM about 6.3 M EU/t, SRM about 33.6 M EU/t. The player figures of 288 A (SCM) and 384 A (SRM) are exactly 6x these maxima and cannot be reproduced from the jar data: treat them as unverified; only the 6:8 ratio matches the multipliers.
    - |-
      Compared with the other eras: the Power Substation (luv_power) buffers the MK I/II start energy and the stargate dialing; the turbine fills it. The quest page ‘ZPM Power’ is just a checkmark; the in-game gate wants far more energy than the turbine alone (quest: an immense amount of power), so size for substation capacitors.
    - |-
      Sub-steps people skip: (1) fusion output and turbine input must match: a pipe with a pump cover from the reactor’s output hatch to the turbine’s fluid input; the helium returns to a drum; (2) the reactor needs its start energy once, a drained substation stops it; (3) the rotor: any GT turbine rotor fits and its power stat is a direct multiplier (prismalium rotor 1600 %); (4) the Large Plasma Turbine is a LuV-hull machine: the controller waits on the LuV hull line and 2 LuV circuits only.
    - |-
      Unverified: the deuterium electrolysis, the liquid carbon source and the structure counts.
  b:
    - ["gtceu:plasma_large_turbine", 1]
    - ["gtceu:zpm_rotor_holder", 1]
    - ["start_core:luv_fusion_reactor", 1]
    - ["gtceu:zpm_energy_output_hatch", 1]
    - ["gtceu:power_substation", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:deuterium_bucket", "gtceu:tritium_bucket"]
      t: |-
        Drums first: deuterium, tritium, helium plasma, returned helium. Each machine on its own Pipez fluid pipe from its drum with a pump cover; Keep Exact on the plasma drum so a full turbine does not stall the reactor.
    - i: ["start_core:luv_fusion_reactor", "gtceu:helium_plasma_bucket"]
      t: |-
        Reactor: the MK I reactor with reflector tier 1: 1 B deuterium + 1 B tritium → 1 B helium plasma every 7.2 s at 4096 EU/t, start energy 40 MEU from the Power Substation. It shares the reactor with the europium recipe (switch via input hatches) or use a second MK I.
    - i: ["gtceu:large_assembler", "gtceu:zpm_rotor_holder", "gtceu:zpm_electric_motor"]
      t: |-
        Rotor holder: ghost circuit 3, ZPM hull + 4 trinium gears + ZPM motor + 4 small osthendah gears + 6 osmiridium rounds + osthendah ring + 8 fine europium wire + 144 mB PBI → holder in 5 s (the LuV one first). Output drawer Keep Exact 2.
    - i: ["gtceu:plasma_large_turbine", "gtceu:luv_machine_hull", "gtceu:tungsten_steel_gear"]
      t: |-
        Controller: crafting table, 2 LuV circuits (P), 4 tungsten steel gears (S), the LuV hull (A) and 2 large tungsten steel pipes (C). Then the structure and the rotor in the holder.
    - i: ["gtceu:plasma_large_turbine", "gtceu:zpm_energy_output_hatch", "gtceu:helium_plasma_bucket"]
      t: |-
        Run: helium plasma into the turbine’s fluid input, helium out to a drum, EU out through the dynamo hatch into the line. Output per turbine follows the formula in the tips (1 048 576 EU/t with a ZPM holder and a prismalium rotor); check the tooltip for your rotor.
    - i: ["functionalstorage:oak_1", "gtceu:tritium_bucket"]
      t: |-
        Easy to miss: tritium is the limiting input; count tritium per hour from your siphon or distillation line before you plan the turbines. Switch to argon plasma (carbon + magnesium, no tritium, about 4 times the energy per mB) if tritium is short.
---
# ZPM power: deuterium + tritium → helium plasma (MK I fusion) → Large Plasma Turbine with a ZPM rotor holder → ZPM dynamo hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_power` · **Tags:** Infinite source, Unverified

**Plan modules:** [Fusion MK I (europium) and plasma power](../../plan/p12.md#fusion1)

**Tips:** 11, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-luv" id="m-fr">
<div class="gt-head"><span class="gt-mname">LuV Fusion Reactor · 7.2 s · 4096 EU/t · start 40 MEU · reflector tier 1</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 B deuterium + 1 B tritium (functionalstorage:oak_1) - 1 + 1 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 B deuterium + 1 B tritium</span><span class="gt-sub"><span>Deuterium</span><span>Tritium</span></span><b class="gt-q">1 + 1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__luv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">7.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="1 B helium plasma (gtceu:helium_plasma_bucket) - 1 B / 7.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__helium_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium Plasma Bucket</span><span class="gt-note">1 B helium plasma</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>start_core:luv_fusion_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-ra">
<div class="gt-head"><span class="gt-mname">Assembler · circuit 3 · 5 s · ZPM power</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 4 trinium gear · ZPM motor · 4 small osthendah gear · 6 osmiridium round · osthendah ring · 8 fine europium wire · 144 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 4 trinium gear · ZPM motor · 4 small osthendah gear · 6 osmiridium round · osthendah ring · 8 fine europium wire · 144 mB PBI</span><span class="gt-sub"><span>ZPM Machine Hull</span><span>Trinium gear</span><span>ZPM motor</span><span>Small osthendah gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Rotor Holder (gtceu:zpm_rotor_holder) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Rotor Holder</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-tb">
<div class="gt-head"><span class="gt-mname">Large Plasma Turbine + rotor + dynamo hatch (5 mB helium plasma / 27 ticks or argon plasma / 116 ticks, base 2048 EU/t)</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 B helium plasma (gtceu:helium_plasma_bucket) - 5 mB / 27 ticks"><img class="gt-ico" src="../../assets/icons/gtceu__helium_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium Plasma Bucket</span><span class="gt-note">1 B helium plasma</span><b class="gt-q">5 mB</b></span><span class="gt-slot" title="ZPM Rotor Holder (gtceu:zpm_rotor_holder) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_rotor_holder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Rotor Holder</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Controller: LuV hull + 2 LuV circuit + 4 tungsten steel gear + 2 large tungsten steel pipe (crafting table) (functionalstorage:oak_1) - controller"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Controller: LuV hull + 2 LuV circuit + 4 tungsten steel gear + 2 large tungsten steel pipe (crafting table)</span><span class="gt-sub"><span>LuV Machine Hull</span><span>Tungsten steel gear</span><span>Nanoprocessor mainframe</span></span><b class="gt-q">controller</b></span><span class="gt-slot" title="1 B argon plasma (gtceu:argon_plasma_bucket) - 5 mB / 116 ticks"><img class="gt-ico" src="../../assets/icons/gtceu__argon_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Argon Plasma Bucket</span><span class="gt-note">1 B argon plasma</span><b class="gt-q">5 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__plasma_large_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">27 ticks · 116 ticks</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Dynamo Hatch → ZPM power line (gtceu:zpm_energy_output_hatch) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Energy Output Hatch</span><span class="gt-note">ZPM Dynamo Hatch → ZPM power line</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:plasma_large_turbine</code></div>
</div>
<div class="gt-panel t-zpm" id="m-fa">
<div class="gt-head"><span class="gt-mname">ZPM Fusion Reactor (MK II) · 7.2 s · 24 576 EU/t · start 180 MEU · reflector tier 2</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="144 mB carbon + 144 mB magnesium (argon route) (functionalstorage:oak_1) - 144 + 144 mB"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">144 mB carbon + 144 mB magnesium (argon route)</span><span class="gt-sub"><span>Carbon dust</span><span>Magnesium</span></span><b class="gt-q">144 + 144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">7.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="1 B argon plasma (gtceu:argon_plasma_bucket) - 1 B / 7.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__argon_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Argon Plasma Bucket</span><span class="gt-note">1 B argon plasma</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
</div>

## Flow

- [LuV Fusion Reactor · 7.2 s · 4096 EU/t · start 40 MEU · reflector tier 1](#m-fr) → [Large Plasma Turbine + rotor + dynamo hatch (5 mB helium plasma / 27 ticks or argon plasma / 116 ticks, base 2048 EU/t)](#m-tb)
- [Assembler · circuit 3 · 5 s · ZPM power](#m-ra) → [Large Plasma Turbine + rotor + dynamo hatch (5 mB helium plasma / 27 ticks or argon plasma / 116 ticks, base 2048 EU/t)](#m-tb)
- [ZPM Fusion Reactor (MK II) · 7.2 s · 24 576 EU/t · start 180 MEU · reflector tier 2](#m-fa) → [Large Plasma Turbine + rotor + dynamo hatch (5 mB helium plasma / 27 ticks or argon plasma / 116 ticks, base 2048 EU/t)](#m-tb)

## How to build

1. Drums first: deuterium, tritium, helium plasma, returned helium. Each machine on its own Pipez fluid pipe from its drum with a pump cover; Keep Exact on the plasma drum so a full turbine does not stall the reactor. — `functionalstorage:oak_1`, `gtceu:deuterium_bucket`, `gtceu:tritium_bucket`
2. Reactor: the MK I reactor with reflector tier 1: 1 B deuterium + 1 B tritium → 1 B helium plasma every 7.2 s at 4096 EU/t, start energy 40 MEU from the Power Substation. It shares the reactor with the europium recipe (switch via input hatches) or use a second MK I. — `start_core:luv_fusion_reactor`, `gtceu:helium_plasma_bucket`
3. Rotor holder: ghost circuit 3, ZPM hull + 4 trinium gears + ZPM motor + 4 small osthendah gears + 6 osmiridium rounds + osthendah ring + 8 fine europium wire + 144 mB PBI → holder in 5 s (the LuV one first). Output drawer Keep Exact 2. — `gtceu:large_assembler`, `gtceu:zpm_rotor_holder`, `gtceu:zpm_electric_motor`
4. Controller: crafting table, 2 LuV circuits (P), 4 tungsten steel gears (S), the LuV hull (A) and 2 large tungsten steel pipes (C). Then the structure and the rotor in the holder. — `gtceu:plasma_large_turbine`, `gtceu:luv_machine_hull`, `gtceu:tungsten_steel_gear`
5. Run: helium plasma into the turbine’s fluid input, helium out to a drum, EU out through the dynamo hatch into the line. Output per turbine follows the formula in the tips (1 048 576 EU/t with a ZPM holder and a prismalium rotor); check the tooltip for your rotor. — `gtceu:plasma_large_turbine`, `gtceu:zpm_energy_output_hatch`, `gtceu:helium_plasma_bucket`
6. Easy to miss: tritium is the limiting input; count tritium per hour from your siphon or distillation line before you plan the turbines. Switch to argon plasma (carbon + magnesium, no tritium, about 4 times the energy per mB) if tritium is short. — `functionalstorage:oak_1`, `gtceu:tritium_bucket`

## Tips

- Fuel (kjs systems/fusion/fusion\_scaling.js + plasma\_turbines.js): the MK I reactor makes 1000 mB helium plasma from 1000 mB deuterium + 1000 mB tritium in 7.2 s at 4096 EU/t, start energy 40 MEU, reflector tier 1. The pack replaces every plasma\_generator recipe: helium plasma is burned in 5 mB batches, 27 ticks each, at 2048 EU/t base (other fuels: oxygen 98, nitrogen 110, argon 116, iron 135, nickel 180, tin 84 and americium 984 ticks per batch; oxygen, nitrogen, argon and helium in 5 mB batches, the metals in 1 mB). So 1000 mB helium plasma = 200 batches x 27 ticks x 2048 EU/t = about 11 MEU of base turbine output against 0.6 MEU of reactor power: roughly 18 to 1 before efficiency, plus the 40 MEU start buffer (Unverified how fast it drains when the reactor idles). The 2048 EU/t is only the recipe base; the real output per turbine follows the holder tier and rotor power formula in the tips below.
- Argon plasma (fusion\_scaling.js, verified): 144 mB carbon + 144 mB magnesium -&gt; 1000 mB argon plasma, 24 576 EU/t, 7.2 s (144 ticks), start 180 MEU, reflector tier 2. It needs the MK II reactor (zpm\_fusion): the MK I buffer caps at 160 MEU, below the 180 MEU start, and the MK II holds 320 MEU. 24 576 EU/t fits a LuV or ZPM hatch. Turbine side (plasma\_turbines.js): argon burns in 5 mB batches of 116 ticks at 2048 EU/t = 47 514 EU per mB, helium (27 ticks) only 11 059 EU per mB. Net per 1000 mB of plasma: argon about 44.0 MEU (47.5 MEU minus 3.5 MEU of reactor power), helium about 10.5 MEU, so argon is about 4.2 times better per mB and per reactor-second, and it spends carbon and magnesium instead of deuterium and tritium.
- Carbon for argon: electrolyzer (LV, 768 ticks) 1 diamond dust -&gt; 64 carbon dust (SeparationRecipes diamond\_electrolysis, not removed by the pack). Diamonds come from the sieves (7.5 % in the sieve table) and from the Rock Filtrator diamond geode (lv\_geodes: 32 gravel + 1000 mB distilled water -&gt; diamond geode 35 %, then cutter or macerator -&gt; raw diamond / crushed diamond ore). Unverified: how the liquid carbon (gtceu:carbon) that the fusion recipe takes is made from carbon dust.
- Real turbine output (formula from the fork jar, verified): Large Plasma Turbine (tier IV) output = 16 384 EU/t x (2^(holder tier - IV) x rotor power %) / 100 at full speed. A ZPM holder is two tiers above IV (x4) and a prismalium rotor has power 1600 (rotorStats in superconductors.js), so one turbine makes 16 384 x 4 x 1600 / 100 = 1 048 576 EU/t. 96 such turbines would be about 100 M EU/t, not the 400 MFE/t that has been quoted; that figure does not follow from the jar data, so do not plan with it. The real limit is the fuel: 50 MK II reactors make 50 x 6.94 mB/tick = 347 mB/tick of argon plasma = about 16.5 M EU/t raw, and each reflector overclock step above the recipe tier doubles that flow. A ZPM 16A dynamo (2.1 M EU/t) is not the cap.
- Controller (MetaTileEntityLoader large\_plasma\_turbine, registerLargeTurbine tier IV, shaped): 2 LuV circuits + 4 tungsten steel gears + 1 LuV Machine Hull + 2 large tungsten steel fluid pipes; the pack removes every rotor holder recipe and re-adds them (plasma\_turbines.js): LuV = LuV hull + 4 HSS-S gears + LuV motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 rhodium plated palladium ring + 288 mB PTFE (circuit 3, 100 ticks, VHA\[LuV\]); ZPM = ZPM hull + 4 trinium gears + ZPM motor + 4 small osthendah gears + 6 osmiridium rounds + 1 osthendah ring + 8 fine europium wire + 144 mB PBI (circuit 3, 100 ticks, VHA\[ZPM\]). Build the LuV holder first: it is enough for the turbine’s own tier; the ZPM holder is the upgrade once ZPM motors exist. Structure (tungsten steel turbine casings, tungstensteel gearbox blocks, the holder, dynamo/energy output hatch): Unverified counts.
- Where deuterium and tritium come from: distillation of liquid ender air (200 B → 50 B deuterium + 10 B tritium + others, IV Distillation Tower, DistillationRecipes) or the Exotic Gas Siphon in the End (50 B deuterium + 10 B tritium per run) or Abydos (9 B deuterium + 4.5 B tritium per run), VA\[ZPM\]; deuterium also from the hydrogen electrolysis chain (earlier eras, Unverified). Tritium is the scarce one: 1 B per 11 MEU, so the reactor, not the turbine, is the limit.
- ZPM dynamo hatch (zpm\_hatches): ZPM hull + 4 vanadium gallium springs + 2 UHPIC chips + ZPM circuit + 2 voltage coils + 8 B sodium potassium + 1440 mB solder, station research of the LuV dynamo hatch, 8 CWU/t. Until it exists, a LuV dynamo hatch (30 720 EU/t) on the turbine caps the output; a 4A or laser dynamo would need more. The cables after it: dragonsteel superconductor (zpm\_urd) or the tier cables.
- Alternative power, modular combustion (kjs additions/progression/power/modular\_combustion.js, verified): the Modular Combustion Frame \[MCF\] is an Assembly Line recipe (LuV hull + 2 LuV circuits + lapotronic orb cluster + LuV emitter, sensor and regulator, VHA\[LuV\], research iridium frame) and holds up to 8 modules. Supreme Combustion Module \[SCM\]: ZPM hull + 6 ZPM circuits, VHA\[ZPM\], research = the Unreal Combustion Module (24 CWU/t); base V\[ZPM\] = 131 072 EU/t per module, up to V\[ZPM\] x 6 = 786 432 EU/t with red fuming nitric acid (120 mB/s, double fuel use). Supreme Rocket Module \[SRM\]: 8 UV circuits + 6 UV regulators, VHA\[UV\], research = the SCM (64 CWU/t); up to V\[UV\] x 8 = 4 194 304 EU/t per module at 200 mB/s. Frame coolant: distilled water +20 %, deionized water +40 %, none -10 % (500 B/h per module). Oxidizer tiers (WFNA, RFNA, dioxygen difluoride, ferrocenium superoxide) multiply by 5 / 6 / 8 / 12. Theoretical maximum with 8 modules: SCM about 6.3 M EU/t, SRM about 33.6 M EU/t. The player figures of 288 A (SCM) and 384 A (SRM) are exactly 6x these maxima and cannot be reproduced from the jar data: treat them as unverified; only the 6:8 ratio matches the multipliers.
- Compared with the other eras: the Power Substation (luv\_power) buffers the MK I/II start energy and the stargate dialing; the turbine fills it. The quest page ‘ZPM Power’ is just a checkmark; the in-game gate wants far more energy than the turbine alone (quest: an immense amount of power), so size for substation capacitors.
- Sub-steps people skip: (1) fusion output and turbine input must match: a pipe with a pump cover from the reactor’s output hatch to the turbine’s fluid input; the helium returns to a drum; (2) the reactor needs its start energy once, a drained substation stops it; (3) the rotor: any GT turbine rotor fits and its power stat is a direct multiplier (prismalium rotor 1600 %); (4) the Large Plasma Turbine is a LuV-hull machine: the controller waits on the LuV hull line and 2 LuV circuits only.
- **Unverified** the deuterium electrolysis, the liquid carbon source and the structure counts.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:plasma_large_turbine` | 1 |
| `gtceu:zpm_rotor_holder` | 1 |
| `start_core:luv_fusion_reactor` | 1 |
| `gtceu:zpm_energy_output_hatch` | 1 |
| `gtceu:power_substation` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Feeds:** [ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines](../zpm/zpm_argon.md)
- **Main source for:** `gtceu:zpm_rotor_holder`, `gtceu:plasma_large_turbine`, `gtceu:helium_plasma_bucket`
