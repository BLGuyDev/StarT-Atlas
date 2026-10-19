---
kind: chain
id: luv_alloys
order: 1200
data:
  t: |-
    LuV alloys: rhodium plated palladium (hull), ruridit (gears, rotor) and niobium titanium (cables, pipes), all IV Mixer → EBF 4500 K (RTM coils) → Vacuum Freezer
  inf: true
  "n":
    - - g1
      - "3 Palladium dust · 1 rhodium dust"
      - g
      - functionalstorage:oak_1
      - [[Palladium dust, "gtceu:palladium_dust"], [Rhodium dust, "gtceu:rhodium_dust"]]
    - - g2
      - "2 Ruthenium dust · 1 iridium dust"
      - g
      - functionalstorage:oak_1
      - [[Ruthenium dust, "gtceu:ruthenium_dust"], [Iridium dust, "gtceu:iridium_dust"]]
    - - g3
      - "1 Niobium dust · 1 titanium dust"
      - g
      - functionalstorage:oak_1
      - [[Niobium dust, "gtceu:niobium_dust"], [Titanium dust, "gtceu:titanium_dust"]]
    - [m1, "IV Mixer · circuit 1 · 20 s · 7680 EU/t", m, "gtceu:iv_mixer"]
    - [m2, "IV Mixer · circuit 1 · 17.5 s · 4096 EU/t", m, "gtceu:iv_mixer"]
    - [m3, "IV Mixer · circuit 1 · 10 s · 7680 EU/t", m, "gtceu:iv_mixer"]
    - [d1, "4 Rhodium plated palladium dust", x, "gtceu:rhodium_plated_palladium_dust"]
    - [d2, "3 Ruridit dust", x, "gtceu:ruridit_dust"]
    - [d3, "2 Niobium titanium dust", x, "gtceu:niobium_titanium_dust"]
    - - eb
      - EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480
      - m
      - gtceu:electric_blast_furnace
    - [vf, "Vacuum Freezer · 15 s · 15 s · 10 s", m, "gtceu:vacuum_freezer"]
    - [o1, Rhodium plated palladium ingot, o, "gtceu:rhodium_plated_palladium_ingot"]
    - [o2, Ruridit ingot, o, "gtceu:ruridit_ingot"]
    - [o3, Niobium titanium ingot, o, "gtceu:niobium_titanium_ingot"]
  e:
    - [g1, m1, "4"]
    - [g2, m2, "3"]
    - [g3, m3, "2"]
    - [m1, d1, "4 / 20 s"]
    - [m2, d2, "3 / 17.5 s"]
    - [m3, d3, "2 / 10 s"]
    - [d1, eb, "1"]
    - [d2, eb, "1"]
    - [d3, eb, "1"]
    - [eb, vf, hot ingots]
    - [vf, o1, "1"]
    - [vf, o2, "1"]
    - [vf, o3, "1"]
  tips:
    - |-
      Mixers (MixerRecipes, the pack does not change them): rhodium plated palladium = 3 palladium + 1 rhodium dust → 4 dust, circuit 1, 400 ticks at 7680 EU/t. Ruridit = 2 ruthenium + 1 iridium → 3 dust, circuit 1, 350 ticks at 4096 EU/t. Niobium titanium = 1 niobium + 1 titanium → 2 dust, circuit 1, 200 ticks at 7680 EU/t. All three are above the EV 2048 V cap, so they are IV Mixers (see the iv_components chain for the IV machine parts).
    - |-
      EBF numbers (material blast data, FirstDegreeMaterials / SecondDegreeMaterials): rhodium plated palladium 4500 K, 7680 EU/t, 1200 ticks (60 s), freezer 1920 EU/t 300 ticks (15 s). Ruridit 4500 K, 1920 EU/t, 1600 ticks (80 s), freezer 480 EU/t 300 ticks (15 s). Niobium titanium 4500 K, 480 EU/t, 1500 ticks (75 s), freezer 480 EU/t 200 ticks (10 s). RTM coils reach exactly 4500 K; none of the three is above 5000 K, so no liquid helium in the freezer. The gas recipe (circuit 2 + a gas hatch, gas tier argon) is 67 % of the time.
    - |-
      The EBF hatch decides which of them runs: the RPP recipe needs an IV Energy Hatch (7680 EU/t), the other two are fine on an EV hatch. One EBF per alloy is the clean way (a drawer queue on one EBF works but then the circuit and the hatch must fit all three). 16 RTM coil blocks per EBF, so about 73 ruthenium per furnace: see the rtm_coil chain, ruthenium is the bottleneck here too.
    - |-
      Sources: palladium, rhodium, ruthenium, iridium (and osmium) come from the platline chain; titanium from the titanium chain. Niobium: Unverified (the fork has pyrochlore ore with niobium, and niobium nitride is a chemical reactor recipe; no pack script gives a niobium route, check EMI for niobium dust). Samarium: rare earth dust centrifuge gives 25 % small samarium dust (SeparationRecipes), so very little; Unverified how the pack sieves/ore-processes it.
    - |-
      What each is for at LuV: rhodium plated palladium = plates for the LuV machine casing (8 per casing), dense plates and frames in later casings; ruridit = gears and rotor of the pack’s pump and piston, and the Assembly Line Unit gears; niobium titanium = cables, fine wire, fluid pipe and the springs of the LuV dynamo hatch. The pack’s startup scripts add rotor and small gear to ruridit and frame and foil to rhodium plated palladium (startup_scripts/elements_materials/material/modifications.js).
    - |-
      Sub-steps people skip: (1) hot ingots go through the freezer before anything else; (2) the three mixers share the circuit-1 recipe pattern, so one machine per alloy or a mixed drawer will jam; (3) ruridit mixer is 4096 EU/t, still an IV mixer; (4) rhodium is the scarce input of the whole LuV era (emitters and sensors eat 24 each, see luv_components2), do not spend it on anything else; (5) Keep Exact 16 on every dust drawer.
    - |-
      Unverified: the exact freezer time of the ruridit and RPP hot ingots (taken from the vacuumStats numbers above), and whether the EBF also accepts the plain EV hatch for the NbTi recipe at 480 EU/t (it should).
  b:
    - ["gtceu:iv_mixer", 3]
    - ["gtceu:electric_blast_furnace", 3]
    - ["gtceu:rtm_alloy_coil_block", 48]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["gtceu:ev_energy_input_hatch", 2]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 1]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:palladium_dust", "gtceu:rhodium_dust", "gtceu:niobium_dust"]
      t: |-
        Drawers first, one per dust: palladium, rhodium, ruthenium, iridium, niobium, titanium. Every mixer gets its own two-dust input (Modular Router or Pipez item pipe with Item Filters on the drawers) and a Robot Arm cover in Keep Exact mode on its output, so each EBF only receives its own alloy dust.
    - i: ["gtceu:iv_mixer", "gtceu:rhodium_plated_palladium_dust"]
      t: |-
        RPP mixer: circuit 1 in the ghost slot, 3 palladium + 1 rhodium dust → 4 dust in 20 s at 7680 EU/t. It needs an IV cable straight from the IV line (single machine, no hatch).
    - i: ["gtceu:iv_mixer", "gtceu:ruridit_dust", "gtceu:niobium_titanium_dust"]
      t: Ruridit mixer (circuit 1, 2 ruthenium + 1 iridium, 17.5 s, 4096 EU/t) and niobium titanium mixer (circuit 1, 1 + 1, 10 s, 7680 EU/t) are two more IV Mixers, one product each.
    - i: ["gtceu:electric_blast_furnace", "gtceu:rtm_alloy_coil_block", "gtceu:iv_energy_input_hatch"]
      t: EBF with 16 RTM coil blocks and an IV Energy Hatch for the RPP recipe (7680 EU/t). Input bus with ghost circuit 1, muffler hatch free above. 1 dust → 1 hot ingot (RPP 60 s, ruridit 80 s, NbTi 75 s). The gas recipe is circuit 2 plus a hatch of gas.
    - i: ["gtceu:vacuum_freezer", "gtceu:rhodium_plated_palladium_ingot"]
      t: |-
        Vacuum Freezer: a Robot Arm with an Item Filter takes the hot ingot from the EBF output into the freezer bus; no coolant below 5000 K. 10 to 15 s per ingot at 480 or 1920 EU/t. Output drawers with Keep Exact 32.
    - i: ["gtceu:lv_bender", "gtceu:rhodium_plated_palladium_plate", "gtceu:ruridit_ingot"]
      t: |-
        After the ingots: plates in an LV Bender (1 ingot → 1 plate, circuit 1) for the hull, wiremills for NbTi wire, and the gear/rotor lines of the component chain. Do not make them before you know the demand: 8 RPP plates per hull casing.
    - i: ["gtceu:iv_mixer", "gtceu:rhodium_dust", "gtceu:ruthenium_dust"]
      t: |-
        Easy to miss: all three alloys need the platinum group line first (rhodium, ruthenium, iridium) and RTM coils on the EBF. If the RTM coils are not built yet you cannot start; at 4500 K nothing else is lower.
---
# LuV alloys: rhodium plated palladium (hull), ruridit (gears, rotor) and niobium titanium (cables, pipes), all IV Mixer → EBF 4500 K (RTM coils) → Vacuum Freezer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [LuV metals (RPP, ruridit, NbTi, HSS-S)](../../plan/p11.md#luvmetals)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-m1">
<div class="gt-head"><span class="gt-mname">IV Mixer · circuit 1 · 20 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="3 Palladium dust · 1 rhodium dust (functionalstorage:oak_1) - 4"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">3 Palladium dust · 1 rhodium dust</span><span class="gt-sub"><span>Palladium dust</span><span>Rhodium dust</span></span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Rhodium plated palladium dust (gtceu:rhodium_plated_palladium_dust) - 4 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Dust</span><span class="gt-note">4 Rhodium plated palladium dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-iv" id="m-m2">
<div class="gt-head"><span class="gt-mname">IV Mixer · circuit 1 · 17.5 s · 4096 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 Ruthenium dust · 1 iridium dust (functionalstorage:oak_1) - 3"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 Ruthenium dust · 1 iridium dust</span><span class="gt-sub"><span>Ruthenium dust</span><span>Iridium dust</span></span><b class="gt-q">3</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">17.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="3 Ruridit dust (gtceu:ruridit_dust) - 3 / 17.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__ruridit_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruridit Dust</span><span class="gt-note">3 Ruridit dust</span><b class="gt-q">3</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-iv" id="m-m3">
<div class="gt-head"><span class="gt-mname">IV Mixer · circuit 1 · 10 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 Niobium dust · 1 titanium dust (functionalstorage:oak_1) - 2"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 Niobium dust · 1 titanium dust</span><span class="gt-sub"><span>Niobium dust</span><span>Titanium dust</span></span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Niobium titanium dust (gtceu:niobium_titanium_dust) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_titanium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Titanium Dust</span><span class="gt-note">2 Niobium titanium dust</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Rhodium plated palladium dust (gtceu:rhodium_plated_palladium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Dust</span><span class="gt-note">4 Rhodium plated palladium dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="3 Ruridit dust (gtceu:ruridit_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ruridit_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruridit Dust</span><span class="gt-note">3 Ruridit dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Niobium titanium dust (gtceu:niobium_titanium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_titanium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Titanium Dust</span><span class="gt-note">2 Niobium titanium dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-vf" title="Vacuum Freezer · 15 s · 15 s · 10 s (gtceu:vacuum_freezer) - hot ingots"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer · 15 s · 15 s · 10 s</span><b class="gt-q">hot ingots</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 15 s · 15 s · 10 s</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-eb" title="EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480 (gtceu:electric_blast_furnace) - hot ingots"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480</span><b class="gt-q">hot ingots</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Rhodium plated palladium ingot (gtceu:rhodium_plated_palladium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Ingot</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Ruridit ingot (gtceu:ruridit_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ruridit_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruridit Ingot</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Niobium titanium ingot (gtceu:niobium_titanium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Titanium Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [IV Mixer · circuit 1 · 20 s · 7680 EU/t](#m-m1) → [EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480](#m-eb) → [Vacuum Freezer · 15 s · 15 s · 10 s](#m-vf)
- [IV Mixer · circuit 1 · 17.5 s · 4096 EU/t](#m-m2) → [EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480](#m-eb)
- [IV Mixer · circuit 1 · 10 s · 7680 EU/t](#m-m3) → [EBF · RTM coils 4500 K · RPP 60 s 7680 EU/t · ruridit 80 s 1920 · NbTi 75 s 480](#m-eb)

## How to build

1. Drawers first, one per dust: palladium, rhodium, ruthenium, iridium, niobium, titanium. Every mixer gets its own two-dust input (Modular Router or Pipez item pipe with Item Filters on the drawers) and a Robot Arm cover in Keep Exact mode on its output, so each EBF only receives its own alloy dust. — `functionalstorage:oak_1`, `gtceu:palladium_dust`, `gtceu:rhodium_dust`, `gtceu:niobium_dust`
2. RPP mixer: circuit 1 in the ghost slot, 3 palladium + 1 rhodium dust → 4 dust in 20 s at 7680 EU/t. It needs an IV cable straight from the IV line (single machine, no hatch). — `gtceu:iv_mixer`, `gtceu:rhodium_plated_palladium_dust`
3. Ruridit mixer (circuit 1, 2 ruthenium + 1 iridium, 17.5 s, 4096 EU/t) and niobium titanium mixer (circuit 1, 1 + 1, 10 s, 7680 EU/t) are two more IV Mixers, one product each. — `gtceu:iv_mixer`, `gtceu:ruridit_dust`, `gtceu:niobium_titanium_dust`
4. EBF with 16 RTM coil blocks and an IV Energy Hatch for the RPP recipe (7680 EU/t). Input bus with ghost circuit 1, muffler hatch free above. 1 dust → 1 hot ingot (RPP 60 s, ruridit 80 s, NbTi 75 s). The gas recipe is circuit 2 plus a hatch of gas. — `gtceu:electric_blast_furnace`, `gtceu:rtm_alloy_coil_block`, `gtceu:iv_energy_input_hatch`
5. Vacuum Freezer: a Robot Arm with an Item Filter takes the hot ingot from the EBF output into the freezer bus; no coolant below 5000 K. 10 to 15 s per ingot at 480 or 1920 EU/t. Output drawers with Keep Exact 32. — `gtceu:vacuum_freezer`, `gtceu:rhodium_plated_palladium_ingot`
6. After the ingots: plates in an LV Bender (1 ingot → 1 plate, circuit 1) for the hull, wiremills for NbTi wire, and the gear/rotor lines of the component chain. Do not make them before you know the demand: 8 RPP plates per hull casing. — `gtceu:lv_bender`, `gtceu:rhodium_plated_palladium_plate`, `gtceu:ruridit_ingot`
7. Easy to miss: all three alloys need the platinum group line first (rhodium, ruthenium, iridium) and RTM coils on the EBF. If the RTM coils are not built yet you cannot start; at 4500 K nothing else is lower. — `gtceu:iv_mixer`, `gtceu:rhodium_dust`, `gtceu:ruthenium_dust`

## Tips

- Mixers (MixerRecipes, the pack does not change them): rhodium plated palladium = 3 palladium + 1 rhodium dust → 4 dust, circuit 1, 400 ticks at 7680 EU/t. Ruridit = 2 ruthenium + 1 iridium → 3 dust, circuit 1, 350 ticks at 4096 EU/t. Niobium titanium = 1 niobium + 1 titanium → 2 dust, circuit 1, 200 ticks at 7680 EU/t. All three are above the EV 2048 V cap, so they are IV Mixers (see the iv\_components chain for the IV machine parts).
- EBF numbers (material blast data, FirstDegreeMaterials / SecondDegreeMaterials): rhodium plated palladium 4500 K, 7680 EU/t, 1200 ticks (60 s), freezer 1920 EU/t 300 ticks (15 s). Ruridit 4500 K, 1920 EU/t, 1600 ticks (80 s), freezer 480 EU/t 300 ticks (15 s). Niobium titanium 4500 K, 480 EU/t, 1500 ticks (75 s), freezer 480 EU/t 200 ticks (10 s). RTM coils reach exactly 4500 K; none of the three is above 5000 K, so no liquid helium in the freezer. The gas recipe (circuit 2 + a gas hatch, gas tier argon) is 67 % of the time.
- The EBF hatch decides which of them runs: the RPP recipe needs an IV Energy Hatch (7680 EU/t), the other two are fine on an EV hatch. One EBF per alloy is the clean way (a drawer queue on one EBF works but then the circuit and the hatch must fit all three). 16 RTM coil blocks per EBF, so about 73 ruthenium per furnace: see the rtm\_coil chain, ruthenium is the bottleneck here too.
- Sources: palladium, rhodium, ruthenium, iridium (and osmium) come from the platline chain; titanium from the titanium chain. Niobium: Unverified (the fork has pyrochlore ore with niobium, and niobium nitride is a chemical reactor recipe; no pack script gives a niobium route, check EMI for niobium dust). Samarium: rare earth dust centrifuge gives 25 % small samarium dust (SeparationRecipes), so very little; Unverified how the pack sieves/ore-processes it.
- What each is for at LuV: rhodium plated palladium = plates for the LuV machine casing (8 per casing), dense plates and frames in later casings; ruridit = gears and rotor of the pack’s pump and piston, and the Assembly Line Unit gears; niobium titanium = cables, fine wire, fluid pipe and the springs of the LuV dynamo hatch. The pack’s startup scripts add rotor and small gear to ruridit and frame and foil to rhodium plated palladium (startup\_scripts/elements\_materials/material/modifications.js).
- Sub-steps people skip: (1) hot ingots go through the freezer before anything else; (2) the three mixers share the circuit-1 recipe pattern, so one machine per alloy or a mixed drawer will jam; (3) ruridit mixer is 4096 EU/t, still an IV mixer; (4) rhodium is the scarce input of the whole LuV era (emitters and sensors eat 24 each, see luv\_components2), do not spend it on anything else; (5) Keep Exact 16 on every dust drawer.
- **Unverified** the exact freezer time of the ruridit and RPP hot ingots (taken from the vacuumStats numbers above), and whether the EBF also accepts the plain EV hatch for the NbTi recipe at 480 EU/t (it should).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_mixer` | 3 |
| `gtceu:electric_blast_furnace` | 3 |
| `gtceu:rtm_alloy_coil_block` | 48 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `gtceu:ev_energy_input_hatch` | 2 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 1 |

## Needs / Feeds

- **Feeds:** [LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI](luv_hull.md), [LuV power: Large Gas Turbine with a LuV rotor holder](luv_turbines.md)
- **Main source for:** `gtceu:rhodium_plated_palladium_ingot`, `gtceu:rhodium_plated_palladium_dust`, `gtceu:ruridit_ingot`, `gtceu:ruridit_dust`, `gtceu:niobium_titanium_ingot`, `gtceu:niobium_titanium_dust`
