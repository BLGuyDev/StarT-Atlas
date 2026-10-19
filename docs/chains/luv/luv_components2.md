---
kind: chain
id: luv_components2
order: 1240
data:
  t: |-
    LuV components 2: robot arm, emitter, sensor, field generator (Assembly Line, 30 s, 7680 EU/t, LuV circuits, quantum stars, rhodium foil)
  inf: true
  "n":
    - - ag
      - |-
        Robot arm: 4 long HSS-S rod · 1 HSS-S gear · 3 small HSS-S gear · 2 LuV motor · 1 LuV piston · 1 LuV + 2 IV + 4 EV circuit · 4 NbTi cable · 288 mB solder · 250 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [LuV motor, "gtceu:luv_electric_motor"]
        - [LuV piston, "gtceu:luv_electric_piston"]
        - [HSS-S gear, "gtceu:hsss_gear"]
        - [Small HSS-S gear, "gtceu:small_hsss_gear"]
        - [NbTi single cable, "gtceu:niobium_titanium_single_cable"]
    - [a1, "Assembly Line · 30 s · 7680 EU/t", m, "gtceu:assembly_line"]
    - [ra, LuV Robot Arm, o, "gtceu:luv_robot_arm"]
    - [qs, "Quantum star · 1 per emitter, sensor, field generator", i, "gtceu:quantum_star"]
    - - eg
      - |-
        Emitter: HSS-S frame · LuV motor · 4 long HSS-S rod · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder
      - g
      - functionalstorage:oak_1
      - - [HSS-S frame, "gtceu:hsss_frame"]
        - [Long HSS-S rod, "gtceu:long_hsss_rod"]
        - [Rhodium foil, "gtceu:rhodium_foil"]
    - [a2, "Assembly Line (emitter)", m, "gtceu:assembly_line"]
    - [em, LuV Emitter, x, "gtceu:luv_emitter"]
    - - sg
      - |-
        Sensor: HSS-S frame · LuV motor · 4 HSS-S plate · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder
      - g
      - functionalstorage:oak_1
      - [[HSS-S frame, "gtceu:hsss_frame"], [HSS-S plate, "gtceu:hsss_plate"], [Rhodium foil, "gtceu:rhodium_foil"]]
    - [a3, "Assembly Line (sensor)", m, "gtceu:assembly_line"]
    - [se, LuV Sensor, o, "gtceu:luv_sensor"]
    - - fg
      - |-
        Field generator: HSS-S frame · 6 HSS-S plate · quantum star · 2 LuV emitter · 2 LuV circuit · 128 fine ITBTC wire · 4 NbTi cable · 576 mB solder
      - g
      - functionalstorage:oak_1
      - - [HSS-S frame, "gtceu:hsss_frame"]
        - [Fine ITBTC wire, "gtceu:fine_indium_tin_barium_titanium_cuprate_wire"]
        - [Soldering alloy, "gtceu:soldering_alloy_bucket"]
    - [a4, "Assembly Line (field generator)", m, "gtceu:assembly_line"]
    - [fo, LuV Field Generator, o, "gtceu:luv_field_generator"]
  e:
    - [ag, a1, "1"]
    - [a1, ra, "1 / 30 s"]
    - [eg, a2, "1"]
    - [qs, a2, "1"]
    - [a2, em, "1 / 30 s"]
    - [sg, a3, "1"]
    - [qs, a3, "1"]
    - [a3, se, "1 / 30 s"]
    - [em, a4, "2"]
    - [fg, a4, "1"]
    - [qs, a4, "1"]
    - [a4, fo, "1 / 30 s"]
  tips:
    - |-
      Pack recipes (luv_to_uv_components.js, luv row of tier_data.js; the vanilla Assembly Line recipes are removed): Robot arm: 4 long HSS-S rods, 1 HSS-S gear, 3 small HSS-S gears, 2 LuV motors, 1 LuV piston, 1 LuV circuit, 2 IV circuits, 4 EV circuits, 4 NbTi single cables, 288 mB soldering alloy + 250 mB lubricant. Emitter: 1 HSS-S frame, 1 LuV motor, 4 long HSS-S rods, 1 quantum star, 2 LuV circuits, 64 + 32 rhodium foil, 4 NbTi cables, 288 mB solder (no lubricant). Sensor: the same with 4 HSS-S plates instead of the rods. Field generator: 1 HSS-S frame, 6 HSS-S plates, 1 quantum star, 2 LuV emitters, 2 LuV circuits, 2 x 64 fine indium tin barium titanium cuprate wire, 4 NbTi cables, 576 mB solder. All 600 ticks at 7680 EU/t. The pack replaced vanilla’s ruridit / palladium parts (vanilla used ruridit plates and palladium foil) with HSS-S and rhodium.
    - |-
      Research: the arm uses the EV scanner (90 s, 1920 EU/t) with an IV Robot Arm; the emitter, sensor and field generator use an IV Scanner (3 s, 7680 EU/t) with the IV emitter, IV sensor and IV field generator in the scanner. The IV field generator is the only one you may not have: craft it first (1 quantum star + 2 double tungsten steel plates + 2 IV circuits + 4 samarium iron arsenic oxide quadruple wire, assembler in the iv_components chain tips).
    - |-
      LuV circuit use per part: arm 1 (plus 2 IV and 4 EV, so it also eats the earlier nano line), emitter 2, sensor 2, field generator 2 + 2 emitters = 6. Every LuV machine that holds arms, emitters or sensors adds more, so stock 8 to 16 nano mainframes before you start the line.
    - |-
      Quantum star: nether star + 1250 mB radon, HV chemical bath, 96 s at 480 EU/t (iv_components tips); 3 per emitter + sensor + field generator set. The nether star line is the nether_star chain; this era wants about 4 stars per LuV machine that holds an emitter and sensor, so the star loop (nether star shards) is the real rate limit.
    - |-
      Rhodium foil: 96 per emitter and 96 per sensor = 24 rhodium ingots each at 4 foil per bender craft. Rhodium comes from the platline chain at roughly 2.3 per 42 sludge, so each emitter or sensor is about 420 sludge, about 105 purified cooperite ore. This is the single most expensive part of LuV; do not build more emitters than you need. Unverified: whether the rhodium foil item exists in the fork without an extra pack flag (the pack script asks for gtceu:rhodium_foil; rhodium has only gear and fine wire flags in the material source). If EMI shows no rhodium foil, report it.
    - |-
      Fine ITBTC wire: indium tin barium titanium cuprate dust (mixer, 4 indium + 2 tin + 2 barium + 1 titanium + 7 copper + 14 B oxygen → 16 dust, circuit 4, 600 ticks at 30720 EU/t = a LuV mixer) → EBF 6000 K, 7680 EU/t, 1000 ticks → hot ingot → Vacuum Freezer 30720 EU/t → ingot → wiremill (about 8 fine wire per ingot, Unverified). 128 wire = about 16 ingots per generator. 6000 K needs naquadah coils (7200 K); an IV/LuV hatch bonus does not reach it (RTM 4500 K, HSS-G 5400 K + LuV hatch 400 K = 5800 K). Indium source: Unverified (indium concentrate chemical recipe exists, no pack route traced). So the field generator is the LAST LuV component: it needs naquadah coils, a LuV mixer, a LuV freezer.
    - |-
      Sub-steps people skip: (1) 96 foil are TWO stacks (64 and 32) in two buses; the field generator’s 128 wire likewise; (2) the LuV circuit is a tag: any of the three LuV circuits works; (3) the arm eats IV and EV circuits too: set Keep Exact on those drawers; (4) the emitter’s scan is of the IV emitter in the IV Scanner, not the EV scanner; (5) quantum stars are not consumed twice: 3 per set, not per part; (6) never share the Assembly Line bus order between emitter and sensor: the 4th item differs (long rod vs plate).
    - |-
      Unverified: how the pack gets samarium magnetic rods in volume (rare earth line only gives 25 % small dust), the niobium source for NbTi cables, and indium; these three are the raw-material gaps of LuV.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:iv_scanner", 1]
    - ["gtceu:lv_bender", 2]
    - ["gtceu:lv_wiremill", 1]
    - ["functionalstorage:oak_1", 30]
    - ["modularrouters:modular_router", 18]
    - ["gtceu:lv_robot_arm", 18]
    - ["gtceu:item_filter", 18]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["gtceu:assembly_line", "gtceu:luv_robot_arm", "gtceu:luv_electric_piston"]
      t: |-
        Robot arm first (it feeds every LuV machine): scan an IV Robot Arm at the EV Scanner, then load 9 buses in order: 4 long HSS-S rods, HSS-S gear, 3 small HSS-S gears, 2 LuV motors, LuV piston, a LuV circuit, 2 IV circuits (a stack of 2), 4 EV circuits (a stack of 4), 4 NbTi cables; 288 mB solder and 250 mB lubricant. 30 s at 7680 EU/t → LuV Robot Arm. Build the line at least 10 slices long.
    - i: ["gtceu:quantum_star", "gtceu:iv_emitter", "gtceu:iv_scanner"]
      t: |-
        Emitter and sensor need a quantum star each, and the IV Scanner: scan an IV emitter / IV sensor (3 s, 7680 EU/t) with the IV Scanner, one stick each. The IV Scanner is 4 LuV circuits + IV emitter + IV sensor + IV hull + 2 platinum cables.
    - i: ["gtceu:assembly_line", "gtceu:hsss_frame", "gtceu:rhodium_foil", "gtceu:luv_emitter"]
      t: |-
        Emitter: HSS-S frame, LuV motor, 4 long HSS-S rods, quantum star, 2 LuV circuits, 64 rhodium foil (one bus), 32 rhodium foil (next bus), 4 NbTi cables; 288 mB solder. 30 s → LuV Emitter. Output drawer Keep Exact 8; the field generator takes 2.
    - i: ["gtceu:assembly_line", "gtceu:hsss_plate", "gtceu:luv_sensor"]
      t: |-
        Sensor: the same ingredients but 4 HSS-S plates in the third slot instead of the long rods. One more data stick, one more bus order. 30 s → LuV Sensor, the first LuV part the quest chapter asks for after the Assembly Line.
    - i: ["gtceu:assembly_line", "gtceu:fine_indium_tin_barium_titanium_cuprate_wire", "gtceu:luv_field_generator"]
      t: |-
        Field generator last: HSS-S frame, 6 HSS-S plates, quantum star, 2 LuV emitters, 2 LuV circuits, 64 + 64 fine ITBTC wire, 4 NbTi cables; 576 mB solder. Needs the ITBTC line first (naquadah coils, luv_circuits stock, LuV freezer). 30 s → LuV Field Generator.
    - i: ["functionalstorage:oak_1", "gtceu:luv_robot_arm", "gtceu:luv_sensor", "gtceu:luv_emitter"]
      t: |-
        Output drawers with Keep Exact: arms 8, emitters 4, sensors 4, generators 2. These are the parts for the LuV machine line (assembler, circuit assembler), the LuV parallel hatch (sensor + emitter) and the fusion reactor (field generators).
    - i: ["functionalstorage:oak_1", "gtceu:micro_processor_mainframe", "gtceu:nano_processor_mainframe"]
      t: |-
        Easy to miss: the robot arm needs IV and EV circuits as well; the IV mainframe and the nano assembly (EV) must be in stock besides the LuV one. Keep the three drawers apart (tags look alike).
---
# LuV components 2: robot arm, emitter, sensor, field generator (Assembly Line, 30 s, 7680 EU/t, LuV circuits, quantum stars, rhodium foil)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Robot arm: 4 long HSS-S rod · 1 HSS-S gear · 3 small HSS-S gear · 2 LuV motor · 1 LuV piston · 1 LuV + 2 IV + 4 EV circuit · 4 NbTi cable · 288 mB solder · 250 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Robot arm: 4 long HSS-S rod · 1 HSS-S gear · 3 small HSS-S gear · 2 LuV motor · 1 LuV piston · 1 LuV + 2 IV + 4 EV circuit · 4 NbTi cable · 288 mB solder · 250 mB lubricant</span><span class="gt-sub"><span>LuV motor</span><span>LuV piston</span><span>HSS-S gear</span><span>Small HSS-S gear</span><span>NbTi single cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Robot Arm (gtceu:luv_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line (emitter)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Emitter: HSS-S frame · LuV motor · 4 long HSS-S rod · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Emitter: HSS-S frame · LuV motor · 4 long HSS-S rod · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder</span><span class="gt-sub"><span>HSS-S frame</span><span>Long HSS-S rod</span><span>Rhodium foil</span></span><b class="gt-q">1</b></span><span class="gt-slot" title="Quantum star · 1 per emitter, sensor, field generator (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><span class="gt-note">Quantum star · 1 per emitter, sensor, field generator</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LuV Emitter (gtceu:luv_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Emitter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line (sensor)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Sensor: HSS-S frame · LuV motor · 4 HSS-S plate · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Sensor: HSS-S frame · LuV motor · 4 HSS-S plate · quantum star · 2 LuV circuit · 96 rhodium foil · 4 NbTi cable · 288 mB solder</span><span class="gt-sub"><span>HSS-S frame</span><span>HSS-S plate</span><span>Rhodium foil</span></span><b class="gt-q">1</b></span><span class="gt-slot" title="Quantum star · 1 per emitter, sensor, field generator (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><span class="gt-note">Quantum star · 1 per emitter, sensor, field generator</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Sensor (gtceu:luv_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line (field generator)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Emitter (gtceu:luv_emitter) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__luv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Emitter</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Field generator: HSS-S frame · 6 HSS-S plate · quantum star · 2 LuV emitter · 2 LuV circuit · 128 fine ITBTC wire · 4 NbTi cable · 576 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Field generator: HSS-S frame · 6 HSS-S plate · quantum star · 2 LuV emitter · 2 LuV circuit · 128 fine ITBTC wire · 4 NbTi cable · 576 mB solder</span><span class="gt-sub"><span>HSS-S frame</span><span>Fine ITBTC wire</span><span>Soldering alloy</span></span><b class="gt-q">1</b></span><span class="gt-slot" title="Quantum star · 1 per emitter, sensor, field generator (gtceu:quantum_star) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__quantum_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Quantum Star</span><span class="gt-note">Quantum star · 1 per emitter, sensor, field generator</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Field Generator (gtceu:luv_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Field Generator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 7680 EU/t](#m-a1)
- [Assembly Line (emitter)](#m-a2) → [Assembly Line (field generator)](#m-a4)
- [Assembly Line (sensor)](#m-a3)

## How to build

1. Robot arm first (it feeds every LuV machine): scan an IV Robot Arm at the EV Scanner, then load 9 buses in order: 4 long HSS-S rods, HSS-S gear, 3 small HSS-S gears, 2 LuV motors, LuV piston, a LuV circuit, 2 IV circuits (a stack of 2), 4 EV circuits (a stack of 4), 4 NbTi cables; 288 mB solder and 250 mB lubricant. 30 s at 7680 EU/t → LuV Robot Arm. Build the line at least 10 slices long. — `gtceu:assembly_line`, `gtceu:luv_robot_arm`, `gtceu:luv_electric_piston`
2. Emitter and sensor need a quantum star each, and the IV Scanner: scan an IV emitter / IV sensor (3 s, 7680 EU/t) with the IV Scanner, one stick each. The IV Scanner is 4 LuV circuits + IV emitter + IV sensor + IV hull + 2 platinum cables. — `gtceu:quantum_star`, `gtceu:iv_emitter`, `gtceu:iv_scanner`
3. Emitter: HSS-S frame, LuV motor, 4 long HSS-S rods, quantum star, 2 LuV circuits, 64 rhodium foil (one bus), 32 rhodium foil (next bus), 4 NbTi cables; 288 mB solder. 30 s → LuV Emitter. Output drawer Keep Exact 8; the field generator takes 2. — `gtceu:assembly_line`, `gtceu:hsss_frame`, `gtceu:rhodium_foil`, `gtceu:luv_emitter`
4. Sensor: the same ingredients but 4 HSS-S plates in the third slot instead of the long rods. One more data stick, one more bus order. 30 s → LuV Sensor, the first LuV part the quest chapter asks for after the Assembly Line. — `gtceu:assembly_line`, `gtceu:hsss_plate`, `gtceu:luv_sensor`
5. Field generator last: HSS-S frame, 6 HSS-S plates, quantum star, 2 LuV emitters, 2 LuV circuits, 64 + 64 fine ITBTC wire, 4 NbTi cables; 576 mB solder. Needs the ITBTC line first (naquadah coils, luv\_circuits stock, LuV freezer). 30 s → LuV Field Generator. — `gtceu:assembly_line`, `gtceu:fine_indium_tin_barium_titanium_cuprate_wire`, `gtceu:luv_field_generator`
6. Output drawers with Keep Exact: arms 8, emitters 4, sensors 4, generators 2. These are the parts for the LuV machine line (assembler, circuit assembler), the LuV parallel hatch (sensor + emitter) and the fusion reactor (field generators). — `functionalstorage:oak_1`, `gtceu:luv_robot_arm`, `gtceu:luv_sensor`, `gtceu:luv_emitter`
7. Easy to miss: the robot arm needs IV and EV circuits as well; the IV mainframe and the nano assembly (EV) must be in stock besides the LuV one. Keep the three drawers apart (tags look alike). — `functionalstorage:oak_1`, `gtceu:micro_processor_mainframe`, `gtceu:nano_processor_mainframe`

## Tips

- Pack recipes (luv\_to\_uv\_components.js, luv row of tier\_data.js; the vanilla Assembly Line recipes are removed): Robot arm: 4 long HSS-S rods, 1 HSS-S gear, 3 small HSS-S gears, 2 LuV motors, 1 LuV piston, 1 LuV circuit, 2 IV circuits, 4 EV circuits, 4 NbTi single cables, 288 mB soldering alloy + 250 mB lubricant. Emitter: 1 HSS-S frame, 1 LuV motor, 4 long HSS-S rods, 1 quantum star, 2 LuV circuits, 64 + 32 rhodium foil, 4 NbTi cables, 288 mB solder (no lubricant). Sensor: the same with 4 HSS-S plates instead of the rods. Field generator: 1 HSS-S frame, 6 HSS-S plates, 1 quantum star, 2 LuV emitters, 2 LuV circuits, 2 x 64 fine indium tin barium titanium cuprate wire, 4 NbTi cables, 576 mB solder. All 600 ticks at 7680 EU/t. The pack replaced vanilla’s ruridit / palladium parts (vanilla used ruridit plates and palladium foil) with HSS-S and rhodium.
- Research: the arm uses the EV scanner (90 s, 1920 EU/t) with an IV Robot Arm; the emitter, sensor and field generator use an IV Scanner (3 s, 7680 EU/t) with the IV emitter, IV sensor and IV field generator in the scanner. The IV field generator is the only one you may not have: craft it first (1 quantum star + 2 double tungsten steel plates + 2 IV circuits + 4 samarium iron arsenic oxide quadruple wire, assembler in the iv\_components chain tips).
- LuV circuit use per part: arm 1 (plus 2 IV and 4 EV, so it also eats the earlier nano line), emitter 2, sensor 2, field generator 2 + 2 emitters = 6. Every LuV machine that holds arms, emitters or sensors adds more, so stock 8 to 16 nano mainframes before you start the line.
- Quantum star: nether star + 1250 mB radon, HV chemical bath, 96 s at 480 EU/t (iv\_components tips); 3 per emitter + sensor + field generator set. The nether star line is the nether\_star chain; this era wants about 4 stars per LuV machine that holds an emitter and sensor, so the star loop (nether star shards) is the real rate limit.
- Rhodium foil: 96 per emitter and 96 per sensor = 24 rhodium ingots each at 4 foil per bender craft. Rhodium comes from the platline chain at roughly 2.3 per 42 sludge, so each emitter or sensor is about 420 sludge, about 105 purified cooperite ore. This is the single most expensive part of LuV; do not build more emitters than you need. Unverified: whether the rhodium foil item exists in the fork without an extra pack flag (the pack script asks for gtceu:rhodium\_foil; rhodium has only gear and fine wire flags in the material source). If EMI shows no rhodium foil, report it.
- Fine ITBTC wire: indium tin barium titanium cuprate dust (mixer, 4 indium + 2 tin + 2 barium + 1 titanium + 7 copper + 14 B oxygen → 16 dust, circuit 4, 600 ticks at 30720 EU/t = a LuV mixer) → EBF 6000 K, 7680 EU/t, 1000 ticks → hot ingot → Vacuum Freezer 30720 EU/t → ingot → wiremill (about 8 fine wire per ingot, Unverified). 128 wire = about 16 ingots per generator. 6000 K needs naquadah coils (7200 K); an IV/LuV hatch bonus does not reach it (RTM 4500 K, HSS-G 5400 K + LuV hatch 400 K = 5800 K). Indium source: Unverified (indium concentrate chemical recipe exists, no pack route traced). So the field generator is the LAST LuV component: it needs naquadah coils, a LuV mixer, a LuV freezer.
- Sub-steps people skip: (1) 96 foil are TWO stacks (64 and 32) in two buses; the field generator’s 128 wire likewise; (2) the LuV circuit is a tag: any of the three LuV circuits works; (3) the arm eats IV and EV circuits too: set Keep Exact on those drawers; (4) the emitter’s scan is of the IV emitter in the IV Scanner, not the EV scanner; (5) quantum stars are not consumed twice: 3 per set, not per part; (6) never share the Assembly Line bus order between emitter and sensor: the 4th item differs (long rod vs plate).
- **Unverified** how the pack gets samarium magnetic rods in volume (rare earth line only gives 25 % small dust), the niobium source for NbTi cables, and indium; these three are the raw-material gaps of LuV.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:iv_scanner` | 1 |
| `gtceu:lv_bender` | 2 |
| `gtceu:lv_wiremill` | 1 |
| `functionalstorage:oak_1` | 30 |
| `modularrouters:modular_router` | 18 |
| `gtceu:lv_robot_arm` | 18 |
| `gtceu:item_filter` | 18 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Needs:** [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](../iv/iv_components.md)
- **Main source for:** `gtceu:luv_robot_arm`, `gtceu:luv_emitter`, `gtceu:luv_sensor`, `gtceu:luv_field_generator`
