---
kind: chain
id: zpm_hull
order: 1430
data:
  t: |-
    ZPM Machine Hull: naquadah alloy casing + 2 vanadium gallium cables (PPS foil + PVC foil + silicone rubber) + 288 mB PBI
  inf: true
  "n":
    - [ig, Naquadah alloy ingot, i, "gtceu:naquadah_alloy_ingot"]
    - [be, "LV Bender · circuit 1", m, "gtceu:lv_bender"]
    - [pl, "8 Naquadah alloy plate", x, "gtceu:naquadah_alloy_plate"]
    - [a1, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, ZPM Machine Casing, x, "gtceu:zpm_machine_casing"]
    - - vg
      - Vanadium gallium ingot (EV Mixer circuit 1 + EBF 4500 K) → single wire
      - x
      - gtceu:vanadium_gallium_single_wire
    - - cw
      - |-
        1 VG single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber
      - g
      - functionalstorage:oak_1
      - - [VG single wire, "gtceu:vanadium_gallium_single_wire"]
        - [PPS foil, "gtceu:polyphenylene_sulfide_foil"]
        - [PVC foil, "gtceu:polyvinyl_chloride_foil"]
        - [Silicone rubber, "gtceu:silicone_rubber_bucket"]
    - [a2, "LV Assembler · 5 s · 8 EU/t (cable)", m, "gtceu:lv_assembler"]
    - [cb, "2 VG single cable", x, "gtceu:vanadium_gallium_single_cable"]
    - [pb, "288 mB PBI (zpm_pbi)", f, "gtceu:polybenzimidazole_bucket"]
    - [a3, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, ZPM Machine Hull, o, "gtceu:zpm_machine_hull"]
  e:
    - [ig, be, "8"]
    - [be, pl, "1 / ingot"]
    - [pl, a1, "8"]
    - [a1, mc, "1 / 2.5 s"]
    - [vg, cw, "1"]
    - [cw, a2, "2 crafts"]
    - [a2, cb, "2 / 5 s"]
    - [mc, a3, "1"]
    - [cb, a3, "2"]
    - [pb, a3, "288 mB"]
    - [a3, hu, "1 / 2.5 s"]
  tips:
    - |-
      Recipes. Casing: 8 naquadah alloy plates, assembler, circuit 8, 50 ticks at 16 EU/t (MachineRecipeLoader casing_zpm; crafting-table version 8 plates around a wrench). Hull: the PACK replaces the GT hull for LuV, ZPM and UV (kjs additions/machines_and_parts/tiered_machines/singleblocks.js, luvUVMachines): casing + 2 tier single cables + 288 mB of the tier plastic, assembler 50 ticks at 16 EU/t, and a crafting-table alternative (middle row: PBI plate, naquadah alloy plate, PBI plate; bottom row: cable, casing, cable). For ZPM: casing + 2 vanadium gallium single cables + 288 mB polybenzimidazole. Vanilla GT (hull_zpm) is the same with PBI as well; the LuV hull is the one that differs (see zpm_pbi).
    - |-
      Cable (WireRecipeHandler): vanadium gallium is a ZPM-rated cable (V[ZPM]), so like the LuV cable it needs, in the assembler at 100 ticks and 8 EU/t: 1 single wire + 1 polyphenylene sulfide foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber). Two cables per hull. The ZPM energy hatch uses 4 more VG single cables (energy_hatch_zpm) and the pack’s ZPM 4A hatch 2 VG quadruple wires. Vanadium gallium dust (MixerRecipes): 3 vanadium + 1 gallium dust → 4 dust, circuit 1, 400 ticks at 1920 EU/t (EV Mixer); EBF 4500 K (RTM coils), 1920 EU/t, 1200 ticks (60 s), freezer VA[HV]. Vanadium and gallium sources: Unverified (check EMI).
    - |-
      The pack also keeps the plastic in tier_data.js: ZPM plastic = polybenzimidazole, cable = vanadium gallium, tier material naquadah alloy, glass = fusion glass. Hull cost: 8 naquadah alloy ingots (4 naquadah dust, 2 osmiridium, 2 trinium dust), 2 VG wire (about 1 ingot), 2 PPS and 2 PVC foils, 144 mB silicone, 288 mB PBI. The hull is the starting item for every ZPM machine and hatch, so the cost per hull is mostly trinium and naquadah.
    - |-
      What the hull unlocks in this guide: ZPM energy hatch (zpm_hatches), ZPM input/output buses, ZPM assembler and other ZPM machines, the research parts (zpm_research), the fusion casings (zpm_fusion), the rotor holder. 4A and 16A hatches use the transformers: the pack’s ZPM transformer = ZPM hull + 1 yttrium barium cuprate cable + 4 vanadium gallium cables + 2 UHPIC chips (transformers.js).
    - |-
      Sub-steps people skip: (1) bender plates on circuit 1, casing on circuit 8; (2) PPS foil is mandatory for the cable: keep its drawer even though you made it for the LuV cables; (3) the cable is a 100 tick recipe, make 4 at a time with Keep Exact 4; (4) keep 3 casings spare, the ZPM fusion casings need hulls too; (5) PBI hull recipe bypasses PTFE entirely.
    - "Unverified: the exact vanadium and gallium sources."
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
        - gtceu:naquadah_alloy_ingot
        - gtceu:vanadium_gallium_single_wire
        - gtceu:polyphenylene_sulfide_foil
      t: |-
        Drawers first: naquadah alloy ingots, VG single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PBI. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode.
    - i: ["gtceu:lv_bender", "gtceu:naquadah_alloy_plate"]
      t: |-
        LV Bender, circuit 1: 1 naquadah alloy ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16.
    - i: ["gtceu:lv_assembler", "gtceu:zpm_machine_casing"]
      t: |-
        LV Assembler, circuit 8: 8 plates → 1 ZPM Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer.
    - i: ["gtceu:lv_wiremill", "gtceu:vanadium_gallium_single_wire"]
      t: |-
        VG wire: a wiremill on the vanadium gallium ingot, single wire, circuit 1. Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 VG single cable in 5 s at 8 EU/t. Two per hull.
    - i: ["gtceu:lv_assembler", "gtceu:polybenzimidazole_bucket", "gtceu:zpm_machine_hull"]
      t: |-
        Hull assembler: casing + 2 VG cables + 288 mB PBI → ZPM Machine Hull in 2.5 s at 16 EU/t. PBI by a Pipez fluid pipe from its drum, casing and cables by one router each.
    - i: ["functionalstorage:oak_1", "gtceu:zpm_machine_hull"]
      t: Output drawer Keep Exact 8. Hulls are what every ZPM hatch, bus, component machine and fusion casing starts from.
---
# ZPM Machine Hull: naquadah alloy casing + 2 vanadium gallium cables (PPS foil + PVC foil + silicone rubber) + 288 mB PBI

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_hull` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM hull, hatch and components](../../plan/p12.md#zpmmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Naquadah alloy ingot (gtceu:naquadah_alloy_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Ingot</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Naquadah alloy plate (gtceu:naquadah_alloy_plate) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Plate</span><span class="gt-note">8 Naquadah alloy plate</span><b class="gt-q">1 / ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Naquadah alloy plate (gtceu:naquadah_alloy_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_alloy_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Alloy Plate</span><span class="gt-note">8 Naquadah alloy plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Machine Casing (gtceu:zpm_machine_casing) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 8 EU/t (cable)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 VG single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (functionalstorage:oak_1) - 2 crafts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 VG single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber</span><span class="gt-sub"><span>VG single wire</span><span>PPS foil</span><span>PVC foil</span><span>Silicone rubber</span></span><b class="gt-q">2 crafts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 VG single cable (gtceu:vanadium_gallium_single_cable) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_gallium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Gallium Single Cable</span><span class="gt-note">2 VG single cable</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="ZPM Machine Casing (gtceu:zpm_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 VG single cable (gtceu:vanadium_gallium_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_gallium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Gallium Single Cable</span><span class="gt-note">2 VG single cable</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PBI (zpm_pbi) (gtceu:polybenzimidazole_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">288 mB PBI (zpm_pbi)</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="ZPM Machine Hull (gtceu:zpm_machine_hull) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1](#m-be) → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a1) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)
- [LV Assembler · 5 s · 8 EU/t (cable)](#m-a2) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)

### Direct steps

- Vanadium gallium ingot (EV Mixer circuit 1 + EBF 4500 K) → single wire → 1 VG single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (1)

## How to build

1. Drawers first: naquadah alloy ingots, VG single wire, PPS foil, PVC foil. Drums: silicone rubber (or SBR) and PBI. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:naquadah_alloy_ingot`, `gtceu:vanadium_gallium_single_wire`, `gtceu:polyphenylene_sulfide_foil`
2. LV Bender, circuit 1: 1 naquadah alloy ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16. — `gtceu:lv_bender`, `gtceu:naquadah_alloy_plate`
3. LV Assembler, circuit 8: 8 plates → 1 ZPM Machine Casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer. — `gtceu:lv_assembler`, `gtceu:zpm_machine_casing`
4. VG wire: a wiremill on the vanadium gallium ingot, single wire, circuit 1. Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 VG single cable in 5 s at 8 EU/t. Two per hull. — `gtceu:lv_wiremill`, `gtceu:vanadium_gallium_single_wire`
5. Hull assembler: casing + 2 VG cables + 288 mB PBI → ZPM Machine Hull in 2.5 s at 16 EU/t. PBI by a Pipez fluid pipe from its drum, casing and cables by one router each. — `gtceu:lv_assembler`, `gtceu:polybenzimidazole_bucket`, `gtceu:zpm_machine_hull`
6. Output drawer Keep Exact 8. Hulls are what every ZPM hatch, bus, component machine and fusion casing starts from. — `functionalstorage:oak_1`, `gtceu:zpm_machine_hull`

## Tips

- Recipes. Casing: 8 naquadah alloy plates, assembler, circuit 8, 50 ticks at 16 EU/t (MachineRecipeLoader casing\_zpm; crafting-table version 8 plates around a wrench). Hull: the PACK replaces the GT hull for LuV, ZPM and UV (kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js, luvUVMachines): casing + 2 tier single cables + 288 mB of the tier plastic, assembler 50 ticks at 16 EU/t, and a crafting-table alternative (middle row: PBI plate, naquadah alloy plate, PBI plate; bottom row: cable, casing, cable). For ZPM: casing + 2 vanadium gallium single cables + 288 mB polybenzimidazole. Vanilla GT (hull\_zpm) is the same with PBI as well; the LuV hull is the one that differs (see zpm\_pbi).
- Cable (WireRecipeHandler): vanadium gallium is a ZPM-rated cable (V\[ZPM\]), so like the LuV cable it needs, in the assembler at 100 ticks and 8 EU/t: 1 single wire + 1 polyphenylene sulfide foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber). Two cables per hull. The ZPM energy hatch uses 4 more VG single cables (energy\_hatch\_zpm) and the pack’s ZPM 4A hatch 2 VG quadruple wires. Vanadium gallium dust (MixerRecipes): 3 vanadium + 1 gallium dust → 4 dust, circuit 1, 400 ticks at 1920 EU/t (EV Mixer); EBF 4500 K (RTM coils), 1920 EU/t, 1200 ticks (60 s), freezer VA\[HV\]. Vanadium and gallium sources: Unverified (check EMI).
- The pack also keeps the plastic in tier\_data.js: ZPM plastic = polybenzimidazole, cable = vanadium gallium, tier material naquadah alloy, glass = fusion glass. Hull cost: 8 naquadah alloy ingots (4 naquadah dust, 2 osmiridium, 2 trinium dust), 2 VG wire (about 1 ingot), 2 PPS and 2 PVC foils, 144 mB silicone, 288 mB PBI. The hull is the starting item for every ZPM machine and hatch, so the cost per hull is mostly trinium and naquadah.
- What the hull unlocks in this guide: ZPM energy hatch (zpm\_hatches), ZPM input/output buses, ZPM assembler and other ZPM machines, the research parts (zpm\_research), the fusion casings (zpm\_fusion), the rotor holder. 4A and 16A hatches use the transformers: the pack’s ZPM transformer = ZPM hull + 1 yttrium barium cuprate cable + 4 vanadium gallium cables + 2 UHPIC chips (transformers.js).
- Sub-steps people skip: (1) bender plates on circuit 1, casing on circuit 8; (2) PPS foil is mandatory for the cable: keep its drawer even though you made it for the LuV cables; (3) the cable is a 100 tick recipe, make 4 at a time with Keep Exact 4; (4) keep 3 casings spare, the ZPM fusion casings need hulls too; (5) PBI hull recipe bypasses PTFE entirely.
- **Unverified** the exact vanadium and gallium sources.

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

- **Needs:** [ZPM alloys: naquadah alloy (hull casing) and osthendah (all ZPM parts): mixers → EBF with naquadah coils (7200 K) → Vacuum Freezer with liquid helium](zpm_alloys.md)
- **Main source for:** `gtceu:zpm_machine_hull`, `gtceu:zpm_machine_casing`, `gtceu:vanadium_gallium_single_cable`, `gtceu:vanadium_gallium_single_wire`
