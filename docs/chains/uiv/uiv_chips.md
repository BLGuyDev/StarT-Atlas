---
kind: chain
id: uiv_chips
order: 2180
data:
  t: |-
    UIPIC chip (UIV chip): UEPIC wafer + 7-input Draco Infusion with pure dragon breath → UIPIC wafer → 2 chips
  inf: true
  "n":
    - - g1
      - |-
        UIPIC wafer infusion: 1 uepic wafer · 1 draconyallium foil · 16 silicon carbide over bismuth tritelluride dust · 1 naquadah foil · 1 neutronium foil · 4 draconic stem cells · 1 vanadium gallium foil · 2 000 mB pure dragon breath
      - g
      - functionalstorage:oak_1
      - - [uepic wafer, "kubejs:uepic_wafer"]
        - [draconyallium foil, "gtceu:draconyallium_foil"]
        - [silicon carbide over bismuth tritelluride dust, "gtceu:silicon_carbide_over_bismuth_tritelluride_dust"]
        - [naquadah foil, "gtceu:naquadah_foil"]
        - [neutronium foil, "gtceu:neutronium_foil"]
        - [draconic stem cells, "kubejs:draconic_stem_cells"]
    - [di, "Draco Infusion · 3 min · 491 520 EU/t", m, "gtceu:draco_infusion"]
    - [uw, UIPIC wafer, x, "kubejs:uipic_wafer"]
    - [cu, "Cutter · sterile cleanroom · 45 s · 491 520 EU/t", m, "gtceu:uv_cutter"]
    - [ch, "2 UIPIC chip per wafer", o, "kubejs:uipic_chip"]
  e: [[g1, di, "1 set"], [di, uw, "1 / 180 s"], [uw, cu, "1"], [cu, ch, "2 / 45 s"]]
  tips:
    - |-
      Source: circuits.js (uipic_wafer, uipic_chip). uipic_wafer: draco_infusion recipe, 3600 ticks (3 min), VA[UV] = 491 520 EU/t: 1 UEPIC wafer + 1 draconyallium foil + 16 silicon carbide over bismuth tritelluride dust + 1 naquadah foil + 1 neutronium foil + 4 draconic stem cells + 1 vanadium gallium foil, 2000 mB pure dragon breath. uipic_chip: cutter, 1 wafer → 2 chips, 900 ticks, VA[UV], sterile cleanroom.
    - |-
      Uses of UIPIC chips: the UIV absolute parallel hatch (4), the Primordial Infusion (64) and the UIV fusion reactor (96 = 64 + 32). Everything else of this era still uses UEPIC chips (tier_data chip = kubejs:uepic): UIV transformers and energy hatches (2 each), Draco Infusion (64), Nyinsane Plasma Turbine (160), Abyssal Containment Room (224), draconic mainframe (2).
    - |-
      Pure dragon breath, vanadium gallium foil, naquadah foil, neutronium foil and the silicon carbide dust: sources Unverified (pure dragon breath is not produced by any recipe traced in this guide).
    - |-
      Sub-steps people skip: (1) the wafer needs a UEPIC wafer first (uev_chips): do not cut all of them into chips; (2) 4 stem cells per wafer from uiv_infusion; (3) this is the only recipe in this chain that needs the infusion; (4) the cutter is a UV machine in the sterile cleanroom.
    - |-
      Unverified: pure dragon breath source and the primordial infusion timing.
  b:
    - ["gtceu:draco_infusion", 1]
    - ["gtceu:uv_cutter", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:uepic_wafer", "kubejs:draconic_stem_cells"]
      t: |-
        Drawers first: UEPIC wafers (Keep Exact 4), 4 draconic stem cells per wafer, the five foils and the dust. Drum of pure dragon breath on a Pipez fluid pipe.
    - i: ["gtceu:draco_infusion", "kubejs:uipic_wafer"]
      t: |-
        Draco Infusion: the UEPIC wafer in the center slot and the six other inputs in the listed order; 3 minutes per wafer at 491 520 EU/t.
    - i: ["gtceu:uv_cutter", "kubejs:uipic_chip"]
      t: |-
        UV Cutter in the sterile cleanroom: 2 chips per wafer, 45 s. Output drawer Keep Exact 64.
    - i: ["functionalstorage:oak_1", "kubejs:uipic_chip"]
      t: Chip drawer feeds the parallel hatch and the reactor; check the recipes before cutting every wafer.
    - i: ["gtceu:pure_dragon_breath_bucket"]
      t: |-
        Count pure dragon breath before starting: 2000 mB per wafer = 1000 mB per chip.
---
# UIPIC chip (UIV chip): UEPIC wafer + 7-input Draco Infusion with pure dragon breath → UIPIC wafer → 2 chips

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_chips` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [Draco Infusion, UIPIC chip, UIV circuits](../../plan/p19.md#uivdraco)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-di">
<div class="gt-head"><span class="gt-mname">Draco Infusion · 3 min · 491 520 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UIPIC wafer infusion: 1 uepic wafer · 1 draconyallium foil · 16 silicon carbide over bismuth tritelluride dust · 1 naquadah foil · 1 neutronium foil · 4 draconic stem cells · 1 vanadium gallium foil · 2 000 mB pure dragon breath (functionalstorage:oak_1) - 1 set"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UIPIC wafer infusion: 1 uepic wafer · 1 draconyallium foil · 16 silicon carbide over bismuth tritelluride dust · 1 naquadah foil · 1 neutronium foil · 4 draconic stem cells · 1 vanadium gallium foil · 2 000 mB pure dragon breath</span><span class="gt-sub"><span>uepic wafer</span><span>draconyallium foil</span><span>silicon carbide over bismuth tritelluride dust</span><span>naquadah foil</span><span>neutronium foil</span><span>draconic stem cells</span></span><b class="gt-q">1 set</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__draco_infusion.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">180 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UIPIC wafer (kubejs:uipic_wafer) - 1 / 180 s"><img class="gt-ico" src="../../assets/icons/kubejs__uipic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uipic Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:draco_infusion</code></div>
</div>
<div class="gt-panel t-uv" id="m-cu">
<div class="gt-head"><span class="gt-mname">Cutter · sterile cleanroom · 45 s · 491 520 EU/t</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UIPIC wafer (kubejs:uipic_wafer) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__uipic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uipic Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 UIPIC chip per wafer (kubejs:uipic_chip) - 2 / 45 s"><img class="gt-ico" src="../../assets/icons/kubejs__uipic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Uipic Chip</span><span class="gt-note">2 UIPIC chip per wafer</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:uv_cutter</code></div>
</div>
</div>

## Flow

- [Draco Infusion · 3 min · 491 520 EU/t](#m-di) → [Cutter · sterile cleanroom · 45 s · 491 520 EU/t](#m-cu)

## How to build

1. Drawers first: UEPIC wafers (Keep Exact 4), 4 draconic stem cells per wafer, the five foils and the dust. Drum of pure dragon breath on a Pipez fluid pipe. — `functionalstorage:oak_1`, `kubejs:uepic_wafer`, `kubejs:draconic_stem_cells`
2. Draco Infusion: the UEPIC wafer in the center slot and the six other inputs in the listed order; 3 minutes per wafer at 491 520 EU/t. — `gtceu:draco_infusion`, `kubejs:uipic_wafer`
3. UV Cutter in the sterile cleanroom: 2 chips per wafer, 45 s. Output drawer Keep Exact 64. — `gtceu:uv_cutter`, `kubejs:uipic_chip`
4. Chip drawer feeds the parallel hatch and the reactor; check the recipes before cutting every wafer. — `functionalstorage:oak_1`, `kubejs:uipic_chip`
5. Count pure dragon breath before starting: 2000 mB per wafer = 1000 mB per chip. — `gtceu:pure_dragon_breath_bucket`

## Tips

- Source: circuits.js (uipic\_wafer, uipic\_chip). uipic\_wafer: draco\_infusion recipe, 3600 ticks (3 min), VA\[UV\] = 491 520 EU/t: 1 UEPIC wafer + 1 draconyallium foil + 16 silicon carbide over bismuth tritelluride dust + 1 naquadah foil + 1 neutronium foil + 4 draconic stem cells + 1 vanadium gallium foil, 2000 mB pure dragon breath. uipic\_chip: cutter, 1 wafer → 2 chips, 900 ticks, VA\[UV\], sterile cleanroom.
- Uses of UIPIC chips: the UIV absolute parallel hatch (4), the Primordial Infusion (64) and the UIV fusion reactor (96 = 64 + 32). Everything else of this era still uses UEPIC chips (tier\_data chip = kubejs:uepic): UIV transformers and energy hatches (2 each), Draco Infusion (64), Nyinsane Plasma Turbine (160), Abyssal Containment Room (224), draconic mainframe (2).
- Pure dragon breath, vanadium gallium foil, naquadah foil, neutronium foil and the silicon carbide dust: sources Unverified (pure dragon breath is not produced by any recipe traced in this guide).
- Sub-steps people skip: (1) the wafer needs a UEPIC wafer first (uev\_chips): do not cut all of them into chips; (2) 4 stem cells per wafer from uiv\_infusion; (3) this is the only recipe in this chain that needs the infusion; (4) the cutter is a UV machine in the sterile cleanroom.
- **Unverified** pure dragon breath source and the primordial infusion timing.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:draco_infusion` | 1 |
| `gtceu:uv_cutter` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `kubejs:uipic_chip`, `kubejs:uipic_wafer`
