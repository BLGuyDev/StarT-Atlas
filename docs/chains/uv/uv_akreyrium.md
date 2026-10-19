---
kind: chain
id: uv_akreyrium
order: 1730
data:
  t: |-
    Abydos mantle: ZPM Fluid Drilling Rig (144 CWU/t research) → gritty akreyrium → Cyclonic Sifter and Molten Destabiliser (280 B and 72 B of it per controller)
  inf: true
  "n":
    - - g1
      - UV hull · 4 enriched naquadah frame · 4 UV circuit · 4 UV motor · 4 UV pump · 4 naquadah alloy gear · 1872 mB solder
      - g
      - functionalstorage:oak_1
      - - [UV Machine Hull, "gtceu:uv_machine_hull"]
        - [Enriched naquadah frame, "gtceu:enriched_naquadah_frame"]
        - [UV motor, "gtceu:uv_electric_motor"]
        - [UV pump, "gtceu:uv_electric_pump"]
        - [Naquadah alloy gear, "gtceu:naquadah_alloy_gear"]
    - - a1
      - Assembly Line · 20 s · 245 760 EU/t · research EV Fluid Drilling Rig 144 CWU/t
      - m
      - gtceu:assembly_line
    - [rig, "ZPM Fluid Drilling Rig (Abydos)", x, "start_core:zpm_fluid_drilling_rig"]
    - - vn
      - Gritty akreyrium fluid vein (Abydos, weight 19, yield 360 to 640, depleted 320)
      - x
      - gtceu:gritty_akreyrium_bucket
    - [gk, "Gritty akreyrium (280 B + 72 B)", f, "gtceu:gritty_akreyrium_bucket"]
    - - g2
      - ZPM hull · 12 UV circuit · 56 UHPIC · 16 prismalium gear · 8 ZPM pump · 4 ZPM motor · 2 ZPM field generator · 6 pure netherite gear · 4 B PBI · 280 B gritty akreyrium
      - g
      - functionalstorage:oak_1
      - - [ZPM Machine Hull, "gtceu:zpm_machine_hull"]
        - [Prismalium gear, "gtceu:prismalium_gear"]
        - [ZPM pump, "gtceu:zpm_electric_pump"]
        - [Pure netherite gear, "gtceu:pure_netherite_gear"]
    - [a2, "Assembly Line · 80 s · 491 520 EU/t · research Large Sifting Funnel 24 CWU/t", m, "gtceu:assembly_line"]
    - [cs, Cyclonic Sifter, o, "gtceu:cyclonic_sifter"]
    - - g3
      - ZPM hull · 6 UV circuit · 4 dense naquadria plate · 64 UHPIC · 4 huge duranium pipe · 4 pure netherite rotor · 4 small netherite gear · 24 ZPM pump · 8 B PBI · 72 B gritty akreyrium
      - g
      - functionalstorage:oak_1
      - - [Dense naquadria plate, "gtceu:dense_naquadria_plate"]
        - [Duranium huge fluid pipe, "gtceu:duranium_huge_fluid_pipe"]
        - [Pure netherite rotor, "gtceu:pure_netherite_rotor"]
    - [a3, "Assembly Line · 112.5 s · 491 520 EU/t · research Large Distillery 24 CWU/t", m, "gtceu:assembly_line"]
    - [md, Molten Destabiliser, o, "gtceu:molten_destabiliser"]
  e:
    - [g1, a1, "1"]
    - [a1, rig, "1 / 20 s"]
    - [rig, vn, drill]
    - [vn, gk, fluid]
    - [gk, g2, "280 B"]
    - [gk, g3, "72 B"]
    - [g2, a2, "1"]
    - [a2, cs, "1 / 80 s"]
    - [g3, a3, "1"]
    - [a3, md, "1 / 112 s"]
  tips:
    - |-
      Fluid drilling rig (kjs additions/multiblock_recipes/fluid_drill.js): Assembly Line, 400 ticks at VHA[UV] = 245 760 EU/t, UV hull + 4 enriched naquadah frames + 4 UV circuits + 4 UV motors + 4 UV pumps + 4 naquadah alloy gears + 1872 mB soldering alloy, STATION research of the EV fluid drilling rig at 144 CWU/t and VHA[UV]. 144 CWU/t is the highest research load of the UV era: nine advanced HPCA components, i.e. about four HPCAs through a Network Switch (uv_research). The rig drills fluid veins of its dimension; the pack adds the Abydos vein ‘gritty akreyrium’ (kjs utils/fluid_veins.js: dimension sgjourney:abydos, weight 19, yield 360 to 640, depletes by 2 per cycle with chance 1, depleted yield 320) next to the dense magma veins of Abydos (weight 25 and 28, yield 400 to 540).
    - |-
      Cyclonic Sifter (UV): ZPM hull + 12 UV circuits + 56 UHPIC chips + 16 prismalium gears + 8 ZPM pumps + 4 ZPM motors + 2 ZPM field generators + 6 pure netherite gears; 4 B PBI + 280 B gritty akreyrium (280 000 mB!), 1600 ticks (80 s) at VA[UV] = 491 520 EU/t, research Large Sifting Funnel 24 CWU/t at VHA[UV]. Molten Destabiliser (UV): ZPM hull + 6 UV circuits + 4 dense naquadria plates + 64 UHPIC + 4 huge duranium pipes + 4 pure netherite rotors + 4 small pure netherite gears + 24 ZPM pumps; 8 B PBI + 72 B gritty akreyrium, 2250 ticks (112.5 s) at VA[UV], research Large Distillery 24 CWU/t. Both need 491 520 EU/t = a ZPM 4A hatch or a UV hatch on the Assembly Line.
    - |-
      What the sifter does later (akreyrium.js, UHV page): cyclonic sifter recipe akreyrium_sieving, 100 B gritty akreyrium + a netherite reinforced mesh (50 % chance kept) → 1 B lepton sparse akreyrium + crystalline and amorphous akreyrium, 1200 ticks at VA[UHV] x 0.8; manifold centrifuge then splits the lepton form into electron / muon / tau akreyrium (UHV). So the UV page ends at building the sifter and filling a 280 B tank.
    - |-
      Order inside Abydos (verified, NOT a loop): both controllers need UV motors and pumps, and every UV motor carries a long magnetic dysprosium rod (UV primary magnet = dysprosium, tier_data.js). Dysprosium has one source: the xenotime line (uv_rare_earth), and xenotime exists only in the Abydos ore veins (ore_veins.js removes every other vein; abydos_refractory_metals_vein carries xenotime, weight 3), plus 3 raw xenotime per refractory magma residue run later. So: mine xenotime by hand in Abydos -> uv_rare_earth -> dysprosium rod -> UV motors and pumps -> ZPM Fluid Drilling Rig (UV hull, VHA[UV], 144 CWU/t research) -> drill the gritty akreyrium vein -> Molten Destabiliser (ZPM hull, 6 UV circuits, 24 ZPM pumps, VA[UV], 24 CWU/t research) -> magma. The dysprosium comes from the ore vein, not from the magma, so nothing waits on itself; both machines need a UV hatch to be assembled. The bacterial machines (uv_bio2) come after this.
    - |-
      Cost reality: 280 000 mB of gritty akreyrium for ONE sifter. At the vein yield of 360 to 640 per cycle that is hundreds of cycles of one rig (drill output per cycle: Unverified), so build several rigs on the same vein or find the vein with a big field. A Magmatic Drill (komaru modules, UV power, 250 MEU start) can output up to 4 096 000 mB of gritty akreyrium per run but needs kaleidoscope agitation serum, which is a later line.
    - |-
      Sub-steps people skip: (1) rigs only drill in their own dimension: put the rig, a power line and an output pipe/drum in Abydos (needs the Abydos talisman, uv era step 1); (2) 24 ZPM pumps for the destabiliser come from the ZPM pump line, many at once; (3) prismalium gears (16): prismalium is a Nether line metal (Unverified route); (4) both controllers need a vacuum of UHPIC chips: 56 + 64 chips = 60 wafers.
    - |-
      Unverified: drill output per cycle, prismalium route, what the destabiliser recipe types do.
  b:
    - ["gtceu:assembly_line", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["start_core:zpm_fluid_drilling_rig", 1]
    - ["gtceu:uv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 24]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 20]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:uv_machine_hull", "gtceu:zpm_machine_hull", "gtceu:uhpic_chip"]
      t: |-
        Drawers first, one per input: hulls, frames, UV circuits (4 / 12 / 6), UV motors and pumps, ZPM pumps (8 and 24), prismalium gears, pure netherite gears and rotors, UHPIC chips, dense plates. Drums: soldering alloy, PBI, gritty akreyrium (several big drums).
    - i: ["gtceu:research_station", "gtceu:ev_fluid_drilling_rig", "gtceu:data_orb"]
      t: |-
        Research for the rig: an EV fluid drilling rig in the Object Holder, 144 CWU/t at 245 760 EU/t → orb. Do it only after the Network Switch + HPCAs read 144 CWU/t.
    - i: ["gtceu:assembly_line", "start_core:zpm_fluid_drilling_rig"]
      t: |-
        Rig: Assembly Line, 20 s, 245 760 EU/t; place it over the Abydos vein (use a prospecting tool for the vein), connect a UV energy hatch and an output hatch with a Pipez fluid pipe to the drum.
    - i: ["gtceu:assembly_line", "gtceu:cyclonic_sifter", "gtceu:molten_destabiliser"]
      t: |-
        Sifter first (24 CWU/t research, 80 s) then the destabiliser (24 CWU/t research, 112.5 s); both on a ZPM 4A hatch. Fluids by hatches: PBI and gritty akreyrium through the Pipez pipes with Keep Exact valves.
    - i: ["gtceu:cyclonic_sifter", "functionalstorage:oak_1"]
      t: |-
        Output drawers Keep Exact 1 per controller. The sifter stays idle until the UHV page: it needs netherite reinforced meshes and UHV power for its recipe.
    - i: ["gtceu:gritty_akreyrium_bucket", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: 280 B for a sifter plus 72 B for a destabiliser is 352 000 mB: plan storage (steel drums hold 32 B; the Abydos bulk tanks matter).
---
# Abydos mantle: ZPM Fluid Drilling Rig (144 CWU/t research) → gritty akreyrium → Cyclonic Sifter and Molten Destabiliser (280 B and 72 B of it per controller)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_akreyrium` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Abydos first: xenotime → dysprosium → drilling rig and magma](../../plan/p14.md#abydos)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 245 760 EU/t · research EV Fluid Drilling Rig 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UV hull · 4 enriched naquadah frame · 4 UV circuit · 4 UV motor · 4 UV pump · 4 naquadah alloy gear · 1872 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UV hull · 4 enriched naquadah frame · 4 UV circuit · 4 UV motor · 4 UV pump · 4 naquadah alloy gear · 1872 mB solder</span><span class="gt-sub"><span>UV Machine Hull</span><span>Enriched naquadah frame</span><span>UV motor</span><span>UV pump</span><span>Naquadah alloy gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Fluid Drilling Rig (Abydos) (start_core:zpm_fluid_drilling_rig) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fluid_drilling_rig.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fluid Drilling Rig</span><span class="gt-note">ZPM Fluid Drilling Rig (Abydos)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 80 s · 491 520 EU/t · research Large Sifting Funnel 24 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 12 UV circuit · 56 UHPIC · 16 prismalium gear · 8 ZPM pump · 4 ZPM motor · 2 ZPM field generator · 6 pure netherite gear · 4 B PBI · 280 B gritty akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 12 UV circuit · 56 UHPIC · 16 prismalium gear · 8 ZPM pump · 4 ZPM motor · 2 ZPM field generator · 6 pure netherite gear · 4 B PBI · 280 B gritty akreyrium</span><span class="gt-sub"><span>ZPM Machine Hull</span><span>Prismalium gear</span><span>ZPM pump</span><span>Pure netherite gear</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">80 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Cyclonic Sifter (gtceu:cyclonic_sifter) - 1 / 80 s"><img class="gt-ico" src="../../assets/icons/gtceu__cyclonic_sifter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cyclonic Sifter</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 112.5 s · 491 520 EU/t · research Large Distillery 24 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="ZPM hull · 6 UV circuit · 4 dense naquadria plate · 64 UHPIC · 4 huge duranium pipe · 4 pure netherite rotor · 4 small netherite gear · 24 ZPM pump · 8 B PBI · 72 B gritty akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">ZPM hull · 6 UV circuit · 4 dense naquadria plate · 64 UHPIC · 4 huge duranium pipe · 4 pure netherite rotor · 4 small netherite gear · 24 ZPM pump · 8 B PBI · 72 B gritty akreyrium</span><span class="gt-sub"><span>Dense naquadria plate</span><span>Duranium huge fluid pipe</span><span>Pure netherite rotor</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">112 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Molten Destabiliser (gtceu:molten_destabiliser) - 1 / 112 s"><img class="gt-ico" src="../../assets/icons/gtceu__molten_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Destabiliser</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 245 760 EU/t · research EV Fluid Drilling Rig 144 CWU/t](#m-a1) → [Assembly Line · 80 s · 491 520 EU/t · research Large Sifting Funnel 24 CWU/t](#m-a2) (also Assembly Line · 20 s · 245 760 EU/t · research EV Fluid Drilling Rig 144 CWU/t → [Assembly Line · 112.5 s · 491 520 EU/t · research Large Distillery 24 CWU/t](#m-a3))
- [Assembly Line · 112.5 s · 491 520 EU/t · research Large Distillery 24 CWU/t](#m-a3)

### Direct steps

- ZPM Fluid Drilling Rig (Abydos) → Gritty akreyrium fluid vein (Abydos, weight 19, yield 360 to 640, depleted 320) (drill)
- Gritty akreyrium fluid vein (Abydos, weight 19, yield 360 to 640, depleted 320) → Gritty akreyrium (280 B + 72 B) (fluid)
- Gritty akreyrium (280 B + 72 B) → ZPM hull · 12 UV circuit · 56 UHPIC · 16 prismalium gear · 8 ZPM pump · 4 ZPM motor · 2 ZPM field generator · 6 pure netherite gear · 4 B PBI · 280 B gritty akreyrium (280 B)
- Gritty akreyrium (280 B + 72 B) → ZPM hull · 6 UV circuit · 4 dense naquadria plate · 64 UHPIC · 4 huge duranium pipe · 4 pure netherite rotor · 4 small netherite gear · 24 ZPM pump · 8 B PBI · 72 B gritty akreyrium (72 B)

## How to build

1. Drawers first, one per input: hulls, frames, UV circuits (4 / 12 / 6), UV motors and pumps, ZPM pumps (8 and 24), prismalium gears, pure netherite gears and rotors, UHPIC chips, dense plates. Drums: soldering alloy, PBI, gritty akreyrium (several big drums). — `functionalstorage:oak_1`, `gtceu:uv_machine_hull`, `gtceu:zpm_machine_hull`, `gtceu:uhpic_chip`
2. Research for the rig: an EV fluid drilling rig in the Object Holder, 144 CWU/t at 245 760 EU/t → orb. Do it only after the Network Switch + HPCAs read 144 CWU/t. — `gtceu:research_station`, `gtceu:ev_fluid_drilling_rig`, `gtceu:data_orb`
3. Rig: Assembly Line, 20 s, 245 760 EU/t; place it over the Abydos vein (use a prospecting tool for the vein), connect a UV energy hatch and an output hatch with a Pipez fluid pipe to the drum. — `gtceu:assembly_line`, `start_core:zpm_fluid_drilling_rig`
4. Sifter first (24 CWU/t research, 80 s) then the destabiliser (24 CWU/t research, 112.5 s); both on a ZPM 4A hatch. Fluids by hatches: PBI and gritty akreyrium through the Pipez pipes with Keep Exact valves. — `gtceu:assembly_line`, `gtceu:cyclonic_sifter`, `gtceu:molten_destabiliser`
5. Output drawers Keep Exact 1 per controller. The sifter stays idle until the UHV page: it needs netherite reinforced meshes and UHV power for its recipe. — `gtceu:cyclonic_sifter`, `functionalstorage:oak_1`
6. Easy to miss: 280 B for a sifter plus 72 B for a destabiliser is 352 000 mB: plan storage (steel drums hold 32 B; the Abydos bulk tanks matter). — `gtceu:gritty_akreyrium_bucket`, `functionalstorage:oak_1`

## Tips

- Fluid drilling rig (kjs additions/multiblock\_recipes/fluid\_drill.js): Assembly Line, 400 ticks at VHA\[UV\] = 245 760 EU/t, UV hull + 4 enriched naquadah frames + 4 UV circuits + 4 UV motors + 4 UV pumps + 4 naquadah alloy gears + 1872 mB soldering alloy, STATION research of the EV fluid drilling rig at 144 CWU/t and VHA\[UV\]. 144 CWU/t is the highest research load of the UV era: nine advanced HPCA components, i.e. about four HPCAs through a Network Switch (uv\_research). The rig drills fluid veins of its dimension; the pack adds the Abydos vein ‘gritty akreyrium’ (kjs utils/fluid\_veins.js: dimension sgjourney:abydos, weight 19, yield 360 to 640, depletes by 2 per cycle with chance 1, depleted yield 320) next to the dense magma veins of Abydos (weight 25 and 28, yield 400 to 540).
- Cyclonic Sifter (UV): ZPM hull + 12 UV circuits + 56 UHPIC chips + 16 prismalium gears + 8 ZPM pumps + 4 ZPM motors + 2 ZPM field generators + 6 pure netherite gears; 4 B PBI + 280 B gritty akreyrium (280 000 mB!), 1600 ticks (80 s) at VA\[UV\] = 491 520 EU/t, research Large Sifting Funnel 24 CWU/t at VHA\[UV\]. Molten Destabiliser (UV): ZPM hull + 6 UV circuits + 4 dense naquadria plates + 64 UHPIC + 4 huge duranium pipes + 4 pure netherite rotors + 4 small pure netherite gears + 24 ZPM pumps; 8 B PBI + 72 B gritty akreyrium, 2250 ticks (112.5 s) at VA\[UV\], research Large Distillery 24 CWU/t. Both need 491 520 EU/t = a ZPM 4A hatch or a UV hatch on the Assembly Line.
- What the sifter does later (akreyrium.js, UHV page): cyclonic sifter recipe akreyrium\_sieving, 100 B gritty akreyrium + a netherite reinforced mesh (50 % chance kept) → 1 B lepton sparse akreyrium + crystalline and amorphous akreyrium, 1200 ticks at VA\[UHV\] x 0.8; manifold centrifuge then splits the lepton form into electron / muon / tau akreyrium (UHV). So the UV page ends at building the sifter and filling a 280 B tank.
- Order inside Abydos (verified, NOT a loop): both controllers need UV motors and pumps, and every UV motor carries a long magnetic dysprosium rod (UV primary magnet = dysprosium, tier\_data.js). Dysprosium has one source: the xenotime line (uv\_rare\_earth), and xenotime exists only in the Abydos ore veins (ore\_veins.js removes every other vein; abydos\_refractory\_metals\_vein carries xenotime, weight 3), plus 3 raw xenotime per refractory magma residue run later. So: mine xenotime by hand in Abydos -&gt; uv\_rare\_earth -&gt; dysprosium rod -&gt; UV motors and pumps -&gt; ZPM Fluid Drilling Rig (UV hull, VHA\[UV\], 144 CWU/t research) -&gt; drill the gritty akreyrium vein -&gt; Molten Destabiliser (ZPM hull, 6 UV circuits, 24 ZPM pumps, VA\[UV\], 24 CWU/t research) -&gt; magma. The dysprosium comes from the ore vein, not from the magma, so nothing waits on itself; both machines need a UV hatch to be assembled. The bacterial machines (uv\_bio2) come after this.
- Cost reality: 280 000 mB of gritty akreyrium for ONE sifter. At the vein yield of 360 to 640 per cycle that is hundreds of cycles of one rig (drill output per cycle: Unverified), so build several rigs on the same vein or find the vein with a big field. A Magmatic Drill (komaru modules, UV power, 250 MEU start) can output up to 4 096 000 mB of gritty akreyrium per run but needs kaleidoscope agitation serum, which is a later line.
- Sub-steps people skip: (1) rigs only drill in their own dimension: put the rig, a power line and an output pipe/drum in Abydos (needs the Abydos talisman, uv era step 1); (2) 24 ZPM pumps for the destabiliser come from the ZPM pump line, many at once; (3) prismalium gears (16): prismalium is a Nether line metal (Unverified route); (4) both controllers need a vacuum of UHPIC chips: 56 + 64 chips = 60 wafers.
- **Unverified** drill output per cycle, prismalium route, what the destabiliser recipe types do.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `start_core:zpm_fluid_drilling_rig` | 1 |
| `gtceu:uv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 24 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 20 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Feeds:** [Nether magma line: highly unstable nether magma → mystical magma → mythrillic, adamantamite and estaltadyne dusts (start of mythril, adamantine and estalt)](../uev/uev_nether.md)
- **Main source for:** `gtceu:gritty_akreyrium_bucket`, `start_core:zpm_fluid_drilling_rig`, `gtceu:cyclonic_sifter`, `gtceu:molten_destabiliser`
