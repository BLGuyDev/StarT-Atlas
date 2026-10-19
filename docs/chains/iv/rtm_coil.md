---
kind: chain
id: rtm_coil
order: 1130
data:
  t: |-
    RTM coil: ruthenium + tungsten + molybdenum → RTM alloy → double wire + vanadium steel foil + borosilicate foil + molten nichrome
  inf: true
  "n":
    - [ru, "4 Ruthenium dust", i, "gtceu:ruthenium_dust"]
    - [tu, "2 Tungsten dust", i, "gtceu:tungsten_dust"]
    - [mo, "1 Molybdenum dust", i, "gtceu:molybdenum_dust"]
    - [mx, "EV Mixer · circuit 1 · 15 s · 1920 EU/t", m, "gtceu:ev_mixer"]
    - [rd, "7 RTM alloy dust", x, "gtceu:rtm_alloy_dust"]
    - [he, "Helium · 1 B (optional)", f, "gtceu:helium_bucket"]
    - [eb, "EBF · Nichrome 3000 K · 70 s · 1920 EU/t", m, "gtceu:electric_blast_furnace"]
    - [hr, Hot RTM alloy ingot, x, "gtceu:hot_rtm_alloy_ingot"]
    - [vf, "Vacuum Freezer · 12.5 s · 480 EU/t", m, "gtceu:vacuum_freezer"]
    - [ri, RTM alloy ingot, x, "gtceu:rtm_alloy_ingot"]
    - [wm, "LV Wiremill · circuit 2", m, "gtceu:lv_wiremill"]
    - [dw, "8 RTM alloy double wire", x, "gtceu:rtm_alloy_double_wire"]
    - [vs, "2 Vanadium steel ingot", i, "gtceu:vanadium_steel_ingot"]
    - [b1, "LV Bender · circuit 10 · 1 → 4", m, "gtceu:lv_bender"]
    - [vfo, "8 Vanadium steel foil", x, "gtceu:vanadium_steel_foil"]
    - [bg, "2 Borosilicate glass ingot", i, "gtceu:borosilicate_glass_ingot"]
    - [b2, "LV Bender · circuit 10 · 1 → 4", m, "gtceu:lv_bender"]
    - [bfo, "8 Borosilicate glass foil", x, "gtceu:borosilicate_glass_foil"]
    - [ni, Nichrome ingot, i, "gtceu:nichrome_ingot"]
    - [ex, LV Extractor, m, "gtceu:lv_extractor"]
    - [mn, "144 mB molten nichrome", f, "gtceu:nichrome_bucket"]
    - [as, "EV Assembler · 25 s · 1920 EU/t", m, "gtceu:ev_assembler"]
    - [co, RTM Alloy Coil Block, o, "gtceu:rtm_alloy_coil_block"]
  e:
    - [ru, mx, "4"]
    - [tu, mx, "2"]
    - [mo, mx, "1"]
    - [mx, rd, "7 / 15 s"]
    - [rd, eb, "1"]
    - [he, eb, circuit 2]
    - [eb, hr, "1 / 70 s"]
    - [hr, vf, "1"]
    - [vf, ri, "1 / 12.5 s"]
    - [ri, wm, "8"]
    - [wm, dw, "1 : 1"]
    - [dw, as, "8"]
    - [vs, b1, "2"]
    - [b1, vfo, "8"]
    - [vfo, as, "8"]
    - [bg, b2, "2"]
    - [b2, bfo, "8"]
    - [bfo, as, "8"]
    - [ni, ex, "1"]
    - [ex, mn, "144 mB"]
    - [mn, as, "144 mB"]
    - [as, co, "1 / 25 s"]
  tips:
    - |-
      Coil tiers, verified in the mod jar (CoilBlock$CoilType) and the pack quests: cupronickel 1800 K, kanthal 2700 K, nichrome 3600 K (3rd tier), RTM alloy 4500 K (4th), HSS-G 5400 K (5th), naquadah 7200 K. An EV hatch adds 200 K. Iridium (4500 K), HSS-G (4200 K) and the later hard alloys need RTM; osmium is 4500 K too.
    - |-
      RTM alloy (MixerRecipes): 4 ruthenium dust + 2 tungsten dust + 1 molybdenum dust, circuit 1, 300 ticks at 1920 EU/t → 7 RTM alloy dust (EV Mixer). EBF (FirstDegreeMaterials): 3000 K, VA[EV] = 1920 EU/t, 1400 ticks = 70 s per ingot, nichrome coils are enough; with circuit 2 and 1 B helium the time is 67 % (about 47 s). Hot ingot to the Vacuum Freezer: 250 ticks (12.5 s) at 480 EU/t.
    - |-
      Coil block (kjs coils.js): 8 RTM alloy double wire + 8 vanadium steel foil + 8 borosilicate glass foil + 144 mB molten nichrome → 1 RTM Alloy Coil Block, 500 ticks (25 s) at 1920 EU/t, so an EV Assembler (the nichrome coil was an HV one). Cost per block: 8 RTM ingots (= 4.6 ruthenium, 2.3 tungsten, 1.1 molybdenum), 2 vanadium steel ingots, 2 borosilicate ingots and 1 nichrome ingot.
    - Ruthenium is the bottleneck. One ruthenium needs about 18 platinum group sludge dust (3 centrifuge runs of 2 inert metal mixture each, platline chain), so a 16-coil EBF (128 ingots, 73 ruthenium) is roughly 1300 sludge, about 330 purified cooperite ore. The ZPM Chemical Plant skip (kjs chemical_plant.js) yields 7 ruthenium per 30 ore, which is the late fix.
    - |-
      Vanadium steel: MV Mixer circuit 1, 7 steel + 1 vanadium + 1 chromium dust → 9 dust (400 ticks, 120 EU/t), then an EBF at 1453 K (cupronickel is enough; MV power, about 80 s per ingot, derived from mass x 1453 / 50). Foil: LV Bender, circuit 10, 1 ingot → 4 foil (24 EU/t). Vanadium comes from vanadium magnetite (kjs sieving.js iron mesh 5 % on gravel); chromium from the chromium line.
    - |-
      Borosilicate glass: mixer (ULV recipe, circuit 1): 1 boron dust + 7 glass dust → 8 dust (200 ticks, 7 EU/t); furnace it into an ingot (the quest calls it a glass bar), then an LV Bender on circuit 10 makes 4 foil per ingot (PartsRecipeHandler.processFoil; the foil tag exists in the EMI list). Molybdenum comes from molybdenite (sieve with a diamond mesh on crushed blackstone, 12 %, or the ore factory).
    - |-
      Molten nichrome: LV Extractor, 1 nichrome ingot → 144 mB. Pipe it into the assembler’s fluid hatch through a drum with a pump cover. The same assembler cannot also make the nichrome coil (different foils), so build one assembler per coil type.
    - |-
      HSS-G coil (5th tier, 5400 K) is the same shape: 8 HSS-G double wire + 8 tungsten carbide foil + 16 borosilicate foil + 144 mB molten TUNGSTEN, 600 ticks (30 s) at 7680 EU/t = an IV Assembler. HSS-G: EV Mixer circuit 1, 5 tungsten steel dust + 1 chromium + 2 molybdenum + 1 vanadium → 9 dust (400 ticks); EBF 4200 K, 1920 EU/t, 1300 ticks (65 s), RTM coils needed. Because HSS-G melts at 4200 K the RTM furnace is enough to make it; the HSS-G COIL is first needed for the 5000 K recipes (HSS-S, the naquadah ingot in the EBF) and for 5300 K twinite. Tungsten carbide: EV Mixer circuit 2, 1 tungsten + 1 carbon dust → 2 dust.
    - |-
      Sub-steps people skip: (1) the hot RTM ingot must go through the freezer before the wiremill; (2) the double wire is circuit 2, circuit 1 makes single wires; (3) benders on circuit 10 for foil, never 1 (that makes plates); (4) 16 coil blocks per EBF, so 128 double wires, 128 foil of each kind and 16 nichrome ingots; (5) the EBF needs an EV Energy Hatch, and the EV Assembler (a single machine) needs an EV cable.
    - |-
      Unverified: the vanadium steel EBF time (derived from the formula), the platline yields per ore (derived from PlatGroupMetalsRecipes), and the exact seconds of the bender foil recipes (mass-based).
  b:
    - ["gtceu:ev_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:nichrome_coil_block", 16]
    - ["gtceu:ev_energy_input_hatch", 2]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_bender", 2]
    - ["gtceu:lv_extractor", 1]
    - ["gtceu:ev_assembler", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:ruthenium_dust", "gtceu:tungsten_dust", "gtceu:molybdenum_dust"]
      t: |-
        Input drawers first, one per item: ruthenium dust (from the platinum group line), tungsten dust, molybdenum dust, vanadium steel ingots, borosilicate glass ingots, nichrome ingots. A drum for helium and one for molten nichrome. Every machine below gets a Modular Router or Pipez item pipe with an Item Filter and a Robot Arm Keep Exact cap on its output drawer.
    - i: ["gtceu:ev_mixer", "gtceu:rtm_alloy_dust"]
      t: |-
        EV Mixer with ghost circuit 1, dedicated: 4 ruthenium + 2 tungsten + 1 molybdenum dust → 7 RTM alloy dust in 15 s at 1920 EU/t. The three inputs are three drawers with three filters, since an unfiltered pipe floods the bus with the wrong dust. Keep Exact 64 on the dust output.
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:nichrome_coil_block
        - gtceu:ev_energy_input_hatch
        - gtceu:hot_rtm_alloy_ingot
      t: |-
        Dedicated EBF with 16 Nichrome coil blocks and an EV Energy Hatch. Input bus with ghost circuit 1 (or circuit 2 plus a 1 B helium hatch for the 67 % recipe). 1 RTM dust → 1 hot RTM alloy ingot in 70 s, 1920 EU/t. Let the bus fill and keep it running: 128 ingots for a full RTM furnace is 2.5 hours on one machine.
    - i: ["gtceu:vacuum_freezer", "gtceu:rtm_alloy_ingot"]
      t: |-
        Vacuum Freezer: Robot Arm from the EBF output bus (Item Filter: hot RTM alloy ingot) into its input bus; 1 ingot in 12.5 s at 480 EU/t, no coolant. This is the step people forget, then wonder why the wiremill ignores the ingot. Output into a drawer with Keep Exact at 32.
    - i: ["gtceu:lv_wiremill", "gtceu:rtm_alloy_double_wire"]
      t: |-
        LV Wiremill, ghost circuit 2: 1 RTM alloy ingot → 1 double wire (30 EU/t because the alloy is above 2800 K). One coil needs 8, so cap its drawer at 16.
    - i: ["gtceu:lv_bender", "gtceu:vanadium_steel_foil", "gtceu:borosilicate_glass_foil"]
      t: |-
        Two LV Benders on ghost circuit 10, one per metal: 1 vanadium steel ingot → 4 foil and 1 borosilicate glass ingot → 4 foil (24 EU/t). 2 ingots of each per coil. Vanadium steel ingots come from the MV Mixer + EBF line in the tips; borosilicate dust from the ULV mixer and a furnace.
    - i: ["gtceu:lv_extractor", "gtceu:nichrome_bucket"]
      t: |-
        LV Extractor: 1 nichrome ingot → 144 mB molten nichrome, then a pump cover into a drum beside the assembler. If the drum is empty the assembler runs the item part and then waits, with a full input bus and no output.
    - i: ["gtceu:ev_assembler", "gtceu:rtm_alloy_coil_block"]
      t: |-
        EV Assembler (build it from EV parts: it is 1920 EU/t): 8 RTM double wire + 8 vanadium steel foil + 8 borosilicate glass foil in the input bus, 144 mB molten nichrome in the fluid hatch → 1 RTM Alloy Coil Block in 25 s. Output drawer with Keep Exact 16. Craft one by hand first, it proves the three foils are right.
    - i: ["gtceu:hssg_coil_block", "gtceu:iv_assembler"]
      t: |-
        Easy to miss: the next coil (HSS-G) cannot be made on this assembler (7680 EU/t), and the RTM furnace is what makes iridium, HSS-G and the later alloys possible. Build 16 RTM blocks for the EBF first, only then think about HSS-G.
---
# RTM coil: ruthenium + tungsten + molybdenum → RTM alloy → double wire + vanadium steel foil + borosilicate foil + molten nichrome

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `rtm_coil` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [IV components, RTM coil, Shellite](../../plan/p10.md#ivmach)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-mx">
<div class="gt-head"><span class="gt-mname">EV Mixer · circuit 1 · 15 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Ruthenium dust (gtceu:ruthenium_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Dust</span><span class="gt-note">4 Ruthenium dust</span><b class="gt-q">4</b></span><span class="gt-slot" title="2 Tungsten dust (gtceu:tungsten_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Dust</span><span class="gt-note">2 Tungsten dust</span><b class="gt-q">2</b></span><span class="gt-slot" title="1 Molybdenum dust (gtceu:molybdenum_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__molybdenum_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molybdenum Dust</span><span class="gt-note">1 Molybdenum dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="7 RTM alloy dust (gtceu:rtm_alloy_dust) - 7 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Dust</span><span class="gt-note">7 RTM alloy dust</span><b class="gt-q">7</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · Nichrome 3000 K · 70 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="7 RTM alloy dust (gtceu:rtm_alloy_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Dust</span><span class="gt-note">7 RTM alloy dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Helium · 1 B (optional) (gtceu:helium_bucket) - circuit 2"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium · 1 B (optional)</span><b class="gt-q">circuit 2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">70 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot RTM alloy ingot (gtceu:hot_rtm_alloy_ingot) - 1 / 70 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_rtm_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Rtm Alloy Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 12.5 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot RTM alloy ingot (gtceu:hot_rtm_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_rtm_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Rtm Alloy Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="RTM alloy ingot (gtceu:rtm_alloy_ingot) - 1 / 12.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">LV Wiremill · circuit 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="RTM alloy ingot (gtceu:rtm_alloy_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Ingot</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 RTM alloy double wire (gtceu:rtm_alloy_double_wire) - 1 : 1"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Double Wire</span><span class="gt-note">8 RTM alloy double wire</span><b class="gt-q">1 : 1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-b1">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 10 · 1 → 4</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Vanadium steel ingot (gtceu:vanadium_steel_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Steel Ingot</span><span class="gt-note">2 Vanadium steel ingot</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Vanadium steel foil (gtceu:vanadium_steel_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_steel_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Steel Foil</span><span class="gt-note">8 Vanadium steel foil</span><b class="gt-q">8</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-b2">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 10 · 1 → 4</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Borosilicate glass ingot (gtceu:borosilicate_glass_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__borosilicate_glass_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borosilicate Glass Ingot</span><span class="gt-note">2 Borosilicate glass ingot</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Borosilicate glass foil (gtceu:borosilicate_glass_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__borosilicate_glass_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borosilicate Glass Foil</span><span class="gt-note">8 Borosilicate glass foil</span><b class="gt-q">8</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-ex">
<div class="gt-head"><span class="gt-mname">LV Extractor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nichrome ingot (gtceu:nichrome_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="144 mB molten nichrome (gtceu:nichrome_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome</span><span class="gt-note">144 mB molten nichrome</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_extractor</code></div>
</div>
<div class="gt-panel t-ev" id="m-as">
<div class="gt-head"><span class="gt-mname">EV Assembler · 25 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 RTM alloy double wire (gtceu:rtm_alloy_double_wire) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Double Wire</span><span class="gt-note">8 RTM alloy double wire</span><b class="gt-q">8</b></span><span class="gt-slot" title="8 Vanadium steel foil (gtceu:vanadium_steel_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_steel_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Steel Foil</span><span class="gt-note">8 Vanadium steel foil</span><b class="gt-q">8</b></span><span class="gt-slot" title="8 Borosilicate glass foil (gtceu:borosilicate_glass_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__borosilicate_glass_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borosilicate Glass Foil</span><span class="gt-note">8 Borosilicate glass foil</span><b class="gt-q">8</b></span><span class="gt-slot gt-fluid" title="144 mB molten nichrome (gtceu:nichrome_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome</span><span class="gt-note">144 mB molten nichrome</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">25 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="RTM Alloy Coil Block (gtceu:rtm_alloy_coil_block) - 1 / 25 s"><img class="gt-ico" src="../../assets/icons/gtceu__rtm_alloy_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rtm Alloy Coil Block</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_assembler</code></div>
</div>
</div>

## Flow

- [EV Mixer · circuit 1 · 15 s · 1920 EU/t](#m-mx) → [EBF · Nichrome 3000 K · 70 s · 1920 EU/t](#m-eb) → [Vacuum Freezer · 12.5 s · 480 EU/t](#m-vf) → [LV Wiremill · circuit 2](#m-wm) → [EV Assembler · 25 s · 1920 EU/t](#m-as)
- [LV Bender · circuit 10 · 1 → 4](#m-b1) → [EV Assembler · 25 s · 1920 EU/t](#m-as)
- [LV Bender · circuit 10 · 1 → 4](#m-b2) → [EV Assembler · 25 s · 1920 EU/t](#m-as)
- [LV Extractor](#m-ex) → [EV Assembler · 25 s · 1920 EU/t](#m-as)

## How to build

1. Input drawers first, one per item: ruthenium dust (from the platinum group line), tungsten dust, molybdenum dust, vanadium steel ingots, borosilicate glass ingots, nichrome ingots. A drum for helium and one for molten nichrome. Every machine below gets a Modular Router or Pipez item pipe with an Item Filter and a Robot Arm Keep Exact cap on its output drawer. — `functionalstorage:oak_1`, `gtceu:ruthenium_dust`, `gtceu:tungsten_dust`, `gtceu:molybdenum_dust`
2. EV Mixer with ghost circuit 1, dedicated: 4 ruthenium + 2 tungsten + 1 molybdenum dust → 7 RTM alloy dust in 15 s at 1920 EU/t. The three inputs are three drawers with three filters, since an unfiltered pipe floods the bus with the wrong dust. Keep Exact 64 on the dust output. — `gtceu:ev_mixer`, `gtceu:rtm_alloy_dust`
3. Dedicated EBF with 16 Nichrome coil blocks and an EV Energy Hatch. Input bus with ghost circuit 1 (or circuit 2 plus a 1 B helium hatch for the 67 % recipe). 1 RTM dust → 1 hot RTM alloy ingot in 70 s, 1920 EU/t. Let the bus fill and keep it running: 128 ingots for a full RTM furnace is 2.5 hours on one machine. — `gtceu:electric_blast_furnace`, `gtceu:nichrome_coil_block`, `gtceu:ev_energy_input_hatch`, `gtceu:hot_rtm_alloy_ingot`
4. Vacuum Freezer: Robot Arm from the EBF output bus (Item Filter: hot RTM alloy ingot) into its input bus; 1 ingot in 12.5 s at 480 EU/t, no coolant. This is the step people forget, then wonder why the wiremill ignores the ingot. Output into a drawer with Keep Exact at 32. — `gtceu:vacuum_freezer`, `gtceu:rtm_alloy_ingot`
5. LV Wiremill, ghost circuit 2: 1 RTM alloy ingot → 1 double wire (30 EU/t because the alloy is above 2800 K). One coil needs 8, so cap its drawer at 16. — `gtceu:lv_wiremill`, `gtceu:rtm_alloy_double_wire`
6. Two LV Benders on ghost circuit 10, one per metal: 1 vanadium steel ingot → 4 foil and 1 borosilicate glass ingot → 4 foil (24 EU/t). 2 ingots of each per coil. Vanadium steel ingots come from the MV Mixer + EBF line in the tips; borosilicate dust from the ULV mixer and a furnace. — `gtceu:lv_bender`, `gtceu:vanadium_steel_foil`, `gtceu:borosilicate_glass_foil`
7. LV Extractor: 1 nichrome ingot → 144 mB molten nichrome, then a pump cover into a drum beside the assembler. If the drum is empty the assembler runs the item part and then waits, with a full input bus and no output. — `gtceu:lv_extractor`, `gtceu:nichrome_bucket`
8. EV Assembler (build it from EV parts: it is 1920 EU/t): 8 RTM double wire + 8 vanadium steel foil + 8 borosilicate glass foil in the input bus, 144 mB molten nichrome in the fluid hatch → 1 RTM Alloy Coil Block in 25 s. Output drawer with Keep Exact 16. Craft one by hand first, it proves the three foils are right. — `gtceu:ev_assembler`, `gtceu:rtm_alloy_coil_block`
9. Easy to miss: the next coil (HSS-G) cannot be made on this assembler (7680 EU/t), and the RTM furnace is what makes iridium, HSS-G and the later alloys possible. Build 16 RTM blocks for the EBF first, only then think about HSS-G. — `gtceu:hssg_coil_block`, `gtceu:iv_assembler`

## Tips

- Coil tiers, verified in the mod jar (CoilBlock$CoilType) and the pack quests: cupronickel 1800 K, kanthal 2700 K, nichrome 3600 K (3rd tier), RTM alloy 4500 K (4th), HSS-G 5400 K (5th), naquadah 7200 K. An EV hatch adds 200 K. Iridium (4500 K), HSS-G (4200 K) and the later hard alloys need RTM; osmium is 4500 K too.
- RTM alloy (MixerRecipes): 4 ruthenium dust + 2 tungsten dust + 1 molybdenum dust, circuit 1, 300 ticks at 1920 EU/t → 7 RTM alloy dust (EV Mixer). EBF (FirstDegreeMaterials): 3000 K, VA\[EV\] = 1920 EU/t, 1400 ticks = 70 s per ingot, nichrome coils are enough; with circuit 2 and 1 B helium the time is 67 % (about 47 s). Hot ingot to the Vacuum Freezer: 250 ticks (12.5 s) at 480 EU/t.
- Coil block (kjs coils.js): 8 RTM alloy double wire + 8 vanadium steel foil + 8 borosilicate glass foil + 144 mB molten nichrome → 1 RTM Alloy Coil Block, 500 ticks (25 s) at 1920 EU/t, so an EV Assembler (the nichrome coil was an HV one). Cost per block: 8 RTM ingots (= 4.6 ruthenium, 2.3 tungsten, 1.1 molybdenum), 2 vanadium steel ingots, 2 borosilicate ingots and 1 nichrome ingot.
- Ruthenium is the bottleneck. One ruthenium needs about 18 platinum group sludge dust (3 centrifuge runs of 2 inert metal mixture each, platline chain), so a 16-coil EBF (128 ingots, 73 ruthenium) is roughly 1300 sludge, about 330 purified cooperite ore. The ZPM Chemical Plant skip (kjs chemical\_plant.js) yields 7 ruthenium per 30 ore, which is the late fix.
- Vanadium steel: MV Mixer circuit 1, 7 steel + 1 vanadium + 1 chromium dust → 9 dust (400 ticks, 120 EU/t), then an EBF at 1453 K (cupronickel is enough; MV power, about 80 s per ingot, derived from mass x 1453 / 50). Foil: LV Bender, circuit 10, 1 ingot → 4 foil (24 EU/t). Vanadium comes from vanadium magnetite (kjs sieving.js iron mesh 5 % on gravel); chromium from the chromium line.
- Borosilicate glass: mixer (ULV recipe, circuit 1): 1 boron dust + 7 glass dust → 8 dust (200 ticks, 7 EU/t); furnace it into an ingot (the quest calls it a glass bar), then an LV Bender on circuit 10 makes 4 foil per ingot (PartsRecipeHandler.processFoil; the foil tag exists in the EMI list). Molybdenum comes from molybdenite (sieve with a diamond mesh on crushed blackstone, 12 %, or the ore factory).
- Molten nichrome: LV Extractor, 1 nichrome ingot → 144 mB. Pipe it into the assembler’s fluid hatch through a drum with a pump cover. The same assembler cannot also make the nichrome coil (different foils), so build one assembler per coil type.
- HSS-G coil (5th tier, 5400 K) is the same shape: 8 HSS-G double wire + 8 tungsten carbide foil + 16 borosilicate foil + 144 mB molten TUNGSTEN, 600 ticks (30 s) at 7680 EU/t = an IV Assembler. HSS-G: EV Mixer circuit 1, 5 tungsten steel dust + 1 chromium + 2 molybdenum + 1 vanadium → 9 dust (400 ticks); EBF 4200 K, 1920 EU/t, 1300 ticks (65 s), RTM coils needed. Because HSS-G melts at 4200 K the RTM furnace is enough to make it; the HSS-G COIL is first needed for the 5000 K recipes (HSS-S, the naquadah ingot in the EBF) and for 5300 K twinite. Tungsten carbide: EV Mixer circuit 2, 1 tungsten + 1 carbon dust → 2 dust.
- Sub-steps people skip: (1) the hot RTM ingot must go through the freezer before the wiremill; (2) the double wire is circuit 2, circuit 1 makes single wires; (3) benders on circuit 10 for foil, never 1 (that makes plates); (4) 16 coil blocks per EBF, so 128 double wires, 128 foil of each kind and 16 nichrome ingots; (5) the EBF needs an EV Energy Hatch, and the EV Assembler (a single machine) needs an EV cable.
- **Unverified** the vanadium steel EBF time (derived from the formula), the platline yields per ore (derived from PlatGroupMetalsRecipes), and the exact seconds of the bender foil recipes (mass-based).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:ev_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:nichrome_coil_block` | 16 |
| `gtceu:ev_energy_input_hatch` | 2 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_bender` | 2 |
| `gtceu:lv_extractor` | 1 |
| `gtceu:ev_assembler` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../ev/nichrome_line.md)
- **Main source for:** `gtceu:rtm_alloy_coil_block`, `gtceu:rtm_alloy_dust`, `gtceu:rtm_alloy_ingot`, `gtceu:rtm_alloy_double_wire`, `gtceu:hssg_coil_block`
