---
kind: chain
id: uhv_hull
order: 1770
data:
  t: |-
    UHV Machine Hull: neutronium casing + 2 europium cables (PPS foil + PVC foil + silicone) + 288 mB PEEK
  inf: true
  "n":
    - [ig, "Neutronium ingot (uv_fusion_mats)", i, "gtceu:neutronium_ingot"]
    - [be, "LV Bender · circuit 1", m, "gtceu:lv_bender"]
    - [pl, "8 Neutronium plate", x, "gtceu:neutronium_plate"]
    - [a1, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, UHV Machine Casing, x, "gtceu:uhv_machine_casing"]
    - [ew, "Europium ingot (fusion) → wiremill → single wire", x, "gtceu:europium_single_wire"]
    - - cw
      - |-
        1 europium single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber
      - g
      - functionalstorage:oak_1
      - - [Europium single wire, "gtceu:europium_single_wire"]
        - [PPS foil, "gtceu:polyphenylene_sulfide_foil"]
        - [PVC foil, "gtceu:polyvinyl_chloride_foil"]
        - [Silicone rubber, "gtceu:silicone_rubber_bucket"]
    - [a2, "LV Assembler · 5 s · 8 EU/t (cable)", m, "gtceu:lv_assembler"]
    - [cb, "2 europium single cable", x, "gtceu:europium_single_cable"]
    - [pk, "288 mB PEEK (uv_peek)", f, "gtceu:polyether_ether_ketone_bucket"]
    - [a3, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, UHV Machine Hull, o, "gtceu:uhv_machine_hull"]
  e:
    - [ig, be, "8"]
    - [be, pl, "1 / ingot"]
    - [pl, a1, "8"]
    - [a1, mc, "1 / 2.5 s"]
    - [ew, cw, "1"]
    - [cw, a2, "2 crafts"]
    - [a2, cb, "2 / 5 s"]
    - [mc, a3, "1"]
    - [cb, a3, "2"]
    - [pk, a3, "288 mB"]
    - [a3, hu, "1 / 2.5 s"]
  tips:
    - |-
      The pack removes EVERY GT recipe whose output or input is a UHV, UEV, UIV, UXV, OpV or MAX tier item (except the ultimate battery) and re-creates them in kjs additions/machines_and_parts/tiered_machines/singleblocks.js (postUVMachines). UHV casing: 8 neutronium plates (circuit 8 assembler, 50 ticks, 16 EU/t, or 8 plates + wrench). UHV hull: casing + 2 europium single cables + 288 mB PEEK, assembler 50 ticks at 16 EU/t; shaped alternative: middle row PEEK plate, neutronium plate, PEEK plate; bottom row cable, casing, cable. Plastic and cable come from tier_data.js (uhv: polyether ether ketone, europium).
    - |-
      Europium cable: europium is a V[UHV] cable in this pack (tier_data cable for uhv), so like every cable above LuV it needs the PPS foil + PVC foil + silicone wrap (WireRecipeHandler), 1 wire + 1 PPS foil + 1 PVC foil + 72 mB silicone rubber, 100 ticks at 8 EU/t. Europium: fusion (kjs fusion_scaling.js, tier 1 reflector: 144 mB neodymium + 3 B hydrogen → 144 mB europium, 24 576 EU/t, 28.8 s, 150 MEU) or the rare earth line (uv_rare_earth).
    - |-
      A UHV hull costs 8 neutronium ingots (1152 mB = 8 UV-reactor runs of 72 s: 9.6 reactor minutes), 2 europium ingots of cable wire and 288 mB PEEK. UHV machines in this pack are shaped crafts of the hull plus UHV circuits, UHV components and cables, so the hull is the unit you count (hatches, buses, fusion casings, the Compact Assembly Line and the Supreme Plasma Turbine start from it).
    - |-
      Sub-steps people skip: (1) neutronium is the scarce part: plan the UV reactor’s neutronium runs ahead; (2) bender plates on circuit 1, casing on circuit 8; (3) PPS foil is mandatory for the cable; (4) keep 6 hulls spare.
    - |-
      Unverified: nothing beyond the source of the europium ingots.
  b:
    - ["gtceu:lv_assembler", 3]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:neutronium_ingot
        - gtceu:europium_single_wire
        - gtceu:polyphenylene_sulfide_foil
      t: |-
        Drawers first: neutronium ingots, europium single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PEEK. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode.
    - i: ["gtceu:lv_bender", "gtceu:neutronium_plate"]
      t: |-
        LV Bender, circuit 1: 1 neutronium ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16.
    - i: ["gtceu:lv_assembler", "gtceu:uhv_machine_casing"]
      t: |-
        LV Assembler, circuit 8: 8 plates → 1 UHV Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer.
    - i: ["gtceu:lv_wiremill", "gtceu:europium_single_cable"]
      t: |-
        Europium wire: a wiremill on the ingot, single wire, circuit 1. Cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 cable in 5 s at 8 EU/t. Two per hull.
    - i: ["gtceu:lv_assembler", "gtceu:polyether_ether_ketone_bucket", "gtceu:uhv_machine_hull"]
      t: |-
        Hull assembler: casing + 2 cables + 288 mB PEEK → UHV Machine Hull in 2.5 s at 16 EU/t. PEEK by a Pipez fluid pipe.
    - i: ["functionalstorage:oak_1", "gtceu:uhv_machine_hull"]
      t: Output drawer Keep Exact 8.
---
# UHV Machine Hull: neutronium casing + 2 europium cables (PPS foil + PVC foil + silicone) + 288 mB PEEK

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_hull` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [UHV hull, parts, hatches and components](../../plan/p17.md#uhvmach)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Neutronium ingot (uv_fusion_mats) (gtceu:neutronium_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium Ingot</span><span class="gt-note">Neutronium ingot (uv_fusion_mats)</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Neutronium plate (gtceu:neutronium_plate) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium Plate</span><span class="gt-note">8 Neutronium plate</span><b class="gt-q">1 / ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Neutronium plate (gtceu:neutronium_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium Plate</span><span class="gt-note">8 Neutronium plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UHV Machine Casing (gtceu:uhv_machine_casing) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 8 EU/t (cable)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 europium single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (functionalstorage:oak_1) - 2 crafts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 europium single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber</span><span class="gt-sub"><span>Europium single wire</span><span>PPS foil</span><span>PVC foil</span><span>Silicone rubber</span></span><b class="gt-q">2 crafts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 europium single cable (gtceu:europium_single_cable) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__europium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Europium Single Cable</span><span class="gt-note">2 europium single cable</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UHV Machine Casing (gtceu:uhv_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 europium single cable (gtceu:europium_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__europium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Europium Single Cable</span><span class="gt-note">2 europium single cable</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PEEK (uv_peek) (gtceu:polyether_ether_ketone_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polyether_ether_ketone_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyether Ether Ketone</span><span class="gt-note">288 mB PEEK (uv_peek)</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UHV Machine Hull (gtceu:uhv_machine_hull) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uhv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UHV Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1](#m-be) → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a1) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)
- [LV Assembler · 5 s · 8 EU/t (cable)](#m-a2) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)

### Direct steps

- Europium ingot (fusion) → wiremill → single wire → 1 europium single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (1)

## How to build

1. Drawers first: neutronium ingots, europium single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PEEK. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:neutronium_ingot`, `gtceu:europium_single_wire`, `gtceu:polyphenylene_sulfide_foil`
2. LV Bender, circuit 1: 1 neutronium ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16. — `gtceu:lv_bender`, `gtceu:neutronium_plate`
3. LV Assembler, circuit 8: 8 plates → 1 UHV Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer. — `gtceu:lv_assembler`, `gtceu:uhv_machine_casing`
4. Europium wire: a wiremill on the ingot, single wire, circuit 1. Cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 cable in 5 s at 8 EU/t. Two per hull. — `gtceu:lv_wiremill`, `gtceu:europium_single_cable`
5. Hull assembler: casing + 2 cables + 288 mB PEEK → UHV Machine Hull in 2.5 s at 16 EU/t. PEEK by a Pipez fluid pipe. — `gtceu:lv_assembler`, `gtceu:polyether_ether_ketone_bucket`, `gtceu:uhv_machine_hull`
6. Output drawer Keep Exact 8. — `functionalstorage:oak_1`, `gtceu:uhv_machine_hull`

## Tips

- The pack removes EVERY GT recipe whose output or input is a UHV, UEV, UIV, UXV, OpV or MAX tier item (except the ultimate battery) and re-creates them in kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js (postUVMachines). UHV casing: 8 neutronium plates (circuit 8 assembler, 50 ticks, 16 EU/t, or 8 plates + wrench). UHV hull: casing + 2 europium single cables + 288 mB PEEK, assembler 50 ticks at 16 EU/t; shaped alternative: middle row PEEK plate, neutronium plate, PEEK plate; bottom row cable, casing, cable. Plastic and cable come from tier\_data.js (uhv: polyether ether ketone, europium).
- Europium cable: europium is a V\[UHV\] cable in this pack (tier\_data cable for uhv), so like every cable above LuV it needs the PPS foil + PVC foil + silicone wrap (WireRecipeHandler), 1 wire + 1 PPS foil + 1 PVC foil + 72 mB silicone rubber, 100 ticks at 8 EU/t. Europium: fusion (kjs fusion\_scaling.js, tier 1 reflector: 144 mB neodymium + 3 B hydrogen → 144 mB europium, 24 576 EU/t, 28.8 s, 150 MEU) or the rare earth line (uv\_rare\_earth).
- A UHV hull costs 8 neutronium ingots (1152 mB = 8 UV-reactor runs of 72 s: 9.6 reactor minutes), 2 europium ingots of cable wire and 288 mB PEEK. UHV machines in this pack are shaped crafts of the hull plus UHV circuits, UHV components and cables, so the hull is the unit you count (hatches, buses, fusion casings, the Compact Assembly Line and the Supreme Plasma Turbine start from it).
- Sub-steps people skip: (1) neutronium is the scarce part: plan the UV reactor’s neutronium runs ahead; (2) bender plates on circuit 1, casing on circuit 8; (3) PPS foil is mandatory for the cable; (4) keep 6 hulls spare.
- **Unverified** nothing beyond the source of the europium ingots.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 3 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [Fusion metals: lutetium → americium, gallium + radon → duranium → tritanium, then neutronium (americium + naquadria); everything but neutronium runs in the ZPM Fusion Reactor (MK II) with tier-2/3 reflectors, neutronium needs the UV reactor (MK III)](../uv/uv_fusion_mats.md)
- **Main source for:** `gtceu:uhv_machine_hull`, `gtceu:uhv_machine_casing`, `gtceu:europium_single_cable`, `gtceu:neutronium_plate`
