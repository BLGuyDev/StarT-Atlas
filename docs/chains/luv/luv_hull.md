---
kind: chain
id: luv_hull
order: 1210
data:
  t: |-
    LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI
  inf: true
  "n":
    - [ig, Rhodium plated palladium ingot, i, "gtceu:rhodium_plated_palladium_ingot"]
    - [be, "LV Bender · circuit 1", m, "gtceu:lv_bender"]
    - [pl, "8 Rhodium plated palladium plate", x, "gtceu:rhodium_plated_palladium_plate"]
    - [a1, "LV Assembler · circuit 8 · 2.5 s · 16 EU/t", m, "gtceu:lv_assembler"]
    - [mc, LuV Machine Casing, x, "gtceu:luv_machine_casing"]
    - - cw
      - |-
        1 NbTi single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber
      - g
      - functionalstorage:oak_1
      - - [NbTi single wire, "gtceu:niobium_titanium_single_wire"]
        - [PPS foil, "gtceu:polyphenylene_sulfide_foil"]
        - [PVC foil, "gtceu:polyvinyl_chloride_foil"]
        - [Silicone rubber, "gtceu:silicone_rubber_bucket"]
    - [a2, "LV Assembler · 5 s · 7 EU/t (cable)", m, "gtceu:lv_assembler"]
    - [cb, "2 NbTi single cable", x, "gtceu:niobium_titanium_single_cable"]
    - [pf, "288 mB PBI (zpm_pbi chain)", f, "gtceu:polybenzimidazole_bucket"]
    - [a3, "LV Assembler · 2.5 s · 16 EU/t (hull)", m, "gtceu:lv_assembler"]
    - [hu, LuV Machine Hull, o, "gtceu:luv_machine_hull"]
  e:
    - [ig, be, "8"]
    - [be, pl, "1 / ingot"]
    - [pl, a1, "8"]
    - [a1, mc, "1 / 2.5 s"]
    - [cw, a2, "2 crafts"]
    - [a2, cb, "2 / 5 s"]
    - [mc, a3, "1"]
    - [cb, a3, "2"]
    - [pf, a3, "288 mB"]
    - [a3, hu, "1 / 2.5 s"]
  tips:
    - |-
      Recipes: machine casing = 8 rhodium plated palladium plates, assembler, circuit 8, 50 ticks at 16 EU/t (MachineRecipeLoader casing_luv; crafting table version: 8 plates around a wrench). Hull: the PACK replaces the GT hull for LuV, ZPM and UV (kjs tiered_machines/singleblocks.js luvUVMachines): casing + 2 niobium titanium single cables + 288 mB polybenzimidazole (PBI, tier_data.js plastic), assembler, 50 ticks at 16 EU/t; vanilla hull_luv used PTFE. IV used tungsten steel plates, platinum cables, PTFE; from LuV the plastic is PBI. The hull does NOT use the Assembly Line: the casing and the hull are two plain assembler recipes that an LV Assembler runs; the Assembly Line is for the LuV components that go into LuV machines.
    - |-
      The new problem is the cable: niobium titanium cables are LuV rated (cableProperties V[LuV]), so WireRecipeHandler adds a Polyphenylene Sulfide foil on top of the PVC foil: 1 NbTi single wire + 1 PPS foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber), assembler, 100 ticks, ULV power. Two cables per hull, so 2 wires, 2 PPS foils, 2 PVC foils and 144 mB silicone. Plain rubber is not accepted any more.
    - |-
      Polyphenylene sulfide (PPS): chemical reactor, 3 sodium sulfide dust + 1 B dichlorobenzene + 8 B oxygen (or 16 B air) → 1500 mB (1000 with air) PPS + 4 salt, 240 ticks at 360 EU/t, which is an HV reactor. Sodium sulfide = 2 sodium + 1 sulfur dust, LV reactor, 60 ticks. Dichlorobenzene = 4 B chlorine + 1 B benzene, circuit 2, chemical reactor. Benzene is the oil_distill chain. The pack also has a hydrocarbon skip for PPS (EV hatch, kjs hydrocarbons.js) but it is not needed. Foil: bender on the PPS plate (solidifier plate mold, 144 mB each). Unverified: the PPS foil press and the exact bender time.
    - |-
      PBI: the polybenzimidazole line of the zpm_pbi chain (IV-power chemistry); 288 mB per hull, so build it before the first LuV hull. PTFE is no longer used by the hull (it is still the optical pipe and hatch fluid). Silicone rubber (HV): 9 polydimethylsiloxane dust + 1 sulfur → 1296 mB, chemical reactor 600 ticks at 30 EU/t (ReactorRecipes).
    - |-
      Cost per hull: 8 RPP ingots = 6 palladium + 2 rhodium, 2 niobium titanium (cable wire), 2 PPS and 2 PVC foils, 144 mB silicone, 288 mB PBI. One rhodium plated palladium ingot is 3/4 palladium and 1/4 rhodium. You need many hulls: each LuV machine, each hatch and the ZPM hull path start from one.
    - |-
      Sub-steps people skip: (1) plates by LV Bender on circuit 1, not 10 (10 is foil from an ingot); (2) the casing recipe uses circuit 8; (3) cables need three inputs: wire, two foils, one fluid; (4) PVC foil is also an IV/EV item you may already have drawers for; (5) keep a Keep Exact 4 casing drawer so a stalled hull assembler does not flood.
    - |-
      Unverified: that the LV Assembler accepts the 7 EU/t cable recipe at once (any assembler should), and the plate time of a rhodium plated palladium ingot in the bender (mass based).
  b:
    - ["gtceu:lv_assembler", 3]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_fluid_solidifier", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:rhodium_plated_palladium_ingot", "gtceu:niobium_titanium_single_wire"]
      t: |-
        Drawers first: RPP ingots (from the luv_alloys chain), NbTi single wire, PPS foil, PVC foil. Two drums: silicone rubber (or styrene butadiene rubber) and PBI. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez pipe with Item Filters and a Robot Arm cover in Keep Exact mode.
    - i: ["gtceu:lv_bender", "gtceu:rhodium_plated_palladium_plate"]
      t: |-
        LV Bender, circuit 1 in the bus: 1 RPP ingot → 1 plate. 8 plates per casing. Output drawer Keep Exact 16.
    - i: ["gtceu:lv_assembler", "gtceu:luv_machine_casing"]
      t: |-
        LV Assembler, circuit 8: 8 plates → 1 LuV Machine Casing in 2.5 s at 16 EU/t. Casings are also what the LuV hull line and other casing recipes eat; the 8-circuit setting is what separates it from other 8-plate recipes.
    - i: ["gtceu:niobium_titanium_single_wire", "gtceu:polyphenylene_sulfide_foil", "gtceu:polyvinyl_chloride_foil"]
      t: |-
        NbTi wire: LV Wiremill on the NbTi ingot (single wire, circuit 1). Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 NbTi single cable in 5 s at about 7 EU/t. Keep the PPS foil in its own drawer; it is the new input of this tier.
    - i: ["gtceu:lv_assembler", "gtceu:polybenzimidazole_bucket", "gtceu:luv_machine_hull"]
      t: |-
        Hull assembler: casing + 2 NbTi single cables + 288 mB PBI → LuV Machine Hull in 2.5 s at 16 EU/t. PBI by a Pipez fluid pipe from its drum, casing and cables by one router each.
    - i: ["functionalstorage:oak_1", "gtceu:luv_machine_hull"]
      t: Output drawer Keep Exact 8. Hulls are what the Assembly Line machines, the 4A/16A hatches, converters and the dimensional destabiliser all start from.
---
# LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_hull` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 1</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Rhodium plated palladium ingot (gtceu:rhodium_plated_palladium_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Ingot</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Rhodium plated palladium plate (gtceu:rhodium_plated_palladium_plate) - 1 / ingot"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Plate</span><span class="gt-note">8 Rhodium plated palladium plate</span><b class="gt-q">1 / ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-a1">
<div class="gt-head"><span class="gt-mname">LV Assembler · circuit 8 · 2.5 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Rhodium plated palladium plate (gtceu:rhodium_plated_palladium_plate) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_plated_palladium_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Plated Palladium Plate</span><span class="gt-note">8 Rhodium plated palladium plate</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LuV Machine Casing (gtceu:luv_machine_casing) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Machine Casing</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a2">
<div class="gt-head"><span class="gt-mname">LV Assembler · 5 s · 7 EU/t (cable)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 NbTi single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber (functionalstorage:oak_1) - 2 crafts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 NbTi single wire · 1 PPS foil · 1 PVC foil · 72 mB silicone rubber</span><span class="gt-sub"><span>NbTi single wire</span><span>PPS foil</span><span>PVC foil</span><span>Silicone rubber</span></span><b class="gt-q">2 crafts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 NbTi single cable (gtceu:niobium_titanium_single_cable) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_titanium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Titanium Single Cable</span><span class="gt-note">2 NbTi single cable</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
<div class="gt-panel t-lv" id="m-a3">
<div class="gt-head"><span class="gt-mname">LV Assembler · 2.5 s · 16 EU/t (hull)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Machine Casing (gtceu:luv_machine_casing) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__luv_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Machine Casing</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 NbTi single cable (gtceu:niobium_titanium_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_titanium_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Titanium Single Cable</span><span class="gt-note">2 NbTi single cable</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB PBI (zpm_pbi chain) (gtceu:polybenzimidazole_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__polybenzimidazole_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polybenzimidazole</span><span class="gt-note">288 mB PBI (zpm_pbi chain)</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">2.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Machine Hull (gtceu:luv_machine_hull) - 1 / 2.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Machine Hull</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Bender · circuit 1](#m-be) → [LV Assembler · circuit 8 · 2.5 s · 16 EU/t](#m-a1) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)
- [LV Assembler · 5 s · 7 EU/t (cable)](#m-a2) → [LV Assembler · 2.5 s · 16 EU/t (hull)](#m-a3)

## How to build

1. Drawers first: RPP ingots (from the luv\_alloys chain), NbTi single wire, PPS foil, PVC foil. Two drums: silicone rubber (or styrene butadiene rubber) and PBI. One dedicated assembler per product (plate bender, casing, cable, hull), each behind its own router or Pipez pipe with Item Filters and a Robot Arm cover in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:rhodium_plated_palladium_ingot`, `gtceu:niobium_titanium_single_wire`
2. LV Bender, circuit 1 in the bus: 1 RPP ingot → 1 plate. 8 plates per casing. Output drawer Keep Exact 16. — `gtceu:lv_bender`, `gtceu:rhodium_plated_palladium_plate`
3. LV Assembler, circuit 8: 8 plates → 1 LuV Machine Casing in 2.5 s at 16 EU/t. Casings are also what the LuV hull line and other casing recipes eat; the 8-circuit setting is what separates it from other 8-plate recipes. — `gtceu:lv_assembler`, `gtceu:luv_machine_casing`
4. NbTi wire: LV Wiremill on the NbTi ingot (single wire, circuit 1). Then the cable assembler: wire + PPS foil + PVC foil + 72 mB silicone rubber → 1 NbTi single cable in 5 s at about 7 EU/t. Keep the PPS foil in its own drawer; it is the new input of this tier. — `gtceu:niobium_titanium_single_wire`, `gtceu:polyphenylene_sulfide_foil`, `gtceu:polyvinyl_chloride_foil`
5. Hull assembler: casing + 2 NbTi single cables + 288 mB PBI → LuV Machine Hull in 2.5 s at 16 EU/t. PBI by a Pipez fluid pipe from its drum, casing and cables by one router each. — `gtceu:lv_assembler`, `gtceu:polybenzimidazole_bucket`, `gtceu:luv_machine_hull`
6. Output drawer Keep Exact 8. Hulls are what the Assembly Line machines, the 4A/16A hatches, converters and the dimensional destabiliser all start from. — `functionalstorage:oak_1`, `gtceu:luv_machine_hull`

## Tips

- Recipes: machine casing = 8 rhodium plated palladium plates, assembler, circuit 8, 50 ticks at 16 EU/t (MachineRecipeLoader casing\_luv; crafting table version: 8 plates around a wrench). Hull: the PACK replaces the GT hull for LuV, ZPM and UV (kjs tiered\_machines/singleblocks.js luvUVMachines): casing + 2 niobium titanium single cables + 288 mB polybenzimidazole (PBI, tier\_data.js plastic), assembler, 50 ticks at 16 EU/t; vanilla hull\_luv used PTFE. IV used tungsten steel plates, platinum cables, PTFE; from LuV the plastic is PBI. The hull does NOT use the Assembly Line: the casing and the hull are two plain assembler recipes that an LV Assembler runs; the Assembly Line is for the LuV components that go into LuV machines.
- The new problem is the cable: niobium titanium cables are LuV rated (cableProperties V\[LuV\]), so WireRecipeHandler adds a Polyphenylene Sulfide foil on top of the PVC foil: 1 NbTi single wire + 1 PPS foil + 1 PVC foil + 72 mB silicone rubber (or 36 mB styrene butadiene rubber), assembler, 100 ticks, ULV power. Two cables per hull, so 2 wires, 2 PPS foils, 2 PVC foils and 144 mB silicone. Plain rubber is not accepted any more.
- Polyphenylene sulfide (PPS): chemical reactor, 3 sodium sulfide dust + 1 B dichlorobenzene + 8 B oxygen (or 16 B air) → 1500 mB (1000 with air) PPS + 4 salt, 240 ticks at 360 EU/t, which is an HV reactor. Sodium sulfide = 2 sodium + 1 sulfur dust, LV reactor, 60 ticks. Dichlorobenzene = 4 B chlorine + 1 B benzene, circuit 2, chemical reactor. Benzene is the oil\_distill chain. The pack also has a hydrocarbon skip for PPS (EV hatch, kjs hydrocarbons.js) but it is not needed. Foil: bender on the PPS plate (solidifier plate mold, 144 mB each). Unverified: the PPS foil press and the exact bender time.
- PBI: the polybenzimidazole line of the zpm\_pbi chain (IV-power chemistry); 288 mB per hull, so build it before the first LuV hull. PTFE is no longer used by the hull (it is still the optical pipe and hatch fluid). Silicone rubber (HV): 9 polydimethylsiloxane dust + 1 sulfur → 1296 mB, chemical reactor 600 ticks at 30 EU/t (ReactorRecipes).
- Cost per hull: 8 RPP ingots = 6 palladium + 2 rhodium, 2 niobium titanium (cable wire), 2 PPS and 2 PVC foils, 144 mB silicone, 288 mB PBI. One rhodium plated palladium ingot is 3/4 palladium and 1/4 rhodium. You need many hulls: each LuV machine, each hatch and the ZPM hull path start from one.
- Sub-steps people skip: (1) plates by LV Bender on circuit 1, not 10 (10 is foil from an ingot); (2) the casing recipe uses circuit 8; (3) cables need three inputs: wire, two foils, one fluid; (4) PVC foil is also an IV/EV item you may already have drawers for; (5) keep a Keep Exact 4 casing drawer so a stalled hull assembler does not flood.
- **Unverified** that the LV Assembler accepts the 7 EU/t cable recipe at once (any assembler should), and the plate time of a rhodium plated palladium ingot in the bender (mass based).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 3 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_fluid_solidifier` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Needs:** [LuV alloys: rhodium plated palladium (hull), ruridit (gears, rotor) and niobium titanium (cables, pipes), all IV Mixer → EBF 4500 K (RTM coils) → Vacuum Freezer](luv_alloys.md)
- **Feeds:** [LuV power: Large Gas Turbine with a LuV rotor holder](luv_turbines.md), [Combo: Modular Combustion Frame with combustion and rocket modules](../combos/combo_mcf.md)
- **Main source for:** `gtceu:luv_machine_hull`, `gtceu:luv_machine_casing`, `gtceu:rhodium_plated_palladium_plate`, `gtceu:niobium_titanium_single_cable`
