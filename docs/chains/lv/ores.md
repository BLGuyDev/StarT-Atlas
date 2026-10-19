---
kind: chain
id: ores
order: 150
data:
  t: Ore processing
  inf: true
  "n":
    - [cr, Crushed ores, i, "gtceu:crushed_iron_ore"]
    - [w, Water, f, "minecraft:water_bucket"]
    - [eof, Electric Ore Factory, m, "gtceu:electric_ore_factory"]
    - [d, Metal dust, x, "gtceu:iron_dust"]
    - [bp, Byproducts, o, "gtceu:nickel_dust"]
    - [fu, "Furnace / EBF", m, "gtceu:lv_electric_furnace"]
    - [ig, Ingots, o, "minecraft:iron_ingot"]
  e: [[cr, eof], [w, eof], [eof, d], [eof, bp], [d, fu], [fu, ig]]
  tips: ["HV: Super EOF / Ore Processing Factory · UHV: Bulk Ore Processing Array."]
  b: [["gtceu:electric_ore_factory", 1], ["gtceu:lv_electric_furnace", 2]]
---
# Ore processing

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `ores` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Ore processing (Electric Ore Factory)](../../plan/p2.md#orefactory)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-eof">
<div class="gt-head"><span class="gt-mname">Electric Ore Factory</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crushed ores (gtceu:crushed_iron_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_iron_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Iron Ore</span><span class="gt-note">Crushed ores</span></span><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_ore_factory.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Metal dust (gtceu:iron_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><span class="gt-note">Metal dust</span></span><span class="gt-slot gt-outp" title="Byproducts (gtceu:nickel_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Dust</span><span class="gt-note">Byproducts</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_ore_factory</code></div>
</div>
<div class="gt-panel t-lv" id="m-fu">
<div class="gt-head"><span class="gt-mname">Furnace / EBF</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Metal dust (gtceu:iron_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><span class="gt-note">Metal dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Ingots (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">Ingots</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electric_furnace</code></div>
</div>
</div>

## Flow

- [Electric Ore Factory](#m-eof) → [Furnace / EBF](#m-fu)

## Tips

- HV: Super EOF / Ore Processing Factory · UHV: Bulk Ore Processing Array.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_ore_factory` | 1 |
| `gtceu:lv_electric_furnace` | 2 |

## Needs / Feeds

- **Needs:** [Four-sieve block (gravel, sand, dust, blackstone)](sieve_block4.md)
- **Feeds:** [Alloys: Create heated mixer](../steam/alloys.md), [Cupronickel coils ×16](coils.md), [Board etching](../mv/etchant.md), [Stainless steel: MV Mixer + HV Electric Blast Furnace](../hv/stainless.md), [Alloys: Steam / LV Alloy Smelter (more per ingot)](../steam/alloys_smelter.md), [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](../hv/kanthal.md), [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../ev/nichrome_line.md), [Soul infused ingots (LV superconductor): sand → soul sand → dust + invar](soul_infused.md)
- **Main source for:** `gtceu:iron_dust`, `gtceu:zinc_dust`, `gtceu:nickel_ingot`, `gtceu:nickel_dust`
