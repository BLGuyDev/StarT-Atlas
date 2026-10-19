---
kind: chain
id: uhv_akreyrium
order: 1900
data:
  t: |-
    Akreyrium refining: gritty → lepton sparse (sifter) → electron / muon / tau sparse (manifold centrifuge) → dense (catalyst injection) → utopian akreyrium (folding stabiliser)
  inf: true
  "n":
    - - gk
      - |-
        100 B gritty akreyrium · 1 netherite reinforced mesh (50 % kept)
      - g
      - functionalstorage:oak_1
      - - [Gritty akreyrium, "gtceu:gritty_akreyrium_bucket"]
        - [Netherite reinforced mesh, "kubejs:netherite_reinforced_mesh"]
    - - sf
      - Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium
      - m
      - gtceu:cyclonic_sifter
    - - mc
      - Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 %
      - m
      - gtceu:manifold_centrifuge
    - - ff
      - Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux
      - m
      - gtceu:injection_mixer
    - - b1
      - |-
        Tau branch: mercury → light, superlight, heavy, superheavy flux → 5 B ethereal flux (6 machines)
      - x
      - kubejs:tau_injection_catalyst
    - - b2
      - |-
        Muon branch: glowstone, lava, blaze, lumium → 4 B brilliant flux (5 machines)
      - x
      - kubejs:muon_injection_catalyst
    - - b3
      - |-
        Electron branch: electrum → agent dust phases → alternating phase flux (8 machines)
      - x
      - kubejs:electron_injection_catalyst
    - - cn
      - Canner (LuV) · 125 mB flux + blank injection catalyst → tau / muon / electron catalyst
      - m
      - gtceu:luv_canner
    - - ij
      - Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst
      - m
      - gtceu:injection_mixer
    - - wa
      - Assembler · 18 s · 491 520 EU/t · damaged catalyst + 80 mB neutronium → blank catalyst
      - m
      - gtceu:large_assembler
    - - fs
      - Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy
      - m
      - gtceu:folding_akreyrium_stabiliser
    - [ut, Utopian akreyrium, o, "gtceu:utopian_akreyrium_bucket"]
  e:
    - [gk, sf, "100 B"]
    - [sf, mc, "1 B"]
    - [sf, ff, amorphous]
    - [ff, b1, flux]
    - [ff, b2, flux]
    - [ff, b3, flux]
    - [b1, cn, "125 mB"]
    - [b2, cn, "125 mB"]
    - [b3, cn, "125 mB"]
    - [cn, ij, catalyst]
    - [mc, ij, sparse X 1 B]
    - [ij, wa, damaged]
    - [ij, fs, dense X 1 B]
    - [fs, ut, "500 mB"]
  tips:
    - |-
      Source: kjs abydos_lines/akreyrium.js (verified). Sifter (UHV power): 100 B gritty akreyrium + netherite reinforced mesh (chance 500, -50) → 1 B lepton sparse akreyrium + 1 crystalline akreyrium + 1 amorphous akreyrium, 1200 ticks at VA[UHV] x 0.8. Manifold Centrifuge: 1 B lepton sparse → chanced 1 B sparse electron (20 %), muon (40 %), tau (40 %), 1200 ticks at VA[UHV]. Note the huge ratio: 100 B gritty per B of sparse.
    - |-
      Catalysts: blank injection catalyst (assembler in a cleanroom, 800 ticks, VA[UHV]): 1 petri dish + 2 UHV microfluidic flow valves + 32 neutronium foil + 12 UHV high strength panels + 8 neutronium screws + 512 mB PEEK. TAU: mixer mercury 3850 + 1 B foundational flux → light tau flux; distillation tower (UV) → 800 superlight + 200 heavy + 1 aspect of weight; brewery superlight + aspect → 500 heavy; injection mixer heavy + aspect + osmiridium → superheavy; mixer 2 B superheavy + 2 B superlight + aspect → 5 B ethereal tau flux; canner 125 mB. MUON: foundational flux + glowstone 512 → twinkling; + 1 B lava → glowing; + 288 mB blaze → shining; + 288 mB lumium → radiant; injection mixer all four → 4 B brilliant; canner 125 mB. ELECTRON: flux + electrum 512 → mono-phase; distillation → di-phase dust + 864 mB coalescing superalloy; polarizers and separator give 10 gamma + 5 beta + 1 alpha dust, gamma + annealed copper dust, beta + sterling silver dust, polarize up to alpha; injection mixer 16 alpha dust + 864 mB superalloy → 1 B alternating phase flux; canner 125 mB.
    - |-
      Injection (mixer, VHA[UHV]): sparse X + the matching catalyst → 1 B dense X (the other two types give only 200 mB), 200 ticks, the catalyst becomes damaged and is washed with 80 mB neutronium (assembler, 360 ticks, VA[UV]). Stabilisation (folding stabiliser, UHV hull recipe in uhv_multis): 1 B dense electron / muon / tau + 1 crystalline akreyrium + a magenta / lime / light blue glass lens (not consumed) → 500 mB utopian akreyrium + 90 mB coalescing superalloy, 200 ticks at VHA[UHV]; the lepton route (lepton flux + gray lens) gives only 10 mB but returns 720 mB superalloy.
    - |-
      Coalescing superalloy: mixer 4 thallium tungstate + 2 nickel + 4 graphene + 3 niobium + 4 bismuth dust → 17 lepton coalescing superalloy dust (600 ticks, VA[LuV]), then molten; thallium tungstate = LCR 2 thallium + 4 tungsten trioxide + 1 B oxygen → 7 dust (800 ticks, VHA[LuV]); the folding stabiliser returns it, so it is a loop with small losses. UEV page: the abyssal stabiliser turns lepton dense akreyrium into more utopian.
    - |-
      Branches (verified): every dense branch gives 500 mB utopian akreyrium per 1000 mB (+ 90 mB superalloy), so the electron line is a real source of utopian too; its exclusive job is the leptonic catalyst (100 electron + 200 muon + 200 tau dense + crystalline) -> lepton dense akreyrium -> Abyssal Akreyriadix Stabiliser (VHA[UIV] = 15 728 640 EU/t) -> lepton resonant thallium antimonide, which only UIV items consume. Power by step: magma sifter and Molten Destabiliser are UV (uv_magma); this line needs UHV power (manifold centrifuge 1 966 080 EU/t, injection mixers and the Folding Akreyrium Stabiliser 983 040 EU/t), plus the one UIV step.
    - |-
      Utopian akreyrium is the fuel and ingredient of everything after: the runic circuits (via the infusion), the Manifold Centrifuge / Injection Mixer controllers (1250 mB each), the bulk ore array (750 mB), the IHPCA (576 mB), the Component Nexus (1000 mB), the nanofluidic heat sink coolant (2000 mB). 500 mB per run means hundreds of sifter cycles of the gritty vein.
    - |-
      Sub-steps people skip: (1) the catalysts are NOT consumed on use: they turn damaged and must be washed (80 mB neutronium each time); keep 3 catalysts of each type in rotation; (2) the lens stays in the stabiliser and is returned as an item output: keep it in an output bus; (3) distillation tower with UV power for the tau branch; (4) one machine per branch step: 19 machines in total.
    - |-
      Unverified: the real throughput per gritty vein, aspect of weight origin (kubejs:aspect_of_weight), mercury and blaze fluid sources.
  b:
    - ["gtceu:cyclonic_sifter", 1]
    - ["gtceu:manifold_centrifuge", 1]
    - ["gtceu:injection_mixer", 2]
    - ["gtceu:folding_akreyrium_stabiliser", 1]
    - ["gtceu:luv_canner", 1]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:uhv_energy_input_hatch_4a", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 18]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 16]
    - ["gtceu:steel_drum", 20]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:netherite_reinforced_mesh
        - kubejs:blank_injection_catalyst
        - gtceu:gray_glass_lens
      t: |-
        Drawers first: meshes, blank / three kinds of / damaged catalysts, the four lenses (gray, magenta, lime, light blue), crystalline akreyrium, amorphous akreyrium, osmiridium dust, aspect of weight, agent dusts. Drums: gritty / lepton sparse / three sparse / three dense / utopian akreyrium, superalloy, every flux, mercury, glowstone, lava, blaze, lumium, electrum.
    - i: ["gtceu:cyclonic_sifter", "gtceu:manifold_centrifuge"]
      t: Sifter then centrifuge on UHV power; separate output hatches for the three sparse types into drums.
    - i: ["gtceu:injection_mixer", "kubejs:amorphous_akreyrium"]
      t: Foundational flux first (amorphous + superalloy), then three catalyst branches each with its own drums; canner into blank catalysts.
    - i: ["gtceu:injection_mixer", "kubejs:tau_injection_catalyst"]
      t: |-
        Injection mixer: sparse X + catalyst by router (Keep Exact 1); damaged catalysts back to the washing assembler.
    - i: ["gtceu:folding_akreyrium_stabiliser", "gtceu:utopian_akreyrium_bucket"]
      t: |-
        Folding stabiliser: dense X + crystalline akreyrium + the lens in the lens slot; utopian akreyrium to a drum.
    - i: ["functionalstorage:oak_1", "gtceu:utopian_akreyrium_bucket"]
      t: |-
        Easy to miss: crystalline akreyrium is consumed 1 per run and comes only from the sifter: it is the pacing item.
---
# Akreyrium refining: gritty → lepton sparse (sifter) → electron / muon / tau sparse (manifold centrifuge) → dense (catalyst injection) → utopian akreyrium (folding stabiliser)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_akreyrium` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Akreyrium refining, UHV controllers](../../plan/p17.md#uhvmulti)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-sf">
<div class="gt-head"><span class="gt-mname">Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="100 B gritty akreyrium · 1 netherite reinforced mesh (50 % kept) (functionalstorage:oak_1) - 100 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">100 B gritty akreyrium · 1 netherite reinforced mesh (50 % kept)</span><span class="gt-sub"><span>Gritty akreyrium</span><span>Netherite reinforced mesh</span></span><b class="gt-q">100 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-mc" title="Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 % (gtceu:manifold_centrifuge) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__manifold_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Manifold Centrifuge</span><span class="gt-note">Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 %</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-ff" title="Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux (gtceu:injection_mixer) - amorphous"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Injection Mixer</span><span class="gt-note">Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux</span><b class="gt-q">amorphous</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:cyclonic_sifter</code></div>
</div>
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 %</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-sf" title="Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium (gtceu:cyclonic_sifter) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cyclonic Sifter</span><span class="gt-note">Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__manifold_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ij" title="Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst (gtceu:injection_mixer) - sparse X 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Injection Mixer</span><span class="gt-note">Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst</span><b class="gt-q">sparse X 1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:manifold_centrifuge</code></div>
</div>
<div class="gt-panel t-mod" id="m-ff">
<div class="gt-head"><span class="gt-mname">Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-sf" title="Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium (gtceu:cyclonic_sifter) - amorphous"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cyclonic Sifter</span><span class="gt-note">Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium</span><b class="gt-q">amorphous</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Tau branch: mercury → light, superlight, heavy, superheavy flux → 5 B ethereal flux (6 machines) (kubejs:tau_injection_catalyst) - flux"><img class="gt-ico" src="../../assets/icons/kubejs__tau_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tau Injection Catalyst</span><span class="gt-note">Tau branch: mercury → light, superlight, heavy, superheavy flux → 5 B ethereal flux (6 machines)</span><b class="gt-q">flux</b></span><span class="gt-slot" title="Muon branch: glowstone, lava, blaze, lumium → 4 B brilliant flux (5 machines) (kubejs:muon_injection_catalyst) - flux"><img class="gt-ico" src="../../assets/icons/kubejs__muon_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Muon Injection Catalyst</span><span class="gt-note">Muon branch: glowstone, lava, blaze, lumium → 4 B brilliant flux (5 machines)</span><b class="gt-q">flux</b></span><span class="gt-slot" title="Electron branch: electrum → agent dust phases → alternating phase flux (8 machines) (kubejs:electron_injection_catalyst) - flux"><img class="gt-ico" src="../../assets/icons/kubejs__electron_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electron Injection Catalyst</span><span class="gt-note">Electron branch: electrum → agent dust phases → alternating phase flux (8 machines)</span><b class="gt-q">flux</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:injection_mixer</code></div>
</div>
<div class="gt-panel t-luv" id="m-cn">
<div class="gt-head"><span class="gt-mname">Canner (LuV) · 125 mB flux + blank injection catalyst → tau / muon / electron catalyst</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Tau branch: mercury → light, superlight, heavy, superheavy flux → 5 B ethereal flux (6 machines) (kubejs:tau_injection_catalyst) - 125 mB"><img class="gt-ico" src="../../assets/icons/kubejs__tau_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tau Injection Catalyst</span><span class="gt-note">Tau branch: mercury → light, superlight, heavy, superheavy flux → 5 B ethereal flux (6 machines)</span><b class="gt-q">125 mB</b></span><span class="gt-slot" title="Muon branch: glowstone, lava, blaze, lumium → 4 B brilliant flux (5 machines) (kubejs:muon_injection_catalyst) - 125 mB"><img class="gt-ico" src="../../assets/icons/kubejs__muon_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Muon Injection Catalyst</span><span class="gt-note">Muon branch: glowstone, lava, blaze, lumium → 4 B brilliant flux (5 machines)</span><b class="gt-q">125 mB</b></span><span class="gt-slot" title="Electron branch: electrum → agent dust phases → alternating phase flux (8 machines) (kubejs:electron_injection_catalyst) - 125 mB"><img class="gt-ico" src="../../assets/icons/kubejs__electron_injection_catalyst.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electron Injection Catalyst</span><span class="gt-note">Electron branch: electrum → agent dust phases → alternating phase flux (8 machines)</span><b class="gt-q">125 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_canner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ij" title="Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst (gtceu:injection_mixer) - catalyst"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Injection Mixer</span><span class="gt-note">Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst</span><b class="gt-q">catalyst</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:luv_canner</code></div>
</div>
<div class="gt-panel t-mod" id="m-ij">
<div class="gt-head"><span class="gt-mname">Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-cn" title="Canner (LuV) · 125 mB flux + blank injection catalyst → tau / muon / electron catalyst (gtceu:luv_canner) - catalyst"><img class="gt-ico" src="../../assets/icons/gtceu__luv_canner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Canner</span><span class="gt-note">Canner (LuV) · 125 mB flux + blank injection catalyst → tau / muon / electron catalyst</span><b class="gt-q">catalyst</b></a><a class="gt-slot gt-mach" href="#m-mc" title="Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 % (gtceu:manifold_centrifuge) - sparse X 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__manifold_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Manifold Centrifuge</span><span class="gt-note">Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 %</span><b class="gt-q">sparse X 1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-wa" title="Assembler · 18 s · 491 520 EU/t · damaged catalyst + 80 mB neutronium → blank catalyst (gtceu:large_assembler) - damaged"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Assembler</span><span class="gt-note">Assembler · 18 s · 491 520 EU/t · damaged catalyst + 80 mB neutronium → blank catalyst</span><b class="gt-q">damaged</b></a><a class="gt-slot gt-mach" href="#m-fs" title="Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy (gtceu:folding_akreyrium_stabiliser) - dense X 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__folding_akreyrium_stabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Folding Akreyrium Stabiliser</span><span class="gt-note">Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy</span><b class="gt-q">dense X 1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:injection_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-wa">
<div class="gt-head"><span class="gt-mname">Assembler · 18 s · 491 520 EU/t · damaged catalyst + 80 mB neutronium → blank catalyst</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ij" title="Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst (gtceu:injection_mixer) - damaged"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Injection Mixer</span><span class="gt-note">Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst</span><b class="gt-q">damaged</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-fs">
<div class="gt-head"><span class="gt-mname">Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ij" title="Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst (gtceu:injection_mixer) - dense X 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__injection_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Injection Mixer</span><span class="gt-note">Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst</span><b class="gt-q">dense X 1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__folding_akreyrium_stabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Utopian akreyrium (gtceu:utopian_akreyrium_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__utopian_akreyrium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Utopian Akreyrium Bucket</span><b class="gt-q">500 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:folding_akreyrium_stabiliser</code></div>
</div>
</div>

## Flow

- [Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium](#m-sf) → [Manifold Centrifuge · 60 s · 1 966 080 EU/t → sparse electron 20 % / muon 40 % / tau 40 %](#m-mc) → [Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst](#m-ij) → [Assembler · 18 s · 491 520 EU/t · damaged catalyst + 80 mB neutronium → blank catalyst](#m-wa) (also Cyclonic Sifter · 60 s · 1 572 864 EU/t → 1 B lepton sparse + crystalline + amorphous akreyrium → [Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux](#m-ff), Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst → [Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy](#m-fs))
- [Injection Mixer · 8 s · 491 520 EU/t · amorphous + 864 mB coalescing superalloy → 1 B foundational flux](#m-ff) → [Canner (LuV) · 125 mB flux + blank injection catalyst → tau / muon / electron catalyst](#m-cn) → [Injection Mixer · 10 s · 983 040 EU/t · sparse X + catalyst → dense X (1 B same type, 200 mB others) + damaged catalyst](#m-ij)
- [Folding Akreyrium Stabiliser · 10 s · 983 040 EU/t · 1 B dense X + crystalline + colour lens → 500 mB utopian akreyrium + 90 mB superalloy](#m-fs)

## How to build

1. Drawers first: meshes, blank / three kinds of / damaged catalysts, the four lenses (gray, magenta, lime, light blue), crystalline akreyrium, amorphous akreyrium, osmiridium dust, aspect of weight, agent dusts. Drums: gritty / lepton sparse / three sparse / three dense / utopian akreyrium, superalloy, every flux, mercury, glowstone, lava, blaze, lumium, electrum. — `functionalstorage:oak_1`, `kubejs:netherite_reinforced_mesh`, `kubejs:blank_injection_catalyst`, `gtceu:gray_glass_lens`
2. Sifter then centrifuge on UHV power; separate output hatches for the three sparse types into drums. — `gtceu:cyclonic_sifter`, `gtceu:manifold_centrifuge`
3. Foundational flux first (amorphous + superalloy), then three catalyst branches each with its own drums; canner into blank catalysts. — `gtceu:injection_mixer`, `kubejs:amorphous_akreyrium`
4. Injection mixer: sparse X + catalyst by router (Keep Exact 1); damaged catalysts back to the washing assembler. — `gtceu:injection_mixer`, `kubejs:tau_injection_catalyst`
5. Folding stabiliser: dense X + crystalline akreyrium + the lens in the lens slot; utopian akreyrium to a drum. — `gtceu:folding_akreyrium_stabiliser`, `gtceu:utopian_akreyrium_bucket`
6. Easy to miss: crystalline akreyrium is consumed 1 per run and comes only from the sifter: it is the pacing item. — `functionalstorage:oak_1`, `gtceu:utopian_akreyrium_bucket`

## Tips

- Source: kjs abydos\_lines/akreyrium.js (verified). Sifter (UHV power): 100 B gritty akreyrium + netherite reinforced mesh (chance 500, -50) → 1 B lepton sparse akreyrium + 1 crystalline akreyrium + 1 amorphous akreyrium, 1200 ticks at VA\[UHV\] x 0.8. Manifold Centrifuge: 1 B lepton sparse → chanced 1 B sparse electron (20 %), muon (40 %), tau (40 %), 1200 ticks at VA\[UHV\]. Note the huge ratio: 100 B gritty per B of sparse.
- Catalysts: blank injection catalyst (assembler in a cleanroom, 800 ticks, VA\[UHV\]): 1 petri dish + 2 UHV microfluidic flow valves + 32 neutronium foil + 12 UHV high strength panels + 8 neutronium screws + 512 mB PEEK. TAU: mixer mercury 3850 + 1 B foundational flux → light tau flux; distillation tower (UV) → 800 superlight + 200 heavy + 1 aspect of weight; brewery superlight + aspect → 500 heavy; injection mixer heavy + aspect + osmiridium → superheavy; mixer 2 B superheavy + 2 B superlight + aspect → 5 B ethereal tau flux; canner 125 mB. MUON: foundational flux + glowstone 512 → twinkling; + 1 B lava → glowing; + 288 mB blaze → shining; + 288 mB lumium → radiant; injection mixer all four → 4 B brilliant; canner 125 mB. ELECTRON: flux + electrum 512 → mono-phase; distillation → di-phase dust + 864 mB coalescing superalloy; polarizers and separator give 10 gamma + 5 beta + 1 alpha dust, gamma + annealed copper dust, beta + sterling silver dust, polarize up to alpha; injection mixer 16 alpha dust + 864 mB superalloy → 1 B alternating phase flux; canner 125 mB.
- Injection (mixer, VHA\[UHV\]): sparse X + the matching catalyst → 1 B dense X (the other two types give only 200 mB), 200 ticks, the catalyst becomes damaged and is washed with 80 mB neutronium (assembler, 360 ticks, VA\[UV\]). Stabilisation (folding stabiliser, UHV hull recipe in uhv\_multis): 1 B dense electron / muon / tau + 1 crystalline akreyrium + a magenta / lime / light blue glass lens (not consumed) → 500 mB utopian akreyrium + 90 mB coalescing superalloy, 200 ticks at VHA\[UHV\]; the lepton route (lepton flux + gray lens) gives only 10 mB but returns 720 mB superalloy.
- Coalescing superalloy: mixer 4 thallium tungstate + 2 nickel + 4 graphene + 3 niobium + 4 bismuth dust → 17 lepton coalescing superalloy dust (600 ticks, VA\[LuV\]), then molten; thallium tungstate = LCR 2 thallium + 4 tungsten trioxide + 1 B oxygen → 7 dust (800 ticks, VHA\[LuV\]); the folding stabiliser returns it, so it is a loop with small losses. UEV page: the abyssal stabiliser turns lepton dense akreyrium into more utopian.
- Branches (verified): every dense branch gives 500 mB utopian akreyrium per 1000 mB (+ 90 mB superalloy), so the electron line is a real source of utopian too; its exclusive job is the leptonic catalyst (100 electron + 200 muon + 200 tau dense + crystalline) -&gt; lepton dense akreyrium -&gt; Abyssal Akreyriadix Stabiliser (VHA\[UIV\] = 15 728 640 EU/t) -&gt; lepton resonant thallium antimonide, which only UIV items consume. Power by step: magma sifter and Molten Destabiliser are UV (uv\_magma); this line needs UHV power (manifold centrifuge 1 966 080 EU/t, injection mixers and the Folding Akreyrium Stabiliser 983 040 EU/t), plus the one UIV step.
- Utopian akreyrium is the fuel and ingredient of everything after: the runic circuits (via the infusion), the Manifold Centrifuge / Injection Mixer controllers (1250 mB each), the bulk ore array (750 mB), the IHPCA (576 mB), the Component Nexus (1000 mB), the nanofluidic heat sink coolant (2000 mB). 500 mB per run means hundreds of sifter cycles of the gritty vein.
- Sub-steps people skip: (1) the catalysts are NOT consumed on use: they turn damaged and must be washed (80 mB neutronium each time); keep 3 catalysts of each type in rotation; (2) the lens stays in the stabiliser and is returned as an item output: keep it in an output bus; (3) distillation tower with UV power for the tau branch; (4) one machine per branch step: 19 machines in total.
- **Unverified** the real throughput per gritty vein, aspect of weight origin (kubejs:aspect\_of\_weight), mercury and blaze fluid sources.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:cyclonic_sifter` | 1 |
| `gtceu:manifold_centrifuge` | 1 |
| `gtceu:injection_mixer` | 2 |
| `gtceu:folding_akreyrium_stabiliser` | 1 |
| `gtceu:luv_canner` | 1 |
| `gtceu:large_assembler` | 1 |
| `gtceu:uhv_energy_input_hatch_4a` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 18 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 16 |
| `gtceu:steel_drum` | 20 |

## Needs / Feeds

- **Main source for:** `gtceu:utopian_akreyrium_bucket`, `kubejs:crystalline_akreyrium`, `kubejs:amorphous_akreyrium`, `kubejs:blank_injection_catalyst`, `kubejs:tau_injection_catalyst`, `kubejs:muon_injection_catalyst`, `kubejs:electron_injection_catalyst`
