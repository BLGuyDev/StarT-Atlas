---
kind: chain
id: charcoal
order: 420
data:
  t: "Charcoal & creosote: Coke Oven"
  inf: true
  "n":
    - [tf, Create tree farm, s, "create:mechanical_saw"]
    - [lg, Logs, x, "minecraft:oak_log"]
    - [co, "Coke Oven ×2", m, "gtceu:coke_oven"]
    - [hh, Coke Oven Hatch, m, "gtceu:coke_oven_hatch"]
    - [ch, Charcoal, o, "minecraft:charcoal"]
    - [cr, Creosote, f, "gtceu:creosote_bucket"]
  e: [[tf, lg], [lg, co, hatch in], [co, hh], [hh, ch], [hh, cr]]
  tips:
    - |-
      1 log → 1 charcoal + 250 mB creosote per 45 s: 1.3 charcoal per minute per oven. Build them for creosote (lubricant → drilling fluid), not for charcoal.
    - "Sugar cane: 8 → 1 charcoal + 50 mB creosote in 60 s."
    - "MV: the Pyrolyse Oven is 20× faster per machine."
  b: [["gtceu:coke_oven", 2], ["gtceu:coke_oven_hatch", 1], ["pipez:item_pipe", 6], ["thermal:fluid_cell", 1]]
  how:
    - i: ["gtceu:coke_oven", "gtceu:coke_oven_bricks"]
      t: Two Coke Ovens (25 coke oven bricks each) sharing one wall.
    - i: ["gtceu:coke_oven_hatch"]
      t: |-
        A Coke Oven Hatch in the shared wall: pipe logs in, and it pushes out charcoal and creosote.
    - i: ["minecraft:charcoal", "gtceu:creosote_bucket"]
      t: Each oven turns 1 log into 1 charcoal + 250 mB creosote every 45 s. Two ovens make 2.7 charcoal and 667 mB creosote per minute.
    - i: ["thermal:fluid_cell"]
      t: |-
        Store the creosote in a Fluid Cell: it becomes lubricant (and then drilling fluid) in LV.
---
# Charcoal &amp; creosote: Coke Oven

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `charcoal` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Charcoal and creosote](../../plan/p1.md#fuel)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-co">
<div class="gt-head"><span class="gt-mname">Coke Oven ×2</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Logs (minecraft:oak_log) - hatch in"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs</span><b class="gt-q">hatch in</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__coke_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-hh" title="Coke Oven Hatch (gtceu:coke_oven_hatch)"><img class="gt-ico" src="../../assets/icons/gtceu__coke_oven_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Coke Oven Hatch</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:coke_oven</code></div>
</div>
<div class="gt-panel t-mod" id="m-hh">
<div class="gt-head"><span class="gt-mname">Coke Oven Hatch</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-co" title="Coke Oven ×2 (gtceu:coke_oven)"><img class="gt-ico" src="../../assets/icons/gtceu__coke_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Coke Oven</span><span class="gt-note">Coke Oven ×2</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__coke_oven_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span><span class="gt-slot gt-fluid" title="Creosote (gtceu:creosote_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__creosote_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Creosote</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:coke_oven_hatch</code></div>
</div>
</div>

## Flow

- [Coke Oven ×2](#m-co) → [Coke Oven Hatch](#m-hh)

### Direct steps

- Create tree farm → Logs

## How to build

1. Two Coke Ovens (25 coke oven bricks each) sharing one wall. — `gtceu:coke_oven`, `gtceu:coke_oven_bricks`
2. A Coke Oven Hatch in the shared wall: pipe logs in, and it pushes out charcoal and creosote. — `gtceu:coke_oven_hatch`
3. Each oven turns 1 log into 1 charcoal + 250 mB creosote every 45 s. Two ovens make 2.7 charcoal and 667 mB creosote per minute. — `minecraft:charcoal`, `gtceu:creosote_bucket`
4. Store the creosote in a Fluid Cell: it becomes lubricant (and then drilling fluid) in LV. — `thermal:fluid_cell`

## Tips

- 1 log → 1 charcoal + 250 mB creosote per 45 s: 1.3 charcoal per minute per oven. Build them for creosote (lubricant → drilling fluid), not for charcoal.
- Sugar cane: 8 → 1 charcoal + 50 mB creosote in 60 s.
- MV: the Pyrolyse Oven is 20× faster per machine.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:coke_oven` | 2 |
| `gtceu:coke_oven_hatch` | 1 |
| `pipez:item_pipe` | 6 |
| `thermal:fluid_cell` | 1 |

## Needs / Feeds

- **Feeds:** [LV power grid](../power/power_lv.md), [LV circuit parts from earlier lines](../feeders/circuit_parts.md), [SMDs from HV Assemblers (one machine per part)](../hv/smd.md), [LV power: boilers + steam turbines](../power/power_steam.md), [Create steam power: Steam Engines + Generator Coils](power_steam_engine.md), [Gravel, sand &amp; dust: Steam Forge Hammer](gravel_steam.md), [Steel: Primitive Blast Furnace](steel_pbf.md), [Glue line (resin → glue)](../lv/glue.md), [Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer](../ev/titanium_line.md)
- **Main source for:** `minecraft:charcoal`, `gtceu:creosote_bucket`, `gtceu:carbon_dust`
