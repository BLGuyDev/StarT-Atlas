---
kind: chain
id: pcb_coolant
order: 590
data:
  t: |-
    PCB coolant: benzene → biphenyl → polychlorinated biphenyl → mix with distilled water (HV machines)
  inf: true
  "n":
    - [bz, "Benzene · 2 B", f, "gtceu:benzene_bucket"]
    - [ox, "Oxygen · 1 B", f, "gtceu:oxygen_bucket"]
    - [c1, "HV Chemical Reactor · circuit 1 · 20 s · 480 EU/t", m, "gtceu:hv_chemical_reactor"]
    - [bp, "2 Biphenyl dust", x, "gtceu:biphenyl_dust"]
    - [cl, "Chlorine · 4 B", f, "gtceu:chlorine_bucket"]
    - [c2, "HV Chemical Reactor · 10 s · 480 EU/t", m, "gtceu:hv_chemical_reactor"]
    - [pc, "1 B polychlorinated biphenyl", x, "gtceu:polychlorinated_biphenyl_bucket"]
    - [dw, "Distilled water · 250 mB", f, "gtceu:distilled_water_bucket"]
    - [mx, "HV Mixer · 10 s · 480 EU/t", m, "gtceu:hv_mixer"]
    - [o, "1 B PCB coolant", o, "gtceu:pcb_coolant_bucket"]
  e:
    - [bz, c1, "2 B"]
    - [ox, c1, "1 B"]
    - [c1, bp, "2 / 20 s"]
    - [bp, c2, "2"]
    - [cl, c2, "4 B"]
    - [c2, pc, "1 B / 10 s"]
    - [pc, mx, "750 mB"]
    - [dw, mx, "250 mB"]
    - [mx, o, "1 B / 10 s"]
  tips:
    - |-
      Recipes (ReactorRecipes, MixerRecipes; the pack does not change them): Biphenyl = 2 B benzene + 1 B oxygen, chemical reactor, circuit 1, 400 ticks at 480 EU/t → 2 biphenyl dust + 1 B water (alternative: 1 B benzene + 1 B toluene, 200 ticks → 2 dust + 1 B methane). Polychlorinated biphenyl = 2 biphenyl dust + 4 B chlorine → 1 B PCB + 2 B hydrochloric acid, 200 ticks, a HV chemical reactor. PCB coolant = 750 mB PCB + 250 mB distilled water, MIXER, 200 ticks at 480 EU/t (VA[HV]): an HV Mixer, not the IV Mixer the old node showed.
    - |-
      The loop is exactly closed: the Dimensional Destabiliser takes 8 B coolant per run and returns 9.6 B HOT coolant; the pack’s Vacuum Freezer recipe turns 1200 mB hot into 1000 mB cold (140 ticks, 512 EU/t, kubejs dimensional_destabilising.js), so 9.6 B hot gives back 8 B. You only make the first fill and the top-ups for leaks (and the research parts below): the cost is about 8 B plus whatever the HPCA components take (1000 mB each).
    - |-
      Raw cost of 8 B coolant: 6 B PCB = 12 biphenyl = 12 B benzene + 6 B oxygen (or 6 B benzene + 6 B toluene), 24 B chlorine (hydrochloric acid comes back, 12 B), and 2 B distilled water. Benzene: the oil_distill chain; chlorine: the chlorine chain; distilled water: the distilled chain.
    - |-
      Where else coolant goes: HPCA components (1000 mB each), the HPCA itself (4000 mB), later the research and Abydos machines. Keep a drum of 16 B or more in the research building, separate from the destabiliser drum.
    - |-
      Sub-steps people skip: (1) three machines with three products: biphenyl reactor, PCB reactor, mixer; one dedicated machine each; (2) hydrochloric acid and water by-products need a drum or a voiding cover, they stall the reactor otherwise; (3) distilled water is NOT plain water (the mixer will not start); (4) the biphenyl is a dust, so its output goes by Robot Arm into a drawer, not a pipe; (5) the freezer cools the HOT fluid only, so never pipe hot coolant to anything else.
    - |-
      Unverified: the exact recipe time of the PCB reactor (the source lists a half-voltage helper VH[HV]; treat 480 EU/t as the upper bound), and whether the pack scripts remove the toluene route.
  b:
    - ["gtceu:hv_chemical_reactor", 2]
    - ["gtceu:hv_mixer", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 5]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:benzene_bucket", "gtceu:chlorine_bucket"]
      t: |-
        Drums first: benzene, oxygen, chlorine, distilled water, hydrochloric acid (by-product), and one for the finished coolant. One dedicated machine per product, each behind its own Pipez fluid pipes with a filter, and a Robot Arm for the dust between reactors.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:biphenyl_dust"]
      t: |-
        Reactor 1: circuit 1 in the bus, 2 B benzene + 1 B oxygen → 2 biphenyl dust in 20 s at 480 EU/t (an HV hatch or a 480 EU/t cable; no overclock). Water out into a voiding drum.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:polychlorinated_biphenyl_bucket", "gtceu:hydrochloric_acid_bucket"]
      t: |-
        Reactor 2: 2 biphenyl dust + 4 B chlorine → 1 B polychlorinated biphenyl + 2 B hydrochloric acid in 10 s. The acid goes back to the chlorine chain or a drum.
    - i: ["gtceu:hv_mixer", "gtceu:distilled_water_bucket", "gtceu:pcb_coolant_bucket"]
      t: |-
        HV Mixer: 750 mB PCB + 250 mB distilled water → 1 B PCB coolant in 10 s. Output into the coolant drum.
    - i: ["gtceu:vacuum_freezer", "gtceu:hot_pcb_coolant_bucket", "gtceu:dimensional_destabiliser"]
      t: |-
        Return loop: the destabiliser’s output hatch pumps hot coolant (9.6 B per run) through a Pipez fluid pipe into a Vacuum Freezer; 1.2 B hot → 1 B cold in 7 s at 512 EU/t; its output goes straight back to the destabiliser input hatch. Add a second freezer if you run more than one destabiliser.
    - i: ["functionalstorage:oak_1", "gtceu:pcb_coolant_bucket"]
      t: |-
        Top-up: one full drum of finished coolant as a buffer. The line only runs when the destabiliser or the HPCA components call for it; do not overproduce, the biphenyl line is slow.
---
# PCB coolant: benzene → biphenyl → polychlorinated biphenyl → mix with distilled water (HV machines)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `pcb_coolant` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Naquadah and PCB coolant](../../plan/p11.md#naquadah)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-c1">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · circuit 1 · 20 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Benzene · 2 B (gtceu:benzene_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__benzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Benzene</span><span class="gt-note">Benzene · 2 B</span><b class="gt-q">2 B</b></span><span class="gt-slot gt-fluid" title="Oxygen · 1 B (gtceu:oxygen_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><span class="gt-note">Oxygen · 1 B</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Biphenyl dust (gtceu:biphenyl_dust) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__biphenyl_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Biphenyl Dust</span><span class="gt-note">2 Biphenyl dust</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-c2">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 10 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Biphenyl dust (gtceu:biphenyl_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__biphenyl_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Biphenyl Dust</span><span class="gt-note">2 Biphenyl dust</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="Chlorine · 4 B (gtceu:chlorine_bucket) - 4 B"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><span class="gt-note">Chlorine · 4 B</span><b class="gt-q">4 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="1 B polychlorinated biphenyl (gtceu:polychlorinated_biphenyl_bucket) - 1 B / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__polychlorinated_biphenyl_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polychlorinated Biphenyl Bucket</span><span class="gt-note">1 B polychlorinated biphenyl</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-mx">
<div class="gt-head"><span class="gt-mname">HV Mixer · 10 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 B polychlorinated biphenyl (gtceu:polychlorinated_biphenyl_bucket) - 750 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polychlorinated_biphenyl_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polychlorinated Biphenyl Bucket</span><span class="gt-note">1 B polychlorinated biphenyl</span><b class="gt-q">750 mB</b></span><span class="gt-slot gt-fluid" title="Distilled water · 250 mB (gtceu:distilled_water_bucket) - 250 mB"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water</span><span class="gt-note">Distilled water · 250 mB</span><b class="gt-q">250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="1 B PCB coolant (gtceu:pcb_coolant_bucket) - 1 B / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__pcb_coolant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Pcb Coolant Bucket</span><span class="gt-note">1 B PCB coolant</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_mixer</code></div>
</div>
</div>

## Flow

- [HV Chemical Reactor · circuit 1 · 20 s · 480 EU/t](#m-c1) → [HV Chemical Reactor · 10 s · 480 EU/t](#m-c2) → [HV Mixer · 10 s · 480 EU/t](#m-mx)

## How to build

1. Drums first: benzene, oxygen, chlorine, distilled water, hydrochloric acid (by-product), and one for the finished coolant. One dedicated machine per product, each behind its own Pipez fluid pipes with a filter, and a Robot Arm for the dust between reactors. — `functionalstorage:oak_1`, `gtceu:benzene_bucket`, `gtceu:chlorine_bucket`
2. Reactor 1: circuit 1 in the bus, 2 B benzene + 1 B oxygen → 2 biphenyl dust in 20 s at 480 EU/t (an HV hatch or a 480 EU/t cable; no overclock). Water out into a voiding drum. — `gtceu:hv_chemical_reactor`, `gtceu:biphenyl_dust`
3. Reactor 2: 2 biphenyl dust + 4 B chlorine → 1 B polychlorinated biphenyl + 2 B hydrochloric acid in 10 s. The acid goes back to the chlorine chain or a drum. — `gtceu:hv_chemical_reactor`, `gtceu:polychlorinated_biphenyl_bucket`, `gtceu:hydrochloric_acid_bucket`
4. HV Mixer: 750 mB PCB + 250 mB distilled water → 1 B PCB coolant in 10 s. Output into the coolant drum. — `gtceu:hv_mixer`, `gtceu:distilled_water_bucket`, `gtceu:pcb_coolant_bucket`
5. Return loop: the destabiliser’s output hatch pumps hot coolant (9.6 B per run) through a Pipez fluid pipe into a Vacuum Freezer; 1.2 B hot → 1 B cold in 7 s at 512 EU/t; its output goes straight back to the destabiliser input hatch. Add a second freezer if you run more than one destabiliser. — `gtceu:vacuum_freezer`, `gtceu:hot_pcb_coolant_bucket`, `gtceu:dimensional_destabiliser`
6. Top-up: one full drum of finished coolant as a buffer. The line only runs when the destabiliser or the HPCA components call for it; do not overproduce, the biphenyl line is slow. — `functionalstorage:oak_1`, `gtceu:pcb_coolant_bucket`

## Tips

- Recipes (ReactorRecipes, MixerRecipes; the pack does not change them): Biphenyl = 2 B benzene + 1 B oxygen, chemical reactor, circuit 1, 400 ticks at 480 EU/t → 2 biphenyl dust + 1 B water (alternative: 1 B benzene + 1 B toluene, 200 ticks → 2 dust + 1 B methane). Polychlorinated biphenyl = 2 biphenyl dust + 4 B chlorine → 1 B PCB + 2 B hydrochloric acid, 200 ticks, a HV chemical reactor. PCB coolant = 750 mB PCB + 250 mB distilled water, MIXER, 200 ticks at 480 EU/t (VA\[HV\]): an HV Mixer, not the IV Mixer the old node showed.
- The loop is exactly closed: the Dimensional Destabiliser takes 8 B coolant per run and returns 9.6 B HOT coolant; the pack’s Vacuum Freezer recipe turns 1200 mB hot into 1000 mB cold (140 ticks, 512 EU/t, kubejs dimensional\_destabilising.js), so 9.6 B hot gives back 8 B. You only make the first fill and the top-ups for leaks (and the research parts below): the cost is about 8 B plus whatever the HPCA components take (1000 mB each).
- Raw cost of 8 B coolant: 6 B PCB = 12 biphenyl = 12 B benzene + 6 B oxygen (or 6 B benzene + 6 B toluene), 24 B chlorine (hydrochloric acid comes back, 12 B), and 2 B distilled water. Benzene: the oil\_distill chain; chlorine: the chlorine chain; distilled water: the distilled chain.
- Where else coolant goes: HPCA components (1000 mB each), the HPCA itself (4000 mB), later the research and Abydos machines. Keep a drum of 16 B or more in the research building, separate from the destabiliser drum.
- Sub-steps people skip: (1) three machines with three products: biphenyl reactor, PCB reactor, mixer; one dedicated machine each; (2) hydrochloric acid and water by-products need a drum or a voiding cover, they stall the reactor otherwise; (3) distilled water is NOT plain water (the mixer will not start); (4) the biphenyl is a dust, so its output goes by Robot Arm into a drawer, not a pipe; (5) the freezer cools the HOT fluid only, so never pipe hot coolant to anything else.
- **Unverified** the exact recipe time of the PCB reactor (the source lists a half-voltage helper VH\[HV\]; treat 480 EU/t as the upper bound), and whether the pack scripts remove the toluene route.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_chemical_reactor` | 2 |
| `gtceu:hv_mixer` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 5 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:pcb_coolant_bucket`
