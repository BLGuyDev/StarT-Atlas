---
kind: chain
id: mv_board
order: 970
data:
  t: Phenolic printed circuit board (silver foil + etching)
  inf: true
  "n":
    - [cg, "Crushed galena (sieve)", i, "gtceu:crushed_galena_ore"]
    - [wt, Water 100 mB, f, "minecraft:water_bucket"]
    - [eof, Electric Ore Factory, m, "gtceu:electric_ore_factory"]
    - [sd, "Silver dust (45 %)", x, "gtceu:silver_dust"]
    - [fu, Furnace, m, "minecraft:furnace"]
    - [si, Silver ingot, i, "gtceu:silver_ingot"]
    - [be, "Bender · circuit 10", m, "gtceu:lv_bender"]
    - [sf, "4 Silver foil", x, "gtceu:silver_foil"]
    - [wd, Wood dust, i, "gtceu:wood_dust"]
    - [gl, Glue 50 mB, f, "gtceu:glue_bucket"]
    - [a1, "Assembler · circuit 1", m, "gtceu:lv_assembler"]
    - [pb, Phenolic circuit board, x, "gtceu:phenolic_circuit_board"]
    - [fc, Iron III chloride 100 mB, f, "gtceu:iron_iii_chloride_bucket"]
    - [cr, LV Chemical Reactor, m, "gtceu:lv_chemical_reactor"]
    - [out, Phenolic printed circuit board, o, "gtceu:phenolic_printed_circuit_board"]
  e:
    - [cg, eof]
    - [wt, eof, "100 mB"]
    - [eof, sd, "45 %"]
    - [sd, fu]
    - [fu, si]
    - [si, be, "1"]
    - [be, sf, "1 → 4"]
    - [wd, a1, "1"]
    - [gl, a1, "50 mB"]
    - [a1, pb, "7.5 s"]
    - [pb, cr, "1"]
    - [sf, cr, "4"]
    - [fc, cr, "100 mB"]
    - [cr, out, "15 s"]
  tips:
    - |-
      One board = 4 silver foil = 1 silver ingot. Silver is the limit of the whole phase: one Electric Ore Factory on galena gives about 3 silver ingots a minute.
    - The hand-crafted Good Circuit Board is removed in this pack (mass_removals.js), so etching in the chemical reactor is the only way.
    - |-
      Second silver source: the Void Extractor gives 2 raw silver (35 %) per 32 s; smelt raw silver straight to an ingot.
  b:
    - ["gtceu:electric_ore_factory", 1]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_chemical_reactor", 1]
    - ["minecraft:furnace", 1]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["functionalstorage:oak_1", 9]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
  how:
    - i: ["gtceu:electric_ore_factory", "gtceu:crushed_galena_ore", "gtceu:silver_dust"]
      t: |-
        Electric Ore Factory (30 EU/t, 8 s): 1 crushed galena + 100 mB water → 1 galena dust, +1 galena dust (75 %), 1 silver dust (45 %), 1 sulfur dust (32.5 %). Routers pull only silver dust into the next drawer; galena (lead) and sulfur go to storage.
    - i: ["minecraft:furnace", "gtceu:silver_ingot"]
      t: |-
        Furnace on the same row as your other ingots: silver dust → silver ingot.
    - i: ["gtceu:lv_bender", "gtceu:silver_foil"]
      t: |-
        LV Bender with ghost circuit 10: 1 silver ingot → 4 silver foil (24 EU/t). Circuit 1 does the same from a plate. Robot Arm cover on Keep Exact 64.
    - i: ["gtceu:lv_assembler", "gtceu:phenolic_circuit_board", "gtceu:wood_dust"]
      t: |-
        Assembler with ghost circuit 1: 1 wood dust + 50 mB glue → 1 phenolic circuit board in 7.5 s (30 EU/t). Wood dust from the treated wood line, glue from the glue line.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:phenolic_printed_circuit_board"]
      t: |-
        LV Chemical Reactor: 4 silver foil + 1 phenolic circuit board + 100 mB iron III chloride → 1 phenolic printed circuit board in 15 s (30 EU/t). Drawer buffers before it for boards and foil, a Robot Arm cover on Keep Exact 64 on the output.
---
# Phenolic printed circuit board (silver foil + etching)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_board` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Phenolic printed circuit boards](../../plan/p6.md#pcb)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-eof">
<div class="gt-head"><span class="gt-mname">Electric Ore Factory</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crushed galena (sieve) (gtceu:crushed_galena_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_galena_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Galena Ore</span><span class="gt-note">Crushed galena (sieve)</span></span><span class="gt-slot gt-fluid" title="Water 100 mB (minecraft:water_bucket) - 100 mB"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><span class="gt-note">Water 100 mB</span><b class="gt-q">100 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_ore_factory.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Silver dust (45 %) (gtceu:silver_dust) - 45 %"><img class="gt-ico" src="../../assets/icons/gtceu__silver_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Dust</span><span class="gt-note">Silver dust (45 %)</span><b class="gt-q">45 %</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_ore_factory</code></div>
</div>
<div class="gt-panel t-mod" id="m-fu">
<div class="gt-head"><span class="gt-mname">Furnace</span><span class="gt-badge t-mod">Vanilla</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silver dust (45 %) (gtceu:silver_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__silver_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Dust</span><span class="gt-note">Silver dust (45 %)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/minecraft__furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Silver ingot (gtceu:silver_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__silver_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Ingot</span></span></div>
</div>
<div class="gt-foot"><code>minecraft:furnace</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">Bender · circuit 10</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silver ingot (gtceu:silver_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__silver_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Silver foil (gtceu:silver_foil) - 1 → 4"><img class="gt-ico" src="../../assets/icons/gtceu__silver_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Foil</span><span class="gt-note">4 Silver foil</span><b class="gt-q">1 → 4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembler · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wood dust (gtceu:wood_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__wood_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Glue 50 mB (gtceu:glue_bucket) - 50 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glue</span><span class="gt-note">Glue 50 mB</span><b class="gt-q">50 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Phenolic circuit board (gtceu:phenolic_circuit_board) - 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Circuit Board</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-cr">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Phenolic circuit board (gtceu:phenolic_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Circuit Board</span><b class="gt-q">1</b></span><span class="gt-slot" title="4 Silver foil (gtceu:silver_foil) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__silver_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Foil</span><span class="gt-note">4 Silver foil</span><b class="gt-q">4</b></span><span class="gt-slot gt-fluid" title="Iron III chloride 100 mB (gtceu:iron_iii_chloride_bucket) - 100 mB"><img class="gt-ico" src="../../assets/icons/gtceu__iron_iii_chloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Iii Chloride</span><span class="gt-note">Iron III chloride 100 mB</span><b class="gt-q">100 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Phenolic printed circuit board (gtceu:phenolic_printed_circuit_board) - 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__phenolic_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phenolic Printed Circuit Board</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Electric Ore Factory](#m-eof) → [Furnace](#m-fu) → [Bender · circuit 10](#m-be) → [LV Chemical Reactor](#m-cr)
- [Assembler · circuit 1](#m-a1) → [LV Chemical Reactor](#m-cr)

## How to build

1. Electric Ore Factory (30 EU/t, 8 s): 1 crushed galena + 100 mB water → 1 galena dust, +1 galena dust (75 %), 1 silver dust (45 %), 1 sulfur dust (32.5 %). Routers pull only silver dust into the next drawer; galena (lead) and sulfur go to storage. — `gtceu:electric_ore_factory`, `gtceu:crushed_galena_ore`, `gtceu:silver_dust`
2. Furnace on the same row as your other ingots: silver dust → silver ingot. — `minecraft:furnace`, `gtceu:silver_ingot`
3. LV Bender with ghost circuit 10: 1 silver ingot → 4 silver foil (24 EU/t). Circuit 1 does the same from a plate. Robot Arm cover on Keep Exact 64. — `gtceu:lv_bender`, `gtceu:silver_foil`
4. Assembler with ghost circuit 1: 1 wood dust + 50 mB glue → 1 phenolic circuit board in 7.5 s (30 EU/t). Wood dust from the treated wood line, glue from the glue line. — `gtceu:lv_assembler`, `gtceu:phenolic_circuit_board`, `gtceu:wood_dust`
5. LV Chemical Reactor: 4 silver foil + 1 phenolic circuit board + 100 mB iron III chloride → 1 phenolic printed circuit board in 15 s (30 EU/t). Drawer buffers before it for boards and foil, a Robot Arm cover on Keep Exact 64 on the output. — `gtceu:lv_chemical_reactor`, `gtceu:phenolic_printed_circuit_board`

## Tips

- One board = 4 silver foil = 1 silver ingot. Silver is the limit of the whole phase: one Electric Ore Factory on galena gives about 3 silver ingots a minute.
- The hand-crafted Good Circuit Board is removed in this pack (mass\_removals.js), so etching in the chemical reactor is the only way.
- Second silver source: the Void Extractor gives 2 raw silver (35 %) per 32 s; smelt raw silver straight to an ingot.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_ore_factory` | 1 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_chemical_reactor` | 1 |
| `minecraft:furnace` | 1 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `functionalstorage:oak_1` | 9 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |

## Needs / Feeds

- **Needs:** [Treated wood: cutter + spout](../lv/treated_wood.md)
- **Feeds:** [Board etching](etchant.md), [MV circuit line (Good Electronic Circuit)](mv_circuit.md)
- **Main source for:** `gtceu:phenolic_circuit_board`, `gtceu:phenolic_printed_circuit_board`, `gtceu:silver_foil`
