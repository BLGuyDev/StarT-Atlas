---
kind: chain
id: uv_bio2
order: 1550
data:
  t: |-
    Sterile bio line 2: collagen → gelatin → agar, then raw medium, sterilized growth medium and stem cells (Sterile Cleanroom)
  inf: true
  "n":
    - - g1
      - "1 meat dust · 1 bone meal · 500 mB sulfuric acid"
      - g
      - functionalstorage:oak_1
      - - [Meat dust, "gtceu:meat_dust"]
        - [Bone meal, "minecraft:bone_meal"]
        - [Sulfuric acid, "gtceu:sulfuric_acid_bucket"]
    - [c1, "HV Chemical Reactor · 40 s · 480 EU/t · Sterile Cleanroom", m, "gtceu:hv_chemical_reactor"]
    - - g2
      - "4 collagen dust · 1 B phosphoric acid · 3 B water"
      - g
      - functionalstorage:oak_1
      - [[Collagen dust, "gtceu:collagen_dust"], [Phosphoric acid, "gtceu:phosphoric_acid_bucket"]]
    - [m1, "HV Mixer · 80 s · 480 EU/t", m, "gtceu:hv_mixer"]
    - [ce, "HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus", m, "gtceu:hv_centrifuge"]
    - [au, "HV Autoclave · 30 s · 1 gelatin + 1 B distilled water", m, "gtceu:hv_autoclave"]
    - [ag, Agar dust, x, "gtceu:agar_dust"]
    - - g3
      - |-
        4 meat · 4 salt · 3 calcium · 4 agar · 1 strontium dust · 4 B mutagen
      - g
      - functionalstorage:oak_1
      - - [Salt dust, "gtceu:salt_dust"]
        - [Calcium dust, "gtceu:calcium_dust"]
        - [Strontium dust, "gtceu:strontium_dust"]
        - [Mutagen, "gtceu:mutagen_bucket"]
    - [m2, "IV Mixer · 75 s · 7680 EU/t · Sterile Cleanroom", m, "gtceu:iv_mixer"]
    - [fh, "IV Fluid Heater · circuit 1 · 1 s per 100 mB · 7680 EU/t", m, "gtceu:iv_fluid_heater"]
    - [sm, Sterilized growth medium, f, "gtceu:sterilized_growth_medium_bucket"]
    - - g4
      - "1 osmiridium dust · 500 mB bacteria · 500 mB sterile medium"
      - g
      - functionalstorage:oak_1
      - [[Osmiridium dust, "gtceu:osmiridium_dust"], [Bacteria, "gtceu:bacteria_bucket"]]
    - [r2, "LuV Chemical Reactor · 15 s · 30 720 EU/t · Sterile Cleanroom", m, "gtceu:luv_chemical_reactor"]
    - [sc, "Stem cells (32 per run)", o, "gtceu:stem_cells"]
  e:
    - [g1, c1, "1"]
    - [c1, g2, collagen]
    - [g2, m1, "1 / 80 s"]
    - [m1, ce, "4 B"]
    - [ce, au, gelatin]
    - [au, ag, "1 / 30 s"]
    - [ag, g3, "4"]
    - [g3, m2, "1"]
    - [m2, fh, "7.5 B / 75 s"]
    - [fh, sm, "100 mB / s"]
    - [sm, g4, "500 mB"]
    - [g4, r2, "1"]
    - [r2, sc, "32 / 15 s"]
  tips:
    - |-
      Verified chain (gtsrc GrowthMediumRecipes + pack kjs): collagen = chemical reactor, 1 meat dust + 1 bone meal + 500 mB sulfuric acid → 1 collagen dust + 500 mB diluted sulfuric acid, 800 ticks at VA[HV] (the 2 meat + 1 bone + 1 B acid version is 1600 ticks). Gelatin mixture = mixer, 4 collagen + 1 B phosphoric acid + 3 B water → 4 B, 1600 ticks. Centrifuge 6 B mixture → 4 gelatin + 1 phosphorus, 2400 ticks. Agar = autoclave, 1 gelatin + 1 B distilled water, 600 ticks. All four are Sterile Cleanroom recipes at VA[HV] = 480 EU/t.
    - |-
      Raw growth medium: the pack REPLACED the GT recipe (kjs additions/recipe_changes.js): mixer, circuit 1, 4 meat + 4 salt + 4 calcium + 4 agar + 4 B mutagen → 4 B raw medium, 1200 ticks at VA[IV]. circuits.js adds a boosted version: 4 meat + 4 salt + 3 calcium + 4 agar + 1 strontium dust + 4 B mutagen → 7.5 B raw medium, 1500 ticks at VA[IV]. Always use the boosted one: 1.875 B of medium per B of mutagen against 1 B. Sterilization: fluid heater, circuit 1, 100 mB raw → 100 mB sterile, 20 ticks at VA[IV] (Sterile Cleanroom).
    - |-
      Stem cells (GrowthMediumRecipes stem_cells): chemical reactor, 1 osmiridium dust + 500 mB bacteria + 500 mB sterile medium → 32 stem cells + 500 mB bacterial sludge, 300 ticks at VA[LuV] = 30 720 EU/t (a LuV reactor), Sterile Cleanroom. The returned sludge is not waste: send it to bio line 1 (uv_bio1) to enrich. A neuro processing unit eats 16 stem cells, so one run makes the cells for 2 units.
    - |-
      Budget (see uv_wetware): every 4 B of sterile medium makes 16 wetware boards; each neuro unit needs 250 mB of medium plus 16 stem cells (a 500 mB medium run gives the cells for 2 units, so 250 mB more per unit). That is about 500 mB of sterile medium per neuro unit, i.e. about 270 mB of mutagen with the boosted mixer (7.5 B of medium per 4 B of mutagen).
    - |-
      Bacterial machines (verified, bacterial_multiblocks.js): the Bacterial Runic Mutator [BRM] = UV hull + 4 UV motors + melodium gear + 6 ZPM emitters + 4 UV circuits + 576 mB naquadria, VHA[ZPM], research ZPM fermenter 32 CWU/t; the Bacterial Breeding Vat [BBV] and Bacterial Hydrocarbon Harvester [BHH] = UV hull + 4 UV pumps (each UV pump holds a UV motor). Every UV motor needs a dysprosium magnet rod, so Abydos (uv_akreyrium, uv_rare_earth) comes BEFORE these machines; the melodium gear needs the 10 000 K melodium superconductor (tritanium coils). The biostimulating mixture does NOT depend on Abydos: Large Chemical Reactor, VHA[IV], 150 mB silicic acid + 250 mB seaweed oil + 325 mB liquefied nutrient paste + 25 mB fermented biomass + 250 mB glycerol -> 1000 mB.
    - |-
      Sub-steps people skip: (1) agar needs DISTILLED water, not plain water; the gelatin mixer uses plain water; (2) meat dust, salt, calcium and strontium dust each need their own drawer: use Keep Exact 4 / 4 / 3 / 1 and one router with an Item Filter per drawer; (3) circuit 1 on both the mixer and the fluid heater; (4) stem cells return bacterial sludge: do not let the output hatch fill, or the reactor stalls.
    - |-
      Unverified: meat dust, salt, calcium and strontium sources; the phosphoric acid line; whether any pack script changes the collagen or agar recipes (nothing found in kubejs).
  b:
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:hv_mixer", 1]
    - ["gtceu:hv_centrifuge", 1]
    - ["gtceu:hv_autoclave", 1]
    - ["gtceu:iv_mixer", 1]
    - ["gtceu:iv_fluid_heater", 1]
    - ["gtceu:luv_chemical_reactor", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:meat_dust", "gtceu:salt_dust", "gtceu:calcium_dust"]
      t: |-
        Drawers first, one per solid: meat dust (Keep Exact 4), bone meal, salt dust, calcium dust, strontium dust (Keep Exact 1), osmiridium dust. Steel drums for sulfuric acid, phosphoric acid, plain water, distilled water, mutagen, raw medium, sterile medium, bacteria. All machines are inside the Sterile Cleanroom.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:collagen_dust"]
      t: |-
        Collagen: one HV chemical reactor, bone meal and meat dust by one router (Item Filter on both), sulfuric acid by Pipez; dump the diluted acid into its own drum. 40 s per dust.
    - i: ["gtceu:hv_mixer", "gtceu:hv_centrifuge", "gtceu:hv_autoclave"]
      t: |-
        Gelatin line, one machine each and nothing shared: mixer (4 collagen + 1 B phosphoric + 3 B water, 80 s), centrifuge (6 B → 4 gelatin, 120 s), autoclave (gelatin + 1 B distilled, 30 s). Agar goes into an output drawer, Keep Exact 16.
    - i: ["gtceu:iv_mixer", "gtceu:agar_dust", "gtceu:strontium_dust"]
      t: |-
        Raw medium: IV mixer, circuit 1. Drawers feed it through one router with five Item Filters; mutagen by Pipez from the bio line 1 drum. 7.5 B of raw medium per 75 s.
    - i: ["gtceu:iv_fluid_heater", "gtceu:sterilized_growth_medium_bucket"]
      t: Fluid heater, circuit 1, raw medium in by Pipez, sterile medium out into a drum. Keep 8 B in the drum, the boards and neuro units pull from it.
    - i: ["gtceu:luv_chemical_reactor", "gtceu:stem_cells"]
      t: |-
        Stem cell reactor: osmiridium drawer + bacteria + sterile medium by fluid pipes; the 500 mB sludge goes back to line 1. Output drawer Keep Exact 64.
---
# Sterile bio line 2: collagen → gelatin → agar, then raw medium, sterilized growth medium and stem cells (Sterile Cleanroom)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_bio2` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Sterile bio lines](../../plan/p14.md#uvbio)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-c1">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 40 s · 480 EU/t · Sterile Cleanroom</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 meat dust · 1 bone meal · 500 mB sulfuric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 meat dust · 1 bone meal · 500 mB sulfuric acid</span><span class="gt-sub"><span>Meat dust</span><span>Bone meal</span><span>Sulfuric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="4 collagen dust · 1 B phosphoric acid · 3 B water (functionalstorage:oak_1) - collagen"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 collagen dust · 1 B phosphoric acid · 3 B water</span><span class="gt-sub"><span>Collagen dust</span><span>Phosphoric acid</span></span><b class="gt-q">collagen</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-m1">
<div class="gt-head"><span class="gt-mname">HV Mixer · 80 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 collagen dust · 1 B phosphoric acid · 3 B water (functionalstorage:oak_1) - 1 / 80 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 collagen dust · 1 B phosphoric acid · 3 B water</span><span class="gt-sub"><span>Collagen dust</span><span>Phosphoric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">80 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ce" title="HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus (gtceu:hv_centrifuge) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Centrifuge</span><span class="gt-note">HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus</span><b class="gt-q">4 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_mixer</code></div>
</div>
<div class="gt-panel t-hv" id="m-ce">
<div class="gt-head"><span class="gt-mname">HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="HV Mixer · 80 s · 480 EU/t (gtceu:hv_mixer) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Mixer</span><span class="gt-note">HV Mixer · 80 s · 480 EU/t</span><b class="gt-q">4 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-au" title="HV Autoclave · 30 s · 1 gelatin + 1 B distilled water (gtceu:hv_autoclave) - gelatin"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Autoclave</span><span class="gt-note">HV Autoclave · 30 s · 1 gelatin + 1 B distilled water</span><b class="gt-q">gelatin</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_centrifuge</code></div>
</div>
<div class="gt-panel t-hv" id="m-au">
<div class="gt-head"><span class="gt-mname">HV Autoclave · 30 s · 1 gelatin + 1 B distilled water</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ce" title="HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus (gtceu:hv_centrifuge) - gelatin"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Centrifuge</span><span class="gt-note">HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus</span><b class="gt-q">gelatin</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Agar dust (gtceu:agar_dust) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__agar_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Agar Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-iv" id="m-m2">
<div class="gt-head"><span class="gt-mname">IV Mixer · 75 s · 7680 EU/t · Sterile Cleanroom</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 meat · 4 salt · 3 calcium · 4 agar · 1 strontium dust · 4 B mutagen (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 meat · 4 salt · 3 calcium · 4 agar · 1 strontium dust · 4 B mutagen</span><span class="gt-sub"><span>Salt dust</span><span>Calcium dust</span><span>Strontium dust</span><span>Mutagen</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-fh" title="IV Fluid Heater · circuit 1 · 1 s per 100 mB · 7680 EU/t (gtceu:iv_fluid_heater) - 7.5 B / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_fluid_heater.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Fluid Heater</span><span class="gt-note">IV Fluid Heater · circuit 1 · 1 s per 100 mB · 7680 EU/t</span><b class="gt-q">7.5 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-iv" id="m-fh">
<div class="gt-head"><span class="gt-mname">IV Fluid Heater · circuit 1 · 1 s per 100 mB · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="IV Mixer · 75 s · 7680 EU/t · Sterile Cleanroom (gtceu:iv_mixer) - 7.5 B / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Mixer</span><span class="gt-note">IV Mixer · 75 s · 7680 EU/t · Sterile Cleanroom</span><b class="gt-q">7.5 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_fluid_heater.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sterilized growth medium (gtceu:sterilized_growth_medium_bucket) - 100 mB / s"><img class="gt-ico" src="../../assets/icons/gtceu__sterilized_growth_medium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sterilized Growth Medium</span><b class="gt-q">100 mB / s</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_fluid_heater</code></div>
</div>
<div class="gt-panel t-luv" id="m-r2">
<div class="gt-head"><span class="gt-mname">LuV Chemical Reactor · 15 s · 30 720 EU/t · Sterile Cleanroom</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 osmiridium dust · 500 mB bacteria · 500 mB sterile medium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 osmiridium dust · 500 mB bacteria · 500 mB sterile medium</span><span class="gt-sub"><span>Osmiridium dust</span><span>Bacteria</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Stem cells (32 per run) (gtceu:stem_cells) - 32 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__stem_cells.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stem Cells</span><span class="gt-note">Stem cells (32 per run)</span><b class="gt-q">32</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [HV Chemical Reactor · 40 s · 480 EU/t · Sterile Cleanroom](#m-c1) → [HV Mixer · 80 s · 480 EU/t](#m-m1) → [HV Centrifuge · 120 s · 6 B mixture → 4 gelatin + 1 phosphorus](#m-ce) → [HV Autoclave · 30 s · 1 gelatin + 1 B distilled water](#m-au) → [IV Mixer · 75 s · 7680 EU/t · Sterile Cleanroom](#m-m2) → [IV Fluid Heater · circuit 1 · 1 s per 100 mB · 7680 EU/t](#m-fh) → [LuV Chemical Reactor · 15 s · 30 720 EU/t · Sterile Cleanroom](#m-r2)

### Direct steps

- Agar dust → 4 meat · 4 salt · 3 calcium · 4 agar · 1 strontium dust · 4 B mutagen (4)
- Sterilized growth medium → 1 osmiridium dust · 500 mB bacteria · 500 mB sterile medium (500 mB)

## How to build

1. Drawers first, one per solid: meat dust (Keep Exact 4), bone meal, salt dust, calcium dust, strontium dust (Keep Exact 1), osmiridium dust. Steel drums for sulfuric acid, phosphoric acid, plain water, distilled water, mutagen, raw medium, sterile medium, bacteria. All machines are inside the Sterile Cleanroom. — `functionalstorage:oak_1`, `gtceu:meat_dust`, `gtceu:salt_dust`, `gtceu:calcium_dust`
2. Collagen: one HV chemical reactor, bone meal and meat dust by one router (Item Filter on both), sulfuric acid by Pipez; dump the diluted acid into its own drum. 40 s per dust. — `gtceu:hv_chemical_reactor`, `gtceu:collagen_dust`
3. Gelatin line, one machine each and nothing shared: mixer (4 collagen + 1 B phosphoric + 3 B water, 80 s), centrifuge (6 B → 4 gelatin, 120 s), autoclave (gelatin + 1 B distilled, 30 s). Agar goes into an output drawer, Keep Exact 16. — `gtceu:hv_mixer`, `gtceu:hv_centrifuge`, `gtceu:hv_autoclave`
4. Raw medium: IV mixer, circuit 1. Drawers feed it through one router with five Item Filters; mutagen by Pipez from the bio line 1 drum. 7.5 B of raw medium per 75 s. — `gtceu:iv_mixer`, `gtceu:agar_dust`, `gtceu:strontium_dust`
5. Fluid heater, circuit 1, raw medium in by Pipez, sterile medium out into a drum. Keep 8 B in the drum, the boards and neuro units pull from it. — `gtceu:iv_fluid_heater`, `gtceu:sterilized_growth_medium_bucket`
6. Stem cell reactor: osmiridium drawer + bacteria + sterile medium by fluid pipes; the 500 mB sludge goes back to line 1. Output drawer Keep Exact 64. — `gtceu:luv_chemical_reactor`, `gtceu:stem_cells`

## Tips

- Verified chain (gtsrc GrowthMediumRecipes + pack kjs): collagen = chemical reactor, 1 meat dust + 1 bone meal + 500 mB sulfuric acid → 1 collagen dust + 500 mB diluted sulfuric acid, 800 ticks at VA\[HV\] (the 2 meat + 1 bone + 1 B acid version is 1600 ticks). Gelatin mixture = mixer, 4 collagen + 1 B phosphoric acid + 3 B water → 4 B, 1600 ticks. Centrifuge 6 B mixture → 4 gelatin + 1 phosphorus, 2400 ticks. Agar = autoclave, 1 gelatin + 1 B distilled water, 600 ticks. All four are Sterile Cleanroom recipes at VA\[HV\] = 480 EU/t.
- Raw growth medium: the pack REPLACED the GT recipe (kjs additions/recipe\_changes.js): mixer, circuit 1, 4 meat + 4 salt + 4 calcium + 4 agar + 4 B mutagen → 4 B raw medium, 1200 ticks at VA\[IV\]. circuits.js adds a boosted version: 4 meat + 4 salt + 3 calcium + 4 agar + 1 strontium dust + 4 B mutagen → 7.5 B raw medium, 1500 ticks at VA\[IV\]. Always use the boosted one: 1.875 B of medium per B of mutagen against 1 B. Sterilization: fluid heater, circuit 1, 100 mB raw → 100 mB sterile, 20 ticks at VA\[IV\] (Sterile Cleanroom).
- Stem cells (GrowthMediumRecipes stem\_cells): chemical reactor, 1 osmiridium dust + 500 mB bacteria + 500 mB sterile medium → 32 stem cells + 500 mB bacterial sludge, 300 ticks at VA\[LuV\] = 30 720 EU/t (a LuV reactor), Sterile Cleanroom. The returned sludge is not waste: send it to bio line 1 (uv\_bio1) to enrich. A neuro processing unit eats 16 stem cells, so one run makes the cells for 2 units.
- Budget (see uv\_wetware): every 4 B of sterile medium makes 16 wetware boards; each neuro unit needs 250 mB of medium plus 16 stem cells (a 500 mB medium run gives the cells for 2 units, so 250 mB more per unit). That is about 500 mB of sterile medium per neuro unit, i.e. about 270 mB of mutagen with the boosted mixer (7.5 B of medium per 4 B of mutagen).
- Bacterial machines (verified, bacterial\_multiblocks.js): the Bacterial Runic Mutator \[BRM\] = UV hull + 4 UV motors + melodium gear + 6 ZPM emitters + 4 UV circuits + 576 mB naquadria, VHA\[ZPM\], research ZPM fermenter 32 CWU/t; the Bacterial Breeding Vat \[BBV\] and Bacterial Hydrocarbon Harvester \[BHH\] = UV hull + 4 UV pumps (each UV pump holds a UV motor). Every UV motor needs a dysprosium magnet rod, so Abydos (uv\_akreyrium, uv\_rare\_earth) comes BEFORE these machines; the melodium gear needs the 10 000 K melodium superconductor (tritanium coils). The biostimulating mixture does NOT depend on Abydos: Large Chemical Reactor, VHA\[IV\], 150 mB silicic acid + 250 mB seaweed oil + 325 mB liquefied nutrient paste + 25 mB fermented biomass + 250 mB glycerol -&gt; 1000 mB.
- Sub-steps people skip: (1) agar needs DISTILLED water, not plain water; the gelatin mixer uses plain water; (2) meat dust, salt, calcium and strontium dust each need their own drawer: use Keep Exact 4 / 4 / 3 / 1 and one router with an Item Filter per drawer; (3) circuit 1 on both the mixer and the fluid heater; (4) stem cells return bacterial sludge: do not let the output hatch fill, or the reactor stalls.
- **Unverified** meat dust, salt, calcium and strontium sources; the phosphoric acid line; whether any pack script changes the collagen or agar recipes (nothing found in kubejs).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:hv_mixer` | 1 |
| `gtceu:hv_centrifuge` | 1 |
| `gtceu:hv_autoclave` | 1 |
| `gtceu:iv_mixer` | 1 |
| `gtceu:iv_fluid_heater` | 1 |
| `gtceu:luv_chemical_reactor` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:stem_cells`, `gtceu:sterilized_growth_medium_bucket`, `gtceu:raw_growth_medium_bucket`, `gtceu:agar_dust`, `gtceu:collagen_dust`
