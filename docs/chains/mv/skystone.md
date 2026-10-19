---
kind: chain
id: skystone
order: 250
data:
  t: Infinite sky stone (AE2)
  inf: true
  "n":
    - [mx, "Mixer (one seed)", m, "gtceu:mv_mixer"]
    - [sd, Sky Dust, x, "ae2:sky_dust"]
    - [lv, Lava, f, "minecraft:lava_bucket"]
    - [en, Resonant Ender, f, "thermal:ender_bucket"]
    - [rb, Rock Breaker, m, "gtceu:mv_rock_crusher"]
    - [ss, Sky Stone, x, "ae2:sky_stone_block"]
    - [mc, Macerator, m, "gtceu:mv_macerator"]
    - [out, Sky Dust, o, "ae2:sky_dust"]
  e: [[mx, sd, seed], [sd, rb, not used], [lv, rb, adjacent], [en, rb, adjacent], [rb, ss], [ss, mc], [mc, out]]
  tips:
    - |-
      Seed: 6 stone dust + 4 ender pearl dust + redstone + glowstone (MV mixer, circuit 4, 112 EU/t). Ender pearl dust comes from pearls; the GT beryllium/potassium mix is HV.
  b: [["gtceu:mv_mixer", 1], ["gtceu:mv_rock_crusher", 1], ["gtceu:mv_macerator", 1], ["gtceu:lv_extractor", 1]]
  how:
    - i: ["gtceu:mv_mixer", "ae2:sky_dust"]
      t: |-
        One-time seed: MV Mixer, 6 stone dust + 4 ender pearl dust + redstone + glowstone (circuit 4) → 1 sky dust.
    - i: ["gtceu:mv_rock_crusher", "minecraft:lava_bucket", "thermal:ender_bucket"]
      t: MV Rock Breaker with the sky dust inside (kept), lava on one side and resonant ender on the other → sky stone blocks.
    - i: ["gtceu:mv_macerator"]
      t: Macerate a share of the sky stone back into sky dust; the rest feeds skystone alloys.
---
# Infinite sky stone (AE2)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `skystone` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer (one seed)</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Sky Dust (ae2:sky_dust) - seed"><img class="gt-ico" src="../../assets/icons/ae2__sky_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sky Dust</span><b class="gt-q">seed</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_mixer</code></div>
</div>
<div class="gt-panel t-mv" id="m-rb">
<div class="gt-head"><span class="gt-mname">Rock Breaker</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sky Dust (ae2:sky_dust) - not used"><img class="gt-ico" src="../../assets/icons/ae2__sky_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sky Dust</span><b class="gt-q">not used</b></span><span class="gt-slot gt-fluid" title="Lava (minecraft:lava_bucket) - adjacent"><img class="gt-ico" src="../../assets/icons/minecraft__lava_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lava</span><b class="gt-q">adjacent</b></span><span class="gt-slot gt-fluid" title="Resonant Ender (thermal:ender_bucket) - adjacent"><img class="gt-ico" src="../../assets/icons/thermal__ender_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender</span><span class="gt-note">Resonant Ender</span><b class="gt-q">adjacent</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_rock_crusher.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Sky Stone (ae2:sky_stone_block)"><img class="gt-ico" src="../../assets/icons/ae2__sky_stone_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sky Stone Block</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_rock_crusher</code></div>
</div>
<div class="gt-panel t-mv" id="m-mc">
<div class="gt-head"><span class="gt-mname">Macerator</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sky Stone (ae2:sky_stone_block)"><img class="gt-ico" src="../../assets/icons/ae2__sky_stone_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sky Stone Block</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Sky Dust (ae2:sky_dust)"><img class="gt-ico" src="../../assets/icons/ae2__sky_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sky Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_macerator</code></div>
</div>
</div>

## Flow

- [Mixer (one seed)](#m-mx) → [Rock Breaker](#m-rb) → [Macerator](#m-mc)

## How to build

1. One-time seed: MV Mixer, 6 stone dust + 4 ender pearl dust + redstone + glowstone (circuit 4) → 1 sky dust. — `gtceu:mv_mixer`, `ae2:sky_dust`
2. MV Rock Breaker with the sky dust inside (kept), lava on one side and resonant ender on the other → sky stone blocks. — `gtceu:mv_rock_crusher`, `minecraft:lava_bucket`, `thermal:ender_bucket`
3. Macerate a share of the sky stone back into sky dust; the rest feeds skystone alloys. — `gtceu:mv_macerator`

## Tips

- Seed: 6 stone dust + 4 ender pearl dust + redstone + glowstone (MV mixer, circuit 4, 112 EU/t). Ender pearl dust comes from pearls; the GT beryllium/potassium mix is HV.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_mixer` | 1 |
| `gtceu:mv_rock_crusher` | 1 |
| `gtceu:mv_macerator` | 1 |
| `gtceu:lv_extractor` | 1 |
