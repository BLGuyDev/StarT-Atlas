---
kind: chain
id: uiv_threading
order: 2210
data:
  t: |-
    Threading: prismalic helix core → prisma helical nucleus → Threading Controller (every threaded multiblock eats nuclei and UXV circuits)
  inf: true
  "n":
    - - g1
      - |-
        Prismalic helix core: 1 void frame · 4 draco advanced soc · 1 runic wave generator · 2 prismalic neutron reflector · 32 fine ancient runicalium wire · 32 fine stellarium wire · 32 fine melodium wire · 5 000 mB utopian akreyrium · 3 456 mB borealic concentrate · 2 880 mB naquadated soldering alloy
      - g
      - functionalstorage:oak_1
      - - [void frame, "gtceu:void_frame"]
        - [draco advanced soc, "kubejs:draco_advanced_soc"]
        - [runic wave generator, "kubejs:runic_wave_generator"]
        - [prismalic neutron reflector, "kubejs:prismalic_neutron_reflector"]
        - [fine ancient runicalium wire, "gtceu:fine_ancient_runicalium_wire"]
        - [fine stellarium wire, "gtceu:fine_stellarium_wire"]
    - [a1, "Assembly Line · 45 s · 3 932 160 EU/t · research Core Casing 160 CWU/t", m, "gtceu:assembly_line"]
    - [hc, "Prismalic Helix Core (+ 8 more fine wires, 32 each)", x, "kubejs:prismalic_helix_core"]
    - - g2
      - |-
        Prisma helical nucleus: 1 nyanium frame · 3 prismalic helix core · 2 dense hvga steel plate · 2 soul ascendant cuperite rod · 2 uiv sensor · 32 uipic chip · 5 472 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 4 384 mB naquadated soldering alloy · 2 500 mB dragon breath
      - g
      - functionalstorage:oak_1
      - - [nyanium frame, "gtceu:nyanium_frame"]
        - [prismalic helix core, "kubejs:prismalic_helix_core"]
        - [dense hvga steel plate, "gtceu:dense_hvga_steel_plate"]
        - [soul ascendant cuperite rod, "gtceu:soul_ascendant_cuperite_rod"]
        - [uiv sensor, "gtceu:uiv_sensor"]
        - [uipic chip, "kubejs:uipic_chip"]
    - [a2, "Assembly Line · 60 s · 15 728 640 EU/t · research Helix Core 192 CWU/t", m, "gtceu:assembly_line"]
    - [nu, Prisma Helical Nucleus, x, "kubejs:prisma_helical_nucleus"]
    - - g3
      - |-
        Threading controller: 1 uiv absolute parallel hatch · 2 abyssal processor mainframe · 2 prisma helical nucleus · 8 lepton resonant thallium antimonide double cable · 27 360 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 21 920 mB naquadated soldering alloy · 5 000 mB pure dragon breath
      - g
      - functionalstorage:oak_1
      - - [uiv absolute parallel hatch, "start_core:uiv_absolute_parallel_hatch"]
        - [abyssal processor mainframe, "kubejs:abyssal_processor_mainframe"]
        - [prisma helical nucleus, "kubejs:prisma_helical_nucleus"]
        - [lepton resonant thallium antimonide double cable, "gtceu:lepton_resonant_thallium_antimonide_double_cable"]
    - [a3, "Assembly Line · 75 s · 31 457 280 EU/t · research Nucleus 216 CWU/t", m, "gtceu:assembly_line"]
    - [tc, Threading Controller, o, "start_core:threading_controller"]
  e:
    - [g1, a1, "1"]
    - [a1, hc, "1 / 45 s"]
    - [hc, g2, "3"]
    - [g2, a2, "1"]
    - [a2, nu, "1 / 60 s"]
    - [nu, g3, "2"]
    - [g3, a3, "1"]
    - [a3, tc, "1 / 75 s"]
  tips:
    - |-
      Source: kjs systems/threading.js. Prismalic helix core: Assembly Line 900 ticks, VHA[UEV] = 3 932 160 EU/t, research Core Casing (VHA[UHV], 160 CWU/t): void frame + 4 draco advanced SoCs + 1 runic wave generator + 2 prismalic neutron reflector panels + 32 each of 11 fine wires (ancient runicalium, stellarium, melodium, prismalium, dragonsteel, twinite, shellite, enderium, lumium, signalum, soul infused) + 5000 mB utopian akreyrium + 3456 mB borealic concentrate + 2880 mB naquadated soldering alloy. The prismalic panel is the tier 7 reflector panel (draco abyssal plate + double hvga steel + a draconic panel, Abyssal Containment Room cleanroom): so the helix core already needs the Abyssal Containment Room (uiv_circuits).
    - |-
      Nucleus: 1200 ticks, VHA[UIV], research helix core 192 CWU/t: nyanium frame + 3 helix cores + 2 dense hvga steel plates + 2 soul ascendant cuperite rods + 2 UIV sensors + 32 UIPIC chips, 5472 mB PEDOT:PSS + 4384 mB soldering + 2500 mB dragon breath. Threading controller: 1500 ticks, VA[UIV], research nucleus 216 CWU/t: UIV absolute parallel hatch + 2 UXV circuits (abyssal processor mainframes) + 2 nuclei + 8 lepton resonant thallium antimonide double cables, 27 360 mB PEDOT:PSS + 21 920 mB soldering + 5000 mB pure dragon breath. So one controller = 6 helix cores = 6 x 11 x 32 fine wires.
    - |-
      Threaded machines (assemblyThreadMachine, 18 000 ticks = 15 min at VHA[UIV] unless noted, station research of the UIV singleblock of the same kind, 240 CWU/t): each needs a core frame, 4 x N UXV circuits and N nuclei, where N is its nexus amount: aqueous transformation processing center N 8 (8 UIV extractors, canners, solidifiers), ascendant engraving matrix 9, byteforce unified incomparable logistics depot 12, electro magnetic material ripper 10, material annihilation array 8, molecular inducing xanadu 8, subatomic particle lattice isolation terminal 12, superior particulate isolation nexus 8, further machines of the same pattern in the file that this guide did not read (benders, compressors, hammers, presses, packers, macerators, arc furnaces), and the multithreaded component synthesis forge (core casing, N 36 = 144 UXV circuits and 36 nuclei, 72 component nexus + 72 component part hubs + 40 UIV assemblers + 40 UIV scanners + 640 UIPIC chips, 36 000 ticks at VA[UIV]).
    - |-
      What threading is for: the era page says speed, efficiency, parallels and multi-thread (stat-point multiblocks). The pack mod docs for the stats are not in the scripts: Unverified how the stat points are assigned. The cost sizes mean only one or two threaded machines are realistic in the first pass: choose by what you need (the forge for 64-at-once components, the byteforce depot for assembling, the material annihilation array for ores).
    - |-
      Sub-steps people skip: (1) 6 helix cores per nucleus-pair chain: the 11 fine wires (including soul infused and shellite) must be made first: 352 fine wires per core set; (2) abyssal processor mainframes (UXV circuits) come from the Draco Circuit Assembler (uiv_circuits): a threaded machine eats 32 to 144; (3) the UIV absolute parallel hatch (uiv_hatches) needs UXV circuits and UIPIC chips too; (4) the pure dragon breath for the controller has no traced source.
    - |-
      Unverified: all stat-point mechanics, the machines of the file that were not read, and the pure dragon breath source.
  b:
    - ["gtceu:assembly_line", 1]
    - ["gtceu:research_station", 1]
    - ["gtceu:uhv_input_bus", 6]
    - ["gtceu:uhv_input_hatch", 4]
    - ["functionalstorage:oak_1", 20]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 6]
  how:
    - i: ["functionalstorage:oak_1", "kubejs:draco_advanced_soc", "gtceu:fine_stellarium_wire"]
      t: |-
        Drawers first: void frames, draco advanced SoCs, runic wave generators, prismalic panels, 11 fine wires (Keep Exact 64 each), nyanium frames, UIPIC chips. Drums: utopian akreyrium, borealic concentrate, soldering alloy, PEDOT:PSS, dragon breath.
    - i: ["gtceu:assembly_line", "kubejs:prismalic_helix_core"]
      t: |-
        Helix cores: 45 s each at 3 932 160 EU/t; scan the Core Casing first. Make 6 for the controller path.
    - i: ["gtceu:assembly_line", "kubejs:prisma_helical_nucleus"]
      t: |-
        Nuclei: 3 helix cores + frame + plates + rods + sensors + 32 UIPIC chips, 60 s at 15 728 640 EU/t. Output Keep Exact 4.
    - i: ["gtceu:assembly_line", "start_core:threading_controller"]
      t: |-
        Controller: absolute parallel hatch + 2 UXV circuits + 2 nuclei + 8 double cables, 75 s. Pure dragon breath 5000 mB by Pipez fluid pipe.
    - i: ["functionalstorage:oak_1", "kubejs:prisma_helical_nucleus"]
      t: |-
        Nuclei stay in a drawer: each threaded multiblock needs 8 to 36 of them and 4 UXV circuits per nucleus.
---
# Threading: prismalic helix core → prisma helical nucleus → Threading Controller (every threaded multiblock eats nuclei and UXV circuits)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uiv_threading` · **Tags:** Infinite source, Unverified

**Era setup:** [UIV · End &amp; Draconic](../../eras/uiv.md)

**Plan modules:** [UIV controllers, threading, fusion](../../plan/p19.md#uivmulti)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 45 s · 3 932 160 EU/t · research Core Casing 160 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Prismalic helix core: 1 void frame · 4 draco advanced soc · 1 runic wave generator · 2 prismalic neutron reflector · 32 fine ancient runicalium wire · 32 fine stellarium wire · 32 fine melodium wire · 5 000 mB utopian akreyrium · 3 456 mB borealic concentrate · 2 880 mB naquadated soldering alloy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Prismalic helix core: 1 void frame · 4 draco advanced soc · 1 runic wave generator · 2 prismalic neutron reflector · 32 fine ancient runicalium wire · 32 fine stellarium wire · 32 fine melodium wire · 5 000 mB utopian akreyrium · 3 456 mB borealic concentrate · 2 880 mB naquadated soldering alloy</span><span class="gt-sub"><span>void frame</span><span>draco advanced soc</span><span>runic wave generator</span><span>prismalic neutron reflector</span><span>fine ancient runicalium wire</span><span>fine stellarium wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Prismalic Helix Core (+ 8 more fine wires, 32 each) (kubejs:prismalic_helix_core) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/kubejs__prismalic_helix_core.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Prismalic Helix Core</span><span class="gt-note">Prismalic Helix Core (+ 8 more fine wires, 32 each)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 15 728 640 EU/t · research Helix Core 192 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Prisma helical nucleus: 1 nyanium frame · 3 prismalic helix core · 2 dense hvga steel plate · 2 soul ascendant cuperite rod · 2 uiv sensor · 32 uipic chip · 5 472 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 4 384 mB naquadated soldering alloy · 2 500 mB dragon breath (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Prisma helical nucleus: 1 nyanium frame · 3 prismalic helix core · 2 dense hvga steel plate · 2 soul ascendant cuperite rod · 2 uiv sensor · 32 uipic chip · 5 472 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 4 384 mB naquadated soldering alloy · 2 500 mB dragon breath</span><span class="gt-sub"><span>nyanium frame</span><span>prismalic helix core</span><span>dense hvga steel plate</span><span>soul ascendant cuperite rod</span><span>uiv sensor</span><span>uipic chip</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Prisma Helical Nucleus (kubejs:prisma_helical_nucleus) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/kubejs__prisma_helical_nucleus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Prisma Helical Nucleus</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 75 s · 31 457 280 EU/t · research Nucleus 216 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Threading controller: 1 uiv absolute parallel hatch · 2 abyssal processor mainframe · 2 prisma helical nucleus · 8 lepton resonant thallium antimonide double cable · 27 360 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 21 920 mB naquadated soldering alloy · 5 000 mB pure dragon breath (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Threading controller: 1 uiv absolute parallel hatch · 2 abyssal processor mainframe · 2 prisma helical nucleus · 8 lepton resonant thallium antimonide double cable · 27 360 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 21 920 mB naquadated soldering alloy · 5 000 mB pure dragon breath</span><span class="gt-sub"><span>uiv absolute parallel hatch</span><span>abyssal processor mainframe</span><span>prisma helical nucleus</span><span>lepton resonant thallium antimonide double cable</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">75 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Threading Controller (start_core:threading_controller) - 1 / 75 s"><img class="gt-ico" src="../../assets/icons/start_core__threading_controller.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Threading Controller</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 45 s · 3 932 160 EU/t · research Core Casing 160 CWU/t](#m-a1) → [Assembly Line · 60 s · 15 728 640 EU/t · research Helix Core 192 CWU/t](#m-a2) → [Assembly Line · 75 s · 31 457 280 EU/t · research Nucleus 216 CWU/t](#m-a3)

### Direct steps

- Prismalic Helix Core (+ 8 more fine wires, 32 each) → Prisma helical nucleus: 1 nyanium frame · 3 prismalic helix core · 2 dense hvga steel plate · 2 soul ascendant cuperite rod · 2 uiv sensor · 32 uipic chip · 5 472 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 4 384 mB naquadated soldering alloy · 2 500 mB dragon breath (3)
- Prisma Helical Nucleus → Threading controller: 1 uiv absolute parallel hatch · 2 abyssal processor mainframe · 2 prisma helical nucleus · 8 lepton resonant thallium antimonide double cable · 27 360 mB poly 34 ethylenedioxythiophene polystyrene sulfonate · 21 920 mB naquadated soldering alloy · 5 000 mB pure dragon breath (2)

## How to build

1. Drawers first: void frames, draco advanced SoCs, runic wave generators, prismalic panels, 11 fine wires (Keep Exact 64 each), nyanium frames, UIPIC chips. Drums: utopian akreyrium, borealic concentrate, soldering alloy, PEDOT:PSS, dragon breath. — `functionalstorage:oak_1`, `kubejs:draco_advanced_soc`, `gtceu:fine_stellarium_wire`
2. Helix cores: 45 s each at 3 932 160 EU/t; scan the Core Casing first. Make 6 for the controller path. — `gtceu:assembly_line`, `kubejs:prismalic_helix_core`
3. Nuclei: 3 helix cores + frame + plates + rods + sensors + 32 UIPIC chips, 60 s at 15 728 640 EU/t. Output Keep Exact 4. — `gtceu:assembly_line`, `kubejs:prisma_helical_nucleus`
4. Controller: absolute parallel hatch + 2 UXV circuits + 2 nuclei + 8 double cables, 75 s. Pure dragon breath 5000 mB by Pipez fluid pipe. — `gtceu:assembly_line`, `start_core:threading_controller`
5. Nuclei stay in a drawer: each threaded multiblock needs 8 to 36 of them and 4 UXV circuits per nucleus. — `functionalstorage:oak_1`, `kubejs:prisma_helical_nucleus`

## Tips

- Source: kjs systems/threading.js. Prismalic helix core: Assembly Line 900 ticks, VHA\[UEV\] = 3 932 160 EU/t, research Core Casing (VHA\[UHV\], 160 CWU/t): void frame + 4 draco advanced SoCs + 1 runic wave generator + 2 prismalic neutron reflector panels + 32 each of 11 fine wires (ancient runicalium, stellarium, melodium, prismalium, dragonsteel, twinite, shellite, enderium, lumium, signalum, soul infused) + 5000 mB utopian akreyrium + 3456 mB borealic concentrate + 2880 mB naquadated soldering alloy. The prismalic panel is the tier 7 reflector panel (draco abyssal plate + double hvga steel + a draconic panel, Abyssal Containment Room cleanroom): so the helix core already needs the Abyssal Containment Room (uiv\_circuits).
- Nucleus: 1200 ticks, VHA\[UIV\], research helix core 192 CWU/t: nyanium frame + 3 helix cores + 2 dense hvga steel plates + 2 soul ascendant cuperite rods + 2 UIV sensors + 32 UIPIC chips, 5472 mB PEDOT:PSS + 4384 mB soldering + 2500 mB dragon breath. Threading controller: 1500 ticks, VA\[UIV\], research nucleus 216 CWU/t: UIV absolute parallel hatch + 2 UXV circuits (abyssal processor mainframes) + 2 nuclei + 8 lepton resonant thallium antimonide double cables, 27 360 mB PEDOT:PSS + 21 920 mB soldering + 5000 mB pure dragon breath. So one controller = 6 helix cores = 6 x 11 x 32 fine wires.
- Threaded machines (assemblyThreadMachine, 18 000 ticks = 15 min at VHA\[UIV\] unless noted, station research of the UIV singleblock of the same kind, 240 CWU/t): each needs a core frame, 4 x N UXV circuits and N nuclei, where N is its nexus amount: aqueous transformation processing center N 8 (8 UIV extractors, canners, solidifiers), ascendant engraving matrix 9, byteforce unified incomparable logistics depot 12, electro magnetic material ripper 10, material annihilation array 8, molecular inducing xanadu 8, subatomic particle lattice isolation terminal 12, superior particulate isolation nexus 8, further machines of the same pattern in the file that this guide did not read (benders, compressors, hammers, presses, packers, macerators, arc furnaces), and the multithreaded component synthesis forge (core casing, N 36 = 144 UXV circuits and 36 nuclei, 72 component nexus + 72 component part hubs + 40 UIV assemblers + 40 UIV scanners + 640 UIPIC chips, 36 000 ticks at VA\[UIV\]).
- What threading is for: the era page says speed, efficiency, parallels and multi-thread (stat-point multiblocks). The pack mod docs for the stats are not in the scripts: Unverified how the stat points are assigned. The cost sizes mean only one or two threaded machines are realistic in the first pass: choose by what you need (the forge for 64-at-once components, the byteforce depot for assembling, the material annihilation array for ores).
- Sub-steps people skip: (1) 6 helix cores per nucleus-pair chain: the 11 fine wires (including soul infused and shellite) must be made first: 352 fine wires per core set; (2) abyssal processor mainframes (UXV circuits) come from the Draco Circuit Assembler (uiv\_circuits): a threaded machine eats 32 to 144; (3) the UIV absolute parallel hatch (uiv\_hatches) needs UXV circuits and UIPIC chips too; (4) the pure dragon breath for the controller has no traced source.
- **Unverified** all stat-point mechanics, the machines of the file that were not read, and the pure dragon breath source.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 1 |
| `gtceu:research_station` | 1 |
| `gtceu:uhv_input_bus` | 6 |
| `gtceu:uhv_input_hatch` | 4 |
| `functionalstorage:oak_1` | 20 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `kubejs:prismalic_helix_core`, `kubejs:prisma_helical_nucleus`, `start_core:threading_controller`
