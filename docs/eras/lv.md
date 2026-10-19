---
kind: era
id: lv
order: 30
data:
  id: lv
  tier: lv
  name: LV
  sub: "32 EU/t · Industrial Revolution I"
  goal: Full LV machine set, steady power, the EBF and the first resource multis.
  exit: ["gtceu:aluminium_ingot", "gtceu:mv_machine_hull"]
  steps:
    - i: ["thermal:dynamo_stirling", "create_new_age:generator_coil", "gtceu:lv_4a_energy_converter"]
      t: Power first
      d: Dynamos or a magnet generator → converter → soul infused wire. See the power setup below.
    - i:
        - gtceu:lv_electric_motor
        - gtceu:lv_electric_piston
        - gtceu:lv_conveyor_module
        - gtceu:lv_robot_arm
        - gtceu:lv_electric_pump
      t: Components
      d: Motor first; everything is built from these five.
    - i: ["gtceu:lv_bender", "gtceu:lv_wiremill", "gtceu:lv_lathe", "gtceu:lv_alloy_smelter", "gtceu:lv_assembler"]
      t: Machine order
      d: Bender → Wiremill → Lathe → Alloy Smelter → Assembler (unlocks hatches, kits, cheaper everything).
    - i: ["gtceu:lv_macerator", "gtceu:lv_mixer", "gtceu:lv_extractor", "gtceu:lv_fluid_solidifier", "gtceu:lv_cutter"]
      t: Then
      d: Macerator, Mixer, Extractor, Solidifier, Cutter (steel buzzsaw), Chemical Reactor, Electrolyzer, Centrifuge.
    - i: ["gtceu:cupronickel_coil_block", "gtceu:electric_blast_furnace"]
      t: EBF
      d: |-
        16 cupronickel coils. Two LV energy hatches reach MV recipes: aluminium and signalum before MV machines.
    - i: ["gtceu:mechanical_sieve", "gtceu:void_extractor", "gtceu:rock_filtrator"]
      t: Resource multis
      d: |-
        Mechanical Sieve: 64 in → 16 of each drop every 40 s. Void Extractor: ores the sieve never gives. Rock Filtrator: gems. One energy hatch each.
    - i: ["gtceu:lv_distillery", "gtceu:lubricant_bucket", "gtceu:drilling_fluid_bucket"]
      t: Drilling fluid
      d: Creosote → lubricant → drilling fluid.
    - i: ["gtceu:electric_ore_factory"]
      t: Ore processing
      d: Crushed ore + water → dust + byproducts, twice the primitive speed, no fuel.
    - i: ["gtceu:graphite_dust", "gtceu:lv_arc_furnace", "gtceu:annealed_copper_ingot"]
      t: Arc furnace
      d: Needs graphite. Recycles machines; annealed copper.
    - i: ["gtceu:gallium_arsenide_dust", "gtceu:silicon_boule"]
      t: Towards MV
      d: Realgar + sphalerite → gallium arsenide → silicon boule in the EBF.
  build:
    - id: thermal:dynamo_stirling
      "n": "4–6"
    - id: thermal:dynamo_lapidary
      "n": "2–4"
    - id: gtceu:lv_4a_energy_converter
      "n": "1–2"
    - id: gtceu:lv_assembler
      "n": "2"
    - id: gtceu:lv_bender
      "n": "1"
    - id: gtceu:lv_wiremill
      "n": "1"
    - id: gtceu:lv_alloy_smelter
      "n": "1"
    - id: gtceu:lv_macerator
      "n": "1"
    - id: gtceu:electric_blast_furnace
      "n": "1"
    - id: gtceu:mechanical_sieve
      "n": "1–2"
    - id: gtceu:void_extractor
      "n": "1"
    - id: gtceu:rock_filtrator
      "n": "1"
    - id: gtceu:electric_ore_factory
      "n": "1"
  power: power_lapidary
  setups:
    - sieve_block4
    - power_lapidary
    - coils
    - drilling
    - void
    - geodes
    - ores
    - distilled
    - crop_greenhouse
    - comp_stock
    - comp_parts
    - comp_wires
    - comp_motor
    - comp_piston
    - comp_conveyor
    - comp_pump
    - comp_robot_arm
    - comp_circuit_lv
    - magnets
    - treated_wood
    - fertilizer
    - ingots
    - glue
    - lv_hull_line
    - soul_infused
  multis:
    - gtceu:electric_blast_furnace
    - gtceu:mechanical_sieve
    - gtceu:void_extractor
    - gtceu:rock_filtrator
    - gtceu:electric_ore_factory
  storage:
    - i: ["gtceu:lv_super_chest"]
      k: Raw ores
      v: One Super Chest per main ore (thousands of items).
    - i: ["gtceu:lv_super_tank", "gtceu:steel_drum"]
      k: Fluids
      v: Steel drums now; Super Tank once you have polyethylene (4 LV circuits + 3 steel plates + hermetic casing + LV pump).
    - i: ["gtceu:lv_conveyor_module", "gtceu:lv_electric_pump"]
      k: Machine to machine
      v: Conveyor / pump covers set to export into the next machine.
    - i: ["laserio:laser_node", "laserio:card_item"]
      k: Many machines
      v: "LaserIO nodes with filtered cards: no pipes, no TPS cost."
---
# LV — 32 EU/t · Industrial Revolution I

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `lv` · **Tier:** `lv`

**Goal:** Full LV machine set, steady power, the EBF and the first resource multis.

**Exit items:** `gtceu:aluminium_ingot`, `gtceu:mv_machine_hull`

## Steps

1. **Power first** — Dynamos or a magnet generator → converter → soul infused wire. See the power setup below. (`thermal:dynamo_stirling`, `create_new_age:generator_coil`, `gtceu:lv_4a_energy_converter`)
2. **Components** — Motor first; everything is built from these five. (`gtceu:lv_electric_motor`, `gtceu:lv_electric_piston`, `gtceu:lv_conveyor_module`, `gtceu:lv_robot_arm`, `gtceu:lv_electric_pump`)
3. **Machine order** — Bender → Wiremill → Lathe → Alloy Smelter → Assembler (unlocks hatches, kits, cheaper everything). (`gtceu:lv_bender`, `gtceu:lv_wiremill`, `gtceu:lv_lathe`, `gtceu:lv_alloy_smelter`, `gtceu:lv_assembler`)
4. **Then** — Macerator, Mixer, Extractor, Solidifier, Cutter (steel buzzsaw), Chemical Reactor, Electrolyzer, Centrifuge. (`gtceu:lv_macerator`, `gtceu:lv_mixer`, `gtceu:lv_extractor`, `gtceu:lv_fluid_solidifier`, `gtceu:lv_cutter`)
5. **EBF** — 16 cupronickel coils. Two LV energy hatches reach MV recipes: aluminium and signalum before MV machines. (`gtceu:cupronickel_coil_block`, `gtceu:electric_blast_furnace`)
6. **Resource multis** — Mechanical Sieve: 64 in → 16 of each drop every 40 s. Void Extractor: ores the sieve never gives. Rock Filtrator: gems. One energy hatch each. (`gtceu:mechanical_sieve`, `gtceu:void_extractor`, `gtceu:rock_filtrator`)
7. **Drilling fluid** — Creosote → lubricant → drilling fluid. (`gtceu:lv_distillery`, `gtceu:lubricant_bucket`, `gtceu:drilling_fluid_bucket`)
8. **Ore processing** — Crushed ore + water → dust + byproducts, twice the primitive speed, no fuel. (`gtceu:electric_ore_factory`)
9. **Arc furnace** — Needs graphite. Recycles machines; annealed copper. (`gtceu:graphite_dust`, `gtceu:lv_arc_furnace`, `gtceu:annealed_copper_ingot`)
10. **Towards MV** — Realgar + sphalerite → gallium arsenide → silicon boule in the EBF. (`gtceu:gallium_arsenide_dust`, `gtceu:silicon_boule`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `thermal:dynamo_stirling` | 4–6 |
| `thermal:dynamo_lapidary` | 2–4 |
| `gtceu:lv_4a_energy_converter` | 1–2 |
| `gtceu:lv_assembler` | 2 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_alloy_smelter` | 1 |
| `gtceu:lv_macerator` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:mechanical_sieve` | 1–2 |
| `gtceu:void_extractor` | 1 |
| `gtceu:rock_filtrator` | 1 |
| `gtceu:electric_ore_factory` | 1 |

## Setups

- [Four-sieve block (gravel, sand, dust, blackstone)](../chains/lv/sieve_block4.md)
- [Diamond power (Lapidary Dynamos)](../chains/lv/power_lapidary.md)
- [Cupronickel coils ×16](../chains/lv/coils.md)
- [Drilling fluid](../chains/lv/drilling.md)
- [Void Extractor](../chains/lv/void.md)
- [Rock Filtrator (gems)](../chains/lv/geodes.md)
- [Ore processing](../chains/lv/ores.md)
- [Distilled water](../chains/lv/distilled.md)
- [Crops: Greenhouse (LV, day and night)](../chains/lv/crop_greenhouse.md)
- [Component wall: always a stock of every part (no AE2)](../chains/lv/comp_stock.md)
- [Parts row 1: rods, plates, bolts, gears](../chains/lv/comp_parts.md)
- [Parts row 2: wires, fine wire, cables](../chains/lv/comp_wires.md)
- [LV Electric Motor line](../chains/lv/comp_motor.md)
- [LV Electric Piston line](../chains/lv/comp_piston.md)
- [LV Conveyor Module line](../chains/lv/comp_conveyor.md)
- [LV Electric Pump line](../chains/lv/comp_pump.md)
- [LV Robot Arm line](../chains/lv/comp_robot_arm.md)
- [LV circuit line (Basic Electronic Circuit)](../chains/lv/comp_circuit_lv.md)
- [Magnets: from magnetite block to Fluxuated Magnetite](../chains/lv/magnets.md)
- [Treated wood: cutter + spout](../chains/lv/treated_wood.md)
- [Fertilizer (for the rubber extractor and greenhouses)](../chains/lv/fertilizer.md)
- [Ingots, wrought iron, wires and foil from the sieve](../chains/lv/ingots.md)
- [Glue line (resin → glue)](../chains/lv/glue.md)
- [LV hull line (Create mechanical crafters)](../chains/lv/lv_hull_line.md)
- [Soul infused ingots (LV superconductor): sand → soul sand → dust + invar](../chains/lv/soul_infused.md)

## Power

[Diamond power (Lapidary Dynamos)](../chains/lv/power_lapidary.md)

## Storage

- **Raw ores:** One Super Chest per main ore (thousands of items). (`gtceu:lv_super_chest`)
- **Fluids:** Steel drums now; Super Tank once you have polyethylene (4 LV circuits + 3 steel plates + hermetic casing + LV pump). (`gtceu:lv_super_tank`, `gtceu:steel_drum`)
- **Machine to machine:** Conveyor / pump covers set to export into the next machine. (`gtceu:lv_conveyor_module`, `gtceu:lv_electric_pump`)
- **Many machines:** LaserIO nodes with filtered cards: no pipes, no TPS cost. (`laserio:laser_node`, `laserio:card_item`)

## Multiblocks

`gtceu:electric_blast_furnace`, `gtceu:mechanical_sieve`, `gtceu:void_extractor`, `gtceu:rock_filtrator`, `gtceu:electric_ore_factory`

## Plan phases

- [Raw materials](../plan/p2.md)
- [Base materials](../plan/p3.md)
- [Parts in stock](../plan/p4.md)
