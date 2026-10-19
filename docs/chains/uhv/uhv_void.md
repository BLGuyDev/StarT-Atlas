---
kind: chain
id: uhv_void
order: 1890
data:
  t: |-
    Void ingot: echo shard → echo fluid; neutronium ingot + echo fluid → raw void ingot → Heat Chamber → hot void ingot → vacuum freezer
  inf: true
  "n":
    - [es, "Echo shard (Deep Dark loot)", i, "minecraft:echo_shard"]
    - [ex, "Extractor · 250 s · 15 360 EU/t (LuV)", m, "gtceu:luv_extractor"]
    - [er, "144 mB echo fluid per shard", f, "gtceu:echo_r_bucket"]
    - [ni, "Neutronium ingot (uv_fusion_mats)", i, "gtceu:neutronium_ingot"]
    - [so, "Fluid Solidifier · 200 s · 15 360 EU/t · 144 mB echo fluid", m, "gtceu:luv_fluid_solidifier"]
    - [rv, Raw void ingot, x, "gtceu:raw_void_ingot"]
    - [hc, "Heat Chamber · 300 s · 15 360 EU/t", m, "gtceu:heat_chamber"]
    - [hv, Hot void ingot, x, "gtceu:hot_void_ingot"]
    - [vf, "Vacuum Freezer / Mega Vacuum Freezer", m, "gtceu:mega_vacuum_freezer"]
    - [vi, "Void ingot (plate, frame, dust)", o, "gtceu:void_ingot"]
    - - vd
      - |-
        Alt: void dust → Super Pressure Heat Chamber · 150 s · 15 360 EU/t
      - m
      - gtceu:super_pressure_heat_chamber
  e:
    - [es, ex, "1"]
    - [ex, er, "144 mB"]
    - [er, so, "144 mB"]
    - [ni, so, "1"]
    - [so, rv, "1 / 200 s"]
    - [rv, hc, "1"]
    - [hc, hv, "1 / 300 s"]
    - [hv, vf, "1"]
    - [vf, vi, "1"]
    - [vd, hv, alt]
  tips:
    - |-
      Source: kjs systems/gate_based/misc_materials.js (verified; the pack removes the GT hot void ingot recipe and adds its own): extractor, 1 echo shard → 144 mB echo fluid (echo_r), 5000 ticks at VHA[LuV] = 15 360 EU/t (250 s); fluid solidifier, 1 NEUTRONIUM INGOT + 144 mB echo fluid → 1 raw void ingot, 4000 ticks (200 s) at VHA[LuV]; heat chamber (ZPM-era multiblock), 1 raw void ingot → 1 hot void ingot, 6000 ticks (300 s) at VHA[LuV]; alternative: pressure heat chamber (the Super Pressure Heat Chamber), 1 void dust → 1 hot void ingot, 3000 ticks (150 s). Then the usual vacuum freezer cools it. Echo fluid also makes echo shard dust (chemical bath: silicon dioxide dust + 144 mB echo fluid → echo shard dust, 160 ticks at VA[ZPM]) for echo shard foil used by the shard-based components (bender 160 ticks at VA[LuV]; titan forge ream 816 ticks).
    - |-
      Why it matters: void plates / frames are the casing and wiring metal of the UHV page: the Super Pressure Heat Chamber needs a double void plate, the runic engraver and the Draco infusion multis use void frames, the Exotic Gas Siphon uses void. Each void ingot costs 1 neutronium ingot (about 72 s of UV-reactor time) + 1 echo shard (a Deep Dark loot item): echo shards are the limit, not machines.
    - |-
      Echo shards: only found in the Deep Dark (ancient cities); the pack does not add a recipe (Unverified, check EMI). Void dust, for the alternative route, is not made by any script of the pack that I found: Unverified.
    - |-
      Sub-steps people skip: (1) solidifier consumes the neutronium INGOT (not the fluid); (2) three long recipes: queue several machines (the Heat Chamber needs 5 min per ingot); (3) echo fluid is also used by the stargate recipes (7200 mB per ASG step), do not spend it all; (4) the hot ingot must go through a vacuum freezer or Mega Vacuum Freezer: Unverified freezer EU for void.
    - |-
      Unverified: echo shard supply, void dust supply, the freezer tier.
  b:
    - ["gtceu:luv_extractor", 1]
    - ["gtceu:luv_fluid_solidifier", 1]
    - ["gtceu:heat_chamber", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["functionalstorage:oak_1", 6]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 5]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "minecraft:echo_shard", "gtceu:neutronium_ingot"]
      t: |-
        Drawers first: echo shards (Keep Exact 1), neutronium ingots. Drum: echo fluid. Output drawer for void ingots.
    - i: ["gtceu:luv_extractor", "gtceu:echo_r_bucket"]
      t: |-
        Extractor: 1 shard → 144 mB echo fluid every 250 s: build 4 of them to match a solidifier.
    - i: ["gtceu:luv_fluid_solidifier", "gtceu:raw_void_ingot"]
      t: |-
        Solidifier: neutronium ingot by router (Keep Exact 1), echo fluid by Pipez fluid pipe; 200 s per raw ingot.
    - i: ["gtceu:heat_chamber", "gtceu:hot_void_ingot"]
      t: |-
        Heat Chamber: raw void ingot → hot ingot, 300 s at 15 360 EU/t; parallel Heat Chambers help.
    - i: ["gtceu:mega_vacuum_freezer", "gtceu:void_ingot"]
      t: |-
        Freeze: the Mega Vacuum Freezer; the ingot goes to the bender / pipe extruders.
    - i: ["functionalstorage:oak_1", "gtceu:void_ingot"]
      t: Output drawer Keep Exact 8.
---
# Void ingot: echo shard → echo fluid; neutronium ingot + echo fluid → raw void ingot → Heat Chamber → hot void ingot → vacuum freezer

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_void` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Zapolgium, superconductors, alloys, void ingot](../../plan/p17.md#uhvmetals)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-luv" id="m-ex">
<div class="gt-head"><span class="gt-mname">Extractor · 250 s · 15 360 EU/t (LuV)</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Echo shard (Deep Dark loot) (minecraft:echo_shard) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__echo_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Echo Shard</span><span class="gt-note">Echo shard (Deep Dark loot)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="144 mB echo fluid per shard (gtceu:echo_r_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__echo_r_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Echo R</span><span class="gt-note">144 mB echo fluid per shard</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_extractor</code></div>
</div>
<div class="gt-panel t-luv" id="m-so">
<div class="gt-head"><span class="gt-mname">Fluid Solidifier · 200 s · 15 360 EU/t · 144 mB echo fluid</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="144 mB echo fluid per shard (gtceu:echo_r_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__echo_r_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Echo R</span><span class="gt-note">144 mB echo fluid per shard</span><b class="gt-q">144 mB</b></span><span class="gt-slot" title="Neutronium ingot (uv_fusion_mats) (gtceu:neutronium_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium Ingot</span><span class="gt-note">Neutronium ingot (uv_fusion_mats)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_fluid_solidifier.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">200 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Raw void ingot (gtceu:raw_void_ingot) - 1 / 200 s"><img class="gt-ico" src="../../assets/icons/gtceu__raw_void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Void Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_fluid_solidifier</code></div>
</div>
<div class="gt-panel t-mod" id="m-hc">
<div class="gt-head"><span class="gt-mname">Heat Chamber · 300 s · 15 360 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Raw void ingot (gtceu:raw_void_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__raw_void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Void Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">300 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot void ingot (gtceu:hot_void_ingot) - 1 / 300 s"><img class="gt-ico" src="../../assets/icons/gtceu__hot_void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Void Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:heat_chamber</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer / Mega Vacuum Freezer</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot void ingot (gtceu:hot_void_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hot_void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Void Ingot</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mega_vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Void ingot (plate, frame, dust) (gtceu:void_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Void Ingot</span><span class="gt-note">Void ingot (plate, frame, dust)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mega_vacuum_freezer</code></div>
</div>
<div class="gt-panel t-mod" id="m-vd">
<div class="gt-head"><span class="gt-mname">Alt: void dust → Super Pressure Heat Chamber · 150 s · 15 360 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__super_pressure_heat_chamber.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot void ingot (gtceu:hot_void_ingot) - alt"><img class="gt-ico" src="../../assets/icons/gtceu__hot_void_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Void Ingot</span><b class="gt-q">alt</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:super_pressure_heat_chamber</code></div>
</div>
</div>

## Flow

- [Extractor · 250 s · 15 360 EU/t (LuV)](#m-ex) → [Fluid Solidifier · 200 s · 15 360 EU/t · 144 mB echo fluid](#m-so) → [Heat Chamber · 300 s · 15 360 EU/t](#m-hc) → [Vacuum Freezer / Mega Vacuum Freezer](#m-vf)
- [Alt: void dust → Super Pressure Heat Chamber · 150 s · 15 360 EU/t](#m-vd) → [Vacuum Freezer / Mega Vacuum Freezer](#m-vf)

## How to build

1. Drawers first: echo shards (Keep Exact 1), neutronium ingots. Drum: echo fluid. Output drawer for void ingots. — `functionalstorage:oak_1`, `minecraft:echo_shard`, `gtceu:neutronium_ingot`
2. Extractor: 1 shard → 144 mB echo fluid every 250 s: build 4 of them to match a solidifier. — `gtceu:luv_extractor`, `gtceu:echo_r_bucket`
3. Solidifier: neutronium ingot by router (Keep Exact 1), echo fluid by Pipez fluid pipe; 200 s per raw ingot. — `gtceu:luv_fluid_solidifier`, `gtceu:raw_void_ingot`
4. Heat Chamber: raw void ingot → hot ingot, 300 s at 15 360 EU/t; parallel Heat Chambers help. — `gtceu:heat_chamber`, `gtceu:hot_void_ingot`
5. Freeze: the Mega Vacuum Freezer; the ingot goes to the bender / pipe extruders. — `gtceu:mega_vacuum_freezer`, `gtceu:void_ingot`
6. Output drawer Keep Exact 8. — `functionalstorage:oak_1`, `gtceu:void_ingot`

## Tips

- Source: kjs systems/gate\_based/misc\_materials.js (verified; the pack removes the GT hot void ingot recipe and adds its own): extractor, 1 echo shard → 144 mB echo fluid (echo\_r), 5000 ticks at VHA\[LuV\] = 15 360 EU/t (250 s); fluid solidifier, 1 NEUTRONIUM INGOT + 144 mB echo fluid → 1 raw void ingot, 4000 ticks (200 s) at VHA\[LuV\]; heat chamber (ZPM-era multiblock), 1 raw void ingot → 1 hot void ingot, 6000 ticks (300 s) at VHA\[LuV\]; alternative: pressure heat chamber (the Super Pressure Heat Chamber), 1 void dust → 1 hot void ingot, 3000 ticks (150 s). Then the usual vacuum freezer cools it. Echo fluid also makes echo shard dust (chemical bath: silicon dioxide dust + 144 mB echo fluid → echo shard dust, 160 ticks at VA\[ZPM\]) for echo shard foil used by the shard-based components (bender 160 ticks at VA\[LuV\]; titan forge ream 816 ticks).
- Why it matters: void plates / frames are the casing and wiring metal of the UHV page: the Super Pressure Heat Chamber needs a double void plate, the runic engraver and the Draco infusion multis use void frames, the Exotic Gas Siphon uses void. Each void ingot costs 1 neutronium ingot (about 72 s of UV-reactor time) + 1 echo shard (a Deep Dark loot item): echo shards are the limit, not machines.
- Echo shards: only found in the Deep Dark (ancient cities); the pack does not add a recipe (Unverified, check EMI). Void dust, for the alternative route, is not made by any script of the pack that I found: Unverified.
- Sub-steps people skip: (1) solidifier consumes the neutronium INGOT (not the fluid); (2) three long recipes: queue several machines (the Heat Chamber needs 5 min per ingot); (3) echo fluid is also used by the stargate recipes (7200 mB per ASG step), do not spend it all; (4) the hot ingot must go through a vacuum freezer or Mega Vacuum Freezer: Unverified freezer EU for void.
- **Unverified** echo shard supply, void dust supply, the freezer tier.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:luv_extractor` | 1 |
| `gtceu:luv_fluid_solidifier` | 1 |
| `gtceu:heat_chamber` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `functionalstorage:oak_1` | 6 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 5 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Needs:** [Fusion metals: lutetium → americium, gallium + radon → duranium → tritanium, then neutronium (americium + naquadria); everything but neutronium runs in the ZPM Fusion Reactor (MK II) with tier-2/3 reflectors, neutronium needs the UV reactor (MK III)](../uv/uv_fusion_mats.md)
- **Main source for:** `gtceu:void_ingot`, `gtceu:raw_void_ingot`, `gtceu:hot_void_ingot`, `gtceu:echo_r_bucket`, `gtceu:void_plate`
