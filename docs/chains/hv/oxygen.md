---
kind: chain
id: oxygen
order: 300
data:
  t: Oxygen & nitrogen from air (Gas Collector + Centrifuge)
  inf: true
  "n":
    - [gc, "Gas Collector · circ 1", s, "gtceu:mv_gas_collector"]
    - [air, Air, f, "gtceu:air_bucket"]
    - [ce, Centrifuge, m, "gtceu:mv_centrifuge"]
    - [o, Oxygen, o, "gtceu:oxygen_bucket"]
    - ["n", Nitrogen, o, "gtceu:nitrogen_bucket"]
  e: [[gc, air], [air, ce], [ce, o], [ce, "n"]]
  tips:
    - |-
      MV Gas Collector, ghost circuit 1: 10 B of air per 5 s at 64 EU/t = 120 B a minute (HV: 240 B a minute at 256 EU/t). Overworld only.
    - |-
      Centrifuge: 10 B of air → 3.9 B nitrogen + 1 B oxygen. MV centrifuge 20 s at 112 EU/t, HV centrifuge 10 s at 448 EU/t.
    - One collector (120 B a minute) feeds four MV centrifuges; add centrifuges, not collectors. One MV centrifuge alone makes 11.7 B nitrogen and 3 B oxygen a minute.
    - The PTFE line can use plain air and the stainless EBF takes 1 B nitrogen per ingot, so nitrogen is the real consumer here.
    - |-
      Liquid air is the EV step: a Vacuum Freezer (3 pumps + 3 EV circuits) makes 4 B liquid air from 4 B air in 80 ticks at 480 EU/t; the Distillation Tower (HV hull + 4 EV circuits) splits 50 B into 35 B nitrogen + 11 B oxygen + 2.5 B CO2 + 1 B helium + 0.5 B argon in 2000 ticks at 480 EU/t. The air collector stays at 16 EU/t.
  b: [["gtceu:mv_gas_collector", 1], ["gtceu:mv_centrifuge", 1], ["gtceu:steel_drum", 3], ["pipez:fluid_pipe", 8]]
  how:
    - i: ["gtceu:mv_gas_collector", "gtceu:air_bucket"]
      t: |-
        MV Gas Collector with ghost circuit 1: 10 B of air every 5 s at 64 EU/t (the recipe is 16 EU/t over 10 s, an MV machine overclocks it once). 120 B a minute. It needs open air in the overworld; place it outside or under glass, not deep in a mine.
    - i: ["gtceu:steel_drum", "pipez:fluid_pipe"]
      t: The air goes into a steel drum next to the centrifuge, through a Pipez fluid pipe or a pump cover. The collector simply pauses when the drum is full.
    - i: ["gtceu:mv_centrifuge", "gtceu:nitrogen_bucket", "gtceu:oxygen_bucket"]
      t: |-
        MV Centrifuge: 10 B air → 3.9 B nitrogen + 1 B oxygen. The recipe is 80 s at 7 EU/t, an MV machine overclocks twice: 20 s at 112 EU/t. That is 30 B of air a minute, so a collector can feed four centrifuges.
    - i: ["gtceu:steel_drum", "gtceu:nitrogen_bucket"]
      t: |-
        Lock each output hatch to its own gas (fluid filter or the hatch lock), then a drum for each: nitrogen and oxygen in separate drums, so the full one never blocks the other.
    - i: ["gtceu:electric_blast_furnace", "gtceu:polytetrafluoroethylene_bucket"]
      t: |-
        Where it goes: 1 B nitrogen per stainless or lumium ingot in the EBF (circuit 2, 33 % faster); 200 mB oxygen per steel in the MV steel line; 1 B oxygen per 144 mB TFE for PTFE. For PTFE the plain-air route is cheaper.
---
# Oxygen &amp; nitrogen from air (Gas Collector + Centrifuge)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `oxygen` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Air: oxygen and nitrogen](../../plan/p7.md#air)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-ce">
<div class="gt-head"><span class="gt-mname">Centrifuge</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Air (gtceu:air_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__air_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Air</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Oxygen (gtceu:oxygen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygen Bucket</span></span><span class="gt-slot gt-outp" title="Nitrogen (gtceu:nitrogen_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__nitrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitrogen Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_centrifuge</code></div>
</div>
</div>

## Flow

- [Centrifuge](#m-ce)

### Direct steps

- Gas Collector · circ 1 → Air

## How to build

1. MV Gas Collector with ghost circuit 1: 10 B of air every 5 s at 64 EU/t (the recipe is 16 EU/t over 10 s, an MV machine overclocks it once). 120 B a minute. It needs open air in the overworld; place it outside or under glass, not deep in a mine. — `gtceu:mv_gas_collector`, `gtceu:air_bucket`
2. The air goes into a steel drum next to the centrifuge, through a Pipez fluid pipe or a pump cover. The collector simply pauses when the drum is full. — `gtceu:steel_drum`, `pipez:fluid_pipe`
3. MV Centrifuge: 10 B air → 3.9 B nitrogen + 1 B oxygen. The recipe is 80 s at 7 EU/t, an MV machine overclocks twice: 20 s at 112 EU/t. That is 30 B of air a minute, so a collector can feed four centrifuges. — `gtceu:mv_centrifuge`, `gtceu:nitrogen_bucket`, `gtceu:oxygen_bucket`
4. Lock each output hatch to its own gas (fluid filter or the hatch lock), then a drum for each: nitrogen and oxygen in separate drums, so the full one never blocks the other. — `gtceu:steel_drum`, `gtceu:nitrogen_bucket`
5. Where it goes: 1 B nitrogen per stainless or lumium ingot in the EBF (circuit 2, 33 % faster); 200 mB oxygen per steel in the MV steel line; 1 B oxygen per 144 mB TFE for PTFE. For PTFE the plain-air route is cheaper. — `gtceu:electric_blast_furnace`, `gtceu:polytetrafluoroethylene_bucket`

## Tips

- MV Gas Collector, ghost circuit 1: 10 B of air per 5 s at 64 EU/t = 120 B a minute (HV: 240 B a minute at 256 EU/t). Overworld only.
- Centrifuge: 10 B of air → 3.9 B nitrogen + 1 B oxygen. MV centrifuge 20 s at 112 EU/t, HV centrifuge 10 s at 448 EU/t.
- One collector (120 B a minute) feeds four MV centrifuges; add centrifuges, not collectors. One MV centrifuge alone makes 11.7 B nitrogen and 3 B oxygen a minute.
- The PTFE line can use plain air and the stainless EBF takes 1 B nitrogen per ingot, so nitrogen is the real consumer here.
- Liquid air is the EV step: a Vacuum Freezer (3 pumps + 3 EV circuits) makes 4 B liquid air from 4 B air in 80 ticks at 480 EU/t; the Distillation Tower (HV hull + 4 EV circuits) splits 50 B into 35 B nitrogen + 11 B oxygen + 2.5 B CO2 + 1 B helium + 0.5 B argon in 2000 ticks at 480 EU/t. The air collector stays at 16 EU/t.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_gas_collector` | 1 |
| `gtceu:mv_centrifuge` | 1 |
| `gtceu:steel_drum` | 3 |
| `pipez:fluid_pipe` | 8 |

## Needs / Feeds

- **Feeds:** [Charcoal: Pyrolyse Oven](../feeders/charcoal_pyro.md)
- **Main source for:** `gtceu:oxygen_bucket`, `gtceu:nitrogen_bucket`
