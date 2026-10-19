---
kind: chain
id: zpm_urd
order: 1420
data:
  t: Uranium rhodium dinaquadide (URD, 9000 K) and dragonsteel (ZPM superconductor, 7100 K)
  inf: true
  "n":
    - - g1
      - "1 uranium dust · 1 rhodium dust · 2 naquadah dust"
      - g
      - functionalstorage:oak_1
      - - [Uranium dust, "gtceu:uranium_dust"]
        - [Rhodium dust, "gtceu:rhodium_dust"]
        - [Naquadah dust, "gtceu:naquadah_dust"]
    - [m1, "Large Mixer on a LuV 4A hatch · circuit 4 · 7.5 s · 122 880 EU/t", m, "gtceu:large_mixer"]
    - [d1, "4 URD dust", x, "gtceu:uranium_rhodium_dinaquadide_dust"]
    - [e1, "EBF · trinium coils 9001 K · 75 s · 7680 EU/t", m, "gtceu:electric_blast_furnace"]
    - - f1
      - ZPM Vacuum Freezer or Mega Vacuum Freezer · liquid helium · 10 s · 122 880 EU/t
      - m
      - gtceu:vacuum_freezer
    - [o1, "URD ingot (wire, double wire, fine wire)", o, "gtceu:uranium_rhodium_dinaquadide_ingot"]
    - - g2
      - "4 tungsten dust · 8 magnesium diboride dust · 2 cadmium dust"
      - g
      - functionalstorage:oak_1
      - - [Tungsten dust, "gtceu:tungsten_dust"]
        - [Magnesium diboride dust, "gtceu:magnesium_diboride_dust"]
        - [Cadmium dust, "gtceu:cadmium_dust"]
    - [m2, "Large Mixer on a 4A hatch · 45 s · 16 000 EU/t", m, "gtceu:large_mixer"]
    - [d2, "14 Dragonsteel dust", x, "gtceu:dragonsteel_dust"]
    - [e2, "EBF · naquadah coils 7200 K · 90 s · 122 880 EU/t", m, "gtceu:electric_blast_furnace"]
    - [o2, "Dragonsteel ingot (ZPM superconductor)", o, "gtceu:dragonsteel_ingot"]
  e:
    - [g1, m1, "4"]
    - [m1, d1, "4 / 7.5 s"]
    - [d1, e1, "1"]
    - [e1, f1, "hot ingot / 75 s"]
    - [f1, o1, "1"]
    - [g2, m2, "14"]
    - [m2, d2, "14 / 45 s"]
    - [d2, e2, "1"]
    - [e2, o2, "1 / 90 s"]
  tips:
    - |-
      URD (MixerRecipes uranium_rhodium_dinaquadide, FirstDegreeMaterials): 1 uranium dust (the pack’s uranium is the 238 isotope, id gtceu:uranium) + 1 rhodium dust + 2 naquadah dust → 4 dust, circuit 4, 150 ticks at VA[ZPM] = 122 880 EU/t. That is a ZPM-power mixer recipe: a ZPM Mixer, or the Large Mixer on a LuV 4A hatch. EBF: 9000 K (trinium coils, zpm_coils), 1500 ticks (75 s) but only VA[IV] = 7680 EU/t; the hot ingot then needs a freezer with vacuumStats VA[ZPM], 200 ticks: a freezer at ZPM voltage (122 880 EU/t), or the Mega Vacuum Freezer (GCYM multi in the era list) on the 4A hatch. Quest: URD is ‘used for ZPM Field Generators and the second tier of Fusion Reactors’.
    - |-
      What eats URD (verified recipes): ZPM field generator 128 fine URD wire (16 ingots) each, Research Station 32 double wire (32 ingots), HPCA 64 double wire, Object Holder 16 double wire, the ZPM superconducting coil 16 double wire, ZPM Fusion Reactor 32 single wire (16 ingots). A first Research Station + HPCA + holder is about 112 URD ingots, i.e. 112 uranium, 112 rhodium and 224 naquadah dust: rhodium (platline, 7 per cooperite batch) is the scarce one.
    - |-
      Dragonsteel (kjs additions/progression/superconductors.js + startup superconductors.js): 4 tungsten + 8 magnesium diboride + 2 cadmium dust → 14 dust, mixer 900 ticks at 16 000 EU/t (above an IV mixer: Large Mixer on a 4A hatch); EBF 7100 K, VA[ZPM] = 122 880 EU/t, 1800 ticks (90 s), gas tier high. It is the ZPM superconductor: a dragonsteel single wire carries 96 amps (quest), no loss. Only needed for ZPM power cables; skip it until your ZPM energy hatch exists. Magnesium diboride = 1 magnesium + 2 boron dust → 3 dust, circuit 4, 600 ticks at VA[MV] (MixerRecipes). Cadmium: Unverified source.
    - |-
      Why EBF power is low for URD but the mixer is high: the 9000 K recipe itself is 7680 EU/t, so ONE furnace with an IV hatch can make URD from dust. Only the mixer (122 880 EU/t) and the freezer (122 880 EU/t) are ZPM power: batch the 4 dust per 7.5 s into a drawer, then the slow furnace. Since the Research Station recipe, field generators and the fusion reactor all need URD, this is the single most-needed ZPM alloy after osthendah.
    - |-
      Sub-steps people skip: (1) circuit 4 in the mixer, 3 for osthendah, 2 for naquadah alloy: three machines, three ghost circuits; (2) trinium coils are required for 9000 K, so the order is: naquadah coils → trinium → trinium coils → URD; (3) the freezer step is the real power gate: if your only ZPM-capable machine is the Large Assembler, build the Mega Vacuum Freezer or a ZPM freezer before the first URD ingot; (4) keep naquadah dust Keep Exact in three drawers: three alloys fight for it.
    - |-
      Unverified: the uranium dust source (check EMI: the Chemical Plant skip uranite_line_skip gives 9 uranium + 1 uranium-235 from 30 uraninite + 40 B hydrofluoric acid at LuV power but needs the UV multiblock), the cadmium source, and the Mega Vacuum Freezer recipe tiers.
  b:
    - ["gtceu:large_mixer", 2]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:trinium_coil_block", 16]
    - ["gtceu:naquadah_coil_block", 16]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 2]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uranium_dust", "gtceu:rhodium_dust", "gtceu:naquadah_dust"]
      t: |-
        Drawers first, one per dust: uranium, rhodium, naquadah, tungsten, magnesium diboride, cadmium. Keep Exact 16 on each so a stuck mixer never swallows the rhodium. Every mixer sits behind its own router with Item Filters, with a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:large_mixer", "gtceu:uranium_rhodium_dinaquadide_dust"]
      t: |-
        URD mixer: Large Mixer on a LuV 4A hatch (122 880 EU/t), ghost circuit 4, 1 uranium + 1 rhodium + 2 naquadah dust → 4 URD dust in 7.5 s. Output dust goes by Robot Arm to the furnace drawer.
    - i: ["gtceu:electric_blast_furnace", "gtceu:trinium_coil_block", "gtceu:uranium_rhodium_dinaquadide_ingot"]
      t: |-
        URD furnace: the trinium-coil EBF with a plain IV hatch (7680 EU/t), 1 dust → hot ingot in 75 s. Do NOT share it with naquadria unless you accept the swap: separate input drawers with circuit-keyed routers.
    - i: ["gtceu:vacuum_freezer", "gtceu:liquid_helium_bucket"]
      t: |-
        Freezer: hot URD ingot into a freezer at ZPM voltage (or the Mega Vacuum Freezer) with 500 mB liquid helium → URD ingot in 10 s at 122 880 EU/t. Output drawer Keep Exact 64; then the wiremill: single wire, double wire (the research chains), fine wire (field generators).
    - i: ["gtceu:large_mixer", "gtceu:dragonsteel_dust", "gtceu:magnesium_diboride_dust"]
      t: |-
        Dragonsteel (later): ghost circuit none, 4 tungsten + 8 magnesium diboride + 2 cadmium dust → 14 dust in 45 s at 16 000 EU/t in the Large Mixer on a 4A hatch.
    - i: ["gtceu:electric_blast_furnace", "gtceu:naquadah_coil_block", "gtceu:dragonsteel_ingot"]
      t: |-
        Dragonsteel furnace: naquadah coils (7200 K) on a LuV 4A hatch, 122 880 EU/t for 90 s per ingot; then freezer. Wires made from it are the ZPM superconductor cables.
    - i: ["functionalstorage:oak_1", "gtceu:uranium_rhodium_dinaquadide_ingot"]
      t: |-
        Easy to miss: count URD ingots before you start: the first research gear alone is about 112. Start the URD furnace as soon as the trinium coils are ready and let it run through the whole ZPM era.
---
# Uranium rhodium dinaquadide (URD, 9000 K) and dragonsteel (ZPM superconductor, 7100 K)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_urd` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Naquadah metals and ZPM coils](../../plan/p12.md#zpmmetals)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">Large Mixer on a LuV 4A hatch · circuit 4 · 7.5 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 uranium dust · 1 rhodium dust · 2 naquadah dust (functionalstorage:oak_1) - 4"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 uranium dust · 1 rhodium dust · 2 naquadah dust</span><span class="gt-sub"><span>Uranium dust</span><span>Rhodium dust</span><span>Naquadah dust</span></span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 URD dust (gtceu:uranium_rhodium_dinaquadide_dust) - 4 / 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uranium_rhodium_dinaquadide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uranium Rhodium Dinaquadide Dust</span><span class="gt-note">4 URD dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF · trinium coils 9001 K · 75 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 URD dust (gtceu:uranium_rhodium_dinaquadide_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uranium_rhodium_dinaquadide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uranium Rhodium Dinaquadide Dust</span><span class="gt-note">4 URD dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-f1" title="ZPM Vacuum Freezer or Mega Vacuum Freezer · liquid helium · 10 s · 122 880 EU/t (gtceu:vacuum_freezer) - hot ingot / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">ZPM Vacuum Freezer or Mega Vacuum Freezer · liquid helium · 10 s · 122 880 EU/t</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-f1">
<div class="gt-head"><span class="gt-mname">ZPM Vacuum Freezer or Mega Vacuum Freezer · liquid helium · 10 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-e1" title="EBF · trinium coils 9001 K · 75 s · 7680 EU/t (gtceu:electric_blast_furnace) - hot ingot / 75 s"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · trinium coils 9001 K · 75 s · 7680 EU/t</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="URD ingot (wire, double wire, fine wire) (gtceu:uranium_rhodium_dinaquadide_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uranium_rhodium_dinaquadide_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uranium Rhodium Dinaquadide Ingot</span><span class="gt-note">URD ingot (wire, double wire, fine wire)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">Large Mixer on a 4A hatch · 45 s · 16 000 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 tungsten dust · 8 magnesium diboride dust · 2 cadmium dust (functionalstorage:oak_1) - 14"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 tungsten dust · 8 magnesium diboride dust · 2 cadmium dust</span><span class="gt-sub"><span>Tungsten dust</span><span>Magnesium diboride dust</span><span>Cadmium dust</span></span><b class="gt-q">14</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="14 Dragonsteel dust (gtceu:dragonsteel_dust) - 14 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__dragonsteel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dragonsteel Dust</span><span class="gt-note">14 Dragonsteel dust</span><b class="gt-q">14</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF · naquadah coils 7200 K · 90 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="14 Dragonsteel dust (gtceu:dragonsteel_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__dragonsteel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dragonsteel Dust</span><span class="gt-note">14 Dragonsteel dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Dragonsteel ingot (ZPM superconductor) (gtceu:dragonsteel_ingot) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__dragonsteel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dragonsteel Ingot</span><span class="gt-note">Dragonsteel ingot (ZPM superconductor)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [Large Mixer on a LuV 4A hatch · circuit 4 · 7.5 s · 122 880 EU/t](#m-m1) → [EBF · trinium coils 9001 K · 75 s · 7680 EU/t](#m-e1) → [ZPM Vacuum Freezer or Mega Vacuum Freezer · liquid helium · 10 s · 122 880 EU/t](#m-f1)
- [Large Mixer on a 4A hatch · 45 s · 16 000 EU/t](#m-m2) → [EBF · naquadah coils 7200 K · 90 s · 122 880 EU/t](#m-e2)

## How to build

1. Drawers first, one per dust: uranium, rhodium, naquadah, tungsten, magnesium diboride, cadmium. Keep Exact 16 on each so a stuck mixer never swallows the rhodium. Every mixer sits behind its own router with Item Filters, with a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:uranium_dust`, `gtceu:rhodium_dust`, `gtceu:naquadah_dust`
2. URD mixer: Large Mixer on a LuV 4A hatch (122 880 EU/t), ghost circuit 4, 1 uranium + 1 rhodium + 2 naquadah dust → 4 URD dust in 7.5 s. Output dust goes by Robot Arm to the furnace drawer. — `gtceu:large_mixer`, `gtceu:uranium_rhodium_dinaquadide_dust`
3. URD furnace: the trinium-coil EBF with a plain IV hatch (7680 EU/t), 1 dust → hot ingot in 75 s. Do NOT share it with naquadria unless you accept the swap: separate input drawers with circuit-keyed routers. — `gtceu:electric_blast_furnace`, `gtceu:trinium_coil_block`, `gtceu:uranium_rhodium_dinaquadide_ingot`
4. Freezer: hot URD ingot into a freezer at ZPM voltage (or the Mega Vacuum Freezer) with 500 mB liquid helium → URD ingot in 10 s at 122 880 EU/t. Output drawer Keep Exact 64; then the wiremill: single wire, double wire (the research chains), fine wire (field generators). — `gtceu:vacuum_freezer`, `gtceu:liquid_helium_bucket`
5. Dragonsteel (later): ghost circuit none, 4 tungsten + 8 magnesium diboride + 2 cadmium dust → 14 dust in 45 s at 16 000 EU/t in the Large Mixer on a 4A hatch. — `gtceu:large_mixer`, `gtceu:dragonsteel_dust`, `gtceu:magnesium_diboride_dust`
6. Dragonsteel furnace: naquadah coils (7200 K) on a LuV 4A hatch, 122 880 EU/t for 90 s per ingot; then freezer. Wires made from it are the ZPM superconductor cables. — `gtceu:electric_blast_furnace`, `gtceu:naquadah_coil_block`, `gtceu:dragonsteel_ingot`
7. Easy to miss: count URD ingots before you start: the first research gear alone is about 112. Start the URD furnace as soon as the trinium coils are ready and let it run through the whole ZPM era. — `functionalstorage:oak_1`, `gtceu:uranium_rhodium_dinaquadide_ingot`

## Tips

- URD (MixerRecipes uranium\_rhodium\_dinaquadide, FirstDegreeMaterials): 1 uranium dust (the pack’s uranium is the 238 isotope, id gtceu:uranium) + 1 rhodium dust + 2 naquadah dust → 4 dust, circuit 4, 150 ticks at VA\[ZPM\] = 122 880 EU/t. That is a ZPM-power mixer recipe: a ZPM Mixer, or the Large Mixer on a LuV 4A hatch. EBF: 9000 K (trinium coils, zpm\_coils), 1500 ticks (75 s) but only VA\[IV\] = 7680 EU/t; the hot ingot then needs a freezer with vacuumStats VA\[ZPM\], 200 ticks: a freezer at ZPM voltage (122 880 EU/t), or the Mega Vacuum Freezer (GCYM multi in the era list) on the 4A hatch. Quest: URD is ‘used for ZPM Field Generators and the second tier of Fusion Reactors’.
- What eats URD (verified recipes): ZPM field generator 128 fine URD wire (16 ingots) each, Research Station 32 double wire (32 ingots), HPCA 64 double wire, Object Holder 16 double wire, the ZPM superconducting coil 16 double wire, ZPM Fusion Reactor 32 single wire (16 ingots). A first Research Station + HPCA + holder is about 112 URD ingots, i.e. 112 uranium, 112 rhodium and 224 naquadah dust: rhodium (platline, 7 per cooperite batch) is the scarce one.
- Dragonsteel (kjs additions/progression/superconductors.js + startup superconductors.js): 4 tungsten + 8 magnesium diboride + 2 cadmium dust → 14 dust, mixer 900 ticks at 16 000 EU/t (above an IV mixer: Large Mixer on a 4A hatch); EBF 7100 K, VA\[ZPM\] = 122 880 EU/t, 1800 ticks (90 s), gas tier high. It is the ZPM superconductor: a dragonsteel single wire carries 96 amps (quest), no loss. Only needed for ZPM power cables; skip it until your ZPM energy hatch exists. Magnesium diboride = 1 magnesium + 2 boron dust → 3 dust, circuit 4, 600 ticks at VA\[MV\] (MixerRecipes). Cadmium: Unverified source.
- Why EBF power is low for URD but the mixer is high: the 9000 K recipe itself is 7680 EU/t, so ONE furnace with an IV hatch can make URD from dust. Only the mixer (122 880 EU/t) and the freezer (122 880 EU/t) are ZPM power: batch the 4 dust per 7.5 s into a drawer, then the slow furnace. Since the Research Station recipe, field generators and the fusion reactor all need URD, this is the single most-needed ZPM alloy after osthendah.
- Sub-steps people skip: (1) circuit 4 in the mixer, 3 for osthendah, 2 for naquadah alloy: three machines, three ghost circuits; (2) trinium coils are required for 9000 K, so the order is: naquadah coils → trinium → trinium coils → URD; (3) the freezer step is the real power gate: if your only ZPM-capable machine is the Large Assembler, build the Mega Vacuum Freezer or a ZPM freezer before the first URD ingot; (4) keep naquadah dust Keep Exact in three drawers: three alloys fight for it.
- **Unverified** the uranium dust source (check EMI: the Chemical Plant skip uranite\_line\_skip gives 9 uranium + 1 uranium-235 from 30 uraninite + 40 B hydrofluoric acid at LuV power but needs the UV multiblock), the cadmium source, and the Mega Vacuum Freezer recipe tiers.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_mixer` | 2 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:trinium_coil_block` | 16 |
| `gtceu:naquadah_coil_block` | 16 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 2 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `gtceu:uranium_rhodium_dinaquadide_ingot`, `gtceu:uranium_rhodium_dinaquadide_dust`, `gtceu:uranium_rhodium_dinaquadide_double_wire`, `gtceu:dragonsteel_ingot`, `gtceu:dragonsteel_dust`, `gtceu:dragonsteel_single_wire`
