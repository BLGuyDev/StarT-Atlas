---
kind: chain
id: circuit_parts
order: 450
data:
  t: LV circuit parts from earlier lines
  inf: true
  "n":
    - [lg, Logs, i, "minecraft:oak_log"]
    - [sp, Slime spores, i, "thermal:slime_mushroom_spores"]
    - [cu, Copper, i, "minecraft:copper_ingot"]
    - [ch, Charcoal, i, "minecraft:charcoal"]
    - [st, Steel, i, "gtceu:steel_ingot"]
    - [gl, Glass, i, "minecraft:glass"]
    - [rs, Sticky Resin, x, "gtceu:sticky_resin"]
    - [wm, Wiremill, m, "gtceu:lv_wiremill"]
    - [fw, Fine copper wire, x, "gtceu:fine_copper_wire"]
    - [as, Assembler, m, "gtceu:lv_assembler"]
    - [rb, Resin board, o, "gtceu:resin_printed_circuit_board"]
    - [re, Resistor, o, "gtceu:resistor"]
    - [vt, Vacuum Tube, o, "gtceu:vacuum_tube"]
  e:
    - [sp, rs]
    - [cu, wm]
    - [wm, fw]
    - [lg, as]
    - [rs, as]
    - [fw, as]
    - [ch, as]
    - [st, as]
    - [gl, as]
    - [as, rb]
    - [as, re]
    - [as, vt]
  tips: ["One AE2 pattern per part; the assembler pulls everything from earlier lines."]
  b: [["gtceu:lv_assembler", 2], ["gtceu:lv_wiremill", 1]]
---
# LV circuit parts from earlier lines

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `circuit_parts` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">Wiremill</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper (minecraft:copper_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Fine copper wire (gtceu:fine_copper_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__fine_copper_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Copper Wire</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Logs (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs</span></span><span class="gt-slot" title="Sticky Resin (gtceu:sticky_resin)"><img class="gt-ico" src="../../assets/icons/gtceu__sticky_resin.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sticky Resin</span></span><span class="gt-slot" title="Fine copper wire (gtceu:fine_copper_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__fine_copper_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Copper Wire</span></span><span class="gt-slot" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span><span class="gt-slot" title="Steel (gtceu:steel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span><span class="gt-slot" title="Glass (minecraft:glass)"><img class="gt-ico" src="../../assets/icons/minecraft__glass.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Resin board (gtceu:resin_printed_circuit_board)"><img class="gt-ico" src="../../assets/icons/gtceu__resin_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resin Printed Circuit Board</span><span class="gt-note">Resin board</span></span><span class="gt-slot gt-outp" title="Resistor (gtceu:resistor)"><img class="gt-ico" src="../../assets/icons/gtceu__resistor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resistor</span></span><span class="gt-slot gt-outp" title="Vacuum Tube (gtceu:vacuum_tube)"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_tube.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Tube</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Wiremill](#m-wm) → [Assembler](#m-as)

### Direct steps

- Slime spores → Sticky Resin

## Tips

- One AE2 pattern per part; the assembler pulls everything from earlier lines.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 2 |
| `gtceu:lv_wiremill` | 1 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](../steam/tree_farm.md), [Sieve station (manual)](../stone/sieve_manual.md), [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md), [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md), [Steel: Solid Blast Furnace](../steam/steel.md), [Infinite gems (sand sieve)](sieve_sand.md)
- **Main source for:** `gtceu:resin_printed_circuit_board`, `gtceu:resistor`, `gtceu:vacuum_tube`
