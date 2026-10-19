---
kind: chain
id: mv_fecl3
order: 960
data:
  t: Etching fluid (iron III chloride)
  inf: true
  "n":
    - [fe, Iron ingot, i, "minecraft:iron_ingot"]
    - [ma, LV Macerator, m, "gtceu:lv_macerator"]
    - [fd, Iron dust, x, "gtceu:iron_dust"]
    - [hc, Hydrochloric acid, f, "gtceu:hydrochloric_acid_bucket"]
    - [cr, "LV Chemical Reactor · circuit 1", m, "gtceu:lv_chemical_reactor"]
    - [fc, Iron III chloride, o, "gtceu:iron_iii_chloride_bucket"]
    - [hy, "Hydrogen (surplus)", f, "gtceu:hydrogen_bucket"]
  e: [[fe, ma], [ma, fd, "1"], [fd, cr, "1"], [hc, cr, "3 B"], [cr, fc, "1 B / 20 s"], [cr, hy, "3 B"]]
  tips:
    - One reaction (1 iron dust + 3 B acid) makes 1 B of etchant = 10 boards at 100 mB each.
    - |-
      The reaction gives 3 B of hydrogen back. The electrolyzer already makes exactly the hydrogen the acid reactor needs, so this hydrogen is surplus: put a Fluid Voiding Cover (switch it on with a soft mallet) or a drum on that output, or the reactor stops when its tank is full.
    - |-
      Sodium persulfate etches too (200 mB per board) but needs sulfuric acid and sodium bisulfate first. The pack’s cupric chloride etch (50 mB per board) needs an HV reactor (240 EU/t) and an EV mixer: not yet.
  b:
    - ["gtceu:lv_macerator", 1]
    - ["gtceu:lv_chemical_reactor", 1]
    - ["gtceu:steel_drum", 2]
    - ["gtceu:fluid_voiding_cover", 1]
    - ["pipez:fluid_pipe", 8]
    - ["functionalstorage:oak_1", 2]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:lv_macerator", "gtceu:iron_dust"]
      t: |-
        LV Macerator on a drawer of iron ingots: 1 ingot → 1 iron dust (GregTech macerator recycling, yield 1.0 in gtceu.yaml; you need 1 dust per 10 boards, so very little).
    - i: ["gtceu:lv_chemical_reactor", "gtceu:iron_iii_chloride_bucket"]
      t: |-
        LV Chemical Reactor with ghost circuit 1: 1 iron dust + 3000 mB hydrochloric acid → 1000 mB iron III chloride + 3000 mB hydrogen in 20 s (30 EU/t). Acid comes by Pipez fluid pipe from the acid drum; the etchant goes into its own drum.
    - i: ["gtceu:fluid_voiding_cover", "gtceu:hydrogen_bucket"]
      t: |-
        Hydrogen output: Fluid Voiding Cover on the pipe (or a steel drum). 300 mB of hydrogen per board you etch.
---
# Etching fluid (iron III chloride)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_fecl3` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Etching fluid (iron III chloride)](../../plan/p6.md#fecl3)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-ma">
<div class="gt-head"><span class="gt-mname">LV Macerator</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron ingot (minecraft:iron_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Iron dust (gtceu:iron_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_macerator</code></div>
</div>
<div class="gt-panel t-lv" id="m-cr">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron dust (gtceu:iron_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Hydrochloric acid (gtceu:hydrochloric_acid_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrochloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrochloric Acid</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Iron III chloride (gtceu:iron_iii_chloride_bucket) - 1 B / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__iron_iii_chloride_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Iii Chloride Bucket</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-fluid" title="Hydrogen (surplus) (gtceu:hydrogen_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><span class="gt-note">Hydrogen (surplus)</span><b class="gt-q">3 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LV Macerator](#m-ma) → [LV Chemical Reactor · circuit 1](#m-cr)

## How to build

1. LV Macerator on a drawer of iron ingots: 1 ingot → 1 iron dust (GregTech macerator recycling, yield 1.0 in gtceu.yaml; you need 1 dust per 10 boards, so very little). — `gtceu:lv_macerator`, `gtceu:iron_dust`
2. LV Chemical Reactor with ghost circuit 1: 1 iron dust + 3000 mB hydrochloric acid → 1000 mB iron III chloride + 3000 mB hydrogen in 20 s (30 EU/t). Acid comes by Pipez fluid pipe from the acid drum; the etchant goes into its own drum. — `gtceu:lv_chemical_reactor`, `gtceu:iron_iii_chloride_bucket`
3. Hydrogen output: Fluid Voiding Cover on the pipe (or a steel drum). 300 mB of hydrogen per board you etch. — `gtceu:fluid_voiding_cover`, `gtceu:hydrogen_bucket`

## Tips

- One reaction (1 iron dust + 3 B acid) makes 1 B of etchant = 10 boards at 100 mB each.
- The reaction gives 3 B of hydrogen back. The electrolyzer already makes exactly the hydrogen the acid reactor needs, so this hydrogen is surplus: put a Fluid Voiding Cover (switch it on with a soft mallet) or a drum on that output, or the reactor stops when its tank is full.
- Sodium persulfate etches too (200 mB per board) but needs sulfuric acid and sodium bisulfate first. The pack’s cupric chloride etch (50 mB per board) needs an HV reactor (240 EU/t) and an EV mixer: not yet.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_macerator` | 1 |
| `gtceu:lv_chemical_reactor` | 1 |
| `gtceu:steel_drum` | 2 |
| `gtceu:fluid_voiding_cover` | 1 |
| `pipez:fluid_pipe` | 8 |
| `functionalstorage:oak_1` | 2 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md)
- **Main source for:** `gtceu:iron_iii_chloride_bucket`
