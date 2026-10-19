---
kind: chain
id: uhv_multis
order: 1910
data:
  t: |-
    UHV controllers (Assembly Line): Compact Assembly Line, Super Pressure Heat Chamber, Bacteria Synthesizer, Manifold Centrifuge, Injection Mixer, Folding Akreyrium Stabiliser
  inf: true
  "n":
    - - g1
      - |-
        4 Assembly Line · 8 UHV circuit · 8 UV robot arm · 2 UHV pump · 32 fine trinaquadalloy wire · 16 pure netherite screw · 96 UHPIC · 14 688 mB ITLC + 9504 mB tungsten disulfide + 1152 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [Assembly Line, "gtceu:assembly_line"]
        - [UV robot arm, "gtceu:uv_robot_arm"]
        - [UHV pump, "gtceu:uhv_electric_pump"]
        - [Pure netherite screw, "gtceu:pure_netherite_screw"]
    - [a1, "AL · 75 s · 983 040 EU/t · 128 CWU/t", m, "gtceu:assembly_line"]
    - - g2
      - Heat Chamber · 4 UHV circuit · double void plate · double TiC plate · UV field generator · 288 UHPIC · 48 prismalium wire · 6912 mB HSS-E + 1728 mB NbTi
      - g
      - functionalstorage:oak_1
      - - [Heat Chamber, "gtceu:heat_chamber"]
        - [Double void plate, "gtceu:double_void_plate"]
        - [Double titanium carbide plate, "gtceu:double_titanium_carbide_plate"]
        - [UV field generator, "gtceu:uv_field_generator"]
    - [a2, "AL · 160 s · 245 760 EU/t · 128 CWU/t", m, "gtceu:assembly_line"]
    - - g3
      - UHV hull · 4 UHV motor · naquadah alloy rotor · 2 UHV fluid regulator · 4 UHV circuit · 1872 mB solder + 288 mB naquadria
      - g
      - functionalstorage:oak_1
      - - [UHV Machine Hull, "gtceu:uhv_machine_hull"]
        - [UHV motor, "gtceu:uhv_electric_motor"]
        - [UHV fluid regulator, "gtceu:uhv_fluid_regulator"]
    - [a3, "AL · 60 s · 983 040 EU/t · 96 CWU/t", m, "gtceu:assembly_line"]
    - - g4
      - UHV hull · 24 UHV circuit · 96 UEPIC chip · 18 double thacoloy plate · 16 neutronium large pipe · 16 pure netherite foil · 6 super magnetic core · 4 UHV pump · 6 UHV emitter · 4 B PEEK + 1250 mB utopian akreyrium
      - g
      - functionalstorage:oak_1
      - - [UEPIC chip, "kubejs:uepic_chip"]
        - [Double thacoloy plate, "gtceu:double_thacoloy_nq_42x_plate"]
        - [UHV emitter, "gtceu:uhv_emitter"]
    - [a4, "AL · 2 min · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - - g5
      - UHV hull · 24 UHV circuit · 12 double astrenalloy plate · 64 UEPIC chip · 8 neutronium huge pipe · 4 pure netherite rotor · 4 small zalloy gear · 6 UHV pump · 4 B PEEK + 1250 mB utopian akreyrium
      - g
      - functionalstorage:oak_1
      - - [Double astrenalloy plate, "gtceu:double_astrenalloy_nx_plate"]
        - [Neutronium huge fluid pipe, "gtceu:neutronium_huge_fluid_pipe"]
    - [a5, "AL · 2 min · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - - g6
      - UHV hull · 12 UHV circuit · 48 UEPIC chip · 16 small netherite gear · 32 neutronium pipe · 48 colour glass lens · 8 UHV field generator · 8 fluid regulator · 4 UHV sensor · 8 netherite rotor · 9216 mB HSS-E + 147 456 mB borosilicate glass
      - g
      - functionalstorage:oak_1
      - - [Light blue glass lens, "gtceu:light_blue_glass_lens"]
        - [Lime glass lens, "gtceu:lime_glass_lens"]
        - [Magenta glass lens, "gtceu:magenta_glass_lens"]
        - [UHV field generator, "gtceu:uhv_field_generator"]
    - [a6, "AL · 90 s · 491 520 EU/t · 144 CWU/t", m, "gtceu:assembly_line"]
    - - out
      - Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser
      - g
      - functionalstorage:oak_1
      - - [Compact Assembly Line, "gtceu:compact_assembly_line"]
        - [Super Pressure Heat Chamber, "gtceu:super_pressure_heat_chamber"]
        - [Bacteria Synthesizer, "gtceu:bacteria_synthesizer"]
        - [Manifold Centrifuge, "gtceu:manifold_centrifuge"]
        - [Injection Mixer, "gtceu:injection_mixer"]
        - [Folding Akreyrium Stabiliser, "gtceu:folding_akreyrium_stabiliser"]
  e:
    - [g1, a1, "1"]
    - [g2, a2, "1"]
    - [g3, a3, "1"]
    - [g4, a4, "1"]
    - [g5, a5, "1"]
    - [g6, a6, "1"]
    - [a1, out, "1"]
    - [a2, out, "1"]
    - [a3, out, "1"]
    - [a4, out, "1"]
    - [a5, out, "1"]
    - [a6, out, "1"]
  tips:
    - |-
      Source: kjs abydos_multis.js, akreyrium.js (verified). Compact Assembly Line: 4 Assembly Lines + 8 UHV circuits + 8 UV robot arms + 2 UHV pumps + 32 fine trinaquadalloy wire + 16 pure netherite screws + 96 UHPIC chips; fluids 14 688 mB ITLC solder + 9504 mB tungsten disulfide + 1152 mB naquadria; 1500 ticks at VHA[UHV] = 983 040 EU/t; research Assembly Line 128 CWU/t at VHA[UV]. Super Pressure Heat Chamber (recipe id super_heat_chamber): Heat Chamber + 4 UHV circuits + double void plate + double titanium carbide plate + UV field generator + 288 UHPIC + 48 prismalium single wire; 6912 mB HSS-E + 1728 mB NbTi; 3200 ticks at VHA[UV]; research Heat Chamber 128 CWU/t. Bacteria Synthesizer: UHV hull + 4 UHV motors + naquadah alloy rotor + 2 UHV fluid regulators + 4 UHV circuits, 1872 mB solder + 288 mB naquadria, 1200 ticks at VHA[UHV]; research UV chemical reactor 96 CWU/t at 983 040 EU/t.
    - |-
      Manifold Centrifuge: UHV hull + 24 UHV circuits + 96 UEPIC chips + 18 double thacoloy NQ 42x plates + 16 neutronium large fluid pipes + 16 pure netherite foil + 6 UHV super magnetic cores + 4 UHV pumps + 6 UHV emitters; 4 B PEEK + 1250 mB utopian akreyrium; 2400 ticks at VA[UV]; research Large Centrifuge 144 CWU/t. Injection Mixer: UHV hull + 24 UHV circuits + 12 double astrenalloy NX plates + 64 UEPIC chips + 8 neutronium huge pipes + 4 pure netherite rotors + 4 small zalloy gears + 6 UHV pumps; same fluids and time; research Large Mixer 144 CWU/t. Folding Akreyrium Stabiliser: UHV hull + 12 UHV circuits + 48 UEPIC chips + 16 small pure netherite gears + 32 neutronium normal fluid pipes + 16 light blue + 16 lime + 16 magenta glass lenses + 8 UHV field generators + 8 UHV fluid regulators + 4 UHV sensors + 8 pure netherite rotors; 9216 mB HSS-E + 147 456 mB borosilicate glass; 1800 ticks at VA[UV]; research Large Engraving Laser 144 CWU/t.
    - |-
      CIRCUIT BILL: UHV circuits = wetware mainframes: Compact Assembly Line 8, Super Pressure Heat Chamber 4, Bacteria Synthesizer 4, Manifold Centrifuge 24, Injection Mixer 24, Folding Stabiliser 12 = 76 mainframes (152 wetware computers) for these six controllers. The Manifold Centrifuge and Injection Mixer are therefore late-UHV; the Compact Assembly Line and the Super Pressure Heat Chamber come first. Component Nexus (listed in this era) needs 6 UEV circuits: UEV page.
    - |-
      UEV dependencies inside the UHV era (verified): the first UEV circuit, the Runic Processor Mainframe, needs nothing UEV (uhv_runic, uev_circuits), and these UHV-era builds already need it: the UHV Fusion Reactor [AUX I] = Assembly Line VA[UHV] = 1 966 080 EU/t, 1650 ticks, research UV fusion reactor 144 CWU/t, 4 UEV circuits + 96 UEPIC chips (64 + 32) + 2 UV field generators + gravi star; the Folding Akreyrium Stabiliser above wants 48 UEPIC chips (and 12 UHV circuits); the Ancient Stargate Generator (ASG) is the UHV -> UEV step: base block, ring and chevron are EUtVHA(UEV) = 3 932 160 EU/t in the Stargate Component Assembly (3750 mB utopian akreyrium for the base), and its parts use about 96 UEV circuits (dimensional supercomputer) and UEPIC chips (64 per computational matrix). The Bulk Ore Processing Array is UHV hull + 18 UHV circuits + 64 UEPIC chips at EUtVHA(UEV) (3 932 160 EU/t), so it shares the UEV power gate with the ASG. Supreme Plasma Turbine: Assembly Line VHA[UHV] = 983 040 EU/t, no UEV; Compact Assembly Line: VHA[UHV], 96 UHPIC (no UEPIC). Also UHV: Giga Pattern Provider (assembler at VA[UHV] = 1 966 080 EU/t, 1 UHV circuit) and the ETU fuel rod (2 Cm-244 + Cf-252 + Am-241 blend; reactor with deionized water 786 432 EU/t; canner or mixer at 491 520 EU/t).
    - |-
      UEPIC chips (kjs circuits.js): chemical reactor, cleanroom, 1200 ticks at VA[ZPM]: 1 UHPIC wafer + 4 silicon carbide over bismuth tritelluride dust + 576 mB neutronium → 1 UEPIC wafer; cutter (sterile cleanroom, 900 ticks at VA[ZPM]) → 2 chips. 96 chips = 48 wafers = 27.6 B of neutronium. Silicon carbide over bismuth tritelluride dust source: Unverified.
    - |-
      Sub-steps people skip: (1) lenses (colour glass lenses) are crafted by the lens recipes of the laser engraver chain: Unverified here; (2) borosilicate glass 147 456 mB is 1024 ingots-equivalents: a glass line at scale; (3) data modules or DNA disks for the 144 CWU/t research; (4) the Assembly Lines need a UV 4A hatch (983 040 EU/t) or UHV hatch; (5) do the Compact Assembly Line first: it multiplies the Assembly Line.
    - |-
      Unverified: lens recipes, UEPIC chip volume, prismalium supply, thacoloy / astrenalloy production (ABS alloys listed in the materials startup scripts).
  b:
    - ["gtceu:assembly_line", 3]
    - ["gtceu:research_station", 1]
    - ["gtceu:data_bank", 1]
    - ["gtceu:uv_energy_input_hatch_4a", 2]
    - ["gtceu:uhv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 26]
    - ["modularrouters:modular_router", 14]
    - ["gtceu:lv_robot_arm", 14]
    - ["gtceu:item_filter", 22]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 8]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:wetware_processor_mainframe
        - kubejs:uepic_chip
        - gtceu:uhv_machine_hull
      t: |-
        Drawers first, one per input: hulls, UHV circuits (Keep Exact per recipe), UEPIC chips (64), plates, pipes, foils, pumps, motors, emitters, field generators, lenses, gears, rotors. Drums: ITLC solder, tungsten disulfide, naquadria, PEEK, utopian akreyrium, HSS-E, borosilicate glass.
    - i: ["gtceu:research_station", "gtceu:assembly_line", "gtceu:data_module"]
      t: |-
        Research per controller (scan item = the previous version): Assembly Line 128, Heat Chamber 128, UV chemical reactor 96, large centrifuge / mixer / engraving laser 144 CWU/t. 128 and 144 CWU/t need the Network Hub or a Network Switch with 4 to 5 HPCAs.
    - i: ["gtceu:assembly_line", "gtceu:compact_assembly_line", "gtceu:super_pressure_heat_chamber"]
      t: |-
        Compact Assembly Line and Super Pressure Heat Chamber first: they are the throughput upgrades.
    - i: ["gtceu:assembly_line", "gtceu:bacteria_synthesizer"]
      t: "Bacteria Synthesizer: smallest of the group (4 mainframes)."
    - i: ["gtceu:assembly_line", "gtceu:manifold_centrifuge", "gtceu:injection_mixer"]
      t: |-
        Manifold Centrifuge and Injection Mixer: 24 UHV circuits each + UEPIC chips + 1250 mB utopian akreyrium (uhv_akreyrium).
    - i: ["gtceu:assembly_line", "gtceu:folding_akreyrium_stabiliser"]
      t: |-
        Folding stabiliser: 12 mainframes, 48 UEPIC chips, 48 lenses, 147 456 mB borosilicate glass.
---
# UHV controllers (Assembly Line): Compact Assembly Line, Super Pressure Heat Chamber, Bacteria Synthesizer, Manifold Centrifuge, Injection Mixer, Folding Akreyrium Stabiliser

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_multis` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Akreyrium refining, UHV controllers](../../plan/p17.md#uhvmulti)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">AL · 75 s · 983 040 EU/t · 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 Assembly Line · 8 UHV circuit · 8 UV robot arm · 2 UHV pump · 32 fine trinaquadalloy wire · 16 pure netherite screw · 96 UHPIC · 14 688 mB ITLC + 9504 mB tungsten disulfide + 1152 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 Assembly Line · 8 UHV circuit · 8 UV robot arm · 2 UHV pump · 32 fine trinaquadalloy wire · 16 pure netherite screw · 96 UHPIC · 14 688 mB ITLC + 9504 mB tungsten disulfide + 1152 mB naquadria</span><span class="gt-sub"><span>Assembly Line</span><span>UV robot arm</span><span>UHV pump</span><span>Pure netherite screw</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">AL · 160 s · 245 760 EU/t · 128 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Heat Chamber · 4 UHV circuit · double void plate · double TiC plate · UV field generator · 288 UHPIC · 48 prismalium wire · 6912 mB HSS-E + 1728 mB NbTi (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Heat Chamber · 4 UHV circuit · double void plate · double TiC plate · UV field generator · 288 UHPIC · 48 prismalium wire · 6912 mB HSS-E + 1728 mB NbTi</span><span class="gt-sub"><span>Heat Chamber</span><span>Double void plate</span><span>Double titanium carbide plate</span><span>UV field generator</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">AL · 60 s · 983 040 EU/t · 96 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 4 UHV motor · naquadah alloy rotor · 2 UHV fluid regulator · 4 UHV circuit · 1872 mB solder + 288 mB naquadria (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 4 UHV motor · naquadah alloy rotor · 2 UHV fluid regulator · 4 UHV circuit · 1872 mB solder + 288 mB naquadria</span><span class="gt-sub"><span>UHV Machine Hull</span><span>UHV motor</span><span>UHV fluid regulator</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">AL · 2 min · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 24 UHV circuit · 96 UEPIC chip · 18 double thacoloy plate · 16 neutronium large pipe · 16 pure netherite foil · 6 super magnetic core · 4 UHV pump · 6 UHV emitter · 4 B PEEK + 1250 mB utopian akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 24 UHV circuit · 96 UEPIC chip · 18 double thacoloy plate · 16 neutronium large pipe · 16 pure netherite foil · 6 super magnetic core · 4 UHV pump · 6 UHV emitter · 4 B PEEK + 1250 mB utopian akreyrium</span><span class="gt-sub"><span>UEPIC chip</span><span>Double thacoloy plate</span><span>UHV emitter</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a5">
<div class="gt-head"><span class="gt-mname">AL · 2 min · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 24 UHV circuit · 12 double astrenalloy plate · 64 UEPIC chip · 8 neutronium huge pipe · 4 pure netherite rotor · 4 small zalloy gear · 6 UHV pump · 4 B PEEK + 1250 mB utopian akreyrium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 24 UHV circuit · 12 double astrenalloy plate · 64 UEPIC chip · 8 neutronium huge pipe · 4 pure netherite rotor · 4 small zalloy gear · 6 UHV pump · 4 B PEEK + 1250 mB utopian akreyrium</span><span class="gt-sub"><span>Double astrenalloy plate</span><span>Neutronium huge fluid pipe</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-multi" id="m-a6">
<div class="gt-head"><span class="gt-mname">AL · 90 s · 491 520 EU/t · 144 CWU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="UHV hull · 12 UHV circuit · 48 UEPIC chip · 16 small netherite gear · 32 neutronium pipe · 48 colour glass lens · 8 UHV field generator · 8 fluid regulator · 4 UHV sensor · 8 netherite rotor · 9216 mB HSS-E + 147 456 mB borosilicate glass (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">UHV hull · 12 UHV circuit · 48 UEPIC chip · 16 small netherite gear · 32 neutronium pipe · 48 colour glass lens · 8 UHV field generator · 8 fluid regulator · 4 UHV sensor · 8 netherite rotor · 9216 mB HSS-E + 147 456 mB borosilicate glass</span><span class="gt-sub"><span>Light blue glass lens</span><span>Lime glass lens</span><span>Magenta glass lens</span><span>UHV field generator</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-group" title="Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Compact Assembly Line · Super Pressure Heat Chamber · Bacteria Synthesizer · Manifold Centrifuge · Injection Mixer · Folding Stabiliser</span><span class="gt-sub"><span>Compact Assembly Line</span><span>Super Pressure Heat Chamber</span><span>Bacteria Synthesizer</span><span>Manifold Centrifuge</span><span>Injection Mixer</span><span>Folding Akreyrium Stabiliser</span></span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [AL · 75 s · 983 040 EU/t · 128 CWU/t](#m-a1)
- [AL · 160 s · 245 760 EU/t · 128 CWU/t](#m-a2)
- [AL · 60 s · 983 040 EU/t · 96 CWU/t](#m-a3)
- [AL · 2 min · 491 520 EU/t · 144 CWU/t](#m-a4)
- [AL · 2 min · 491 520 EU/t · 144 CWU/t](#m-a5)
- [AL · 90 s · 491 520 EU/t · 144 CWU/t](#m-a6)

## How to build

1. Drawers first, one per input: hulls, UHV circuits (Keep Exact per recipe), UEPIC chips (64), plates, pipes, foils, pumps, motors, emitters, field generators, lenses, gears, rotors. Drums: ITLC solder, tungsten disulfide, naquadria, PEEK, utopian akreyrium, HSS-E, borosilicate glass. — `functionalstorage:oak_1`, `gtceu:wetware_processor_mainframe`, `kubejs:uepic_chip`, `gtceu:uhv_machine_hull`
2. Research per controller (scan item = the previous version): Assembly Line 128, Heat Chamber 128, UV chemical reactor 96, large centrifuge / mixer / engraving laser 144 CWU/t. 128 and 144 CWU/t need the Network Hub or a Network Switch with 4 to 5 HPCAs. — `gtceu:research_station`, `gtceu:assembly_line`, `gtceu:data_module`
3. Compact Assembly Line and Super Pressure Heat Chamber first: they are the throughput upgrades. — `gtceu:assembly_line`, `gtceu:compact_assembly_line`, `gtceu:super_pressure_heat_chamber`
4. Bacteria Synthesizer: smallest of the group (4 mainframes). — `gtceu:assembly_line`, `gtceu:bacteria_synthesizer`
5. Manifold Centrifuge and Injection Mixer: 24 UHV circuits each + UEPIC chips + 1250 mB utopian akreyrium (uhv\_akreyrium). — `gtceu:assembly_line`, `gtceu:manifold_centrifuge`, `gtceu:injection_mixer`
6. Folding stabiliser: 12 mainframes, 48 UEPIC chips, 48 lenses, 147 456 mB borosilicate glass. — `gtceu:assembly_line`, `gtceu:folding_akreyrium_stabiliser`

## Tips

- Source: kjs abydos\_multis.js, akreyrium.js (verified). Compact Assembly Line: 4 Assembly Lines + 8 UHV circuits + 8 UV robot arms + 2 UHV pumps + 32 fine trinaquadalloy wire + 16 pure netherite screws + 96 UHPIC chips; fluids 14 688 mB ITLC solder + 9504 mB tungsten disulfide + 1152 mB naquadria; 1500 ticks at VHA\[UHV\] = 983 040 EU/t; research Assembly Line 128 CWU/t at VHA\[UV\]. Super Pressure Heat Chamber (recipe id super\_heat\_chamber): Heat Chamber + 4 UHV circuits + double void plate + double titanium carbide plate + UV field generator + 288 UHPIC + 48 prismalium single wire; 6912 mB HSS-E + 1728 mB NbTi; 3200 ticks at VHA\[UV\]; research Heat Chamber 128 CWU/t. Bacteria Synthesizer: UHV hull + 4 UHV motors + naquadah alloy rotor + 2 UHV fluid regulators + 4 UHV circuits, 1872 mB solder + 288 mB naquadria, 1200 ticks at VHA\[UHV\]; research UV chemical reactor 96 CWU/t at 983 040 EU/t.
- Manifold Centrifuge: UHV hull + 24 UHV circuits + 96 UEPIC chips + 18 double thacoloy NQ 42x plates + 16 neutronium large fluid pipes + 16 pure netherite foil + 6 UHV super magnetic cores + 4 UHV pumps + 6 UHV emitters; 4 B PEEK + 1250 mB utopian akreyrium; 2400 ticks at VA\[UV\]; research Large Centrifuge 144 CWU/t. Injection Mixer: UHV hull + 24 UHV circuits + 12 double astrenalloy NX plates + 64 UEPIC chips + 8 neutronium huge pipes + 4 pure netherite rotors + 4 small zalloy gears + 6 UHV pumps; same fluids and time; research Large Mixer 144 CWU/t. Folding Akreyrium Stabiliser: UHV hull + 12 UHV circuits + 48 UEPIC chips + 16 small pure netherite gears + 32 neutronium normal fluid pipes + 16 light blue + 16 lime + 16 magenta glass lenses + 8 UHV field generators + 8 UHV fluid regulators + 4 UHV sensors + 8 pure netherite rotors; 9216 mB HSS-E + 147 456 mB borosilicate glass; 1800 ticks at VA\[UV\]; research Large Engraving Laser 144 CWU/t.
- CIRCUIT BILL: UHV circuits = wetware mainframes: Compact Assembly Line 8, Super Pressure Heat Chamber 4, Bacteria Synthesizer 4, Manifold Centrifuge 24, Injection Mixer 24, Folding Stabiliser 12 = 76 mainframes (152 wetware computers) for these six controllers. The Manifold Centrifuge and Injection Mixer are therefore late-UHV; the Compact Assembly Line and the Super Pressure Heat Chamber come first. Component Nexus (listed in this era) needs 6 UEV circuits: UEV page.
- UEV dependencies inside the UHV era (verified): the first UEV circuit, the Runic Processor Mainframe, needs nothing UEV (uhv\_runic, uev\_circuits), and these UHV-era builds already need it: the UHV Fusion Reactor \[AUX I\] = Assembly Line VA\[UHV\] = 1 966 080 EU/t, 1650 ticks, research UV fusion reactor 144 CWU/t, 4 UEV circuits + 96 UEPIC chips (64 + 32) + 2 UV field generators + gravi star; the Folding Akreyrium Stabiliser above wants 48 UEPIC chips (and 12 UHV circuits); the Ancient Stargate Generator (ASG) is the UHV -&gt; UEV step: base block, ring and chevron are EUtVHA(UEV) = 3 932 160 EU/t in the Stargate Component Assembly (3750 mB utopian akreyrium for the base), and its parts use about 96 UEV circuits (dimensional supercomputer) and UEPIC chips (64 per computational matrix). The Bulk Ore Processing Array is UHV hull + 18 UHV circuits + 64 UEPIC chips at EUtVHA(UEV) (3 932 160 EU/t), so it shares the UEV power gate with the ASG. Supreme Plasma Turbine: Assembly Line VHA\[UHV\] = 983 040 EU/t, no UEV; Compact Assembly Line: VHA\[UHV\], 96 UHPIC (no UEPIC). Also UHV: Giga Pattern Provider (assembler at VA\[UHV\] = 1 966 080 EU/t, 1 UHV circuit) and the ETU fuel rod (2 Cm-244 + Cf-252 + Am-241 blend; reactor with deionized water 786 432 EU/t; canner or mixer at 491 520 EU/t).
- UEPIC chips (kjs circuits.js): chemical reactor, cleanroom, 1200 ticks at VA\[ZPM\]: 1 UHPIC wafer + 4 silicon carbide over bismuth tritelluride dust + 576 mB neutronium → 1 UEPIC wafer; cutter (sterile cleanroom, 900 ticks at VA\[ZPM\]) → 2 chips. 96 chips = 48 wafers = 27.6 B of neutronium. Silicon carbide over bismuth tritelluride dust source: Unverified.
- Sub-steps people skip: (1) lenses (colour glass lenses) are crafted by the lens recipes of the laser engraver chain: Unverified here; (2) borosilicate glass 147 456 mB is 1024 ingots-equivalents: a glass line at scale; (3) data modules or DNA disks for the 144 CWU/t research; (4) the Assembly Lines need a UV 4A hatch (983 040 EU/t) or UHV hatch; (5) do the Compact Assembly Line first: it multiplies the Assembly Line.
- **Unverified** lens recipes, UEPIC chip volume, prismalium supply, thacoloy / astrenalloy production (ABS alloys listed in the materials startup scripts).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:assembly_line` | 3 |
| `gtceu:research_station` | 1 |
| `gtceu:data_bank` | 1 |
| `gtceu:uv_energy_input_hatch_4a` | 2 |
| `gtceu:uhv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 26 |
| `modularrouters:modular_router` | 14 |
| `gtceu:lv_robot_arm` | 14 |
| `gtceu:item_filter` | 22 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Main source for:** `gtceu:compact_assembly_line`, `gtceu:super_pressure_heat_chamber`, `gtceu:bacteria_synthesizer`, `gtceu:manifold_centrifuge`, `gtceu:injection_mixer`, `gtceu:folding_akreyrium_stabiliser`, `kubejs:uepic_chip`
