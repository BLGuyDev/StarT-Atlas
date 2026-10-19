---
kind: chain
id: hv_components2
order: 1050
data:
  t: |-
    HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers
  inf: true
  "n":
    - [mo, HV Electric Motor, i, "gtceu:hv_electric_motor"]
    - [gc, Gold cables, i, "gtceu:gold_single_cable"]
    - [sr, Stainless rods, i, "gtceu:stainless_steel_rod"]
    - [pl, Stainless plates, i, "gtceu:stainless_steel_plate"]
    - [gr, "1 Small stainless gear", i, "gtceu:small_stainless_steel_gear"]
    - [a2, "LV Assembler (piston)", m, "gtceu:lv_assembler"]
    - [pi, HV Electric Piston, x, "gtceu:hv_electric_piston"]
    - [hc, HV circuit, i, "gtceu:advanced_integrated_circuit"]
    - [a5, "LV Assembler (robot arm)", m, "gtceu:lv_assembler"]
    - [ra, HV Robot Arm, o, "gtceu:hv_robot_arm"]
    - [ch, Chromium rods, i, "gtceu:chromium_rod"]
    - [ey, Ender eye, i, "minecraft:ender_eye"]
    - [a6, "LV Assembler · circuit 1 (emitter)", m, "gtceu:lv_assembler"]
    - [em, HV Emitter, o, "gtceu:hv_emitter"]
    - [a7, "LV Assembler (sensor)", m, "gtceu:lv_assembler"]
    - [se, HV Sensor, o, "gtceu:hv_sensor"]
  e:
    - [mo, a2, "1"]
    - [gc, a2, "2"]
    - [pl, a2, "3"]
    - [gr, a2]
    - [sr, a2, "2"]
    - [a2, pi]
    - [mo, a5, "2"]
    - [pi, a5, "1"]
    - [hc, a5, "1"]
    - [gc, a5, "3"]
    - [sr, a5, "2"]
    - [a5, ra]
    - [ch, a6, "4"]
    - [ey, a6]
    - [hc, a6, "2"]
    - [gc, a6, "2"]
    - [a6, em]
    - [ch, a7, "1"]
    - [ey, a7]
    - [pl, a7, "4"]
    - [hc, a7, "1"]
    - [a7, se]
  tips:
    - Motors, gold cables and stainless rods come from HV components 1/2 (follow the green links). Every recipe here is also an LV assembler recipe of 5 s at 30 EU/t (ComponentRecipes).
    - One HV Assembler needs 2 arms + 2 conveyors = 10 motors, plus 4 HV circuits (2 in the arms, 2 in the hull recipe).
    - |-
      Emitter and sensor are needed by the HV Laser Engraver (2 pistons + 1 emitter), the Industrial Barrel and parallel hatches; the HV Circuit Assembler and Scanner also need EV circuits, so they are not HV targets. Both want chromium rods and an ender eye: the eye is the gem for HV (GTCraftingComponents).
    - |-
      Field generator: not needed for any HV machine in this guide. The recipe is 1 quantum eye (ender eye + 250 mB radon, chemical bath, 24 s at 480 EU/t) + 2 stainless plates + 2 HV circuits + 4 mercury barium calcium cuprate quadruple wire. It only feeds the HV World Accelerator, gcrop machines and IV quantum chests, so leave it.
    - |-
      Unverified: the pack source of ender pearls (for the eye) and of chromium (route: see the Chromium chain in the EV era; rods: chromium ingot is EBF 1700 K, about 88 s at 120 EU/t from the gtsrc defaults, then lathe 1 → 2). Read both in EMI before you plan emitters and sensors.
  b:
    - ["gtceu:lv_assembler", 4]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_alloy_smelter", 1]
    - ["functionalstorage:oak_1", 6]
    - ["modularrouters:modular_router", 3]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:item_pipe", 16]
  how:
    - i:
        - gtceu:lv_bender
        - gtceu:stainless_steel_plate
        - gtceu:lv_alloy_smelter
        - gtceu:small_stainless_steel_gear
      t: |-
        Bender: stainless ingot → plate (3 per piston, 4 per sensor). Small gear: alloy smelter with the small gear mold, 2 stainless ingots → 1 gear. Motors, gold cables and stainless rods come from the drawers of HV components 1/2.
    - i: ["gtceu:lv_assembler", "gtceu:hv_electric_piston", "gtceu:small_stainless_steel_gear"]
      t: |-
        Piston assembler: 1 motor + 3 stainless plates + 2 stainless rods + 2 gold cables + 1 small stainless gear → 1 HV piston, 5 s. Keep 32 (two per Laser Engraver, one per robot arm).
    - i: ["gtceu:lv_assembler", "gtceu:hv_robot_arm", "gtceu:advanced_integrated_circuit"]
      t: |-
        Robot arm assembler: 3 gold cables + 2 stainless rods + 2 motors + 1 piston + 1 HV circuit (Advanced Integrated Circuit) → 1 HV robot arm, 5 s. The circuit comes from the circuit line’s drawer; stock 16 of them before you start arms and the HV Assembler.
    - i: ["gtceu:lv_assembler", "gtceu:hv_emitter", "gtceu:hv_sensor", "minecraft:ender_eye"]
      t: |-
        Emitter assembler on ghost circuit 1: 4 chromium rods + 2 gold cables + 2 HV circuits + 1 ender eye → 1 emitter. Sensor assembler: 1 chromium rod + 4 stainless plates + 1 HV circuit + 1 ender eye → 1 sensor. Both 5 s. The ender eye is the only unusual input: keep a small drawer of eyes and read the eye recipe in EMI.
    - i: ["gtceu:hv_machine_hull", "gtceu:hv_assembler"]
      t: |-
        Easy to miss: the HV Assembler is built from this line’s output (2 arms, 2 conveyors, 2 HV circuits, hull, 2 gold cables); the assembler that makes the parts stays LV. Craft the first set by hand and keep the line for the HV Laser Engraver (2 pistons + emitter), the Chemical Reactor (1 motor), the Large Chemical Reactor (1 motor) and the Cleanroom (2 motors).
---
# HV components 2/2: piston, robot arm, emitter, sensor (and field generator) on LV assemblers

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `hv_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [HV components (on LV assemblers)](../../plan/p8.md#hvcomp)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler (piston)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HV Electric Motor (gtceu:hv_electric_motor) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Motor</span><b class="gt-q">1</b></span><span class="gt-slot" title="Gold cables (gtceu:gold_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">Gold cables</span><b class="gt-q">2</b></span><span class="gt-slot" title="Stainless plates (gtceu:stainless_steel_plate) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Plate</span><span class="gt-note">Stainless plates</span><b class="gt-q">3</b></span><span class="gt-slot" title="1 Small stainless gear (gtceu:small_stainless_steel_gear)"><img class="gt-ico" src="../../assets/icons/gtceu__small_stainless_steel_gear.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Stainless Steel Gear</span><span class="gt-note">1 Small stainless gear</span></span><span class="gt-slot" title="Stainless rods (gtceu:stainless_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Rod</span><span class="gt-note">Stainless rods</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HV Electric Piston (gtceu:hv_electric_piston)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Piston</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a5">
<div class="gt-head"><span class="gt-mname">LV Assembler (robot arm)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HV Electric Motor (gtceu:hv_electric_motor) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_motor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Motor</span><b class="gt-q">2</b></span><span class="gt-slot" title="HV Electric Piston (gtceu:hv_electric_piston) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electric_piston.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Electric Piston</span><b class="gt-q">1</b></span><span class="gt-slot" title="HV circuit (gtceu:advanced_integrated_circuit) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_integrated_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Integrated Circuit</span><span class="gt-note">HV circuit</span><b class="gt-q">1</b></span><span class="gt-slot" title="Gold cables (gtceu:gold_single_cable) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">Gold cables</span><b class="gt-q">3</b></span><span class="gt-slot" title="Stainless rods (gtceu:stainless_steel_rod) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Rod</span><span class="gt-note">Stainless rods</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Robot Arm (gtceu:hv_robot_arm)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Robot Arm</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a6">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 1 (emitter)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chromium rods (gtceu:chromium_rod) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Rod</span><span class="gt-note">Chromium rods</span><b class="gt-q">4</b></span><span class="gt-slot" title="Ender eye (minecraft:ender_eye)"><img class="gt-ico" src="../../assets/icons/minecraft__ender_eye.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender Eye</span></span><span class="gt-slot" title="HV circuit (gtceu:advanced_integrated_circuit) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_integrated_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Integrated Circuit</span><span class="gt-note">HV circuit</span><b class="gt-q">2</b></span><span class="gt-slot" title="Gold cables (gtceu:gold_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__gold_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gold Single Cable</span><span class="gt-note">Gold cables</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Emitter (gtceu:hv_emitter)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Emitter</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a7">
<div class="gt-head"><span class="gt-mname">LV Assembler (sensor)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chromium rods (gtceu:chromium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Rod</span><span class="gt-note">Chromium rods</span><b class="gt-q">1</b></span><span class="gt-slot" title="Ender eye (minecraft:ender_eye)"><img class="gt-ico" src="../../assets/icons/minecraft__ender_eye.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ender Eye</span></span><span class="gt-slot" title="Stainless plates (gtceu:stainless_steel_plate) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Plate</span><span class="gt-note">Stainless plates</span><b class="gt-q">4</b></span><span class="gt-slot" title="HV circuit (gtceu:advanced_integrated_circuit) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__advanced_integrated_circuit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Integrated Circuit</span><span class="gt-note">HV circuit</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="HV Sensor (gtceu:hv_sensor)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Sensor</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Assembler (piston)](#m-a2) → [LV Assembler (robot arm)](#m-a5)
- [LV Assembler · circuit 1 (emitter)](#m-a6)
- [LV Assembler (sensor)](#m-a7)

## How to build

1. Bender: stainless ingot → plate (3 per piston, 4 per sensor). Small gear: alloy smelter with the small gear mold, 2 stainless ingots → 1 gear. Motors, gold cables and stainless rods come from the drawers of HV components 1/2. — `gtceu:lv_bender`, `gtceu:stainless_steel_plate`, `gtceu:lv_alloy_smelter`, `gtceu:small_stainless_steel_gear`
2. Piston assembler: 1 motor + 3 stainless plates + 2 stainless rods + 2 gold cables + 1 small stainless gear → 1 HV piston, 5 s. Keep 32 (two per Laser Engraver, one per robot arm). — `gtceu:lv_assembler`, `gtceu:hv_electric_piston`, `gtceu:small_stainless_steel_gear`
3. Robot arm assembler: 3 gold cables + 2 stainless rods + 2 motors + 1 piston + 1 HV circuit (Advanced Integrated Circuit) → 1 HV robot arm, 5 s. The circuit comes from the circuit line’s drawer; stock 16 of them before you start arms and the HV Assembler. — `gtceu:lv_assembler`, `gtceu:hv_robot_arm`, `gtceu:advanced_integrated_circuit`
4. Emitter assembler on ghost circuit 1: 4 chromium rods + 2 gold cables + 2 HV circuits + 1 ender eye → 1 emitter. Sensor assembler: 1 chromium rod + 4 stainless plates + 1 HV circuit + 1 ender eye → 1 sensor. Both 5 s. The ender eye is the only unusual input: keep a small drawer of eyes and read the eye recipe in EMI. — `gtceu:lv_assembler`, `gtceu:hv_emitter`, `gtceu:hv_sensor`, `minecraft:ender_eye`
5. Easy to miss: the HV Assembler is built from this line’s output (2 arms, 2 conveyors, 2 HV circuits, hull, 2 gold cables); the assembler that makes the parts stays LV. Craft the first set by hand and keep the line for the HV Laser Engraver (2 pistons + emitter), the Chemical Reactor (1 motor), the Large Chemical Reactor (1 motor) and the Cleanroom (2 motors). — `gtceu:hv_machine_hull`, `gtceu:hv_assembler`

## Tips

- Motors, gold cables and stainless rods come from HV components 1/2 (follow the green links). Every recipe here is also an LV assembler recipe of 5 s at 30 EU/t (ComponentRecipes).
- One HV Assembler needs 2 arms + 2 conveyors = 10 motors, plus 4 HV circuits (2 in the arms, 2 in the hull recipe).
- Emitter and sensor are needed by the HV Laser Engraver (2 pistons + 1 emitter), the Industrial Barrel and parallel hatches; the HV Circuit Assembler and Scanner also need EV circuits, so they are not HV targets. Both want chromium rods and an ender eye: the eye is the gem for HV (GTCraftingComponents).
- Field generator: not needed for any HV machine in this guide. The recipe is 1 quantum eye (ender eye + 250 mB radon, chemical bath, 24 s at 480 EU/t) + 2 stainless plates + 2 HV circuits + 4 mercury barium calcium cuprate quadruple wire. It only feeds the HV World Accelerator, gcrop machines and IV quantum chests, so leave it.
- **Unverified** the pack source of ender pearls (for the eye) and of chromium (route: see the Chromium chain in the EV era; rods: chromium ingot is EBF 1700 K, about 88 s at 120 EU/t from the gtsrc defaults, then lathe 1 → 2). Read both in EMI before you plan emitters and sensors.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 4 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_alloy_smelter` | 1 |
| `functionalstorage:oak_1` | 6 |
| `modularrouters:modular_router` | 3 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [HV components 1/2: motor, pump, conveyor on LV assemblers](hv_components.md), [HV circuits: Advanced Integrated Circuit and Microprocessor Assembly](circuits_hv.md), [Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod](chromium_line.md)
- **Feeds:** [HV hull line (stainless casing + polyethylene)](hv_hull_line.md)
- **Main source for:** `gtceu:hv_electric_piston`, `gtceu:hv_robot_arm`, `gtceu:hv_emitter`, `gtceu:hv_sensor`, `gtceu:stainless_steel_plate`
