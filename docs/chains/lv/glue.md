---
kind: chain
id: glue
order: 910
data:
  t: Glue line (resin → glue)
  inf: true
  "n":
    - [oak, Oak tree extractor, s, "start_core:large_arboreal_extractor"]
    - [rs, Resin, f, "thermal:resin_bucket"]
    - [ch, Charcoal, i, "minecraft:charcoal"]
    - [ma, Macerator, m, "gtceu:lv_macerator"]
    - [cd, Charcoal dust, x, "gtceu:charcoal_dust"]
    - [mx, Mixer, m, "gtceu:lv_mixer"]
    - [gl, Glue, o, "gtceu:glue_bucket"]
  e:
    - [oak, rs, "100–250 mB / 20 s"]
    - [rs, mx, "500 mB"]
    - [ch, ma]
    - [ma, cd]
    - [cd, mx, "1"]
    - [mx, gl, "500 mB / 10 s"]
  tips:
    - |-
      Same Large Arboreal Extractor as for latex, but built with oak logs and leaves: it gives resin.
    - Glue goes into circuit boards (100 mB), resistors (100 mB per 2) and phenolic boards (50 mB).
  b:
    - ["start_core:large_arboreal_extractor", 1]
    - ["gtceu:lv_macerator", 1]
    - ["gtceu:lv_mixer", 1]
    - ["thermal:fluid_cell", 1]
    - ["gtceu:iron_screw", 1]
  how:
    - i: ["start_core:large_arboreal_extractor", "minecraft:oak_log", "minecraft:oak_leaves"]
      t: |-
        Build a second Large Arboreal Extractor with 5 oak logs and 5 oak leaves: it outputs resin (100 mB per 20 s, 250 with an iron screw + fertilizer).
    - i: ["gtceu:lv_macerator", "gtceu:charcoal_dust"]
      t: |-
        Macerator: charcoal → charcoal dust (one per 500 mB of glue).
    - i: ["gtceu:lv_mixer", "gtceu:glue_bucket"]
      t: |-
        LV Mixer: 500 mB resin + 1 charcoal dust → 500 mB glue in 10 s (16 EU/t). Store it in a fluid cell; pipes feed the assemblers.
---
# Glue line (resin → glue)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `glue` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [Glue](../../plan/p3.md#glue)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-ma">
<div class="gt-head"><span class="gt-mname">Macerator</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Charcoal dust (gtceu:charcoal_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__charcoal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_macerator</code></div>
</div>
<div class="gt-panel t-lv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Resin (thermal:resin_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/thermal__resin_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Resin</span><b class="gt-q">500 mB</b></span><span class="gt-slot" title="Charcoal dust (gtceu:charcoal_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__charcoal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Glue (gtceu:glue_bucket) - 500 mB / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__glue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glue Bucket</span><b class="gt-q">500 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
</div>

## Flow

- [Macerator](#m-ma) → [Mixer](#m-mx)

### Direct steps

- Oak tree extractor → Resin (100–250 mB / 20 s)

## How to build

1. Build a second Large Arboreal Extractor with 5 oak logs and 5 oak leaves: it outputs resin (100 mB per 20 s, 250 with an iron screw + fertilizer). — `start_core:large_arboreal_extractor`, `minecraft:oak_log`, `minecraft:oak_leaves`
2. Macerator: charcoal → charcoal dust (one per 500 mB of glue). — `gtceu:lv_macerator`, `gtceu:charcoal_dust`
3. LV Mixer: 500 mB resin + 1 charcoal dust → 500 mB glue in 10 s (16 EU/t). Store it in a fluid cell; pipes feed the assemblers. — `gtceu:lv_mixer`, `gtceu:glue_bucket`

## Tips

- Same Large Arboreal Extractor as for latex, but built with oak logs and leaves: it gives resin.
- Glue goes into circuit boards (100 mB), resistors (100 mB per 2) and phenolic boards (50 mB).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:large_arboreal_extractor` | 1 |
| `gtceu:lv_macerator` | 1 |
| `gtceu:lv_mixer` | 1 |
| `thermal:fluid_cell` | 1 |
| `gtceu:iron_screw` | 1 |

## Needs / Feeds

- **Needs:** [Charcoal &amp; creosote: Coke Oven](../steam/charcoal.md)
- **Main source for:** `gtceu:glue_bucket`
