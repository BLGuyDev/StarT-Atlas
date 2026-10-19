---
kind: chain
id: alloys
order: 70
data:
  t: "Alloys: Create heated mixer"
  "n":
    - [cu, Copper, i, "minecraft:copper_ingot"]
    - [sn, Tin, i, "gtceu:tin_ingot"]
    - [zn, Zinc, i, "gtceu:zinc_dust"]
    - [rs, Redstone, i, "minecraft:redstone"]
    - [fe, Iron, i, "minecraft:iron_ingot"]
    - [ni, Nickel, i, "gtceu:nickel_ingot"]
    - [mx, Heated Mixer, m, "create:mechanical_mixer"]
    - [bz, "Bronze ×3", o, "gtceu:bronze_ingot"]
    - [ba, "Brass ×3", o, "gtceu:brass_ingot"]
    - [ra, Red Alloy, o, "gtceu:red_alloy_ingot"]
    - [iv, "Invar ×2", o, "gtceu:invar_ingot"]
  e:
    - [cu, mx, "3"]
    - [sn, mx, "1"]
    - [zn, mx, "1"]
    - [rs, mx, "4"]
    - [fe, mx, "2"]
    - [ni, mx, "1"]
    - [mx, bz]
    - [mx, ba]
    - [mx, ra]
    - [mx, iv]
  tips:
    - Bronze 3 Cu + Sn → 3 · Brass 3 Cu + Zn → 3 · Invar 2 Fe + Ni → 2 · Tin alloy Sn + Fe → 1 · Red alloy Cu + 4 redstone → 1 · Soul infused 2 soul sand dust + invar → 1.
    - |-
      A GT alloy smelter makes more from the same metal: 4 bronze, 4 brass, 3 invar, 2 tin alloy. Use the mixer only before you have steam. Soul infused also has an alloy smelter recipe (3 ingots per run, see the soul infused line).
    - |-
      Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.
  b:
    - ["create:mechanical_mixer", 1]
    - ["create:basin", 1]
    - ["createlowheated:basic_burner", 1]
    - ["create:mechanical_press", 1]
    - ["create:depot", 1]
  how:
    - i: ["create:basin", "create:mechanical_mixer"]
      t: Basin with a Mechanical Mixer above it.
    - i: ["createlowheated:basic_burner", "minecraft:charcoal"]
      t: Basic Burner below the basin, fed charcoal by a funnel (low heat is enough for every alloy).
    - i: ["create:andesite_funnel"]
      t: Funnels on the basin sides insert the metals and pull the alloy out into a drawer.
    - i: ["create:mechanical_press", "create:depot"]
      t: A Press over a Depot turns ingots into plates 1:1.
---
# Alloys: Create heated mixer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `alloys`

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Alloys (bronze, red alloy, cupronickel, tin alloy)](../../plan/p3.md#alloys)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-mx">
<div class="gt-head"><span class="gt-mname">Heated Mixer</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Copper (minecraft:copper_ingot) - 3"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span><b class="gt-q">3</b></span><span class="gt-slot" title="Tin (gtceu:tin_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__tin_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Ingot</span><b class="gt-q">1</b></span><span class="gt-slot" title="Zinc (gtceu:zinc_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zinc_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Zinc Dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="Redstone (minecraft:redstone) - 4"><img class="gt-ico" src="../../assets/icons/minecraft__redstone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Redstone</span><b class="gt-q">4</b></span><span class="gt-slot" title="Iron (minecraft:iron_ingot) - 2"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><b class="gt-q">2</b></span><span class="gt-slot" title="Nickel (gtceu:nickel_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Bronze ×3 (gtceu:bronze_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Ingot</span><span class="gt-note">Bronze ×3</span></span><span class="gt-slot gt-outp" title="Brass ×3 (gtceu:brass_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__brass_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Brass Ingot</span><span class="gt-note">Brass ×3</span></span><span class="gt-slot gt-outp" title="Red Alloy (gtceu:red_alloy_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__red_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Red Alloy Ingot</span></span><span class="gt-slot gt-outp" title="Invar ×2 (gtceu:invar_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__invar_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Invar Ingot</span><span class="gt-note">Invar ×2</span></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_mixer</code></div>
</div>
</div>

## Flow

- [Heated Mixer](#m-mx)

## How to build

1. Basin with a Mechanical Mixer above it. — `create:basin`, `create:mechanical_mixer`
2. Basic Burner below the basin, fed charcoal by a funnel (low heat is enough for every alloy). — `createlowheated:basic_burner`, `minecraft:charcoal`
3. Funnels on the basin sides insert the metals and pull the alloy out into a drawer. — `create:andesite_funnel`
4. A Press over a Depot turns ingots into plates 1:1. — `create:mechanical_press`, `create:depot`

## Tips

- Bronze 3 Cu + Sn → 3 · Brass 3 Cu + Zn → 3 · Invar 2 Fe + Ni → 2 · Tin alloy Sn + Fe → 1 · Red alloy Cu + 4 redstone → 1 · Soul infused 2 soul sand dust + invar → 1.
- A GT alloy smelter makes more from the same metal: 4 bronze, 4 brass, 3 invar, 2 tin alloy. Use the mixer only before you have steam. Soul infused also has an alloy smelter recipe (3 ingots per run, see the soul infused line).
- Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:mechanical_mixer` | 1 |
| `create:basin` | 1 |
| `createlowheated:basic_burner` | 1 |
| `create:mechanical_press` | 1 |
| `create:depot` | 1 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md), [Ore processing](../lv/ores.md), [Infinite redstone, sulfur &amp; pearls (dust sieve)](../feeders/sieve_dust.md)
- **Main source for:** `gtceu:red_alloy_single_cable`, `gtceu:tin_alloy_bucket`, `gtceu:invar_ingot`
