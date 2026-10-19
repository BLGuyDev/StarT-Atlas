---
kind: chain
id: uv_hull
order: 1610
data:
  t: |-
    UV Machine Hull: darmstadtium casing + 2 yttrium barium cuprate cables (PPS foil + PVC foil + silicone) + 288 mB PEEK
  inf: true
  "n":
    - [ig, "Darmstadtium ingot (fusion fluid → solidifier)", i, "gtceu:darmstadtium_ingot"]
    - [be, "LV Bender · circuit 1", m, "gtceu:lv_bender"]
    - [pl, "8 Darmstadtium plate", x, "gtceu:darmstadtium_plate"]
    - [a1, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, UV Machine Casing, x, "gtceu:uv_machine_casing"]
    - [yw, "YBCO ingot → wiremill → single wire", x, "gtceu:yttrium_barium_cuprate_single_wire"]
    - - cw
      - |-
        1 YBCO single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber
      - g
      - functionalstorage:oak_1
      - - [YBCO single wire, "gtceu:yttrium_barium_cuprate_single_wire"]
        - [PPS foil, "gtceu:polyphenylene_sulfide_foil"]
        - [PVC foil, "gtceu:polyvinyl_chloride_foil"]
        - [Silicone rubber, "gtceu:silicone_rubber_bucket"]
    - [a2, "LV Assembler · 5 s · 8 EU/t (cable)", m, "gtceu:lv_assembler"]
    - [cb, "2 YBCO single cable", x, "gtceu:yttrium_barium_cuprate_single_cable"]
    - [pk, "288 mB PEEK (uv_peek)", f, "gtceu:polyether_ether_ketone_bucket"]
    - [a3, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, UV Machine Hull, o, "gtceu:uv_machine_hull"]
  e:
    - [ig, be, "8"]
    - [be, pl, "1 / ingot"]
    - [pl, a1, "8"]
    - [a1, mc, "1 / 2.5 s"]
    - [yw, cw, "1"]
    - [cw, a2, "2 crafts"]
    - [a2, cb, "2 / 5 s"]
    - [mc, a3, "1"]
    - [cb, a3, "2"]
    - [pk, a3, "288 mB"]
    - [a3, hu, "1 / 2.5 s"]
  tips:
    - |-
      Recipes. Casing (MachineRecipeLoader casing_uv): 8 darmstadtium plates, assembler circuit 8, 50 ticks at 16 EU/t (crafting-table alternative: 8 plates around a wrench). Hull: the pack replaces the GT hull for LuV, ZPM and UV (kjs additions/machines_and_parts/tiered_machines/singleblocks.js luvUVMachines): casing + 2 tier single cables + 288 mB of the TIER PLASTIC, assembler 50 ticks at 16 EU/t; shaped alternative: middle row PEEK plate, darmstadtium plate, PEEK plate; bottom row cable, casing, cable. For UV the cable is yttrium barium cuprate and the plastic is POLYETHER ETHER KETONE (pack tier data, uv), NOT PBI (the base GT recipe data still shows the PBI version, the pack removes it).
    - |-
      Cable (WireRecipeHandler): YBCO is above LuV so the single cable needs, in the assembler at 100 ticks and 8 EU/t, 1 single wire + 1 polyphenylene sulfide foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber). Two per hull. YBCO ingot: EBF 4500 K from the mixer dust (yttrium, barium, copper, oxygen); Unverified: the mixer recipe, the yttrium and barium sources (the abyss harvesting script also lists the ingot as an output: kjs systems/resource_gen/abyss_harvesting.js).
    - |-
      Darmstadtium: the fusion reactor MK II recipe (see zpm_fusion): 288 mB arsenic + 144 mB ruthenium → 144 mB darmstadtium in 28.8 s, then a fluid solidifier (ingot mold) and a bender. A casing is 8 plates = 8 ingots = 1152 mB; with the 2 YBCO cables and 288 mB PEEK a hull costs about 1152 mB darmstadtium. Each UV machine, hatch and the fusion reactor starts from one.
    - |-
      What the hull unlocks in this guide: UV energy input/dynamo hatch (uv_hatches), UV bus and hatch (UV I/O recipes use hull + enriched naquadah crate/drum + 324 mB PEEK), UV transformer (hull + 1 europium cable + 4 YBCO cables + 2 UHPIC chips), UV components (uv_components), UV circuit assembler and the UV research parts. UV voltage coils are in uv_hatches.
    - |-
      Sub-steps people skip: (1) bender plates on circuit 1, casing on circuit 8; (2) PPS foil is mandatory for the cable; (3) the UV hull uses PEEK, not PBI; the PEEK line (uv_peek) must exist first; (4) keep 6 casings spare for the UV fusion casings and the UV laser hatches.
    - |-
      Unverified: YBCO mixer recipe and the yttrium / barium sources.
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
        - gtceu:darmstadtium_ingot
        - gtceu:yttrium_barium_cuprate_single_wire
        - gtceu:polyphenylene_sulfide_foil
      t: |-
        Drawers first: darmstadtium ingots, YBCO single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PEEK. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode on the output.
    - i: ["gtceu:lv_bender", "gtceu:darmstadtium_plate"]
      t: |-
        LV Bender, circuit 1: 1 darmstadtium ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16.
    - i: ["gtceu:lv_assembler", "gtceu:uv_machine_casing"]
      t: |-
        LV Assembler, circuit 8: 8 plates → 1 UV Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer.
    - i: ["gtceu:lv_wiremill", "gtceu:yttrium_barium_cuprate_single_cable"]
      t: |-
        YBCO wire: a wiremill on the ingot, single wire, circuit 1. Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 YBCO single cable in 5 s at 8 EU/t. Two per hull.
    - i: ["gtceu:lv_assembler", "gtceu:polyether_ether_ketone_bucket", "gtceu:uv_machine_hull"]
      t: |-
        Hull assembler: casing + 2 YBCO cables + 288 mB PEEK → UV Machine Hull in 2.5 s at 16 EU/t. PEEK by a Pipez fluid pipe from its drum.
    - i: ["functionalstorage:oak_1", "gtceu:uv_machine_hull"]
      t: Output drawer Keep Exact 8. Hulls feed every UV hatch, bus, component machine and fusion casing.
---
# UV Machine Hull: darmstadtium casing + 2 yttrium barium cuprate cables (PPS foil + PVC foil + silicone) + 288 mB PEEK

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_hull` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV hull](../../plan/p14.md#uvhull)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Darmstadtium ingot (fusion fluid → solidifier) (gtceu:darmstadtium_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__darmstadtium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Darmstadtium Ingot</span><span class="gt-note">Darmstadtium ingot (fusion fluid → solidifier)</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Darmstadtium plate (gtceu:darmstadtium_plate) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__darmstadtium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Darmstadtium Plate</span><span class="gt-note">8 Darmstadtium plate</span><b class="gt-q">1 / ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Darmstadtium plate (gtceu:darmstadtium_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__darmstadtium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Darmstadtium Plate</span><span class="gt-note">8 Darmstadtium plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UV Machine Casing (gtceu:uv_machine_casing) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 8 EU/t (cable)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 YBCO single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (functionalstorage:oak_1) - 2 crafts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 YBCO single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber</span><span class="gt-sub"><span>YBCO single wire</span><span>PPS foil</span><span>PVC foil</span><span>Silicone rubber</span></span><b class="gt-q">2 crafts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 YBCO single cable (gtceu:yttrium_barium_cuprate_single_cable) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__yttrium_barium_cuprate_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Yttrium Barium Cuprate Single Cable</span><span class="gt-note">2 YBCO single cable</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UV Machine Casing (gtceu:uv_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 YBCO single cable (gtceu:yttrium_barium_cuprate_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__yttrium_barium_cuprate_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Yttrium Barium Cuprate Single Cable</span><span class="gt-note">2 YBCO single cable</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PEEK (uv_peek) (gtceu:polyether_ether_ketone_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polyether_ether_ketone_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyether Ether Ketone</span><span class="gt-note">288 mB PEEK (uv_peek)</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UV Machine Hull (gtceu:uv_machine_hull) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1](#m-be) → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a1) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)
- [LV Assembler · 5 s · 8 EU/t (cable)](#m-a2) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)

### Direct steps

- YBCO ingot → wiremill → single wire → 1 YBCO single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (1)

## How to build

1. Drawers first: darmstadtium ingots, YBCO single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PEEK. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode on the output. — `functionalstorage:oak_1`, `gtceu:darmstadtium_ingot`, `gtceu:yttrium_barium_cuprate_single_wire`, `gtceu:polyphenylene_sulfide_foil`
2. LV Bender, circuit 1: 1 darmstadtium ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16. — `gtceu:lv_bender`, `gtceu:darmstadtium_plate`
3. LV Assembler, circuit 8: 8 plates → 1 UV Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer. — `gtceu:lv_assembler`, `gtceu:uv_machine_casing`
4. YBCO wire: a wiremill on the ingot, single wire, circuit 1. Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 YBCO single cable in 5 s at 8 EU/t. Two per hull. — `gtceu:lv_wiremill`, `gtceu:yttrium_barium_cuprate_single_cable`
5. Hull assembler: casing + 2 YBCO cables + 288 mB PEEK → UV Machine Hull in 2.5 s at 16 EU/t. PEEK by a Pipez fluid pipe from its drum. — `gtceu:lv_assembler`, `gtceu:polyether_ether_ketone_bucket`, `gtceu:uv_machine_hull`
6. Output drawer Keep Exact 8. Hulls feed every UV hatch, bus, component machine and fusion casing. — `functionalstorage:oak_1`, `gtceu:uv_machine_hull`

## Tips

- Recipes. Casing (MachineRecipeLoader casing\_uv): 8 darmstadtium plates, assembler circuit 8, 50 ticks at 16 EU/t (crafting-table alternative: 8 plates around a wrench). Hull: the pack replaces the GT hull for LuV, ZPM and UV (kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js luvUVMachines): casing + 2 tier single cables + 288 mB of the TIER PLASTIC, assembler 50 ticks at 16 EU/t; shaped alternative: middle row PEEK plate, darmstadtium plate, PEEK plate; bottom row cable, casing, cable. For UV the cable is yttrium barium cuprate and the plastic is POLYETHER ETHER KETONE (pack tier data, uv), NOT PBI (the base GT recipe data still shows the PBI version, the pack removes it).
- Cable (WireRecipeHandler): YBCO is above LuV so the single cable needs, in the assembler at 100 ticks and 8 EU/t, 1 single wire + 1 polyphenylene sulfide foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber). Two per hull. YBCO ingot: EBF 4500 K from the mixer dust (yttrium, barium, copper, oxygen); Unverified: the mixer recipe, the yttrium and barium sources (the abyss harvesting script also lists the ingot as an output: kjs systems/resource\_gen/abyss\_harvesting.js).
- Darmstadtium: the fusion reactor MK II recipe (see zpm\_fusion): 288 mB arsenic + 144 mB ruthenium → 144 mB darmstadtium in 28.8 s, then a fluid solidifier (ingot mold) and a bender. A casing is 8 plates = 8 ingots = 1152 mB; with the 2 YBCO cables and 288 mB PEEK a hull costs about 1152 mB darmstadtium. Each UV machine, hatch and the fusion reactor starts from one.
- What the hull unlocks in this guide: UV energy input/dynamo hatch (uv\_hatches), UV bus and hatch (UV I/O recipes use hull + enriched naquadah crate/drum + 324 mB PEEK), UV transformer (hull + 1 europium cable + 4 YBCO cables + 2 UHPIC chips), UV components (uv\_components), UV circuit assembler and the UV research parts. UV voltage coils are in uv\_hatches.
- Sub-steps people skip: (1) bender plates on circuit 1, casing on circuit 8; (2) PPS foil is mandatory for the cable; (3) the UV hull uses PEEK, not PBI; the PEEK line (uv\_peek) must exist first; (4) keep 6 casings spare for the UV fusion casings and the UV laser hatches.
- **Unverified** YBCO mixer recipe and the yttrium / barium sources.

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

- **Needs:** [Fusion MK II (ZPM): URD superconducting coil → fusion coil, advanced reflector casing, then the reactor (needs 4 UV circuits) and darmstadtium](../zpm/zpm_fusion.md)
- **Main source for:** `gtceu:uv_machine_hull`, `gtceu:uv_machine_casing`, `gtceu:yttrium_barium_cuprate_single_cable`, `gtceu:yttrium_barium_cuprate_single_wire`, `gtceu:darmstadtium_plate`
