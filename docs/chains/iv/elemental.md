---
kind: chain
id: elemental
order: 580
data:
  t: |-
    Elemental powders: blizz, blitz, basalz from dust + gas, then molten powder for the nether star loop
  inf: true
  "n":
    - [co, Cobalt dust, i, "gtceu:cobalt_dust"]
    - [fl, Fluorine, f, "gtceu:fluorine_bucket"]
    - [pt, Platinum dust, i, "gtceu:platinum_dust"]
    - [de, Deuterium, f, "gtceu:deuterium_bucket"]
    - [rh, Rhodium dust, i, "gtceu:rhodium_dust"]
    - [he, Helium, f, "gtceu:helium_bucket"]
    - [cr, "IV Chemical Reactor or LCR with an IV hatch · 10 s · 7680 EU/t", m, "gtceu:iv_chemical_reactor"]
    - [b1, "16 Blizz powder", x, "thermal:blizz_powder"]
    - [b2, "16 Blitz powder", x, "thermal:blitz_powder"]
    - [b3, "16 Basalz powder", x, "thermal:basalz_powder"]
    - [ex, LV Extractor, m, "gtceu:lv_extractor"]
    - [o, "Liquid powders (144 mB each)", o, "gtceu:blizz_bucket"]
    - [bp, "Blaze powder (source unverified)", i, "minecraft:blaze_powder"]
  e:
    - [co, cr]
    - [fl, cr]
    - [pt, cr]
    - [de, cr]
    - [rh, cr]
    - [he, cr]
    - [cr, b1]
    - [cr, b2]
    - [cr, b3]
    - [b1, ex]
    - [b2, ex]
    - [b3, ex]
    - [ex, o]
    - [bp, ex, "1"]
  tips:
    - |-
      Source: kubejs lines/nether_stars.js. Each powder is a Chemical Reactor (or Large Chemical Reactor) recipe at 480 x 16 = 7680 EU/t: 1 dust + 1000 mB gas → 16 powder in 200 ticks (10 s). Cobalt dust + fluorine → blizz; platinum dust + deuterium → blitz; rhodium dust + helium → basalz. 7680 EU/t is an IV recipe: an IV Chemical Reactor (iv_chemical_reactor, fed by an IV cable) or a Large Chemical Reactor on an IV Energy Hatch.
    - |-
      Molten powder: LV Extractor (30 EU/t, 22 ticks): 1 powder → 144 mB of the matching fluid; the old node said IV Extractor, which is not needed. Blaze powder has no recipe in the pack (the vanilla one is removed) and is the fourth powder: Unverified: where it comes from.
    - |-
      Cost per nether star in powder: about 5.3 powder items of each of the 4 elements (4 × about 760 mB molten), so a single craft of 16 serves 3 stars. Rhodium for basalz is the rare input (platinum group line, 1 per 6 inert metal mixture); platinum dust for blitz and cobalt for blizz are plentiful. Fluorine is the slurry chain; deuterium and helium come from the air/hydrogen lines.
    - |-
      A Macerator turns the Thermal rods back into powder (1 rod → 4 powder, 88 ticks, 2 EU/t): blizz, blitz and basalz rods from the Thermal mobs work too.
    - |-
      The Heat Chamber that “energizes” molten powders in the same script is a LuV recipe (energized nether star shard + 1728 mB powder): do not plan it for IV.
    - |-
      Sub-steps people skip: (1) each powder is its own dust + gas pair, so three machines or one machine with three drawers and filters, never a single mixed bus; (2) do not extract more molten powder than 5 items per run; extra just sits in the drum; (3) the reactor wants the gas as a fluid, in a hatch.
    - |-
      Unverified: the blaze powder source, and the exact supply of deuterium (the guide has no deuterium chain).
  b:
    - ["gtceu:iv_chemical_reactor", 1]
    - ["gtceu:lv_extractor", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 5]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:cobalt_dust", "gtceu:platinum_dust", "gtceu:rhodium_dust"]
      t: |-
        Three dust drawers (cobalt, platinum, rhodium) and three gas drums (fluorine, deuterium, helium), each with a Modular Router or Pipez route and an Item Filter or fluid filter to the reactor. The three powders are three different recipes: give each its own filter pair so the reactor never sees two dusts at once.
    - i: ["gtceu:iv_chemical_reactor", "thermal:blizz_powder"]
      t: |-
        IV Chemical Reactor (a single machine, 7680 EU/t from an IV cable; a Large Chemical Reactor would need an IV Energy Hatch instead): 1 cobalt dust + 1 B fluorine → 16 blizz powder in 10 s. A big output slot is needed: use an output bus or a Robot Arm cover that moves powder into a drawer, or the reactor stops at 64.
    - i: ["gtceu:iv_chemical_reactor", "thermal:blitz_powder"]
      t: |-
        Same machine type, second unit or the same reactor with a different drawer: 1 platinum dust + 1 B deuterium → 16 blitz powder (10 s, 7680 EU/t). Deuterium is a gas drum on a fluid hatch; check its tank before blaming the reactor.
    - i: ["gtceu:iv_chemical_reactor", "thermal:basalz_powder"]
      t: |-
        Third recipe: 1 rhodium dust + 1 B helium → 16 basalz powder (10 s, 7680 EU/t). Rhodium is the scarcest input of the three (the platinum group line), but one dust gives 16 powder, enough for 3 nether stars.
    - i: ["gtceu:lv_extractor", "gtceu:blizz_bucket", "gtceu:blitz_bucket", "gtceu:basalz_bucket"]
      t: |-
        LV Extractor, one per powder or one extractor with a filter: 1 powder → 144 mB molten (22 ticks, 30 EU/t). Pipe each fluid into its own drum with a pump cover to the IV Autoclave of the nether star chain; keep the four drums apart.
    - i: ["minecraft:blaze_powder", "gtceu:blaze_bucket"]
      t: Blaze powder goes through the same extractor to give molten blaze. The pack removes the vanilla blaze powder recipe, so look the source up in EMI before you build the fire line.
---
# Elemental powders: blizz, blitz, basalz from dust + gas, then molten powder for the nether star loop

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `elemental` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [Nether star loop and elemental powders](../../plan/p10.md#netherstar)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-iv" id="m-cr">
<div class="gt-head"><span class="gt-mname">IV Chemical Reactor or LCR with an IV hatch · 10 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cobalt dust (gtceu:cobalt_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__cobalt_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobalt Dust</span></span><span class="gt-slot gt-fluid" title="Fluorine (gtceu:fluorine_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__fluorine_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluorine</span></span><span class="gt-slot" title="Platinum dust (gtceu:platinum_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Dust</span></span><span class="gt-slot gt-fluid" title="Deuterium (gtceu:deuterium_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__deuterium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Deuterium</span></span><span class="gt-slot" title="Rhodium dust (gtceu:rhodium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Dust</span></span><span class="gt-slot gt-fluid" title="Helium (gtceu:helium_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__helium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Helium</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="16 Blizz powder (thermal:blizz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__blizz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blizz Powder</span><span class="gt-note">16 Blizz powder</span></span><span class="gt-slot" title="16 Blitz powder (thermal:blitz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__blitz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blitz Powder</span><span class="gt-note">16 Blitz powder</span></span><span class="gt-slot" title="16 Basalz powder (thermal:basalz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__basalz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basalz Powder</span><span class="gt-note">16 Basalz powder</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-ex">
<div class="gt-head"><span class="gt-mname">LV Extractor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="16 Blizz powder (thermal:blizz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__blizz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blizz Powder</span><span class="gt-note">16 Blizz powder</span></span><span class="gt-slot" title="16 Blitz powder (thermal:blitz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__blitz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blitz Powder</span><span class="gt-note">16 Blitz powder</span></span><span class="gt-slot" title="16 Basalz powder (thermal:basalz_powder)"><img class="gt-ico" src="../../assets/icons/thermal__basalz_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basalz Powder</span><span class="gt-note">16 Basalz powder</span></span><span class="gt-slot" title="Blaze powder (source unverified) (minecraft:blaze_powder) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__blaze_powder.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blaze Powder</span><span class="gt-note">Blaze powder (source unverified)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Liquid powders (144 mB each) (gtceu:blizz_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__blizz_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blizz Bucket</span><span class="gt-note">Liquid powders (144 mB each)</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_extractor</code></div>
</div>
</div>

## Flow

- [IV Chemical Reactor or LCR with an IV hatch · 10 s · 7680 EU/t](#m-cr) → [LV Extractor](#m-ex)

## How to build

1. Three dust drawers (cobalt, platinum, rhodium) and three gas drums (fluorine, deuterium, helium), each with a Modular Router or Pipez route and an Item Filter or fluid filter to the reactor. The three powders are three different recipes: give each its own filter pair so the reactor never sees two dusts at once. — `functionalstorage:oak_1`, `gtceu:cobalt_dust`, `gtceu:platinum_dust`, `gtceu:rhodium_dust`
2. IV Chemical Reactor (a single machine, 7680 EU/t from an IV cable; a Large Chemical Reactor would need an IV Energy Hatch instead): 1 cobalt dust + 1 B fluorine → 16 blizz powder in 10 s. A big output slot is needed: use an output bus or a Robot Arm cover that moves powder into a drawer, or the reactor stops at 64. — `gtceu:iv_chemical_reactor`, `thermal:blizz_powder`
3. Same machine type, second unit or the same reactor with a different drawer: 1 platinum dust + 1 B deuterium → 16 blitz powder (10 s, 7680 EU/t). Deuterium is a gas drum on a fluid hatch; check its tank before blaming the reactor. — `gtceu:iv_chemical_reactor`, `thermal:blitz_powder`
4. Third recipe: 1 rhodium dust + 1 B helium → 16 basalz powder (10 s, 7680 EU/t). Rhodium is the scarcest input of the three (the platinum group line), but one dust gives 16 powder, enough for 3 nether stars. — `gtceu:iv_chemical_reactor`, `thermal:basalz_powder`
5. LV Extractor, one per powder or one extractor with a filter: 1 powder → 144 mB molten (22 ticks, 30 EU/t). Pipe each fluid into its own drum with a pump cover to the IV Autoclave of the nether star chain; keep the four drums apart. — `gtceu:lv_extractor`, `gtceu:blizz_bucket`, `gtceu:blitz_bucket`, `gtceu:basalz_bucket`
6. Blaze powder goes through the same extractor to give molten blaze. The pack removes the vanilla blaze powder recipe, so look the source up in EMI before you build the fire line. — `minecraft:blaze_powder`, `gtceu:blaze_bucket`

## Tips

- Source: kubejs lines/nether\_stars.js. Each powder is a Chemical Reactor (or Large Chemical Reactor) recipe at 480 x 16 = 7680 EU/t: 1 dust + 1000 mB gas → 16 powder in 200 ticks (10 s). Cobalt dust + fluorine → blizz; platinum dust + deuterium → blitz; rhodium dust + helium → basalz. 7680 EU/t is an IV recipe: an IV Chemical Reactor (iv\_chemical\_reactor, fed by an IV cable) or a Large Chemical Reactor on an IV Energy Hatch.
- Molten powder: LV Extractor (30 EU/t, 22 ticks): 1 powder → 144 mB of the matching fluid; the old node said IV Extractor, which is not needed. Blaze powder has no recipe in the pack (the vanilla one is removed) and is the fourth powder: Unverified: where it comes from.
- Cost per nether star in powder: about 5.3 powder items of each of the 4 elements (4 × about 760 mB molten), so a single craft of 16 serves 3 stars. Rhodium for basalz is the rare input (platinum group line, 1 per 6 inert metal mixture); platinum dust for blitz and cobalt for blizz are plentiful. Fluorine is the slurry chain; deuterium and helium come from the air/hydrogen lines.
- A Macerator turns the Thermal rods back into powder (1 rod → 4 powder, 88 ticks, 2 EU/t): blizz, blitz and basalz rods from the Thermal mobs work too.
- The Heat Chamber that “energizes” molten powders in the same script is a LuV recipe (energized nether star shard + 1728 mB powder): do not plan it for IV.
- Sub-steps people skip: (1) each powder is its own dust + gas pair, so three machines or one machine with three drawers and filters, never a single mixed bus; (2) do not extract more molten powder than 5 items per run; extra just sits in the drum; (3) the reactor wants the gas as a fluid, in a hatch.
- **Unverified** the blaze powder source, and the exact supply of deuterium (the guide has no deuterium chain).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_chemical_reactor` | 1 |
| `gtceu:lv_extractor` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 5 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Needs:** [Rare Ore Residue](../mv/rare_residue.md), [Platinum group line: sludge → aqua regia centrifuge → platinum, palladium, rhodium, ruthenium, iridium, osmium](platline.md)
- **Main source for:** `gtceu:blaze_bucket`
