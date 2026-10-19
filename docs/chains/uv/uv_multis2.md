---
kind: chain
id: uv_multis2
order: 1880
data:
  t: |-
    UV-era controllers 2/2: Mega Blast Furnace (2 UHV circuits), Exotic Rock Crusher and Network Hub (4 UHV circuits) - the UHV circuit is the real gate
  inf: true
  "n":
    - - g1
      - tungsten carbide frame · 2 UHV circuit · 4 dense naquadah alloy plate · 2 ZPM field generator · 4 naquadah spring · 32 fine URD wire · 6 HSS-S screw · 1152 mB solder
      - g
      - functionalstorage:oak_1
      - - [Tungsten carbide frame, "gtceu:tungsten_carbide_frame"]
        - [Dense naquadah alloy plate, "gtceu:dense_naquadah_alloy_plate"]
        - [ZPM field generator, "gtceu:zpm_field_generator"]
        - [Naquadah spring, "gtceu:naquadah_spring"]
        - [Fine URD wire, "gtceu:fine_uranium_rhodium_dinaquadide_wire"]
    - [a1, "Assembly Line · 20 s · 983 040 EU/t · research Super EBF 64 CWU/t", m, "gtceu:assembly_line"]
    - [o1, Mega Blast Furnace, o, "gtceu:mega_blast_furnace"]
    - - g2
      - Large Material Press · 8 UV piston · 4 heat vent · 4 silicon bronze frame · 4 UV circuit · 2 ultradense tritan steel plate · 8 TiC plate · 4 HSLA plate · 1296 mB tritan steel · 3744 mB solder
      - g
      - functionalstorage:oak_1
      - - [Large Material Press, "gtceu:large_material_press"]
        - [UV piston, "gtceu:uv_electric_piston"]
        - [Heat vent, "gtceu:heat_vent"]
        - [Ultradense tritan steel plate, "gtceu:tritan_steel_ultradense_plate"]
    - [a2, "Assembly Line · 2 min · 245 760 EU/t · research UV Rock Crusher 24 CWU/t", m, "gtceu:assembly_line"]
    - [o2, Exotic Tectonic Formation Apparatus, o, "gtceu:exotic_tectonic_formation_apparatus"]
    - - g3
      - Network Switch · 4 UV emitter · 4 UV sensor · 4 UHV circuit · 32 double RTAN wire · 128 tritan steel foil · 48 optical pipe · 576 mB ITLC solder · 576 mB polyimide
      - g
      - functionalstorage:oak_1
      - - [Network Switch, "gtceu:network_switch"]
        - [UV emitter, "gtceu:uv_emitter"]
        - [UV sensor, "gtceu:uv_sensor"]
        - [Double RTAN wire, "gtceu:ruthenium_trinium_americium_neutronate_double_wire"]
    - [a3, "Assembly Line · 2 min · 245 760 EU/t · research Network Switch 32 CWU/t", m, "gtceu:assembly_line"]
    - [o3, Network Hub, o, "gtceu:network_hub"]
  e:
    - [g1, a1, "1"]
    - [a1, o1, "1 / 20 s"]
    - [g2, a2, "1"]
    - [a2, o2, "1 / 120 s"]
    - [g3, a3, "1"]
    - [a3, o3, "1 / 120 s"]
  tips:
    - |-
      Source: kjs large_multis.js and abydos_multis.js (verified). Mega Blast Furnace = Rotary Hearth Furnace [RHF] (listed in the UV era, but verified as a UHV BUILD): AL 400 ticks at VHA[UHV] = 983 040 EU/t, which needs UHV power (a UHV hatch; a UV 4A hatch reaches the same voltage class), and 2 UHV circuits; only its RESEARCH is UV: STATION research of the Hardened Industrial Furnace (super_ebf) at 64 CWU/t and VHA[UV]; 2 UHV circuits (wetware mainframes, uv_wetware3) and 2 ZPM field generators, 32 fine URD wire, 6 HSS-S screws, 1152 mB soldering alloy. Exotic Rock Crusher (gtceu:exotic_tectonic_formation_apparatus): large material press + 8 UV pistons + 4 heat vents + 4 silicon bronze frames + 4 UV circuits + 2 tritan steel ULTRADENSE plates + 8 titanium carbide plates + 4 HSLA steel plates, 1296 mB tritan steel + 3744 mB solder, 2400 ticks at VHA[UV]; research UV rock crusher 24 CWU/t at VHA[ZPM]. Network Hub: Network Switch + 4 UV emitters + 4 UV sensors + 4 UHV circuits + 32 RTAN double wire + 128 tritan steel foil + 48 optical pipes (normal), 576 mB ITLC solder + 576 mB polyimide, 2400 ticks at VHA[UV], research Network Switch 32 CWU/t.
    - |-
      Power gate: Mega Blast Furnace (RHF) 983 040 EU/t needs UHV-class power on the Assembly Line (UHV hatch, or UV 4A); the others 245 760 EU/t run on a ZPM hatch. The MBF is the UHV-circuit customer (2); the Network Hub 4. A tritan steel ultradense plate is 9 ingots of tritan steel (two of them 18 ingots = 1.1 ABS batch, uv_alloys); the apparatus needs tritanium from fusion indirectly through tritan steel.
    - |-
      What they do (quest / lang text): the Mega Blast Furnace is an upgrade of the EBF with parallel and coil discount (tritanium or zalloy coils: zalloy coil 13 499 K, level 24, energy discount 12; Unverified numbers per tier), the Network Hub joins many Network Switches for a 100+ CWU/t research cluster, the Exotic Tectonic Formation Apparatus is the UV rock crusher for Abydos stone and ores (Unverified recipes).
    - |-
      The Exotic Gas Siphon (era listing) is NOT a UV recipe: its Assembly Line recipe needs a UHV gas collector, 8 UHV circuits, 16 sterilizing filter casings and runs at VHA[UEV]; Bulk Ore Processing Array [BOPA]: UHV hull + 18 UHV circuits + 64 UEPIC chips (not 96) + 8 UHV motors + 12 UHV super magnetic cores + 8 UHV microfluidic flow valves at VHA[UEV] = 3 932 160 EU/t, research ore processing plant 144 CWU/t; Component Nexus: 2 Compact Assembly Lines + 6 UEV circuits at VHA[UEV]: all three are UEV-power controllers listed here by mistake (the BOPA and the ASG share the UEV power requirement; the BOPA hull and circuits are UHV).
    - |-
      Sub-steps people skip: (1) 2 and 4 UHV circuits are wetware mainframes: the circuit bill of this page is 6 mainframes; (2) tritan steel ultradense plates come from the plate compressor (plate -> dense -> ultradense, 9 ingots each, Unverified compressor steps); (3) HSS-S screws and fine URD wire are ZPM-era parts; (4) research item for the Network Hub is the Network Switch itself: keep one.
    - |-
      Unverified: coil discounts, the exact function of the apparatus recipes.
  b:
    - ["gtceu:assembly_line", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 1]
    - ["gtceu:zpm_energy_input_hatch", 2]
    - ["functionalstorage:oak_1", 22]
    - ["modularrouters:modular_router", 12]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 18]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 6]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:tungsten_carbide_frame
        - gtceu:wetware_processor_mainframe
        - gtceu:zpm_field_generator
      t: |-
        Drawers first, one per input: frames, plates, UHV circuits (Keep Exact 2 / 4), ZPM field generators, springs, fine URD wire, screws, pistons, vents, UV emitters and sensors, foils, optical pipes. Drums: solder, tritan steel, polyimide.
    - i: ["gtceu:research_station", "gtceu:super_ebf", "gtceu:data_module"]
      t: |-
        Research each: Super EBF (64 CWU/t), UV rock crusher (24), Network Switch (32); one scan item each, kept aside.
    - i: ["gtceu:assembly_line", "gtceu:mega_blast_furnace"]
      t: "Mega Blast Furnace first: UV 4A hatch, 20 s at 983 040 EU/t."
    - i: ["gtceu:assembly_line", "gtceu:exotic_tectonic_formation_apparatus", "gtceu:network_hub"]
      t: |-
        Apparatus and Network Hub: 2 minutes each on a ZPM hatch at 245 760 EU/t.
    - i: ["functionalstorage:oak_1", "gtceu:mega_blast_furnace"]
      t: Output drawers Keep Exact 1.
---
# UV-era controllers 2/2: Mega Blast Furnace (2 UHV circuits), Exotic Rock Crusher and Network Hub (4 UHV circuits) - the UHV circuit is the real gate

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_multis2` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV multiblock controllers](../../plan/p16.md#uvmultis)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 983 040 EU/t · research Super EBF 64 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="tungsten carbide frame · 2 UHV circuit · 4 dense naquadah alloy plate · 2 ZPM field generator · 4 naquadah spring · 32 fine URD wire · 6 HSS-S screw · 1152 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">tungsten carbide frame · 2 UHV circuit · 4 dense naquadah alloy plate · 2 ZPM field generator · 4 naquadah spring · 32 fine URD wire · 6 HSS-S screw · 1152 mB solder</span><span class="gt-sub"><span>Tungsten carbide frame</span><span>Dense naquadah alloy plate</span><span>ZPM field generator</span><span>Naquadah spring</span><span>Fine URD wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mega Blast Furnace (gtceu:mega_blast_furnace) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__mega_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mega Blast Furnace</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Assembly Line · 2 min · 245 760 EU/t · research UV Rock Crusher 24 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Large Material Press · 8 UV piston · 4 heat vent · 4 silicon bronze frame · 4 UV circuit · 2 ultradense tritan steel plate · 8 TiC plate · 4 HSLA plate · 1296 mB tritan steel · 3744 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Large Material Press · 8 UV piston · 4 heat vent · 4 silicon bronze frame · 4 UV circuit · 2 ultradense tritan steel plate · 8 TiC plate · 4 HSLA plate · 1296 mB tritan steel · 3744 mB solder</span><span class="gt-sub"><span>Large Material Press</span><span>UV piston</span><span>Heat vent</span><span>Ultradense tritan steel plate</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">120 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Exotic Tectonic Formation Apparatus (gtceu:exotic_tectonic_formation_apparatus) - 1 / 120 s"><img class="gt-ico" src="../../assets/icons/gtceu__exotic_tectonic_formation_apparatus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Exotic Tectonic Formation Apparatus</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Assembly Line · 2 min · 245 760 EU/t · research Network Switch 32 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Network Switch · 4 UV emitter · 4 UV sensor · 4 UHV circuit · 32 double RTAN wire · 128 tritan steel foil · 48 optical pipe · 576 mB ITLC solder · 576 mB polyimide (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Network Switch · 4 UV emitter · 4 UV sensor · 4 UHV circuit · 32 double RTAN wire · 128 tritan steel foil · 48 optical pipe · 576 mB ITLC solder · 576 mB polyimide</span><span class="gt-sub"><span>Network Switch</span><span>UV emitter</span><span>UV sensor</span><span>Double RTAN wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">120 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Network Hub (gtceu:network_hub) - 1 / 120 s"><img class="gt-ico" src="../../assets/icons/gtceu__network_hub.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Network Hub</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Assembly Line · 20 s · 983 040 EU/t · research Super EBF 64 CWU/t](#m-a1)
- [Assembly Line · 2 min · 245 760 EU/t · research UV Rock Crusher 24 CWU/t](#m-a2)
- [Assembly Line · 2 min · 245 760 EU/t · research Network Switch 32 CWU/t](#m-a3)

## How to build

1. Drawers first, one per input: frames, plates, UHV circuits (Keep Exact 2 / 4), ZPM field generators, springs, fine URD wire, screws, pistons, vents, UV emitters and sensors, foils, optical pipes. Drums: solder, tritan steel, polyimide. — `functionalstorage:oak_1`, `gtceu:tungsten_carbide_frame`, `gtceu:wetware_processor_mainframe`, `gtceu:zpm_field_generator`
2. Research each: Super EBF (64 CWU/t), UV rock crusher (24), Network Switch (32); one scan item each, kept aside. — `gtceu:research_station`, `gtceu:super_ebf`, `gtceu:data_module`
3. Mega Blast Furnace first: UV 4A hatch, 20 s at 983 040 EU/t. — `gtceu:assembly_line`, `gtceu:mega_blast_furnace`
4. Apparatus and Network Hub: 2 minutes each on a ZPM hatch at 245 760 EU/t. — `gtceu:assembly_line`, `gtceu:exotic_tectonic_formation_apparatus`, `gtceu:network_hub`
5. Output drawers Keep Exact 1. — `functionalstorage:oak_1`, `gtceu:mega_blast_furnace`

## Tips

- Source: kjs large\_multis.js and abydos\_multis.js (verified). Mega Blast Furnace = Rotary Hearth Furnace \[RHF\] (listed in the UV era, but verified as a UHV BUILD): AL 400 ticks at VHA\[UHV\] = 983 040 EU/t, which needs UHV power (a UHV hatch; a UV 4A hatch reaches the same voltage class), and 2 UHV circuits; only its RESEARCH is UV: STATION research of the Hardened Industrial Furnace (super\_ebf) at 64 CWU/t and VHA\[UV\]; 2 UHV circuits (wetware mainframes, uv\_wetware3) and 2 ZPM field generators, 32 fine URD wire, 6 HSS-S screws, 1152 mB soldering alloy. Exotic Rock Crusher (gtceu:exotic\_tectonic\_formation\_apparatus): large material press + 8 UV pistons + 4 heat vents + 4 silicon bronze frames + 4 UV circuits + 2 tritan steel ULTRADENSE plates + 8 titanium carbide plates + 4 HSLA steel plates, 1296 mB tritan steel + 3744 mB solder, 2400 ticks at VHA\[UV\]; research UV rock crusher 24 CWU/t at VHA\[ZPM\]. Network Hub: Network Switch + 4 UV emitters + 4 UV sensors + 4 UHV circuits + 32 RTAN double wire + 128 tritan steel foil + 48 optical pipes (normal), 576 mB ITLC solder + 576 mB polyimide, 2400 ticks at VHA\[UV\], research Network Switch 32 CWU/t.
- Power gate: Mega Blast Furnace (RHF) 983 040 EU/t needs UHV-class power on the Assembly Line (UHV hatch, or UV 4A); the others 245 760 EU/t run on a ZPM hatch. The MBF is the UHV-circuit customer (2); the Network Hub 4. A tritan steel ultradense plate is 9 ingots of tritan steel (two of them 18 ingots = 1.1 ABS batch, uv\_alloys); the apparatus needs tritanium from fusion indirectly through tritan steel.
- What they do (quest / lang text): the Mega Blast Furnace is an upgrade of the EBF with parallel and coil discount (tritanium or zalloy coils: zalloy coil 13 499 K, level 24, energy discount 12; Unverified numbers per tier), the Network Hub joins many Network Switches for a 100+ CWU/t research cluster, the Exotic Tectonic Formation Apparatus is the UV rock crusher for Abydos stone and ores (Unverified recipes).
- The Exotic Gas Siphon (era listing) is NOT a UV recipe: its Assembly Line recipe needs a UHV gas collector, 8 UHV circuits, 16 sterilizing filter casings and runs at VHA\[UEV\]; Bulk Ore Processing Array \[BOPA\]: UHV hull + 18 UHV circuits + 64 UEPIC chips (not 96) + 8 UHV motors + 12 UHV super magnetic cores + 8 UHV microfluidic flow valves at VHA\[UEV\] = 3 932 160 EU/t, research ore processing plant 144 CWU/t; Component Nexus: 2 Compact Assembly Lines + 6 UEV circuits at VHA\[UEV\]: all three are UEV-power controllers listed here by mistake (the BOPA and the ASG share the UEV power requirement; the BOPA hull and circuits are UHV).
- Sub-steps people skip: (1) 2 and 4 UHV circuits are wetware mainframes: the circuit bill of this page is 6 mainframes; (2) tritan steel ultradense plates come from the plate compressor (plate -&gt; dense -&gt; ultradense, 9 ingots each, Unverified compressor steps); (3) HSS-S screws and fine URD wire are ZPM-era parts; (4) research item for the Network Hub is the Network Switch itself: keep one.
- **Unverified** coil discounts, the exact function of the apparatus recipes.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 1 |
| `gtceu:zpm_energy_input_hatch` | 2 |
| `functionalstorage:oak_1` | 22 |
| `modularrouters:modular_router` | 12 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 18 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 6 |

## Needs / Feeds

- **Main source for:** `gtceu:mega_blast_furnace`, `gtceu:exotic_tectonic_formation_apparatus`, `gtceu:network_hub`
