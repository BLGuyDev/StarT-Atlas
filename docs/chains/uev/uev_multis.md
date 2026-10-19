---
kind: chain
id: uev_multis
order: 2100
data:
  t: |-
    UEV multiblock controllers: Heart of the Flame → Hell Forge, Cryostate Quantum Chiller, Mega ABS, Super Compact Heat Chamber (all Assembly Line + station research)
  inf: true
  "n":
    - - g0
      - |-
        Heart of the Flame: husk brick · 2 decaying core · 6 dense ancient netherite plate · 24 pure netherite screw · 500 000 mB flamewake solvent
      - g
      - functionalstorage:oak_1
      - - [Husk brick, "kubejs:husk_brick"]
        - [Decaying core, "kubejs:decaying_core"]
        - [Ancient netherite plate, "gtceu:dense_ancient_netherite_plate"]
        - [Pure netherite screw, "gtceu:pure_netherite_screw"]
    - - g1
      - |-
        Hell Forge: calamatium frame · 12 UEV circuit · 32 UHV high strength panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 calamatium rotor · 32 isovol screw · 240 B flamewake solvent · 60 B utopian akreyrium
      - g
      - functionalstorage:oak_1
      - - [Calamatium frame, "gtceu:calamatium_frame"]
        - [UHV field generator, "gtceu:uhv_field_generator"]
        - [UHV pump, "gtceu:uhv_electric_pump"]
        - [Neutronium huge pipe, "gtceu:neutronium_huge_fluid_pipe"]
        - [Calamatium rotor, "gtceu:calamatium_rotor"]
    - - g2
      - |-
        Cryostate Chiller: isovol frame · 12 UEV circuit · 32 UHV panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 isovol rotor · 32 calamatium screw · 1000 B liquid helium · 60 B akreyrium
      - g
      - functionalstorage:oak_1
      - - [Isovol frame, "gtceu:isovol_frame"]
        - [UHV field generator, "gtceu:uhv_field_generator"]
        - [Isovol rotor, "gtceu:isovol_rotor"]
        - [Calamatium screw, "gtceu:calamatium_screw"]
    - - g3
      - |-
        Mega ABS: UHV alloy smelter · 12 UEV circuit · 8 UHV field gen · 6 dense ancient netherite plate · 4 UHV arm · 12 UHV fluid regulator · 12 RTA neutronate quad wire · 4 calamatium rotor · 4 cerium tritelluride spring · 8 calamatium screw
      - g
      - functionalstorage:oak_1
      - - [UHV alloy smelter, "gtceu:uhv_alloy_smelter"]
        - [UHV robot arm, "gtceu:uhv_robot_arm"]
        - [UHV fluid regulator, "gtceu:uhv_fluid_regulator"]
        - [Cerium tritelluride spring, "gtceu:cerium_tritelluride_spring"]
    - - g4
      - |-
        Super Compact Heat Chamber: heat chamber · 4 UEV circuit · double prismalium plate · double ancient netherite plate · UHV field gen · 160 UEPIC chip · 48 stellarium wire · 6912 mB trinaquadalloy · 1728 mB tritanium
      - g
      - functionalstorage:oak_1
      - - [Heat chamber, "gtceu:heat_chamber"]
        - [UEPIC chip, "kubejs:uepic_chip"]
        - [Stellarium wire, "gtceu:stellarium_single_wire"]
        - [Prismalium plate, "gtceu:double_prismalium_plate"]
    - [a1, "Assembly Line · 5 min · 3 932 160 EU/t (research husk of the flame)", m, "gtceu:assembly_line"]
    - [a2, "Assembly Line · 140 s / 90 s · 7 864 320 EU/t", m, "gtceu:assembly_line"]
    - [a3, "Assembly Line · 90 s · 3 932 160 EU/t · and 200 s · 983 040 EU/t", m, "gtceu:assembly_line"]
    - [h0, Heart of the Flame, x, "kubejs:heart_of_the_flame"]
    - [o1, Hell Forge, o, "start_core:hellforge"]
    - [o2, Cryostate Quantum Chiller, o, "gtceu:cryostate_quantum_chiller"]
    - [o3, Mega ABS, o, "gtceu:mega_abs"]
    - [o4, Super Compact Heat Chamber, o, "gtceu:super_compact_heat_chamber"]
  e:
    - [g0, a1, "1"]
    - [a1, h0, "1 / 300 s"]
    - [h0, a2, research]
    - [g1, a2, "1"]
    - [g2, a2, "1"]
    - [a2, o1, "1 / 140 s"]
    - [a2, o2, "1 / 90 s"]
    - [g3, a3, "1"]
    - [g4, a3, "1"]
    - [a3, o3, "1 / 90 s"]
    - [a3, o4, "1 / 200 s"]
  tips:
    - |-
      Source: kjs additions/multiblock_recipes/nether_multis.js. Heart of the Flame: 6000 ticks, VHA[UEV] = 3 932 160 EU/t, station research of the Husk of the Flame (192 CWU/t). Hell Forge: 2800 ticks (140 s), VA[UEV] = 7 864 320 EU/t, research Heart of the Flame (VA[UHV], 192 CWU/t). Cryostate Quantum Chiller: 1800 ticks, VA[UEV], research Mega Vacuum Freezer (192 CWU/t). Mega ABS: 1800 ticks, VHA[UEV], research Super ABS (160 CWU/t); fluids 13 824 mB soldering alloy, 10 368 mB PEDOT:PSS, 12 000 mB utopian akreyrium, 8640 mB perfluoroelastomer rubber. Super Compact Heat Chamber: 4000 ticks (200 s), VHA[UHV] = 983 040 EU/t, research Super Pressure Heat Chamber (160 CWU/t); 160 UEPIC chips = 80 wafers (uev_chips).
    - |-
      Multiblock sizes (from the pack patterns): Cryostate Quantum Chiller about 2800 blocks: 776 reinforced cryostone casings, 640 void frames, 535 enriched naquadah pipe casings, 497 subzero casings (hatches go here), 216 firebox casings, 59 engine intake casings, 37 cleanroom glass, 20 heat vents. Mega ABS about 2100 blocks: 918 extreme temperature smelting casings (at least 898 must stay casings, rest hatches), 312 enriched estalt frames, 213 pipe casings, 147 coil blocks, 129 intake casings, 124 firebox casings, 120 reinforced brimstone casings, 68 heat escape casings, 48 machine casings, 1 muffler. Super Compact Heat Chamber: 74 enderium casings, 34 zalloy coils, 32 neutronium frames, 32 high temperature smelting casings (at least 22 casings), 16 firebox, 8 intake, 1 muffler. The Hell Forge pattern is in the start_core jar: Unverified counts.
    - |-
      Casing recipes (casings.js): reinforced cryostone casing = 16 cryostone compressed; reinforced brimstone casing = 16 brimstone compressed; subzero casing = assembler circuit 6, 4 aluminium plate + 2 pure netherite plate + 1 void frame → 2 casings; extreme temperature smelting casing = circuit 6, 4 calamatium plate + 2 astatium bioselex carbonite plate + 1 enriched estalt frame → 2 casings. Cryostone and brimstone come from exotic rock crushing (misc_materials.js): 32 netherrack + 500 mB liquid helium (cryostone, circuit 2) or 500 mB blaze (brimstone, circuit 3) with a seed block and lava not consumed, 300 ticks, VHA[LuV] → 2 stones.
    - |-
      Recipe oddity worth noting: three of the four controllers eat 12 UEV circuits each (Mega ABS 12, Hell Forge 12, Chiller 12; heat chamber 4): 40 Runic Processor Mainframes for the four. The UEV circuit line (uev_circuits) is the whole bottleneck of this era; the chips for the heat chamber (160) are the second.
    - |-
      Sub-steps people skip: (1) research chain: Husk of the Flame → Heart of the Flame → Hell Forge, and Super ABS, Mega Vacuum Freezer and Super Pressure Heat Chamber must exist first (UV and UHV pages); (2) utopian akreyrium (60 000 mB for forge or chiller, 12 000 for ABS) is the UHV akreyrium line output; (3) liquid helium 1 000 000 mB for the Chiller needs a dedicated tank and pipe; (4) the multis are huge: plan chunk loading and a flat build site before you start the casings.
    - |-
      Access to the End (verified): travel is cancelled without the access_end stage (dimensional_stages.js), granted by clicking the Milky Way Stargate with the End coordinate crystal. The End crystal is made in a Dimensional Finder run in the NETHER: 1 coordinate crystal + 64 end stone + 16 UHV sensors + 7200 mB echo fluid, 384 CWU/t (1 843 200 CWU), EUtVA(UIV) = 31 457 280 EU/t, 5 % chance; a UEV 4A hatch (33 554 432) covers it and a UEV 16A hatch gives margin, which is why the End comes right after the UEV 16A hatches. Crystal chain: Abydos crystal (Overworld, VHA[UV], 16 ZPM sensors) -> Nether crystal (run in Abydos, VHA[UEV], 16 UV sensors + 50 000 mB lava, 192 CWU/t) -> End crystal; every crystal can be duplicated in a scanner. Unverified: Husk of the Flame, decaying core and husk brick recipes and the Hell Forge pattern.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uhv_input_bus", 4]
    - ["gtceu:uhv_input_hatch", 4]
    - ["functionalstorage:oak_1", 20]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:uev_universal_circuit", "kubejs:uepic_chip"]
      t: |-
        Drawers first (Keep Exact 16): UEV circuits (12 per controller), UHV field generators, UHV pumps, UHV panels, UEPIC chips (64 per slot). Drums: flamewake solvent, utopian akreyrium, liquid helium, soldering alloy, PEDOT:PSS, perfluoroelastomer rubber, trinaquadalloy, tritanium.
    - i: ["kubejs:heart_of_the_flame", "kubejs:husk_brick"]
      t: Heart of the Flame first (5 min, 3 932 160 EU/t). Station research of the Husk of the Flame must be done; the Hell Forge recipe needs the HEART scanned in turn.
    - i: ["start_core:hellforge", "gtceu:calamatium_frame"]
      t: |-
        Hell Forge, then the Chiller: each is a 12 circuit, 32 panel, 32 field generator, 24 pump recipe; do them one after the other because each takes a full set of UHV parts.
    - i: ["gtceu:mega_abs", "gtceu:super_compact_heat_chamber"]
      t: Mega ABS and the Super Compact Heat Chamber next; both need only parts you already stock (UHV field generators, arms, regulators, chips) plus the research of their UHV predecessors.
    - i: ["gtceu:cryostate_quantum_chiller", "kubejs:subzero_casing"]
      t: |-
        Build the big ones in the order: Chiller (the alloys cannot be frozen without it), Hell Forge, then the rest. Each has hundreds of casings; the casing recipes give 2 per craft, so one assembler per casing type is enough.
    - i: ["functionalstorage:oak_1", "start_core:hellforge"]
      t: |-
        Hatches: UEV energy hatches from uev_hatches, UHV item and fluid hatches (there are no UEV ones). Minimum hatch counts per multi: Unverified, read the multiblock card.
---
# UEV multiblock controllers: Heart of the Flame → Hell Forge, Cryostate Quantum Chiller, Mega ABS, Super Compact Heat Chamber (all Assembly Line + station research)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_multis` · **Tags:** Infinite source

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [Hell Forge, Chiller and UEV alloys](../../plan/p18.md#uevforge)

**Tips:** 6

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 5 min · 3 932 160 EU/t (research husk of the flame)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Heart of the Flame: husk brick · 2 decaying core · 6 dense ancient netherite plate · 24 pure netherite screw · 500 000 mB flamewake solvent (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Heart of the Flame: husk brick · 2 decaying core · 6 dense ancient netherite plate · 24 pure netherite screw · 500 000 mB flamewake solvent</span><span class="gt-sub"><span>Husk brick</span><span>Decaying core</span><span>Ancient netherite plate</span><span>Pure netherite screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">300 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Heart of the Flame (kubejs:heart_of_the_flame) - 1 / 300 s"><img class="gt-ico" src="../../assets/icons/kubejs__heart_of_the_flame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Heart Of The Flame</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 140 s / 90 s · 7 864 320 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Heart of the Flame (kubejs:heart_of_the_flame) - research"><img class="gt-ico" src="../../assets/icons/kubejs__heart_of_the_flame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Heart Of The Flame</span><b class="gt-q">research</b></span><span class="gt-slot gt-group" title="Hell Forge: calamatium frame · 12 UEV circuit · 32 UHV high strength panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 calamatium rotor · 32 isovol screw · 240 B flamewake solvent · 60 B utopian akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Hell Forge: calamatium frame · 12 UEV circuit · 32 UHV high strength panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 calamatium rotor · 32 isovol screw · 240 B flamewake solvent · 60 B utopian akreyrium</span><span class="gt-sub"><span>Calamatium frame</span><span>UHV field generator</span><span>UHV pump</span><span>Neutronium huge pipe</span><span>Calamatium rotor</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Cryostate Chiller: isovol frame · 12 UEV circuit · 32 UHV panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 isovol rotor · 32 calamatium screw · 1000 B liquid helium · 60 B akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Cryostate Chiller: isovol frame · 12 UEV circuit · 32 UHV panel · 8 neutronium huge pipe · 32 UHV field gen · 24 UHV pump · 4 isovol rotor · 32 calamatium screw · 1000 B liquid helium · 60 B akreyrium</span><span class="gt-sub"><span>Isovol frame</span><span>UHV field generator</span><span>Isovol rotor</span><span>Calamatium screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">140 s · 90 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Hell Forge (start_core:hellforge) - 1 / 140 s"><img class="gt-ico" src="../../assets/icons/start_core__hellforge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hellforge</span><span class="gt-note">Hell Forge</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Cryostate Quantum Chiller (gtceu:cryostate_quantum_chiller) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__cryostate_quantum_chiller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cryostate Quantum Chiller</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 90 s · 3 932 160 EU/t · and 200 s · 983 040 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Mega ABS: UHV alloy smelter · 12 UEV circuit · 8 UHV field gen · 6 dense ancient netherite plate · 4 UHV arm · 12 UHV fluid regulator · 12 RTA neutronate quad wire · 4 calamatium rotor · 4 cerium tritelluride spring · 8 calamatium screw (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Mega ABS: UHV alloy smelter · 12 UEV circuit · 8 UHV field gen · 6 dense ancient netherite plate · 4 UHV arm · 12 UHV fluid regulator · 12 RTA neutronate quad wire · 4 calamatium rotor · 4 cerium tritelluride spring · 8 calamatium screw</span><span class="gt-sub"><span>UHV alloy smelter</span><span>UHV robot arm</span><span>UHV fluid regulator</span><span>Cerium tritelluride spring</span></span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Super Compact Heat Chamber: heat chamber · 4 UEV circuit · double prismalium plate · double ancient netherite plate · UHV field gen · 160 UEPIC chip · 48 stellarium wire · 6912 mB trinaquadalloy · 1728 mB tritanium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Super Compact Heat Chamber: heat chamber · 4 UEV circuit · double prismalium plate · double ancient netherite plate · UHV field gen · 160 UEPIC chip · 48 stellarium wire · 6912 mB trinaquadalloy · 1728 mB tritanium</span><span class="gt-sub"><span>Heat chamber</span><span>UEPIC chip</span><span>Stellarium wire</span><span>Prismalium plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">90 s · 200 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mega ABS (gtceu:mega_abs) - 1 / 90 s"><img class="gt-ico" src="../../assets/icons/gtceu__mega_abs.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mega ABS</span><b class="gt-q">1</b></span><span class="gt-slot gt-outp" title="Super Compact Heat Chamber (gtceu:super_compact_heat_chamber) - 1 / 200 s"><img class="gt-ico" src="../../assets/icons/gtceu__super_compact_heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Super Compact Heat Chamber</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 5 min · 3 932 160 EU/t (research husk of the flame)](#m-a1) → [Assembly Line · 140 s / 90 s · 7 864 320 EU/t](#m-a2)
- [Assembly Line · 90 s · 3 932 160 EU/t · and 200 s · 983 040 EU/t](#m-a3)

## How to build

1. Drawers first (Keep Exact 16): UEV circuits (12 per controller), UHV field generators, UHV pumps, UHV panels, UEPIC chips (64 per slot). Drums: flamewake solvent, utopian akreyrium, liquid helium, soldering alloy, PEDOT:PSS, perfluoroelastomer rubber, trinaquadalloy, tritanium. — `functionalstorage:oak_1`, `kubejs:uev_universal_circuit`, `kubejs:uepic_chip`
2. Heart of the Flame first (5 min, 3 932 160 EU/t). Station research of the Husk of the Flame must be done; the Hell Forge recipe needs the HEART scanned in turn. — `kubejs:heart_of_the_flame`, `kubejs:husk_brick`
3. Hell Forge, then the Chiller: each is a 12 circuit, 32 panel, 32 field generator, 24 pump recipe; do them one after the other because each takes a full set of UHV parts. — `start_core:hellforge`, `gtceu:calamatium_frame`
4. Mega ABS and the Super Compact Heat Chamber next; both need only parts you already stock (UHV field generators, arms, regulators, chips) plus the research of their UHV predecessors. — `gtceu:mega_abs`, `gtceu:super_compact_heat_chamber`
5. Build the big ones in the order: Chiller (the alloys cannot be frozen without it), Hell Forge, then the rest. Each has hundreds of casings; the casing recipes give 2 per craft, so one assembler per casing type is enough. — `gtceu:cryostate_quantum_chiller`, `kubejs:subzero_casing`
6. Hatches: UEV energy hatches from uev\_hatches, UHV item and fluid hatches (there are no UEV ones). Minimum hatch counts per multi: Unverified, read the multiblock card. — `functionalstorage:oak_1`, `start_core:hellforge`

## Tips

- Source: kjs additions/multiblock\_recipes/nether\_multis.js. Heart of the Flame: 6000 ticks, VHA\[UEV\] = 3 932 160 EU/t, station research of the Husk of the Flame (192 CWU/t). Hell Forge: 2800 ticks (140 s), VA\[UEV\] = 7 864 320 EU/t, research Heart of the Flame (VA\[UHV\], 192 CWU/t). Cryostate Quantum Chiller: 1800 ticks, VA\[UEV\], research Mega Vacuum Freezer (192 CWU/t). Mega ABS: 1800 ticks, VHA\[UEV\], research Super ABS (160 CWU/t); fluids 13 824 mB soldering alloy, 10 368 mB PEDOT:PSS, 12 000 mB utopian akreyrium, 8640 mB perfluoroelastomer rubber. Super Compact Heat Chamber: 4000 ticks (200 s), VHA\[UHV\] = 983 040 EU/t, research Super Pressure Heat Chamber (160 CWU/t); 160 UEPIC chips = 80 wafers (uev\_chips).
- Multiblock sizes (from the pack patterns): Cryostate Quantum Chiller about 2800 blocks: 776 reinforced cryostone casings, 640 void frames, 535 enriched naquadah pipe casings, 497 subzero casings (hatches go here), 216 firebox casings, 59 engine intake casings, 37 cleanroom glass, 20 heat vents. Mega ABS about 2100 blocks: 918 extreme temperature smelting casings (at least 898 must stay casings, rest hatches), 312 enriched estalt frames, 213 pipe casings, 147 coil blocks, 129 intake casings, 124 firebox casings, 120 reinforced brimstone casings, 68 heat escape casings, 48 machine casings, 1 muffler. Super Compact Heat Chamber: 74 enderium casings, 34 zalloy coils, 32 neutronium frames, 32 high temperature smelting casings (at least 22 casings), 16 firebox, 8 intake, 1 muffler. The Hell Forge pattern is in the start\_core jar: Unverified counts.
- Casing recipes (casings.js): reinforced cryostone casing = 16 cryostone compressed; reinforced brimstone casing = 16 brimstone compressed; subzero casing = assembler circuit 6, 4 aluminium plate + 2 pure netherite plate + 1 void frame → 2 casings; extreme temperature smelting casing = circuit 6, 4 calamatium plate + 2 astatium bioselex carbonite plate + 1 enriched estalt frame → 2 casings. Cryostone and brimstone come from exotic rock crushing (misc\_materials.js): 32 netherrack + 500 mB liquid helium (cryostone, circuit 2) or 500 mB blaze (brimstone, circuit 3) with a seed block and lava not consumed, 300 ticks, VHA\[LuV\] → 2 stones.
- Recipe oddity worth noting: three of the four controllers eat 12 UEV circuits each (Mega ABS 12, Hell Forge 12, Chiller 12; heat chamber 4): 40 Runic Processor Mainframes for the four. The UEV circuit line (uev\_circuits) is the whole bottleneck of this era; the chips for the heat chamber (160) are the second.
- Sub-steps people skip: (1) research chain: Husk of the Flame → Heart of the Flame → Hell Forge, and Super ABS, Mega Vacuum Freezer and Super Pressure Heat Chamber must exist first (UV and UHV pages); (2) utopian akreyrium (60 000 mB for forge or chiller, 12 000 for ABS) is the UHV akreyrium line output; (3) liquid helium 1 000 000 mB for the Chiller needs a dedicated tank and pipe; (4) the multis are huge: plan chunk loading and a flat build site before you start the casings.
- Access to the End (verified): travel is cancelled without the access\_end stage (dimensional\_stages.js), granted by clicking the Milky Way Stargate with the End coordinate crystal. The End crystal is made in a Dimensional Finder run in the NETHER: 1 coordinate crystal + 64 end stone + 16 UHV sensors + 7200 mB echo fluid, 384 CWU/t (1 843 200 CWU), EUtVA(UIV) = 31 457 280 EU/t, 5 % chance; a UEV 4A hatch (33 554 432) covers it and a UEV 16A hatch gives margin, which is why the End comes right after the UEV 16A hatches. Crystal chain: Abydos crystal (Overworld, VHA\[UV\], 16 ZPM sensors) -&gt; Nether crystal (run in Abydos, VHA\[UEV\], 16 UV sensors + 50 000 mB lava, 192 CWU/t) -&gt; End crystal; every crystal can be duplicated in a scanner. Unverified: Husk of the Flame, decaying core and husk brick recipes and the Hell Forge pattern.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uhv_input_bus` | 4 |
| `gtceu:uhv_input_hatch` | 4 |
| `functionalstorage:oak_1` | 20 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `start_core:hellforge`, `gtceu:cryostate_quantum_chiller`, `gtceu:mega_abs`, `gtceu:super_compact_heat_chamber`, `kubejs:heart_of_the_flame`
