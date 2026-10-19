---
kind: chain
id: combo_diesel
order: 2310
data:
  t: |-
    Combo: a wall of Huge Diesel Engines on crude biodiesel (Create)
  inf: true
  power: true
  "n":
    - [po, "Plant oil · 100 mB", f, "createdieselgenerators:plant_oil_bucket"]
    - [fe, "Fermenter · 8 crops → 200 mB", m, "gtceu:lv_fermenter"]
    - [et, "Ethanol · 100 mB", f, "createdieselgenerators:ethanol_bucket"]
    - [mx, "Mechanical Mixer + basin", m, "create:mechanical_mixer"]
    - [bd, "Crude biodiesel · 200 mB", x, "createdieselgenerators:biodiesel_bucket"]
    - [se, "Steam engine, flint and steel, andesite alloy, brass, fluid pipes", i, "create:steam_engine"]
    - [hd, "Huge Diesel Engine · 12 288 SU at 224 RPM", p, "createdieselgenerators:huge_diesel_engine"]
    - [sh, Shaft line, x, "create:shaft"]
    - [gc, "Generator coils (Create New Age)", p, "create_new_age:generator_coil"]
    - [out, "208 engines = 2 555 904 SU", o, "create_new_age:generator_coil"]
  e:
    - [fe, et]
    - [po, mx]
    - [et, mx]
    - [mx, bd, "200 mB"]
    - [bd, hd, fuel]
    - [se, hd, craft]
    - [hd, sh, SU]
    - [sh, gc]
    - [gc, out]
  tips:
    - |-
      Huge Diesel Engine (createdieselgenerators jar recipe, not removed by the pack): 1 steam engine + 1 flint and steel + 2 andesite alloy + 2 brass plates + 1 brass block + 2 fluid pipes.
    - |-
      Crude biodiesel in a Huge engine (fuel_type/biodiesel.json): 12 288 SU at 224 RPM, burn rate 0.05; a modular engine gives 6 144 SU, a normal one 4 096. 208 Huge engines x 12 288 = 2 555 904 SU: the community figure of more than 2.5 M SU checks out.
    - |-
      Fuel: Create mixing, 100 plant oil + 100 ethanol → 200 crude biodiesel (recipes/mixing/biodiesel.json). GT ethanol: fermenter, 8 crops → 200 mB (early_game/casket.js). The pack removes other parts of the mod (canister, oil barrel, pumpjack, lighter: mass_removals.js).
    - |-
      SU to FE with Create New Age generator coils: FE/t = RPM x force / 20 and the coil draws RPM x (force + 24) SU; 8 coils per brush, at most 12 magnets per coil (see power_steam_engine and magnets). The engines turn at 224 RPM, under the 256 RPM Create cap.
    - |-
      The GT LCR biodiesel route (54 B fish oil + 9 B ethanol or methanol + NaOH → 54 B biodiesel, 270 s, LV) needs fish, and the only fish source is the Industrial Fishery (IV controller): it is not an early option.
    - |-
      Unverified: the real fuel use in game (burn rate 0.05 per engine), whether the Create mixer takes GT ethanol, the plant oil source in this pack, and the "32 coils at 256 RPM" layout from the same community report.
  b:
    - ["createdieselgenerators:huge_diesel_engine", 16]
    - ["create:mechanical_mixer", 1]
    - ["create:basin", 1]
    - ["create:fluid_pipe", 32]
    - ["create_new_age:generator_coil", 8]
  how:
    - i:
        - createdieselgenerators:plant_oil_bucket
        - createdieselgenerators:ethanol_bucket
        - create:mechanical_mixer
      t: |-
        Fuel: a Mechanical Mixer over a basin with plant oil and ethanol piped in (100 mB each) makes 200 mB crude biodiesel per batch; pump it into a fluid tank that feeds the engine row.
    - i: ["createdieselgenerators:huge_diesel_engine", "create:fluid_pipe"]
      t: |-
        Engines: craft Huge Diesel Engines (steam engine + flint and steel + andesite alloy + brass) and put them on one shaft line, all fed from the biodiesel tank by fluid pipes. Each adds 12 288 SU at 224 RPM.
    - i: ["create_new_age:generator_coil", "create:shaft"]
      t: |-
        Power: the shaft drives Create New Age generator coils (FE) that feed your energy converters. Add engines in blocks of 8 and check the stress meter.
---
# Combo: a wall of Huge Diesel Engines on crude biodiesel (Create)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_diesel` · **Tags:** Infinite source, Power, Unverified

**Plan modules:** [Engine wall: 208 Huge Diesel Engines on biodiesel](../../plan/p20.md#cb_diesel)

**Tips:** 6, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-fe">
<div class="gt-head"><span class="gt-mname">Fermenter · 8 crops → 200 mB</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_fermenter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Ethanol · 100 mB (createdieselgenerators:ethanol_bucket)"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__ethanol_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethanol</span><span class="gt-note">Ethanol · 100 mB</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_fermenter</code></div>
</div>
<div class="gt-panel t-mod" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mechanical Mixer + basin</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Plant oil · 100 mB (createdieselgenerators:plant_oil_bucket)"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__plant_oil_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plant Oil</span><span class="gt-note">Plant oil · 100 mB</span></span><span class="gt-slot gt-fluid" title="Ethanol · 100 mB (createdieselgenerators:ethanol_bucket)"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__ethanol_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ethanol</span><span class="gt-note">Ethanol · 100 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Crude biodiesel · 200 mB (createdieselgenerators:biodiesel_bucket) - 200 mB"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__biodiesel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Biodiesel Bucket</span><span class="gt-note">Crude biodiesel · 200 mB</span><b class="gt-q">200 mB</b></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_mixer</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-hd">
<div class="gt-head"><span class="gt-mname">Huge Diesel Engine · 12 288 SU at 224 RPM</span><span class="gt-badge t-mod">Createdieselgenerators</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crude biodiesel · 200 mB (createdieselgenerators:biodiesel_bucket) - fuel"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__biodiesel_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Biodiesel Bucket</span><span class="gt-note">Crude biodiesel · 200 mB</span><b class="gt-q">fuel</b></span><span class="gt-slot" title="Steam engine, flint and steel, andesite alloy, brass, fluid pipes (create:steam_engine) - craft"><img class="gt-ico" src="../../assets/icons/create__steam_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam Engine</span><span class="gt-note">Steam engine, flint and steel, andesite alloy, brass, fluid pipes</span><b class="gt-q">craft</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/createdieselgenerators__huge_diesel_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Shaft line (create:shaft) - SU"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shaft line</span><b class="gt-q">SU</b></span></div>
</div>
<div class="gt-foot"><code>createdieselgenerators:huge_diesel_engine</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-gc">
<div class="gt-head"><span class="gt-mname">Generator coils (Create New Age)</span><span class="gt-badge t-mod">New Age</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shaft line (create:shaft)"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shaft line</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="208 engines = 2 555 904 SU (create_new_age:generator_coil)"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Generator Coil</span><span class="gt-note">208 engines = 2 555 904 SU</span></span></div>
</div>
<div class="gt-foot"><code>create_new_age:generator_coil</code></div>
</div>
</div>

## Flow

- [Fermenter · 8 crops → 200 mB](#m-fe) → [Mechanical Mixer + basin](#m-mx) → [Huge Diesel Engine · 12 288 SU at 224 RPM](#m-hd) → [Generator coils (Create New Age)](#m-gc)

## How to build

1. Fuel: a Mechanical Mixer over a basin with plant oil and ethanol piped in (100 mB each) makes 200 mB crude biodiesel per batch; pump it into a fluid tank that feeds the engine row. — `createdieselgenerators:plant_oil_bucket`, `createdieselgenerators:ethanol_bucket`, `create:mechanical_mixer`
2. Engines: craft Huge Diesel Engines (steam engine + flint and steel + andesite alloy + brass) and put them on one shaft line, all fed from the biodiesel tank by fluid pipes. Each adds 12 288 SU at 224 RPM. — `createdieselgenerators:huge_diesel_engine`, `create:fluid_pipe`
3. Power: the shaft drives Create New Age generator coils (FE) that feed your energy converters. Add engines in blocks of 8 and check the stress meter. — `create_new_age:generator_coil`, `create:shaft`

## Tips

- Huge Diesel Engine (createdieselgenerators jar recipe, not removed by the pack): 1 steam engine + 1 flint and steel + 2 andesite alloy + 2 brass plates + 1 brass block + 2 fluid pipes.
- Crude biodiesel in a Huge engine (fuel\_type/biodiesel.json): 12 288 SU at 224 RPM, burn rate 0.05; a modular engine gives 6 144 SU, a normal one 4 096. 208 Huge engines x 12 288 = 2 555 904 SU: the community figure of more than 2.5 M SU checks out.
- Fuel: Create mixing, 100 plant oil + 100 ethanol → 200 crude biodiesel (recipes/mixing/biodiesel.json). GT ethanol: fermenter, 8 crops → 200 mB (early\_game/casket.js). The pack removes other parts of the mod (canister, oil barrel, pumpjack, lighter: mass\_removals.js).
- SU to FE with Create New Age generator coils: FE/t = RPM x force / 20 and the coil draws RPM x (force + 24) SU; 8 coils per brush, at most 12 magnets per coil (see power\_steam\_engine and magnets). The engines turn at 224 RPM, under the 256 RPM Create cap.
- The GT LCR biodiesel route (54 B fish oil + 9 B ethanol or methanol + NaOH → 54 B biodiesel, 270 s, LV) needs fish, and the only fish source is the Industrial Fishery (IV controller): it is not an early option.
- **Unverified** the real fuel use in game (burn rate 0.05 per engine), whether the Create mixer takes GT ethanol, the plant oil source in this pack, and the "32 coils at 256 RPM" layout from the same community report.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `createdieselgenerators:huge_diesel_engine` | 16 |
| `create:mechanical_mixer` | 1 |
| `create:basin` | 1 |
| `create:fluid_pipe` | 32 |
| `create_new_age:generator_coil` | 8 |

## Needs / Feeds

- **Main source for:** `createdieselgenerators:huge_diesel_engine`, `createdieselgenerators:biodiesel_bucket`
