---
kind: view
view: farms
---
# Farm options

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

Data: `docs/_data/options.yml`.

## Charcoal (`minecraft:charcoal`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Charcoal: Create fan smelting](chains/steam/charcoal_fan.md) | Steam | Rotation + lava block | A belt stack at a time | No fuel, no power, 1 log → 1 charcoal | No creosote | Steam &amp; LV |
| [Charcoal: Pyrolyse Oven](chains/feeders/charcoal_pyro.md) | MV | 64 EU/t | 20 charcoal + 4 B creosote per 16 logs / 32 s | +25 % charcoal, lots of creosote; other circuits: wood gas, tar, vinegar | Needs MV | MV onwards |
| [Charcoal &amp; creosote: Coke Oven](chains/steam/charcoal.md) | Stone | None | 1.3 charcoal / min per oven | The only early creosote | Slow; build it for creosote, not charcoal |  |
| [Charcoal: Charcoal Pile Igniter](chains/feeders/charcoal_pile.md) | Stone | None | Huge batches | Very early bulk charcoal | Mined by hand |  |

## Logs (`minecraft:oak_log`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Create tree farm (rotating saws + deployers)](chains/steam/tree_farm.md) | Steam | Rotation | Depends on arm size | No GT power; saplings and apples too | Large build, slow to plant | Steam age |
| [Logs: Greenhouse](chains/feeders/greenhouse_logs.md) | LV | 30 EU/t | 32 logs / min (128 with CO₂, 256 with NPK) | Compact, day and night, any tree; CO₂ mode also gives oxygen | MV circuit to build; CO₂ mode needs an MV distillery | LV onwards |

## Cobblestone (`minecraft:cobblestone`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Infinite cobble &amp; blackstone](chains/stone/inf_cobble.md) | Stone | None | 80 per minute per barrel | Cheapest, also blackstone/obsidian | Needs a water input | Always |
| [Cobble: Create drill generator](chains/feeders/cobble_drill.md) | Steam | Rotation | Scales with RPM | Pure Create | Lava + water sources in world |  |
| [Cobble: Rock Breaker (LV)](chains/feeders/cobble_rb.md) | LV | LV | Fast, scales with tier | Compact, no inputs | Uses EU |  |

## Gravel, sand &amp; dust (`minecraft:gravel`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Gravel, sand &amp; dust: Steam Forge Hammer](chains/steam/gravel_steam.md) | Steam | Steam 32 mB/t | 0.5 s per block | One block, no SU; also sand and dust | Boilers need charcoal + water | Steam age |
| [Gravel, sand &amp; dust: Forge Hammers](chains/feeders/gravel_hammer.md) | LV | 16 EU/t each | 0.5 s per block per hammer | All three blocks in a row | Uses EU | LV onwards |
| [Infinite gravel (Create)](chains/steam/inf_gravel_create.md) | Steam | Rotation | A stack at a time | Only if you already have spare SU | 2 wheels + big SU load for gravel only |  |

## Crushed ores (`gtceu:crushed_iron_ore`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Sieve station (manual)](chains/stone/sieve_manual.md) | Stone | You | Click by click | Day one | Manual |  |
| [Four-sieve block (gravel, sand, dust, blackstone)](chains/lv/sieve_block4.md) | LV | ≈ 210 EU/t (own diamonds) | 4 sieves · 64 each / 40 s | Ores, gems, redstone/sulfur and lead/antimony in one block; powers itself | Needs a Lapidary Dynamo + LV kit (or the steam option meanwhile) | LV onwards |
| [Ore sieve, Create-powered (windmill + crushing wheels)](chains/feeders/sieve_auto.md) | LV | 128-sail windmill | 16 of each ore / 40 s | No fuel, no diamonds | Huge windmill for one sieve (31.5 EU/t) |  |
| [Void Extractor](chains/lv/void.md) | LV | LV | 32 s per cycle | Ores the sieves never give + rare fluids | Needs drilling fluid |  |

## Crops (`minecraft:wheat`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Crops: Large Farm (no power)](chains/steam/crop_farm.md) | Steam | None | 16 / 40 s, daytime only | No power, treated wood only | Stops at night |  |
| [Crops: Greenhouse (LV, day and night)](chains/lv/crop_greenhouse.md) | LV | 16 EU/t | 64 / 30 s with fertilizer | 5× a Large Farm, day and night | Greenhouse needs an MV circuit; fertilizer 1.5 / min | LV onwards |

## Alloys (`gtceu:bronze_ingot`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Alloys: Steam / LV Alloy Smelter (more per ingot)](chains/steam/alloys_smelter.md) | Steam | Steam 32 mB/t | 4 bronze / 10 s | +33 % bronze &amp; brass, +50 % invar, 2× tin alloy | Needs a boiler | Steam onwards |
| [Alloys: Create heated mixer](chains/steam/alloys.md) | Steam | Rotation + Basic Burner | 3 bronze per mix | Also makes soul infused | Loses a quarter of the metal |  |

## Steel (`gtceu:steel_ingot`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Steel: Primitive Blast Furnace](chains/steam/steel_pbf.md) | Steam | None | 1 / 90 s | Firebricks only | Very slow; only for the first steel |  |
| [Steel: Solid Blast Furnace](chains/steam/steel.md) | Steam | None | 1 / 16 s (12 s with coke) | No power; blocks mode for bulk | 2 charcoal per steel | Steam → HV |
| [Steel: Electric Blast Furnace + oxygen](chains/mv/steel_ebf.md) | MV | 120 EU/t + 200 mB O₂ | 1 / 15 s (7.5 s at HV) | No charcoal | Only worth it once oxygen is free |  |

## Lava (`minecraft:lava_bucket`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Infinite lava, obsidian &amp; pebbles](chains/stone/inf_lava.md) | Steam | None | 500 mB / 10 s per cobble | Automatic with buses | Multiblock to build | Always |

## Rubber (`thermal:rubber`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Rubber: Large Arboreal Extractor](chains/steam/rubber.md) | Steam | None | 1.2 rubber / min (3 with fertilizer) per extractor | No power, cheap bricks, scales by copying | Solidifier + chemical reactor need LV | Always (until chemical rubbers) |

## Rotation (Create SU) (`create:steam_engine`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Create steam power: Steam Engines + Generator Coils](chains/steam/power_steam_engine.md) | Steam | Any furnace fuel | 16 384 SU per burner + engine | Small, strong, cheap fuel | Needs fuel and water | Always |
| [Free rotation (Create)](chains/steam/create_power.md) | Stone | Wind | 512 SU per windmill RPM (8 192 max) | No fuel at all | 128 sails for half of one steam engine |  |

## Power (EU) (`thermal:dynamo_stirling`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Diamond power (Lapidary Dynamos)](chains/lv/power_lapidary.md) | LV | Diamonds from your own sand sieve | 300 EU/t per dynamo, 5 per sieve | Self-fed, tiny, scales to ~1 500 EU/t per sand sieve | Lapidary Dynamo needs cobalt brass; LV kit per dynamo | LV onwards |
| [Create steam power: Steam Engines + Generator Coils](chains/steam/power_steam_engine.md) | Steam | ≈ 2.25 charcoal/min | ≈ 307 EU/t (3 engines, 4 coils) | Big power before LV kits; the SU also runs Create machines | Needs a charcoal farm and a water pump | Steam / early LV |
| [Fuel-free LV power (Create New Age)](chains/power/power_newage.md) | Steam | Windmill | RPM × magnets / 20 FE/t | No fuel at all | 128 sails → only ~31 EU/t |  |
| [LV power grid](chains/power/power_lv.md) | LV | Charcoal / diamonds | ×6 with LV kits | Stirling works on any furnace fuel | Stirling burns fuel fast; prefer Lapidary |  |
| [LV power: boilers + steam turbines](chains/power/power_steam.md) | LV | Charcoal | Per turbine | EU directly, no converter | Water + fuel logistics |  |

## Components (LV) (`gtceu:lv_electric_motor`)

| Chain | Tier | Power | Rate | Pro | Con | Best |
| --- | --- | --- | --- | --- | --- | --- |
| [Component wall: always a stock of every part (no AE2)](chains/lv/comp_stock.md) | LV | under ~350 EU/t | 12 per minute per line | Parts always in stock, no AE2 needed | Many machines and covers | LV onwards |
| [LV Electric Motor line](chains/lv/comp_motor.md) | LV | 30 EU/t | 1 motor / 5 s | Feeds every other component | — |  |
| [LV circuit line (Basic Electronic Circuit)](chains/lv/comp_circuit_lv.md) | LV | 16 EU/t | 2 circuits / 10 s | Twice what hand crafting gives | Needs a glue (resin) source |  |
