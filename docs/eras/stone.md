---
kind: era
id: stone
order: 10
data:
  id: stone
  tier: pre
  name: Stone Age
  sub: Ex Nihilo · starter island
  goal: From one tree to infinite water, cobble, sieved ores, wrought iron, glass and bricks.
  exit: ["gtceu:firebrick", "gtceu:coke_oven_brick", "minecraft:soul_sand", "gtceu:crushed_iron_ore"]
  steps:
    - i: ["minecraft:oak_sapling", "minecraft:stick"]
      t: Keep every sapling
      d: |-
        2 logs = 16 sticks, 8 logs = 4 chests (pack recipes). Make dirt with coarse dirt sieving before spending it.
    - i: ["minecraft:grass_block", "exnihilosequentia:stone_pebble", "minecraft:cobblestone"]
      t: Pebbles
      d: Sneak + right-click grass with an empty hand. 4 pebbles = 1 cobble.
    - i: ["exnihilosequentia:wooden_crook", "exnihilosequentia:silkworm", "minecraft:string"]
      t: String
      d: Crook leaves → silkworm → infest leaves → crook them for string.
    - i: ["exnihilosequentia:oak_sieve", "exnihilosequentia:string_mesh"]
      t: Sieves
      d: |-
        Place 6–8 together: one click works all adjacent sieves. String is the only mesh in this pack.
    - i: ["exnihilosequentia:stone_hammer", "minecraft:gravel", "minecraft:sand", "exnihilosequentia:dust"]
      t: Hammer chain
      d: Cobble → gravel → sand → dust. Each step sieves into different resources.
    - i: ["exnihilosequentia:oak_crucible", "woodenbucket:wooden_bucket"]
      t: Water
      d: Melt saplings/leaves in the crucible, scoop with the wooden bucket.
    - i: ["gtceu:barrel"]
      t: GT barrel modes
      d: Composting / transformation tabs on the left. Re-insert items after switching.
    - i: ["exnihilosequentia:porcelain_clay", "exnihilosequentia:fired_crucible", "minecraft:lava_bucket"]
      t: Lava
      d: Clay + bonemeal = porcelain. Fired crucible over a heat source melts cobble.
    - i: ["minecraft:campfire", "gtceu:wrought_iron_ingot", "minecraft:glass"]
      t: Campfire
      d: Iron → wrought iron (20 s). Glass dust → glass. Furnaces no longer make glass.
    - i: ["gtceu:brick_wooden_form", "gtceu:compressed_fireclay", "gtceu:firebrick"]
      t: Bricks
      d: Only compressed clay makes bricks now. The wooden form is never consumed.
  build:
    - id: exnihilosequentia:oak_sieve
      "n": "6–8"
    - id: gtceu:barrel
      "n": "3–4"
    - id: gtceu:stone_barrel
      "n": "2"
    - id: exnihilosequentia:fired_crucible
      "n": "2"
    - id: minecraft:campfire
      "n": "3"
    - id: thermal:device_water_gen
      "n": "1"
  setups: [inf_water, inf_cobble, inf_lava, sieve_manual, barrel, bricks]
  multis: ["gtceu:kiln"]
  storage:
    - i: ["functionalstorage:oak_1", "functionalstorage:storage_controller"]
      k: Bulk
      v: Drawers for cobble, gravel and every crushed ore.
    - i: ["minecraft:hopper"]
      k: Moving
      v: Hoppers under sieves and barrels.
    - i: ["minecraft:bucket"]
      k: Fluids
      v: Buckets until you have a Fluid Cell.
---
# Stone Age — Ex Nihilo · starter island

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Era id:** `stone` · **Tier:** `pre`

**Goal:** From one tree to infinite water, cobble, sieved ores, wrought iron, glass and bricks.

**Exit items:** `gtceu:firebrick`, `gtceu:coke_oven_brick`, `minecraft:soul_sand`, `gtceu:crushed_iron_ore`

## Steps

1. **Keep every sapling** — 2 logs = 16 sticks, 8 logs = 4 chests (pack recipes). Make dirt with coarse dirt sieving before spending it. (`minecraft:oak_sapling`, `minecraft:stick`)
2. **Pebbles** — Sneak + right-click grass with an empty hand. 4 pebbles = 1 cobble. (`minecraft:grass_block`, `exnihilosequentia:stone_pebble`, `minecraft:cobblestone`)
3. **String** — Crook leaves → silkworm → infest leaves → crook them for string. (`exnihilosequentia:wooden_crook`, `exnihilosequentia:silkworm`, `minecraft:string`)
4. **Sieves** — Place 6–8 together: one click works all adjacent sieves. String is the only mesh in this pack. (`exnihilosequentia:oak_sieve`, `exnihilosequentia:string_mesh`)
5. **Hammer chain** — Cobble → gravel → sand → dust. Each step sieves into different resources. (`exnihilosequentia:stone_hammer`, `minecraft:gravel`, `minecraft:sand`, `exnihilosequentia:dust`)
6. **Water** — Melt saplings/leaves in the crucible, scoop with the wooden bucket. (`exnihilosequentia:oak_crucible`, `woodenbucket:wooden_bucket`)
7. **GT barrel modes** — Composting / transformation tabs on the left. Re-insert items after switching. (`gtceu:barrel`)
8. **Lava** — Clay + bonemeal = porcelain. Fired crucible over a heat source melts cobble. (`exnihilosequentia:porcelain_clay`, `exnihilosequentia:fired_crucible`, `minecraft:lava_bucket`)
9. **Campfire** — Iron → wrought iron (20 s). Glass dust → glass. Furnaces no longer make glass. (`minecraft:campfire`, `gtceu:wrought_iron_ingot`, `minecraft:glass`)
10. **Bricks** — Only compressed clay makes bricks now. The wooden form is never consumed. (`gtceu:brick_wooden_form`, `gtceu:compressed_fireclay`, `gtceu:firebrick`)

## Machines to build

| Machine | Count |
| --- | ---: |
| `exnihilosequentia:oak_sieve` | 6–8 |
| `gtceu:barrel` | 3–4 |
| `gtceu:stone_barrel` | 2 |
| `exnihilosequentia:fired_crucible` | 2 |
| `minecraft:campfire` | 3 |
| `thermal:device_water_gen` | 1 |

## Setups

- [Infinite water](../chains/stone/inf_water.md)
- [Infinite cobble &amp; blackstone](../chains/stone/inf_cobble.md)
- [Infinite lava, obsidian &amp; pebbles](../chains/stone/inf_lava.md)
- [Sieve station (manual)](../chains/stone/sieve_manual.md)
- [Barrel transformations](../chains/stone/barrel.md)
- [Firebricks &amp; coke oven bricks](../chains/stone/bricks.md)

## Storage

- **Bulk:** Drawers for cobble, gravel and every crushed ore. (`functionalstorage:oak_1`, `functionalstorage:storage_controller`)
- **Moving:** Hoppers under sieves and barrels. (`minecraft:hopper`)
- **Fluids:** Buckets until you have a Fluid Cell. (`minecraft:bucket`)

## Multiblocks

`gtceu:kiln`

## Plan phases

- [Stone age](../plan/p0.md)
