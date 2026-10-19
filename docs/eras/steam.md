---
kind: era
id: steam
order: 20
data:
  id: steam
  tier: ulv
  name: Steam & Create
  sub: ULV · bronze age, hybrid route
  goal: Alloys, automated steel and rubber, first circuits, LV hull and the first energy converter.
  exit: ["gtceu:lv_machine_hull", "gtceu:basic_electronic_circuit", "gtceu:lv_1a_energy_converter"]
  route: |-
    Create does the mechanical work (press, heated mixer, crushing wheels, windmills). Steam only where it pays: the Solid Blast Furnace. Skip boilers.
  steps:
    - i: ["create:andesite_alloy", "create:windmill_bearing", "create:white_sail"]
      t: Rotation
      d: "Windmill bearing + sails: free stress forever, no fuel."
    - i: ["create:mechanical_press"]
      t: Press
      d: Plates at 1 ingot each (hand hammer costs 2).
    - i: ["create:mechanical_mixer", "create:basin", "createlowheated:basic_burner"]
      t: Heated mixer
      d: |-
        Your alloy smelter until LV: bronze, brass, red alloy, invar, soul infused, cured rubber.
    - i: ["gtceu:primitive_ore_factory", "gtceu:nickel_dust", "gtceu:gold_dust"]
      t: Primitive Ore Factory
      d: |-
        Nickel, gold and zinc come out as byproducts of crushed ores. Use the 10 ores + 2 coal blocks recipe: 15 dusts + byproducts.
    - i: ["gtceu:coke_oven", "minecraft:charcoal", "gtceu:creosote_bucket"]
      t: Charcoal
      d: Logs → charcoal + creosote. 8 sugar cane → 1 charcoal also works.
    - i: ["gtceu:solid_blast_furnace", "gtceu:steel_ingot"]
      t: Steel
      d: Wrought iron + 2 charcoal → steel in 16 s, with buses. Plain iron takes 36 s.
    - i: ["thermal:device_tree_extractor", "thermal:rubber", "thermal:cured_rubber", "gtceu:rubber_plate"]
      t: Rubber
      d: Latex from jungle trees → rubber → +sulfur in the mixer → press into rubber plates.
    - i: ["thermal_extra:soul_sand_dust", "gtceu:invar_ingot", "gtceu:soul_infused_ingot"]
      t: LV superconductor
      d: Invar + 2 soul sand dust → 3 soul infused.
    - i: ["gtceu:resistor", "gtceu:vacuum_tube", "gtceu:resin_printed_circuit_board", "gtceu:basic_electronic_circuit"]
      t: First circuit
      d: Make 8–16 at once; every LV machine needs one.
    - i: ["gtceu:lv_machine_hull", "gtceu:lv_1a_energy_converter"]
      t: Into LV
      d: Converter turns FE into EU (4 FE = 1 EU). FE→EU is the only direction allowed.
  build:
    - id: create:windmill_bearing
      "n": "2"
    - id: create:mechanical_press
      "n": "1–2"
    - id: create:mechanical_mixer
      "n": "2"
    - id: create:crushing_wheel
      "n": "2"
    - id: gtceu:coke_oven
      "n": "2"
    - id: gtceu:solid_blast_furnace
      "n": "1"
    - id: gtceu:primitive_ore_factory
      "n": "1"
    - id: gtceu:large_barrel
      "n": "1"
    - id: gtceu:large_stone_barrel
      "n": "1–2"
  setups:
    - create_power
    - power_steam_engine
    - tree_farm
    - charcoal_fan
    - charcoal
    - inf_gravel_create
    - gravel_steam
    - crop_farm
    - alloys
    - alloys_smelter
    - steel_pbf
    - steel
    - rubber
  multis:
    - gtceu:coke_oven
    - gtceu:primitive_blast_furnace
    - gtceu:solid_blast_furnace
    - gtceu:primitive_ore_factory
    - gtceu:large_barrel
    - gtceu:large_stone_barrel
    - gtceu:large_farm
    - gtceu:steam_grinder
    - gtceu:steam_oven
    - gtceu:steam_ore_factory
    - gtceu:high_pressure_steam_hammer
    - gtceu:steam_kiln
  storage:
    - i: ["functionalstorage:oak_1"]
      k: Parts
      v: Drawers for plates, rods, screws.
    - i: ["toms_storage:ts.storage_terminal", "toms_storage:ts.inventory_connector"]
      k: Access
      v: Tom’s Storage terminal over all chests and drawers — your network until AE2.
    - i: ["pipez:item_pipe", "pipez:fluid_pipe"]
      k: Moving
      v: Pipez between coke ovens, SBF and drawers. Keep pipe networks short.
    - i: ["thermal:fluid_cell"]
      k: Fluids
      v: Fluid Cells for creosote and water; upgrade with kits.
---
# Steam &amp; Create — ULV · bronze age, hybrid route

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `steam` · **Tier:** `ulv`

**Goal:** Alloys, automated steel and rubber, first circuits, LV hull and the first energy converter.

**Exit items:** `gtceu:lv_machine_hull`, `gtceu:basic_electronic_circuit`, `gtceu:lv_1a_energy_converter`

> Create does the mechanical work (press, heated mixer, crushing wheels, windmills). Steam only where it pays: the Solid Blast Furnace. Skip boilers.

## Steps

1. **Rotation** — Windmill bearing + sails: free stress forever, no fuel. (`create:andesite_alloy`, `create:windmill_bearing`, `create:white_sail`)
2. **Press** — Plates at 1 ingot each (hand hammer costs 2). (`create:mechanical_press`)
3. **Heated mixer** — Your alloy smelter until LV: bronze, brass, red alloy, invar, soul infused, cured rubber. (`create:mechanical_mixer`, `create:basin`, `createlowheated:basic_burner`)
4. **Primitive Ore Factory** — Nickel, gold and zinc come out as byproducts of crushed ores. Use the 10 ores + 2 coal blocks recipe: 15 dusts + byproducts. (`gtceu:primitive_ore_factory`, `gtceu:nickel_dust`, `gtceu:gold_dust`)
5. **Charcoal** — Logs → charcoal + creosote. 8 sugar cane → 1 charcoal also works. (`gtceu:coke_oven`, `minecraft:charcoal`, `gtceu:creosote_bucket`)
6. **Steel** — Wrought iron + 2 charcoal → steel in 16 s, with buses. Plain iron takes 36 s. (`gtceu:solid_blast_furnace`, `gtceu:steel_ingot`)
7. **Rubber** — Latex from jungle trees → rubber → +sulfur in the mixer → press into rubber plates. (`thermal:device_tree_extractor`, `thermal:rubber`, `thermal:cured_rubber`, `gtceu:rubber_plate`)
8. **LV superconductor** — Invar + 2 soul sand dust → 3 soul infused. (`thermal_extra:soul_sand_dust`, `gtceu:invar_ingot`, `gtceu:soul_infused_ingot`)
9. **First circuit** — Make 8–16 at once; every LV machine needs one. (`gtceu:resistor`, `gtceu:vacuum_tube`, `gtceu:resin_printed_circuit_board`, `gtceu:basic_electronic_circuit`)
10. **Into LV** — Converter turns FE into EU (4 FE = 1 EU). FE→EU is the only direction allowed. (`gtceu:lv_machine_hull`, `gtceu:lv_1a_energy_converter`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `create:windmill_bearing` | 2 |
| `create:mechanical_press` | 1–2 |
| `create:mechanical_mixer` | 2 |
| `create:crushing_wheel` | 2 |
| `gtceu:coke_oven` | 2 |
| `gtceu:solid_blast_furnace` | 1 |
| `gtceu:primitive_ore_factory` | 1 |
| `gtceu:large_barrel` | 1 |
| `gtceu:large_stone_barrel` | 1–2 |

## Setups

- [Free rotation (Create)](../chains/steam/create_power.md)
- [Create steam power: Steam Engines + Generator Coils](../chains/steam/power_steam_engine.md)
- [Create tree farm (rotating saws + deployers)](../chains/steam/tree_farm.md)
- [Charcoal: Create fan smelting](../chains/steam/charcoal_fan.md)
- [Charcoal &amp; creosote: Coke Oven](../chains/steam/charcoal.md)
- [Infinite gravel (Create)](../chains/steam/inf_gravel_create.md)
- [Gravel, sand &amp; dust: Steam Forge Hammer](../chains/steam/gravel_steam.md)
- [Crops: Large Farm (no power)](../chains/steam/crop_farm.md)
- [Alloys: Create heated mixer](../chains/steam/alloys.md)
- [Alloys: Steam / LV Alloy Smelter (more per ingot)](../chains/steam/alloys_smelter.md)
- [Steel: Primitive Blast Furnace](../chains/steam/steel_pbf.md)
- [Steel: Solid Blast Furnace](../chains/steam/steel.md)
- [Rubber: Large Arboreal Extractor](../chains/steam/rubber.md)

## Storage

- **Parts:** Drawers for plates, rods, screws. (`functionalstorage:oak_1`)
- **Access:** Tom’s Storage terminal over all chests and drawers — your network until AE2. (`toms_storage:ts.storage_terminal`, `toms_storage:ts.inventory_connector`)
- **Moving:** Pipez between coke ovens, SBF and drawers. Keep pipe networks short. (`pipez:item_pipe`, `pipez:fluid_pipe`)
- **Fluids:** Fluid Cells for creosote and water; upgrade with kits. (`thermal:fluid_cell`)

## Multiblocks

`gtceu:coke_oven`, `gtceu:primitive_blast_furnace`, `gtceu:solid_blast_furnace`, `gtceu:primitive_ore_factory`, `gtceu:large_barrel`, `gtceu:large_stone_barrel`, `gtceu:large_farm`, `gtceu:steam_grinder`, `gtceu:steam_oven`, `gtceu:steam_ore_factory`, `gtceu:high_pressure_steam_hammer`, `gtceu:steam_kiln`

## Plan phases

- [Foundation](../plan/p1.md)
