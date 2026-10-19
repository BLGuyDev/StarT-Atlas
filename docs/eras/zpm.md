---
kind: era
id: zpm
order: 90
data:
  id: zpm
  tier: zpm
  name: ZPM & Classic Stargate
  sub: "131k EU/t · the gate to Abydos"
  goal: Crystal circuits, trinium coils, then the Classic Stargate.
  exit: ["sgjourney:classic_stargate_base_block"]
  steps:
    - i: ["gtceu:quantum_processor_mainframe", "gtceu:qbit_cpu_chip", "gtceu:fiber_reinforced_printed_circuit_board"]
      t: ZPM circuits
      d: |-
        First ZPM circuit: Quantum Processor Mainframe (qubit chips made with radon, extreme boards, three IV Circuit Assembler stages, final Assembly Line recipe at 30 720 EU/t). Five different items count as a ZPM circuit; the Research Station and its HPCA alone eat about 50.
    - i: ["gtceu:raw_crystal_chip", "gtceu:crystal_processor_mainframe"]
      t: Crystal circuits
      d: One exquisite emerald (4 emeralds) + 16 mB europium gives a 10 % chance of the FIRST raw crystal chip; hammer each chip into 9 parts and regrow every part with 16 mB europium (10 min per autoclave run). The crystal computer is the second ZPM circuit, the Crystal Processor Mainframe the UV circuit that the era multiblocks need.
    - i: ["gtceu:trinium_coil_block", "gtceu:naquadria_ingot"]
      t: Trinium
      d: Naquadah coils (7200 K) make trinium, naquadah alloy and osthendah; a trinium coil block needs 8 trinium ingots and a 122 880 EU/t assembler. Build ONE 9001 K furnace for naquadria and URD instead of upgrading every EBF.
    - i: ["gtceu:zpm_machine_hull", "gtceu:zpm_electric_motor", "gtceu:osthendah_ingot"]
      t: Hull and components
      d: |-
        Naquadah alloy hull with PBI (not PTFE), osthendah parts, europium wire: a ZPM motor eats 8 europium ingots. Motor, pump, piston, conveyor and arm are scanner research; emitter, sensor and field generator need the Research Station.
    - i: ["gtceu:research_station", "gtceu:data_orb", "gtceu:object_holder"]
      t: Research
      d: Moved here from LuV. The station recipe needs 8 ZPM circuits, 2 ZPM motors, URD and trinium foil; its parts (36 advanced computer casings, Object Holder, computation hatch, HPCA components) need about 50 ZPM circuits. Station research writes onto data ORBS.
    - i: ["start_core:zpm_fusion_reactor", "gtceu:fusion_coil", "gtceu:darmstadtium_bucket"]
      t: Fusion MK II
      d: URD superconducting coil, fusion coil, tier-2 reflector casings; the reactor itself needs 4 UV circuits. Darmstadtium (tier-2 recipe) is the UV hull metal.
    - i: ["gtceu:crystal_processor_mainframe", "gtceu:component_part_assembly", "gtceu:heat_chamber"]
      t: UV circuits and multis
      d: Every ZPM-era multiblock recipe asks for 2 to 16 UV circuits (crystal mainframes, 61 440 EU/t Assembly Line, 16 CWU/t research). Component Part Assembly, Heat Chamber, Large Rotor Machine, Runic Engraver, Stargate Component Assembly and the Dimensional Finder add up to 40.
    - i: ["gtceu:large_rotor_machine", "kubejs:raw_stargate_rod", "kubejs:activated_stargate_rod"]
      t: Stargate rods
      d: |-
        Large Rotor Machine layers at UV power, then the Heat Chamber: 9 foil reams and 2 quantum stars per raw rod, 720 mB nether star concentrate to activate. The whole gate needs about 480 activated rods.
    - i: ["gtceu:dimensional_finder", "kubejs:abydos_coordinate_crystal"]
      t: Coordinates
      d: |-
        Dimensional Finder run in the Overworld: 48 CWU/t, 5 % chance, 16 ZPM sensors and 7200 mB naquadria per attempt; duplicate a lucky crystal in a scanner.
    - i: ["sgjourney:classic_stargate_ring_block", "sgjourney:classic_stargate_chevron_block", "sgjourney:classic_dhd"]
      t: Build the gate
      d: |-
        24 ring blocks (14 in the gate; the 9 chevrons and the base each consume one), 9 chevron blocks, 1 base block, DHD and crystal interface; the final step is Create mechanical crafting.
  setups:
    - zpm_asmd
    - zpm_quantum
    - zpm_circuits
    - luv_fusion
    - zpm_naq_products
    - zpm_alloys
    - zpm_coils
    - zpm_urd
    - zpm_hull
    - zpm_components
    - zpm_hatches
    - zpm_research
    - luv_research
    - zpm_data
    - zpm_components2
    - zpm_crystal
    - zpm_crystal2
    - zpm_uv_circuit
    - zpm_fusion
    - zpm_multis
    - zpm_rods
    - zpm_multis2
    - zpm_gate
    - zpm_argon
  multis:
    - gtceu:research_station
    - gtceu:high_performance_computation_array
    - gtceu:stargate_component_assembly
    - gtceu:large_rotor_machine
    - gtceu:runic_circuitry_assembling_station
    - gtceu:dimensional_finder
    - gtceu:heat_chamber
    - gtceu:component_part_assembly
    - gtceu:vacuum_chemical_reaction_chamber
  build:
    - id: gtceu:zpm_machine_hull
      "n": "4+"
    - id: gtceu:assembly_line
      "n": "2"
    - id: gtceu:luv_energy_input_hatch_4a
      "n": "3"
    - id: gtceu:research_station
      "n": "1"
    - id: gtceu:high_performance_computation_array
      "n": "1"
    - id: gtceu:large_assembler
      "n": "2"
    - id: gtceu:electric_blast_furnace
      "n": "3"
    - id: gtceu:large_mixer
      "n": "2"
    - id: start_core:luv_fusion_reactor
      "n": "1"
  power: zpm_power
  storage:
    - i: ["gtceu:data_stick", "gtceu:data_orb"]
      k: Research data
      v: Sticks for scanner research, orbs for Research Station research; a Data Bank shares them between Assembly Lines.
    - i: ["gtceu:uhpic_chip", "gtceu:quantum_star"]
      k: Keep stocked
      v: UHPIC chips (96 to 256 per multiblock) and quantum stars (2 per emitter, 6 per field generator) in drawers with Keep Exact 64.
---
# ZPM &amp; Classic Stargate — 131k EU/t · the gate to Abydos

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `zpm` · **Tier:** `zpm`

**Goal:** Crystal circuits, trinium coils, then the Classic Stargate.

**Exit items:** `sgjourney:classic_stargate_base_block`

## Steps

1. **ZPM circuits** — First ZPM circuit: Quantum Processor Mainframe (qubit chips made with radon, extreme boards, three IV Circuit Assembler stages, final Assembly Line recipe at 30 720 EU/t). Five different items count as a ZPM circuit; the Research Station and its HPCA alone eat about 50. (`gtceu:quantum_processor_mainframe`, `gtceu:qbit_cpu_chip`, `gtceu:fiber_reinforced_printed_circuit_board`)
2. **Crystal circuits** — One exquisite emerald (4 emeralds) + 16 mB europium gives a 10 % chance of the FIRST raw crystal chip; hammer each chip into 9 parts and regrow every part with 16 mB europium (10 min per autoclave run). The crystal computer is the second ZPM circuit, the Crystal Processor Mainframe the UV circuit that the era multiblocks need. (`gtceu:raw_crystal_chip`, `gtceu:crystal_processor_mainframe`)
3. **Trinium** — Naquadah coils (7200 K) make trinium, naquadah alloy and osthendah; a trinium coil block needs 8 trinium ingots and a 122 880 EU/t assembler. Build ONE 9001 K furnace for naquadria and URD instead of upgrading every EBF. (`gtceu:trinium_coil_block`, `gtceu:naquadria_ingot`)
4. **Hull and components** — Naquadah alloy hull with PBI (not PTFE), osthendah parts, europium wire: a ZPM motor eats 8 europium ingots. Motor, pump, piston, conveyor and arm are scanner research; emitter, sensor and field generator need the Research Station. (`gtceu:zpm_machine_hull`, `gtceu:zpm_electric_motor`, `gtceu:osthendah_ingot`)
5. **Research** — Moved here from LuV. The station recipe needs 8 ZPM circuits, 2 ZPM motors, URD and trinium foil; its parts (36 advanced computer casings, Object Holder, computation hatch, HPCA components) need about 50 ZPM circuits. Station research writes onto data ORBS. (`gtceu:research_station`, `gtceu:data_orb`, `gtceu:object_holder`)
6. **Fusion MK II** — URD superconducting coil, fusion coil, tier-2 reflector casings; the reactor itself needs 4 UV circuits. Darmstadtium (tier-2 recipe) is the UV hull metal. (`start_core:zpm_fusion_reactor`, `gtceu:fusion_coil`, `gtceu:darmstadtium_bucket`)
7. **UV circuits and multis** — Every ZPM-era multiblock recipe asks for 2 to 16 UV circuits (crystal mainframes, 61 440 EU/t Assembly Line, 16 CWU/t research). Component Part Assembly, Heat Chamber, Large Rotor Machine, Runic Engraver, Stargate Component Assembly and the Dimensional Finder add up to 40. (`gtceu:crystal_processor_mainframe`, `gtceu:component_part_assembly`, `gtceu:heat_chamber`)
8. **Stargate rods** — Large Rotor Machine layers at UV power, then the Heat Chamber: 9 foil reams and 2 quantum stars per raw rod, 720 mB nether star concentrate to activate. The whole gate needs about 480 activated rods. (`gtceu:large_rotor_machine`, `kubejs:raw_stargate_rod`, `kubejs:activated_stargate_rod`)
9. **Coordinates** — Dimensional Finder run in the Overworld: 48 CWU/t, 5 % chance, 16 ZPM sensors and 7200 mB naquadria per attempt; duplicate a lucky crystal in a scanner. (`gtceu:dimensional_finder`, `kubejs:abydos_coordinate_crystal`)
10. **Build the gate** — 24 ring blocks (14 in the gate; the 9 chevrons and the base each consume one), 9 chevron blocks, 1 base block, DHD and crystal interface; the final step is Create mechanical crafting. (`sgjourney:classic_stargate_ring_block`, `sgjourney:classic_stargate_chevron_block`, `sgjourney:classic_dhd`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:zpm_machine_hull` | 4+ |
| `gtceu:assembly_line` | 2 |
| `gtceu:luv_energy_input_hatch_4a` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:high_performance_computation_array` | 1 |
| `gtceu:large_assembler` | 2 |
| `gtceu:electric_blast_furnace` | 3 |
| `gtceu:large_mixer` | 2 |
| `start_core:luv_fusion_reactor` | 1 |

## Setups

- [Advanced SMDs (IV Assembler, 3840 EU/t): inductor, capacitor, diode, transistor, all with polybenzimidazole](../chains/zpm/zpm_asmd.md)
- [Quantum chips: nano CPU wafer + radon → qubit CPU wafer → 4 chips, and the extreme circuit board (reinforced epoxy → fiber board → extreme board)](../chains/zpm/zpm_quantum.md)
- [ZPM circuit: Quantum Processor Mainframe (processor → assembly → supercomputer in IV Circuit Assemblers, mainframe in the Assembly Line)](../chains/zpm/zpm_circuits.md)
- [Fusion MK I: superconducting coil + ZPM circuits + UHPIC chips in the Assembly Line, then europium in the reactor (reflector tier 1)](../chains/zpm/luv_fusion.md)
- [Naquadah products: 6 naquadah dust → 1 trinium + 1.5 enriched naquadah + 1.5 naquadria (centrifuges, acid loops, EBF 7000 / 7200 / 9000 K)](../chains/zpm/zpm_naq_products.md)
- [ZPM alloys: naquadah alloy (hull casing) and osthendah (all ZPM parts): mixers → EBF with naquadah coils (7200 K) → Vacuum Freezer with liquid helium](../chains/zpm/zpm_alloys.md)
- [EBF coils: naquadah coil block (30 720 EU/t) → trinium → trinium coil block (122 880 EU/t), niobium nitride foil in both](../chains/zpm/zpm_coils.md)
- [Uranium rhodium dinaquadide (URD, 9000 K) and dragonsteel (ZPM superconductor, 7100 K)](../chains/zpm/zpm_urd.md)
- [ZPM Machine Hull: naquadah alloy casing + 2 vanadium gallium cables (PPS foil + PVC foil + silicone rubber) + 288 mB PBI](../chains/zpm/zpm_hull.md)
- [ZPM components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 30 720 EU/t, osthendah + osmiridium + europium wire)](../chains/zpm/zpm_components.md)
- [ZPM Energy Input Hatch: europium voltage coils → Assembly Line (station research 8 CWU/t), then the ZPM transformer and 4A hatch](../chains/zpm/zpm_hatches.md)
- [Research Station parts: advanced computer casing, Object Holder, computation hatch, HPCA components (all need ZPM circuits)](../chains/zpm/zpm_research.md)
- [Research: Data Bank (IV power), High Performance Computation Array and Research Station (both 100 000 EU/t, ZPM circuits)](../chains/zpm/luv_research.md)
- [Research data: data stick (IV Scanner: ZPM motor, pump, piston, conveyor, arm) and data orb (Research Station: emitter, sensor, field generator, hatches)](../chains/zpm/zpm_data.md)
- [ZPM components 2: robot arm (scanned), emitter, sensor, field generator (station research, 2 quantum stars each, trinium foil, URD wire)](../chains/zpm/zpm_components2.md)
- [Crystal CPU: exquisite emerald + europium → raw crystal chip (10 %) → 9 parts → loop at 100 % → EBF with helium → laser engraver](../chains/zpm/zpm_crystal.md)
- [ZPM circuit 2: Crystal Processor Supercomputer (elite board, crystal processor → assembly in the LCAF, computer in the Assembly Line)](../chains/zpm/zpm_crystal2.md)
- [UV circuit: Crystal Processor Mainframe (2 crystal computers + advanced SMDs in the Assembly Line, station research 16 CWU/t) - 4 of them gate every ZPM multiblock](../chains/zpm/zpm_uv_circuit.md)
- [Fusion MK II (ZPM): URD superconducting coil → fusion coil, advanced reflector casing, then the reactor (needs 4 UV circuits) and darmstadtium](../chains/zpm/zpm_fusion.md)
- [Era multiblocks 1: Component Part Assembly, Heat Chamber, Large Rotor Machine (Assembly Line, ZPM power, 4 UV circuits each, station research 16 CWU/t)](../chains/zpm/zpm_multis.md)
- [Stargate rods: rod base → raw rod (Large Rotor Machine, foil reams, lubricant) → activated rod (Heat Chamber, nether star concentrate)](../chains/zpm/zpm_rods.md)
- [Era multiblocks 2: Runic Engraver (RCAS), Stargate Component Assembly, Dimensional Finder with coordinate crystals](../chains/zpm/zpm_multis2.md)
- [Classic Stargate: runes (RCAS) + gate parts (Component Part Assembly) + activated rods → ring, chevron, base blocks (Stargate Component Assembly) → Create mechanical crafting](../chains/zpm/zpm_gate.md)
- [ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines](../chains/zpm/zpm_argon.md)

## Power

[ZPM power: deuterium + tritium → helium plasma (MK I fusion) → Large Plasma Turbine with a ZPM rotor holder → ZPM dynamo hatch](../chains/power/zpm_power.md)

## Storage

- **Research data:** Sticks for scanner research, orbs for Research Station research; a Data Bank shares them between Assembly Lines. (`gtceu:data_stick`, `gtceu:data_orb`)
- **Keep stocked:** UHPIC chips (96 to 256 per multiblock) and quantum stars (2 per emitter, 6 per field generator) in drawers with Keep Exact 64. (`gtceu:uhpic_chip`, `gtceu:quantum_star`)

## Multiblocks

`gtceu:research_station`, `gtceu:high_performance_computation_array`, `gtceu:stargate_component_assembly`, `gtceu:large_rotor_machine`, `gtceu:runic_circuitry_assembling_station`, `gtceu:dimensional_finder`, `gtceu:heat_chamber`, `gtceu:component_part_assembly`, `gtceu:vacuum_chemical_reaction_chamber`

## Plan phases

- [ZPM: circuits and research](../plan/p12.md)
- [ZPM: fusion and Stargate](../plan/p13.md)
