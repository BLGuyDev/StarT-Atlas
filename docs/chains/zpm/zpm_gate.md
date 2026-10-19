---
kind: chain
id: zpm_gate
order: 1520
data:
  t: |-
    Classic Stargate: runes (RCAS) + gate parts (Component Part Assembly) + activated rods → ring, chevron, base blocks (Stargate Component Assembly) → Create mechanical crafting
  inf: true
  "n":
    - - ru
      - Enscription plate + 64 IGP dust + 576 mB nether star concentrate + lens (yellow / ruby / sapphire)
      - g
      - functionalstorage:oak_1
      - - [Enscription plate, "kubejs:csg_enscription_plate"]
        - [Indium gallium phosphide dust, "gtceu:indium_gallium_phosphide_dust"]
        - [Sapphire lens, "gtceu:sapphire_lens"]
    - [a0, "Runic Circuitry Assembling Station · 30 s · VHA[ZPM]", m, "gtceu:runic_circuitry_assembling_station"]
    - [rn, "Proto solarus, energized and lunarus rune", x, "kubejs:proto_solarus_rune"]
    - - cp
      - Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each)
      - g
      - functionalstorage:oak_1
      - - [Reinforced plating, "kubejs:csg_reinforced_plating"]
        - [Field stabiliser, "kubejs:csg_field_stabiliser"]
        - [Stellar access point, "kubejs:csg_stellar_access_point"]
        - [Dimensional supercomputer, "kubejs:csg_dimensional_supercomputer"]
        - [Chevron part, "kubejs:csg_chevron"]
    - [ro, "16 / 10 / 10 activated stargate rods", i, "kubejs:activated_stargate_rod"]
    - - a1
      - Stargate Component Assembly · ring · 60 s · 1728 mB naquadria · prismalium frame
      - m
      - gtceu:stargate_component_assembly
    - [rg, "Classic Stargate Ring Block · 24 needed", x, "sgjourney:classic_stargate_ring_block"]
    - - a2
      - Stargate Component Assembly · chevron · 60 s · 1152 mB naquadria
      - m
      - gtceu:stargate_component_assembly
    - [ch, "Classic Chevron Block · 9", x, "sgjourney:classic_stargate_chevron_block"]
    - [a3, "Stargate Component Assembly · base · 60 s · 1152 mB naquadria", m, "gtceu:stargate_component_assembly"]
    - [bs, "Classic Base Block · 1", x, "sgjourney:classic_stargate_base_block"]
    - [gt, "Create mechanical crafting 7 x 7 · 14 ring + 9 chevron + 1 base", o, "sgjourney:classic_stargate"]
  e:
    - [ru, a0, "1"]
    - [a0, rn, "1 / 30 s"]
    - [rn, a1, "6"]
    - [cp, a1, "3 plating"]
    - [ro, a1, "16"]
    - [a1, rg, "1 / 60 s"]
    - [rg, a2, "1"]
    - [rn, a2, "5"]
    - [cp, a2, parts]
    - [ro, a2, "10"]
    - [a2, ch, "1 / 60 s"]
    - [rg, a3, "1"]
    - [rn, a3, "16"]
    - [cp, a3, parts]
    - [ro, a3, "10"]
    - [a3, bs, "1 / 60 s"]
    - [rg, gt, "14"]
    - [ch, gt, "9"]
    - [bs, gt, "1"]
  tips:
    - |-
      Recipes (kjs systems/gate_based/csg.js; all EUtVHA(UV) in the Stargate Component Assembly, 1200 ticks, layered recipes). Ring block: layer 1 = prismalium frame + 16 activated stargate rods; layer 2 = 2 proto solarus runes + 1 reinforced plating; layer 3 = 2 proto lunarus runes + 1 plating; layer 4 = 2 proto energized runes + 1 plating; 1728 mB naquadria. Chevron block: layer 1 = a RING BLOCK + a chevron part + 6 activated rods; layer 2 = field stabiliser + plating + 2 rods; layer 3 = solarus + 3 energized + lunarus runes; layer 4 = field stabiliser + plating + 2 rods; 1152 mB naquadria. Base block: layer 1 = a RING BLOCK + the dimensional supercomputer + 6 rods; layer 2 = stellar access point + plating + 2 rods; layer 3 = 6 solarus + 4 energized + 6 lunarus runes; layer 4 = access point + plating + 2 rods; 1152 mB naquadria. Final gate: Create mechanical crafting, 7 x 7 pattern with 14 ring, 9 chevron and 1 base block (pack recipe start:shaped/csg).
    - |-
      Tier gate (verified, csg.js): the CSG is the step from ZPM to UV. The pieces made in the Component Part Assembly (plating, stabiliser, modulator, access point, chevron part, dialer), the enscription plates and the DHD run at VHA[ZPM] (61 440 EU/t), but the stargate rod base, raw rod and activated rod (zpm_rods) and the ring, chevron and base blocks in the Stargate Component Assembly are all EUtVHA(UV) = 245 760 EU/t, which needs a UV energy hatch and UV circuits. A run that only has ZPM hatches cannot finish the three block types. Final assembly is the Create mechanical crafting recipe start:shaped/csg.
    - |-
      Derived totals for the whole gate: chevron and base blocks each consume a ring block, so 14 + 9 + 1 = 24 ring blocks. Activated rods: 24 x 16 + 9 x 10 + 1 x 10 = 484. Reinforced plating: 3 per ring x 24 + 2 per chevron x 9 + 2 for the base = 92. Runes: 6 per ring x 24 + 5 per chevron x 9 + 16 for the base = 205 plus 38 for the DHD (12 solarus + 14 energized + 12 lunarus). So this is a project of hundreds of rods and runes: check each chain for throughput before you commit. These are the derived counts from the recipe list, not a number the pack states.
    - |-
      Parts (kjs gate_based/csg.js ‘researchBuilder’ recipes; each is a Component Part Assembly craft of 6000 ticks, 24 CWU/t station data, VHA[ZPM], or Assembly Line for the two big ones): reinforced plating = dense trinaquadalloy plate + ZPM piston + dense naquadah alloy plate + 1 UV circuit + dense enriched naquadah plate + 8 YBCO single cable + 288 mB naquadria + 864 mB ITLC; field stabiliser = 2 dense enriched naquadah plates + 4 ZPM field generators + energy modulator + 16 fine lumium + 16 fine twinite + 16 fine signalum wire + 1296 mB ITLC; energy modulator = trinaquadalloy frame + ZPM emitter + 4 prismalium foil + energy module + 4 advanced neutron reflector + 4 naquadah alloy foil + 250 B PCB coolant + 864 mB ITLC; stellar access point = double naquadah plate + computational matrix + 4 prismalium double wire + 3 foil reams (polycarbonate, PPS, PVC) + 864 mB ITLC + 1296 mB PBI; chevron part = 2 long prismalium rods + exquisite naquadic netherite gem + field stabiliser + computational matrix + 4 ZPM sensors + 64 fine borosilicate glass wire + 864 mB ITLC; dimensional supercomputer (Assembly Line) = 3 trinaquadalloy frames + 8 computational matrices + quantum core + 64 UV circuits + 8 prismalium foil reams + 24 small enriched naquadah pipes + 36 silicone rings + 48 tiny polycarbonate pipes + 3888 mB PBI + 2592 mB ITLC + 576 mB naquadria; quantum core (Assembly Line) = weapon-grade naquadah frame + 4 energy modulators + 16 quantum stars + 2 ZPM field generators + 6 trinium springs + 4 ZPM pumps + fine prismalium wire + 16 osthendah foil + 8 naquadah alloy plates + 4 osmiridium bolts + 864 mB nether star concentrate + 1296 mB PBI.
    - |-
      Runes: Runic Circuitry Assembling Station (zpm_multis2), recipes (kjs gate_based/runes.js): proto solarus rune = enscription plate + 64 indium gallium phosphide dust + 576 mB nether star concentrate with a NON-consumed yellow glass lens; energized = ruby lens; lunarus = sapphire lens; each 600 ticks at VHA[ZPM]. The csg dpu chip (for the computational matrix) = enscription chip + 8 IGP dust + 72 mB concentrate + nether star lens. Enscription plate (Large Chemical Reactor, cleanroom, 4000 ticks, VHA[ZPM]) = 1 naquadah wafer + 48 aerogel foil + 1 UV circuit + 1152 mB europium + 432 mB naquadria; cut into 2 chips with 432 mB concentrate (cutter, 3000 ticks). So every rune is a plate + 64 dust + 576 mB concentrate: 205 runes = 205 plates, 13 120 IGP dust and 118 B of concentrate.
    - |-
      DHD (assembler, 6000 ticks, VHA[ZPM]) = atomic casing + stellar dialer + 12 dragonsteel foil + 12 solarus + 14 energized + 12 lunarus runes + 1296 mB ITLC; stellar dialer = dense enriched naquadah plate + computer monitor cover + computational matrix + dragonsteel bolt. Crystal interface (Assembly Line, research: the ZPM 64A converter) = trinaquadalloy frame + 16 prismalium hex wire + 6 reinforced plating + stellar access point + energy modulator + 128 fine dragonsteel wire; 3888 mB ITLC + 2592 mB polycarbonate. Display: right-click the base block with the DHD and crystal interface placed (quest ‘Stargate Forming Help’). If the gate has no power, hit the bottom block with a mallet (quest).
    - |-
      Sub-steps people skip: (1) the chevron and base consume ring blocks, so the first 10 ring blocks are not gate rings; (2) the computational matrix (circuit assembler, cleanroom, VHA[ZPM], 6000 ticks: elite board + 16 fine trinaquadalloy wire + 12 csg dpu + 6 advanced SoC + 8 prismalium bolts + 48 UHPIC chips + 15 552 mB ITLC) is needed by three parts; (3) polycarbonate and aerogel are material lines of their own (gate_lines aerogels.js); (4) coordinates: to dial Abydos, you need the crystal from the Dimensional Finder (zpm_multis2).
    - |-
      Unverified: the energy module, aerogel, polycarbonate, advanced SoC and lumium/twinite wire sources, the runes’ effect in the finished gate, the exact CWU needs of the parts, and whether the Create mechanical crafter needs a 7 x 7 array (the recipe pattern is 7 wide and 7 tall).
  b:
    - ["gtceu:stargate_component_assembly", 1]
    - ["gtceu:runic_circuitry_assembling_station", 1]
    - ["gtceu:component_part_assembly", 1]
    - ["gtceu:large_rotor_machine", 1]
    - ["gtceu:heat_chamber", 1]
    - ["gtceu:dimensional_finder", 1]
    - ["sgjourney:classic_dhd", 1]
    - ["sgjourney:crystal_interface", 1]
    - ["create:mechanical_crafter", 49]
    - ["functionalstorage:oak_1", 30]
    - ["modularrouters:modular_router", 16]
    - ["gtceu:lv_robot_arm", 16]
    - ["gtceu:item_filter", 16]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - kubejs:csg_enscription_plate
        - gtceu:indium_gallium_phosphide_dust
        - gtceu:nether_star_concentrate_bucket
      t: |-
        Drawers first, one per input: enscription plates, IGP dust (Keep Exact 128), lenses, activated rods (Keep Exact 64), reinforced plating, field stabilisers, access points, chevron parts, runes (3 drawers), naquadria and concentrate drums. Every machine behind its own router with Item Filters and Keep Exact arms; the Stargate Component Assembly gets layered buses in order.
    - i: ["gtceu:runic_circuitry_assembling_station", "kubejs:proto_solarus_rune", "gtceu:sapphire_lens"]
      t: |-
        Runes: the RCAS with the lens in a ghost slot, enscription plate + 64 IGP dust + 576 mB concentrate → rune in 30 s. One RCAS recipe at a time, so three lens switches: use three separate input buses with filters or three machines.
    - i: ["gtceu:component_part_assembly", "kubejs:csg_reinforced_plating", "kubejs:csg_field_stabiliser"]
      t: |-
        Parts: Component Part Assembly for plating, stabiliser, modulator, access point, chevron part and dialer (5 min each), the Assembly Line for the quantum core and the dimensional supercomputer. One data orb of research per part type (24 CWU/t parts use orbs, zpm_data).
    - i:
        - gtceu:stargate_component_assembly
        - sgjourney:classic_stargate_ring_block
        - kubejs:activated_stargate_rod
      t: |-
        Ring blocks first (24): the Stargate Component Assembly, layer by layer: frame + 16 rods, then 2 + 2 + 2 runes with a plating each; 1728 mB naquadria; 1200 ticks. Keep 10 aside for chevrons and the base.
    - i:
        - gtceu:stargate_component_assembly
        - sgjourney:classic_stargate_chevron_block
        - sgjourney:classic_stargate_base_block
      t: |-
        Chevrons (9) and the base (1): same machine, ring block in layer 1, then the extras listed above; 1152 mB naquadria each.
    - i: ["create:mechanical_crafter", "sgjourney:classic_stargate"]
      t: |-
        Final: a 7 x 7 mechanical crafter wall (the recipe pattern ‘ CRCRC / RR   RR / C     C / R     R / R     R / CR   RC /  RCBCR ’), put the 14 ring, 9 chevron and base blocks in, power it. Then place the DHD and the crystal interface (right-click the base block).
    - i: ["sgjourney:classic_dhd", "sgjourney:crystal_interface", "kubejs:abydos_coordinate_crystal"]
      t: |-
        Easy to miss: the gate does nothing without a coordinate crystal (zpm_multis2) and a crystal interface; also the power: dialing needs an immense amount of energy (quest), so a Power Substation or big batteries next to the gate.
---
# Classic Stargate: runes (RCAS) + gate parts (Component Part Assembly) + activated rods → ring, chevron, base blocks (Stargate Component Assembly) → Create mechanical crafting

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_gate` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Era multiblocks and the Classic Stargate](../../plan/p13.md#zpmmultis)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-a0">
<div class="gt-head"><span class="gt-mname">Runic Circuitry Assembling Station · 30 s · VHA[ZPM]</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Enscription plate + 64 IGP dust + 576 mB nether star concentrate + lens (yellow / ruby / sapphire) (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Enscription plate + 64 IGP dust + 576 mB nether star concentrate + lens (yellow / ruby / sapphire)</span><span class="gt-sub"><span>Enscription plate</span><span>Indium gallium phosphide dust</span><span>Sapphire lens</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__runic_circuitry_assembling_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Proto solarus, energized and lunarus rune (kubejs:proto_solarus_rune) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/kubejs__proto_solarus_rune.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Proto Solarus Rune</span><span class="gt-note">Proto solarus, energized and lunarus rune</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:runic_circuitry_assembling_station</code></div>
</div>
<div class="gt-panel t-mod" id="m-a1">
<div class="gt-head"><span class="gt-mname">Stargate Component Assembly · ring · 60 s · 1728 mB naquadria · prismalium frame</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Proto solarus, energized and lunarus rune (kubejs:proto_solarus_rune) - 6"><img class="gt-ico" src="../../assets/icons/kubejs__proto_solarus_rune.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Proto Solarus Rune</span><span class="gt-note">Proto solarus, energized and lunarus rune</span><b class="gt-q">6</b></span><span class="gt-slot gt-group" title="Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each) (functionalstorage:oak_1) - 3 plating"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each)</span><span class="gt-sub"><span>Reinforced plating</span><span>Field stabiliser</span><span>Stellar access point</span><span>Dimensional supercomputer</span><span>Chevron part</span></span><b class="gt-q">3 plating</b></span><span class="gt-slot" title="16 / 10 / 10 activated stargate rods (kubejs:activated_stargate_rod) - 16"><img class="gt-ico" src="../../assets/icons/kubejs__activated_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Activated Stargate Rod</span><span class="gt-note">16 / 10 / 10 activated stargate rods</span><b class="gt-q">16</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stargate_component_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Classic Stargate Ring Block · 24 needed (sgjourney:classic_stargate_ring_block) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/sgjourney__classic_stargate_ring_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Classic Stargate Ring Block</span><span class="gt-note">Classic Stargate Ring Block · 24 needed</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:stargate_component_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a2">
<div class="gt-head"><span class="gt-mname">Stargate Component Assembly · chevron · 60 s · 1152 mB naquadria</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Classic Stargate Ring Block · 24 needed (sgjourney:classic_stargate_ring_block) - 1"><img class="gt-ico" src="../../assets/icons/sgjourney__classic_stargate_ring_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Classic Stargate Ring Block</span><span class="gt-note">Classic Stargate Ring Block · 24 needed</span><b class="gt-q">1</b></span><span class="gt-slot" title="Proto solarus, energized and lunarus rune (kubejs:proto_solarus_rune) - 5"><img class="gt-ico" src="../../assets/icons/kubejs__proto_solarus_rune.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Proto Solarus Rune</span><span class="gt-note">Proto solarus, energized and lunarus rune</span><b class="gt-q">5</b></span><span class="gt-slot gt-group" title="Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each) (functionalstorage:oak_1) - parts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each)</span><span class="gt-sub"><span>Reinforced plating</span><span>Field stabiliser</span><span>Stellar access point</span><span>Dimensional supercomputer</span><span>Chevron part</span></span><b class="gt-q">parts</b></span><span class="gt-slot" title="16 / 10 / 10 activated stargate rods (kubejs:activated_stargate_rod) - 10"><img class="gt-ico" src="../../assets/icons/kubejs__activated_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Activated Stargate Rod</span><span class="gt-note">16 / 10 / 10 activated stargate rods</span><b class="gt-q">10</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stargate_component_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Classic Chevron Block · 9 (sgjourney:classic_stargate_chevron_block) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/sgjourney__classic_stargate_chevron_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Classic Stargate Chevron Block</span><span class="gt-note">Classic Chevron Block · 9</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:stargate_component_assembly</code></div>
</div>
<div class="gt-panel t-mod" id="m-a3">
<div class="gt-head"><span class="gt-mname">Stargate Component Assembly · base · 60 s · 1152 mB naquadria</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Classic Stargate Ring Block · 24 needed (sgjourney:classic_stargate_ring_block) - 1"><img class="gt-ico" src="../../assets/icons/sgjourney__classic_stargate_ring_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Classic Stargate Ring Block</span><span class="gt-note">Classic Stargate Ring Block · 24 needed</span><b class="gt-q">1</b></span><span class="gt-slot" title="Proto solarus, energized and lunarus rune (kubejs:proto_solarus_rune) - 16"><img class="gt-ico" src="../../assets/icons/kubejs__proto_solarus_rune.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Proto Solarus Rune</span><span class="gt-note">Proto solarus, energized and lunarus rune</span><b class="gt-q">16</b></span><span class="gt-slot gt-group" title="Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each) (functionalstorage:oak_1) - parts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Reinforced plating · field stabiliser · stellar access point · dimensional supercomputer · chevron part (Component Part Assembly / Assembly Line, 5 min each)</span><span class="gt-sub"><span>Reinforced plating</span><span>Field stabiliser</span><span>Stellar access point</span><span>Dimensional supercomputer</span><span>Chevron part</span></span><b class="gt-q">parts</b></span><span class="gt-slot" title="16 / 10 / 10 activated stargate rods (kubejs:activated_stargate_rod) - 10"><img class="gt-ico" src="../../assets/icons/kubejs__activated_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Activated Stargate Rod</span><span class="gt-note">16 / 10 / 10 activated stargate rods</span><b class="gt-q">10</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stargate_component_assembly.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Classic Base Block · 1 (sgjourney:classic_stargate_base_block) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/sgjourney__classic_stargate_base_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Classic Stargate Base Block</span><span class="gt-note">Classic Base Block · 1</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:stargate_component_assembly</code></div>
</div>
</div>

## Flow

- [Runic Circuitry Assembling Station · 30 s · VHA\[ZPM\]](#m-a0) → [Stargate Component Assembly · ring · 60 s · 1728 mB naquadria · prismalium frame](#m-a1) → [Stargate Component Assembly · chevron · 60 s · 1152 mB naquadria](#m-a2) (also Runic Circuitry Assembling Station · 30 s · VHA\[ZPM\] → [Stargate Component Assembly · chevron · 60 s · 1152 mB naquadria](#m-a2), Runic Circuitry Assembling Station · 30 s · VHA\[ZPM\] → [Stargate Component Assembly · base · 60 s · 1152 mB naquadria](#m-a3), Stargate Component Assembly · ring · 60 s · 1728 mB naquadria · prismalium frame → [Stargate Component Assembly · base · 60 s · 1152 mB naquadria](#m-a3))
- [Stargate Component Assembly · base · 60 s · 1152 mB naquadria](#m-a3)

### Direct steps

- Classic Stargate Ring Block · 24 needed → Create mechanical crafting 7 x 7 · 14 ring + 9 chevron + 1 base (14)
- Classic Chevron Block · 9 → Create mechanical crafting 7 x 7 · 14 ring + 9 chevron + 1 base (9)
- Classic Base Block · 1 → Create mechanical crafting 7 x 7 · 14 ring + 9 chevron + 1 base (1)

## How to build

1. Drawers first, one per input: enscription plates, IGP dust (Keep Exact 128), lenses, activated rods (Keep Exact 64), reinforced plating, field stabilisers, access points, chevron parts, runes (3 drawers), naquadria and concentrate drums. Every machine behind its own router with Item Filters and Keep Exact arms; the Stargate Component Assembly gets layered buses in order. — `functionalstorage:oak_1`, `kubejs:csg_enscription_plate`, `gtceu:indium_gallium_phosphide_dust`, `gtceu:nether_star_concentrate_bucket`
2. Runes: the RCAS with the lens in a ghost slot, enscription plate + 64 IGP dust + 576 mB concentrate → rune in 30 s. One RCAS recipe at a time, so three lens switches: use three separate input buses with filters or three machines. — `gtceu:runic_circuitry_assembling_station`, `kubejs:proto_solarus_rune`, `gtceu:sapphire_lens`
3. Parts: Component Part Assembly for plating, stabiliser, modulator, access point, chevron part and dialer (5 min each), the Assembly Line for the quantum core and the dimensional supercomputer. One data orb of research per part type (24 CWU/t parts use orbs, zpm\_data). — `gtceu:component_part_assembly`, `kubejs:csg_reinforced_plating`, `kubejs:csg_field_stabiliser`
4. Ring blocks first (24): the Stargate Component Assembly, layer by layer: frame + 16 rods, then 2 + 2 + 2 runes with a plating each; 1728 mB naquadria; 1200 ticks. Keep 10 aside for chevrons and the base. — `gtceu:stargate_component_assembly`, `sgjourney:classic_stargate_ring_block`, `kubejs:activated_stargate_rod`
5. Chevrons (9) and the base (1): same machine, ring block in layer 1, then the extras listed above; 1152 mB naquadria each. — `gtceu:stargate_component_assembly`, `sgjourney:classic_stargate_chevron_block`, `sgjourney:classic_stargate_base_block`
6. Final: a 7 x 7 mechanical crafter wall (the recipe pattern ‘ CRCRC / RR   RR / C     C / R     R / R     R / CR   RC /  RCBCR ’), put the 14 ring, 9 chevron and base blocks in, power it. Then place the DHD and the crystal interface (right-click the base block). — `create:mechanical_crafter`, `sgjourney:classic_stargate`
7. Easy to miss: the gate does nothing without a coordinate crystal (zpm\_multis2) and a crystal interface; also the power: dialing needs an immense amount of energy (quest), so a Power Substation or big batteries next to the gate. — `sgjourney:classic_dhd`, `sgjourney:crystal_interface`, `kubejs:abydos_coordinate_crystal`

## Tips

- Recipes (kjs systems/gate\_based/csg.js; all EUtVHA(UV) in the Stargate Component Assembly, 1200 ticks, layered recipes). Ring block: layer 1 = prismalium frame + 16 activated stargate rods; layer 2 = 2 proto solarus runes + 1 reinforced plating; layer 3 = 2 proto lunarus runes + 1 plating; layer 4 = 2 proto energized runes + 1 plating; 1728 mB naquadria. Chevron block: layer 1 = a RING BLOCK + a chevron part + 6 activated rods; layer 2 = field stabiliser + plating + 2 rods; layer 3 = solarus + 3 energized + lunarus runes; layer 4 = field stabiliser + plating + 2 rods; 1152 mB naquadria. Base block: layer 1 = a RING BLOCK + the dimensional supercomputer + 6 rods; layer 2 = stellar access point + plating + 2 rods; layer 3 = 6 solarus + 4 energized + 6 lunarus runes; layer 4 = access point + plating + 2 rods; 1152 mB naquadria. Final gate: Create mechanical crafting, 7 x 7 pattern with 14 ring, 9 chevron and 1 base block (pack recipe start:shaped/csg).
- Tier gate (verified, csg.js): the CSG is the step from ZPM to UV. The pieces made in the Component Part Assembly (plating, stabiliser, modulator, access point, chevron part, dialer), the enscription plates and the DHD run at VHA\[ZPM\] (61 440 EU/t), but the stargate rod base, raw rod and activated rod (zpm\_rods) and the ring, chevron and base blocks in the Stargate Component Assembly are all EUtVHA(UV) = 245 760 EU/t, which needs a UV energy hatch and UV circuits. A run that only has ZPM hatches cannot finish the three block types. Final assembly is the Create mechanical crafting recipe start:shaped/csg.
- Derived totals for the whole gate: chevron and base blocks each consume a ring block, so 14 + 9 + 1 = 24 ring blocks. Activated rods: 24 x 16 + 9 x 10 + 1 x 10 = 484. Reinforced plating: 3 per ring x 24 + 2 per chevron x 9 + 2 for the base = 92. Runes: 6 per ring x 24 + 5 per chevron x 9 + 16 for the base = 205 plus 38 for the DHD (12 solarus + 14 energized + 12 lunarus). So this is a project of hundreds of rods and runes: check each chain for throughput before you commit. These are the derived counts from the recipe list, not a number the pack states.
- Parts (kjs gate\_based/csg.js ‘researchBuilder’ recipes; each is a Component Part Assembly craft of 6000 ticks, 24 CWU/t station data, VHA\[ZPM\], or Assembly Line for the two big ones): reinforced plating = dense trinaquadalloy plate + ZPM piston + dense naquadah alloy plate + 1 UV circuit + dense enriched naquadah plate + 8 YBCO single cable + 288 mB naquadria + 864 mB ITLC; field stabiliser = 2 dense enriched naquadah plates + 4 ZPM field generators + energy modulator + 16 fine lumium + 16 fine twinite + 16 fine signalum wire + 1296 mB ITLC; energy modulator = trinaquadalloy frame + ZPM emitter + 4 prismalium foil + energy module + 4 advanced neutron reflector + 4 naquadah alloy foil + 250 B PCB coolant + 864 mB ITLC; stellar access point = double naquadah plate + computational matrix + 4 prismalium double wire + 3 foil reams (polycarbonate, PPS, PVC) + 864 mB ITLC + 1296 mB PBI; chevron part = 2 long prismalium rods + exquisite naquadic netherite gem + field stabiliser + computational matrix + 4 ZPM sensors + 64 fine borosilicate glass wire + 864 mB ITLC; dimensional supercomputer (Assembly Line) = 3 trinaquadalloy frames + 8 computational matrices + quantum core + 64 UV circuits + 8 prismalium foil reams + 24 small enriched naquadah pipes + 36 silicone rings + 48 tiny polycarbonate pipes + 3888 mB PBI + 2592 mB ITLC + 576 mB naquadria; quantum core (Assembly Line) = weapon-grade naquadah frame + 4 energy modulators + 16 quantum stars + 2 ZPM field generators + 6 trinium springs + 4 ZPM pumps + fine prismalium wire + 16 osthendah foil + 8 naquadah alloy plates + 4 osmiridium bolts + 864 mB nether star concentrate + 1296 mB PBI.
- Runes: Runic Circuitry Assembling Station (zpm\_multis2), recipes (kjs gate\_based/runes.js): proto solarus rune = enscription plate + 64 indium gallium phosphide dust + 576 mB nether star concentrate with a NON-consumed yellow glass lens; energized = ruby lens; lunarus = sapphire lens; each 600 ticks at VHA\[ZPM\]. The csg dpu chip (for the computational matrix) = enscription chip + 8 IGP dust + 72 mB concentrate + nether star lens. Enscription plate (Large Chemical Reactor, cleanroom, 4000 ticks, VHA\[ZPM\]) = 1 naquadah wafer + 48 aerogel foil + 1 UV circuit + 1152 mB europium + 432 mB naquadria; cut into 2 chips with 432 mB concentrate (cutter, 3000 ticks). So every rune is a plate + 64 dust + 576 mB concentrate: 205 runes = 205 plates, 13 120 IGP dust and 118 B of concentrate.
- DHD (assembler, 6000 ticks, VHA\[ZPM\]) = atomic casing + stellar dialer + 12 dragonsteel foil + 12 solarus + 14 energized + 12 lunarus runes + 1296 mB ITLC; stellar dialer = dense enriched naquadah plate + computer monitor cover + computational matrix + dragonsteel bolt. Crystal interface (Assembly Line, research: the ZPM 64A converter) = trinaquadalloy frame + 16 prismalium hex wire + 6 reinforced plating + stellar access point + energy modulator + 128 fine dragonsteel wire; 3888 mB ITLC + 2592 mB polycarbonate. Display: right-click the base block with the DHD and crystal interface placed (quest ‘Stargate Forming Help’). If the gate has no power, hit the bottom block with a mallet (quest).
- Sub-steps people skip: (1) the chevron and base consume ring blocks, so the first 10 ring blocks are not gate rings; (2) the computational matrix (circuit assembler, cleanroom, VHA\[ZPM\], 6000 ticks: elite board + 16 fine trinaquadalloy wire + 12 csg dpu + 6 advanced SoC + 8 prismalium bolts + 48 UHPIC chips + 15 552 mB ITLC) is needed by three parts; (3) polycarbonate and aerogel are material lines of their own (gate\_lines aerogels.js); (4) coordinates: to dial Abydos, you need the crystal from the Dimensional Finder (zpm\_multis2).
- **Unverified** the energy module, aerogel, polycarbonate, advanced SoC and lumium/twinite wire sources, the runes’ effect in the finished gate, the exact CWU needs of the parts, and whether the Create mechanical crafter needs a 7 x 7 array (the recipe pattern is 7 wide and 7 tall).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:stargate_component_assembly` | 1 |
| `gtceu:runic_circuitry_assembling_station` | 1 |
| `gtceu:component_part_assembly` | 1 |
| `gtceu:large_rotor_machine` | 1 |
| `gtceu:heat_chamber` | 1 |
| `gtceu:dimensional_finder` | 1 |
| `sgjourney:classic_dhd` | 1 |
| `sgjourney:crystal_interface` | 1 |
| `create:mechanical_crafter` | 49 |
| `functionalstorage:oak_1` | 30 |
| `modularrouters:modular_router` | 16 |
| `gtceu:lv_robot_arm` | 16 |
| `gtceu:item_filter` | 16 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Needs:** [Stargate rods: rod base → raw rod (Large Rotor Machine, foil reams, lubricant) → activated rod (Heat Chamber, nether star concentrate)](zpm_rods.md)
- **Main source for:** `sgjourney:classic_stargate_base_block`, `sgjourney:classic_stargate_ring_block`, `sgjourney:classic_stargate_chevron_block`, `sgjourney:classic_stargate`, `sgjourney:classic_dhd`, `sgjourney:crystal_interface`, `kubejs:proto_solarus_rune`, `kubejs:csg_reinforced_plating`
