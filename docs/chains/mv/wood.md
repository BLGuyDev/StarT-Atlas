---
kind: chain
id: wood
order: 240
data:
  t: Infinite wood & charcoal
  inf: true
  "n":
    - [gh, "Greenhouse / tree farm", s, "gtceu:greenhouse"]
    - [lg, Logs, x, "minecraft:oak_log"]
    - [po, Pyrolyse Oven, m, "gtceu:pyrolyse_oven"]
    - [ch, Charcoal, o, "minecraft:charcoal"]
    - [cr, "Creosote / wood tar", f, "gtceu:creosote_bucket"]
    - [oil, "Heavy oil (circ 3)", o, "gtceu:oil_heavy_bucket"]
  e: [[gh, lg], [lg, po], [po, ch], [po, cr], [po, oil, "32 logs → 16 B"]]
  tips: ["Sapling + water + bonemeal in the greenhouse."]
  b: [["gtceu:greenhouse", 1], ["gtceu:pyrolyse_oven", 1]]
  how:
    - i: ["gtceu:greenhouse"]
      t: Greenhouse logs (32–128 per minute) go straight into the Pyrolyse Oven’s input bus.
    - i: ["gtceu:pyrolyse_oven"]
      t: |-
        Circuit 1: charcoal + creosote · circuit 3: heavy oil (HV power) · other circuits: wood gas, tar, vinegar.
---
# Infinite wood &amp; charcoal

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `wood` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Wood farm](../../plan/p1.md#wood)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-po">
<div class="gt-head"><span class="gt-mname">Pyrolyse Oven</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Logs (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__pyrolyse_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Charcoal (minecraft:charcoal)"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span></span><span class="gt-slot gt-fluid" title="Creosote / wood tar (gtceu:creosote_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__creosote_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Creosote</span><span class="gt-note">Creosote / wood tar</span></span><span class="gt-slot gt-outp" title="Heavy oil (circ 3) (gtceu:oil_heavy_bucket) - 32 logs → 16 B"><img class="gt-ico" src="../../assets/icons/gtceu__oil_heavy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Heavy Bucket</span><span class="gt-note">Heavy oil (circ 3)</span><b class="gt-q">32 logs → 16 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:pyrolyse_oven</code></div>
</div>
</div>

## Flow

- [Pyrolyse Oven](#m-po)

### Direct steps

- Greenhouse / tree farm → Logs

## How to build

1. Greenhouse logs (32–128 per minute) go straight into the Pyrolyse Oven’s input bus. — `gtceu:greenhouse`
2. Circuit 1: charcoal + creosote · circuit 3: heavy oil (HV power) · other circuits: wood gas, tar, vinegar. — `gtceu:pyrolyse_oven`

## Tips

- Sapling + water + bonemeal in the greenhouse.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:greenhouse` | 1 |
| `gtceu:pyrolyse_oven` | 1 |
