---
kind: chain
id: oil_pyro
order: 290
data:
  t: |-
    Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff
  inf: true
  "n":
    - [gh, Greenhouse logs, s, "gtceu:greenhouse"]
    - [po, "Pyrolyse Oven · circ 3", m, "gtceu:pyrolyse_oven"]
    - [ho, Heavy Oil 16 B, f, "gtceu:oil_heavy_bucket"]
    - [wd, "32 Wood dust", i, "gtceu:wood_dust"]
    - [lo, Light Oil 16 B, f, "gtceu:oil_light_bucket"]
    - [pb, "32 Plant balls", i, "gtceu:plant_ball"]
    - [mo, Medium Oil 16 B, f, "gtceu:oil_medium_bucket"]
    - [dt, Distillation, o, "gtceu:distillation_tower"]
  e:
    - [gh, po, "32 logs"]
    - [wd, po]
    - [pb, po]
    - [po, ho, "384 EU/t"]
    - [po, lo, "96 EU/t"]
    - [po, mo, "96 EU/t"]
    - [ho, dt]
    - [lo, dt]
    - [mo, dt]
  tips:
    - |-
      Pack recipes (circuit 3, 32 items → 16 B oil + 4 ash dust): heavy oil from logs 15 s at 384 EU/t; light oil from wood dust 24 s and plain oil from bio chaff 16 s, both 96 EU/t; medium oil from plant balls 22.5 s, 96 EU/t.
    - |-
      Coils slow or speed the oven: cupronickel x1.33 duration (heavy oil 20 s), Kanthal x1.0 (15 s), Nichrome x0.67 (10 s). An HV hatch also overclocks the 96 EU/t oils once (half the time, 384 EU/t); heavy oil cannot overclock further.
    - |-
      Heavy oil is the only 384 EU/t one: it needs an HV Energy Hatch. The BOM lists the oven with an MV hatch; swap it for the HV hatch.
    - One greenhouse in CO₂ + fertilizer mode (128 logs per 30 s) feeds about 2.7 cupronickel ovens (96 logs a minute each).
    - |-
      Nothing in HV uses the oil yet: it waits for the EV distillation tower (HV hull + 4 EV circuits; oil recipe 96 EU/t). In this pack oil only comes from pyrolysis, there are no wells. Keep it in drums and do not overbuild.
  b:
    - ["gtceu:greenhouse", 1]
    - ["gtceu:pyrolyse_oven", 1]
    - ["gtceu:hv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 2]
    - ["modularrouters:modular_router", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["gtceu:steel_drum", 3]
    - ["pipez:fluid_pipe", 8]
    - ["pipez:item_pipe", 16]
  how:
    - i: ["gtceu:greenhouse", "minecraft:oak_log", "functionalstorage:oak_1"]
      t: Logs from the greenhouse go to a drawer. In CO₂ + fertilizer mode the greenhouse makes 128 logs per 30 s, 256 a minute. Keep the log drawer next to the oven so a Modular Router or a Pipez item pipe feeds it directly.
    - i: ["gtceu:pyrolyse_oven", "gtceu:cupronickel_coil_block", "gtceu:ulv_machine_casing"]
      t: |-
        Pyrolyse Oven: 17 ULV machine casings (6 minimum), 16 coils (cupronickel is enough), 2 air blocks in the middle, controller. Hatches: input bus, output bus, output hatch, maintenance, and an HV Energy Hatch. Kanthal coils make it faster, not just hotter.
    - i: ["gtceu:oil_heavy_bucket", "gtceu:ash_dust"]
      t: |-
        Heavy oil line, ghost circuit 3: 32 logs → 16 B heavy oil + 4 ash dust in 15 s at 384 EU/t. With cupronickel coils the oven is 25 % slower: 20 s, 48 B of oil and 96 logs a minute. Output hatch → steel drum; the ash goes to a drawer or an Item Voiding Cover.
    - i: ["gtceu:oil_light_bucket", "gtceu:wood_dust"]
      t: |-
        Light oil: 32 wood dust (from the cutter) → 16 B light oil in 24 s at 96 EU/t. Medium oil: 32 plant balls (8 crops each in a compressor) → 16 B in 22.5 s. Plain oil: 32 bio chaff → 16 B in 16 s. All use circuit 3 and only need an MV hatch; run each on its own oven if you want all three.
    - i: ["modularrouters:modular_router", "gtceu:steel_drum"]
      t: |-
        One input drawer per ingredient, with a Modular Router (or Pipez item pipe + Item Filter) into the oven’s input bus. The oil leaves through the output hatch by a pump cover or Pipez fluid pipe into its own steel drum: the oven simply stops when the drum is full. Never share a drum between oil types.
    - i: ["gtceu:steel_drum", "gtceu:distillation_tower"]
      t: |-
        Easy to miss: the distillation tower that uses all this is an EV machine. Until then the oil just piles up, so build one oven, fill four drums, and stop. Do not burn logs you need for charcoal and rubber.
---
# Oil without oil: Pyrolyse Oven on logs, wood dust, plant balls or bio chaff

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `oil_pyro` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Oil without wells (pyrolyse + distillery)](../../plan/p8.md#oil)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-po">
<div class="gt-head"><span class="gt-mname">Pyrolyse Oven · circ 3</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Greenhouse logs (gtceu:greenhouse) - 32 logs"><img class="gt-ico" src="../../assets/icons/gtceu__greenhouse.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Greenhouse</span><span class="gt-note">Greenhouse logs</span><span class="gt-tag">infinite</span><b class="gt-q">32 logs</b></span><span class="gt-slot" title="32 Wood dust (gtceu:wood_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__wood_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Wood Dust</span><span class="gt-note">32 Wood dust</span></span><span class="gt-slot" title="32 Plant balls (gtceu:plant_ball)"><img class="gt-ico" src="../../assets/icons/gtceu__plant_ball.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plant Ball</span><span class="gt-note">32 Plant balls</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__pyrolyse_oven.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Heavy Oil 16 B (gtceu:oil_heavy_bucket) - 384 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__oil_heavy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Heavy</span><span class="gt-note">Heavy Oil 16 B</span><b class="gt-q">384 EU/t</b></span><span class="gt-slot gt-fluid" title="Light Oil 16 B (gtceu:oil_light_bucket) - 96 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__oil_light_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Light</span><span class="gt-note">Light Oil 16 B</span><b class="gt-q">96 EU/t</b></span><span class="gt-slot gt-fluid" title="Medium Oil 16 B (gtceu:oil_medium_bucket) - 96 EU/t"><img class="gt-ico" src="../../assets/icons/gtceu__oil_medium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oil Medium</span><span class="gt-note">Medium Oil 16 B</span><b class="gt-q">96 EU/t</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:pyrolyse_oven</code></div>
</div>
</div>

## Flow

- [Pyrolyse Oven · circ 3](#m-po)

### Direct steps

- Heavy Oil 16 B → Distillation
- Light Oil 16 B → Distillation
- Medium Oil 16 B → Distillation

## How to build

1. Logs from the greenhouse go to a drawer. In CO₂ + fertilizer mode the greenhouse makes 128 logs per 30 s, 256 a minute. Keep the log drawer next to the oven so a Modular Router or a Pipez item pipe feeds it directly. — `gtceu:greenhouse`, `minecraft:oak_log`, `functionalstorage:oak_1`
2. Pyrolyse Oven: 17 ULV machine casings (6 minimum), 16 coils (cupronickel is enough), 2 air blocks in the middle, controller. Hatches: input bus, output bus, output hatch, maintenance, and an HV Energy Hatch. Kanthal coils make it faster, not just hotter. — `gtceu:pyrolyse_oven`, `gtceu:cupronickel_coil_block`, `gtceu:ulv_machine_casing`
3. Heavy oil line, ghost circuit 3: 32 logs → 16 B heavy oil + 4 ash dust in 15 s at 384 EU/t. With cupronickel coils the oven is 25 % slower: 20 s, 48 B of oil and 96 logs a minute. Output hatch → steel drum; the ash goes to a drawer or an Item Voiding Cover. — `gtceu:oil_heavy_bucket`, `gtceu:ash_dust`
4. Light oil: 32 wood dust (from the cutter) → 16 B light oil in 24 s at 96 EU/t. Medium oil: 32 plant balls (8 crops each in a compressor) → 16 B in 22.5 s. Plain oil: 32 bio chaff → 16 B in 16 s. All use circuit 3 and only need an MV hatch; run each on its own oven if you want all three. — `gtceu:oil_light_bucket`, `gtceu:wood_dust`
5. One input drawer per ingredient, with a Modular Router (or Pipez item pipe + Item Filter) into the oven’s input bus. The oil leaves through the output hatch by a pump cover or Pipez fluid pipe into its own steel drum: the oven simply stops when the drum is full. Never share a drum between oil types. — `modularrouters:modular_router`, `gtceu:steel_drum`
6. Easy to miss: the distillation tower that uses all this is an EV machine. Until then the oil just piles up, so build one oven, fill four drums, and stop. Do not burn logs you need for charcoal and rubber. — `gtceu:steel_drum`, `gtceu:distillation_tower`

## Tips

- Pack recipes (circuit 3, 32 items → 16 B oil + 4 ash dust): heavy oil from logs 15 s at 384 EU/t; light oil from wood dust 24 s and plain oil from bio chaff 16 s, both 96 EU/t; medium oil from plant balls 22.5 s, 96 EU/t.
- Coils slow or speed the oven: cupronickel x1.33 duration (heavy oil 20 s), Kanthal x1.0 (15 s), Nichrome x0.67 (10 s). An HV hatch also overclocks the 96 EU/t oils once (half the time, 384 EU/t); heavy oil cannot overclock further.
- Heavy oil is the only 384 EU/t one: it needs an HV Energy Hatch. The BOM lists the oven with an MV hatch; swap it for the HV hatch.
- One greenhouse in CO₂ + fertilizer mode (128 logs per 30 s) feeds about 2.7 cupronickel ovens (96 logs a minute each).
- Nothing in HV uses the oil yet: it waits for the EV distillation tower (HV hull + 4 EV circuits; oil recipe 96 EU/t). In this pack oil only comes from pyrolysis, there are no wells. Keep it in drums and do not overbuild.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:greenhouse` | 1 |
| `gtceu:pyrolyse_oven` | 1 |
| `gtceu:hv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 2 |
| `modularrouters:modular_router` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `gtceu:steel_drum` | 3 |
| `pipez:fluid_pipe` | 8 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Treated wood: cutter + spout](../lv/treated_wood.md), [Crops: Large Farm (no power)](../steam/crop_farm.md)
- **Feeds:** [Oil refinery](../ev/refinery.md)
- **Main source for:** `gtceu:oil_heavy_bucket`, `gtceu:oil_light_bucket`, `gtceu:oil_medium_bucket`
