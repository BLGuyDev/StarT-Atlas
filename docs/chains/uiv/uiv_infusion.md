---
kind: chain
id: uiv_infusion
order: 2160
data:
  t: |-
    Draco Infusion: controller (Assembly Line) and its 7-input recipes: draconic stem, brain and scale cells, draconic eye, dragon egg → dragon breath
  inf: true
  "n":
    - - g0
      - |-
        Draco Infusion controller: 1 void frame · 6 uev robot arm · 2 uev field generator · 6 dense nyanium plate · 1 uev electric pump · 64 uepic chip · 48 fine enriched pallarovium alloy wire · 3 echo shard lens · 57 600 mB naquadated soldering alloy · 21 600 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 500 mB dragon breath
      - g
      - functionalstorage:oak_1
      - - [void frame, "gtceu:void_frame"]
        - [uev robot arm, "gtceu:uev_robot_arm"]
        - [uev field generator, "gtceu:uev_field_generator"]
        - [dense nyanium plate, "gtceu:dense_nyanium_plate"]
        - [uev electric pump, "gtceu:uev_electric_pump"]
        - [uepic chip, "kubejs:uepic_chip"]
    - [al, "Assembly Line · 2 min · 7 864 320 EU/t · research Dragon Head 216 CWU/t", m, "gtceu:assembly_line"]
    - [di, Draco Infusion, x, "gtceu:draco_infusion"]
    - - r1
      - |-
        Stem cells: 32 stem cells (center) · echo shard plate · nether star plate · 4 quantum star · 4 popped chorus fruit · 2 lenses · 125 mB dragon breath · 32 s
      - g
      - functionalstorage:oak_1
      - - [Stem cells, "gtceu:stem_cells"]
        - [Quantum star, "gtceu:quantum_star"]
        - [Popped chorus fruit, "minecraft:popped_chorus_fruit"]
    - - r2
      - |-
        Brain matter: 4 draconic stem cells (center) · 8 fine prismalium wire · 16 carbon fibers · runic circuit board · 8 fine borosilicate wire · LuV emitter · wetware board · 10 B ender · 32 s
      - g
      - functionalstorage:oak_1
      - - [Runic circuit board, "kubejs:runic_circuit_board"]
        - [Wetware circuit board, "gtceu:wetware_circuit_board"]
        - [Carbon fibers, "gtceu:carbon_fibers"]
    - - r3
      - |-
        Scale cells: 32 stem cells (center) · dense plates of naquadah alloy, tungsten steel, ancient netherite, darmstadtium, obsidian, magnetic steel · 6804 mB neutronium · 128 s
      - g
      - functionalstorage:oak_1
      - - [Dense darmstadtium plate, "gtceu:dense_darmstadtium_plate"]
        - [Dense obsidian plate, "gtceu:dense_obsidian_plate"]
        - [Dense ancient netherite plate, "gtceu:dense_ancient_netherite_plate"]
    - - r4
      - |-
        Draconic eye: quantum eye (center) · ZPM sensor · double abyssal alloy plate · 2 scale + 2 stem cells · 4 draconyallium foil · 2 decaying star · 12.5 B dragon breath · 20 s
      - g
      - functionalstorage:oak_1
      - - [Quantum eye, "gtceu:quantum_eye"]
        - [Double abyssal alloy plate, "gtceu:double_abyssal_alloy_plate"]
        - [Decaying star, "kubejs:decaying_star"]
    - - r5
      - |-
        Dragon egg: 32 draconic stem cells (center) · pure + ancient netherite foil · void plate · abyssal alloy plate · dense naquadria + enriched naquadah plates · 1008 mB draconyallium · 45 s
      - g
      - functionalstorage:oak_1
      - - [Pure netherite foil, "gtceu:pure_netherite_foil"]
        - [Void plate, "gtceu:void_plate"]
        - [Abyssal alloy plate, "gtceu:abyssal_alloy_plate"]
    - [o1, "Draconic stem cells (8) · brain matter cells (4) · scale cells (32)", x, "kubejs:draconic_stem_cells"]
    - [o2, Draconic Eye, x, "kubejs:draconic_eye"]
    - [o3, "Dragon Egg → extractor (VHA[UIV], 50 s) → 750 mB dragon breath", o, "minecraft:dragon_egg"]
  e:
    - [g0, al, "1"]
    - [al, di, "1 / 2 min"]
    - [di, r1, recipe]
    - [di, r2, recipe]
    - [di, r3, recipe]
    - [di, r4, recipe]
    - [di, r5, recipe]
    - [r1, o1, "8"]
    - [r2, o1, "4"]
    - [r3, o1, "32"]
    - [r4, o2, "1"]
    - [r5, o3, "1"]
  tips:
    - |-
      Source: kjs systems/draco_infusion.js. Controller (Assembly Line, 2400 ticks, VA[UIV] = 31 457 280 EU/t, station research of a Dragon Head at VA[UEV], 216 CWU/t): void frame + 6 UEV robot arms + 2 UEV field generators + 6 dense nyanium plates + 1 UEV pump + 64 UEPIC chips + 48 fine enriched pallarovium alloy wire + 3 echo shard lenses, 57 600 mB naquadated soldering alloy + 21 600 mB PEDOT:PSS + 500 mB dragon breath. The 15-layer multiblock is in the multis card; the recipe layout is an ordered 7-input infusion around the center item: slot 0 center, then slots 1 to 6 around it (the file lists them in that order).
    - |-
      Recipes: draconic stem cells = 8 for 32 stem cells (center) + echo shard plate + nether star plate + 4 quantum stars + 4 popped chorus fruit + echo shard lens + nether star lens, 125 mB dragon breath, 640 ticks, VHA[UHV] = 983 040 EU/t. Draconic brain matter cells = 4 for 4 draconic stem cells + 8 fine prismalium wire + 16 carbon fibers + runic circuit board + 8 fine borosilicate glass wire + LuV emitter + wetware circuit board, 10 000 mB ender, 640 ticks, VHA[UHV]. Draconic scale cells = 32 for 32 draconic stem cells + dense plates of naquadah alloy, tungsten steel, ancient netherite, darmstadtium, obsidian and magnetic steel, 6804 mB neutronium, 2560 ticks, VHA[UHV]. Draconic eye = quantum eye + ZPM sensor + double abyssal alloy plate + 2 scale cells + 2 stem cells + 4 draconyallium foil + 2 decaying stars, 12 500 mB dragon breath, 400 ticks, VHA[UIV] = 15 728 640 EU/t. Dragon egg = 32 draconic stem cells + pure netherite foil + ancient netherite foil + void plate + abyssal alloy plate + dense naquadria plate + dense enriched naquadah plate, 1008 mB draconyallium, 900 ticks, VHA[UIV]; the extractor turns the egg into 750 mB dragon breath (1000 ticks, VHA[UIV]).
    - |-
      Pre-array parts: popped chorus fruit = heat chamber, chorus fruit + 10 mB oganesson, 2400 ticks, VHA[UV]; true absolute chorus = Assembly Line, voidic core + 1024 popped chorus fruit + 5 000 000 mB ender air, 12 000 ticks (10 min), VHA[UHV], research popped chorus fruit 192 CWU/t; core casing = assembler circuit 7, 6 double aurourium plates + void frame + 2 true absolute chorus + 2 runic wave generators + UEV field generator + UEV emitter, 2400 ticks, VHA[UEV]. The Primordial Infusion (UXV: 3 UXV circuits, pure dragon breath 15 000 mB) is beyond this era; the draconic eye is the key product here: it is the UIV catalyst core item and one goes into every abyssal mainframe.
    - |-
      Dragon breath is the era fluid: 500 mB for the controller, 125 mB per stem cell batch, 12.5 B per eye, 2000 mB per batch of 48 draconic circuit boards, 25 to 500 mB per Draco Circuit Assembler recipe. The only source traced in these scripts is the egg route (egg → 750 mB breath), so every 750 mB costs 32 stem cells and 1008 mB draconyallium. Draconyallium: Hell Forge (uiv_alloys). Unverified whether a second source of dragon breath exists.
    - |-
      Sub-steps people skip: (1) the center item sits in slot 0, items 1 to 6 in the listed order: put each in its own input bus slot with an Item Filter; (2) fluid first, then items; (3) quantum star (4 per stem batch) and nether stars (plate and lens) are the hidden cost; (4) the infusion recipes of UHV outputs (stem, brain, scale) belong to the UHV page: here you only need their results.
    - |-
      Unverified: infusion slot geometry on the controller card, dragon egg re-use (the extractor consumes the egg), the voidic core and runic wave generator recipes.
  b:
    - ["gtceu:draco_infusion", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:uhv_input_bus", 7]
    - ["gtceu:uhv_input_hatch", 3]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uev_robot_arm", "kubejs:uepic_chip"]
      t: |-
        Controller first: drawers for the 6 UEV robot arms, 2 UEV field generators, 64 UEPIC chips, dense nyanium plates, enriched pallarovium alloy wire, echo shard lenses; drums for soldering alloy, PEDOT:PSS, dragon breath. Research the Dragon Head once (216 CWU/t).
    - i: ["gtceu:draco_infusion", "kubejs:draconic_stem_cells"]
      t: |-
        Stem cells first: 32 stem cells in the center slot, plates and lenses in order, dragon breath by Pipez fluid pipe. 8 cells per batch. Output drawer Keep Exact 64: brain, scale, eye and egg all take stem cells.
    - i: ["gtceu:draco_infusion", "kubejs:draconic_brain_matter_cells"]
      t: Brain matter cells (4 stem cells in the center) and scale cells (32 stem cells + 6 dense plates + 6.8 B neutronium). Do them in separate runs; never leave a half-filled slot.
    - i: ["gtceu:draco_infusion", "kubejs:draconic_eye"]
      t: |-
        Draconic eye: quantum eye center, 2 scale + 2 stem cells, 4 draconyallium foil, 2 decaying stars, 12.5 B dragon breath. One eye per abyssal mainframe and per UIV catalyst core.
    - i: ["gtceu:draco_infusion", "minecraft:dragon_egg"]
      t: |-
        Dragon egg: 32 stem cells center + the 6 plates/foils + 1008 mB draconyallium. Then an extractor (VHA[UIV]) for 750 mB dragon breath.
    - i: ["functionalstorage:oak_1", "kubejs:draconic_eye"]
      t: |-
        Drawers: eyes Keep Exact 4, cells Keep Exact 64. These feed uiv_circuits (brain matter cells, eye) and uiv_alloys (dragon breath).
---
# Draco Infusion: controller (Assembly Line) and its 7-input recipes: draconic stem, brain and scale cells, draconic eye, dragon egg → dragon breath

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_infusion` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [Draco Infusion, UIPIC chip, UIV circuits](../../plan/p19.md#uivdraco)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 2 min · 7 864 320 EU/t · research Dragon Head 216 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Draco Infusion controller: 1 void frame · 6 uev robot arm · 2 uev field generator · 6 dense nyanium plate · 1 uev electric pump · 64 uepic chip · 48 fine enriched pallarovium alloy wire · 3 echo shard lens · 57 600 mB naquadated soldering alloy · 21 600 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 500 mB dragon breath (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Draco Infusion controller: 1 void frame · 6 uev robot arm · 2 uev field generator · 6 dense nyanium plate · 1 uev electric pump · 64 uepic chip · 48 fine enriched pallarovium alloy wire · 3 echo shard lens · 57 600 mB naquadated soldering alloy · 21 600 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 500 mB dragon breath</span><span class="gt-sub"><span>void frame</span><span>uev robot arm</span><span>uev field generator</span><span>dense nyanium plate</span><span>uev electric pump</span><span>uepic chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">2 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Draco Infusion (gtceu:draco_infusion) - 1 / 2 min"><img class="gt-ico" src="../../assets/icons/gtceu__draco_infusion.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Draco Infusion</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 2 min · 7 864 320 EU/t · research Dragon Head 216 CWU/t](#m-al)

### Direct steps

- Draco Infusion → Stem cells: 32 stem cells (center) · echo shard plate · nether star plate · 4 quantum star · 4 popped chorus fruit · 2 lenses · 125 mB dragon breath · 32 s (recipe)
- Draco Infusion → Brain matter: 4 draconic stem cells (center) · 8 fine prismalium wire · 16 carbon fibers · runic circuit board · 8 fine borosilicate wire · LuV emitter · wetware board · 10 B ender · 32 s (recipe)
- Draco Infusion → Scale cells: 32 stem cells (center) · dense plates of naquadah alloy, tungsten steel, ancient netherite, darmstadtium, obsidian, magnetic steel · 6804 mB neutronium · 128 s (recipe)
- Draco Infusion → Draconic eye: quantum eye (center) · ZPM sensor · double abyssal alloy plate · 2 scale + 2 stem cells · 4 draconyallium foil · 2 decaying star · 12.5 B dragon breath · 20 s (recipe)
- Draco Infusion → Dragon egg: 32 draconic stem cells (center) · pure + ancient netherite foil · void plate · abyssal alloy plate · dense naquadria + enriched naquadah plates · 1008 mB draconyallium · 45 s (recipe)
- Stem cells: 32 stem cells (center) · echo shard plate · nether star plate · 4 quantum star · 4 popped chorus fruit · 2 lenses · 125 mB dragon breath · 32 s → Draconic stem cells (8) · brain matter cells (4) · scale cells (32) (8)
- Brain matter: 4 draconic stem cells (center) · 8 fine prismalium wire · 16 carbon fibers · runic circuit board · 8 fine borosilicate wire · LuV emitter · wetware board · 10 B ender · 32 s → Draconic stem cells (8) · brain matter cells (4) · scale cells (32) (4)
- Scale cells: 32 stem cells (center) · dense plates of naquadah alloy, tungsten steel, ancient netherite, darmstadtium, obsidian, magnetic steel · 6804 mB neutronium · 128 s → Draconic stem cells (8) · brain matter cells (4) · scale cells (32) (32)
- Draconic eye: quantum eye (center) · ZPM sensor · double abyssal alloy plate · 2 scale + 2 stem cells · 4 draconyallium foil · 2 decaying star · 12.5 B dragon breath · 20 s → Draconic Eye (1)
- Dragon egg: 32 draconic stem cells (center) · pure + ancient netherite foil · void plate · abyssal alloy plate · dense naquadria + enriched naquadah plates · 1008 mB draconyallium · 45 s → Dragon Egg → extractor (VHA\[UIV\], 50 s) → 750 mB dragon breath (1)

## How to build

1. Controller first: drawers for the 6 UEV robot arms, 2 UEV field generators, 64 UEPIC chips, dense nyanium plates, enriched pallarovium alloy wire, echo shard lenses; drums for soldering alloy, PEDOT:PSS, dragon breath. Research the Dragon Head once (216 CWU/t). — `functionalstorage:oak_1`, `gtceu:uev_robot_arm`, `kubejs:uepic_chip`
2. Stem cells first: 32 stem cells in the center slot, plates and lenses in order, dragon breath by Pipez fluid pipe. 8 cells per batch. Output drawer Keep Exact 64: brain, scale, eye and egg all take stem cells. — `gtceu:draco_infusion`, `kubejs:draconic_stem_cells`
3. Brain matter cells (4 stem cells in the center) and scale cells (32 stem cells + 6 dense plates + 6.8 B neutronium). Do them in separate runs; never leave a half-filled slot. — `gtceu:draco_infusion`, `kubejs:draconic_brain_matter_cells`
4. Draconic eye: quantum eye center, 2 scale + 2 stem cells, 4 draconyallium foil, 2 decaying stars, 12.5 B dragon breath. One eye per abyssal mainframe and per UIV catalyst core. — `gtceu:draco_infusion`, `kubejs:draconic_eye`
5. Dragon egg: 32 stem cells center + the 6 plates/foils + 1008 mB draconyallium. Then an extractor (VHA\[UIV\]) for 750 mB dragon breath. — `gtceu:draco_infusion`, `minecraft:dragon_egg`
6. Drawers: eyes Keep Exact 4, cells Keep Exact 64. These feed uiv\_circuits (brain matter cells, eye) and uiv\_alloys (dragon breath). — `functionalstorage:oak_1`, `kubejs:draconic_eye`

## Tips

- Source: kjs systems/draco\_infusion.js. Controller (Assembly Line, 2400 ticks, VA\[UIV\] = 31 457 280 EU/t, station research of a Dragon Head at VA\[UEV\], 216 CWU/t): void frame + 6 UEV robot arms + 2 UEV field generators + 6 dense nyanium plates + 1 UEV pump + 64 UEPIC chips + 48 fine enriched pallarovium alloy wire + 3 echo shard lenses, 57 600 mB naquadated soldering alloy + 21 600 mB PEDOT:PSS + 500 mB dragon breath. The 15-layer multiblock is in the multis card; the recipe layout is an ordered 7-input infusion around the center item: slot 0 center, then slots 1 to 6 around it (the file lists them in that order).
- Recipes: draconic stem cells = 8 for 32 stem cells (center) + echo shard plate + nether star plate + 4 quantum stars + 4 popped chorus fruit + echo shard lens + nether star lens, 125 mB dragon breath, 640 ticks, VHA\[UHV\] = 983 040 EU/t. Draconic brain matter cells = 4 for 4 draconic stem cells + 8 fine prismalium wire + 16 carbon fibers + runic circuit board + 8 fine borosilicate glass wire + LuV emitter + wetware circuit board, 10 000 mB ender, 640 ticks, VHA\[UHV\]. Draconic scale cells = 32 for 32 draconic stem cells + dense plates of naquadah alloy, tungsten steel, ancient netherite, darmstadtium, obsidian and magnetic steel, 6804 mB neutronium, 2560 ticks, VHA\[UHV\]. Draconic eye = quantum eye + ZPM sensor + double abyssal alloy plate + 2 scale cells + 2 stem cells + 4 draconyallium foil + 2 decaying stars, 12 500 mB dragon breath, 400 ticks, VHA\[UIV\] = 15 728 640 EU/t. Dragon egg = 32 draconic stem cells + pure netherite foil + ancient netherite foil + void plate + abyssal alloy plate + dense naquadria plate + dense enriched naquadah plate, 1008 mB draconyallium, 900 ticks, VHA\[UIV\]; the extractor turns the egg into 750 mB dragon breath (1000 ticks, VHA\[UIV\]).
- Pre-array parts: popped chorus fruit = heat chamber, chorus fruit + 10 mB oganesson, 2400 ticks, VHA\[UV\]; true absolute chorus = Assembly Line, voidic core + 1024 popped chorus fruit + 5 000 000 mB ender air, 12 000 ticks (10 min), VHA\[UHV\], research popped chorus fruit 192 CWU/t; core casing = assembler circuit 7, 6 double aurourium plates + void frame + 2 true absolute chorus + 2 runic wave generators + UEV field generator + UEV emitter, 2400 ticks, VHA\[UEV\]. The Primordial Infusion (UXV: 3 UXV circuits, pure dragon breath 15 000 mB) is beyond this era; the draconic eye is the key product here: it is the UIV catalyst core item and one goes into every abyssal mainframe.
- Dragon breath is the era fluid: 500 mB for the controller, 125 mB per stem cell batch, 12.5 B per eye, 2000 mB per batch of 48 draconic circuit boards, 25 to 500 mB per Draco Circuit Assembler recipe. The only source traced in these scripts is the egg route (egg → 750 mB breath), so every 750 mB costs 32 stem cells and 1008 mB draconyallium. Draconyallium: Hell Forge (uiv\_alloys). Unverified whether a second source of dragon breath exists.
- Sub-steps people skip: (1) the center item sits in slot 0, items 1 to 6 in the listed order: put each in its own input bus slot with an Item Filter; (2) fluid first, then items; (3) quantum star (4 per stem batch) and nether stars (plate and lens) are the hidden cost; (4) the infusion recipes of UHV outputs (stem, brain, scale) belong to the UHV page: here you only need their results.
- **Unverified** infusion slot geometry on the controller card, dragon egg re-use (the extractor consumes the egg), the voidic core and runic wave generator recipes.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:draco_infusion` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:uhv_input_bus` | 7 |
| `gtceu:uhv_input_hatch` | 3 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:draco_infusion`, `kubejs:draconic_eye`, `kubejs:draconic_stem_cells`, `kubejs:draconic_brain_matter_cells`, `kubejs:draconic_scale_cells`, `gtceu:dragon_breath_bucket`
