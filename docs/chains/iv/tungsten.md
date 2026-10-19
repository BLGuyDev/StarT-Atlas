---
kind: chain
id: tungsten
order: 570
data:
  t: |-
    Tungsten and tungsten steel: chemical bath → electrolyzer → EBF 3600 K (nichrome coils) → Vacuum Freezer
  "n":
    - [tg, Tungstate or scheelite dust, i, "gtceu:tungstate_dust"]
    - [hc, "Hydrochloric acid · 2 B", f, "gtceu:hydrochloric_acid_bucket"]
    - [cb, "EV Chemical Bath · 10.5 s · 960 EU/t", m, "gtceu:ev_chemical_bath"]
    - [ta, "7 Tungstic acid dust", x, "gtceu:tungstic_acid_dust"]
    - [el, "EV Electrolyzer · 10.5 s · 960 EU/t", m, "gtceu:ev_electrolyzer"]
    - [w, Tungsten dust, x, "gtceu:tungsten_dust"]
    - [ho, "2 B hydrogen + 4 B oxygen", f, "gtceu:hydrogen_bucket"]
    - [sd, Steel dust, i, "gtceu:steel_dust"]
    - [mx, "EV Mixer · circuit 1 · 10 s · 1920 EU/t", m, "gtceu:ev_mixer"]
    - [td, "2 Tungsten steel dust", x, "gtceu:tungsten_steel_dust"]
    - [he, "Helium · 1 B (optional)", f, "gtceu:helium_bucket"]
    - [e1, "EBF · Nichrome 3000 K · 50 s · 1920 EU/t", m, "gtceu:electric_blast_furnace"]
    - [ht, Hot tungsten steel ingot, x, "gtceu:hot_tungsten_steel_ingot"]
    - [v1, "Vacuum Freezer · about 18 s · 480 EU/t", m, "gtceu:vacuum_freezer"]
    - [ts, Tungsten steel ingot, o, "gtceu:tungsten_steel_ingot"]
    - [e2, "EBF · Nichrome 3600 K · 90 s · 1920 EU/t", m, "gtceu:electric_blast_furnace"]
    - [hw, Hot tungsten ingot, x, "gtceu:hot_tungsten_ingot"]
    - [v2, "Vacuum Freezer · 15 s · 480 EU/t", m, "gtceu:vacuum_freezer"]
    - [tw, Tungsten ingot, o, "gtceu:tungsten_ingot"]
  e:
    - [tg, cb, "7"]
    - [hc, cb, "2 B"]
    - [cb, ta, "7 / 10.5 s"]
    - [ta, el, "7"]
    - [el, w, "1 / 10.5 s"]
    - [el, ho]
    - [w, mx, "1"]
    - [sd, mx, "1"]
    - [mx, td, "2 / 10 s"]
    - [td, e1, "1"]
    - [he, e1, circuit 2]
    - [e1, ht, "1 / 50 s"]
    - [ht, v1, "1"]
    - [v1, ts, "1"]
    - [w, e2, "1"]
    - [he, e2, circuit 2]
    - [e2, hw, "1 / 90 s"]
    - [hw, v2, "1"]
    - [v2, tw, "1"]
  tips:
    - |-
      Tungstic acid is a CHEMICAL BATH recipe, not a reactor one (ChemicalBathRecipes): 7 tungstate dust + 2 B hydrochloric acid → 7 tungstic acid dust + 4 lithium chloride dust, 210 ticks at 960 EU/t. Scheelite instead: 6 scheelite dust + 2 B acid → 7 tungstic acid + 3 calcium chloride. 960 EU/t is above the HV 480, so the bath is an EV machine; the old step list that says “Chemical Reactor” is wrong.
    - |-
      Electrolysis (SeparationRecipes): 7 tungstic acid dust → 1 tungsten dust + 2 B hydrogen + 4 B oxygen, 210 ticks at 960 EU/t in an EV Electrolyzer. So one tungsten costs 7 tungstate dust. That ratio, not the power, paces the whole era: a motor needs about 2.5 tungsten (2 for the double cables, 0.5 for the rod ingot) = 17 tungstate dust. The ZPM Chemical Plant skip does it 1 : 1 (kjs chemical_plant.js tungstate_line), which is the later fix.
    - |-
      Tungsten steel: EV Mixer circuit 1, 1 tungsten dust + 1 steel dust → 2 tungsten steel dust, 200 ticks at 1920 EU/t (MixerRecipes). EBF recipe: 3000 K, 1920 EU/t (VA[EV]), 1000 ticks = 50 s per ingot, then the Vacuum Freezer (480 EU/t, mass-based time, about 18 s). Both EBF numbers come from SecondDegreeMaterials; the 50 s is per single ingot, the mixer batch of 2 dust gives 2 ingots in 100 s of one furnace.
    - |-
      Tungsten ingot (for wires, cables and the coil recipes): EBF 3600 K, 1920 EU/t, 1800 ticks = 90 s, Vacuum Freezer 300 ticks (15 s) at 480 EU/t (ElementMaterials: tungsten blast 3600 K, vacuumStats(VA[HV], 300)). Tungsten dust goes either into the mixer or into this furnace, never both: keep two separate drawers.
    - |-
      Coils: 3600 K needs Nichrome coils exactly (jar CoilType: cupronickel 1800, kanthal 2700, nichrome 3600, RTM 4500, HSS-G 5400). Kanthal 2700 K plus 200 K from an EV hatch is only 2900 K, not enough for the 3000 K of tungsten steel. The furnace therefore needs an EV Energy Hatch and 16 Nichrome coil blocks (the nichrome_line chain). Also needed: a vacuum freezer or two.
    - |-
      Helium: tungsten and tungsten steel are gas tier “mid” = helium (jar GasTier). Circuit 2 plus 1 B helium per ingot runs the same recipe in 67 % of the time (about 34 s for tungsten steel, 60 s for tungsten). Optional: without helium use circuit 1.
    - |-
      Alloy Blast Smelter alternative: circuit 2, 1 steel dust + 1 tungsten dust → 288 mB molten tungsten steel (2 ingots) in 1500 ticks (75 s) at 1920 EU/t, 3000 K (AlloyBlastRecipeProducer: base 1000 ticks × 2 × 3/4). That is 37.5 s per ingot against the EBF’s 50 s plus 18 s of cooling, but it needs the multiblock; see the abs_super_ebf chain.
    - |-
      Sources of the ore: crushed tungstate ore (15 %) and crushed scheelite ore (12.5 %) come from the Ex Nihilo sieve with an EMERALD mesh on gravel (kjs sieving.js); the Electric Ore Factory also processes both. Unverified: the exact ore → pure dust steps and which of tungstate and scheelite is cheaper per tungsten (scheelite is 6 dust for the same 7 acid).
    - |-
      Sub-steps people skip: (1) hot ingots must be frozen before the wiremill or the assembler accepts them; (2) 2 dust from the mixer = 2 ingots, but each recipe in the EBF eats ONE dust; (3) steel dust for the mixer is its own drawer, not the steel ingot drawer; (4) the chemical bath needs the acid as a fluid, so the bath has a fluid hatch; (5) with Kanthal coils the 3000 K recipe never starts, so check the coil tier before blaming the power.
    - |-
      Unverified: the helium amount per recipe is read from the class constant 1000 mB; the freezer times use an assumed average component mass of 120 for tungsten steel.
  b:
    - ["gtceu:ev_chemical_bath", 1]
    - ["gtceu:ev_electrolyzer", 1]
    - ["gtceu:ev_mixer", 1]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:nichrome_coil_block", 32]
    - ["gtceu:ev_energy_input_hatch", 2]
    - ["gtceu:vacuum_freezer", 2]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 3]
  inf: true
  how:
    - i: ["functionalstorage:oak_1", "gtceu:tungstate_dust", "gtceu:scheelite_dust", "gtceu:steel_dust"]
      t: |-
        Input drawers first: tungstate or scheelite dust, steel dust, plus one drum each for hydrochloric acid, hydrogen/oxygen by-product and helium. One Modular Router or Pipez item pipe with an Item Filter from each drawer to exactly one machine; every output drawer gets a Robot Arm cover in Keep Exact mode (64 for dusts, 16 for ingots).
    - i: ["gtceu:ev_chemical_bath", "gtceu:tungstic_acid_dust"]
      t: |-
        EV Chemical Bath: 7 tungstate dust (or 6 scheelite) in the input bus, 2 B hydrochloric acid in a fluid hatch from the acid drum, 210 ticks at 960 EU/t → 7 tungstic acid dust plus lithium chloride (calcium chloride) dust. The by-product dust goes to its own output slot or drawer; do not let it clog the acid’s drawer.
    - i: ["gtceu:ev_electrolyzer", "gtceu:tungsten_dust"]
      t: |-
        EV Electrolyzer, own machine: 7 tungstic acid dust → 1 tungsten dust + 2 B hydrogen + 4 B oxygen in 10.5 s at 960 EU/t. Vent or store the gases in their own drums; the hydrogen is useful for the oil_distill chain. The output drawer of tungsten dust splits two ways, so use two Item Filter routes, one to the mixer and one to the tungsten EBF.
    - i: ["gtceu:ev_mixer", "gtceu:tungsten_steel_dust"]
      t: |-
        EV Mixer with ghost circuit 1: 1 tungsten dust + 1 steel dust → 2 tungsten steel dust in 10 s at 1920 EU/t. This is the only EV recipe on that mixer; do not switch it to nichrome or any other circuit, give those their own machines (the nichrome_line chain uses the MV one).
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:nichrome_coil_block
        - gtceu:ev_energy_input_hatch
        - gtceu:hot_tungsten_steel_ingot
      t: |-
        Dedicated EBF for tungsten steel: 16 Nichrome coil blocks, an EV Energy Hatch (1920 EU/t), input bus with ghost circuit 1 (circuit 2 + a helium hatch for the fast recipe), output bus. 1 dust → 1 hot tungsten steel ingot in 50 s. Keep its output set to a Robot Arm into the freezer’s bus.
    - i: ["gtceu:vacuum_freezer", "gtceu:tungsten_steel_ingot"]
      t: |-
        Vacuum Freezer after the furnace: Robot Arm cover from the EBF output bus (Item Filter on hot tungsten steel ingot) into its input bus, 480 EU/t, about 18 s per ingot, no coolant (below 5000 K). The sub-step people skip: the hot ingot looks like a normal one but nothing crafts with it. Output drawer with Keep Exact at 64: motors, pistons and plates all pull from here.
    - i: ["gtceu:electric_blast_furnace", "gtceu:hot_tungsten_ingot", "gtceu:tungsten_ingot"]
      t: Second EBF for the tungsten ingot (3600 K, nichrome coils exactly, EV hatch, 90 s per ingot) with its own Vacuum Freezer (15 s at 480 EU/t). These ingots become the wire for the IV cables, part of the RTM alloy and the molten tungsten of the HSS-G coil recipe. A single furnace that switches recipes also works if you accept the delay.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:tungsten_steel_ingot"]
      t: |-
        Easy to miss: once you have the Alloy Blast Smelter, steel dust + tungsten dust go straight into it (circuit 2) and give molten tungsten steel for the pump rotors and the coil recipes; the mixer, EBF and first freezer disappear from this line.
---
# Tungsten and tungsten steel: chemical bath → electrolyzer → EBF 3600 K (nichrome coils) → Vacuum Freezer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `tungsten` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [Tungsten and tungsten steel](../../plan/p10.md#tungsten)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-cb">
<div class="gt-head"><span class="gt-mname">EV Chemical Bath · 10.5 s · 960 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungstate or scheelite dust (gtceu:tungstate_dust) - 7"><img class="gt-ico" src="../../assets/icons/gtceu__tungstate_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungstate Dust</span><span class="gt-note">Tungstate or scheelite dust</span><b class="gt-q">7</b></span><span class="gt-slot gt-fluid" title="Hydrochloric acid · 2 B (gtceu:hydrochloric_acid_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrochloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrochloric Acid</span><span class="gt-note">Hydrochloric acid · 2 B</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_bath.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">10.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="7 Tungstic acid dust (gtceu:tungstic_acid_dust) - 7 / 10.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__tungstic_acid_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungstic Acid Dust</span><span class="gt-note">7 Tungstic acid dust</span><b class="gt-q">7</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_bath</code></div>
</div>
<div class="gt-panel t-ev" id="m-el">
<div class="gt-head"><span class="gt-mname">EV Electrolyzer · 10.5 s · 960 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="7 Tungstic acid dust (gtceu:tungstic_acid_dust) - 7"><img class="gt-ico" src="../../assets/icons/gtceu__tungstic_acid_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungstic Acid Dust</span><span class="gt-note">7 Tungstic acid dust</span><b class="gt-q">7</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">10.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Tungsten dust (gtceu:tungsten_dust) - 1 / 10.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="2 B hydrogen + 4 B oxygen (gtceu:hydrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><span class="gt-note">2 B hydrogen + 4 B oxygen</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_electrolyzer</code></div>
</div>
<div class="gt-panel t-ev" id="m-mx">
<div class="gt-head"><span class="gt-mname">EV Mixer · circuit 1 · 10 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten dust (gtceu:tungsten_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="Steel dust (gtceu:steel_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Tungsten steel dust (gtceu:tungsten_steel_dust) - 2 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Dust</span><span class="gt-note">2 Tungsten steel dust</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF · Nichrome 3000 K · 50 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Tungsten steel dust (gtceu:tungsten_steel_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Dust</span><span class="gt-note">2 Tungsten steel dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Helium · 1 B (optional) (gtceu:helium_bucket) - circuit 2"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium · 1 B (optional)</span><b class="gt-q">circuit 2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot tungsten steel ingot (gtceu:hot_tungsten_steel_ingot) - 1 / 50 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Tungsten Steel Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-v1">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · about 18 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot tungsten steel ingot (gtceu:hot_tungsten_steel_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Tungsten Steel Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Tungsten steel ingot (gtceu:tungsten_steel_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Steel Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF · Nichrome 3600 K · 90 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tungsten dust (gtceu:tungsten_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Helium · 1 B (optional) (gtceu:helium_bucket) - circuit 2"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span><span class="gt-note">Helium · 1 B (optional)</span><b class="gt-q">circuit 2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot tungsten ingot (gtceu:hot_tungsten_ingot) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_tungsten_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Tungsten Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-v2">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 15 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot tungsten ingot (gtceu:hot_tungsten_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_tungsten_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Tungsten Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Tungsten ingot (gtceu:tungsten_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [EV Chemical Bath · 10.5 s · 960 EU/t](#m-cb) → [EV Electrolyzer · 10.5 s · 960 EU/t](#m-el) → [EV Mixer · circuit 1 · 10 s · 1920 EU/t](#m-mx) → [EBF · Nichrome 3000 K · 50 s · 1920 EU/t](#m-e1) → [Vacuum Freezer · about 18 s · 480 EU/t](#m-v1) (also EV Electrolyzer · 10.5 s · 960 EU/t → [EBF · Nichrome 3600 K · 90 s · 1920 EU/t](#m-e2))
- [EBF · Nichrome 3600 K · 90 s · 1920 EU/t](#m-e2) → [Vacuum Freezer · 15 s · 480 EU/t](#m-v2)

## How to build

1. Input drawers first: tungstate or scheelite dust, steel dust, plus one drum each for hydrochloric acid, hydrogen/oxygen by-product and helium. One Modular Router or Pipez item pipe with an Item Filter from each drawer to exactly one machine; every output drawer gets a Robot Arm cover in Keep Exact mode (64 for dusts, 16 for ingots). — `functionalstorage:oak_1`, `gtceu:tungstate_dust`, `gtceu:scheelite_dust`, `gtceu:steel_dust`
2. EV Chemical Bath: 7 tungstate dust (or 6 scheelite) in the input bus, 2 B hydrochloric acid in a fluid hatch from the acid drum, 210 ticks at 960 EU/t → 7 tungstic acid dust plus lithium chloride (calcium chloride) dust. The by-product dust goes to its own output slot or drawer; do not let it clog the acid’s drawer. — `gtceu:ev_chemical_bath`, `gtceu:tungstic_acid_dust`
3. EV Electrolyzer, own machine: 7 tungstic acid dust → 1 tungsten dust + 2 B hydrogen + 4 B oxygen in 10.5 s at 960 EU/t. Vent or store the gases in their own drums; the hydrogen is useful for the oil\_distill chain. The output drawer of tungsten dust splits two ways, so use two Item Filter routes, one to the mixer and one to the tungsten EBF. — `gtceu:ev_electrolyzer`, `gtceu:tungsten_dust`
4. EV Mixer with ghost circuit 1: 1 tungsten dust + 1 steel dust → 2 tungsten steel dust in 10 s at 1920 EU/t. This is the only EV recipe on that mixer; do not switch it to nichrome or any other circuit, give those their own machines (the nichrome\_line chain uses the MV one). — `gtceu:ev_mixer`, `gtceu:tungsten_steel_dust`
5. Dedicated EBF for tungsten steel: 16 Nichrome coil blocks, an EV Energy Hatch (1920 EU/t), input bus with ghost circuit 1 (circuit 2 + a helium hatch for the fast recipe), output bus. 1 dust → 1 hot tungsten steel ingot in 50 s. Keep its output set to a Robot Arm into the freezer’s bus. — `gtceu:electric_blast_furnace`, `gtceu:nichrome_coil_block`, `gtceu:ev_energy_input_hatch`, `gtceu:hot_tungsten_steel_ingot`
6. Vacuum Freezer after the furnace: Robot Arm cover from the EBF output bus (Item Filter on hot tungsten steel ingot) into its input bus, 480 EU/t, about 18 s per ingot, no coolant (below 5000 K). The sub-step people skip: the hot ingot looks like a normal one but nothing crafts with it. Output drawer with Keep Exact at 64: motors, pistons and plates all pull from here. — `gtceu:vacuum_freezer`, `gtceu:tungsten_steel_ingot`
7. Second EBF for the tungsten ingot (3600 K, nichrome coils exactly, EV hatch, 90 s per ingot) with its own Vacuum Freezer (15 s at 480 EU/t). These ingots become the wire for the IV cables, part of the RTM alloy and the molten tungsten of the HSS-G coil recipe. A single furnace that switches recipes also works if you accept the delay. — `gtceu:electric_blast_furnace`, `gtceu:hot_tungsten_ingot`, `gtceu:tungsten_ingot`
8. Easy to miss: once you have the Alloy Blast Smelter, steel dust + tungsten dust go straight into it (circuit 2) and give molten tungsten steel for the pump rotors and the coil recipes; the mixer, EBF and first freezer disappear from this line. — `gtceu:alloy_blast_smelter`, `gtceu:tungsten_steel_ingot`

## Tips

- Tungstic acid is a CHEMICAL BATH recipe, not a reactor one (ChemicalBathRecipes): 7 tungstate dust + 2 B hydrochloric acid → 7 tungstic acid dust + 4 lithium chloride dust, 210 ticks at 960 EU/t. Scheelite instead: 6 scheelite dust + 2 B acid → 7 tungstic acid + 3 calcium chloride. 960 EU/t is above the HV 480, so the bath is an EV machine; the old step list that says “Chemical Reactor” is wrong.
- Electrolysis (SeparationRecipes): 7 tungstic acid dust → 1 tungsten dust + 2 B hydrogen + 4 B oxygen, 210 ticks at 960 EU/t in an EV Electrolyzer. So one tungsten costs 7 tungstate dust. That ratio, not the power, paces the whole era: a motor needs about 2.5 tungsten (2 for the double cables, 0.5 for the rod ingot) = 17 tungstate dust. The ZPM Chemical Plant skip does it 1 : 1 (kjs chemical\_plant.js tungstate\_line), which is the later fix.
- Tungsten steel: EV Mixer circuit 1, 1 tungsten dust + 1 steel dust → 2 tungsten steel dust, 200 ticks at 1920 EU/t (MixerRecipes). EBF recipe: 3000 K, 1920 EU/t (VA\[EV\]), 1000 ticks = 50 s per ingot, then the Vacuum Freezer (480 EU/t, mass-based time, about 18 s). Both EBF numbers come from SecondDegreeMaterials; the 50 s is per single ingot, the mixer batch of 2 dust gives 2 ingots in 100 s of one furnace.
- Tungsten ingot (for wires, cables and the coil recipes): EBF 3600 K, 1920 EU/t, 1800 ticks = 90 s, Vacuum Freezer 300 ticks (15 s) at 480 EU/t (ElementMaterials: tungsten blast 3600 K, vacuumStats(VA\[HV\], 300)). Tungsten dust goes either into the mixer or into this furnace, never both: keep two separate drawers.
- Coils: 3600 K needs Nichrome coils exactly (jar CoilType: cupronickel 1800, kanthal 2700, nichrome 3600, RTM 4500, HSS-G 5400). Kanthal 2700 K plus 200 K from an EV hatch is only 2900 K, not enough for the 3000 K of tungsten steel. The furnace therefore needs an EV Energy Hatch and 16 Nichrome coil blocks (the nichrome\_line chain). Also needed: a vacuum freezer or two.
- Helium: tungsten and tungsten steel are gas tier “mid” = helium (jar GasTier). Circuit 2 plus 1 B helium per ingot runs the same recipe in 67 % of the time (about 34 s for tungsten steel, 60 s for tungsten). Optional: without helium use circuit 1.
- Alloy Blast Smelter alternative: circuit 2, 1 steel dust + 1 tungsten dust → 288 mB molten tungsten steel (2 ingots) in 1500 ticks (75 s) at 1920 EU/t, 3000 K (AlloyBlastRecipeProducer: base 1000 ticks × 2 × 3/4). That is 37.5 s per ingot against the EBF’s 50 s plus 18 s of cooling, but it needs the multiblock; see the abs\_super\_ebf chain.
- Sources of the ore: crushed tungstate ore (15 %) and crushed scheelite ore (12.5 %) come from the Ex Nihilo sieve with an EMERALD mesh on gravel (kjs sieving.js); the Electric Ore Factory also processes both. Unverified: the exact ore → pure dust steps and which of tungstate and scheelite is cheaper per tungsten (scheelite is 6 dust for the same 7 acid).
- Sub-steps people skip: (1) hot ingots must be frozen before the wiremill or the assembler accepts them; (2) 2 dust from the mixer = 2 ingots, but each recipe in the EBF eats ONE dust; (3) steel dust for the mixer is its own drawer, not the steel ingot drawer; (4) the chemical bath needs the acid as a fluid, so the bath has a fluid hatch; (5) with Kanthal coils the 3000 K recipe never starts, so check the coil tier before blaming the power.
- **Unverified** the helium amount per recipe is read from the class constant 1000 mB; the freezer times use an assumed average component mass of 120 for tungsten steel.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:ev_chemical_bath` | 1 |
| `gtceu:ev_electrolyzer` | 1 |
| `gtceu:ev_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:nichrome_coil_block` | 32 |
| `gtceu:ev_energy_input_hatch` | 2 |
| `gtceu:vacuum_freezer` | 2 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Needs:** [Molten Ore Mixture](../ev/molten_mix.md)
