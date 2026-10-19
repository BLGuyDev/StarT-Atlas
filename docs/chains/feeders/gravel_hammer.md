---
kind: chain
id: gravel_hammer
order: 660
data:
  t: "Gravel, sand & dust: Forge Hammers"
  inf: true
  "n":
    - [c, Cobblestone, s, "minecraft:cobblestone"]
    - [h1, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [g, Gravel, o, "minecraft:gravel"]
    - [h2, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [s, Sand, o, "minecraft:sand"]
    - [h3, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [d, Dust, o, "exnihilosequentia:dust"]
  e: [[c, h1], [h1, g, "0.5 s"], [g, h2], [h2, s, "0.5 s"], [s, h3], [h3, d, "0.5 s"]]
  tips: ["Each step: 0.5 s at 16 EU/t. Three hammers in a row = all three blocks."]
  b: [["gtceu:lv_forge_hammer", 3]]
  how:
    - i: ["gtceu:lv_forge_hammer"]
      t: Three LV Forge Hammers in a row, each with a Conveyor Module exporting into the next.
    - i: ["minecraft:gravel", "minecraft:sand", "exnihilosequentia:dust"]
      t: |-
        Hammer 1: cobble → gravel · 2: gravel → sand · 3: sand → dust. 0.5 s and 16 EU/t each.
    - i: ["gtceu:mechanical_sieve"]
      t: Branch each output into its own Mechanical Sieve (ores, gems, redstone/sulfur).
---
# Gravel, sand &amp; dust: Forge Hammers

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `gravel_hammer` · **Tags:** Infinite source

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-h1">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Cobblestone (minecraft:cobblestone)"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">0.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Gravel (minecraft:gravel) - 0.5 s"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-lv" id="m-h2">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">0.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Sand (minecraft:sand) - 0.5 s"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-lv" id="m-h3">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="Sand (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">0.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Dust (exnihilosequentia:dust) - 0.5 s"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
</div>

## Flow

- [Forge Hammer](#m-h1) → [Forge Hammer](#m-h2) → [Forge Hammer](#m-h3)

## How to build

1. Three LV Forge Hammers in a row, each with a Conveyor Module exporting into the next. — `gtceu:lv_forge_hammer`
2. Hammer 1: cobble → gravel · 2: gravel → sand · 3: sand → dust. 0.5 s and 16 EU/t each. — `minecraft:gravel`, `minecraft:sand`, `exnihilosequentia:dust`
3. Branch each output into its own Mechanical Sieve (ores, gems, redstone/sulfur). — `gtceu:mechanical_sieve`

## Tips

- Each step: 0.5 s at 16 EU/t. Three hammers in a row = all three blocks.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_forge_hammer` | 3 |

## Needs / Feeds

- **Needs:** [Infinite cobble &amp; blackstone](../stone/inf_cobble.md)
- **Feeds:** [Rock Filtrator (gems)](../lv/geodes.md), [Infinite gems (sand sieve)](sieve_sand.md)
- **Main source for:** `minecraft:gravel`
