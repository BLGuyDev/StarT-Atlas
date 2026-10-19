---
kind: chain
id: uv_gravi
order: 1690
data:
  t: |-
    Gravi star: nether star → quantum star (radon bath) → gravi star (autoclave with 288 mB neutronium) - 1 per UV emitter, sensor and field generator
  inf: true
  "n":
    - [ns, "Nether star (nether_star chain)", i, "minecraft:nether_star"]
    - [g1, "1250 mB radon", g, "functionalstorage:oak_1", [[Radon, "gtceu:radon_bucket"]]]
    - [cb, "HV Chemical Bath · 96 s · 480 EU/t", m, "gtceu:hv_chemical_bath"]
    - [qs, Quantum star, x, "gtceu:quantum_star"]
    - [g2, "288 mB molten neutronium", g, "functionalstorage:oak_1", [[Neutronium, "gtceu:neutronium_bucket"]]]
    - [au, "IV Autoclave · 24 s · 7680 EU/t", m, "gtceu:iv_autoclave"]
    - [gs, Gravi star, o, "gtceu:gravi_star"]
  e:
    - [ns, cb, "1"]
    - [g1, cb, "1250 mB"]
    - [cb, qs, "1 / 96 s"]
    - [qs, au, "1"]
    - [g2, au, "288 mB"]
    - [au, gs, "1 / 24 s"]
  tips:
    - |-
      Source (gtsrc CircuitRecipes, not touched by the pack): chemical bath, 1 nether star + 1250 mB radon → 1 quantum star, 1920 ticks (96 s) at VA[HV] = 480 EU/t; autoclave, 1 quantum star + 288 mB (2 x 144) molten neutronium → 1 gravi star, 480 ticks (24 s) at VA[IV] = 7680 EU/t. Quantum stars are already used by the ZPM component line (2 per ZPM emitter / sensor, 6 per field generator) and the UV fusion reactor takes one; gravi stars are the UV catalyst (1 per UV emitter, sensor, field generator) and the UHV one is 2.
    - |-
      Neutronium comes from the UV fusion reactor (uv_fusion_mats, 144 mB per 72 s run), so every gravi star is two thirds of a neutronium run. Radon: tier-1 fusion (gold + mercury), 1 B per run, so a quantum star costs 1.25 runs of radon. Nether stars: the pack loop in the nether_star chain (shards from the Wither star, energized and infused with the four elemental shards; Unverified details), or the wither.
    - |-
      Sub-steps people skip: (1) the autoclave wants a fluid hatch for neutronium, not the item; (2) quantum stars sit in a drawer Keep Exact 4; (3) the bath uses the star item, not the nether star shard; (4) radon is also a gas for other chains: keep a 4 B reserve drum.
    - "Unverified: the nether star supply rate."
  b:
    - ["gtceu:hv_chemical_bath", 1]
    - ["gtceu:iv_autoclave", 1]
    - ["functionalstorage:oak_1", 4]
    - ["modularrouters:modular_router", 2]
    - ["gtceu:lv_robot_arm", 2]
    - ["gtceu:item_filter", 3]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "minecraft:nether_star", "gtceu:quantum_star"]
      t: |-
        Drawers first: nether stars (Keep Exact 1), quantum stars, gravi stars. Drums: radon, neutronium.
    - i: ["gtceu:hv_chemical_bath", "gtceu:quantum_star"]
      t: |-
        Bath: one nether star + 1250 mB radon → quantum star every 96 s at 480 EU/t. One HV chemical bath is enough.
    - i: ["gtceu:iv_autoclave", "gtceu:gravi_star"]
      t: |-
        Autoclave: quantum star by router, 288 mB neutronium by Pipez fluid pipe with a valve, 24 s at 7680 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:gravi_star"]
      t: Output drawer Keep Exact 4; routers to the three component lines that need them.
    - i: ["gtceu:neutronium_bucket", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: reserve neutronium before the first run, the fusion line has to deliver 288 mB per star.
---
# Gravi star: nether star → quantum star (radon bath) → gravi star (autoclave with 288 mB neutronium) - 1 per UV emitter, sensor and field generator

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_gravi` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Gravi stars](../../plan/p16.md#uvgravi)

**Tips:** 4, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-cb">
<div class="gt-head"><span class="gt-mname">HV Chemical Bath · 96 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nether star (nether_star chain) (minecraft:nether_star) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__nether_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star</span><span class="gt-note">Nether star (nether_star chain)</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="1250 mB radon (functionalstorage:oak_1) - 1250 mB"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1250 mB radon</span><span class="gt-sub"><span>Radon</span></span><b class="gt-q">1250 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_bath.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">96 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Quantum star (gtceu:quantum_star) - 1 / 96 s"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_bath</code></div>
</div>
<div class="gt-panel t-iv" id="m-au">
<div class="gt-head"><span class="gt-mname">IV Autoclave · 24 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Quantum star (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="288 mB molten neutronium (functionalstorage:oak_1) - 288 mB"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">288 mB molten neutronium</span><span class="gt-sub"><span>Neutronium</span></span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">24 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Gravi star (gtceu:gravi_star) - 1 / 24 s"><img class="gt-ico" src="../../assets/icons/gtceu__gravi_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravi Star</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_autoclave</code></div>
</div>
</div>

## Flow

- [HV Chemical Bath · 96 s · 480 EU/t](#m-cb) → [IV Autoclave · 24 s · 7680 EU/t](#m-au)

## How to build

1. Drawers first: nether stars (Keep Exact 1), quantum stars, gravi stars. Drums: radon, neutronium. — `functionalstorage:oak_1`, `minecraft:nether_star`, `gtceu:quantum_star`
2. Bath: one nether star + 1250 mB radon → quantum star every 96 s at 480 EU/t. One HV chemical bath is enough. — `gtceu:hv_chemical_bath`, `gtceu:quantum_star`
3. Autoclave: quantum star by router, 288 mB neutronium by Pipez fluid pipe with a valve, 24 s at 7680 EU/t. — `gtceu:iv_autoclave`, `gtceu:gravi_star`
4. Output drawer Keep Exact 4; routers to the three component lines that need them. — `functionalstorage:oak_1`, `gtceu:gravi_star`
5. Easy to miss: reserve neutronium before the first run, the fusion line has to deliver 288 mB per star. — `gtceu:neutronium_bucket`, `functionalstorage:oak_1`

## Tips

- Source (gtsrc CircuitRecipes, not touched by the pack): chemical bath, 1 nether star + 1250 mB radon → 1 quantum star, 1920 ticks (96 s) at VA\[HV\] = 480 EU/t; autoclave, 1 quantum star + 288 mB (2 x 144) molten neutronium → 1 gravi star, 480 ticks (24 s) at VA\[IV\] = 7680 EU/t. Quantum stars are already used by the ZPM component line (2 per ZPM emitter / sensor, 6 per field generator) and the UV fusion reactor takes one; gravi stars are the UV catalyst (1 per UV emitter, sensor, field generator) and the UHV one is 2.
- Neutronium comes from the UV fusion reactor (uv\_fusion\_mats, 144 mB per 72 s run), so every gravi star is two thirds of a neutronium run. Radon: tier-1 fusion (gold + mercury), 1 B per run, so a quantum star costs 1.25 runs of radon. Nether stars: the pack loop in the nether\_star chain (shards from the Wither star, energized and infused with the four elemental shards; Unverified details), or the wither.
- Sub-steps people skip: (1) the autoclave wants a fluid hatch for neutronium, not the item; (2) quantum stars sit in a drawer Keep Exact 4; (3) the bath uses the star item, not the nether star shard; (4) radon is also a gas for other chains: keep a 4 B reserve drum.
- **Unverified** the nether star supply rate.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_chemical_bath` | 1 |
| `gtceu:iv_autoclave` | 1 |
| `functionalstorage:oak_1` | 4 |
| `modularrouters:modular_router` | 2 |
| `gtceu:lv_robot_arm` | 2 |
| `gtceu:item_filter` | 3 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Needs:** [Nether star loop: shards → energized shards → infused shards → impure star → implosion](../iv/nether_star.md)
- **Main source for:** `gtceu:gravi_star`
