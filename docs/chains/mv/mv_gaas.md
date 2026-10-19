---
kind: chain
id: mv_gaas
order: 980
data:
  t: Gallium arsenide (sphalerite + realgar)
  inf: true
  "n":
    - [sp, "Crushed sphalerite (sieve)", i, "gtceu:crushed_sphalerite_ore"]
    - [eof, Electric Ore Factory, m, "gtceu:electric_ore_factory"]
    - [ga, "Gallium dust (45 %)", x, "gtceu:gallium_dust"]
    - [ve, Void Extractor, s, "gtceu:void_extractor"]
    - [rr, "Raw realgar (60 %)", i, "gtceu:raw_realgar"]
    - [pu, LV Pulverizer, m, "gtceu:lv_pulverizer"]
    - [cr, "2 Crushed realgar ore", i, "gtceu:crushed_realgar_ore"]
    - [ma, LV Macerator, m, "gtceu:lv_macerator"]
    - [id, Impure realgar dust, x, "gtceu:impure_realgar_dust"]
    - [ow, "LV Ore Washer · 100 mB water", m, "gtceu:lv_ore_washer"]
    - [rd, Realgar dust, x, "gtceu:realgar_dust"]
    - [ce, LV Centrifuge, m, "gtceu:lv_centrifuge"]
    - [as, "1 Arsenic dust", x, "gtceu:arsenic_dust"]
    - [mx, "LV Mixer · circuit 1", m, "gtceu:lv_mixer"]
    - [gs, "2 Gallium arsenide dust", o, "gtceu:gallium_arsenide_dust"]
  e:
    - [sp, eof, "1 + 100 mB water"]
    - [eof, ga, "45 %"]
    - [ve, rr, "60 % / 32 s"]
    - [rr, pu, "1"]
    - [pu, cr, "1 → 2 / 15 s"]
    - [cr, ma, "2"]
    - [ma, id, "1 each"]
    - [id, ow, "2"]
    - [ow, rd, "2"]
    - [rd, ce, "2"]
    - [ce, as, "1 / ~64 s"]
    - [ga, mx, "1"]
    - [as, mx, "1"]
    - [mx, gs, "10 s"]
  tips:
    - |-
      1 gallium + 1 arsenic = 2 gallium arsenide dust = 8 small dust = 8 diodes = 4 MV circuits. Gallium and arsenic are always used in equal numbers.
    - Plain electrolysis of sphalerite dust also gives gallium but only 5 % per craft; the Electric Ore Factory gives 0.45 per crushed sphalerite.
    - |-
      Arsenic is the slow part: the only source in reach is realgar, and only the Void Extractor makes it (no sieve in this pack gives it). Count: 1 raw realgar → 2 crushed → 2 impure dust → 2 realgar dust → 1 arsenic dust (+1 sulfur dust).
  b:
    - ["gtceu:electric_ore_factory", 1]
    - ["gtceu:void_extractor", 1]
    - ["gtceu:lv_pulverizer", 1]
    - ["gtceu:lv_macerator", 1]
    - ["gtceu:lv_ore_washer", 1]
    - ["gtceu:lv_centrifuge", 1]
    - ["gtceu:lv_mixer", 1]
    - ["gtceu:lv_robot_arm", 5]
    - ["gtceu:item_filter", 5]
    - ["functionalstorage:oak_1", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
  how:
    - i: ["gtceu:electric_ore_factory", "gtceu:crushed_sphalerite_ore", "gtceu:gallium_dust"]
      t: |-
        Same Electric Ore Factory as the silver line (30 EU/t, 8 s): 1 crushed sphalerite + 100 mB water → 1 sphalerite dust, +1 (75 %), 1 gallium dust (45 %), 1 sulfur dust (32.5 %). Sphalerite comes from the gravel sieve (16 per batch). Give it its own input bus drawer so galena and sphalerite never mix.
    - i: ["gtceu:void_extractor", "gtceu:raw_realgar", "gtceu:drilling_fluid_bucket"]
      t: |-
        Void Extractor: 5 B drilling fluid per 32 s (30 EU/t) gives raw realgar at 60 % (+12 % per tier over LV) with the other ores. Filter only raw realgar and raw silver into drawers.
    - i: ["gtceu:lv_pulverizer", "gtceu:crushed_realgar_ore"]
      t: |-
        LV Pulverizer (pack machine): 1 raw realgar → 2 crushed realgar ore, 30 EU/t, 15 s (it copies the macerator’s crushed-ore count). The Pulverizer only does raw ore → crushed ore (and heated smelting variants); it has no crushed → dust recipe.
    - i: ["gtceu:lv_macerator", "gtceu:impure_realgar_dust"]
      t: |-
        LV Macerator: crushed realgar ore → 1 impure realgar dust (recipe 2 EU/t, 20 s base, so about 10 s at LV) plus a small chance of a bonus dust.
    - i: ["gtceu:lv_ore_washer", "gtceu:realgar_dust"]
      t: |-
        LV Ore Washer, ghost circuit 2: 1 impure realgar dust + 100 mB water → 1 realgar dust in 0.4 s (4 EU/t). A Centrifuge also cleans impure dust but is far slower.
    - i: ["gtceu:lv_centrifuge", "gtceu:arsenic_dust"]
      t: |-
        LV Centrifuge on the realgar dust drawer: realgar is 4 arsenic + 4 sulfur, which GregTech reduces to 2 realgar dust → 1 arsenic dust + 1 sulfur dust, 30 EU/t, about 64 s. Counts come from the standard decomposition code, not from a local dump: confirm in EMI. Keep only the arsenic.
    - i: ["gtceu:lv_mixer", "gtceu:gallium_arsenide_dust"]
      t: |-
        LV Mixer with ghost circuit 1: 1 gallium dust + 1 arsenic dust → 2 gallium arsenide dust in 10 s (7 EU/t). Output drawer capped by a Robot Arm cover on Keep Exact 16: that is already 64 MV circuits.
---
# Gallium arsenide (sphalerite + realgar)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_gaas` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Gallium arsenide](../../plan/p6.md#gaas)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-eof">
<div class="gt-head"><span class="gt-mname">Electric Ore Factory</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Crushed sphalerite (sieve) (gtceu:crushed_sphalerite_ore) - 1 + 100 mB water"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_sphalerite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Sphalerite Ore</span><span class="gt-note">Crushed sphalerite (sieve)</span><b class="gt-q">1 + 100 mB water</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_ore_factory.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Gallium dust (45 %) (gtceu:gallium_dust) - 45 %"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Dust</span><span class="gt-note">Gallium dust (45 %)</span><b class="gt-q">45 %</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_ore_factory</code></div>
</div>
<div class="gt-panel t-lv" id="m-pu">
<div class="gt-head"><span class="gt-mname">LV Pulverizer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Raw realgar (60 %) (gtceu:raw_realgar) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_realgar.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Realgar</span><span class="gt-note">Raw realgar (60 %)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_pulverizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Crushed realgar ore (gtceu:crushed_realgar_ore) - 1 → 2 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_realgar_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Realgar Ore</span><span class="gt-note">2 Crushed realgar ore</span><b class="gt-q">1 → 2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_pulverizer</code></div>
</div>
<div class="gt-panel t-lv" id="m-ma">
<div class="gt-head"><span class="gt-mname">LV Macerator</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Crushed realgar ore (gtceu:crushed_realgar_ore) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_realgar_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Realgar Ore</span><span class="gt-note">2 Crushed realgar ore</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Impure realgar dust (gtceu:impure_realgar_dust) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__impure_realgar_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Impure Realgar Dust</span><b class="gt-q">1 each</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_macerator</code></div>
</div>
<div class="gt-panel t-lv" id="m-ow">
<div class="gt-head"><span class="gt-mname">LV Ore Washer · 100 mB water</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Impure realgar dust (gtceu:impure_realgar_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__impure_realgar_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Impure Realgar Dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_ore_washer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Realgar dust (gtceu:realgar_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__realgar_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Realgar Dust</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_ore_washer</code></div>
</div>
<div class="gt-panel t-lv" id="m-ce">
<div class="gt-head"><span class="gt-mname">LV Centrifuge</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Realgar dust (gtceu:realgar_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__realgar_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Realgar Dust</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">~64 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="1 Arsenic dust (gtceu:arsenic_dust) - 1 / ~64 s"><img class="gt-ico" src="../../assets/icons/gtceu__arsenic_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Arsenic Dust</span><span class="gt-note">1 Arsenic dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_centrifuge</code></div>
</div>
<div class="gt-panel t-lv" id="m-mx">
<div class="gt-head"><span class="gt-mname">LV Mixer · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gallium dust (45 %) (gtceu:gallium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Dust</span><span class="gt-note">Gallium dust (45 %)</span><b class="gt-q">1</b></span><span class="gt-slot" title="1 Arsenic dust (gtceu:arsenic_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__arsenic_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Arsenic Dust</span><span class="gt-note">1 Arsenic dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 Gallium arsenide dust (gtceu:gallium_arsenide_dust) - 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_arsenide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Arsenide Dust</span><span class="gt-note">2 Gallium arsenide dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_mixer</code></div>
</div>
</div>

## Flow

- [Electric Ore Factory](#m-eof) → [LV Mixer · circuit 1](#m-mx)
- [LV Pulverizer](#m-pu) → [LV Macerator](#m-ma) → [LV Ore Washer · 100 mB water](#m-ow) → [LV Centrifuge](#m-ce) → [LV Mixer · circuit 1](#m-mx)

### Direct steps

- Void Extractor → Raw realgar (60 %) (60 % / 32 s)

## How to build

1. Same Electric Ore Factory as the silver line (30 EU/t, 8 s): 1 crushed sphalerite + 100 mB water → 1 sphalerite dust, +1 (75 %), 1 gallium dust (45 %), 1 sulfur dust (32.5 %). Sphalerite comes from the gravel sieve (16 per batch). Give it its own input bus drawer so galena and sphalerite never mix. — `gtceu:electric_ore_factory`, `gtceu:crushed_sphalerite_ore`, `gtceu:gallium_dust`
2. Void Extractor: 5 B drilling fluid per 32 s (30 EU/t) gives raw realgar at 60 % (+12 % per tier over LV) with the other ores. Filter only raw realgar and raw silver into drawers. — `gtceu:void_extractor`, `gtceu:raw_realgar`, `gtceu:drilling_fluid_bucket`
3. LV Pulverizer (pack machine): 1 raw realgar → 2 crushed realgar ore, 30 EU/t, 15 s (it copies the macerator’s crushed-ore count). The Pulverizer only does raw ore → crushed ore (and heated smelting variants); it has no crushed → dust recipe. — `gtceu:lv_pulverizer`, `gtceu:crushed_realgar_ore`
4. LV Macerator: crushed realgar ore → 1 impure realgar dust (recipe 2 EU/t, 20 s base, so about 10 s at LV) plus a small chance of a bonus dust. — `gtceu:lv_macerator`, `gtceu:impure_realgar_dust`
5. LV Ore Washer, ghost circuit 2: 1 impure realgar dust + 100 mB water → 1 realgar dust in 0.4 s (4 EU/t). A Centrifuge also cleans impure dust but is far slower. — `gtceu:lv_ore_washer`, `gtceu:realgar_dust`
6. LV Centrifuge on the realgar dust drawer: realgar is 4 arsenic + 4 sulfur, which GregTech reduces to 2 realgar dust → 1 arsenic dust + 1 sulfur dust, 30 EU/t, about 64 s. Counts come from the standard decomposition code, not from a local dump: confirm in EMI. Keep only the arsenic. — `gtceu:lv_centrifuge`, `gtceu:arsenic_dust`
7. LV Mixer with ghost circuit 1: 1 gallium dust + 1 arsenic dust → 2 gallium arsenide dust in 10 s (7 EU/t). Output drawer capped by a Robot Arm cover on Keep Exact 16: that is already 64 MV circuits. — `gtceu:lv_mixer`, `gtceu:gallium_arsenide_dust`

## Tips

- 1 gallium + 1 arsenic = 2 gallium arsenide dust = 8 small dust = 8 diodes = 4 MV circuits. Gallium and arsenic are always used in equal numbers.
- Plain electrolysis of sphalerite dust also gives gallium but only 5 % per craft; the Electric Ore Factory gives 0.45 per crushed sphalerite.
- Arsenic is the slow part: the only source in reach is realgar, and only the Void Extractor makes it (no sieve in this pack gives it). Count: 1 raw realgar → 2 crushed → 2 impure dust → 2 realgar dust → 1 arsenic dust (+1 sulfur dust).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_ore_factory` | 1 |
| `gtceu:void_extractor` | 1 |
| `gtceu:lv_pulverizer` | 1 |
| `gtceu:lv_macerator` | 1 |
| `gtceu:lv_ore_washer` | 1 |
| `gtceu:lv_centrifuge` | 1 |
| `gtceu:lv_mixer` | 1 |
| `gtceu:lv_robot_arm` | 5 |
| `gtceu:item_filter` | 5 |
| `functionalstorage:oak_1` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |

## Needs / Feeds

- **Feeds:** [Silicon wafers &amp; chips](wafer.md), [Diodes (gallium arsenide + glass + fine wire)](mv_diode.md)
- **Main source for:** `gtceu:gallium_arsenide_dust`, `gtceu:gallium_dust`, `gtceu:arsenic_dust`
