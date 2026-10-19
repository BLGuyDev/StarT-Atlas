---
kind: chain
id: alloys_smelter
order: 750
data:
  t: "Alloys: Steam / LV Alloy Smelter (more per ingot)"
  inf: false
  "n":
    - [cu, "3 Copper", i, "minecraft:copper_ingot"]
    - [sn, "1 Tin", i, "gtceu:tin_ingot"]
    - [fe, "2 Iron", i, "minecraft:iron_ingot"]
    - [ni, "1 Nickel", i, "gtceu:nickel_ingot"]
    - [st, "Steam 32 mB/t", f, "gtceu:steam_bucket"]
    - [as, HP Steam Alloy Smelter, m, "gtceu:hp_steam_alloy_smelter"]
    - [bz, "4 Bronze", o, "gtceu:bronze_ingot"]
    - [iv, "3 Invar", o, "gtceu:invar_ingot"]
  e: [[cu, as], [sn, as], [fe, as], [ni, as], [st, as], [as, bz, "10 s"], [as, iv, "7.5 s"]]
  tips:
    - |-
      Every GT alloy is the full sum of its parts: bronze 3+1 → 4, brass 3+1 → 4, cupronickel 1+1 → 2, invar 2+1 → 3, tin alloy 1+1 → 2, battery alloy 4+1 → 5, electrum 1+1 → 2.
    - Time = 2.5 s per output ingot at 16 EU/t, so the steam version runs them at full speed.
    - |-
      Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.
  b:
    - ["gtceu:hp_steam_alloy_smelter", 1]
    - ["gtceu:hp_steam_solid_boiler", 2]
    - ["pipez:item_pipe", 4]
    - ["functionalstorage:oak_1", 2]
  how:
    - i: ["gtceu:hp_steam_alloy_smelter"]
      t: |-
        High Pressure Steam Alloy Smelter (bronze version + steel plate, wrought iron plates and tin alloy pipe). Steam machines run any alloy recipe up to 16 EU/t at full speed: 2 mB steam per EU, 32 mB/t while working.
    - i: ["gtceu:hp_steam_solid_boiler", "minecraft:charcoal"]
      t: Two HP Solid Boilers (15 mB/t each when hot) keep it running nonstop on charcoal.
    - i: ["minecraft:copper_ingot", "gtceu:tin_ingot", "gtceu:bronze_ingot"]
      t: |-
        3 copper + 1 tin → 4 bronze in 10 s (the Create mixer gives 3). Same 33 % gain for brass; invar +50 %, tin alloy double.
    - i: ["gtceu:lv_alloy_smelter"]
      t: At LV swap to LV Alloy Smelters (same recipes, 16 EU/t); at HV the Multi Smelter runs them in parallel.
---
# Alloys: Steam / LV Alloy Smelter (more per ingot)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `alloys_smelter`

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Alloys (bronze, red alloy, cupronickel, tin alloy)](../../plan/p3.md#alloys)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-as">
<div class="gt-head"><span class="gt-mname">HP Steam Alloy Smelter</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Copper (minecraft:copper_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span><span class="gt-note">3 Copper</span></span><span class="gt-slot" title="1 Tin (gtceu:tin_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Ingot</span><span class="gt-note">1 Tin</span></span><span class="gt-slot" title="2 Iron (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span><span class="gt-note">2 Iron</span></span><span class="gt-slot" title="1 Nickel (gtceu:nickel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Ingot</span><span class="gt-note">1 Nickel</span></span><span class="gt-slot gt-fluid" title="Steam 32 mB/t (gtceu:steam_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__steam_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steam</span><span class="gt-note">Steam 32 mB/t</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hp_steam_alloy_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s · 7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="4 Bronze (gtceu:bronze_ingot) - 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Ingot</span><span class="gt-note">4 Bronze</span></span><span class="gt-slot gt-outp" title="3 Invar (gtceu:invar_ingot) - 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__invar_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Invar Ingot</span><span class="gt-note">3 Invar</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hp_steam_alloy_smelter</code></div>
</div>
</div>

## Flow

- [HP Steam Alloy Smelter](#m-as)

## How to build

1. High Pressure Steam Alloy Smelter (bronze version + steel plate, wrought iron plates and tin alloy pipe). Steam machines run any alloy recipe up to 16 EU/t at full speed: 2 mB steam per EU, 32 mB/t while working. — `gtceu:hp_steam_alloy_smelter`
2. Two HP Solid Boilers (15 mB/t each when hot) keep it running nonstop on charcoal. — `gtceu:hp_steam_solid_boiler`, `minecraft:charcoal`
3. 3 copper + 1 tin → 4 bronze in 10 s (the Create mixer gives 3). Same 33 % gain for brass; invar +50 %, tin alloy double. — `minecraft:copper_ingot`, `gtceu:tin_ingot`, `gtceu:bronze_ingot`
4. At LV swap to LV Alloy Smelters (same recipes, 16 EU/t); at HV the Multi Smelter runs them in parallel. — `gtceu:lv_alloy_smelter`

## Tips

- Every GT alloy is the full sum of its parts: bronze 3+1 → 4, brass 3+1 → 4, cupronickel 1+1 → 2, invar 2+1 → 3, tin alloy 1+1 → 2, battery alloy 4+1 → 5, electrum 1+1 → 2.
- Time = 2.5 s per output ingot at 16 EU/t, so the steam version runs them at full speed.
- Needs copper, tin and iron ingots from the LV sieve line (ingots chain, LV era) and zinc or nickel dust from ore processing (ores, LV). Before that: hand sieve (stone era) and smelt the crushed ore in a furnace.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hp_steam_alloy_smelter` | 1 |
| `gtceu:hp_steam_solid_boiler` | 2 |
| `pipez:item_pipe` | 4 |
| `functionalstorage:oak_1` | 2 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md), [Ore processing](../lv/ores.md)
- **Feeds:** [Cupronickel coils ×16](../lv/coils.md)
- **Main source for:** `gtceu:bronze_ingot`
