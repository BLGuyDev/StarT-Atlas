---
kind: chain
id: uev_hull
order: 1950
data:
  t: |-
    UEV Machine Hull: 8 mythrolic alloy plates → casing, + 2 cerium tritelluride single cables + 288 mB PEDOT:PSS plastic
  inf: true
  "n":
    - [ig, "Mythrolic alloy ingot (uev_alloys)", i, "gtceu:mythrolic_alloy_ingot"]
    - [be, "LV Bender · circuit 1", m, "gtceu:lv_bender"]
    - [pl, "8 Mythrolic alloy plate", x, "gtceu:mythrolic_alloy_plate"]
    - [a1, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, UEV Machine Casing, x, "gtceu:uev_machine_casing"]
    - [cw, "Cerium tritelluride single wire · foils · rubber (cable)", x, "gtceu:cerium_tritelluride_single_cable"]
    - [pb, "288 mB PEDOT:PSS plastic", f, "gtceu:poly_34_ethylenedioxythiophene_polystyrene_sulfonate_bucket"]
    - [a3, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, UEV Machine Hull, o, "gtceu:uev_machine_hull"]
  e:
    - [ig, be, "8"]
    - [be, pl, "1 / ingot"]
    - [pl, a1, "8"]
    - [a1, mc, "1 / 2.5 s"]
    - [mc, a3, "1"]
    - [cw, a3, "2"]
    - [pb, a3, "288 mB"]
    - [a3, hu, "1 / 2.5 s"]
  tips:
    - |-
      Recipes (kjs additions/machines_and_parts/tiered_machines/singleblocks.js, postUVMachines): casing = 8 mythrolic alloy plates, assembler circuit 8, 50 ticks, 16 EU/t (crafting table: 8 plates around a wrench). Hull = casing + 2 cerium tritelluride single cables + 288 mB poly(3,4-ethylenedioxythiophene) polystyrene sulfonate (PEDOT:PSS), assembler 50 ticks, 16 EU/t; crafting-table alternative: plastic plate, tier plate, plastic plate over cable, casing, cable. Same shape as the UV hull; the only change from ZPM is the materials.
    - |-
      Materials from tier_data.js: tier plate mythrolic alloy, cable cerium tritelluride, wire astatium bioselex carbonite (electric furnace/blaster style machines use the double and quadruple wire), glass reinforced fusion glass, solder naquadated soldering alloy. Casing multiblock recipes in casings.js use the same alloy, so the plate stock is shared.
    - |-
      The pack removes every GregTech recipe whose output or input starts with gtceu:uev (singleblocks.js top) and re-adds only: hull, casing, and the machines listed there (furnace, blaster, assembler, circuit assembler, etc. in the crafting table). Only the hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder and sterile maintenance paths are traced for this guide; for any other UEV singleblock check the recipe browser. Unverified: whether the plastic fluid needs a dedicated drum line (PEDOT:PSS recipe not traced here).
    - |-
      Where the alloy comes from: Hell Forge plasma, then Cryostate Quantum Chiller, then a vacuum freezer with an ingot mold (see uev_alloys). Cable: cerium tritelluride wire from its own line (tellurium and cerium mixed, 11 699 K blast, UHV hatch, per MH.conductor in base_materials.js). Cable needs foils and rubber like the lower tiers: Unverified which ones (WireRecipeHandler for superconductors).
    - |-
      Sub-steps people skip: (1) plates on the bender with circuit 1, casing on circuit 8; (2) 3 hulls spare for the fusion and rotor holder recipes, which each eat one; (3) keep plastic in a drum with a Pipez fluid pipe, not a bucket by hand: one hull is 288 mB; (4) hulls are the input of every UEV hatch and of the field generator line.
    - |-
      Unverified: cable source, plastic route, exact cable foil inputs.
  b:
    - ["gtceu:lv_assembler", 2]
    - ["gtceu:lv_bender", 1]
    - ["functionalstorage:oak_1", 8]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 2]
    - ["gtceu:steel_drum", 1]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:mythrolic_alloy_ingot", "gtceu:cerium_tritelluride_single_cable"]
      t: |-
        Drawers first: mythrolic alloy ingots, cerium tritelluride single cables. One drum for PEDOT:PSS. One dedicated machine per product (bender, casing assembler, hull assembler), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode.
    - i: ["gtceu:lv_bender", "gtceu:mythrolic_alloy_plate"]
      t: |-
        LV Bender, circuit 1: 1 ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16.
    - i: ["gtceu:lv_assembler", "gtceu:uev_machine_casing"]
      t: |-
        LV Assembler, circuit 8: 8 plates → 1 casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer.
    - i:
        - gtceu:lv_assembler
        - gtceu:poly_34_ethylenedioxythiophene_polystyrene_sulfonate_bucket
        - gtceu:uev_machine_hull
      t: |-
        Hull assembler: casing + 2 cables from their drawer + 288 mB PEDOT:PSS by a Pipez fluid pipe from the drum → hull in 2.5 s at 16 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:uev_machine_hull"]
      t: Output drawer Keep Exact 8. Every UEV energy hatch, transformer, parallel hatch and component starts here.
---
# UEV Machine Hull: 8 mythrolic alloy plates → casing, + 2 cerium tritelluride single cables + 288 mB PEDOT:PSS plastic

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uev_hull` · **Tags:** Infinite source, Unverified

**Era setup:** [UEV · Nether](../../eras/uev.md)

**Plan modules:** [UEV hull, parts, hatches and components](../../plan/p18.md#uevmach)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Mythrolic alloy ingot (uev_alloys) (gtceu:mythrolic_alloy_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Ingot</span><span class="gt-note">Mythrolic alloy ingot (uev_alloys)</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Mythrolic alloy plate (gtceu:mythrolic_alloy_plate) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Plate</span><span class="gt-note">8 Mythrolic alloy plate</span><b class="gt-q">1 / ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Mythrolic alloy plate (gtceu:mythrolic_alloy_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__mythrolic_alloy_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mythrolic Alloy Plate</span><span class="gt-note">8 Mythrolic alloy plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="UEV Machine Casing (gtceu:uev_machine_casing) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="UEV Machine Casing (gtceu:uev_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__uev_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="Cerium tritelluride single wire · foils · rubber (cable) (gtceu:cerium_tritelluride_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__cerium_tritelluride_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cerium Tritelluride Single Cable</span><span class="gt-note">Cerium tritelluride single wire · foils · rubber (cable)</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PEDOT:PSS plastic (gtceu:poly_34_ethylenedioxythiophene_polystyrene_sulfonate_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__poly_34_ethylenedioxythiophene_polystyrene_sulfonate_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Poly 34 Ethylenedioxythiophene Polystyrene Sulfonate</span><span class="gt-note">288 mB PEDOT:PSS plastic</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="UEV Machine Hull (gtceu:uev_machine_hull) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__uev_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UEV Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1](#m-be) → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a1) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)

## How to build

1. Drawers first: mythrolic alloy ingots, cerium tritelluride single cables. One drum for PEDOT:PSS. One dedicated machine per product (bender, casing assembler, hull assembler), each behind its own router or Pipez item pipe with Item Filters and a Robot Arm cover in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:mythrolic_alloy_ingot`, `gtceu:cerium_tritelluride_single_cable`
2. LV Bender, circuit 1: 1 ingot → 1 plate. 8 plates per casing; output drawer Keep Exact 16. — `gtceu:lv_bender`, `gtceu:mythrolic_alloy_plate`
3. LV Assembler, circuit 8: 8 plates → 1 casing in 2.5 s at 16 EU/t. Keep Exact 4 on the casing drawer. — `gtceu:lv_assembler`, `gtceu:uev_machine_casing`
4. Hull assembler: casing + 2 cables from their drawer + 288 mB PEDOT:PSS by a Pipez fluid pipe from the drum → hull in 2.5 s at 16 EU/t. — `gtceu:lv_assembler`, `gtceu:poly_34_ethylenedioxythiophene_polystyrene_sulfonate_bucket`, `gtceu:uev_machine_hull`
5. Output drawer Keep Exact 8. Every UEV energy hatch, transformer, parallel hatch and component starts here. — `functionalstorage:oak_1`, `gtceu:uev_machine_hull`

## Tips

- Recipes (kjs additions/machines\_and\_parts/tiered\_machines/singleblocks.js, postUVMachines): casing = 8 mythrolic alloy plates, assembler circuit 8, 50 ticks, 16 EU/t (crafting table: 8 plates around a wrench). Hull = casing + 2 cerium tritelluride single cables + 288 mB poly(3,4-ethylenedioxythiophene) polystyrene sulfonate (PEDOT:PSS), assembler 50 ticks, 16 EU/t; crafting-table alternative: plastic plate, tier plate, plastic plate over cable, casing, cable. Same shape as the UV hull; the only change from ZPM is the materials.
- Materials from tier\_data.js: tier plate mythrolic alloy, cable cerium tritelluride, wire astatium bioselex carbonite (electric furnace/blaster style machines use the double and quadruple wire), glass reinforced fusion glass, solder naquadated soldering alloy. Casing multiblock recipes in casings.js use the same alloy, so the plate stock is shared.
- The pack removes every GregTech recipe whose output or input starts with gtceu:uev (singleblocks.js top) and re-adds only: hull, casing, and the machines listed there (furnace, blaster, assembler, circuit assembler, etc. in the crafting table). Only the hull, energy hatches, transformers, laser hatches, parallel hatch, rotor holder and sterile maintenance paths are traced for this guide; for any other UEV singleblock check the recipe browser. Unverified: whether the plastic fluid needs a dedicated drum line (PEDOT:PSS recipe not traced here).
- Where the alloy comes from: Hell Forge plasma, then Cryostate Quantum Chiller, then a vacuum freezer with an ingot mold (see uev\_alloys). Cable: cerium tritelluride wire from its own line (tellurium and cerium mixed, 11 699 K blast, UHV hatch, per MH.conductor in base\_materials.js). Cable needs foils and rubber like the lower tiers: Unverified which ones (WireRecipeHandler for superconductors).
- Sub-steps people skip: (1) plates on the bender with circuit 1, casing on circuit 8; (2) 3 hulls spare for the fusion and rotor holder recipes, which each eat one; (3) keep plastic in a drum with a Pipez fluid pipe, not a bucket by hand: one hull is 288 mB; (4) hulls are the input of every UEV hatch and of the field generator line.
- **Unverified** cable source, plastic route, exact cable foil inputs.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 2 |
| `gtceu:lv_bender` | 1 |
| `functionalstorage:oak_1` | 8 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 2 |
| `gtceu:steel_drum` | 1 |

## Needs / Feeds

- **Needs:** [UEV alloys (mythrolic, magmada, starium): molten metals + element plasma in the Hell Forge → alloy plasma → Cryostate Quantum Chiller → molten alloy → vacuum freezer → ingot](uev_alloys.md)
- **Main source for:** `gtceu:uev_machine_hull`, `gtceu:uev_machine_casing`
