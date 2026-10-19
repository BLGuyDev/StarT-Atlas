---
kind: chain
id: zpm_crystal
order: 1360
data:
  t: |-
    Crystal CPU: exquisite emerald + europium → raw crystal chip (10 %) → 9 parts → loop at 100 % → EBF with helium → laser engraver
  inf: true
  "n":
    - [ex, "Exquisite emerald (2 flawless = 4 emeralds)", i, "gtceu:exquisite_emerald_gem"]
    - [eu, "16 mB europium per autoclave run", f, "gtceu:europium_bucket"]
    - [a1, "HV Autoclave in the cleanroom · 10 min · 320 EU/t · 10 % chip", m, "gtceu:hv_autoclave"]
    - [rc, Raw Crystal Chip, x, "gtceu:raw_crystal_chip"]
    - [fh, "HV Forge Hammer · 5 s · 480 EU/t", m, "gtceu:hv_forge_hammer"]
    - [pt, "9 Raw crystal chip parts", x, "gtceu:raw_crystal_chip_parts"]
    - [a2, "HV Autoclave in the cleanroom · 10 min · 480 EU/t · 100 %", m, "gtceu:hv_autoclave"]
    - [eb, "EBF 5000 K or more · 45 s · 480 EU/t · emerald plate + 1 B helium", m, "gtceu:electric_blast_furnace"]
    - [ec, Engraved Crystal Chip, x, "gtceu:engraved_crystal_chip"]
    - [le, "LuV Laser Engraver in the cleanroom · 5 s · 10 000 EU/t · lime lens", m, "gtceu:luv_laser_engraver"]
    - [cc, Crystal CPU, o, "gtceu:crystal_cpu"]
  e:
    - [ex, a1, "1"]
    - [eu, a1, "16 mB"]
    - [a1, rc, "10 % / 10 min"]
    - [rc, fh, "1"]
    - [fh, pt, "9 / 5 s"]
    - [pt, a2, "1"]
    - [eu, a2, "16 mB"]
    - [a2, rc, "1 / 10 min"]
    - [rc, eb, "1"]
    - [eb, ec, "1 / 45 s"]
    - [ec, le, "1"]
    - [le, cc, "1 / 5 s"]
  tips:
    - |-
      Recipes (CircuitRecipes, GT fork): raw crystal chip = 1 exquisite emerald + 16 mB molten europium in an Autoclave, CLEANROOM, 12 000 ticks (10 min) at 320 EU/t, with only a 10 % chance (chancedOutput 1000 of 10 000, tier boost 2000). The pack REMOVES the olivine, mutagen and bacterial sludge autoclave variants (mass_removals.js), so the emerald is the only way to the FIRST chip. Then the loop: Forge Hammer 1 raw crystal chip → 9 raw crystal chip PARTS (100 ticks, 480 EU/t), and 1 part + 16 mB europium in an Autoclave (cleanroom, 12 000 ticks, 480 EU/t) → 1 raw chip at 100 %. So one lucky chip becomes 9, then 81, as fast as you have autoclaves: the era text ‘loop the chip parts’ is exactly this.
    - |-
      Unverified: the autoclave tier boost. In GT each voltage tier above the recipe adds the ‘boost’ to a chanced output, which would make an IV autoclave about 50 % per exquisite emerald. The only fixed fact is 10 % at the base tier; test with one machine tier up before you grind emeralds.
    - |-
      Exquisite emerald: gem conversion in MaterialRecipeHandler, laser engraver recipes with a NON-consumed white lens: 2 emeralds → 1 flawless emerald (300 ticks, 240 EU/t), 2 flawless → 1 exquisite. So 4 emeralds per exquisite gem; the cutter reverses it. Emeralds come from the sand sieve (guide base chapters: 16 emerald per 64 sand in the Mechanical Sieve) or gem ore processing. Since the loop makes chips for free after the first one, you need only one or two exquisite gems.
    - |-
      Engraved crystal chip (BLAST_RECIPES engraved_crystal_chip_from_emerald): 1 emerald plate + 1 raw crystal chip + 1000 mB helium in an EBF at 5000 K or more (HSS-G coils, 5400 K, are enough), 900 ticks (45 s) at 480 EU/t. The emerald plate is a Bender product of an emerald gem (Unverified plate machine/time). Helium: the same air/gas helium the vacuum freezer lines use.
    - |-
      Crystal CPU (laser_engraver crystal_cpu): 1 engraved chip + a lime lens that is not consumed, cleanroom, 100 ticks at 10 000 EU/t. 10 000 EU/t is above an IV machine (8192 V), so this needs a LuV Laser Engraver (LuV hull + LuV emitter + LuV sensor; see luv_components2). The Crystal SoC is a second engraving at 40 000 EU/t with a blue lens: a ZPM-tier machine, and not needed for the era.
    - |-
      Europium: 16 mB per chip is nothing; the real europium use is fine wire for ZPM motors and voltage coils (luv_fusion chain: 144 mB per 28.8 s run). So the LuV fusion reactor is also the start of the crystal line.
    - |-
      Sub-steps people skip: (1) two autoclaves, one per recipe, because the part recipe and the gem recipe share an output but not an input; (2) cleanroom filter: both autoclaves must stand inside the cleanroom; (3) the lens stays in the engraver, keep a spare lime lens; (4) never hammer your LAST raw chip: put 1 or 2 aside as seed; (5) the EBF needs the helium input AND a 5000 K coil, a plain Kanthal furnace does not start the recipe.
    - |-
      Unverified: the plate recipe of emerald, the exact lens id, and whether a Large autoclave multi exists in this pack for bulk loops (check the multis list).
  b:
    - ["gtceu:hv_autoclave", 2]
    - ["gtceu:hv_forge_hammer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:hssg_coil_block", 16]
    - ["gtceu:luv_laser_engraver", 1]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:exquisite_emerald_gem", "gtceu:raw_crystal_chip", "gtceu:emerald_plate"]
      t: |-
        Drawers first, one per input: exquisite emeralds, raw crystal chips, raw chip parts, emerald plates, lime lenses. Drums: molten europium, helium. Every machine has its own drawer behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:hv_autoclave", "gtceu:exquisite_emerald_gem", "gtceu:europium_bucket"]
      t: |-
        Seed autoclave inside the cleanroom: exquisite emerald + 16 mB europium → 10 % chance of a raw chip after 10 min at 320 EU/t. Feed one gem at a time and let a drawer hold the failures’ spare gems.
    - i: ["gtceu:hv_forge_hammer", "gtceu:raw_crystal_chip_parts"]
      t: |-
        Hammer: 1 raw chip → 9 parts (100 ticks, 480 EU/t). A Robot Arm with an Item Filter takes the chip out of the seed autoclave into the hammer, but ONLY while the stock is below your target; keep the first chip until the part loop has produced a second one.
    - i: ["gtceu:hv_autoclave", "gtceu:raw_crystal_chip", "gtceu:europium_bucket"]
      t: |-
        Loop autoclave (second machine, cleanroom): 1 part + 16 mB europium → 1 raw chip in 10 min at 480 EU/t, 100 %. Its output goes back to the chip drawer; one chip per 10 minutes per machine, so add machines until you cover your crystal computer plan.
    - i: ["gtceu:electric_blast_furnace", "gtceu:hssg_coil_block", "gtceu:engraved_crystal_chip"]
      t: |-
        EBF with 16 HSS-G coils (5400 K): input bus with the raw chip + emerald plate, a fluid input hatch fed with 1 B helium per run → engraved crystal chip in 45 s at 480 EU/t. Muffler hatch free above.
    - i: ["gtceu:luv_laser_engraver", "gtceu:crystal_cpu", "gtceu:lime_glass_lens"]
      t: |-
        Engrave: LuV Laser Engraver inside the cleanroom, 1 engraved chip + the lime lens in a ghost slot → Crystal CPU in 5 s at 10 000 EU/t (a LuV cable line). Output into a drawer with Keep Exact 4.
    - i: ["functionalstorage:oak_1", "gtceu:crystal_cpu"]
      t: |-
        Easy to miss: each crystal computer (the second ZPM circuit) eats ONE crystal CPU, so a handful is plenty; the long part is the 10 minute autoclave clock, so start it a session before you need the circuits.
---
# Crystal CPU: exquisite emerald + europium → raw crystal chip (10 %) → 9 parts → loop at 100 % → EBF with helium → laser engraver

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_crystal` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Crystal circuits and the UV circuit](../../plan/p12.md#zpmcrystal)

**Tips:** 8, 2 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-a1">
<div class="gt-head"><span class="gt-mname">HV Autoclave in the cleanroom · 10 min · 320 EU/t · 10 % chip</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Exquisite emerald (2 flawless = 4 emeralds) (gtceu:exquisite_emerald_gem) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__exquisite_emerald_gem.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Exquisite Emerald Gem</span><span class="gt-note">Exquisite emerald (2 flawless = 4 emeralds)</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="16 mB europium per autoclave run (gtceu:europium_bucket) - 16 mB"><img class="gt-ico" src="../../assets/icons/gtceu__europium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Europium</span><span class="gt-note">16 mB europium per autoclave run</span><b class="gt-q">16 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">10 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Raw Crystal Chip (gtceu:raw_crystal_chip) - 10 % / 10 min"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip</span><b class="gt-q">10 %</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-hv" id="m-fh">
<div class="gt-head"><span class="gt-mname">HV Forge Hammer · 5 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Raw Crystal Chip (gtceu:raw_crystal_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="9 Raw crystal chip parts (gtceu:raw_crystal_chip_parts) - 9 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip_parts.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip Parts</span><span class="gt-note">9 Raw crystal chip parts</span><b class="gt-q">9</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_forge_hammer</code></div>
</div>
<div class="gt-panel t-hv" id="m-a2">
<div class="gt-head"><span class="gt-mname">HV Autoclave in the cleanroom · 10 min · 480 EU/t · 100 %</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="9 Raw crystal chip parts (gtceu:raw_crystal_chip_parts) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip_parts.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip Parts</span><span class="gt-note">9 Raw crystal chip parts</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="16 mB europium per autoclave run (gtceu:europium_bucket) - 16 mB"><img class="gt-ico" src="../../assets/icons/gtceu__europium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Europium</span><span class="gt-note">16 mB europium per autoclave run</span><b class="gt-q">16 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">10 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Raw Crystal Chip (gtceu:raw_crystal_chip) - 1 / 10 min"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF 5000 K or more · 45 s · 480 EU/t · emerald plate + 1 B helium</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Raw Crystal Chip (gtceu:raw_crystal_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Crystal Chip</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Engraved Crystal Chip (gtceu:engraved_crystal_chip) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__engraved_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Engraved Crystal Chip</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-luv" id="m-le">
<div class="gt-head"><span class="gt-mname">LuV Laser Engraver in the cleanroom · 5 s · 10 000 EU/t · lime lens</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Engraved Crystal Chip (gtceu:engraved_crystal_chip) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__engraved_crystal_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Engraved Crystal Chip</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crystal CPU (gtceu:crystal_cpu) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__crystal_cpu.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crystal CPU</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_laser_engraver</code></div>
</div>
</div>

## Flow

- [HV Autoclave in the cleanroom · 10 min · 320 EU/t · 10 % chip](#m-a1) → [HV Forge Hammer · 5 s · 480 EU/t](#m-fh) → [HV Autoclave in the cleanroom · 10 min · 480 EU/t · 100 %](#m-a2) → [EBF 5000 K or more · 45 s · 480 EU/t · emerald plate + 1 B helium](#m-eb) → [LuV Laser Engraver in the cleanroom · 5 s · 10 000 EU/t · lime lens](#m-le) (also HV Autoclave in the cleanroom · 10 min · 320 EU/t · 10 % chip → [EBF 5000 K or more · 45 s · 480 EU/t · emerald plate + 1 B helium](#m-eb), HV Autoclave in the cleanroom · 10 min · 480 EU/t · 100 % → [HV Forge Hammer · 5 s · 480 EU/t](#m-fh))

## How to build

1. Drawers first, one per input: exquisite emeralds, raw crystal chips, raw chip parts, emerald plates, lime lenses. Drums: molten europium, helium. Every machine has its own drawer behind a Modular Router or Pipez item pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:exquisite_emerald_gem`, `gtceu:raw_crystal_chip`, `gtceu:emerald_plate`
2. Seed autoclave inside the cleanroom: exquisite emerald + 16 mB europium → 10 % chance of a raw chip after 10 min at 320 EU/t. Feed one gem at a time and let a drawer hold the failures’ spare gems. — `gtceu:hv_autoclave`, `gtceu:exquisite_emerald_gem`, `gtceu:europium_bucket`
3. Hammer: 1 raw chip → 9 parts (100 ticks, 480 EU/t). A Robot Arm with an Item Filter takes the chip out of the seed autoclave into the hammer, but ONLY while the stock is below your target; keep the first chip until the part loop has produced a second one. — `gtceu:hv_forge_hammer`, `gtceu:raw_crystal_chip_parts`
4. Loop autoclave (second machine, cleanroom): 1 part + 16 mB europium → 1 raw chip in 10 min at 480 EU/t, 100 %. Its output goes back to the chip drawer; one chip per 10 minutes per machine, so add machines until you cover your crystal computer plan. — `gtceu:hv_autoclave`, `gtceu:raw_crystal_chip`, `gtceu:europium_bucket`
5. EBF with 16 HSS-G coils (5400 K): input bus with the raw chip + emerald plate, a fluid input hatch fed with 1 B helium per run → engraved crystal chip in 45 s at 480 EU/t. Muffler hatch free above. — `gtceu:electric_blast_furnace`, `gtceu:hssg_coil_block`, `gtceu:engraved_crystal_chip`
6. Engrave: LuV Laser Engraver inside the cleanroom, 1 engraved chip + the lime lens in a ghost slot → Crystal CPU in 5 s at 10 000 EU/t (a LuV cable line). Output into a drawer with Keep Exact 4. — `gtceu:luv_laser_engraver`, `gtceu:crystal_cpu`, `gtceu:lime_glass_lens`
7. Easy to miss: each crystal computer (the second ZPM circuit) eats ONE crystal CPU, so a handful is plenty; the long part is the 10 minute autoclave clock, so start it a session before you need the circuits. — `functionalstorage:oak_1`, `gtceu:crystal_cpu`

## Tips

- Recipes (CircuitRecipes, GT fork): raw crystal chip = 1 exquisite emerald + 16 mB molten europium in an Autoclave, CLEANROOM, 12 000 ticks (10 min) at 320 EU/t, with only a 10 % chance (chancedOutput 1000 of 10 000, tier boost 2000). The pack REMOVES the olivine, mutagen and bacterial sludge autoclave variants (mass\_removals.js), so the emerald is the only way to the FIRST chip. Then the loop: Forge Hammer 1 raw crystal chip → 9 raw crystal chip PARTS (100 ticks, 480 EU/t), and 1 part + 16 mB europium in an Autoclave (cleanroom, 12 000 ticks, 480 EU/t) → 1 raw chip at 100 %. So one lucky chip becomes 9, then 81, as fast as you have autoclaves: the era text ‘loop the chip parts’ is exactly this.
- **Unverified** the autoclave tier boost. In GT each voltage tier above the recipe adds the ‘boost’ to a chanced output, which would make an IV autoclave about 50 % per exquisite emerald. The only fixed fact is 10 % at the base tier; test with one machine tier up before you grind emeralds.
- Exquisite emerald: gem conversion in MaterialRecipeHandler, laser engraver recipes with a NON-consumed white lens: 2 emeralds → 1 flawless emerald (300 ticks, 240 EU/t), 2 flawless → 1 exquisite. So 4 emeralds per exquisite gem; the cutter reverses it. Emeralds come from the sand sieve (guide base chapters: 16 emerald per 64 sand in the Mechanical Sieve) or gem ore processing. Since the loop makes chips for free after the first one, you need only one or two exquisite gems.
- Engraved crystal chip (BLAST\_RECIPES engraved\_crystal\_chip\_from\_emerald): 1 emerald plate + 1 raw crystal chip + 1000 mB helium in an EBF at 5000 K or more (HSS-G coils, 5400 K, are enough), 900 ticks (45 s) at 480 EU/t. The emerald plate is a Bender product of an emerald gem (Unverified plate machine/time). Helium: the same air/gas helium the vacuum freezer lines use.
- Crystal CPU (laser\_engraver crystal\_cpu): 1 engraved chip + a lime lens that is not consumed, cleanroom, 100 ticks at 10 000 EU/t. 10 000 EU/t is above an IV machine (8192 V), so this needs a LuV Laser Engraver (LuV hull + LuV emitter + LuV sensor; see luv\_components2). The Crystal SoC is a second engraving at 40 000 EU/t with a blue lens: a ZPM-tier machine, and not needed for the era.
- Europium: 16 mB per chip is nothing; the real europium use is fine wire for ZPM motors and voltage coils (luv\_fusion chain: 144 mB per 28.8 s run). So the LuV fusion reactor is also the start of the crystal line.
- Sub-steps people skip: (1) two autoclaves, one per recipe, because the part recipe and the gem recipe share an output but not an input; (2) cleanroom filter: both autoclaves must stand inside the cleanroom; (3) the lens stays in the engraver, keep a spare lime lens; (4) never hammer your LAST raw chip: put 1 or 2 aside as seed; (5) the EBF needs the helium input AND a 5000 K coil, a plain Kanthal furnace does not start the recipe.
- **Unverified** the plate recipe of emerald, the exact lens id, and whether a Large autoclave multi exists in this pack for bulk loops (check the multis list).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_autoclave` | 2 |
| `gtceu:hv_forge_hammer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:hssg_coil_block` | 16 |
| `gtceu:luv_laser_engraver` | 1 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `gtceu:crystal_cpu`, `gtceu:engraved_crystal_chip`, `gtceu:raw_crystal_chip`, `gtceu:raw_crystal_chip_parts`
