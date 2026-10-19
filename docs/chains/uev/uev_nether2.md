---
kind: chain
id: uev_nether2
order: 2140
data:
  t: Mythril, adamantine, estalt, calamatium and isovol from the nether dusts (Advanced Synthesis Plant, large chemical reactor, EBF, vacuum chemical reactor)
  inf: true
  "n":
    - - d1
      - Mythrillic dust + 2875 mB hydrogen · 3 carbon + 3250 mB hydrogen · 2 NaOH + 1875 mB HCl · 1875 mB oxygen
      - g
      - functionalstorage:oak_1
      - - [Mythrillic dust, "gtceu:mythrillic_dust"]
        - [Carbon dust, "gtceu:carbon_dust"]
        - [Sodium hydroxide dust, "gtceu:sodium_hydroxide_dust"]
    - - d2
      - |-
        Adamantamite dust + acids and metals (5 layers: HCl, hydrogen, NaOH + sodium, HF + chlorine, magnesium + nitric acid)
      - g
      - functionalstorage:oak_1
      - - [Adamantamite dust, "gtceu:adamantamite_dust"]
        - [Sodium dust, "gtceu:sodium_dust"]
        - [Magnesium dust, "gtceu:magnesium_dust"]
    - - d3
      - Estaltadyne dust + 6 carbon · 4 sodium + CO2 · HF + hydrogen · 2 magnesium + NaOH · NaOH + nitric acid
      - g
      - functionalstorage:oak_1
      - - [Estaltadyne dust, "gtceu:estaltadyne_dust"]
        - [Carbon dust, "gtceu:carbon_dust"]
        - [Sodium dust, "gtceu:sodium_dust"]
    - [asp, "Advanced Synthesis Plant (ordered chemistry) · 6 to 9 s · UEV", m, "gtceu:advanced_synthesis_plant"]
    - - hy
      - |-
        6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust
      - x
      - gtceu:mythrillic_hydride_dust
    - [ebf, "EBF 9100 K + sulfur · 21 s · 3.9 M EU/t", m, "gtceu:electric_blast_furnace"]
    - - lcr
      - Large Chemical Reactor · + 3 sodium (adamantine) · + 15 phosphate (estalt)
      - m
      - gtceu:large_chemical_reactor
    - [o1, Mythril dust, x, "gtceu:mythril_dust"]
    - [o2, Adamantine dust, x, "gtceu:adamantine_dust"]
    - [o3, "4 Estalt dust per hydride", x, "gtceu:estalt_dust"]
    - - vc
      - Vacuum Chemical Reactor · 6 estalt dust + 2000 mB fluoroantimonic acid · 24 s · vacuum 90
      - m
      - gtceu:dual_chambered_vacuum_complex
    - [o4, "Calamatium and isovol dust (via solutions, 2 centrifuge steps and water)", o, "gtceu:isovol_dust"]
  e:
    - [d1, asp, "1"]
    - [d2, asp, "1"]
    - [d3, asp, "1"]
    - [asp, hy, "1 / recipe"]
    - [hy, ebf, mythril]
    - [hy, lcr, "adamantine, estalt"]
    - [ebf, o1, "1"]
    - [lcr, o2, "1"]
    - [lcr, o3, "4"]
    - [o3, vc, "6"]
    - [vc, o4, solutions]
  tips:
    - |-
      Source: nether_lines/{mythril,adamantine,estalt,calamatium_and_isovol}.js. Mythril: Advanced Synthesis Plant (ordered_chemistry, VA[UEV], 116 ticks): 1 mythrillic dust + 2875 mB hydrogen, then 3 carbon + 3250 mB hydrogen, then 2 sodium hydroxide + 1875 mB hydrochloric acid, plus 1875 mB oxygen → 6 mythrillic hydride dust; EBF (blast 9100 K, VHA[UEV], 420 ticks): 1 hydride dust + 1 sulfur → 1 mythril dust + 1000 mB hydrogen sulfide. The blast gas uses xenon instead of krypton (event.replaceInput).
    - |-
      Adamantine (VA[UEV], 180 ticks): 1 adamantamite dust + 2500 mB HCl, then 3 carbon + 4250 mB hydrogen, then 3 NaOH + 2 sodium, then 1875 mB hydrofluoric acid + 2000 mB chlorine, then 2 magnesium + 1500 mB nitric acid → 5 adamantine hydroxide dust; Large Chemical Reactor (VHA[UV], 540 ticks): 1 hydroxide + 3 sodium → 1 adamantine dust + 9 NaOH. Estalt (VHA[UEV], 160 ticks): 1 estaltadyne dust + 6 carbon, 4 sodium + 2000 mB CO2, 3500 mB HF + 1500 mB hydrogen, 2 magnesium + 1 NaOH, 1 NaOH + 2000 mB nitric acid → 1 estaltadyne hydride dust; Large Chemical Reactor (UV, 1200 ticks): 1 hydride + 15 phosphate → 4 estalt dust + 3000 mB phosphoric acid (electrolysed back to phosphorus, hydrogen and oxygen).
    - |-
      Isovol and calamatium (VHA[ZPM], 480 ticks, vacuum level 90): 6 estalt dust + 2000 mB fluoroantimonic acid → 1000 mB impure calamatium solution + 1000 mB impure isovol solution + 4000 mB fluorine. Each impure solution: centrifuge (100 000 EU/t, 600 ticks) → solution + 4 antimony trifluoride; centrifuge (80 000 EU/t, 600 ticks) → fluoride dust + 2000 mB hydrogen; Large Chemical Reactor (80 000 EU/t, 600 ticks) + 1000 mB water → calamatium or isovol dust + 2000 mB HF + 1000 mB oxygen. Isovol is the UEV tier fluid (parts and components), calamatium the UIV one and the UEV frame/rotor/screw metal.
    - |-
      Machines of the whole nether line (verified): magma and nether dust steps run in the Manifold Centrifuge (VHA[UHV]) and the Cyclonic Sifter (VA[UEV] x 3 / 11); molten mixtures in the Molten Destabiliser (VHA[UV]); electrolysis VHA[UHV]; the Advanced Synthesis Plant steps are VA[UEV] for mythrillic and adamantine hydroxide and VHA[UEV] for estaltadyne hydride; the final mythril EBF is VHA[UEV] (a Rotary Hearth Furnace, built at UHV), the final adamantine step an LCR at VHA[UV], estalt an LCR plus manifold centrifuge at VHA[UEV]. The alloys of uev_alloys then need Bulk Blast Chillers (freezing) and Cryostate Quantum Chillers (plasma cooling).
    - Mythril and adamantine and estalt go into the Hell Forge (uev_alloys); starium alloy also needs estalt, magmada needs adamantine, mythrolic needs mythril.
    - |-
      Sub-steps people skip: (1) the three ordered chemistry recipes are NOT the same machine as a Chemical Plant: the Advanced Synthesis Plant runs the layered ones; (2) HF, nitric acid, hydrogen, chlorine, magnesium and sodium must be in drawers/drums first: the plant takes them in layers; (3) fluoroantimonic acid and its antimony trifluoride return: loop them; (4) bake the dusts to ingots with the matching EBF recipes: Unverified blast temperatures of the calamatium, isovol, adamantine and estalt ingots (only the mythril dust recipe is traced here).
    - |-
      Unverified: ingot blast temperatures, fluoroantimonic acid supply, and which EBF/coil tier reaches 9100 K (the strongest coil listed in this guide is the 9001 K trinium one; the Ultimate EBF and Mega Blast Furnace take any heating coil block).
  b:
    - ["gtceu:advanced_synthesis_plant", 1]
    - ["gtceu:large_chemical_reactor", 2]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:dual_chambered_vacuum_complex", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:mythrillic_dust", "gtceu:carbon_dust"]
      t: |-
        Drawers first: the three nether dusts, carbon, sodium, magnesium, sodium hydroxide, sulfur, phosphate. Drums: hydrogen, HCl, oxygen, HF, chlorine, nitric acid, CO2, water. Item filters per drawer; Pipez fluid pipes with pump covers; one product at a time on the Advanced Synthesis Plant.
    - i: ["gtceu:advanced_synthesis_plant", "gtceu:mythrillic_hydride_dust"]
      t: |-
        Mythril first (it feeds mythrolic alloy): plant → hydride dust → EBF with sulfur → mythril dust.
    - i: ["gtceu:advanced_synthesis_plant", "gtceu:adamantine_dust"]
      t: |-
        Adamantine: 5-layer recipe, then the large chemical reactor with 3 sodium. The 9 NaOH it returns go back to the drawer.
    - i: ["gtceu:large_chemical_reactor", "gtceu:estalt_dust"]
      t: |-
        Estalt: hydride + 15 phosphate; phosphoric acid out to an electrolyzer (30 EU/t) that returns phosphorus, hydrogen and oxygen.
    - i: ["gtceu:dual_chambered_vacuum_complex", "gtceu:isovol_dust"]
      t: |-
        Isovol and calamatium: vacuum chemical reactor with fluoroantimonic acid, then two centrifuge steps and the water reactor.
    - i: ["functionalstorage:oak_1", "gtceu:mythril_dust", "gtceu:adamantine_dust"]
      t: Drawers Keep Exact 64 on the four dusts; EBF them with the matching alloy recipes (Unverified temperatures).
---
# Mythril, adamantine, estalt, calamatium and isovol from the nether dusts (Advanced Synthesis Plant, large chemical reactor, EBF, vacuum chemical reactor)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_nether2` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [Nether magma: mythril, adamantine, estalt](../../plan/p18.md#uevnether)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-asp">
<div class="gt-head"><span class="gt-mname">Advanced Synthesis Plant (ordered chemistry) · 6 to 9 s · UEV</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Mythrillic dust + 2875 mB hydrogen · 3 carbon + 3250 mB hydrogen · 2 NaOH + 1875 mB HCl · 1875 mB oxygen (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Mythrillic dust + 2875 mB hydrogen · 3 carbon + 3250 mB hydrogen · 2 NaOH + 1875 mB HCl · 1875 mB oxygen</span><span class="gt-sub"><span>Mythrillic dust</span><span>Carbon dust</span><span>Sodium hydroxide dust</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Adamantamite dust + acids and metals (5 layers: HCl, hydrogen, NaOH + sodium, HF + chlorine, magnesium + nitric acid) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Adamantamite dust + acids and metals (5 layers: HCl, hydrogen, NaOH + sodium, HF + chlorine, magnesium + nitric acid)</span><span class="gt-sub"><span>Adamantamite dust</span><span>Sodium dust</span><span>Magnesium dust</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Estaltadyne dust + 6 carbon · 4 sodium + CO2 · HF + hydrogen · 2 magnesium + NaOH · NaOH + nitric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Estaltadyne dust + 6 carbon · 4 sodium + CO2 · HF + hydrogen · 2 magnesium + NaOH · NaOH + nitric acid</span><span class="gt-sub"><span>Estaltadyne dust</span><span>Carbon dust</span><span>Sodium dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_synthesis_plant.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust (gtceu:mythrillic_hydride_dust) - 1 / recipe"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_hydride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Hydride Dust</span><span class="gt-note">6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust</span><b class="gt-q">1 / recipe</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:advanced_synthesis_plant</code></div>
</div>
<div class="gt-panel t-multi" id="m-ebf">
<div class="gt-head"><span class="gt-mname">EBF 9100 K + sulfur · 21 s · 3.9 M EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust (gtceu:mythrillic_hydride_dust) - mythril"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_hydride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Hydride Dust</span><span class="gt-note">6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust</span><b class="gt-q">mythril</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Mythril dust (gtceu:mythril_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__mythril_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythril Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-lcr">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · + 3 sodium (adamantine) · + 15 phosphate (estalt)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust (gtceu:mythrillic_hydride_dust) - adamantine, estalt"><img class="gt-ico" src="../../assets/icons/gtceu__mythrillic_hydride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrillic Hydride Dust</span><span class="gt-note">6 mythrillic hydride · 5 adamantine hydroxide · 1 estaltadyne hydride dust</span><b class="gt-q">adamantine, estalt</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Adamantine dust (gtceu:adamantine_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__adamantine_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Adamantine Dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="4 Estalt dust per hydride (gtceu:estalt_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__estalt_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Estalt Dust</span><span class="gt-note">4 Estalt dust per hydride</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mod" id="m-vc">
<div class="gt-head"><span class="gt-mname">Vacuum Chemical Reactor · 6 estalt dust + 2000 mB fluoroantimonic acid · 24 s · vacuum 90</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Estalt dust per hydride (gtceu:estalt_dust) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__estalt_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Estalt Dust</span><span class="gt-note">4 Estalt dust per hydride</span><b class="gt-q">6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__dual_chambered_vacuum_complex.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Calamatium and isovol dust (via solutions, 2 centrifuge steps and water) (gtceu:isovol_dust) - solutions"><img class="gt-ico" src="../../assets/icons/gtceu__isovol_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Isovol Dust</span><span class="gt-note">Calamatium and isovol dust (via solutions, 2 centrifuge steps and water)</span><b class="gt-q">solutions</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:dual_chambered_vacuum_complex</code></div>
</div>
</div>

## Flow

- [Advanced Synthesis Plant (ordered chemistry) · 6 to 9 s · UEV](#m-asp) → [EBF 9100 K + sulfur · 21 s · 3.9 M EU/t](#m-ebf) (also Advanced Synthesis Plant (ordered chemistry) · 6 to 9 s · UEV → [Large Chemical Reactor · + 3 sodium (adamantine) · + 15 phosphate (estalt)](#m-lcr))
- [Large Chemical Reactor · + 3 sodium (adamantine) · + 15 phosphate (estalt)](#m-lcr) → [Vacuum Chemical Reactor · 6 estalt dust + 2000 mB fluoroantimonic acid · 24 s · vacuum 90](#m-vc)

## How to build

1. Drawers first: the three nether dusts, carbon, sodium, magnesium, sodium hydroxide, sulfur, phosphate. Drums: hydrogen, HCl, oxygen, HF, chlorine, nitric acid, CO2, water. Item filters per drawer; Pipez fluid pipes with pump covers; one product at a time on the Advanced Synthesis Plant. — `functionalstorage:oak_1`, `gtceu:mythrillic_dust`, `gtceu:carbon_dust`
2. Mythril first (it feeds mythrolic alloy): plant → hydride dust → EBF with sulfur → mythril dust. — `gtceu:advanced_synthesis_plant`, `gtceu:mythrillic_hydride_dust`
3. Adamantine: 5-layer recipe, then the large chemical reactor with 3 sodium. The 9 NaOH it returns go back to the drawer. — `gtceu:advanced_synthesis_plant`, `gtceu:adamantine_dust`
4. Estalt: hydride + 15 phosphate; phosphoric acid out to an electrolyzer (30 EU/t) that returns phosphorus, hydrogen and oxygen. — `gtceu:large_chemical_reactor`, `gtceu:estalt_dust`
5. Isovol and calamatium: vacuum chemical reactor with fluoroantimonic acid, then two centrifuge steps and the water reactor. — `gtceu:dual_chambered_vacuum_complex`, `gtceu:isovol_dust`
6. Drawers Keep Exact 64 on the four dusts; EBF them with the matching alloy recipes (Unverified temperatures). — `functionalstorage:oak_1`, `gtceu:mythril_dust`, `gtceu:adamantine_dust`

## Tips

- Source: nether\_lines/{mythril,adamantine,estalt,calamatium\_and\_isovol}.js. Mythril: Advanced Synthesis Plant (ordered\_chemistry, VA\[UEV\], 116 ticks): 1 mythrillic dust + 2875 mB hydrogen, then 3 carbon + 3250 mB hydrogen, then 2 sodium hydroxide + 1875 mB hydrochloric acid, plus 1875 mB oxygen → 6 mythrillic hydride dust; EBF (blast 9100 K, VHA\[UEV\], 420 ticks): 1 hydride dust + 1 sulfur → 1 mythril dust + 1000 mB hydrogen sulfide. The blast gas uses xenon instead of krypton (event.replaceInput).
- Adamantine (VA\[UEV\], 180 ticks): 1 adamantamite dust + 2500 mB HCl, then 3 carbon + 4250 mB hydrogen, then 3 NaOH + 2 sodium, then 1875 mB hydrofluoric acid + 2000 mB chlorine, then 2 magnesium + 1500 mB nitric acid → 5 adamantine hydroxide dust; Large Chemical Reactor (VHA\[UV\], 540 ticks): 1 hydroxide + 3 sodium → 1 adamantine dust + 9 NaOH. Estalt (VHA\[UEV\], 160 ticks): 1 estaltadyne dust + 6 carbon, 4 sodium + 2000 mB CO2, 3500 mB HF + 1500 mB hydrogen, 2 magnesium + 1 NaOH, 1 NaOH + 2000 mB nitric acid → 1 estaltadyne hydride dust; Large Chemical Reactor (UV, 1200 ticks): 1 hydride + 15 phosphate → 4 estalt dust + 3000 mB phosphoric acid (electrolysed back to phosphorus, hydrogen and oxygen).
- Isovol and calamatium (VHA\[ZPM\], 480 ticks, vacuum level 90): 6 estalt dust + 2000 mB fluoroantimonic acid → 1000 mB impure calamatium solution + 1000 mB impure isovol solution + 4000 mB fluorine. Each impure solution: centrifuge (100 000 EU/t, 600 ticks) → solution + 4 antimony trifluoride; centrifuge (80 000 EU/t, 600 ticks) → fluoride dust + 2000 mB hydrogen; Large Chemical Reactor (80 000 EU/t, 600 ticks) + 1000 mB water → calamatium or isovol dust + 2000 mB HF + 1000 mB oxygen. Isovol is the UEV tier fluid (parts and components), calamatium the UIV one and the UEV frame/rotor/screw metal.
- Machines of the whole nether line (verified): magma and nether dust steps run in the Manifold Centrifuge (VHA\[UHV\]) and the Cyclonic Sifter (VA\[UEV\] x 3 / 11); molten mixtures in the Molten Destabiliser (VHA\[UV\]); electrolysis VHA\[UHV\]; the Advanced Synthesis Plant steps are VA\[UEV\] for mythrillic and adamantine hydroxide and VHA\[UEV\] for estaltadyne hydride; the final mythril EBF is VHA\[UEV\] (a Rotary Hearth Furnace, built at UHV), the final adamantine step an LCR at VHA\[UV\], estalt an LCR plus manifold centrifuge at VHA\[UEV\]. The alloys of uev\_alloys then need Bulk Blast Chillers (freezing) and Cryostate Quantum Chillers (plasma cooling).
- Mythril and adamantine and estalt go into the Hell Forge (uev\_alloys); starium alloy also needs estalt, magmada needs adamantine, mythrolic needs mythril.
- Sub-steps people skip: (1) the three ordered chemistry recipes are NOT the same machine as a Chemical Plant: the Advanced Synthesis Plant runs the layered ones; (2) HF, nitric acid, hydrogen, chlorine, magnesium and sodium must be in drawers/drums first: the plant takes them in layers; (3) fluoroantimonic acid and its antimony trifluoride return: loop them; (4) bake the dusts to ingots with the matching EBF recipes: Unverified blast temperatures of the calamatium, isovol, adamantine and estalt ingots (only the mythril dust recipe is traced here).
- **Unverified** ingot blast temperatures, fluoroantimonic acid supply, and which EBF/coil tier reaches 9100 K (the strongest coil listed in this guide is the 9001 K trinium one; the Ultimate EBF and Mega Blast Furnace take any heating coil block).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:advanced_synthesis_plant` | 1 |
| `gtceu:large_chemical_reactor` | 2 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:dual_chambered_vacuum_complex` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Main source for:** `gtceu:mythril_dust`, `gtceu:adamantine_dust`, `gtceu:estalt_dust`, `gtceu:isovol_dust`, `gtceu:calamatium_dust`
