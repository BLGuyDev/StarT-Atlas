---
kind: chain
id: uhv_zapolgium
order: 1800
data:
  t: |-
    Zapolgium from zapolite: separator, centrifuge, electrolyzer, hydrochloric acid, KOH, EBF 10 299 K
  inf: true
  "n":
    - [g1, "1 zapolite dust", g, "functionalstorage:oak_1", [[Zapolite dust, "gtceu:zapolite_dust"]]]
    - - m1
      - Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide
      - m
      - gtceu:ev_electromagnetic_separator
    - [m2, "Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite", m, "gtceu:iv_centrifuge"]
    - [m3, "Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine", m, "gtceu:iv_electrolyzer"]
    - - m4
      - LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water
      - m
      - gtceu:large_chemical_reactor
    - [m5, "LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride", m, "gtceu:large_chemical_reactor"]
    - - m6
      - LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt
      - m
      - gtceu:large_chemical_reactor
    - - m7
      - EBF 10 299 K (tritanium coils) · 4.6 min · 98 000 EU/t · 5 hydroxide + 1 carbon
      - m
      - gtceu:electric_blast_furnace
    - [hz, "Hot zapolgium ingot → vacuum freezer → ingot", x, "gtceu:hot_zapolgium_ingot"]
    - [zg, "Zapolgium ingot (zalloy, pipes, magnets)", o, "gtceu:zapolgium_ingot"]
  e:
    - [g1, m1, "1"]
    - [m1, m2, "9 of Zg Al oxide"]
    - [m1, m4, "5 of dioxide"]
    - [m2, m3, "4"]
    - [m3, m5, "2 oxide"]
    - [m4, m5, "2 oxide"]
    - [m5, m6, "3"]
    - [m6, m7, "5"]
    - [m7, hz, "1"]
    - [hz, zg, freeze]
  tips:
    - |-
      Source: kjs abydos_lines/zapolgium.js (verified, EU/t as written). 1) Electromagnetic separator, 1 zapolite dust → 1 zapolgium aluminium oxide dust + a 40 % chance (+10 % per tier above) of 1 zapolgium diiodide dioxide dust, 100 ticks, 2600 EU/t. 2a) Centrifuge, 9 Zg aluminium oxide → 4 Zg diiodide oxide + 5 bauxite dust, 800 ticks, 12 000 EU/t; then electrolyzer 4 diiodide oxide → 2 zapolgium oxide + 2 iodine dust, 600 ticks, 16 000 EU/t. 2b) LCR, 5 Zg diiodide dioxide + 2 B hydrogen → 2 zapolgium oxide + 2 iodine + 1 B water, 300 ticks, 20 000 EU/t. 3) LCR 2 oxide + 2 B HCl → 3 zapolgium chloride + 1 B water, 600 ticks, 28 000 EU/t. 4) LCR 3 chloride + 6 potassium hydroxide → 5 zapolgium hydroxide + 4 rock salt, 1200 ticks, 56 000 EU/t. 5) EBF 10 299 K, 5 hydroxide + 1 carbon → 1 hot zapolgium ingot + 1 B carbon monoxide + 1 B steam, 5500 ticks (4.6 min), 98 000 EU/t; freeze in a vacuum freezer.
    - |-
      Ratios: one ingot needs 5 zapolgium hydroxide = 3 chloride (1.67 oxide) = about 3 zapolite dust if the oxide route is the main one: the line gives ~1 ingot per 5 zapolite. Iodine returns (2 per oxide run) feed the zirconium selenide diiodide of uhv_alloys and the hydroiodic acid of the naquadite line. Zalloy needs 3 zapolgium per 9 parts, magnetic zapolgium rods (polarizer, UV tier) and zapolgium pipes (UHV pump and valve) are the other users.
    - |-
      Order and alternatives (verified): the 10 299 K EBF step needs tritanium coils and tritanium (Fusion MK II with tier-3 reflectors, 200 MEU), NOT the UV Fusion Reactor, so zapolgium can be finished before the MK III exists; the zapolite itself comes from the Abydos activation-metals vein and from the reactive magma residue (4 raw zapolite). Zapolite is also a gCrop (start_core:zapolite_gcrop, fruit tier 7); the fruit-to-dust recipe lives in the jar and is unverified, so treat it as an unconfirmed alternative. Do not plan a zalloy coil before the gate: kubejs:zalloy_coil_block (13 499 K) is an assembler recipe at 1 966 080 EU/t (UHV hatch) with a neutronium frame + 8 zalloy double wire + 8 zirconium foil + 32 fine RTAN wire + 16 neutronium SiC foil + 144 mB tritanium.
    - |-
      Machine tiers: 98 000 EU/t EBF recipe needs a ZPM-class hatch (131 072 EU/t) on the EBF or a Mega Blast Furnace; 10 299 K means TRITANIUM coils (10 800 K), the same coil as zalloy. The LCR at 56 000 EU/t needs ZPM, 28 000 and 20 000 LuV.
    - |-
      Sub-steps people skip: (1) the separator chance output feeds a second path (LCR with hydrogen): do not void it; (2) rock salt and bauxite are by-products with uses in the chlorine and aluminium lines; (3) one machine per step (7 machines); (4) the EBF needs a gas? The blast data of zapolgium says highest gas tier (Unverified gas usage: the script has no gas input).
    - |-
      Unverified: potassium hydroxide supply, zapolite dust from raw zapolite (ore line), gas for the hot ingot.
  b:
    - ["gtceu:large_chemical_reactor", 3]
    - ["gtceu:ev_electromagnetic_separator", 1]
    - ["gtceu:iv_centrifuge", 1]
    - ["gtceu:iv_electrolyzer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:zapolite_dust", "gtceu:potassium_hydroxide_dust", "gtceu:carbon_dust"]
      t: |-
        Drawers first: zapolite dust, potassium hydroxide (6), carbon (1), output drawers for bauxite, iodine, rock salt, zapolgium oxide. Drums: hydrogen, hydrochloric acid, water, carbon monoxide, steam.
    - i: ["gtceu:ev_electromagnetic_separator", "gtceu:zapolgium_aluminium_oxide_dust"]
      t: |-
        Separator: 1 dust → aluminium oxide dust + chanced dioxide dust: two output paths, each with its own drawer.
    - i: ["gtceu:iv_centrifuge", "gtceu:iv_electrolyzer"]
      t: |-
        Path A: centrifuge then electrolyzer (oxide + iodine). Path B: LCR with hydrogen (oxide + iodine).
    - i: ["gtceu:large_chemical_reactor", "gtceu:zapolgium_chloride_dust", "gtceu:zapolgium_hydroxide_dust"]
      t: Chloride LCR (HCl) then hydroxide LCR (KOH), 3 + 6 → 5 hydroxide dust.
    - i: ["gtceu:electric_blast_furnace", "gtceu:hot_zapolgium_ingot"]
      t: |-
        EBF, 10 299 K, circuit none: 5 hydroxide + 1 carbon → hot ingot; carbon monoxide and steam into drums; vacuum freezer for the ingot.
    - i: ["functionalstorage:oak_1", "gtceu:zapolgium_ingot"]
      t: Output drawer Keep Exact 16.
---
# Zapolgium from zapolite: separator, centrifuge, electrolyzer, hydrochloric acid, KOH, EBF 10 299 K

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_zapolgium` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Zapolgium, superconductors, alloys, void ingot](../../plan/p17.md#uhvmetals)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-m1">
<div class="gt-head"><span class="gt-mname">Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 zapolite dust (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 zapolite dust</span><span class="gt-sub"><span>Zapolite dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electromagnetic_separator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite (gtceu:iv_centrifuge) - 9 of Zg Al oxide"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite</span><b class="gt-q">9 of Zg Al oxide</b></a><a class="gt-slot gt-mach" href="#m-m4" title="LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water (gtceu:large_chemical_reactor) - 5 of dioxide"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water</span><b class="gt-q">5 of dioxide</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:ev_electromagnetic_separator</code></div>
</div>
<div class="gt-panel t-iv" id="m-m2">
<div class="gt-head"><span class="gt-mname">Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide (gtceu:ev_electromagnetic_separator) - 9 of Zg Al oxide"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electromagnetic_separator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electromagnetic Separator</span><span class="gt-note">Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide</span><b class="gt-q">9 of Zg Al oxide</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine (gtceu:iv_electrolyzer) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electrolyzer</span><span class="gt-note">Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine</span><b class="gt-q">4</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_centrifuge</code></div>
</div>
<div class="gt-panel t-iv" id="m-m3">
<div class="gt-head"><span class="gt-mname">Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite (gtceu:iv_centrifuge) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite</span><b class="gt-q">4</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride (gtceu:large_chemical_reactor) - 2 oxide"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride</span><b class="gt-q">2 oxide</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_electrolyzer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide (gtceu:ev_electromagnetic_separator) - 5 of dioxide"><img class="gt-ico" src="../../assets/icons/gtceu__ev_electromagnetic_separator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Electromagnetic Separator</span><span class="gt-note">Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide</span><b class="gt-q">5 of dioxide</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride (gtceu:large_chemical_reactor) - 2 oxide"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride</span><b class="gt-q">2 oxide</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine (gtceu:iv_electrolyzer) - 2 oxide"><img class="gt-ico" src="../../assets/icons/gtceu__iv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Electrolyzer</span><span class="gt-note">Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine</span><b class="gt-q">2 oxide</b></a><a class="gt-slot gt-mach" href="#m-m4" title="LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water (gtceu:large_chemical_reactor) - 2 oxide"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water</span><b class="gt-q">2 oxide</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m6" title="LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt (gtceu:large_chemical_reactor) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt</span><b class="gt-q">3</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m6">
<div class="gt-head"><span class="gt-mname">LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride (gtceu:large_chemical_reactor) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride</span><b class="gt-q">3</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m7" title="EBF 10 299 K (tritanium coils) · 4.6 min · 98 000 EU/t · 5 hydroxide + 1 carbon (gtceu:electric_blast_furnace) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 10 299 K (tritanium coils) · 4.6 min · 98 000 EU/t · 5 hydroxide + 1 carbon</span><b class="gt-q">5</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m7">
<div class="gt-head"><span class="gt-mname">EBF 10 299 K (tritanium coils) · 4.6 min · 98 000 EU/t · 5 hydroxide + 1 carbon</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m6" title="LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt (gtceu:large_chemical_reactor) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt</span><b class="gt-q">5</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot zapolgium ingot → vacuum freezer → ingot (gtceu:hot_zapolgium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_zapolgium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Zapolgium Ingot</span><span class="gt-note">Hot zapolgium ingot → vacuum freezer → ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide](#m-m1) → [Centrifuge · 40 s · 12 000 EU/t · 9 dust → 4 Zg diiodide oxide + 5 bauxite](#m-m2) → [Electrolyzer · 30 s · 16 000 EU/t · 4 dust → 2 zapolgium oxide + 2 iodine](#m-m3) → [LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride](#m-m5) → [LCR · 60 s · 56 000 EU/t · 3 chloride + 6 KOH → 5 hydroxide + 4 rock salt](#m-m6) → [EBF 10 299 K (tritanium coils) · 4.6 min · 98 000 EU/t · 5 hydroxide + 1 carbon](#m-m7) (also Electromagnetic Separator · 5 s · 2600 EU/t → Zg aluminium oxide + 40 % Zg diiodide dioxide → [LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water](#m-m4))
- [LCR · 15 s · 20 000 EU/t · 5 dioxide dust + 2 B hydrogen → 2 oxide + 2 iodine + water](#m-m4) → [LCR · 30 s · 28 000 EU/t · 2 oxide + 2 B HCl → 3 zapolgium chloride](#m-m5)

### Direct steps

- Hot zapolgium ingot → vacuum freezer → ingot → Zapolgium ingot (zalloy, pipes, magnets) (freeze)

## How to build

1. Drawers first: zapolite dust, potassium hydroxide (6), carbon (1), output drawers for bauxite, iodine, rock salt, zapolgium oxide. Drums: hydrogen, hydrochloric acid, water, carbon monoxide, steam. — `functionalstorage:oak_1`, `gtceu:zapolite_dust`, `gtceu:potassium_hydroxide_dust`, `gtceu:carbon_dust`
2. Separator: 1 dust → aluminium oxide dust + chanced dioxide dust: two output paths, each with its own drawer. — `gtceu:ev_electromagnetic_separator`, `gtceu:zapolgium_aluminium_oxide_dust`
3. Path A: centrifuge then electrolyzer (oxide + iodine). Path B: LCR with hydrogen (oxide + iodine). — `gtceu:iv_centrifuge`, `gtceu:iv_electrolyzer`
4. Chloride LCR (HCl) then hydroxide LCR (KOH), 3 + 6 → 5 hydroxide dust. — `gtceu:large_chemical_reactor`, `gtceu:zapolgium_chloride_dust`, `gtceu:zapolgium_hydroxide_dust`
5. EBF, 10 299 K, circuit none: 5 hydroxide + 1 carbon → hot ingot; carbon monoxide and steam into drums; vacuum freezer for the ingot. — `gtceu:electric_blast_furnace`, `gtceu:hot_zapolgium_ingot`
6. Output drawer Keep Exact 16. — `functionalstorage:oak_1`, `gtceu:zapolgium_ingot`

## Tips

- Source: kjs abydos\_lines/zapolgium.js (verified, EU/t as written). 1) Electromagnetic separator, 1 zapolite dust → 1 zapolgium aluminium oxide dust + a 40 % chance (+10 % per tier above) of 1 zapolgium diiodide dioxide dust, 100 ticks, 2600 EU/t. 2a) Centrifuge, 9 Zg aluminium oxide → 4 Zg diiodide oxide + 5 bauxite dust, 800 ticks, 12 000 EU/t; then electrolyzer 4 diiodide oxide → 2 zapolgium oxide + 2 iodine dust, 600 ticks, 16 000 EU/t. 2b) LCR, 5 Zg diiodide dioxide + 2 B hydrogen → 2 zapolgium oxide + 2 iodine + 1 B water, 300 ticks, 20 000 EU/t. 3) LCR 2 oxide + 2 B HCl → 3 zapolgium chloride + 1 B water, 600 ticks, 28 000 EU/t. 4) LCR 3 chloride + 6 potassium hydroxide → 5 zapolgium hydroxide + 4 rock salt, 1200 ticks, 56 000 EU/t. 5) EBF 10 299 K, 5 hydroxide + 1 carbon → 1 hot zapolgium ingot + 1 B carbon monoxide + 1 B steam, 5500 ticks (4.6 min), 98 000 EU/t; freeze in a vacuum freezer.
- Ratios: one ingot needs 5 zapolgium hydroxide = 3 chloride (1.67 oxide) = about 3 zapolite dust if the oxide route is the main one: the line gives ~1 ingot per 5 zapolite. Iodine returns (2 per oxide run) feed the zirconium selenide diiodide of uhv\_alloys and the hydroiodic acid of the naquadite line. Zalloy needs 3 zapolgium per 9 parts, magnetic zapolgium rods (polarizer, UV tier) and zapolgium pipes (UHV pump and valve) are the other users.
- Order and alternatives (verified): the 10 299 K EBF step needs tritanium coils and tritanium (Fusion MK II with tier-3 reflectors, 200 MEU), NOT the UV Fusion Reactor, so zapolgium can be finished before the MK III exists; the zapolite itself comes from the Abydos activation-metals vein and from the reactive magma residue (4 raw zapolite). Zapolite is also a gCrop (start\_core:zapolite\_gcrop, fruit tier 7); the fruit-to-dust recipe lives in the jar and is unverified, so treat it as an unconfirmed alternative. Do not plan a zalloy coil before the gate: kubejs:zalloy\_coil\_block (13 499 K) is an assembler recipe at 1 966 080 EU/t (UHV hatch) with a neutronium frame + 8 zalloy double wire + 8 zirconium foil + 32 fine RTAN wire + 16 neutronium SiC foil + 144 mB tritanium.
- Machine tiers: 98 000 EU/t EBF recipe needs a ZPM-class hatch (131 072 EU/t) on the EBF or a Mega Blast Furnace; 10 299 K means TRITANIUM coils (10 800 K), the same coil as zalloy. The LCR at 56 000 EU/t needs ZPM, 28 000 and 20 000 LuV.
- Sub-steps people skip: (1) the separator chance output feeds a second path (LCR with hydrogen): do not void it; (2) rock salt and bauxite are by-products with uses in the chlorine and aluminium lines; (3) one machine per step (7 machines); (4) the EBF needs a gas? The blast data of zapolgium says highest gas tier (Unverified gas usage: the script has no gas input).
- **Unverified** potassium hydroxide supply, zapolite dust from raw zapolite (ore line), gas for the hot ingot.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 3 |
| `gtceu:ev_electromagnetic_separator` | 1 |
| `gtceu:iv_centrifuge` | 1 |
| `gtceu:iv_electrolyzer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:zapolgium_ingot`, `gtceu:hot_zapolgium_ingot`, `gtceu:zapolite_dust`, `gtceu:zapolgium_dust`
