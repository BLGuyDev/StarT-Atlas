---
kind: chain
id: uhv_runic_infusion
order: 1930
data:
  t: |-
    Runic convergence infusion: netherite trisulfate complex → voidic nitride + astral fluorosilicate → primordial nitrosilicate; + magnesium nitride in the Vacuum Chemical Reaction Chamber
  inf: true
  "n":
    - - m1
      - LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen
      - m
      - gtceu:large_chemical_reactor
    - - m2
      - LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust
      - m
      - gtceu:large_chemical_reactor
    - - m3
      - LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid)
      - m
      - gtceu:large_chemical_reactor
    - - m4
      - LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate
      - m
      - gtceu:large_chemical_reactor
    - - m5
      - LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate
      - m
      - gtceu:large_chemical_reactor
    - - m6
      - Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate
      - m
      - gtceu:uv_mixer
    - - m7
      - LCR · 12 s · 122 880 EU/t · 3 magnesium dust + 2 B nitrogen → 1 B magnesium nitride
      - m
      - gtceu:large_chemical_reactor
    - - m8
      - Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)
      - m
      - gtceu:vacuum_chemical_reaction_chamber
    - [ri, Runic convergence infusion 1 B, o, "gtceu:runic_convergence_infusion_bucket"]
  e:
    - [m1, m2, "1 B"]
    - [m1, m4, "1 B"]
    - [m2, m3, "30 dust"]
    - [m4, m5, "9 dust"]
    - [m3, m6, "1 B"]
    - [m5, m6, "1 B"]
    - [m6, m8, "1 B"]
    - [m7, m8, "1 B"]
    - [m8, ri, "1 B / 6 s"]
  tips:
    - |-
      Source: kjs additions/progression/lines/gate_lines/runic_convergence.js (verified). Steps and power: netherite trisulfate complex (LCR, 160 ticks, VHA[ZPM] = 61 440 EU/t); hexammine sulfate (220 ticks, VHA[ZPM]); voidic nitride (480 ticks, VHA[UV] = 245 760); netherite tetrahydroxide (120 ticks, VHA[UV]; the script notes a x6 scale of the dust amounts); astral fluorosilicate (200 ticks, VHA[ZPM]); primordial nitrosilicate (mixer, 80 ticks at VHA[UHV] = 983 040 EU/t); magnesium nitride (240 ticks, VA[ZPM]); the infusion: Vacuum Chemical Reaction Chamber, 120 ticks at VA[UV] = 491 520 EU/t, vacuum level 90 (ZPM-era multi, zpm_multis), 7 ancient runicalium bolts as a non-consumed catalyst.
    - |-
      Ratios: 1 B of complex (from 1 pure netherite dust) splits into the two branches: 1 B goes to the hexammine/voidic branch and 1 B to the tetrahydroxide branch, so 2 pure netherite dust per 1 B of infusion, 1 B magnesium nitride (3 magnesium dust) and 8 B + 16 B hydrogen, 8 B nitrobenzene. By-products: ammonia, phenol, sulfuric acid return to their drums; 18 calcium sulfate dust per run (the dust amounts in step 4 show 9 and 18 per 15 calcium hydroxide).
    - |-
      The infusion is consumed by the runic circuits (7.5 B per 32 runic boards, 250 mB per convergence unit, 500 to 1000 mB per assembly / computer / mainframe: uhv_runic), the 3-fluid draconic recipes and the Draco infusion line.
    - |-
      Machine tiers: the mixer step needs 983 040 EU/t (UV 4A); the VCRC step needs the multiblock at UV power; the others run on ZPM hatches. 7 LCR + 1 mixer + 1 VCRC.
    - |-
      Sub-steps people skip: (1) the bolts are a catalyst: put them in an input bus and never void them; (2) pure netherite dust (the 5000 K netherite line, Unverified source); (3) vacuum level 90 means the chamber needs its vacuum pump / vacuum casing status; (4) every step is a separate machine.
    - |-
      Unverified: pure netherite dust supply, ancient runicalium source, nitrobenzene supply, vacuum level mechanic.
  b:
    - ["gtceu:large_chemical_reactor", 7]
    - ["gtceu:uv_mixer", 1]
    - ["gtceu:vacuum_chemical_reaction_chamber", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 1]
    - ["gtceu:zpm_energy_input_hatch", 2]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 14]
    - ["gtceu:steel_drum", 14]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:pure_netherite_dust
        - gtceu:ancient_runicalium_bolt
        - gtceu:calcium_hydroxide_dust
      t: |-
        Drawers first: pure netherite dust, calcium hydroxide (15), silicon dioxide (2), magnesium (3), ancient runicalium bolts (7, catalyst, Keep Exact 7). Drums: sulfuric acid, water, ammonia, hydrogen, nitrobenzene, HF, nitrogen and each intermediate.
    - i: ["gtceu:large_chemical_reactor", "gtceu:netherite_trisulfate_complex_bucket"]
      t: Complex reactor, then split the output with two Pipez fluid pipes and valves into the hexammine and tetrahydroxide branches.
    - i: ["gtceu:large_chemical_reactor", "gtceu:voidic_nitride_bucket", "gtceu:astral_fluorosilicate_bucket"]
      t: Voidic nitride branch (2 LCRs, UV hatch for the second) and astral branch (2 LCRs).
    - i: ["gtceu:uv_mixer", "gtceu:primordial_nitrosilicate_bucket"]
      t: "Mixer at 983 040 EU/t: 1 B + 1 B per 4 s."
    - i: ["gtceu:vacuum_chemical_reaction_chamber", "gtceu:runic_convergence_infusion_bucket"]
      t: |-
        Vacuum Chemical Reaction Chamber: nitrosilicate + magnesium nitride by fluid pipes, bolts in the bus; infusion into a drum.
    - i: ["functionalstorage:oak_1", "gtceu:runic_convergence_infusion_bucket"]
      t: |-
        Easy to miss: the line is small in machines (9) but eats hydrogen by the 20 B: plan the drums.
---
# Runic convergence infusion: netherite trisulfate complex → voidic nitride + astral fluorosilicate → primordial nitrosilicate; + magnesium nitride in the Vacuum Chemical Reaction Chamber

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_runic_infusion` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Runic infusion and runic circuits](../../plan/p17.md#uhvcirc)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m4" title="LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid) (gtceu:large_chemical_reactor) - 30 dust"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid)</span><b class="gt-q">30 dust</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust (gtceu:large_chemical_reactor) - 30 dust"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust</span><b class="gt-q">30 dust</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m6" title="Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate (gtceu:uv_mixer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Mixer</span><span class="gt-note">Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate (gtceu:large_chemical_reactor) - 9 dust"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate</span><b class="gt-q">9 dust</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m4" title="LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate (gtceu:large_chemical_reactor) - 9 dust"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate</span><b class="gt-q">9 dust</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m6" title="Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate (gtceu:uv_mixer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Mixer</span><span class="gt-note">Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-uv" id="m-m6">
<div class="gt-head"><span class="gt-mname">Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid) (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid)</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m8" title="Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept) (gtceu:vacuum_chemical_reaction_chamber) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_chemical_reaction_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Chemical Reaction Chamber</span><span class="gt-note">Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:uv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m7">
<div class="gt-head"><span class="gt-mname">LCR · 12 s · 122 880 EU/t · 3 magnesium dust + 2 B nitrogen → 1 B magnesium nitride</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m8" title="Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept) (gtceu:vacuum_chemical_reaction_chamber) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_chemical_reaction_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Chemical Reaction Chamber</span><span class="gt-note">Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mod" id="m-m8">
<div class="gt-head"><span class="gt-mname">Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m6" title="Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate (gtceu:uv_mixer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Mixer</span><span class="gt-note">Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m7" title="LCR · 12 s · 122 880 EU/t · 3 magnesium dust + 2 B nitrogen → 1 B magnesium nitride (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12 s · 122 880 EU/t · 3 magnesium dust + 2 B nitrogen → 1 B magnesium nitride</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_chemical_reaction_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">6 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Runic convergence infusion 1 B (gtceu:runic_convergence_infusion_bucket) - 1 B / 6 s"><img class="gt-ico" src="../../assets/icons/gtceu__runic_convergence_infusion_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Runic Convergence Infusion Bucket</span><span class="gt-note">Runic convergence infusion 1 B</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_chemical_reaction_chamber</code></div>
</div>
</div>

## Flow

- [LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen](#m-m1) → [LCR · 11 s · 61 440 EU/t · 1 B complex + 6 B ammonia + 6 B hydrogen → 30 hexammine sulfate dust](#m-m2) → [LCR · 24 s · 245 760 EU/t · 30 dust + 8 B nitrobenzene + 16 B hydrogen → 1 B voidic nitride (+ ammonia, phenol, sulfuric acid)](#m-m3) → [Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate](#m-m6) → [Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)](#m-m8) (also LCR · 8 s · 61 440 EU/t · 1 pure netherite dust + 3 B sulfuric acid + 2 B water → 1 B netherite trisulfate complex + 8 B hydrogen → [LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate](#m-m4))
- [LCR · 12 s · 122 880 EU/t · 3 magnesium dust + 2 B nitrogen → 1 B magnesium nitride](#m-m7) → [Vacuum Chemical Reaction Chamber · vacuum 90 · 6 s · 491 520 EU/t · 7 ancient runicalium bolts (kept)](#m-m8)
- [LCR · 6 s · 245 760 EU/t · 15 calcium hydroxide + 1 B complex + 4 B hydrogen → 9 netherite tetrahydroxide + 18 calcium sulfate](#m-m4) → [LCR · 10 s · 61 440 EU/t · 9 tetrahydroxide + 2 silicon dioxide + 4 B HF → 1 B astral fluorosilicate](#m-m5) → [Mixer · 4 s · 983 040 EU/t · 1 B voidic nitride + 1 B astral → 1 B primordial nitrosilicate](#m-m6)

## How to build

1. Drawers first: pure netherite dust, calcium hydroxide (15), silicon dioxide (2), magnesium (3), ancient runicalium bolts (7, catalyst, Keep Exact 7). Drums: sulfuric acid, water, ammonia, hydrogen, nitrobenzene, HF, nitrogen and each intermediate. — `functionalstorage:oak_1`, `gtceu:pure_netherite_dust`, `gtceu:ancient_runicalium_bolt`, `gtceu:calcium_hydroxide_dust`
2. Complex reactor, then split the output with two Pipez fluid pipes and valves into the hexammine and tetrahydroxide branches. — `gtceu:large_chemical_reactor`, `gtceu:netherite_trisulfate_complex_bucket`
3. Voidic nitride branch (2 LCRs, UV hatch for the second) and astral branch (2 LCRs). — `gtceu:large_chemical_reactor`, `gtceu:voidic_nitride_bucket`, `gtceu:astral_fluorosilicate_bucket`
4. Mixer at 983 040 EU/t: 1 B + 1 B per 4 s. — `gtceu:uv_mixer`, `gtceu:primordial_nitrosilicate_bucket`
5. Vacuum Chemical Reaction Chamber: nitrosilicate + magnesium nitride by fluid pipes, bolts in the bus; infusion into a drum. — `gtceu:vacuum_chemical_reaction_chamber`, `gtceu:runic_convergence_infusion_bucket`
6. Easy to miss: the line is small in machines (9) but eats hydrogen by the 20 B: plan the drums. — `functionalstorage:oak_1`, `gtceu:runic_convergence_infusion_bucket`

## Tips

- Source: kjs additions/progression/lines/gate\_lines/runic\_convergence.js (verified). Steps and power: netherite trisulfate complex (LCR, 160 ticks, VHA\[ZPM\] = 61 440 EU/t); hexammine sulfate (220 ticks, VHA\[ZPM\]); voidic nitride (480 ticks, VHA\[UV\] = 245 760); netherite tetrahydroxide (120 ticks, VHA\[UV\]; the script notes a x6 scale of the dust amounts); astral fluorosilicate (200 ticks, VHA\[ZPM\]); primordial nitrosilicate (mixer, 80 ticks at VHA\[UHV\] = 983 040 EU/t); magnesium nitride (240 ticks, VA\[ZPM\]); the infusion: Vacuum Chemical Reaction Chamber, 120 ticks at VA\[UV\] = 491 520 EU/t, vacuum level 90 (ZPM-era multi, zpm\_multis), 7 ancient runicalium bolts as a non-consumed catalyst.
- Ratios: 1 B of complex (from 1 pure netherite dust) splits into the two branches: 1 B goes to the hexammine/voidic branch and 1 B to the tetrahydroxide branch, so 2 pure netherite dust per 1 B of infusion, 1 B magnesium nitride (3 magnesium dust) and 8 B + 16 B hydrogen, 8 B nitrobenzene. By-products: ammonia, phenol, sulfuric acid return to their drums; 18 calcium sulfate dust per run (the dust amounts in step 4 show 9 and 18 per 15 calcium hydroxide).
- The infusion is consumed by the runic circuits (7.5 B per 32 runic boards, 250 mB per convergence unit, 500 to 1000 mB per assembly / computer / mainframe: uhv\_runic), the 3-fluid draconic recipes and the Draco infusion line.
- Machine tiers: the mixer step needs 983 040 EU/t (UV 4A); the VCRC step needs the multiblock at UV power; the others run on ZPM hatches. 7 LCR + 1 mixer + 1 VCRC.
- Sub-steps people skip: (1) the bolts are a catalyst: put them in an input bus and never void them; (2) pure netherite dust (the 5000 K netherite line, Unverified source); (3) vacuum level 90 means the chamber needs its vacuum pump / vacuum casing status; (4) every step is a separate machine.
- **Unverified** pure netherite dust supply, ancient runicalium source, nitrobenzene supply, vacuum level mechanic.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 7 |
| `gtceu:uv_mixer` | 1 |
| `gtceu:vacuum_chemical_reaction_chamber` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 1 |
| `gtceu:zpm_energy_input_hatch` | 2 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 14 |
| `gtceu:steel_drum` | 14 |

## Needs / Feeds

- **Main source for:** `gtceu:runic_convergence_infusion_bucket`, `gtceu:primordial_nitrosilicate_bucket`, `gtceu:voidic_nitride_bucket`
