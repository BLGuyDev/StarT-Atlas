---
kind: chain
id: sieve_manual
order: 510
data:
  t: Sieve station (manual)
  "n":
    - [c, Cobblestone, i, "minecraft:cobblestone"]
    - [h1, Hammer, m, "exnihilosequentia:stone_hammer"]
    - [g, Gravel, x, "minecraft:gravel"]
    - [sv, "Sieve + String Mesh", m, "exnihilosequentia:oak_sieve"]
    - [o1, "Crushed Copper 65 %", o, "gtceu:crushed_copper_ore"]
    - [o2, "Crushed Iron 45 %", o, "gtceu:crushed_iron_ore"]
    - [o3, "Crushed Tin 30 %", o, "gtceu:crushed_tin_ore"]
    - [o4, "Crushed Sphalerite 25 %", o, "gtceu:crushed_sphalerite_ore"]
    - [o5, "Crushed Magnetite 25 %", o, "gtceu:crushed_magnetite_ore"]
  e: [[c, h1], [h1, g], [g, sv], [sv, o1], [sv, o2], [sv, o3], [sv, o4], [sv, o5]]
  tips:
    - Hammer gravel again for sand (gems) and sand for dust (redstone, glowstone, sulfur, pearls). Tables in Resources.
    - Mud gives the slitake and mycelium spores; dirt gives every sapling.
  b:
    - ["exnihilosequentia:oak_sieve", 6]
    - ["exnihilosequentia:string_mesh", 6]
    - ["exnihilosequentia:stone_hammer", 1]
    - ["minecraft:hopper", 6]
    - ["functionalstorage:oak_1", 4]
  how:
    - i: ["exnihilosequentia:oak_sieve", "exnihilosequentia:string_mesh"]
      t: Place 6–8 Oak Sieves in a 2×3 / 2×4 block, each with a String Mesh.
    - i: ["minecraft:gravel"]
      t: |-
        Right-click with a stack of gravel: one click fills every adjacent sieve.
    - i: ["minecraft:hopper", "functionalstorage:oak_1"]
      t: Hoppers under the sieves send drops into drawers.
---
# Sieve station (manual)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `sieve_manual`

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Hand sieve](../../plan/p0.md#handsieve)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-h1">
<div class="gt-head"><span class="gt-mname">Hammer</span><span class="gt-badge t-mod">Ex Nihilo</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cobblestone (minecraft:cobblestone)"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__stone_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
</div>
<div class="gt-foot"><code>exnihilosequentia:stone_hammer</code></div>
</div>
<div class="gt-panel t-mod" id="m-sv">
<div class="gt-head"><span class="gt-mname">Sieve + String Mesh</span><span class="gt-badge t-mod">Ex Nihilo</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__oak_sieve.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Copper 65 % (gtceu:crushed_copper_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_copper_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Copper Ore</span><span class="gt-note">Crushed Copper 65 %</span></span><span class="gt-slot gt-outp" title="Crushed Iron 45 % (gtceu:crushed_iron_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_iron_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Iron Ore</span><span class="gt-note">Crushed Iron 45 %</span></span><span class="gt-slot gt-outp" title="Crushed Tin 30 % (gtceu:crushed_tin_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_tin_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Tin Ore</span><span class="gt-note">Crushed Tin 30 %</span></span><span class="gt-slot gt-outp" title="Crushed Sphalerite 25 % (gtceu:crushed_sphalerite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_sphalerite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Sphalerite Ore</span><span class="gt-note">Crushed Sphalerite 25 %</span></span><span class="gt-slot gt-outp" title="Crushed Magnetite 25 % (gtceu:crushed_magnetite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_magnetite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Magnetite Ore</span><span class="gt-note">Crushed Magnetite 25 %</span></span></div>
</div>
<div class="gt-foot"><code>exnihilosequentia:oak_sieve</code></div>
</div>
</div>

## Flow

- [Hammer](#m-h1) → [Sieve + String Mesh](#m-sv)

## How to build

1. Place 6–8 Oak Sieves in a 2×3 / 2×4 block, each with a String Mesh. — `exnihilosequentia:oak_sieve`, `exnihilosequentia:string_mesh`
2. Right-click with a stack of gravel: one click fills every adjacent sieve. — `minecraft:gravel`
3. Hoppers under the sieves send drops into drawers. — `minecraft:hopper`, `functionalstorage:oak_1`

## Tips

- Hammer gravel again for sand (gems) and sand for dust (redstone, glowstone, sulfur, pearls). Tables in Resources.
- Mud gives the slitake and mycelium spores; dirt gives every sapling.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `exnihilosequentia:oak_sieve` | 6 |
| `exnihilosequentia:string_mesh` | 6 |
| `exnihilosequentia:stone_hammer` | 1 |
| `minecraft:hopper` | 6 |
| `functionalstorage:oak_1` | 4 |

## Needs / Feeds

- **Needs:** [Infinite cobble &amp; blackstone](inf_cobble.md)
- **Feeds:** [Barrel transformations](barrel.md), [LV circuit parts from earlier lines](../feeders/circuit_parts.md)
- **Main source for:** `exnihilosequentia:mycelium_spores`, `thermal:slime_mushroom_spores`
