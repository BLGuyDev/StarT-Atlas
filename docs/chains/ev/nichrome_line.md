---
kind: chain
id: nichrome_line
order: 1090
data:
  t: |-
    Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block
  inf: true
  "n":
    - [ni, "Nickel dust · 4", i, "gtceu:nickel_dust"]
    - [cr, "Chromium dust · 1", i, "gtceu:chromium_dust"]
    - [mx, "MV Mixer · circuit 2 · 25 s · 120 EU/t", m, "gtceu:mv_mixer"]
    - [nd, "5 Nichrome dust", x, "gtceu:nichrome_dust"]
    - [eb, "EBF · Kanthal 2700 K · 65 s · 1920 EU/t", m, "gtceu:electric_blast_furnace"]
    - [hn, Hot nichrome ingot, x, "gtceu:hot_nichrome_ingot"]
    - [vf, "Vacuum Freezer · 480 EU/t", m, "gtceu:vacuum_freezer"]
    - [ng, Nichrome ingot, x, "gtceu:nichrome_ingot"]
    - [wm, "LV Wiremill · circuit 2", m, "gtceu:lv_wiremill"]
    - [dw, "8 Double wire", x, "gtceu:nichrome_double_wire"]
    - [ss, "2 Stainless steel ingots", i, "gtceu:stainless_steel_ingot"]
    - [be, "LV Bender · circuit 10", m, "gtceu:lv_bender"]
    - [sf, "8 Stainless steel foil", x, "gtceu:stainless_steel_foil"]
    - [bf, "4 Borosilicate glass foil", i, "gtceu:borosilicate_glass_foil"]
    - [al, "1 Aluminium ingot", i, "gtceu:aluminium_ingot"]
    - [ex, LV Extractor, m, "gtceu:lv_extractor"]
    - [ma, "144 mB molten aluminium", f, "gtceu:aluminium_bucket"]
    - [as, "HV Assembler · 20 s · 480 EU/t", m, "gtceu:hv_assembler"]
    - [co, Nichrome Coil Block, o, "gtceu:nichrome_coil_block"]
  e:
    - [ni, mx, "4"]
    - [cr, mx, "1"]
    - [mx, nd, "5"]
    - [nd, eb, "1"]
    - [eb, hn, "1 / 65 s"]
    - [hn, vf, "1"]
    - [vf, ng, "1"]
    - [ng, wm, "8"]
    - [wm, dw, "1 : 1"]
    - [ss, be, "2"]
    - [be, sf, "1 → 4"]
    - [al, ex, "1"]
    - [ex, ma, "144 mB"]
    - [dw, as, "8"]
    - [sf, as, "8"]
    - [bf, as, "4"]
    - [ma, as, "144 mB"]
    - [as, co, "1 / 20 s"]
  tips:
    - |-
      Mixer: 4 nickel dust + 1 chromium dust with ghost circuit 2 → 5 nichrome dust, 500 ticks (25 s), 120 EU/t. Circuit 1 on the same mixer is the Kanthal recipe, so keep a separate mixer for each alloy. One batch is 5 dust = 5 ingots.
    - |-
      EBF: nichrome is 2700 K, VA[EV] = 1920 EU/t, 1300 ticks (65 s) with circuit 1. With circuit 2 and 1 B nitrogen per ingot the same recipe takes x0.67 = 871 ticks (about 43 s). It is an EV recipe: an HV energy hatch cannot supply 1920 EU/t, so the EBF needs an EV Energy Hatch. Kanthal coils are exactly 2700 K, which is enough (an EV hatch adds +200 K). Cupronickel (1800 K, 2000 K at EV) is not.
    - Hot nichrome must be cooled in the Vacuum Freezer (VA[HV] = 480 EU/t, duration is the material mass times 3 ticks, about 8 to 9 s; no coolant below 5000 K). Put the freezer from the titanium chain beside this EBF only if you can accept it switching recipes; a second freezer is cheaper than a stall.
    - |-
      Coil block: 8 nichrome double wire (wiremill circuit 2, 1 ingot → 1 double wire) + 8 stainless steel foil (2 stainless ingots in an LV bender, circuit 10, 1 ingot → 4 foil) + 4 borosilicate glass foil + 144 mB molten aluminium → Nichrome Coil Block. Assembler 400 ticks (20 s) at 480 EU/t, so an HV Assembler, not MV. Source: kjs coils.js.
    - |-
      Cost of 16 coils: 128 nichrome ingots = 102 nickel dust + 26 chromium dust, 32 stainless ingots, 64 borosilicate foil and 16 aluminium ingots. One EBF takes 2 h 18 min for the 128 ingots (about 1 h 33 min with nitrogen), at 1920 EU/t. Run two furnaces if you want the coils the same evening.
    - |-
      What it unlocks: nichrome coils are 3600 K (3800 K at an EV hatch), the third coil tier. The RTM coil block recipe also consumes 144 mB molten nichrome per block and the EV heating wire for machines is nichrome too (see the next tip).
    - |-
      Nichrome is also the EV heating wire: double and quadruple wire go into the EV furnace, alloy smelter and similar single machines, and a nichrome spring into the EV distillery and brewery (GTCraftingComponents COIL_HEATING and ROD_DISTILLATION; the pack tier_data.js also lists nichrome as the EV wire). Make more ingots than the 128 once EV machines start.
    - |-
      Unverified: the exact vacuum freezer time (mass-based, read EMI), and how borosilicate glass foil is made. The base source only gives the glass plate and fine wire flags; its dust comes from a mixer recipe and the pack coil recipe asks for the foil, so open the foil in EMI to see the machine (bender on the plate or ingot is the likely one) before building 64.
  b:
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:kanthal_coil_block", 16]
    - ["gtceu:ev_energy_input_hatch", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_bender", 2]
    - ["gtceu:lv_extractor", 1]
    - ["gtceu:hv_assembler", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:nickel_dust", "gtceu:chromium_dust"]
      t: |-
        Two input drawers for the mixer: nickel dust (the stainless chain’s drawer works; size it for 4 per 5 dust) and chromium dust from the chromium line. Four nickel and one chromium must be on hand each batch, so give the mixer two separate Modular Router pulls or two Pipez item pipes with Item Filters, never one mixed pipe.
    - i: ["gtceu:mv_mixer", "gtceu:nichrome_dust"]
      t: |-
        MV Mixer with ghost circuit 2 (not 1: that is Kanthal). 4 nickel + 1 chromium dust → 5 nichrome dust in 25 s at 120 EU/t. A Robot Arm cover on the output in Keep Exact mode with an Item Filter on nichrome dust and 64 fills the drawer and then stops the mixer.
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:kanthal_coil_block
        - gtceu:ev_energy_input_hatch
        - gtceu:hot_nichrome_ingot
      t: Dedicated EBF with Kanthal coils (16 coil blocks) and an EV Energy Hatch. Input bus with ghost circuit 1, output bus. 1 nichrome dust → 1 hot nichrome ingot in 65 s at 1920 EU/t. With circuit 2 and an input hatch of nitrogen (1 B per ingot) it takes 43 s. Let the furnace fill its bus slot to 64 and keep it running.
    - i: ["gtceu:vacuum_freezer", "gtceu:nichrome_ingot"]
      t: |-
        Vacuum Freezer: Robot Arm cover from the EBF output bus (Item Filter on hot nichrome ingot) into its input bus. 1 hot ingot → 1 nichrome ingot, 480 EU/t, no coolant. The sub-step people skip: the hot ingot looks like the real thing, but nothing accepts it in a wiremill or an assembler. Output drawer with Keep Exact at 64.
    - i: ["gtceu:lv_wiremill", "gtceu:nichrome_double_wire"]
      t: |-
        LV Wiremill, ghost circuit 2: 1 nichrome ingot → 1 double wire. One coil needs 8 double wires, so keep the output drawer at 16 with a Keep Exact arm. Circuit 1 would make single wires: another machine, never change the circuit.
    - i: ["gtceu:lv_bender", "gtceu:stainless_steel_foil"]
      t: |-
        LV Bender with ghost circuit 10: 1 stainless steel ingot → 4 stainless steel foil. 8 foil per coil = 2 ingots. A second bender for aluminium would also take circuit 10, so keep each metal in its own machine.
    - i: ["gtceu:lv_extractor", "gtceu:aluminium_bucket"]
      t: |-
        LV Extractor: 1 aluminium ingot → 144 mB molten aluminium, then into a drum with a pump cover to the assembler. The coil recipe takes the molten aluminium as a fluid input, so the assembler needs a fluid input hatch.
    - i: ["gtceu:hv_assembler", "gtceu:nichrome_coil_block"]
      t: |-
        HV Assembler (the recipe is 480 EU/t): 8 nichrome double wire + 8 stainless steel foil + 4 borosilicate glass foil in the input bus, 144 mB molten aluminium into the fluid hatch, 20 s → one Nichrome Coil Block. Borosilicate foil is a plain drawer for now (see the Unverified tip); keep at least 4 on hand per coil.
---
# Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `nichrome_line` · **Tags:** Infinite source, Unverified

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Nichrome and the 3600 K coil](../../plan/p9.md#nichrome)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-mx">
<div class="gt-head"><span class="gt-mname">MV Mixer · circuit 2 · 25 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nickel dust · 4 (gtceu:nickel_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Dust</span><span class="gt-note">Nickel dust · 4</span><b class="gt-q">4</b></span><span class="gt-slot" title="Chromium dust · 1 (gtceu:chromium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Dust</span><span class="gt-note">Chromium dust · 1</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Nichrome dust (gtceu:nichrome_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Dust</span><span class="gt-note">5 Nichrome dust</span><b class="gt-q">5</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · Kanthal 2700 K · 65 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="5 Nichrome dust (gtceu:nichrome_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Dust</span><span class="gt-note">5 Nichrome dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">65 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot nichrome ingot (gtceu:hot_nichrome_ingot) - 1 / 65 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_nichrome_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Nichrome Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot nichrome ingot (gtceu:hot_nichrome_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_nichrome_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Nichrome Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Nichrome ingot (gtceu:nichrome_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">LV Wiremill · circuit 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nichrome ingot (gtceu:nichrome_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Ingot</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Double wire (gtceu:nichrome_double_wire) - 1 : 1"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Double Wire</span><span class="gt-note">8 Double wire</span><b class="gt-q">1 : 1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 10</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Stainless steel ingots (gtceu:stainless_steel_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Ingot</span><span class="gt-note">2 Stainless steel ingots</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Stainless steel foil (gtceu:stainless_steel_foil) - 1 → 4"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Foil</span><span class="gt-note">8 Stainless steel foil</span><b class="gt-q">1 → 4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-ex">
<div class="gt-head"><span class="gt-mname">LV Extractor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Aluminium ingot (gtceu:aluminium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Ingot</span><span class="gt-note">1 Aluminium ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="144 mB molten aluminium (gtceu:aluminium_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium</span><span class="gt-note">144 mB molten aluminium</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_extractor</code></div>
</div>
<div class="gt-panel t-hv" id="m-as">
<div class="gt-head"><span class="gt-mname">HV Assembler · 20 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Double wire (gtceu:nichrome_double_wire) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Double Wire</span><span class="gt-note">8 Double wire</span><b class="gt-q">8</b></span><span class="gt-slot" title="8 Stainless steel foil (gtceu:stainless_steel_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Foil</span><span class="gt-note">8 Stainless steel foil</span><b class="gt-q">8</b></span><span class="gt-slot" title="4 Borosilicate glass foil (gtceu:borosilicate_glass_foil) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__borosilicate_glass_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Borosilicate Glass Foil</span><span class="gt-note">4 Borosilicate glass foil</span><b class="gt-q">4</b></span><span class="gt-slot gt-fluid" title="144 mB molten aluminium (gtceu:aluminium_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium</span><span class="gt-note">144 mB molten aluminium</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Nichrome Coil Block (gtceu:nichrome_coil_block) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__nichrome_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nichrome Coil Block</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_assembler</code></div>
</div>
</div>

## Flow

- [MV Mixer · circuit 2 · 25 s · 120 EU/t](#m-mx) → [EBF · Kanthal 2700 K · 65 s · 1920 EU/t](#m-eb) → [Vacuum Freezer · 480 EU/t](#m-vf) → [LV Wiremill · circuit 2](#m-wm) → [HV Assembler · 20 s · 480 EU/t](#m-as)
- [LV Bender · circuit 10](#m-be) → [HV Assembler · 20 s · 480 EU/t](#m-as)
- [LV Extractor](#m-ex) → [HV Assembler · 20 s · 480 EU/t](#m-as)

## How to build

1. Two input drawers for the mixer: nickel dust (the stainless chain’s drawer works; size it for 4 per 5 dust) and chromium dust from the chromium line. Four nickel and one chromium must be on hand each batch, so give the mixer two separate Modular Router pulls or two Pipez item pipes with Item Filters, never one mixed pipe. — `functionalstorage:oak_1`, `gtceu:nickel_dust`, `gtceu:chromium_dust`
2. MV Mixer with ghost circuit 2 (not 1: that is Kanthal). 4 nickel + 1 chromium dust → 5 nichrome dust in 25 s at 120 EU/t. A Robot Arm cover on the output in Keep Exact mode with an Item Filter on nichrome dust and 64 fills the drawer and then stops the mixer. — `gtceu:mv_mixer`, `gtceu:nichrome_dust`
3. Dedicated EBF with Kanthal coils (16 coil blocks) and an EV Energy Hatch. Input bus with ghost circuit 1, output bus. 1 nichrome dust → 1 hot nichrome ingot in 65 s at 1920 EU/t. With circuit 2 and an input hatch of nitrogen (1 B per ingot) it takes 43 s. Let the furnace fill its bus slot to 64 and keep it running. — `gtceu:electric_blast_furnace`, `gtceu:kanthal_coil_block`, `gtceu:ev_energy_input_hatch`, `gtceu:hot_nichrome_ingot`
4. Vacuum Freezer: Robot Arm cover from the EBF output bus (Item Filter on hot nichrome ingot) into its input bus. 1 hot ingot → 1 nichrome ingot, 480 EU/t, no coolant. The sub-step people skip: the hot ingot looks like the real thing, but nothing accepts it in a wiremill or an assembler. Output drawer with Keep Exact at 64. — `gtceu:vacuum_freezer`, `gtceu:nichrome_ingot`
5. LV Wiremill, ghost circuit 2: 1 nichrome ingot → 1 double wire. One coil needs 8 double wires, so keep the output drawer at 16 with a Keep Exact arm. Circuit 1 would make single wires: another machine, never change the circuit. — `gtceu:lv_wiremill`, `gtceu:nichrome_double_wire`
6. LV Bender with ghost circuit 10: 1 stainless steel ingot → 4 stainless steel foil. 8 foil per coil = 2 ingots. A second bender for aluminium would also take circuit 10, so keep each metal in its own machine. — `gtceu:lv_bender`, `gtceu:stainless_steel_foil`
7. LV Extractor: 1 aluminium ingot → 144 mB molten aluminium, then into a drum with a pump cover to the assembler. The coil recipe takes the molten aluminium as a fluid input, so the assembler needs a fluid input hatch. — `gtceu:lv_extractor`, `gtceu:aluminium_bucket`
8. HV Assembler (the recipe is 480 EU/t): 8 nichrome double wire + 8 stainless steel foil + 4 borosilicate glass foil in the input bus, 144 mB molten aluminium into the fluid hatch, 20 s → one Nichrome Coil Block. Borosilicate foil is a plain drawer for now (see the Unverified tip); keep at least 4 on hand per coil. — `gtceu:hv_assembler`, `gtceu:nichrome_coil_block`

## Tips

- Mixer: 4 nickel dust + 1 chromium dust with ghost circuit 2 → 5 nichrome dust, 500 ticks (25 s), 120 EU/t. Circuit 1 on the same mixer is the Kanthal recipe, so keep a separate mixer for each alloy. One batch is 5 dust = 5 ingots.
- EBF: nichrome is 2700 K, VA\[EV\] = 1920 EU/t, 1300 ticks (65 s) with circuit 1. With circuit 2 and 1 B nitrogen per ingot the same recipe takes x0.67 = 871 ticks (about 43 s). It is an EV recipe: an HV energy hatch cannot supply 1920 EU/t, so the EBF needs an EV Energy Hatch. Kanthal coils are exactly 2700 K, which is enough (an EV hatch adds +200 K). Cupronickel (1800 K, 2000 K at EV) is not.
- Hot nichrome must be cooled in the Vacuum Freezer (VA\[HV\] = 480 EU/t, duration is the material mass times 3 ticks, about 8 to 9 s; no coolant below 5000 K). Put the freezer from the titanium chain beside this EBF only if you can accept it switching recipes; a second freezer is cheaper than a stall.
- Coil block: 8 nichrome double wire (wiremill circuit 2, 1 ingot → 1 double wire) + 8 stainless steel foil (2 stainless ingots in an LV bender, circuit 10, 1 ingot → 4 foil) + 4 borosilicate glass foil + 144 mB molten aluminium → Nichrome Coil Block. Assembler 400 ticks (20 s) at 480 EU/t, so an HV Assembler, not MV. Source: kjs coils.js.
- Cost of 16 coils: 128 nichrome ingots = 102 nickel dust + 26 chromium dust, 32 stainless ingots, 64 borosilicate foil and 16 aluminium ingots. One EBF takes 2 h 18 min for the 128 ingots (about 1 h 33 min with nitrogen), at 1920 EU/t. Run two furnaces if you want the coils the same evening.
- What it unlocks: nichrome coils are 3600 K (3800 K at an EV hatch), the third coil tier. The RTM coil block recipe also consumes 144 mB molten nichrome per block and the EV heating wire for machines is nichrome too (see the next tip).
- Nichrome is also the EV heating wire: double and quadruple wire go into the EV furnace, alloy smelter and similar single machines, and a nichrome spring into the EV distillery and brewery (GTCraftingComponents COIL\_HEATING and ROD\_DISTILLATION; the pack tier\_data.js also lists nichrome as the EV wire). Make more ingots than the 128 once EV machines start.
- **Unverified** the exact vacuum freezer time (mass-based, read EMI), and how borosilicate glass foil is made. The base source only gives the glass plate and fine wire flags; its dust comes from a mixer recipe and the pack coil recipe asks for the foil, so open the foil in EMI to see the machine (bender on the plate or ingot is the likely one) before building 64.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:kanthal_coil_block` | 16 |
| `gtceu:ev_energy_input_hatch` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_bender` | 2 |
| `gtceu:lv_extractor` | 1 |
| `gtceu:hv_assembler` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |

## Needs / Feeds

- **Needs:** [Ore processing](../lv/ores.md), [Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod](../hv/chromium_line.md), [Stainless steel: MV Mixer + HV Electric Blast Furnace](../hv/stainless.md), [Infinite aluminium (clay)](../mv/aluminium.md)
- **Feeds:** [RTM coil: ruthenium + tungsten + molybdenum → RTM alloy → double wire + vanadium steel foil + borosilicate foil + molten nichrome](../iv/rtm_coil.md)
- **Main source for:** `gtceu:nichrome_dust`, `gtceu:hot_nichrome_ingot`, `gtceu:nichrome_ingot`, `gtceu:nichrome_double_wire`, `gtceu:nichrome_coil_block`, `gtceu:vacuum_freezer`
