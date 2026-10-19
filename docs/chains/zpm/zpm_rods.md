---
kind: chain
id: zpm_rods
order: 1510
data:
  t: |-
    Stargate rods: rod base → raw rod (Large Rotor Machine, foil reams, lubricant) → activated rod (Heat Chamber, nether star concentrate)
  inf: true
  "n":
    - - gb
      - |-
        2 prismalium ring · europium wire spool · trinaquadalloy wire spool · long pure netherite rod · 2592 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Prismalium ring, "gtceu:prismalium_ring"]
        - [Europium wire spool, "gtceu:europium_wire_spool"]
        - [Trinaquadalloy wire spool, "gtceu:trinaquadalloy_wire_spool"]
        - [Long pure netherite rod, "gtceu:long_pure_netherite_rod"]
    - [a1, "Large Rotor Machine · 3 layers · 40 s · UV power", m, "gtceu:large_rotor_machine"]
    - [rb, Stargate Rod Base, x, "kubejs:csg_stargate_rod_base"]
    - - gr
      - Rod base · 2 quantum star · 9 foil reams (naquadah alloy 2, weapon-grade naquadah 2, pure netherite 2, netherite, nether star, trinaquadalloy) · 75 B lubricant
      - g
      - functionalstorage:oak_1
      - - [Naquadah alloy foil ream, "gtceu:naquadah_alloy_foil_ream"]
        - [Weapon-grade naquadah foil ream, "gtceu:weapon_grade_naquadah_foil_ream"]
        - [Pure netherite foil ream, "gtceu:pure_netherite_foil_ream"]
        - [Nether star foil ream, "gtceu:nether_star_foil_ream"]
    - [a2, "Large Rotor Machine · 4 layers · 40 s · UV power", m, "gtceu:large_rotor_machine"]
    - [rr, Raw Stargate Rod, x, "kubejs:raw_stargate_rod"]
    - - nc
      - |-
        16 tiny nether star dust · 720 mB each energized blitz, blizz, basalz, blaze
      - g
      - functionalstorage:oak_1
      - [[Tiny nether star dust, "gtceu:tiny_nether_star_dust"], [Energized blaze, "gtceu:energized_blaze_bucket"]]
    - [h1, "Heat Chamber · 12.5 s · (1/3) VA[UV]", m, "gtceu:heat_chamber"]
    - [ns, "576 mB nether star concentrate", f, "gtceu:nether_star_concentrate_bucket"]
    - [a3, "Heat Chamber · 40 s · UV power · raw rod + 720 mB concentrate", m, "gtceu:heat_chamber"]
    - [ar, Activated Stargate Rod, o, "kubejs:activated_stargate_rod"]
  e:
    - [gb, a1, "1"]
    - [a1, rb, "1 / 40 s"]
    - [rb, a2, "1"]
    - [gr, a2, "1"]
    - [a2, rr, "1 / 40 s"]
    - [nc, h1, "1"]
    - [h1, ns, "576 mB / 12.5 s"]
    - [rr, a3, "1"]
    - [ns, a3, "720 mB"]
    - [a3, ar, "1 / 40 s"]
  tips:
    - |-
      Recipes (kjs systems/gate_based/csg.js and misc_materials.js, all with EUtVHA(UV), i.e. UV-power recipes: a LuV 16A hatch (quest: the 16A hatch ‘gives UV speeds’) or a UV hatch on the machine). Rod base (Large Rotor Machine, layered recipe, 800 ticks): layer 1 = 2 prismalium rings; layer 2 = 1 europium wire spool + 1296 mB naquadria; layer 3 = 1 trinaquadalloy wire spool + 1296 mB naquadria; plus 1 long pure netherite rod → kubejs:csg_stargate_rod_base. Raw rod (800 ticks): layer 1 = rod base + 2 quantum stars; layer 2 = 1 naquadah alloy foil ream + 1 weapon-grade naquadah foil ream + 1 pure netherite foil ream + 25 000 mB lubricant; layer 3 = 1 netherite foil ream + 1 nether star foil ream + 1 trinaquadalloy foil ream + 25 000 mB lubricant; layer 4 = layer 2 again + 25 000 mB lubricant. Activated rod: Heat Chamber, 1 raw rod + 720 mB nether star concentrate, 800 ticks.
    - |-
      Cost of ONE activated rod in the guide’s units: 9 foil reams (1 ream = 64 foil = 16 ingots, per the pack’s ream convention in component_parts.js, Unverified recipe of the ream itself), i.e. 32 ingots each of naquadah alloy, weapon-grade naquadah and pure netherite, 16 each of netherite, nether star and trinaquadalloy, plus 2 quantum stars, 2 prismalium rings, 1 long pure netherite rod, wire spools of europium and trinaquadalloy, 5184 mB naquadria, 75 B lubricant and 720 mB nether star concentrate. Nether star foil is a literal foil of nether star material (the pack adds the foil flag to nether star).
    - |-
      Materials: trinaquadalloy = 5 trinium + 3 naquadah + 2 carbon (startup netherite_alloys_and_derivatives.js), blast 8750 K at VA[ZPM] for 1000 ticks, so it needs TRINIUM COILS (9001 K); weapon-grade naquadah = 4 pure netherite dust + 6 trinaquadalloy dust + 1008 mB naquadria + 12 B fluorine → 29 dust in a mixer (1200 ticks, EUtVHA(ZPM), kjs gate_based/misc_materials.js); prismalium = 8 naquadah + 4 mercury barium calcium cuprate + 7 tungsten carbide dust → 19 dust, mixer 1000 ticks at 65 536 EU/t, EBF 9000 K, VA[ZPM], 1800 ticks (startup superconductors.js); pure netherite = purified debris dust + 100 mB tetrachloroethylene in a chemical bath (200 ticks, 20 450 EU/t) from the netherite line (kjs lines/netherite.js). Those lines are chains of their own: Unverified here.
    - |-
      Nether star concentrate (misc_materials.js heat_chamber nether_star_concentrate): 16 tiny nether star dust + 720 mB each of energized blitz, blizz, basalz and blaze → 576 mB concentrate, 250 ticks at one third of VA[UV]. One activated rod eats 720 mB concentrate = 1.25 runs = 20 tiny dust = 2.2 nether stars. Nether star dust: from nether stars (macerator) and the nether_star loop (nether_star chain, 1.19 stars per star).
    - |-
      Sub-steps people skip: (1) two Large Rotor Machine layouts: the base uses 3 layers, the raw rod 4 (input buses must be loaded layer by layer, in the order of the recipe); (2) lubricant 75 B per raw rod: a big drum on a pump; (3) the Heat Chamber then needs the concentrate pre-made: one chemistry line, not a drawer; (4) the whole line is UV-power: a plain ZPM 4A hatch is too small; (5) keep reams in drawers, never loose foil, and one drawer per ream type.
    - |-
      Unverified: layered-recipe loading order in the Large Rotor Machine controller (see the tooltip), the ream recipe, and the energized blitz/blizz/basalz/blaze sources (Thermal Foundation fluids).
  b:
    - ["gtceu:large_rotor_machine", 2]
    - ["gtceu:heat_chamber", 2]
    - ["gtceu:luv_energy_input_hatch_16a", 2]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:naquadah_alloy_foil_ream
        - gtceu:weapon_grade_naquadah_foil_ream
        - gtceu:pure_netherite_foil_ream
      t: |-
        Drawers first, one per input: prismalium rings, europium and trinaquadalloy wire spools, long pure netherite rods, quantum stars (Keep Exact 4), each foil ream type, tiny nether star dust. Drums: naquadria, lubricant (huge), energized blitz, blizz, basalz, blaze, nether star concentrate. Every machine behind its own router with Item Filters and Keep Exact arms.
    - i: ["gtceu:large_rotor_machine", "kubejs:csg_stargate_rod_base"]
      t: |-
        Rod base: the Large Rotor Machine on its UV-power hatch: layer 1 rings, layer 2 europium spool + 1296 mB naquadria, layer 3 trinaquadalloy spool + 1296 mB naquadria, the long pure netherite rod in the main bus. 40 s → 1 rod base.
    - i: ["gtceu:large_rotor_machine", "kubejs:raw_stargate_rod", "gtceu:quantum_star"]
      t: |-
        Raw rod: 4 layers: rod base + 2 stars, then the three reams of layer 2, the three of layer 3, layer 2 again, each with 25 B of lubricant. 40 s → 1 raw rod. Make a second Large Rotor Machine for this: the base machine is idle most of the time.
    - i: ["gtceu:heat_chamber", "gtceu:nether_star_concentrate_bucket", "gtceu:tiny_nether_star_dust"]
      t: |-
        Concentrate: a Heat Chamber run on tiny nether star dust + the four energized fluids → 576 mB concentrate in 12.5 s; into a drum, then a Pipez fluid pipe to the activation chamber.
    - i: ["gtceu:heat_chamber", "kubejs:activated_stargate_rod"]
      t: |-
        Activate: second Heat Chamber, raw rod in the bus + 720 mB concentrate → Activated Stargate Rod in 40 s; output drawer Keep Exact 64. The rods are also the research item of the Stargate Component Assembly.
    - i: ["functionalstorage:oak_1", "kubejs:activated_stargate_rod"]
      t: |-
        Easy to miss: the gate needs about 480 activated rods (zpm_gate): decide on a per-rod throughput before you build the whole chain. At 40 s per step per machine that is 5 h on one line; parallel hatches cut it.
---
# Stargate rods: rod base → raw rod (Large Rotor Machine, foil reams, lubricant) → activated rod (Heat Chamber, nether star concentrate)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_rods` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Era multiblocks and the Classic Stargate](../../plan/p13.md#zpmmultis)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Large Rotor Machine · 3 layers · 40 s · UV power</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 prismalium ring · europium wire spool · trinaquadalloy wire spool · long pure netherite rod · 2592 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 prismalium ring · europium wire spool · trinaquadalloy wire spool · long pure netherite rod · 2592 mB naquadria</span><span class="gt-sub"><span>Prismalium ring</span><span>Europium wire spool</span><span>Trinaquadalloy wire spool</span><span>Long pure netherite rod</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_rotor_machine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Stargate Rod Base (kubejs:csg_stargate_rod_base) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/kubejs__csg_stargate_rod_base.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Csg Stargate Rod Base</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_rotor_machine</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Large Rotor Machine · 4 layers · 40 s · UV power</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Stargate Rod Base (kubejs:csg_stargate_rod_base) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__csg_stargate_rod_base.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Csg Stargate Rod Base</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Rod base · 2 quantum star · 9 foil reams (naquadah alloy 2, weapon-grade naquadah 2, pure netherite 2, netherite, nether star, trinaquadalloy) · 75 B lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Rod base · 2 quantum star · 9 foil reams (naquadah alloy 2, weapon-grade naquadah 2, pure netherite 2, netherite, nether star, trinaquadalloy) · 75 B lubricant</span><span class="gt-sub"><span>Naquadah alloy foil ream</span><span>Weapon-grade naquadah foil ream</span><span>Pure netherite foil ream</span><span>Nether star foil ream</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_rotor_machine.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Raw Stargate Rod (kubejs:raw_stargate_rod) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/kubejs__raw_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Stargate Rod</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_rotor_machine</code></div>
</div>
<div class="gt-panel t-mod" id="m-h1">
<div class="gt-head"><span class="gt-mname">Heat Chamber · 12.5 s · (1/3) VA[UV]</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="16 tiny nether star dust · 720 mB each energized blitz, blizz, basalz, blaze (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">16 tiny nether star dust · 720 mB each energized blitz, blizz, basalz, blaze</span><span class="gt-sub"><span>Tiny nether star dust</span><span>Energized blaze</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">12.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="576 mB nether star concentrate (gtceu:nether_star_concentrate_bucket) - 576 mB / 12.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__nether_star_concentrate_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star Concentrate</span><span class="gt-note">576 mB nether star concentrate</span><b class="gt-q">576 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:heat_chamber</code></div>
</div>
<div class="gt-panel t-mod" id="m-a3">
<div class="gt-head"><span class="gt-mname">Heat Chamber · 40 s · UV power · raw rod + 720 mB concentrate</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Raw Stargate Rod (kubejs:raw_stargate_rod) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__raw_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Stargate Rod</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="576 mB nether star concentrate (gtceu:nether_star_concentrate_bucket) - 720 mB"><img class="gt-ico" src="../../assets/icons/gtceu__nether_star_concentrate_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star Concentrate</span><span class="gt-note">576 mB nether star concentrate</span><b class="gt-q">720 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Activated Stargate Rod (kubejs:activated_stargate_rod) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/kubejs__activated_stargate_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Activated Stargate Rod</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:heat_chamber</code></div>
</div>
</div>

## Flow

- [Large Rotor Machine · 3 layers · 40 s · UV power](#m-a1) → [Large Rotor Machine · 4 layers · 40 s · UV power](#m-a2) → [Heat Chamber · 40 s · UV power · raw rod + 720 mB concentrate](#m-a3)
- [Heat Chamber · 12.5 s · (1/3) VA\[UV\]](#m-h1) → [Heat Chamber · 40 s · UV power · raw rod + 720 mB concentrate](#m-a3)

## How to build

1. Drawers first, one per input: prismalium rings, europium and trinaquadalloy wire spools, long pure netherite rods, quantum stars (Keep Exact 4), each foil ream type, tiny nether star dust. Drums: naquadria, lubricant (huge), energized blitz, blizz, basalz, blaze, nether star concentrate. Every machine behind its own router with Item Filters and Keep Exact arms. — `functionalstorage:oak_1`, `gtceu:naquadah_alloy_foil_ream`, `gtceu:weapon_grade_naquadah_foil_ream`, `gtceu:pure_netherite_foil_ream`
2. Rod base: the Large Rotor Machine on its UV-power hatch: layer 1 rings, layer 2 europium spool + 1296 mB naquadria, layer 3 trinaquadalloy spool + 1296 mB naquadria, the long pure netherite rod in the main bus. 40 s → 1 rod base. — `gtceu:large_rotor_machine`, `kubejs:csg_stargate_rod_base`
3. Raw rod: 4 layers: rod base + 2 stars, then the three reams of layer 2, the three of layer 3, layer 2 again, each with 25 B of lubricant. 40 s → 1 raw rod. Make a second Large Rotor Machine for this: the base machine is idle most of the time. — `gtceu:large_rotor_machine`, `kubejs:raw_stargate_rod`, `gtceu:quantum_star`
4. Concentrate: a Heat Chamber run on tiny nether star dust + the four energized fluids → 576 mB concentrate in 12.5 s; into a drum, then a Pipez fluid pipe to the activation chamber. — `gtceu:heat_chamber`, `gtceu:nether_star_concentrate_bucket`, `gtceu:tiny_nether_star_dust`
5. Activate: second Heat Chamber, raw rod in the bus + 720 mB concentrate → Activated Stargate Rod in 40 s; output drawer Keep Exact 64. The rods are also the research item of the Stargate Component Assembly. — `gtceu:heat_chamber`, `kubejs:activated_stargate_rod`
6. Easy to miss: the gate needs about 480 activated rods (zpm\_gate): decide on a per-rod throughput before you build the whole chain. At 40 s per step per machine that is 5 h on one line; parallel hatches cut it. — `functionalstorage:oak_1`, `kubejs:activated_stargate_rod`

## Tips

- Recipes (kjs systems/gate\_based/csg.js and misc\_materials.js, all with EUtVHA(UV), i.e. UV-power recipes: a LuV 16A hatch (quest: the 16A hatch ‘gives UV speeds’) or a UV hatch on the machine). Rod base (Large Rotor Machine, layered recipe, 800 ticks): layer 1 = 2 prismalium rings; layer 2 = 1 europium wire spool + 1296 mB naquadria; layer 3 = 1 trinaquadalloy wire spool + 1296 mB naquadria; plus 1 long pure netherite rod → kubejs:csg\_stargate\_rod\_base. Raw rod (800 ticks): layer 1 = rod base + 2 quantum stars; layer 2 = 1 naquadah alloy foil ream + 1 weapon-grade naquadah foil ream + 1 pure netherite foil ream + 25 000 mB lubricant; layer 3 = 1 netherite foil ream + 1 nether star foil ream + 1 trinaquadalloy foil ream + 25 000 mB lubricant; layer 4 = layer 2 again + 25 000 mB lubricant. Activated rod: Heat Chamber, 1 raw rod + 720 mB nether star concentrate, 800 ticks.
- Cost of ONE activated rod in the guide’s units: 9 foil reams (1 ream = 64 foil = 16 ingots, per the pack’s ream convention in component\_parts.js, Unverified recipe of the ream itself), i.e. 32 ingots each of naquadah alloy, weapon-grade naquadah and pure netherite, 16 each of netherite, nether star and trinaquadalloy, plus 2 quantum stars, 2 prismalium rings, 1 long pure netherite rod, wire spools of europium and trinaquadalloy, 5184 mB naquadria, 75 B lubricant and 720 mB nether star concentrate. Nether star foil is a literal foil of nether star material (the pack adds the foil flag to nether star).
- Materials: trinaquadalloy = 5 trinium + 3 naquadah + 2 carbon (startup netherite\_alloys\_and\_derivatives.js), blast 8750 K at VA\[ZPM\] for 1000 ticks, so it needs TRINIUM COILS (9001 K); weapon-grade naquadah = 4 pure netherite dust + 6 trinaquadalloy dust + 1008 mB naquadria + 12 B fluorine → 29 dust in a mixer (1200 ticks, EUtVHA(ZPM), kjs gate\_based/misc\_materials.js); prismalium = 8 naquadah + 4 mercury barium calcium cuprate + 7 tungsten carbide dust → 19 dust, mixer 1000 ticks at 65 536 EU/t, EBF 9000 K, VA\[ZPM\], 1800 ticks (startup superconductors.js); pure netherite = purified debris dust + 100 mB tetrachloroethylene in a chemical bath (200 ticks, 20 450 EU/t) from the netherite line (kjs lines/netherite.js). Those lines are chains of their own: Unverified here.
- Nether star concentrate (misc\_materials.js heat\_chamber nether\_star\_concentrate): 16 tiny nether star dust + 720 mB each of energized blitz, blizz, basalz and blaze → 576 mB concentrate, 250 ticks at one third of VA\[UV\]. One activated rod eats 720 mB concentrate = 1.25 runs = 20 tiny dust = 2.2 nether stars. Nether star dust: from nether stars (macerator) and the nether\_star loop (nether\_star chain, 1.19 stars per star).
- Sub-steps people skip: (1) two Large Rotor Machine layouts: the base uses 3 layers, the raw rod 4 (input buses must be loaded layer by layer, in the order of the recipe); (2) lubricant 75 B per raw rod: a big drum on a pump; (3) the Heat Chamber then needs the concentrate pre-made: one chemistry line, not a drawer; (4) the whole line is UV-power: a plain ZPM 4A hatch is too small; (5) keep reams in drawers, never loose foil, and one drawer per ream type.
- **Unverified** layered-recipe loading order in the Large Rotor Machine controller (see the tooltip), the ream recipe, and the energized blitz/blizz/basalz/blaze sources (Thermal Foundation fluids).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_rotor_machine` | 2 |
| `gtceu:heat_chamber` | 2 |
| `gtceu:luv_energy_input_hatch_16a` | 2 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Feeds:** [Classic Stargate: runes (RCAS) + gate parts (Component Part Assembly) + activated rods → ring, chevron, base blocks (Stargate Component Assembly) → Create mechanical crafting](zpm_gate.md)
- **Main source for:** `kubejs:activated_stargate_rod`, `kubejs:raw_stargate_rod`, `kubejs:csg_stargate_rod_base`, `gtceu:nether_star_concentrate_bucket`
