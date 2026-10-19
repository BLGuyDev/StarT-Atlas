---
kind: chain
id: abs_super_ebf
order: 1150
data:
  t: Alloy Blast Smelter (alloy dust → molten metal in one step) and the Super EBF
  inf: true
  "n":
    - - cp
      - |-
        Controller: 4 tantalum carbide plate + 2 EV circuit + 2 aluminium cable + EV Alloy Smelter
      - g
      - functionalstorage:oak_1
      - - [Tantalum carbide plate, "gtceu:tantalum_carbide_plate"]
        - [EV circuit, "gtceu:micro_processor_computer"]
        - [Aluminium single cable, "gtceu:aluminium_single_cable"]
        - [EV Alloy Smelter, "gtceu:ev_alloy_smelter"]
    - - hp
      - |-
        20 crafts of 2 casings: 4 titanium carbide plate + 2 HSLA steel plate + tungsten carbide frame (circuit 6)
      - g
      - functionalstorage:oak_1
      - - [Titanium carbide plate, "gtceu:titanium_carbide_plate"]
        - [HSLA steel plate, "gtceu:hsla_steel_plate"]
        - [Tungsten carbide frame, "gtceu:tungsten_carbide_frame"]
        - [Casing, "gtceu:high_temperature_smelting_casing"]
    - - vp
      - |-
        6 crafts of 2 vents: 4 tantalum carbide plate + 2 MoSi2 double plate + 2 titanium rotor + MoSi2 long rod
      - g
      - functionalstorage:oak_1
      - - [Tantalum carbide plate, "gtceu:tantalum_carbide_plate"]
        - [Molybdenum disilicide double plate, "gtceu:double_molybdenum_disilicide_plate"]
        - [Titanium rotor, "gtceu:titanium_rotor"]
        - [Heat vent, "gtceu:heat_vent"]
    - [ab, "Alloy Blast Smelter · 40 casings, 24 coils, 12 vents, muffler", m, "gtceu:alloy_blast_smelter"]
    - - ds
      - "1 Steel dust + 1 tungsten dust · circuit 2"
      - g
      - functionalstorage:oak_1
      - [[Steel dust, "gtceu:steel_dust"], [Tungsten dust, "gtceu:tungsten_dust"]]
    - [he, "Helium · 2 B (circuit 12, 67 % time)", f, "gtceu:helium_bucket"]
    - [mt, "288 mB molten tungsten steel · 75 s · 1920 EU/t", f, "gtceu:tungsten_steel_bucket"]
    - [vf, "Vacuum Freezer · ingot mold · mass x 3 ticks", m, "gtceu:vacuum_freezer"]
    - [ts, "2 Tungsten steel ingot", o, "gtceu:tungsten_steel_ingot"]
    - - sc
      - |-
        Super EBF controller: EBF + 2 IV circuit + EV sensor + 2 small tungsten spring + 2 aluminium double cable + double black steel plate
      - g
      - functionalstorage:oak_1
      - - [Electric Blast Furnace, "gtceu:electric_blast_furnace"]
        - [EV sensor, "gtceu:ev_sensor"]
        - [Small tungsten spring, "gtceu:small_tungsten_spring"]
        - [Double black steel plate, "gtceu:double_black_steel_plate"]
    - - hf
      - Hardened Industrial Furnace (Super EBF) · 40 coils, 32 casings, 24 firebox, 20 black steel frames, 12 vents, 8 pipe casings
      - m
      - gtceu:super_ebf
  e:
    - [cp, ab, controller]
    - [hp, ab, "40"]
    - [vp, ab, "12"]
    - [ds, ab, "1 + 1"]
    - [he, ab, optional]
    - [ab, mt, "288 mB"]
    - [mt, vf, "144 mB each"]
    - [vf, ts, "2"]
    - [sc, hf, controller]
    - [hp, hf, "32"]
    - [vp, hf, "12"]
  tips:
    - |-
      The Alloy Blast Smelter is an EV craft, not an IV one: the controller is 4 tantalum carbide plates + 2 EV circuits + 2 aluminium cables + an EV Alloy Smelter (GCYMRecipes.java:105), so build it as soon as the carbide lines run. The boosted version (super_abs, Chambered Alloy Transmuter) is a ZPM assembly-line item, do not confuse them.
    - |-
      What the ABS does (AlloyBlastRecipeProducer, applied to every alloy that has a blast temperature): the same inputs as the EBF alloy mix, but straight as dusts in the bus (1 dust of each component, no mixer), circuit = number of components, output molten metal of N ingots (144 mB each) in 3/4 of the EBF time times N. With 1 B of helium per ingot and circuit +10 it takes 67 % of that time. The coil tier must still meet the blast temperature.
    - |-
      Worked examples (all verified from material blast data): tungsten steel, 1 steel + 1 tungsten dust, circuit 2: 288 mB in 1500 ticks (75 s) at 1920 EU/t, 3000 K. RTM alloy, 4 ruthenium + 2 tungsten + 1 molybdenum, circuit 3: 1008 mB in 7350 ticks (6 min 7 s), 1920 EU/t, 3000 K, 52.5 s per ingot against 70 s in the EBF plus the mixer. Nichrome, 4 nickel + 1 chromium, circuit 2: 720 mB in 4875 ticks (4 min 4 s), 1920 EU/t, 2700 K.
    - |-
      Molten metal needs the Vacuum Freezer with the ingot mold (the freezer recipe takes 144 mB → 1 ingot in mass x 3 ticks, no helium below 5000 K). Molten tungsten steel is also what the LV Fluid Solidifier turns into rotors and pipes. Unverified: the freezer EU/t of those fluid recipes (the source leaves it unset); copy the 480 EU/t of the solid ingot freezing and check it in EMI.
    - |-
      ABS structure (multis card): 40 High Temperature Smelting Casings (at least 30, hatches may replace the rest), 24 heating coils of any tier (the tier sets the allowed temperature), 12 heat vents, 1 muffler hatch. The casing recipe gives 2 per craft: 4 titanium carbide plates + 2 HSLA steel plates + 1 tungsten carbide frame, circuit 6, 50 ticks at 16 EU/t (GCYMRecipes). The heat vent: 4 tantalum carbide plates + 2 molybdenum disilicide double plates + 2 titanium rotors + 1 molybdenum disilicide long rod, 2 per craft (crafting table). Controller recipe: 4 tantalum carbide plates + 2 EV circuits + 2 aluminium cables + 1 EV Alloy Smelter (GCYMRecipes).
    - |-
      Materials from EV mixers (GCYMRecipes): tantalum carbide = 1 tantalum + 1 carbon dust → 2 (150 ticks, 1920 EU/t); titanium carbide = 1 titanium + 1 carbon, circuit 3 → 2 (160 ticks); molybdenum disilicide = 1 molybdenum + 2 silicon → 3 (180 ticks); HSLA steel = HV Mixer (140 ticks, 480 EU/t): 2 invar + 1 vanadium + 1 titanium + 1 molybdenum → 5; tungsten carbide = tungsten + carbon, circuit 2 → 2. Tantalum: crushed tantalite from the sieve with a diamond mesh (5 %, kjs sieving.js). Unverified: the EBF temperatures of these carbides and of HSLA steel, read the recipe in EMI before building the blast part.
    - |-
      Super EBF (Hardened Industrial Furnace, kjs startup super_ebf.js): runs plain Electric Blast Furnace recipes with the EBF overclock, a StarT throughput modifier and batch mode, but accepts exactly ONE energy hatch and exactly one maintenance hatch. Structure: 40 heating coils, 32 high temperature smelting casings (at least 5, buses and hatches replace the rest), 24 steel firebox casings, 20 black steel frames, 12 heat vents, 8 steel pipe casings, 1 muffler. Controller (shaped): 1 EBF + 2 IV circuits + 1 EV sensor + 2 small tungsten springs + 2 aluminium double cables + 1 double black steel plate.
    - |-
      The Super EBF (HIF) is an IV craft: 2 IV circuits + EBF + EV sensor + black steel parts, so it exists well before LuV. It runs any EBF recipe, so with HSS-G coils (5400 K) it makes naquadah (5000 K, 7680 EU/t, 30 s); trinium (7200 K, LuV hatch) and naquadria (9000 K, ZPM hatch) need naquadah coils or better, and europium (6000 K, 7680 EU/t) needs naquadah coils too. The naquadah coil block is an assembler recipe at 30 720 EU/t, so a LuV-class machine can build it as soon as naquadah exists.
    - |-
      Which one when: the ABS is for alloys and gives molten metal (needs a freezer step), and runs unboosted EBF recipes at 75 % time. The Super EBF is for plain EBF recipes (a single metal ingot such as iridium or tungsten) and boosts throughput. Unverified: the factor of the throughput modifier; read the multiblock tooltip in game.
    - |-
      Sub-steps people skip: (1) coils are counted for temperature, not for the casing number, so put the best coil in; (2) a muffler hatch with free space above it is mandatory in both; (3) one energy hatch only in the Super EBF, so use a hatch that fits the recipe voltage (an EV one for 1920 EU/t, an IV one for 7680 EU/t); (4) black steel frames and firebox casings are separate crafts; (5) set the circuit by the component count, or by +10 when helium is in the hatch.
    - |-
      Unverified: whether the ABS recipes need exactly the molten tank to be empty between alloys, and the recipe of the muffler hatch at these tiers.
  b:
    - ["gtceu:alloy_blast_smelter", 1]
    - ["gtceu:super_ebf", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:nichrome_coil_block", 64]
    - ["gtceu:ev_energy_input_hatch", 2]
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:ev_mixer", 1]
    - ["gtceu:mv_assembler", 2]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:steel_dust", "gtceu:tungsten_dust", "gtceu:helium_bucket"]
      t: |-
        Input drawers first: one per dust (steel, tungsten, later RTM parts), a helium drum with a pump cover, and an output drum for each molten metal. The Alloy Blast Smelter takes dust directly from an input bus with a ghost circuit set to the number of components; one recipe per circuit, so keep one smelter per alloy line.
    - i:
        - gtceu:ev_mixer
        - gtceu:tantalum_carbide_dust
        - gtceu:titanium_carbide_dust
        - gtceu:molybdenum_disilicide_dust
      t: |-
        Make the blast-proof materials first, in EV Mixers: tantalum carbide (1 tantalum + 1 carbon, no circuit), titanium carbide (circuit 3), molybdenum disilicide (1 molybdenum + 2 silicon), tungsten carbide (circuit 2). HSLA steel in the HV Mixer. Each dust is smelted or blasted into ingots, then bent into plates and double plates: one mixer per recipe, never one mixer with changing circuits.
    - i: ["gtceu:mv_assembler", "gtceu:high_temperature_smelting_casing", "gtceu:tungsten_carbide_frame"]
      t: |-
        Casings: MV Assembler with ghost circuit 6 (16 EU/t): 4 titanium carbide plates + 2 HSLA steel plates + 1 tungsten carbide frame → 2 High Temperature Smelting Casings in 2.5 s. 40 casings for the ABS and 32 more for a Super EBF is 36 crafts. Frames: assembler, 4 rods + ghost circuit 4 → 1 frame (64 ticks, 7 EU/t).
    - i: ["gtceu:heat_vent", "gtceu:double_molybdenum_disilicide_plate", "gtceu:titanium_rotor"]
      t: |-
        Heat vents, crafted by hand: 4 tantalum carbide plates, 2 molybdenum disilicide double plates, 2 titanium rotors, 1 molybdenum disilicide long rod → 2 vents. 12 for the ABS, 12 more for the Super EBF. Long rod: forge hammer on 2 rods; double plate: bender circuit 2.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:ev_alloy_smelter"]
      t: |-
        Controller by hand: 4 tantalum carbide plates (top and bottom row), 2 EV circuits, 2 aluminium cables, the EV Alloy Smelter in the middle. Build the 24 coils of the ABS with at least the tier of the highest-temperature alloy: Nichrome (3600 K) covers tungsten steel (3000 K), RTM alloy (3000 K) and HSS-G needs RTM coils (4200 K).
    - i: ["gtceu:alloy_blast_smelter", "gtceu:tungsten_steel_bucket", "gtceu:vacuum_freezer"]
      t: |-
        Run the first alloy: 1 steel dust + 1 tungsten dust in the bus, ghost circuit 2, an EV energy hatch (1920 EU/t), 75 s → 288 mB molten tungsten steel in the output hatch. Pump it into a Vacuum Freezer with the ingot mold in its bus slot: each 144 mB → 1 ingot. Add helium (circuit 12 and a helium hatch) to cut the time to 67 %.
    - i: ["gtceu:super_ebf", "gtceu:black_steel_frame", "gtceu:steel_firebox_casing"]
      t: |-
        Super EBF: controller shaped from an EBF + 2 IV circuits + EV sensor + 2 small tungsten springs (bender, 1 tungsten rod → 2) + 2 aluminium double cables + a double black steel plate. Build 40 coils, 32 casings, 24 steel firebox casings, 20 black steel frames, 8 steel pipe casings and 12 heat vents, with exactly one energy hatch. Use it for single-metal EBF recipes at IV power.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:rtm_alloy_dust"]
      t: |-
        Easy to miss: the ABS also makes RTM alloy and nichrome without the mixer (circuit 3 and 2). Once it runs, the mixer and the first EBF of the tungsten, RTM and nichrome lines are replaced; keep the mixers for the Super EBF recipes that want dust.
---
# Alloy Blast Smelter (alloy dust → molten metal in one step) and the Super EBF

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `abs_super_ebf` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [Tungsten and tungsten steel](../../plan/p10.md#tungsten)

**Tips:** 11, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-ab">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · 40 casings, 24 coils, 12 vents, muffler</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Controller: 4 tantalum carbide plate + 2 EV circuit + 2 aluminium cable + EV Alloy Smelter (functionalstorage:oak_1) - controller"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Controller: 4 tantalum carbide plate + 2 EV circuit + 2 aluminium cable + EV Alloy Smelter</span><span class="gt-sub"><span>Tantalum carbide plate</span><span>EV circuit</span><span>Aluminium single cable</span><span>EV Alloy Smelter</span></span><b class="gt-q">controller</b></span><span class="gt-slot gt-group" title="20 crafts of 2 casings: 4 titanium carbide plate + 2 HSLA steel plate + tungsten carbide frame (circuit 6) (functionalstorage:oak_1) - 40"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">20 crafts of 2 casings: 4 titanium carbide plate + 2 HSLA steel plate + tungsten carbide frame (circuit 6)</span><span class="gt-sub"><span>Titanium carbide plate</span><span>HSLA steel plate</span><span>Tungsten carbide frame</span><span>Casing</span></span><b class="gt-q">40</b></span><span class="gt-slot gt-group" title="6 crafts of 2 vents: 4 tantalum carbide plate + 2 MoSi2 double plate + 2 titanium rotor + MoSi2 long rod (functionalstorage:oak_1) - 12"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 crafts of 2 vents: 4 tantalum carbide plate + 2 MoSi2 double plate + 2 titanium rotor + MoSi2 long rod</span><span class="gt-sub"><span>Tantalum carbide plate</span><span>Molybdenum disilicide double plate</span><span>Titanium rotor</span><span>Heat vent</span></span><b class="gt-q">12</b></span><span class="gt-slot gt-group" title="1 Steel dust + 1 tungsten dust · circuit 2 (functionalstorage:oak_1) - 1 + 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 Steel dust + 1 tungsten dust · circuit 2</span><span class="gt-sub"><span>Steel dust</span><span>Tungsten dust</span></span><b class="gt-q">1 + 1</b></span><span class="gt-slot gt-fluid" title="Helium · 2 B (circuit 12, 67 % time) (gtceu:helium_bucket) - optional"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium · 2 B (circuit 12, 67 % time)</span><b class="gt-q">optional</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="288 mB molten tungsten steel · 75 s · 1920 EU/t (gtceu:tungsten_steel_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel</span><span class="gt-note">288 mB molten tungsten steel · 75 s · 1920 EU/t</span><b class="gt-q">288 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · ingot mold · mass x 3 ticks</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="288 mB molten tungsten steel · 75 s · 1920 EU/t (gtceu:tungsten_steel_bucket) - 144 mB each"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel</span><span class="gt-note">288 mB molten tungsten steel · 75 s · 1920 EU/t</span><b class="gt-q">144 mB each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 Tungsten steel ingot (gtceu:tungsten_steel_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Ingot</span><span class="gt-note">2 Tungsten steel ingot</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-hf">
<div class="gt-head"><span class="gt-mname">Hardened Industrial Furnace (Super EBF) · 40 coils, 32 casings, 24 firebox, 20 black steel frames, 12 vents, 8 pipe casings</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Super EBF controller: EBF + 2 IV circuit + EV sensor + 2 small tungsten spring + 2 aluminium double cable + double black steel plate (functionalstorage:oak_1) - controller"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Super EBF controller: EBF + 2 IV circuit + EV sensor + 2 small tungsten spring + 2 aluminium double cable + double black steel plate</span><span class="gt-sub"><span>Electric Blast Furnace</span><span>EV sensor</span><span>Small tungsten spring</span><span>Double black steel plate</span></span><b class="gt-q">controller</b></span><span class="gt-slot gt-group" title="20 crafts of 2 casings: 4 titanium carbide plate + 2 HSLA steel plate + tungsten carbide frame (circuit 6) (functionalstorage:oak_1) - 32"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">20 crafts of 2 casings: 4 titanium carbide plate + 2 HSLA steel plate + tungsten carbide frame (circuit 6)</span><span class="gt-sub"><span>Titanium carbide plate</span><span>HSLA steel plate</span><span>Tungsten carbide frame</span><span>Casing</span></span><b class="gt-q">32</b></span><span class="gt-slot gt-group" title="6 crafts of 2 vents: 4 tantalum carbide plate + 2 MoSi2 double plate + 2 titanium rotor + MoSi2 long rod (functionalstorage:oak_1) - 12"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 crafts of 2 vents: 4 tantalum carbide plate + 2 MoSi2 double plate + 2 titanium rotor + MoSi2 long rod</span><span class="gt-sub"><span>Tantalum carbide plate</span><span>Molybdenum disilicide double plate</span><span>Titanium rotor</span><span>Heat vent</span></span><b class="gt-q">12</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__super_ebf.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:super_ebf</code></div>
</div>
</div>

## Flow

- [Alloy Blast Smelter · 40 casings, 24 coils, 12 vents, muffler](#m-ab) → [Vacuum Freezer · ingot mold · mass x 3 ticks](#m-vf)
- [Hardened Industrial Furnace (Super EBF) · 40 coils, 32 casings, 24 firebox, 20 black steel frames, 12 vents, 8 pipe casings](#m-hf)

## How to build

1. Input drawers first: one per dust (steel, tungsten, later RTM parts), a helium drum with a pump cover, and an output drum for each molten metal. The Alloy Blast Smelter takes dust directly from an input bus with a ghost circuit set to the number of components; one recipe per circuit, so keep one smelter per alloy line. — `functionalstorage:oak_1`, `gtceu:steel_dust`, `gtceu:tungsten_dust`, `gtceu:helium_bucket`
2. Make the blast-proof materials first, in EV Mixers: tantalum carbide (1 tantalum + 1 carbon, no circuit), titanium carbide (circuit 3), molybdenum disilicide (1 molybdenum + 2 silicon), tungsten carbide (circuit 2). HSLA steel in the HV Mixer. Each dust is smelted or blasted into ingots, then bent into plates and double plates: one mixer per recipe, never one mixer with changing circuits. — `gtceu:ev_mixer`, `gtceu:tantalum_carbide_dust`, `gtceu:titanium_carbide_dust`, `gtceu:molybdenum_disilicide_dust`
3. Casings: MV Assembler with ghost circuit 6 (16 EU/t): 4 titanium carbide plates + 2 HSLA steel plates + 1 tungsten carbide frame → 2 High Temperature Smelting Casings in 2.5 s. 40 casings for the ABS and 32 more for a Super EBF is 36 crafts. Frames: assembler, 4 rods + ghost circuit 4 → 1 frame (64 ticks, 7 EU/t). — `gtceu:mv_assembler`, `gtceu:high_temperature_smelting_casing`, `gtceu:tungsten_carbide_frame`
4. Heat vents, crafted by hand: 4 tantalum carbide plates, 2 molybdenum disilicide double plates, 2 titanium rotors, 1 molybdenum disilicide long rod → 2 vents. 12 for the ABS, 12 more for the Super EBF. Long rod: forge hammer on 2 rods; double plate: bender circuit 2. — `gtceu:heat_vent`, `gtceu:double_molybdenum_disilicide_plate`, `gtceu:titanium_rotor`
5. Controller by hand: 4 tantalum carbide plates (top and bottom row), 2 EV circuits, 2 aluminium cables, the EV Alloy Smelter in the middle. Build the 24 coils of the ABS with at least the tier of the highest-temperature alloy: Nichrome (3600 K) covers tungsten steel (3000 K), RTM alloy (3000 K) and HSS-G needs RTM coils (4200 K). — `gtceu:alloy_blast_smelter`, `gtceu:ev_alloy_smelter`
6. Run the first alloy: 1 steel dust + 1 tungsten dust in the bus, ghost circuit 2, an EV energy hatch (1920 EU/t), 75 s → 288 mB molten tungsten steel in the output hatch. Pump it into a Vacuum Freezer with the ingot mold in its bus slot: each 144 mB → 1 ingot. Add helium (circuit 12 and a helium hatch) to cut the time to 67 %. — `gtceu:alloy_blast_smelter`, `gtceu:tungsten_steel_bucket`, `gtceu:vacuum_freezer`
7. Super EBF: controller shaped from an EBF + 2 IV circuits + EV sensor + 2 small tungsten springs (bender, 1 tungsten rod → 2) + 2 aluminium double cables + a double black steel plate. Build 40 coils, 32 casings, 24 steel firebox casings, 20 black steel frames, 8 steel pipe casings and 12 heat vents, with exactly one energy hatch. Use it for single-metal EBF recipes at IV power. — `gtceu:super_ebf`, `gtceu:black_steel_frame`, `gtceu:steel_firebox_casing`
8. Easy to miss: the ABS also makes RTM alloy and nichrome without the mixer (circuit 3 and 2). Once it runs, the mixer and the first EBF of the tungsten, RTM and nichrome lines are replaced; keep the mixers for the Super EBF recipes that want dust. — `gtceu:alloy_blast_smelter`, `gtceu:rtm_alloy_dust`

## Tips

- The Alloy Blast Smelter is an EV craft, not an IV one: the controller is 4 tantalum carbide plates + 2 EV circuits + 2 aluminium cables + an EV Alloy Smelter (GCYMRecipes.java:105), so build it as soon as the carbide lines run. The boosted version (super\_abs, Chambered Alloy Transmuter) is a ZPM assembly-line item, do not confuse them.
- What the ABS does (AlloyBlastRecipeProducer, applied to every alloy that has a blast temperature): the same inputs as the EBF alloy mix, but straight as dusts in the bus (1 dust of each component, no mixer), circuit = number of components, output molten metal of N ingots (144 mB each) in 3/4 of the EBF time times N. With 1 B of helium per ingot and circuit +10 it takes 67 % of that time. The coil tier must still meet the blast temperature.
- Worked examples (all verified from material blast data): tungsten steel, 1 steel + 1 tungsten dust, circuit 2: 288 mB in 1500 ticks (75 s) at 1920 EU/t, 3000 K. RTM alloy, 4 ruthenium + 2 tungsten + 1 molybdenum, circuit 3: 1008 mB in 7350 ticks (6 min 7 s), 1920 EU/t, 3000 K, 52.5 s per ingot against 70 s in the EBF plus the mixer. Nichrome, 4 nickel + 1 chromium, circuit 2: 720 mB in 4875 ticks (4 min 4 s), 1920 EU/t, 2700 K.
- Molten metal needs the Vacuum Freezer with the ingot mold (the freezer recipe takes 144 mB → 1 ingot in mass x 3 ticks, no helium below 5000 K). Molten tungsten steel is also what the LV Fluid Solidifier turns into rotors and pipes. Unverified: the freezer EU/t of those fluid recipes (the source leaves it unset); copy the 480 EU/t of the solid ingot freezing and check it in EMI.
- ABS structure (multis card): 40 High Temperature Smelting Casings (at least 30, hatches may replace the rest), 24 heating coils of any tier (the tier sets the allowed temperature), 12 heat vents, 1 muffler hatch. The casing recipe gives 2 per craft: 4 titanium carbide plates + 2 HSLA steel plates + 1 tungsten carbide frame, circuit 6, 50 ticks at 16 EU/t (GCYMRecipes). The heat vent: 4 tantalum carbide plates + 2 molybdenum disilicide double plates + 2 titanium rotors + 1 molybdenum disilicide long rod, 2 per craft (crafting table). Controller recipe: 4 tantalum carbide plates + 2 EV circuits + 2 aluminium cables + 1 EV Alloy Smelter (GCYMRecipes).
- Materials from EV mixers (GCYMRecipes): tantalum carbide = 1 tantalum + 1 carbon dust → 2 (150 ticks, 1920 EU/t); titanium carbide = 1 titanium + 1 carbon, circuit 3 → 2 (160 ticks); molybdenum disilicide = 1 molybdenum + 2 silicon → 3 (180 ticks); HSLA steel = HV Mixer (140 ticks, 480 EU/t): 2 invar + 1 vanadium + 1 titanium + 1 molybdenum → 5; tungsten carbide = tungsten + carbon, circuit 2 → 2. Tantalum: crushed tantalite from the sieve with a diamond mesh (5 %, kjs sieving.js). Unverified: the EBF temperatures of these carbides and of HSLA steel, read the recipe in EMI before building the blast part.
- Super EBF (Hardened Industrial Furnace, kjs startup super\_ebf.js): runs plain Electric Blast Furnace recipes with the EBF overclock, a StarT throughput modifier and batch mode, but accepts exactly ONE energy hatch and exactly one maintenance hatch. Structure: 40 heating coils, 32 high temperature smelting casings (at least 5, buses and hatches replace the rest), 24 steel firebox casings, 20 black steel frames, 12 heat vents, 8 steel pipe casings, 1 muffler. Controller (shaped): 1 EBF + 2 IV circuits + 1 EV sensor + 2 small tungsten springs + 2 aluminium double cables + 1 double black steel plate.
- The Super EBF (HIF) is an IV craft: 2 IV circuits + EBF + EV sensor + black steel parts, so it exists well before LuV. It runs any EBF recipe, so with HSS-G coils (5400 K) it makes naquadah (5000 K, 7680 EU/t, 30 s); trinium (7200 K, LuV hatch) and naquadria (9000 K, ZPM hatch) need naquadah coils or better, and europium (6000 K, 7680 EU/t) needs naquadah coils too. The naquadah coil block is an assembler recipe at 30 720 EU/t, so a LuV-class machine can build it as soon as naquadah exists.
- Which one when: the ABS is for alloys and gives molten metal (needs a freezer step), and runs unboosted EBF recipes at 75 % time. The Super EBF is for plain EBF recipes (a single metal ingot such as iridium or tungsten) and boosts throughput. Unverified: the factor of the throughput modifier; read the multiblock tooltip in game.
- Sub-steps people skip: (1) coils are counted for temperature, not for the casing number, so put the best coil in; (2) a muffler hatch with free space above it is mandatory in both; (3) one energy hatch only in the Super EBF, so use a hatch that fits the recipe voltage (an EV one for 1920 EU/t, an IV one for 7680 EU/t); (4) black steel frames and firebox casings are separate crafts; (5) set the circuit by the component count, or by +10 when helium is in the hatch.
- **Unverified** whether the ABS recipes need exactly the molten tank to be empty between alloys, and the recipe of the muffler hatch at these tiers.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:alloy_blast_smelter` | 1 |
| `gtceu:super_ebf` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:nichrome_coil_block` | 64 |
| `gtceu:ev_energy_input_hatch` | 2 |
| `gtceu:mv_mixer` | 1 |
| `gtceu:ev_mixer` | 1 |
| `gtceu:mv_assembler` | 2 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:alloy_blast_smelter`, `gtceu:super_ebf`
