---
kind: era
id: hv
order: 50
data:
  id: hv
  tier: hv
  name: HV
  sub: "512 EU/t · Automation Age I"
  goal: Stainless steel, cleanroom, plastic boards, microprocessors, SMDs, PTFE and the LCR.
  exit: ["gtceu:titanium_ingot", "gtceu:ev_machine_hull"]
  steps:
    - i: ["gtceu:stainless_steel_dust", "gtceu:stainless_steel_ingot"]
      t: Stainless
      d: |-
        6 Fe + Cr + Mn + Ni in the mixer → EBF (1700 K, 480 EU/t: an HV energy hatch or two MV hatches). Can be prepared at the end of MV.
    - i: ["gtceu:kanthal_coil_block", "gtceu:hot_kanthal_ingot"]
      t: Kanthal
      d: |-
        HV step in this pack: iron + aluminium + chromium in the mixer, EBF (1800 K, 480 EU/t, 45 s; HV hatch or two MV hatches), cool hot ingots in an MV chemical bath (100 mB water, 20 s); coil = 8 double wire + 8 aluminium foil + copper.
    - i: ["gtceu:lumium_ingot", "gtceu:hv_4a_energy_converter"]
      t: HV line
      d: Lumium = silver + 3 tin + 2 glowstone.
    - i: ["gtceu:cleanroom", "gtceu:filter_casing", "gtceu:plascrete"]
      t: Cleanroom
      d: Nothing up to MV needs it. The controller is HV (HV hull, 2 HV motors, 1 HV circuit). Put circuit assemblers and engravers inside.
    - i: ["gtceu:plastic_printed_circuit_board", "gtceu:cpu_chip", "gtceu:microchip_processor"]
      t: Microprocessors
      d: Plastic boards + CPU chips. The whole HV/EV circuit tree.
    - i: ["gtceu:smd_transistor", "gtceu:smd_resistor", "gtceu:smd_capacitor"]
      t: SMDs
      d: HV assembler; far cheaper components.
    - i: ["gtceu:polytetrafluoroethylene_bucket", "gtceu:large_chemical_reactor"]
      t: PTFE → LCR
      d: PTFE pipe casings unlock the LCR and its circuit-24 shortcuts.
    - i: ["gtceu:pyrolyse_oven", "gtceu:oil_heavy_bucket"]
      t: Oil
      d: |-
        No oil in the world: 32 logs → 16 B heavy oil in the pyrolyse oven (circuit 3).
    - i: ["gtceu:energy_crystal", "gtceu:hv_autoclave"]
      t: Energy crystals
      d: Needed for HV/EV components and batteries.
    - i: ["gtceu:auto_maintenance_hatch"]
      t: Auto maintenance
      d: Swap every maintenance hatch.
  build:
    - id: gtceu:cleanroom
      "n": "1"
    - id: gtceu:mv_circuit_assembler
      "n": "1"
    - id: gtceu:hv_assembler
      "n": "1"
    - id: gtceu:large_chemical_reactor
      "n": "2–3"
    - id: gtceu:multi_smelter
      "n": "1"
    - id: gtceu:hv_autoclave
      "n": "1"
  power: power_hv
  setups:
    - stainless
    - ptfe
    - oil_pyro
    - oxygen
    - circuits_hv
    - smd
    - hv_cleanroom
    - kanthal
    - hv_components
    - hv_components2
    - oil_distill
    - chromium_line
    - hv_hull_line
  multis:
    - gtceu:cleanroom
    - gtceu:large_chemical_reactor
    - gtceu:multi_smelter
    - gtceu:industrial_barrel
    - gtceu:super_electric_ore_factory
    - gtceu:ore_processing_plant
  storage:
    - i: ["ae2:pattern_provider", "ae2:molecular_assembler"]
      k: Autocrafting
      v: Pattern providers on every machine; molecular assemblers for crafting-table recipes.
    - i: ["gtceu:me_output_bus", "gtceu:me_output_hatch"]
      k: Outputs
      v: |-
        ME output bus/hatch on multis: products go straight to the network.
    - i: ["fluxnetworks:flux_point", "fluxnetworks:flux_plug"]
      k: Power transport
      v: |-
        Flux Networks: wireless FE between generators and converters. Flux dust is an EV recipe, but the quest shop sells 8 plugs + 8 points for 16 coins once you build the Large Chemical Reactor.
---
# HV — 512 EU/t · Automation Age I

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `hv` · **Tier:** `hv`

**Goal:** Stainless steel, cleanroom, plastic boards, microprocessors, SMDs, PTFE and the LCR.

**Exit items:** `gtceu:titanium_ingot`, `gtceu:ev_machine_hull`

## Steps

1. **Stainless** — 6 Fe + Cr + Mn + Ni in the mixer → EBF (1700 K, 480 EU/t: an HV energy hatch or two MV hatches). Can be prepared at the end of MV. (`gtceu:stainless_steel_dust`, `gtceu:stainless_steel_ingot`)
2. **Kanthal** — HV step in this pack: iron + aluminium + chromium in the mixer, EBF (1800 K, 480 EU/t, 45 s; HV hatch or two MV hatches), cool hot ingots in an MV chemical bath (100 mB water, 20 s); coil = 8 double wire + 8 aluminium foil + copper. (`gtceu:kanthal_coil_block`, `gtceu:hot_kanthal_ingot`)
3. **HV line** — Lumium = silver + 3 tin + 2 glowstone. (`gtceu:lumium_ingot`, `gtceu:hv_4a_energy_converter`)
4. **Cleanroom** — Nothing up to MV needs it. The controller is HV (HV hull, 2 HV motors, 1 HV circuit). Put circuit assemblers and engravers inside. (`gtceu:cleanroom`, `gtceu:filter_casing`, `gtceu:plascrete`)
5. **Microprocessors** — Plastic boards + CPU chips. The whole HV/EV circuit tree. (`gtceu:plastic_printed_circuit_board`, `gtceu:cpu_chip`, `gtceu:microchip_processor`)
6. **SMDs** — HV assembler; far cheaper components. (`gtceu:smd_transistor`, `gtceu:smd_resistor`, `gtceu:smd_capacitor`)
7. **PTFE → LCR** — PTFE pipe casings unlock the LCR and its circuit-24 shortcuts. (`gtceu:polytetrafluoroethylene_bucket`, `gtceu:large_chemical_reactor`)
8. **Oil** — No oil in the world: 32 logs → 16 B heavy oil in the pyrolyse oven (circuit 3). (`gtceu:pyrolyse_oven`, `gtceu:oil_heavy_bucket`)
9. **Energy crystals** — Needed for HV/EV components and batteries. (`gtceu:energy_crystal`, `gtceu:hv_autoclave`)
10. **Auto maintenance** — Swap every maintenance hatch. (`gtceu:auto_maintenance_hatch`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:cleanroom` | 1 |
| `gtceu:mv_circuit_assembler` | 1 |
| `gtceu:hv_assembler` | 1 |
| `gtceu:large_chemical_reactor` | 2–3 |
| `gtceu:multi_smelter` | 1 |
| `gtceu:hv_autoclave` | 1 |

## Setups

- [Stainless steel: MV Mixer + HV Electric Blast Furnace](../chains/hv/stainless.md)
- [PTFE: three HV Chemical Reactors](../chains/hv/ptfe.md)
- [Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff](../chains/hv/oil_pyro.md)
- [Oxygen &amp; nitrogen from air (Gas Collector + Centrifuge)](../chains/hv/oxygen.md)
- [HV circuits: Advanced Integrated Circuit and Microprocessor Assembly](../chains/hv/circuits_hv.md)
- [SMDs from HV Assemblers (one machine per part)](../chains/hv/smd.md)
- [Cleanroom (5×5×5): plascrete, filter casings, one energy hatch](../chains/hv/hv_cleanroom.md)
- [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](../chains/hv/kanthal.md)
- [HV components 1/2: motor, pump, conveyor on LV assemblers](../chains/hv/hv_components.md)
- [HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers](../chains/hv/hv_components2.md)
- [Oil in a Distillery (no tower): methane from light oil, benzene from heavy oil](../chains/hv/oil_distill.md)
- [Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod](../chains/hv/chromium_line.md)
- [HV hull line (stainless casing + polyethylene)](../chains/hv/hv_hull_line.md)

## Power

[HV power: diatron gems in Lapidary Dynamos](../chains/power/power_hv.md)

## Storage

- **Autocrafting:** Pattern providers on every machine; molecular assemblers for crafting-table recipes. (`ae2:pattern_provider`, `ae2:molecular_assembler`)
- **Outputs:** ME output bus/hatch on multis: products go straight to the network. (`gtceu:me_output_bus`, `gtceu:me_output_hatch`)
- **Power transport:** Flux Networks: wireless FE between generators and converters. Flux dust is an EV recipe, but the quest shop sells 8 plugs + 8 points for 16 coins once you build the Large Chemical Reactor. (`fluxnetworks:flux_point`, `fluxnetworks:flux_plug`)

## Multiblocks

`gtceu:cleanroom`, `gtceu:large_chemical_reactor`, `gtceu:multi_smelter`, `gtceu:industrial_barrel`, `gtceu:super_electric_ore_factory`, `gtceu:ore_processing_plant`

## Plan phases

- [HV: stainless, Kanthal and air](../plan/p7.md)
- [HV: plastics and circuits](../plan/p8.md)
- [Combos: multiblocks that share parts](../plan/p20.md)
