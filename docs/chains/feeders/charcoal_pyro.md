---
kind: chain
id: charcoal_pyro
order: 610
data:
  t: "Charcoal: Pyrolyse Oven"
  inf: true
  "n":
    - [lg, "16 Logs", s, "minecraft:oak_log"]
    - [n2, "Nitrogen 1 B (circ 2)", i, "gtceu:nitrogen_bucket"]
    - [po, Pyrolyse Oven, m, "gtceu:pyrolyse_oven"]
    - [ch, "20 Charcoal", o, "minecraft:charcoal"]
    - [cr, "4 B Creosote", o, "gtceu:creosote_bucket"]
  e: [[lg, po], [n2, po, optional], [po, ch, "32 s · 16 s"], [po, cr]]
  tips:
    - |-
      Circuit 1: 32 s at 64 EU/t. Circuit 2 + 1 B nitrogen: 16 s at 96 EU/t.
    - |-
      1.25 charcoal per log + creosote: the best yield in the pack.
  b: [["gtceu:pyrolyse_oven", 1]]
  how:
    - i: ["gtceu:pyrolyse_oven", "gtceu:cupronickel_coil_block"]
      t: |-
        Pyrolyse Oven: 16 cupronickel coils, ULV casings and an MV energy hatch. Better coils run faster.
    - i: ["gtceu:lv_input_bus", "minecraft:oak_log"]
      t: Logs from the greenhouse go into the input bus. Ghost circuit 1.
    - i: ["minecraft:charcoal", "gtceu:creosote_bucket"]
      t: |-
        16 logs → 20 charcoal + 4 B creosote every 32 s at 64 EU/t: 37.5 charcoal and 7.5 B creosote per minute.
    - i: ["gtceu:nitrogen_bucket"]
      t: Circuit 2 + 1 B nitrogen per craft halves the time to 16 s (96 EU/t).
---
# Charcoal: Pyrolyse Oven

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `charcoal_pyro` · **Tags:** Infinite source

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-po">
<div class="gt-head"><span class="gt-mname">Pyrolyse Oven</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="16 Logs (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">16 Logs</span><span class="gt-tag">infinite</span></span><span class="gt-slot" title="Nitrogen 1 B (circ 2) (gtceu:nitrogen_bucket) - optional"><img class="gt-ico" src="../../assets/icons/gtceu__nitrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrogen Bucket</span><span class="gt-note">Nitrogen 1 B (circ 2)</span><b class="gt-q">optional</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__pyrolyse_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">16 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="20 Charcoal (minecraft:charcoal) - 32 s · 16 s"><img class="gt-ico" src="../../assets/icons/minecraft__charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Charcoal</span><span class="gt-note">20 Charcoal</span><b class="gt-q">32 s</b></span><span class="gt-slot gt-outp" title="4 B Creosote (gtceu:creosote_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__creosote_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Creosote Bucket</span><span class="gt-note">4 B Creosote</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:pyrolyse_oven</code></div>
</div>
</div>

## Flow

- [Pyrolyse Oven](#m-po)

## How to build

1. Pyrolyse Oven: 16 cupronickel coils, ULV casings and an MV energy hatch. Better coils run faster. — `gtceu:pyrolyse_oven`, `gtceu:cupronickel_coil_block`
2. Logs from the greenhouse go into the input bus. Ghost circuit 1. — `gtceu:lv_input_bus`, `minecraft:oak_log`
3. 16 logs → 20 charcoal + 4 B creosote every 32 s at 64 EU/t: 37.5 charcoal and 7.5 B creosote per minute. — `minecraft:charcoal`, `gtceu:creosote_bucket`
4. Circuit 2 + 1 B nitrogen per craft halves the time to 16 s (96 EU/t). — `gtceu:nitrogen_bucket`

## Tips

- Circuit 1: 32 s at 64 EU/t. Circuit 2 + 1 B nitrogen: 16 s at 96 EU/t.
- 1.25 charcoal per log + creosote: the best yield in the pack.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:pyrolyse_oven` | 1 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](../steam/tree_farm.md), [Oxygen &amp; nitrogen from air (Gas Collector + Centrifuge)](../hv/oxygen.md)
