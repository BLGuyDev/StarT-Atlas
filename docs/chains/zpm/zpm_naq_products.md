---
kind: chain
id: zpm_naq_products
order: 1390
data:
  t: |-
    Naquadah products: 6 naquadah dust → 1 trinium + 1.5 enriched naquadah + 1.5 naquadria (centrifuges, acid loops, EBF 7000 / 7200 / 9000 K)
  inf: true
  "n":
    - - lc
      - Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid
      - m
      - gtceu:large_chemical_reactor
    - [c1, "Centrifuge · 40 s · IV power · 4 B impure enriched solution", m, "gtceu:iv_centrifuge"]
    - [c2, "Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution", m, "gtceu:iv_centrifuge"]
    - [ts, Trinium sulfide dust, x, "gtceu:trinium_sulfide_dust"]
    - - a1
      - HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate
      - m
      - gtceu:hv_mixer
    - - a2
      - HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate
      - m
      - gtceu:hv_mixer
    - [e1, "EBF 7200 K · 37.5 s · 30 720 EU/t · 2 trinium sulfide + 1 zinc dust", m, "gtceu:electric_blast_furnace"]
    - [e2, "EBF 7000 K · 25 s · 7680 EU/t · 6 sulfate + 2 B hydrogen", m, "gtceu:electric_blast_furnace"]
    - - e3
      - EBF 9000 K (trinium coils) · 30 s · 122 880 EU/t · 6 sulfate + 2 B hydrogen
      - m
      - gtceu:electric_blast_furnace
    - [o1, "Trinium ingot (after the Vacuum Freezer)", o, "gtceu:trinium_ingot"]
    - [o2, Enriched naquadah ingot, o, "gtceu:enriched_naquadah_ingot"]
    - [o3, Naquadria ingot, o, "gtceu:naquadria_ingot"]
  e:
    - [lc, c1, "2 B"]
    - [lc, c2, "2 B"]
    - [c1, ts, "3 per 4 B"]
    - [c2, ts, "1 per 4 B"]
    - [c1, a1, "3 B solution"]
    - [c2, a2, "3 B solution"]
    - [ts, e1, "2"]
    - [a1, e2, "6"]
    - [a2, e3, "6"]
    - [e1, o1, "1"]
    - [e2, o2, "1"]
    - [e3, o3, "1"]
  tips:
    - |-
      The base line is in the naquadah chain (naquadah dust → 6 dust + 1 B fluoroantimonic acid → 2 B impure enriched + 2 B impure naquadria + 4 titanium trifluoride, Large Chemical Reactor 600 ticks at 30 720 EU/t, NaquadahRecipes naquadah_separation). This chain is what happens next. Pack change (kjs additions/recipe_changes.js, ‘naquadah changes’): the impure-solution centrifuges are replaced: 4 B impure enriched naquadah solution → 3 trinium sulfide + 4 antimony trifluoride + 3 B enriched naquadah solution, 800 ticks, VHA[IV]; 4 B impure naquadria solution → 2 indium phosphide + 1 trinium sulfide + 4 antimony trifluoride + 3 B naquadria solution, 600 ticks, VA[IV].
    - |-
      Yield (derived from those recipes and cross-checked with the Chemical Plant skip, which gives 12 naquadah → 3 enriched + 3 naquadria + 2 trinium): 6 naquadah dust give 2 B + 2 B impure solution, i.e. 1.5 + 0.5 trinium sulfide = 2 sulfide = 1 trinium ingot, 1.5 B enriched solution and 1.5 B naquadria solution = 1.5 enriched naquadah ingots + 1.5 naquadria ingots, before the waste loops add a little more. The antimony trifluoride goes back into the fluoroantimonic acid line (4 antimony trifluoride + 4 B hydrofluoric acid → 1 B acid + 2 B hydrogen, 300 ticks, 480 EU/t), the indium phosphide into the indium line, the titanium trifluoride into titanium.
    - |-
      Acid loops (NaquadahRecipes, not changed by the pack): enriched: Mixer (HV, 100 ticks, 480 EU/t) 1 B solution + 2 B sulfuric acid → 3 B acidic solution; Centrifuge (HV, 100 ticks, 480 EU/t) 3 B acidic → 2 B waste + 500 mB fluorine + 6 enriched naquadah sulfate; EBF 7000 K, 500 ticks at 7680 EU/t: 6 sulfate + 2 B hydrogen → hot enriched naquadah ingot + 1 B sulfuric acid (freezer: 150 ticks at 2048, liquid helium above 5000 K). Naquadria is the same with the sulfate EBF at 9000 K, 600 ticks, VA[ZPM] = 122 880 EU/t (freezer 200 ticks at VA[LuV]). The waste loop: distillation tower 2 B waste → 50 % barium sulfide (enriched) or gallium sulfide (naquadria) + 500 mB sulfuric acid + 250 mB own solution + 100 mB of the other solution, 300 ticks at 480 EU/t.
    - |-
      Trinium: EBF 7200 K, EUt VA[LuV] = 30 720, 750 ticks: 2 trinium sulfide + 1 zinc dust → hot trinium ingot + 2 zinc sulfide (the zinc sulfide goes to the zinc loop); freezer 300 ticks at VA[IV] (ElementMaterials trinium: 7200 K, vacuum VA[IV] 300). 7200 K is exactly a NAQUADAH coil; so the first trinium needs naquadah coils (zpm_coils), which only need naquadah, not trinium. Naquadria needs 9000 K = TRINIUM coils (9001 K): the coils are made from trinium double wire, so the first naquadria comes only after the first 16 trinium ingots.
    - |-
      Power: the 9000 K recipe is 122 880 EU/t: an EBF on a LuV 4A hatch (4 x 32 768) or a ZPM hatch. The 7200 K and 7000 K ones fit a 4A IV hatch (30 720) and an IV hatch (7680). One EBF per recipe, each with its own coils: a single furnace cannot switch between 7000 K, 7200 K and 9000 K runs when circuit and hatch must differ.
    - |-
      Machines (verified): naquadah_separation is a Large Chemical Reactor recipe (LuV, 600 ticks). The LCR runs it with perfect overclock and NO parallel hatch; the Extreme Chemical Reactor (ECR) is the multi that accepts a parallel hatch (non-perfect overclock, batch mode), so scale this line with an ECR. The last step (naquadria sulfate, 9000 K, VA[ZPM], 600 ticks) can run in the Hardened Industrial Furnace [HIF, gtceu:super_ebf]: it takes ONE energy hatch and any heating coil, with batch mode and throughput boosting; a trinium coil (9001 K) covers 9000 K, the tritanium coil (10 800 K) is for hotter recipes. Unverified: how many HIFs equal one ECR.
    - |-
      Why you want all three: trinium is the foil of every ZPM emitter and sensor (96 foil = 24 ingots each, zpm_components2) and of the trinium coil and trinium gears; enriched naquadah is the foil of the trinium coil block and the ZPM fusion/UV casings; naquadria is molten in the stargate ring and the later UV recipes (and a fusion ingredient: the double naquadria plate of the ZPM fusion reactor). Trinium is the real bottleneck: 6 naquadah dust per ingot.
    - |-
      Sub-steps people skip: (1) the zinc dust of the trinium recipe is CONSUMED (2 zinc sulfide come back), unlike the zinc catalyst in the PBI line; (2) hot ingots must go through the Vacuum Freezer with liquid helium (all three are above 5000 K); (3) each acid loop returns its own sulfuric acid, so pipe EBF outputs into the sulfuric acid drum; (4) keep Keep Exact 16 on the sulfate drawers, an EBF waiting for hydrogen blocks the loop; (5) the 20 raw naquadah per run of the destabiliser is only about a quarter of an ingot each: plan the nether star line for dozens of shards.
    - |-
      Unverified: the Centrifuge tier names (an IV Centrifuge for the 7680 EU/t centrifuges; the HV ones 480 EU/t), the hydrogen helium and sulfuric acid sources (earlier chains), and the exact yield of naquadah dust per raw naquadah ore.
  b:
    - ["gtceu:large_chemical_reactor", 1]
    - ["gtceu:iv_centrifuge", 2]
    - ["gtceu:hv_centrifuge", 2]
    - ["gtceu:hv_mixer", 2]
    - ["gtceu:electric_blast_furnace", 3]
    - ["gtceu:naquadah_coil_block", 16]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:distillation_tower", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:naquadah_dust", "gtceu:zinc_dust", "gtceu:fluoroantimonic_acid_bucket"]
      t: |-
        Drawers first: naquadah dust (Keep Exact 12), zinc dust. Drums: fluoroantimonic acid, sulfuric acid, hydrogen, liquid helium, and one drum per solution (impure enriched, impure naquadria, enriched, naquadria). Each machine on its own router or Pipez pipe, with a Robot Arm cover in Keep Exact mode on the output.
    - i:
        - gtceu:large_chemical_reactor
        - gtceu:titanium_trifluoride_dust
        - gtceu:impure_enriched_naquadah_solution_bucket
      t: |-
        Reactor: the Large Chemical Reactor on a LuV hatch takes 6 naquadah dust + 1 B fluoroantimonic acid and gives 2 B of each impure solution + 4 titanium trifluoride in 30 s. Two output hatches to two drums; the dust goes to the titanium line.
    - i: ["gtceu:iv_centrifuge", "gtceu:trinium_sulfide_dust", "gtceu:antimony_trifluoride_dust"]
      t: |-
        Two IV Centrifuges (IV power; the naquadria one is exactly 7680 EU/t): 4 B impure enriched → 3 trinium sulfide + 4 antimony trifluoride + 3 B enriched solution (40 s); 4 B impure naquadria → 2 indium phosphide + 1 trinium sulfide + 4 antimony trifluoride + 3 B naquadria solution (30 s). Sulfide into one drawer, antimony trifluoride back to the acid line.
    - i: ["gtceu:electric_blast_furnace", "gtceu:naquadah_coil_block", "gtceu:trinium_ingot"]
      t: |-
        Trinium EBF: 16 naquadah coil blocks (7200 K), a 4A hatch, circuit as the recipe wants, 2 trinium sulfide + 1 zinc dust → hot trinium in 37.5 s; then the Vacuum Freezer with liquid helium. The first ingots feed the trinium coils.
    - i: ["gtceu:hv_mixer", "gtceu:enriched_naquadah_sulfate_dust", "gtceu:enriched_naquadah_ingot"]
      t: |-
        Enriched: HV Mixer (1 B solution + 2 B sulfuric acid → 3 B acidic solution), HV Centrifuge (3 B → 2 B waste + 500 mB fluorine + 6 sulfate), then the 7000 K EBF with 2 B hydrogen → hot enriched ingot + 1 B acid. 7680 EU/t, 25 s.
    - i: ["gtceu:electric_blast_furnace", "gtceu:trinium_coil_block", "gtceu:naquadria_ingot"]
      t: |-
        Naquadria: same two steps, then an EBF with 16 trinium coil blocks (9001 K) and a 4A LuV or ZPM hatch for 122 880 EU/t: 6 naquadria sulfate + 2 B hydrogen → hot naquadria in 30 s, then the freezer.
    - i: ["functionalstorage:oak_1", "gtceu:trinium_ingot"]
      t: |-
        Easy to miss: loop the waste. A distillation tower takes the 2 B waste of each acid step and returns 250 mB of its own solution; without it you lose about 15 % of the line. Keep trinium for the coils first, only then spend it on foils.
---
# Naquadah products: 6 naquadah dust → 1 trinium + 1.5 enriched naquadah + 1.5 naquadria (centrifuges, acid loops, EBF 7000 / 7200 / 9000 K)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_naq_products` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Naquadah metals and ZPM coils](../../plan/p12.md#zpmmetals)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lc">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-c1" title="Centrifuge · 40 s · IV power · 4 B impure enriched solution (gtceu:iv_centrifuge) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 40 s · IV power · 4 B impure enriched solution</span><b class="gt-q">2 B</b></a><a class="gt-slot gt-mach" href="#m-c2" title="Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution (gtceu:iv_centrifuge) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution</span><b class="gt-q">2 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-iv" id="m-c1">
<div class="gt-head"><span class="gt-mname">Centrifuge · 40 s · IV power · 4 B impure enriched solution</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-lc" title="Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid</span><b class="gt-q">2 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Trinium sulfide dust (gtceu:trinium_sulfide_dust) - 3 per 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_sulfide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Sulfide Dust</span><b class="gt-q">3 per 4 B</b></span><a class="gt-slot gt-mach" href="#m-a1" title="HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate (gtceu:hv_mixer) - 3 B solution"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Mixer</span><span class="gt-note">HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate</span><b class="gt-q">3 B solution</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_centrifuge</code></div>
</div>
<div class="gt-panel t-iv" id="m-c2">
<div class="gt-head"><span class="gt-mname">Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-lc" title="Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid</span><b class="gt-q">2 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Trinium sulfide dust (gtceu:trinium_sulfide_dust) - 1 per 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_sulfide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Sulfide Dust</span><b class="gt-q">1 per 4 B</b></span><a class="gt-slot gt-mach" href="#m-a2" title="HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate (gtceu:hv_mixer) - 3 B solution"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Mixer</span><span class="gt-note">HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate</span><b class="gt-q">3 B solution</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:iv_centrifuge</code></div>
</div>
<div class="gt-panel t-hv" id="m-a1">
<div class="gt-head"><span class="gt-mname">HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-c1" title="Centrifuge · 40 s · IV power · 4 B impure enriched solution (gtceu:iv_centrifuge) - 3 B solution"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 40 s · IV power · 4 B impure enriched solution</span><b class="gt-q">3 B solution</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-e2" title="EBF 7000 K · 25 s · 7680 EU/t · 6 sulfate + 2 B hydrogen (gtceu:electric_blast_furnace) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 7000 K · 25 s · 7680 EU/t · 6 sulfate + 2 B hydrogen</span><b class="gt-q">6</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_mixer</code></div>
</div>
<div class="gt-panel t-hv" id="m-a2">
<div class="gt-head"><span class="gt-mname">HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-c2" title="Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution (gtceu:iv_centrifuge) - 3 B solution"><img class="gt-ico" src="../../assets/icons/gtceu__iv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Centrifuge</span><span class="gt-note">Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution</span><b class="gt-q">3 B solution</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-e3" title="EBF 9000 K (trinium coils) · 30 s · 122 880 EU/t · 6 sulfate + 2 B hydrogen (gtceu:electric_blast_furnace) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 9000 K (trinium coils) · 30 s · 122 880 EU/t · 6 sulfate + 2 B hydrogen</span><b class="gt-q">6</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF 7200 K · 37.5 s · 30 720 EU/t · 2 trinium sulfide + 1 zinc dust</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Trinium sulfide dust (gtceu:trinium_sulfide_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_sulfide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Sulfide Dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Trinium ingot (after the Vacuum Freezer) (gtceu:trinium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Ingot</span><span class="gt-note">Trinium ingot (after the Vacuum Freezer)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF 7000 K · 25 s · 7680 EU/t · 6 sulfate + 2 B hydrogen</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-a1" title="HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate (gtceu:hv_mixer) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Mixer</span><span class="gt-note">HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate</span><b class="gt-q">6</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Enriched naquadah ingot (gtceu:enriched_naquadah_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_naquadah_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Naquadah Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-e3">
<div class="gt-head"><span class="gt-mname">EBF 9000 K (trinium coils) · 30 s · 122 880 EU/t · 6 sulfate + 2 B hydrogen</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-a2" title="HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate (gtceu:hv_mixer) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Mixer</span><span class="gt-note">HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate</span><b class="gt-q">6</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Naquadria ingot (gtceu:naquadria_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__naquadria_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadria Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid](#m-lc) → [Centrifuge · 40 s · IV power · 4 B impure enriched solution](#m-c1) → [EBF 7200 K · 37.5 s · 30 720 EU/t · 2 trinium sulfide + 1 zinc dust](#m-e1) (also Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 naquadah dust + 1 B fluoroantimonic acid → [Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution](#m-c2), Centrifuge · 40 s · IV power · 4 B impure enriched solution → [HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate](#m-a1))
- [Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution](#m-c2) → [HV Mixer + HV Centrifuge · 1 B naquadria solution + 2 B sulfuric acid → 6 naquadria sulfate](#m-a2) → [EBF 9000 K (trinium coils) · 30 s · 122 880 EU/t · 6 sulfate + 2 B hydrogen](#m-e3) (also Centrifuge · 30 s · 7680 EU/t · 4 B impure naquadria solution → [EBF 7200 K · 37.5 s · 30 720 EU/t · 2 trinium sulfide + 1 zinc dust](#m-e1))
- [HV Mixer + HV Centrifuge · 1 B enriched solution + 2 B sulfuric acid → 6 enriched naquadah sulfate](#m-a1) → [EBF 7000 K · 25 s · 7680 EU/t · 6 sulfate + 2 B hydrogen](#m-e2)

## How to build

1. Drawers first: naquadah dust (Keep Exact 12), zinc dust. Drums: fluoroantimonic acid, sulfuric acid, hydrogen, liquid helium, and one drum per solution (impure enriched, impure naquadria, enriched, naquadria). Each machine on its own router or Pipez pipe, with a Robot Arm cover in Keep Exact mode on the output. — `functionalstorage:oak_1`, `gtceu:naquadah_dust`, `gtceu:zinc_dust`, `gtceu:fluoroantimonic_acid_bucket`
2. Reactor: the Large Chemical Reactor on a LuV hatch takes 6 naquadah dust + 1 B fluoroantimonic acid and gives 2 B of each impure solution + 4 titanium trifluoride in 30 s. Two output hatches to two drums; the dust goes to the titanium line. — `gtceu:large_chemical_reactor`, `gtceu:titanium_trifluoride_dust`, `gtceu:impure_enriched_naquadah_solution_bucket`
3. Two IV Centrifuges (IV power; the naquadria one is exactly 7680 EU/t): 4 B impure enriched → 3 trinium sulfide + 4 antimony trifluoride + 3 B enriched solution (40 s); 4 B impure naquadria → 2 indium phosphide + 1 trinium sulfide + 4 antimony trifluoride + 3 B naquadria solution (30 s). Sulfide into one drawer, antimony trifluoride back to the acid line. — `gtceu:iv_centrifuge`, `gtceu:trinium_sulfide_dust`, `gtceu:antimony_trifluoride_dust`
4. Trinium EBF: 16 naquadah coil blocks (7200 K), a 4A hatch, circuit as the recipe wants, 2 trinium sulfide + 1 zinc dust → hot trinium in 37.5 s; then the Vacuum Freezer with liquid helium. The first ingots feed the trinium coils. — `gtceu:electric_blast_furnace`, `gtceu:naquadah_coil_block`, `gtceu:trinium_ingot`
5. Enriched: HV Mixer (1 B solution + 2 B sulfuric acid → 3 B acidic solution), HV Centrifuge (3 B → 2 B waste + 500 mB fluorine + 6 sulfate), then the 7000 K EBF with 2 B hydrogen → hot enriched ingot + 1 B acid. 7680 EU/t, 25 s. — `gtceu:hv_mixer`, `gtceu:enriched_naquadah_sulfate_dust`, `gtceu:enriched_naquadah_ingot`
6. Naquadria: same two steps, then an EBF with 16 trinium coil blocks (9001 K) and a 4A LuV or ZPM hatch for 122 880 EU/t: 6 naquadria sulfate + 2 B hydrogen → hot naquadria in 30 s, then the freezer. — `gtceu:electric_blast_furnace`, `gtceu:trinium_coil_block`, `gtceu:naquadria_ingot`
7. Easy to miss: loop the waste. A distillation tower takes the 2 B waste of each acid step and returns 250 mB of its own solution; without it you lose about 15 % of the line. Keep trinium for the coils first, only then spend it on foils. — `functionalstorage:oak_1`, `gtceu:trinium_ingot`

## Tips

- The base line is in the naquadah chain (naquadah dust → 6 dust + 1 B fluoroantimonic acid → 2 B impure enriched + 2 B impure naquadria + 4 titanium trifluoride, Large Chemical Reactor 600 ticks at 30 720 EU/t, NaquadahRecipes naquadah\_separation). This chain is what happens next. Pack change (kjs additions/recipe\_changes.js, ‘naquadah changes’): the impure-solution centrifuges are replaced: 4 B impure enriched naquadah solution → 3 trinium sulfide + 4 antimony trifluoride + 3 B enriched naquadah solution, 800 ticks, VHA\[IV\]; 4 B impure naquadria solution → 2 indium phosphide + 1 trinium sulfide + 4 antimony trifluoride + 3 B naquadria solution, 600 ticks, VA\[IV\].
- Yield (derived from those recipes and cross-checked with the Chemical Plant skip, which gives 12 naquadah → 3 enriched + 3 naquadria + 2 trinium): 6 naquadah dust give 2 B + 2 B impure solution, i.e. 1.5 + 0.5 trinium sulfide = 2 sulfide = 1 trinium ingot, 1.5 B enriched solution and 1.5 B naquadria solution = 1.5 enriched naquadah ingots + 1.5 naquadria ingots, before the waste loops add a little more. The antimony trifluoride goes back into the fluoroantimonic acid line (4 antimony trifluoride + 4 B hydrofluoric acid → 1 B acid + 2 B hydrogen, 300 ticks, 480 EU/t), the indium phosphide into the indium line, the titanium trifluoride into titanium.
- Acid loops (NaquadahRecipes, not changed by the pack): enriched: Mixer (HV, 100 ticks, 480 EU/t) 1 B solution + 2 B sulfuric acid → 3 B acidic solution; Centrifuge (HV, 100 ticks, 480 EU/t) 3 B acidic → 2 B waste + 500 mB fluorine + 6 enriched naquadah sulfate; EBF 7000 K, 500 ticks at 7680 EU/t: 6 sulfate + 2 B hydrogen → hot enriched naquadah ingot + 1 B sulfuric acid (freezer: 150 ticks at 2048, liquid helium above 5000 K). Naquadria is the same with the sulfate EBF at 9000 K, 600 ticks, VA\[ZPM\] = 122 880 EU/t (freezer 200 ticks at VA\[LuV\]). The waste loop: distillation tower 2 B waste → 50 % barium sulfide (enriched) or gallium sulfide (naquadria) + 500 mB sulfuric acid + 250 mB own solution + 100 mB of the other solution, 300 ticks at 480 EU/t.
- Trinium: EBF 7200 K, EUt VA\[LuV\] = 30 720, 750 ticks: 2 trinium sulfide + 1 zinc dust → hot trinium ingot + 2 zinc sulfide (the zinc sulfide goes to the zinc loop); freezer 300 ticks at VA\[IV\] (ElementMaterials trinium: 7200 K, vacuum VA\[IV\] 300). 7200 K is exactly a NAQUADAH coil; so the first trinium needs naquadah coils (zpm\_coils), which only need naquadah, not trinium. Naquadria needs 9000 K = TRINIUM coils (9001 K): the coils are made from trinium double wire, so the first naquadria comes only after the first 16 trinium ingots.
- Power: the 9000 K recipe is 122 880 EU/t: an EBF on a LuV 4A hatch (4 x 32 768) or a ZPM hatch. The 7200 K and 7000 K ones fit a 4A IV hatch (30 720) and an IV hatch (7680). One EBF per recipe, each with its own coils: a single furnace cannot switch between 7000 K, 7200 K and 9000 K runs when circuit and hatch must differ.
- Machines (verified): naquadah\_separation is a Large Chemical Reactor recipe (LuV, 600 ticks). The LCR runs it with perfect overclock and NO parallel hatch; the Extreme Chemical Reactor (ECR) is the multi that accepts a parallel hatch (non-perfect overclock, batch mode), so scale this line with an ECR. The last step (naquadria sulfate, 9000 K, VA\[ZPM\], 600 ticks) can run in the Hardened Industrial Furnace \[HIF, gtceu:super\_ebf\]: it takes ONE energy hatch and any heating coil, with batch mode and throughput boosting; a trinium coil (9001 K) covers 9000 K, the tritanium coil (10 800 K) is for hotter recipes. Unverified: how many HIFs equal one ECR.
- Why you want all three: trinium is the foil of every ZPM emitter and sensor (96 foil = 24 ingots each, zpm\_components2) and of the trinium coil and trinium gears; enriched naquadah is the foil of the trinium coil block and the ZPM fusion/UV casings; naquadria is molten in the stargate ring and the later UV recipes (and a fusion ingredient: the double naquadria plate of the ZPM fusion reactor). Trinium is the real bottleneck: 6 naquadah dust per ingot.
- Sub-steps people skip: (1) the zinc dust of the trinium recipe is CONSUMED (2 zinc sulfide come back), unlike the zinc catalyst in the PBI line; (2) hot ingots must go through the Vacuum Freezer with liquid helium (all three are above 5000 K); (3) each acid loop returns its own sulfuric acid, so pipe EBF outputs into the sulfuric acid drum; (4) keep Keep Exact 16 on the sulfate drawers, an EBF waiting for hydrogen blocks the loop; (5) the 20 raw naquadah per run of the destabiliser is only about a quarter of an ingot each: plan the nether star line for dozens of shards.
- **Unverified** the Centrifuge tier names (an IV Centrifuge for the 7680 EU/t centrifuges; the HV ones 480 EU/t), the hydrogen helium and sulfuric acid sources (earlier chains), and the exact yield of naquadah dust per raw naquadah ore.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 1 |
| `gtceu:iv_centrifuge` | 2 |
| `gtceu:hv_centrifuge` | 2 |
| `gtceu:hv_mixer` | 2 |
| `gtceu:electric_blast_furnace` | 3 |
| `gtceu:naquadah_coil_block` | 16 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:distillation_tower` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:trinium_ingot`, `gtceu:trinium_sulfide_dust`, `gtceu:enriched_naquadah_ingot`, `gtceu:naquadria_ingot`, `gtceu:trinium_foil`, `gtceu:trinium_dust`
