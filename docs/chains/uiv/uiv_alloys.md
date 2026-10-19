---
kind: chain
id: uiv_alloys
order: 2190
data:
  t: |-
    UIV alloys (chaotixic, ohmderblux, abyssal): molten metals + fusion plasma in the Hell Forge → plasma → Chiller → molten → vacuum freezer; abyssal catalyst from the draconic eye
  inf: true
  "n":
    - - g1
      - |-
        Chaotixic (24 ingots): rhexis 864 · stellite 100 288 · hafnium 144 · electrum 1728 · vanadium steel 432 mB + 3456 mB paradox plasma
      - g
      - functionalstorage:oak_1
      - - [Rhexis, "gtceu:rhexis_bucket"]
        - [Stellite 100, "gtceu:stellite_100_bucket"]
        - [Electrum, "gtceu:electrum_bucket"]
        - [Paradox plasma, "gtceu:paradox_plasma_bucket"]
    - - g2
      - |-
        Ohmderblux (23 ingots): chalyblux 720 · maraging steel 300 288 · zirconium 576 · glowstone 1296 · ultimet 432 mB + 3312 mB paradox plasma
      - g
      - functionalstorage:oak_1
      - - [Chalyblux, "gtceu:chalyblux_bucket"]
        - [Maraging steel 300, "gtceu:maraging_steel_300_bucket"]
        - [Ultimet, "gtceu:ultimet_bucket"]
        - [Paradox plasma, "gtceu:paradox_plasma_bucket"]
    - - g3
      - |-
        Abyssal (14 ingots): xeproda 720 · blue alloy 432 · void 576 · flerovium 144 · zapolgium 144 mB + 2016 mB voidic plasma
      - g
      - functionalstorage:oak_1
      - - [Xeproda, "gtceu:xeproda_bucket"]
        - [Blue alloy, "gtceu:blue_alloy_bucket"]
        - [Void, "gtceu:void_bucket"]
        - [Voidic plasma, "gtceu:voidic_plasma_bucket"]
    - - ct
      - |-
        Abyssal catalyst (96 per craft): draconyallium frame · draconic eye · 2 long void rod · UIV circuit · 32 echo shard lens · 704 mB PEDOT:PSS
      - g
      - functionalstorage:oak_1
      - - [Draconyallium frame, "gtceu:draconyallium_frame"]
        - [Draconic eye, "kubejs:draconic_eye"]
        - [Echo shard lens, "gtceu:echo_shard_lens"]
    - [hf, "Hell Forge · 15 728 640 EU/t · 9 to 17 min per run", m, "start_core:hellforge"]
    - [pl, "Alloy plasma (144 mB per ingot)", f, "gtceu:chaotixic_alloy_plasma_bucket"]
    - [qc, "Cryostate Quantum Chiller + BEC oganesson (uev_chiller)", m, "gtceu:cryostate_quantum_chiller"]
    - [vf, "Vacuum Freezer + superstate helium 3 + ingot mold", m, "gtceu:vacuum_freezer"]
    - [o1, "Chaotixic alloy ingot (UIV hull and parts)", o, "gtceu:chaotixic_alloy_ingot"]
    - [o2, "Ohmderblux alloy ingot (UIV primary)", o, "gtceu:ohmderblux_alloy_ingot"]
    - [o3, "Abyssal alloy ingot (UIV secondary)", o, "gtceu:abyssal_alloy_ingot"]
  e:
    - [g1, hf, "24"]
    - [g2, hf, "23"]
    - [g3, hf, "14"]
    - [ct, hf, "1 / ingot"]
    - [hf, pl, "144 mB / ingot"]
    - [pl, qc, "144 mB"]
    - [qc, vf, molten]
    - [vf, o1, "1"]
    - [vf, o2, "1"]
    - [vf, o3, "1"]
  tips:
    - |-
      Hell Forge (kjs systems/hellforge.js): all three at VHA[UIV] = 15 728 640 EU/t with the ABYSSAL catalyst class (boosted: 1 catalyst per ingot, +10 to the circuit, 85 % time, 125 % plasma). Chaotixic alloy: 24 ingots, 3456 mB paradox plasma + 864 rhexis + 288 stellite 100 + 144 hafnium + 1728 electrum + 432 vanadium steel (circuit 5), 20 976 ticks (17.5 min), heat 1472. Ohmderblux alloy: 23 ingots, 3312 mB paradox plasma + 720 chalyblux + 288 maraging steel 300 + 576 zirconium + 1296 glowstone + 432 ultimet, 21 574 ticks (18 min), heat 1351. Abyssal alloy: 14 ingots, 2016 mB voidic plasma + 720 xeproda + 432 blue alloy + 576 void + 144 flerovium + 144 zapolgium, 10 780 ticks (9 min), heat 1586. Also made here: nyanium (VA[UHV], 14 ingots, nitrogen plasma, ascendant catalyst, 76.8 s each) and rhenate w (VA[UIV], 33 ingots, tin plasma, ascendant catalyst) = the pipe and coil metals of the UIV tier.
    - |-
      Cooling is the same two steps as uev_alloys: Chiller (144 mB plasma + 250 mB BEC oganesson, duration = seconds x 6 ticks: abyssal 61.5 s → 369 ticks, chaotixic 29.25 s → 176, ohmderblux 22.95 s → 138; VHA[UEV]) then Vacuum Freezer at UV with 500 mB superstate helium 3 (61.5, 29.25 and 22.95 s per ingot). Abyssal catalyst (assembler, 600 ticks, 15 728 640 EU/t = VHA[UV] x 4^3): draconyallium frame + draconic eye + 2 long void rods + 1 UIV circuit + 32 echo shard lenses + 704 mB PEDOT:PSS gives 96 catalysts: one eye per 96 ingots of boost.
    - |-
      Plasma (fusion_scaling.js, reflector tier 6 = draconic reflector casing, uiv_fusion): paradox plasma = 200 mB chaos centric void + 200 mB order centric void → 144 mB, 294 912 EU/t, 16.2 s, start 900 MEU; voidic plasma = 432 mB echo r + 144 mB void → 144 mB, 344 064 EU/t, 19.2 s, start 1040 MEU; preon plasma (draco abyssal, rhenium composite) = 500 mB utopian akreyrium + 50 mB dragon breath → 144 mB, 688 128 EU/t, 9.6 s, start 1160 MEU. Chaos and order centric void and echo r: Unverified (not traced).
    - |-
      Hidden gates: (1) the UEV superconductor wire (enriched pallarovium alloy: UEV field generator, catalyst core and fusion reactor) is made in the Hell Forge at VHA[UIV] too (17 ingots, nickel plasma, infernal catalyst, heat 878): so the UEV field generator line needs UIV power. (2) The UIV superconductor (rhenium super composite alloy, in the UIV field generator and catalyst core) is a Hell Forge recipe at VHA[UXV] = 62 914 560 EU/t with preon plasma and abyssal catalyst, heat 1723. A UIV 4096A laser target hatch carries it, but it is the first thing in the guide that is clearly UXV-priced. (3) Draconyallium (frames, foils, rods) is a 258-ingot recipe (duranium 9792 + silver 2880 + oxygen/nitrogen plasma 94 000 / 76 000 mB + dragon breath 25 800 mB, 16 s per ingot, VA[UIV]).
    - |-
      Sub-steps people skip: (1) paradox plasma serves two alloys: keep it in a big drum; (2) a 17.5-minute run at 15.7 M EU/t needs a stable power line: size the buffer before you start; (3) the forge can only hold one recipe: run chaotixic first, it is the plate, hull and casing material; (4) only the boosted recipe gives 125 % plasma and 85 % of the time, at the price of 1 catalyst per ingot.
    - |-
      Unverified: xeproda, rhexis, chalyblux, stellite 100, blue alloy, zapolgium sources; the real heat meaning; whether VHA[UXV] recipes run with UIV hatches.
  b:
    - ["start_core:hellforge", 1]
    - ["gtceu:cryostate_quantum_chiller", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 14]
    - ["gtceu:steel_drum", 14]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:draconic_eye", "gtceu:echo_shard_lens"]
      t: |-
        Catalyst first: assembler with draconyallium frame, one eye, long void rods, a UIV circuit, 32 echo shard lenses and PEDOT:PSS gives 96 abyssal catalysts. Drawer Keep Exact 96.
    - i: ["start_core:hellforge", "gtceu:paradox_plasma_bucket"]
      t: |-
        Hell Forge: one drum per input metal and per plasma; the fluids you feed pick the alloy. Chaotixic first (plates, hull, casing). Plasma out to a UHV drum with Keep Exact.
    - i: ["gtceu:cryostate_quantum_chiller", "gtceu:bec_og_bucket"]
      t: |-
        Chiller: plasma + BEC oganesson (uev_chiller). 144 mB per recipe, so use a parallel hatch for the 3456 mB batch.
    - i: ["gtceu:vacuum_freezer", "gtceu:ingot_casting_mold"]
      t: Vacuum Freezer with the ingot casting mold and 500 mB superstate helium 3 per 144 mB. Ingots into three drawers Keep Exact 64.
    - i: ["functionalstorage:oak_1", "gtceu:chaotixic_alloy_ingot"]
      t: |-
        Check power before every run: 15.7 M EU/t for 17 minutes; use a power substation or laser buffer so the batch does not stop.
---
# UIV alloys (chaotixic, ohmderblux, abyssal): molten metals + fusion plasma in the Hell Forge → plasma → Chiller → molten → vacuum freezer; abyssal catalyst from the draconic eye

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV alloys](../../plan/p19.md#uivalloys)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-hf">
<div class="gt-head"><span class="gt-mname">Hell Forge · 15 728 640 EU/t · 9 to 17 min per run</span><span class="gt-badge t-mod">StarT</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Chaotixic (24 ingots): rhexis 864 · stellite 100 288 · hafnium 144 · electrum 1728 · vanadium steel 432 mB + 3456 mB paradox plasma (functionalstorage:oak_1) - 24"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Chaotixic (24 ingots): rhexis 864 · stellite 100 288 · hafnium 144 · electrum 1728 · vanadium steel 432 mB + 3456 mB paradox plasma</span><span class="gt-sub"><span>Rhexis</span><span>Stellite 100</span><span>Electrum</span><span>Paradox plasma</span></span><b class="gt-q">24</b></span><span class="gt-slot gt-group" title="Ohmderblux (23 ingots): chalyblux 720 · maraging steel 300 288 · zirconium 576 · glowstone 1296 · ultimet 432 mB + 3312 mB paradox plasma (functionalstorage:oak_1) - 23"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Ohmderblux (23 ingots): chalyblux 720 · maraging steel 300 288 · zirconium 576 · glowstone 1296 · ultimet 432 mB + 3312 mB paradox plasma</span><span class="gt-sub"><span>Chalyblux</span><span>Maraging steel 300</span><span>Ultimet</span><span>Paradox plasma</span></span><b class="gt-q">23</b></span><span class="gt-slot gt-group" title="Abyssal (14 ingots): xeproda 720 · blue alloy 432 · void 576 · flerovium 144 · zapolgium 144 mB + 2016 mB voidic plasma (functionalstorage:oak_1) - 14"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Abyssal (14 ingots): xeproda 720 · blue alloy 432 · void 576 · flerovium 144 · zapolgium 144 mB + 2016 mB voidic plasma</span><span class="gt-sub"><span>Xeproda</span><span>Blue alloy</span><span>Void</span><span>Voidic plasma</span></span><b class="gt-q">14</b></span><span class="gt-slot gt-group" title="Abyssal catalyst (96 per craft): draconyallium frame · draconic eye · 2 long void rod · UIV circuit · 32 echo shard lens · 704 mB PEDOT:PSS (functionalstorage:oak_1) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Abyssal catalyst (96 per craft): draconyallium frame · draconic eye · 2 long void rod · UIV circuit · 32 echo shard lens · 704 mB PEDOT:PSS</span><span class="gt-sub"><span>Draconyallium frame</span><span>Draconic eye</span><span>Echo shard lens</span></span><b class="gt-q">1 / ingot</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__hellforge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Alloy plasma (144 mB per ingot) (gtceu:chaotixic_alloy_plasma_bucket) - 144 mB / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__chaotixic_alloy_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chaotixic Alloy Plasma</span><span class="gt-note">Alloy plasma (144 mB per ingot)</span><b class="gt-q">144 mB / ingot</b></span></div>
</div>
<div class="gt-foot"><code>start_core:hellforge</code></div>
</div>
<div class="gt-panel t-mod" id="m-qc">
<div class="gt-head"><span class="gt-mname">Cryostate Quantum Chiller + BEC oganesson (uev_chiller)</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Alloy plasma (144 mB per ingot) (gtceu:chaotixic_alloy_plasma_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__chaotixic_alloy_plasma_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chaotixic Alloy Plasma</span><span class="gt-note">Alloy plasma (144 mB per ingot)</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-vf" title="Vacuum Freezer + superstate helium 3 + ingot mold (gtceu:vacuum_freezer) - molten"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer + superstate helium 3 + ingot mold</span><b class="gt-q">molten</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:cryostate_quantum_chiller</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer + superstate helium 3 + ingot mold</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-qc" title="Cryostate Quantum Chiller + BEC oganesson (uev_chiller) (gtceu:cryostate_quantum_chiller) - molten"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cryostate Quantum Chiller</span><span class="gt-note">Cryostate Quantum Chiller + BEC oganesson (uev_chiller)</span><b class="gt-q">molten</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Chaotixic alloy ingot (UIV hull and parts) (gtceu:chaotixic_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chaotixic_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chaotixic Alloy Ingot</span><span class="gt-note">Chaotixic alloy ingot (UIV hull and parts)</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Ohmderblux alloy ingot (UIV primary) (gtceu:ohmderblux_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ohmderblux_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ohmderblux Alloy Ingot</span><span class="gt-note">Ohmderblux alloy ingot (UIV primary)</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Abyssal alloy ingot (UIV secondary) (gtceu:abyssal_alloy_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__abyssal_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Abyssal Alloy Ingot</span><span class="gt-note">Abyssal alloy ingot (UIV secondary)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
</div>

## Flow

- [Hell Forge · 15 728 640 EU/t · 9 to 17 min per run](#m-hf) → [Cryostate Quantum Chiller + BEC oganesson (uev\_chiller)](#m-qc) → [Vacuum Freezer + superstate helium 3 + ingot mold](#m-vf)

## How to build

1. Catalyst first: assembler with draconyallium frame, one eye, long void rods, a UIV circuit, 32 echo shard lenses and PEDOT:PSS gives 96 abyssal catalysts. Drawer Keep Exact 96. — `functionalstorage:oak_1`, `kubejs:draconic_eye`, `gtceu:echo_shard_lens`
2. Hell Forge: one drum per input metal and per plasma; the fluids you feed pick the alloy. Chaotixic first (plates, hull, casing). Plasma out to a UHV drum with Keep Exact. — `start_core:hellforge`, `gtceu:paradox_plasma_bucket`
3. Chiller: plasma + BEC oganesson (uev\_chiller). 144 mB per recipe, so use a parallel hatch for the 3456 mB batch. — `gtceu:cryostate_quantum_chiller`, `gtceu:bec_og_bucket`
4. Vacuum Freezer with the ingot casting mold and 500 mB superstate helium 3 per 144 mB. Ingots into three drawers Keep Exact 64. — `gtceu:vacuum_freezer`, `gtceu:ingot_casting_mold`
5. Check power before every run: 15.7 M EU/t for 17 minutes; use a power substation or laser buffer so the batch does not stop. — `functionalstorage:oak_1`, `gtceu:chaotixic_alloy_ingot`

## Tips

- Hell Forge (kjs systems/hellforge.js): all three at VHA\[UIV\] = 15 728 640 EU/t with the ABYSSAL catalyst class (boosted: 1 catalyst per ingot, +10 to the circuit, 85 % time, 125 % plasma). Chaotixic alloy: 24 ingots, 3456 mB paradox plasma + 864 rhexis + 288 stellite 100 + 144 hafnium + 1728 electrum + 432 vanadium steel (circuit 5), 20 976 ticks (17.5 min), heat 1472. Ohmderblux alloy: 23 ingots, 3312 mB paradox plasma + 720 chalyblux + 288 maraging steel 300 + 576 zirconium + 1296 glowstone + 432 ultimet, 21 574 ticks (18 min), heat 1351. Abyssal alloy: 14 ingots, 2016 mB voidic plasma + 720 xeproda + 432 blue alloy + 576 void + 144 flerovium + 144 zapolgium, 10 780 ticks (9 min), heat 1586. Also made here: nyanium (VA\[UHV\], 14 ingots, nitrogen plasma, ascendant catalyst, 76.8 s each) and rhenate w (VA\[UIV\], 33 ingots, tin plasma, ascendant catalyst) = the pipe and coil metals of the UIV tier.
- Cooling is the same two steps as uev\_alloys: Chiller (144 mB plasma + 250 mB BEC oganesson, duration = seconds x 6 ticks: abyssal 61.5 s → 369 ticks, chaotixic 29.25 s → 176, ohmderblux 22.95 s → 138; VHA\[UEV\]) then Vacuum Freezer at UV with 500 mB superstate helium 3 (61.5, 29.25 and 22.95 s per ingot). Abyssal catalyst (assembler, 600 ticks, 15 728 640 EU/t = VHA\[UV\] x 4^3): draconyallium frame + draconic eye + 2 long void rods + 1 UIV circuit + 32 echo shard lenses + 704 mB PEDOT:PSS gives 96 catalysts: one eye per 96 ingots of boost.
- Plasma (fusion\_scaling.js, reflector tier 6 = draconic reflector casing, uiv\_fusion): paradox plasma = 200 mB chaos centric void + 200 mB order centric void → 144 mB, 294 912 EU/t, 16.2 s, start 900 MEU; voidic plasma = 432 mB echo r + 144 mB void → 144 mB, 344 064 EU/t, 19.2 s, start 1040 MEU; preon plasma (draco abyssal, rhenium composite) = 500 mB utopian akreyrium + 50 mB dragon breath → 144 mB, 688 128 EU/t, 9.6 s, start 1160 MEU. Chaos and order centric void and echo r: Unverified (not traced).
- Hidden gates: (1) the UEV superconductor wire (enriched pallarovium alloy: UEV field generator, catalyst core and fusion reactor) is made in the Hell Forge at VHA\[UIV\] too (17 ingots, nickel plasma, infernal catalyst, heat 878): so the UEV field generator line needs UIV power. (2) The UIV superconductor (rhenium super composite alloy, in the UIV field generator and catalyst core) is a Hell Forge recipe at VHA\[UXV\] = 62 914 560 EU/t with preon plasma and abyssal catalyst, heat 1723. A UIV 4096A laser target hatch carries it, but it is the first thing in the guide that is clearly UXV-priced. (3) Draconyallium (frames, foils, rods) is a 258-ingot recipe (duranium 9792 + silver 2880 + oxygen/nitrogen plasma 94 000 / 76 000 mB + dragon breath 25 800 mB, 16 s per ingot, VA\[UIV\]).
- Sub-steps people skip: (1) paradox plasma serves two alloys: keep it in a big drum; (2) a 17.5-minute run at 15.7 M EU/t needs a stable power line: size the buffer before you start; (3) the forge can only hold one recipe: run chaotixic first, it is the plate, hull and casing material; (4) only the boosted recipe gives 125 % plasma and 85 % of the time, at the price of 1 catalyst per ingot.
- **Unverified** xeproda, rhexis, chalyblux, stellite 100, blue alloy, zapolgium sources; the real heat meaning; whether VHA\[UXV\] recipes run with UIV hatches.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:hellforge` | 1 |
| `gtceu:cryostate_quantum_chiller` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 14 |
| `gtceu:steel_drum` | 14 |

## Needs / Feeds

- **Feeds:** [UIV Machine Hull: 8 chaotixic alloy plates → casing, + 2 polonium bismide single cables + 288 mB PEDOT:PSS plastic](uiv_hull.md)
- **Main source for:** `gtceu:chaotixic_alloy_ingot`, `gtceu:ohmderblux_alloy_ingot`, `gtceu:abyssal_alloy_ingot`
