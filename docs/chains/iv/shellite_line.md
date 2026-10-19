---
kind: chain
id: shellite_line
order: 1160
data:
  t: |-
    Shellite: signalum + black bronze → EV Mixer → EBF 4400 K (RTM coils, IV hatch) → wire → IV converters
  inf: true
  "n":
    - [sa, "1 Silver + 3 copper + 4 redstone dust", i, "gtceu:silver_dust"]
    - [m1, "LV Mixer · circuit 3 · 15 s · 20 EU/t", m, "gtceu:lv_mixer"]
    - [sg, "4 Signalum dust", x, "gtceu:signalum_dust"]
    - [cb, "3 Copper + 2 electrum dust", i, "gtceu:copper_dust"]
    - [m2, "LV Mixer · circuit 1 · 25 s · 7 EU/t", m, "gtceu:lv_mixer"]
    - [bb, "5 Black bronze dust", x, "gtceu:black_bronze_dust"]
    - [m3, "EV Mixer · 35 s · 1024 EU/t", m, "gtceu:ev_mixer"]
    - [sd, "4 Shellite dust", x, "gtceu:shellite_dust"]
    - [he, "Helium · 1 B (optional, circuit 2)", f, "gtceu:helium_bucket"]
    - [eb, "EBF · RTM coils 4400 K · 70 s · 7680 EU/t", m, "gtceu:electric_blast_furnace"]
    - [hs, Hot shellite ingot, x, "gtceu:hot_shellite_ingot"]
    - [vf, Vacuum Freezer, m, "gtceu:vacuum_freezer"]
    - [si, Shellite ingot, o, "gtceu:shellite_ingot"]
    - [wm, "LV Wiremill · circuit 1 / 4 / 8 / 16", m, "gtceu:lv_wiremill"]
    - [w1, "Shellite single wire (2 per ingot)", x, "gtceu:shellite_single_wire"]
    - [w4, "Shellite quadruple wire (2 ingots)", x, "gtceu:shellite_quadruple_wire"]
    - [ic, "IV circuit + IV hull", i, "gtceu:iv_machine_hull"]
    - [cv, IV 4A Energy Converter, o, "gtceu:iv_4a_energy_converter"]
  e:
    - [sa, m1, "1 + 3 + 4"]
    - [m1, sg, "4"]
    - [cb, m2, "3 + 2"]
    - [m2, bb, "5"]
    - [sg, m3, "3"]
    - [bb, m3, "1"]
    - [m3, sd, "4"]
    - [sd, eb, "1"]
    - [he, eb]
    - [eb, hs, "1 / 70 s"]
    - [hs, vf, "1"]
    - [vf, si, "1"]
    - [si, wm, "1"]
    - [wm, w1, "2 per ingot"]
    - [wm, w4, "1 per 2 ingots"]
    - [w4, cv, "4"]
    - [ic, cv, "1 + 1"]
  tips:
    - |-
      Shellite (kjs startup superconductors.js, additions/progression/superconductors.js): the IV superconductor, 64 A in a single wire at 8192 V, no cable coating and no loss. Signalum dust: LV Mixer, circuit 3, 1 silver + 3 copper + 4 redstone dust → 4 dust (300 ticks, 20 EU/t). Black bronze dust: mixer, circuit 1, 3 copper + 2 electrum → 5 dust (500 ticks, 7 EU/t). Shellite dust: 1 black bronze + 3 signalum → 4 dust in 700 ticks at 1024 EU/t, which is above the HV 512, so an EV Mixer.
    - |-
      Blast recipe: 4400 K, gas tier mid (helium), 7680 EU/t (VA[IV]), 1400 ticks = 70 s per ingot. 4400 K needs RTM coils (4500 K) and 7680 EU/t needs an IV Energy Hatch on the EBF (the iv_hatches chain). With circuit 2 and 1 B helium the recipe takes 67 % of the time (about 47 s). The hot ingot then goes through the Vacuum Freezer (below 5000 K: no coolant); the pack sets no freezer numbers, so it uses the default 120 EU/t and a mass-based time.
    - |-
      Wire: LV Wiremill (30 EU/t, shellite is above 2800 K): circuit 1 = 2 single wires per ingot, circuit 2 = 1 double wire per ingot, circuit 4 = 1 quadruple wire per 2 ingots, circuit 8 = octal (4 ingots), circuit 16 = hex (8 ingots). The pack’s converters use these directly (converters.js): the 1A, 4A, 8A and 16A converters are 4 wires of single, quadruple, octal and hex + 1 circuit + the hull, shaped in a crafting table.
    - |-
      So the IV 4A Energy Converter = 4 quadruple wires (8 ingots) + 1 IV circuit + 1 IV machine hull, and one shellite ingot costs about 0.54 million EU in the furnace. The 64A converter is an EV Assembler recipe (600 ticks, 1625 EU/t): 16 hex wires (128 ingots) + IV circuit + hull, so plan about 2.5 hours of one furnace. Converters let Thermal dynamos, Lapidary dynamos and flux plugs feed IV machines: FE in, EU out.
    - |-
      Cost in the mixers: 4 shellite dust need 1 black bronze + 3 signalum, i.e. 3 silver-based signalum dust (0.75 silver) and 1 black bronze dust (0.6 copper, 0.4 electrum) per 4 dust. The signalum mixer and the shellite mixer are separate machines; the two mixers on circuit 1 and 3 must not share a bus.
    - |-
      Where else shellite goes: the shellite casing and frame (kjs casings.js) in late multiblocks, the thermal augment kits of the IV tier (thermal_augments.js), the Hellforge and the stargate parts. None are IV goals, so make wire and the 4A converter first.
    - |-
      Sub-steps people skip: (1) the hot ingot must be frozen, a shellite wire never accepts it; (2) each wire size has its own circuit, so build one wiremill per size you actually need (single for the 1A converter, quadruple for 4A); (3) the EBF needs the IV hatch AND RTM coils: a Nichrome EBF with an IV hatch still refuses the 4400 K recipe; (4) the mixer for shellite takes the dust, not the ingots, of black bronze and signalum.
    - |-
      Unverified: the vacuum freezer time and power for shellite (default values assumed), and the helium amount per ingot (read as 1000 mB from the jar).
  b:
    - ["gtceu:lv_mixer", 2]
    - ["gtceu:ev_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:rtm_alloy_coil_block", 16]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:lv_wiremill", 2]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:silver_dust", "gtceu:copper_dust", "gtceu:electrum_dust"]
      t: |-
        Drawers first: silver, copper, electrum and redstone dust, one drawer each, and a helium drum. Each mixer gets its own pair of drawers through Modular Router or Pipez routes with Item Filters; the two LV mixers differ only in their ghost circuit (3 and 1), so they are two machines.
    - i: ["gtceu:lv_mixer", "gtceu:signalum_dust"]
      t: |-
        Signalum: LV Mixer, ghost circuit 3: 1 silver + 3 copper + 4 redstone dust → 4 signalum dust in 15 s at 20 EU/t. Keep Exact 64 on the output; three of these dust go into every shellite batch.
    - i: ["gtceu:lv_mixer", "gtceu:black_bronze_dust"]
      t: |-
        Black bronze: LV Mixer, ghost circuit 1: 3 copper + 2 electrum dust → 5 black bronze dust in 25 s at 7 EU/t. Keep Exact 16 on the output: one dust per shellite batch.
    - i: ["gtceu:ev_mixer", "gtceu:shellite_dust"]
      t: |-
        Shellite dust: EV Mixer (1024 EU/t, no ghost circuit needed in the recipe but keep the machine dedicated): 1 black bronze + 3 signalum dust → 4 shellite dust in 35 s. Output drawer with Keep Exact 64.
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:rtm_alloy_coil_block
        - gtceu:iv_energy_input_hatch
        - gtceu:hot_shellite_ingot
      t: |-
        Dedicated EBF with 16 RTM coil blocks and an IV Energy Hatch: input bus with ghost circuit 1 (circuit 2 plus a 1 B helium hatch for the 67 % recipe), 1 shellite dust → 1 hot shellite ingot in 70 s at 7680 EU/t. Muffler hatch free above it. Do not mix this furnace with other recipes: the coils decide the temperature.
    - i: ["gtceu:vacuum_freezer", "gtceu:shellite_ingot"]
      t: |-
        Vacuum Freezer: Robot Arm from the EBF output into its bus (Item Filter on the hot ingot), 1 ingot per freeze, no coolant. Output drawer with Keep Exact 32.
    - i: ["gtceu:lv_wiremill", "gtceu:shellite_single_wire", "gtceu:shellite_quadruple_wire"]
      t: |-
        LV Wiremills, one per size: circuit 1 gives 2 single wires per ingot, circuit 4 gives 1 quadruple wire per 2 ingots. Each output drawer is capped by a Keep Exact arm at 16, because converters need 4 wires of one size.
    - i: ["gtceu:iv_4a_energy_converter", "gtceu:iv_machine_hull"]
      t: |-
        Easy to miss: craft the converter in a crafting table: bottom row wire, hull, wire; middle row wire, IV circuit, wire (4 wires, circuit, hull in the pack’s shaped recipe). 8 ingots, 1 circuit and 1 hull for the 4A one; the 1A one is only 2 ingots for its 4 single wires.
---
# Shellite: signalum + black bronze → EV Mixer → EBF 4400 K (RTM coils, IV hatch) → wire → IV converters

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `shellite_line` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [IV components, RTM coil, Shellite](../../plan/p10.md#ivmach)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-m1">
<div class="gt-head"><span class="gt-mname">LV Mixer · circuit 3 · 15 s · 20 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Silver + 3 copper + 4 redstone dust (gtceu:silver_dust) - 1 + 3 + 4"><img class="gt-ico" src="../../assets/icons/gtceu__silver_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Dust</span><span class="gt-note">1 Silver + 3 copper + 4 redstone dust</span><b class="gt-q">1 + 3 + 4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Signalum dust (gtceu:signalum_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__signalum_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Signalum Dust</span><span class="gt-note">4 Signalum dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
<div class="gt-panel t-lv" id="m-m2">
<div class="gt-head"><span class="gt-mname">LV Mixer · circuit 1 · 25 s · 7 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Copper + 2 electrum dust (gtceu:copper_dust) - 3 + 2"><img class="gt-ico" src="../../assets/icons/gtceu__copper_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Dust</span><span class="gt-note">3 Copper + 2 electrum dust</span><b class="gt-q">3 + 2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Black bronze dust (gtceu:black_bronze_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__black_bronze_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Black Bronze Dust</span><span class="gt-note">5 Black bronze dust</span><b class="gt-q">5</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
<div class="gt-panel t-ev" id="m-m3">
<div class="gt-head"><span class="gt-mname">EV Mixer · 35 s · 1024 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Signalum dust (gtceu:signalum_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__signalum_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Signalum Dust</span><span class="gt-note">4 Signalum dust</span><b class="gt-q">3</b></span><span class="gt-slot" title="5 Black bronze dust (gtceu:black_bronze_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__black_bronze_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Black Bronze Dust</span><span class="gt-note">5 Black bronze dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Shellite dust (gtceu:shellite_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Dust</span><span class="gt-note">4 Shellite dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · RTM coils 4400 K · 70 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Shellite dust (gtceu:shellite_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Dust</span><span class="gt-note">4 Shellite dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Helium · 1 B (optional, circuit 2) (gtceu:helium_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium · 1 B (optional, circuit 2)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">70 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot shellite ingot (gtceu:hot_shellite_ingot) - 1 / 70 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_shellite_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Shellite Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot shellite ingot (gtceu:hot_shellite_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_shellite_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Shellite Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Shellite ingot (gtceu:shellite_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">LV Wiremill · circuit 1 / 4 / 8 / 16</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="Shellite ingot (gtceu:shellite_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Shellite single wire (2 per ingot) (gtceu:shellite_single_wire) - 2 per ingot"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Single Wire</span><span class="gt-note">Shellite single wire (2 per ingot)</span><b class="gt-q">2 per ingot</b></span><span class="gt-slot" title="Shellite quadruple wire (2 ingots) (gtceu:shellite_quadruple_wire) - 1 per 2 ingots"><img class="gt-ico" src="../../assets/icons/gtceu__shellite_quadruple_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shellite Quadruple Wire</span><span class="gt-note">Shellite quadruple wire (2 ingots)</span><b class="gt-q">1 per 2 ingots</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
</div>

## Flow

- [LV Mixer · circuit 3 · 15 s · 20 EU/t](#m-m1) → [EV Mixer · 35 s · 1024 EU/t](#m-m3) → [EBF · RTM coils 4400 K · 70 s · 7680 EU/t](#m-eb) → [Vacuum Freezer](#m-vf) → [LV Wiremill · circuit 1 / 4 / 8 / 16](#m-wm)
- [LV Mixer · circuit 1 · 25 s · 7 EU/t](#m-m2) → [EV Mixer · 35 s · 1024 EU/t](#m-m3)

### Direct steps

- Shellite quadruple wire (2 ingots) → IV 4A Energy Converter (4)
- IV circuit + IV hull → IV 4A Energy Converter (1 + 1)

## How to build

1. Drawers first: silver, copper, electrum and redstone dust, one drawer each, and a helium drum. Each mixer gets its own pair of drawers through Modular Router or Pipez routes with Item Filters; the two LV mixers differ only in their ghost circuit (3 and 1), so they are two machines. — `functionalstorage:oak_1`, `gtceu:silver_dust`, `gtceu:copper_dust`, `gtceu:electrum_dust`
2. Signalum: LV Mixer, ghost circuit 3: 1 silver + 3 copper + 4 redstone dust → 4 signalum dust in 15 s at 20 EU/t. Keep Exact 64 on the output; three of these dust go into every shellite batch. — `gtceu:lv_mixer`, `gtceu:signalum_dust`
3. Black bronze: LV Mixer, ghost circuit 1: 3 copper + 2 electrum dust → 5 black bronze dust in 25 s at 7 EU/t. Keep Exact 16 on the output: one dust per shellite batch. — `gtceu:lv_mixer`, `gtceu:black_bronze_dust`
4. Shellite dust: EV Mixer (1024 EU/t, no ghost circuit needed in the recipe but keep the machine dedicated): 1 black bronze + 3 signalum dust → 4 shellite dust in 35 s. Output drawer with Keep Exact 64. — `gtceu:ev_mixer`, `gtceu:shellite_dust`
5. Dedicated EBF with 16 RTM coil blocks and an IV Energy Hatch: input bus with ghost circuit 1 (circuit 2 plus a 1 B helium hatch for the 67 % recipe), 1 shellite dust → 1 hot shellite ingot in 70 s at 7680 EU/t. Muffler hatch free above it. Do not mix this furnace with other recipes: the coils decide the temperature. — `gtceu:electric_blast_furnace`, `gtceu:rtm_alloy_coil_block`, `gtceu:iv_energy_input_hatch`, `gtceu:hot_shellite_ingot`
6. Vacuum Freezer: Robot Arm from the EBF output into its bus (Item Filter on the hot ingot), 1 ingot per freeze, no coolant. Output drawer with Keep Exact 32. — `gtceu:vacuum_freezer`, `gtceu:shellite_ingot`
7. LV Wiremills, one per size: circuit 1 gives 2 single wires per ingot, circuit 4 gives 1 quadruple wire per 2 ingots. Each output drawer is capped by a Keep Exact arm at 16, because converters need 4 wires of one size. — `gtceu:lv_wiremill`, `gtceu:shellite_single_wire`, `gtceu:shellite_quadruple_wire`
8. Easy to miss: craft the converter in a crafting table: bottom row wire, hull, wire; middle row wire, IV circuit, wire (4 wires, circuit, hull in the pack’s shaped recipe). 8 ingots, 1 circuit and 1 hull for the 4A one; the 1A one is only 2 ingots for its 4 single wires. — `gtceu:iv_4a_energy_converter`, `gtceu:iv_machine_hull`

## Tips

- Shellite (kjs startup superconductors.js, additions/progression/superconductors.js): the IV superconductor, 64 A in a single wire at 8192 V, no cable coating and no loss. Signalum dust: LV Mixer, circuit 3, 1 silver + 3 copper + 4 redstone dust → 4 dust (300 ticks, 20 EU/t). Black bronze dust: mixer, circuit 1, 3 copper + 2 electrum → 5 dust (500 ticks, 7 EU/t). Shellite dust: 1 black bronze + 3 signalum → 4 dust in 700 ticks at 1024 EU/t, which is above the HV 512, so an EV Mixer.
- Blast recipe: 4400 K, gas tier mid (helium), 7680 EU/t (VA\[IV\]), 1400 ticks = 70 s per ingot. 4400 K needs RTM coils (4500 K) and 7680 EU/t needs an IV Energy Hatch on the EBF (the iv\_hatches chain). With circuit 2 and 1 B helium the recipe takes 67 % of the time (about 47 s). The hot ingot then goes through the Vacuum Freezer (below 5000 K: no coolant); the pack sets no freezer numbers, so it uses the default 120 EU/t and a mass-based time.
- Wire: LV Wiremill (30 EU/t, shellite is above 2800 K): circuit 1 = 2 single wires per ingot, circuit 2 = 1 double wire per ingot, circuit 4 = 1 quadruple wire per 2 ingots, circuit 8 = octal (4 ingots), circuit 16 = hex (8 ingots). The pack’s converters use these directly (converters.js): the 1A, 4A, 8A and 16A converters are 4 wires of single, quadruple, octal and hex + 1 circuit + the hull, shaped in a crafting table.
- So the IV 4A Energy Converter = 4 quadruple wires (8 ingots) + 1 IV circuit + 1 IV machine hull, and one shellite ingot costs about 0.54 million EU in the furnace. The 64A converter is an EV Assembler recipe (600 ticks, 1625 EU/t): 16 hex wires (128 ingots) + IV circuit + hull, so plan about 2.5 hours of one furnace. Converters let Thermal dynamos, Lapidary dynamos and flux plugs feed IV machines: FE in, EU out.
- Cost in the mixers: 4 shellite dust need 1 black bronze + 3 signalum, i.e. 3 silver-based signalum dust (0.75 silver) and 1 black bronze dust (0.6 copper, 0.4 electrum) per 4 dust. The signalum mixer and the shellite mixer are separate machines; the two mixers on circuit 1 and 3 must not share a bus.
- Where else shellite goes: the shellite casing and frame (kjs casings.js) in late multiblocks, the thermal augment kits of the IV tier (thermal\_augments.js), the Hellforge and the stargate parts. None are IV goals, so make wire and the 4A converter first.
- Sub-steps people skip: (1) the hot ingot must be frozen, a shellite wire never accepts it; (2) each wire size has its own circuit, so build one wiremill per size you actually need (single for the 1A converter, quadruple for 4A); (3) the EBF needs the IV hatch AND RTM coils: a Nichrome EBF with an IV hatch still refuses the 4400 K recipe; (4) the mixer for shellite takes the dust, not the ingots, of black bronze and signalum.
- **Unverified** the vacuum freezer time and power for shellite (default values assumed), and the helium amount per ingot (read as 1000 mB from the jar).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_mixer` | 2 |
| `gtceu:ev_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:rtm_alloy_coil_block` | 16 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:lv_wiremill` | 2 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](iv_components.md)
- **Main source for:** `gtceu:shellite_ingot`, `gtceu:shellite_single_wire`
