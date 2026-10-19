---
kind: chain
id: power_iv
order: 370
data:
  t: |-
    IV power: thorium fuel rods in the Nuclear Reactor, or fuel in the Extreme Combustion Engine, into an IV Dynamo Hatch
  power: true
  "n":
    - [th, "4 Thorium dust", i, "gtceu:thorium_dust"]
    - [fc, Aluminium fluid cell, i, "gtceu:aluminium_fluid_cell"]
    - [cn, "EV Canner · 30 s · 1920 EU/t", m, "gtceu:ev_canner"]
    - [rd, Thorium fuel rod, x, "kubejs:thr_fuel_rod"]
    - [dw, "Distilled water · 5 B per rod", f, "gtceu:distilled_water_bucket"]
    - [nr, "Nuclear Reactor · 29.4 s per rod · 4096 EU/t out", p, "gtceu:nuclear_reactor"]
    - [dr, Depleted thorium rod, x, "kubejs:depleted_thr_fuel_rod"]
    - [cf, "EV Centrifuge · 40 s · 960 EU/t", m, "gtceu:ev_centrifuge"]
    - [u5, "4 Uranium 235 dust", x, "gtceu:uranium_235_dust"]
    - - ff
      - Combustion fuel (toluene, naphtha, gasoline, high-octane gasoline)
      - f
      - gtceu:high_octane_gasoline_bucket
    - [ox, "Oxygen 20 mB/s (optional boost)", f, "gtceu:oxygen_bucket"]
    - [lu, Lubricant, f, "gtceu:lubricant_bucket"]
    - [ec, "Extreme Combustion Engine (needs 1 LuV circuit)", p, "gtceu:extreme_combustion_engine"]
    - [dy, "IV Dynamo Hatch (8192 V)", x, "gtceu:iv_energy_output_hatch"]
    - [w, Shellite wire or IV 4A converter line, x, "gtceu:shellite_single_wire"]
    - [mc, IV machines, o, "gtceu:iv_assembler"]
  e:
    - [th, cn, "4"]
    - [fc, cn, "1"]
    - [cn, rd, "1 / 30 s"]
    - [rd, nr, "1"]
    - [dw, nr, "5 B"]
    - [nr, dr, "1 / 29.4 s"]
    - [nr, dy, "4096 EU/t"]
    - [dr, cf, "1"]
    - [cf, u5, "4"]
    - [ff, ec]
    - [ox, ec]
    - [lu, ec]
    - [ec, dy, "about 8192 EU/t"]
    - [dy, w, "8192 V"]
    - [w, mc]
  tips:
    - |-
      The reactor is in the era list, the engine is not: a Nuclear Reactor controller needs 2 IV circuits, an EV robot arm, 2 EV fluid regulators, an EV emitter, a Large Chemical Reactor and 2 heat vents (kjs systems/fission/nuclear_reactor.js). The Extreme Combustion Engine controller (gt_machine_recipes) needs 1 LuV circuit, 2 IV pistons, 2 IV motors, an IV hull, 2 tungsten steel gears and an HSS-G cable, so it waits for the LuV circuits. The other controllers from the extracted recipes: Large Gas Turbine = EV hull + 2 EV circuits + 4 stainless steel gears + 2 stainless large fluid pipes (an EV machine, nothing IV in it); Large Combustion Engine = EV hull + 2 EV pistons + 2 EV motors + 1 IV circuit + 2 titanium gears + aluminium cable (an EV-tier controller, but the IV circuit means you cannot build it before the Microprocessor Mainframe); Large Steam Turbine = HV hull + 2 HV circuits.
    - |-
      Thorium fuel rod numbers (kjs nuclear_reactor.js, nuclear_fission.js): the Canner makes 1 rod from 1 aluminium fluid cell + 4 thorium dust in 600 ticks at VA[HV] x 4 = 1920 EU/t. The reactor burns 1 rod and 5 B distilled water in 588 ticks (29.4 s) and generates V[EV] x boost x 2^tier = 2048 x 1 x 2 = 4096 EU/t, so one rod is about 2.4 million EU. The LEU-238 rod (4 uranium dust, same tier) gives 4506 EU/t for 611 ticks.
    - |-
      The 4096 EU/t fits one IV Dynamo Hatch (8192 V, 1 A); higher rods do not: HEU makes 19 661 EU/t and the MOX rods up to 32 768 EU/t, which needs LuV-voltage hatches. A Parallel Hatch needs LuV circuits too (the IV one allows up to 4 recipes and costs 4 LuV circuits + IV sensor, emitter, hull + 2 platinum double cables). So at IV you run exactly one rod at a time.
    - |-
      The reactor structure (multis): 110 High Temperature Smelting casings (hatches go in them), 42 heat vents, 16 pallaridium engine intake casings, 13 tungstensteel pipe casings, 10 laminated glass, 1 dynamo hatch. The intake casing is the bottleneck: 2 per craft = 2 palladium rotors + 4 iridium normal fluid pipes + 1 palladium substation casing (6 palladium plates + 1 iridium frame), so the 16 casings are 8 crafts of about 13 iridium ingots each (4 pipes of 3 ingots plus half an iridium frame), roughly 105 iridium ingots in all. Treat the reactor as a late-IV goal, after the platinum group line runs.
    - |-
      Waste: EV Centrifuge, 1 depleted thorium rod → 1 aluminium fluid cell + 4 uranium 235 dust, 800 ticks at 960 EU/t (VHA[HV] x 4). That is the fuel for the HEU rod at the next tier, so keep the uranium dust rather than voiding it. Thorium: from the Electric Ore Factory as a by-product of coal (tertiary) and pitchblende; 8 dust a minute feeds one reactor.
    - |-
      Fuel energy in the engine and in LV combustion generators (FuelRecipes: 32 EU/t times the ticks per amount): high-octane gasoline 3200 EU/mB, gasoline 1600, cetane diesel 720, diesel 480, toluene 320, naphtha 320, light fuel 320, biodiesel 256, rocket fuel 250, ethanol 192, octane 80. The engine’s own lang says: 20 mB/s oxygen (or 80 mB/s liquid oxygen with a bigger dynamo hatch) gives more power at 2x fuel use. Unverified: the base output (assumed to be the IV 8192 EU/t) and the lubricant rate; read the multiblock tooltip.
    - |-
      Nitrobenzene (what players call NBZ) is a GAS TURBINE fuel, not a combustion fuel: 1 mB lasts 40 ticks at 32 EU/t = 1280 EU/mB (1.28 MEU per bucket, 3.6x the 352 EU/mB of benzene) and it burns in gas turbines and the Large Gas Turbine (EV), but not in the combustion engines or LV combustion generators. Recipe: chemical reactor HV 480 EU/t, 160 ticks, 5 B benzene + 2 B nitration mixture + 2 B distilled water → 8 B nitrobenzene + 1 B diluted sulfuric acid; nitration mixture = mixer (2 EU/t, 1 B nitric acid + 1 B sulfuric acid → 2 B). One HV reactor makes 1 B/s, which is 25 600 EU/t of fuel. The EV way to burn it is a Large Gas Turbine, not the engine.
    - |-
      The quest chapter also lists large turbines (steam HV, gas EV, plasma IV), rotor holders and IV solar panels as IV power. Rotor holder tier up doubles power and parallels at 1.8x fuel (pack quest). The steam and gas controllers are in the first tip; the LuV rotor holder is in the luv_power tips. Unverified: the plasma turbine controller recipe. The Power Substation in the old step list is a LuV multiblock (4 lapotron crystals, 2 LuV circuits).
    - |-
      Sub-steps people skip: (1) the reactor wants the water as DISTILLED water, not plain; (2) the depleted rod goes to the centrifuge, not the bin, because the cell comes back; (3) the dynamo hatch goes in the reactor’s hatch slot, the same casing row as the buses; (4) never let the rod drawer feed two reactors; (5) shellite wire is the IV superconductor for the output cable (see the shellite_line chain).
    - |-
      Unverified: distilled water supply rate (170 mB/s per rod, see the EV chains), the exact hatch slot layout (read the multiblock card), and how the engine intake tooltip numbers scale with the rotor-holder style upgrades in the pack.
  b:
    - ["gtceu:ev_canner", 1]
    - ["gtceu:ev_centrifuge", 1]
    - ["gtceu:nuclear_reactor", 1]
    - ["gtceu:iv_energy_output_hatch", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 5]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 4]
  inf: true
  how:
    - i: ["functionalstorage:oak_1", "gtceu:thorium_dust", "gtceu:aluminium_fluid_cell"]
      t: |-
        Drawers first: thorium dust, aluminium fluid cells, finished fuel rods, depleted rods, uranium 235 dust. A distilled water drum with a pump cover to the reactor. Every machine here is a single task with its own filtered route and Keep Exact on its output.
    - i: ["gtceu:ev_canner", "kubejs:thr_fuel_rod"]
      t: |-
        EV Canner: 1 aluminium fluid cell + 4 thorium dust → 1 thorium fuel rod, 30 s at 1920 EU/t (an EV machine on an EV cable). Output drawer with Keep Exact 4 so the reactor always has a spare.
    - i: ["gtceu:nuclear_reactor", "gtceu:distilled_water_bucket", "gtceu:iv_energy_output_hatch"]
      t: |-
        Nuclear Reactor: the rod goes in an input bus, 5 B distilled water through a fluid hatch per rod, one IV Dynamo Hatch in a hatch slot. 29.4 s per rod at 4096 EU/t output. Route the depleted rod out through an output bus with a Robot Arm into the centrifuge drawer.
    - i: ["gtceu:ev_centrifuge", "gtceu:uranium_235_dust"]
      t: |-
        EV Centrifuge: 1 depleted thorium rod → 1 aluminium fluid cell + 4 uranium 235 dust in 40 s at 960 EU/t. The cell goes back to the canner drawer; the uranium goes to its own drawer. That closes the loop and gives the fuel for the next rod tier.
    - i: ["gtceu:iv_energy_output_hatch", "gtceu:shellite_single_wire"]
      t: |-
        Output: the dynamo hatch feeds an IV cable (tungsten or platinum, 8192 V) or shellite wire from the dynamo to a distribution row or to an IV 4A converter line. One rod at 4096 EU/t uses half an amp of an 8192 V hatch.
    - i: ["gtceu:extreme_combustion_engine", "gtceu:high_octane_gasoline_bucket"]
      t: |-
        Option once you hold a LuV circuit: Extreme Combustion Engine (tungstensteel casings, tungstensteel gearbox, extreme engine intake), fuel from a drum through a pump cover, lubricant and optional oxygen the same way, dynamo hatch on the output. Fuel per second = output EU/t divided by the fuel’s EU per mB. Toluene from the oil_distill chain is the cheap one (320 EU/mB).
    - i: ["gtceu:nuclear_reactor", "gtceu:iridium_dust"]
      t: |-
        Easy to miss: before you plan the reactor, count iridium. The 16 intake casings alone need roughly 105 iridium ingots (8 crafts of 4 iridium pipes plus a palladium substation casing with an iridium frame), and iridium comes from the platinum group line at 1 per 42 sludge. If that is too slow, power the IV era from converters on Lapidary Dynamos instead (the HV power chain with EV upgrade kits) and leave the reactor for LuV.
---
# IV power: thorium fuel rods in the Nuclear Reactor, or fuel in the Extreme Combustion Engine, into an IV Dynamo Hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_iv` · **Tags:** Infinite source, Power, Unverified

**Plan modules:** [IV power: thorium Nuclear Reactor (or more turbines)](../../plan/p10.md#ivpower)

**Tips:** 10, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-cn">
<div class="gt-head"><span class="gt-mname">EV Canner · 30 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Thorium dust (gtceu:thorium_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__thorium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Thorium Dust</span><span class="gt-note">4 Thorium dust</span><b class="gt-q">4</b></span><span class="gt-slot" title="Aluminium fluid cell (gtceu:aluminium_fluid_cell) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_fluid_cell.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Fluid Cell</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_canner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Thorium fuel rod (kubejs:thr_fuel_rod) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/kubejs__thr_fuel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Thr Fuel Rod</span><span class="gt-note">Thorium fuel rod</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_canner</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-nr">
<div class="gt-head"><span class="gt-mname">Nuclear Reactor · 29.4 s per rod · 4096 EU/t out</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Thorium fuel rod (kubejs:thr_fuel_rod) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__thr_fuel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Thr Fuel Rod</span><span class="gt-note">Thorium fuel rod</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Distilled water · 5 B per rod (gtceu:distilled_water_bucket) - 5 B"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water</span><span class="gt-note">Distilled water · 5 B per rod</span><b class="gt-q">5 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__nuclear_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">29.4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Depleted thorium rod (kubejs:depleted_thr_fuel_rod) - 1 / 29.4 s"><img class="gt-ico" src="../../assets/icons/kubejs__depleted_thr_fuel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Depleted Thr Fuel Rod</span><span class="gt-note">Depleted thorium rod</span><b class="gt-q">1</b></span><span class="gt-slot" title="IV Dynamo Hatch (8192 V) (gtceu:iv_energy_output_hatch) - 4096 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Output Hatch</span><span class="gt-note">IV Dynamo Hatch (8192 V)</span><b class="gt-q">4096 EU/t</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:nuclear_reactor</code></div>
</div>
<div class="gt-panel t-ev" id="m-cf">
<div class="gt-head"><span class="gt-mname">EV Centrifuge · 40 s · 960 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Depleted thorium rod (kubejs:depleted_thr_fuel_rod) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__depleted_thr_fuel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Depleted Thr Fuel Rod</span><span class="gt-note">Depleted thorium rod</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Uranium 235 dust (gtceu:uranium_235_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__uranium_235_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uranium 235 Dust</span><span class="gt-note">4 Uranium 235 dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_centrifuge</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-ec">
<div class="gt-head"><span class="gt-mname">Extreme Combustion Engine (needs 1 LuV circuit)</span><span class="gt-badge t-mod">GregTech</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Combustion fuel (toluene, naphtha, gasoline, high-octane gasoline) (gtceu:high_octane_gasoline_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__high_octane_gasoline_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">High Octane Gasoline</span><span class="gt-note">Combustion fuel (toluene, naphtha, gasoline, high-octane gasoline)</span></span><span class="gt-slot gt-fluid" title="Oxygen 20 mB/s (optional boost) (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><span class="gt-note">Oxygen 20 mB/s (optional boost)</span></span><span class="gt-slot gt-fluid" title="Lubricant (gtceu:lubricant_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__lubricant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lubricant</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__extreme_combustion_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="IV Dynamo Hatch (8192 V) (gtceu:iv_energy_output_hatch) - about 8192 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Output Hatch</span><span class="gt-note">IV Dynamo Hatch (8192 V)</span><b class="gt-q">about 8192 EU/t</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:extreme_combustion_engine</code></div>
</div>
</div>

## Flow

- [EV Canner · 30 s · 1920 EU/t](#m-cn) → [Nuclear Reactor · 29.4 s per rod · 4096 EU/t out](#m-nr) → [EV Centrifuge · 40 s · 960 EU/t](#m-cf)
- [Extreme Combustion Engine (needs 1 LuV circuit)](#m-ec)

### Direct steps

- IV Dynamo Hatch (8192 V) → Shellite wire or IV 4A converter line (8192 V)
- Shellite wire or IV 4A converter line → IV machines

## How to build

1. Drawers first: thorium dust, aluminium fluid cells, finished fuel rods, depleted rods, uranium 235 dust. A distilled water drum with a pump cover to the reactor. Every machine here is a single task with its own filtered route and Keep Exact on its output. — `functionalstorage:oak_1`, `gtceu:thorium_dust`, `gtceu:aluminium_fluid_cell`
2. EV Canner: 1 aluminium fluid cell + 4 thorium dust → 1 thorium fuel rod, 30 s at 1920 EU/t (an EV machine on an EV cable). Output drawer with Keep Exact 4 so the reactor always has a spare. — `gtceu:ev_canner`, `kubejs:thr_fuel_rod`
3. Nuclear Reactor: the rod goes in an input bus, 5 B distilled water through a fluid hatch per rod, one IV Dynamo Hatch in a hatch slot. 29.4 s per rod at 4096 EU/t output. Route the depleted rod out through an output bus with a Robot Arm into the centrifuge drawer. — `gtceu:nuclear_reactor`, `gtceu:distilled_water_bucket`, `gtceu:iv_energy_output_hatch`
4. EV Centrifuge: 1 depleted thorium rod → 1 aluminium fluid cell + 4 uranium 235 dust in 40 s at 960 EU/t. The cell goes back to the canner drawer; the uranium goes to its own drawer. That closes the loop and gives the fuel for the next rod tier. — `gtceu:ev_centrifuge`, `gtceu:uranium_235_dust`
5. Output: the dynamo hatch feeds an IV cable (tungsten or platinum, 8192 V) or shellite wire from the dynamo to a distribution row or to an IV 4A converter line. One rod at 4096 EU/t uses half an amp of an 8192 V hatch. — `gtceu:iv_energy_output_hatch`, `gtceu:shellite_single_wire`
6. Option once you hold a LuV circuit: Extreme Combustion Engine (tungstensteel casings, tungstensteel gearbox, extreme engine intake), fuel from a drum through a pump cover, lubricant and optional oxygen the same way, dynamo hatch on the output. Fuel per second = output EU/t divided by the fuel’s EU per mB. Toluene from the oil\_distill chain is the cheap one (320 EU/mB). — `gtceu:extreme_combustion_engine`, `gtceu:high_octane_gasoline_bucket`
7. Easy to miss: before you plan the reactor, count iridium. The 16 intake casings alone need roughly 105 iridium ingots (8 crafts of 4 iridium pipes plus a palladium substation casing with an iridium frame), and iridium comes from the platinum group line at 1 per 42 sludge. If that is too slow, power the IV era from converters on Lapidary Dynamos instead (the HV power chain with EV upgrade kits) and leave the reactor for LuV. — `gtceu:nuclear_reactor`, `gtceu:iridium_dust`

## Tips

- The reactor is in the era list, the engine is not: a Nuclear Reactor controller needs 2 IV circuits, an EV robot arm, 2 EV fluid regulators, an EV emitter, a Large Chemical Reactor and 2 heat vents (kjs systems/fission/nuclear\_reactor.js). The Extreme Combustion Engine controller (gt\_machine\_recipes) needs 1 LuV circuit, 2 IV pistons, 2 IV motors, an IV hull, 2 tungsten steel gears and an HSS-G cable, so it waits for the LuV circuits. The other controllers from the extracted recipes: Large Gas Turbine = EV hull + 2 EV circuits + 4 stainless steel gears + 2 stainless large fluid pipes (an EV machine, nothing IV in it); Large Combustion Engine = EV hull + 2 EV pistons + 2 EV motors + 1 IV circuit + 2 titanium gears + aluminium cable (an EV-tier controller, but the IV circuit means you cannot build it before the Microprocessor Mainframe); Large Steam Turbine = HV hull + 2 HV circuits.
- Thorium fuel rod numbers (kjs nuclear\_reactor.js, nuclear\_fission.js): the Canner makes 1 rod from 1 aluminium fluid cell + 4 thorium dust in 600 ticks at VA\[HV\] x 4 = 1920 EU/t. The reactor burns 1 rod and 5 B distilled water in 588 ticks (29.4 s) and generates V\[EV\] x boost x 2^tier = 2048 x 1 x 2 = 4096 EU/t, so one rod is about 2.4 million EU. The LEU-238 rod (4 uranium dust, same tier) gives 4506 EU/t for 611 ticks.
- The 4096 EU/t fits one IV Dynamo Hatch (8192 V, 1 A); higher rods do not: HEU makes 19 661 EU/t and the MOX rods up to 32 768 EU/t, which needs LuV-voltage hatches. A Parallel Hatch needs LuV circuits too (the IV one allows up to 4 recipes and costs 4 LuV circuits + IV sensor, emitter, hull + 2 platinum double cables). So at IV you run exactly one rod at a time.
- The reactor structure (multis): 110 High Temperature Smelting casings (hatches go in them), 42 heat vents, 16 pallaridium engine intake casings, 13 tungstensteel pipe casings, 10 laminated glass, 1 dynamo hatch. The intake casing is the bottleneck: 2 per craft = 2 palladium rotors + 4 iridium normal fluid pipes + 1 palladium substation casing (6 palladium plates + 1 iridium frame), so the 16 casings are 8 crafts of about 13 iridium ingots each (4 pipes of 3 ingots plus half an iridium frame), roughly 105 iridium ingots in all. Treat the reactor as a late-IV goal, after the platinum group line runs.
- Waste: EV Centrifuge, 1 depleted thorium rod → 1 aluminium fluid cell + 4 uranium 235 dust, 800 ticks at 960 EU/t (VHA\[HV\] x 4). That is the fuel for the HEU rod at the next tier, so keep the uranium dust rather than voiding it. Thorium: from the Electric Ore Factory as a by-product of coal (tertiary) and pitchblende; 8 dust a minute feeds one reactor.
- Fuel energy in the engine and in LV combustion generators (FuelRecipes: 32 EU/t times the ticks per amount): high-octane gasoline 3200 EU/mB, gasoline 1600, cetane diesel 720, diesel 480, toluene 320, naphtha 320, light fuel 320, biodiesel 256, rocket fuel 250, ethanol 192, octane 80. The engine’s own lang says: 20 mB/s oxygen (or 80 mB/s liquid oxygen with a bigger dynamo hatch) gives more power at 2x fuel use. Unverified: the base output (assumed to be the IV 8192 EU/t) and the lubricant rate; read the multiblock tooltip.
- Nitrobenzene (what players call NBZ) is a GAS TURBINE fuel, not a combustion fuel: 1 mB lasts 40 ticks at 32 EU/t = 1280 EU/mB (1.28 MEU per bucket, 3.6x the 352 EU/mB of benzene) and it burns in gas turbines and the Large Gas Turbine (EV), but not in the combustion engines or LV combustion generators. Recipe: chemical reactor HV 480 EU/t, 160 ticks, 5 B benzene + 2 B nitration mixture + 2 B distilled water → 8 B nitrobenzene + 1 B diluted sulfuric acid; nitration mixture = mixer (2 EU/t, 1 B nitric acid + 1 B sulfuric acid → 2 B). One HV reactor makes 1 B/s, which is 25 600 EU/t of fuel. The EV way to burn it is a Large Gas Turbine, not the engine.
- The quest chapter also lists large turbines (steam HV, gas EV, plasma IV), rotor holders and IV solar panels as IV power. Rotor holder tier up doubles power and parallels at 1.8x fuel (pack quest). The steam and gas controllers are in the first tip; the LuV rotor holder is in the luv\_power tips. Unverified: the plasma turbine controller recipe. The Power Substation in the old step list is a LuV multiblock (4 lapotron crystals, 2 LuV circuits).
- Sub-steps people skip: (1) the reactor wants the water as DISTILLED water, not plain; (2) the depleted rod goes to the centrifuge, not the bin, because the cell comes back; (3) the dynamo hatch goes in the reactor’s hatch slot, the same casing row as the buses; (4) never let the rod drawer feed two reactors; (5) shellite wire is the IV superconductor for the output cable (see the shellite\_line chain).
- **Unverified** distilled water supply rate (170 mB/s per rod, see the EV chains), the exact hatch slot layout (read the multiblock card), and how the engine intake tooltip numbers scale with the rotor-holder style upgrades in the pack.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:ev_canner` | 1 |
| `gtceu:ev_centrifuge` | 1 |
| `gtceu:nuclear_reactor` | 1 |
| `gtceu:iv_energy_output_hatch` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 5 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 4 |
