---
kind: chain
id: uev_chips
order: 1980
data:
  t: |-
    UEPIC chip (UEV chip): UHPIC wafer + silicon carbide over bismuth tritelluride + 576 mB neutronium → wafer → 2 chips
  inf: true
  "n":
    - - g1
      - UHPIC wafer · 4 silicon carbide over bismuth tritelluride dust
      - g
      - functionalstorage:oak_1
      - - [UHPIC wafer, "gtceu:uhpic_wafer"]
        - [SiC over bismuth tritelluride dust, "gtceu:silicon_carbide_over_bismuth_tritelluride_dust"]
    - [nm, "576 mB molten neutronium", f, "gtceu:neutronium_bucket"]
    - [cr, "Chemical Reactor · cleanroom · 60 s · 122 880 EU/t", m, "gtceu:zpm_chemical_reactor"]
    - [uw, UEPIC wafer, x, "kubejs:uepic_wafer"]
    - [cu, "Cutter · sterile cleanroom · 45 s · 122 880 EU/t", m, "gtceu:zpm_cutter"]
    - [ch, "2 UEPIC chip per wafer", o, "kubejs:uepic_chip"]
  e: [[g1, cr, "1 + 4"], [nm, cr, "576 mB"], [cr, uw, "1 / 60 s"], [uw, cu, "1"], [cu, ch, "2 / 45 s"]]
  tips:
    - |-
      Source: circuits.js. uepic_wafer: chemical reactor, 1 UHPIC wafer + 4 silicon carbide over bismuth tritelluride dust + 576 mB neutronium, 1200 ticks (60 s), VA[ZPM] = 122 880 EU/t, plain cleanroom. uepic_chip: cutter, 1 wafer → 2 chips, 900 ticks (45 s), 122 880 EU/t, STERILE cleanroom.
    - The UEPIC chip is the chip of the UEV and UIV tiers (tier_data.js chip = kubejs:uepic). It goes into the UEV and UIV energy hatches (2 each), transformers (2 per transformer), parallel hatches (4 per absolute parallel hatch), the Super Compact Heat Chamber (160!), the Omega Pressure Heat Chamber (288) and the draconic and abyssal mainframes (2 and 4 per mainframe). The UIV absolute parallel hatch uses the UIPIC chip instead (uiv_circuits).
    - |-
      UEPIC chips are asked for from the UHV era on (verified): AUX I 96, Folding Akreyrium Stabiliser 48, Bulk Ore Processing Array 64, Exotic Gas Siphon 64, Manifold Centrifuge 96, Injection Mixer 64, and 64 per ASG computational matrix. Start this chip line when you start the runic mainframe, not at the UEV hull.
    - The UHPIC wafer is the UV/UHV wafer from earlier pages; the dust source (silicon carbide over bismuth tritelluride) is Unverified here. Because every chip needs 1 neutronium dust-worth of fluid per 2 chips (576 mB per wafer), neutronium output limits how many hatches and heat chambers you can make; plan 160 chips = 80 wafers = 46 B neutronium for the Super Compact Heat Chamber alone.
    - |-
      Sub-steps people skip: (1) the cutter needs the STERILE cleanroom, not the plain one; (2) keep the wafers in their own drawer so a stalled cutter does not stop the reactor; (3) the reactor is a ZPM machine but needs a plain cleanroom: place it inside the cleanroom with its own energy hatch; (4) chips are the cap on how many UEV energy hatches you can queue.
    - |-
      Unverified: the bismuth tritelluride dust source and the neutronium supply.
  b:
    - ["gtceu:zpm_chemical_reactor", 1]
    - ["gtceu:zpm_cutter", 1]
    - ["functionalstorage:oak_1", 6]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uhpic_wafer", "gtceu:silicon_carbide_over_bismuth_tritelluride_dust"]
      t: |-
        Drawers first: UHPIC wafers (Keep Exact 8), the dust (Keep Exact 32). Drum of molten neutronium on a Pipez fluid pipe with a pump cover.
    - i: ["gtceu:zpm_chemical_reactor", "kubejs:uepic_wafer"]
      t: |-
        ZPM Chemical Reactor in the cleanroom: wafer + 4 dust + 576 mB neutronium → 1 UEPIC wafer per 60 s at 122 880 EU/t. Dedicated reactor for this product only.
    - i: ["gtceu:zpm_cutter", "kubejs:uepic_chip"]
      t: |-
        ZPM Cutter in the sterile cleanroom behind a router with an Item Filter: wafer → 2 chips in 45 s at 122 880 EU/t.
    - i: ["functionalstorage:oak_1", "kubejs:uepic_chip"]
      t: Chip drawer with Keep Exact 64; every UEV hatch and heat chamber pulls from it.
    - i: ["gtceu:neutronium_bucket"]
      t: |-
        Count the neutronium before you start the heat chambers: 80 wafers need 46 080 mB.
---
# UEPIC chip (UEV chip): UHPIC wafer + silicon carbide over bismuth tritelluride + 576 mB neutronium → wafer → 2 chips

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_chips` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEPIC chip and UEV circuit](../../plan/p17.md#uevcirc)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-cr">
<div class="gt-head"><span class="gt-mname">Chemical Reactor · cleanroom · 60 s · 122 880 EU/t</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHPIC wafer · 4 silicon carbide over bismuth tritelluride dust (functionalstorage:oak_1) - 1 + 4"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHPIC wafer · 4 silicon carbide over bismuth tritelluride dust</span><span class="gt-sub"><span>UHPIC wafer</span><span>SiC over bismuth tritelluride dust</span></span><b class="gt-q">1 + 4</b></span><span class="gt-slot gt-fluid" title="576 mB molten neutronium (gtceu:neutronium_bucket) - 576 mB"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium</span><span class="gt-note">576 mB molten neutronium</span><b class="gt-q">576 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEPIC wafer (kubejs:uepic_wafer) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/kubejs__uepic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEPIC Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_chemical_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-cu">
<div class="gt-head"><span class="gt-mname">Cutter · sterile cleanroom · 45 s · 122 880 EU/t</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UEPIC wafer (kubejs:uepic_wafer) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__uepic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEPIC Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="2 UEPIC chip per wafer (kubejs:uepic_chip) - 2 / 45 s"><img class="gt-ico" src="../../assets/icons/kubejs__uepic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEPIC Chip</span><span class="gt-note">2 UEPIC chip per wafer</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_cutter</code></div>
</div>
</div>

## Flow

- [Chemical Reactor · cleanroom · 60 s · 122 880 EU/t](#m-cr) → [Cutter · sterile cleanroom · 45 s · 122 880 EU/t](#m-cu)

## How to build

1. Drawers first: UHPIC wafers (Keep Exact 8), the dust (Keep Exact 32). Drum of molten neutronium on a Pipez fluid pipe with a pump cover. — `functionalstorage:oak_1`, `gtceu:uhpic_wafer`, `gtceu:silicon_carbide_over_bismuth_tritelluride_dust`
2. ZPM Chemical Reactor in the cleanroom: wafer + 4 dust + 576 mB neutronium → 1 UEPIC wafer per 60 s at 122 880 EU/t. Dedicated reactor for this product only. — `gtceu:zpm_chemical_reactor`, `kubejs:uepic_wafer`
3. ZPM Cutter in the sterile cleanroom behind a router with an Item Filter: wafer → 2 chips in 45 s at 122 880 EU/t. — `gtceu:zpm_cutter`, `kubejs:uepic_chip`
4. Chip drawer with Keep Exact 64; every UEV hatch and heat chamber pulls from it. — `functionalstorage:oak_1`, `kubejs:uepic_chip`
5. Count the neutronium before you start the heat chambers: 80 wafers need 46 080 mB. — `gtceu:neutronium_bucket`

## Tips

- Source: circuits.js. uepic\_wafer: chemical reactor, 1 UHPIC wafer + 4 silicon carbide over bismuth tritelluride dust + 576 mB neutronium, 1200 ticks (60 s), VA\[ZPM\] = 122 880 EU/t, plain cleanroom. uepic\_chip: cutter, 1 wafer → 2 chips, 900 ticks (45 s), 122 880 EU/t, STERILE cleanroom.
- The UEPIC chip is the chip of the UEV and UIV tiers (tier\_data.js chip = kubejs:uepic). It goes into the UEV and UIV energy hatches (2 each), transformers (2 per transformer), parallel hatches (4 per absolute parallel hatch), the Super Compact Heat Chamber (160!), the Omega Pressure Heat Chamber (288) and the draconic and abyssal mainframes (2 and 4 per mainframe). The UIV absolute parallel hatch uses the UIPIC chip instead (uiv\_circuits).
- UEPIC chips are asked for from the UHV era on (verified): AUX I 96, Folding Akreyrium Stabiliser 48, Bulk Ore Processing Array 64, Exotic Gas Siphon 64, Manifold Centrifuge 96, Injection Mixer 64, and 64 per ASG computational matrix. Start this chip line when you start the runic mainframe, not at the UEV hull.
- The UHPIC wafer is the UV/UHV wafer from earlier pages; the dust source (silicon carbide over bismuth tritelluride) is Unverified here. Because every chip needs 1 neutronium dust-worth of fluid per 2 chips (576 mB per wafer), neutronium output limits how many hatches and heat chambers you can make; plan 160 chips = 80 wafers = 46 B neutronium for the Super Compact Heat Chamber alone.
- Sub-steps people skip: (1) the cutter needs the STERILE cleanroom, not the plain one; (2) keep the wafers in their own drawer so a stalled cutter does not stop the reactor; (3) the reactor is a ZPM machine but needs a plain cleanroom: place it inside the cleanroom with its own energy hatch; (4) chips are the cap on how many UEV energy hatches you can queue.
- **Unverified** the bismuth tritelluride dust source and the neutronium supply.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:zpm_chemical_reactor` | 1 |
| `gtceu:zpm_cutter` | 1 |
| `functionalstorage:oak_1` | 6 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `kubejs:uepic_wafer`
