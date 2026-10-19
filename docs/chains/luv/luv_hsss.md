---
kind: chain
id: luv_hsss
order: 1250
data:
  t: |-
    HSS-S: HSS-G + iridium + osmium → EBF 5000 K (HSS-G coils) → Vacuum Freezer with liquid helium → the LuV component metal
  inf: true
  "n":
    - - g1
      - "6 HSS-G dust · 2 iridium dust · 1 osmium dust"
      - g
      - functionalstorage:oak_1
      - [[HSS-G dust, "gtceu:hssg_dust"], [Iridium dust, "gtceu:iridium_dust"], [Osmium dust, "gtceu:osmium_dust"]]
    - [mx, "IV Mixer · circuit 2 · 25 s · 7680 EU/t", m, "gtceu:iv_mixer"]
    - [d1, "9 HSS-S dust", x, "gtceu:hsss_dust"]
    - [eb, "EBF · HSS-G coils 5400 K · 75 s · 1920 EU/t", m, "gtceu:electric_blast_furnace"]
    - [ht, Hot HSS-S ingot, x, "gtceu:hot_hsss_ingot"]
    - [he, "Helium gas · 1 B", f, "gtceu:helium_bucket"]
    - [v1, "Vacuum Freezer · 12 s · 1920 EU/t", m, "gtceu:vacuum_freezer"]
    - [lh, "Liquid helium · 500 mB per ingot", f, "gtceu:helium_bucket"]
    - [v2, "Vacuum Freezer · 10 s · 1920 EU/t", m, "gtceu:vacuum_freezer"]
    - [oi, HSS-S ingot, o, "gtceu:hsss_ingot"]
    - - ps
      - |-
        Parts: plate · rod · long rod · ring · round · screw · gear · small gear · frame
      - g
      - functionalstorage:oak_1
      - - [HSS-S plate, "gtceu:hsss_plate"]
        - [Long HSS-S rod, "gtceu:long_hsss_rod"]
        - [HSS-S ring, "gtceu:hsss_ring"]
        - [HSS-S round, "gtceu:hsss_round"]
        - [HSS-S gear, "gtceu:hsss_gear"]
        - [HSS-S frame, "gtceu:hsss_frame"]
  e:
    - [g1, mx, "6 + 2 + 1"]
    - [mx, d1, "9 / 25 s"]
    - [d1, eb, "1"]
    - [eb, ht, "1 / 75 s"]
    - [he, v1, "1 B"]
    - [v1, lh, "1 B / 12 s"]
    - [lh, v2, "500 mB"]
    - [ht, v2, "1"]
    - [v2, oi, "1 / 10 s"]
    - [oi, ps, "1"]
  tips:
    - |-
      Recipes (MixerRecipes hsss, HigherDegreeMaterials; the pack does not change them): mixer = 6 HSS-G dust + 2 iridium dust + 1 osmium dust → 9 HSS-S dust, circuit 2, 500 ticks at VA[IV] = 7680 EU/t, so an IV Mixer. EBF: 5000 K, VA[EV] = 1920 EU/t, 1500 ticks (75 s) per ingot, gas tier argon (circuit 2 + argon is 67 % of the time). Hot ingot to the Vacuum Freezer: 200 ticks (10 s) at 1920 EU/t.
    - |-
      Why helium here: every blast material at 5000 K or above freezes with 500 mB LIQUID helium per ingot (MaterialRecipeHandler: temperature >= 5000 K adds 500 mB liquid helium, 250 mB gas helium comes back). HSS-S is exactly 5000 K. Liquid helium: Vacuum Freezer, 1 B helium gas → 1 B liquid helium, 240 ticks (12 s) at 1920 EU/t (ChemistryRecipes). So 2 ingots per B of liquid helium, and the 250 mB returned is almost half: loop it back to the first freezer. Helium comes from the air chain.
    - |-
      Temperature: 5000 K needs HSS-G coils (5400 K, the 5th tier). RTM coils are 4500 K and the hatch bonus (200 K on an EV hatch, 300 K on IV, 400 K on LuV) does not close the gap. That means: HSS-G coil blocks first (8 HSS-G double wire + 8 tungsten carbide foil + 16 borosilicate foil + 144 mB molten tungsten, IV Assembler, 30 s, from the rtm_coil chain tips), 16 per EBF = 128 HSS-G double wires. The EBF also needs an EV hatch for the 1920 EU/t.
    - |-
      HSS-G dust (mixer, 5 tungsten steel + 1 chromium + 2 molybdenum + 1 vanadium → 9 dust, EV Mixer): the MIXER recipe takes dust, not ingots, so no EBF step for HSS-G here. One HSS-S ingot costs 2/3 HSS-G dust, 2/9 iridium and 1/9 osmium: 9 ingots = 6 + 2 + 1. Iridium and osmium come from the platline chain at roughly 1 per 42 platinum group sludge each, so 100 HSS-S ingots eat 22 iridium and 11 osmium (about 900 and 450 sludge). This is why LuV is slower than IV: plan the platline for the whole era and passive it.
    - |-
      Where the metal goes: motor about 5.9 ingots, piston 8.8, pump 2.9 plus the motor, conveyor 5.2, robot arm 11, emitter 6, sensor 6, field generator 8 (plates, rods, frames in HSS-S, ingot equivalents derived from material units). An Assembly Line finishes a part every 30 s, so a line eats up to about 10 to 15 ingots a minute in the worst case; one EBF makes 0.8 ingots a minute, so run 2 or 3 furnaces.
    - |-
      Part machines (standard GregTech, check each in EMI): plate = Bender (circuit 1); rod and round = Lathe; ring, gear and small gear = extruder or alloy smelter with a mold (gear from 4 ingots in the extruder, 8 in the mold); screw = lathe on a bolt; long rod = two rods; frame = from rods. Unverified: the times and the extruder tier for a 5000 K material.
    - |-
      Sub-steps people skip: (1) liquid helium is NOT the same fluid as helium gas: freezer one has gas, freezer two liquid; (2) circuit 2 on the mixer, not 1; (3) iridium and osmium are dusts, not ingots, here (the mixer takes dust); (4) the HSS-S ingot melts into molten HSS-S for the Alloy Blast Smelter: the ABS route (no hot ingot) needs the same coils; (5) keep Keep Exact 16 on the dust drawers so one stuck run does not drain iridium.
    - |-
      Unverified: the Alloy Blast Smelter shortcut for HSS-S (6 + 2 + 1 dusts straight, circuit 3, 75 % of the EBF time per ingot, output 9 x 144 mB molten, then a freezer step with liquid helium), and whether the ABS counts the extra argon gas the same way: read the recipe in EMI before you use it.
  b:
    - ["gtceu:iv_mixer", 1]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:hssg_coil_block", 32]
    - ["gtceu:ev_energy_input_hatch", 3]
    - ["gtceu:vacuum_freezer", 2]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:hv_extruder", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 9]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:hssg_dust", "gtceu:iridium_dust", "gtceu:osmium_dust"]
      t: |-
        Drawers first: HSS-G dust, iridium dust, osmium dust, one drum of helium gas and one of liquid helium. The mixer, the EBF, each freezer and each part machine are one product each, behind their own routers/pipes with Item Filters and Robot Arm covers in Keep Exact mode.
    - i: ["gtceu:iv_mixer", "gtceu:hsss_dust"]
      t: |-
        IV Mixer with circuit 2 in the ghost slot: 6 HSS-G + 2 iridium + 1 osmium dust → 9 HSS-S dust in 25 s at 7680 EU/t. Output into a drawer Keep Exact 32.
    - i: ["gtceu:electric_blast_furnace", "gtceu:hssg_coil_block", "gtceu:ev_energy_input_hatch"]
      t: |-
        EBF: 16 HSS-G coil blocks (5400 K), an EV Energy Hatch, bus with ghost circuit 1 (circuit 2 plus argon for 67 % time), muffler hatch with free air above. 1 dust → 1 hot ingot in 75 s at 1920 EU/t. Run two furnaces for 1.6 ingots a minute.
    - i: ["gtceu:vacuum_freezer", "gtceu:helium_bucket"]
      t: |-
        Helium: first Vacuum Freezer (12 s, 1920 EU/t) turns 1 B helium gas into 1 B liquid helium; pipe it by a Pipez fluid pipe to the second freezer, and pipe the 250 mB gas that comes back into the first one again so the loop only loses what you pull out.
    - i: ["gtceu:vacuum_freezer", "gtceu:hot_hsss_ingot", "gtceu:hsss_ingot"]
      t: |-
        Second Vacuum Freezer: Robot Arm with an Item Filter on the hot ingot from the EBF output, 500 mB liquid helium per ingot, 10 s at 1920 EU/t → HSS-S ingot. Output drawer Keep Exact 32. Never let two hot ingots sit in a bus without helium: the recipe just waits, nothing is lost.
    - i: ["gtceu:lv_bender", "gtceu:lv_lathe", "gtceu:hsss_plate", "gtceu:hsss_round"]
      t: |-
        Parts: one machine per part type (bender for plates and rings, lathe for rods and rounds, extruder for gears and long parts), each with its own input drawer and Keep Exact output. Do not start them all at once: wait for the Assembly Line stage that needs them (luv_components).
    - i: ["gtceu:hssg_coil_block", "gtceu:electric_blast_furnace"]
      t: |-
        Easy to miss: the very first HSS-S needs HSS-G COILS, so upgrade the EBF in the iv rtm_coil chain before you plan this one; with RTM coils the 5000 K recipe is simply refused.
---
# HSS-S: HSS-G + iridium + osmium → EBF 5000 K (HSS-G coils) → Vacuum Freezer with liquid helium → the LuV component metal

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_hsss` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [LuV metals (RPP, ruridit, NbTi, HSS-S)](../../plan/p11.md#luvmetals)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-mx">
<div class="gt-head"><span class="gt-mname">IV Mixer · circuit 2 · 25 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="6 HSS-G dust · 2 iridium dust · 1 osmium dust (functionalstorage:oak_1) - 6 + 2 + 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 HSS-G dust · 2 iridium dust · 1 osmium dust</span><span class="gt-sub"><span>HSS-G dust</span><span>Iridium dust</span><span>Osmium dust</span></span><b class="gt-q">6 + 2 + 1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">25 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="9 HSS-S dust (gtceu:hsss_dust) - 9 / 25 s"><img class="gt-ico" src="../../assets/icons/gtceu__hsss_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hsss Dust</span><span class="gt-note">9 HSS-S dust</span><b class="gt-q">9</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · HSS-G coils 5400 K · 75 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="9 HSS-S dust (gtceu:hsss_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hsss_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hsss Dust</span><span class="gt-note">9 HSS-S dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot HSS-S ingot (gtceu:hot_hsss_ingot) - 1 / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_hsss_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Hsss Ingot</span><span class="gt-note">Hot HSS-S ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-v1">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 12 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Helium gas · 1 B (gtceu:helium_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium gas · 1 B</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Liquid helium · 500 mB per ingot (gtceu:helium_bucket) - 1 B / 12 s"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Liquid helium · 500 mB per ingot</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-v2">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 10 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Liquid helium · 500 mB per ingot (gtceu:helium_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Liquid helium · 500 mB per ingot</span><b class="gt-q">500 mB</b></span><span class="gt-slot" title="Hot HSS-S ingot (gtceu:hot_hsss_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_hsss_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Hsss Ingot</span><span class="gt-note">Hot HSS-S ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HSS-S ingot (gtceu:hsss_ingot) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__hsss_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hsss Ingot</span><span class="gt-note">HSS-S ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [IV Mixer · circuit 2 · 25 s · 7680 EU/t](#m-mx) → [EBF · HSS-G coils 5400 K · 75 s · 1920 EU/t](#m-eb) → [Vacuum Freezer · 10 s · 1920 EU/t](#m-v2)
- [Vacuum Freezer · 12 s · 1920 EU/t](#m-v1) → [Vacuum Freezer · 10 s · 1920 EU/t](#m-v2)

### Direct steps

- HSS-S ingot → Parts: plate · rod · long rod · ring · round · screw · gear · small gear · frame (1)

## How to build

1. Drawers first: HSS-G dust, iridium dust, osmium dust, one drum of helium gas and one of liquid helium. The mixer, the EBF, each freezer and each part machine are one product each, behind their own routers/pipes with Item Filters and Robot Arm covers in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:hssg_dust`, `gtceu:iridium_dust`, `gtceu:osmium_dust`
2. IV Mixer with circuit 2 in the ghost slot: 6 HSS-G + 2 iridium + 1 osmium dust → 9 HSS-S dust in 25 s at 7680 EU/t. Output into a drawer Keep Exact 32. — `gtceu:iv_mixer`, `gtceu:hsss_dust`
3. EBF: 16 HSS-G coil blocks (5400 K), an EV Energy Hatch, bus with ghost circuit 1 (circuit 2 plus argon for 67 % time), muffler hatch with free air above. 1 dust → 1 hot ingot in 75 s at 1920 EU/t. Run two furnaces for 1.6 ingots a minute. — `gtceu:electric_blast_furnace`, `gtceu:hssg_coil_block`, `gtceu:ev_energy_input_hatch`
4. Helium: first Vacuum Freezer (12 s, 1920 EU/t) turns 1 B helium gas into 1 B liquid helium; pipe it by a Pipez fluid pipe to the second freezer, and pipe the 250 mB gas that comes back into the first one again so the loop only loses what you pull out. — `gtceu:vacuum_freezer`, `gtceu:helium_bucket`
5. Second Vacuum Freezer: Robot Arm with an Item Filter on the hot ingot from the EBF output, 500 mB liquid helium per ingot, 10 s at 1920 EU/t → HSS-S ingot. Output drawer Keep Exact 32. Never let two hot ingots sit in a bus without helium: the recipe just waits, nothing is lost. — `gtceu:vacuum_freezer`, `gtceu:hot_hsss_ingot`, `gtceu:hsss_ingot`
6. Parts: one machine per part type (bender for plates and rings, lathe for rods and rounds, extruder for gears and long parts), each with its own input drawer and Keep Exact output. Do not start them all at once: wait for the Assembly Line stage that needs them (luv\_components). — `gtceu:lv_bender`, `gtceu:lv_lathe`, `gtceu:hsss_plate`, `gtceu:hsss_round`
7. Easy to miss: the very first HSS-S needs HSS-G COILS, so upgrade the EBF in the iv rtm\_coil chain before you plan this one; with RTM coils the 5000 K recipe is simply refused. — `gtceu:hssg_coil_block`, `gtceu:electric_blast_furnace`

## Tips

- Recipes (MixerRecipes hsss, HigherDegreeMaterials; the pack does not change them): mixer = 6 HSS-G dust + 2 iridium dust + 1 osmium dust → 9 HSS-S dust, circuit 2, 500 ticks at VA\[IV\] = 7680 EU/t, so an IV Mixer. EBF: 5000 K, VA\[EV\] = 1920 EU/t, 1500 ticks (75 s) per ingot, gas tier argon (circuit 2 + argon is 67 % of the time). Hot ingot to the Vacuum Freezer: 200 ticks (10 s) at 1920 EU/t.
- Why helium here: every blast material at 5000 K or above freezes with 500 mB LIQUID helium per ingot (MaterialRecipeHandler: temperature &gt;= 5000 K adds 500 mB liquid helium, 250 mB gas helium comes back). HSS-S is exactly 5000 K. Liquid helium: Vacuum Freezer, 1 B helium gas → 1 B liquid helium, 240 ticks (12 s) at 1920 EU/t (ChemistryRecipes). So 2 ingots per B of liquid helium, and the 250 mB returned is almost half: loop it back to the first freezer. Helium comes from the air chain.
- Temperature: 5000 K needs HSS-G coils (5400 K, the 5th tier). RTM coils are 4500 K and the hatch bonus (200 K on an EV hatch, 300 K on IV, 400 K on LuV) does not close the gap. That means: HSS-G coil blocks first (8 HSS-G double wire + 8 tungsten carbide foil + 16 borosilicate foil + 144 mB molten tungsten, IV Assembler, 30 s, from the rtm\_coil chain tips), 16 per EBF = 128 HSS-G double wires. The EBF also needs an EV hatch for the 1920 EU/t.
- HSS-G dust (mixer, 5 tungsten steel + 1 chromium + 2 molybdenum + 1 vanadium → 9 dust, EV Mixer): the MIXER recipe takes dust, not ingots, so no EBF step for HSS-G here. One HSS-S ingot costs 2/3 HSS-G dust, 2/9 iridium and 1/9 osmium: 9 ingots = 6 + 2 + 1. Iridium and osmium come from the platline chain at roughly 1 per 42 platinum group sludge each, so 100 HSS-S ingots eat 22 iridium and 11 osmium (about 900 and 450 sludge). This is why LuV is slower than IV: plan the platline for the whole era and passive it.
- Where the metal goes: motor about 5.9 ingots, piston 8.8, pump 2.9 plus the motor, conveyor 5.2, robot arm 11, emitter 6, sensor 6, field generator 8 (plates, rods, frames in HSS-S, ingot equivalents derived from material units). An Assembly Line finishes a part every 30 s, so a line eats up to about 10 to 15 ingots a minute in the worst case; one EBF makes 0.8 ingots a minute, so run 2 or 3 furnaces.
- Part machines (standard GregTech, check each in EMI): plate = Bender (circuit 1); rod and round = Lathe; ring, gear and small gear = extruder or alloy smelter with a mold (gear from 4 ingots in the extruder, 8 in the mold); screw = lathe on a bolt; long rod = two rods; frame = from rods. Unverified: the times and the extruder tier for a 5000 K material.
- Sub-steps people skip: (1) liquid helium is NOT the same fluid as helium gas: freezer one has gas, freezer two liquid; (2) circuit 2 on the mixer, not 1; (3) iridium and osmium are dusts, not ingots, here (the mixer takes dust); (4) the HSS-S ingot melts into molten HSS-S for the Alloy Blast Smelter: the ABS route (no hot ingot) needs the same coils; (5) keep Keep Exact 16 on the dust drawers so one stuck run does not drain iridium.
- **Unverified** the Alloy Blast Smelter shortcut for HSS-S (6 + 2 + 1 dusts straight, circuit 3, 75 % of the EBF time per ingot, output 9 x 144 mB molten, then a freezer step with liquid helium), and whether the ABS counts the extra argon gas the same way: read the recipe in EMI before you use it.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:hssg_coil_block` | 32 |
| `gtceu:ev_energy_input_hatch` | 3 |
| `gtceu:vacuum_freezer` | 2 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_lathe` | 2 |
| `gtceu:hv_extruder` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 9 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Feeds:** [LuV power: Large Gas Turbine with a LuV rotor holder](luv_turbines.md)
- **Main source for:** `gtceu:hsss_ingot`, `gtceu:hsss_dust`, `gtceu:hsss_plate`, `gtceu:hsss_frame`, `gtceu:long_hsss_rod`, `gtceu:hsss_gear`
