---
kind: chain
id: uv_data
order: 1820
data:
  t: |-
    Data Module (sterile circuit assembler) and the data item per CWU/t: orb below 32, module from 32, data DNA disk from 160, component data core from 320
  inf: true
  "n":
    - - g1
      - Wetware printed circuit board · 2 ZPM circuit · 32 RAM chip · 64 NOR chip · 64 NAND chip · 32 fine YBCO wire · double solder
      - g
      - functionalstorage:oak_1
      - - [Wetware printed circuit board, "gtceu:wetware_printed_circuit_board"]
        - [RAM chip, "gtceu:ram_chip"]
        - [NOR chip, "gtceu:nor_memory_chip"]
        - [NAND chip, "gtceu:nand_memory_chip"]
        - [Fine YBCO wire, "gtceu:fine_yttrium_barium_cuprate_wire"]
    - [a1, "ZPM Circuit Assembler · 20 s · 38 400 EU/t · STERILE Cleanroom", m, "gtceu:zpm_circuit_assembler"]
    - [dm, Data Module, x, "gtceu:data_module"]
    - [rs, "Research Station · 32 to 159 CWU/t · module + scan item", m, "gtceu:research_station"]
    - [dh, "Advanced Data Access Hatch (module slot) → Assembly Line", o, "gtceu:advanced_data_access_hatch"]
  e: [[g1, a1, "1"], [a1, dm, "1 / 20 s"], [dm, rs, "1"], [rs, dh, recipe data]]
  tips:
    - |-
      Data Module (gtsrc CircuitRecipes data_module, not changed by the pack): circuit assembler in the STERILE cleanroom, 400 ticks at 38 400 EU/t, 1 wetware printed circuit board + 2 ZPM circuits + 32 RAM + 64 NOR + 64 NAND + 32 fine YBCO wire with the double solder multiplier. Data item rule of the pack’s own research recipes (kjs utils/helpers/recipe_helpers.js getDataItem): below 32 CWU/t a data orb, from 32 a data module, from 160 a data DNA disk (circuit assembler, sterile, 400 ticks at V[UHV]: runic printed board + 2 UHV circuits + 24 QRAM + 16 hyper NOR + 16 hyper NAND + 32 fine europium wire + 144 mB ITLC solder), from 320 a component data core (UIV). The Assembly Line research recipes use the GT default carrier: Unverified which one the fork writes at 48 to 144 CWU/t (GT default: module above 32), so build a module before you try the UV hatch (64 CWU/t).
    - |-
      What needs a module here: every UV research (hatch 64, components 32 / 48, wetware computer 64, mainframe 96, fusion 96, drilling rig 144, chemical plant 64) and the UHV component parts (128 / 144). The Advanced Data Access Hatch (ZPM era, zpm_data) accepts orbs, sticks and modules; a Data Bank shares them between lines. Write the module in the Research Station with the scan item in the Object Holder.
    - |-
      Sub-steps people skip: (1) the data module is made in the STERILE room while the circuit assemblers are in the normal one; (2) each recipe needs its own module: 12+ modules for the UV era; (3) NOR and NAND chips by the hundred: 64 + 64 per module; (4) a research that overwrites a module with a different recipe needs a fresh one (GT clears NBT with a shapeless recipe: gtceu data_module_nbt).
    - |-
      Unverified: data carrier used by assembly line research at 48 to 144 CWU/t.
  b:
    - ["gtceu:zpm_circuit_assembler", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:advanced_data_access_hatch", 2]
    - ["gtceu:data_bank", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 2]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:wetware_printed_circuit_board
        - gtceu:nor_memory_chip
        - gtceu:nand_memory_chip
      t: |-
        Drawers first: printed boards (1), ZPM circuits (2), RAM (32), NOR (64), NAND (64), fine YBCO wire (32). Drum: soldering alloy. The assembler sits in the Sterile Cleanroom.
    - i: ["gtceu:zpm_circuit_assembler", "gtceu:data_module"]
      t: |-
        ZPM circuit assembler: 20 s per module at 38 400 EU/t. Output drawer Keep Exact 4.
    - i: ["gtceu:research_station", "gtceu:data_module"]
      t: |-
        Research Station: module + the scan item in the Object Holder; the CWU/t of the recipe must be available.
    - i: ["gtceu:advanced_data_access_hatch", "gtceu:assembly_line"]
      t: Put the written module into the Assembly Line’s Advanced Data Access Hatch (or the Data Bank).
    - i: ["functionalstorage:oak_1", "gtceu:data_module"]
      t: |-
        Easy to miss: label modules with an item frame: all written modules look alike.
---
# Data Module (sterile circuit assembler) and the data item per CWU/t: orb below 32, module from 32, data DNA disk from 160, component data core from 320

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_data` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Research data and CWU power](../../plan/p14.md#uvdata)

**Tips:** 4, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-a1">
<div class="gt-head"><span class="gt-mname">ZPM Circuit Assembler · 20 s · 38 400 EU/t · STERILE Cleanroom</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Wetware printed circuit board · 2 ZPM circuit · 32 RAM chip · 64 NOR chip · 64 NAND chip · 32 fine YBCO wire · double solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Wetware printed circuit board · 2 ZPM circuit · 32 RAM chip · 64 NOR chip · 64 NAND chip · 32 fine YBCO wire · double solder</span><span class="gt-sub"><span>Wetware printed circuit board</span><span>RAM chip</span><span>NOR chip</span><span>NAND chip</span><span>Fine YBCO wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_circuit_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Data Module (gtceu:data_module) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__data_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Module</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_circuit_assembler</code></div>
</div>
<div class="gt-panel t-mod" id="m-rs">
<div class="gt-head"><span class="gt-mname">Research Station · 32 to 159 CWU/t · module + scan item</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Data Module (gtceu:data_module) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__data_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Data Module</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__research_station.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Advanced Data Access Hatch (module slot) → Assembly Line (gtceu:advanced_data_access_hatch) - recipe data"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_data_access_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Data Access Hatch</span><span class="gt-note">Advanced Data Access Hatch (module slot) → Assembly Line</span><b class="gt-q">recipe data</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:research_station</code></div>
</div>
</div>

## Flow

- [ZPM Circuit Assembler · 20 s · 38 400 EU/t · STERILE Cleanroom](#m-a1) → [Research Station · 32 to 159 CWU/t · module + scan item](#m-rs)

## How to build

1. Drawers first: printed boards (1), ZPM circuits (2), RAM (32), NOR (64), NAND (64), fine YBCO wire (32). Drum: soldering alloy. The assembler sits in the Sterile Cleanroom. — `functionalstorage:oak_1`, `gtceu:wetware_printed_circuit_board`, `gtceu:nor_memory_chip`, `gtceu:nand_memory_chip`
2. ZPM circuit assembler: 20 s per module at 38 400 EU/t. Output drawer Keep Exact 4. — `gtceu:zpm_circuit_assembler`, `gtceu:data_module`
3. Research Station: module + the scan item in the Object Holder; the CWU/t of the recipe must be available. — `gtceu:research_station`, `gtceu:data_module`
4. Put the written module into the Assembly Line’s Advanced Data Access Hatch (or the Data Bank). — `gtceu:advanced_data_access_hatch`, `gtceu:assembly_line`
5. Easy to miss: label modules with an item frame: all written modules look alike. — `functionalstorage:oak_1`, `gtceu:data_module`

## Tips

- Data Module (gtsrc CircuitRecipes data\_module, not changed by the pack): circuit assembler in the STERILE cleanroom, 400 ticks at 38 400 EU/t, 1 wetware printed circuit board + 2 ZPM circuits + 32 RAM + 64 NOR + 64 NAND + 32 fine YBCO wire with the double solder multiplier. Data item rule of the pack’s own research recipes (kjs utils/helpers/recipe\_helpers.js getDataItem): below 32 CWU/t a data orb, from 32 a data module, from 160 a data DNA disk (circuit assembler, sterile, 400 ticks at V\[UHV\]: runic printed board + 2 UHV circuits + 24 QRAM + 16 hyper NOR + 16 hyper NAND + 32 fine europium wire + 144 mB ITLC solder), from 320 a component data core (UIV). The Assembly Line research recipes use the GT default carrier: Unverified which one the fork writes at 48 to 144 CWU/t (GT default: module above 32), so build a module before you try the UV hatch (64 CWU/t).
- What needs a module here: every UV research (hatch 64, components 32 / 48, wetware computer 64, mainframe 96, fusion 96, drilling rig 144, chemical plant 64) and the UHV component parts (128 / 144). The Advanced Data Access Hatch (ZPM era, zpm\_data) accepts orbs, sticks and modules; a Data Bank shares them between lines. Write the module in the Research Station with the scan item in the Object Holder.
- Sub-steps people skip: (1) the data module is made in the STERILE room while the circuit assemblers are in the normal one; (2) each recipe needs its own module: 12+ modules for the UV era; (3) NOR and NAND chips by the hundred: 64 + 64 per module; (4) a research that overwrites a module with a different recipe needs a fresh one (GT clears NBT with a shapeless recipe: gtceu data\_module\_nbt).
- **Unverified** data carrier used by assembly line research at 48 to 144 CWU/t.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:zpm_circuit_assembler` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:advanced_data_access_hatch` | 2 |
| `gtceu:data_bank` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `gtceu:data_module`, `start_core:data_dna_disk`
