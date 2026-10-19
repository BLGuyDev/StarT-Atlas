---
kind: chain
id: sieve_auto
order: 470
data:
  t: Ore sieve, Create-powered (windmill + crushing wheels)
  inf: true
  hero: false
  "n":
    - [acc, Aqueous Accumulator, s, "thermal:device_water_gen"]
    - [sb, Stone Barrel, m, "gtceu:stone_barrel"]
    - [c, Cobblestone, x, "minecraft:cobblestone"]
    - [wm, Windmill, p, "create:windmill_bearing"]
    - [cw, Crushing Wheels, m, "create:crushing_wheel"]
    - [g, Gravel, x, "minecraft:gravel"]
    - [gc, Magnet generator, p, "create_new_age:generator_coil"]
    - [cv, LV Converter, m, "gtceu:lv_1a_energy_converter"]
    - [ms, Mechanical Sieve, m, "gtceu:mechanical_sieve"]
    - [o1, Crushed Copper, o, "gtceu:crushed_copper_ore"]
    - [o2, Crushed Iron, o, "gtceu:crushed_iron_ore"]
    - [o3, Crushed Tin, o, "gtceu:crushed_tin_ore"]
    - [o4, Crushed Sphalerite, o, "gtceu:crushed_sphalerite_ore"]
    - [o5, Crushed Magnetite, o, "gtceu:crushed_magnetite_ore"]
  e:
    - [acc, sb, water]
    - [sb, c, "0.75 s"]
    - [c, cw, smart chute]
    - [wm, cw, SU]
    - [cw, g]
    - [g, ms, "64"]
    - [gc, cv, FE]
    - [cv, ms, LV]
    - [ms, o1, "×16"]
    - [ms, o2, "×16"]
    - [ms, o3, "×16"]
    - [ms, o4, "×16"]
    - [ms, o5, "×16"]
  tips:
    - |-
      64 gravel → 16 of each ore every 40 s. The string mesh inside is never consumed.
    - Same build with sand (gems), dust (redstone, sulfur…) or crushed blackstone (lead, silver, antimony).
    - "IV Large Sieve: 48 in, same outputs, 10 s."
    - Works, but 128 sails of windmill only give 31.5 EU/t. The four-sieve block does this and three more sieves with one compact power source.
  store: ["functionalstorage:oak_1", "gtceu:lv_super_chest"]
  b:
    - ["thermal:device_water_gen", 1]
    - ["gtceu:stone_barrel", 1]
    - ["create:crushing_wheel", 2]
    - ["create:smart_chute", 1]
    - ["create:windmill_bearing", 1]
    - ["create:white_sail", 16]
    - ["create_new_age:generator_coil", 2]
    - ["create_new_age:redstone_magnet", 4]
    - ["create_new_age:carbon_brushes", 1]
    - ["gtceu:lv_1a_energy_converter", 1]
    - ["gtceu:mechanical_sieve", 1]
    - ["exnihilosequentia:string_mesh", 1]
    - ["gtceu:lv_conveyor_module", 2]
    - ["functionalstorage:oak_1", 5]
  how:
    - i: ["thermal:device_water_gen"]
      t: Aqueous Accumulator between two water source blocks. Turn on auto-output on two faces, one into each Stone Barrel.
    - i: ["gtceu:stone_barrel", "minecraft:lava_bucket"]
      t: Two Stone Barrels, each with one lava bucket inside (never used up) and ghost circuit 0. Each makes 1 cobblestone every 0.75 s, so the pair gives 160 cobble per minute.
    - i: ["functionalstorage:oak_1"]
      t: Both barrels auto-output straight into one drawer, which acts as the cobble buffer.
    - i: ["create:brass_funnel"]
      t: A Brass Funnel (filtered to cobblestone) pulls from the drawer and drops cobble between the crushing wheels.
    - i: ["create:crushing_wheel"]
      t: |-
        Two Crushing Wheels spinning toward each other at 140 RPM. Stress: 2 × 8 SU/RPM × 140 = 2 240 SU. Gravel falls underneath.
    - i: ["create_new_age:generator_coil", "create_new_age:magnetite_block", "create_new_age:redstone_magnet"]
      t: |-
        Generator Coil on the same shaft at 140 RPM, ringed by 6 Magnetite Blocks (force 1) and 6 Redstone Magnets (force 2). Total force 18, so 140 × 18 / 20 = 126 FE/t. Stress: 140 × (18 + 24) = 5 880 SU.
    - i: ["create_new_age:carbon_brushes", "gtceu:lv_1a_energy_converter"]
      t: Carbon Brushes touching the coil collect the FE, and an LV 1A Energy Converter turns it into EU at 4 FE per 1 EU. 126 FE/t is about 31.5 EU/t, just over the Mechanical Sieve’s 30 EU/t, so it never starves.
    - i: ["create:windmill_bearing", "create:white_sail"]
      t: One Windmill Bearing with 128 sails turns at 16 RPM and gives 512 × 16 = 8 192 SU. Gear it up with large→small cogwheels. The load is 16 + 42 = 58 SU per RPM, so the maximum speed is 8 192 / 58 ≈ 141 RPM.
    - i: ["gtceu:mechanical_sieve", "exnihilosequentia:string_mesh"]
      t: Gravel goes into the Mechanical Sieve’s input bus, with a string mesh that is never consumed. Every 40 s, 64 gravel becomes 16 Copper, 16 Iron, 16 Tin, 16 Sphalerite and 16 Magnetite, which leave through the output bus into drawers.
    - i: ["create:rotation_speed_controller", "create:windmill_bearing"]
      t: Going to 256 RPM (Create’s limit) needs 58 × 256 = 14 848 SU. Add a second 128-sail windmill (16 384 SU total) and set a Rotation Speed Controller to 256. The coil then makes 230 FE/t ≈ 57 EU/t, and the wheels crush 1.8× faster.
  calc:
    rpm: 140
    windmills: 1
    sails: 128
    mag:
      magnetite: 6
      redstone: 6
      layered: 0
      fluxuated: 0
      netherite: 0
    wheels: 2
    coils: 1
    euNeed: 30
---
# Ore sieve, Create-powered (windmill + crushing wheels)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_auto` · **Tags:** Infinite source

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-sb">
<div class="gt-head"><span class="gt-mname">Stone Barrel</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Aqueous Accumulator (thermal:device_water_gen) - water"><img class="gt-ico" src="../../assets/icons/thermal__device_water_gen.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Device Water Gen</span><span class="gt-note">Aqueous Accumulator</span><span class="gt-tag">infinite</span><b class="gt-q">water</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">0.75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Cobblestone (minecraft:cobblestone) - 0.75 s"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cw" title="Crushing Wheels (create:crushing_wheel) - SU"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushing Wheel</span><span class="gt-note">Crushing Wheels</span><b class="gt-q">SU</b></a></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
<div class="gt-panel t-mod" id="m-cw">
<div class="gt-head"><span class="gt-mname">Crushing Wheels</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cobblestone (minecraft:cobblestone) - smart chute"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><b class="gt-q">smart chute</b></span><a class="gt-slot gt-power" href="#m-wm" title="Windmill (create:windmill_bearing) - SU"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Windmill Bearing</span><b class="gt-q">SU</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
</div>
<div class="gt-foot"><code>create:crushing_wheel</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-gc">
<div class="gt-head"><span class="gt-mname">Magnet generator</span><span class="gt-badge t-mod">New Age</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cv" title="LV Converter (gtceu:lv_1a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__lv_1a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 1a Energy Converter</span><span class="gt-note">LV Converter</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>create_new_age:generator_coil</code></div>
</div>
<div class="gt-panel t-lv" id="m-cv">
<div class="gt-head"><span class="gt-mname">LV Converter</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-gc" title="Magnet generator (create_new_age:generator_coil) - FE"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Generator Coil</span><span class="gt-note">Magnet generator</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_1a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-ms" title="Mechanical Sieve (gtceu:mechanical_sieve) - LV"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><b class="gt-q">LV</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_1a_energy_converter</code></div>
</div>
<div class="gt-panel t-mod" id="m-ms">
<div class="gt-head"><span class="gt-mname">Mechanical Sieve</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gravel (minecraft:gravel) - 64"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span><b class="gt-q">64</b></span><a class="gt-slot gt-mach" href="#m-cv" title="LV Converter (gtceu:lv_1a_energy_converter) - LV"><img class="gt-ico" src="../../assets/icons/gtceu__lv_1a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 1a Energy Converter</span><span class="gt-note">LV Converter</span><b class="gt-q">LV</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Copper (gtceu:crushed_copper_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_copper_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Copper Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Iron (gtceu:crushed_iron_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_iron_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Iron Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Tin (gtceu:crushed_tin_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_tin_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Tin Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Sphalerite (gtceu:crushed_sphalerite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_sphalerite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Sphalerite Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Magnetite (gtceu:crushed_magnetite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_magnetite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Magnetite Ore</span><b class="gt-q">×16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
</div>

## Flow

- [Stone Barrel](#m-sb) → [Crushing Wheels](#m-cw) → [Mechanical Sieve](#m-ms)
- [Windmill](#m-wm) → [Crushing Wheels](#m-cw)
- [Magnet generator](#m-gc) → [LV Converter](#m-cv) → [Mechanical Sieve](#m-ms)

## How to build

1. Aqueous Accumulator between two water source blocks. Turn on auto-output on two faces, one into each Stone Barrel. — `thermal:device_water_gen`
2. Two Stone Barrels, each with one lava bucket inside (never used up) and ghost circuit 0. Each makes 1 cobblestone every 0.75 s, so the pair gives 160 cobble per minute. — `gtceu:stone_barrel`, `minecraft:lava_bucket`
3. Both barrels auto-output straight into one drawer, which acts as the cobble buffer. — `functionalstorage:oak_1`
4. A Brass Funnel (filtered to cobblestone) pulls from the drawer and drops cobble between the crushing wheels. — `create:brass_funnel`
5. Two Crushing Wheels spinning toward each other at 140 RPM. Stress: 2 × 8 SU/RPM × 140 = 2 240 SU. Gravel falls underneath. — `create:crushing_wheel`
6. Generator Coil on the same shaft at 140 RPM, ringed by 6 Magnetite Blocks (force 1) and 6 Redstone Magnets (force 2). Total force 18, so 140 × 18 / 20 = 126 FE/t. Stress: 140 × (18 + 24) = 5 880 SU. — `create_new_age:generator_coil`, `create_new_age:magnetite_block`, `create_new_age:redstone_magnet`
7. Carbon Brushes touching the coil collect the FE, and an LV 1A Energy Converter turns it into EU at 4 FE per 1 EU. 126 FE/t is about 31.5 EU/t, just over the Mechanical Sieve’s 30 EU/t, so it never starves. — `create_new_age:carbon_brushes`, `gtceu:lv_1a_energy_converter`
8. One Windmill Bearing with 128 sails turns at 16 RPM and gives 512 × 16 = 8 192 SU. Gear it up with large→small cogwheels. The load is 16 + 42 = 58 SU per RPM, so the maximum speed is 8 192 / 58 ≈ 141 RPM. — `create:windmill_bearing`, `create:white_sail`
9. Gravel goes into the Mechanical Sieve’s input bus, with a string mesh that is never consumed. Every 40 s, 64 gravel becomes 16 Copper, 16 Iron, 16 Tin, 16 Sphalerite and 16 Magnetite, which leave through the output bus into drawers. — `gtceu:mechanical_sieve`, `exnihilosequentia:string_mesh`
10. Going to 256 RPM (Create’s limit) needs 58 × 256 = 14 848 SU. Add a second 128-sail windmill (16 384 SU total) and set a Rotation Speed Controller to 256. The coil then makes 230 FE/t ≈ 57 EU/t, and the wheels crush 1.8× faster. — `create:rotation_speed_controller`, `create:windmill_bearing`

## Tips

- 64 gravel → 16 of each ore every 40 s. The string mesh inside is never consumed.
- Same build with sand (gems), dust (redstone, sulfur…) or crushed blackstone (lead, silver, antimony).
- IV Large Sieve: 48 in, same outputs, 10 s.
- Works, but 128 sails of windmill only give 31.5 EU/t. The four-sieve block does this and three more sieves with one compact power source.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:device_water_gen` | 1 |
| `gtceu:stone_barrel` | 1 |
| `create:crushing_wheel` | 2 |
| `create:smart_chute` | 1 |
| `create:windmill_bearing` | 1 |
| `create:white_sail` | 16 |
| `create_new_age:generator_coil` | 2 |
| `create_new_age:redstone_magnet` | 4 |
| `create_new_age:carbon_brushes` | 1 |
| `gtceu:lv_1a_energy_converter` | 1 |
| `gtceu:mechanical_sieve` | 1 |
| `exnihilosequentia:string_mesh` | 1 |
| `gtceu:lv_conveyor_module` | 2 |
| `functionalstorage:oak_1` | 5 |

## Storage

`functionalstorage:oak_1`, `gtceu:lv_super_chest`

## Extras

- Power calculator defaults are stored in the front matter (`calc`).
