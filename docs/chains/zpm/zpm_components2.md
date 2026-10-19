---
kind: chain
id: zpm_components2
order: 1450
data:
  t: |-
    ZPM components 2: robot arm (scanned), emitter, sensor, field generator (station research, 2 quantum stars each, trinium foil, URD wire)
  inf: true
  "n":
    - - ra
      - |-
        Arm: 4 long osthendah rod · gear · 3 small gear · 2 ZPM motor · ZPM piston · ZPM + 2 LuV + 4 IV circuit · 4 VG cable · 576 mB solder + 500 mB lubricant
      - g
      - functionalstorage:oak_1
      - - [ZPM motor, "gtceu:zpm_electric_motor"]
        - [ZPM piston, "gtceu:zpm_electric_piston"]
        - [Osthendah gear, "gtceu:osthendah_gear"]
        - [Small osthendah gear, "gtceu:small_osthendah_gear"]
        - [Quantum processor mainframe, "gtceu:quantum_processor_mainframe"]
    - [a1, "Assembly Line · 30 s · 30 720 EU/t (scan: LuV arm)", m, "gtceu:assembly_line"]
    - [ar, ZPM Robot Arm, o, "gtceu:zpm_robot_arm"]
    - - em
      - |-
        Emitter: osthendah frame · ZPM motor · 4 long osthendah rod · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder
      - g
      - functionalstorage:oak_1
      - - [Osthendah frame, "gtceu:osthendah_frame"]
        - [Quantum star, "gtceu:quantum_star"]
        - [Trinium foil, "gtceu:trinium_foil"]
        - [ZPM motor, "gtceu:zpm_electric_motor"]
    - [a2, "Assembly Line · 30 s · 30 720 EU/t (station: LuV emitter, 4 CWU/t)", m, "gtceu:assembly_line"]
    - [et, ZPM Emitter, x, "gtceu:zpm_emitter"]
    - - se
      - |-
        Sensor: osthendah frame · ZPM motor · 4 osthendah plate · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder
      - g
      - functionalstorage:oak_1
      - - [Osthendah frame, "gtceu:osthendah_frame"]
        - [Quantum star, "gtceu:quantum_star"]
        - [Trinium foil, "gtceu:trinium_foil"]
    - [a3, "Assembly Line · 30 s · 30 720 EU/t (station: LuV sensor)", m, "gtceu:assembly_line"]
    - [sn, ZPM Sensor, o, "gtceu:zpm_sensor"]
    - - fg
      - |-
        Field generator: osthendah frame · 6 plate · 2 quantum star · 2 ZPM emitter · 2 ZPM circuit · 128 fine URD wire · 4 VG cable · 1152 mB solder
      - g
      - functionalstorage:oak_1
      - - [Osthendah plate, "gtceu:osthendah_plate"]
        - [Fine URD wire, "gtceu:fine_uranium_rhodium_dinaquadide_wire"]
        - [Quantum star, "gtceu:quantum_star"]
    - [a4, "Assembly Line · 30 s · 30 720 EU/t (station: LuV field generator)", m, "gtceu:assembly_line"]
    - [fo, ZPM Field Generator, o, "gtceu:zpm_field_generator"]
  e:
    - [ra, a1, "1"]
    - [a1, ar, "1 / 30 s"]
    - [em, a2, "1"]
    - [a2, et, "1 / 30 s"]
    - [et, a4, "2"]
    - [se, a3, "1"]
    - [a3, sn, "1 / 30 s"]
    - [fg, a4, "1"]
    - [a4, fo, "1 / 30 s"]
  tips:
    - |-
      Recipes (utils/tier_data.js zpm row + luv_to_uv_components.js; all 600 ticks at 30 720 EU/t, scaler 2: solder x 4, quantum stars x 2). Robot arm: 4 long osthendah rods + 1 osthendah gear + 3 small osthendah gears + 2 ZPM motors + 1 ZPM piston + 1 ZPM circuit + 2 LuV circuits + 4 IV circuits + 4 VG single cables, 576 mB soldering alloy + 500 mB lubricant, SCANNER research of the LuV arm. Emitter: 1 osthendah frame + 1 ZPM motor + 4 long osthendah rods + 2 quantum stars + 2 ZPM circuits + 96 trinium foil (64 + 32) + 4 cables, 576 mB solder. Sensor: same with 4 osthendah plates instead of the rods. Field generator: 1 osthendah frame + 6 plates + 2 quantum stars + 2 ZPM emitters + 2 ZPM circuits + 128 fine URD wire (64 + 64) + 4 cables, 1152 mB solder. Emitter, sensor and field generator use STATION research of the LuV part: 4 CWU/t at 30 720 EU/t, so the Research Station and HPCA (zpm_research) must stand first.
    - |-
      Cost in rare inputs (verified counts): emitter and sensor 24 trinium ingots each (foil = 1/4 ingot, 4 foil per plate), 2 quantum stars, 2 ZPM circuits, 1 motor; field generator 16 URD ingots (128 fine wire), 2 stars, 2 circuits PLUS 2 emitters = 6 stars, 6 ZPM circuits, 48 trinium and 2 motors in total. Robot arm: 3 motors in total (2 + the piston’s) and 3 circuit tiers, no stars. A quantum star = 1 nether star + 1250 mB radon (HV Chemical Bath, 1920 ticks at 480 EU/t): 6 stars per field generator is 6 whole nether stars, 7.5 B of radon, and a nether star loop (nether_star chain) that yields 1.19 stars per star: start it now.
    - |-
      Circuits per arm: 1 ZPM + 2 LuV + 4 IV circuits (tag-based, any LuV or IV circuit works); the nano line gives LuV circuits (luv_circuits) and the IV mainframes the IV ones. So the arm is the one ZPM component you can make as soon as the first ZPM circuit exists and the piston and motors are done; it does not need the Research Station.
    - |-
      Where each goes: ZPM robot arm: Object Holder (2), ZPM buses and assemblers; ZPM emitter: ZPM sensors and field generators, the object holder (8 LuV emitters, not ZPM), the computation transmitter hatch (LuV emitter); ZPM sensor and field generator: ZPM machines, the fusion casing (the casing takes the LuV field generator below the tier: fusion MK II casing = ZPM hull + fusion coil + 2 ZPM voltage coils + 1 LuV field generator + 6 reflector panels), the HPCA advanced computation component (ZPM field generator + UV circuits, UV era).
    - |-
      Foil: Bender, circuit 10 (Unverified, per the LuV chain’s rule): 1 trinium plate → 4 foil, so 96 foil = 24 plates = 24 ingots for each emitter and each sensor. This is the biggest metal load of the era: with trinium at about 1 ingot per 6 naquadah dust (zpm_naq_products) one emitter is 144 naquadah dust. Run both naquadah chains hard before this one. Fine URD wire: wiremill on a URD ingot, 8 wire per ingot, 128 wire = 16 ingots.
    - |-
      Sub-steps people skip: (1) emitters go INTO field generators: make 2 per field generator on top of the 1 per sensor line; (2) catalyst stars are the standard ‘quantum_star’, not nether stars; (3) frames: osthendah frame = 2 osthendah ingots, assembler or hand; (4) soldering alloy 576 / 1152 mB: size the drum for 10 crafts; (5) station research needs the item you scan in the Object Holder; scanning the LuV emitter does not consume it (Unverified); (6) 4 VG cables each: make cables in 8-packs.
    - |-
      Unverified: the foil bender circuit number and yield, the frame recipe machine, and that the fusion casing uses the LuV (not ZPM) field generator exactly as listed (taken from start_fusion_machines.js fusionCasing: tierUnder field generator).
  b:
    - ["gtceu:assembly_line", 2]
    - ["gtceu:lv_bender", 2]
    - ["gtceu:lv_wiremill", 2]
    - ["gtceu:hv_chemical_bath", 1]
    - ["gtceu:luv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 30]
    - ["modularrouters:modular_router", 16]
    - ["gtceu:lv_robot_arm", 16]
    - ["gtceu:item_filter", 16]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:quantum_star", "gtceu:trinium_foil", "gtceu:osthendah_frame"]
      t: |-
        Drawers first, one per part: ZPM motors, pistons, circuits (ZPM, LuV, IV), long osthendah rods, plates, frames, gears, trinium foil (huge), fine URD wire, quantum stars (Keep Exact 4), VG cables. Drums: soldering alloy (576 / 1152 mB per craft), lubricant. Each Assembly Line input bus has its own drawer behind a router with an Item Filter.
    - i: ["gtceu:hv_chemical_bath", "gtceu:quantum_star", "minecraft:nether_star"]
      t: |-
        Quantum stars: HV Chemical Bath, 1 nether star + 1250 mB radon → 1 star in 96 s at 480 EU/t. Two stars per component, 6 per field generator; stars and nether stars each in their own drawer, never shared with other machines.
    - i: ["gtceu:assembly_line", "gtceu:osthendah_gear", "gtceu:zpm_robot_arm"]
      t: |-
        Robot arm (no station needed): buses: 4 long osthendah rods, gear, 3 small gears, 2 motors, piston, ZPM + 2 LuV + 4 IV circuits, 4 cables; 576 mB solder + 500 mB lubricant. 30 s. Scan stick: LuV robot arm.
    - i: ["gtceu:research_station", "gtceu:luv_emitter", "gtceu:data_orb"]
      t: |-
        Station research first (zpm_data): LuV emitter, sensor and field generator, one data ORB each, 4 CWU/t, 30 720 EU/t. Then the orbs go in the Assembly Line’s Data Access Hatch.
    - i: ["gtceu:assembly_line", "gtceu:zpm_emitter", "gtceu:zpm_sensor"]
      t: |-
        Emitter and sensor: osthendah frame + motor + 4 long rods (emitter) or 4 plates (sensor) + 2 quantum stars + 2 ZPM circuits + 96 trinium foil + 4 cables; 576 mB solder. 30 s each at 30 720 EU/t, one Assembly Line per product if you want them in parallel.
    - i: ["gtceu:assembly_line", "gtceu:fine_uranium_rhodium_dinaquadide_wire", "gtceu:zpm_field_generator"]
      t: |-
        Field generator: frame + 6 plates + 2 stars + 2 ZPM EMITTERS + 2 ZPM circuits + 128 fine URD wire + 4 cables; 1152 mB solder. 30 s. Feed the 2 emitters by a Robot Arm Keep Exact 2 from the emitter output drawer.
    - i: ["functionalstorage:oak_1", "gtceu:zpm_field_generator"]
      t: |-
        Easy to miss: build the emitter line before the field generator one, and the nether star loop before both. Counting stars, not shards: a field generator is 6 whole nether stars.
---
# ZPM components 2: robot arm (scanned), emitter, sensor, field generator (station research, 2 quantum stars each, trinium foil, URD wire)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_components2` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM hull, hatch and components](../../plan/p12.md#zpmmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (scan: LuV arm)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Arm: 4 long osthendah rod · gear · 3 small gear · 2 ZPM motor · ZPM piston · ZPM + 2 LuV + 4 IV circuit · 4 VG cable · 576 mB solder + 500 mB lubricant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Arm: 4 long osthendah rod · gear · 3 small gear · 2 ZPM motor · ZPM piston · ZPM + 2 LuV + 4 IV circuit · 4 VG cable · 576 mB solder + 500 mB lubricant</span><span class="gt-sub"><span>ZPM motor</span><span>ZPM piston</span><span>Osthendah gear</span><span>Small osthendah gear</span><span>Quantum processor mainframe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Robot Arm (gtceu:zpm_robot_arm) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_robot_arm.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Robot Arm</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (station: LuV emitter, 4 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Emitter: osthendah frame · ZPM motor · 4 long osthendah rod · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Emitter: osthendah frame · ZPM motor · 4 long osthendah rod · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder</span><span class="gt-sub"><span>Osthendah frame</span><span>Quantum star</span><span>Trinium foil</span><span>ZPM motor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Emitter (gtceu:zpm_emitter) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Emitter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (station: LuV sensor)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Sensor: osthendah frame · ZPM motor · 4 osthendah plate · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Sensor: osthendah frame · ZPM motor · 4 osthendah plate · 2 quantum star · 2 ZPM circuit · 96 trinium foil · 4 VG cable · 576 mB solder</span><span class="gt-sub"><span>Osthendah frame</span><span>Quantum star</span><span>Trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Sensor (gtceu:zpm_sensor) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_sensor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Sensor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Assembly Line · 30 s · 30 720 EU/t (station: LuV field generator)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ZPM Emitter (gtceu:zpm_emitter) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Emitter</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="Field generator: osthendah frame · 6 plate · 2 quantum star · 2 ZPM emitter · 2 ZPM circuit · 128 fine URD wire · 4 VG cable · 1152 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Field generator: osthendah frame · 6 plate · 2 quantum star · 2 ZPM emitter · 2 ZPM circuit · 128 fine URD wire · 4 VG cable · 1152 mB solder</span><span class="gt-sub"><span>Osthendah plate</span><span>Fine URD wire</span><span>Quantum star</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Field Generator (gtceu:zpm_field_generator) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_field_generator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Field Generator</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 30 s · 30 720 EU/t (scan: LuV arm)](#m-a1)
- [Assembly Line · 30 s · 30 720 EU/t (station: LuV emitter, 4 CWU/t)](#m-a2) → [Assembly Line · 30 s · 30 720 EU/t (station: LuV field generator)](#m-a4)
- [Assembly Line · 30 s · 30 720 EU/t (station: LuV sensor)](#m-a3)

## How to build

1. Drawers first, one per part: ZPM motors, pistons, circuits (ZPM, LuV, IV), long osthendah rods, plates, frames, gears, trinium foil (huge), fine URD wire, quantum stars (Keep Exact 4), VG cables. Drums: soldering alloy (576 / 1152 mB per craft), lubricant. Each Assembly Line input bus has its own drawer behind a router with an Item Filter. — `functionalstorage:oak_1`, `gtceu:quantum_star`, `gtceu:trinium_foil`, `gtceu:osthendah_frame`
2. Quantum stars: HV Chemical Bath, 1 nether star + 1250 mB radon → 1 star in 96 s at 480 EU/t. Two stars per component, 6 per field generator; stars and nether stars each in their own drawer, never shared with other machines. — `gtceu:hv_chemical_bath`, `gtceu:quantum_star`, `minecraft:nether_star`
3. Robot arm (no station needed): buses: 4 long osthendah rods, gear, 3 small gears, 2 motors, piston, ZPM + 2 LuV + 4 IV circuits, 4 cables; 576 mB solder + 500 mB lubricant. 30 s. Scan stick: LuV robot arm. — `gtceu:assembly_line`, `gtceu:osthendah_gear`, `gtceu:zpm_robot_arm`
4. Station research first (zpm\_data): LuV emitter, sensor and field generator, one data ORB each, 4 CWU/t, 30 720 EU/t. Then the orbs go in the Assembly Line’s Data Access Hatch. — `gtceu:research_station`, `gtceu:luv_emitter`, `gtceu:data_orb`
5. Emitter and sensor: osthendah frame + motor + 4 long rods (emitter) or 4 plates (sensor) + 2 quantum stars + 2 ZPM circuits + 96 trinium foil + 4 cables; 576 mB solder. 30 s each at 30 720 EU/t, one Assembly Line per product if you want them in parallel. — `gtceu:assembly_line`, `gtceu:zpm_emitter`, `gtceu:zpm_sensor`
6. Field generator: frame + 6 plates + 2 stars + 2 ZPM EMITTERS + 2 ZPM circuits + 128 fine URD wire + 4 cables; 1152 mB solder. 30 s. Feed the 2 emitters by a Robot Arm Keep Exact 2 from the emitter output drawer. — `gtceu:assembly_line`, `gtceu:fine_uranium_rhodium_dinaquadide_wire`, `gtceu:zpm_field_generator`
7. Easy to miss: build the emitter line before the field generator one, and the nether star loop before both. Counting stars, not shards: a field generator is 6 whole nether stars. — `functionalstorage:oak_1`, `gtceu:zpm_field_generator`

## Tips

- Recipes (utils/tier\_data.js zpm row + luv\_to\_uv\_components.js; all 600 ticks at 30 720 EU/t, scaler 2: solder x 4, quantum stars x 2). Robot arm: 4 long osthendah rods + 1 osthendah gear + 3 small osthendah gears + 2 ZPM motors + 1 ZPM piston + 1 ZPM circuit + 2 LuV circuits + 4 IV circuits + 4 VG single cables, 576 mB soldering alloy + 500 mB lubricant, SCANNER research of the LuV arm. Emitter: 1 osthendah frame + 1 ZPM motor + 4 long osthendah rods + 2 quantum stars + 2 ZPM circuits + 96 trinium foil (64 + 32) + 4 cables, 576 mB solder. Sensor: same with 4 osthendah plates instead of the rods. Field generator: 1 osthendah frame + 6 plates + 2 quantum stars + 2 ZPM emitters + 2 ZPM circuits + 128 fine URD wire (64 + 64) + 4 cables, 1152 mB solder. Emitter, sensor and field generator use STATION research of the LuV part: 4 CWU/t at 30 720 EU/t, so the Research Station and HPCA (zpm\_research) must stand first.
- Cost in rare inputs (verified counts): emitter and sensor 24 trinium ingots each (foil = 1/4 ingot, 4 foil per plate), 2 quantum stars, 2 ZPM circuits, 1 motor; field generator 16 URD ingots (128 fine wire), 2 stars, 2 circuits PLUS 2 emitters = 6 stars, 6 ZPM circuits, 48 trinium and 2 motors in total. Robot arm: 3 motors in total (2 + the piston’s) and 3 circuit tiers, no stars. A quantum star = 1 nether star + 1250 mB radon (HV Chemical Bath, 1920 ticks at 480 EU/t): 6 stars per field generator is 6 whole nether stars, 7.5 B of radon, and a nether star loop (nether\_star chain) that yields 1.19 stars per star: start it now.
- Circuits per arm: 1 ZPM + 2 LuV + 4 IV circuits (tag-based, any LuV or IV circuit works); the nano line gives LuV circuits (luv\_circuits) and the IV mainframes the IV ones. So the arm is the one ZPM component you can make as soon as the first ZPM circuit exists and the piston and motors are done; it does not need the Research Station.
- Where each goes: ZPM robot arm: Object Holder (2), ZPM buses and assemblers; ZPM emitter: ZPM sensors and field generators, the object holder (8 LuV emitters, not ZPM), the computation transmitter hatch (LuV emitter); ZPM sensor and field generator: ZPM machines, the fusion casing (the casing takes the LuV field generator below the tier: fusion MK II casing = ZPM hull + fusion coil + 2 ZPM voltage coils + 1 LuV field generator + 6 reflector panels), the HPCA advanced computation component (ZPM field generator + UV circuits, UV era).
- Foil: Bender, circuit 10 (Unverified, per the LuV chain’s rule): 1 trinium plate → 4 foil, so 96 foil = 24 plates = 24 ingots for each emitter and each sensor. This is the biggest metal load of the era: with trinium at about 1 ingot per 6 naquadah dust (zpm\_naq\_products) one emitter is 144 naquadah dust. Run both naquadah chains hard before this one. Fine URD wire: wiremill on a URD ingot, 8 wire per ingot, 128 wire = 16 ingots.
- Sub-steps people skip: (1) emitters go INTO field generators: make 2 per field generator on top of the 1 per sensor line; (2) catalyst stars are the standard ‘quantum\_star’, not nether stars; (3) frames: osthendah frame = 2 osthendah ingots, assembler or hand; (4) soldering alloy 576 / 1152 mB: size the drum for 10 crafts; (5) station research needs the item you scan in the Object Holder; scanning the LuV emitter does not consume it (Unverified); (6) 4 VG cables each: make cables in 8-packs.
- **Unverified** the foil bender circuit number and yield, the frame recipe machine, and that the fusion casing uses the LuV (not ZPM) field generator exactly as listed (taken from start\_fusion\_machines.js fusionCasing: tierUnder field generator).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 2 |
| `gtceu:lv_bender` | 2 |
| `gtceu:lv_wiremill` | 2 |
| `gtceu:hv_chemical_bath` | 1 |
| `gtceu:luv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 30 |
| `modularrouters:modular_router` | 16 |
| `gtceu:lv_robot_arm` | 16 |
| `gtceu:item_filter` | 16 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:zpm_robot_arm`, `gtceu:zpm_emitter`, `gtceu:zpm_sensor`, `gtceu:zpm_field_generator`
