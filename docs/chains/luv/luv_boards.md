---
kind: chain
id: luv_boards
order: 1170
data:
  t: |-
    Advanced Circuit Board: epoxy plate + gold foil → advanced board → electrum foil + iron III chloride → 6 per Nanoprocessor Mainframe
  inf: true
  "n":
    - [ep, Epoxy plate, i, "gtceu:epoxy_plate"]
    - [gf, "8 Gold foil", i, "gtceu:gold_foil"]
    - [sa, "500 mB sulfuric acid", f, "gtceu:sulfuric_acid_bucket"]
    - [r1, "LV Chemical Reactor · 30 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [eb, "Epoxy Circuit Board (advanced board)", x, "gtceu:epoxy_circuit_board"]
    - [el, "8 Electrum foil", i, "gtceu:electrum_foil"]
    - [fc, "500 mB iron III chloride (or 1 B sodium persulfate)", f, "gtceu:iron_iii_chloride_bucket"]
    - [r2, "LV Chemical Reactor · 45 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [ab, Advanced Circuit Board, o, "gtceu:epoxy_printed_circuit_board"]
  e:
    - [ep, r1, "1"]
    - [gf, r1, "8"]
    - [sa, r1, "500 mB"]
    - [r1, eb, "1 / 30 s"]
    - [eb, r2, "1"]
    - [el, r2, "8"]
    - [fc, r2, "500 mB"]
    - [r2, ab, "1 / 45 s"]
  tips:
    - |-
      Recipes (CircuitRecipes, the pack does not change them): Epoxy Circuit Board = 1 epoxy plate + 8 gold foil + 500 mB sulfuric acid, chemical reactor, 600 ticks at 30 EU/t. Advanced Circuit Board = that board + 8 electrum foil + 1 B sodium persulfate OR 500 mB iron III chloride, 900 ticks at 30 EU/t. No cleanroom, both fit an LV Chemical Reactor.
    - |-
      One Nanoprocessor Mainframe eats 6 advanced boards (2 for the nanoprocessors, 2 for the assemblies, 2 for the supercomputers). That is 6 plates, 48 gold foil, 48 electrum foil, 3 B sulfuric acid and 3 B iron III chloride per mainframe: foil is the real cost. Bender (24 EU/t, circuit 1): 1 plate → 4 foil, so 12 gold plates and 12 electrum plates per mainframe.
    - |-
      Epoxy plate: LV Fluid Solidifier with the plate mold, 144 mB epoxy → 1 plate, 40 ticks (PartsRecipeHandler). Epoxy fluid itself is the large chemical reactor line of the epoxy chain. Iron III chloride: see the etchant chain. Sodium persulfate also works and is the one the cleanroom boards later use.
    - |-
      The pack also adds a copper-chloride etch (circuit_etching.js: advanced board + 8 electrum foil + 250 mB cupric chloride solution, 900 ticks, 30 EU/t). The only recipe found for cupric chloride solution is the Chemical Plant skip (kjs chemical_plant.js), so it is not a LuV route: use iron III chloride or persulfate.
    - |-
      Sub-steps people skip: (1) the board comes in two reactions with two different fluids, so two reactors and two drums, never one reactor with both; (2) gold foil and electrum foil are different drawers; (3) the plastic board (6 per mainframe too) is a different item from this epoxy one: do not mix their drawers; (4) epoxy needs the solidifier and a plate mold, a bucket is not enough.
    - |-
      Unverified: the exact plate-mold solidifier machine tier in this pack (any solidifier should accept a 2 s ULV-power recipe, check EMI), and where the epoxy plate drawer feeds from if you automate the epoxy line.
  b:
    - ["gtceu:lv_chemical_reactor", 2]
    - ["gtceu:lv_fluid_solidifier", 1]
    - ["gtceu:lv_bender", 2]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 5]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:epoxy_plate", "gtceu:gold_foil", "gtceu:electrum_foil"]
      t: |-
        Drawers first, one per input: epoxy plates, gold foil, electrum foil. Two drums: sulfuric acid and iron III chloride. Each reactor sits behind its own Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode caps what the drawer holds.
    - i: ["gtceu:lv_fluid_solidifier", "gtceu:epoxy_plate", "gtceu:epoxy_bucket"]
      t: |-
        Epoxy plates: an LV Fluid Solidifier with the plate mold takes 144 mB epoxy and gives 1 plate in 2 s. Feed it from an epoxy drum with a Pipez fluid pipe; the output goes by Robot Arm into the plate drawer.
    - i: ["gtceu:lv_bender", "gtceu:gold_foil", "gtceu:electrum_foil"]
      t: |-
        Foil: one LV Bender per metal, circuit 1 in the bus, 1 plate → 4 foil in a few ticks at 24 EU/t. Keep Exact 64 on both foil drawers so the reactors never wait.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:sulfuric_acid_bucket", "gtceu:epoxy_circuit_board"]
      t: |-
        Reactor 1 (30 s, 30 EU/t): 1 epoxy plate + 8 gold foil + 500 mB sulfuric acid → 1 Epoxy Circuit Board. Sulfuric acid by a Pipez fluid pipe from its drum; no ghost circuit needed.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:iron_iii_chloride_bucket", "gtceu:epoxy_printed_circuit_board"]
      t: |-
        Reactor 2 (45 s, 30 EU/t): the board from reactor 1 + 8 electrum foil + 500 mB iron III chloride → 1 Advanced Circuit Board. A Robot Arm cover between the two reactors in Keep Exact mode moves boards only when reactor 2 has foil.
    - i: ["functionalstorage:oak_1", "gtceu:epoxy_printed_circuit_board"]
      t: |-
        Output drawer with Keep Exact 16: the three cleanroom circuit assemblers of the LuV line (nanoprocessor, assembly, supercomputer) all take one advanced board per craft, and the chip chain needs none, so this one drawer feeds the whole line.
---
# Advanced Circuit Board: epoxy plate + gold foil → advanced board → electrum foil + iron III chloride → 6 per Nanoprocessor Mainframe

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_boards` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Advanced boards and nano chips](../../plan/p11.md#luvboards)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-r1">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 30 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Epoxy plate (gtceu:epoxy_plate) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Plate</span><b class="gt-q">1</b></span><span class="gt-slot" title="8 Gold foil (gtceu:gold_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__gold_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Foil</span><span class="gt-note">8 Gold foil</span><b class="gt-q">8</b></span><span class="gt-slot gt-fluid" title="500 mB sulfuric acid (gtceu:sulfuric_acid_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Acid</span><span class="gt-note">500 mB sulfuric acid</span><b class="gt-q">500 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Epoxy Circuit Board (advanced board) (gtceu:epoxy_circuit_board) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Circuit Board</span><span class="gt-note">Epoxy Circuit Board (advanced board)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-r2">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 45 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Epoxy Circuit Board (advanced board) (gtceu:epoxy_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Circuit Board</span><span class="gt-note">Epoxy Circuit Board (advanced board)</span><b class="gt-q">1</b></span><span class="gt-slot" title="8 Electrum foil (gtceu:electrum_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__electrum_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electrum Foil</span><span class="gt-note">8 Electrum foil</span><b class="gt-q">8</b></span><span class="gt-slot gt-fluid" title="500 mB iron III chloride (or 1 B sodium persulfate) (gtceu:iron_iii_chloride_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__iron_iii_chloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Iii Chloride</span><span class="gt-note">500 mB iron III chloride (or 1 B sodium persulfate)</span><b class="gt-q">500 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Advanced Circuit Board (gtceu:epoxy_printed_circuit_board) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Printed Circuit Board</span><span class="gt-note">Advanced Circuit Board</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LV Chemical Reactor · 30 s · 30 EU/t](#m-r1) → [LV Chemical Reactor · 45 s · 30 EU/t](#m-r2)

## How to build

1. Drawers first, one per input: epoxy plates, gold foil, electrum foil. Two drums: sulfuric acid and iron III chloride. Each reactor sits behind its own Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode caps what the drawer holds. — `functionalstorage:oak_1`, `gtceu:epoxy_plate`, `gtceu:gold_foil`, `gtceu:electrum_foil`
2. Epoxy plates: an LV Fluid Solidifier with the plate mold takes 144 mB epoxy and gives 1 plate in 2 s. Feed it from an epoxy drum with a Pipez fluid pipe; the output goes by Robot Arm into the plate drawer. — `gtceu:lv_fluid_solidifier`, `gtceu:epoxy_plate`, `gtceu:epoxy_bucket`
3. Foil: one LV Bender per metal, circuit 1 in the bus, 1 plate → 4 foil in a few ticks at 24 EU/t. Keep Exact 64 on both foil drawers so the reactors never wait. — `gtceu:lv_bender`, `gtceu:gold_foil`, `gtceu:electrum_foil`
4. Reactor 1 (30 s, 30 EU/t): 1 epoxy plate + 8 gold foil + 500 mB sulfuric acid → 1 Epoxy Circuit Board. Sulfuric acid by a Pipez fluid pipe from its drum; no ghost circuit needed. — `gtceu:lv_chemical_reactor`, `gtceu:sulfuric_acid_bucket`, `gtceu:epoxy_circuit_board`
5. Reactor 2 (45 s, 30 EU/t): the board from reactor 1 + 8 electrum foil + 500 mB iron III chloride → 1 Advanced Circuit Board. A Robot Arm cover between the two reactors in Keep Exact mode moves boards only when reactor 2 has foil. — `gtceu:lv_chemical_reactor`, `gtceu:iron_iii_chloride_bucket`, `gtceu:epoxy_printed_circuit_board`
6. Output drawer with Keep Exact 16: the three cleanroom circuit assemblers of the LuV line (nanoprocessor, assembly, supercomputer) all take one advanced board per craft, and the chip chain needs none, so this one drawer feeds the whole line. — `functionalstorage:oak_1`, `gtceu:epoxy_printed_circuit_board`

## Tips

- Recipes (CircuitRecipes, the pack does not change them): Epoxy Circuit Board = 1 epoxy plate + 8 gold foil + 500 mB sulfuric acid, chemical reactor, 600 ticks at 30 EU/t. Advanced Circuit Board = that board + 8 electrum foil + 1 B sodium persulfate OR 500 mB iron III chloride, 900 ticks at 30 EU/t. No cleanroom, both fit an LV Chemical Reactor.
- One Nanoprocessor Mainframe eats 6 advanced boards (2 for the nanoprocessors, 2 for the assemblies, 2 for the supercomputers). That is 6 plates, 48 gold foil, 48 electrum foil, 3 B sulfuric acid and 3 B iron III chloride per mainframe: foil is the real cost. Bender (24 EU/t, circuit 1): 1 plate → 4 foil, so 12 gold plates and 12 electrum plates per mainframe.
- Epoxy plate: LV Fluid Solidifier with the plate mold, 144 mB epoxy → 1 plate, 40 ticks (PartsRecipeHandler). Epoxy fluid itself is the large chemical reactor line of the epoxy chain. Iron III chloride: see the etchant chain. Sodium persulfate also works and is the one the cleanroom boards later use.
- The pack also adds a copper-chloride etch (circuit\_etching.js: advanced board + 8 electrum foil + 250 mB cupric chloride solution, 900 ticks, 30 EU/t). The only recipe found for cupric chloride solution is the Chemical Plant skip (kjs chemical\_plant.js), so it is not a LuV route: use iron III chloride or persulfate.
- Sub-steps people skip: (1) the board comes in two reactions with two different fluids, so two reactors and two drums, never one reactor with both; (2) gold foil and electrum foil are different drawers; (3) the plastic board (6 per mainframe too) is a different item from this epoxy one: do not mix their drawers; (4) epoxy needs the solidifier and a plate mold, a bucket is not enough.
- **Unverified** the exact plate-mold solidifier machine tier in this pack (any solidifier should accept a 2 s ULV-power recipe, check EMI), and where the epoxy plate drawer feeds from if you automate the epoxy line.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_chemical_reactor` | 2 |
| `gtceu:lv_fluid_solidifier` | 1 |
| `gtceu:lv_bender` | 2 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 5 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Feeds:** [LuV circuit: Nanoprocessor Mainframe (nanoprocessor → assembly → supercomputer → mainframe, four EV Circuit Assemblers in the cleanroom)](luv_circuits.md)
- **Main source for:** `gtceu:epoxy_printed_circuit_board`, `gtceu:epoxy_circuit_board`
