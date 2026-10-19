---
kind: chain
id: magnets
order: 860
data:
  t: "Magnets: from magnetite block to Fluxuated Magnetite"
  inf: true
  "n":
    - [fe, Iron ingot, i, "minecraft:iron_ingot"]
    - [p1, "Polarizer (2 passes)", m, "gtceu:lv_polarizer"]
    - [oi, Overcharged iron, x, "create_new_age:overcharged_iron"]
    - [au, Gold ingot, i, "minecraft:gold_ingot"]
    - [p2, Polarizer, m, "gtceu:lv_polarizer"]
    - [og, Overcharged gold, x, "create_new_age:overcharged_gold"]
    - [be, Bender, m, "gtceu:lv_bender"]
    - [ois, Overcharged iron sheet, x, "create_new_age:overcharged_iron_sheet"]
    - [ogs, Overcharged golden sheet, x, "create_new_age:overcharged_golden_sheet"]
    - [di, Diamond, i, "minecraft:diamond"]
    - [p3, Polarizer, m, "gtceu:lv_polarizer"]
    - [od, Overcharged diamond, x, "create_new_age:overcharged_diamond"]
    - [md, Magnetite dust, i, "gtceu:magnetite_dust"]
    - [sto, Stone, i, "minecraft:stone"]
    - [mb, Magnetite Block, x, "create_new_age:magnetite_block"]
    - [ra, Red alloy ingot, i, "gtceu:red_alloy_ingot"]
    - [rm, Redstone Magnet, x, "create_new_age:redstone_magnet"]
    - [lm, Layered Magnet, x, "create_new_age:layered_magnet"]
    - [fm, "2 Fluxuated Magnetite", o, "create_new_age:fluxuated_magnetite"]
  e:
    - [fe, p1]
    - [p1, oi]
    - [oi, be]
    - [au, p2]
    - [p2, og]
    - [og, be]
    - [be, ois]
    - [be, ogs]
    - [di, p3]
    - [p3, od]
    - [md, mb, "4"]
    - [sto, mb, "5"]
    - [mb, rm]
    - [md, rm, "4"]
    - [ra, rm, "4"]
    - [rm, lm]
    - [ois, lm, "4"]
    - [ogs, lm, "4"]
    - [lm, fm]
    - [ogs, fm, "4"]
    - [mb, fm, "2"]
    - [od, fm, "2"]
  tips:
    - |-
      Magnetic force: magnetite block 1, redstone magnet 2, layered 4, fluxuated 8, large neodymium 24. A coil takes up to 12 magnets; magnets can be shared between coils.
    - |-
      Per Fluxuated Magnetite: 4 gold, 2 iron, 1 diamond, 8 magnetite dust, 7.5 stone, 2 red alloy. A full coil (12) = 48 gold, 24 iron, 12 diamonds, 96 magnetite dust, 24 red alloy.
    - |-
      Magnetite block and redstone magnet need no power: start the coils with those, then swap to fluxuated magnetite once the LV polarizer and bender run.
  b: [["gtceu:lv_polarizer", 1], ["gtceu:lv_bender", 1], ["functionalstorage:oak_1", 6]]
  how:
    - i: ["create_new_age:magnetite_block", "gtceu:magnetite_dust"]
      t: |-
        Magnetite Block (crafting): 5 stone + 4 magnetite dust. Magnetite dust: macerate the crushed magnetite from the gravel sieve.
    - i: ["create_new_age:redstone_magnet", "gtceu:red_alloy_ingot"]
      t: |-
        Redstone Magnet (crafting): 1 magnetite block + 4 red alloy ingots + 4 magnetite dust. No power needed.
    - i: ["gtceu:lv_polarizer", "gtceu:magnetic_iron_ingot", "create_new_age:overcharged_iron"]
      t: |-
        Overcharged iron: polarize an iron ingot into a magnetic iron ingot, then polarize again (0.8 s, 16 EU/t). Overcharged gold: polarize a gold ingot (1.6 s). Overcharged diamond: polarize a diamond (8 s).
    - i: ["gtceu:lv_bender", "create_new_age:overcharged_iron_sheet", "create_new_age:overcharged_golden_sheet"]
      t: |-
        Bender at 24 EU/t: overcharged iron → overcharged iron sheet (2.4 s); overcharged gold → overcharged golden sheet (9.8 s).
    - i: ["create_new_age:layered_magnet"]
      t: |-
        Layered Magnet (crafting): 1 redstone magnet + 4 overcharged iron sheets + 4 overcharged golden sheets.
    - i: ["create_new_age:fluxuated_magnetite"]
      t: |-
        Fluxuated Magnetite (crafting, makes 2): 1 layered magnet + 2 magnetite blocks + 2 overcharged diamonds + 4 overcharged golden sheets.
    - i: ["minecraft:raw_gold", "minecraft:diamond"]
      t: Gold comes from the Void Extractor (raw gold), diamonds from the sand sieve, red alloy from copper + redstone (dust sieve) in the alloy smelter.
---
# Magnets: from magnetite block to Fluxuated Magnetite

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `magnets` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Steam engines + generator coils](../../plan/p1.md#power)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-p1">
<div class="gt-head"><span class="gt-mname">Polarizer (2 passes)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron ingot (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Overcharged iron (create_new_age:overcharged_iron)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_iron.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Iron</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_polarizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-p2">
<div class="gt-head"><span class="gt-mname">Polarizer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gold ingot (minecraft:gold_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__gold_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Overcharged gold (create_new_age:overcharged_gold)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_gold.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Gold</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_polarizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">Bender</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Overcharged iron (create_new_age:overcharged_iron)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_iron.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Iron</span></span><span class="gt-slot" title="Overcharged gold (create_new_age:overcharged_gold)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_gold.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Gold</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Overcharged iron sheet (create_new_age:overcharged_iron_sheet)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_iron_sheet.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Iron Sheet</span></span><span class="gt-slot" title="Overcharged golden sheet (create_new_age:overcharged_golden_sheet)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_golden_sheet.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Golden Sheet</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-p3">
<div class="gt-head"><span class="gt-mname">Polarizer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Diamond (minecraft:diamond)"><img class="gt-ico" src="../../assets/icons/minecraft__diamond.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diamond</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Overcharged diamond (create_new_age:overcharged_diamond)"><img class="gt-ico" src="../../assets/icons/create_new_age__overcharged_diamond.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Overcharged Diamond</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_polarizer</code></div>
</div>
</div>

## Flow

- [Polarizer (2 passes)](#m-p1) → [Bender](#m-be)
- [Polarizer](#m-p2) → [Bender](#m-be)
- [Polarizer](#m-p3)

### Direct steps

- Magnetite dust → Magnetite Block (4)
- Stone → Magnetite Block (5)
- Magnetite Block → Redstone Magnet
- Magnetite dust → Redstone Magnet (4)
- Red alloy ingot → Redstone Magnet (4)
- Redstone Magnet → Layered Magnet
- Overcharged iron sheet → Layered Magnet (4)
- Overcharged golden sheet → Layered Magnet (4)
- Layered Magnet → 2 Fluxuated Magnetite
- Overcharged golden sheet → 2 Fluxuated Magnetite (4)
- Magnetite Block → 2 Fluxuated Magnetite (2)
- Overcharged diamond → 2 Fluxuated Magnetite (2)

## How to build

1. Magnetite Block (crafting): 5 stone + 4 magnetite dust. Magnetite dust: macerate the crushed magnetite from the gravel sieve. — `create_new_age:magnetite_block`, `gtceu:magnetite_dust`
2. Redstone Magnet (crafting): 1 magnetite block + 4 red alloy ingots + 4 magnetite dust. No power needed. — `create_new_age:redstone_magnet`, `gtceu:red_alloy_ingot`
3. Overcharged iron: polarize an iron ingot into a magnetic iron ingot, then polarize again (0.8 s, 16 EU/t). Overcharged gold: polarize a gold ingot (1.6 s). Overcharged diamond: polarize a diamond (8 s). — `gtceu:lv_polarizer`, `gtceu:magnetic_iron_ingot`, `create_new_age:overcharged_iron`
4. Bender at 24 EU/t: overcharged iron → overcharged iron sheet (2.4 s); overcharged gold → overcharged golden sheet (9.8 s). — `gtceu:lv_bender`, `create_new_age:overcharged_iron_sheet`, `create_new_age:overcharged_golden_sheet`
5. Layered Magnet (crafting): 1 redstone magnet + 4 overcharged iron sheets + 4 overcharged golden sheets. — `create_new_age:layered_magnet`
6. Fluxuated Magnetite (crafting, makes 2): 1 layered magnet + 2 magnetite blocks + 2 overcharged diamonds + 4 overcharged golden sheets. — `create_new_age:fluxuated_magnetite`
7. Gold comes from the Void Extractor (raw gold), diamonds from the sand sieve, red alloy from copper + redstone (dust sieve) in the alloy smelter. — `minecraft:raw_gold`, `minecraft:diamond`

## Tips

- Magnetic force: magnetite block 1, redstone magnet 2, layered 4, fluxuated 8, large neodymium 24. A coil takes up to 12 magnets; magnets can be shared between coils.
- Per Fluxuated Magnetite: 4 gold, 2 iron, 1 diamond, 8 magnetite dust, 7.5 stone, 2 red alloy. A full coil (12) = 48 gold, 24 iron, 12 diamonds, 96 magnetite dust, 24 red alloy.
- Magnetite block and redstone magnet need no power: start the coils with those, then swap to fluxuated magnetite once the LV polarizer and bender run.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_polarizer` | 1 |
| `gtceu:lv_bender` | 1 |
| `functionalstorage:oak_1` | 6 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](ingots.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
- **Feeds:** [Create steam power: Steam Engines + Generator Coils](../steam/power_steam_engine.md)
- **Main source for:** `create_new_age:fluxuated_magnetite`
