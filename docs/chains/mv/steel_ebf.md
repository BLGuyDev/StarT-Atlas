---
kind: chain
id: steel_ebf
order: 740
data:
  t: "Steel: Electric Blast Furnace + oxygen"
  "n":
    - [wi, Wrought Iron, i, "gtceu:wrought_iron_ingot"]
    - [o, "200 mB Oxygen", f, "gtceu:oxygen_bucket"]
    - [ebf, "EBF · 1000 K", m, "gtceu:electric_blast_furnace"]
    - [st, Steel, o, "gtceu:steel_ingot"]
  e: [[wi, ebf], [o, ebf], [ebf, st, "15 s"]]
  tips:
    - |-
      120 EU/t (MV). Iron instead of wrought iron: 25 s. With HV power it overclocks to 7.5 s.
    - Only worth it once oxygen is free (the CO₂ greenhouse makes 1 B per cycle); until then the Solid Blast Furnace is cheaper.
    - Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.
  b: [["gtceu:electric_blast_furnace", 1]]
  how:
    - i: ["gtceu:electric_blast_furnace", "gtceu:cupronickel_coil_block"]
      t: EBF with cupronickel coils (1800 K) is enough for steel (1000 K).
    - i: ["gtceu:wrought_iron_ingot", "gtceu:oxygen_bucket"]
      t: |-
        1 wrought iron + 200 mB oxygen → 1 steel in 15 s at 120 EU/t. No charcoal at all.
---
# Steel: Electric Blast Furnace + oxygen

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `steel_ebf`

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Air: oxygen and nitrogen](../../plan/p7.md#air)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-ebf">
<div class="gt-head"><span class="gt-mname">EBF · 1000 K</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Wrought Iron (gtceu:wrought_iron_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__wrought_iron_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wrought Iron Ingot</span></span><span class="gt-slot gt-fluid" title="200 mB Oxygen (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen</span><span class="gt-note">200 mB Oxygen</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Steel (gtceu:steel_ingot) - 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [EBF · 1000 K](#m-ebf)

## How to build

1. EBF with cupronickel coils (1800 K) is enough for steel (1000 K). — `gtceu:electric_blast_furnace`, `gtceu:cupronickel_coil_block`
2. 1 wrought iron + 200 mB oxygen → 1 steel in 15 s at 120 EU/t. No charcoal at all. — `gtceu:wrought_iron_ingot`, `gtceu:oxygen_bucket`

## Tips

- 120 EU/t (MV). Iron instead of wrought iron: 25 s. With HV power it overclocks to 7.5 s.
- Only worth it once oxygen is free (the CO₂ greenhouse makes 1 B per cycle); until then the Solid Blast Furnace is cheaper.
- Needs oxygen from the HV air line (oxygen chain, HV era); plan it before this step.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_blast_furnace` | 1 |

## Needs / Feeds

- **Needs:** [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md)
