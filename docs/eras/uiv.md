---
kind: era
id: uiv
order: 130
data:
  id: uiv
  tier: uiv
  name: UIV · End & Draconic
  sub: "33.5M EU/t · Draconic Empires II → the stars"
  goal: Draco infusion, draconic cells, threading and the Draconic Stargate.
  exit: ["sgjourney:pegasus_stargate"]
  steps:
    - i: ["minecraft:dragon_egg", "gtceu:draco_infusion"]
      t: Draco Infusion
      d: Ordered 7-input infusion around an orb.
    - i: ["kubejs:draconic_stem_cells", "kubejs:draconic_processor_mainframe"]
      t: Draconic circuits
      d: Draco circuit assembler.
    - i: ["gtceu:draco_circuit_assembler", "kubejs:draconic_processor_mainframe", "kubejs:uipic_chip"]
      t: UIV circuits
      d: The Draco Circuit Assembler (small multi, 4 min Assembly Line recipe) makes the draconic computer and abyssal assembly (UEV) and the draconic mainframe and abyssal computer (UIV). Abyssal boards need the Abyssal Containment Room (a UXV-voltage recipe).
    - i: ["gtceu:chaotixic_alloy_ingot", "gtceu:ohmderblux_alloy_ingot", "gtceu:abyssal_alloy_ingot"]
      t: Abyssal alloys
      d: Hell Forge with abyssal catalysts (96 per draconic eye), tier 6 fusion plasma (paradox, voidic), then the same Chiller and freezer as UEV. Each run is 9 to 18 minutes at 33.5 M EU/t.
    - i: ["gtceu:uiv_machine_hull", "kubejs:uiv_computational_matrix", "gtceu:uiv_field_generator"]
      t: Hull, parts and components
      d: Hull = 8 chaotixic alloy plates + 2 polonium bismide cables + PEDOT:PSS (chaotixic is the plate, not abyssal alloy). Same part and component recipes as UEV with starium replaced by ohmderblux, 6x scaling and station research of the UEV items.
    - i: ["gtceu:uiv_energy_input_hatch", "start_core:uiv_absolute_parallel_hatch"]
      t: Hatches
      d: |-
        As UEV: no UIV item or fluid hatches, energy, transformer, multi-amp and laser hatches only. The UIV parallel hatch needs 4 UXV circuits (abyssal mainframes).
    - i: ["start_core:threading_controller", "start_core:uev_supreme_thread_helix"]
      t: Threading
      d: |-
        Stat-point multis: speed, efficiency, parallels, multi-thread.
    - i: ["start_core:komaru", "sgjourney:pegasus_stargate"]
      t: The stars
      d: Komaru modules, riftic rods, the Draconic gate.
  setups:
    - uiv_infusion
    - uiv_circuits
    - uiv_chips
    - uiv_alloys
    - uiv_hull
    - uiv_parts
    - uiv_parts2
    - uiv_components
    - uiv_components2
    - uiv_hatches
    - uiv_multis
    - uiv_threading
    - uiv_fusion
    - uiv_gate
  multis:
    - gtceu:draco_infusion
    - gtceu:draco_circuit_assembler
    - gtceu:ultimate_ebf
    - gtceu:atomic_materialization_plant
    - gtceu:primordial_infusion
    - gtceu:multithreaded_component_synthesis_forge
  build:
    - id: gtceu:uiv_machine_hull
      "n": "4+"
    - id: gtceu:draco_circuit_assembler
      "n": "1"
    - id: gtceu:draco_infusion
      "n": "1"
    - id: gtceu:component_part_hub
      "n": "1"
    - id: start_core:abyssal_containment_room
      "n": "1"
    - id: gtceu:ultimate_ebf
      "n": "1"
    - id: gtceu:atomic_materialization_plant
      "n": "1"
    - id: gtceu:nyinsane_plasma_turbine
      "n": "1"
    - id: start_core:threading_controller
      "n": "1"
  power: uiv_power
  storage:
    - i: ["kubejs:draconic_eye", "kubejs:draconic_stem_cells"]
      k: Keep stocked
      v: Draconic eyes (catalysts, abyssal mainframes), stem cells (eye, egg, UIPIC wafers) and dragon breath drums.
    - i: ["kubejs:uepic_chip", "kubejs:uipic_chip"]
      k: Chips
      v: UEPIC chips (64 to 224 per controller) and UIPIC chips (32 to 96) in separate drawers, Keep Exact 64.
---
# UIV · End &amp; Draconic — 33.5M EU/t · Draconic Empires II → the stars

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `uiv` · **Tier:** `uiv`

**Goal:** Draco infusion, draconic cells, threading and the Draconic Stargate.

**Exit items:** `sgjourney:pegasus_stargate`

## Steps

1. **Draco Infusion** — Ordered 7-input infusion around an orb. (`minecraft:dragon_egg`, `gtceu:draco_infusion`)
2. **Draconic circuits** — Draco circuit assembler. (`kubejs:draconic_stem_cells`, `kubejs:draconic_processor_mainframe`)
3. **UIV circuits** — The Draco Circuit Assembler (small multi, 4 min Assembly Line recipe) makes the draconic computer and abyssal assembly (UEV) and the draconic mainframe and abyssal computer (UIV). Abyssal boards need the Abyssal Containment Room (a UXV-voltage recipe). (`gtceu:draco_circuit_assembler`, `kubejs:draconic_processor_mainframe`, `kubejs:uipic_chip`)
4. **Abyssal alloys** — Hell Forge with abyssal catalysts (96 per draconic eye), tier 6 fusion plasma (paradox, voidic), then the same Chiller and freezer as UEV. Each run is 9 to 18 minutes at 33.5 M EU/t. (`gtceu:chaotixic_alloy_ingot`, `gtceu:ohmderblux_alloy_ingot`, `gtceu:abyssal_alloy_ingot`)
5. **Hull, parts and components** — Hull = 8 chaotixic alloy plates + 2 polonium bismide cables + PEDOT:PSS (chaotixic is the plate, not abyssal alloy). Same part and component recipes as UEV with starium replaced by ohmderblux, 6x scaling and station research of the UEV items. (`gtceu:uiv_machine_hull`, `kubejs:uiv_computational_matrix`, `gtceu:uiv_field_generator`)
6. **Hatches** — As UEV: no UIV item or fluid hatches, energy, transformer, multi-amp and laser hatches only. The UIV parallel hatch needs 4 UXV circuits (abyssal mainframes). (`gtceu:uiv_energy_input_hatch`, `start_core:uiv_absolute_parallel_hatch`)
7. **Threading** — Stat-point multis: speed, efficiency, parallels, multi-thread. (`start_core:threading_controller`, `start_core:uev_supreme_thread_helix`)
8. **The stars** — Komaru modules, riftic rods, the Draconic gate. (`start_core:komaru`, `sgjourney:pegasus_stargate`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:uiv_machine_hull` | 4+ |
| `gtceu:draco_circuit_assembler` | 1 |
| `gtceu:draco_infusion` | 1 |
| `gtceu:component_part_hub` | 1 |
| `start_core:abyssal_containment_room` | 1 |
| `gtceu:ultimate_ebf` | 1 |
| `gtceu:atomic_materialization_plant` | 1 |
| `gtceu:nyinsane_plasma_turbine` | 1 |
| `start_core:threading_controller` | 1 |

## Setups

- [Draco Infusion: controller (Assembly Line) and its 7-input recipes: draconic stem, brain and scale cells, draconic eye, dragon egg → dragon breath](../chains/uiv/uiv_infusion.md)
- [Draco Circuit Assembler (controller) and its UEV and UIV circuits: draconic computer and mainframe, abyssal assembly and computer](../chains/uiv/uiv_circuits.md)
- [UIPIC chip (UIV chip): UEPIC wafer + 7-input Draco Infusion with pure dragon breath → UIPIC wafer → 2 chips](../chains/uiv/uiv_chips.md)
- [UIV alloys (chaotixic, ohmderblux, abyssal): molten metals + fusion plasma in the Hell Forge → plasma → Chiller → molten → vacuum freezer; abyssal catalyst from the draconic eye](../chains/uiv/uiv_alloys.md)
- [UIV Machine Hull: 8 chaotixic alloy plates → casing, + 2 polonium bismide single cables + 288 mB PEDOT:PSS plastic](../chains/uiv/uiv_hull.md)
- [UIV component parts 1/2: voltage coil, computational matrix, transmission assembly, precision drive mechanism, microfluidic flow valve](../chains/uiv/uiv_parts.md)
- [UIV component parts 2/2: super magnetic core, catalyst core, high strength panel, micropower router](../chains/uiv/uiv_parts2.md)
- [UIV components 1/2: electric motor, electric pump, conveyor module, electric piston](../chains/uiv/uiv_components.md)
- [UIV components 2/2: robot arm, field generator, emitter, sensor, fluid regulator](../chains/uiv/uiv_components2.md)
- [UIV power hatches: energy hatch (Assembly Line), transformers, 4A / 16A / 64A hatches and 256A to 4096A laser hatches](../chains/uiv/uiv_hatches.md)
- [UIV multiblock controllers: Abyssal Containment Room, Ultimate EBF, Atomic Materialization Plant, Component Part Hub (all Assembly Line + station research)](../chains/uiv/uiv_multis.md)
- [Threading: prismalic helix core → prisma helical nucleus → Threading Controller (every threaded multiblock eats nuclei and UXV circuits)](../chains/uiv/uiv_threading.md)
- [UIV fusion parts: draconic reflector panel and casing (tier 6), auxiliary fusion coil MK2, boosted fusion casing MK2 → UEV and UIV Fusion Reactors](../chains/uiv/uiv_fusion.md)
- [Pegasus Stargate (Draconic Gate): mechanical crafting](../chains/uiv/uiv_gate.md)

## Power

[UIV power: plasma → Nyinsane Plasma Turbine with a UIV rotor holder (tungsten disulfide + BEC oganesson boost) → laser hatch](../chains/power/uiv_power.md)

## Storage

- **Keep stocked:** Draconic eyes (catalysts, abyssal mainframes), stem cells (eye, egg, UIPIC wafers) and dragon breath drums. (`kubejs:draconic_eye`, `kubejs:draconic_stem_cells`)
- **Chips:** UEPIC chips (64 to 224 per controller) and UIPIC chips (32 to 96) in separate drawers, Keep Exact 64. (`kubejs:uepic_chip`, `kubejs:uipic_chip`)

## Multiblocks

`gtceu:draco_infusion`, `gtceu:draco_circuit_assembler`, `gtceu:ultimate_ebf`, `gtceu:atomic_materialization_plant`, `gtceu:primordial_infusion`, `gtceu:multithreaded_component_synthesis_forge`

## Plan phases

- [UIV: Draco lines and threading](../plan/p19.md)
