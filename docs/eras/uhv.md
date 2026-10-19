---
kind: era
id: uhv
order: 110
data:
  id: uhv
  tier: uhv
  name: UHV · Ancient Gate
  sub: "2.1M EU/t · A Portal of Lost Worlds"
  goal: Runic tablets, void ingots and the Milky Way gate.
  exit: ["sgjourney:milky_way_stargate"]
  steps:
    - i: ["kubejs:ruined_computational_matrix", "kubejs:uhv_micropower_router", "gtceu:zalloy_ingot"]
      t: Ruined parts and zalloy
      d: |-
        Loot ruined component parts in Abydos and research them (128 to 144 CWU/t) to unlock the UHV parts: Component Part Assembly at 1 966 080 EU/t. Parts and components are built from zalloy (10 799 K, tritanium coils), zircalloy-4 (96 minutes per 257 ingots), zirconium (1 per 8 titanite) and zapolgium.
    - i: ["gtceu:uhv_machine_hull", "gtceu:uhv_energy_input_hatch", "gtceu:uhv_electric_motor"]
      t: Hull, hatches, components
      d: |-
        UHV hull = neutronium casing + 2 europium cables + 288 mB PEEK. UHV energy hatch: Assembly Line 40 s at 1 966 080 EU/t with 2 UHV voltage coils, research 128 CWU/t. UHV components: 600 ticks at 491 520 EU/t, built from the parts.
    - i: ["kubejs:runic_processor_mainframe", "kubejs:uepic_chip", "start_core:uhv_fusion_reactor"]
      t: First UEV circuit in UHV
      d: |-
        The Runic Processor Mainframe (UEV circuit) needs no UEV machine: Assembly Line, 600 000 EU/t, 1800 ticks. AUX I, the Ancient Stargate Generator and the Folding Akreyrium Stabiliser need UEV circuits and UEPIC chips, so build it in this era (uhv_runic, uev_circuits).
    - i: ["gtceu:wetware_processor_mainframe", "gtceu:network_hub"]
      t: Circuits and CWU
      d: UHV circuit = wetware mainframe (built in the UV era). Research at 128 to 176 CWU/t needs a Network Switch / Hub with several HPCAs, or the optimised HPCA parts of the UEV page.
    - i: ["kubejs:runic_tablet_complete", "gtceu:runic_inscribe_manipulate"]
      t: Runes
      d: |-
        Six runic tablets (Abydos loot, each can be converted into the next with 16 ancient runicalium foil + 1080 mB naquadria in a scanner) are fused with 21 600 mB naquadria in a sterile cleanroom into the complete tablet, the research item (176 CWU/t) of the Runic Inscribe Manipulate controller. That controller itself needs 4 UEV circuits and 16 UHV emitters: the controller is a UEV-circuit project.
    - i: ["gtceu:void_ingot", "gtceu:super_pressure_heat_chamber"]
      t: Void
      d: |-
        Echo shard → 144 mB echo fluid; 1 neutronium ingot + 144 mB echo fluid → raw void ingot (200 s); Heat Chamber 300 s → hot void ingot; vacuum freeze. Alternative: void dust in the Super Pressure Heat Chamber (150 s). The SPHC itself needs 4 UHV circuits, a UV field generator, 288 UHPIC chips and a double void plate.
    - i: ["kubejs:awakened_abyss_stargate_rod", "kubejs:awakened_inferno_stargate_rod"]
      t: Awakened rods
      d: Abyss and inferno fragments.
  setups:
    - uhv_zirconium
    - uhv_zapolgium
    - uhv_sc
    - uhv_alloys
    - uhv_hull
    - uhv_void
    - uhv_runic_infusion
    - uhv_runic
    - uhv_parts
    - uhv_parts2
    - uhv_components
    - uhv_components2
    - uhv_hatches
    - uhv_akreyrium
    - uhv_multis
    - uhv_gate
  multis:
    - gtceu:runic_inscribe_manipulate
    - gtceu:super_pressure_heat_chamber
    - gtceu:folding_akreyrium_stabiliser
    - gtceu:compact_assembly_line
    - gtceu:bulk_ore_processing_array
    - gtceu:manifold_centrifuge
    - gtceu:injection_mixer
    - gtceu:bacteria_synthesizer
    - gtceu:supreme_plasma_turbine
  build:
    - id: gtceu:uhv_machine_hull
      "n": "4+"
    - id: gtceu:uv_energy_input_hatch_4a
      "n": "3"
    - id: gtceu:component_part_assembly
      "n": "1"
    - id: gtceu:assembly_line
      "n": "4"
    - id: gtceu:alloy_blast_smelter
      "n": "3"
    - id: gtceu:electric_blast_furnace
      "n": "2"
    - id: gtceu:mega_vacuum_freezer
      "n": "1"
    - id: gtceu:large_chemical_reactor
      "n": "8"
    - id: start_core:uv_fusion_reactor
      "n": "1"
  power: uhv_power
  storage:
    - i: ["kubejs:ruined_computational_matrix", "kubejs:uhv_micropower_router"]
      k: Parts
      v: Ruined parts (duplicate 1 to 2), UHV routers, matrices, panels, cores, transmission assemblies in drawers with Keep Exact 4 to 8.
    - i: ["gtceu:zalloy_ingot", "gtceu:zirconium_dust"]
      k: Metals
      v: Zalloy and zircalloy-4 ingots, zirconium dust (251 per zircalloy batch), neutronium ingots Keep Exact 16.
    - i: ["gtceu:wetware_processor_mainframe", "kubejs:uepic_chip"]
      k: Circuits
      v: UHV circuits (76 for the six controllers of uhv_multis) and UEPIC chips (up to 64 per craft).
---
# UHV · Ancient Gate — 2.1M EU/t · A Portal of Lost Worlds

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `uhv` · **Tier:** `uhv`

**Goal:** Runic tablets, void ingots and the Milky Way gate.

**Exit items:** `sgjourney:milky_way_stargate`

## Steps

1. **Ruined parts and zalloy** — Loot ruined component parts in Abydos and research them (128 to 144 CWU/t) to unlock the UHV parts: Component Part Assembly at 1 966 080 EU/t. Parts and components are built from zalloy (10 799 K, tritanium coils), zircalloy-4 (96 minutes per 257 ingots), zirconium (1 per 8 titanite) and zapolgium. (`kubejs:ruined_computational_matrix`, `kubejs:uhv_micropower_router`, `gtceu:zalloy_ingot`)
2. **Hull, hatches, components** — UHV hull = neutronium casing + 2 europium cables + 288 mB PEEK. UHV energy hatch: Assembly Line 40 s at 1 966 080 EU/t with 2 UHV voltage coils, research 128 CWU/t. UHV components: 600 ticks at 491 520 EU/t, built from the parts. (`gtceu:uhv_machine_hull`, `gtceu:uhv_energy_input_hatch`, `gtceu:uhv_electric_motor`)
3. **First UEV circuit in UHV** — The Runic Processor Mainframe (UEV circuit) needs no UEV machine: Assembly Line, 600 000 EU/t, 1800 ticks. AUX I, the Ancient Stargate Generator and the Folding Akreyrium Stabiliser need UEV circuits and UEPIC chips, so build it in this era (uhv\_runic, uev\_circuits). (`kubejs:runic_processor_mainframe`, `kubejs:uepic_chip`, `start_core:uhv_fusion_reactor`)
4. **Circuits and CWU** — UHV circuit = wetware mainframe (built in the UV era). Research at 128 to 176 CWU/t needs a Network Switch / Hub with several HPCAs, or the optimised HPCA parts of the UEV page. (`gtceu:wetware_processor_mainframe`, `gtceu:network_hub`)
5. **Runes** — Six runic tablets (Abydos loot, each can be converted into the next with 16 ancient runicalium foil + 1080 mB naquadria in a scanner) are fused with 21 600 mB naquadria in a sterile cleanroom into the complete tablet, the research item (176 CWU/t) of the Runic Inscribe Manipulate controller. That controller itself needs 4 UEV circuits and 16 UHV emitters: the controller is a UEV-circuit project. (`kubejs:runic_tablet_complete`, `gtceu:runic_inscribe_manipulate`)
6. **Void** — Echo shard → 144 mB echo fluid; 1 neutronium ingot + 144 mB echo fluid → raw void ingot (200 s); Heat Chamber 300 s → hot void ingot; vacuum freeze. Alternative: void dust in the Super Pressure Heat Chamber (150 s). The SPHC itself needs 4 UHV circuits, a UV field generator, 288 UHPIC chips and a double void plate. (`gtceu:void_ingot`, `gtceu:super_pressure_heat_chamber`)
7. **Awakened rods** — Abyss and inferno fragments. (`kubejs:awakened_abyss_stargate_rod`, `kubejs:awakened_inferno_stargate_rod`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:uhv_machine_hull` | 4+ |
| `gtceu:uv_energy_input_hatch_4a` | 3 |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:assembly_line` | 4 |
| `gtceu:alloy_blast_smelter` | 3 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:mega_vacuum_freezer` | 1 |
| `gtceu:large_chemical_reactor` | 8 |
| `start_core:uv_fusion_reactor` | 1 |

## Setups

- [Zirconium from titanite: perchloric acid leach, slurry, hydroxide, chloride, hydrogen reduction - 8 titanite dust per 1 zirconium dust](../chains/uhv/uhv_zirconium.md)
- [Zapolgium from zapolite: separator, centrifuge, electrolyzer, hydrochloric acid, KOH, EBF 10 299 K](../chains/uhv/uhv_zapolgium.md)
- [UHV superconductors: thorium plutonium duranide 241 (voltage coil wire) and ruthenium trinium americium neutronate (RTAN, UHV cable and fusion wire)](../chains/uhv/uhv_sc.md)
- [UHV metals: tritanium coil block (10 800 K), zalloy (ABS 10 799 K), zircalloy-4 (251 zirconium per batch), zirconium selenide diiodide](../chains/uhv/uhv_alloys.md)
- [UHV Machine Hull: neutronium casing + 2 europium cables (PPS foil + PVC foil + silicone) + 288 mB PEEK](../chains/uhv/uhv_hull.md)
- [Void ingot: echo shard → echo fluid; neutronium ingot + echo fluid → raw void ingot → Heat Chamber → hot void ingot → vacuum freezer](../chains/uhv/uhv_void.md)
- [Runic convergence infusion: netherite trisulfate complex → voidic nitride + astral fluorosilicate → primordial nitrosilicate; + magnesium nitride in the Vacuum Chemical Reaction Chamber](../chains/uhv/uhv_runic_infusion.md)
- [Runic circuits: board → etched board → convergence unit → runic processor (ZPM) → runic assembly (UV) → runic computer (UHV); the pack adds them to the circuit tags](../chains/uhv/uhv_runic.md)
- [UHV component parts 1/2 (Component Part Assembly, 1 966 080 EU/t): voltage coil, computational matrix, transmission assembly, precision drive mechanism - first unlocked by researching RUINED parts looted in Abydos](../chains/uhv/uhv_parts.md)
- [UHV component parts 2/2 (Component Part Assembly): microfluidic flow valve, super magnetic core, catalyst core, high strength panel, micropower router](../chains/uhv/uhv_parts2.md)
- [UHV components 1/2: motor, pump, conveyor module, piston and fluid regulator (Assembly Line, 30 s, 491 520 EU/t, research 128 CWU/t, component parts instead of raw metal)](../chains/uhv/uhv_components.md)
- [UHV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, catalyst cores, computational matrices, research 128 / 144 CWU/t)](../chains/uhv/uhv_components2.md)
- [UHV Energy Input Hatch: UHV voltage coils (Component Part Assembly) → Assembly Line (research 128 CWU/t, 1 966 080 EU/t), then transformer, 4A hatch and I/O hatches](../chains/uhv/uhv_hatches.md)
- [Akreyrium refining: gritty → lepton sparse (sifter) → electron / muon / tau sparse (manifold centrifuge) → dense (catalyst injection) → utopian akreyrium (folding stabiliser)](../chains/uhv/uhv_akreyrium.md)
- [UHV controllers (Assembly Line): Compact Assembly Line, Super Pressure Heat Chamber, Bacteria Synthesizer, Manifold Centrifuge, Injection Mixer, Folding Akreyrium Stabiliser](../chains/uhv/uhv_multis.md)
- [Milky Way Stargate (Ancient Gate): mechanical crafting](../chains/uhv/uhv_gate.md)

## Power

[UHV power: UHV rotor holder + Supreme Plasma Turbine (Assembly Line) burning nickel / iron plasma (UV reactor) or americium plasma (tier-4 reflectors, UHV reactor) into a UHV dynamo hatch](../chains/power/uhv_power.md)

## Storage

- **Parts:** Ruined parts (duplicate 1 to 2), UHV routers, matrices, panels, cores, transmission assemblies in drawers with Keep Exact 4 to 8. (`kubejs:ruined_computational_matrix`, `kubejs:uhv_micropower_router`)
- **Metals:** Zalloy and zircalloy-4 ingots, zirconium dust (251 per zircalloy batch), neutronium ingots Keep Exact 16. (`gtceu:zalloy_ingot`, `gtceu:zirconium_dust`)
- **Circuits:** UHV circuits (76 for the six controllers of uhv\_multis) and UEPIC chips (up to 64 per craft). (`gtceu:wetware_processor_mainframe`, `kubejs:uepic_chip`)

## Multiblocks

`gtceu:runic_inscribe_manipulate`, `gtceu:super_pressure_heat_chamber`, `gtceu:folding_akreyrium_stabiliser`, `gtceu:compact_assembly_line`, `gtceu:bulk_ore_processing_array`, `gtceu:manifold_centrifuge`, `gtceu:injection_mixer`, `gtceu:bacteria_synthesizer`, `gtceu:supreme_plasma_turbine`

## Plan phases

- [UHV: Abydos metals and runic circuits](../plan/p17.md)
