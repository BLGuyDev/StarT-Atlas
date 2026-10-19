---
kind: chain
id: zpm_alloys
order: 1400
data:
  t: |-
    ZPM alloys: naquadah alloy (hull casing) and osthendah (all ZPM parts): mixers → EBF with naquadah coils (7200 K) → Vacuum Freezer with liquid helium
  inf: true
  "n":
    - - g1
      - "2 naquadah dust · 1 osmiridium dust · 1 trinium dust"
      - g
      - functionalstorage:oak_1
      - - [Naquadah dust, "gtceu:naquadah_dust"]
        - [Osmiridium dust, "gtceu:osmiridium_dust"]
        - [Trinium dust, "gtceu:trinium_dust"]
    - [m1, "IV Mixer · circuit 2 · 20 s · 7680 EU/t", m, "gtceu:iv_mixer"]
    - [d1, "4 Naquadah alloy dust", x, "gtceu:naquadah_alloy_dust"]
    - - g2
      - "1 osmium dust · 1 ruthenium dust · 2 naquadah dust"
      - g
      - functionalstorage:oak_1
      - - [Osmium dust, "gtceu:osmium_dust"]
        - [Ruthenium dust, "gtceu:ruthenium_dust"]
        - [Naquadah dust, "gtceu:naquadah_dust"]
    - [m2, "Large Mixer on a 4A hatch · circuit 3 · 18 s · LuV power", m, "gtceu:large_mixer"]
    - [d2, "4 Osthendah dust", x, "gtceu:osthendah_dust"]
    - [e1, "EBF · naquadah coils 7200 K · 50 s · 30 720 EU/t", m, "gtceu:electric_blast_furnace"]
    - [e2, "EBF · naquadah coils 7050 K · 60 s · 30 720 EU/t", m, "gtceu:electric_blast_furnace"]
    - [v1, "Vacuum Freezer · liquid helium · 15 s · 7680 EU/t", m, "gtceu:vacuum_freezer"]
    - [v2, "Vacuum Freezer · liquid helium", m, "gtceu:vacuum_freezer"]
    - [o1, Naquadah alloy ingot, o, "gtceu:naquadah_alloy_ingot"]
    - [o2, Osthendah ingot, o, "gtceu:osthendah_ingot"]
  e:
    - [g1, m1, "4"]
    - [m1, d1, "4 / 20 s"]
    - [d1, e1, "1"]
    - [e1, v1, "hot ingot / 50 s"]
    - [v1, o1, "1"]
    - [g2, m2, "4"]
    - [m2, d2, "4 / 18 s"]
    - [d2, e2, "1"]
    - [e2, v2, "hot ingot / 60 s"]
    - [v2, o2, "1"]
  tips:
    - |-
      Recipes. Naquadah alloy (MixerRecipes naquadah_alloy, SecondDegreeMaterials): 2 naquadah dust + 1 osmiridium dust + 1 trinium dust → 4 dust, circuit 2, 400 ticks at VA[IV] = 7680 EU/t (an IV Mixer). EBF (material blast data): 7200 K, VA[LuV] = 30 720 EU/t, 1000 ticks (50 s); vacuum freezer VA[IV], 300 ticks. Osthendah (pack, kjs additions/progression/misc_additions.js and startup base_materials.js): 1 osmium dust + 1 ruthenium dust + 2 naquadah dust → 4 dust, circuit 3, 360 ticks, EUtVHA(LuV); EBF 7050 K, VA[LuV] = 30 720 EU/t, 1200 ticks (60 s), gas tier ‘higher’. Both stop below a naquadah coil (7200 K) and need the 4A hatch route for the EBF (luv_hatches chain): 30 720 EU/t is above an IV hatch.
    - |-
      Trinium dust is the trinium INGOT macerated (1 ingot → 1 dust, Unverified machine, any macerator), so naquadah alloy waits for the first trinium (zpm_naq_products), which itself waits for naquadah coils (zpm_coils). Osmiridium: luv_hatches chain (Large Mixer, EBF 4500 K). Osmium and ruthenium: the platinum group chain; osthendah uses osmium and ruthenium 1 : 1 per 4 dust, so ruthenium (also the RTM coil metal) is shared with the RTM line: stock 50 or more before you start.
    - |-
      What each is for. Naquadah alloy: 8 plates per ZPM Machine Casing (MachineRecipeLoader casing_zpm), the ZPM hull, and several UV items (naquadah alloy foil in the runic circuit board, dense plates in the stargate reinforced plating, plates in the quantum core), and the quest calls it the core ZPM material. A hull = 8 ingots = 4 naquadah dust + 2 osmiridium + 2 trinium per hull. Osthendah: the primary material of every pack ZPM component (tier_data.js zpm row: primMaterial osthendah): rods, rings, rounds, plates, screws, frames, gears and small gears; plus the ZPM rotor holder ring and gears. A single ZPM motor eats about 6 osthendah ingots (zpm_components).
    - |-
      Both also have an Alloy Blast Smelter route (osthendah is registered with a liquid; naquadah alloy has a fluid): the ABS makes the molten metal directly from the dust. Unverified: the ABS recipe numbers for these two (check EMI); the EBF + freezer route above is the verified one.
    - |-
      Vacuum Freezer: both are above 5000 K, so each freezer run needs liquid helium (500 mB per ingot by the rule used in the luv_hsss chain); times are mass-based (3 ticks per mass unit by MaterialRecipeHandler when no override), vacuum stats for naquadah alloy are 300 ticks at VA[IV]; osthendah’s freezer time is Unverified (check the freezer in EMI).
    - |-
      Sub-steps people skip: (1) circuit 2 for naquadah alloy and 3 for osthendah in the mixers: set the ghost slot; (2) both recipes eat 2 naquadah dust per 4 dust, and the URD line eats 2 more: naquadah dust is the common bottleneck, together with the trinium line; (3) never run both alloys in one EBF: temperatures differ (7200 K vs 7050 K) and the recipes would swap with the circuit; (4) hot ingots go to the freezer first.
    - |-
      Unverified: the osthendah freezer time, the macerating of trinium ingots and how many osthendah rounds, screws and gears a lathe/extruder produces per ingot in this pack (mass based: round 1/9 ingot, screw 1/9, ring 1/4, plate 1, long rod 1, gear 4, small gear 1).
  b:
    - ["gtceu:iv_mixer", 1]
    - ["gtceu:large_mixer", 1]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:naquadah_coil_block", 32]
    - ["gtceu:iv_energy_input_hatch_4a", 2]
    - ["gtceu:vacuum_freezer", 2]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:naquadah_dust", "gtceu:osmiridium_dust", "gtceu:trinium_dust"]
      t: |-
        Drawers first, one per dust: naquadah, osmiridium, trinium, osmium, ruthenium (Keep Exact 16 each). Every mixer gets its own two or three dust inputs behind a Modular Router or Pipez item pipe with Item Filters on the drawers, and a Robot Arm cover in Keep Exact mode on its output so each EBF gets only its own dust.
    - i: ["gtceu:iv_mixer", "gtceu:naquadah_alloy_dust"]
      t: |-
        Naquadah alloy mixer: ghost circuit 2, 2 naquadah + 1 osmiridium + 1 trinium dust → 4 naquadah alloy dust in 20 s at 7680 EU/t (an IV Mixer on its own IV cable).
    - i: ["gtceu:large_mixer", "gtceu:osthendah_dust"]
      t: |-
        Osthendah mixer: ghost circuit 3, 1 osmium + 1 ruthenium + 2 naquadah dust → 4 osthendah dust in 18 s. This is a LuV-power recipe: a Large Mixer on a 4A hatch (luv_hatches) or a LuV Mixer.
    - i: ["gtceu:electric_blast_furnace", "gtceu:naquadah_coil_block", "gtceu:naquadah_alloy_ingot"]
      t: |-
        EBF one: 16 naquadah coil blocks (7200 K), a 4A hatch (30 720 EU/t), ghost circuit 1, input bus with the naquadah alloy dust: hot ingot in 50 s. Muffler hatch free above the controller.
    - i: ["gtceu:electric_blast_furnace", "gtceu:osthendah_ingot"]
      t: |-
        EBF two, separate machine with its own coils and hatch: osthendah dust → hot ingot in 60 s at 30 720 EU/t. Run it more than the first: osthendah is the bulk metal of the era.
    - i: ["gtceu:vacuum_freezer", "gtceu:liquid_helium_bucket", "gtceu:osthendah_ingot"]
      t: |-
        Freezers: a Robot Arm with an Item Filter pulls each hot ingot into its own Vacuum Freezer with a liquid helium line (500 mB per ingot); outputs into drawers Keep Exact 32. Then the part machines: LV benders and lathes, extruders and the wiremill for the component chains.
    - i: ["functionalstorage:oak_1", "gtceu:naquadah_alloy_ingot"]
      t: |-
        Easy to miss: build 2 hulls worth (16 plates) of naquadah alloy before you spend osthendah, and keep 2 naquadah ingots per hull ready: both alloys and the URD line eat naquadah dust at the same time.
---
# ZPM alloys: naquadah alloy (hull casing) and osthendah (all ZPM parts): mixers → EBF with naquadah coils (7200 K) → Vacuum Freezer with liquid helium

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Naquadah metals and ZPM coils](../../plan/p12.md#zpmmetals)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-m1">
<div class="gt-head"><span class="gt-mname">IV Mixer · circuit 2 · 20 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 naquadah dust · 1 osmiridium dust · 1 trinium dust (functionalstorage:oak_1) - 4"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 naquadah dust · 1 osmiridium dust · 1 trinium dust</span><span class="gt-sub"><span>Naquadah dust</span><span>Osmiridium dust</span><span>Trinium dust</span></span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Naquadah alloy dust (gtceu:naquadah_alloy_dust) - 4 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Dust</span><span class="gt-note">4 Naquadah alloy dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">Large Mixer on a 4A hatch · circuit 3 · 18 s · LuV power</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 osmium dust · 1 ruthenium dust · 2 naquadah dust (functionalstorage:oak_1) - 4"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 osmium dust · 1 ruthenium dust · 2 naquadah dust</span><span class="gt-sub"><span>Osmium dust</span><span>Ruthenium dust</span><span>Naquadah dust</span></span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">18 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Osthendah dust (gtceu:osthendah_dust) - 4 / 18 s"><img class="gt-ico" src="../../assets/icons/gtceu__osthendah_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osthendah Dust</span><span class="gt-note">4 Osthendah dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF · naquadah coils 7200 K · 50 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Naquadah alloy dust (gtceu:naquadah_alloy_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Dust</span><span class="gt-note">4 Naquadah alloy dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-v1" title="Vacuum Freezer · liquid helium · 15 s · 7680 EU/t (gtceu:vacuum_freezer) - hot ingot / 50 s"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer · liquid helium · 15 s · 7680 EU/t</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF · naquadah coils 7050 K · 60 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Osthendah dust (gtceu:osthendah_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__osthendah_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osthendah Dust</span><span class="gt-note">4 Osthendah dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-v2" title="Vacuum Freezer · liquid helium (gtceu:vacuum_freezer) - hot ingot / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer · liquid helium</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-v1">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · liquid helium · 15 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-e1" title="EBF · naquadah coils 7200 K · 50 s · 30 720 EU/t (gtceu:electric_blast_furnace) - hot ingot / 50 s"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · naquadah coils 7200 K · 50 s · 30 720 EU/t</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">50 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Naquadah alloy ingot (gtceu:naquadah_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-v2">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · liquid helium</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-e2" title="EBF · naquadah coils 7050 K · 60 s · 30 720 EU/t (gtceu:electric_blast_furnace) - hot ingot / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · naquadah coils 7050 K · 60 s · 30 720 EU/t</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Osthendah ingot (gtceu:osthendah_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__osthendah_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osthendah Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [IV Mixer · circuit 2 · 20 s · 7680 EU/t](#m-m1) → [EBF · naquadah coils 7200 K · 50 s · 30 720 EU/t](#m-e1) → [Vacuum Freezer · liquid helium · 15 s · 7680 EU/t](#m-v1)
- [Large Mixer on a 4A hatch · circuit 3 · 18 s · LuV power](#m-m2) → [EBF · naquadah coils 7050 K · 60 s · 30 720 EU/t](#m-e2) → [Vacuum Freezer · liquid helium](#m-v2)

## How to build

1. Drawers first, one per dust: naquadah, osmiridium, trinium, osmium, ruthenium (Keep Exact 16 each). Every mixer gets its own two or three dust inputs behind a Modular Router or Pipez item pipe with Item Filters on the drawers, and a Robot Arm cover in Keep Exact mode on its output so each EBF gets only its own dust. — `functionalstorage:oak_1`, `gtceu:naquadah_dust`, `gtceu:osmiridium_dust`, `gtceu:trinium_dust`
2. Naquadah alloy mixer: ghost circuit 2, 2 naquadah + 1 osmiridium + 1 trinium dust → 4 naquadah alloy dust in 20 s at 7680 EU/t (an IV Mixer on its own IV cable). — `gtceu:iv_mixer`, `gtceu:naquadah_alloy_dust`
3. Osthendah mixer: ghost circuit 3, 1 osmium + 1 ruthenium + 2 naquadah dust → 4 osthendah dust in 18 s. This is a LuV-power recipe: a Large Mixer on a 4A hatch (luv\_hatches) or a LuV Mixer. — `gtceu:large_mixer`, `gtceu:osthendah_dust`
4. EBF one: 16 naquadah coil blocks (7200 K), a 4A hatch (30 720 EU/t), ghost circuit 1, input bus with the naquadah alloy dust: hot ingot in 50 s. Muffler hatch free above the controller. — `gtceu:electric_blast_furnace`, `gtceu:naquadah_coil_block`, `gtceu:naquadah_alloy_ingot`
5. EBF two, separate machine with its own coils and hatch: osthendah dust → hot ingot in 60 s at 30 720 EU/t. Run it more than the first: osthendah is the bulk metal of the era. — `gtceu:electric_blast_furnace`, `gtceu:osthendah_ingot`
6. Freezers: a Robot Arm with an Item Filter pulls each hot ingot into its own Vacuum Freezer with a liquid helium line (500 mB per ingot); outputs into drawers Keep Exact 32. Then the part machines: LV benders and lathes, extruders and the wiremill for the component chains. — `gtceu:vacuum_freezer`, `gtceu:liquid_helium_bucket`, `gtceu:osthendah_ingot`
7. Easy to miss: build 2 hulls worth (16 plates) of naquadah alloy before you spend osthendah, and keep 2 naquadah ingots per hull ready: both alloys and the URD line eat naquadah dust at the same time. — `functionalstorage:oak_1`, `gtceu:naquadah_alloy_ingot`

## Tips

- Recipes. Naquadah alloy (MixerRecipes naquadah\_alloy, SecondDegreeMaterials): 2 naquadah dust + 1 osmiridium dust + 1 trinium dust → 4 dust, circuit 2, 400 ticks at VA\[IV\] = 7680 EU/t (an IV Mixer). EBF (material blast data): 7200 K, VA\[LuV\] = 30 720 EU/t, 1000 ticks (50 s); vacuum freezer VA\[IV\], 300 ticks. Osthendah (pack, kjs additions/progression/misc\_additions.js and startup base\_materials.js): 1 osmium dust + 1 ruthenium dust + 2 naquadah dust → 4 dust, circuit 3, 360 ticks, EUtVHA(LuV); EBF 7050 K, VA\[LuV\] = 30 720 EU/t, 1200 ticks (60 s), gas tier ‘higher’. Both stop below a naquadah coil (7200 K) and need the 4A hatch route for the EBF (luv\_hatches chain): 30 720 EU/t is above an IV hatch.
- Trinium dust is the trinium INGOT macerated (1 ingot → 1 dust, Unverified machine, any macerator), so naquadah alloy waits for the first trinium (zpm\_naq\_products), which itself waits for naquadah coils (zpm\_coils). Osmiridium: luv\_hatches chain (Large Mixer, EBF 4500 K). Osmium and ruthenium: the platinum group chain; osthendah uses osmium and ruthenium 1 : 1 per 4 dust, so ruthenium (also the RTM coil metal) is shared with the RTM line: stock 50 or more before you start.
- What each is for. Naquadah alloy: 8 plates per ZPM Machine Casing (MachineRecipeLoader casing\_zpm), the ZPM hull, and several UV items (naquadah alloy foil in the runic circuit board, dense plates in the stargate reinforced plating, plates in the quantum core), and the quest calls it the core ZPM material. A hull = 8 ingots = 4 naquadah dust + 2 osmiridium + 2 trinium per hull. Osthendah: the primary material of every pack ZPM component (tier\_data.js zpm row: primMaterial osthendah): rods, rings, rounds, plates, screws, frames, gears and small gears; plus the ZPM rotor holder ring and gears. A single ZPM motor eats about 6 osthendah ingots (zpm\_components).
- Both also have an Alloy Blast Smelter route (osthendah is registered with a liquid; naquadah alloy has a fluid): the ABS makes the molten metal directly from the dust. Unverified: the ABS recipe numbers for these two (check EMI); the EBF + freezer route above is the verified one.
- Vacuum Freezer: both are above 5000 K, so each freezer run needs liquid helium (500 mB per ingot by the rule used in the luv\_hsss chain); times are mass-based (3 ticks per mass unit by MaterialRecipeHandler when no override), vacuum stats for naquadah alloy are 300 ticks at VA\[IV\]; osthendah’s freezer time is Unverified (check the freezer in EMI).
- Sub-steps people skip: (1) circuit 2 for naquadah alloy and 3 for osthendah in the mixers: set the ghost slot; (2) both recipes eat 2 naquadah dust per 4 dust, and the URD line eats 2 more: naquadah dust is the common bottleneck, together with the trinium line; (3) never run both alloys in one EBF: temperatures differ (7200 K vs 7050 K) and the recipes would swap with the circuit; (4) hot ingots go to the freezer first.
- **Unverified** the osthendah freezer time, the macerating of trinium ingots and how many osthendah rounds, screws and gears a lathe/extruder produces per ingot in this pack (mass based: round 1/9 ingot, screw 1/9, ring 1/4, plate 1, long rod 1, gear 4, small gear 1).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_mixer` | 1 |
| `gtceu:large_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:naquadah_coil_block` | 32 |
| `gtceu:iv_energy_input_hatch_4a` | 2 |
| `gtceu:vacuum_freezer` | 2 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Feeds:** [ZPM Machine Hull: naquadah alloy casing + 2 vanadium gallium cables (PPS foil + PVC foil + silicone rubber) + 288 mB PBI](zpm_hull.md)
- **Main source for:** `gtceu:naquadah_alloy_ingot`, `gtceu:naquadah_alloy_dust`, `gtceu:naquadah_alloy_plate`, `gtceu:osthendah_ingot`, `gtceu:osthendah_dust`, `gtceu:osthendah_plate`
