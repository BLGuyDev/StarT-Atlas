---
kind: era
id: iv
order: 70
data:
  id: iv
  tier: iv
  name: IV
  sub: "8192 EU/t · Automation Age III"
  goal: Tungstensteel, the platinum line, RTM and HSS-G coils, ABS and parallel multis.
  exit: ["gtceu:assembly_line", "gtceu:luv_machine_hull"]
  steps:
    - i: ["gtceu:tungstate_dust", "gtceu:tungstic_acid_dust", "gtceu:tungsten_dust"]
      t: Tungsten
      d: Tungstate or scheelite + HCl in an EV Chemical Bath → tungstic acid → EV Electrolyzer → tungsten dust → EBF 3600 K (Nichrome coils) + Vacuum Freezer.
    - i: ["gtceu:tungsten_steel_ingot", "gtceu:iv_machine_hull"]
      t: Tungstensteel
      d: |-
        1 tungsten dust + 1 steel dust → EV Mixer → EBF 3000 K (Nichrome coils, EV hatch) → Vacuum Freezer. The IV material.
    - i: ["gtceu:purified_cooperite_ore", "gtceu:platinum_dust", "gtceu:palladium_dust", "gtceu:ruthenium_dust"]
      t: Platline
      d: Pt, Pd, Ru, Rh, Ir, Os. Ruthenium → RTM coils.
    - i: ["gtceu:rtm_alloy_coil_block", "gtceu:hssg_coil_block"]
      t: Coils
      d: RTM (4th tier, 4500 K, needs ruthenium) then HSS-G (5th, 5400 K). RTM coils unlock iridium, vanadium gallium and shellite.
    - i: ["gtceu:alloy_blast_smelter"]
      t: ABS
      d: Mixes + smelts in one step, 75 % of EBF time, molten output → freezer.
    - i: ["gtceu:shellite_ingot", "gtceu:iv_4a_energy_converter"]
      t: IV line
      d: Shellite = black bronze + 3 signalum.
    - i: ["gtceu:iv_parallel_hatch", "gtceu:large_chemical_bath"]
      t: Parallels
      d: Large multis accept parallel hatches. The IV Parallel Hatch (4 LuV circuits) and the IV Circuit Assembler (2 LuV circuits) already need LuV circuits.
    - i: ["gtceu:nuclear_reactor", "kubejs:thr_fuel_rod"]
      t: Nuclear
      d: "Optional: big power and isotope chains."
    - i: ["gtceu:advanced_smd_transistor", "gtceu:graphene_dust"]
      t: Advanced SMDs
      d: HSS-E/HSS-S + graphene.
  build:
    - id: gtceu:alloy_blast_smelter
      "n": "1"
    - id: gtceu:iv_circuit_assembler
      "n": "1"
    - id: gtceu:large_chemical_bath
      "n": "1"
    - id: gtceu:iv_parallel_hatch
      "n": "2+"
    - id: gtceu:super_ebf
      "n": "1"
  power: power_iv
  setups:
    - tungsten
    - platline
    - nether_star
    - elemental
    - iv_components
    - iv_circuits
    - rtm_coil
    - iv_hatches
    - abs_super_ebf
    - shellite_line
  multis:
    - gtceu:alloy_blast_smelter
    - gtceu:super_ebf
    - gtceu:nuclear_reactor
    - gtceu:large_chemical_bath
    - gtceu:large_mixer
    - gtceu:large_centrifuge
    - gtceu:large_electrolyzer
    - gtceu:large_maceration_tower
    - gtceu:rock_sifter
    - gtceu:void_excavator
    - gtceu:large_sieve
  storage:
    - i: ["megacells:mega_item_cell_housing", "megacells:cell_component_1m"]
      k: Mega cells
      v: Bulk storage for ores and dusts.
    - i: ["expatternprovider:ex_pattern_provider", "expatternprovider:assembler_matrix_frame"]
      k: Extended AE
      v: Bigger providers and the Assembler Matrix for crafting-grid recipes.
---
# IV — 8192 EU/t · Automation Age III

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `iv` · **Tier:** `iv`

**Goal:** Tungstensteel, the platinum line, RTM and HSS-G coils, ABS and parallel multis.

**Exit items:** `gtceu:assembly_line`, `gtceu:luv_machine_hull`

## Steps

1. **Tungsten** — Tungstate or scheelite + HCl in an EV Chemical Bath → tungstic acid → EV Electrolyzer → tungsten dust → EBF 3600 K (Nichrome coils) + Vacuum Freezer. (`gtceu:tungstate_dust`, `gtceu:tungstic_acid_dust`, `gtceu:tungsten_dust`)
2. **Tungstensteel** — 1 tungsten dust + 1 steel dust → EV Mixer → EBF 3000 K (Nichrome coils, EV hatch) → Vacuum Freezer. The IV material. (`gtceu:tungsten_steel_ingot`, `gtceu:iv_machine_hull`)
3. **Platline** — Pt, Pd, Ru, Rh, Ir, Os. Ruthenium → RTM coils. (`gtceu:purified_cooperite_ore`, `gtceu:platinum_dust`, `gtceu:palladium_dust`, `gtceu:ruthenium_dust`)
4. **Coils** — RTM (4th tier, 4500 K, needs ruthenium) then HSS-G (5th, 5400 K). RTM coils unlock iridium, vanadium gallium and shellite. (`gtceu:rtm_alloy_coil_block`, `gtceu:hssg_coil_block`)
5. **ABS** — Mixes + smelts in one step, 75 % of EBF time, molten output → freezer. (`gtceu:alloy_blast_smelter`)
6. **IV line** — Shellite = black bronze + 3 signalum. (`gtceu:shellite_ingot`, `gtceu:iv_4a_energy_converter`)
7. **Parallels** — Large multis accept parallel hatches. The IV Parallel Hatch (4 LuV circuits) and the IV Circuit Assembler (2 LuV circuits) already need LuV circuits. (`gtceu:iv_parallel_hatch`, `gtceu:large_chemical_bath`)
8. **Nuclear** — Optional: big power and isotope chains. (`gtceu:nuclear_reactor`, `kubejs:thr_fuel_rod`)
9. **Advanced SMDs** — HSS-E/HSS-S + graphene. (`gtceu:advanced_smd_transistor`, `gtceu:graphene_dust`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:alloy_blast_smelter` | 1 |
| `gtceu:iv_circuit_assembler` | 1 |
| `gtceu:large_chemical_bath` | 1 |
| `gtceu:iv_parallel_hatch` | 2+ |
| `gtceu:super_ebf` | 1 |

## Setups

- [Tungsten and tungsten steel: chemical bath → electrolyzer → EBF 3600 K (nichrome coils) → Vacuum Freezer](../chains/iv/tungsten.md)
- [Platinum group line: sludge → aqua regia centrifuge → platinum, palladium, rhodium, ruthenium, iridium, osmium](../chains/iv/platline.md)
- [Nether star loop: shards → energized shards → infused shards → impure star → implosion](../chains/iv/nether_star.md)
- [Elemental powders: blizz, blitz, basalz from dust + gas, then molten powder for the nether star loop](../chains/iv/elemental.md)
- [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](../chains/iv/iv_components.md)
- [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../chains/iv/iv_circuits.md)
- [RTM coil: ruthenium + tungsten + molybdenum → RTM alloy → double wire + vanadium steel foil + borosilicate foil + molten nichrome](../chains/iv/rtm_coil.md)
- [IV Energy and Dynamo Hatch: phosphorus wafer → MPIC wafer → HPIC wafer → 2 HPIC chips, IV voltage coil, IV Assembler](../chains/iv/iv_hatches.md)
- [Alloy Blast Smelter (alloy dust → molten metal in one step) and the Super EBF](../chains/iv/abs_super_ebf.md)
- [Shellite: signalum + black bronze → EV Mixer → EBF 4400 K (RTM coils, IV hatch) → wire → IV converters](../chains/iv/shellite_line.md)

## Power

[IV power: thorium fuel rods in the Nuclear Reactor, or fuel in the Extreme Combustion Engine, into an IV Dynamo Hatch](../chains/power/power_iv.md)

## Storage

- **Mega cells:** Bulk storage for ores and dusts. (`megacells:mega_item_cell_housing`, `megacells:cell_component_1m`)
- **Extended AE:** Bigger providers and the Assembler Matrix for crafting-grid recipes. (`expatternprovider:ex_pattern_provider`, `expatternprovider:assembler_matrix_frame`)

## Multiblocks

`gtceu:alloy_blast_smelter`, `gtceu:super_ebf`, `gtceu:nuclear_reactor`, `gtceu:large_chemical_bath`, `gtceu:large_mixer`, `gtceu:large_centrifuge`, `gtceu:large_electrolyzer`, `gtceu:large_maceration_tower`, `gtceu:rock_sifter`, `gtceu:void_excavator`, `gtceu:large_sieve`

## Plan phases

- [IV: tungsten, nether star, IV circuits and power](../plan/p10.md)
