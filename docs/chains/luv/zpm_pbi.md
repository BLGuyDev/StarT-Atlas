---
kind: chain
id: zpm_pbi
order: 1380
data:
  t: |-
    Polybenzimidazole (PBI): chlorobenzene → dichlorobenzidine → diaminobenzidine + diphenyl isophthalate → PBI (the hull, bus and ASMD plastic)
  inf: true
  "n":
    - - cl
      - "2 B chlorine + 1 B benzene (circuit 1)"
      - g
      - functionalstorage:oak_1
      - [[Chlorine, "gtceu:chlorine_bucket"], [Benzene, "gtceu:benzene_bucket"]]
    - [r1, "LV Chemical Reactor · 12 s · 30 EU/t → 1 B chlorobenzene", m, "gtceu:lv_chemical_reactor"]
    - [nm, "2 B nitration mixture", f, "gtceu:nitration_mixture_bucket"]
    - [r2, "HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene", m, "gtceu:hv_chemical_reactor"]
    - - h2
      - "2 B hydrogen + 1 tiny copper dust (2 B nitrochlorobenzene)"
      - g
      - functionalstorage:oak_1
      - [[Hydrogen, "gtceu:hydrogen_bucket"], [Tiny copper dust, "gtceu:tiny_copper_dust"]]
    - [r3, "EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine", m, "gtceu:ev_chemical_reactor"]
    - - am
      - "2 B ammonia + zinc dust (not consumed)"
      - g
      - functionalstorage:oak_1
      - [[Ammonia, "gtceu:ammonia_bucket"], [Zinc dust, "gtceu:zinc_dust"]]
    - [r4, "Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine", m, "gtceu:large_chemical_reactor"]
    - - dp
      - "2 B phenol + 1 B sulfuric acid + 1 B phthalic acid"
      - g
      - functionalstorage:oak_1
      - - [Phenol, "gtceu:phenol_bucket"]
        - [Sulfuric acid, "gtceu:sulfuric_acid_bucket"]
        - [Phthalic acid, "gtceu:phthalic_acid_bucket"]
    - - r5
      - Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diphenyl isophthalate
      - m
      - gtceu:large_chemical_reactor
    - [r6, "IV Chemical Reactor · 5 s · 7680 EU/t", m, "gtceu:iv_chemical_reactor"]
    - [o, "1008 mB PBI + 1 B phenol (back to the reactor drum)", o, "gtceu:polybenzimidazole_bucket"]
  e:
    - [cl, r1, "1"]
    - [r1, r2, "1 B"]
    - [nm, r2, "2 B"]
    - [r2, r3, "2 B"]
    - [h2, r3, "1"]
    - [r3, r4, "1 B"]
    - [am, r4, "1"]
    - [r4, r6, "1 B"]
    - [dp, r5, "1"]
    - [r5, r6, "1 B"]
    - [r6, o, "1 B / 5 s"]
  tips:
    - |-
      Recipes (PolymerRecipes polybenzimidazoleProcess, not changed by the pack; the pack only adds a PBI plunger): PBI = 1 B diaminobenzidine + 1 B diphenyl isophthalate → 1 B phenol + 1008 mB PBI, chemical reactor, 100 ticks at VA[IV] = 7680 EU/t. Diaminobenzidine = 1 B dichlorobenzidine + 2 B ammonia (zinc dust as a non-consumed catalyst) → 1 B + 2 B hydrochloric acid, Large Chemical Reactor, 100 ticks at 7680 EU/t. Dichlorobenzidine = 2 B nitrochlorobenzene + 2 B hydrogen + 1 tiny copper dust → 1 B, 200 ticks at 1920 EU/t (a 9x variant in the Large Chemical Reactor gives 9 B for 18 + 18 B and 1 copper dust, 1800 ticks). Nitrochlorobenzene = 2 B nitration mixture + 1 B chlorobenzene → 1 B + 1 B diluted sulfuric acid, 100 ticks at 480 EU/t. Chlorobenzene = 2 B chlorine + 1 B benzene (circuit 1) → 1 B + 1 B hydrochloric acid, 240 ticks at 30 EU/t.
    - |-
      Diphenyl isophthalate = 2 B phenol + 1 B sulfuric acid + 1 B phthalic acid → 1 B + 1 B diluted sulfuric acid, Large Chemical Reactor, 100 ticks at 7680 EU/t. Phthalic acid has two routes: dimethylbenzene (Large Chemical Reactor, 1 B dimethylbenzene + 2 B oxygen + 1 tiny potassium dichromate dust → 1 B acid + 2 B water, 100 ticks at 1920 EU/t; dimethylbenzene itself = 2 B methane + 1 B benzene, 4000 ticks at 120 EU/t) or naphthalene (2 B naphthalene + 1 B sulfuric acid + 1 tiny potassium dust → 2500 mB acid + 1 B hydrogen sulfide, 125 ticks at 30 EU/t, no Large Reactor tier needed). Phenol: cumene route (1 B cumene + 2 B oxygen → 1 B phenol + 1 B acetone, 160 ticks at 30 EU/t); one B of PBI costs 2 B phenol and gives 1 B back, so net 1 B fresh phenol.
    - |-
      Raw per 1 B PBI: 2 B benzene + 4 B chlorine + 4 B nitration mixture + 2 B hydrogen + 2 B ammonia + 1 B phthalic acid + 1 B sulfuric acid + 1 net B phenol. This is a big chemistry line for what looks like a small fluid, but a ZPM hull, ZPM bus and ZPM hatch take only 288 mB each, an ASMD craft 36 to 288 mB, and a fusion casing 576 mB: a 10 B drum lasts many dozens of items. Build the line once, run it until a 16 B drum is full, then switch it off.
    - |-
      Where PBI enters: the pack’s hull recipe for LuV, ZPM and UV (kjs additions/machines_and_parts/tiered_machines/singleblocks.js luvUVMachines: casing + 2 tier cables + 288 mB PBI) and the tier-data plastic of LuV and ZPM, buses and hatches (io_hatches.js), ASMDs, computation hatches, object holder, Assembly Line recipes of the research parts. So the guide’s LuV hull chain that says PTFE is out of date for this pack; PBI is needed already at LuV.
    - |-
      Nitration mixture: a mixer recipe of sulfuric and nitric acid (earlier chemistry chains, Unverified exact ratio here: check EMI). Nitric acid and the benzene line come from the oil_distill and chem chains of the HV era; chlorine from the chlor chain.
    - |-
      Sub-steps people skip: (1) the zinc dust in the diaminobenzidine reactor is a NON-consumed catalyst in a ghost slot or input bus: put one dust in, do not feed a stack; (2) every step has a by-product (hydrochloric acid, diluted sulfuric acid, phenol, hydrogen sulfide), void or recycle it into the chlor line before it fills the output hatch and stops the reactor; (3) the final step returns 1 B phenol: pipe it back to the diphenyl isophthalate reactor; (4) 1008 mB per craft, not 1000: the drum overflows by 8 mB, so leave room.
    - |-
      The Chemical Plant skips (kjs chemical_plant.js, a UV multiblock) cover fluoroantimonic acid, the platinum line, the naquadah line, uranite, persulfate, iron III chloride, borax and others, but none of the PBI steps, so the chain above is the only PBI route in the pack as far as the scripts show. Unverified: the exact nitration mixture recipe.
  b:
    - ["gtceu:lv_chemical_reactor", 1]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:ev_chemical_reactor", 1]
    - ["gtceu:large_chemical_reactor", 2]
    - ["gtceu:iv_chemical_reactor", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:tiny_copper_dust", "gtceu:zinc_dust", "gtceu:chlorine_bucket"]
      t: |-
        Drawers first for the dusts (tiny copper, zinc, potassium dichromate); drums for every fluid: chlorine, benzene, nitration mixture, hydrogen, ammonia, phenol, sulfuric acid, phthalic acid. One drum per fluid, each behind a Pipez fluid pipe or Modular Router; each reactor gets its own pipes and a Robot Arm cover in Keep Exact mode on the output hatch drum.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:chlorine_bucket", "gtceu:benzene_bucket"]
      t: |-
        Reactor 1 (LV, circuit 1 in the bus): 2 B chlorine + 1 B benzene → 1 B chlorobenzene in 12 s at 30 EU/t. Hydrochloric acid out to a separate drum.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:nitration_mixture_bucket"]
      t: |-
        Reactor 2 (HV): chlorobenzene + 2 B nitration mixture → 1 B nitrochlorobenzene in 5 s at 480 EU/t, diluted sulfuric acid out. Reactor 3 (EV, 1920 EU/t): 2 B nitrochlorobenzene + 2 B hydrogen + 1 tiny copper dust → 1 B dichlorobenzidine in 10 s: this is the line’s rate limit, 1 B per 10 s.
    - i: ["gtceu:large_chemical_reactor", "gtceu:ammonia_bucket", "gtceu:zinc_dust"]
      t: |-
        Reactor 4 (Large Chemical Reactor, an IV hatch): 1 B dichlorobenzidine + 2 B ammonia + the zinc dust catalyst → 1 B diaminobenzidine in 5 s at 7680 EU/t.
    - i: ["gtceu:large_chemical_reactor", "gtceu:phenol_bucket", "gtceu:phthalic_acid_bucket"]
      t: |-
        Reactor 5 (Large Chemical Reactor): 2 B phenol + 1 B sulfuric acid + 1 B phthalic acid → 1 B diphenyl isophthalate in 5 s. Phthalic acid is a drum fed from its own line (naphthalene is the cheapest: LV Large Chemical Reactor).
    - i: ["gtceu:iv_chemical_reactor", "gtceu:polybenzimidazole_bucket"]
      t: |-
        Reactor 6 (IV Chemical Reactor, 7680 EU/t): diaminobenzidine + diphenyl isophthalate → phenol + 1008 mB PBI in 5 s. A Pipez fluid pipe sends the phenol back to the reactor 5 drum, the PBI to a big steel drum with Keep Exact (a pump cover) so the hull and hatch assemblers can pull from it.
    - i: ["functionalstorage:oak_1", "gtceu:polybenzimidazole_bucket"]
      t: |-
        Easy to miss: build the whole line before the first ZPM hull; without PBI you cannot build even the LuV hull in this pack, and PBI also decides the ASMD output. Run it in batches until you hold about 10 B, then power it down.
---
# Polybenzimidazole (PBI): chlorobenzene → dichlorobenzidine → diaminobenzidine + diphenyl isophthalate → PBI (the hull, bus and ASMD plastic)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_pbi` · **Tags:** Infinite source

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [PBI plastic (hull and bus plastic)](../../plan/p11.md#pbi)

**Tips:** 7

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-r1">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 12 s · 30 EU/t → 1 B chlorobenzene</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 B chlorine + 1 B benzene (circuit 1) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 B chlorine + 1 B benzene (circuit 1)</span><span class="gt-sub"><span>Chlorine</span><span>Benzene</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-r2" title="HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene (gtceu:hv_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Chemical Reactor</span><span class="gt-note">HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-r2">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-r1" title="LV Chemical Reactor · 12 s · 30 EU/t → 1 B chlorobenzene (gtceu:lv_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Chemical Reactor</span><span class="gt-note">LV Chemical Reactor · 12 s · 30 EU/t → 1 B chlorobenzene</span><b class="gt-q">1 B</b></a><span class="gt-slot gt-fluid" title="2 B nitration mixture (gtceu:nitration_mixture_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__nitration_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitration Mixture</span><span class="gt-note">2 B nitration mixture</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-r3" title="EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine (gtceu:ev_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Chemical Reactor</span><span class="gt-note">EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine</span><b class="gt-q">2 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-ev" id="m-r3">
<div class="gt-head"><span class="gt-mname">EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-r2" title="HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene (gtceu:hv_chemical_reactor) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Chemical Reactor</span><span class="gt-note">HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene</span><b class="gt-q">2 B</b></a><span class="gt-slot gt-group" title="2 B hydrogen + 1 tiny copper dust (2 B nitrochlorobenzene) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 B hydrogen + 1 tiny copper dust (2 B nitrochlorobenzene)</span><span class="gt-sub"><span>Hydrogen</span><span>Tiny copper dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-r4" title="Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-r4">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-r3" title="EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine (gtceu:ev_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">EV Chemical Reactor</span><span class="gt-note">EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine</span><b class="gt-q">1 B</b></a><span class="gt-slot gt-group" title="2 B ammonia + zinc dust (not consumed) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 B ammonia + zinc dust (not consumed)</span><span class="gt-sub"><span>Ammonia</span><span>Zinc dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-r6" title="IV Chemical Reactor · 5 s · 7680 EU/t (gtceu:iv_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__iv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Chemical Reactor</span><span class="gt-note">IV Chemical Reactor · 5 s · 7680 EU/t</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-r5">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diphenyl isophthalate</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 B phenol + 1 B sulfuric acid + 1 B phthalic acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 B phenol + 1 B sulfuric acid + 1 B phthalic acid</span><span class="gt-sub"><span>Phenol</span><span>Sulfuric acid</span><span>Phthalic acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-r6" title="IV Chemical Reactor · 5 s · 7680 EU/t (gtceu:iv_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__iv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Chemical Reactor</span><span class="gt-note">IV Chemical Reactor · 5 s · 7680 EU/t</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-iv" id="m-r6">
<div class="gt-head"><span class="gt-mname">IV Chemical Reactor · 5 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-r4" title="Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine</span><b class="gt-q">1 B</b></a><a class="gt-slot gt-mach" href="#m-r5" title="Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diphenyl isophthalate (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diphenyl isophthalate</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="1008 mB PBI + 1 B phenol (back to the reactor drum) (gtceu:polybenzimidazole_bucket) - 1 B / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole Bucket</span><span class="gt-note">1008 mB PBI + 1 B phenol (back to the reactor drum)</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LV Chemical Reactor · 12 s · 30 EU/t → 1 B chlorobenzene](#m-r1) → [HV Chemical Reactor · 5 s · 480 EU/t → 1 B nitrochlorobenzene](#m-r2) → [EV Chemical Reactor · 10 s · 1920 EU/t → 1 B dichlorobenzidine](#m-r3) → [Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diaminobenzidine](#m-r4) → [IV Chemical Reactor · 5 s · 7680 EU/t](#m-r6)
- [Large Chemical Reactor · 5 s · 7680 EU/t → 1 B diphenyl isophthalate](#m-r5) → [IV Chemical Reactor · 5 s · 7680 EU/t](#m-r6)

## How to build

1. Drawers first for the dusts (tiny copper, zinc, potassium dichromate); drums for every fluid: chlorine, benzene, nitration mixture, hydrogen, ammonia, phenol, sulfuric acid, phthalic acid. One drum per fluid, each behind a Pipez fluid pipe or Modular Router; each reactor gets its own pipes and a Robot Arm cover in Keep Exact mode on the output hatch drum. — `functionalstorage:oak_1`, `gtceu:tiny_copper_dust`, `gtceu:zinc_dust`, `gtceu:chlorine_bucket`
2. Reactor 1 (LV, circuit 1 in the bus): 2 B chlorine + 1 B benzene → 1 B chlorobenzene in 12 s at 30 EU/t. Hydrochloric acid out to a separate drum. — `gtceu:lv_chemical_reactor`, `gtceu:chlorine_bucket`, `gtceu:benzene_bucket`
3. Reactor 2 (HV): chlorobenzene + 2 B nitration mixture → 1 B nitrochlorobenzene in 5 s at 480 EU/t, diluted sulfuric acid out. Reactor 3 (EV, 1920 EU/t): 2 B nitrochlorobenzene + 2 B hydrogen + 1 tiny copper dust → 1 B dichlorobenzidine in 10 s: this is the line’s rate limit, 1 B per 10 s. — `gtceu:hv_chemical_reactor`, `gtceu:nitration_mixture_bucket`
4. Reactor 4 (Large Chemical Reactor, an IV hatch): 1 B dichlorobenzidine + 2 B ammonia + the zinc dust catalyst → 1 B diaminobenzidine in 5 s at 7680 EU/t. — `gtceu:large_chemical_reactor`, `gtceu:ammonia_bucket`, `gtceu:zinc_dust`
5. Reactor 5 (Large Chemical Reactor): 2 B phenol + 1 B sulfuric acid + 1 B phthalic acid → 1 B diphenyl isophthalate in 5 s. Phthalic acid is a drum fed from its own line (naphthalene is the cheapest: LV Large Chemical Reactor). — `gtceu:large_chemical_reactor`, `gtceu:phenol_bucket`, `gtceu:phthalic_acid_bucket`
6. Reactor 6 (IV Chemical Reactor, 7680 EU/t): diaminobenzidine + diphenyl isophthalate → phenol + 1008 mB PBI in 5 s. A Pipez fluid pipe sends the phenol back to the reactor 5 drum, the PBI to a big steel drum with Keep Exact (a pump cover) so the hull and hatch assemblers can pull from it. — `gtceu:iv_chemical_reactor`, `gtceu:polybenzimidazole_bucket`
7. Easy to miss: build the whole line before the first ZPM hull; without PBI you cannot build even the LuV hull in this pack, and PBI also decides the ASMD output. Run it in batches until you hold about 10 B, then power it down. — `functionalstorage:oak_1`, `gtceu:polybenzimidazole_bucket`

## Tips

- Recipes (PolymerRecipes polybenzimidazoleProcess, not changed by the pack; the pack only adds a PBI plunger): PBI = 1 B diaminobenzidine + 1 B diphenyl isophthalate → 1 B phenol + 1008 mB PBI, chemical reactor, 100 ticks at VA\[IV\] = 7680 EU/t. Diaminobenzidine = 1 B dichlorobenzidine + 2 B ammonia (zinc dust as a non-consumed catalyst) → 1 B + 2 B hydrochloric acid, Large Chemical Reactor, 100 ticks at 7680 EU/t. Dichlorobenzidine = 2 B nitrochlorobenzene + 2 B hydrogen + 1 tiny copper dust → 1 B, 200 ticks at 1920 EU/t (a 9x variant in the Large Chemical Reactor gives 9 B for 18 + 18 B and 1 copper dust, 1800 ticks). Nitrochlorobenzene = 2 B nitration mixture + 1 B chlorobenzene → 1 B + 1 B diluted sulfuric acid, 100 ticks at 480 EU/t. Chlorobenzene = 2 B chlorine + 1 B benzene (circuit 1) → 1 B + 1 B hydrochloric acid, 240 ticks at 30 EU/t.
- Diphenyl isophthalate = 2 B phenol + 1 B sulfuric acid + 1 B phthalic acid → 1 B + 1 B diluted sulfuric acid, Large Chemical Reactor, 100 ticks at 7680 EU/t. Phthalic acid has two routes: dimethylbenzene (Large Chemical Reactor, 1 B dimethylbenzene + 2 B oxygen + 1 tiny potassium dichromate dust → 1 B acid + 2 B water, 100 ticks at 1920 EU/t; dimethylbenzene itself = 2 B methane + 1 B benzene, 4000 ticks at 120 EU/t) or naphthalene (2 B naphthalene + 1 B sulfuric acid + 1 tiny potassium dust → 2500 mB acid + 1 B hydrogen sulfide, 125 ticks at 30 EU/t, no Large Reactor tier needed). Phenol: cumene route (1 B cumene + 2 B oxygen → 1 B phenol + 1 B acetone, 160 ticks at 30 EU/t); one B of PBI costs 2 B phenol and gives 1 B back, so net 1 B fresh phenol.
- Raw per 1 B PBI: 2 B benzene + 4 B chlorine + 4 B nitration mixture + 2 B hydrogen + 2 B ammonia + 1 B phthalic acid + 1 B sulfuric acid + 1 net B phenol. This is a big chemistry line for what looks like a small fluid, but a ZPM hull, ZPM bus and ZPM hatch take only 288 mB each, an ASMD craft 36 to 288 mB, and a fusion casing 576 mB: a 10 B drum lasts many dozens of items. Build the line once, run it until a 16 B drum is full, then switch it off.
- Where PBI enters: the pack’s hull recipe for LuV, ZPM and UV (kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js luvUVMachines: casing + 2 tier cables + 288 mB PBI) and the tier-data plastic of LuV and ZPM, buses and hatches (io\_hatches.js), ASMDs, computation hatches, object holder, Assembly Line recipes of the research parts. So the guide’s LuV hull chain that says PTFE is out of date for this pack; PBI is needed already at LuV.
- Nitration mixture: a mixer recipe of sulfuric and nitric acid (earlier chemistry chains, Unverified exact ratio here: check EMI). Nitric acid and the benzene line come from the oil\_distill and chem chains of the HV era; chlorine from the chlor chain.
- Sub-steps people skip: (1) the zinc dust in the diaminobenzidine reactor is a NON-consumed catalyst in a ghost slot or input bus: put one dust in, do not feed a stack; (2) every step has a by-product (hydrochloric acid, diluted sulfuric acid, phenol, hydrogen sulfide), void or recycle it into the chlor line before it fills the output hatch and stops the reactor; (3) the final step returns 1 B phenol: pipe it back to the diphenyl isophthalate reactor; (4) 1008 mB per craft, not 1000: the drum overflows by 8 mB, so leave room.
- The Chemical Plant skips (kjs chemical\_plant.js, a UV multiblock) cover fluoroantimonic acid, the platinum line, the naquadah line, uranite, persulfate, iron III chloride, borax and others, but none of the PBI steps, so the chain above is the only PBI route in the pack as far as the scripts show. Unverified: the exact nitration mixture recipe.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_chemical_reactor` | 1 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:ev_chemical_reactor` | 1 |
| `gtceu:large_chemical_reactor` | 2 |
| `gtceu:iv_chemical_reactor` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Main source for:** `gtceu:polybenzimidazole_bucket`, `gtceu:polybenzimidazole_plate`, `gtceu:polybenzimidazole_foil`
