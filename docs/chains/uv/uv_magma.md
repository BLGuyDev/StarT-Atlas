---
kind: chain
id: uv_magma
order: 1750
data:
  t: Abydos dense magma → residues, lava and 12 raw ores (titanite, xenotime, monazite, scheelite; zapolite, crookesite, kitkaite, lautarite; naquadite, magnesite, chromite, magnetite)
  inf: true
  "n":
    - - dm
      - |-
        Dense magma 25 B: refractory / reactive / naquadite (Abydos veins, 400 to 540 yield)
      - f
      - gtceu:abydos_refractory_dense_magma_bucket
    - - cs
      - Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance)
      - m
      - gtceu:cyclonic_sifter
    - [rd, "Dense residue 16 B (+ 1 magma slag dust)", f, "gtceu:refractory_dense_residue_bucket"]
    - [d1, "Molten Destabiliser · 54 s · 245 760 EU/t · 300 B magma", m, "gtceu:molten_destabiliser"]
    - [d2, "Molten Destabiliser · 42 s · 245 760 EU/t · 60 B residue", m, "gtceu:molten_destabiliser"]
    - - r1
      - |-
        Refractory: 4 titanite · 3 xenotime · 2 monazite · 1 scheelite (raw)
      - g
      - functionalstorage:oak_1
      - - [Raw titanite, "gtceu:raw_titanite"]
        - [Raw xenotime, "gtceu:raw_xenotime"]
        - [Raw monazite, "gtceu:raw_monazite"]
        - [Raw scheelite, "gtceu:raw_scheelite"]
    - - r2
      - |-
        Reactive: 4 zapolite · 3 crookesite · 2 kitkaite · 1 lautarite (raw)
      - g
      - functionalstorage:oak_1
      - - [Raw zapolite, "gtceu:raw_zapolite"]
        - [Raw crookesite, "gtceu:raw_crookesite"]
        - [Raw kitkaite, "gtceu:raw_kitkaite"]
        - [Raw lautarite, "gtceu:raw_lautarite"]
    - - r3
      - |-
        Naquadite: 4 naquadite · 3 magnesite · 2 chromite · 1 magnetite (raw)
      - g
      - functionalstorage:oak_1
      - - [Raw naquadite, "gtceu:raw_naquadite"]
        - [Raw magnesite, "gtceu:raw_magnesite"]
        - [Raw chromite, "gtceu:raw_chromite"]
        - [Raw magnetite, "gtceu:raw_magnetite"]
    - [lv, "290 B lava (per 300 B magma)", f, "minecraft:lava_bucket"]
    - [sc, "EV Centrifuge · 17 s · 960 EU/t · 7 slag dust", m, "gtceu:ev_centrifuge"]
    - - sl
      - "3 strontianite · 2 celestine · 1 metal mixture · 1 gypsum"
      - g
      - functionalstorage:oak_1
      - - [Strontianite dust, "gtceu:strontianite_dust"]
        - [Celestine dust, "gtceu:celestine_dust"]
        - [Metal mixture dust, "gtceu:metal_mixture_dust"]
        - [Gypsum dust, "gtceu:gypsum_dust"]
  e:
    - [dm, cs, "25 B"]
    - [cs, rd, "16 B / 12 s"]
    - [dm, d1, "300 B"]
    - [d1, r1, per type]
    - [d1, r2, per type]
    - [d1, r3, per type]
    - [d1, lv, "290 B"]
    - [rd, d2, "60 B"]
    - [d2, r1, "8/6/5/3"]
    - [cs, sc, slag]
    - [sc, sl, "7 → 7"]
  tips:
    - |-
      Source: kjs abydos_lines/magma.js (verified). Three magma types come from the Abydos fluid veins (kjs utils/fluid_veins.js: abydos_reactive_dense_magma weight 25 and abydos_naquadite_dense_magma weight 28, both yield 400 to 540; the refractory vein is analogous: Unverified numbers) pumped by the ZPM Fluid Drilling Rig (uv_akreyrium). Cyclonic Sifter: 25 B magma + 1 netherite reinforced mesh (chancedInput 300, -20: about a 3 % chance per recipe of consuming it, plus tier loss; Unverified exact meaning) → 16 B residue + 1 magma slag dust, 240 ticks at VHA[ZPM] x 0.8 = 49 152 EU/t.
    - |-
      Molten Destabiliser (UV, VHA[UV] = 245 760 EU/t): 300 B magma → 290 B lava + raws: refractory 4 raw titanite + 3 xenotime + 2 monazite + 1 scheelite; reactive 4 zapolite + 3 crookesite + 2 kitkaite + 1 lautarite; naquadite 4 naquadite + 3 magnesite + 2 chromite + 1 magnetite; 1080 ticks (54 s). Residues: 60 B residue → 50 B molten ore mixture + 8 / 6 / 5 / 3 raws of the same family, 840 ticks (42 s). Sift first: 300 B of magma straight into the destabiliser gives 10 raws, but through the sifter it becomes 192 B of residue = 3.2 residue runs = about 22 x 3.2 = 70 raws (and 1 slag per sifter run), so the sifter path yields about 7 times more ore per magma. Slag: 7 abydos magma slag dust → 3 strontianite + 2 celestine + 1 metal mixture + 1 gypsum in an EV centrifuge (342 ticks, 960 EU/t).
    - |-
      Where each raw ore goes (kjs abydos_lines, verified): xenotime → yttrium, lutetium, dysprosium, europium, samarium (uv_rare_earth); titanite → zirconium (UHV page); zapolite → zapolgium (UHV page); naquadite → naquadah dust via hydroiodic acid (kjs naquadite.js: 4 naquadite dust + 500 mB hydroiodic acid → 1 B naquadite solution, then a ZPM centrifuge → 2 naquadah + magnesia + magnetite); scheelite → tungsten (chemical plant skip recipe), chromite → chromium, strontianite/celestine → strontium (for the boosted growth medium of uv_bio2), monazite → rare earth / thorium (Unverified), crookesite, kitkaite, lautarite: thallium, selenium and iodine ores (Unverified).
    - |-
      Lava 290 B per run is a fluid output: pipe it into a lava drum or a Large Stone Barrel; a full lava hatch stops the destabiliser. The raws are still raw ores: they go into the normal ore line (crusher, washer, centrifuge) before the chemistry.
    - |-
      Sub-steps people skip: (1) three magma types need three input drums, never one hatch; (2) the destabiliser must have the lava output handled; (3) netherite reinforced mesh (assembler: carbon fiber mesh + 4 netherite rods + 1 netherite ingot + 288 mB epoxy, IV power, 5 s) has to be stocked: Keep Exact 8; (4) always sift before you destabilise (7x yield).
    - |-
      Unverified: the refractory vein numbers, mesh chance semantics, ore processing of the thallium family.
  b:
    - ["gtceu:cyclonic_sifter", 1]
    - ["gtceu:molten_destabiliser", 1]
    - ["gtceu:ev_centrifuge", 1]
    - ["gtceu:uv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 10]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:netherite_reinforced_mesh
        - gtceu:raw_xenotime
        - gtceu:abydos_magma_slag_dust
      t: |-
        Drawers first: netherite reinforced meshes (Keep Exact 8), magma slag dust, and one output drawer per raw ore (12 types). Drums: the three magmas, three residues, molten ore mixture, lava.
    - i: ["gtceu:cyclonic_sifter", "gtceu:refractory_dense_residue_bucket"]
      t: |-
        Sifter: 25 B magma per 12 s with a mesh. One sifter per magma type is not needed: switch with a pump valve between the three drums and clear the input hatch in between.
    - i: ["gtceu:molten_destabiliser", "gtceu:raw_titanite", "minecraft:lava_bucket"]
      t: |-
        Destabiliser: 300 B magma → raws every 54 s; lava into a drum or a Large Stone Barrel. A second recipe on residues (60 B, 42 s) → molten ore mixture + raws.
    - i: ["gtceu:ev_centrifuge", "gtceu:strontianite_dust"]
      t: |-
        Slag centrifuge: 7 slag dust → 3 strontianite + 2 celestine + 1 metal mixture + 1 gypsum; four output drawers.
    - i: ["gtceu:molten_ore_mixture_bucket", "functionalstorage:oak_1"]
      t: |-
        Molten ore mixture (50 B per residue run) is the input of the later ore lines (Unverified use): keep a drum.
    - i: ["gtceu:raw_zapolite", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: raw ores pile up fast (a single destabiliser run gives 10 raws); size the drawer banks and route each ore to its own line.
---
# Abydos dense magma → residues, lava and 12 raw ores (titanite, xenotime, monazite, scheelite; zapolite, crookesite, kitkaite, lautarite; naquadite, magnesite, chromite, magnetite)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_magma` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Abydos first: xenotime → dysprosium → drilling rig and magma](../../plan/p14.md#abydos)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cs">
<div class="gt-head"><span class="gt-mname">Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance)</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Dense magma 25 B: refractory / reactive / naquadite (Abydos veins, 400 to 540 yield) (gtceu:abydos_refractory_dense_magma_bucket) - 25 B"><img class="gt-ico" src="../../assets/icons/gtceu__abydos_refractory_dense_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Abydos Refractory Dense Magma</span><span class="gt-note">Dense magma 25 B: refractory / reactive / naquadite (Abydos veins, 400 to 540 yield)</span><b class="gt-q">25 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Dense residue 16 B (+ 1 magma slag dust) (gtceu:refractory_dense_residue_bucket) - 16 B / 12 s"><img class="gt-ico" src="../../assets/icons/gtceu__refractory_dense_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Refractory Dense Residue</span><span class="gt-note">Dense residue 16 B (+ 1 magma slag dust)</span><b class="gt-q">16 B</b></span><a class="gt-slot gt-mach" href="#m-sc" title="EV Centrifuge · 17 s · 960 EU/t · 7 slag dust (gtceu:ev_centrifuge) - slag"><img class="gt-ico" src="../../assets/icons/gtceu__ev_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Centrifuge</span><span class="gt-note">EV Centrifuge · 17 s · 960 EU/t · 7 slag dust</span><b class="gt-q">slag</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:cyclonic_sifter</code></div>
</div>
<div class="gt-panel t-mod" id="m-d1">
<div class="gt-head"><span class="gt-mname">Molten Destabiliser · 54 s · 245 760 EU/t · 300 B magma</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Dense magma 25 B: refractory / reactive / naquadite (Abydos veins, 400 to 540 yield) (gtceu:abydos_refractory_dense_magma_bucket) - 300 B"><img class="gt-ico" src="../../assets/icons/gtceu__abydos_refractory_dense_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Abydos Refractory Dense Magma</span><span class="gt-note">Dense magma 25 B: refractory / reactive / naquadite (Abydos veins, 400 to 540 yield)</span><b class="gt-q">300 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__molten_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Refractory: 4 titanite · 3 xenotime · 2 monazite · 1 scheelite (raw) (functionalstorage:oak_1) - per type"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Refractory: 4 titanite · 3 xenotime · 2 monazite · 1 scheelite (raw)</span><span class="gt-sub"><span>Raw titanite</span><span>Raw xenotime</span><span>Raw monazite</span><span>Raw scheelite</span></span><b class="gt-q">per type</b></span><span class="gt-slot gt-group" title="Reactive: 4 zapolite · 3 crookesite · 2 kitkaite · 1 lautarite (raw) (functionalstorage:oak_1) - per type"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Reactive: 4 zapolite · 3 crookesite · 2 kitkaite · 1 lautarite (raw)</span><span class="gt-sub"><span>Raw zapolite</span><span>Raw crookesite</span><span>Raw kitkaite</span><span>Raw lautarite</span></span><b class="gt-q">per type</b></span><span class="gt-slot gt-group" title="Naquadite: 4 naquadite · 3 magnesite · 2 chromite · 1 magnetite (raw) (functionalstorage:oak_1) - per type"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Naquadite: 4 naquadite · 3 magnesite · 2 chromite · 1 magnetite (raw)</span><span class="gt-sub"><span>Raw naquadite</span><span>Raw magnesite</span><span>Raw chromite</span><span>Raw magnetite</span></span><b class="gt-q">per type</b></span><span class="gt-slot gt-fluid" title="290 B lava (per 300 B magma) (minecraft:lava_bucket) - 290 B"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava</span><span class="gt-note">290 B lava (per 300 B magma)</span><b class="gt-q">290 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:molten_destabiliser</code></div>
</div>
<div class="gt-panel t-mod" id="m-d2">
<div class="gt-head"><span class="gt-mname">Molten Destabiliser · 42 s · 245 760 EU/t · 60 B residue</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Dense residue 16 B (+ 1 magma slag dust) (gtceu:refractory_dense_residue_bucket) - 60 B"><img class="gt-ico" src="../../assets/icons/gtceu__refractory_dense_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Refractory Dense Residue</span><span class="gt-note">Dense residue 16 B (+ 1 magma slag dust)</span><b class="gt-q">60 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__molten_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Refractory: 4 titanite · 3 xenotime · 2 monazite · 1 scheelite (raw) (functionalstorage:oak_1) - 8/6/5/3"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Refractory: 4 titanite · 3 xenotime · 2 monazite · 1 scheelite (raw)</span><span class="gt-sub"><span>Raw titanite</span><span>Raw xenotime</span><span>Raw monazite</span><span>Raw scheelite</span></span><b class="gt-q">8/6/5/3</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:molten_destabiliser</code></div>
</div>
<div class="gt-panel t-ev" id="m-sc">
<div class="gt-head"><span class="gt-mname">EV Centrifuge · 17 s · 960 EU/t · 7 slag dust</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-cs" title="Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance) (gtceu:cyclonic_sifter) - slag"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cyclonic Sifter</span><span class="gt-note">Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance)</span><b class="gt-q">slag</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="3 strontianite · 2 celestine · 1 metal mixture · 1 gypsum (functionalstorage:oak_1) - 7 → 7"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">3 strontianite · 2 celestine · 1 metal mixture · 1 gypsum</span><span class="gt-sub"><span>Strontianite dust</span><span>Celestine dust</span><span>Metal mixture dust</span><span>Gypsum dust</span></span><b class="gt-q">7 → 7</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_centrifuge</code></div>
</div>
</div>

## Flow

- [Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance)](#m-cs) → [Molten Destabiliser · 42 s · 245 760 EU/t · 60 B residue](#m-d2) (also Cyclonic Sifter · 12 s · 49 152 EU/t · netherite reinforced mesh (30 % chance) → [EV Centrifuge · 17 s · 960 EU/t · 7 slag dust](#m-sc))
- [Molten Destabiliser · 54 s · 245 760 EU/t · 300 B magma](#m-d1)
- [EV Centrifuge · 17 s · 960 EU/t · 7 slag dust](#m-sc)

## How to build

1. Drawers first: netherite reinforced meshes (Keep Exact 8), magma slag dust, and one output drawer per raw ore (12 types). Drums: the three magmas, three residues, molten ore mixture, lava. — `functionalstorage:oak_1`, `kubejs:netherite_reinforced_mesh`, `gtceu:raw_xenotime`, `gtceu:abydos_magma_slag_dust`
2. Sifter: 25 B magma per 12 s with a mesh. One sifter per magma type is not needed: switch with a pump valve between the three drums and clear the input hatch in between. — `gtceu:cyclonic_sifter`, `gtceu:refractory_dense_residue_bucket`
3. Destabiliser: 300 B magma → raws every 54 s; lava into a drum or a Large Stone Barrel. A second recipe on residues (60 B, 42 s) → molten ore mixture + raws. — `gtceu:molten_destabiliser`, `gtceu:raw_titanite`, `minecraft:lava_bucket`
4. Slag centrifuge: 7 slag dust → 3 strontianite + 2 celestine + 1 metal mixture + 1 gypsum; four output drawers. — `gtceu:ev_centrifuge`, `gtceu:strontianite_dust`
5. Molten ore mixture (50 B per residue run) is the input of the later ore lines (Unverified use): keep a drum. — `gtceu:molten_ore_mixture_bucket`, `functionalstorage:oak_1`
6. Easy to miss: raw ores pile up fast (a single destabiliser run gives 10 raws); size the drawer banks and route each ore to its own line. — `gtceu:raw_zapolite`, `functionalstorage:oak_1`

## Tips

- Source: kjs abydos\_lines/magma.js (verified). Three magma types come from the Abydos fluid veins (kjs utils/fluid\_veins.js: abydos\_reactive\_dense\_magma weight 25 and abydos\_naquadite\_dense\_magma weight 28, both yield 400 to 540; the refractory vein is analogous: Unverified numbers) pumped by the ZPM Fluid Drilling Rig (uv\_akreyrium). Cyclonic Sifter: 25 B magma + 1 netherite reinforced mesh (chancedInput 300, -20: about a 3 % chance per recipe of consuming it, plus tier loss; Unverified exact meaning) → 16 B residue + 1 magma slag dust, 240 ticks at VHA\[ZPM\] x 0.8 = 49 152 EU/t.
- Molten Destabiliser (UV, VHA\[UV\] = 245 760 EU/t): 300 B magma → 290 B lava + raws: refractory 4 raw titanite + 3 xenotime + 2 monazite + 1 scheelite; reactive 4 zapolite + 3 crookesite + 2 kitkaite + 1 lautarite; naquadite 4 naquadite + 3 magnesite + 2 chromite + 1 magnetite; 1080 ticks (54 s). Residues: 60 B residue → 50 B molten ore mixture + 8 / 6 / 5 / 3 raws of the same family, 840 ticks (42 s). Sift first: 300 B of magma straight into the destabiliser gives 10 raws, but through the sifter it becomes 192 B of residue = 3.2 residue runs = about 22 x 3.2 = 70 raws (and 1 slag per sifter run), so the sifter path yields about 7 times more ore per magma. Slag: 7 abydos magma slag dust → 3 strontianite + 2 celestine + 1 metal mixture + 1 gypsum in an EV centrifuge (342 ticks, 960 EU/t).
- Where each raw ore goes (kjs abydos\_lines, verified): xenotime → yttrium, lutetium, dysprosium, europium, samarium (uv\_rare\_earth); titanite → zirconium (UHV page); zapolite → zapolgium (UHV page); naquadite → naquadah dust via hydroiodic acid (kjs naquadite.js: 4 naquadite dust + 500 mB hydroiodic acid → 1 B naquadite solution, then a ZPM centrifuge → 2 naquadah + magnesia + magnetite); scheelite → tungsten (chemical plant skip recipe), chromite → chromium, strontianite/celestine → strontium (for the boosted growth medium of uv\_bio2), monazite → rare earth / thorium (Unverified), crookesite, kitkaite, lautarite: thallium, selenium and iodine ores (Unverified).
- Lava 290 B per run is a fluid output: pipe it into a lava drum or a Large Stone Barrel; a full lava hatch stops the destabiliser. The raws are still raw ores: they go into the normal ore line (crusher, washer, centrifuge) before the chemistry.
- Sub-steps people skip: (1) three magma types need three input drums, never one hatch; (2) the destabiliser must have the lava output handled; (3) netherite reinforced mesh (assembler: carbon fiber mesh + 4 netherite rods + 1 netherite ingot + 288 mB epoxy, IV power, 5 s) has to be stocked: Keep Exact 8; (4) always sift before you destabilise (7x yield).
- **Unverified** the refractory vein numbers, mesh chance semantics, ore processing of the thallium family.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:cyclonic_sifter` | 1 |
| `gtceu:molten_destabiliser` | 1 |
| `gtceu:ev_centrifuge` | 1 |
| `gtceu:uv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Main source for:** `gtceu:raw_xenotime`, `gtceu:raw_titanite`, `gtceu:raw_zapolite`, `gtceu:raw_naquadite`, `gtceu:abydos_magma_slag_dust`
