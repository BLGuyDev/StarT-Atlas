---
kind: chain
id: uv_polyimide
order: 1600
data:
  t: |-
    Polyimide: 12 reactions (maleic anhydride, BTDA, NMP, phenylenediamine, polyamic acid) - needs UV-tier Large Chemical Reactors for the last two steps
  inf: true
  "n":
    - - g
      - Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel)
      - g
      - functionalstorage:oak_1
      - - [Benzene, "gtceu:benzene_bucket"]
        - [Methanol, "gtceu:methanol_bucket"]
        - [Ammonia, "gtceu:ammonia_bucket"]
        - [Nitrobenzene, "gtceu:nitrobenzene_bucket"]
        - [Palladium on carbon dust, "gtceu:palladium_on_carbon_dust"]
    - - m1
      - LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride
      - m
      - gtceu:large_chemical_reactor
    - [m2, "LCR · circuit 0 · 29 s · 15 360 EU/t → 1 B benzophenone", m, "gtceu:large_chemical_reactor"]
    - [m3, "LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust", m, "gtceu:large_chemical_reactor"]
    - [m4, "HV Chemical Reactor · circuit 1 · 45 s → 1 B methylamine", m, "gtceu:hv_chemical_reactor"]
    - [m5, "LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate", m, "gtceu:large_chemical_reactor"]
    - [m6, "LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate", m, "gtceu:large_chemical_reactor"]
    - - m7
      - LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol
      - m
      - gtceu:large_chemical_reactor
    - [m8, "LCR · 19 s · 122 880 EU/t → 1 B butyrolactone", m, "gtceu:large_chemical_reactor"]
    - [m9, "LCR · 22 s · 122 880 EU/t → 16 NMP dust", m, "gtceu:large_chemical_reactor"]
    - [m10, "LCR · 36 s · 30 720 EU/t · nickel → 3 B phenylenediamine", m, "gtceu:large_chemical_reactor"]
    - [m11, "LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid", m, "gtceu:large_chemical_reactor"]
    - [m12, "LCR · 12 s · 491 520 EU/t (UV) → 4.032 B polyimide", m, "gtceu:large_chemical_reactor"]
  e:
    - [g, m1, "3 B"]
    - [g, m2, "1 B"]
    - [m1, m3, "1 B"]
    - [m2, m3, "2 B"]
    - [g, m4, "NH3 + MeOH"]
    - [m1, m5, "1 B"]
    - [m5, m6, "2 B"]
    - [m6, m7, "4 B"]
    - [m7, m8, "1 B"]
    - [m8, m9, "1 B"]
    - [m4, m9, "1 B"]
    - [g, m10, "3 B"]
    - [m3, m11, "60"]
    - [m9, m11, "16"]
    - [m10, m11, "2 B"]
    - [m11, m12, "4 B"]
  tips:
    - |-
      Source: kjs lines/polymers/polyimide.js (all verified). Tiers: VHA[LuV] = 15 360 EU/t for maleic anhydride and benzophenone, VHA[ZPM] = 61 440 for BTDA and butanediol, VA[ZPM] = 122 880 for dimethyl succinate, butyrolactone and NMP, VHA[UV] = 245 760 for dimethyl maleate and VA[UV] = 491 520 EU/t for polyamic acid and the final polyimide step. The last three need a UV energy hatch on the Large Chemical Reactor (see uv_hatches), so polyimide is the first thing the UV hull is spent on.
    - |-
      Ratios (one end-to-end batch, 4.032 B polyimide): 4 B polyamic acid needs 4/3 of a polyamic run = 80 BTDA dust (1.33 BTDA runs of 60 = 2.67 B benzophenone + 1.33 B maleic anhydride + 2.67 B acetic acid + 18.7 B oxygen), 21.3 NMP (1.33 of 16 = 1.33 B butyrolactone + 1.33 B methylamine) and 2.67 B phenylenediamine. A single living SMD run takes 108 to 288 mB, so one batch makes about 15 to 40 SMD runs (240 to 640 SMDs).
    - |-
      Dimethyl maleate and butanediol come from maleic anhydride: m1 makes 4 B per run and m3 eats 1 B per run, so m1 feeds BTDA (1 B) and dimethyl maleate (1 B per B of dimethyl succinate chain: 2 B per 3 B succinate). Keep the maleic anhydride drum split: Pipez fluid pipes to two valves with Keep Exact, or two output hatches.
    - The 1,4-butanediol step is the only one with a CLEANROOM tag (normal cleanroom); the LCR must sit in one or be a cleanroom-compatible multiblock. The others have none. Note that the sequence of 12 reactions needs 11 different Large Chemical Reactors (m4 is a plain HV chemical reactor).
    - |-
      Sub-steps people skip: (1) catalysts are NOT consumed: put one aluminium dust, one palladium on carbon dust and one nickel dust in the input bus of their reactors and leave them; (2) circuit numbers: m1 3, m2 0, m3 1, m4 1, others none; (3) the water and CO2 outputs must have somewhere to go; (4) nitrobenzene, nitric acid and acetic acid are bought from the earlier chemistry chains; (5) the polyamic acid step also needs 1 B nitric acid per run and gives back 2 B hydrogen.
    - |-
      Unverified: the benzoyl chloride supply from the PEEK chain (uv_peek m2) is shared, so one benzotrichloride line has to feed both polymers; acetic acid, ammonia, nitrobenzene sources.
  b:
    - ["gtceu:large_chemical_reactor", 11]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:uv_energy_input_hatch", 1]
    - ["gtceu:zpm_energy_input_hatch", 2]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 20]
    - ["gtceu:steel_drum", 18]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:palladium_on_carbon_dust", "gtceu:nickel_dust"]
      t: |-
        Drawers: catalysts only (aluminium, Pd on carbon, nickel; Keep Exact 1) plus output drawers for BTDA, NMP. Everything else is a fluid: one drum per reactant and per intermediate, and the hydrogen / oxygen / methanol drums need a refill line.
    - i: ["gtceu:large_chemical_reactor", "gtceu:maleic_anhydride_bucket"]
      t: |-
        Reactor 1 (circuit 3) makes maleic anhydride: 4 B per 26 s. A fluid pipe splits it to the BTDA reactor and the dimethyl maleate reactor, each with a valve.
    - i: ["gtceu:large_chemical_reactor", "gtceu:benzophenone_3344_tetracarboxylic_dianhydride_dust"]
      t: |-
        BTDA reactor (circuit 1, ZPM hatch): 2 B benzophenone + 1 B maleic anhydride + 2 B acetic acid + 14 B oxygen → 60 dust. Output drawer Keep Exact 60.
    - i: ["gtceu:large_chemical_reactor", "gtceu:n_methyl_2_pyrrolidone_dust"]
      t: |-
        NMP branch: dimethyl maleate (UV hatch) → dimethyl succinate (Pd) → butanediol (cleanroom) → butyrolactone → NMP with methylamine from the HV reactor. Five reactors in a row, one drum between each.
    - i: ["gtceu:large_chemical_reactor", "gtceu:uv_energy_input_hatch"]
      t: |-
        UV pair: polyamic acid reactor (60 BTDA + 16 NMP + 2 B phenylenediamine + 1 B nitric acid) and the polyimide reactor (4 B polyamic acid + 2 B ammonia). 491 520 EU/t each; run them on a UV hatch, not an overclock of a lower tier.
    - i: ["functionalstorage:oak_1", "gtceu:polyimide_bucket"]
      t: |-
        Output: polyimide to a drum, Keep Exact 8 B for the five SMD assemblers. Polyimide foil (used by the capacitor SMD) is the GT polymer route: a fluid solidifier makes the plate from the fluid and a bender makes the foil (Unverified: pack changes).
---
# Polyimide: 12 reactions (maleic anhydride, BTDA, NMP, phenylenediamine, polyamic acid) - needs UV-tier Large Chemical Reactors for the last two steps

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_polyimide` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [PEEK, polyimide and UV solder](../../plan/p14.md#uvchem)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel) (functionalstorage:oak_1) - 3 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel)</span><span class="gt-sub"><span>Benzene</span><span>Methanol</span><span>Ammonia</span><span>Nitrobenzene</span><span>Palladium on carbon dust</span></span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">LCR · circuit 0 · 29 s · 15 360 EU/t → 1 B benzophenone</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel) (functionalstorage:oak_1) - 1 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel)</span><span class="gt-sub"><span>Benzene</span><span>Methanol</span><span>Ammonia</span><span>Nitrobenzene</span><span>Palladium on carbon dust</span></span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust</span><b class="gt-q">2 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m2" title="LCR · circuit 0 · 29 s · 15 360 EU/t → 1 B benzophenone (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 0 · 29 s · 15 360 EU/t → 1 B benzophenone</span><b class="gt-q">2 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m11" title="LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid (gtceu:large_chemical_reactor) - 60"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid</span><b class="gt-q">60</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-m4">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · circuit 1 · 45 s → 1 B methylamine</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel) (functionalstorage:oak_1) - NH3 + MeOH"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel)</span><span class="gt-sub"><span>Benzene</span><span>Methanol</span><span>Ammonia</span><span>Nitrobenzene</span><span>Palladium on carbon dust</span></span><b class="gt-q">NH3 + MeOH</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m9" title="LCR · 22 s · 122 880 EU/t → 16 NMP dust (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 22 s · 122 880 EU/t → 16 NMP dust</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m6" title="LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate</span><b class="gt-q">2 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m6">
<div class="gt-head"><span class="gt-mname">LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate</span><b class="gt-q">2 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m7" title="LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol (gtceu:large_chemical_reactor) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol</span><b class="gt-q">4 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m7">
<div class="gt-head"><span class="gt-mname">LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m6" title="LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate (gtceu:large_chemical_reactor) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate</span><b class="gt-q">4 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m8" title="LCR · 19 s · 122 880 EU/t → 1 B butyrolactone (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 19 s · 122 880 EU/t → 1 B butyrolactone</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m8">
<div class="gt-head"><span class="gt-mname">LCR · 19 s · 122 880 EU/t → 1 B butyrolactone</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m7" title="LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m9" title="LCR · 22 s · 122 880 EU/t → 16 NMP dust (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 22 s · 122 880 EU/t → 16 NMP dust</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m9">
<div class="gt-head"><span class="gt-mname">LCR · 22 s · 122 880 EU/t → 16 NMP dust</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m8" title="LCR · 19 s · 122 880 EU/t → 1 B butyrolactone (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 19 s · 122 880 EU/t → 1 B butyrolactone</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m4" title="HV Chemical Reactor · circuit 1 · 45 s → 1 B methylamine (gtceu:hv_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Chemical Reactor</span><span class="gt-note">HV Chemical Reactor · circuit 1 · 45 s → 1 B methylamine</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m11" title="LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid (gtceu:large_chemical_reactor) - 16"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid</span><b class="gt-q">16</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m10">
<div class="gt-head"><span class="gt-mname">LCR · 36 s · 30 720 EU/t · nickel → 3 B phenylenediamine</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel) (functionalstorage:oak_1) - 3 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Benzene · oxygen · benzoyl chloride · acetic acid · methanol · ammonia · hydrogen · nitrobenzene · nitric acid · catalysts (aluminium, Pd on carbon, nickel)</span><span class="gt-sub"><span>Benzene</span><span>Methanol</span><span>Ammonia</span><span>Nitrobenzene</span><span>Palladium on carbon dust</span></span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m11" title="LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid</span><b class="gt-q">2 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m11">
<div class="gt-head"><span class="gt-mname">LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust (gtceu:large_chemical_reactor) - 60"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust</span><b class="gt-q">60</b></a><a class="gt-slot gt-mach" href="#m-m9" title="LCR · 22 s · 122 880 EU/t → 16 NMP dust (gtceu:large_chemical_reactor) - 16"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 22 s · 122 880 EU/t → 16 NMP dust</span><b class="gt-q">16</b></a><a class="gt-slot gt-mach" href="#m-m10" title="LCR · 36 s · 30 720 EU/t · nickel → 3 B phenylenediamine (gtceu:large_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 36 s · 30 720 EU/t · nickel → 3 B phenylenediamine</span><b class="gt-q">2 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m12" title="LCR · 12 s · 491 520 EU/t (UV) → 4.032 B polyimide (gtceu:large_chemical_reactor) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12 s · 491 520 EU/t (UV) → 4.032 B polyimide</span><b class="gt-q">4 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m12">
<div class="gt-head"><span class="gt-mname">LCR · 12 s · 491 520 EU/t (UV) → 4.032 B polyimide</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m11" title="LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid (gtceu:large_chemical_reactor) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid</span><b class="gt-q">4 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride](#m-m1) → [LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust](#m-m3) → [LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid](#m-m11) → [LCR · 12 s · 491 520 EU/t (UV) → 4.032 B polyimide](#m-m12) (also LCR · circuit 3 · 26 s · 15 360 EU/t · 3 B benzene + 23 B O → 4 B maleic anhydride → [LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate](#m-m5))
- [LCR · circuit 0 · 29 s · 15 360 EU/t → 1 B benzophenone](#m-m2) → [LCR · circuit 1 · 31 s · 61 440 EU/t → 60 BTDA dust](#m-m3)
- [HV Chemical Reactor · circuit 1 · 45 s → 1 B methylamine](#m-m4) → [LCR · 22 s · 122 880 EU/t → 16 NMP dust](#m-m9) → [LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid](#m-m11)
- [LCR · 36 s · 30 720 EU/t · nickel → 3 B phenylenediamine](#m-m10) → [LCR · 33 s · 491 520 EU/t (UV) → 3 B polyamic acid](#m-m11)
- [LCR · 21 s · 245 760 EU/t → 1 B dimethyl maleate](#m-m5) → [LCR · 38 s · 122 880 EU/t · Pd catalyst → 3 B dimethyl succinate](#m-m6) → [LCR · cleanroom · 31 s · 61 440 EU/t → 2 B butanediol + 8 B methanol](#m-m7) → [LCR · 19 s · 122 880 EU/t → 1 B butyrolactone](#m-m8) → [LCR · 22 s · 122 880 EU/t → 16 NMP dust](#m-m9)

## How to build

1. Drawers: catalysts only (aluminium, Pd on carbon, nickel; Keep Exact 1) plus output drawers for BTDA, NMP. Everything else is a fluid: one drum per reactant and per intermediate, and the hydrogen / oxygen / methanol drums need a refill line. — `functionalstorage:oak_1`, `gtceu:palladium_on_carbon_dust`, `gtceu:nickel_dust`
2. Reactor 1 (circuit 3) makes maleic anhydride: 4 B per 26 s. A fluid pipe splits it to the BTDA reactor and the dimethyl maleate reactor, each with a valve. — `gtceu:large_chemical_reactor`, `gtceu:maleic_anhydride_bucket`
3. BTDA reactor (circuit 1, ZPM hatch): 2 B benzophenone + 1 B maleic anhydride + 2 B acetic acid + 14 B oxygen → 60 dust. Output drawer Keep Exact 60. — `gtceu:large_chemical_reactor`, `gtceu:benzophenone_3344_tetracarboxylic_dianhydride_dust`
4. NMP branch: dimethyl maleate (UV hatch) → dimethyl succinate (Pd) → butanediol (cleanroom) → butyrolactone → NMP with methylamine from the HV reactor. Five reactors in a row, one drum between each. — `gtceu:large_chemical_reactor`, `gtceu:n_methyl_2_pyrrolidone_dust`
5. UV pair: polyamic acid reactor (60 BTDA + 16 NMP + 2 B phenylenediamine + 1 B nitric acid) and the polyimide reactor (4 B polyamic acid + 2 B ammonia). 491 520 EU/t each; run them on a UV hatch, not an overclock of a lower tier. — `gtceu:large_chemical_reactor`, `gtceu:uv_energy_input_hatch`
6. Output: polyimide to a drum, Keep Exact 8 B for the five SMD assemblers. Polyimide foil (used by the capacitor SMD) is the GT polymer route: a fluid solidifier makes the plate from the fluid and a bender makes the foil (Unverified: pack changes). — `functionalstorage:oak_1`, `gtceu:polyimide_bucket`

## Tips

- Source: kjs lines/polymers/polyimide.js (all verified). Tiers: VHA\[LuV\] = 15 360 EU/t for maleic anhydride and benzophenone, VHA\[ZPM\] = 61 440 for BTDA and butanediol, VA\[ZPM\] = 122 880 for dimethyl succinate, butyrolactone and NMP, VHA\[UV\] = 245 760 for dimethyl maleate and VA\[UV\] = 491 520 EU/t for polyamic acid and the final polyimide step. The last three need a UV energy hatch on the Large Chemical Reactor (see uv\_hatches), so polyimide is the first thing the UV hull is spent on.
- Ratios (one end-to-end batch, 4.032 B polyimide): 4 B polyamic acid needs 4/3 of a polyamic run = 80 BTDA dust (1.33 BTDA runs of 60 = 2.67 B benzophenone + 1.33 B maleic anhydride + 2.67 B acetic acid + 18.7 B oxygen), 21.3 NMP (1.33 of 16 = 1.33 B butyrolactone + 1.33 B methylamine) and 2.67 B phenylenediamine. A single living SMD run takes 108 to 288 mB, so one batch makes about 15 to 40 SMD runs (240 to 640 SMDs).
- Dimethyl maleate and butanediol come from maleic anhydride: m1 makes 4 B per run and m3 eats 1 B per run, so m1 feeds BTDA (1 B) and dimethyl maleate (1 B per B of dimethyl succinate chain: 2 B per 3 B succinate). Keep the maleic anhydride drum split: Pipez fluid pipes to two valves with Keep Exact, or two output hatches.
- The 1,4-butanediol step is the only one with a CLEANROOM tag (normal cleanroom); the LCR must sit in one or be a cleanroom-compatible multiblock. The others have none. Note that the sequence of 12 reactions needs 11 different Large Chemical Reactors (m4 is a plain HV chemical reactor).
- Sub-steps people skip: (1) catalysts are NOT consumed: put one aluminium dust, one palladium on carbon dust and one nickel dust in the input bus of their reactors and leave them; (2) circuit numbers: m1 3, m2 0, m3 1, m4 1, others none; (3) the water and CO2 outputs must have somewhere to go; (4) nitrobenzene, nitric acid and acetic acid are bought from the earlier chemistry chains; (5) the polyamic acid step also needs 1 B nitric acid per run and gives back 2 B hydrogen.
- **Unverified** the benzoyl chloride supply from the PEEK chain (uv\_peek m2) is shared, so one benzotrichloride line has to feed both polymers; acetic acid, ammonia, nitrobenzene sources.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 11 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:uv_energy_input_hatch` | 1 |
| `gtceu:zpm_energy_input_hatch` | 2 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 20 |
| `gtceu:steel_drum` | 18 |

## Needs / Feeds

- **Main source for:** `gtceu:polyimide_bucket`, `gtceu:polyimide_foil`, `gtceu:maleic_anhydride_bucket`
