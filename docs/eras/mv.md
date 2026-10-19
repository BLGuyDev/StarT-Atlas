---
kind: era
id: mv
order: 40
data:
  id: mv
  tier: mv
  name: MV
  sub: "128 EU/t · Industrial Revolution II"
  goal: Aluminium in bulk, silicon wafers and chips, circuit assembler, first plastics, AE2.
  exit: ["gtceu:stainless_steel_ingot", "gtceu:hv_machine_hull"]
  steps:
    - i: ["minecraft:clay", "gtceu:mv_electrolyzer", "gtceu:aluminium_dust"]
      t: Aluminium forever
      d: Barrel clay from sieve dust → electrolyze → Al + Si + Na + Li.
    - i: ["gtceu:signalum_ingot", "gtceu:mv_4a_energy_converter"]
      t: MV power line
      d: Signalum = 1 silver + 3 copper + 4 redstone. MV converters and wire.
    - i: ["gtceu:silicon_boule", "gtceu:mv_cutter", "gtceu:silicon_wafer"]
      t: Wafers
      d: Boule → 16 wafers. MV cutter with lubricant.
    - i: ["gtceu:mv_laser_engraver", "gtceu:red_glass_lens", "gtceu:ilc_chip", "gtceu:ram_chip"]
      t: Chips
      d: |-
        Laser engraver + coloured lens: ILC (red), RAM (green), ULPIC (blue), CPU (white).
    - i: ["gtceu:lv_circuit_assembler", "gtceu:basic_integrated_circuit", "gtceu:good_integrated_circuit"]
      t: Integrated circuits
      d: Much cheaper LV and MV circuits.
    - i: ["gtceu:sulfuric_acid_bucket", "gtceu:polyethylene_bucket"]
      t: First chemistry
      d: Sulfuric acid → ethylene → polyethylene.
    - i: ["gtceu:sodium_persulfate_bucket", "gtceu:phenolic_printed_circuit_board", "gtceu:good_electronic_circuit"]
      t: Etching
      d: Sodium persulfate or iron III chloride etch the boards.
    - i: ["gtceu:greenhouse", "gtceu:pyrolyse_oven"]
      t: Wood economy
      d: |-
        Greenhouse logs → Pyrolyse Oven: charcoal, creosote, later oil.
    - i: ["gtceu:rare_earth_dust", "gtceu:chromite_dust", "gtceu:vanadium_magnetite_dust"]
      t: Process the void fluids
      d: MV centrifuge/electrolyzer unlock everything stored from the Void Extractor. Chromite (chromium) and pyrolusite (manganese) are already MV here, so stainless and Kanthal can be prepared at the end of MV.
    - i: ["ae2:sky_dust", "gtceu:fluix_steel_dust", "ae2:controller"]
      t: AE2 (late MV)
      d: |-
        Not a first MV step: fluix steel ingots need an EBF at 1900 K (Kanthal coils) and sky dust needs ender pearl dust. Controller = 4 diamond skystone alloy plates + 4 engineering processors + fluix steel frame; then drive, crafting terminal.
  build:
    - id: gtceu:mv_electrolyzer
      "n": "2"
    - id: gtceu:mv_centrifuge
      "n": "2"
    - id: gtceu:mv_cutter
      "n": "1"
    - id: gtceu:mv_laser_engraver
      "n": "2"
    - id: gtceu:lv_circuit_assembler
      "n": "1"
    - id: gtceu:mv_chemical_reactor
      "n": "3–4"
    - id: gtceu:mv_assembler
      "n": "1"
    - id: gtceu:greenhouse
      "n": "1"
    - id: gtceu:pyrolyse_oven
      "n": "1"
  power: power_mv
  setups:
    - aluminium
    - wafer
    - sulfuric
    - polyethylene
    - sea_water
    - wood_gas
    - chlorine
    - etchant
    - wood
    - rare_residue
    - slurry
    - skystone
    - steel_ebf
    - mv_hull
    - mv_hull_line
    - comp_mv
    - mv_chlorine
    - mv_fecl3
    - mv_board
    - mv_gaas
    - mv_diode
    - mv_circuit
    - comp_mv_arm
  multis: ["gtceu:greenhouse", "gtceu:pyrolyse_oven", "gtceu:large_me_assembler"]
  storage:
    - i: ["ae2:controller", "ae2:drive", "ae2:crafting_terminal"]
      k: AE2 starts
      v: |-
        Late MV or HV: once the controller stands, move all storage into ME drives.
    - i: ["gtceu:mv_super_tank"]
      k: Chemicals
      v: One Super Tank per acid/gas (4 MV circuits + 3 aluminium plates + hermetic casing + MV pump); lock output hatches to their fluid.
    - i: ["laserio:laser_node"]
      k: Chem lines
      v: One LaserIO node per reactor cluster, fluid cards with filters.
---
# MV — 128 EU/t · Industrial Revolution II

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `mv` · **Tier:** `mv`

**Goal:** Aluminium in bulk, silicon wafers and chips, circuit assembler, first plastics, AE2.

**Exit items:** `gtceu:stainless_steel_ingot`, `gtceu:hv_machine_hull`

## Steps

1. **Aluminium forever** — Barrel clay from sieve dust → electrolyze → Al + Si + Na + Li. (`minecraft:clay`, `gtceu:mv_electrolyzer`, `gtceu:aluminium_dust`)
2. **MV power line** — Signalum = 1 silver + 3 copper + 4 redstone. MV converters and wire. (`gtceu:signalum_ingot`, `gtceu:mv_4a_energy_converter`)
3. **Wafers** — Boule → 16 wafers. MV cutter with lubricant. (`gtceu:silicon_boule`, `gtceu:mv_cutter`, `gtceu:silicon_wafer`)
4. **Chips** — Laser engraver + coloured lens: ILC (red), RAM (green), ULPIC (blue), CPU (white). (`gtceu:mv_laser_engraver`, `gtceu:red_glass_lens`, `gtceu:ilc_chip`, `gtceu:ram_chip`)
5. **Integrated circuits** — Much cheaper LV and MV circuits. (`gtceu:lv_circuit_assembler`, `gtceu:basic_integrated_circuit`, `gtceu:good_integrated_circuit`)
6. **First chemistry** — Sulfuric acid → ethylene → polyethylene. (`gtceu:sulfuric_acid_bucket`, `gtceu:polyethylene_bucket`)
7. **Etching** — Sodium persulfate or iron III chloride etch the boards. (`gtceu:sodium_persulfate_bucket`, `gtceu:phenolic_printed_circuit_board`, `gtceu:good_electronic_circuit`)
8. **Wood economy** — Greenhouse logs → Pyrolyse Oven: charcoal, creosote, later oil. (`gtceu:greenhouse`, `gtceu:pyrolyse_oven`)
9. **Process the void fluids** — MV centrifuge/electrolyzer unlock everything stored from the Void Extractor. Chromite (chromium) and pyrolusite (manganese) are already MV here, so stainless and Kanthal can be prepared at the end of MV. (`gtceu:rare_earth_dust`, `gtceu:chromite_dust`, `gtceu:vanadium_magnetite_dust`)
10. **AE2 (late MV)** — Not a first MV step: fluix steel ingots need an EBF at 1900 K (Kanthal coils) and sky dust needs ender pearl dust. Controller = 4 diamond skystone alloy plates + 4 engineering processors + fluix steel frame; then drive, crafting terminal. (`ae2:sky_dust`, `gtceu:fluix_steel_dust`, `ae2:controller`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:mv_electrolyzer` | 2 |
| `gtceu:mv_centrifuge` | 2 |
| `gtceu:mv_cutter` | 1 |
| `gtceu:mv_laser_engraver` | 2 |
| `gtceu:lv_circuit_assembler` | 1 |
| `gtceu:mv_chemical_reactor` | 3–4 |
| `gtceu:mv_assembler` | 1 |
| `gtceu:greenhouse` | 1 |
| `gtceu:pyrolyse_oven` | 1 |

## Setups

- [Infinite aluminium (clay)](../chains/mv/aluminium.md)
- [Silicon wafers &amp; chips](../chains/mv/wafer.md)
- [Sulfuric acid](../chains/mv/sulfuric.md)
- [Polyethylene](../chains/mv/polyethylene.md)
- [Salt water](../chains/mv/sea_water.md)
- [Methane &amp; wood chemicals](../chains/mv/wood_gas.md)
- [Chlorine, hydrogen &amp; HCl](../chains/mv/chlorine.md)
- [Board etching](../chains/mv/etchant.md)
- [Infinite wood &amp; charcoal](../chains/mv/wood.md)
- [Rare Ore Residue](../chains/mv/rare_residue.md)
- [Raw Ore Slurry &amp; mineral mixtures](../chains/mv/slurry.md)
- [Infinite sky stone (AE2)](../chains/mv/skystone.md)
- [Steel: Electric Blast Furnace + oxygen](../chains/mv/steel_ebf.md)
- [First MV hull and the LV → MV transformer](../chains/mv/mv_hull.md)
- [MV hull line (Create mechanical crafters)](../chains/mv/mv_hull_line.md)
- [MV components on LV machines](../chains/mv/comp_mv.md)
- [Chlorine and hydrochloric acid (water → salt water → acid)](../chains/mv/mv_chlorine.md)
- [Etching fluid (iron III chloride)](../chains/mv/mv_fecl3.md)
- [Phenolic printed circuit board (silver foil + etching)](../chains/mv/mv_board.md)
- [Gallium arsenide (sphalerite + realgar)](../chains/mv/mv_gaas.md)
- [Diodes (gallium arsenide + glass + fine wire)](../chains/mv/mv_diode.md)
- [MV circuit line (Good Electronic Circuit)](../chains/mv/mv_circuit.md)
- [MV Robot Arm (uses the new circuits)](../chains/mv/comp_mv_arm.md)

## Power

[MV power grid](../chains/power/power_mv.md)

## Storage

- **AE2 starts:** Late MV or HV: once the controller stands, move all storage into ME drives. (`ae2:controller`, `ae2:drive`, `ae2:crafting_terminal`)
- **Chemicals:** One Super Tank per acid/gas (4 MV circuits + 3 aluminium plates + hermetic casing + MV pump); lock output hatches to their fluid. (`gtceu:mv_super_tank`)
- **Chem lines:** One LaserIO node per reactor cluster, fluid cards with filters. (`laserio:laser_node`)

## Multiblocks

`gtceu:greenhouse`, `gtceu:pyrolyse_oven`, `gtceu:large_me_assembler`

## Plan phases

- [Into MV](../plan/p5.md)
- [MV circuits and chemistry](../plan/p6.md)
