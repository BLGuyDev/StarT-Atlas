---
kind: chain
id: comp_pump
order: 830
data:
  t: LV Electric Pump line
  inf: true
  "n":
    - [m, "1 Motor", i, "gtceu:lv_electric_motor"]
    - [c, "1 Tin cable", i, "gtceu:tin_single_cable"]
    - [pp, "1 Bronze fluid pipe", i, "gtceu:bronze_normal_fluid_pipe"]
    - [sc, "1 Tin screw", i, "gtceu:tin_screw"]
    - [ro, "1 Tin rotor", i, "gtceu:tin_rotor"]
    - [rr, "2 Rubber rings", i, "gtceu:rubber_ring"]
    - [as, "Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [out, LV Electric Pump, o, "gtceu:lv_electric_pump"]
  e: [[m, as], [c, as], [pp, as], [sc, as], [ro, as], [rr, as], [as, out, "12 / min"]]
  b:
    - ["gtceu:lv_assembler", 1]
    - ["gtceu:lv_robot_arm", 1]
    - ["gtceu:item_filter", 1]
    - ["functionalstorage:oak_1", 1]
    - ["pipez:item_pipe", 8]
  how:
    - i: ["gtceu:lv_assembler", "gtceu:lv_electric_pump"]
      t: |-
        Assembler: 1 motor + 1 tin cable + 1 bronze normal fluid pipe + 1 tin screw + 1 tin rotor + 2 rubber rings → 1 pump in 5 s.
    - i: ["gtceu:rubber_ring", "gtceu:ring_extruder_mold"]
      t: |-
        Rubber rings: liquid rubber → rubber ingot (solidifier, ingot mold) → extruder with the ring mold. Make a few dozen at a time; pumps are needed less often.
    - i: ["gtceu:tin_rotor", "gtceu:tin_screw"]
      t: |-
        Rotor and screw are cheap to craft by hand in batches (or a lathe: tin bolt → screw).
---
# LV Electric Pump line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `comp_pump` · **Tags:** Infinite source

**Era setup:** [LV](../../eras/lv.md)

**Plan modules:** [LV components](../../plan/p4.md#lvcomp)

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Motor (gtceu:lv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Motor</span><span class="gt-note">1 Motor</span></span><span class="gt-slot" title="1 Tin cable (gtceu:tin_single_cable)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Single Cable</span><span class="gt-note">1 Tin cable</span></span><span class="gt-slot" title="1 Bronze fluid pipe (gtceu:bronze_normal_fluid_pipe)"><img class="gt-ico" src="../../assets/icons/gtceu__bronze_normal_fluid_pipe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bronze Normal Fluid Pipe</span><span class="gt-note">1 Bronze fluid pipe</span></span><span class="gt-slot" title="1 Tin screw (gtceu:tin_screw)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_screw.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Screw</span><span class="gt-note">1 Tin screw</span></span><span class="gt-slot" title="1 Tin rotor (gtceu:tin_rotor)"><img class="gt-ico" src="../../assets/icons/gtceu__tin_rotor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tin Rotor</span><span class="gt-note">1 Tin rotor</span></span><span class="gt-slot" title="2 Rubber rings (gtceu:rubber_ring)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_ring.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber Ring</span><span class="gt-note">2 Rubber rings</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LV Electric Pump (gtceu:lv_electric_pump) - 12 / min"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LV Electric Pump</span><b class="gt-q">12 / min</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 30 EU/t](#m-as)

## How to build

1. Assembler: 1 motor + 1 tin cable + 1 bronze normal fluid pipe + 1 tin screw + 1 tin rotor + 2 rubber rings → 1 pump in 5 s. — `gtceu:lv_assembler`, `gtceu:lv_electric_pump`
2. Rubber rings: liquid rubber → rubber ingot (solidifier, ingot mold) → extruder with the ring mold. Make a few dozen at a time; pumps are needed less often. — `gtceu:rubber_ring`, `gtceu:ring_extruder_mold`
3. Rotor and screw are cheap to craft by hand in batches (or a lathe: tin bolt → screw). — `gtceu:tin_rotor`, `gtceu:tin_screw`

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 1 |
| `gtceu:lv_robot_arm` | 1 |
| `gtceu:item_filter` | 1 |
| `functionalstorage:oak_1` | 1 |
| `pipez:item_pipe` | 8 |

## Needs / Feeds

- **Needs:** [LV Electric Motor line](comp_motor.md), [Parts row 2: wires, fine wire, cables](comp_wires.md)
- **Main source for:** `gtceu:lv_electric_pump`
