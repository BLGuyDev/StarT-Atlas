---
kind: chain
id: power_hv
order: 260
data:
  t: "HV power: diatron gems in Lapidary Dynamos"
  power: true
  "n":
    - [en, "Energium dust (5 redstone + 4 ruby)", i, "gtceu:energium_dust"]
    - [dd, "2 Diamond dust", i, "gtceu:diamond_dust"]
    - [hm, HV Mixer, m, "gtceu:hv_mixer"]
    - [dt, "3 Diatron dust", x, "gtceu:diatron_dust"]
    - [ac, "HV Autoclave · distilled water", m, "gtceu:hv_autoclave"]
    - [dg, Diatron gem, x, "gtceu:diatron_gem"]
    - [d2, "2 Lapidary Dynamos + HV kits", p, "thermal:dynamo_lapidary"]
    - [cv, HV 4A Converter, m, "gtceu:hv_4a_energy_converter"]
    - [w, Lumium wire, x, "gtceu:lumium_single_wire"]
    - [mc, HV machines, o, "gtceu:hv_assembler"]
    - [bz, "Methane / benzene (option)", f, "gtceu:benzene_bucket"]
    - [gt, "HV Gas Turbine (option)", p, "gtceu:hv_gas_turbine"]
  e:
    - [en, hm, "1"]
    - [dd, hm, "2"]
    - [hm, dt, "6 s"]
    - [dt, ac, "1"]
    - [ac, dg, "7.5 s"]
    - [dg, d2, "12.5 s each"]
    - [d2, cv, FE]
    - [cv, w, "512 V"]
    - [w, mc]
    - [bz, gt]
    - [gt, w, EU]
  tips:
    - |-
      One diatron gem = 750 000 RF in a lapidary. The pack code gives the HV Upgrade Kit a ×15 multiplier on the 200 RF/t base (kit base mod (2^index + 1) / 2 x 6): 3 000 RF/t = 750 EU/t and a gem every 12.5 s (4.8 a minute). The quest text says ×24 (4 800 RF/t = 1 200 EU/t per dynamo) and community reports measured about 115 kRF/t from 24 dynamos: check the kit tooltip before you size the converters.
    - |-
      Multi-Cycle Injector (MCI) augments raise the energy per fuel, not the power: ×1.15 (LV), 1.30 (MV), 1.45 (HV), 1.60 (EV) each, stacking multiplicatively: three HV MCI = ×3.05 (a 300 000 RF diamond gives 914 700), three EV MCI = ×4.1. ARC augments do the opposite (more power, less efficiency).
    - The 4A converter’s ceiling is 2 048 EU/t = 8 192 FE/t, so at ×15 two dynamos (1 500 EU/t) fit one converter and a third would waste output; at ×24 two dynamos give 9 600 FE/t, so one converter takes only 1.7 of them.
    - |-
      A gem costs 2/3 of a diamond (2 diamond dust per 3 diatron dust) and 1/3 of an energium dust. Two dynamos need about 9.6 gems a minute: 6.4 diamonds a minute.
    - Flawless diatron = 2 gems (laser engraver, white lens, 8 s, 240 EU/t) → 2.5× value; exquisite = 2 flawless → 6.25×. Four gems as one exquisite give 56 % more energy.
    - Flux dust only comes from an LCR recipe at 1 024 EU/t (EV hatch). But the quest shop (repeatable) sells 8 flux plugs + 8 flux points for 16 coins as soon as you have built the Large Chemical Reactor, so Flux Networks is available at HV. Or put the converter next to the dynamos.
  b:
    - ["thermal:dynamo_lapidary", 2]
    - ["kubejs:hv_upgrade_kit", 2]
    - ["gtceu:hv_4a_energy_converter", 1]
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:hv_mixer", 1]
    - ["gtceu:hv_autoclave", 1]
    - ["functionalstorage:oak_1", 5]
    - ["modularrouters:modular_router", 2]
    - ["gtceu:lv_robot_arm", 3]
    - ["gtceu:item_filter", 3]
    - ["pipez:fluid_pipe", 8]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:mv_mixer", "gtceu:energium_dust", "gtceu:ruby_dust"]
      t: |-
        Energium dust, MV Mixer with ghost circuit 1: 5 redstone dust + 4 ruby dust → 9 energium dust in 30 s at 120 EU/t. Ruby: crushed ruby ore from the flint-mesh sand sieve (10 %, sieving.js) or the Electric Ore Factory, macerated. One batch makes 27 gems, so this step runs rarely.
    - i: ["gtceu:hv_mixer", "gtceu:diatron_dust"]
      t: |-
        Diatron dust, HV Mixer (480 EU/t): 1 energium dust + 2 diamond dust → 3 diatron dust in 6 s. Pack recipe (thermal.js). Diamonds come from the sand sieve; a router moves them from their drawer.
    - i: ["gtceu:hv_autoclave", "gtceu:diatron_gem", "gtceu:distilled_water_bucket"]
      t: |-
        Gems, HV Autoclave: 1 diatron dust + 50 mB distilled water → 1 gem in 30 s at 24 EU/t, which an HV autoclave overclocks twice to 7.5 s at 384 EU/t = 8 gems a minute. With plain water (250 mB) the chance is 70 % and it takes 60 s, so use distilled water.
    - i: ["thermal:dynamo_lapidary", "kubejs:hv_upgrade_kit"]
      t: |-
        Two Lapidary Dynamos, each with an HV Upgrade Kit (4 electrum plates + lumium glass + aluminium gear + HV circuit + 720 mB glowstone, 30 s at 480 EU/t in an HV assembler). A Robot Arm or router feeds gems from the gem drawer: each dynamo burns one every 12.5 s for 3 000 RF/t.
    - i: ["gtceu:hv_4a_energy_converter", "gtceu:lumium_ingot"]
      t: |-
        HV 4A Energy Converter = 4 lumium quadruple wire + 1 HV circuit + HV hull (pack recipe). Lumium: silver + 3 tin + 2 glowstone dust in a mixer (20 s, 80 EU/t) → 4 dust → EBF 1700 K, 480 EU/t, 50 s per ingot; 8 ingots (2 per quadruple wire in a wiremill). Place the converter touching the dynamos; FE goes in and 512 V EU comes out of its output face (wire goes there).
    - i: ["gtceu:lumium_single_wire", "gtceu:hv_assembler"]
      t: |-
        Lumium wire is a loss-free superconductor in this pack: 16 A per single wire (8 192 EU/t), no insulation needed. Run it from the converter to a distribution row and to your HV machines; one wire carries more than the converter can give.
    - i: ["gtceu:hv_gas_turbine", "gtceu:benzene_bucket"]
      t: |-
        Option: HV Gas Turbine (512 EU/t, 16 times the LV recipe at once). Fuel energy per mB (from FuelRecipes): methane 112 EU, benzene 352, ethylene 128, wood gas 24. A turbine on methane burns 4.6 mB a tick (5.5 B a minute), on benzene 1.45 mB a tick (1.7 B a minute). Put a pump cover and a fuel drum before each turbine.
    - i: ["functionalstorage:oak_1", "gtceu:diatron_gem"]
      t: |-
        Easy to miss: the Thermal dynamo’s own output cap and how many sides of the converter accept FE were not verified; place one dynamo, watch the energy readout, and only then build the second. The BOM lists no flux parts: plugs and points come from the quest shop (16 coins for 8 + 8), not from crafting.
---
# HV power: diatron gems in Lapidary Dynamos

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_hv` · **Tags:** Power

**Plan modules:** [HV power: diatron gems in lapidary dynamos](../../plan/p8.md#hvpower)

**Tips:** 6

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-hm">
<div class="gt-head"><span class="gt-mname">HV Mixer</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Energium dust (5 redstone + 4 ruby) (gtceu:energium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__energium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energium Dust</span><span class="gt-note">Energium dust (5 redstone + 4 ruby)</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Diamond dust (gtceu:diamond_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__diamond_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond Dust</span><span class="gt-note">2 Diamond dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">6 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="3 Diatron dust (gtceu:diatron_dust) - 6 s"><img class="gt-ico" src="../../assets/icons/gtceu__diatron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diatron Dust</span><span class="gt-note">3 Diatron dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_mixer</code></div>
</div>
<div class="gt-panel t-hv" id="m-ac">
<div class="gt-head"><span class="gt-mname">HV Autoclave · distilled water</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Diatron dust (gtceu:diatron_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__diatron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diatron Dust</span><span class="gt-note">3 Diatron dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Diatron gem (gtceu:diatron_gem) - 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__diatron_gem.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diatron Gem</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-d2">
<div class="gt-head"><span class="gt-mname">2 Lapidary Dynamos + HV kits</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Diatron gem (gtceu:diatron_gem) - 12.5 s each"><img class="gt-ico" src="../../assets/icons/gtceu__diatron_gem.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diatron Gem</span><b class="gt-q">12.5 s each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cv" title="HV 4A Converter (gtceu:hv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__hv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV 4a Energy Converter</span><span class="gt-note">HV 4A Converter</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_lapidary</code></div>
</div>
<div class="gt-panel t-hv" id="m-cv">
<div class="gt-head"><span class="gt-mname">HV 4A Converter</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-d2" title="2 Lapidary Dynamos + HV kits (thermal:dynamo_lapidary) - FE"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">2 Lapidary Dynamos + HV kits</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Lumium wire (gtceu:lumium_single_wire) - 512 V"><img class="gt-ico" src="../../assets/icons/gtceu__lumium_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lumium Single Wire</span><span class="gt-note">Lumium wire</span><b class="gt-q">512 V</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_4a_energy_converter</code></div>
</div>
<div class="gt-panel t-hv gt-gen" id="m-gt">
<div class="gt-head"><span class="gt-mname">HV Gas Turbine (option)</span><span class="gt-badge t-hv">HV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Methane / benzene (option) (gtceu:benzene_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__benzene_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Benzene</span><span class="gt-note">Methane / benzene (option)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_gas_turbine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Lumium wire (gtceu:lumium_single_wire) - EU"><img class="gt-ico" src="../../assets/icons/gtceu__lumium_single_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lumium Single Wire</span><span class="gt-note">Lumium wire</span><b class="gt-q">EU</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_gas_turbine</code></div>
</div>
</div>

## Flow

- [HV Mixer](#m-hm) → [HV Autoclave · distilled water](#m-ac) → [2 Lapidary Dynamos + HV kits](#m-d2) → [HV 4A Converter](#m-cv)
- [HV Gas Turbine (option)](#m-gt)

### Direct steps

- Lumium wire → HV machines

## How to build

1. Energium dust, MV Mixer with ghost circuit 1: 5 redstone dust + 4 ruby dust → 9 energium dust in 30 s at 120 EU/t. Ruby: crushed ruby ore from the flint-mesh sand sieve (10 %, sieving.js) or the Electric Ore Factory, macerated. One batch makes 27 gems, so this step runs rarely. — `gtceu:mv_mixer`, `gtceu:energium_dust`, `gtceu:ruby_dust`
2. Diatron dust, HV Mixer (480 EU/t): 1 energium dust + 2 diamond dust → 3 diatron dust in 6 s. Pack recipe (thermal.js). Diamonds come from the sand sieve; a router moves them from their drawer. — `gtceu:hv_mixer`, `gtceu:diatron_dust`
3. Gems, HV Autoclave: 1 diatron dust + 50 mB distilled water → 1 gem in 30 s at 24 EU/t, which an HV autoclave overclocks twice to 7.5 s at 384 EU/t = 8 gems a minute. With plain water (250 mB) the chance is 70 % and it takes 60 s, so use distilled water. — `gtceu:hv_autoclave`, `gtceu:diatron_gem`, `gtceu:distilled_water_bucket`
4. Two Lapidary Dynamos, each with an HV Upgrade Kit (4 electrum plates + lumium glass + aluminium gear + HV circuit + 720 mB glowstone, 30 s at 480 EU/t in an HV assembler). A Robot Arm or router feeds gems from the gem drawer: each dynamo burns one every 12.5 s for 3 000 RF/t. — `thermal:dynamo_lapidary`, `kubejs:hv_upgrade_kit`
5. HV 4A Energy Converter = 4 lumium quadruple wire + 1 HV circuit + HV hull (pack recipe). Lumium: silver + 3 tin + 2 glowstone dust in a mixer (20 s, 80 EU/t) → 4 dust → EBF 1700 K, 480 EU/t, 50 s per ingot; 8 ingots (2 per quadruple wire in a wiremill). Place the converter touching the dynamos; FE goes in and 512 V EU comes out of its output face (wire goes there). — `gtceu:hv_4a_energy_converter`, `gtceu:lumium_ingot`
6. Lumium wire is a loss-free superconductor in this pack: 16 A per single wire (8 192 EU/t), no insulation needed. Run it from the converter to a distribution row and to your HV machines; one wire carries more than the converter can give. — `gtceu:lumium_single_wire`, `gtceu:hv_assembler`
7. Option: HV Gas Turbine (512 EU/t, 16 times the LV recipe at once). Fuel energy per mB (from FuelRecipes): methane 112 EU, benzene 352, ethylene 128, wood gas 24. A turbine on methane burns 4.6 mB a tick (5.5 B a minute), on benzene 1.45 mB a tick (1.7 B a minute). Put a pump cover and a fuel drum before each turbine. — `gtceu:hv_gas_turbine`, `gtceu:benzene_bucket`
8. Easy to miss: the Thermal dynamo’s own output cap and how many sides of the converter accept FE were not verified; place one dynamo, watch the energy readout, and only then build the second. The BOM lists no flux parts: plugs and points come from the quest shop (16 coins for 8 + 8), not from crafting. — `functionalstorage:oak_1`, `gtceu:diatron_gem`

## Tips

- One diatron gem = 750 000 RF in a lapidary. The pack code gives the HV Upgrade Kit a ×15 multiplier on the 200 RF/t base (kit base mod (2^index + 1) / 2 x 6): 3 000 RF/t = 750 EU/t and a gem every 12.5 s (4.8 a minute). The quest text says ×24 (4 800 RF/t = 1 200 EU/t per dynamo) and community reports measured about 115 kRF/t from 24 dynamos: check the kit tooltip before you size the converters.
- Multi-Cycle Injector (MCI) augments raise the energy per fuel, not the power: ×1.15 (LV), 1.30 (MV), 1.45 (HV), 1.60 (EV) each, stacking multiplicatively: three HV MCI = ×3.05 (a 300 000 RF diamond gives 914 700), three EV MCI = ×4.1. ARC augments do the opposite (more power, less efficiency).
- The 4A converter’s ceiling is 2 048 EU/t = 8 192 FE/t, so at ×15 two dynamos (1 500 EU/t) fit one converter and a third would waste output; at ×24 two dynamos give 9 600 FE/t, so one converter takes only 1.7 of them.
- A gem costs 2/3 of a diamond (2 diamond dust per 3 diatron dust) and 1/3 of an energium dust. Two dynamos need about 9.6 gems a minute: 6.4 diamonds a minute.
- Flawless diatron = 2 gems (laser engraver, white lens, 8 s, 240 EU/t) → 2.5× value; exquisite = 2 flawless → 6.25×. Four gems as one exquisite give 56 % more energy.
- Flux dust only comes from an LCR recipe at 1 024 EU/t (EV hatch). But the quest shop (repeatable) sells 8 flux plugs + 8 flux points for 16 coins as soon as you have built the Large Chemical Reactor, so Flux Networks is available at HV. Or put the converter next to the dynamos.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:dynamo_lapidary` | 2 |
| `kubejs:hv_upgrade_kit` | 2 |
| `gtceu:hv_4a_energy_converter` | 1 |
| `gtceu:mv_mixer` | 1 |
| `gtceu:hv_mixer` | 1 |
| `gtceu:hv_autoclave` | 1 |
| `functionalstorage:oak_1` | 5 |
| `modularrouters:modular_router` | 2 |
| `gtceu:lv_robot_arm` | 3 |
| `gtceu:item_filter` | 3 |
| `pipez:fluid_pipe` | 8 |
| `pipez:item_pipe` | 16 |
