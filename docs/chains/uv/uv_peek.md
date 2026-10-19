---
kind: chain
id: uv_peek
order: 1590
data:
  t: |-
    Polyether ether ketone (PEEK): 8 Large Chemical Reactor steps from toluene, benzene, fluorine and propene - the UV hull plastic
  inf: true
  "n":
    - - g1
      - "1 B toluene · 3 B chlorine"
      - g
      - functionalstorage:oak_1
      - [[Toluene, "gtceu:toluene_bucket"], [Chlorine, "gtceu:chlorine_bucket"]]
    - [m1, "LCR · 2.5 s · 61 440 EU/t → 1 B benzotrichloride + 3 B hydrogen", m, "gtceu:large_chemical_reactor"]
    - - m2
      - LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl
      - m
      - gtceu:large_chemical_reactor
    - - m3
      - LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride
      - m
      - gtceu:large_chemical_reactor
    - - g2
      - "1 B benzene · 2 B fluorine"
      - g
      - functionalstorage:oak_1
      - [[Benzene, "gtceu:benzene_bucket"], [Fluorine, "gtceu:fluorine_bucket"]]
    - [m4, "LCR · 5 s · 30 720 EU/t → 1 B fluorobenzene + 1 B hydrofluoric acid", m, "gtceu:large_chemical_reactor"]
    - [m5, "LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl", m, "gtceu:large_chemical_reactor"]
    - - g3
      - "1 B benzene · 1 B propene · 1 B oxygen · circuit 2"
      - g
      - functionalstorage:oak_1
      - [[Propene, "gtceu:propene_bucket"], [Oxygen, "gtceu:oxygen_bucket"]]
    - [m6, "LCR · 8 s · 122 880 EU/t → 14 hydroquinone dust + 1 B acetone", m, "gtceu:large_chemical_reactor"]
    - [g4, "6 soda ash dust", g, "functionalstorage:oak_1", [[Soda ash dust, "gtceu:soda_ash_dust"]]]
    - [m7, "LCR · 6 s · 7680 EU/t → 14 disodium salt dust + 1 B carbonic acid", m, "gtceu:large_chemical_reactor"]
    - [m8, "LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt", m, "gtceu:large_chemical_reactor"]
    - [pk, "PEEK 2448 mB + 2 sodium fluoride dust", o, "gtceu:polyether_ether_ketone_bucket"]
  e:
    - [g1, m1, "1 / 3 B"]
    - [m1, m2, "1 B"]
    - [m2, m3, "1 B"]
    - [g2, m4, "1 / 2 B"]
    - [m3, m5, "1 B"]
    - [m4, m5, "1 B"]
    - [m5, m8, "12 of 24"]
    - [g3, m6, "1"]
    - [m6, g4, "14"]
    - [g4, m7, "6 + 14"]
    - [m7, m8, "7 of 14"]
    - [m8, pk, "2448 mB / 12.5 s"]
  tips:
    - |-
      Source: kjs additions/progression/lines/polymers/peek.js (verified, all Large Chemical Reactor recipes). Energy: VHA[ZPM] = 61 440 EU/t for the benzotrichloride step, VA[ZPM] = 122 880 EU/t for hydroquinone, VA[LuV] = 30 720 EU/t for the rest (the polyimide line is UV tier, see uv_polyimide). The hydroquinone step is the one that needs a ZPM-tier energy hatch on the Large Chemical Reactor; everything else can run on a LuV hatch.
    - |-
      Numbers per one PEEK run (2448 mB, 12.5 s): 12 difluorobenzophenone dust is HALF of a 24-dust run (1 B fluorobenzene + 1 B fluorobenzoyl chloride), so a run takes 0.5 B each of those, i.e. 0.5 B benzotrichloride = 0.5 B toluene + 1.5 B chlorine, and 0.5 B fluorobenzene = 0.5 B benzene + 1 B fluorine; and 7 disodium salt = half of a 14-dust run = 0.5 B benzene + 0.5 B propene + 0.5 B oxygen and 3 soda ash. One UV hull costs 288 mB of PEEK, so about 0.12 of a run.
    - |-
      Sodium loop: the pack removes the GT sodium bicarbonate decomposition, then adds its own pair: carbonic acid + 1 sodium dust → 6 sodium bicarbonate + 1 B hydrogen (120 ticks, VA[HV]) and 12 bicarbonate → 6 soda ash + 2 B hydrogen in an electrolyzer (120 ticks, VA[HV]). Per 14 disodium salt: 6 soda ash in, 3 soda ash back, 1 sodium dust consumed. Sodium dust is the only recurring solid cost.
    - |-
      Byproducts to handle: hydrogen (3 B + 1 B + 1 B ...), HCl (2 B + 1 B per run of m2/m5), hydrofluoric acid, acetone, sodium fluoride dust (2 per run). Put every output on a drum or a void/recycle valve; the Large Chemical Reactor stops when an output hatch is full.
    - |-
      Sub-steps people skip: (1) one dedicated LCR per step (eight machines), a single LCR cannot hold two recipes; (2) circuit 2 on the hydroquinone step and no circuit on the others; (3) fluorine is the scarce input: 1 B + 2 B per DFBP batch of 24 dust, so a fluorine electrolysis line must run first; (4) PEEK is also used for circuit boards, PEEK foil for the runic computer and as 288 mB in every UV hull, keep a 4 B drum reserve.
    - |-
      Unverified: the toluene, benzene, propene and fluorine sources in this pack (oil_distill and the HV/EV chemistry chains cover toluene/benzene; fluorine = hydrofluoric acid electrolysis), the exact LCR parallel behaviour at these voltages.
  b:
    - ["gtceu:large_chemical_reactor", 8]
    - ["gtceu:hv_electrolyzer", 1]
    - ["gtceu:zpm_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 14]
    - ["gtceu:steel_drum", 14]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:soda_ash_dust", "gtceu:sodium_dust"]
      t: |-
        Drawers: soda ash dust (Keep Exact 6), sodium dust, output drawers for difluorobenzophenone, hydroquinone and disodium salt dust. Fluid drums first: toluene, chlorine, benzene, fluorine, propene, oxygen, water, and a drum for each intermediate. Pipez fluid pipes between neighbours, one pipe per fluid, never shared.
    - i: ["gtceu:large_chemical_reactor", "gtceu:benzoyl_chloride_bucket"]
      t: |-
        Chain A (one LCR each, in a row): benzotrichloride → benzoyl chloride → 4-fluorobenzoyl chloride. Each step’s output goes straight into a drum that feeds the next LCR; hydrogen and HCl by-products to their own drums.
    - i: ["gtceu:large_chemical_reactor", "gtceu:fluorobenzene_bucket"]
      t: |-
        Chain B: fluorobenzene LCR (benzene + 2 B fluorine) and the difluorobenzophenone LCR that reads both drums; it returns 24 dust per run into the output drawer. Keep Exact 12.
    - i: ["gtceu:large_chemical_reactor", "gtceu:hydroquinone_dust", "gtceu:disodium_salt_of_hydroquinone_dust"]
      t: |-
        Chain C: hydroquinone LCR (circuit 2, ZPM hatch), then the disodium salt LCR (6 soda ash + 14 hydroquinone). Carbonic acid goes to the electrolyzer pair that recycles soda ash.
    - i: ["gtceu:large_chemical_reactor", "gtceu:polyether_ether_ketone_bucket"]
      t: |-
        PEEK LCR: 12 difluorobenzophenone + 7 disodium salt by one router (Item Filters, Keep Exact 12 / 7), output 2448 mB into a drum; sodium fluoride dust into a drawer.
    - i: ["gtceu:zpm_energy_input_hatch", "gtceu:large_chemical_reactor"]
      t: |-
        Power: hatch tier decides which steps run. A LuV hatch (32 768 EU/t) runs everything except benzotrichloride and hydroquinone; give those two their own ZPM-hatch LCRs. Each run is seconds, so total energy per 288 mB is small.
---
# Polyether ether ketone (PEEK): 8 Large Chemical Reactor steps from toluene, benzene, fluorine and propene - the UV hull plastic

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_peek` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [PEEK, polyimide and UV solder](../../plan/p14.md#uvchem)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">LCR · 2.5 s · 61 440 EU/t → 1 B benzotrichloride + 3 B hydrogen</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 B toluene · 3 B chlorine (functionalstorage:oak_1) - 1 / 3 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 B toluene · 3 B chlorine</span><span class="gt-sub"><span>Toluene</span><span>Chlorine</span></span><b class="gt-q">1 / 3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LCR · 2.5 s · 61 440 EU/t → 1 B benzotrichloride + 3 B hydrogen (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 2.5 s · 61 440 EU/t → 1 B benzotrichloride + 3 B hydrogen</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m4">
<div class="gt-head"><span class="gt-mname">LCR · 5 s · 30 720 EU/t → 1 B fluorobenzene + 1 B hydrofluoric acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 B benzene · 2 B fluorine (functionalstorage:oak_1) - 1 / 2 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 B benzene · 2 B fluorine</span><span class="gt-sub"><span>Benzene</span><span>Fluorine</span></span><b class="gt-q">1 / 2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-m4" title="LCR · 5 s · 30 720 EU/t → 1 B fluorobenzene + 1 B hydrofluoric acid (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 5 s · 30 720 EU/t → 1 B fluorobenzene + 1 B hydrofluoric acid</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m8" title="LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt (gtceu:large_chemical_reactor) - 12 of 24"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt</span><b class="gt-q">12 of 24</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m6">
<div class="gt-head"><span class="gt-mname">LCR · 8 s · 122 880 EU/t → 14 hydroquinone dust + 1 B acetone</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 B benzene · 1 B propene · 1 B oxygen · circuit 2 (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 B benzene · 1 B propene · 1 B oxygen · circuit 2</span><span class="gt-sub"><span>Propene</span><span>Oxygen</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="6 soda ash dust (functionalstorage:oak_1) - 14"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 soda ash dust</span><span class="gt-sub"><span>Soda ash dust</span></span><b class="gt-q">14</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m7">
<div class="gt-head"><span class="gt-mname">LCR · 6 s · 7680 EU/t → 14 disodium salt dust + 1 B carbonic acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="6 soda ash dust (functionalstorage:oak_1) - 6 + 14"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 soda ash dust</span><span class="gt-sub"><span>Soda ash dust</span></span><b class="gt-q">6 + 14</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m8" title="LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt (gtceu:large_chemical_reactor) - 7 of 14"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt</span><b class="gt-q">7 of 14</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-m8">
<div class="gt-head"><span class="gt-mname">LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl (gtceu:large_chemical_reactor) - 12 of 24"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl</span><b class="gt-q">12 of 24</b></a><a class="gt-slot gt-mach" href="#m-m7" title="LCR · 6 s · 7680 EU/t → 14 disodium salt dust + 1 B carbonic acid (gtceu:large_chemical_reactor) - 7 of 14"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 6 s · 7680 EU/t → 14 disodium salt dust + 1 B carbonic acid</span><b class="gt-q">7 of 14</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="PEEK 2448 mB + 2 sodium fluoride dust (gtceu:polyether_ether_ketone_bucket) - 2448 mB / 12.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__polyether_ether_ketone_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyether Ether Ketone Bucket</span><span class="gt-note">PEEK 2448 mB + 2 sodium fluoride dust</span><b class="gt-q">2448 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LCR · 2.5 s · 61 440 EU/t → 1 B benzotrichloride + 3 B hydrogen](#m-m1) → [LCR · 7.5 s · 30 720 EU/t · + 1 B water → 1 B benzoyl chloride + 2 B HCl](#m-m2) → [LCR · 12.5 s · 30 720 EU/t · + 1 B fluorine → 1 B 4-fluorobenzoyl chloride](#m-m3) → [LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl](#m-m5) → [LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt](#m-m8)
- [LCR · 5 s · 30 720 EU/t → 1 B fluorobenzene + 1 B hydrofluoric acid](#m-m4) → [LCR · 6 s · 30 720 EU/t → 24 difluorobenzophenone dust + 1 B HCl](#m-m5)
- [LCR · 8 s · 122 880 EU/t → 14 hydroquinone dust + 1 B acetone](#m-m6) → [LCR · 6 s · 7680 EU/t → 14 disodium salt dust + 1 B carbonic acid](#m-m7) → [LCR · 12.5 s · 30 720 EU/t · 12 DFBP + 7 disodium salt](#m-m8)

## How to build

1. Drawers: soda ash dust (Keep Exact 6), sodium dust, output drawers for difluorobenzophenone, hydroquinone and disodium salt dust. Fluid drums first: toluene, chlorine, benzene, fluorine, propene, oxygen, water, and a drum for each intermediate. Pipez fluid pipes between neighbours, one pipe per fluid, never shared. — `functionalstorage:oak_1`, `gtceu:soda_ash_dust`, `gtceu:sodium_dust`
2. Chain A (one LCR each, in a row): benzotrichloride → benzoyl chloride → 4-fluorobenzoyl chloride. Each step’s output goes straight into a drum that feeds the next LCR; hydrogen and HCl by-products to their own drums. — `gtceu:large_chemical_reactor`, `gtceu:benzoyl_chloride_bucket`
3. Chain B: fluorobenzene LCR (benzene + 2 B fluorine) and the difluorobenzophenone LCR that reads both drums; it returns 24 dust per run into the output drawer. Keep Exact 12. — `gtceu:large_chemical_reactor`, `gtceu:fluorobenzene_bucket`
4. Chain C: hydroquinone LCR (circuit 2, ZPM hatch), then the disodium salt LCR (6 soda ash + 14 hydroquinone). Carbonic acid goes to the electrolyzer pair that recycles soda ash. — `gtceu:large_chemical_reactor`, `gtceu:hydroquinone_dust`, `gtceu:disodium_salt_of_hydroquinone_dust`
5. PEEK LCR: 12 difluorobenzophenone + 7 disodium salt by one router (Item Filters, Keep Exact 12 / 7), output 2448 mB into a drum; sodium fluoride dust into a drawer. — `gtceu:large_chemical_reactor`, `gtceu:polyether_ether_ketone_bucket`
6. Power: hatch tier decides which steps run. A LuV hatch (32 768 EU/t) runs everything except benzotrichloride and hydroquinone; give those two their own ZPM-hatch LCRs. Each run is seconds, so total energy per 288 mB is small. — `gtceu:zpm_energy_input_hatch`, `gtceu:large_chemical_reactor`

## Tips

- Source: kjs additions/progression/lines/polymers/peek.js (verified, all Large Chemical Reactor recipes). Energy: VHA\[ZPM\] = 61 440 EU/t for the benzotrichloride step, VA\[ZPM\] = 122 880 EU/t for hydroquinone, VA\[LuV\] = 30 720 EU/t for the rest (the polyimide line is UV tier, see uv\_polyimide). The hydroquinone step is the one that needs a ZPM-tier energy hatch on the Large Chemical Reactor; everything else can run on a LuV hatch.
- Numbers per one PEEK run (2448 mB, 12.5 s): 12 difluorobenzophenone dust is HALF of a 24-dust run (1 B fluorobenzene + 1 B fluorobenzoyl chloride), so a run takes 0.5 B each of those, i.e. 0.5 B benzotrichloride = 0.5 B toluene + 1.5 B chlorine, and 0.5 B fluorobenzene = 0.5 B benzene + 1 B fluorine; and 7 disodium salt = half of a 14-dust run = 0.5 B benzene + 0.5 B propene + 0.5 B oxygen and 3 soda ash. One UV hull costs 288 mB of PEEK, so about 0.12 of a run.
- Sodium loop: the pack removes the GT sodium bicarbonate decomposition, then adds its own pair: carbonic acid + 1 sodium dust → 6 sodium bicarbonate + 1 B hydrogen (120 ticks, VA\[HV\]) and 12 bicarbonate → 6 soda ash + 2 B hydrogen in an electrolyzer (120 ticks, VA\[HV\]). Per 14 disodium salt: 6 soda ash in, 3 soda ash back, 1 sodium dust consumed. Sodium dust is the only recurring solid cost.
- Byproducts to handle: hydrogen (3 B + 1 B + 1 B ...), HCl (2 B + 1 B per run of m2/m5), hydrofluoric acid, acetone, sodium fluoride dust (2 per run). Put every output on a drum or a void/recycle valve; the Large Chemical Reactor stops when an output hatch is full.
- Sub-steps people skip: (1) one dedicated LCR per step (eight machines), a single LCR cannot hold two recipes; (2) circuit 2 on the hydroquinone step and no circuit on the others; (3) fluorine is the scarce input: 1 B + 2 B per DFBP batch of 24 dust, so a fluorine electrolysis line must run first; (4) PEEK is also used for circuit boards, PEEK foil for the runic computer and as 288 mB in every UV hull, keep a 4 B drum reserve.
- **Unverified** the toluene, benzene, propene and fluorine sources in this pack (oil\_distill and the HV/EV chemistry chains cover toluene/benzene; fluorine = hydrofluoric acid electrolysis), the exact LCR parallel behaviour at these voltages.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 8 |
| `gtceu:hv_electrolyzer` | 1 |
| `gtceu:zpm_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 14 |
| `gtceu:steel_drum` | 14 |

## Needs / Feeds

- **Main source for:** `gtceu:polyether_ether_ketone_bucket`, `gtceu:polyether_ether_ketone_plate`, `gtceu:polyether_ether_ketone_foil`, `gtceu:44_difluorobenzophenone_dust`
