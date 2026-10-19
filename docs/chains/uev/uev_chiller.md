---
kind: chain
id: uev_chiller
order: 2110
data:
  t: |-
    Cryostate Quantum Chiller coolants: superstate helium 3 → BEC oganesson (the loop that freezes every UEV and UIV alloy)
  inf: true
  "n":
    - - g1
      - "5000 mB helium 3 + 5000 mB liquid helium"
      - g
      - functionalstorage:oak_1
      - [[Helium 3, "gtceu:helium_3_bucket"], [Liquid helium, "gtceu:liquid_helium_bucket"]]
    - [q1, "Quantum cooling · 20 s · 491 520 EU/t", m, "gtceu:cryostate_quantum_chiller"]
    - [ss, "5000 mB superstate helium 3 (+ 2500 mB helium)", f, "gtceu:superstate_helium_3_bucket"]
    - - g2
      - "500 mB oganesson plasma + 5000 mB liquid helium"
      - g
      - functionalstorage:oak_1
      - [[Oganesson plasma, "gtceu:oganesson_plasma_bucket"], [Liquid helium, "gtceu:liquid_helium_bucket"]]
    - [q2, "Quantum cooling · 4 s · 7 864 320 EU/t", m, "gtceu:cryostate_quantum_chiller"]
    - [og, "500 mB oganesson (+ 2500 mB helium)", f, "gtceu:oganesson_bucket"]
    - - q3
      - Quantum cooling · 16 s · 983 040 EU/t · 500 mB oganesson + 7500 mB superstate helium 3
      - m
      - gtceu:cryostate_quantum_chiller
    - [bec, "500 mB BEC oganesson (+ 5000 mB helium 3)", f, "gtceu:bec_og_bucket"]
    - - al
      - |-
        Alloy cooling: 250 mB BEC per 144 mB plasma (uev_alloys, uiv_alloys)
      - o
      - gtceu:cryostate_quantum_chiller
  e:
    - [g1, q1, "1"]
    - [q1, ss, "5000 / 20 s"]
    - [g2, q2, "1"]
    - [q2, og, "500 / 4 s"]
    - [og, q3, "500"]
    - [ss, q3, "7500"]
    - [q3, bec, "500 / 16 s"]
    - [bec, al, "250 / recipe"]
  tips:
    - |-
      Source: kjs systems/cryostate_quantum_chiller.js (recipe type quantum_cooling). Superstate helium 3: 5000 mB helium 3 + 5000 mB liquid helium → 5000 mB superstate helium 3 + 2500 mB helium, 400 ticks, VA[UV] = 491 520 EU/t. Oganesson: 500 mB oganesson plasma + 5000 mB liquid helium → 500 mB oganesson + 2500 mB helium, 80 ticks, VA[UEV] = 7 864 320 EU/t. BEC oganesson: 500 mB oganesson + 7500 mB superstate helium 3 → 500 mB BEC oganesson + 5000 mB helium 3, 320 ticks, VHA[UHV] = 983 040 EU/t.
    - |-
      The alloy step (uev_alloys) consumes 250 mB BEC oganesson per 144 mB of plasma and returns 200 mB oganesson, so the loop LOSES 50 mB oganesson per 144 mB of alloy (about 0.35 mB per mB of molten alloy): the oganesson plasma for the first step is the real input. Oganesson plasma is a fusion product (fusion_scaling.js): 144 mB fermium + 360 mB selenium → 1500 mB oganesson plasma, reflector tier 5, 61 440 EU/t, 7.2 s, start energy 800 MEU. Fermium and selenium sources: Unverified.
    - |-
      The two modes of the Cryostate Quantum Chiller (verified, recipeTypes quantum_cooling + vacuum_freezer): mode 1 quantum_cooling = plasma 144 + BEC oganesson 250 -> molten 144 + oganesson 200 (VHA[UEV] = 3 932 160 EU/t, duration = seconds x 6 ticks); mode 2 vacuum_freezer = molten alloy + 500 mB superstate helium 3 -> ingot or liquid (VA[UV] = 491 520 EU/t), used only for alloys above 15 000 K. The Hell Forge is a different machine with normal and boosted recipes. Coolant chain: liquid helium + helium 3 -> superstate helium 3 (VA[UV]); oganesson plasma + liquid helium -> oganesson (VA[UEV]); oganesson + superstate -> BEC oganesson (VHA[UHV]). Controller (nether_multis.js): VA[UEV], 12 UEV circuits, 24 UHV pumps, 32 UHV field generators, 1 000 000 mB liquid helium + 60 000 mB utopian akreyrium.
    - |-
      Exotic Gas Siphon [EGS] (verified): Assembly Line VHA[UEV] = 3 932 160 EU/t, 2400 ticks, UHV gas collector + 8 UHV circuits + 64 UEPIC chips; three modes (exotic_gas_siphon, gas_collector, void_gas_collector). The siphon mode gives gases already distilled per dimension (Overworld per run: 140 000 mB N2 + 44 000 O2 + 10 000 CO2 + 4000 He + 2000 Ar, VA[ZPM], 1000 ticks; Abydos, Nether and End are analogous). No EGS recipe makes ender air: it is mixed, 3 netherrack dust + 32 000 mB air -> 24 000 mB nether air, then 3 endstone dust + 32 000 mB nether air -> 24 000 mB ender air (HV mixer, 1200 ticks; netherrack and endstone from the LCR recipes easy_netherrack / easy_endstone). The biggest sink is True Absolute Chorus, 5 000 000 mB (5000 buckets) per craft.
    - |-
      Helium: liquid helium and helium 3 come from the exotic gas siphon (Abydos: 32 B helium 3 and 9 B deuterium per run; the Nether: 5 B helium 3 per run; VA[ZPM], 1000 ticks) and from distillation: Unverified exact liquid helium route. The Chiller itself needs 1 000 000 mB liquid helium in its recipe, so helium is the other limiting resource of this era.
    - |-
      Moulds: a zalloyic fluid mold (UV bender circuit 4, 16 dense zalloy plates → empty mold, 900 ticks; then ZPM forming press with a cylinder casting mold, 480 ticks) lets the vacuum freezer produce LIQUID alloy instead of ingots; the ingot casting mold is enough for ingots (uev_alloys).
    - |-
      Sub-steps people skip: (1) three different recipes run on one machine: use three input hatch groups or the recipe locks; (2) helium 3 returns from the BEC step and from the alloy freezer: pipe it back into the superstate step; (3) keep a start stock of oganesson: the loop loses about 50 mB per 144 mB of alloy.
    - |-
      Unverified: fermium, selenium and liquid helium supply chains; exact hatch counts of the chiller.
  b:
    - ["gtceu:cryostate_quantum_chiller", 1]
    - ["gtceu:uhv_input_hatch", 4]
    - ["gtceu:uhv_output_hatch", 4]
    - ["functionalstorage:oak_1", 4]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 8]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:helium_3_bucket", "gtceu:liquid_helium_bucket"]
      t: |-
        Drums first: helium 3, liquid helium, oganesson plasma, superstate helium 3, oganesson, BEC oganesson, helium. One Pipez fluid pipe with a pump cover per drum into its own UHV fluid hatch.
    - i: ["gtceu:cryostate_quantum_chiller", "gtceu:superstate_helium_3_bucket"]
      t: Run superstate helium 3 first (20 s per 5 B at 491 520 EU/t). It is the input of BEC oganesson and of every ingot freezer run.
    - i: ["gtceu:cryostate_quantum_chiller", "gtceu:oganesson_bucket"]
      t: |-
        Oganesson from the plasma: 4 s per 500 mB. Keep a buffer drum of at least 5 B so the BEC step never starves.
    - i: ["gtceu:cryostate_quantum_chiller", "gtceu:bec_og_bucket"]
      t: |-
        BEC oganesson: 16 s per 500 mB. Keep Exact on the BEC drum so the alloy runs can pull 250 mB each time.
    - i: ["gtceu:helium_3_bucket"]
      t: |-
        Return lines: helium 3 from both the BEC step and the alloy freezer goes back into the superstate drum; plain helium goes to a separate tank.
---
# Cryostate Quantum Chiller coolants: superstate helium 3 → BEC oganesson (the loop that freezes every UEV and UIV alloy)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_chiller` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [Hell Forge, Chiller and UEV alloys](../../plan/p18.md#uevforge)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-q1">
<div class="gt-head"><span class="gt-mname">Quantum cooling · 20 s · 491 520 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="5000 mB helium 3 + 5000 mB liquid helium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">5000 mB helium 3 + 5000 mB liquid helium</span><span class="gt-sub"><span>Helium 3</span><span>Liquid helium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="5000 mB superstate helium 3 (+ 2500 mB helium) (gtceu:superstate_helium_3_bucket) - 5000 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__superstate_helium_3_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superstate Helium 3</span><span class="gt-note">5000 mB superstate helium 3 (+ 2500 mB helium)</span><b class="gt-q">5000</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cryostate_quantum_chiller</code></div>
</div>
<div class="gt-panel t-mod" id="m-q2">
<div class="gt-head"><span class="gt-mname">Quantum cooling · 4 s · 7 864 320 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="500 mB oganesson plasma + 5000 mB liquid helium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">500 mB oganesson plasma + 5000 mB liquid helium</span><span class="gt-sub"><span>Oganesson plasma</span><span>Liquid helium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="500 mB oganesson (+ 2500 mB helium) (gtceu:oganesson_bucket) - 500 / 4 s"><img class="gt-ico" src="../../assets/icons/gtceu__oganesson_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oganesson</span><span class="gt-note">500 mB oganesson (+ 2500 mB helium)</span><b class="gt-q">500</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cryostate_quantum_chiller</code></div>
</div>
<div class="gt-panel t-mod" id="m-q3">
<div class="gt-head"><span class="gt-mname">Quantum cooling · 16 s · 983 040 EU/t · 500 mB oganesson + 7500 mB superstate helium 3</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="500 mB oganesson (+ 2500 mB helium) (gtceu:oganesson_bucket) - 500"><img class="gt-ico" src="../../assets/icons/gtceu__oganesson_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oganesson</span><span class="gt-note">500 mB oganesson (+ 2500 mB helium)</span><b class="gt-q">500</b></span><span class="gt-slot gt-fluid" title="5000 mB superstate helium 3 (+ 2500 mB helium) (gtceu:superstate_helium_3_bucket) - 7500"><img class="gt-ico" src="../../assets/icons/gtceu__superstate_helium_3_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superstate Helium 3</span><span class="gt-note">5000 mB superstate helium 3 (+ 2500 mB helium)</span><b class="gt-q">7500</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="500 mB BEC oganesson (+ 5000 mB helium 3) (gtceu:bec_og_bucket) - 500 / 16 s"><img class="gt-ico" src="../../assets/icons/gtceu__bec_og_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bec Og</span><span class="gt-note">500 mB BEC oganesson (+ 5000 mB helium 3)</span><b class="gt-q">500</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cryostate_quantum_chiller</code></div>
</div>
</div>

## Flow

- [Quantum cooling · 20 s · 491 520 EU/t](#m-q1) → [Quantum cooling · 16 s · 983 040 EU/t · 500 mB oganesson + 7500 mB superstate helium 3](#m-q3)
- [Quantum cooling · 4 s · 7 864 320 EU/t](#m-q2) → [Quantum cooling · 16 s · 983 040 EU/t · 500 mB oganesson + 7500 mB superstate helium 3](#m-q3)

### Direct steps

- 500 mB BEC oganesson (+ 5000 mB helium 3) → Alloy cooling: 250 mB BEC per 144 mB plasma (uev\_alloys, uiv\_alloys) (250 / recipe)

## How to build

1. Drums first: helium 3, liquid helium, oganesson plasma, superstate helium 3, oganesson, BEC oganesson, helium. One Pipez fluid pipe with a pump cover per drum into its own UHV fluid hatch. — `functionalstorage:oak_1`, `gtceu:helium_3_bucket`, `gtceu:liquid_helium_bucket`
2. Run superstate helium 3 first (20 s per 5 B at 491 520 EU/t). It is the input of BEC oganesson and of every ingot freezer run. — `gtceu:cryostate_quantum_chiller`, `gtceu:superstate_helium_3_bucket`
3. Oganesson from the plasma: 4 s per 500 mB. Keep a buffer drum of at least 5 B so the BEC step never starves. — `gtceu:cryostate_quantum_chiller`, `gtceu:oganesson_bucket`
4. BEC oganesson: 16 s per 500 mB. Keep Exact on the BEC drum so the alloy runs can pull 250 mB each time. — `gtceu:cryostate_quantum_chiller`, `gtceu:bec_og_bucket`
5. Return lines: helium 3 from both the BEC step and the alloy freezer goes back into the superstate drum; plain helium goes to a separate tank. — `gtceu:helium_3_bucket`

## Tips

- Source: kjs systems/cryostate\_quantum\_chiller.js (recipe type quantum\_cooling). Superstate helium 3: 5000 mB helium 3 + 5000 mB liquid helium → 5000 mB superstate helium 3 + 2500 mB helium, 400 ticks, VA\[UV\] = 491 520 EU/t. Oganesson: 500 mB oganesson plasma + 5000 mB liquid helium → 500 mB oganesson + 2500 mB helium, 80 ticks, VA\[UEV\] = 7 864 320 EU/t. BEC oganesson: 500 mB oganesson + 7500 mB superstate helium 3 → 500 mB BEC oganesson + 5000 mB helium 3, 320 ticks, VHA\[UHV\] = 983 040 EU/t.
- The alloy step (uev\_alloys) consumes 250 mB BEC oganesson per 144 mB of plasma and returns 200 mB oganesson, so the loop LOSES 50 mB oganesson per 144 mB of alloy (about 0.35 mB per mB of molten alloy): the oganesson plasma for the first step is the real input. Oganesson plasma is a fusion product (fusion\_scaling.js): 144 mB fermium + 360 mB selenium → 1500 mB oganesson plasma, reflector tier 5, 61 440 EU/t, 7.2 s, start energy 800 MEU. Fermium and selenium sources: Unverified.
- The two modes of the Cryostate Quantum Chiller (verified, recipeTypes quantum\_cooling + vacuum\_freezer): mode 1 quantum\_cooling = plasma 144 + BEC oganesson 250 -&gt; molten 144 + oganesson 200 (VHA\[UEV\] = 3 932 160 EU/t, duration = seconds x 6 ticks); mode 2 vacuum\_freezer = molten alloy + 500 mB superstate helium 3 -&gt; ingot or liquid (VA\[UV\] = 491 520 EU/t), used only for alloys above 15 000 K. The Hell Forge is a different machine with normal and boosted recipes. Coolant chain: liquid helium + helium 3 -&gt; superstate helium 3 (VA\[UV\]); oganesson plasma + liquid helium -&gt; oganesson (VA\[UEV\]); oganesson + superstate -&gt; BEC oganesson (VHA\[UHV\]). Controller (nether\_multis.js): VA\[UEV\], 12 UEV circuits, 24 UHV pumps, 32 UHV field generators, 1 000 000 mB liquid helium + 60 000 mB utopian akreyrium.
- Exotic Gas Siphon \[EGS\] (verified): Assembly Line VHA\[UEV\] = 3 932 160 EU/t, 2400 ticks, UHV gas collector + 8 UHV circuits + 64 UEPIC chips; three modes (exotic\_gas\_siphon, gas\_collector, void\_gas\_collector). The siphon mode gives gases already distilled per dimension (Overworld per run: 140 000 mB N2 + 44 000 O2 + 10 000 CO2 + 4000 He + 2000 Ar, VA\[ZPM\], 1000 ticks; Abydos, Nether and End are analogous). No EGS recipe makes ender air: it is mixed, 3 netherrack dust + 32 000 mB air -&gt; 24 000 mB nether air, then 3 endstone dust + 32 000 mB nether air -&gt; 24 000 mB ender air (HV mixer, 1200 ticks; netherrack and endstone from the LCR recipes easy\_netherrack / easy\_endstone). The biggest sink is True Absolute Chorus, 5 000 000 mB (5000 buckets) per craft.
- Helium: liquid helium and helium 3 come from the exotic gas siphon (Abydos: 32 B helium 3 and 9 B deuterium per run; the Nether: 5 B helium 3 per run; VA\[ZPM\], 1000 ticks) and from distillation: Unverified exact liquid helium route. The Chiller itself needs 1 000 000 mB liquid helium in its recipe, so helium is the other limiting resource of this era.
- Moulds: a zalloyic fluid mold (UV bender circuit 4, 16 dense zalloy plates → empty mold, 900 ticks; then ZPM forming press with a cylinder casting mold, 480 ticks) lets the vacuum freezer produce LIQUID alloy instead of ingots; the ingot casting mold is enough for ingots (uev\_alloys).
- Sub-steps people skip: (1) three different recipes run on one machine: use three input hatch groups or the recipe locks; (2) helium 3 returns from the BEC step and from the alloy freezer: pipe it back into the superstate step; (3) keep a start stock of oganesson: the loop loses about 50 mB per 144 mB of alloy.
- **Unverified** fermium, selenium and liquid helium supply chains; exact hatch counts of the chiller.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:cryostate_quantum_chiller` | 1 |
| `gtceu:uhv_input_hatch` | 4 |
| `gtceu:uhv_output_hatch` | 4 |
| `functionalstorage:oak_1` | 4 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:bec_og_bucket`, `gtceu:superstate_helium_3_bucket`, `gtceu:oganesson_bucket`
