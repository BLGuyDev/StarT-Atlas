---
kind: chain
id: uv_rare_earth
order: 1760
data:
  t: |-
    Xenotime rare earth line: 5 machines → yttrium + small lutetium, dysprosium, europium, samarium dust; dysprosium and zapolgium rods are polarized in the pack’s own recipe
  inf: true
  "n":
    - - g1
      - "3 xenotime dust · 3 B sulfuric acid"
      - g
      - functionalstorage:oak_1
      - [[Xenotime dust, "gtceu:xenotime_dust"], [Sulfuric acid, "gtceu:sulfuric_acid_bucket"]]
    - - m1
      - LCR · 27.5 s · 28 000 EU/t → 1 B RE sulfate solution + 2 B phosphoric acid
      - m
      - gtceu:large_chemical_reactor
    - - g2
      - "1 rare earth dust · 2 B RE sulfate solution"
      - g
      - functionalstorage:oak_1
      - [[Rare earth dust, "gtceu:rare_earth_dust"]]
    - [m2, "Mixer · 7.5 s · 88 000 EU/t → 2 B leach mixture", m, "gtceu:zpm_mixer"]
    - [m3, "Electrolyzer · 35 s · 26 000 EU/t → 1 yttrium dust + 3 B RE concentrate", m, "gtceu:luv_electrolyzer"]
    - - g3
      - "2 quicklime dust · 1 B RE concentrate"
      - g
      - functionalstorage:oak_1
      - [[Quicklime dust, "gtceu:quicklime_dust"]]
    - - m4
      - EBF 7500 K · 60 s · 30 000 EU/t → 1 rich rare earth dust + 6 calcium sulfate + 1 B oxygen
      - m
      - gtceu:electric_blast_furnace
    - [m5, "Centrifuge · 1.4 s · 48 000 EU/t · chanced", m, "gtceu:zpm_centrifuge"]
    - - out
      - |-
        Small dusts (40 % each, +3 % per tier above the recipe): lutetium · dysprosium · europium · samarium
      - g
      - functionalstorage:oak_1
      - - [Small lutetium dust, "gtceu:small_lutetium_dust"]
        - [Small dysprosium dust, "gtceu:small_dysprosium_dust"]
        - [Small europium dust, "gtceu:small_europium_dust"]
        - [Small samarium dust, "gtceu:small_samarium_dust"]
    - [pl, "Polarizer · dysprosium rod → magnetic rod 5 s (long rod 10 s) · 30 720 EU/t", m, "gtceu:luv_polarizer"]
    - [mg, "Magnetic dysprosium rod (UV voltage coil, motor)", o, "gtceu:magnetic_dysprosium_rod"]
  e:
    - [g1, m1, "1"]
    - [m1, g2, "2 B"]
    - [g2, m2, "1"]
    - [m2, m3, "1 B"]
    - [m3, g3, "3 B"]
    - [g3, m4, "1"]
    - [m4, m5, "1 dust"]
    - [m5, out, chance]
    - [out, pl, dysprosium]
    - [pl, mg, "1"]
  tips:
    - |-
      Source: kjs abydos_lines/rare_earth.js (verified numbers; the EU/t are the raw values written in the script). Step 1: Large Chemical Reactor, 3 xenotime dust + 3 B sulfuric acid → 1 B rare earth sulfate solution + 2 B phosphoric acid, 550 ticks, 28 000 EU/t. Step 2: mixer, 1 rare earth dust + 2 B sulfate solution → 2 B leach mixture, 150 ticks, 88 000 EU/t (needs a UV-tier hatch or the ZPM mixer at 131 072 EU/t: 88 000 is below ZPM, so a ZPM mixer works). Step 3: electrolyzer, 1 B leach → 1 yttrium dust + 3 B rare earth concentrate, 700 ticks, 26 000 EU/t. Step 4: EBF at 7500 K, 2 quicklime + 1 B concentrate → 1 rich rare earth dust + 6 calcium sulfate dust + 1 B oxygen, 1200 ticks, 30 000 EU/t (7500 K needs trinium coils 9001 K). Step 5: centrifuge, 1 rich dust → small dusts of lutetium, dysprosium, europium, samarium at 40 % each (boost 3 % per tier above), 28 ticks, 48 000 EU/t.
    - |-
      Yield warning: a small dust is a quarter of a dust, so one run of the whole chain gives 0.1 dust of each rare earth plus 1 yttrium dust per 3 xenotime dust: the line is slow by design. Each UV motor needs 1 long magnetic dysprosium rod (2 ingots = 8 small dusts from 20 rich dust), each voltage coil 1 rod, so dysprosium is the bottleneck of UV machines and hatches. Europium and lutetium also have fusion routes (kjs fusion_scaling.js: europium from neodymium + hydrogen; lutetium from lanthanum + silicon), samarium and yttrium do not.
    - |-
      Magnetic rods (pack override, same file): the GT recipes for magnetic dysprosium and zapolgium rods are removed; the new polarizer recipes are rod → magnetic rod in duration/2 (dysprosium: 100 ticks at VA[LuV] = 30 720 EU/t) and long rod → long magnetic rod (200 ticks); zapolgium: 150 / 300 ticks at VA[UV] = 491 520 EU/t. So a UV-tier polarizer is needed for zapolgium (UHV) magnets, and any LuV polarizer for dysprosium.
    - |-
      Loop warning: step 2 consumes a rare earth dust each time; the line recovers none (the 40 % small dusts are different metals). Rare earth dust and quicklime need their own source (Unverified: rare earth dust comes from the monazite / ore line).
    - |-
      Where it sits in the order (verified): xenotime is mined only in the Abydos refractory-metals ore vein (and later comes out of the refractory magma), so this line is the first Abydos job. The dysprosium rods feed the UV motors and pumps of the Fluid Drilling Rig and Molten Destabiliser (uv_akreyrium) and of the Bacterial Runic Mutator, Breeding Vat and Hydrocarbon Harvester (uv_bio2). Rare earth dust itself is an ordinary ore/gCrop product (source not traced here).
    - |-
      Sub-steps people skip: (1) the EBF needs trinium coils (9001 K) or better for 7500 K; (2) phosphoric acid by-product (2 B per run) feeds the gelatin line (uv_bio2); (3) separate machines for each of the five steps, never reuse a hatch; (4) machine tier follows the raw EU/t: the 88 000 EU/t mixer and the 48 000 EU/t centrifuge need ZPM machines, 26 000 to 30 000 EU/t fits LuV.
    - |-
      Unverified: rare earth dust and quicklime sources, monazite processing, UV recipe oxygen sink.
  b:
    - ["gtceu:large_chemical_reactor", 1]
    - ["gtceu:zpm_mixer", 1]
    - ["gtceu:luv_electrolyzer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:zpm_centrifuge", 1]
    - ["gtceu:luv_polarizer", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:xenotime_dust", "gtceu:quicklime_dust", "gtceu:rare_earth_dust"]
      t: |-
        Drawers first: xenotime dust (Keep Exact 3), rare earth dust (1), quicklime dust (2), and output drawers for yttrium dust, the four small dusts, calcium sulfate. Drums: sulfuric acid, RE sulfate solution, leach mixture, concentrate, phosphoric acid, oxygen.
    - i: ["gtceu:large_chemical_reactor", "gtceu:rare_earth_sulfate_solution_bucket"]
      t: |-
        LCR step: 3 dust + 3 B acid → 1 B solution (+2 B phosphoric acid into its own drum for uv_bio2). 27.5 s.
    - i: ["gtceu:zpm_mixer", "gtceu:luv_electrolyzer"]
      t: |-
        Mixer then electrolyzer, one machine each: leach mixture 2 B per 7.5 s; 1 yttrium dust + 3 B concentrate per 35 s.
    - i: ["gtceu:electric_blast_furnace", "gtceu:rich_rare_earth_dust"]
      t: |-
        EBF at 7500 K (trinium coils): 2 quicklime + 1 B concentrate → rich dust in 60 s at 30 000 EU/t; calcium sulfate dust to a drawer, oxygen to a drum.
    - i: ["gtceu:zpm_centrifuge", "gtceu:small_dysprosium_dust"]
      t: |-
        Centrifuge: rich dust → four chanced small dusts; compress 4 small into 1 dust with a packer.
    - i: ["gtceu:luv_polarizer", "gtceu:magnetic_dysprosium_rod"]
      t: |-
        Dysprosium: ingot → rod (lathe) → polarizer (100 ticks, 30 720 EU/t) → magnetic rod; long rod → long magnetic rod (200 ticks). Output drawer Keep Exact 4.
---
# Xenotime rare earth line: 5 machines → yttrium + small lutetium, dysprosium, europium, samarium dust; dysprosium and zapolgium rods are polarized in the pack’s own recipe

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_rare_earth` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Abydos first: xenotime → dysprosium → drilling rig and magma](../../plan/p14.md#abydos)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">LCR · 27.5 s · 28 000 EU/t → 1 B RE sulfate solution + 2 B phosphoric acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="3 xenotime dust · 3 B sulfuric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">3 xenotime dust · 3 B sulfuric acid</span><span class="gt-sub"><span>Xenotime dust</span><span>Sulfuric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="1 rare earth dust · 2 B RE sulfate solution (functionalstorage:oak_1) - 2 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 rare earth dust · 2 B RE sulfate solution</span><span class="gt-sub"><span>Rare earth dust</span></span><b class="gt-q">2 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m2">
<div class="gt-head"><span class="gt-mname">Mixer · 7.5 s · 88 000 EU/t → 2 B leach mixture</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 rare earth dust · 2 B RE sulfate solution (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 rare earth dust · 2 B RE sulfate solution</span><span class="gt-sub"><span>Rare earth dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="Electrolyzer · 35 s · 26 000 EU/t → 1 yttrium dust + 3 B RE concentrate (gtceu:luv_electrolyzer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Electrolyzer</span><span class="gt-note">Electrolyzer · 35 s · 26 000 EU/t → 1 yttrium dust + 3 B RE concentrate</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_mixer</code></div>
</div>
<div class="gt-panel t-luv" id="m-m3">
<div class="gt-head"><span class="gt-mname">Electrolyzer · 35 s · 26 000 EU/t → 1 yttrium dust + 3 B RE concentrate</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="Mixer · 7.5 s · 88 000 EU/t → 2 B leach mixture (gtceu:zpm_mixer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Mixer</span><span class="gt-note">Mixer · 7.5 s · 88 000 EU/t → 2 B leach mixture</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="2 quicklime dust · 1 B RE concentrate (functionalstorage:oak_1) - 3 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 quicklime dust · 1 B RE concentrate</span><span class="gt-sub"><span>Quicklime dust</span></span><b class="gt-q">3 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_electrolyzer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">EBF 7500 K · 60 s · 30 000 EU/t → 1 rich rare earth dust + 6 calcium sulfate + 1 B oxygen</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 quicklime dust · 1 B RE concentrate (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 quicklime dust · 1 B RE concentrate</span><span class="gt-sub"><span>Quicklime dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="Centrifuge · 1.4 s · 48 000 EU/t · chanced (gtceu:zpm_centrifuge) - 1 dust"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Centrifuge</span><span class="gt-note">Centrifuge · 1.4 s · 48 000 EU/t · chanced</span><b class="gt-q">1 dust</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m5">
<div class="gt-head"><span class="gt-mname">Centrifuge · 1.4 s · 48 000 EU/t · chanced</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m4" title="EBF 7500 K · 60 s · 30 000 EU/t → 1 rich rare earth dust + 6 calcium sulfate + 1 B oxygen (gtceu:electric_blast_furnace) - 1 dust"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 7500 K · 60 s · 30 000 EU/t → 1 rich rare earth dust + 6 calcium sulfate + 1 B oxygen</span><b class="gt-q">1 dust</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Small dusts (40 % each, +3 % per tier above the recipe): lutetium · dysprosium · europium · samarium (functionalstorage:oak_1) - chance"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Small dusts (40 % each, +3 % per tier above the recipe): lutetium · dysprosium · europium · samarium</span><span class="gt-sub"><span>Small lutetium dust</span><span>Small dysprosium dust</span><span>Small europium dust</span><span>Small samarium dust</span></span><b class="gt-q">chance</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_centrifuge</code></div>
</div>
<div class="gt-panel t-luv" id="m-pl">
<div class="gt-head"><span class="gt-mname">Polarizer · dysprosium rod → magnetic rod 5 s (long rod 10 s) · 30 720 EU/t</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Small dusts (40 % each, +3 % per tier above the recipe): lutetium · dysprosium · europium · samarium (functionalstorage:oak_1) - dysprosium"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Small dusts (40 % each, +3 % per tier above the recipe): lutetium · dysprosium · europium · samarium</span><span class="gt-sub"><span>Small lutetium dust</span><span>Small dysprosium dust</span><span>Small europium dust</span><span>Small samarium dust</span></span><b class="gt-q">dysprosium</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Magnetic dysprosium rod (UV voltage coil, motor) (gtceu:magnetic_dysprosium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_dysprosium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Dysprosium Rod</span><span class="gt-note">Magnetic dysprosium rod (UV voltage coil, motor)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_polarizer</code></div>
</div>
</div>

## Flow

- [LCR · 27.5 s · 28 000 EU/t → 1 B RE sulfate solution + 2 B phosphoric acid](#m-m1) → [Mixer · 7.5 s · 88 000 EU/t → 2 B leach mixture](#m-m2) → [Electrolyzer · 35 s · 26 000 EU/t → 1 yttrium dust + 3 B RE concentrate](#m-m3) → [EBF 7500 K · 60 s · 30 000 EU/t → 1 rich rare earth dust + 6 calcium sulfate + 1 B oxygen](#m-m4) → [Centrifuge · 1.4 s · 48 000 EU/t · chanced](#m-m5) → [Polarizer · dysprosium rod → magnetic rod 5 s (long rod 10 s) · 30 720 EU/t](#m-pl)

## How to build

1. Drawers first: xenotime dust (Keep Exact 3), rare earth dust (1), quicklime dust (2), and output drawers for yttrium dust, the four small dusts, calcium sulfate. Drums: sulfuric acid, RE sulfate solution, leach mixture, concentrate, phosphoric acid, oxygen. — `functionalstorage:oak_1`, `gtceu:xenotime_dust`, `gtceu:quicklime_dust`, `gtceu:rare_earth_dust`
2. LCR step: 3 dust + 3 B acid → 1 B solution (+2 B phosphoric acid into its own drum for uv\_bio2). 27.5 s. — `gtceu:large_chemical_reactor`, `gtceu:rare_earth_sulfate_solution_bucket`
3. Mixer then electrolyzer, one machine each: leach mixture 2 B per 7.5 s; 1 yttrium dust + 3 B concentrate per 35 s. — `gtceu:zpm_mixer`, `gtceu:luv_electrolyzer`
4. EBF at 7500 K (trinium coils): 2 quicklime + 1 B concentrate → rich dust in 60 s at 30 000 EU/t; calcium sulfate dust to a drawer, oxygen to a drum. — `gtceu:electric_blast_furnace`, `gtceu:rich_rare_earth_dust`
5. Centrifuge: rich dust → four chanced small dusts; compress 4 small into 1 dust with a packer. — `gtceu:zpm_centrifuge`, `gtceu:small_dysprosium_dust`
6. Dysprosium: ingot → rod (lathe) → polarizer (100 ticks, 30 720 EU/t) → magnetic rod; long rod → long magnetic rod (200 ticks). Output drawer Keep Exact 4. — `gtceu:luv_polarizer`, `gtceu:magnetic_dysprosium_rod`

## Tips

- Source: kjs abydos\_lines/rare\_earth.js (verified numbers; the EU/t are the raw values written in the script). Step 1: Large Chemical Reactor, 3 xenotime dust + 3 B sulfuric acid → 1 B rare earth sulfate solution + 2 B phosphoric acid, 550 ticks, 28 000 EU/t. Step 2: mixer, 1 rare earth dust + 2 B sulfate solution → 2 B leach mixture, 150 ticks, 88 000 EU/t (needs a UV-tier hatch or the ZPM mixer at 131 072 EU/t: 88 000 is below ZPM, so a ZPM mixer works). Step 3: electrolyzer, 1 B leach → 1 yttrium dust + 3 B rare earth concentrate, 700 ticks, 26 000 EU/t. Step 4: EBF at 7500 K, 2 quicklime + 1 B concentrate → 1 rich rare earth dust + 6 calcium sulfate dust + 1 B oxygen, 1200 ticks, 30 000 EU/t (7500 K needs trinium coils 9001 K). Step 5: centrifuge, 1 rich dust → small dusts of lutetium, dysprosium, europium, samarium at 40 % each (boost 3 % per tier above), 28 ticks, 48 000 EU/t.
- Yield warning: a small dust is a quarter of a dust, so one run of the whole chain gives 0.1 dust of each rare earth plus 1 yttrium dust per 3 xenotime dust: the line is slow by design. Each UV motor needs 1 long magnetic dysprosium rod (2 ingots = 8 small dusts from 20 rich dust), each voltage coil 1 rod, so dysprosium is the bottleneck of UV machines and hatches. Europium and lutetium also have fusion routes (kjs fusion\_scaling.js: europium from neodymium + hydrogen; lutetium from lanthanum + silicon), samarium and yttrium do not.
- Magnetic rods (pack override, same file): the GT recipes for magnetic dysprosium and zapolgium rods are removed; the new polarizer recipes are rod → magnetic rod in duration/2 (dysprosium: 100 ticks at VA\[LuV\] = 30 720 EU/t) and long rod → long magnetic rod (200 ticks); zapolgium: 150 / 300 ticks at VA\[UV\] = 491 520 EU/t. So a UV-tier polarizer is needed for zapolgium (UHV) magnets, and any LuV polarizer for dysprosium.
- Loop warning: step 2 consumes a rare earth dust each time; the line recovers none (the 40 % small dusts are different metals). Rare earth dust and quicklime need their own source (Unverified: rare earth dust comes from the monazite / ore line).
- Where it sits in the order (verified): xenotime is mined only in the Abydos refractory-metals ore vein (and later comes out of the refractory magma), so this line is the first Abydos job. The dysprosium rods feed the UV motors and pumps of the Fluid Drilling Rig and Molten Destabiliser (uv\_akreyrium) and of the Bacterial Runic Mutator, Breeding Vat and Hydrocarbon Harvester (uv\_bio2). Rare earth dust itself is an ordinary ore/gCrop product (source not traced here).
- Sub-steps people skip: (1) the EBF needs trinium coils (9001 K) or better for 7500 K; (2) phosphoric acid by-product (2 B per run) feeds the gelatin line (uv\_bio2); (3) separate machines for each of the five steps, never reuse a hatch; (4) machine tier follows the raw EU/t: the 88 000 EU/t mixer and the 48 000 EU/t centrifuge need ZPM machines, 26 000 to 30 000 EU/t fits LuV.
- **Unverified** rare earth dust and quicklime sources, monazite processing, UV recipe oxygen sink.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 1 |
| `gtceu:zpm_mixer` | 1 |
| `gtceu:luv_electrolyzer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:zpm_centrifuge` | 1 |
| `gtceu:luv_polarizer` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:magnetic_dysprosium_rod`, `gtceu:long_magnetic_dysprosium_rod`, `gtceu:yttrium_dust`, `gtceu:small_dysprosium_dust`, `gtceu:rich_rare_earth_dust`
