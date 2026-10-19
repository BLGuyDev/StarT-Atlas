---
kind: chain
id: fertilizer
order: 880
data:
  t: Fertilizer (for the rubber extractor and greenhouses)
  inf: true
  "n":
    - [sa, Sapling, i, "minecraft:oak_sapling"]
    - [ba, "Wooden Barrel · compost", m, "gtceu:barrel"]
    - [di, Dirt, x, "minecraft:dirt"]
    - [wp, "2 Wood pulp", i, "gtceu:wood_dust"]
    - [sd, "4 Sand", i, "minecraft:sand"]
    - [wa, "1 B Water", f, "minecraft:water_bucket"]
    - [mx, Mixer, m, "gtceu:lv_mixer"]
    - [fz, "4 Fertilizer", o, "gtceu:fertilizer"]
  e: [[sa, ba], [ba, di], [di, mx, "1"], [wp, mx], [sd, mx], [wa, mx], [mx, fz, "5 s"]]
  tips:
    - |-
      LV Mixer: 1 dirt + 2 wood pulp + 4 sand + 1 B water → 4 fertilizer in 5 s at 30 EU/t.
    - One run feeds a Large Arboreal Extractor for about 5 minutes (it uses fertilizer on 1 run in 4).
  b:
    - ["gtceu:lv_mixer", 1]
    - ["gtceu:barrel", 1]
    - ["functionalstorage:oak_1", 2]
    - ["modularrouters:modular_router", 1]
  how:
    - i: ["gtceu:barrel", "minecraft:oak_sapling", "minecraft:dirt"]
      t: |-
        Dirt: a Wooden Barrel in compost mode fed spare saplings from the tree farm.
    - i: ["gtceu:wood_dust", "minecraft:sand"]
      t: Wood pulp from the treated wood cutter; sand from the sand sieve line (hammer on gravel).
    - i: ["gtceu:lv_mixer", "gtceu:fertilizer"]
      t: |-
        LV Mixer with water piped in: 4 fertilizer per run. Routers move dirt, pulp and sand from their drawers.
---
# Fertilizer (for the rubber extractor and greenhouses)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `fertilizer` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Rubber and liquid rubber](../../plan/p3.md#rubber)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-ba">
<div class="gt-head"><span class="gt-mname">Wooden Barrel · compost</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sapling (minecraft:oak_sapling)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_sapling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Sapling</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Dirt (minecraft:dirt)"><img class="gt-ico" src="../../assets/icons/minecraft__dirt.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dirt</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:barrel</code></div>
</div>
<div class="gt-panel t-lv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Dirt (minecraft:dirt) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__dirt.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dirt</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Wood pulp (gtceu:wood_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Dust</span><span class="gt-note">2 Wood pulp</span></span><span class="gt-slot" title="4 Sand (minecraft:sand)"><img class="gt-ico" src="../../assets/icons/minecraft__sand.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sand</span><span class="gt-note">4 Sand</span></span><span class="gt-slot gt-fluid" title="1 B Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><span class="gt-note">1 B Water</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="4 Fertilizer (gtceu:fertilizer) - 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__fertilizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fertilizer</span><span class="gt-note">4 Fertilizer</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
</div>

## Flow

- [Wooden Barrel · compost](#m-ba) → [Mixer](#m-mx)

## How to build

1. Dirt: a Wooden Barrel in compost mode fed spare saplings from the tree farm. — `gtceu:barrel`, `minecraft:oak_sapling`, `minecraft:dirt`
2. Wood pulp from the treated wood cutter; sand from the sand sieve line (hammer on gravel). — `gtceu:wood_dust`, `minecraft:sand`
3. LV Mixer with water piped in: 4 fertilizer per run. Routers move dirt, pulp and sand from their drawers. — `gtceu:lv_mixer`, `gtceu:fertilizer`

## Tips

- LV Mixer: 1 dirt + 2 wood pulp + 4 sand + 1 B water → 4 fertilizer in 5 s at 30 EU/t.
- One run feeds a Large Arboreal Extractor for about 5 minutes (it uses fertilizer on 1 run in 4).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_mixer` | 1 |
| `gtceu:barrel` | 1 |
| `functionalstorage:oak_1` | 2 |
| `modularrouters:modular_router` | 1 |

## Needs / Feeds

- **Needs:** [Treated wood: cutter + spout](treated_wood.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md)
- **Feeds:** [Rubber: Large Arboreal Extractor](../steam/rubber.md), [Crops: Greenhouse (LV, day and night)](crop_greenhouse.md)
- **Main source for:** `gtceu:fertilizer`
