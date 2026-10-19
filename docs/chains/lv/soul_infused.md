---
kind: chain
id: soul_infused
order: 2270
data:
  t: |-
    Soul infused ingots (LV superconductor): sand → soul sand → dust + invar
  inf: true
  "n":
    - [sa, "Sand (sieve block)", i, "minecraft:sand"]
    - [ww, "Witch water · 250 mB per sand", f, "exnihilosequentia:witch_water_bucket"]
    - [lb, "Large Barrel · no spores", m, "gtceu:large_barrel"]
    - [ss, Soul sand, x, "minecraft:soul_sand"]
    - [ma, LV Macerator, m, "gtceu:lv_macerator"]
    - [sd, Soul sand dust, x, "thermal_extra:soul_sand_dust"]
    - [fe, "Iron dust · 2", i, "gtceu:iron_dust"]
    - [ni, "Nickel dust · 1", i, "gtceu:nickel_dust"]
    - [a1, "Alloy Smelter · invar", m, "gtceu:lv_alloy_smelter"]
    - [iv, Invar ingot, x, "gtceu:invar_ingot"]
    - [a2, "Alloy Smelter · soul infused", m, "gtceu:lv_alloy_smelter"]
    - [si, "Soul infused ingot · 3 per run", o, "gtceu:soul_infused_ingot"]
  e:
    - [sa, lb, "1 each"]
    - [ww, lb, "250 mB"]
    - [lb, ss, "5 ticks"]
    - [ss, ma]
    - [ma, sd, "1 s"]
    - [sd, a2, "2 per run"]
    - [fe, a1, "2"]
    - [ni, a1, "1"]
    - [a1, iv, "3 per 7.5 s"]
    - [iv, a2, "1 per run"]
    - [a2, si, "10 s"]
  tips:
    - |-
      Recipes (superconductors.js, only loaded when Thermal Extra is in the pack, and ThermalExtra-3.3.1 is in mods): Alloy Smelter, 1 invar (dust OR ingot) + 2 thermal_extra:soul_sand_dust → 3 soul infused ingots, 200 ticks, 8 EU/t. Macerator: 1 soul sand → 1 soul sand dust, 20 ticks, 8 EU/t. Invar: GT Alloy Smelter 2 iron + 1 nickel → 3 invar, 150 ticks, 16 EU/t (dust or ingot forms all work).
    - |-
      Per minute at base speed: 1 LV Macerator = 60 soul sand dust. 1 soul infused Alloy Smelter = 6 runs = 18 ingots, eating 12 dust + 6 invar. 1 invar Alloy Smelter = 8 runs = 24 invar from 16 iron + 8 nickel dust. A Large Barrel makes 12 soul sand a second, so it is never the limit.
    - |-
      How many machines: 1 stack (64) an hour = 22 runs = 4 minutes of ONE soul smelter, 44 soul sand dust, 44 sand, 11 B of witch water and 8 invar runs (16 iron + 8 nickel dust, about 18 crushed iron ore through the ore factory). 1 stack a minute = 4 soul smelters + 1 macerator + 1 invar smelter. One of each machine is plenty until you build soul infused casings in bulk.
    - |-
      Sub-steps people skip: (1) the soul infused smelter takes invar INGOT or invar DUST: do not add a second step to make dust. (2) Soul sand dust is thermal_extra:soul_sand_dust, not a GregTech dust: set filters and covers to that exact item. (3) Soul sand sifting is removed and the Nether is not needed: sand + witch water in a barrel makes it. (4) The hand, Create heated mixer and shapeless recipes give 1 ingot from 2 dust + 1 invar, one third of the alloy smelter.
    - |-
      Keep the soul sand Large Barrel separate from the witch water Large Barrel: the witch water recipe needs mycelium spores in the bus, the soul sand one must not have them. Feed it witch water by a Pipez fluid pipe from the barrel in the sieve block (15 B a minute is 5 smelters worth, and blackstone shares it).
    - |-
      Bootstrap: the Void Extractor is made with soul infused hex wire, so the first nickel cannot come from it. Use the electric ore factory (iron ore gives 45 % nickel dust, copper ore 32.5 %; 160 ticks per ore). The extractor cluster (3 raw pentlandite at 30 %) only matters later.
    - |-
      The three consumers that matter: (1) soul infused wire: the LV superconductor cable and the LV Energy Converter (4 A) your whole LV power line needs, plus the Void Extractor (hex wire). (2) soul infused plate and gear: Functional Storage void upgrade, LaserIO energy card, Thermal LV augment kits. (3) soul infused casing (6 plates + frame, kubejs:soul_infused_casing: Runic Circuitry Assembling Station) and the ultimate casing true_revitilization (1728 mB soul infused in the Hell Forge). Soul infused glass (144 mB + tempered glass, LV) also needs it.
    - |-
      Steam also works: a High Pressure Steam Alloy Smelter runs both recipes (8 and 16 EU/t are inside the LV limit), so this line can start before the LV power grid.
    - |-
      Unverified: whether an LV (non-steam) Alloy Smelter overclocks the 8 EU/t recipe to 100 ticks at 32 EU/t (double the rates above); plan on the base 10 s. Unverified: parallels of the electric ore factory; ingots per soul infused hex wire in the wiremill and assembler. Unverified: the Large Barrel pipe layout (item output bus into the drawer, fluid hatch for witch water) from the multiblock card, not from a live build.
  store: ["functionalstorage:oak_1"]
  b:
    - ["gtceu:lv_alloy_smelter", 2]
    - ["gtceu:lv_macerator", 1]
    - ["gtceu:large_barrel", 1]
    - ["functionalstorage:oak_1", 8]
    - ["pipez:item_pipe", 32]
    - ["pipez:fluid_pipe", 8]
    - ["modularrouters:modular_router", 2]
    - ["gtceu:lv_robot_arm", 2]
    - ["gtceu:item_filter", 4]
  how:
    - i: ["minecraft:sand", "functionalstorage:oak_1"]
      t: |-
        Sand: a spare sand drawer from the sieve block (the sand hammer line makes 96 a minute and the sieves only need what they eat). Run a Pipez item pipe or a Modular Router from the sand drawer to the Large Barrel item bus. One soul sand needs one sand, so 12 sand a minute per soul smelter.
    - i: ["gtceu:large_barrel", "exnihilosequentia:witch_water_bucket"]
      t: |-
        Large Barrel for soul sand: 9 pump decks + treated wood planks, an item input bus, an item output bus and a fluid input hatch. NO mycelium spores in it. Pipe witch water from the sieve block barrel (Pipez fluid pipe): 250 mB + 1 sand → 1 soul sand every 5 ticks. The output bus goes straight into a soul sand drawer.
    - i: ["minecraft:soul_sand", "gtceu:lv_macerator", "thermal_extra:soul_sand_dust"]
      t: |-
        Soul sand drawer → LV Macerator (filtered pipe, soul sand only): 1 soul sand → 1 soul sand dust, 20 ticks, 8 EU/t. Its output goes into a soul sand dust drawer. Put a Robot Arm cover (Keep Exact, Item Filter = soul sand dust, 64) on the output so it stops when full.
    - i: ["gtceu:iron_dust", "gtceu:nickel_dust", "gtceu:lv_alloy_smelter", "gtceu:invar_ingot"]
      t: |-
        Invar: iron dust and nickel dust come from the electric ore factory drawers (ores line). Two drawers feed ONE LV Alloy Smelter (no circuit needed): 2 iron dust + 1 nickel dust → 3 invar ingots in 7.5 s. The smelter outputs into an invar drawer. A Robot Arm cover Keep Exact 64 on the output caps the stock.
    - i: ["gtceu:lv_alloy_smelter", "thermal_extra:soul_sand_dust", "gtceu:invar_ingot"]
      t: |-
        The soul infused smelter is a second, dedicated LV Alloy Smelter. Two filtered pipes (or Modular Routers with one filter each): soul sand dust drawer and invar drawer. 2 dust + 1 invar → 3 soul infused ingots every 10 s at 8 EU/t.
    - i: ["gtceu:soul_infused_ingot", "functionalstorage:oak_1", "gtceu:lv_robot_arm", "gtceu:item_filter"]
      t: |-
        Stock: output into a drawer with a Robot Arm cover in Keep Exact mode and an Item Filter holding soul infused ingot and 64. The smelter then just pauses when the drawer is full and draws no power.
    - i: ["gtceu:lv_4a_energy_converter", "gtceu:soul_infused_single_wire"]
      t: |-
        Power: the whole line uses under 60 EU/t (macerator 8, soul smelter 8, invar smelter 16): one branch of your LV net is enough. Use the first ingots for soul infused wire (the LV energy converter and the Void Extractor need it).
---
# Soul infused ingots (LV superconductor): sand → soul sand → dust + invar

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `soul_infused` · **Tags:** Infinite source, Unverified

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Soul infused ingots (LV superconductor)](../../plan/p2.md#soul_infused)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lb">
<div class="gt-head"><span class="gt-mname">Large Barrel · no spores</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sand (sieve block) (minecraft:sand) - 1 each"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span><span class="gt-note">Sand (sieve block)</span><b class="gt-q">1 each</b></span><span class="gt-slot gt-fluid" title="Witch water · 250 mB per sand (exnihilosequentia:witch_water_bucket) - 250 mB"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__witch_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Witch Water</span><span class="gt-note">Witch water · 250 mB per sand</span><b class="gt-q">250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Soul sand (minecraft:soul_sand) - 5 ticks"><img class="gt-ico" src="../../assets/icons/minecraft__soul_sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Sand</span><b class="gt-q">5 ticks</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-ma">
<div class="gt-head"><span class="gt-mname">LV Macerator</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Soul sand (minecraft:soul_sand)"><img class="gt-ico" src="../../assets/icons/minecraft__soul_sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Sand</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">1 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Soul sand dust (thermal_extra:soul_sand_dust) - 1 s"><img class="gt-ico" src="../../assets/icons/thermal_extra__soul_sand_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Sand Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_macerator</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">Alloy Smelter · invar</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron dust · 2 (gtceu:iron_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><span class="gt-note">Iron dust · 2</span><b class="gt-q">2</b></span><span class="gt-slot" title="Nickel dust · 1 (gtceu:nickel_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Dust</span><span class="gt-note">Nickel dust · 1</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_alloy_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Invar ingot (gtceu:invar_ingot) - 3 per 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__invar_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Invar Ingot</span><b class="gt-q">3 per 7.5 s</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_alloy_smelter</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">Alloy Smelter · soul infused</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Soul sand dust (thermal_extra:soul_sand_dust) - 2 per run"><img class="gt-ico" src="../../assets/icons/thermal_extra__soul_sand_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Sand Dust</span><b class="gt-q">2 per run</b></span><span class="gt-slot" title="Invar ingot (gtceu:invar_ingot) - 1 per run"><img class="gt-ico" src="../../assets/icons/gtceu__invar_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Invar Ingot</span><b class="gt-q">1 per run</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_alloy_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Soul infused ingot · 3 per run (gtceu:soul_infused_ingot) - 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__soul_infused_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Soul Infused Ingot</span><span class="gt-note">Soul infused ingot · 3 per run</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_alloy_smelter</code></div>
</div>
</div>

## Flow

- [Large Barrel · no spores](#m-lb) → [LV Macerator](#m-ma) → [Alloy Smelter · soul infused](#m-a2)
- [Alloy Smelter · invar](#m-a1) → [Alloy Smelter · soul infused](#m-a2)

## How to build

1. Sand: a spare sand drawer from the sieve block (the sand hammer line makes 96 a minute and the sieves only need what they eat). Run a Pipez item pipe or a Modular Router from the sand drawer to the Large Barrel item bus. One soul sand needs one sand, so 12 sand a minute per soul smelter. — `minecraft:sand`, `functionalstorage:oak_1`
2. Large Barrel for soul sand: 9 pump decks + treated wood planks, an item input bus, an item output bus and a fluid input hatch. NO mycelium spores in it. Pipe witch water from the sieve block barrel (Pipez fluid pipe): 250 mB + 1 sand → 1 soul sand every 5 ticks. The output bus goes straight into a soul sand drawer. — `gtceu:large_barrel`, `exnihilosequentia:witch_water_bucket`
3. Soul sand drawer → LV Macerator (filtered pipe, soul sand only): 1 soul sand → 1 soul sand dust, 20 ticks, 8 EU/t. Its output goes into a soul sand dust drawer. Put a Robot Arm cover (Keep Exact, Item Filter = soul sand dust, 64) on the output so it stops when full. — `minecraft:soul_sand`, `gtceu:lv_macerator`, `thermal_extra:soul_sand_dust`
4. Invar: iron dust and nickel dust come from the electric ore factory drawers (ores line). Two drawers feed ONE LV Alloy Smelter (no circuit needed): 2 iron dust + 1 nickel dust → 3 invar ingots in 7.5 s. The smelter outputs into an invar drawer. A Robot Arm cover Keep Exact 64 on the output caps the stock. — `gtceu:iron_dust`, `gtceu:nickel_dust`, `gtceu:lv_alloy_smelter`, `gtceu:invar_ingot`
5. The soul infused smelter is a second, dedicated LV Alloy Smelter. Two filtered pipes (or Modular Routers with one filter each): soul sand dust drawer and invar drawer. 2 dust + 1 invar → 3 soul infused ingots every 10 s at 8 EU/t. — `gtceu:lv_alloy_smelter`, `thermal_extra:soul_sand_dust`, `gtceu:invar_ingot`
6. Stock: output into a drawer with a Robot Arm cover in Keep Exact mode and an Item Filter holding soul infused ingot and 64. The smelter then just pauses when the drawer is full and draws no power. — `gtceu:soul_infused_ingot`, `functionalstorage:oak_1`, `gtceu:lv_robot_arm`, `gtceu:item_filter`
7. Power: the whole line uses under 60 EU/t (macerator 8, soul smelter 8, invar smelter 16): one branch of your LV net is enough. Use the first ingots for soul infused wire (the LV energy converter and the Void Extractor need it). — `gtceu:lv_4a_energy_converter`, `gtceu:soul_infused_single_wire`

## Tips

- Recipes (superconductors.js, only loaded when Thermal Extra is in the pack, and ThermalExtra-3.3.1 is in mods): Alloy Smelter, 1 invar (dust OR ingot) + 2 thermal\_extra:soul\_sand\_dust → 3 soul infused ingots, 200 ticks, 8 EU/t. Macerator: 1 soul sand → 1 soul sand dust, 20 ticks, 8 EU/t. Invar: GT Alloy Smelter 2 iron + 1 nickel → 3 invar, 150 ticks, 16 EU/t (dust or ingot forms all work).
- Per minute at base speed: 1 LV Macerator = 60 soul sand dust. 1 soul infused Alloy Smelter = 6 runs = 18 ingots, eating 12 dust + 6 invar. 1 invar Alloy Smelter = 8 runs = 24 invar from 16 iron + 8 nickel dust. A Large Barrel makes 12 soul sand a second, so it is never the limit.
- How many machines: 1 stack (64) an hour = 22 runs = 4 minutes of ONE soul smelter, 44 soul sand dust, 44 sand, 11 B of witch water and 8 invar runs (16 iron + 8 nickel dust, about 18 crushed iron ore through the ore factory). 1 stack a minute = 4 soul smelters + 1 macerator + 1 invar smelter. One of each machine is plenty until you build soul infused casings in bulk.
- Sub-steps people skip: (1) the soul infused smelter takes invar INGOT or invar DUST: do not add a second step to make dust. (2) Soul sand dust is thermal\_extra:soul\_sand\_dust, not a GregTech dust: set filters and covers to that exact item. (3) Soul sand sifting is removed and the Nether is not needed: sand + witch water in a barrel makes it. (4) The hand, Create heated mixer and shapeless recipes give 1 ingot from 2 dust + 1 invar, one third of the alloy smelter.
- Keep the soul sand Large Barrel separate from the witch water Large Barrel: the witch water recipe needs mycelium spores in the bus, the soul sand one must not have them. Feed it witch water by a Pipez fluid pipe from the barrel in the sieve block (15 B a minute is 5 smelters worth, and blackstone shares it).
- Bootstrap: the Void Extractor is made with soul infused hex wire, so the first nickel cannot come from it. Use the electric ore factory (iron ore gives 45 % nickel dust, copper ore 32.5 %; 160 ticks per ore). The extractor cluster (3 raw pentlandite at 30 %) only matters later.
- The three consumers that matter: (1) soul infused wire: the LV superconductor cable and the LV Energy Converter (4 A) your whole LV power line needs, plus the Void Extractor (hex wire). (2) soul infused plate and gear: Functional Storage void upgrade, LaserIO energy card, Thermal LV augment kits. (3) soul infused casing (6 plates + frame, kubejs:soul\_infused\_casing: Runic Circuitry Assembling Station) and the ultimate casing true\_revitilization (1728 mB soul infused in the Hell Forge). Soul infused glass (144 mB + tempered glass, LV) also needs it.
- Steam also works: a High Pressure Steam Alloy Smelter runs both recipes (8 and 16 EU/t are inside the LV limit), so this line can start before the LV power grid.
- **Unverified** whether an LV (non-steam) Alloy Smelter overclocks the 8 EU/t recipe to 100 ticks at 32 EU/t (double the rates above); plan on the base 10 s. Unverified: parallels of the electric ore factory; ingots per soul infused hex wire in the wiremill and assembler. Unverified: the Large Barrel pipe layout (item output bus into the drawer, fluid hatch for witch water) from the multiblock card, not from a live build.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_alloy_smelter` | 2 |
| `gtceu:lv_macerator` | 1 |
| `gtceu:large_barrel` | 1 |
| `functionalstorage:oak_1` | 8 |
| `pipez:item_pipe` | 32 |
| `pipez:fluid_pipe` | 8 |
| `modularrouters:modular_router` | 2 |
| `gtceu:lv_robot_arm` | 2 |
| `gtceu:item_filter` | 4 |

## Storage

`functionalstorage:oak_1`

## Needs / Feeds

- **Needs:** [Infinite gems (sand sieve)](../feeders/sieve_sand.md), [Ore processing](ores.md)
- **Main source for:** `gtceu:soul_infused_ingot`, `gtceu:soul_infused_dust`, `minecraft:soul_sand`, `thermal_extra:soul_sand_dust`
