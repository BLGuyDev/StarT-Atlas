---
kind: chain
id: oil_distill
order: 1060
data:
  t: |-
    Oil in a Distillery (no tower): methane from light oil, benzene from heavy oil
  inf: true
  "n":
    - [ho, Heavy oil 16 B, f, "gtceu:oil_heavy_bucket"]
    - [lo, Light oil 16 B, f, "gtceu:oil_light_bucket"]
    - [d1, "MV Distillery · circuit 1 · 72 EU/t", m, "gtceu:mv_distillery"]
    - [sh, Sulfuric heavy fuel, f, "gtceu:sulfuric_heavy_fuel_bucket"]
    - [hy, Hydrogen, f, "gtceu:hydrogen_bucket"]
    - [r1, "Reactor · desulfurize · 8 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [hf, Heavy fuel, f, "gtceu:heavy_fuel_bucket"]
    - [d2, "LV Distillery · circuit 2 · 24 EU/t", m, "gtceu:lv_distillery"]
    - [bz, Benzene, o, "gtceu:benzene_bucket"]
    - [d3, "LV Distillery · circuit 4 · 24 EU/t", m, "gtceu:lv_distillery"]
    - [sg, Sulfuric gas, f, "gtceu:sulfuric_gas_bucket"]
    - [r2, "Reactor · desulfurize · 8 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [rg, Refinery gas, f, "gtceu:refinery_gas_bucket"]
    - [d4, "LV Distillery · circuit 4 · 30 EU/t", m, "gtceu:lv_distillery"]
    - [me, Methane, o, "gtceu:methane_bucket"]
    - [hs, Hydrogen sulfide, f, "gtceu:hydrogen_sulfide_bucket"]
    - [ox, Oxygen 4 B, f, "gtceu:oxygen_bucket"]
    - [r3, "Reactor · circuit 2 · 16 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [sa, Sulfuric acid, o, "gtceu:sulfuric_acid_bucket"]
  e:
    - [ho, d1, "100 → 250"]
    - [d1, sh]
    - [sh, r1, "8 B"]
    - [hy, r1, "2 B"]
    - [r1, hf, "8 B"]
    - [hf, d2, "10 → 4"]
    - [d2, bz]
    - [lo, d3, "150 → 240"]
    - [d3, sg]
    - [sg, r2, "16 B"]
    - [hy, r2, "2 B"]
    - [r2, rg, "16 B"]
    - [rg, d4, "1000 → 750"]
    - [d4, me]
    - [r1, hs, "1 B"]
    - [r2, hs, "1 B"]
    - [hs, r3, "1 B"]
    - [ox, r3]
    - [r3, sa]
  tips:
    - |-
      The tower is EV (controller: 4 EV circuits), but every tower recipe also exists in the single-block Distillery: one recipe per output, circuit = the output’s position, EU/t = tower EU/t divided by 4, amounts divided when they divide evenly. Source: GTRecipeTypes onRecipeBuild in the fork. The catch: a run gives only that one fraction and wastes the rest, so pick the oil that is rich in it.
    - Heavy oil (100 mB) → 250 sulfuric heavy fuel (circuit 1, tower 288 EU/t → 72 EU/t, so an MV hatch). Light oil (150 mB) → 240 sulfuric gas (circuit 4, 24 EU/t, LV). Raw (medium) oil gives 150 naphtha per 100 mB on circuit 3; plain oil (bio chaff) 50 mB gives 15 heavy fuel / 50 light fuel / 20 naphtha / 60 gas. Pyrolyse numbers are in the oil_pyro chain.
    - |-
      Desulfurize (chemical reactor, 8 s, 30 EU/t): 8 B sulfuric heavy fuel + 2 B hydrogen → 8 B heavy fuel + 1 B hydrogen sulfide; 16 B sulfuric gas + 2 B hydrogen → 16 B refinery gas + 1 B hydrogen sulfide.
    - |-
      Benzene: 10 mB heavy fuel → 4 mB benzene on circuit 2, 24 EU/t (that recipe already exists as a distillery recipe). Toluene is circuit 1 (10 → 4) and phenol circuit 3 (20 → 5). 16 B of pyrolysed heavy oil (32 logs) ends as 40 B sulfuric heavy fuel → 40 B heavy fuel (10 B hydrogen) → 16 B benzene. Benzene is the HV gas turbine fuel (352 EU per mB).
    - |-
      Methane: refinery gas 1000 mB → 750 methane on circuit 4 (butane 60 / propane 70 / ethane 100 / helium 20 are the other circuits 1, 2, 3, 5, 30 EU/t). 16 B light oil (32 wood dust) ends as 25.6 B sulfuric gas → 25.6 B refinery gas → 19.2 B methane. PTFE chloroform needs 1 B methane per 6 B chlorine.
    - |-
      Hydrogen sulfide is a by-product, not waste: 1 B hydrogen sulfide + 4 B oxygen → 1 B sulfuric acid (reactor, circuit 2, 16 s, 30 EU/t). Sulfuric acid feeds the plastic board step (250 mB per board) and the ethanol → ethylene step.
    - |-
      Unverified: the tank size of an LV or MV reactor against the 16 B and 8 B batch recipes (read the machine tooltip; if the batch does not fit, run the step in the Large Chemical Reactor). Also unverified: Oil Cracking Unit (cracker: 4 cupronickel coils, 2 HV pumps, 2 HV circuits, HV hull) layout and use for ethylene; steam cracked ethane gives 250 mB ethylene per 1000 mB in the tower recipe, the pack removed the chemical reactor cracking recipes.
    - |-
      This replaces the “waits for the EV tower” note in the oil_pyro chain: the Distillery already turns the oven’s oil into methane, benzene and sulfuric acid at HV.
  b:
    - ["gtceu:mv_distillery", 1]
    - ["gtceu:lv_distillery", 3]
    - ["gtceu:lv_chemical_reactor", 3]
    - ["gtceu:steel_drum", 8]
    - ["pipez:fluid_pipe", 24]
  how:
    - i: ["gtceu:steel_drum", "gtceu:oil_heavy_bucket", "gtceu:oil_light_bucket"]
      t: |-
        Buffer first: one steel drum for heavy oil and one for light oil (both from the Pyrolyse Oven line), then one drum for each product: sulfuric heavy fuel, heavy fuel, benzene, sulfuric gas, refinery gas, methane, hydrogen sulfide, sulfuric acid. Never put two fluids in one drum. Pipez fluid pipes with a filter, or pump covers, between every pair.
    - i: ["gtceu:mv_distillery", "gtceu:sulfuric_heavy_fuel_bucket"]
      t: |-
        Distillery 1 (MV, because the recipe is 72 EU/t): ghost circuit 1, heavy oil in, 100 mB → 250 mB sulfuric heavy fuel. The other three fractions are lost, that is the price of no tower. It is the only machine here that needs MV power; build it from your MV circuits and the pack’s MV pump (cupronickel spring, 2 MV circuits, MV hull, MV pump, 2 copper cables, 2 glass).
    - i: ["gtceu:lv_chemical_reactor", "gtceu:heavy_fuel_bucket", "gtceu:hydrogen_bucket"]
      t: |-
        Reactor 1, ghost circuit none: sulfuric heavy fuel + hydrogen in a 4:1 ratio (8 B : 2 B) → heavy fuel + hydrogen sulfide, 8 s, 30 EU/t. Hydrogen from the chlorine or water electrolysis line. Send the hydrogen sulfide to its own drum, never back into the reactor tanks.
    - i: ["gtceu:lv_distillery", "gtceu:benzene_bucket"]
      t: |-
        Distillery 2 (LV), ghost circuit 2: heavy fuel in, 10 mB → 4 mB benzene, 16 ticks at 24 EU/t. Benzene drum: it fuels the HV Gas Turbines. Distillery with circuit 1 would make toluene, circuit 3 phenol: use another machine, never change the circuit.
    - i: ["gtceu:lv_distillery", "gtceu:sulfuric_gas_bucket"]
      t: |-
        Distillery 3 (LV), ghost circuit 4: light oil in, 150 mB → 240 mB sulfuric gas at 24 EU/t. Light oil comes from 32 wood dust in the oven (circuit 3, 16 B). If you only run heavy oil, the same circuit 4 gives 60 mB gas per 100 mB oil, 0.6 per mB instead of 1.6.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:refinery_gas_bucket"]
      t: |-
        Reactor 2: 16 B sulfuric gas + 2 B hydrogen → 16 B refinery gas + 1 B hydrogen sulfide, 8 s, 30 EU/t. A drum between the distillery and the reactor smooths the batch, because the reactor waits for the whole 16 B.
    - i: ["gtceu:lv_distillery", "gtceu:methane_bucket"]
      t: |-
        Distillery 4 (LV), ghost circuit 4: refinery gas in, 1000 mB → 750 mB methane at 30 EU/t. Methane goes to PTFE reactor 1 (chlorine + methane → chloroform) and to the gas turbines (112 EU per mB). Ethane (circuit 3), propane (2), butane (1) and helium (5) need their own machines if you ever want them.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:hydrogen_sulfide_bucket", "gtceu:sulfuric_acid_bucket"]
      t: |-
        Reactor 3, ghost circuit 2: 1 B hydrogen sulfide + 4 B oxygen → 1 B sulfuric acid, 16 s, 30 EU/t. Oxygen from the air line. Sulfuric acid goes into the plastic board and ethylene steps.
    - i: ["gtceu:oil_heavy_bucket", "gtceu:pyrolyse_oven"]
      t: |-
        Easy to miss: one oven run (32 logs) makes 16 B of heavy oil, 15 s with Kanthal coils (20 s on cupronickel) at 384 EU/t. The distilleries do not care how fast it arrives, so stop the oven when the drums are full instead of building more distilleries. Never route the same oil into two distilleries to get two fractions: each run eats its own oil.
---
# Oil in a Distillery (no tower): methane from light oil, benzene from heavy oil

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `oil_distill` · **Tags:** Infinite source, Unverified

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Oil without wells (pyrolyse + distillery)](../../plan/p8.md#oil)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-d1">
<div class="gt-head"><span class="gt-mname">MV Distillery · circuit 1 · 72 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Heavy oil 16 B (gtceu:oil_heavy_bucket) - 100 → 250"><img class="gt-ico" src="../../assets/icons/gtceu__oil_heavy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Heavy</span><span class="gt-note">Heavy oil 16 B</span><b class="gt-q">100 → 250</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sulfuric heavy fuel (gtceu:sulfuric_heavy_fuel_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Heavy Fuel</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-r1">
<div class="gt-head"><span class="gt-mname">Reactor · desulfurize · 8 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfuric heavy fuel (gtceu:sulfuric_heavy_fuel_bucket) - 8 B"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Heavy Fuel</span><b class="gt-q">8 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Heavy fuel (gtceu:heavy_fuel_bucket) - 8 B"><img class="gt-ico" src="../../assets/icons/gtceu__heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Heavy Fuel</span><b class="gt-q">8 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen sulfide (gtceu:hydrogen_sulfide_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_sulfide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen Sulfide</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-d2">
<div class="gt-head"><span class="gt-mname">LV Distillery · circuit 2 · 24 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Heavy fuel (gtceu:heavy_fuel_bucket) - 10 → 4"><img class="gt-ico" src="../../assets/icons/gtceu__heavy_fuel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Heavy Fuel</span><b class="gt-q">10 → 4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Benzene (gtceu:benzene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__benzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Benzene Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-d3">
<div class="gt-head"><span class="gt-mname">LV Distillery · circuit 4 · 24 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Light oil 16 B (gtceu:oil_light_bucket) - 150 → 240"><img class="gt-ico" src="../../assets/icons/gtceu__oil_light_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Light</span><span class="gt-note">Light oil 16 B</span><b class="gt-q">150 → 240</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sulfuric gas (gtceu:sulfuric_gas_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Gas</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-r2">
<div class="gt-head"><span class="gt-mname">Reactor · desulfurize · 8 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfuric gas (gtceu:sulfuric_gas_bucket) - 16 B"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Gas</span><b class="gt-q">16 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Refinery gas (gtceu:refinery_gas_bucket) - 16 B"><img class="gt-ico" src="../../assets/icons/gtceu__refinery_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Refinery Gas</span><b class="gt-q">16 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen sulfide (gtceu:hydrogen_sulfide_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_sulfide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen Sulfide</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-d4">
<div class="gt-head"><span class="gt-mname">LV Distillery · circuit 4 · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Refinery gas (gtceu:refinery_gas_bucket) - 1000 → 750"><img class="gt-ico" src="../../assets/icons/gtceu__refinery_gas_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Refinery Gas</span><b class="gt-q">1000 → 750</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Methane (gtceu:methane_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__methane_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Methane Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-r3">
<div class="gt-head"><span class="gt-mname">Reactor · circuit 2 · 16 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Hydrogen sulfide (gtceu:hydrogen_sulfide_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_sulfide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen Sulfide</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-fluid" title="Oxygen 4 B (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><span class="gt-note">Oxygen 4 B</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Sulfuric acid (gtceu:sulfuric_acid_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Acid Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [MV Distillery · circuit 1 · 72 EU/t](#m-d1) → [Reactor · desulfurize · 8 s · 30 EU/t](#m-r1) → [LV Distillery · circuit 2 · 24 EU/t](#m-d2) (also Reactor · desulfurize · 8 s · 30 EU/t → [Reactor · circuit 2 · 16 s · 30 EU/t](#m-r3))
- [LV Distillery · circuit 4 · 24 EU/t](#m-d3) → [Reactor · desulfurize · 8 s · 30 EU/t](#m-r2) → [LV Distillery · circuit 4 · 30 EU/t](#m-d4) (also Reactor · desulfurize · 8 s · 30 EU/t → [Reactor · circuit 2 · 16 s · 30 EU/t](#m-r3))
- [Reactor · circuit 2 · 16 s · 30 EU/t](#m-r3)

## How to build

1. Buffer first: one steel drum for heavy oil and one for light oil (both from the Pyrolyse Oven line), then one drum for each product: sulfuric heavy fuel, heavy fuel, benzene, sulfuric gas, refinery gas, methane, hydrogen sulfide, sulfuric acid. Never put two fluids in one drum. Pipez fluid pipes with a filter, or pump covers, between every pair. — `gtceu:steel_drum`, `gtceu:oil_heavy_bucket`, `gtceu:oil_light_bucket`
2. Distillery 1 (MV, because the recipe is 72 EU/t): ghost circuit 1, heavy oil in, 100 mB → 250 mB sulfuric heavy fuel. The other three fractions are lost, that is the price of no tower. It is the only machine here that needs MV power; build it from your MV circuits and the pack’s MV pump (cupronickel spring, 2 MV circuits, MV hull, MV pump, 2 copper cables, 2 glass). — `gtceu:mv_distillery`, `gtceu:sulfuric_heavy_fuel_bucket`
3. Reactor 1, ghost circuit none: sulfuric heavy fuel + hydrogen in a 4:1 ratio (8 B : 2 B) → heavy fuel + hydrogen sulfide, 8 s, 30 EU/t. Hydrogen from the chlorine or water electrolysis line. Send the hydrogen sulfide to its own drum, never back into the reactor tanks. — `gtceu:lv_chemical_reactor`, `gtceu:heavy_fuel_bucket`, `gtceu:hydrogen_bucket`
4. Distillery 2 (LV), ghost circuit 2: heavy fuel in, 10 mB → 4 mB benzene, 16 ticks at 24 EU/t. Benzene drum: it fuels the HV Gas Turbines. Distillery with circuit 1 would make toluene, circuit 3 phenol: use another machine, never change the circuit. — `gtceu:lv_distillery`, `gtceu:benzene_bucket`
5. Distillery 3 (LV), ghost circuit 4: light oil in, 150 mB → 240 mB sulfuric gas at 24 EU/t. Light oil comes from 32 wood dust in the oven (circuit 3, 16 B). If you only run heavy oil, the same circuit 4 gives 60 mB gas per 100 mB oil, 0.6 per mB instead of 1.6. — `gtceu:lv_distillery`, `gtceu:sulfuric_gas_bucket`
6. Reactor 2: 16 B sulfuric gas + 2 B hydrogen → 16 B refinery gas + 1 B hydrogen sulfide, 8 s, 30 EU/t. A drum between the distillery and the reactor smooths the batch, because the reactor waits for the whole 16 B. — `gtceu:lv_chemical_reactor`, `gtceu:refinery_gas_bucket`
7. Distillery 4 (LV), ghost circuit 4: refinery gas in, 1000 mB → 750 mB methane at 30 EU/t. Methane goes to PTFE reactor 1 (chlorine + methane → chloroform) and to the gas turbines (112 EU per mB). Ethane (circuit 3), propane (2), butane (1) and helium (5) need their own machines if you ever want them. — `gtceu:lv_distillery`, `gtceu:methane_bucket`
8. Reactor 3, ghost circuit 2: 1 B hydrogen sulfide + 4 B oxygen → 1 B sulfuric acid, 16 s, 30 EU/t. Oxygen from the air line. Sulfuric acid goes into the plastic board and ethylene steps. — `gtceu:lv_chemical_reactor`, `gtceu:hydrogen_sulfide_bucket`, `gtceu:sulfuric_acid_bucket`
9. Easy to miss: one oven run (32 logs) makes 16 B of heavy oil, 15 s with Kanthal coils (20 s on cupronickel) at 384 EU/t. The distilleries do not care how fast it arrives, so stop the oven when the drums are full instead of building more distilleries. Never route the same oil into two distilleries to get two fractions: each run eats its own oil. — `gtceu:oil_heavy_bucket`, `gtceu:pyrolyse_oven`

## Tips

- The tower is EV (controller: 4 EV circuits), but every tower recipe also exists in the single-block Distillery: one recipe per output, circuit = the output’s position, EU/t = tower EU/t divided by 4, amounts divided when they divide evenly. Source: GTRecipeTypes onRecipeBuild in the fork. The catch: a run gives only that one fraction and wastes the rest, so pick the oil that is rich in it.
- Heavy oil (100 mB) → 250 sulfuric heavy fuel (circuit 1, tower 288 EU/t → 72 EU/t, so an MV hatch). Light oil (150 mB) → 240 sulfuric gas (circuit 4, 24 EU/t, LV). Raw (medium) oil gives 150 naphtha per 100 mB on circuit 3; plain oil (bio chaff) 50 mB gives 15 heavy fuel / 50 light fuel / 20 naphtha / 60 gas. Pyrolyse numbers are in the oil\_pyro chain.
- Desulfurize (chemical reactor, 8 s, 30 EU/t): 8 B sulfuric heavy fuel + 2 B hydrogen → 8 B heavy fuel + 1 B hydrogen sulfide; 16 B sulfuric gas + 2 B hydrogen → 16 B refinery gas + 1 B hydrogen sulfide.
- Benzene: 10 mB heavy fuel → 4 mB benzene on circuit 2, 24 EU/t (that recipe already exists as a distillery recipe). Toluene is circuit 1 (10 → 4) and phenol circuit 3 (20 → 5). 16 B of pyrolysed heavy oil (32 logs) ends as 40 B sulfuric heavy fuel → 40 B heavy fuel (10 B hydrogen) → 16 B benzene. Benzene is the HV gas turbine fuel (352 EU per mB).
- Methane: refinery gas 1000 mB → 750 methane on circuit 4 (butane 60 / propane 70 / ethane 100 / helium 20 are the other circuits 1, 2, 3, 5, 30 EU/t). 16 B light oil (32 wood dust) ends as 25.6 B sulfuric gas → 25.6 B refinery gas → 19.2 B methane. PTFE chloroform needs 1 B methane per 6 B chlorine.
- Hydrogen sulfide is a by-product, not waste: 1 B hydrogen sulfide + 4 B oxygen → 1 B sulfuric acid (reactor, circuit 2, 16 s, 30 EU/t). Sulfuric acid feeds the plastic board step (250 mB per board) and the ethanol → ethylene step.
- **Unverified** the tank size of an LV or MV reactor against the 16 B and 8 B batch recipes (read the machine tooltip; if the batch does not fit, run the step in the Large Chemical Reactor). Also unverified: Oil Cracking Unit (cracker: 4 cupronickel coils, 2 HV pumps, 2 HV circuits, HV hull) layout and use for ethylene; steam cracked ethane gives 250 mB ethylene per 1000 mB in the tower recipe, the pack removed the chemical reactor cracking recipes.
- This replaces the “waits for the EV tower” note in the oil\_pyro chain: the Distillery already turns the oven’s oil into methane, benzene and sulfuric acid at HV.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_distillery` | 1 |
| `gtceu:lv_distillery` | 3 |
| `gtceu:lv_chemical_reactor` | 3 |
| `gtceu:steel_drum` | 8 |
| `pipez:fluid_pipe` | 24 |

## Needs / Feeds

- **Main source for:** `gtceu:sulfuric_heavy_fuel_bucket`, `gtceu:heavy_fuel_bucket`, `gtceu:sulfuric_gas_bucket`, `gtceu:refinery_gas_bucket`, `gtceu:hydrogen_sulfide_bucket`
