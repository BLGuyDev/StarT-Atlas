---
kind: era
id: ev
order: 60
data:
  id: ev
  tier: ev
  name: EV
  sub: "2048 EU/t · Automation Age II"
  goal: Vacuum freezer, oil refining, liquid air, titanium, epoxy and nanoprocessors.
  exit: ["gtceu:tungsten_steel_ingot", "gtceu:iv_machine_hull"]
  steps:
    - i: ["gtceu:vacuum_freezer", "gtceu:nichrome_ingot", "gtceu:nichrome_coil_block"]
      t: Vacuum Freezer
      d: Cools hot ingots. Nichrome coils → enderium and heat bonuses.
    - i: ["gtceu:distillation_tower", "gtceu:cracker"]
      t: Refinery
      d: Pyrolysed oil → desulfurize → distill → crack → distill again.
    - i: ["gtceu:liquid_air_bucket", "gtceu:radon_bucket"]
      t: Air
      d: |-
        Liquid air, nether air and ender air: nitrogen, oxygen, argon, radon.
    - i: ["gtceu:rutile_dust", "gtceu:titanium_tetrachloride_bucket", "gtceu:titanium_ingot"]
      t: Titanium
      d: Rutile + carbon + chlorine → TiCl4 → magnesium in the EBF.
    - i: ["gtceu:epoxy_bucket", "gtceu:epoxy_printed_circuit_board"]
      t: Epoxy
      d: Bisphenol A + epichlorohydrin.
    - i: ["gtceu:phosphorus_boule", "gtceu:nor_memory_chip", "gtceu:mpic_chip"]
      t: Phosphorus wafers
      d: New chips and cheaper old ones.
    - i: ["gtceu:nano_cpu_chip", "gtceu:nano_processor"]
      t: Nanoprocessors
      d: EV circuit assembler; HV→IV circuits.
    - i: ["gtceu:cupric_chloride_solution_bucket"]
      t: Better etchant
      d: Re-encode board patterns to cupric chloride.
    - i: ["kubejs:multiblock_upgrade_kit"]
      t: Perfect-OC cubes
      d: Turns HV single machines into perfect-overclock multis.
  build:
    - id: gtceu:vacuum_freezer
      "n": "1"
    - id: gtceu:distillation_tower
      "n": "2–3"
    - id: gtceu:cracker
      "n": "1"
    - id: gtceu:ev_circuit_assembler
      "n": "1"
    - id: gtceu:large_chemical_reactor
      "n": "4+"
  power: power_ev
  setups: [refinery, air, radon, epoxy, molten_mix, titanium_line, nichrome_line, ev_components, ev_nitrobenzene]
  multis:
    - gtceu:vacuum_freezer
    - gtceu:distillation_tower
    - gtceu:cracker
    - gtceu:super_cutter
    - gtceu:implosion_compressor
  storage:
    - i: ["gtceu:me_pattern_buffer", "gtceu:me_pattern_buffer_proxy"]
      k: Pattern buffer
      v: One buffer feeds a multi with every pattern; proxies share it across wall-shared multis.
    - i: ["gtceu:me_stocking_input_bus", "gtceu:me_stocking_input_hatch"]
      k: Stocking
      v: Multis pull straight from ME — ideal for coolants, lubricant and catalysts.
---
# EV — 2048 EU/t · Automation Age II

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `ev` · **Tier:** `ev`

**Goal:** Vacuum freezer, oil refining, liquid air, titanium, epoxy and nanoprocessors.

**Exit items:** `gtceu:tungsten_steel_ingot`, `gtceu:iv_machine_hull`

## Steps

1. **Vacuum Freezer** — Cools hot ingots. Nichrome coils → enderium and heat bonuses. (`gtceu:vacuum_freezer`, `gtceu:nichrome_ingot`, `gtceu:nichrome_coil_block`)
2. **Refinery** — Pyrolysed oil → desulfurize → distill → crack → distill again. (`gtceu:distillation_tower`, `gtceu:cracker`)
3. **Air** — Liquid air, nether air and ender air: nitrogen, oxygen, argon, radon. (`gtceu:liquid_air_bucket`, `gtceu:radon_bucket`)
4. **Titanium** — Rutile + carbon + chlorine → TiCl4 → magnesium in the EBF. (`gtceu:rutile_dust`, `gtceu:titanium_tetrachloride_bucket`, `gtceu:titanium_ingot`)
5. **Epoxy** — Bisphenol A + epichlorohydrin. (`gtceu:epoxy_bucket`, `gtceu:epoxy_printed_circuit_board`)
6. **Phosphorus wafers** — New chips and cheaper old ones. (`gtceu:phosphorus_boule`, `gtceu:nor_memory_chip`, `gtceu:mpic_chip`)
7. **Nanoprocessors** — EV circuit assembler; HV→IV circuits. (`gtceu:nano_cpu_chip`, `gtceu:nano_processor`)
8. **Better etchant** — Re-encode board patterns to cupric chloride. (`gtceu:cupric_chloride_solution_bucket`)
9. **Perfect-OC cubes** — Turns HV single machines into perfect-overclock multis. (`kubejs:multiblock_upgrade_kit`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:distillation_tower` | 2–3 |
| `gtceu:cracker` | 1 |
| `gtceu:ev_circuit_assembler` | 1 |
| `gtceu:large_chemical_reactor` | 4+ |

## Setups

- [Oil refinery](../chains/ev/refinery.md)
- [Liquid air distillation](../chains/ev/air.md)
- [Radon](../chains/ev/radon.md)
- [Epoxy](../chains/ev/epoxy.md)
- [Molten Ore Mixture](../chains/ev/molten_mix.md)
- [Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer](../chains/ev/titanium_line.md)
- [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../chains/ev/nichrome_line.md)
- [EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull](../chains/ev/ev_components.md)
- [EV power: nitrobenzene in Large Gas Turbines (1 280 EU per mB)](../chains/ev/ev_nitrobenzene.md)

## Power

[EV power](../chains/power/power_ev.md)

## Storage

- **Pattern buffer:** One buffer feeds a multi with every pattern; proxies share it across wall-shared multis. (`gtceu:me_pattern_buffer`, `gtceu:me_pattern_buffer_proxy`)
- **Stocking:** Multis pull straight from ME — ideal for coolants, lubricant and catalysts. (`gtceu:me_stocking_input_bus`, `gtceu:me_stocking_input_hatch`)

## Multiblocks

`gtceu:vacuum_freezer`, `gtceu:distillation_tower`, `gtceu:cracker`, `gtceu:super_cutter`, `gtceu:implosion_compressor`

## Plan phases

- [EV: titanium, platinum and nitrobenzene power](../plan/p9.md)
