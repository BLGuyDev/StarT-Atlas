---
kind: chain
id: uev_nether
order: 2130
data:
  t: |-
    Nether magma line: highly unstable nether magma → mystical magma → mythrillic, adamantamite and estaltadyne dusts (start of mythril, adamantine and estalt)
  inf: true
  "n":
    - - v
      - |-
        Fluid vein in the Nether: highly unstable nether magma (weight 15, 960 to 1280 yield)
      - s
      - start_core:zpm_fluid_drilling_rig
    - - cs
      - Cyclonic Sifter · 200 B + 1 ancient netherite reinforced mesh (chance) · 67.5 s · 2.1 M EU/t
      - m
      - gtceu:cyclonic_sifter
    - [mm, "12 B mystical nether magma + 3 deactivated nether dust", f, "gtceu:mystical_nether_magma_bucket"]
    - [md, "Molten Destabiliser · 3 B → 1 B of each · 24 s · 0.59 M EU/t", m, "gtceu:molten_destabiliser"]
    - - nm
      - Mythrillic, adamantamite and estaltadyne nether magma (1 B each)
      - f
      - gtceu:mythrillic_nether_magma_bucket
    - - mc
      - Manifold Centrifuge · 9 B → 6 B molten mixture + 2 B enriched + 1 B mystical · 60 s · 0.98 M EU/t
      - m
      - gtceu:manifold_centrifuge
    - - mx
      - Molten mythrillic, adamantamite or estaltadyne mixture (6 B)
      - f
      - gtceu:molten_mythrillic_mixture_bucket
    - - dd
      - Molten Destabiliser · 300 B mixture → 200 B pure fluid + magma + ore mixture + 32 netherrack dust · 180 s · UV
      - m
      - gtceu:molten_destabiliser
    - [pf, "200 B mythrillic, adamantamite or estaltadyne", f, "gtceu:mythrillic_bucket"]
    - [el, "UHV Electrolyzer · 1 B → dust + small dust + 250 mB mystical magma · 7 s", m, "gtceu:uhv_electrolyzer"]
    - [du, "Mythrillic, adamantamite and estaltadyne dust", o, "gtceu:mythrillic_dust"]
  e:
    - [v, cs, "200 B"]
    - [cs, mm, "12 B"]
    - [mm, md, "3 B"]
    - [md, nm, "1 B each"]
    - [nm, mc, "9 B"]
    - [mc, mx, "6 B"]
    - [mx, dd, "300 B"]
    - [dd, pf, "200 B"]
    - [pf, el, "1 B"]
    - [el, du, "1 + 1 small"]
  tips:
    - |-
      Source: kjs additions/progression/lines/nether_lines/{magmas,mythril,adamantine,estalt}.js and utils/fluid_veins.js. Vein: start:highly_unstable_nether_magma_deposit in the Nether (weight 15, yield 960 to 1280, depletes 2 per 1 chance, floor 720). Cyclonic Sifter: 200 000 mB highly unstable nether magma + 1 ancient netherite reinforced mesh (chanced input 1000 of 10 000, boost -150) → 12 000 mB mystical nether magma + 3 deactivated nether dust + 2 small + 1 tiny, 1350 ticks, VA[UEV] x 3 / 11 = 2 144 814 EU/t. Molten Destabiliser: 3 000 mB mystical → 1 000 mB each of estaltadyne, adamantamite and mythrillic nether magma, 480 ticks, VHA[UHV] x 3 / 5 = 589 824 EU/t.
    - |-
      Manifold Centrifuge (VHA[UHV], 1200 ticks): 9 000 mB of each nether magma → 6 000 mB molten mixture + 2 000 mB enriched mixture + 1 000 mB mystical magma back. Molten Destabiliser (VHA[UV], 3600 ticks): 300 000 mB molten mixture → 200 000 mB pure fluid + 25 000 mB (50 000 for estaltadyne) highly unstable nether magma + 75 000 mB (50 000) molten ore mixture + 32 netherrack dust: the magma comes back, so the line is a loop that only loses to the mesh and the ore mixture. Electrolyzer (VHA[UHV], 140 ticks): 1000 mB pure fluid → dust + small dust + 250 mB mystical magma.
    - |-
      Side loops: the enriched mixtures + activated nether dust (polarizer on deactivated dust, 360 ticks) go through a heat chamber into atomic nether sludge dust, which a UEV Manifold Centrifuge with hexafluorobromic acid splits into flerovium-, hafnium- and polonium-rich sludges (flerovium, hafnium, seaborgium, polonium and astatine lines in atomic_nether_sludge.js; the alloys uev_alloys and fusion use flerovium, seaborgium and astatine). Debris-rich nether magma (second vein, weight 25) gives lava, debris and ancient debris for ancient netherite.
    - |-
      Mesh: ancient netherite reinforced mesh = netherite reinforced mesh + 4 ancient netherite rods + 1 ancient netherite ingot + 576 mB niobium nitride, 100 ticks, VHA[UHV]. Ancient netherite = EBF 13 300 K, 4 gold ingots + 4 ancient debris dust + 2000 mB argon, 2500 ticks, hot ingot.
    - |-
      Sub-steps people skip: (1) 200 B per sifter run needs several veins (Unverified drill rate): run a fleet of drilling rigs; (2) three different magmas come out of one destabiliser run: three output hatches and three drums, never share; (3) the mixture and the pure fluids look alike: label drums; (4) the mesh is consumed with a chance, keep 4 spare.
    - |-
      Unverified: sifter mesh consumption chance, vein drilling rate, and the Fluid Drilling Rig tier needed for the Nether vein.
  b:
    - ["gtceu:cyclonic_sifter", 1]
    - ["gtceu:molten_destabiliser", 1]
    - ["gtceu:manifold_centrifuge", 1]
    - ["gtceu:uhv_electrolyzer", 2]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["start_core:zpm_fluid_drilling_rig", "gtceu:highly_unstable_nether_magma_bucket"]
      t: |-
        Nether first: fluid drilling rigs on the highly unstable nether magma veins, pumped to drums (Pipez fluid pipes, pump covers). Debris-rich veins are a separate drum.
    - i: ["gtceu:cyclonic_sifter", "gtceu:mystical_nether_magma_bucket"]
      t: |-
        Cyclonic Sifter: 200 B magma + mesh from a drawer (Robot Arm Keep Exact 4). Output 12 B mystical magma and the three deactivated dusts to their own drawer.
    - i: ["gtceu:molten_destabiliser", "gtceu:mythrillic_nether_magma_bucket"]
      t: |-
        Molten Destabiliser: 3 B mystical in, three magma outputs, one hatch and drum each.
    - i: ["gtceu:manifold_centrifuge", "gtceu:molten_mythrillic_mixture_bucket"]
      t: |-
        Manifold Centrifuge: one run per magma type (9 B each); mystical magma returns to the sifter's output drum.
    - i: ["gtceu:molten_destabiliser", "gtceu:mythrillic_bucket"]
      t: |-
        Molten Destabiliser again with the molten mixtures (300 B each): the highly unstable magma returns to the first drum, the pure fluid goes on.
    - i: ["gtceu:uhv_electrolyzer", "gtceu:mythrillic_dust"]
      t: |-
        Electrolyzer: 1 B per dust; the mystical magma it returns goes back into the loop. Dusts to three drawers for uev_nether2.
---
# Nether magma line: highly unstable nether magma → mystical magma → mythrillic, adamantamite and estaltadyne dusts (start of mythril, adamantine and estalt)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_nether` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [Nether magma: mythril, adamantine, estalt](../../plan/p18.md#uevnether)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-cs">
<div class="gt-head"><span class="gt-mname">Cyclonic Sifter · 200 B + 1 ancient netherite reinforced mesh (chance) · 67.5 s · 2.1 M EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Fluid vein in the Nether: highly unstable nether magma (weight 15, 960 to 1280 yield) (start_core:zpm_fluid_drilling_rig) - 200 B"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fluid_drilling_rig.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fluid Drilling Rig</span><span class="gt-note">Fluid vein in the Nether: highly unstable nether magma (weight 15, 960 to 1280 yield)</span><span class="gt-tag">infinite</span><b class="gt-q">200 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="12 B mystical nether magma + 3 deactivated nether dust (gtceu:mystical_nether_magma_bucket) - 12 B"><img class="gt-ico" src="../../assets/icons/gtceu__mystical_nether_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mystical Nether Magma</span><span class="gt-note">12 B mystical nether magma + 3 deactivated nether dust</span><b class="gt-q">12 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cyclonic_sifter</code></div>
</div>
<div class="gt-panel t-mod" id="m-md">
<div class="gt-head"><span class="gt-mname">Molten Destabiliser · 3 B → 1 B of each · 24 s · 0.59 M EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="12 B mystical nether magma + 3 deactivated nether dust (gtceu:mystical_nether_magma_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__mystical_nether_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mystical Nether Magma</span><span class="gt-note">12 B mystical nether magma + 3 deactivated nether dust</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__molten_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Mythrillic, adamantamite and estaltadyne nether magma (1 B each) (gtceu:mythrillic_nether_magma_bucket) - 1 B each"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_nether_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Nether Magma</span><span class="gt-note">Mythrillic, adamantamite and estaltadyne nether magma (1 B each)</span><b class="gt-q">1 B each</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:molten_destabiliser</code></div>
</div>
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Manifold Centrifuge · 9 B → 6 B molten mixture + 2 B enriched + 1 B mystical · 60 s · 0.98 M EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Mythrillic, adamantamite and estaltadyne nether magma (1 B each) (gtceu:mythrillic_nether_magma_bucket) - 9 B"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_nether_magma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Nether Magma</span><span class="gt-note">Mythrillic, adamantamite and estaltadyne nether magma (1 B each)</span><b class="gt-q">9 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__manifold_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Molten mythrillic, adamantamite or estaltadyne mixture (6 B) (gtceu:molten_mythrillic_mixture_bucket) - 6 B"><img class="gt-ico" src="../../assets/icons/gtceu__molten_mythrillic_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Mythrillic Mixture</span><span class="gt-note">Molten mythrillic, adamantamite or estaltadyne mixture (6 B)</span><b class="gt-q">6 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:manifold_centrifuge</code></div>
</div>
<div class="gt-panel t-mod" id="m-dd">
<div class="gt-head"><span class="gt-mname">Molten Destabiliser · 300 B mixture → 200 B pure fluid + magma + ore mixture + 32 netherrack dust · 180 s · UV</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Molten mythrillic, adamantamite or estaltadyne mixture (6 B) (gtceu:molten_mythrillic_mixture_bucket) - 300 B"><img class="gt-ico" src="../../assets/icons/gtceu__molten_mythrillic_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Mythrillic Mixture</span><span class="gt-note">Molten mythrillic, adamantamite or estaltadyne mixture (6 B)</span><b class="gt-q">300 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__molten_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="200 B mythrillic, adamantamite or estaltadyne (gtceu:mythrillic_bucket) - 200 B"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic</span><span class="gt-note">200 B mythrillic, adamantamite or estaltadyne</span><b class="gt-q">200 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:molten_destabiliser</code></div>
</div>
<div class="gt-panel t-uhv" id="m-el">
<div class="gt-head"><span class="gt-mname">UHV Electrolyzer · 1 B → dust + small dust + 250 mB mystical magma · 7 s</span><span class="gt-badge t-uhv">UHV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="200 B mythrillic, adamantamite or estaltadyne (gtceu:mythrillic_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic</span><span class="gt-note">200 B mythrillic, adamantamite or estaltadyne</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 097 152 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mythrillic, adamantamite and estaltadyne dust (gtceu:mythrillic_dust) - 1 + 1 small"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Dust</span><span class="gt-note">Mythrillic, adamantamite and estaltadyne dust</span><b class="gt-q">1 + 1 small</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uhv_electrolyzer</code></div>
</div>
</div>

## Flow

- [Cyclonic Sifter · 200 B + 1 ancient netherite reinforced mesh (chance) · 67.5 s · 2.1 M EU/t](#m-cs) → [Molten Destabiliser · 3 B → 1 B of each · 24 s · 0.59 M EU/t](#m-md) → [Manifold Centrifuge · 9 B → 6 B molten mixture + 2 B enriched + 1 B mystical · 60 s · 0.98 M EU/t](#m-mc) → [Molten Destabiliser · 300 B mixture → 200 B pure fluid + magma + ore mixture + 32 netherrack dust · 180 s · UV](#m-dd) → [UHV Electrolyzer · 1 B → dust + small dust + 250 mB mystical magma · 7 s](#m-el)

## How to build

1. Nether first: fluid drilling rigs on the highly unstable nether magma veins, pumped to drums (Pipez fluid pipes, pump covers). Debris-rich veins are a separate drum. — `start_core:zpm_fluid_drilling_rig`, `gtceu:highly_unstable_nether_magma_bucket`
2. Cyclonic Sifter: 200 B magma + mesh from a drawer (Robot Arm Keep Exact 4). Output 12 B mystical magma and the three deactivated dusts to their own drawer. — `gtceu:cyclonic_sifter`, `gtceu:mystical_nether_magma_bucket`
3. Molten Destabiliser: 3 B mystical in, three magma outputs, one hatch and drum each. — `gtceu:molten_destabiliser`, `gtceu:mythrillic_nether_magma_bucket`
4. Manifold Centrifuge: one run per magma type (9 B each); mystical magma returns to the sifter's output drum. — `gtceu:manifold_centrifuge`, `gtceu:molten_mythrillic_mixture_bucket`
5. Molten Destabiliser again with the molten mixtures (300 B each): the highly unstable magma returns to the first drum, the pure fluid goes on. — `gtceu:molten_destabiliser`, `gtceu:mythrillic_bucket`
6. Electrolyzer: 1 B per dust; the mystical magma it returns goes back into the loop. Dusts to three drawers for uev\_nether2. — `gtceu:uhv_electrolyzer`, `gtceu:mythrillic_dust`

## Tips

- Source: kjs additions/progression/lines/nether\_lines/{magmas,mythril,adamantine,estalt}.js and utils/fluid\_veins.js. Vein: start:highly\_unstable\_nether\_magma\_deposit in the Nether (weight 15, yield 960 to 1280, depletes 2 per 1 chance, floor 720). Cyclonic Sifter: 200 000 mB highly unstable nether magma + 1 ancient netherite reinforced mesh (chanced input 1000 of 10 000, boost -150) → 12 000 mB mystical nether magma + 3 deactivated nether dust + 2 small + 1 tiny, 1350 ticks, VA\[UEV\] x 3 / 11 = 2 144 814 EU/t. Molten Destabiliser: 3 000 mB mystical → 1 000 mB each of estaltadyne, adamantamite and mythrillic nether magma, 480 ticks, VHA\[UHV\] x 3 / 5 = 589 824 EU/t.
- Manifold Centrifuge (VHA\[UHV\], 1200 ticks): 9 000 mB of each nether magma → 6 000 mB molten mixture + 2 000 mB enriched mixture + 1 000 mB mystical magma back. Molten Destabiliser (VHA\[UV\], 3600 ticks): 300 000 mB molten mixture → 200 000 mB pure fluid + 25 000 mB (50 000 for estaltadyne) highly unstable nether magma + 75 000 mB (50 000) molten ore mixture + 32 netherrack dust: the magma comes back, so the line is a loop that only loses to the mesh and the ore mixture. Electrolyzer (VHA\[UHV\], 140 ticks): 1000 mB pure fluid → dust + small dust + 250 mB mystical magma.
- Side loops: the enriched mixtures + activated nether dust (polarizer on deactivated dust, 360 ticks) go through a heat chamber into atomic nether sludge dust, which a UEV Manifold Centrifuge with hexafluorobromic acid splits into flerovium-, hafnium- and polonium-rich sludges (flerovium, hafnium, seaborgium, polonium and astatine lines in atomic\_nether\_sludge.js; the alloys uev\_alloys and fusion use flerovium, seaborgium and astatine). Debris-rich nether magma (second vein, weight 25) gives lava, debris and ancient debris for ancient netherite.
- Mesh: ancient netherite reinforced mesh = netherite reinforced mesh + 4 ancient netherite rods + 1 ancient netherite ingot + 576 mB niobium nitride, 100 ticks, VHA\[UHV\]. Ancient netherite = EBF 13 300 K, 4 gold ingots + 4 ancient debris dust + 2000 mB argon, 2500 ticks, hot ingot.
- Sub-steps people skip: (1) 200 B per sifter run needs several veins (Unverified drill rate): run a fleet of drilling rigs; (2) three different magmas come out of one destabiliser run: three output hatches and three drums, never share; (3) the mixture and the pure fluids look alike: label drums; (4) the mesh is consumed with a chance, keep 4 spare.
- **Unverified** sifter mesh consumption chance, vein drilling rate, and the Fluid Drilling Rig tier needed for the Nether vein.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:cyclonic_sifter` | 1 |
| `gtceu:molten_destabiliser` | 1 |
| `gtceu:manifold_centrifuge` | 1 |
| `gtceu:uhv_electrolyzer` | 2 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Needs:** [Abydos mantle: ZPM Fluid Drilling Rig (144 CWU/t research) → gritty akreyrium → Cyclonic Sifter and Molten Destabiliser (280 B and 72 B of it per controller)](../uv/uv_akreyrium.md)
- **Main source for:** `gtceu:mythrillic_dust`, `gtceu:adamantamite_dust`, `gtceu:estaltadyne_dust`, `gtceu:mystical_nether_magma_bucket`
