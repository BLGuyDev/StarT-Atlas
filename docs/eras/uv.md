---
kind: era
id: uv
order: 100
data:
  id: uv
  tier: uv
  name: UV · Abydos
  sub: "524k EU/t · Adventures in Abydos"
  goal: Temples, tombs, akreyrium and Abydos magmas; wetware and neutronium.
  exit: ["gtceu:neutronium_ingot"]
  steps:
    - i: ["kubejs:abydos_talisman"]
      t: Survive the sands
      d: The tomb talisman replaces armour.
    - i: ["gtceu:uv_machine_hull", "gtceu:polyether_ether_ketone_bucket", "gtceu:darmstadtium_plate"]
      t: Hull and polymers
      d: UV hull = darmstadtium casing + 2 YBCO cables + 288 mB PEEK (not PBI). PEEK is an 8-step Large Chemical Reactor line; polyimide (living SMDs) is a 12-step line whose last two steps need a UV hatch.
    - i: ["gtceu:uv_energy_input_hatch", "gtceu:uv_electric_motor", "gtceu:tritan_steel_ingot"]
      t: Hatches and components
      d: |-
        UV hatch = Assembly Line, station research 64 CWU/t. UV components: Assembly Line, 600 ticks at 122 880 EU/t, 576 mB naquadria each, tritan steel parts, americium wire, gravi stars for emitters, sensors and field generators.
    - i: ["gtceu:network_switch", "gtceu:hpca_advanced_computation_component"]
      t: CWU
      d: |-
        Research asks 24 to 144 CWU/t: advanced HPCA components give 16 CWU/t each (4 UV circuits each); one HPCA tops out near 48, so a Network Switch joins several bridged HPCAs.
    - i: ["gtceu:gritty_akreyrium_bucket", "gtceu:cyclonic_sifter", "gtceu:molten_destabiliser"]
      t: Akreyrium
      d: |-
        The ZPM Fluid Drilling Rig (research 144 CWU/t) pumps the Abydos gritty akreyrium vein; the Cyclonic Sifter eats 280 B of it and the Molten Destabiliser 72 B (both on 491 520 EU/t Assembly Line recipes). The Exotic Gas Siphon listed here is a UEV recipe (UHV gas collector, 8 UHV circuits): not in this era.
    - i: ["gtceu:wetware_processor_mainframe", "gtceu:stem_cells"]
      t: Wetware
      d: UV circuits are the crystal mainframe (ZPM page) or the Wetware Processor Computer; the UHV circuit is the Wetware Processor Mainframe (2 computers + 60 living SMDs). Stem cells and growth medium come from the Sterile Cleanroom line (Sterilizing Filter Casings replace the filter casings; normal cleanroom recipes do not run in it), the circuit assemblers stay in a normal cleanroom.
    - i: ["start_core:uv_fusion_reactor", "gtceu:neutronium_ingot"]
      t: Neutronium
      d: |-
        UV Fusion Reactor: 4 UHV circuits (wetware mainframes), 128 UHPIC chips, quantum star, double americium plate, 2 ZPM field generators, 32 ENTED wire; research 96 CWU/t. Neutronium = 216 mB americium + 288 mB naquadria, 72 s, 117 964 EU/t, 600 MEU start, tier-3 complex reflectors. You will need tons: every UHV hull is 8 plates.
  setups:
    - uv_peek
    - uv_polyimide
    - uv_solder
    - uv_living_smd
    - uv_bio1
    - uv_bio2
    - uv_wetware1
    - uv_data
    - uv_research
    - uv_wetware2
    - uv_alloys
    - uv_hull
    - uv_hatches
    - uv_gravi
    - uv_components
    - uv_components2
    - uv_wetware3
    - uv_fusion
    - uv_fusion_mats
    - uv_multis
    - uv_multis2
    - uv_akreyrium
    - uv_magma
    - uv_rare_earth
  multis:
    - gtceu:cyclonic_sifter
    - gtceu:molten_destabiliser
    - gtceu:chemical_plant
    - gtceu:advanced_synthesis_plant
    - gtceu:mega_vacuum_freezer
    - gtceu:mega_blast_furnace
    - gtceu:titan_forge
  build:
    - id: gtceu:uv_machine_hull
      "n": "4+"
    - id: gtceu:assembly_line
      "n": "3"
    - id: gtceu:zpm_energy_input_hatch_4a
      "n": "3"
    - id: gtceu:research_station
      "n": "1"
    - id: gtceu:high_performance_computation_array
      "n": "3"
    - id: gtceu:network_switch
      "n": "1"
    - id: gtceu:large_chemical_reactor
      "n": "11"
    - id: gtceu:alloy_blast_smelter
      "n": "1"
    - id: start_core:uv_fusion_reactor
      "n": "1"
  power: uv_power
  storage:
    - i: ["kubejs:living_smd_capacitor", "kubejs:living_smd_diode"]
      k: Living SMDs
      v: Five types in drawers, Keep Exact 64; the UHV mainframe takes 12 of each per craft.
    - i: ["gtceu:uhpic_chip", "gtceu:gravi_star"]
      k: Keep stocked
      v: UHPIC chips (56 to 128 per multiblock), gravi stars for emitters, sensors and field generators (Keep Exact 4).
    - i: ["gtceu:naquadria_bucket", "gtceu:polyether_ether_ketone_bucket"]
      k: Drums
      v: Naquadria (576 mB per component), PEEK (288 mB per hull), ITLC soldering alloy and lubricant, steel drums with Pipez valves.
---
# UV · Abydos — 524k EU/t · Adventures in Abydos

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `uv` · **Tier:** `uv`

**Goal:** Temples, tombs, akreyrium and Abydos magmas; wetware and neutronium.

**Exit items:** `gtceu:neutronium_ingot`

## Steps

1. **Survive the sands** — The tomb talisman replaces armour. (`kubejs:abydos_talisman`)
2. **Hull and polymers** — UV hull = darmstadtium casing + 2 YBCO cables + 288 mB PEEK (not PBI). PEEK is an 8-step Large Chemical Reactor line; polyimide (living SMDs) is a 12-step line whose last two steps need a UV hatch. (`gtceu:uv_machine_hull`, `gtceu:polyether_ether_ketone_bucket`, `gtceu:darmstadtium_plate`)
3. **Hatches and components** — UV hatch = Assembly Line, station research 64 CWU/t. UV components: Assembly Line, 600 ticks at 122 880 EU/t, 576 mB naquadria each, tritan steel parts, americium wire, gravi stars for emitters, sensors and field generators. (`gtceu:uv_energy_input_hatch`, `gtceu:uv_electric_motor`, `gtceu:tritan_steel_ingot`)
4. **CWU** — Research asks 24 to 144 CWU/t: advanced HPCA components give 16 CWU/t each (4 UV circuits each); one HPCA tops out near 48, so a Network Switch joins several bridged HPCAs. (`gtceu:network_switch`, `gtceu:hpca_advanced_computation_component`)
5. **Akreyrium** — The ZPM Fluid Drilling Rig (research 144 CWU/t) pumps the Abydos gritty akreyrium vein; the Cyclonic Sifter eats 280 B of it and the Molten Destabiliser 72 B (both on 491 520 EU/t Assembly Line recipes). The Exotic Gas Siphon listed here is a UEV recipe (UHV gas collector, 8 UHV circuits): not in this era. (`gtceu:gritty_akreyrium_bucket`, `gtceu:cyclonic_sifter`, `gtceu:molten_destabiliser`)
6. **Wetware** — UV circuits are the crystal mainframe (ZPM page) or the Wetware Processor Computer; the UHV circuit is the Wetware Processor Mainframe (2 computers + 60 living SMDs). Stem cells and growth medium come from the Sterile Cleanroom line (Sterilizing Filter Casings replace the filter casings; normal cleanroom recipes do not run in it), the circuit assemblers stay in a normal cleanroom. (`gtceu:wetware_processor_mainframe`, `gtceu:stem_cells`)
7. **Neutronium** — UV Fusion Reactor: 4 UHV circuits (wetware mainframes), 128 UHPIC chips, quantum star, double americium plate, 2 ZPM field generators, 32 ENTED wire; research 96 CWU/t. Neutronium = 216 mB americium + 288 mB naquadria, 72 s, 117 964 EU/t, 600 MEU start, tier-3 complex reflectors. You will need tons: every UHV hull is 8 plates. (`start_core:uv_fusion_reactor`, `gtceu:neutronium_ingot`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `gtceu:uv_machine_hull` | 4+ |
| `gtceu:assembly_line` | 3 |
| `gtceu:zpm_energy_input_hatch_4a` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:high_performance_computation_array` | 3 |
| `gtceu:network_switch` | 1 |
| `gtceu:large_chemical_reactor` | 11 |
| `gtceu:alloy_blast_smelter` | 1 |
| `start_core:uv_fusion_reactor` | 1 |

## Setups

- [Polyether ether ketone (PEEK): 8 Large Chemical Reactor steps from toluene, benzene, fluorine and propene - the UV hull plastic](../chains/uv/uv_peek.md)
- [Polyimide: 12 reactions (maleic anhydride, BTDA, NMP, phenylenediamine, polyamic acid) - needs UV-tier Large Chemical Reactors for the last two steps](../chains/uv/uv_polyimide.md)
- [UV solder: indium tin lead cadmium soldering alloy in the Alloy Blast Smelter (2880 mB per 14 dust batch, circuit 14, 3000 K)](../chains/uv/uv_solder.md)
- [Living SMDs (inductor, transistor, capacitor, resistor, diode): ZPM Assembler recipes, 16 or 32 per run - the UV computer and the UHV mainframe cannot be built without them](../chains/uv/uv_living_smd.md)
- [Sterile bio line 1: bio chaff → bacteria → bacterial sludge → enriched sludge → mutagen (every step inside a Sterile Cleanroom)](../chains/uv/uv_bio1.md)
- [Sterile bio line 2: collagen → gelatin → agar, then raw medium, sterilized growth medium and stem cells (Sterile Cleanroom)](../chains/uv/uv_bio2.md)
- [Wetware circuits 1: wetware board → printed board → neuro processing unit → wetware processor (the LuV circuit of the wetware line)](../chains/uv/uv_wetware1.md)
- [Data Module (sterile circuit assembler) and the data item per CWU/t: orb below 32, module from 32, data DNA disk from 160, component data core from 320](../chains/uv/uv_data.md)
- [More CWU for UV research: advanced HPCA computation component (16 CWU/t), active cooler, bridge component and the Network Switch that joins several HPCAs](../chains/uv/uv_research.md)
- [Wetware circuits 2: QRAM chips → wetware processor assembly → Wetware Processor Computer (UV circuit, Assembly Line + 64 CWU/t research)](../chains/uv/uv_wetware2.md)
- [UV metals: tritan steel (Alloy Blast Smelter, 8990 K) and the UV superconductor enriched naquadah trinium europium duranide (UV mixer + 9900 K blast)](../chains/uv/uv_alloys.md)
- [UV Machine Hull: darmstadtium casing + 2 yttrium barium cuprate cables (PPS foil + PVC foil + silicone) + 288 mB PEEK](../chains/uv/uv_hull.md)
- [UV Energy Input Hatch: dysprosium voltage coils → Assembly Line (station research 64 CWU/t), then the UV transformer and 4A hatch](../chains/uv/uv_hatches.md)
- [Gravi star: nether star → quantum star (radon bath) → gravi star (autoclave with 288 mB neutronium) - 1 per UV emitter, sensor and field generator](../chains/uv/uv_gravi.md)
- [UV components 1/2: electric motor, pump, conveyor module and piston (Assembly Line, 30 s, 122 880 EU/t, research 32 CWU/t, 576 mB naquadria each)](../chains/uv/uv_components.md)
- [UV components 2/2: robot arm, emitter, sensor and field generator (Assembly Line, gravi stars, 96 naquadria foil each, research 32 / 48 CWU/t)](../chains/uv/uv_components2.md)
- [UHV circuit: Wetware Processor Mainframe (2 computers + living SMDs, 70 s at 300 000 EU/t, station research 96 CWU/t) - the UV fusion reactor and the UHV hatches ask for it](../chains/uv/uv_wetware3.md)
- [UV Fusion Reactor: complex reflector panel → complex reflector casing → fusion casing MK3 → reactor (4 UHV circuits, 128 UHPIC chips, research 96 CWU/t)](../chains/uv/uv_fusion.md)
- [Fusion metals: lutetium → americium, gallium + radon → duranium → tritanium, then neutronium (americium + naquadria); everything but neutronium runs in the ZPM Fusion Reactor (MK II) with tier-2/3 reflectors, neutronium needs the UV reactor (MK III)](../chains/uv/uv_fusion_mats.md)
- [UV multiblock controllers (Assembly Line): Mega Vacuum Freezer, Chemical Plant, Advanced Synthesis Plant, Titan Forge - all gated on UV circuits, UV components and 24 to 64 CWU/t research](../chains/uv/uv_multis.md)
- [UV-era controllers 2/2: Mega Blast Furnace (2 UHV circuits), Exotic Rock Crusher and Network Hub (4 UHV circuits) - the UHV circuit is the real gate](../chains/uv/uv_multis2.md)
- [Abydos mantle: ZPM Fluid Drilling Rig (144 CWU/t research) → gritty akreyrium → Cyclonic Sifter and Molten Destabiliser (280 B and 72 B of it per controller)](../chains/uv/uv_akreyrium.md)
- [Abydos dense magma → residues, lava and 12 raw ores (titanite, xenotime, monazite, scheelite; zapolite, crookesite, kitkaite, lautarite; naquadite, magnesite, chromite, magnetite)](../chains/uv/uv_magma.md)
- [Xenotime rare earth line: 5 machines → yttrium + small lutetium, dysprosium, europium, samarium dust; dysprosium and zapolgium rods are polarized in the pack’s own recipe](../chains/uv/uv_rare_earth.md)

## Power

[UV power: potassium + fluorine → nickel plasma (UV Fusion Reactor, tier-3 reflectors) → Large Plasma Turbine with a UV rotor holder → UV dynamo hatch](../chains/power/uv_power.md)

## Storage

- **Living SMDs:** Five types in drawers, Keep Exact 64; the UHV mainframe takes 12 of each per craft. (`kubejs:living_smd_capacitor`, `kubejs:living_smd_diode`)
- **Keep stocked:** UHPIC chips (56 to 128 per multiblock), gravi stars for emitters, sensors and field generators (Keep Exact 4). (`gtceu:uhpic_chip`, `gtceu:gravi_star`)
- **Drums:** Naquadria (576 mB per component), PEEK (288 mB per hull), ITLC soldering alloy and lubricant, steel drums with Pipez valves. (`gtceu:naquadria_bucket`, `gtceu:polyether_ether_ketone_bucket`)

## Multiblocks

`gtceu:cyclonic_sifter`, `gtceu:molten_destabiliser`, `gtceu:chemical_plant`, `gtceu:advanced_synthesis_plant`, `gtceu:mega_vacuum_freezer`, `gtceu:mega_blast_furnace`, `gtceu:titan_forge`

## Plan phases

- [UV: Abydos first, then wetware](../plan/p14.md)
- [UV: alloys and fusion MK III](../plan/p15.md)
- [UV: components and controllers](../plan/p16.md)
