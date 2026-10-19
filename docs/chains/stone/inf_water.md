---
kind: chain
id: inf_water
order: 10
data:
  t: Infinite water
  inf: true
  "n":
    - [src, "2 water sources", s, "minecraft:water_bucket"]
    - [acc, Aqueous Accumulator, m, "thermal:device_water_gen"]
    - [w, Water, f, "minecraft:water_bucket"]
    - [use, "Barrels / machines", o, "gtceu:stone_barrel"]
  e: [[src, acc, adjacent], [acc, w, "∞"], [w, use, pipe]]
  tips: ["Needs a lead ingot (galena from blackstone).", Upgrade kits multiply its output.]
  b: [["thermal:device_water_gen", 1]]
  how:
    - i: ["thermal:device_water_gen"]
      t: |-
        Aqueous Accumulator (in this pack: lead + copper + glass + bucket + redstone servo).
    - i: ["minecraft:water_bucket"]
      t: Place it touching at least two water source blocks.
    - i: ["pipez:fluid_pipe"]
      t: Turn on auto-output in its side config, or pull with a Pipez fluid pipe. An upgrade kit multiplies the rate.
---
# Infinite water

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `inf_water` · **Tags:** Infinite source

**Era setup:** [Stone Age](../../eras/stone.md)

**Plan modules:** [Infinite water](../../plan/p2.md#water)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-acc">
<div class="gt-head"><span class="gt-mname">Aqueous Accumulator</span><span class="gt-badge t-mod">Thermal</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="2 water sources (minecraft:water_bucket) - adjacent"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span><span class="gt-note">2 water sources</span><span class="gt-tag">infinite</span><b class="gt-q">adjacent</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/thermal__device_water_gen.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Water (minecraft:water_bucket) - ∞"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water</span><b class="gt-q">∞</b></span></div>
</div>
<div class="gt-foot"><code>thermal:device_water_gen</code></div>
</div>
</div>

## Flow

- [Aqueous Accumulator](#m-acc)

### Direct steps

- Water → Barrels / machines (pipe)

## How to build

1. Aqueous Accumulator (in this pack: lead + copper + glass + bucket + redstone servo). — `thermal:device_water_gen`
2. Place it touching at least two water source blocks. — `minecraft:water_bucket`
3. Turn on auto-output in its side config, or pull with a Pipez fluid pipe. An upgrade kit multiplies the rate. — `pipez:fluid_pipe`

## Tips

- Needs a lead ingot (galena from blackstone).
- Upgrade kits multiply its output.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `thermal:device_water_gen` | 1 |

## Needs / Feeds

- **Feeds:** [Distilled water](../lv/distilled.md), [Salt water](../mv/sea_water.md), [Logs: Greenhouse](../feeders/greenhouse_logs.md), [Cobble: Rock Breaker (LV)](../feeders/cobble_rb.md), [Cobble: Create drill generator](../feeders/cobble_drill.md), [LV power: boilers + steam turbines](../power/power_steam.md)
- **Main source for:** `minecraft:water_bucket`
