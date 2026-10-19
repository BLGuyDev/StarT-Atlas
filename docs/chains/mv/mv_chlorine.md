---
kind: chain
id: mv_chlorine
order: 950
data:
  t: Chlorine and hydrochloric acid (water → salt water → acid)
  inf: true
  "n":
    - [w, Water, s, "thermal:device_water_gen"]
    - [sa, "Sand (kept in the barrel)", i, "minecraft:sand"]
    - [lb, Large Barrel, m, "gtceu:large_barrel"]
    - [sw, Sea water, f, "exnihilosequentia:sea_water_bucket"]
    - [ce, LV Centrifuge, m, "gtceu:lv_centrifuge"]
    - [sl, Salt water, f, "gtceu:salt_water_bucket"]
    - [by, "Saltpeter + rock salt", x, "gtceu:crushed_rock_salt_ore"]
    - [el, LV Electrolyzer, m, "gtceu:lv_electrolyzer"]
    - [cl, Chlorine, f, "gtceu:chlorine_bucket"]
    - [hy, Hydrogen, f, "gtceu:hydrogen_bucket"]
    - [na, "3 Sodium hydroxide", x, "gtceu:sodium_hydroxide_dust"]
    - [cr, LV Chemical Reactor, m, "gtceu:lv_chemical_reactor"]
    - [hc, Hydrochloric acid, o, "gtceu:hydrochloric_acid_bucket"]
  e:
    - [w, lb, "1 B"]
    - [sa, lb]
    - [lb, sw, "1 B / 4 s"]
    - [sw, ce, "1250 mB"]
    - [ce, sl, "1 B / 2.5 s"]
    - [ce, by]
    - [sl, el, "1 B / 36 s"]
    - [el, cl, "1 B"]
    - [el, hy, "1 B"]
    - [el, na]
    - [cl, cr, "1 B"]
    - [hy, cr, "1 B"]
    - [cr, hc, "1 B / 3 s"]
  tips:
    - Only water and one sand block go in. 1 B of acid costs 1 B salt water = 1.25 B sea water = 1.25 B water.
    - The iron III chloride etchant (next module) eats 3 B of acid per bucket and 100 mB per board, so one electrolyzer (1.67 B acid a minute) covers about 5 boards a minute.
    - |-
      Sodium hydroxide, saltpeter and rock salt are by-products: a drawer, or an Item Voiding Cover on the output.
    - |-
      Unverified: hydrogen from formic acid. 1 B CO2 + 1 B water → 1 B formic acid + 1 B oxygen (LV, 48 s). Marble (calcite source) only comes from the Large Rock Crusher, 240 EU/t (HV). The electrolysis amounts of formic acid were not checked.
  b:
    - ["gtceu:large_barrel", 1]
    - ["gtceu:lv_centrifuge", 1]
    - ["gtceu:lv_electrolyzer", 1]
    - ["gtceu:lv_chemical_reactor", 1]
    - ["thermal:device_water_gen", 1]
    - ["minecraft:sand", 1]
    - ["gtceu:steel_drum", 3]
    - ["pipez:fluid_pipe", 16]
    - ["functionalstorage:oak_1", 3]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["thermal:device_water_gen", "gtceu:large_barrel", "minecraft:sand"]
      t: |-
        Water: an Aqueous Accumulator (or the water line of your power plant) feeds the Large Barrel through a Pipez fluid pipe. Leave one sand block in its input: it is kept. 1 B water → 1 B sea water every 4 s.
    - i: ["gtceu:lv_centrifuge", "exnihilosequentia:sea_water_bucket", "gtceu:salt_water_bucket"]
      t: |-
        LV Centrifuge: 1250 mB sea water → 1000 mB salt water + 1 crushed saltpeter + 1 crushed rock salt in 2.5 s (15 EU/t). Pipe the sea water straight from the barrel; the two crushed ores go to a drawer.
    - i: ["gtceu:lv_electrolyzer", "gtceu:chlorine_bucket", "gtceu:hydrogen_bucket", "gtceu:sodium_hydroxide_dust"]
      t: |-
        LV Electrolyzer: 1000 mB salt water → 3 sodium hydroxide dust + 1000 mB chlorine + 1000 mB hydrogen in 36 s (30 EU/t). Put a steel drum before it as buffer; the dust goes to a drawer.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:hydrochloric_acid_bucket", "gtceu:steel_drum"]
      t: |-
        LV Chemical Reactor: 1000 mB chlorine + 1000 mB hydrogen → 1000 mB hydrochloric acid in 3 s (7 EU/t). Pipe both gases straight from the electrolyzer (equal amounts, so nothing builds up). The acid fills a steel drum: your stock.
---
# Chlorine and hydrochloric acid (water → salt water → acid)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_chlorine` · **Tags:** Infinite source, Unverified

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Chlorine and hydrochloric acid](../../plan/p6.md#chlor)

**Tips:** 4, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lb">
<div class="gt-head"><span class="gt-mname">Large Barrel</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Water (thermal:device_water_gen) - 1 B"><img class="gt-ico" src="../../assets/icons/thermal__device_water_gen.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Device Water Gen</span><span class="gt-tag">infinite</span><b class="gt-q">1 B</b></span><span class="gt-slot" title="Sand (kept in the barrel) (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span><span class="gt-note">Sand (kept in the barrel)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Sea water (exnihilosequentia:sea_water_bucket) - 1 B / 4 s"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__sea_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sea Water</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-ce">
<div class="gt-head"><span class="gt-mname">LV Centrifuge</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sea water (exnihilosequentia:sea_water_bucket) - 1250 mB"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__sea_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sea Water</span><b class="gt-q">1250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Salt water (gtceu:salt_water_bucket) - 1 B / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__salt_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Salt Water</span><b class="gt-q">1 B</b></span><span class="gt-slot" title="Saltpeter + rock salt (gtceu:crushed_rock_salt_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_rock_salt_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Rock Salt Ore</span><span class="gt-note">Saltpeter + rock salt</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_centrifuge</code></div>
</div>
<div class="gt-panel t-lv" id="m-el">
<div class="gt-head"><span class="gt-mname">LV Electrolyzer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Salt water (gtceu:salt_water_bucket) - 1 B / 36 s"><img class="gt-ico" src="../../assets/icons/gtceu__salt_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Salt Water</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">36 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Chlorine (gtceu:chlorine_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><b class="gt-q">1 B</b></span><span class="gt-slot" title="3 Sodium hydroxide (gtceu:sodium_hydroxide_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__sodium_hydroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sodium Hydroxide Dust</span><span class="gt-note">3 Sodium hydroxide</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electrolyzer</code></div>
</div>
<div class="gt-panel t-lv" id="m-cr">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Chlorine (gtceu:chlorine_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__chlorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chlorine</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen (gtceu:hydrogen_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">3 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Hydrochloric acid (gtceu:hydrochloric_acid_bucket) - 1 B / 3 s"><img class="gt-ico" src="../../assets/icons/gtceu__hydrochloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrochloric Acid Bucket</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Large Barrel](#m-lb) → [LV Centrifuge](#m-ce) → [LV Electrolyzer](#m-el) → [LV Chemical Reactor](#m-cr)

## How to build

1. Water: an Aqueous Accumulator (or the water line of your power plant) feeds the Large Barrel through a Pipez fluid pipe. Leave one sand block in its input: it is kept. 1 B water → 1 B sea water every 4 s. — `thermal:device_water_gen`, `gtceu:large_barrel`, `minecraft:sand`
2. LV Centrifuge: 1250 mB sea water → 1000 mB salt water + 1 crushed saltpeter + 1 crushed rock salt in 2.5 s (15 EU/t). Pipe the sea water straight from the barrel; the two crushed ores go to a drawer. — `gtceu:lv_centrifuge`, `exnihilosequentia:sea_water_bucket`, `gtceu:salt_water_bucket`
3. LV Electrolyzer: 1000 mB salt water → 3 sodium hydroxide dust + 1000 mB chlorine + 1000 mB hydrogen in 36 s (30 EU/t). Put a steel drum before it as buffer; the dust goes to a drawer. — `gtceu:lv_electrolyzer`, `gtceu:chlorine_bucket`, `gtceu:hydrogen_bucket`, `gtceu:sodium_hydroxide_dust`
4. LV Chemical Reactor: 1000 mB chlorine + 1000 mB hydrogen → 1000 mB hydrochloric acid in 3 s (7 EU/t). Pipe both gases straight from the electrolyzer (equal amounts, so nothing builds up). The acid fills a steel drum: your stock. — `gtceu:lv_chemical_reactor`, `gtceu:hydrochloric_acid_bucket`, `gtceu:steel_drum`

## Tips

- Only water and one sand block go in. 1 B of acid costs 1 B salt water = 1.25 B sea water = 1.25 B water.
- The iron III chloride etchant (next module) eats 3 B of acid per bucket and 100 mB per board, so one electrolyzer (1.67 B acid a minute) covers about 5 boards a minute.
- Sodium hydroxide, saltpeter and rock salt are by-products: a drawer, or an Item Voiding Cover on the output.
- **Unverified** hydrogen from formic acid. 1 B CO2 + 1 B water → 1 B formic acid + 1 B oxygen (LV, 48 s). Marble (calcite source) only comes from the Large Rock Crusher, 240 EU/t (HV). The electrolysis amounts of formic acid were not checked.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_barrel` | 1 |
| `gtceu:lv_centrifuge` | 1 |
| `gtceu:lv_electrolyzer` | 1 |
| `gtceu:lv_chemical_reactor` | 1 |
| `thermal:device_water_gen` | 1 |
| `minecraft:sand` | 1 |
| `gtceu:steel_drum` | 3 |
| `pipez:fluid_pipe` | 16 |
| `functionalstorage:oak_1` | 3 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
