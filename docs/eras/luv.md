---
kind: era
id: luv
order: 80
data:
  id: luv
  tier: luv
  name: LuV
  sub: "32k EU/t · Futuristic Mechanisms"
  goal: |-
    Assembly line, naquadah, power substation. Research and fusion MK I are ZPM-gated (4-8 ZPM circuits): see the ZPM era.
  exit: ["gtceu:zpm_machine_hull"]
  steps:
    - i: ["gtceu:assembly_line", "gtceu:data_stick", "gtceu:iv_scanner"]
      t: Assembly Line
      d: |-
        The LuV circuit (Nanoprocessor Mainframe) first, then every LuV component is an Assembly Line recipe: scan the IV part, Data Access Hatch, one ULV bus per ingredient, 30 s at 7680 EU/t. The LuV hatch needs an IV 4A hatch.
    - i: ["gtceu:research_station", "gtceu:high_performance_computation_array", "gtceu:data_bank"]
      t: Research
      d: |-
        Data Bank (IV power) first; the HPCA and the Research Station are 100 000 EU/t recipes with ZPM circuits and URD wire: unlocked at ZPM, not in LuV. 48 CWU/t without a bridge. Built in the ZPM era (the recipes need ZPM circuits): see the ZPM page.
    - i: ["gtceu:dimensional_destabiliser", "minecraft:nether_star", "gtceu:naquadah_dust"]
      t: Naquadah
      d: |-
        Controller: LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears. 1 nether star shard + 8 B PCB coolant → 20 raw naquadah per 60 s; the coolant loop is closed. Loop nether stars first.
    - i: ["start_core:luv_fusion_reactor", "gtceu:europium_bucket"]
      t: Fusion MK I
      d: |-
        Unlocked at ZPM (4 ZPM circuits; built at LuV power). Needs a superconducting coil (enriched naquadah + trinium), 4 ZPM circuits, 64 UHPIC chips and basic reflector casings; makes europium (144 mB per 28.8 s). Keep it on passive. Its recipe needs 4 ZPM circuits: it is built in the ZPM era.
    - i: ["gtceu:power_substation", "gtceu:lapotronic_energy_orb_cluster"]
      t: Substation
      d: Endgame energy storage; upgrade capacitors over time.
  power: power_iv
  setups:
    - luv_boards
    - luv_chips
    - luv_circuits
    - luv_lcaf
    - luv_alloys
    - luv_hsss
    - zpm_pbi
    - luv_hull
    - luv_hatches
    - luv_assembly_line
    - luv_components
    - luv_components2
    - pcb_coolant
    - naquadah
    - luv_power
    - luv_turbines
  multis:
    - gtceu:assembly_line
    - gtceu:data_bank
    - gtceu:power_substation
    - gtceu:active_transformer
    - gtceu:dimensional_destabiliser
  build:
    - id: gtceu:luv_machine_hull
      "n": "1+"
    - id: gtceu:iv_circuit_assembler
      "n": "1"
    - id: gtceu:large_circuit_assembler
      "n": "1"
    - id: gtceu:iv_energy_input_hatch_4a
      "n": "2"
    - id: gtceu:assembly_line
      "n": "1"
    - id: gtceu:dimensional_destabiliser
      "n": "1"
---
# LuV — 32k EU/t · Futuristic Mechanisms

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `luv` · **Tier:** `luv`

**Goal:** Assembly line, naquadah, power substation. Research and fusion MK I are ZPM-gated (4-8 ZPM circuits): see the ZPM era.

**Exit items:** `gtceu:zpm_machine_hull`

## Steps

1. **Assembly Line** — The LuV circuit (Nanoprocessor Mainframe) first, then every LuV component is an Assembly Line recipe: scan the IV part, Data Access Hatch, one ULV bus per ingredient, 30 s at 7680 EU/t. The LuV hatch needs an IV 4A hatch. (`gtceu:assembly_line`, `gtceu:data_stick`, `gtceu:iv_scanner`)
2. **Research** — Data Bank (IV power) first; the HPCA and the Research Station are 100 000 EU/t recipes with ZPM circuits and URD wire: unlocked at ZPM, not in LuV. 48 CWU/t without a bridge. Built in the ZPM era (the recipes need ZPM circuits): see the ZPM page. (`gtceu:research_station`, `gtceu:high_performance_computation_array`, `gtceu:data_bank`)
3. **Naquadah** — Controller: LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears. 1 nether star shard + 8 B PCB coolant → 20 raw naquadah per 60 s; the coolant loop is closed. Loop nether stars first. (`gtceu:dimensional_destabiliser`, `minecraft:nether_star`, `gtceu:naquadah_dust`)
4. **Fusion MK I** — Unlocked at ZPM (4 ZPM circuits; built at LuV power). Needs a superconducting coil (enriched naquadah + trinium), 4 ZPM circuits, 64 UHPIC chips and basic reflector casings; makes europium (144 mB per 28.8 s). Keep it on passive. Its recipe needs 4 ZPM circuits: it is built in the ZPM era. (`start_core:luv_fusion_reactor`, `gtceu:europium_bucket`)
5. **Substation** — Endgame energy storage; upgrade capacitors over time. (`gtceu:power_substation`, `gtceu:lapotronic_energy_orb_cluster`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:luv_machine_hull` | 1+ |
| `gtceu:iv_circuit_assembler` | 1 |
| `gtceu:large_circuit_assembler` | 1 |
| `gtceu:iv_energy_input_hatch_4a` | 2 |
| `gtceu:assembly_line` | 1 |
| `gtceu:dimensional_destabiliser` | 1 |

## Setups

- [Advanced Circuit Board: epoxy plate + gold foil → advanced board → electrum foil + iron III chloride → 6 per Nanoprocessor Mainframe](../chains/luv/luv_boards.md)
- [LuV chips: Nano CPU chip (CPU wafer + carbon fibers + molten glowstone) and NOR memory chip (phosphorus wafer)](../chains/luv/luv_chips.md)
- [LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)](../chains/luv/luv_circuits.md)
- [What LuV circuits unlock first: IV Circuit Assembler (2 LuV circuits), IV Parallel Hatch (4), Large Circuit Assembling Facility](../chains/luv/luv_lcaf.md)
- [LuV alloys: rhodium plated palladium (hull), ruridit (gears, rotor) and niobium titanium (cables, pipes), all IV Mixer → EBF 4500 K (RTM coils) → Vacuum Freezer](../chains/luv/luv_alloys.md)
- [HSS-S: HSS-G + iridium + osmium → EBF 5000 K (HSS-G coils) → Vacuum Freezer with liquid helium → the LuV component metal](../chains/luv/luv_hsss.md)
- [Polybenzimidazole (PBI): chlorobenzene → dichlorobenzidine → diaminobenzidine + diphenyl isophthalate → PBI (the hull, bus and ASMD plastic)](../chains/luv/zpm_pbi.md)
- [LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI](../chains/luv/luv_hull.md)
- [LuV Energy Input Hatch: IV 4A hatch gives the 30 720 EU/t, osmiridium → LuV voltage coil, Assembly Line recipe](../chains/luv/luv_hatches.md)
- [Assembly Line: scan the IV part on a data stick, put it in a Data Access Hatch, one ULV bus per ingredient, IV energy hatch](../chains/luv/luv_assembly_line.md)
- [LuV components 1: motor, piston, pump, conveyor module (Assembly Line, 30 s, 7680 EU/t, HSS-S + ruridit + niobium titanium + palladium wire)](../chains/luv/luv_components.md)
- [LuV components 2: robot arm, emitter, sensor, field generator (Assembly Line, 30 s, 7680 EU/t, LuV circuits, quantum stars, rhodium foil)](../chains/luv/luv_components2.md)
- [PCB coolant: benzene → biphenyl → polychlorinated biphenyl → mix with distilled water (HV machines)](../chains/luv/pcb_coolant.md)
- [Naquadah: nether star shard + PCB coolant in the Dimensional Destabiliser → raw naquadah → ore line → dust → EBF 5000 K; byproducts by the fluoroantimonic acid line](../chains/luv/naquadah.md)
- [Power Substation and Active Transformer: palladium substation casing, lapotron crystals, LuV circuits, UHPIC chips](../chains/luv/luv_power.md)
- [LuV power: Large Gas Turbine with a LuV rotor holder](../chains/luv/luv_turbines.md)

## Power

[IV power: thorium fuel rods in the Nuclear Reactor, or fuel in the Extreme Combustion Engine, into an IV Dynamo Hatch](../chains/power/power_iv.md)

## Multiblocks

`gtceu:assembly_line`, `gtceu:data_bank`, `gtceu:power_substation`, `gtceu:active_transformer`, `gtceu:dimensional_destabiliser`

## Plan phases

- [LuV: nano line](../plan/p11.md)
