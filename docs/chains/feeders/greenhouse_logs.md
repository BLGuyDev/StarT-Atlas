---
kind: chain
id: greenhouse_logs
order: 630
data:
  t: "Logs: Greenhouse"
  inf: true
  "n":
    - [sp, "Sapling (kept)", i, "minecraft:oak_sapling"]
    - [w, "100 mB Water", i, "minecraft:water_bucket"]
    - [co2, "CO₂ 500 mB (circ 1)", i, "gtceu:carbon_dioxide_bucket"]
    - [gh, Greenhouse, m, "gtceu:greenhouse"]
    - [lg, "16 / 64 / 128 Logs", o, "minecraft:oak_log"]
    - [ox, "Oxygen (circ 1-2)", o, "gtceu:oxygen_bucket"]
  e: [[sp, gh], [w, gh], [co2, gh, optional], [gh, lg, "30 s"], [gh, ox]]
  tips:
    - |-
      Circuit 0: 16 logs / 30 s · circuit 1 + 500 mB CO₂: 64 logs + 1 B O₂ · circuit 2 + 1 B CO₂ + 150 mB NPK: 128 logs + 2.5 B O₂. All 30 EU/t.
    - Any sapling works, jungle included (logs for the rubber extractor).
    - |-
      CO₂ comes from wood gas (pyrolyse oven circuit 5: 16 logs → 1.5 B) in an MV Distillery on circuit 1 (64 EU/t): ≈ 735 mB CO₂, more than one CO₂ run needs.
    - "IV: Tree Synthesizer, the parallel version."
  b: [["gtceu:greenhouse", 1], ["minecraft:oak_sapling", 1]]
  how:
    - i: ["gtceu:greenhouse"]
      t: Greenhouse multiblock (see its render and materials). It needs grass, dirt, leaves and logs inside the structure.
    - i: ["minecraft:oak_sapling", "gtceu:lv_input_bus"]
      t: One sapling in the input bus (never consumed) and 100 mB water per craft via an input hatch.
    - i: ["minecraft:oak_log"]
      t: "Circuit 0: 16 logs every 30 s at 30 EU/t, i.e. 32 logs/min."
    - i: ["gtceu:carbon_dioxide_bucket", "gtceu:oxygen_bucket"]
      t: |-
        Circuit 1 + 500 mB CO₂: 64 logs + 1 B oxygen per 30 s. Circuit 2 + 1 B CO₂ + 150 mB NPK: 128 logs + 2.5 B oxygen.
    - i: ["gtceu:mv_energy_input_hatch"]
      t: |-
        Overclock: with an MV energy hatch every mode runs twice as fast (circuit 0: 64 logs per minute for 120 EU/t).
    - i: ["gtceu:pyrolyse_oven", "gtceu:carbon_dioxide_bucket"]
      t: |-
        MV loop: a quarter of the logs go to a Pyrolyse Oven on circuit 5 (wood gas + charcoal); distilled wood gas gives the CO₂ for circuit 1, which quadruples the logs and also returns oxygen for steel and chemistry.
---
# Logs: Greenhouse

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `greenhouse_logs` · **Tags:** Infinite source

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-gh">
<div class="gt-head"><span class="gt-mname">Greenhouse</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Sapling (kept) (minecraft:oak_sapling)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_sapling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Sapling</span><span class="gt-note">Sapling (kept)</span></span><span class="gt-slot" title="100 mB Water (minecraft:water_bucket)"><img class="gt-ico" src="../../assets/icons/minecraft__water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Water Bucket</span><span class="gt-note">100 mB Water</span></span><span class="gt-slot" title="CO₂ 500 mB (circ 1) (gtceu:carbon_dioxide_bucket) - optional"><img class="gt-ico" src="../../assets/icons/gtceu__carbon_dioxide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Carbon Dioxide Bucket</span><span class="gt-note">CO₂ 500 mB (circ 1)</span><b class="gt-q">optional</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__greenhouse.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="16 / 64 / 128 Logs (minecraft:oak_log) - 30 s"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">16 / 64 / 128 Logs</span></span><span class="gt-slot gt-outp" title="Oxygen (circ 1-2) (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen Bucket</span><span class="gt-note">Oxygen (circ 1-2)</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:greenhouse</code></div>
</div>
</div>

## Flow

- [Greenhouse](#m-gh)

## How to build

1. Greenhouse multiblock (see its render and materials). It needs grass, dirt, leaves and logs inside the structure. — `gtceu:greenhouse`
2. One sapling in the input bus (never consumed) and 100 mB water per craft via an input hatch. — `minecraft:oak_sapling`, `gtceu:lv_input_bus`
3. Circuit 0: 16 logs every 30 s at 30 EU/t, i.e. 32 logs/min. — `minecraft:oak_log`
4. Circuit 1 + 500 mB CO₂: 64 logs + 1 B oxygen per 30 s. Circuit 2 + 1 B CO₂ + 150 mB NPK: 128 logs + 2.5 B oxygen. — `gtceu:carbon_dioxide_bucket`, `gtceu:oxygen_bucket`
5. Overclock: with an MV energy hatch every mode runs twice as fast (circuit 0: 64 logs per minute for 120 EU/t). — `gtceu:mv_energy_input_hatch`
6. MV loop: a quarter of the logs go to a Pyrolyse Oven on circuit 5 (wood gas + charcoal); distilled wood gas gives the CO₂ for circuit 1, which quadruples the logs and also returns oxygen for steel and chemistry. — `gtceu:pyrolyse_oven`, `gtceu:carbon_dioxide_bucket`

## Tips

- Circuit 0: 16 logs / 30 s · circuit 1 + 500 mB CO₂: 64 logs + 1 B O₂ · circuit 2 + 1 B CO₂ + 150 mB NPK: 128 logs + 2.5 B O₂. All 30 EU/t.
- Any sapling works, jungle included (logs for the rubber extractor).
- CO₂ comes from wood gas (pyrolyse oven circuit 5: 16 logs → 1.5 B) in an MV Distillery on circuit 1 (64 EU/t): ≈ 735 mB CO₂, more than one CO₂ run needs.
- IV: Tree Synthesizer, the parallel version.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:greenhouse` | 1 |
| `minecraft:oak_sapling` | 1 |

## Needs / Feeds

- **Needs:** [Infinite water](../stone/inf_water.md)
