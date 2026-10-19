---
kind: chain
id: uev_alloys
order: 2090
data:
  t: |-
    UEV alloys (mythrolic, magmada, starium): molten metals + element plasma in the Hell Forge → alloy plasma → Cryostate Quantum Chiller → molten alloy → vacuum freezer → ingot
  inf: true
  "n":
    - - g1
      - |-
        Mythrolic (11 ingots): 720 mB mythril + 576 mB HSS-S + 288 mB darmstadtium + 1584 mB argon plasma
      - g
      - functionalstorage:oak_1
      - - [Mythril, "gtceu:mythril_bucket"]
        - [HSS-S, "gtceu:hsss_bucket"]
        - [Darmstadtium, "gtceu:darmstadtium_bucket"]
        - [Argon plasma, "gtceu:argon_plasma_bucket"]
    - - g2
      - |-
        Magmada (8 ingots): 576 mB adamantine + 144 mB neutronium + 432 mB RTM alloy + 1152 mB magmatic plasma
      - g
      - functionalstorage:oak_1
      - - [Adamantine, "gtceu:adamantine_bucket"]
        - [Neutronium, "gtceu:neutronium_bucket"]
        - [RTM alloy, "gtceu:rtm_alloy_bucket"]
        - [Magmatic plasma, "gtceu:magmatic_plasma_bucket"]
    - - g3
      - |-
        Starium (8 ingots): 576 mB nether star concentrate + 288 mB trinaquadalloy + 288 mB estalt + 1152 mB oxygen plasma
      - g
      - functionalstorage:oak_1
      - - [Nether star concentrate, "gtceu:nether_star_concentrate_bucket"]
        - [Trinaquadalloy, "gtceu:trinaquadalloy_bucket"]
        - [Estalt, "gtceu:estalt_bucket"]
        - [Oxygen plasma, "gtceu:oxygen_plasma_bucket"]
    - [hf, "Hell Forge · 3 932 160 EU/t · 8 to 11 ingots per run (uev_hellforge)", m, "start_core:hellforge"]
    - [pl, "Alloy plasma (144 mB per ingot) + tiny hellfire ash dust", f, "gtceu:mythrolic_alloy_plasma_bucket"]
    - [bc, "250 mB BEC oganesson per 144 mB (uev_chiller)", f, "gtceu:bec_og_bucket"]
    - - qc
      - Cryostate Quantum Chiller · 3 932 160 EU/t · 6 to 12 s per 144 mB
      - m
      - gtceu:cryostate_quantum_chiller
    - [mo, "Molten alloy 144 mB (+ 200 mB oganesson back)", f, "gtceu:molten_mythrolic_alloy_bucket"]
    - [sh, "500 mB superstate helium 3 + ingot casting mold", f, "gtceu:superstate_helium_3_bucket"]
    - [vf, "Vacuum Freezer · UV · 491 520 EU/t · 30 to 49 s", m, "gtceu:vacuum_freezer"]
    - [o1, Mythrolic alloy ingot, o, "gtceu:mythrolic_alloy_ingot"]
    - [o2, Magmada alloy ingot, o, "gtceu:magmada_alloy_ingot"]
    - [o3, Starium alloy ingot, o, "gtceu:starium_alloy_ingot"]
  e:
    - [g1, hf, "11 ingots"]
    - [g2, hf, "8 ingots"]
    - [g3, hf, "8 ingots"]
    - [hf, pl, "144 mB / ingot"]
    - [pl, qc, "144 mB"]
    - [bc, qc, "250 mB"]
    - [qc, mo, "144 mB"]
    - [mo, vf, "144 mB"]
    - [sh, vf, "500 mB"]
    - [vf, o1, "1"]
    - [vf, o2, "1"]
    - [vf, o3, "1"]
  tips:
    - |-
      Hell Forge (kjs systems/hellforge.js, hellForgeMat): every alloy is made as PLASMA. Mythrolic alloy: 11 ingots = 1584 mB argon plasma + 720 mB mythril + 576 mB HSS-S + 288 mB darmstadtium (circuit 3), 9592 ticks (479.6 s), 3 932 160 EU/t (VHA[UEV]), heat requirement 568, output 1584 mB mythrolic alloy plasma + 11 tiny hellfire ash dust. Magmada alloy: 8 ingots = 1152 mB magmatic plasma + 576 adamantine + 144 neutronium + 432 RTM alloy, 8384 ticks, heat 708. Starium alloy: 8 ingots = 1152 mB oxygen plasma + 576 nether star concentrate + 288 trinaquadalloy + 288 estalt, 6368 ticks, heat 633. The same recipes with infernal catalysts (1 per ingot, circuit +10): 85 % of the time and 125 % of the plasma.
    - |-
      Cooling (systems/cryostate_quantum_chiller.js, material15000PlusAlloy): the vacuum freezer recipe of each alloy is REMOVED and replaced by two steps. (1) Cryostate Quantum Chiller (quantum_cooling): 144 mB alloy plasma + 250 mB BEC oganesson → 144 mB molten alloy + 200 mB oganesson, duration = seconds x 6 ticks (mythrolic 221 ticks, magmada 295, starium 177), 3 932 160 EU/t (VHA[UEV]). (2) Vacuum Freezer at UV (491 520 EU/t): 144 mB molten alloy + 500 mB superstate helium 3 + non-consumed ingot casting mold → 1 ingot + 250 mB helium 3, 36.9 s (mythrolic), 49.2 s (magmada), 29.55 s (starium). A zalloyic fluid mold instead of the ingot mold gives the liquid alloy (used for pipes and multiblock fluid feeds).
    - |-
      Modes (verified): the Hell Forge has NO cooled mode; each alloy has a normal recipe and a _boosted one (one catalyst per ingot: 85 % of the time, 125 % of the plasma). The two modes people talk about belong to the Cryostate Quantum Chiller (quantum_cooling and vacuum_freezer, see uev_chiller). Hell Forge fuel chain (hellforge.js): crude infernal concentrate (Nether vein) -> Cyclonic Sifter (VHA[UHV], 1150 ticks, ancient netherite reinforced mesh, 50 000 -> 15 000 mB infernal concentrate) -> Heat Chamber superheated infernal concentrate (VA[UEV], 640 ticks, 950 infernal + 50 utopian akreyrium) -> Injection Mixer sub-stellar infernal concentrate (VHA[UEV], 7500 superheated + 36 borealic concentrate -> 5000). Heating solvents: flamewake solvent (pressure heat chamber, 50 000 superheated -> 5000, VA[UV] x 4 = 1 966 080 EU/t) and emberheart nectar (50 000 sub-stellar -> 5000, VA[UV] x 16 = 7 864 320 EU/t); the Molten Destabiliser upgrades them to cinderbrew solvent and corefire nectar (returns 70 000 of the original + 5000 infernal). Catalysts (96 per craft): ascendant (1 UHV circuit), infernal (1 UEV), abyssal (1 UIV). The forge loses 5 MK per 10 s and every 450 MK above the recipe requirement gives 2^n absolute parallels. Unverified: the MK cap of each solvent.
    - |-
      Ingredients (earlier tiers): mythril = nether magma line (uev_nether), HSS-S and darmstadtium (UV/UHV), adamantine (uev_nether), neutronium, RTM alloy (IV), nether star concentrate (IV line), trinaquadalloy (ZPM naquadah products), estalt (uev_nether). Plasma gases: argon and oxygen from air separation, magmatic plasma: Unverified source.
    - |-
      What the alloys are for (tier_data.js): mythrolic = UEV plate, hull, casing, pipe; starium = UEV primary (frames, rods, rings, bolts, gears); magmada = UEV secondary (gears, rotors, screws, rings). So one UEV hull needs 8 mythrolic plates, while the UEV component parts and components eat starium and magmada in large numbers (counts in uev_parts and uev_components). The pack gives no ratio: size the Hell Forge runs from those lists.
    - |-
      Sub-steps people skip: (1) tiny hellfire ash dust is a by-product: void or centrifuge it (hellfire_ash_decomposition) so the output bus does not jam; (2) BEC oganesson is not consumed fully (250 in, 200 oganesson out): the loop needs a start stock (uev_chiller); (3) superstate helium 3 comes back as helium 3: keep the loop closed; (4) one batch of plasma is 1584 mB for mythrolic: use a UEV-size tank (UHV drum) so the chiller does not stall mid-batch.
    - |-
      Unverified: the meaning of the heat values (568, 708, 633) in this fork's Hell Forge, which hatches the plasma needs, and the plasma gas sources.
  b:
    - ["start_core:hellforge", 1]
    - ["gtceu:cryostate_quantum_chiller", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:mythril_bucket", "gtceu:adamantine_bucket"]
      t: |-
        Drums first: one per molten input (mythril, HSS-S, darmstadtium, adamantine, neutronium, RTM alloy, nether star concentrate, trinaquadalloy, estalt) and one per plasma (argon, magmatic, oxygen). Pipez fluid pipes with pump covers into dedicated hatches of the Hell Forge. Never mix two alloy recipes in the same hatch.
    - i: ["start_core:hellforge", "gtceu:mythrolic_alloy_plasma_bucket"]
      t: |-
        Hell Forge: the recipe follows the fluids you feed (all three use circuit 3; the boosted versions use circuit 13 and one infernal catalyst per ingot). Run mythrolic first: you need 8 plates per hull. Plasma leaves through an output hatch into a UHV drum with Keep Exact so it never blocks the forge.
    - i: ["gtceu:cryostate_quantum_chiller", "gtceu:bec_og_bucket"]
      t: |-
        Cryostate Quantum Chiller: plasma + BEC oganesson in, molten alloy and oganesson out; oganesson returns to the BEC loop (uev_chiller). 144 mB per recipe, so use a parallel hatch if you have one.
    - i: ["gtceu:vacuum_freezer", "gtceu:ingot_casting_mold", "gtceu:superstate_helium_3_bucket"]
      t: |-
        Vacuum Freezer (UV): molten alloy + 500 mB superstate helium 3, ingot casting mold in the controller slot (not consumed). Helium 3 out goes back to the quantum cooling that makes superstate helium 3.
    - i:
        - functionalstorage:oak_1
        - gtceu:mythrolic_alloy_ingot
        - gtceu:starium_alloy_ingot
        - gtceu:magmada_alloy_ingot
      t: Ingots to three drawers Keep Exact 64. Their plates, frames and gears come from LV benders and lathes like any other metal.
    - i: ["gtceu:tiny_hellfire_ash_dust"]
      t: |-
        By-product: tiny hellfire ash dust per ingot to a dust drawer (Unverified: 9 tiny make 1 hellfire ash dust); the manifold centrifuge (VHA[ZPM]) splits hellfire ash dust into dark ash, netherrack dust, uvarovite, mica and biotite plus 25 mB infernal tar, and infernal tar goes through a second manifold centrifuge into infernal concentrate (hellforge.js).
---
# UEV alloys (mythrolic, magmada, starium): molten metals + element plasma in the Hell Forge → alloy plasma → Cryostate Quantum Chiller → molten alloy → vacuum freezer → ingot

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [Hell Forge, Chiller and UEV alloys](../../plan/p18.md#uevforge)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-hf">
<div class="gt-head"><span class="gt-mname">Hell Forge · 3 932 160 EU/t · 8 to 11 ingots per run (uev_hellforge)</span><span class="gt-badge t-mod">StarT</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Mythrolic (11 ingots): 720 mB mythril + 576 mB HSS-S + 288 mB darmstadtium + 1584 mB argon plasma (functionalstorage:oak_1) - 11 ingots"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Mythrolic (11 ingots): 720 mB mythril + 576 mB HSS-S + 288 mB darmstadtium + 1584 mB argon plasma</span><span class="gt-sub"><span>Mythril</span><span>HSS-S</span><span>Darmstadtium</span><span>Argon plasma</span></span><b class="gt-q">11 ingots</b></span><span class="gt-slot gt-group" title="Magmada (8 ingots): 576 mB adamantine + 144 mB neutronium + 432 mB RTM alloy + 1152 mB magmatic plasma (functionalstorage:oak_1) - 8 ingots"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Magmada (8 ingots): 576 mB adamantine + 144 mB neutronium + 432 mB RTM alloy + 1152 mB magmatic plasma</span><span class="gt-sub"><span>Adamantine</span><span>Neutronium</span><span>RTM alloy</span><span>Magmatic plasma</span></span><b class="gt-q">8 ingots</b></span><span class="gt-slot gt-group" title="Starium (8 ingots): 576 mB nether star concentrate + 288 mB trinaquadalloy + 288 mB estalt + 1152 mB oxygen plasma (functionalstorage:oak_1) - 8 ingots"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Starium (8 ingots): 576 mB nether star concentrate + 288 mB trinaquadalloy + 288 mB estalt + 1152 mB oxygen plasma</span><span class="gt-sub"><span>Nether star concentrate</span><span>Trinaquadalloy</span><span>Estalt</span><span>Oxygen plasma</span></span><b class="gt-q">8 ingots</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__hellforge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Alloy plasma (144 mB per ingot) + tiny hellfire ash dust (gtceu:mythrolic_alloy_plasma_bucket) - 144 mB / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Plasma</span><span class="gt-note">Alloy plasma (144 mB per ingot) + tiny hellfire ash dust</span><b class="gt-q">144 mB / ingot</b></span></div>
</div>
<div class="gt-foot"><code>start_core:hellforge</code></div>
</div>
<div class="gt-panel t-mod" id="m-qc">
<div class="gt-head"><span class="gt-mname">Cryostate Quantum Chiller · 3 932 160 EU/t · 6 to 12 s per 144 mB</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Alloy plasma (144 mB per ingot) + tiny hellfire ash dust (gtceu:mythrolic_alloy_plasma_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Plasma</span><span class="gt-note">Alloy plasma (144 mB per ingot) + tiny hellfire ash dust</span><b class="gt-q">144 mB</b></span><span class="gt-slot gt-fluid" title="250 mB BEC oganesson per 144 mB (uev_chiller) (gtceu:bec_og_bucket) - 250 mB"><img class="gt-ico" src="../../assets/icons/gtceu__bec_og_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bec Og</span><span class="gt-note">250 mB BEC oganesson per 144 mB (uev_chiller)</span><b class="gt-q">250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Molten alloy 144 mB (+ 200 mB oganesson back) (gtceu:molten_mythrolic_alloy_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__molten_mythrolic_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Mythrolic Alloy</span><span class="gt-note">Molten alloy 144 mB (+ 200 mB oganesson back)</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cryostate_quantum_chiller</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · UV · 491 520 EU/t · 30 to 49 s</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Molten alloy 144 mB (+ 200 mB oganesson back) (gtceu:molten_mythrolic_alloy_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__molten_mythrolic_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Mythrolic Alloy</span><span class="gt-note">Molten alloy 144 mB (+ 200 mB oganesson back)</span><b class="gt-q">144 mB</b></span><span class="gt-slot gt-fluid" title="500 mB superstate helium 3 + ingot casting mold (gtceu:superstate_helium_3_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__superstate_helium_3_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superstate Helium 3</span><span class="gt-note">500 mB superstate helium 3 + ingot casting mold</span><b class="gt-q">500 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mythrolic alloy ingot (gtceu:mythrolic_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Ingot</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Magmada alloy ingot (gtceu:magmada_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magmada_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magmada Alloy Ingot</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Starium alloy ingot (gtceu:starium_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__starium_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Starium Alloy Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [Hell Forge · 3 932 160 EU/t · 8 to 11 ingots per run (uev\_hellforge)](#m-hf) → [Cryostate Quantum Chiller · 3 932 160 EU/t · 6 to 12 s per 144 mB](#m-qc) → [Vacuum Freezer · UV · 491 520 EU/t · 30 to 49 s](#m-vf)

## How to build

1. Drums first: one per molten input (mythril, HSS-S, darmstadtium, adamantine, neutronium, RTM alloy, nether star concentrate, trinaquadalloy, estalt) and one per plasma (argon, magmatic, oxygen). Pipez fluid pipes with pump covers into dedicated hatches of the Hell Forge. Never mix two alloy recipes in the same hatch. — `functionalstorage:oak_1`, `gtceu:mythril_bucket`, `gtceu:adamantine_bucket`
2. Hell Forge: the recipe follows the fluids you feed (all three use circuit 3; the boosted versions use circuit 13 and one infernal catalyst per ingot). Run mythrolic first: you need 8 plates per hull. Plasma leaves through an output hatch into a UHV drum with Keep Exact so it never blocks the forge. — `start_core:hellforge`, `gtceu:mythrolic_alloy_plasma_bucket`
3. Cryostate Quantum Chiller: plasma + BEC oganesson in, molten alloy and oganesson out; oganesson returns to the BEC loop (uev\_chiller). 144 mB per recipe, so use a parallel hatch if you have one. — `gtceu:cryostate_quantum_chiller`, `gtceu:bec_og_bucket`
4. Vacuum Freezer (UV): molten alloy + 500 mB superstate helium 3, ingot casting mold in the controller slot (not consumed). Helium 3 out goes back to the quantum cooling that makes superstate helium 3. — `gtceu:vacuum_freezer`, `gtceu:ingot_casting_mold`, `gtceu:superstate_helium_3_bucket`
5. Ingots to three drawers Keep Exact 64. Their plates, frames and gears come from LV benders and lathes like any other metal. — `functionalstorage:oak_1`, `gtceu:mythrolic_alloy_ingot`, `gtceu:starium_alloy_ingot`, `gtceu:magmada_alloy_ingot`
6. By-product: tiny hellfire ash dust per ingot to a dust drawer (Unverified: 9 tiny make 1 hellfire ash dust); the manifold centrifuge (VHA\[ZPM\]) splits hellfire ash dust into dark ash, netherrack dust, uvarovite, mica and biotite plus 25 mB infernal tar, and infernal tar goes through a second manifold centrifuge into infernal concentrate (hellforge.js). — `gtceu:tiny_hellfire_ash_dust`

## Tips

- Hell Forge (kjs systems/hellforge.js, hellForgeMat): every alloy is made as PLASMA. Mythrolic alloy: 11 ingots = 1584 mB argon plasma + 720 mB mythril + 576 mB HSS-S + 288 mB darmstadtium (circuit 3), 9592 ticks (479.6 s), 3 932 160 EU/t (VHA\[UEV\]), heat requirement 568, output 1584 mB mythrolic alloy plasma + 11 tiny hellfire ash dust. Magmada alloy: 8 ingots = 1152 mB magmatic plasma + 576 adamantine + 144 neutronium + 432 RTM alloy, 8384 ticks, heat 708. Starium alloy: 8 ingots = 1152 mB oxygen plasma + 576 nether star concentrate + 288 trinaquadalloy + 288 estalt, 6368 ticks, heat 633. The same recipes with infernal catalysts (1 per ingot, circuit +10): 85 % of the time and 125 % of the plasma.
- Cooling (systems/cryostate\_quantum\_chiller.js, material15000PlusAlloy): the vacuum freezer recipe of each alloy is REMOVED and replaced by two steps. (1) Cryostate Quantum Chiller (quantum\_cooling): 144 mB alloy plasma + 250 mB BEC oganesson → 144 mB molten alloy + 200 mB oganesson, duration = seconds x 6 ticks (mythrolic 221 ticks, magmada 295, starium 177), 3 932 160 EU/t (VHA\[UEV\]). (2) Vacuum Freezer at UV (491 520 EU/t): 144 mB molten alloy + 500 mB superstate helium 3 + non-consumed ingot casting mold → 1 ingot + 250 mB helium 3, 36.9 s (mythrolic), 49.2 s (magmada), 29.55 s (starium). A zalloyic fluid mold instead of the ingot mold gives the liquid alloy (used for pipes and multiblock fluid feeds).
- Modes (verified): the Hell Forge has NO cooled mode; each alloy has a normal recipe and a \_boosted one (one catalyst per ingot: 85 % of the time, 125 % of the plasma). The two modes people talk about belong to the Cryostate Quantum Chiller (quantum\_cooling and vacuum\_freezer, see uev\_chiller). Hell Forge fuel chain (hellforge.js): crude infernal concentrate (Nether vein) -&gt; Cyclonic Sifter (VHA\[UHV\], 1150 ticks, ancient netherite reinforced mesh, 50 000 -&gt; 15 000 mB infernal concentrate) -&gt; Heat Chamber superheated infernal concentrate (VA\[UEV\], 640 ticks, 950 infernal + 50 utopian akreyrium) -&gt; Injection Mixer sub-stellar infernal concentrate (VHA\[UEV\], 7500 superheated + 36 borealic concentrate -&gt; 5000). Heating solvents: flamewake solvent (pressure heat chamber, 50 000 superheated -&gt; 5000, VA\[UV\] x 4 = 1 966 080 EU/t) and emberheart nectar (50 000 sub-stellar -&gt; 5000, VA\[UV\] x 16 = 7 864 320 EU/t); the Molten Destabiliser upgrades them to cinderbrew solvent and corefire nectar (returns 70 000 of the original + 5000 infernal). Catalysts (96 per craft): ascendant (1 UHV circuit), infernal (1 UEV), abyssal (1 UIV). The forge loses 5 MK per 10 s and every 450 MK above the recipe requirement gives 2^n absolute parallels. Unverified: the MK cap of each solvent.
- Ingredients (earlier tiers): mythril = nether magma line (uev\_nether), HSS-S and darmstadtium (UV/UHV), adamantine (uev\_nether), neutronium, RTM alloy (IV), nether star concentrate (IV line), trinaquadalloy (ZPM naquadah products), estalt (uev\_nether). Plasma gases: argon and oxygen from air separation, magmatic plasma: Unverified source.
- What the alloys are for (tier\_data.js): mythrolic = UEV plate, hull, casing, pipe; starium = UEV primary (frames, rods, rings, bolts, gears); magmada = UEV secondary (gears, rotors, screws, rings). So one UEV hull needs 8 mythrolic plates, while the UEV component parts and components eat starium and magmada in large numbers (counts in uev\_parts and uev\_components). The pack gives no ratio: size the Hell Forge runs from those lists.
- Sub-steps people skip: (1) tiny hellfire ash dust is a by-product: void or centrifuge it (hellfire\_ash\_decomposition) so the output bus does not jam; (2) BEC oganesson is not consumed fully (250 in, 200 oganesson out): the loop needs a start stock (uev\_chiller); (3) superstate helium 3 comes back as helium 3: keep the loop closed; (4) one batch of plasma is 1584 mB for mythrolic: use a UEV-size tank (UHV drum) so the chiller does not stall mid-batch.
- **Unverified** the meaning of the heat values (568, 708, 633) in this fork's Hell Forge, which hatches the plasma needs, and the plasma gas sources.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:hellforge` | 1 |
| `gtceu:cryostate_quantum_chiller` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Feeds:** [UEV Machine Hull: 8 mythrolic alloy plates → casing, + 2 cerium tritelluride single cables + 288 mB PEDOT:PSS plastic](uev_hull.md)
- **Main source for:** `gtceu:mythrolic_alloy_ingot`, `gtceu:starium_alloy_ingot`, `gtceu:magmada_alloy_ingot`
