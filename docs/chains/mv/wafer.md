---
kind: chain
id: wafer
order: 190
data:
  t: Silicon wafers & chips
  "n":
    - [si, "32 Silicon dust", i, "gtceu:silicon_dust"]
    - [ga, Gallium Arsenide, i, "gtceu:gallium_arsenide_dust"]
    - [ebf, EBF, m, "gtceu:electric_blast_furnace"]
    - [bo, Silicon Boule, x, "gtceu:silicon_boule"]
    - [ct, "Cutter + lubricant", m, "gtceu:mv_cutter"]
    - [wf, "16 Wafers", x, "gtceu:silicon_wafer"]
    - [le, Laser Engraver, m, "gtceu:mv_laser_engraver"]
    - [c1, "ILC · red", o, "gtceu:ilc_chip"]
    - [c2, "RAM · green", o, "gtceu:ram_chip"]
    - [c3, "ULPIC · blue", o, "gtceu:ulpic_chip"]
    - [c4, "CPU · white", o, "gtceu:cpu_chip"]
  e: [[si, ebf], [ga, ebf], [ebf, bo], [bo, ct], [ct, wf], [wf, le], [le, c1], [le, c2], [le, c3], [le, c4]]
  tips: ["Engraved wafer → cutter → chips.", One engraver per lens avoids swapping.]
  b:
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:mv_cutter", 1]
    - ["gtceu:mv_laser_engraver", 4]
    - ["gtceu:red_glass_lens", 1]
    - ["gtceu:green_glass_lens", 1]
    - ["gtceu:blue_glass_lens", 1]
    - ["gtceu:glass_lens", 1]
---
# Silicon wafers &amp; chips

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `wafer`

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Silicon wafers and chips](../../plan/p6.md#wafer)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-ebf">
<div class="gt-head"><span class="gt-mname">EBF</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="32 Silicon dust (gtceu:silicon_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Dust</span><span class="gt-note">32 Silicon dust</span></span><span class="gt-slot" title="Gallium Arsenide (gtceu:gallium_arsenide_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_arsenide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Arsenide Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Silicon Boule (gtceu:silicon_boule)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_boule.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Boule</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-mv" id="m-ct">
<div class="gt-head"><span class="gt-mname">Cutter + lubricant</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Silicon Boule (gtceu:silicon_boule)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_boule.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Boule</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="16 Wafers (gtceu:silicon_wafer)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Wafer</span><span class="gt-note">16 Wafers</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_cutter</code></div>
</div>
<div class="gt-panel t-mv" id="m-le">
<div class="gt-head"><span class="gt-mname">Laser Engraver</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="16 Wafers (gtceu:silicon_wafer)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Wafer</span><span class="gt-note">16 Wafers</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ILC · red (gtceu:ilc_chip)"><img class="gt-ico" src="../../assets/icons/gtceu__ilc_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ilc Chip</span><span class="gt-note">ILC · red</span></span><span class="gt-slot gt-outp" title="RAM · green (gtceu:ram_chip)"><img class="gt-ico" src="../../assets/icons/gtceu__ram_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">RAM Chip</span><span class="gt-note">RAM · green</span></span><span class="gt-slot gt-outp" title="ULPIC · blue (gtceu:ulpic_chip)"><img class="gt-ico" src="../../assets/icons/gtceu__ulpic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ULPIC Chip</span><span class="gt-note">ULPIC · blue</span></span><span class="gt-slot gt-outp" title="CPU · white (gtceu:cpu_chip)"><img class="gt-ico" src="../../assets/icons/gtceu__cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">CPU Chip</span><span class="gt-note">CPU · white</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_laser_engraver</code></div>
</div>
</div>

## Flow

- [EBF](#m-ebf) → [Cutter + lubricant](#m-ct) → [Laser Engraver](#m-le)

## Tips

- Engraved wafer → cutter → chips.
- One engraver per lens avoids swapping.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:mv_cutter` | 1 |
| `gtceu:mv_laser_engraver` | 4 |
| `gtceu:red_glass_lens` | 1 |
| `gtceu:green_glass_lens` | 1 |
| `gtceu:blue_glass_lens` | 1 |
| `gtceu:glass_lens` | 1 |

## Needs / Feeds

- **Needs:** [Infinite aluminium (clay)](aluminium.md), [Gallium arsenide (sphalerite + realgar)](mv_gaas.md)
- **Feeds:** [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../iv/iv_circuits.md)
- **Main source for:** `gtceu:cpu_chip`
