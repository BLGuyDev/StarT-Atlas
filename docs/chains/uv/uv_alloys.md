---
kind: chain
id: uv_alloys
order: 1640
data:
  t: |-
    UV metals: tritan steel (Alloy Blast Smelter, 8990 K) and the UV superconductor enriched naquadah trinium europium duranide (UV mixer + 9900 K blast)
  inf: true
  "n":
    - [b1, "LCR · 2 boron + 3 B oxygen → 5 boron trioxide · 5 s · 3840 EU/t", m, "gtceu:large_chemical_reactor"]
    - [b2, "LCR · 5 trioxide + 2 B ammonia → 4 boron nitride · 10 s · 3840 EU/t", m, "gtceu:large_chemical_reactor"]
    - - g1
      - |-
        7 tritanium · 3 maraging steel 300 · 2 enriched naquadah · 3 titanium tungsten carbide · 1 boron nitride (dusts)
      - g
      - functionalstorage:oak_1
      - - [Tritanium dust, "gtceu:tritanium_dust"]
        - [Maraging steel 300 dust, "gtceu:maraging_steel_300_dust"]
        - [Enriched naquadah dust, "gtceu:enriched_naquadah_dust"]
        - [Titanium tungsten carbide dust, "gtceu:titanium_tungsten_carbide_dust"]
        - [Boron nitride dust, "gtceu:boron_nitride_dust"]
    - - ab
      - Alloy Blast Smelter · circuit 5 · coil ≥ 8990 K · 24 min · 245 760 EU/t
      - m
      - gtceu:alloy_blast_smelter
    - [mt, "Tritan steel 2304 mB (16 ingots)", f, "gtceu:tritan_steel_bucket"]
    - [v1, "Vacuum Freezer · ingot mold", m, "gtceu:vacuum_freezer"]
    - - ts
      - Tritan steel ingots → plates, rods, gears, rings, rounds, screws, foil, frame
      - o
      - gtceu:tritan_steel_ingot
    - - g2
      - |-
        4 enriched naquadah · 3 trinium · 2 europium · 1 duranium (dusts)
      - g
      - functionalstorage:oak_1
      - - [Enriched naquadah dust, "gtceu:enriched_naquadah_dust"]
        - [Trinium dust, "gtceu:trinium_dust"]
        - [Europium dust, "gtceu:europium_dust"]
        - [Duranium dust, "gtceu:duranium_dust"]
    - [mx, "UV Mixer · circuit 4 · 8.75 s · 491 520 EU/t", m, "gtceu:uv_mixer"]
    - [ds, "10 ENTED dust", x, "gtceu:enriched_naquadah_trinium_europium_duranide_dust"]
    - [eb, "EBF · 9900 K (tritanium coils) · 60 s · 30 720 EU/t", m, "gtceu:electric_blast_furnace"]
    - [v2, "Vacuum Freezer · 10 s · 491 520 EU/t", m, "gtceu:vacuum_freezer"]
    - - en
      - ENTED ingot → fine / single / double wire
      - o
      - gtceu:enriched_naquadah_trinium_europium_duranide_ingot
  e:
    - [b1, b2, "5"]
    - [b2, g1, "1 per batch"]
    - [g1, ab, "16 dusts"]
    - [ab, mt, "2304 mB"]
    - [mt, v1, "144 mB each"]
    - [v1, ts, "16"]
    - [g2, mx, "10"]
    - [mx, ds, "10 / 8.75 s"]
    - [ds, eb, "1 each"]
    - [eb, v2, hot ingot]
    - [v2, en, "1"]
  tips:
    - |-
      Tritan steel (kjs startup casing_materials.js): 7 tritanium + 3 maraging steel 300 + 2 enriched naquadah + 3 titanium tungsten carbide + 1 boron nitride (16 parts), blast data [8990 K, gas tier highest, VHA[UV] = 245 760 EU/t, 2400 ticks per ingot]. The ABS rule (abs_super_ebf chain): one dust of each ratio part, circuit = number of components (5), output 16 ingots = 2304 mB, time 0.75 x 2400 x 16 = 28 800 ticks (24 min), 245 760 EU/t, which is a UV-tier recipe (a ZPM 4A hatch gives 524 288 EU/t). Coil rule: 8990 K needs trinium coils (9001 K, zpm_coils); the ABS only counts the coil tier.
    - |-
      Dusts to prepare: tritanium dust (from tritanium ingots, uv_fusion_mats: a MK II reactor with tier-3 reflectors makes it, no UV reactor needed), enriched naquadah dust (zpm_naq_products), boron nitride dust (kjs abydos_lines/ultimate.js: LCR boron_trioxide 2 boron + 3 B oxygen → 5 dust, 100 ticks at VHA[IV] and LCR boron_nitride 5 trioxide + 2 B ammonia → 4 BN dust + 3 B water, 200 ticks at VHA[IV]), maraging steel 300 and titanium tungsten carbide (GCYM alloys; Unverified compositions and furnaces: check EMI). The 16-ingot batch is the minimum: the ABS recipe does not scale down.
    - |-
      Tritan steel parts (flags in the material): plate, rod, long rod, frame, gear, small gear, round, ring, bolt, screw, foil, dense plate. UV components eat them in bulk: a UV motor is 4 long rods + 4 rings + 8 rounds, a conveyor adds 16 rounds + 4 screws + 4 rings + 2 plates, the sensor and emitter use a frame each: plan on 30 to 60 ingots per component set.
    - |-
      ENTED (gtsrc MixerRecipes + FirstDegreeMaterials): mixer, circuit 4, 4 enriched naquadah + 3 trinium + 2 europium + 1 duranium dust → 10 dust, 175 ticks at VA[UV] = 491 520 EU/t (a UV mixer, so the hull of uv_hull comes first); blast 9900 K, VA[LuV] = 30 720 EU/t, 1200 ticks; vacuum freezer 200 ticks at VA[UV]. 9900 K is above trinium coils (9001 K), so it needs TRITANIUM coils (10 800 K; uv_hatches) or a Mega Blast Furnace. Cable: V[UV], 16 A (use wire sizes for the field generator: 128 fine wire; fusion reactor: 32 single wire; coil: 16 double wire).
    - |-
      Sub-steps people skip: (1) the ABS rejects a dust stack with a wrong count: 7/3/2/3/1, no spare; (2) the EBF recipe for ENTED needs a gas and a freezer step like every hot ingot above 5000 K (Unverified gas amount); (3) the UV mixer needs a UV hull first (uv_hull), so the very first ENTED comes from the mixer you build with the first hull; (4) the ammonia drum is the same one that feeds the polyimide line.
    - |-
      Unverified: maraging steel 300 and titanium tungsten carbide recipes, the blast gas, boron source.
  b:
    - ["gtceu:alloy_blast_smelter", 1]
    - ["gtceu:uv_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:large_chemical_reactor", 2]
    - ["gtceu:zpm_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 4]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:tritanium_dust
        - gtceu:maraging_steel_300_dust
        - gtceu:boron_nitride_dust
      t: |-
        Drawers first: tritanium (Keep Exact 7), maraging steel 300 (3), enriched naquadah (2), titanium tungsten carbide (3), boron nitride (1); a second set for ENTED: enriched naquadah (4), trinium (3), europium (2), duranium (1). Drums: tritan steel, boron oxygen/ammonia. Each stack has its own router with an Item Filter.
    - i: ["gtceu:large_chemical_reactor", "gtceu:boron_nitride_dust"]
      t: |-
        Boron nitride: LCR 1 (boron + oxygen → trioxide), LCR 2 (trioxide + ammonia → BN); water out into a drum.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:tritan_steel_bucket"]
      t: |-
        ABS: circuit 5, 16 dusts per batch, 245 760 EU/t for 24 min; make sure the structure has trinium coils (9001 K). Output 2304 mB into a drum.
    - i: ["gtceu:vacuum_freezer", "gtceu:tritan_steel_ingot"]
      t: |-
        Freeze: ingot mold in the freezer or a fluid solidifier for plates and frames; 144 mB per ingot.
    - i: ["gtceu:uv_mixer", "gtceu:enriched_naquadah_trinium_europium_duranide_dust"]
      t: |-
        ENTED: UV mixer circuit 4, then EBF 9900 K (tritanium coils) and the vacuum freezer (UV); output drawer for the ingots, then a wiremill for fine, single and double wire.
    - i: ["functionalstorage:oak_1", "gtceu:tritan_steel_ingot"]
      t: Output drawers Keep Exact 16 each. Do not mix tritan steel and tritanium stacks.
---
# UV metals: tritan steel (Alloy Blast Smelter, 8990 K) and the UV superconductor enriched naquadah trinium europium duranide (UV mixer + 9900 K blast)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV metals (tritan steel, UV superconductor)](../../plan/p15.md#uvmetals)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-b1">
<div class="gt-head"><span class="gt-mname">LCR · 2 boron + 3 B oxygen → 5 boron trioxide · 5 s · 3840 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-b2" title="LCR · 5 trioxide + 2 B ammonia → 4 boron nitride · 10 s · 3840 EU/t (gtceu:large_chemical_reactor) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 5 trioxide + 2 B ammonia → 4 boron nitride · 10 s · 3840 EU/t</span><b class="gt-q">5</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-b2">
<div class="gt-head"><span class="gt-mname">LCR · 5 trioxide + 2 B ammonia → 4 boron nitride · 10 s · 3840 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-b1" title="LCR · 2 boron + 3 B oxygen → 5 boron trioxide · 5 s · 3840 EU/t (gtceu:large_chemical_reactor) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 2 boron + 3 B oxygen → 5 boron trioxide · 5 s · 3840 EU/t</span><b class="gt-q">5</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="7 tritanium · 3 maraging steel 300 · 2 enriched naquadah · 3 titanium tungsten carbide · 1 boron nitride (dusts) (functionalstorage:oak_1) - 1 per batch"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">7 tritanium · 3 maraging steel 300 · 2 enriched naquadah · 3 titanium tungsten carbide · 1 boron nitride (dusts)</span><span class="gt-sub"><span>Tritanium dust</span><span>Maraging steel 300 dust</span><span>Enriched naquadah dust</span><span>Titanium tungsten carbide dust</span><span>Boron nitride dust</span></span><b class="gt-q">1 per batch</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-ab">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · circuit 5 · coil ≥ 8990 K · 24 min · 245 760 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="7 tritanium · 3 maraging steel 300 · 2 enriched naquadah · 3 titanium tungsten carbide · 1 boron nitride (dusts) (functionalstorage:oak_1) - 16 dusts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">7 tritanium · 3 maraging steel 300 · 2 enriched naquadah · 3 titanium tungsten carbide · 1 boron nitride (dusts)</span><span class="gt-sub"><span>Tritanium dust</span><span>Maraging steel 300 dust</span><span>Enriched naquadah dust</span><span>Titanium tungsten carbide dust</span><span>Boron nitride dust</span></span><b class="gt-q">16 dusts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Tritan steel 2304 mB (16 ingots) (gtceu:tritan_steel_bucket) - 2304 mB"><img class="gt-ico" src="../../assets/icons/gtceu__tritan_steel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritan Steel</span><span class="gt-note">Tritan steel 2304 mB (16 ingots)</span><b class="gt-q">2304 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
<div class="gt-panel t-multi" id="m-v1">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · ingot mold</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Tritan steel 2304 mB (16 ingots) (gtceu:tritan_steel_bucket) - 144 mB each"><img class="gt-ico" src="../../assets/icons/gtceu__tritan_steel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritan Steel</span><span class="gt-note">Tritan steel 2304 mB (16 ingots)</span><b class="gt-q">144 mB each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Tritan steel ingots → plates, rods, gears, rings, rounds, screws, foil, frame (gtceu:tritan_steel_ingot) - 16"><img class="gt-ico" src="../../assets/icons/gtceu__tritan_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritan Steel Ingot</span><span class="gt-note">Tritan steel ingots → plates, rods, gears, rings, rounds, screws, foil, frame</span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-uv" id="m-mx">
<div class="gt-head"><span class="gt-mname">UV Mixer · circuit 4 · 8.75 s · 491 520 EU/t</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 enriched naquadah · 3 trinium · 2 europium · 1 duranium (dusts) (functionalstorage:oak_1) - 10"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 enriched naquadah · 3 trinium · 2 europium · 1 duranium (dusts)</span><span class="gt-sub"><span>Enriched naquadah dust</span><span>Trinium dust</span><span>Europium dust</span><span>Duranium dust</span></span><b class="gt-q">10</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">8.75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="10 ENTED dust (gtceu:enriched_naquadah_trinium_europium_duranide_dust) - 10 / 8.75 s"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_naquadah_trinium_europium_duranide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Naquadah Trinium Europium Duranide Dust</span><span class="gt-note">10 ENTED dust</span><b class="gt-q">10</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · 9900 K (tritanium coils) · 60 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="10 ENTED dust (gtceu:enriched_naquadah_trinium_europium_duranide_dust) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_naquadah_trinium_europium_duranide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Naquadah Trinium Europium Duranide Dust</span><span class="gt-note">10 ENTED dust</span><b class="gt-q">1 each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-v2" title="Vacuum Freezer · 10 s · 491 520 EU/t (gtceu:vacuum_freezer) - hot ingot"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer · 10 s · 491 520 EU/t</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-v2">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 10 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-eb" title="EBF · 9900 K (tritanium coils) · 60 s · 30 720 EU/t (gtceu:electric_blast_furnace) - hot ingot"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · 9900 K (tritanium coils) · 60 s · 30 720 EU/t</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ENTED ingot → fine / single / double wire (gtceu:enriched_naquadah_trinium_europium_duranide_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_naquadah_trinium_europium_duranide_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Naquadah Trinium Europium Duranide Ingot</span><span class="gt-note">ENTED ingot → fine / single / double wire</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [LCR · 2 boron + 3 B oxygen → 5 boron trioxide · 5 s · 3840 EU/t](#m-b1) → [LCR · 5 trioxide + 2 B ammonia → 4 boron nitride · 10 s · 3840 EU/t](#m-b2) → [Alloy Blast Smelter · circuit 5 · coil ≥ 8990 K · 24 min · 245 760 EU/t](#m-ab) → [Vacuum Freezer · ingot mold](#m-v1)
- [UV Mixer · circuit 4 · 8.75 s · 491 520 EU/t](#m-mx) → [EBF · 9900 K (tritanium coils) · 60 s · 30 720 EU/t](#m-eb) → [Vacuum Freezer · 10 s · 491 520 EU/t](#m-v2)

## How to build

1. Drawers first: tritanium (Keep Exact 7), maraging steel 300 (3), enriched naquadah (2), titanium tungsten carbide (3), boron nitride (1); a second set for ENTED: enriched naquadah (4), trinium (3), europium (2), duranium (1). Drums: tritan steel, boron oxygen/ammonia. Each stack has its own router with an Item Filter. — `functionalstorage:oak_1`, `gtceu:tritanium_dust`, `gtceu:maraging_steel_300_dust`, `gtceu:boron_nitride_dust`
2. Boron nitride: LCR 1 (boron + oxygen → trioxide), LCR 2 (trioxide + ammonia → BN); water out into a drum. — `gtceu:large_chemical_reactor`, `gtceu:boron_nitride_dust`
3. ABS: circuit 5, 16 dusts per batch, 245 760 EU/t for 24 min; make sure the structure has trinium coils (9001 K). Output 2304 mB into a drum. — `gtceu:alloy_blast_smelter`, `gtceu:tritan_steel_bucket`
4. Freeze: ingot mold in the freezer or a fluid solidifier for plates and frames; 144 mB per ingot. — `gtceu:vacuum_freezer`, `gtceu:tritan_steel_ingot`
5. ENTED: UV mixer circuit 4, then EBF 9900 K (tritanium coils) and the vacuum freezer (UV); output drawer for the ingots, then a wiremill for fine, single and double wire. — `gtceu:uv_mixer`, `gtceu:enriched_naquadah_trinium_europium_duranide_dust`
6. Output drawers Keep Exact 16 each. Do not mix tritan steel and tritanium stacks. — `functionalstorage:oak_1`, `gtceu:tritan_steel_ingot`

## Tips

- Tritan steel (kjs startup casing\_materials.js): 7 tritanium + 3 maraging steel 300 + 2 enriched naquadah + 3 titanium tungsten carbide + 1 boron nitride (16 parts), blast data \[8990 K, gas tier highest, VHA\[UV\] = 245 760 EU/t, 2400 ticks per ingot\]. The ABS rule (abs\_super\_ebf chain): one dust of each ratio part, circuit = number of components (5), output 16 ingots = 2304 mB, time 0.75 x 2400 x 16 = 28 800 ticks (24 min), 245 760 EU/t, which is a UV-tier recipe (a ZPM 4A hatch gives 524 288 EU/t). Coil rule: 8990 K needs trinium coils (9001 K, zpm\_coils); the ABS only counts the coil tier.
- Dusts to prepare: tritanium dust (from tritanium ingots, uv\_fusion\_mats: a MK II reactor with tier-3 reflectors makes it, no UV reactor needed), enriched naquadah dust (zpm\_naq\_products), boron nitride dust (kjs abydos\_lines/ultimate.js: LCR boron\_trioxide 2 boron + 3 B oxygen → 5 dust, 100 ticks at VHA\[IV\] and LCR boron\_nitride 5 trioxide + 2 B ammonia → 4 BN dust + 3 B water, 200 ticks at VHA\[IV\]), maraging steel 300 and titanium tungsten carbide (GCYM alloys; Unverified compositions and furnaces: check EMI). The 16-ingot batch is the minimum: the ABS recipe does not scale down.
- Tritan steel parts (flags in the material): plate, rod, long rod, frame, gear, small gear, round, ring, bolt, screw, foil, dense plate. UV components eat them in bulk: a UV motor is 4 long rods + 4 rings + 8 rounds, a conveyor adds 16 rounds + 4 screws + 4 rings + 2 plates, the sensor and emitter use a frame each: plan on 30 to 60 ingots per component set.
- ENTED (gtsrc MixerRecipes + FirstDegreeMaterials): mixer, circuit 4, 4 enriched naquadah + 3 trinium + 2 europium + 1 duranium dust → 10 dust, 175 ticks at VA\[UV\] = 491 520 EU/t (a UV mixer, so the hull of uv\_hull comes first); blast 9900 K, VA\[LuV\] = 30 720 EU/t, 1200 ticks; vacuum freezer 200 ticks at VA\[UV\]. 9900 K is above trinium coils (9001 K), so it needs TRITANIUM coils (10 800 K; uv\_hatches) or a Mega Blast Furnace. Cable: V\[UV\], 16 A (use wire sizes for the field generator: 128 fine wire; fusion reactor: 32 single wire; coil: 16 double wire).
- Sub-steps people skip: (1) the ABS rejects a dust stack with a wrong count: 7/3/2/3/1, no spare; (2) the EBF recipe for ENTED needs a gas and a freezer step like every hot ingot above 5000 K (Unverified gas amount); (3) the UV mixer needs a UV hull first (uv\_hull), so the very first ENTED comes from the mixer you build with the first hull; (4) the ammonia drum is the same one that feeds the polyimide line.
- **Unverified** maraging steel 300 and titanium tungsten carbide recipes, the blast gas, boron source.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:alloy_blast_smelter` | 1 |
| `gtceu:uv_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:large_chemical_reactor` | 2 |
| `gtceu:zpm_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:tritan_steel_ingot`, `gtceu:tritan_steel_bucket`, `gtceu:enriched_naquadah_trinium_europium_duranide_ingot`, `gtceu:boron_nitride_dust`, `gtceu:enriched_naquadah_trinium_europium_duranide_single_wire`
