---
kind: chain
id: chromium_line
order: 1080
data:
  t: |-
    Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod
  inf: true
  "n":
    - [df, "Drilling fluid · 5 B", f, "gtceu:drilling_fluid_bucket"]
    - [ve, "Void Extractor · 32 s · 30 EU/t", s, "gtceu:void_extractor"]
    - [rr, "Rare ore residue · 400 mB", f, "gtceu:rare_ore_residue_bucket"]
    - [e1, "LV Electrolyzer · 6 s · 30 EU/t", m, "gtceu:lv_electrolyzer"]
    - [cs, Chromite sludge dust, x, "gtceu:chromite_sludge_dust"]
    - [ce, "MV Centrifuge · 2.5 s", m, "gtceu:mv_centrifuge"]
    - [rm, Rare metallic residue dust, x, "gtceu:rare_metallic_residue_dust"]
    - [cd, "2 Chromite dust", x, "gtceu:chromite_dust"]
    - [e2, "MV Electrolyzer · 7 dust · about 10 s · 60 EU/t", m, "gtceu:mv_electrolyzer"]
    - [cu, "2 Chromium dust", o, "gtceu:chromium_dust"]
    - [fe, "1 Iron dust", x, "gtceu:iron_dust"]
    - [ox, "4 B oxygen", f, "gtceu:oxygen_bucket"]
    - [eb, "EBF · 1700 K · 88 s · 120 EU/t", m, "gtceu:electric_blast_furnace"]
    - [ci, Chromium ingot, x, "gtceu:chromium_ingot"]
    - [la, LV Lathe, m, "gtceu:lv_lathe"]
    - [rd, "2 Chromium rod", o, "gtceu:chromium_rod"]
  e:
    - [df, ve, "5 B"]
    - [ve, rr, "400 mB / 32 s"]
    - [rr, e1, "1 B"]
    - [e1, cs, "1"]
    - [cs, ce, "1"]
    - [ce, cd, "2"]
    - [ce, rm, "1"]
    - [cd, e2, "7"]
    - [e2, cu, "2"]
    - [e2, fe, "1"]
    - [e2, ox, "4 B"]
    - [cu, eb, "1"]
    - [eb, ci, "1 / 88 s"]
    - [ci, la, "1"]
    - [la, rd, "1 → 2"]
  tips:
    - |-
      Where chromium really comes from in this pack: chromite dust. Chromite is iron 1 + chromium 2 + oxygen 4, and the game decomposes any such compound in an Electrolyzer. The fork code gives 7 chromite dust → 1 iron dust + 2 chromium dust + 4 B oxygen, 60 EU/t (2 x LV because it has three components), so an MV Electrolyzer, not LV. The time works out at about 10 s (protons 15 x 7 dust x 2 = 210 ticks).
    - |-
      The pack scripts give chromite no early ore vein (only the Abydos naquadite vein) and the sieve entries for it are commented out in sieving.js. The route that is live: Void Extractor recipe (5 B drilling fluid, 640 ticks, 30 EU/t) outputs 400 mB rare ore residue + 600 mB raw ore slurry; an LV Electrolyzer turns 1 B residue into 1 each of chromite, rare, vanadium magnetite and cobaltite sludge dust + 250 mB slurry (6 s, 30 EU/t); an MV Centrifuge turns 1 chromite sludge dust into 2 chromite dust + 1 rare metallic residue (50 ticks). Source: void_drill_line/clusters.js and rare_ore_residue.js.
    - |-
      The count is brutal: 1 chromium dust = 3.5 chromite dust = 1.75 chromite sludge = 1.75 B residue = about 4.4 extractor runs. One Void Extractor makes about 26 chromium dust an hour. Kanthal (16 coils) wants 128, stainless 1 per 9 dust, nichrome 1 per 5 dust, plus chromium rods for HV emitters and sensors. Build two or three extractors early and let the drums fill.
    - |-
      Other chromite sources that exist but are late: the Abydos naquadite vein (chromite layer) and the Molten Destabilizing recipes (2 raw chromite per 300 B dense magma, 5 per 60 B residue, magma.js). The Electric Ore Factory lists crushed chromite as an EV ore (iron and magnesium byproducts), which only helps if you already hold crushed chromite.
    - |-
      Second chromium route, HV: crushed ruby ore + aqua regia in an EV Mixer (2 ore + 3 B aqua regia → 3 B ruby slurry, 280 ticks, 1920 EU/t) then an HV Centrifuge (3 B slurry → 2 aluminium dust + 1 chromium dust + 2 % each of titanium, iron and vanadium + 2 B diluted hydrochloric acid, 320 ticks, 480 EU/t). Aqua regia is a 30-tick LV mixer recipe. That is 1 chromium per 2 crushed ruby.
    - |-
      Chromium ingot (for rods): EBF, 1 chromium dust → 1 ingot, 1700 K, 120 EU/t, 88 s with circuit 1 (mass 52 x 1700 K / 50 = 1768 ticks); with circuit 2 and 1 B nitrogen per ingot it is x0.67 (about 59 s). No hot ingot at 1700 K, so cupronickel coils are fine and no freezer. Rod: lathe 1 ingot → 2 rods (config harderRods is false).
    - |-
      Sub-steps people skip: the residue electrolyzer outputs four sludge dusts at once and its output bus clogs unless each goes to its own drawer: filter chromite sludge to this chain, send the other three (rare, vanadium magnetite, cobaltite) to their own centrifuges or leave them in a filtered drawer. The rare metallic residue from every sludge goes to the calcite and silver electrolysis, never back into the chain.
    - |-
      The electrolyzer only starts at 7 chromite dust: use an input drawer with a Robot Arm cover (Keep Exact) set so that only whole batches of 7 enter, or just let the bus fill. Oxygen (4 B per run) goes to the oxygen drum for the air line; the iron dust joins the Kanthal and stainless iron drawer.
    - |-
      Unverified: the electrolyzer timing and output counts for chromite are derived from the decomposition code, not read from EMI; open chromite dust in EMI to confirm 7 → 1 + 2 + 4 B. Unverified: where the pack lets you obtain crushed ruby ore in quantity (the ruby sieve entry is commented out, geodes give a Ruby Geode item).
  b:
    - ["gtceu:void_extractor", 2]
    - ["gtceu:lv_electrolyzer", 1]
    - ["gtceu:mv_centrifuge", 1]
    - ["gtceu:mv_electrolyzer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:lv_lathe", 1]
    - ["functionalstorage:oak_1", 9]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 5]
  how:
    - i: ["gtceu:void_extractor", "gtceu:drilling_fluid_bucket", "gtceu:rare_ore_residue_bucket"]
      t: |-
        Void Extractor (steel casings, frames, gearbox; one fluid input, two fluid outputs, two item outputs). Drilling fluid drum on the input hatch, 5 B per 32 s run at 30 EU/t. Output 1 is rare ore residue 400 mB, output 2 raw ore slurry 600 mB: give each its own drum with a pump cover so a full slurry drum does not stop the extractor. The item outputs are chance raws (gold, silver, pentlandite, realgar): filter them into drawers.
    - i: ["gtceu:lv_electrolyzer", "gtceu:chromite_sludge_dust"]
      t: |-
        LV Electrolyzer on its own: 1 B rare ore residue → 1 chromite sludge + 1 rare sludge + 1 vanadium magnetite sludge + 1 cobaltite sludge dust + 250 mB raw ore slurry, 6 s at 30 EU/t. The four dusts leave through one output bus: put an Item Filter Robot Arm on that bus so only chromite sludge dust goes to this chain and the rest go to their own drawers.
    - i: ["gtceu:mv_centrifuge", "gtceu:chromite_dust"]
      t: |-
        MV Centrifuge on the chromite sludge drawer: 1 sludge dust → 2 chromite dust + 1 rare metallic residue dust in 2.5 s. Never put another sludge into it; the cobaltite, rare and vanadium sludges have their own recipes in the same machine type, so keep one centrifuge per product.
    - i: ["gtceu:mv_electrolyzer", "gtceu:chromium_dust", "gtceu:iron_dust"]
      t: |-
        MV Electrolyzer (HV is fine too): input drawer of chromite dust, output bus split with a filter: chromium dust to the chromium drawer (shared by Kanthal, stainless and nichrome), iron dust to the iron drawer. 7 chromite dust → 1 iron dust + 2 chromium dust + 4 B oxygen per run, 60 EU/t. Oxygen goes to a drum or the oxygen chain.
    - i: ["gtceu:electric_blast_furnace", "gtceu:chromium_ingot"]
      t: |-
        Only if you need rods: EBF with ghost circuit 1, 1 chromium dust → chromium ingot in 88 s at 120 EU/t. 1700 K, so the cupronickel furnace of the stainless chain works, but give it its own bus; do not time-share with stainless. Circuit 2 plus 1 B nitrogen cuts it to about 59 s.
    - i: ["gtceu:lv_lathe", "gtceu:chromium_rod"]
      t: |-
        LV Lathe: 1 chromium ingot → 2 chromium rods. Robot Arm Keep Exact on the rod drawer at 32 stops the line. Rods feed the HV emitter (4 per craft) and sensor (1 per craft).
    - i: ["functionalstorage:oak_1", "gtceu:chromium_dust"]
      t: |-
        The dust drawer is shared. Put a Modular Router (or Pipez item pipe with an Item Filter on chromium dust) on the drawer for each consumer: the Kanthal mixer, the stainless mixer, the nichrome mixer. Size it for the 128 dust a Kanthal coil set eats; if it empties, the mixers simply wait.
---
# Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `chromium_line` · **Tags:** Infinite source, Unverified

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Chromium (Void Extractor residue)](../../plan/p7.md#chromium)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-e1">
<div class="gt-head"><span class="gt-mname">LV Electrolyzer · 6 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Rare ore residue · 400 mB (gtceu:rare_ore_residue_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__rare_ore_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Ore Residue</span><span class="gt-note">Rare ore residue · 400 mB</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Chromite sludge dust (gtceu:chromite_sludge_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Sludge Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electrolyzer</code></div>
</div>
<div class="gt-panel t-mv" id="m-ce">
<div class="gt-head"><span class="gt-mname">MV Centrifuge · 2.5 s</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chromite sludge dust (gtceu:chromite_sludge_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Sludge Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Chromite dust (gtceu:chromite_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Dust</span><span class="gt-note">2 Chromite dust</span><b class="gt-q">2</b></span><span class="gt-slot" title="Rare metallic residue dust (gtceu:rare_metallic_residue_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rare_metallic_residue_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Metallic Residue Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_centrifuge</code></div>
</div>
<div class="gt-panel t-mv" id="m-e2">
<div class="gt-head"><span class="gt-mname">MV Electrolyzer · 7 dust · about 10 s · 60 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Chromite dust (gtceu:chromite_dust) - 7"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Dust</span><span class="gt-note">2 Chromite dust</span><b class="gt-q">7</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 Chromium dust (gtceu:chromium_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Dust</span><span class="gt-note">2 Chromium dust</span><b class="gt-q">2</b></span><span class="gt-slot" title="1 Iron dust (gtceu:iron_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><span class="gt-note">1 Iron dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="4 B oxygen (gtceu:oxygen_bucket) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><span class="gt-note">4 B oxygen</span><b class="gt-q">4 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_electrolyzer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · 1700 K · 88 s · 120 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="2 Chromium dust (gtceu:chromium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Dust</span><span class="gt-note">2 Chromium dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">88 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Chromium ingot (gtceu:chromium_ingot) - 1 / 88 s"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-lv" id="m-la">
<div class="gt-head"><span class="gt-mname">LV Lathe</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chromium ingot (gtceu:chromium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_lathe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 Chromium rod (gtceu:chromium_rod) - 1 → 2"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Rod</span><span class="gt-note">2 Chromium rod</span><b class="gt-q">1 → 2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_lathe</code></div>
</div>
</div>

## Flow

- [LV Electrolyzer · 6 s · 30 EU/t](#m-e1) → [MV Centrifuge · 2.5 s](#m-ce) → [MV Electrolyzer · 7 dust · about 10 s · 60 EU/t](#m-e2) → [EBF · 1700 K · 88 s · 120 EU/t](#m-eb) → [LV Lathe](#m-la)

### Direct steps

- Drilling fluid · 5 B → Void Extractor · 32 s · 30 EU/t (5 B)
- Void Extractor · 32 s · 30 EU/t → Rare ore residue · 400 mB (400 mB / 32 s)

## How to build

1. Void Extractor (steel casings, frames, gearbox; one fluid input, two fluid outputs, two item outputs). Drilling fluid drum on the input hatch, 5 B per 32 s run at 30 EU/t. Output 1 is rare ore residue 400 mB, output 2 raw ore slurry 600 mB: give each its own drum with a pump cover so a full slurry drum does not stop the extractor. The item outputs are chance raws (gold, silver, pentlandite, realgar): filter them into drawers. — `gtceu:void_extractor`, `gtceu:drilling_fluid_bucket`, `gtceu:rare_ore_residue_bucket`
2. LV Electrolyzer on its own: 1 B rare ore residue → 1 chromite sludge + 1 rare sludge + 1 vanadium magnetite sludge + 1 cobaltite sludge dust + 250 mB raw ore slurry, 6 s at 30 EU/t. The four dusts leave through one output bus: put an Item Filter Robot Arm on that bus so only chromite sludge dust goes to this chain and the rest go to their own drawers. — `gtceu:lv_electrolyzer`, `gtceu:chromite_sludge_dust`
3. MV Centrifuge on the chromite sludge drawer: 1 sludge dust → 2 chromite dust + 1 rare metallic residue dust in 2.5 s. Never put another sludge into it; the cobaltite, rare and vanadium sludges have their own recipes in the same machine type, so keep one centrifuge per product. — `gtceu:mv_centrifuge`, `gtceu:chromite_dust`
4. MV Electrolyzer (HV is fine too): input drawer of chromite dust, output bus split with a filter: chromium dust to the chromium drawer (shared by Kanthal, stainless and nichrome), iron dust to the iron drawer. 7 chromite dust → 1 iron dust + 2 chromium dust + 4 B oxygen per run, 60 EU/t. Oxygen goes to a drum or the oxygen chain. — `gtceu:mv_electrolyzer`, `gtceu:chromium_dust`, `gtceu:iron_dust`
5. Only if you need rods: EBF with ghost circuit 1, 1 chromium dust → chromium ingot in 88 s at 120 EU/t. 1700 K, so the cupronickel furnace of the stainless chain works, but give it its own bus; do not time-share with stainless. Circuit 2 plus 1 B nitrogen cuts it to about 59 s. — `gtceu:electric_blast_furnace`, `gtceu:chromium_ingot`
6. LV Lathe: 1 chromium ingot → 2 chromium rods. Robot Arm Keep Exact on the rod drawer at 32 stops the line. Rods feed the HV emitter (4 per craft) and sensor (1 per craft). — `gtceu:lv_lathe`, `gtceu:chromium_rod`
7. The dust drawer is shared. Put a Modular Router (or Pipez item pipe with an Item Filter on chromium dust) on the drawer for each consumer: the Kanthal mixer, the stainless mixer, the nichrome mixer. Size it for the 128 dust a Kanthal coil set eats; if it empties, the mixers simply wait. — `functionalstorage:oak_1`, `gtceu:chromium_dust`

## Tips

- Where chromium really comes from in this pack: chromite dust. Chromite is iron 1 + chromium 2 + oxygen 4, and the game decomposes any such compound in an Electrolyzer. The fork code gives 7 chromite dust → 1 iron dust + 2 chromium dust + 4 B oxygen, 60 EU/t (2 x LV because it has three components), so an MV Electrolyzer, not LV. The time works out at about 10 s (protons 15 x 7 dust x 2 = 210 ticks).
- The pack scripts give chromite no early ore vein (only the Abydos naquadite vein) and the sieve entries for it are commented out in sieving.js. The route that is live: Void Extractor recipe (5 B drilling fluid, 640 ticks, 30 EU/t) outputs 400 mB rare ore residue + 600 mB raw ore slurry; an LV Electrolyzer turns 1 B residue into 1 each of chromite, rare, vanadium magnetite and cobaltite sludge dust + 250 mB slurry (6 s, 30 EU/t); an MV Centrifuge turns 1 chromite sludge dust into 2 chromite dust + 1 rare metallic residue (50 ticks). Source: void\_drill\_line/clusters.js and rare\_ore\_residue.js.
- The count is brutal: 1 chromium dust = 3.5 chromite dust = 1.75 chromite sludge = 1.75 B residue = about 4.4 extractor runs. One Void Extractor makes about 26 chromium dust an hour. Kanthal (16 coils) wants 128, stainless 1 per 9 dust, nichrome 1 per 5 dust, plus chromium rods for HV emitters and sensors. Build two or three extractors early and let the drums fill.
- Other chromite sources that exist but are late: the Abydos naquadite vein (chromite layer) and the Molten Destabilizing recipes (2 raw chromite per 300 B dense magma, 5 per 60 B residue, magma.js). The Electric Ore Factory lists crushed chromite as an EV ore (iron and magnesium byproducts), which only helps if you already hold crushed chromite.
- Second chromium route, HV: crushed ruby ore + aqua regia in an EV Mixer (2 ore + 3 B aqua regia → 3 B ruby slurry, 280 ticks, 1920 EU/t) then an HV Centrifuge (3 B slurry → 2 aluminium dust + 1 chromium dust + 2 % each of titanium, iron and vanadium + 2 B diluted hydrochloric acid, 320 ticks, 480 EU/t). Aqua regia is a 30-tick LV mixer recipe. That is 1 chromium per 2 crushed ruby.
- Chromium ingot (for rods): EBF, 1 chromium dust → 1 ingot, 1700 K, 120 EU/t, 88 s with circuit 1 (mass 52 x 1700 K / 50 = 1768 ticks); with circuit 2 and 1 B nitrogen per ingot it is x0.67 (about 59 s). No hot ingot at 1700 K, so cupronickel coils are fine and no freezer. Rod: lathe 1 ingot → 2 rods (config harderRods is false).
- Sub-steps people skip: the residue electrolyzer outputs four sludge dusts at once and its output bus clogs unless each goes to its own drawer: filter chromite sludge to this chain, send the other three (rare, vanadium magnetite, cobaltite) to their own centrifuges or leave them in a filtered drawer. The rare metallic residue from every sludge goes to the calcite and silver electrolysis, never back into the chain.
- The electrolyzer only starts at 7 chromite dust: use an input drawer with a Robot Arm cover (Keep Exact) set so that only whole batches of 7 enter, or just let the bus fill. Oxygen (4 B per run) goes to the oxygen drum for the air line; the iron dust joins the Kanthal and stainless iron drawer.
- **Unverified** the electrolyzer timing and output counts for chromite are derived from the decomposition code, not read from EMI; open chromite dust in EMI to confirm 7 → 1 + 2 + 4 B. Unverified: where the pack lets you obtain crushed ruby ore in quantity (the ruby sieve entry is commented out, geodes give a Ruby Geode item).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:void_extractor` | 2 |
| `gtceu:lv_electrolyzer` | 1 |
| `gtceu:mv_centrifuge` | 1 |
| `gtceu:mv_electrolyzer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:lv_lathe` | 1 |
| `functionalstorage:oak_1` | 9 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Feeds:** [Stainless steel: MV Mixer + HV Electric Blast Furnace](stainless.md), [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](kanthal.md), [HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers](hv_components2.md), [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../ev/nichrome_line.md)
- **Main source for:** `gtceu:chromium_dust`, `gtceu:chromite_dust`, `gtceu:chromium_ingot`, `gtceu:chromium_rod`
