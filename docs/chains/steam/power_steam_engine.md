---
kind: chain
id: power_steam_engine
order: 690
data:
  t: "Create steam power: Steam Engines + Generator Coils"
  inf: true
  power: true
  "n":
    - [ch, "Charcoal (router)", i, "minecraft:charcoal"]
    - [bb, "9 Basic Burners", m, "createlowheated:basic_burner"]
    - [w, "Water 90 mB/t", f, "minecraft:water_bucket"]
    - [bo, "Boiler 3×3×5 tank", m, "create:fluid_tank"]
    - [se, "9 Steam Engines", m, "create:steam_engine"]
    - [rs, "Speed controller → 256", x, "create:rotation_speed_controller"]
    - [gc, "3 Generator Coils", m, "create_new_age:generator_coil"]
    - [mg, "12 Fluxuated each", i, "create_new_age:fluxuated_magnetite"]
    - [cb, Carbon Brushes, p, "create_new_age:carbon_brushes"]
    - [cv, Energy converters, p, "gtceu:lv_4a_energy_converter"]
  e:
    - [ch, bb, "6.75 / min"]
    - [bb, bo, heat 9]
    - [w, bo]
    - [bo, se, level 9]
    - [se, rs, "64 RPM"]
    - [rs, gc]
    - [mg, gc, force 96]
    - [gc, cb, FE]
    - [cb, cv, FE]
  tips:
    - |-
      Your build: 3 coils × 12 fluxuated (force 96 each) at 136 RPM = 3 × 136 × 96 / 20 ≈ 1 958 FE/t for 48 960 SU, exactly 3 engines’ worth.
    - |-
      Same coils at 256 RPM: ≈ 3 686 FE/t for 92 160 SU (6 engines). With 9 engines (147 456 SU) you can run 4 coils at 256 RPM: ≈ 4 915 FE/t.
    - |-
      Boiler level = the lowest of: lit burners, tank blocks / 4, water / 10 mB/t. A 3×3×5 tank (45 blocks) allows level 11; 9 burners give 9; level 9 needs 90 mB/t of water.
    - Needs fluxuated magnetite from the LV magnets chain; start with redstone magnets until the LV polarizer and bender run.
  b:
    - ["createlowheated:basic_burner", 9]
    - ["create:fluid_tank", 45]
    - ["create:steam_engine", 9]
    - ["create:rotation_speed_controller", 1]
    - ["create_new_age:generator_coil", 3]
    - ["create_new_age:fluxuated_magnetite", 36]
    - ["create_new_age:carbon_brushes", 1]
    - ["gtceu:lv_4a_energy_converter", 4]
    - ["create:shaft", 8]
  how:
    - i: ["create:fluid_tank"]
      t: |-
        Boiler: one 3×3 Fluid Tank, 5 tall (45 blocks). Create allows one boiler level per 4 tank blocks.
    - i: ["createlowheated:basic_burner", "minecraft:flint_and_steel", "minecraft:charcoal"]
      t: |-
        9 Basic Burners under the tank, each lit once with flint and steel. Each = one heat level and burns one charcoal every 80 s (6.75 per minute for nine). Do not empower them with a fan: double heat for 32× fuel.
    - i: ["modularrouters:modular_router"]
      t: A Modular Router feeds charcoal from the charcoal drawer into every burner.
    - i: ["thermal:device_water_gen"]
      t: |-
        Water: 10 mB/t per level, 90 mB/t for level 9. Check the boiler with Engineer’s Goggles: if water is the lowest bar, add accumulators (or an LV Upgrade Kit in one).
    - i: ["create:steam_engine"]
      t: |-
        9 Steam Engines on the tank. At full efficiency each gives 64 RPM and 16 384 SU.
    - i: ["create:rotation_speed_controller"]
      t: |-
        Run the coil shaft at 256 RPM (Create’s cap) with a Rotation Speed Controller: same magnets, 88 % more FE than 136 RPM.
    - i: ["create_new_age:generator_coil", "create_new_age:fluxuated_magnetite"]
      t: Generator Coils in a line on one shaft, each ringed by 12 magnets. FE/t = RPM × total force / 20; SU = RPM × (24 + total force). Magnets between two coils count for both.
    - i: ["create_new_age:carbon_brushes"]
      t: One Carbon Brush at the end of the line collects from up to 8 coils. Pipe the FE to GT Energy Converters (4 FE = 1 EU) of the tier your machines use.
  calc:
    rpm: 256
    engines: 9
    windmills: 0
    sails: 128
    mag:
      magnetite: 0
      redstone: 0
      layered: 0
      fluxuated: 12
      netherite: 0
    wheels: 0
    coils: 3
    euNeed: 0
  s3d:
    b:
      - ["createlowheated:basic_burner", 0, 0, 0, 3, 1, 3, "Basic Burner (lit, charcoal)"]
      - ["create:fluid_tank", 0, 1, 0, 3, 5, 3, "Fluid Tank (boiler, 45 blocks)"]
      - ["create:steam_engine", 3, 1, 0, 1, 3, 3, "Steam Engine (64 RPM, 16 384 SU)"]
      - ["create:rotation_speed_controller", 5, 2, 1, 1, 1, 1, "Rotation Speed Controller → 256 RPM"]
      - ["create_new_age:generator_coil", 7, 2, 1, 3, 1, 1, Generator Coil]
      - ["create_new_age:carbon_brushes", 10, 2, 1, 1, 1, 1, Carbon Brushes]
      - ["gtceu:lv_4a_energy_converter", 12, 0, -1, 1, 1, 4, LV 4A Energy Converter]
      - ["thermal:device_water_gen", -4, 0, 1, 1, 1, 1, Aqueous Accumulator]
      - ["functionalstorage:oak_1", -4, 0, 4, 1, 1, 1, Charcoal drawer]
      - ["modularrouters:modular_router", -2, 0, 4, 1, 1, 1, "Modular Router (charcoal → burners)"]
      - ["create_new_age:fluxuated_magnetite", 7, 4, 1, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 0, 1, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 2, 3, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 2, -1, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 4, 2, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 4, 0, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 0, 2, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 0, 0, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 3, 3, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 1, 3, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 3, -1, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
      - ["create_new_age:fluxuated_magnetite", 7, 1, -1, 3, 1, 1, "Fluxuated Magnetite (force 8)"]
    p:
      - [f, [-3, 0.5, 1.5], [0, 0.5, 1.5]]
      - [i, [-3, 0.5, 4.5], [-2, 0.5, 4.5]]
      - [i, [-1, 0.5, 4.5], [1.5, 0.5, 4.5], [1.5, 0.5, 3]]
      - [r, [4, 2.5, 1.5], [7, 2.5, 1.5]]
      - [p, [11, 2.5, 1.5], [11.6, 2.5, 1.5], [11.6, 0.5, 1.5], [12, 0.5, 1.5]]
    l:
      - ["Charcoal → 9 burners (heat 9)", -1.5, 1.8, 5]
      - ["Boiler 3×3×5", 1.5, 6.6, 1.5]
      - ["9 Steam Engines · 147 456 SU", 3.6, 5.2, 1.5]
      - [Speed controller 256 RPM, 5.5, 3.8, 1.5]
      - ["3 coils × 12 fluxuated magnetite", 8.5, 5.6, 1.5]
      - [Carbon brush, 10.5, 3.8, 1.5]
      - ["FE → EU converters", 12.5, 1.9, 1]
      - ["Water 90 mB/t", -3.5, 1.8, 1.5]
---
# Create steam power: Steam Engines + Generator Coils

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `power_steam_engine` · **Tags:** Infinite source, Power, 3D scene

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Steam engines + generator coils](../../plan/p1.md#power)

**Tips:** 4

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-bb">
<div class="gt-head"><span class="gt-mname">9 Basic Burners</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Charcoal (router) (minecraft:charcoal) - 6.75 / min"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span><span class="gt-note">Charcoal (router)</span><b class="gt-q">6.75 / min</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/createlowheated__basic_burner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-bo" title="Boiler 3×3×5 tank (create:fluid_tank) - heat 9"><img class="gt-ico" src="../../assets/icons/create__fluid_tank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluid Tank</span><span class="gt-note">Boiler 3×3×5 tank</span><b class="gt-q">heat 9</b></a></div>
</div>
<div class="gt-foot"><code>createlowheated:basic_burner</code></div>
</div>
<div class="gt-panel t-mod" id="m-bo">
<div class="gt-head"><span class="gt-mname">Boiler 3×3×5 tank</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-bb" title="9 Basic Burners (createlowheated:basic_burner) - heat 9"><img class="gt-ico" src="../../assets/icons/createlowheated__basic_burner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basic Burner</span><span class="gt-note">9 Basic Burners</span><b class="gt-q">heat 9</b></a><span class="gt-slot gt-fluid" title="Water 90 mB/t (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><span class="gt-note">Water 90 mB/t</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__fluid_tank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-se" title="9 Steam Engines (create:steam_engine) - level 9"><img class="gt-ico" src="../../assets/icons/create__steam_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam Engine</span><span class="gt-note">9 Steam Engines</span><b class="gt-q">level 9</b></a></div>
</div>
<div class="gt-foot"><code>create:fluid_tank</code></div>
</div>
<div class="gt-panel t-mod" id="m-se">
<div class="gt-head"><span class="gt-mname">9 Steam Engines</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-bo" title="Boiler 3×3×5 tank (create:fluid_tank) - level 9"><img class="gt-ico" src="../../assets/icons/create__fluid_tank.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluid Tank</span><span class="gt-note">Boiler 3×3×5 tank</span><b class="gt-q">level 9</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__steam_engine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Speed controller → 256 (create:rotation_speed_controller) - 64 RPM"><img class="gt-ico" src="../../assets/icons/create__rotation_speed_controller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rotation Speed Controller</span><span class="gt-note">Speed controller → 256</span><b class="gt-q">64 RPM</b></span></div>
</div>
<div class="gt-foot"><code>create:steam_engine</code></div>
</div>
<div class="gt-panel t-mod" id="m-gc">
<div class="gt-head"><span class="gt-mname">3 Generator Coils</span><span class="gt-badge t-mod">New Age</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Speed controller → 256 (create:rotation_speed_controller)"><img class="gt-ico" src="../../assets/icons/create__rotation_speed_controller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rotation Speed Controller</span><span class="gt-note">Speed controller → 256</span></span><span class="gt-slot" title="12 Fluxuated each (create_new_age:fluxuated_magnetite) - force 96"><img class="gt-ico" src="../../assets/icons/create_new_age__fluxuated_magnetite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluxuated Magnetite</span><span class="gt-note">12 Fluxuated each</span><b class="gt-q">force 96</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-cb" title="Carbon Brushes (create_new_age:carbon_brushes) - FE"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Brushes</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>create_new_age:generator_coil</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-cb">
<div class="gt-head"><span class="gt-mname">Carbon Brushes</span><span class="gt-badge t-mod">New Age</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-gc" title="3 Generator Coils (create_new_age:generator_coil) - FE"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Generator Coil</span><span class="gt-note">3 Generator Coils</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-cv" title="Energy converters (gtceu:lv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 4a Energy Converter</span><span class="gt-note">Energy converters</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>create_new_age:carbon_brushes</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-cv">
<div class="gt-head"><span class="gt-mname">Energy converters</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-cb" title="Carbon Brushes (create_new_age:carbon_brushes) - FE"><img class="gt-ico" src="../../assets/icons/create_new_age__carbon_brushes.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Brushes</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [9 Basic Burners](#m-bb) → [Boiler 3×3×5 tank](#m-bo) → [9 Steam Engines](#m-se) → [3 Generator Coils](#m-gc) → [Carbon Brushes](#m-cb) → [Energy converters](#m-cv)

## How to build

1. Boiler: one 3×3 Fluid Tank, 5 tall (45 blocks). Create allows one boiler level per 4 tank blocks. — `create:fluid_tank`
2. 9 Basic Burners under the tank, each lit once with flint and steel. Each = one heat level and burns one charcoal every 80 s (6.75 per minute for nine). Do not empower them with a fan: double heat for 32× fuel. — `createlowheated:basic_burner`, `minecraft:flint_and_steel`, `minecraft:charcoal`
3. A Modular Router feeds charcoal from the charcoal drawer into every burner. — `modularrouters:modular_router`
4. Water: 10 mB/t per level, 90 mB/t for level 9. Check the boiler with Engineer’s Goggles: if water is the lowest bar, add accumulators (or an LV Upgrade Kit in one). — `thermal:device_water_gen`
5. 9 Steam Engines on the tank. At full efficiency each gives 64 RPM and 16 384 SU. — `create:steam_engine`
6. Run the coil shaft at 256 RPM (Create’s cap) with a Rotation Speed Controller: same magnets, 88 % more FE than 136 RPM. — `create:rotation_speed_controller`
7. Generator Coils in a line on one shaft, each ringed by 12 magnets. FE/t = RPM × total force / 20; SU = RPM × (24 + total force). Magnets between two coils count for both. — `create_new_age:generator_coil`, `create_new_age:fluxuated_magnetite`
8. One Carbon Brush at the end of the line collects from up to 8 coils. Pipe the FE to GT Energy Converters (4 FE = 1 EU) of the tier your machines use. — `create_new_age:carbon_brushes`

## Tips

- Your build: 3 coils × 12 fluxuated (force 96 each) at 136 RPM = 3 × 136 × 96 / 20 ≈ 1 958 FE/t for 48 960 SU, exactly 3 engines’ worth.
- Same coils at 256 RPM: ≈ 3 686 FE/t for 92 160 SU (6 engines). With 9 engines (147 456 SU) you can run 4 coils at 256 RPM: ≈ 4 915 FE/t.
- Boiler level = the lowest of: lit burners, tank blocks / 4, water / 10 mB/t. A 3×3×5 tank (45 blocks) allows level 11; 9 burners give 9; level 9 needs 90 mB/t of water.
- Needs fluxuated magnetite from the LV magnets chain; start with redstone magnets until the LV polarizer and bender run.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `createlowheated:basic_burner` | 9 |
| `create:fluid_tank` | 45 |
| `create:steam_engine` | 9 |
| `create:rotation_speed_controller` | 1 |
| `create_new_age:generator_coil` | 3 |
| `create_new_age:fluxuated_magnetite` | 36 |
| `create_new_age:carbon_brushes` | 1 |
| `gtceu:lv_4a_energy_converter` | 4 |
| `create:shaft` | 8 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](charcoal.md), [Magnets: from magnetite block to Fluxuated Magnetite](../lv/magnets.md)

## Extras

- 3D assembly scene with 22 blocks (open it in the Atlas page).
- Power calculator defaults are stored in the front matter (`calc`).
