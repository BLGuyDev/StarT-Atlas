---
kind: era
id: uev
order: 120
data:
  id: uev
  tier: uev
  name: UEV · Nether
  sub: "8.4M EU/t · Draconic Empires I"
  goal: Hellstones, hellish magmas, Hell Forge and the UEV alloys.
  exit: ["gtceu:uev_machine_hull"]
  steps:
    - i: ["kubejs:runic_processor_mainframe", "kubejs:uepic_chip"]
      t: UEV circuits and chips
      d: The first UEV circuit is the Runic Processor Mainframe (Assembly Line, 90 s, 600 000 EU/t). The UEPIC chip (UHPIC wafer + neutronium) is the chip of both late tiers; the Super Compact Heat Chamber alone eats 160.
    - i: ["kubejs:nether_talisman", "kubejs:cryostone", "kubejs:brimstone"]
      t: Hellstones
      d: Veins near radioactive / conductive ores.
    - i: ["start_core:hellforge", "gtceu:cryostate_quantum_chiller"]
      t: Forge & chiller
      d: Mega-kelvin smelting and new coolants.
    - i: ["gtceu:magmada_alloy_ingot", "gtceu:mythrolic_alloy_ingot", "gtceu:starium_alloy_ingot"]
      t: UEV alloys
      d: Forged in the Hell Forge.
    - i: ["gtceu:mythrolic_alloy_ingot", "gtceu:starium_alloy_ingot", "gtceu:magmada_alloy_ingot"]
      t: Plasma to ingot
      d: |-
        Alloys are made as plasma in the Hell Forge, cooled in the Cryostate Quantum Chiller with BEC oganesson, then frozen with superstate helium 3: three machines and a coolant loop per ingot.
    - i: ["gtceu:uev_machine_hull", "kubejs:uev_computational_matrix", "gtceu:uev_field_generator"]
      t: Hull, parts and components
      d: Hull = 8 mythrolic plates + 2 cerium tritelluride cables + PEDOT:PSS. Nine component parts (Component Part Assembly, station research of the UHV part) feed motor, pump, conveyor, piston, arm, emitter, sensor and field generator (Assembly Line, 30 s, 1 966 080 EU/t).
    - i: ["gtceu:uev_energy_input_hatch", "start_core:uev_parallel_hatch"]
      t: Hatches
      d: |-
        There are no UEV item or fluid hatches or buses: use UHV ones. UEV adds energy hatches (Assembly Line 40 s), transformers, 4A/16A/64A and 256A to 4096A laser hatches; the parallel hatch needs 4 UIV circuits.
    - i: ["gtceu:uev_rotor_holder", "gtceu:supreme_plasma_turbine", "start_core:uev_fusion_reactor"]
      t: Power and fusion
      d: UEV holder in the Supreme Plasma Turbine, boosted with tungsten disulfide and superstate helium 3. The UEV fusion reactor itself needs 4 UIV circuits, so it is finished in the UIV era; tier 5 reflectors, the advanced coil and casing MK4 are built here.
  setups:
    - uev_nether
    - uev_nether2
    - uev_chiller
    - uev_alloys
    - uev_chips
    - uev_circuits
    - uev_hull
    - uev_parts
    - uev_parts2
    - uev_components
    - uev_components2
    - uev_hatches
    - uev_multis
    - uev_fusion
  multis: ["gtceu:cryostate_quantum_chiller", "gtceu:mega_abs", "gtceu:super_compact_heat_chamber"]
  build:
    - id: gtceu:uev_machine_hull
      "n": "4+"
    - id: start_core:hellforge
      "n": "1"
    - id: gtceu:cryostate_quantum_chiller
      "n": "1"
    - id: gtceu:vacuum_freezer
      "n": "1"
    - id: gtceu:component_part_assembly
      "n": "1"
    - id: gtceu:assembly_line
      "n": "2"
    - id: gtceu:research_station
      "n": "1"
    - id: gtceu:uev_energy_input_hatch
      "n": "4"
    - id: gtceu:supreme_plasma_turbine
      "n": "1"
    - id: gtceu:mega_abs
      "n": "1"
  power: uev_power
  storage:
    - i: ["kubejs:uepic_chip", "kubejs:uev_universal_circuit"]
      k: Keep stocked
      v: UEPIC chips (160 for one heat chamber, 2 per hatch) and UEV circuits (12 per Hell Forge, Chiller and Mega ABS controller) in drawers with Keep Exact 16.
    - i: ["gtceu:superstate_helium_3_bucket", "gtceu:bec_og_bucket"]
      k: Coolant drums
      v: |-
        Superstate helium 3 and BEC oganesson in dedicated UHV drums on Pipez fluid pipes: every alloy ingot pulls 500 mB and 250 mB per 144 mB.
---
# UEV · Nether — 8.4M EU/t · Draconic Empires I

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `uev` · **Tier:** `uev`

**Goal:** Hellstones, hellish magmas, Hell Forge and the UEV alloys.

**Exit items:** `gtceu:uev_machine_hull`

## Steps

1. **UEV circuits and chips** — The first UEV circuit is the Runic Processor Mainframe (Assembly Line, 90 s, 600 000 EU/t). The UEPIC chip (UHPIC wafer + neutronium) is the chip of both late tiers; the Super Compact Heat Chamber alone eats 160. (`kubejs:runic_processor_mainframe`, `kubejs:uepic_chip`)
2. **Hellstones** — Veins near radioactive / conductive ores. (`kubejs:nether_talisman`, `kubejs:cryostone`, `kubejs:brimstone`)
3. **Forge &amp; chiller** — Mega-kelvin smelting and new coolants. (`start_core:hellforge`, `gtceu:cryostate_quantum_chiller`)
4. **UEV alloys** — Forged in the Hell Forge. (`gtceu:magmada_alloy_ingot`, `gtceu:mythrolic_alloy_ingot`, `gtceu:starium_alloy_ingot`)
5. **Plasma to ingot** — Alloys are made as plasma in the Hell Forge, cooled in the Cryostate Quantum Chiller with BEC oganesson, then frozen with superstate helium 3: three machines and a coolant loop per ingot. (`gtceu:mythrolic_alloy_ingot`, `gtceu:starium_alloy_ingot`, `gtceu:magmada_alloy_ingot`)
6. **Hull, parts and components** — Hull = 8 mythrolic plates + 2 cerium tritelluride cables + PEDOT:PSS. Nine component parts (Component Part Assembly, station research of the UHV part) feed motor, pump, conveyor, piston, arm, emitter, sensor and field generator (Assembly Line, 30 s, 1 966 080 EU/t). (`gtceu:uev_machine_hull`, `kubejs:uev_computational_matrix`, `gtceu:uev_field_generator`)
7. **Hatches** — There are no UEV item or fluid hatches or buses: use UHV ones. UEV adds energy hatches (Assembly Line 40 s), transformers, 4A/16A/64A and 256A to 4096A laser hatches; the parallel hatch needs 4 UIV circuits. (`gtceu:uev_energy_input_hatch`, `start_core:uev_parallel_hatch`)
8. **Power and fusion** — UEV holder in the Supreme Plasma Turbine, boosted with tungsten disulfide and superstate helium 3. The UEV fusion reactor itself needs 4 UIV circuits, so it is finished in the UIV era; tier 5 reflectors, the advanced coil and casing MK4 are built here. (`gtceu:uev_rotor_holder`, `gtceu:supreme_plasma_turbine`, `start_core:uev_fusion_reactor`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:uev_machine_hull` | 4+ |
| `start_core:hellforge` | 1 |
| `gtceu:cryostate_quantum_chiller` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:assembly_line` | 2 |
| `gtceu:research_station` | 1 |
| `gtceu:uev_energy_input_hatch` | 4 |
| `gtceu:supreme_plasma_turbine` | 1 |
| `gtceu:mega_abs` | 1 |

## Setups

- [Nether magma line: highly unstable nether magma → mystical magma → mythrillic, adamantamite and estaltadyne dusts (start of mythril, adamantine and estalt)](../chains/uev/uev_nether.md)
- [Mythril, adamantine, estalt, calamatium and isovol from the nether dusts (Advanced Synthesis Plant, large chemical reactor, EBF, vacuum chemical reactor)](../chains/uev/uev_nether2.md)
- [Cryostate Quantum Chiller coolants: superstate helium 3 → BEC oganesson (the loop that freezes every UEV and UIV alloy)](../chains/uev/uev_chiller.md)
- [UEV alloys (mythrolic, magmada, starium): molten metals + element plasma in the Hell Forge → alloy plasma → Cryostate Quantum Chiller → molten alloy → vacuum freezer → ingot](../chains/uev/uev_alloys.md)
- [UEPIC chip (UEV chip): UHPIC wafer + silicon carbide over bismuth tritelluride + 576 mB neutronium → wafer → 2 chips](../chains/uev/uev_chips.md)
- [UEV circuit: Runic Processor Mainframe (2 Runic Processor Computers + 32 QRAM chips + 5 living SMDs + runic convergence infusion)](../chains/uev/uev_circuits.md)
- [UEV Machine Hull: 8 mythrolic alloy plates → casing, + 2 cerium tritelluride single cables + 288 mB PEDOT:PSS plastic](../chains/uev/uev_hull.md)
- [UEV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve](../chains/uev/uev_parts.md)
- [UEV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router](../chains/uev/uev_parts2.md)
- [UEV components 1/2: electric motor, electric pump, conveyor module, electric piston](../chains/uev/uev_components.md)
- [UEV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator](../chains/uev/uev_components2.md)
- [UEV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches](../chains/uev/uev_hatches.md)
- [UEV multiblock controllers: Heart of the Flame → Hell Forge, Cryostate Quantum Chiller, Mega ABS, Super Compact Heat Chamber (all Assembly Line + station research)](../chains/uev/uev_multis.md)
- [UEV fusion parts: borealic reflector panel and casing (tier 5), advanced fusion coil, fusion casing MK4 → UEV Fusion Reactor](../chains/uev/uev_fusion.md)

## Power

[UEV power: plasma → Supreme Plasma Turbine with a UEV rotor holder (tungsten disulfide + superstate helium 3 boost) → laser or dynamo hatch](../chains/power/uev_power.md)

## Storage

- **Keep stocked:** UEPIC chips (160 for one heat chamber, 2 per hatch) and UEV circuits (12 per Hell Forge, Chiller and Mega ABS controller) in drawers with Keep Exact 16. (`kubejs:uepic_chip`, `kubejs:uev_universal_circuit`)
- **Coolant drums:** Superstate helium 3 and BEC oganesson in dedicated UHV drums on Pipez fluid pipes: every alloy ingot pulls 500 mB and 250 mB per 144 mB. (`gtceu:superstate_helium_3_bucket`, `gtceu:bec_og_bucket`)

## Multiblocks

`gtceu:cryostate_quantum_chiller`, `gtceu:mega_abs`, `gtceu:super_compact_heat_chamber`

## Plan phases

- [UEV: nether metals and Hell Forge](../plan/p18.md)
