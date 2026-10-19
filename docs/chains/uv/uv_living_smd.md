---
kind: chain
id: uv_living_smd
order: 1560
data:
  t: |-
    Living SMDs (inductor, transistor, capacitor, resistor, diode): ZPM Assembler recipes, 16 or 32 per run - the UV computer and the UHV mainframe cannot be built without them
  inf: true
  "n":
    - - g1
      - Naquadah alloy ring · 4 fine naquadria wire · 1 ferrosilite dust · 144 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Naquadah alloy ring, "gtceu:naquadah_alloy_ring"]
        - [Fine naquadria wire, "gtceu:fine_naquadria_wire"]
        - [Ferrosilite dust, "gtceu:ferrosilite_dust"]
        - [Polyimide, "gtceu:polyimide_bucket"]
    - - g2
      - |-
        2 naquadah foil · 8 fine trinium wire · 1 pure netherite foil · 144 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Naquadah foil, "gtceu:naquadah_foil"]
        - [Fine trinium wire, "gtceu:fine_trinium_wire"]
        - [Pure netherite foil, "gtceu:pure_netherite_foil"]
    - - g3
      - |-
        2 polyimide foil · 2 trinaquadalloy foil · 1 nether star foil · 108 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Polyimide foil, "gtceu:polyimide_foil"]
        - [Trinaquadalloy foil, "gtceu:trinaquadalloy_foil"]
        - [Nether star foil, "gtceu:nether_star_foil"]
    - - g4
      - |-
        1 silicon carbide dust · 6 fine YBCO wire · 2 duranium foil · 144 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Silicon carbide dust, "gtceu:silicon_carbide_dust"]
        - [Fine YBCO wire, "gtceu:fine_yttrium_barium_cuprate_wire"]
        - [Duranium foil, "gtceu:duranium_foil"]
    - - g5
      - |-
        2 nickel zinc ferrite dust · 1 naquadah wafer · 6 fine ITBTC wire · 288 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Nickel zinc ferrite dust, "gtceu:nickel_zinc_ferrite_dust"]
        - [Naquadah wafer, "gtceu:naquadah_wafer"]
        - [Fine ITBTC wire, "gtceu:fine_indium_tin_barium_titanium_cuprate_wire"]
    - [a1, "ZPM Assembler · 12 s · 61 440 EU/t (inductor x16)", m, "gtceu:zpm_assembler"]
    - [a2, "ZPM Assembler · 12 s · 61 440 EU/t (transistor x16)", m, "gtceu:zpm_assembler"]
    - [a3, "ZPM Assembler · 12 s · 61 440 EU/t (capacitor x16)", m, "gtceu:zpm_assembler"]
    - [a4, "ZPM Assembler · 12 s · 61 440 EU/t (resistor x16)", m, "gtceu:zpm_assembler"]
    - [a5, "ZPM Assembler · 24 s · 61 440 EU/t (diode x32)", m, "gtceu:zpm_assembler"]
    - - out
      - Living SMDs
      - g
      - functionalstorage:oak_1
      - - [Living inductor, "kubejs:living_smd_inductor"]
        - [Living transistor, "kubejs:living_smd_transistor"]
        - [Living capacitor, "kubejs:living_smd_capacitor"]
        - [Living resistor, "kubejs:living_smd_resistor"]
        - [Living diode, "kubejs:living_smd_diode"]
  e:
    - [g1, a1, "1"]
    - [g2, a2, "1"]
    - [g3, a3, "1"]
    - [g4, a4, "1"]
    - [g5, a5, "1"]
    - [a1, out, "16 / 12 s"]
    - [a2, out, "16 / 12 s"]
    - [a3, out, "16 / 12 s"]
    - [a4, out, "16 / 12 s"]
    - [a5, out, "32 / 24 s"]
  tips:
    - |-
      Source: kjs additions/progression/circuitry/circuit_parts.js, livingSMD(): plain assembler recipes (no research, no cleanroom), 15 ticks per output item, EUtVHA(ZPM) = 61 440 EU/t, which is above the LuV limit of 32 768 EU/t, so the machine must be a ZPM Assembler (or a Large Assembler on ZPM hatches). Outputs 16 each (diode 32), duration 240 ticks (diode 480). Those recipes are cheap in time: 16 SMDs every 12 s per machine. The cost is the exotic inputs.
    - |-
      Who needs them (kjs circuits.js, verified): wetware processor 4 capacitors + 4 transistors; wetware processor assembly 3 inductors + 6 capacitors; wetware computer (UV circuit) 4 diodes; wetware mainframe (UHV circuit) 12 each of inductor, capacitor, diode, resistor, transistor; runic processor 8 capacitors + 8 transistors; runic assembly 6 inductors + 12 capacitors; runic computer 8 diodes; runic mainframe 24 each of five. The GT Java wetware processor and assembly recipes still exist and use ADVANCED SMDs instead (zpm_asmd), so for those two steps you can skip the living SMDs; the computer and the mainframe cannot.
    - |-
      Where each ingredient comes from (see the materials chains of this era): polyimide plastic and foil (polymer line), naquadria (zpm_naq_products), trinium, naquadah alloy, trinaquadalloy (zpm_alloys), pure netherite foil (the UV hull/component material, nether line), nether star foil (nether_stars.js), duranium foil, ferrosilite and nickel zinc ferrite dust, naquadah wafer, YBCO and ITBTC fine wire (superconductor wires). Unverified: the polyimide route and the ferrosilite / nickel zinc ferrite recipes.
    - |-
      Sub-steps people skip: (1) all five recipes take polyimide as a FLUID, 108 to 288 mB, from a drum; (2) the nether star foil comes from a nether star (one star per foil batch, check nether_stars.js), so start it early; (3) fine wires are fine wire spools from a wiremill, 2 per ingot-equivalent; (4) one dedicated ZPM assembler per SMD type (the five recipes share no inputs, so one machine cannot alternate between them without swapping drawers by hand); they idle when the output drawer is full.
    - |-
      Unverified: the exact quantity of living SMDs a full UHV mainframe needs through the whole chain (the table above multiplies per craft) and the polyimide / ferrosilite sources.
  b:
    - ["gtceu:zpm_assembler", 5]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 1]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:naquadah_alloy_ring", "gtceu:fine_trinium_wire", "gtceu:polyimide_foil"]
      t: |-
        Drawers first, one per solid input (14 of them, see the BOM). A drum of polyimide for the five assemblers. Each assembler gets a router (or Pipez item pipes + Item Filters) with its own drawers only: never feed two SMD types from one drawer.
    - i: ["gtceu:zpm_assembler", "kubejs:living_smd_inductor"]
      t: |-
        Inductor assembler: ring + 4 fine naquadria wire + 1 ferrosilite dust + 144 mB polyimide → 16 inductors in 12 s. Robot Arm cover Keep Exact 4 on the wire drawer.
    - i: ["gtceu:zpm_assembler", "kubejs:living_smd_transistor", "kubejs:living_smd_capacitor"]
      t: |-
        Transistor and capacitor assemblers: 2 naquadah foil + 8 fine trinium wire + 1 pure netherite foil, and 2 polyimide foil + 2 trinaquadalloy foil + 1 nether star foil. Foils are what gets short: keep their drawers topped up with Keep Exact 8.
    - i: ["gtceu:zpm_assembler", "kubejs:living_smd_resistor", "kubejs:living_smd_diode"]
      t: |-
        Resistor assembler (silicon carbide dust, 6 fine YBCO wire, 2 duranium foil) and the diode assembler (2 nickel zinc ferrite dust, a naquadah wafer, 6 fine ITBTC wire, 288 mB polyimide → 32 diodes in 24 s). Wafers: one per 32 diodes.
    - i: ["gtceu:zpm_energy_input_hatch_4a", "gtceu:zpm_assembler"]
      t: |-
        Power: five ZPM assemblers at 61 440 EU/t each = 307 200 EU/t if all run together; a single ZPM 4A hatch is 4 x 131 072 = 524 288 EU/t. Run them one at a time by price, or use one ZPM energy hatch (131 072 EU/t) per two machines.
    - i: ["functionalstorage:oak_1", "kubejs:living_smd_diode"]
      t: Output drawers Keep Exact 64 per SMD type, then routers to the circuit lines. A UHV mainframe needs 12 of each type per craft, a UV computer 4 diodes.
---
# Living SMDs (inductor, transistor, capacitor, resistor, diode): ZPM Assembler recipes, 16 or 32 per run - the UV computer and the UHV mainframe cannot be built without them

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_living_smd` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Wetware circuits (UV and UHV circuit)](../../plan/p14.md#wetware)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-a1">
<div class="gt-head"><span class="gt-mname">ZPM Assembler · 12 s · 61 440 EU/t (inductor x16)</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Naquadah alloy ring · 4 fine naquadria wire · 1 ferrosilite dust · 144 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Naquadah alloy ring · 4 fine naquadria wire · 1 ferrosilite dust · 144 mB polyimide</span><span class="gt-sub"><span>Naquadah alloy ring</span><span>Fine naquadria wire</span><span>Ferrosilite dust</span><span>Polyimide</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Living SMDs (functionalstorage:oak_1) - 16 / 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs</span><span class="gt-sub"><span>Living inductor</span><span>Living transistor</span><span>Living capacitor</span><span>Living resistor</span><span>Living diode</span></span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a2">
<div class="gt-head"><span class="gt-mname">ZPM Assembler · 12 s · 61 440 EU/t (transistor x16)</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 naquadah foil · 8 fine trinium wire · 1 pure netherite foil · 144 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 naquadah foil · 8 fine trinium wire · 1 pure netherite foil · 144 mB polyimide</span><span class="gt-sub"><span>Naquadah foil</span><span>Fine trinium wire</span><span>Pure netherite foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Living SMDs (functionalstorage:oak_1) - 16 / 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs</span><span class="gt-sub"><span>Living inductor</span><span>Living transistor</span><span>Living capacitor</span><span>Living resistor</span><span>Living diode</span></span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a3">
<div class="gt-head"><span class="gt-mname">ZPM Assembler · 12 s · 61 440 EU/t (capacitor x16)</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 polyimide foil · 2 trinaquadalloy foil · 1 nether star foil · 108 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 polyimide foil · 2 trinaquadalloy foil · 1 nether star foil · 108 mB polyimide</span><span class="gt-sub"><span>Polyimide foil</span><span>Trinaquadalloy foil</span><span>Nether star foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Living SMDs (functionalstorage:oak_1) - 16 / 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs</span><span class="gt-sub"><span>Living inductor</span><span>Living transistor</span><span>Living capacitor</span><span>Living resistor</span><span>Living diode</span></span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a4">
<div class="gt-head"><span class="gt-mname">ZPM Assembler · 12 s · 61 440 EU/t (resistor x16)</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 silicon carbide dust · 6 fine YBCO wire · 2 duranium foil · 144 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 silicon carbide dust · 6 fine YBCO wire · 2 duranium foil · 144 mB polyimide</span><span class="gt-sub"><span>Silicon carbide dust</span><span>Fine YBCO wire</span><span>Duranium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Living SMDs (functionalstorage:oak_1) - 16 / 12 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs</span><span class="gt-sub"><span>Living inductor</span><span>Living transistor</span><span>Living capacitor</span><span>Living resistor</span><span>Living diode</span></span><b class="gt-q">16</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
<div class="gt-panel t-zpm" id="m-a5">
<div class="gt-head"><span class="gt-mname">ZPM Assembler · 24 s · 61 440 EU/t (diode x32)</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 nickel zinc ferrite dust · 1 naquadah wafer · 6 fine ITBTC wire · 288 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 nickel zinc ferrite dust · 1 naquadah wafer · 6 fine ITBTC wire · 288 mB polyimide</span><span class="gt-sub"><span>Nickel zinc ferrite dust</span><span>Naquadah wafer</span><span>Fine ITBTC wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">24 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Living SMDs (functionalstorage:oak_1) - 32 / 24 s"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Living SMDs</span><span class="gt-sub"><span>Living inductor</span><span>Living transistor</span><span>Living capacitor</span><span>Living resistor</span><span>Living diode</span></span><b class="gt-q">32</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_assembler</code></div>
</div>
</div>

## Flow

- [ZPM Assembler · 12 s · 61 440 EU/t (inductor x16)](#m-a1)
- [ZPM Assembler · 12 s · 61 440 EU/t (transistor x16)](#m-a2)
- [ZPM Assembler · 12 s · 61 440 EU/t (capacitor x16)](#m-a3)
- [ZPM Assembler · 12 s · 61 440 EU/t (resistor x16)](#m-a4)
- [ZPM Assembler · 24 s · 61 440 EU/t (diode x32)](#m-a5)

## How to build

1. Drawers first, one per solid input (14 of them, see the BOM). A drum of polyimide for the five assemblers. Each assembler gets a router (or Pipez item pipes + Item Filters) with its own drawers only: never feed two SMD types from one drawer. — `functionalstorage:oak_1`, `gtceu:naquadah_alloy_ring`, `gtceu:fine_trinium_wire`, `gtceu:polyimide_foil`
2. Inductor assembler: ring + 4 fine naquadria wire + 1 ferrosilite dust + 144 mB polyimide → 16 inductors in 12 s. Robot Arm cover Keep Exact 4 on the wire drawer. — `gtceu:zpm_assembler`, `kubejs:living_smd_inductor`
3. Transistor and capacitor assemblers: 2 naquadah foil + 8 fine trinium wire + 1 pure netherite foil, and 2 polyimide foil + 2 trinaquadalloy foil + 1 nether star foil. Foils are what gets short: keep their drawers topped up with Keep Exact 8. — `gtceu:zpm_assembler`, `kubejs:living_smd_transistor`, `kubejs:living_smd_capacitor`
4. Resistor assembler (silicon carbide dust, 6 fine YBCO wire, 2 duranium foil) and the diode assembler (2 nickel zinc ferrite dust, a naquadah wafer, 6 fine ITBTC wire, 288 mB polyimide → 32 diodes in 24 s). Wafers: one per 32 diodes. — `gtceu:zpm_assembler`, `kubejs:living_smd_resistor`, `kubejs:living_smd_diode`
5. Power: five ZPM assemblers at 61 440 EU/t each = 307 200 EU/t if all run together; a single ZPM 4A hatch is 4 x 131 072 = 524 288 EU/t. Run them one at a time by price, or use one ZPM energy hatch (131 072 EU/t) per two machines. — `gtceu:zpm_energy_input_hatch_4a`, `gtceu:zpm_assembler`
6. Output drawers Keep Exact 64 per SMD type, then routers to the circuit lines. A UHV mainframe needs 12 of each type per craft, a UV computer 4 diodes. — `functionalstorage:oak_1`, `kubejs:living_smd_diode`

## Tips

- Source: kjs additions/progression/circuitry/circuit\_parts.js, livingSMD(): plain assembler recipes (no research, no cleanroom), 15 ticks per output item, EUtVHA(ZPM) = 61 440 EU/t, which is above the LuV limit of 32 768 EU/t, so the machine must be a ZPM Assembler (or a Large Assembler on ZPM hatches). Outputs 16 each (diode 32), duration 240 ticks (diode 480). Those recipes are cheap in time: 16 SMDs every 12 s per machine. The cost is the exotic inputs.
- Who needs them (kjs circuits.js, verified): wetware processor 4 capacitors + 4 transistors; wetware processor assembly 3 inductors + 6 capacitors; wetware computer (UV circuit) 4 diodes; wetware mainframe (UHV circuit) 12 each of inductor, capacitor, diode, resistor, transistor; runic processor 8 capacitors + 8 transistors; runic assembly 6 inductors + 12 capacitors; runic computer 8 diodes; runic mainframe 24 each of five. The GT Java wetware processor and assembly recipes still exist and use ADVANCED SMDs instead (zpm\_asmd), so for those two steps you can skip the living SMDs; the computer and the mainframe cannot.
- Where each ingredient comes from (see the materials chains of this era): polyimide plastic and foil (polymer line), naquadria (zpm\_naq\_products), trinium, naquadah alloy, trinaquadalloy (zpm\_alloys), pure netherite foil (the UV hull/component material, nether line), nether star foil (nether\_stars.js), duranium foil, ferrosilite and nickel zinc ferrite dust, naquadah wafer, YBCO and ITBTC fine wire (superconductor wires). Unverified: the polyimide route and the ferrosilite / nickel zinc ferrite recipes.
- Sub-steps people skip: (1) all five recipes take polyimide as a FLUID, 108 to 288 mB, from a drum; (2) the nether star foil comes from a nether star (one star per foil batch, check nether\_stars.js), so start it early; (3) fine wires are fine wire spools from a wiremill, 2 per ingot-equivalent; (4) one dedicated ZPM assembler per SMD type (the five recipes share no inputs, so one machine cannot alternate between them without swapping drawers by hand); they idle when the output drawer is full.
- **Unverified** the exact quantity of living SMDs a full UHV mainframe needs through the whole chain (the table above multiplies per craft) and the polyimide / ferrosilite sources.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:zpm_assembler` | 5 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 1 |

## Needs / Feeds

- **Main source for:** `kubejs:living_smd_inductor`, `kubejs:living_smd_transistor`, `kubejs:living_smd_capacitor`, `kubejs:living_smd_resistor`, `kubejs:living_smd_diode`
