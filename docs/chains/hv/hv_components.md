---
kind: chain
id: hv_components
order: 1040
data:
  t: "HV components 1/2: motor, pump, conveyor on LV assemblers"
  inf: true
  "n":
    - [sv, "2 Silver double cable", i, "gtceu:silver_double_cable"]
    - [el, "4 Electrum double wire", i, "gtceu:electrum_double_wire"]
    - [sr, Stainless rods, i, "gtceu:stainless_steel_rod"]
    - [mg, "1 Magnetic steel rod", i, "gtceu:magnetic_steel_rod"]
    - [a1, "LV Assembler · 5 s · 30 EU/t", m, "gtceu:lv_assembler"]
    - [mo, HV Electric Motor, x, "gtceu:hv_electric_motor"]
    - [gc, Gold cables, i, "gtceu:gold_single_cable"]
    - - pp
      - Pump parts
      - g
      - functionalstorage:oak_1
      - - [Stainless fluid pipe, "gtceu:stainless_steel_normal_fluid_pipe"]
        - [Steel screw, "gtceu:steel_screw"]
        - [Steel rotor, "gtceu:steel_rotor"]
        - ["2 Rubber rings", "gtceu:rubber_ring"]
    - [a3, "LV Assembler (pump)", m, "gtceu:lv_assembler"]
    - [pm, HV Electric Pump, o, "gtceu:hv_electric_pump"]
    - [rb, "864 mB liquid rubber", f, "gtceu:rubber_bucket"]
    - [a4, "LV Assembler · circuit 1 (conveyor)", m, "gtceu:lv_assembler"]
    - [cv, HV Conveyor Module, o, "gtceu:hv_conveyor_module"]
  e:
    - [sv, a1, "2"]
    - [el, a1, "4"]
    - [sr, a1, "2"]
    - [mg, a1, "1"]
    - [a1, mo]
    - [mo, a3, "1"]
    - [pp, a3]
    - [gc, a3, "1"]
    - [a3, pm]
    - [mo, a4, "2"]
    - [rb, a4]
    - [gc, a4, "1"]
    - [a4, cv]
  tips:
    - |-
      Every HV component recipe in this fork is an assembler recipe of 5 s at 30 EU/t (ComponentRecipes: duration 100 ticks, EUt VA[LV]). An LV assembler runs all of them, no HV power and no cleanroom. That is why the chain stays on LV machines even though the parts are HV. Piston, robot arm, emitter, sensor and field generator are in HV components 2/2.
    - |-
      Motors inside: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3. Make the motor line first and biggest, 12 a minute per assembler.
    - |-
      Raw cost per motor: 4 silver + 2 gold (2 silver double cables, 4 electrum ingots from 2 gold + 2 silver in the alloy smelter, standard alloy recipe), 1 stainless ingot (2 rods), 1 steel ingot (1 rod becomes magnetic), 288 mB rubber for the two silver cables.
    - |-
      Pump uses the MV Extruder: normal fluid pipe = 3 stainless ingots in an extruder with the pipe mold (about 42 EU/t, so MV), steel rotor = 4 steel ingots in an extruder with the rotor mold (64 EU/t, MV). Rings and screws as in the LV pump line (rubber ring from rubber ingot, screw from lathe on bolts).
    - |-
      Cables: 1 wire + 144 mB rubber in an assembler gives 1 cable (single and double alike; 7 EU/t). Gold wire: wiremill circuit 1, 1 ingot → 2 wires. Double wire: circuit 2, 1 ingot → 1. Quadruple would be circuit 4.
  b:
    - ["gtceu:lv_assembler", 3]
    - ["gtceu:lv_lathe", 2]
    - ["gtceu:lv_polarizer", 1]
    - ["gtceu:lv_wiremill", 3]
    - ["gtceu:lv_alloy_smelter", 1]
    - ["gtceu:mv_extruder", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:silver_ingot", "gtceu:gold_ingot", "gtceu:stainless_steel_ingot"]
      t: |-
        Input drawers first, one per item: silver, gold and stainless steel ingots (stainless from the EBF chain), steel ingots (steel chain), liquid rubber (rubber chain). Every machine below gets a Modular Router or Pipez item pipe with an Item Filter from its drawers and a Robot Arm Keep Exact cap on its output drawer, so nothing floods.
    - i: ["gtceu:lv_alloy_smelter", "gtceu:electrum_ingot", "gtceu:lv_wiremill", "gtceu:electrum_double_wire"]
      t: |-
        Electrum: LV Alloy Smelter, 1 gold + 1 silver → 2 electrum. Wiremill A on electrum, ghost circuit 2: 1 ingot → 1 double wire (4 per motor). Wiremill B on silver, circuit 2: silver double wire; Wiremill C on gold, circuit 1: 1 ingot → 2 single wires.
    - i: ["gtceu:lv_assembler", "gtceu:silver_double_cable", "gtceu:gold_single_cable", "gtceu:rubber_bucket"]
      t: |-
        Cable assembler (no ghost circuit): silver double wire + 144 mB liquid rubber → silver double cable; a second one for gold single wire + 144 mB rubber → gold single cable. 7 EU/t, 5 s. Each assembler takes one wire type only. Rubber through an input hatch from the rubber drum.
    - i: ["gtceu:lv_lathe", "gtceu:stainless_steel_rod", "gtceu:lv_polarizer", "gtceu:magnetic_steel_rod"]
      t: |-
        Lathe A on stainless: 1 ingot → 2 rods (harder rods are off in this pack). Lathe B on steel: 1 ingot → 2 steel rods; the Polarizer turns 1 steel rod into 1 magnetic steel rod (one per motor).
    - i: ["gtceu:lv_assembler", "gtceu:hv_electric_motor"]
      t: |-
        Motor assembler: 2 silver double cables + 2 stainless rods + 1 magnetic steel rod + 4 electrum double wires → 1 HV motor in 5 s at 30 EU/t (12 a minute). Keep 64 in the drawer: pistons, pumps, conveyors and arms all pull from here.
    - i: ["gtceu:lv_assembler", "gtceu:hv_electric_pump", "gtceu:stainless_steel_normal_fluid_pipe"]
      t: |-
        Pump assembler: 1 motor + 1 gold cable + 1 stainless normal fluid pipe + 1 steel screw + 1 steel rotor + 2 rubber rings → 1 HV pump, 5 s. Extruder: 3 stainless ingots → 1 pipe (pipe mold), 4 steel ingots → 1 rotor (rotor mold). Pumps go into the HV distillery, autoclave, fluid solidifier (2), chemical bath, fluid heater, Industrial Barrel (2) and the cracker (2): stock 8.
    - i: ["gtceu:lv_assembler", "gtceu:hv_conveyor_module", "gtceu:rubber_bucket"]
      t: |-
        Conveyor assembler on ghost circuit 1: 2 motors + 1 gold cable + 864 mB liquid rubber → 1 conveyor, 5 s. Pipe the rubber in through a fluid hatch side of the machine, never mix it with the cable assemblers’ hatch.
---
# HV components 1/2: motor, pump, conveyor on LV assemblers

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `hv_components` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [HV components (on LV assemblers)](../../plan/p8.md#hvcomp)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Silver double cable (gtceu:silver_double_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__silver_double_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silver Double Cable</span><span class="gt-note">2 Silver double cable</span><b class="gt-q">2</b></span><span class="gt-slot" title="4 Electrum double wire (gtceu:electrum_double_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__electrum_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electrum Double Wire</span><span class="gt-note">4 Electrum double wire</span><b class="gt-q">4</b></span><span class="gt-slot" title="Stainless rods (gtceu:stainless_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Rod</span><span class="gt-note">Stainless rods</span><b class="gt-q">2</b></span><span class="gt-slot" title="1 Magnetic steel rod (gtceu:magnetic_steel_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Steel Rod</span><span class="gt-note">1 Magnetic steel rod</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HV Electric Motor (gtceu:hv_electric_motor)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Motor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler (pump)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HV Electric Motor (gtceu:hv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Pump parts (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Pump parts</span><span class="gt-sub"><span>Stainless fluid pipe</span><span>Steel screw</span><span>Steel rotor</span><span>2 Rubber rings</span></span></span><span class="gt-slot" title="Gold cables (gtceu:gold_single_cable) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">Gold cables</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Electric Pump (gtceu:hv_electric_pump)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_pump.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Pump</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a4">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 1 (conveyor)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HV Electric Motor (gtceu:hv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="864 mB liquid rubber (gtceu:rubber_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__rubber_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rubber</span><span class="gt-note">864 mB liquid rubber</span></span><span class="gt-slot" title="Gold cables (gtceu:gold_single_cable) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">Gold cables</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Conveyor Module (gtceu:hv_conveyor_module)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_conveyor_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Conveyor Module</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Assembler · 5 s · 30 EU/t](#m-a1) → [LV Assembler (pump)](#m-a3) (also LV Assembler · 5 s · 30 EU/t → [LV Assembler · circuit 1 (conveyor)](#m-a4))
- [LV Assembler · circuit 1 (conveyor)](#m-a4)

## How to build

1. Input drawers first, one per item: silver, gold and stainless steel ingots (stainless from the EBF chain), steel ingots (steel chain), liquid rubber (rubber chain). Every machine below gets a Modular Router or Pipez item pipe with an Item Filter from its drawers and a Robot Arm Keep Exact cap on its output drawer, so nothing floods. — `functionalstorage:oak_1`, `gtceu:silver_ingot`, `gtceu:gold_ingot`, `gtceu:stainless_steel_ingot`
2. Electrum: LV Alloy Smelter, 1 gold + 1 silver → 2 electrum. Wiremill A on electrum, ghost circuit 2: 1 ingot → 1 double wire (4 per motor). Wiremill B on silver, circuit 2: silver double wire; Wiremill C on gold, circuit 1: 1 ingot → 2 single wires. — `gtceu:lv_alloy_smelter`, `gtceu:electrum_ingot`, `gtceu:lv_wiremill`, `gtceu:electrum_double_wire`
3. Cable assembler (no ghost circuit): silver double wire + 144 mB liquid rubber → silver double cable; a second one for gold single wire + 144 mB rubber → gold single cable. 7 EU/t, 5 s. Each assembler takes one wire type only. Rubber through an input hatch from the rubber drum. — `gtceu:lv_assembler`, `gtceu:silver_double_cable`, `gtceu:gold_single_cable`, `gtceu:rubber_bucket`
4. Lathe A on stainless: 1 ingot → 2 rods (harder rods are off in this pack). Lathe B on steel: 1 ingot → 2 steel rods; the Polarizer turns 1 steel rod into 1 magnetic steel rod (one per motor). — `gtceu:lv_lathe`, `gtceu:stainless_steel_rod`, `gtceu:lv_polarizer`, `gtceu:magnetic_steel_rod`
5. Motor assembler: 2 silver double cables + 2 stainless rods + 1 magnetic steel rod + 4 electrum double wires → 1 HV motor in 5 s at 30 EU/t (12 a minute). Keep 64 in the drawer: pistons, pumps, conveyors and arms all pull from here. — `gtceu:lv_assembler`, `gtceu:hv_electric_motor`
6. Pump assembler: 1 motor + 1 gold cable + 1 stainless normal fluid pipe + 1 steel screw + 1 steel rotor + 2 rubber rings → 1 HV pump, 5 s. Extruder: 3 stainless ingots → 1 pipe (pipe mold), 4 steel ingots → 1 rotor (rotor mold). Pumps go into the HV distillery, autoclave, fluid solidifier (2), chemical bath, fluid heater, Industrial Barrel (2) and the cracker (2): stock 8. — `gtceu:lv_assembler`, `gtceu:hv_electric_pump`, `gtceu:stainless_steel_normal_fluid_pipe`
7. Conveyor assembler on ghost circuit 1: 2 motors + 1 gold cable + 864 mB liquid rubber → 1 conveyor, 5 s. Pipe the rubber in through a fluid hatch side of the machine, never mix it with the cable assemblers’ hatch. — `gtceu:lv_assembler`, `gtceu:hv_conveyor_module`, `gtceu:rubber_bucket`

## Tips

- Every HV component recipe in this fork is an assembler recipe of 5 s at 30 EU/t (ComponentRecipes: duration 100 ticks, EUt VA\[LV\]). An LV assembler runs all of them, no HV power and no cleanroom. That is why the chain stays on LV machines even though the parts are HV. Piston, robot arm, emitter, sensor and field generator are in HV components 2/2.
- Motors inside: piston 1, pump 1, conveyor 2, robot arm 2 plus its piston = 3. Make the motor line first and biggest, 12 a minute per assembler.
- Raw cost per motor: 4 silver + 2 gold (2 silver double cables, 4 electrum ingots from 2 gold + 2 silver in the alloy smelter, standard alloy recipe), 1 stainless ingot (2 rods), 1 steel ingot (1 rod becomes magnetic), 288 mB rubber for the two silver cables.
- Pump uses the MV Extruder: normal fluid pipe = 3 stainless ingots in an extruder with the pipe mold (about 42 EU/t, so MV), steel rotor = 4 steel ingots in an extruder with the rotor mold (64 EU/t, MV). Rings and screws as in the LV pump line (rubber ring from rubber ingot, screw from lathe on bolts).
- Cables: 1 wire + 144 mB rubber in an assembler gives 1 cable (single and double alike; 7 EU/t). Gold wire: wiremill circuit 1, 1 ingot → 2 wires. Double wire: circuit 2, 1 ingot → 1. Quadruple would be circuit 4.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 3 |
| `gtceu:lv_lathe` | 2 |
| `gtceu:lv_polarizer` | 1 |
| `gtceu:lv_wiremill` | 3 |
| `gtceu:lv_alloy_smelter` | 1 |
| `gtceu:mv_extruder` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |

## Needs / Feeds

- **Feeds:** [HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers](hv_components2.md), [HV hull line (stainless casing + polyethylene)](hv_hull_line.md)
- **Main source for:** `gtceu:hv_electric_motor`, `gtceu:hv_electric_pump`, `gtceu:hv_conveyor_module`, `gtceu:silver_double_cable`, `gtceu:electrum_double_wire`, `gtceu:gold_single_cable`, `gtceu:stainless_steel_rod`, `gtceu:magnetic_steel_rod`
