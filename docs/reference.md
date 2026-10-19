---
kind: view
view: reference
---
# Tiers, mechanics and legend

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

Data: `docs/_data/tiers.yml`, `mechanics.yml`, `legend.yml`, `once.yml`, `meta.yml`.

## Tiers

| Tier | EU/t | Superconductor | Hull | Material |
| --- | ---: | --- | --- | --- |
| ULV | 8 |  | `gtceu:ulv_machine_hull` | `gtceu:wrought_iron_ingot` |
| LV | 32 | `gtceu:soul_infused_single_wire` | `gtceu:lv_machine_hull` | `gtceu:steel_ingot` |
| MV | 128 | `gtceu:signalum_single_wire` | `gtceu:mv_machine_hull` | `gtceu:aluminium_ingot` |
| HV | 512 | `gtceu:lumium_single_wire` | `gtceu:hv_machine_hull` | `gtceu:stainless_steel_ingot` |
| EV | 2048 | `gtceu:enderium_single_wire` | `gtceu:ev_machine_hull` | `gtceu:titanium_ingot` |
| IV | 8192 | `gtceu:shellite_single_wire` | `gtceu:iv_machine_hull` | `gtceu:tungsten_steel_ingot` |
| LuV | 32768 | `gtceu:twinite_single_wire` | `gtceu:luv_machine_hull` | `gtceu:rhodium_plated_palladium_ingot` |
| ZPM | 131072 | `gtceu:dragonsteel_single_wire` | `gtceu:zpm_machine_hull` | `gtceu:naquadah_alloy_ingot` |
| UV | 524288 | `gtceu:prismalium_single_wire` | `gtceu:uv_machine_hull` | `gtceu:darmstadtium_ingot` |
| UHV | 2097152 | `gtceu:stellarium_single_wire` | `gtceu:uhv_machine_hull` | `gtceu:neutronium_ingot` |
| UEV | 8388608 | `gtceu:ancient_runicalium_single_wire` | `gtceu:uev_machine_hull` | `gtceu:mythrolic_alloy_ingot` |
| UIV | 33554432 | `gtceu:rhenium_super_composite_alloy_single_wire` | `gtceu:uiv_machine_hull` | `gtceu:chaotixic_alloy_ingot` |

## Mechanics

- **Preview &amp; auto-build** (`gtceu:terminal`): Press U on any controller in EMI for the 3D preview. Shift-right-click a controller with the GT Terminal to place the whole structure from your inventory.
- **Hatches replace casings** (`gtceu:lv_input_bus`): Rows marked "accepts" include the slots for buses/hatches. Keep the minimum casing count or it will not form.
- **Wall-sharing** (`gtceu:heatproof_machine_casing`): Two multis can share casings, coils and even hatches. Double output for half the build.
- **Overclock** (`gtceu:lv_energy_input_hatch`): +1 tier = 4× EU/t, 2× speed (perfect OC: 4×). Two energy hatches let a multi reach the next tier — except assemblers.
- **Ghost circuits** (`gtceu:programmed_circuit`): Bottom-left slot of every machine. Match the number the recipe asks for.
- **Distinct buses** (`gtceu:lv_input_bus`): Each input bus is processed alone — molds and lenses never mix.
- **LCR circuit 24** (`gtceu:large_chemical_reactor`): Single-step versions of whole chemical lines (acids, epoxy…).
- **Parallels** (`gtceu:iv_parallel_hatch`): N recipes at once. Bound by the tier amperage — two 4A hatches do nothing extra.
- **Boosted multis** (`gtceu:super_ebf`): Throughput boosting: 4 recipes, +60 % time, −5 % EU/t (≈2.5×). Bulking: 16 recipes, 13× time.
- **Superconductors** (`gtceu:soul_infused_single_wire`): Lossless cable per tier. Always use them for power lines.

## Node legend

- `s`: Infinite source
- `i`: Input
- `m`: Machine
- `x`: Intermediate
- `f`: Fluid
- `o`: Output
- `p`: Power

## Build once

`kubejs:lv_upgrade_kit`, `create_new_age:redstone_magnet`, `gtceu:mv_mixer`, `minecraft:nether_star`, `minecraft:soul_campfire`
