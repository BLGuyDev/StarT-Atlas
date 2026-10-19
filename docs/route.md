---
kind: view
view: route
---
# Build route

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

Data: `docs/_data/route.yml`.

## 1. Wood farm

**Era:** [Steam &amp; Create](eras/steam.md) · **Chains:** [Create tree farm (rotating saws + deployers)](chains/steam/tree_farm.md)

Endless logs: they become charcoal, planks, wood pulp, treated wood and fuel for everything after.
- Saws on a moving contraption fell the whole tree in one pass.
- Put the logs in a drawer from day one: the cutter, coke ovens and fan all pull from it.

## 2. Charcoal and creosote

**Era:** [Steam &amp; Create](eras/steam.md) · **Chains:** [Charcoal: Create fan smelting](chains/steam/charcoal_fan.md), [Charcoal &amp; creosote: Coke Oven](chains/steam/charcoal.md)

Fuel for the burners and the steel furnace, plus the only early creosote.
- Coke ovens are slow for charcoal (1.3 per minute each) but they are the only early creosote: keep two running for treated wood and lubricant.
- Create fan blowing through a lava block smelts logs into charcoal on a belt with no fuel at all.
- Sugar cane also works in the coke oven: 8 → 1 charcoal.

## 3. Steam engines + generator coils

**Era:** [Steam &amp; Create](eras/steam.md) · **Chains:** [Create steam power: Steam Engines + Generator Coils](chains/steam/power_steam_engine.md)

Big Create rotation and FE/EU for every machine after this. Burners eat charcoal; water from an Aqueous Accumulator.
- Boiler level is the lowest of burners, tank blocks / 4 and water / 10 mB/t: check all three bars with goggles.
- Basic Burners must be lit once with flint and steel. Never empower them with a fan (32× fuel).
- A coil takes 12 magnets. Start with redstone magnets (no power), upgrade to fluxuated magnetite (force 8) once you have an LV polarizer and bender.
- Spin the coils at 256 RPM with a speed controller: same magnets, +88 % FE.
- One carbon brush handles at most 8 coils.

## 4. Sieve zone: cobble → gravel → ore sieve

**Era:** [LV](eras/lv.md) · **Chains:** [Infinite cobble &amp; blackstone](chains/stone/inf_cobble.md), [Gravel, sand &amp; dust: Forge Hammers](chains/feeders/gravel_hammer.md)

Infinite copper, iron, tin, sphalerite and magnetite. Plan room for four sieves side by side from the start.
- Stone barrels keep their lava; only 1 B of water per cobble is used.
- A drawer buffer (yours holds ~2k gravel) before the sieve keeps it from ever starving.
- The string mesh in the sieve’s input bus is never used up, but the structure needs 9 mesh blocks.
- One forge hammer (120 gravel/min) outruns one sieve (96/min).

## 5. Sand and dust sieves + diamond power

**Era:** [LV](eras/lv.md) · **Chains:** [Four-sieve block (gravel, sand, dust, blackstone)](chains/lv/sieve_block4.md), [Diamond power (Lapidary Dynamos)](chains/lv/power_lapidary.md)

Gems, redstone, glowstone, sulfur and pearls; the sand sieve’s diamonds fuel Lapidary Dynamos.
- 16 diamonds per 40 s = 24 per minute; one diamond is 300 000 RF in a Lapidary Dynamo.
- An LV Upgrade Kit makes a dynamo 6× stronger (200 → 1 200 RF/t).
- Sulfur from the dust sieve is what turns rubber into cured or liquid rubber; redstone becomes red alloy.

## 6. Treated wood

**Era:** [LV](eras/lv.md) · **Chains:** [Treated wood: cutter + spout](chains/lv/treated_wood.md)

Treated planks, rods and frames for every primitive multiblock (sieves, Large Farm, Large Barrel).
- The cutter needs water piped in (or lubricant for double speed).
- 125 mB creosote per plank: one coke-oven log treats 2 planks.
- Store the wood pulp: fertilizer needs it.

## 7. Fertilizer → latex → rubber sheets

**Era:** [LV](eras/lv.md) · **Chains:** [Rubber: Large Arboreal Extractor](chains/steam/rubber.md)

Endless rubber plates and liquid rubber for every cable and conveyor.
- Thermal’s small Arboreal Extractor gives nothing here (rubberwood only); use StarT’s Large Arboreal Extractor around a jungle tree you place.
- The extractor needs a screw in its input bus; fertilizer only works with an iron screw (250 mB per 20 s instead of 100).
- Liquid rubber from the LV chemical reactor (3 rubber + sulfur → 576 mB = 4 plates) beats mixer + press (3 plates) and is what copper cables need.

## 8. Lava and obsidian

**Era:** [LV](eras/lv.md) · **Chains:** [Infinite lava, obsidian &amp; pebbles](chains/stone/inf_lava.md)

Lava for the fans and barrels, obsidian for later machines.
- The soul campfire in the input bus is kept, not burned.
- Obsidian mode keeps 1 obsidian + water inside the barrel.

## 9. Ingots, wrought iron, wires, foil

**Era:** [LV](eras/lv.md) · **Chains:** [Ingots, wrought iron, wires and foil from the sieve](chains/lv/ingots.md)

Drawers of ingots, wires and foil that every later line pulls from.
- Crushed ore from the sieve smelts straight to 1 ingot (furnace or fan blasting).
- Kiln: wrought iron in 2 s with no fuel.
- Copper foil needs circuit 10 on the bender (1 copper → 4 foil).

## 10. Steel, plates, rods, magnetic rods

**Era:** [LV](eras/lv.md) · **Chains:** [Steel: Solid Blast Furnace](chains/steam/steel.md), [Parts row 1: rods, plates, bolts, gears](chains/lv/comp_parts.md)

Steel and the rods / plates / magnetic rods every LV component uses, with drawer buffers between machines.
- The Solid Blast Furnace needs steel to build: the first steel comes from a Primitive Blast Furnace (90 s each).
- Wrought iron runs at 16 s per steel, plain iron at 36 s.
- Lathe: 1 ingot → 2 rods. The iron motor recipe uses iron rods + a magnetic iron rod: no steel needed for motors.

## 11. LV component wall

**Era:** [LV](eras/lv.md) · **Chains:** [Component wall: always a stock of every part (no AE2)](chains/lv/comp_stock.md), [Parts row 2: wires, fine wire, cables](chains/lv/comp_wires.md), [LV Electric Motor line](chains/lv/comp_motor.md), [LV Electric Piston line](chains/lv/comp_piston.md), [LV Conveyor Module line](chains/lv/comp_conveyor.md), [LV Electric Pump line](chains/lv/comp_pump.md), [LV Robot Arm line](chains/lv/comp_robot_arm.md)

Motors, pistons, conveyors, pumps and robot arms always in stock.
- A Robot Arm cover on Keep Exact (with an item filter) caps each stock; a GT machine with a full output just pauses.
- Tin cable: wire + 144 mB liquid rubber in the assembler. Copper cable has no hand recipe at all.
- Give each assembler one recipe and one circuit so its slots never clog.

## 12. LV circuits

**Era:** [LV](eras/lv.md) · **Chains:** [LV circuit line (Basic Electronic Circuit)](chains/lv/comp_circuit_lv.md)

Basic Electronic Circuits on tap.
- The Circuit Assembler makes 2 circuits per craft; hand crafting makes 1 and costs a steel plate.
- A Large Arboreal Extractor built with an oak tree gives resin: resin + charcoal dust in a mixer = glue for boards and resistors.
- Glass tubes: 6 glass panes → 2 by hand.

## 13. First MV hull + transformer

**Era:** [MV](eras/mv.md) · **Chains:** [First MV hull and the LV → MV transformer](chains/mv/mv_hull.md)

Step into MV without MV power: hand-crafted hull, LV transformer for power.
- Copper cables only come from the assembler (wire + 144 mB liquid rubber).
- The LV transformer is built from an LV hull, not an MV one.
- MV machines at full speed draw 128 EU/t: 4 A of LV through the transformer.
