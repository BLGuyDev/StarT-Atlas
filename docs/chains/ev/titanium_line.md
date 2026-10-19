---
kind: chain
id: titanium_line
order: 1070
data:
  t: |-
    Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer
  inf: true
  "n":
    - [mm, "Molten ore mixture · 10 B", s, "gtceu:molten_ore_mixture_bucket"]
    - [dt, "Distillation Tower · 60 s · 1920 EU/t", m, "gtceu:distillation_tower"]
    - [mi, "Molten ilmenite ore · 1 B", f, "gtceu:molten_ilmenite_ore_bucket"]
    - [sd, Stone dust, i, "gtceu:stone_dust"]
    - [ac, "HV Autoclave · 8 s · 480 EU/t", m, "gtceu:hv_autoclave"]
    - [ri, "2 Raw ilmenite", x, "gtceu:raw_ilmenite"]
    - [p1, "LV Pulverizer · 15 s", m, "gtceu:lv_pulverizer"]
    - [cr, "4 Crushed ilmenite ore", x, "gtceu:crushed_ilmenite_ore"]
    - [p2, "LV Pulverizer · circuit 0 · 15 s", m, "gtceu:lv_pulverizer"]
    - [id, Ilmenite dust, x, "gtceu:ilmenite_dust"]
    - [c, Carbon dust, i, "gtceu:carbon_dust"]
    - [e1, "EBF · 1700 K · 80 s · 480 EU/t", m, "gtceu:electric_blast_furnace"]
    - [ru, "2 Rutile dust", x, "gtceu:rutile_dust"]
    - [wi, "2 Wrought iron ingot", x, "gtceu:wrought_iron_ingot"]
    - [cl, "Chlorine · 4 B", f, "gtceu:chlorine_bucket"]
    - [rx, "HV Chemical Reactor · 20 s · 480 EU/t", m, "gtceu:hv_chemical_reactor"]
    - [tc, "Titanium tetrachloride · 1 B", f, "gtceu:titanium_tetrachloride_bucket"]
    - [mg, "2 Magnesium dust", i, "gtceu:magnesium_dust"]
    - [e2, "EBF · Kanthal 2141 K · 40 s · 480 EU/t", m, "gtceu:electric_blast_furnace"]
    - [ht, Hot titanium ingot, x, "gtceu:hot_titanium_ingot"]
    - [vf, "Vacuum Freezer · 7.2 s · 480 EU/t", m, "gtceu:vacuum_freezer"]
    - [ti, Titanium ingot, o, "gtceu:titanium_ingot"]
    - [mc, "6 Magnesium chloride dust", x, "gtceu:magnesium_chloride_dust"]
    - [el, "LV Electrolyzer · 4.5 s · 30 EU/t", m, "gtceu:lv_electrolyzer"]
    - [mr, "2 Magnesium dust (back)", x, "gtceu:magnesium_dust"]
    - [cb, "4 B chlorine (back)", f, "gtceu:chlorine_bucket"]
  e:
    - [mm, dt, "10 B"]
    - [dt, mi, "1 B"]
    - [mi, ac, "500 mB"]
    - [sd, ac, "1"]
    - [ac, ri, "1 / 8 s"]
    - [ri, p1, "1"]
    - [p1, cr, "1 → 2"]
    - [cr, p2, "1"]
    - [p2, id, "1 (+25 %)"]
    - [id, e1, "10"]
    - [c, e1, "2"]
    - [e1, ru, "2 / 80 s"]
    - [e1, wi, "2"]
    - [ru, rx, "1"]
    - [c, rx, "2"]
    - [cl, rx, "4 B"]
    - [rx, tc, "1 B / 20 s"]
    - [tc, e2, "1 B"]
    - [mg, e2, "2"]
    - [e2, ht, "1 / 40 s"]
    - [e2, mc, "6"]
    - [ht, vf, "1"]
    - [vf, ti, "1 / 7.2 s"]
    - [mc, el, "3"]
    - [el, mr, "1 per 3"]
    - [el, cb, "2 B per 3"]
  tips:
    - |-
      Per ingot: 1 rutile, 2 carbon for the reactor, 4 B chlorine and 2 magnesium. The magnesium and chlorine come back: 6 magnesium chloride dust electrolyse (3 dust → 1 magnesium + 2 B chlorine, twice) into exactly the 2 magnesium and 4 B chlorine the next ingot needs. After the first fill the loop only loses what you spill.
    - Rutile is the real cost. The pack EBF recipe gives 2 rutile + 2 wrought iron + 2 B carbon monoxide from 10 ilmenite dust + 2 carbon dust (1700 K, 80 s, 480 EU/t), so 5 ilmenite dust per rutile. One tower run (10 B mixture) gives 1 B molten ilmenite = 2 raw ilmenite = 4 crushed ore = 5 dust = 1 rutile = 1 titanium ingot, and the same run gives 1.5 B molten bauxite = 3 raw bauxite = about 7.5 dust.
    - |-
      Bauxite helps: electrolysing 15 bauxite dust gives 6 aluminium + 1 rutile + 9 B oxygen (270 ticks, 60 EU/t, source SeparationRecipes), so the bauxite from the same tower run adds about 0.5 rutile on top.
    - |-
      Better yield: the Electric Ore Factory treats ilmenite as an EV ore (EV hatch, 1920 EU/t, 16 s, 100 mB sodium persulfate per crushed ore). It gives 1 dust (+50 %), 25 % iron, 12.5 % iron and 7.5 % rutile, so 4 crushed ore give 6 dust and 0.3 rutile instead of 5 dust. Source: systems/ore_factory_processing.js. Use it once sodium persulfate flows; the pulverizer line works without.
    - |-
      Molten ore mixture is the bottleneck. EV Mixer recycle: 16 crushed ores (any ore tagged crushed ores) + 32 stone dust + 32 B lava → 6 B mixture in 40 s at 1920 EU/t. One ingot needs 10 B, so 1.7 runs, about 27 crushed ore, 53 stone dust and 53 B lava. The tower also returns 1 metal mixture dust per run; the IV mixer loop (2 metal mixture + 48 stone dust + 48 B lava → 20 B) is the late fix, not an EV one. Tiers of the whole side line: Void Extractor LV, slurry centrifuge MV, residue electrolysis HV, raw-ore autoclave HV, recycle mixer and tower EV, loop mixer IV. Without the tower 1 B of slurry gives only 250 mB of mixture (about 57 extractor runs per 10 B tower batch), so the EV recycle mixer is the real fix.
    - |-
      Coil heat: the titanium recipe needs 2141 K (titanium 1941 K + 200). Cupronickel is 1800 K, 2000 K even with an EV hatch, so it fails. Kanthal is 2700 K and an HV hatch is enough (the recipe is 480 EU/t). Build the Kanthal line first (chain: Kanthal). The rutile EBF (1700 K) works on cupronickel.
    - |-
      Vacuum Freezer: 1 hot titanium ingot → 1 titanium ingot in 144 ticks (7.2 s, mass 48 x 3 ticks) at 480 EU/t, an HV hatch. Controller recipe: 3 HV pumps + 3 EV circuits + 1 frostproof casing + 2 gold cables, so the first EV circuits are needed for the freezer even though it runs on an HV hatch (3 per controller, 12 for four freezers); the pack has no dedicated quad freezer, any extra freezer is another 3x3x3 with the same controller. The shell is 25 frostproof casings (14 minimum, the rest can be hatches); one casing batch is 6 aluminium plates + 1 frame → 2 casings.
    - |-
      Titanium uses right away: 8 titanium plates → 1 EV machine casing (assembler, circuit 8, 50 ticks at 16 EU/t) → EV hull with 2 aluminium cables + 288 mB polyethylene. Titanium foil has an extra pack flag; rods and plates are standard.
    - |-
      A plain titanium dust (from the ruby slurry 2 % chance, for example) also blasts: titanium has an automatic EBF recipe (1941 K, 1500 ticks, 480 EU/t, circuit 1, plus a gas variant). It is not a route, just a way to use stray dust.
    - |-
      Unverified: how many fluid output hatches the Distillation Tower needs for the 7-fluid molten mixture recipe (build 7 layers with 7 hatches to be safe), whether every crushed ore satisfies the EV mixer recycle tag (read the recipe in EMI), and where your carbon dust comes from (read the carbon dust recipe in EMI).
  b:
    - ["gtceu:distillation_tower", 1]
    - ["gtceu:ev_mixer", 1]
    - ["gtceu:hv_autoclave", 1]
    - ["gtceu:lv_pulverizer", 2]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:kanthal_coil_block", 16]
    - ["gtceu:ev_energy_input_hatch", 2]
    - ["gtceu:hv_energy_input_hatch", 3]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:lv_electrolyzer", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 14]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["gtceu:ev_mixer", "gtceu:molten_ore_mixture_bucket", "gtceu:steel_drum"]
      t: |-
        Mixture first. Easy EV route: an EV Mixer with 16 crushed ores of any kind, 32 stone dust and 32 B lava makes 6 B molten ore mixture in 40 s (1920 EU/t). Use junk crushed ore from the sieves. Three input drawers (crushed ore, stone dust) and a drum of lava, all pulled by Modular Routers or Pipez filters; the output goes into a steel drum. The Void Extractor slurry line (250 mB per B of slurry) also feeds the same drum. Tower runs need 10 B at once, so cap this drum with a pump cover at 10 B or more.
    - i: ["gtceu:distillation_tower", "gtceu:molten_ilmenite_ore_bucket", "gtceu:steel_drum"]
      t: Distillation Tower (the refinery tower, EV). Buffer drum of mixture in, 10 B per run, 60 s at 1920 EU/t. It makes 1.5 B molten bauxite, 1.25 B pitchblende, 1 B molybdenite, 1 B ilmenite, 1 B bastnasite, 2 B tungstate, 2.25 B cooperite and 1 metal mixture dust. One drum per fluid, never shared. A filtered pump or Pipez fluid pipe takes only molten ilmenite to the autoclave. Collect bauxite too (see tips).
    - i: ["gtceu:hv_autoclave", "gtceu:raw_ilmenite", "gtceu:stone_dust"]
      t: |-
        HV Autoclave on its own: 1 stone dust + 500 mB molten ilmenite ore → 1 raw ilmenite in 8 s at 480 EU/t. Stone dust drawer (from the cobble line, one macerator) on one face, ilmenite drum on another, a Robot Arm cover in Keep Exact mode with 64 stops the output drawer. 2 raw ilmenite per tower run, so the autoclave is idle most of the time.
    - i: ["gtceu:lv_pulverizer", "gtceu:crushed_ilmenite_ore"]
      t: LV Pulverizer 1, only raw ilmenite → 2 crushed ilmenite ore in 15 s at 30 EU/t (same machine as the realgar line). Item Filter on the drawer so the pulverizer never gets anything else. Never share it with the dust pulverizer below.
    - i: ["gtceu:lv_pulverizer", "gtceu:ilmenite_dust"]
      t: |-
        LV Pulverizer 2 with ghost circuit 0: crushed ilmenite ore → 1 ilmenite dust (+25 % bonus dust) in 15 s at 30 EU/t. The pack defines this crushed → dust recipe for every ore in its processing tables, ilmenite included. A separate machine, because it holds the circuit that the first pulverizer must not have.
    - i: ["gtceu:electric_blast_furnace", "gtceu:cupronickel_coil_block", "gtceu:rutile_dust", "gtceu:carbon_dust"]
      t: |-
        EBF 1 (stainless EBF with cupronickel coils is fine): input bus holds ilmenite dust and carbon dust, one bus for each if you can (10 ilmenite + 2 carbon per run, no circuit). 1700 K, 80 s at 480 EU/t. It outputs 2 rutile dust, 2 wrought iron ingots and 2 B carbon monoxide: add a fluid output hatch or the recipe stops. Send the iron to storage, CO to a drum.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:chlorine_bucket", "gtceu:titanium_tetrachloride_bucket"]
      t: |-
        HV Chemical Reactor (or the LCR): 1 rutile dust + 2 carbon dust + 4 B chlorine → 1 B titanium tetrachloride + 2 B carbon monoxide, 20 s at 480 EU/t, no circuit. Chlorine comes from the salt chain through a drum with a pump cover. TiCl4 goes into its own drum. The reactor also needs a CO drum on its fluid output, and CO must be emptied or burned or both reactor and EBF 1 stall.
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:kanthal_coil_block
        - gtceu:hot_titanium_ingot
        - gtceu:magnesium_chloride_dust
      t: |-
        EBF 2 with Kanthal coils (its own furnace, no other recipe): input bus holds 2 magnesium dust, input hatch takes 1 B TiCl4. Recipe 2141 K, 40 s at 480 EU/t, no circuit: it outputs 1 HOT titanium ingot and 6 magnesium chloride dust. Cupronickel coils do not reach it. A sub-step people skip: the hot ingot is not usable, it must be cooled.
    - i: ["gtceu:vacuum_freezer", "gtceu:titanium_ingot"]
      t: |-
        Vacuum Freezer: Robot Arm cover or Pipez item pipe from the EBF 2 output bus to the freezer input bus (a drawer in between is fine, but keep it only for hot ingots). 1 hot titanium ingot → titanium ingot in 7.2 s at 480 EU/t. HV energy hatch is enough, no coolant for titanium. Output drawer with a Keep Exact Robot Arm at 64 stops the chain.
    - i: ["gtceu:lv_electrolyzer", "gtceu:magnesium_dust", "gtceu:chlorine_bucket"]
      t: |-
        Close the loop with an LV Electrolyzer: 3 magnesium chloride dust → 1 magnesium dust + 2 B chlorine, about 4.5 s at 30 EU/t. Feed magnesium chloride from EBF 2’s output bus; send magnesium back to the EBF 2 magnesium drawer and chlorine back to the chlorine drum. The input must be a multiple of 3 (one run uses 3, one ingot makes 6).
    - i: ["gtceu:magnesite_dust", "gtceu:magnesium_dust"]
      t: |-
        Start-up magnesium: the first 2 magnesium dust per ingot you build before the loop is full come from the slurry line (crushed magnesite), then electrolysed in an MV Electrolyzer (magnesite is 1 magnesium + 1 carbon + 3 oxygen, so 5 dust → 1 magnesium + 1 carbon dust + 3 B oxygen, 60 EU/t). Do it once; do not feed magnesite into the loop.
---
# Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `titanium_line` · **Tags:** Infinite source, Unverified

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Titanium (molten ore line)](../../plan/p9.md#titanium)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-dt">
<div class="gt-head"><span class="gt-mname">Distillation Tower · 60 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Molten ore mixture · 10 B (gtceu:molten_ore_mixture_bucket) - 10 B"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ore_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ore Mixture Bucket</span><span class="gt-note">Molten ore mixture · 10 B</span><span class="gt-tag">infinite</span><b class="gt-q">10 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Molten ilmenite ore · 1 B (gtceu:molten_ilmenite_ore_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ilmenite_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ilmenite Ore</span><span class="gt-note">Molten ilmenite ore · 1 B</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
<div class="gt-panel t-hv" id="m-ac">
<div class="gt-head"><span class="gt-mname">HV Autoclave · 8 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Molten ilmenite ore · 1 B (gtceu:molten_ilmenite_ore_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ilmenite_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ilmenite Ore</span><span class="gt-note">Molten ilmenite ore · 1 B</span><b class="gt-q">500 mB</b></span><span class="gt-slot" title="Stone dust (gtceu:stone_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__stone_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Raw ilmenite (gtceu:raw_ilmenite) - 1 / 8 s"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ilmenite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ilmenite</span><span class="gt-note">2 Raw ilmenite</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-lv" id="m-p1">
<div class="gt-head"><span class="gt-mname">LV Pulverizer · 15 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Raw ilmenite (gtceu:raw_ilmenite) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ilmenite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ilmenite</span><span class="gt-note">2 Raw ilmenite</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_pulverizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Crushed ilmenite ore (gtceu:crushed_ilmenite_ore) - 1 → 2"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_ilmenite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Ilmenite Ore</span><span class="gt-note">4 Crushed ilmenite ore</span><b class="gt-q">1 → 2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_pulverizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-p2">
<div class="gt-head"><span class="gt-mname">LV Pulverizer · circuit 0 · 15 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Crushed ilmenite ore (gtceu:crushed_ilmenite_ore) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_ilmenite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Ilmenite Ore</span><span class="gt-note">4 Crushed ilmenite ore</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_pulverizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Ilmenite dust (gtceu:ilmenite_dust) - 1 (+25 %)"><img class="gt-ico" src="../../assets/icons/gtceu__ilmenite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilmenite Dust</span><b class="gt-q">1 (+25 %)</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_pulverizer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF · 1700 K · 80 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ilmenite dust (gtceu:ilmenite_dust) - 10"><img class="gt-ico" src="../../assets/icons/gtceu__ilmenite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilmenite Dust</span><b class="gt-q">10</b></span><span class="gt-slot" title="Carbon dust (gtceu:carbon_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">80 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Rutile dust (gtceu:rutile_dust) - 2 / 80 s"><img class="gt-ico" src="../../assets/icons/gtceu__rutile_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rutile Dust</span><span class="gt-note">2 Rutile dust</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 Wrought iron ingot (gtceu:wrought_iron_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Ingot</span><span class="gt-note">2 Wrought iron ingot</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-hv" id="m-rx">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 20 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Rutile dust (gtceu:rutile_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rutile_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rutile Dust</span><span class="gt-note">2 Rutile dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="Carbon dust (gtceu:carbon_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dust</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="Chlorine · 4 B (gtceu:chlorine_bucket) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><span class="gt-note">Chlorine · 4 B</span><b class="gt-q">4 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Titanium tetrachloride · 1 B (gtceu:titanium_tetrachloride_bucket) - 1 B / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_tetrachloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Tetrachloride</span><span class="gt-note">Titanium tetrachloride · 1 B</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF · Kanthal 2141 K · 40 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Titanium tetrachloride · 1 B (gtceu:titanium_tetrachloride_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_tetrachloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Tetrachloride</span><span class="gt-note">Titanium tetrachloride · 1 B</span><b class="gt-q">1 B</b></span><span class="gt-slot" title="2 Magnesium dust (gtceu:magnesium_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__magnesium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnesium Dust</span><span class="gt-note">2 Magnesium dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot titanium ingot (gtceu:hot_titanium_ingot) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Titanium Ingot</span><b class="gt-q">1</b></span><span class="gt-slot" title="6 Magnesium chloride dust (gtceu:magnesium_chloride_dust) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__magnesium_chloride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnesium Chloride Dust</span><span class="gt-note">6 Magnesium chloride dust</span><b class="gt-q">6</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 7.2 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot titanium ingot (gtceu:hot_titanium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Titanium Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">7.2 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Titanium ingot (gtceu:titanium_ingot) - 1 / 7.2 s"><img class="gt-ico" src="../../assets/icons/gtceu__titanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Titanium Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-lv" id="m-el">
<div class="gt-head"><span class="gt-mname">LV Electrolyzer · 4.5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 Magnesium chloride dust (gtceu:magnesium_chloride_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__magnesium_chloride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnesium Chloride Dust</span><span class="gt-note">6 Magnesium chloride dust</span><b class="gt-q">3</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Magnesium dust (back) (gtceu:magnesium_dust) - 1 per 3"><img class="gt-ico" src="../../assets/icons/gtceu__magnesium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnesium Dust</span><span class="gt-note">2 Magnesium dust (back)</span><b class="gt-q">1 per 3</b></span><span class="gt-slot gt-fluid" title="4 B chlorine (back) (gtceu:chlorine_bucket) - 2 B per 3"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><span class="gt-note">4 B chlorine (back)</span><b class="gt-q">2 B per 3</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electrolyzer</code></div>
</div>
</div>

## Flow

- [Distillation Tower · 60 s · 1920 EU/t](#m-dt) → [HV Autoclave · 8 s · 480 EU/t](#m-ac) → [LV Pulverizer · 15 s](#m-p1) → [LV Pulverizer · circuit 0 · 15 s](#m-p2) → [EBF · 1700 K · 80 s · 480 EU/t](#m-e1) → [HV Chemical Reactor · 20 s · 480 EU/t](#m-rx) → [EBF · Kanthal 2141 K · 40 s · 480 EU/t](#m-e2) → [Vacuum Freezer · 7.2 s · 480 EU/t](#m-vf) (also EBF · Kanthal 2141 K · 40 s · 480 EU/t → [LV Electrolyzer · 4.5 s · 30 EU/t](#m-el))
- [LV Electrolyzer · 4.5 s · 30 EU/t](#m-el)

## How to build

1. Mixture first. Easy EV route: an EV Mixer with 16 crushed ores of any kind, 32 stone dust and 32 B lava makes 6 B molten ore mixture in 40 s (1920 EU/t). Use junk crushed ore from the sieves. Three input drawers (crushed ore, stone dust) and a drum of lava, all pulled by Modular Routers or Pipez filters; the output goes into a steel drum. The Void Extractor slurry line (250 mB per B of slurry) also feeds the same drum. Tower runs need 10 B at once, so cap this drum with a pump cover at 10 B or more. — `gtceu:ev_mixer`, `gtceu:molten_ore_mixture_bucket`, `gtceu:steel_drum`
2. Distillation Tower (the refinery tower, EV). Buffer drum of mixture in, 10 B per run, 60 s at 1920 EU/t. It makes 1.5 B molten bauxite, 1.25 B pitchblende, 1 B molybdenite, 1 B ilmenite, 1 B bastnasite, 2 B tungstate, 2.25 B cooperite and 1 metal mixture dust. One drum per fluid, never shared. A filtered pump or Pipez fluid pipe takes only molten ilmenite to the autoclave. Collect bauxite too (see tips). — `gtceu:distillation_tower`, `gtceu:molten_ilmenite_ore_bucket`, `gtceu:steel_drum`
3. HV Autoclave on its own: 1 stone dust + 500 mB molten ilmenite ore → 1 raw ilmenite in 8 s at 480 EU/t. Stone dust drawer (from the cobble line, one macerator) on one face, ilmenite drum on another, a Robot Arm cover in Keep Exact mode with 64 stops the output drawer. 2 raw ilmenite per tower run, so the autoclave is idle most of the time. — `gtceu:hv_autoclave`, `gtceu:raw_ilmenite`, `gtceu:stone_dust`
4. LV Pulverizer 1, only raw ilmenite → 2 crushed ilmenite ore in 15 s at 30 EU/t (same machine as the realgar line). Item Filter on the drawer so the pulverizer never gets anything else. Never share it with the dust pulverizer below. — `gtceu:lv_pulverizer`, `gtceu:crushed_ilmenite_ore`
5. LV Pulverizer 2 with ghost circuit 0: crushed ilmenite ore → 1 ilmenite dust (+25 % bonus dust) in 15 s at 30 EU/t. The pack defines this crushed → dust recipe for every ore in its processing tables, ilmenite included. A separate machine, because it holds the circuit that the first pulverizer must not have. — `gtceu:lv_pulverizer`, `gtceu:ilmenite_dust`
6. EBF 1 (stainless EBF with cupronickel coils is fine): input bus holds ilmenite dust and carbon dust, one bus for each if you can (10 ilmenite + 2 carbon per run, no circuit). 1700 K, 80 s at 480 EU/t. It outputs 2 rutile dust, 2 wrought iron ingots and 2 B carbon monoxide: add a fluid output hatch or the recipe stops. Send the iron to storage, CO to a drum. — `gtceu:electric_blast_furnace`, `gtceu:cupronickel_coil_block`, `gtceu:rutile_dust`, `gtceu:carbon_dust`
7. HV Chemical Reactor (or the LCR): 1 rutile dust + 2 carbon dust + 4 B chlorine → 1 B titanium tetrachloride + 2 B carbon monoxide, 20 s at 480 EU/t, no circuit. Chlorine comes from the salt chain through a drum with a pump cover. TiCl4 goes into its own drum. The reactor also needs a CO drum on its fluid output, and CO must be emptied or burned or both reactor and EBF 1 stall. — `gtceu:hv_chemical_reactor`, `gtceu:chlorine_bucket`, `gtceu:titanium_tetrachloride_bucket`
8. EBF 2 with Kanthal coils (its own furnace, no other recipe): input bus holds 2 magnesium dust, input hatch takes 1 B TiCl4. Recipe 2141 K, 40 s at 480 EU/t, no circuit: it outputs 1 HOT titanium ingot and 6 magnesium chloride dust. Cupronickel coils do not reach it. A sub-step people skip: the hot ingot is not usable, it must be cooled. — `gtceu:electric_blast_furnace`, `gtceu:kanthal_coil_block`, `gtceu:hot_titanium_ingot`, `gtceu:magnesium_chloride_dust`
9. Vacuum Freezer: Robot Arm cover or Pipez item pipe from the EBF 2 output bus to the freezer input bus (a drawer in between is fine, but keep it only for hot ingots). 1 hot titanium ingot → titanium ingot in 7.2 s at 480 EU/t. HV energy hatch is enough, no coolant for titanium. Output drawer with a Keep Exact Robot Arm at 64 stops the chain. — `gtceu:vacuum_freezer`, `gtceu:titanium_ingot`
10. Close the loop with an LV Electrolyzer: 3 magnesium chloride dust → 1 magnesium dust + 2 B chlorine, about 4.5 s at 30 EU/t. Feed magnesium chloride from EBF 2’s output bus; send magnesium back to the EBF 2 magnesium drawer and chlorine back to the chlorine drum. The input must be a multiple of 3 (one run uses 3, one ingot makes 6). — `gtceu:lv_electrolyzer`, `gtceu:magnesium_dust`, `gtceu:chlorine_bucket`
11. Start-up magnesium: the first 2 magnesium dust per ingot you build before the loop is full come from the slurry line (crushed magnesite), then electrolysed in an MV Electrolyzer (magnesite is 1 magnesium + 1 carbon + 3 oxygen, so 5 dust → 1 magnesium + 1 carbon dust + 3 B oxygen, 60 EU/t). Do it once; do not feed magnesite into the loop. — `gtceu:magnesite_dust`, `gtceu:magnesium_dust`

## Tips

- Per ingot: 1 rutile, 2 carbon for the reactor, 4 B chlorine and 2 magnesium. The magnesium and chlorine come back: 6 magnesium chloride dust electrolyse (3 dust → 1 magnesium + 2 B chlorine, twice) into exactly the 2 magnesium and 4 B chlorine the next ingot needs. After the first fill the loop only loses what you spill.
- Rutile is the real cost. The pack EBF recipe gives 2 rutile + 2 wrought iron + 2 B carbon monoxide from 10 ilmenite dust + 2 carbon dust (1700 K, 80 s, 480 EU/t), so 5 ilmenite dust per rutile. One tower run (10 B mixture) gives 1 B molten ilmenite = 2 raw ilmenite = 4 crushed ore = 5 dust = 1 rutile = 1 titanium ingot, and the same run gives 1.5 B molten bauxite = 3 raw bauxite = about 7.5 dust.
- Bauxite helps: electrolysing 15 bauxite dust gives 6 aluminium + 1 rutile + 9 B oxygen (270 ticks, 60 EU/t, source SeparationRecipes), so the bauxite from the same tower run adds about 0.5 rutile on top.
- Better yield: the Electric Ore Factory treats ilmenite as an EV ore (EV hatch, 1920 EU/t, 16 s, 100 mB sodium persulfate per crushed ore). It gives 1 dust (+50 %), 25 % iron, 12.5 % iron and 7.5 % rutile, so 4 crushed ore give 6 dust and 0.3 rutile instead of 5 dust. Source: systems/ore\_factory\_processing.js. Use it once sodium persulfate flows; the pulverizer line works without.
- Molten ore mixture is the bottleneck. EV Mixer recycle: 16 crushed ores (any ore tagged crushed ores) + 32 stone dust + 32 B lava → 6 B mixture in 40 s at 1920 EU/t. One ingot needs 10 B, so 1.7 runs, about 27 crushed ore, 53 stone dust and 53 B lava. The tower also returns 1 metal mixture dust per run; the IV mixer loop (2 metal mixture + 48 stone dust + 48 B lava → 20 B) is the late fix, not an EV one. Tiers of the whole side line: Void Extractor LV, slurry centrifuge MV, residue electrolysis HV, raw-ore autoclave HV, recycle mixer and tower EV, loop mixer IV. Without the tower 1 B of slurry gives only 250 mB of mixture (about 57 extractor runs per 10 B tower batch), so the EV recycle mixer is the real fix.
- Coil heat: the titanium recipe needs 2141 K (titanium 1941 K + 200). Cupronickel is 1800 K, 2000 K even with an EV hatch, so it fails. Kanthal is 2700 K and an HV hatch is enough (the recipe is 480 EU/t). Build the Kanthal line first (chain: Kanthal). The rutile EBF (1700 K) works on cupronickel.
- Vacuum Freezer: 1 hot titanium ingot → 1 titanium ingot in 144 ticks (7.2 s, mass 48 x 3 ticks) at 480 EU/t, an HV hatch. Controller recipe: 3 HV pumps + 3 EV circuits + 1 frostproof casing + 2 gold cables, so the first EV circuits are needed for the freezer even though it runs on an HV hatch (3 per controller, 12 for four freezers); the pack has no dedicated quad freezer, any extra freezer is another 3x3x3 with the same controller. The shell is 25 frostproof casings (14 minimum, the rest can be hatches); one casing batch is 6 aluminium plates + 1 frame → 2 casings.
- Titanium uses right away: 8 titanium plates → 1 EV machine casing (assembler, circuit 8, 50 ticks at 16 EU/t) → EV hull with 2 aluminium cables + 288 mB polyethylene. Titanium foil has an extra pack flag; rods and plates are standard.
- A plain titanium dust (from the ruby slurry 2 % chance, for example) also blasts: titanium has an automatic EBF recipe (1941 K, 1500 ticks, 480 EU/t, circuit 1, plus a gas variant). It is not a route, just a way to use stray dust.
- **Unverified** how many fluid output hatches the Distillation Tower needs for the 7-fluid molten mixture recipe (build 7 layers with 7 hatches to be safe), whether every crushed ore satisfies the EV mixer recycle tag (read the recipe in EMI), and where your carbon dust comes from (read the carbon dust recipe in EMI).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:distillation_tower` | 1 |
| `gtceu:ev_mixer` | 1 |
| `gtceu:hv_autoclave` | 1 |
| `gtceu:lv_pulverizer` | 2 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:kanthal_coil_block` | 16 |
| `gtceu:ev_energy_input_hatch` | 2 |
| `gtceu:hv_energy_input_hatch` | 3 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:lv_electrolyzer` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 14 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Needs:** [Raw Ore Slurry &amp; mineral mixtures](../mv/slurry.md), [Infinite cobble &amp; blackstone](../stone/inf_cobble.md), [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md)
- **Feeds:** [EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull](ev_components.md)
- **Main source for:** `gtceu:rutile_dust`, `gtceu:hot_titanium_ingot`, `gtceu:titanium_ingot`, `gtceu:titanium_tetrachloride_bucket`, `gtceu:ilmenite_dust`, `gtceu:raw_ilmenite`, `gtceu:crushed_ilmenite_ore`, `gtceu:molten_ilmenite_ore_bucket`, `gtceu:magnesium_chloride_dust`
