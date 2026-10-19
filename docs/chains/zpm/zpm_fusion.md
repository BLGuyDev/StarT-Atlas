---
kind: chain
id: zpm_fusion
order: 1470
data:
  t: |-
    Fusion MK II (ZPM): URD superconducting coil → fusion coil, advanced reflector casing, then the reactor (needs 4 UV circuits) and darmstadtium
  inf: true
  "n":
    - - sc
      - Enriched naquadah frame · 16 URD double wire · 32 NbTi foil · 1728 mB trinium
      - g
      - functionalstorage:oak_1
      - - [Enriched naquadah frame, "gtceu:enriched_naquadah_frame"]
        - [URD double wire, "gtceu:uranium_rhodium_dinaquadide_double_wire"]
        - [NbTi foil, "gtceu:niobium_titanium_foil"]
        - [Trinium, "gtceu:trinium_bucket"]
    - [m1, "Assembler · 5 s · 122 880 EU/t · 2 coils per craft", m, "gtceu:large_assembler"]
    - [c1, Superconducting Coil, x, "gtceu:superconducting_coil"]
    - - fg
      - Coil · 2 IV field generator · IV pump · 4 basic reflector panel · 4 LuV circuit · naquadah pipe · 4 europium plate · 576 mB vanadium gallium
      - g
      - functionalstorage:oak_1
      - - [IV field generator, "gtceu:iv_field_generator"]
        - [IV pump, "gtceu:iv_electric_pump"]
        - [Basic neutron reflector, "kubejs:basic_neutron_reflector"]
        - [Europium plate, "gtceu:europium_plate"]
    - [m2, "Cleanroom Assembler · 7.5 s · 122 880 EU/t", m, "gtceu:large_assembler"]
    - [fc, Fusion Coil, x, "gtceu:fusion_coil"]
    - - rg
      - |-
        2 basic reflector casing · LuV field generator · 6 advanced panel · 4 VG cable · 12 trinium foil · 576 mB PBI
      - g
      - functionalstorage:oak_1
      - - [Basic reflector casing, "kubejs:basic_reflector_casing"]
        - [Advanced neutron reflector, "kubejs:advanced_neutron_reflector"]
        - [LuV field generator, "gtceu:luv_field_generator"]
        - [Trinium foil, "gtceu:trinium_foil"]
    - [m3, "Cleanroom Assembler · 20 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [rc, "2 Advanced Reflector Casing (tier 2)", x, "kubejs:advanced_reflector_casing"]
    - - fz
      - Fusion coil · 4 UV circuit · double naquadria plate · double europium plate · 2 LuV field generator · 96 UHPIC chip · 32 URD single wire · 1152 mB solder + 1152 mB VG
      - g
      - functionalstorage:oak_1
      - - [UHPIC chip, "gtceu:uhpic_chip"]
        - [Double naquadria plate, "gtceu:double_naquadria_plate"]
        - [Double europium plate, "gtceu:double_europium_plate"]
        - [URD single wire, "gtceu:uranium_rhodium_dinaquadide_single_wire"]
    - - al
      - |-
        Assembly Line · 67.5 s · 122 880 EU/t (station: LuV fusion reactor, 16 CWU/t)
      - m
      - gtceu:assembly_line
    - [fr, "ZPM Fusion Reactor (MK II)", x, "start_core:zpm_fusion_reactor"]
    - - dm
      - Run · 288 mB arsenic + 144 mB ruthenium · 28.8 s · 30 720 EU/t · start 200 MEU · reflector tier 2
      - m
      - start_core:zpm_fusion_reactor
    - [do, "144 mB darmstadtium", o, "gtceu:darmstadtium_bucket"]
  e:
    - [sc, m1, "1"]
    - [m1, c1, "2 / 5 s"]
    - [c1, m2, "1"]
    - [fg, m2, "1"]
    - [m2, fc, "1 / 7.5 s"]
    - [rg, m3, "1"]
    - [m3, rc, "2 / 20 s"]
    - [fc, al, "1"]
    - [fz, al, "1"]
    - [al, fr, "1 / 67.5 s"]
    - [rc, dm, tier-2 reflector]
    - [fr, dm, controller]
    - [dm, do, "144 mB / 28.8 s"]
  tips:
    - |-
      Superconducting coil, ZPM version (kjs systems/fusion/start_fusion_machines.js superconductingCoil(‘zpm’, URD, 2)): 1 enriched naquadah frame + 16 URD DOUBLE wire + 32 niobium titanium foil + 1728 mB molten trinium → 2 superconducting coils (2^(quant-1)), 100 ticks at VA[IV] x 4^2 = 122 880 EU/t. It is the same item as the LuV coil (ITBTC wire, 1 coil, 30 720 EU/t), but the URD version gives two per craft for the same trinium, so switch as soon as you have URD.
    - |-
      Fusion Coil (same file, fusionCoil): 1 superconducting coil + 2 IV field generators + 1 IV electric pump + 4 basic neutron reflector panels + 4 LuV circuits + 1 naquadah normal fluid pipe + 4 europium plates + 576 mB molten vanadium gallium, assembler in the CLEANROOM, 150 ticks at VA[ZPM] = 122 880 EU/t. The pack removes the GT fusion coil recipe. The fusion coil is also an ingredient of the MK II and MK III casings and reactors.
    - |-
      ZPM Fusion Reactor (start_fusion_machines.js zpm_fusion_reactor, the GT mk2 recipe is removed): 1 fusion coil + 4 circuits of the UV tag + 1 double naquadria plate + 1 double europium plate + 2 LuV field generators + 96 UHPIC chips (64 + 32) + 32 URD single wire, 1152 mB soldering alloy + 1152 mB molten vanadium gallium, Assembly Line 1350 ticks (67.5 s) at VA[ZPM] = 122 880 EU/t, station research of the LuV fusion reactor at 16 CWU/t (VHA[ZPM]). The UV circuit tag holds the crystal mainframe (zpm_crystal2 → 61 440 EU/t Assembly Line with station research of the crystal computer) and the runic assembly: so the MK II is the first thing that needs a UV circuit, which makes it the END of this era, not the middle.
    - |-
      What you get from it: the reflector fusion recipes (fusion_scaling.js) are keyed by reflector tier, not by reactor, and overclock when your reflectors are above the recipe’s tier. Tier 1 (basic reflector casing, already in luv_fusion): europium, helium plasma, radon (144 mB gold + 100 mB mercury → 1 B radon, 30 720 EU/t, 28.8 s, 200 MEU), lutetium. Tier 2 (advanced reflector casing, below): DARMSTADTIUM (288 mB arsenic + 144 mB ruthenium → 144 mB, 30 720 EU/t, 28.8 s, 200 MEU), duranium (gallium + radon), nitrogen, oxygen, argon and tin plasma. Darmstadtium is the UV hull material, so the tier-2 casing is the UV prerequisite. Tier 3 (complex casing, built in the UV era): nickel plasma, tritanium, iron plasma, americium, neutronium; of these only neutronium (600 MEU start) needs the MK III, while tritanium (200 MEU) runs on this MK II once you have T3 reflectors. Verified in start_core: the reactor buffer caps at 160 MEU (MK I), 320 MEU (MK II) and 640 MEU (MK III), and a recipe cannot start above the cap; a recipe whose minimum reflector tier is higher than your reflectors does not run; a reflector ABOVE the recipe tier raises the reactor overclock cap by the difference in tiers (each overclock doubles EU/t and halves the time); all reflectors of one reactor must be the same tier. Argon plasma (tier 2, 180 MEU) is therefore a MK II recipe (zpm_power). The start energy (150 to 200 MEU) needs the Power Substation (luv_power).
    - |-
      Advanced Reflector Casing (reflectorBlock tier 2): 2 basic reflector casings + 1 LuV field generator + 6 advanced neutron reflector panels + 4 vanadium gallium single cables + 12 trinium foil + 576 mB PBI → 2 casings, cleanroom assembler, 400 ticks at VA[EV] x 4^2 = 30 720 EU/t. Advanced neutron reflector panel (reflectorPanel tier 2): 1 osmiridium plate + 2 double naquadah plates + 1 basic neutron reflector + 1152 mB soldering alloy, assembler in the cleanroom, 1000 ticks at VHA[IV]. So each tier-2 casing needs a full set of tier-1 parts again plus naquadah double plates (2 ingots each) and 6 trinium foil.
    - |-
      Fusion casings (fusionCasing): MK II casing = ZPM hull + fusion coil + 2 ZPM voltage coils + 1 LuV field generator + 6 advanced reflector panels + 576 mB PBI → 2 casings, cleanroom, 160 ticks at VA[LuV] = 30 720 EU/t. The MK I casing is the same one tier down (LuV hull + superconducting coil + 2 LuV voltage coils + IV field generator + 6 basic panels + 288 mB PBI). The casing counts of the reactor structure are not in the extracted multis: Unverified (read the controller’s structure preview).
    - |-
      Sub-steps people skip: (1) the UV circuit is not a ZPM circuit: stock 4 crystal mainframes (8 crystal computers) before you queue the reactor; (2) 96 UHPIC chips = 48 wafers = 48 HPIC wafers: the chip line must run for hours (luv_fusion chain); (3) the research orb needs the LuV fusion reactor in the Object Holder; do not scrap your MK I; (4) europium stays the first customer: the MK I reactor must keep running while you build the MK II; (5) a double naquadria plate is 2 naquadria ingots from zpm_naq_products.
    - |-
      Structure (StarTFusionMachines pattern): controller, fusion casing of the reactor MK, fusion glass, fusion coils, energy hatch spots, and reflector slots in the inner ring next to the glass (all the same reflector type). Nothing in the pattern forbids two reactors sharing a wall, but the pack does not document it, so plan separate rings. Unverified: the reactor structure size.
  b:
    - ["start_core:zpm_fusion_reactor", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:research_station", 1]
    - ["kubejs:advanced_reflector_casing", 16]
    - ["gtceu:power_substation", 1]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:enriched_naquadah_frame
        - gtceu:uranium_rhodium_dinaquadide_double_wire
        - gtceu:europium_plate
      t: |-
        Drawers first, one per input: enriched naquadah frames, URD double wire, NbTi foil, europium plates, IV field generators, pumps, basic panels, naquadah pipes, trinium foil, VG cables, UHPIC chips. Drums: trinium, vanadium gallium, PBI, soldering alloy. Every machine behind its own router with Item Filters and a Robot Arm cover in Keep Exact mode.
    - i: ["gtceu:large_assembler", "gtceu:superconducting_coil", "gtceu:trinium_bucket"]
      t: |-
        Coil: the Large Assembler on a LuV 4A hatch (122 880 EU/t), enriched naquadah frame + 16 URD double wire + 32 NbTi foil + 1728 mB molten trinium → 2 superconducting coils in 5 s.
    - i: ["gtceu:large_assembler", "gtceu:fusion_coil", "gtceu:europium_plate"]
      t: |-
        Fusion coil (cleanroom): coil + 2 IV field generators + IV pump + 4 basic panels + 4 LuV circuits + naquadah pipe + 4 europium plates + 576 mB molten VG → 1 fusion coil in 7.5 s at 122 880 EU/t.
    - i: ["gtceu:large_assembler", "kubejs:advanced_reflector_casing", "kubejs:advanced_neutron_reflector"]
      t: |-
        Advanced casings: first the advanced panels (osmiridium plate + 2 double naquadah plates + a basic panel + 1152 mB solder, 50 s each), then the casing assembler in the cleanroom (2 basic casings + LuV field generator + 6 panels + 4 cables + 12 trinium foil + 576 mB PBI → 2 casings, 20 s at 30 720 EU/t).
    - i: ["gtceu:assembly_line", "start_core:zpm_fusion_reactor", "gtceu:fusion_coil"]
      t: |-
        Reactor: research orb = station research of the LuV fusion reactor (16 CWU/t); Assembly Line buses: fusion coil, 4 UV circuits, double naquadria plate, double europium plate, 2 LuV field generators, 96 UHPIC chips, 32 URD single wire; 1152 mB solder + 1152 mB VG. 67.5 s.
    - i: ["start_core:zpm_fusion_reactor", "gtceu:darmstadtium_bucket", "gtceu:ruthenium_dust"]
      t: |-
        First runs: darmstadtium (288 mB arsenic + 144 mB ruthenium → 144 mB, 28.8 s) with tier-2 reflectors, output hatch into a drum Keep Exact so a stuck valve does not eat the energy buffer; also helium plasma and radon for the quantum stars.
    - i: ["gtceu:power_substation", "start_core:zpm_fusion_reactor"]
      t: |-
        Easy to miss: the start energy (150 to 200 MEU) must come from a buffer; size the Power Substation (luv_power) before the first MK II run. And keep the MK I reactor on europium meanwhile.
---
# Fusion MK II (ZPM): URD superconducting coil → fusion coil, advanced reflector casing, then the reactor (needs 4 UV circuits) and darmstadtium

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_fusion` · **Tags:** Infinite source

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Fusion MK II (darmstadtium)](../../plan/p13.md#fusion2)

**Tips:** 8

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-m1">
<div class="gt-head"><span class="gt-mname">Assembler · 5 s · 122 880 EU/t · 2 coils per craft</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Enriched naquadah frame · 16 URD double wire · 32 NbTi foil · 1728 mB trinium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Enriched naquadah frame · 16 URD double wire · 32 NbTi foil · 1728 mB trinium</span><span class="gt-sub"><span>Enriched naquadah frame</span><span>URD double wire</span><span>NbTi foil</span><span>Trinium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Superconducting Coil (gtceu:superconducting_coil) - 2 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__superconducting_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superconducting Coil</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-m2">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 7.5 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Superconducting Coil (gtceu:superconducting_coil) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__superconducting_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superconducting Coil</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Coil · 2 IV field generator · IV pump · 4 basic reflector panel · 4 LuV circuit · naquadah pipe · 4 europium plate · 576 mB vanadium gallium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Coil · 2 IV field generator · IV pump · 4 basic reflector panel · 4 LuV circuit · naquadah pipe · 4 europium plate · 576 mB vanadium gallium</span><span class="gt-sub"><span>IV field generator</span><span>IV pump</span><span>Basic neutron reflector</span><span>Europium plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">7.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Fusion Coil (gtceu:fusion_coil) - 1 / 7.5 s"><img class="gt-ico" src="../../assets/icons/gtceu__fusion_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fusion Coil</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">Cleanroom Assembler · 20 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="2 basic reflector casing · LuV field generator · 6 advanced panel · 4 VG cable · 12 trinium foil · 576 mB PBI (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 basic reflector casing · LuV field generator · 6 advanced panel · 4 VG cable · 12 trinium foil · 576 mB PBI</span><span class="gt-sub"><span>Basic reflector casing</span><span>Advanced neutron reflector</span><span>LuV field generator</span><span>Trinium foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Advanced Reflector Casing (tier 2) (kubejs:advanced_reflector_casing) - 2 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__advanced_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Reflector Casing</span><span class="gt-note">2 Advanced Reflector Casing (tier 2)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 67.5 s · 122 880 EU/t (station: LuV fusion reactor, 16 CWU/t)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Fusion Coil (gtceu:fusion_coil) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__fusion_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fusion Coil</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="Fusion coil · 4 UV circuit · double naquadria plate · double europium plate · 2 LuV field generator · 96 UHPIC chip · 32 URD single wire · 1152 mB solder + 1152 mB VG (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Fusion coil · 4 UV circuit · double naquadria plate · double europium plate · 2 LuV field generator · 96 UHPIC chip · 32 URD single wire · 1152 mB solder + 1152 mB VG</span><span class="gt-sub"><span>UHPIC chip</span><span>Double naquadria plate</span><span>Double europium plate</span><span>URD single wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">67.5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="ZPM Fusion Reactor (MK II) (start_core:zpm_fusion_reactor) - 1 / 67.5 s"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">ZPM Fusion Reactor (MK II)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-zpm" id="m-dm">
<div class="gt-head"><span class="gt-mname">Run · 288 mB arsenic + 144 mB ruthenium · 28.8 s · 30 720 EU/t · start 200 MEU · reflector tier 2</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Advanced Reflector Casing (tier 2) (kubejs:advanced_reflector_casing) - tier-2 reflector"><img class="gt-ico" src="../../assets/icons/kubejs__advanced_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Advanced Reflector Casing</span><span class="gt-note">2 Advanced Reflector Casing (tier 2)</span><b class="gt-q">tier-2 reflector</b></span><span class="gt-slot" title="ZPM Fusion Reactor (MK II) (start_core:zpm_fusion_reactor) - controller"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">ZPM Fusion Reactor (MK II)</span><b class="gt-q">controller</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span><span class="gt-stat">28.8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="144 mB darmstadtium (gtceu:darmstadtium_bucket) - 144 mB / 28.8 s"><img class="gt-ico" src="../../assets/icons/gtceu__darmstadtium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Darmstadtium Bucket</span><span class="gt-note">144 mB darmstadtium</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
</div>

## Flow

- [Assembler · 5 s · 122 880 EU/t · 2 coils per craft](#m-m1) → [Cleanroom Assembler · 7.5 s · 122 880 EU/t](#m-m2) → [Assembly Line · 67.5 s · 122 880 EU/t (station: LuV fusion reactor, 16 CWU/t)](#m-al) → [Run · 288 mB arsenic + 144 mB ruthenium · 28.8 s · 30 720 EU/t · start 200 MEU · reflector tier 2](#m-dm)
- [Cleanroom Assembler · 20 s · 30 720 EU/t](#m-m3) → [Run · 288 mB arsenic + 144 mB ruthenium · 28.8 s · 30 720 EU/t · start 200 MEU · reflector tier 2](#m-dm)

## How to build

1. Drawers first, one per input: enriched naquadah frames, URD double wire, NbTi foil, europium plates, IV field generators, pumps, basic panels, naquadah pipes, trinium foil, VG cables, UHPIC chips. Drums: trinium, vanadium gallium, PBI, soldering alloy. Every machine behind its own router with Item Filters and a Robot Arm cover in Keep Exact mode. — `functionalstorage:oak_1`, `gtceu:enriched_naquadah_frame`, `gtceu:uranium_rhodium_dinaquadide_double_wire`, `gtceu:europium_plate`
2. Coil: the Large Assembler on a LuV 4A hatch (122 880 EU/t), enriched naquadah frame + 16 URD double wire + 32 NbTi foil + 1728 mB molten trinium → 2 superconducting coils in 5 s. — `gtceu:large_assembler`, `gtceu:superconducting_coil`, `gtceu:trinium_bucket`
3. Fusion coil (cleanroom): coil + 2 IV field generators + IV pump + 4 basic panels + 4 LuV circuits + naquadah pipe + 4 europium plates + 576 mB molten VG → 1 fusion coil in 7.5 s at 122 880 EU/t. — `gtceu:large_assembler`, `gtceu:fusion_coil`, `gtceu:europium_plate`
4. Advanced casings: first the advanced panels (osmiridium plate + 2 double naquadah plates + a basic panel + 1152 mB solder, 50 s each), then the casing assembler in the cleanroom (2 basic casings + LuV field generator + 6 panels + 4 cables + 12 trinium foil + 576 mB PBI → 2 casings, 20 s at 30 720 EU/t). — `gtceu:large_assembler`, `kubejs:advanced_reflector_casing`, `kubejs:advanced_neutron_reflector`
5. Reactor: research orb = station research of the LuV fusion reactor (16 CWU/t); Assembly Line buses: fusion coil, 4 UV circuits, double naquadria plate, double europium plate, 2 LuV field generators, 96 UHPIC chips, 32 URD single wire; 1152 mB solder + 1152 mB VG. 67.5 s. — `gtceu:assembly_line`, `start_core:zpm_fusion_reactor`, `gtceu:fusion_coil`
6. First runs: darmstadtium (288 mB arsenic + 144 mB ruthenium → 144 mB, 28.8 s) with tier-2 reflectors, output hatch into a drum Keep Exact so a stuck valve does not eat the energy buffer; also helium plasma and radon for the quantum stars. — `start_core:zpm_fusion_reactor`, `gtceu:darmstadtium_bucket`, `gtceu:ruthenium_dust`
7. Easy to miss: the start energy (150 to 200 MEU) must come from a buffer; size the Power Substation (luv\_power) before the first MK II run. And keep the MK I reactor on europium meanwhile. — `gtceu:power_substation`, `start_core:zpm_fusion_reactor`

## Tips

- Superconducting coil, ZPM version (kjs systems/fusion/start\_fusion\_machines.js superconductingCoil(‘zpm’, URD, 2)): 1 enriched naquadah frame + 16 URD DOUBLE wire + 32 niobium titanium foil + 1728 mB molten trinium → 2 superconducting coils (2^(quant-1)), 100 ticks at VA\[IV\] x 4^2 = 122 880 EU/t. It is the same item as the LuV coil (ITBTC wire, 1 coil, 30 720 EU/t), but the URD version gives two per craft for the same trinium, so switch as soon as you have URD.
- Fusion Coil (same file, fusionCoil): 1 superconducting coil + 2 IV field generators + 1 IV electric pump + 4 basic neutron reflector panels + 4 LuV circuits + 1 naquadah normal fluid pipe + 4 europium plates + 576 mB molten vanadium gallium, assembler in the CLEANROOM, 150 ticks at VA\[ZPM\] = 122 880 EU/t. The pack removes the GT fusion coil recipe. The fusion coil is also an ingredient of the MK II and MK III casings and reactors.
- ZPM Fusion Reactor (start\_fusion\_machines.js zpm\_fusion\_reactor, the GT mk2 recipe is removed): 1 fusion coil + 4 circuits of the UV tag + 1 double naquadria plate + 1 double europium plate + 2 LuV field generators + 96 UHPIC chips (64 + 32) + 32 URD single wire, 1152 mB soldering alloy + 1152 mB molten vanadium gallium, Assembly Line 1350 ticks (67.5 s) at VA\[ZPM\] = 122 880 EU/t, station research of the LuV fusion reactor at 16 CWU/t (VHA\[ZPM\]). The UV circuit tag holds the crystal mainframe (zpm\_crystal2 → 61 440 EU/t Assembly Line with station research of the crystal computer) and the runic assembly: so the MK II is the first thing that needs a UV circuit, which makes it the END of this era, not the middle.
- What you get from it: the reflector fusion recipes (fusion\_scaling.js) are keyed by reflector tier, not by reactor, and overclock when your reflectors are above the recipe’s tier. Tier 1 (basic reflector casing, already in luv\_fusion): europium, helium plasma, radon (144 mB gold + 100 mB mercury → 1 B radon, 30 720 EU/t, 28.8 s, 200 MEU), lutetium. Tier 2 (advanced reflector casing, below): DARMSTADTIUM (288 mB arsenic + 144 mB ruthenium → 144 mB, 30 720 EU/t, 28.8 s, 200 MEU), duranium (gallium + radon), nitrogen, oxygen, argon and tin plasma. Darmstadtium is the UV hull material, so the tier-2 casing is the UV prerequisite. Tier 3 (complex casing, built in the UV era): nickel plasma, tritanium, iron plasma, americium, neutronium; of these only neutronium (600 MEU start) needs the MK III, while tritanium (200 MEU) runs on this MK II once you have T3 reflectors. Verified in start\_core: the reactor buffer caps at 160 MEU (MK I), 320 MEU (MK II) and 640 MEU (MK III), and a recipe cannot start above the cap; a recipe whose minimum reflector tier is higher than your reflectors does not run; a reflector ABOVE the recipe tier raises the reactor overclock cap by the difference in tiers (each overclock doubles EU/t and halves the time); all reflectors of one reactor must be the same tier. Argon plasma (tier 2, 180 MEU) is therefore a MK II recipe (zpm\_power). The start energy (150 to 200 MEU) needs the Power Substation (luv\_power).
- Advanced Reflector Casing (reflectorBlock tier 2): 2 basic reflector casings + 1 LuV field generator + 6 advanced neutron reflector panels + 4 vanadium gallium single cables + 12 trinium foil + 576 mB PBI → 2 casings, cleanroom assembler, 400 ticks at VA\[EV\] x 4^2 = 30 720 EU/t. Advanced neutron reflector panel (reflectorPanel tier 2): 1 osmiridium plate + 2 double naquadah plates + 1 basic neutron reflector + 1152 mB soldering alloy, assembler in the cleanroom, 1000 ticks at VHA\[IV\]. So each tier-2 casing needs a full set of tier-1 parts again plus naquadah double plates (2 ingots each) and 6 trinium foil.
- Fusion casings (fusionCasing): MK II casing = ZPM hull + fusion coil + 2 ZPM voltage coils + 1 LuV field generator + 6 advanced reflector panels + 576 mB PBI → 2 casings, cleanroom, 160 ticks at VA\[LuV\] = 30 720 EU/t. The MK I casing is the same one tier down (LuV hull + superconducting coil + 2 LuV voltage coils + IV field generator + 6 basic panels + 288 mB PBI). The casing counts of the reactor structure are not in the extracted multis: Unverified (read the controller’s structure preview).
- Sub-steps people skip: (1) the UV circuit is not a ZPM circuit: stock 4 crystal mainframes (8 crystal computers) before you queue the reactor; (2) 96 UHPIC chips = 48 wafers = 48 HPIC wafers: the chip line must run for hours (luv\_fusion chain); (3) the research orb needs the LuV fusion reactor in the Object Holder; do not scrap your MK I; (4) europium stays the first customer: the MK I reactor must keep running while you build the MK II; (5) a double naquadria plate is 2 naquadria ingots from zpm\_naq\_products.
- Structure (StarTFusionMachines pattern): controller, fusion casing of the reactor MK, fusion glass, fusion coils, energy hatch spots, and reflector slots in the inner ring next to the glass (all the same reflector type). Nothing in the pattern forbids two reactors sharing a wall, but the pack does not document it, so plan separate rings. Unverified: the reactor structure size.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:zpm_fusion_reactor` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:large_assembler` | 1 |
| `gtceu:research_station` | 1 |
| `kubejs:advanced_reflector_casing` | 16 |
| `gtceu:power_substation` | 1 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Feeds:** [UV Machine Hull: darmstadtium casing + 2 yttrium barium cuprate cables (PPS foil + PVC foil + silicone) + 288 mB PEEK](../uv/uv_hull.md), [ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines](zpm_argon.md)
- **Main source for:** `start_core:zpm_fusion_reactor`, `gtceu:fusion_coil`, `kubejs:advanced_reflector_casing`, `kubejs:advanced_neutron_reflector`, `gtceu:darmstadtium_bucket`, `gtceu:darmstadtium_ingot`
