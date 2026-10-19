---
kind: chain
id: crop_greenhouse
order: 760
data:
  t: "Crops: Greenhouse (LV, day and night)"
  inf: true
  "n":
    - [sd, "8 Seeds (kept)", i, "minecraft:wheat_seeds"]
    - [w, "100 mB Water", f, "minecraft:water_bucket"]
    - [fz, "Fertilizer · circ 3", i, "gtceu:fertilizer"]
    - [gh, Greenhouse, m, "gtceu:greenhouse"]
    - [cr, "64 Crops", o, "minecraft:wheat"]
    - [sx, "32 Seeds (50 %)", o, "minecraft:wheat_seeds"]
  e: [[sd, gh], [w, gh], [fz, gh, "75 % used"], [gh, cr, "30 s"], [gh, sx]]
  tips:
    - |-
      Circuit 0: 16 crops · 1 + bone meal: 32 · 2 + compost: 48 · 3 + fertilizer: 64, all per 30 s at 16 EU/t.
    - Same multiblock as the tree greenhouse; one greenhouse runs one recipe, so build one for logs and one for crops.
    - "IV: Hydroponic Garden, up to 256 crops per 7.5 s."
  b: [["gtceu:greenhouse", 1], ["minecraft:wheat_seeds", 8]]
  how:
    - i: ["gtceu:greenhouse"]
      t: |-
        Greenhouse multiblock (see its materials: steel frames, obsidian glass, solid steel casings, grass, dirt, leaves, logs, soul infused blocks).
    - i: ["minecraft:wheat_seeds", "gtceu:fertilizer"]
      t: |-
        8 seeds kept in the input bus, 100 mB water per run, ghost circuit 3 and fertilizer: 64 crops every 30 s (128 per minute), 16 EU/t, day and night. The fertilizer is used 3 times in 4.
    - i: ["gtceu:mv_energy_input_hatch"]
      t: |-
        It overclocks: an MV energy hatch doubles the speed for 4× the power.
---
# Crops: Greenhouse (LV, day and night)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `crop_greenhouse` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-gh">
<div class="gt-head"><span class="gt-mname">Greenhouse</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Seeds (kept) (minecraft:wheat_seeds)"><img class="gt-ico" src="../../assets/icons/minecraft__wheat_seeds.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat Seeds</span><span class="gt-note">8 Seeds (kept)</span></span><span class="gt-slot gt-fluid" title="100 mB Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><span class="gt-note">100 mB Water</span></span><span class="gt-slot" title="Fertilizer · circ 3 (gtceu:fertilizer) - 75 % used"><img class="gt-ico" src="../../assets/icons/gtceu__fertilizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fertilizer</span><span class="gt-note">Fertilizer · circ 3</span><b class="gt-q">75 % used</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__greenhouse.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="64 Crops (minecraft:wheat) - 30 s"><img class="gt-ico" src="../../assets/icons/minecraft__wheat.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat</span><span class="gt-note">64 Crops</span></span><span class="gt-slot gt-outp" title="32 Seeds (50 %) (minecraft:wheat_seeds)"><img class="gt-ico" src="../../assets/icons/minecraft__wheat_seeds.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wheat Seeds</span><span class="gt-note">32 Seeds (50 %)</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:greenhouse</code></div>
</div>
</div>

## Flow

- [Greenhouse](#m-gh)

## How to build

1. Greenhouse multiblock (see its materials: steel frames, obsidian glass, solid steel casings, grass, dirt, leaves, logs, soul infused blocks). — `gtceu:greenhouse`
2. 8 seeds kept in the input bus, 100 mB water per run, ghost circuit 3 and fertilizer: 64 crops every 30 s (128 per minute), 16 EU/t, day and night. The fertilizer is used 3 times in 4. — `minecraft:wheat_seeds`, `gtceu:fertilizer`
3. It overclocks: an MV energy hatch doubles the speed for 4× the power. — `gtceu:mv_energy_input_hatch`

## Tips

- Circuit 0: 16 crops · 1 + bone meal: 32 · 2 + compost: 48 · 3 + fertilizer: 64, all per 30 s at 16 EU/t.
- Same multiblock as the tree greenhouse; one greenhouse runs one recipe, so build one for logs and one for crops.
- IV: Hydroponic Garden, up to 256 crops per 7.5 s.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:greenhouse` | 1 |
| `minecraft:wheat_seeds` | 8 |

## Needs / Feeds

- **Needs:** [Fertilizer (for the rubber extractor and greenhouses)](fertilizer.md)
- **Main source for:** `minecraft:wheat`
