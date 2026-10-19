---
kind: chain
id: uv_solder
order: 1740
data:
  t: |-
    UV solder: indium tin lead cadmium soldering alloy in the Alloy Blast Smelter (2880 mB per 14 dust batch, circuit 14, 3000 K)
  inf: true
  "n":
    - - g1
      - |-
        14 indium dust · 3 tin dust · 2 lead dust · 1 cadmium dust · circuit 14
      - g
      - functionalstorage:oak_1
      - - [Indium dust, "gtceu:indium_dust"]
        - [Tin dust, "gtceu:tin_dust"]
        - [Lead dust, "gtceu:lead_dust"]
        - [Cadmium dust, "gtceu:cadmium_dust"]
    - [ab, "Alloy Blast Smelter · 14 s · 3000 K · ZPM power", m, "gtceu:alloy_blast_smelter"]
    - [so, "ITLC soldering alloy 2880 mB (20 ingots)", o, "gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket"]
    - [mx, "Alt: mixer · 20 s · 45 000 EU/t → 20 dust (for the Super EBF)", m, "gtceu:uv_mixer"]
  e: [[g1, ab, "20 dust"], [ab, so, "2880 mB / 14 s"], [g1, mx, alt]]
  tips:
    - |-
      Recipe (kjs additions/recipe_changes.js, verified): Alloy Blast Smelter, circuit 14, 14 indium + 3 tin + 2 lead + 1 cadmium dust → 2880 mB indium tin lead cadmium soldering alloy, 280 ticks (14 s), blast temperature 3000 K (any coil from nichrome 2700 K ... use RTM 3600 K coils; the 3000 K figure is the minimum), power listed as EUtVH(ZPM) (about 65 536 EU/t, half of 131 072; Unverified exact formula). The same recipe as a mixer (kjs abydos_lines/misc_materials.js): 14 indium + 3 tin + 2 lead + 1 cadmium dust → 20 dust, 400 ticks, 45 000 EU/t.
    - |-
      Why: ITLC solder replaces plain soldering alloy in every UV recipe: UV components (576 mB each, x8 scaler), the wetware computer (864 mB) and mainframe (1728 mB), the UV hatches, the fusion reactor (1152 mB), Titan Forge (7200 mB), compact assembly line (14 688 mB). Plan 10 to 20 B per day of crafting: a single ABS batch every 14 s gives 12 B per hour only per smelter, so run two.
    - The next solder (naquadated soldering alloy, ABS circuit 8, 8980 K, 2250 ticks, 5760 mB from 3 tin + 18 indium + 6 silver + 4 lutetium + 3 cerium + 3 naquadah + 1 trinium + 2 lead dust, EUtVH(UHV)) is the UEV page solder; the neutrindium one is UIV.
    - |-
      Sub-steps people skip: (1) indium dust 14 per batch is the real input: the indium source is a ZPM-era chain (README: indium source Unverified); (2) cadmium is only 1 per batch; (3) output goes to a drum with Keep Exact valves to the assemblers; (4) circuit 14 on the ABS, not 4.
    - |-
      Unverified: indium and cadmium sources, the exact EU of the smelter recipe.
  b:
    - ["gtceu:alloy_blast_smelter", 2]
    - ["functionalstorage:oak_1", 6]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 5]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:indium_dust", "gtceu:cadmium_dust", "gtceu:lead_dust"]
      t: |-
        Drawers first, one per dust: indium (Keep Exact 14), tin (3), lead (2), cadmium (1). One router with four Item Filters per smelter.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket"]
      t: |-
        Smelter: circuit 14, coils ≥ 3000 K, muffler; 2880 mB per 14 s into a drum through a Pipez fluid pipe.
    - i: ["gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket", "functionalstorage:oak_1"]
      t: Drum with Pipez fluid pipes and valves to the Assembly Line hatches. Keep Exact 4 B in the drum; refill from the second smelter.
    - i: ["gtceu:uv_mixer", "gtceu:indium_tin_lead_cadmium_soldering_alloy_dust"]
      t: Optional mixer version for dust stock; the Alloy Blast Smelter is the one that gives the liquid directly.
    - i: ["functionalstorage:oak_1", "gtceu:indium_dust"]
      t: |-
        Easy to miss: indium and cadmium stock decides the solder rate; check the sources before building more smelters.
---
# UV solder: indium tin lead cadmium soldering alloy in the Alloy Blast Smelter (2880 mB per 14 dust batch, circuit 14, 3000 K)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_solder` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [PEEK, polyimide and UV solder](../../plan/p14.md#uvchem)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-ab">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · 14 s · 3000 K · ZPM power</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="14 indium dust · 3 tin dust · 2 lead dust · 1 cadmium dust · circuit 14 (functionalstorage:oak_1) - 20 dust"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">14 indium dust · 3 tin dust · 2 lead dust · 1 cadmium dust · circuit 14</span><span class="gt-sub"><span>Indium dust</span><span>Tin dust</span><span>Lead dust</span><span>Cadmium dust</span></span><b class="gt-q">20 dust</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">14 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ITLC soldering alloy 2880 mB (20 ingots) (gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket) - 2880 mB / 14 s"><img class="gt-ico" src="../../assets/icons/gtceu__indium_tin_lead_cadmium_soldering_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Indium Tin Lead Cadmium Soldering Alloy Bucket</span><span class="gt-note">ITLC soldering alloy 2880 mB (20 ingots)</span><b class="gt-q">2880 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
<div class="gt-panel t-uv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Alt: mixer · 20 s · 45 000 EU/t → 20 dust (for the Super EBF)</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="14 indium dust · 3 tin dust · 2 lead dust · 1 cadmium dust · circuit 14 (functionalstorage:oak_1) - alt"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">14 indium dust · 3 tin dust · 2 lead dust · 1 cadmium dust · circuit 14</span><span class="gt-sub"><span>Indium dust</span><span>Tin dust</span><span>Lead dust</span><span>Cadmium dust</span></span><b class="gt-q">alt</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_mixer</code></div>
</div>
</div>

## Flow

- [Alloy Blast Smelter · 14 s · 3000 K · ZPM power](#m-ab)
- [Alt: mixer · 20 s · 45 000 EU/t → 20 dust (for the Super EBF)](#m-mx)

## How to build

1. Drawers first, one per dust: indium (Keep Exact 14), tin (3), lead (2), cadmium (1). One router with four Item Filters per smelter. — `functionalstorage:oak_1`, `gtceu:indium_dust`, `gtceu:cadmium_dust`, `gtceu:lead_dust`
2. Smelter: circuit 14, coils ≥ 3000 K, muffler; 2880 mB per 14 s into a drum through a Pipez fluid pipe. — `gtceu:alloy_blast_smelter`, `gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket`
3. Drum with Pipez fluid pipes and valves to the Assembly Line hatches. Keep Exact 4 B in the drum; refill from the second smelter. — `gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket`, `functionalstorage:oak_1`
4. Optional mixer version for dust stock; the Alloy Blast Smelter is the one that gives the liquid directly. — `gtceu:uv_mixer`, `gtceu:indium_tin_lead_cadmium_soldering_alloy_dust`
5. Easy to miss: indium and cadmium stock decides the solder rate; check the sources before building more smelters. — `functionalstorage:oak_1`, `gtceu:indium_dust`

## Tips

- Recipe (kjs additions/recipe\_changes.js, verified): Alloy Blast Smelter, circuit 14, 14 indium + 3 tin + 2 lead + 1 cadmium dust → 2880 mB indium tin lead cadmium soldering alloy, 280 ticks (14 s), blast temperature 3000 K (any coil from nichrome 2700 K ... use RTM 3600 K coils; the 3000 K figure is the minimum), power listed as EUtVH(ZPM) (about 65 536 EU/t, half of 131 072; Unverified exact formula). The same recipe as a mixer (kjs abydos\_lines/misc\_materials.js): 14 indium + 3 tin + 2 lead + 1 cadmium dust → 20 dust, 400 ticks, 45 000 EU/t.
- Why: ITLC solder replaces plain soldering alloy in every UV recipe: UV components (576 mB each, x8 scaler), the wetware computer (864 mB) and mainframe (1728 mB), the UV hatches, the fusion reactor (1152 mB), Titan Forge (7200 mB), compact assembly line (14 688 mB). Plan 10 to 20 B per day of crafting: a single ABS batch every 14 s gives 12 B per hour only per smelter, so run two.
- The next solder (naquadated soldering alloy, ABS circuit 8, 8980 K, 2250 ticks, 5760 mB from 3 tin + 18 indium + 6 silver + 4 lutetium + 3 cerium + 3 naquadah + 1 trinium + 2 lead dust, EUtVH(UHV)) is the UEV page solder; the neutrindium one is UIV.
- Sub-steps people skip: (1) indium dust 14 per batch is the real input: the indium source is a ZPM-era chain (README: indium source Unverified); (2) cadmium is only 1 per batch; (3) output goes to a drum with Keep Exact valves to the assemblers; (4) circuit 14 on the ABS, not 4.
- **Unverified** indium and cadmium sources, the exact EU of the smelter recipe.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:alloy_blast_smelter` | 2 |
| `functionalstorage:oak_1` | 6 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 5 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:indium_tin_lead_cadmium_soldering_alloy_bucket`, `gtceu:indium_tin_lead_cadmium_soldering_alloy_dust`
