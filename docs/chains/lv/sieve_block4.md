---
kind: chain
id: sieve_block4
order: 680
data:
  t: Four-sieve block (gravel, sand, dust, blackstone)
  inf: true
  hero: true
  "n":
    - [acc, "Water (Aqueous Accumulators)", s, "thermal:device_water_gen"]
    - [lb, "Large Barrel · spores kept", m, "gtceu:large_barrel"]
    - [sbc, "4 Stone Barrels · cobble", m, "gtceu:stone_barrel"]
    - [sbb, "2 Stone Barrels · blackstone", m, "gtceu:stone_barrel"]
    - [h1, "3 Forge Hammers", m, "gtceu:lv_forge_hammer"]
    - [h2, "2 Forge Hammers", m, "gtceu:lv_forge_hammer"]
    - [h3, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [h4, Forge Hammer, m, "gtceu:lv_forge_hammer"]
    - [s1, "Sieve · gravel", m, "gtceu:mechanical_sieve"]
    - [s2, "Sieve · sand", m, "gtceu:mechanical_sieve"]
    - [s3, "Sieve · dust", m, "gtceu:mechanical_sieve"]
    - [s4, "Sieve · blackstone", m, "gtceu:mechanical_sieve"]
    - [o1, Crushed Copper, o, "gtceu:crushed_copper_ore"]
    - [o2, Crushed Iron, o, "gtceu:crushed_iron_ore"]
    - [o3, Crushed Tin, o, "gtceu:crushed_tin_ore"]
    - [o4, Crushed Sphalerite, o, "gtceu:crushed_sphalerite_ore"]
    - [o5, Crushed Magnetite, o, "gtceu:crushed_magnetite_ore"]
    - [g1, Quartz, o, "minecraft:quartz"]
    - [g2, Lapis, o, "minecraft:lapis_lazuli"]
    - [g3, Amethyst, o, "minecraft:amethyst_shard"]
    - [g4, Emerald, o, "minecraft:emerald"]
    - [d1, Redstone, o, "minecraft:redstone"]
    - [d2, Glowstone, o, "minecraft:glowstone_dust"]
    - [d3, Sulfur, o, "gtceu:sulfur_dust"]
    - [d4, Ender Pearl, o, "minecraft:ender_pearl"]
    - [b1, Crushed Galena, o, "gtceu:crushed_galena_ore"]
    - [b2, Crushed Stibnite, o, "gtceu:crushed_stibnite_ore"]
    - [ld, "Lapidary Dynamo + LV kit", p, "thermal:dynamo_lapidary"]
    - [cv, "2 LV 4A Converters", p, "gtceu:lv_4a_energy_converter"]
  e:
    - [acc, sbc, water]
    - [acc, lb, water]
    - [lb, sbb, witch water]
    - [sbc, h1, cobble]
    - [sbb, h4, blackstone]
    - [h1, s1, gravel]
    - [h1, h2, gravel]
    - [h2, s2, sand]
    - [h2, h3, sand]
    - [h3, s3, dust]
    - [h4, s4, crushed]
    - [s1, o1, "×16"]
    - [s1, o2, "×16"]
    - [s1, o3, "×16"]
    - [s1, o4, "×16"]
    - [s1, o5, "×16"]
    - [s2, g1, "×16"]
    - [s2, g2, "×16"]
    - [s2, g3, "×16"]
    - [s2, g4, "×16"]
    - [s2, ld, diamonds]
    - [s3, d1, "×16"]
    - [s3, d2, "×16"]
    - [s3, d3, "×4"]
    - [s3, d4, "×4"]
    - [s4, b1, "×16"]
    - [s4, b2, "×16"]
    - [ld, cv, FE]
  tips:
    - Every sieve eats 64 blocks per 40 s = 96 per minute. Amounts shown are per 40 s batch.
    - The whole block draws about 210 EU/t (232 at peak). Before you have a Lapidary Dynamo, power it with Steam Engines + Generator Coils (see the power options).
    - |-
      Witch water is the slow part: full speed on the blackstone sieve needs 96 B per minute (7 Large Barrels). Two barrels run it about a third of the time.
  b:
    - ["thermal:device_water_gen", 4]
    - ["gtceu:large_barrel", 2]
    - ["exnihilosequentia:mycelium_spores", 2]
    - ["gtceu:stone_barrel", 6]
    - ["minecraft:lava_bucket", 6]
    - ["gtceu:lv_forge_hammer", 7]
    - ["gtceu:mechanical_sieve", 4]
    - ["exnihilosequentia:string_mesh", 4]
    - ["thermal:dynamo_lapidary", 1]
    - ["kubejs:lv_upgrade_kit", 1]
    - ["gtceu:lv_4a_energy_converter", 2]
    - ["gtceu:soul_infused_quadruple_wire", 8]
    - ["functionalstorage:oak_1", 8]
    - ["pipez:item_pipe", 32]
    - ["pipez:fluid_pipe", 16]
  how:
    - i: ["thermal:device_water_gen", "pipez:fluid_pipe"]
      t: Water first. Each Stone Barrel drinks 1 B per block, so 4 cobble barrels need 320 B per minute (about 270 mB/t). One Aqueous Accumulator keeps two barrels busy (your current line), so use 4, or fewer with an LV Upgrade Kit inside. Run Pipez fluid pipes to every barrel.
    - i: ["gtceu:stone_barrel", "minecraft:lava_bucket"]
      t: |-
        4 Stone Barrels with a lava bucket inside (kept) and ghost circuit 0: 4 × 80 = 320 cobble per minute. The block needs 288 (96 for each of the gravel, sand and dust sieves).
    - i: ["gtceu:large_barrel", "exnihilosequentia:mycelium_spores"]
      t: |-
        Witch water: a Large Barrel with mycelium spores in its input bus (kept) turns 1 B of water into 1 B of witch water every 4 s, 15 B per minute.
    - i: ["gtceu:stone_barrel", "minecraft:blackstone"]
      t: |-
        2 more Stone Barrels with lava kept and witch water piped in make blackstone (1 B witch water each). They are only as fast as the witch water: 2 Large Barrels give 30 blackstone per minute; 7 would feed the sieve at full speed (96).
    - i: ["gtceu:lv_forge_hammer"]
      t: |-
        3 Forge Hammers turn cobble into gravel (0.5 s and 16 EU/t each, 120 per minute per hammer, 360 total for the 288 needed). Barrels auto-output into a drawer; Pipez item pipes in round-robin feed the hammers.
    - i: ["minecraft:gravel", "functionalstorage:oak_1"]
      t: |-
        The gravel drawer splits: one third to the gravel sieve, two thirds to 2 more hammers (gravel to sand, 192 per minute). The sand drawer splits half to the sand sieve, half to 1 hammer (sand to dust, 96 per minute).
    - i: ["exnihilosequentia:crushed_blackstone"]
      t: The 7th hammer crushes blackstone into crushed blackstone for the fourth sieve.
    - i: ["gtceu:mechanical_sieve", "exnihilosequentia:string_mesh"]
      t: |-
        4 Mechanical Sieves, each with a string mesh in its input bus (never used up). Every 40 s at 30 EU/t: gravel gives 16 copper, iron, tin, sphalerite and magnetite; sand 16 quartz, diamond, lapis, amethyst and emerald; dust 16 redstone and glowstone, 4 sulfur and 4 ender pearls; crushed blackstone 16 galena and 16 stibnite.
    - i: ["thermal:dynamo_lapidary", "kubejs:lv_upgrade_kit", "minecraft:diamond"]
      t: |-
        Power from its own diamonds: a pipe with a filter sends diamonds from the sand sieve into a Lapidary Dynamo with an LV Upgrade Kit (200 × 6 = 1 200 RF/t = 300 EU/t). One diamond is 300 000 RF here, so the block burns about 3.4 of the 24 diamonds it makes per minute.
    - i: ["gtceu:lv_4a_energy_converter", "gtceu:soul_infused_quadruple_wire"]
      t: |-
        2 LV 4A Energy Converters (128 EU/t each, 256 total) turn the FE into EU; soul infused wire runs to the 7 hammers and 4 sieves. Peak draw is 4 × 30 + 7 × 16 = 232 EU/t.
    - i: ["create:steam_engine", "create_new_age:generator_coil"]
      t: |-
        No Lapidary Dynamo yet? Use the Create steam option instead: 3 Steam Engines + 4 Generator Coils give about 307 EU/t for roughly 2 charcoal per minute (see "Create steam power").
    - i: ["minecraft:diamond"]
      t: |-
        Bootstrap: the dynamo needs its first diamond. Put a few in by hand, or run the sand sieve once from any other power.
  s3d:
    b:
      - ["gtceu:lv_forge_hammer", 5, 0, 2, 1, 1, 3, "Forge Hammer · gravel"]
      - ["functionalstorage:oak_1", 7, 0, 2, 1, 1, 3, "Gravel drawer (sieve + 2 hammers)"]
      - ["gtceu:treated_wood_frame", 9, 0, 0, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 0, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 0, 4, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 4, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 0, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 4, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 1, 1, 1, 3, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 3, 1, 1, 1, 3, Treated Wood Frame]
      - ["kubejs:treatedwood_casing", 10, 3, 1, 3, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 0, 5, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 1, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 4, 1, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:meshblock", 10, 4, 1, 3, 1, 3, "Reinforced Mesh (string mesh in the bus)"]
      - ["kubejs:treatedwood_casing", 9, 4, 4, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["gtceu:mechanical_sieve", 11, 4, 4, 1, 1, 1, "Mechanical Sieve · gravel"]
      - ["kubejs:treatedwood_casing", 12, 4, 4, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 0, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 4, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 1, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 5, 1, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["functionalstorage:oak_1", 15, 0, 0, 1, 1, 1, "Output drawer · Copper"]
      - ["functionalstorage:oak_1", 15, 0, 1, 1, 1, 1, "Output drawer · Iron"]
      - ["functionalstorage:oak_1", 15, 0, 2, 1, 1, 1, "Output drawer · Tin"]
      - ["functionalstorage:oak_1", 15, 0, 3, 1, 1, 1, "Output drawer · Sphalerite"]
      - ["functionalstorage:oak_1", 15, 0, 4, 1, 1, 1, "Output drawer · Magnetite"]
      - ["gtceu:lv_forge_hammer", 5, 0, 8, 1, 1, 2, "Forge Hammer · sand"]
      - ["functionalstorage:oak_1", 7, 0, 8, 1, 1, 2, "Drawer · sand (feeds sieve + next hammers)"]
      - ["gtceu:treated_wood_frame", 9, 0, 6, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 6, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 0, 10, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 10, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 6, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 10, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 7, 1, 1, 3, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 3, 7, 1, 1, 3, Treated Wood Frame]
      - ["kubejs:treatedwood_casing", 10, 3, 7, 3, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 6, 5, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 7, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 4, 7, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:meshblock", 10, 4, 7, 3, 1, 3, "Reinforced Mesh (string mesh in the bus)"]
      - ["kubejs:treatedwood_casing", 9, 4, 10, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["gtceu:mechanical_sieve", 11, 4, 10, 1, 1, 1, "Mechanical Sieve · sand"]
      - ["kubejs:treatedwood_casing", 12, 4, 10, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 6, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 10, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 7, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 5, 7, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["functionalstorage:oak_1", 15, 0, 6, 1, 1, 1, "Output drawer · Quartz"]
      - ["functionalstorage:oak_1", 15, 0, 7, 1, 1, 1, "Output drawer · Diamond"]
      - ["functionalstorage:oak_1", 15, 0, 8, 1, 1, 1, "Output drawer · Lapis"]
      - ["functionalstorage:oak_1", 15, 0, 9, 1, 1, 1, "Output drawer · Amethyst"]
      - ["functionalstorage:oak_1", 15, 0, 10, 1, 1, 1, "Output drawer · Emerald"]
      - ["gtceu:lv_forge_hammer", 5, 0, 14, 1, 1, 1, "Forge Hammer · dust"]
      - ["functionalstorage:oak_1", 7, 0, 14, 1, 1, 1, "Drawer · dust (feeds sieve + next hammers)"]
      - ["gtceu:treated_wood_frame", 9, 0, 12, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 12, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 0, 16, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 16, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 12, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 16, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 13, 1, 1, 3, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 3, 13, 1, 1, 3, Treated Wood Frame]
      - ["kubejs:treatedwood_casing", 10, 3, 13, 3, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 12, 5, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 13, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 4, 13, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:meshblock", 10, 4, 13, 3, 1, 3, "Reinforced Mesh (string mesh in the bus)"]
      - ["kubejs:treatedwood_casing", 9, 4, 16, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["gtceu:mechanical_sieve", 11, 4, 16, 1, 1, 1, "Mechanical Sieve · dust"]
      - ["kubejs:treatedwood_casing", 12, 4, 16, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 12, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 16, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 13, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 5, 13, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["functionalstorage:oak_1", 15, 0, 12, 1, 1, 1, "Output drawer · Redstone"]
      - ["functionalstorage:oak_1", 15, 0, 13, 1, 1, 1, "Output drawer · Glowstone"]
      - ["functionalstorage:oak_1", 15, 0, 14, 1, 1, 1, "Output drawer · Sulfur"]
      - ["functionalstorage:oak_1", 15, 0, 15, 1, 1, 1, "Output drawer · Ender Pearl"]
      - ["gtceu:lv_forge_hammer", 5, 0, 20, 1, 1, 1, "Forge Hammer · crushed blackstone"]
      - ["functionalstorage:oak_1", 7, 0, 20, 1, 1, 1, "Drawer · crushed (feeds sieve + next hammers)"]
      - ["gtceu:treated_wood_frame", 9, 0, 18, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 18, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 0, 22, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 0, 22, 1, 3, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 18, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 22, 5, 1, 1, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 9, 3, 19, 1, 1, 3, Treated Wood Frame]
      - ["gtceu:treated_wood_frame", 13, 3, 19, 1, 1, 3, Treated Wood Frame]
      - ["kubejs:treatedwood_casing", 10, 3, 19, 3, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 18, 5, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 4, 19, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 4, 19, 1, 1, 3, Treated Wood Reinforced Casing]
      - ["kubejs:meshblock", 10, 4, 19, 3, 1, 3, "Reinforced Mesh (string mesh in the bus)"]
      - ["kubejs:treatedwood_casing", 9, 4, 22, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["gtceu:mechanical_sieve", 11, 4, 22, 1, 1, 1, "Mechanical Sieve · crushed blackstone"]
      - ["kubejs:treatedwood_casing", 12, 4, 22, 2, 1, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 18, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 22, 5, 2, 1, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 9, 5, 19, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["kubejs:treatedwood_casing", 13, 5, 19, 1, 2, 3, Treated Wood Reinforced Casing]
      - ["functionalstorage:oak_1", 15, 0, 18, 1, 1, 1, "Output drawer · Galena"]
      - ["functionalstorage:oak_1", 15, 0, 19, 1, 1, 1, "Output drawer · Stibnite"]
      - ["gtceu:stone_barrel", 0, 0, 1, 2, 1, 2, "Stone Barrel · lava kept, circuit 0"]
      - ["functionalstorage:oak_1", 3, 0, 1, 1, 1, 2, Cobble drawer]
      - ["gtceu:stone_barrel", 0, 0, 19, 1, 1, 2, "Stone Barrel · witch water → blackstone"]
      - ["functionalstorage:oak_1", 3, 0, 19, 1, 1, 2, Blackstone drawer]
      - ["thermal:device_water_gen", -4, 0, 0, 1, 1, 4, Aqueous Accumulator]
      - ["gtceu:large_barrel", -6, 0, 18, 3, 4, 3, "Large Barrel · spores kept → witch water"]
      - ["thermal:dynamo_lapidary", 17, 0, 7, 1, 1, 1, "Lapidary Dynamo + LV Upgrade Kit (1 200 RF/t)"]
      - ["gtceu:lv_4a_energy_converter", 19, 0, 7, 1, 1, 2, "LV 4A Energy Converter (128 EU/t each)"]
    p:
      - [i, [8, 0.5, 3.5], [9.6, 0.5, 3.5]]
      - [i, [13.5, 0.5, 2.5], [14.5, 0.5, 2.5], [14.5, 0.5, 2.5], [15, 0.5, 2.5]]
      - [i, [6, 0.5, 2.5], [7, 0.5, 2.5]]
      - [i, [8, 0.5, 9.5], [9.6, 0.5, 9.5]]
      - [i, [13.5, 0.5, 8.5], [14.5, 0.5, 8.5], [14.5, 0.5, 8.5], [15, 0.5, 8.5]]
      - [i, [6, 0.5, 8.5], [7, 0.5, 8.5]]
      - [i, [8, 0.5, 14.5], [9.6, 0.5, 14.5]]
      - [i, [13.5, 0.5, 14.5], [14.5, 0.5, 14.5], [14.5, 0.5, 14.5], [15, 0.5, 14.5]]
      - [i, [6, 0.5, 14.5], [7, 0.5, 14.5]]
      - [i, [8, 0.5, 20.5], [9.6, 0.5, 20.5]]
      - [i, [13.5, 0.5, 20.5], [14.5, 0.5, 20.5], [14.5, 0.5, 19.5], [15, 0.5, 19.5]]
      - [i, [6, 0.5, 20.5], [7, 0.5, 20.5]]
      - [i, [2, 0.5, 1.5], [3, 0.5, 1.5]]
      - [i, [4, 0.5, 2.5], [4.5, 0.5, 2.5], [4.5, 0.5, 4.5]]
      - [i, [4.5, 0.5, 3.5], [5, 0.5, 3.5]]
      - [i, [4.5, 0.5, 4.5], [5, 0.5, 4.5]]
      - [i, [1, 0.5, 20.5], [3, 0.5, 20.5]]
      - [i, [4, 0.5, 20.5], [5, 0.5, 20.5]]
      - [f, [-3, 0.5, 1.5], [0, 0.5, 1.5]]
      - [f, [-3, 0.5, 3.5], [-2.5, 0.5, 3.5], [-2.5, 0.5, 18.5], [-3, 0.5, 18.5]]
      - [f, [-3, 0.5, 20.5], [0, 0.5, 20.5]]
      - [i, [7.5, 0.5, 5], [7.5, 0.5, 5.5], [5.5, 0.5, 5.5], [5.5, 0.5, 8]]
      - [i, [7.5, 0.5, 10], [7.5, 0.5, 11.5], [5.5, 0.5, 11.5], [5.5, 0.5, 14]]
      - [i, [16, 0.5, 7.5], [17, 0.5, 7.5]]
      - [p, [18, 0.5, 7.5], [19, 0.5, 7.5]]
      - [p, [20, 0.85, 7.5], [21.5, 0.85, 7.5], [21.5, 0.85, 5.5], [21.5, 0.85, 17.5]]
      - [p, [21.5, 0.85, 5.5], [9, 0.85, 5.5]]
      - [p, [21.5, 0.85, 11.5], [9, 0.85, 11.5]]
      - [p, [21.5, 0.85, 17.5], [9, 0.85, 17.5]]
    l:
      - ["Sieve · gravel · 40 s · 30 EU/t", 11.5, 8.4, 2.5]
      - ["3 Hammers · cobble → gravel", 7.5, 2.4, 3]
      - ["Sieve · sand · 5 gems", 11.5, 8.4, 8.5]
      - ["2 Hammers · gravel → sand", 5.5, 4, 9]
      - ["Sieve · dust · 4 items", 11.5, 8.4, 14.5]
      - ["Hammer · sand → dust", 5.5, 2.4, 15]
      - ["Sieve · blackstone · 2 ores", 11.5, 8.4, 20.5]
      - ["Hammer · blackstone → crushed", 5.5, 4, 21]
      - ["4 Aqueous Accumulators · water", -4, 1.4, 2]
      - ["Large Barrel · witch water 15 B/min", -4.5, 5.6, 19.5]
      - ["4 Stone Barrels · 320 cobble/min", 1, 3.9, 2.5]
      - ["2 Stone Barrels · blackstone", 1, 1.9, 20.5]
      - ["Lapidary Dynamo · 3.4 diamonds/min", 17, 1.4, 8.5]
      - ["2 LV 4A Converters · 256 EU/t", 19.5, 4.9, 8]
      - ["Soul wire · peak 232 EU/t", 22, 1.6, 11.5]
---
# Four-sieve block (gravel, sand, dust, blackstone)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_block4` · **Tags:** Infinite source, Hero build, 3D scene

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Sieve block (4 sieves)](../../plan/p2.md#sieves)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lb">
<div class="gt-head"><span class="gt-mname">Large Barrel · spores kept</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Water (Aqueous Accumulators) (thermal:device_water_gen) - water"><img class="gt-ico" src="../../assets/icons/thermal__device_water_gen.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Device Water Gen</span><span class="gt-note">Water (Aqueous Accumulators)</span><span class="gt-tag">infinite</span><b class="gt-q">water</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-sbb" title="2 Stone Barrels · blackstone (gtceu:stone_barrel) - witch water"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Barrel</span><span class="gt-note">2 Stone Barrels · blackstone</span><b class="gt-q">witch water</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_barrel</code></div>
</div>
<div class="gt-panel t-mod" id="m-sbc">
<div class="gt-head"><span class="gt-mname">4 Stone Barrels · cobble</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Water (Aqueous Accumulators) (thermal:device_water_gen) - water"><img class="gt-ico" src="../../assets/icons/thermal__device_water_gen.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Device Water Gen</span><span class="gt-note">Water (Aqueous Accumulators)</span><span class="gt-tag">infinite</span><b class="gt-q">water</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-h1" title="3 Forge Hammers (gtceu:lv_forge_hammer) - cobble"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">3 Forge Hammers</span><b class="gt-q">cobble</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
<div class="gt-panel t-mod" id="m-sbb">
<div class="gt-head"><span class="gt-mname">2 Stone Barrels · blackstone</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-lb" title="Large Barrel · spores kept (gtceu:large_barrel) - witch water"><img class="gt-ico" src="../../assets/icons/gtceu__large_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Barrel</span><span class="gt-note">Large Barrel · spores kept</span><b class="gt-q">witch water</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-h4" title="Forge Hammer (gtceu:lv_forge_hammer) - blackstone"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><b class="gt-q">blackstone</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:stone_barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-h1">
<div class="gt-head"><span class="gt-mname">3 Forge Hammers</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-sbc" title="4 Stone Barrels · cobble (gtceu:stone_barrel) - cobble"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Barrel</span><span class="gt-note">4 Stone Barrels · cobble</span><b class="gt-q">cobble</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-s1" title="Sieve · gravel (gtceu:mechanical_sieve) - gravel"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Sieve · gravel</span><b class="gt-q">gravel</b></a><a class="gt-slot gt-mach" href="#m-h2" title="2 Forge Hammers (gtceu:lv_forge_hammer) - gravel"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">2 Forge Hammers</span><b class="gt-q">gravel</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-lv" id="m-h2">
<div class="gt-head"><span class="gt-mname">2 Forge Hammers</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h1" title="3 Forge Hammers (gtceu:lv_forge_hammer) - gravel"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">3 Forge Hammers</span><b class="gt-q">gravel</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-s2" title="Sieve · sand (gtceu:mechanical_sieve) - sand"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Sieve · sand</span><b class="gt-q">sand</b></a><a class="gt-slot gt-mach" href="#m-h3" title="Forge Hammer (gtceu:lv_forge_hammer) - sand"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><b class="gt-q">sand</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-lv" id="m-h3">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h2" title="2 Forge Hammers (gtceu:lv_forge_hammer) - sand"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">2 Forge Hammers</span><b class="gt-q">sand</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-s3" title="Sieve · dust (gtceu:mechanical_sieve) - dust"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Sieve · dust</span><b class="gt-q">dust</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-lv" id="m-h4">
<div class="gt-head"><span class="gt-mname">Forge Hammer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-sbb" title="2 Stone Barrels · blackstone (gtceu:stone_barrel) - blackstone"><img class="gt-ico" src="../../assets/icons/gtceu__stone_barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Barrel</span><span class="gt-note">2 Stone Barrels · blackstone</span><b class="gt-q">blackstone</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-s4" title="Sieve · blackstone (gtceu:mechanical_sieve) - crushed"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Sieve · blackstone</span><b class="gt-q">crushed</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:lv_forge_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-s1">
<div class="gt-head"><span class="gt-mname">Sieve · gravel</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h1" title="3 Forge Hammers (gtceu:lv_forge_hammer) - gravel"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">3 Forge Hammers</span><b class="gt-q">gravel</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Copper (gtceu:crushed_copper_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_copper_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Copper Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Iron (gtceu:crushed_iron_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_iron_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Iron Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Tin (gtceu:crushed_tin_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_tin_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Tin Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Sphalerite (gtceu:crushed_sphalerite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_sphalerite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Sphalerite Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Magnetite (gtceu:crushed_magnetite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_magnetite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Magnetite Ore</span><b class="gt-q">×16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
<div class="gt-panel t-mod" id="m-s2">
<div class="gt-head"><span class="gt-mname">Sieve · sand</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h2" title="2 Forge Hammers (gtceu:lv_forge_hammer) - sand"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><span class="gt-note">2 Forge Hammers</span><b class="gt-q">sand</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Quartz (minecraft:quartz) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__quartz.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quartz</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Lapis (minecraft:lapis_lazuli) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__lapis_lazuli.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lapis Lazuli</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Amethyst (minecraft:amethyst_shard) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__amethyst_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Amethyst Shard</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Emerald (minecraft:emerald) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__emerald.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Emerald</span><b class="gt-q">×16</b></span><a class="gt-slot gt-power" href="#m-ld" title="Lapidary Dynamo + LV kit (thermal:dynamo_lapidary) - diamonds"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">Lapidary Dynamo + LV kit</span><b class="gt-q">diamonds</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
<div class="gt-panel t-mod" id="m-s3">
<div class="gt-head"><span class="gt-mname">Sieve · dust</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h3" title="Forge Hammer (gtceu:lv_forge_hammer) - dust"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><b class="gt-q">dust</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Redstone (minecraft:redstone) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__redstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Redstone</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Glowstone (minecraft:glowstone_dust) - ×16"><img class="gt-ico" src="../../assets/icons/minecraft__glowstone_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glowstone Dust</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Sulfur (gtceu:sulfur_dust) - ×4"><img class="gt-ico" src="../../assets/icons/gtceu__sulfur_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfur Dust</span><b class="gt-q">×4</b></span><span class="gt-slot gt-outp" title="Ender Pearl (minecraft:ender_pearl) - ×4"><img class="gt-ico" src="../../assets/icons/minecraft__ender_pearl.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender Pearl</span><b class="gt-q">×4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
<div class="gt-panel t-mod" id="m-s4">
<div class="gt-head"><span class="gt-mname">Sieve · blackstone</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-h4" title="Forge Hammer (gtceu:lv_forge_hammer) - crushed"><img class="gt-ico" src="../../assets/icons/gtceu__lv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Forge Hammer</span><b class="gt-q">crushed</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Galena (gtceu:crushed_galena_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_galena_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Galena Ore</span><b class="gt-q">×16</b></span><span class="gt-slot gt-outp" title="Crushed Stibnite (gtceu:crushed_stibnite_ore) - ×16"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_stibnite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Stibnite Ore</span><b class="gt-q">×16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mechanical_sieve</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-ld">
<div class="gt-head"><span class="gt-mname">Lapidary Dynamo + LV kit</span><span class="gt-badge t-mod">Thermal</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-s2" title="Sieve · sand (gtceu:mechanical_sieve) - diamonds"><img class="gt-ico" src="../../assets/icons/gtceu__mechanical_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Sieve</span><span class="gt-note">Sieve · sand</span><b class="gt-q">diamonds</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-cv" title="2 LV 4A Converters (gtceu:lv_4a_energy_converter) - FE"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV 4a Energy Converter</span><span class="gt-note">2 LV 4A Converters</span><b class="gt-q">FE</b></a></div>
</div>
<div class="gt-foot"><code>thermal:dynamo_lapidary</code></div>
</div>
<div class="gt-panel t-lv gt-gen" id="m-cv">
<div class="gt-head"><span class="gt-mname">2 LV 4A Converters</span><span class="gt-badge t-lv">LV</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-ld" title="Lapidary Dynamo + LV kit (thermal:dynamo_lapidary) - FE"><img class="gt-ico" src="../../assets/icons/thermal__dynamo_lapidary.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dynamo Lapidary</span><span class="gt-note">Lapidary Dynamo + LV kit</span><b class="gt-q">FE</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_4a_energy_converter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_4a_energy_converter</code></div>
</div>
</div>

## Flow

- [Large Barrel · spores kept](#m-lb) → [2 Stone Barrels · blackstone](#m-sbb) → [Forge Hammer](#m-h4) → [Sieve · blackstone](#m-s4)
- [4 Stone Barrels · cobble](#m-sbc) → [3 Forge Hammers](#m-h1) → [Sieve · gravel](#m-s1) (also 3 Forge Hammers → [2 Forge Hammers](#m-h2))
- [2 Forge Hammers](#m-h2) → [Sieve · sand](#m-s2) → [Lapidary Dynamo + LV kit](#m-ld) → [2 LV 4A Converters](#m-cv) (also 2 Forge Hammers → [Forge Hammer](#m-h3))
- [Forge Hammer](#m-h3) → [Sieve · dust](#m-s3)

## How to build

1. Water first. Each Stone Barrel drinks 1 B per block, so 4 cobble barrels need 320 B per minute (about 270 mB/t). One Aqueous Accumulator keeps two barrels busy (your current line), so use 4, or fewer with an LV Upgrade Kit inside. Run Pipez fluid pipes to every barrel. — `thermal:device_water_gen`, `pipez:fluid_pipe`
2. 4 Stone Barrels with a lava bucket inside (kept) and ghost circuit 0: 4 × 80 = 320 cobble per minute. The block needs 288 (96 for each of the gravel, sand and dust sieves). — `gtceu:stone_barrel`, `minecraft:lava_bucket`
3. Witch water: a Large Barrel with mycelium spores in its input bus (kept) turns 1 B of water into 1 B of witch water every 4 s, 15 B per minute. — `gtceu:large_barrel`, `exnihilosequentia:mycelium_spores`
4. 2 more Stone Barrels with lava kept and witch water piped in make blackstone (1 B witch water each). They are only as fast as the witch water: 2 Large Barrels give 30 blackstone per minute; 7 would feed the sieve at full speed (96). — `gtceu:stone_barrel`, `minecraft:blackstone`
5. 3 Forge Hammers turn cobble into gravel (0.5 s and 16 EU/t each, 120 per minute per hammer, 360 total for the 288 needed). Barrels auto-output into a drawer; Pipez item pipes in round-robin feed the hammers. — `gtceu:lv_forge_hammer`
6. The gravel drawer splits: one third to the gravel sieve, two thirds to 2 more hammers (gravel to sand, 192 per minute). The sand drawer splits half to the sand sieve, half to 1 hammer (sand to dust, 96 per minute). — `minecraft:gravel`, `functionalstorage:oak_1`
7. The 7th hammer crushes blackstone into crushed blackstone for the fourth sieve. — `exnihilosequentia:crushed_blackstone`
8. 4 Mechanical Sieves, each with a string mesh in its input bus (never used up). Every 40 s at 30 EU/t: gravel gives 16 copper, iron, tin, sphalerite and magnetite; sand 16 quartz, diamond, lapis, amethyst and emerald; dust 16 redstone and glowstone, 4 sulfur and 4 ender pearls; crushed blackstone 16 galena and 16 stibnite. — `gtceu:mechanical_sieve`, `exnihilosequentia:string_mesh`
9. Power from its own diamonds: a pipe with a filter sends diamonds from the sand sieve into a Lapidary Dynamo with an LV Upgrade Kit (200 × 6 = 1 200 RF/t = 300 EU/t). One diamond is 300 000 RF here, so the block burns about 3.4 of the 24 diamonds it makes per minute. — `thermal:dynamo_lapidary`, `kubejs:lv_upgrade_kit`, `minecraft:diamond`
10. 2 LV 4A Energy Converters (128 EU/t each, 256 total) turn the FE into EU; soul infused wire runs to the 7 hammers and 4 sieves. Peak draw is 4 × 30 + 7 × 16 = 232 EU/t. — `gtceu:lv_4a_energy_converter`, `gtceu:soul_infused_quadruple_wire`
11. No Lapidary Dynamo yet? Use the Create steam option instead: 3 Steam Engines + 4 Generator Coils give about 307 EU/t for roughly 2 charcoal per minute (see "Create steam power"). — `create:steam_engine`, `create_new_age:generator_coil`
12. Bootstrap: the dynamo needs its first diamond. Put a few in by hand, or run the sand sieve once from any other power. — `minecraft:diamond`

## Tips

- Every sieve eats 64 blocks per 40 s = 96 per minute. Amounts shown are per 40 s batch.
- The whole block draws about 210 EU/t (232 at peak). Before you have a Lapidary Dynamo, power it with Steam Engines + Generator Coils (see the power options).
- Witch water is the slow part: full speed on the blackstone sieve needs 96 B per minute (7 Large Barrels). Two barrels run it about a third of the time.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:device_water_gen` | 4 |
| `gtceu:large_barrel` | 2 |
| `exnihilosequentia:mycelium_spores` | 2 |
| `gtceu:stone_barrel` | 6 |
| `minecraft:lava_bucket` | 6 |
| `gtceu:lv_forge_hammer` | 7 |
| `gtceu:mechanical_sieve` | 4 |
| `exnihilosequentia:string_mesh` | 4 |
| `thermal:dynamo_lapidary` | 1 |
| `kubejs:lv_upgrade_kit` | 1 |
| `gtceu:lv_4a_energy_converter` | 2 |
| `gtceu:soul_infused_quadruple_wire` | 8 |
| `functionalstorage:oak_1` | 8 |
| `pipez:item_pipe` | 32 |
| `pipez:fluid_pipe` | 16 |

## Needs / Feeds

- **Feeds:** [Ore processing](ores.md)
- **Main source for:** `gtceu:crushed_iron_ore`, `exnihilosequentia:crushed_blackstone`

## Extras

- 3D assembly scene with 112 blocks (open it in the Atlas page).
