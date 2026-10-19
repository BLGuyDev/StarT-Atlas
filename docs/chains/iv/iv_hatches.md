---
kind: chain
id: iv_hatches
order: 1140
data:
  t: |-
    IV Energy and Dynamo Hatch: phosphorus wafer → MPIC wafer → HPIC wafer → 2 HPIC chips, IV voltage coil, IV Assembler
  inf: true
  "n":
    - - si
      - |-
        64 Silicon + 8 phosphorus + 2 small gallium arsenide dust + 8 B nitrogen
      - g
      - functionalstorage:oak_1
      - - [Silicon dust, "gtceu:silicon_dust"]
        - [Phosphorus dust, "gtceu:phosphorus_dust"]
        - [Small gallium arsenide dust, "gtceu:small_gallium_arsenide_dust"]
        - [Nitrogen, "gtceu:nitrogen_bucket"]
    - [eb, "EBF · Kanthal 2484 K · 10 min · 480 EU/t", m, "gtceu:electric_blast_furnace"]
    - [bo, Phosphorus boule, x, "gtceu:phosphorus_boule"]
    - [cu, "HV Cutter in the cleanroom · 40 s · 480 EU/t", m, "gtceu:hv_cutter"]
    - [pw, "32 Phosphorus wafer", x, "gtceu:phosphorus_wafer"]
    - [le, "HV Laser Engraver in the cleanroom · brown lens · 45 s · 480 EU/t", m, "gtceu:hv_laser_engraver"]
    - [pc, "MPIC wafer (power integrated circuit)", x, "gtceu:mpic_wafer"]
    - [ig, "2 Indium gallium phosphide dust", i, "gtceu:indium_gallium_phosphide_dust"]
    - [vg, "288 mB molten vanadium gallium", f, "gtceu:vanadium_gallium_bucket"]
    - [cr, "IV Chemical Reactor in the cleanroom · 60 s · 7680 EU/t", m, "gtceu:iv_chemical_reactor"]
    - [hw, HPIC wafer, x, "gtceu:hpic_wafer"]
    - [c2, "IV Cutter in the cleanroom · 45 s · 7680 EU/t", m, "gtceu:iv_cutter"]
    - [hc, "2 HPIC chips", x, "gtceu:hpic_chip"]
    - [nd, Neodymium magnetic rod, i, "gtceu:magnetic_neodymium_rod"]
    - [iw, "16 Fine iridium wire", i, "gtceu:fine_iridium_wire"]
    - [a1, "IV Assembler · circuit 1 · 10 s · 7680 EU/t", m, "gtceu:iv_assembler"]
    - [vc, IV Voltage Coil, x, "gtceu:iv_voltage_coil"]
    - [hu, IV Machine Hull, i, "gtceu:iv_machine_hull"]
    - [tc, "2 Tungsten single cable", i, "gtceu:tungsten_single_cable"]
    - [sp, "2 Tungsten spring", i, "gtceu:tungsten_spring"]
    - [nk, "3 B sodium potassium", f, "gtceu:sodium_potassium_bucket"]
    - [a2, "IV Assembler · 10 s · 7680 EU/t (input hatch)", m, "gtceu:iv_assembler"]
    - [eh, IV Energy Input Hatch, o, "gtceu:iv_energy_input_hatch"]
    - [a3, "IV Assembler · 10 s · 7680 EU/t (dynamo hatch)", m, "gtceu:iv_assembler"]
    - [dh, IV Dynamo Hatch, o, "gtceu:iv_energy_output_hatch"]
  e:
    - [si, eb]
    - [eb, bo, "1 / 10 min"]
    - [bo, cu, "1"]
    - [cu, pw, "32"]
    - [pw, le, "1"]
    - [le, pc, "1 / 45 s"]
    - [pc, cr, "1"]
    - [ig, cr, "2"]
    - [vg, cr, "288 mB"]
    - [cr, hw, "1 / 60 s"]
    - [hw, c2, "1"]
    - [c2, hc, "2 / 45 s"]
    - [nd, a1, "1"]
    - [iw, a1, "16"]
    - [a1, vc, "1 / 10 s"]
    - [hu, a2, "1"]
    - [tc, a2, "2"]
    - [hc, a2, "2"]
    - [vc, a2, "1"]
    - [nk, a2, "3 B"]
    - [a2, eh, "1 / 10 s"]
    - [hu, a3, "1"]
    - [sp, a3, "2"]
    - [hc, a3, "2"]
    - [vc, a3, "1"]
    - [nk, a3, "3 B"]
    - [a3, dh, "1 / 10 s"]
  tips:
    - |-
      Recipes (MetaTileEntityMachineRecipeLoader, AssemblerRecipeLoader, CircuitRecipes; no pack override): IV Energy Input Hatch = IV hull + 2 tungsten single cables + 2 HPIC chips + 1 IV voltage coil + 3 B sodium potassium, assembler 200 ticks at 7680 EU/t. IV Dynamo Hatch = the same with 2 tungsten SPRINGS instead of cables. IV voltage coil = 1 magnetic neodymium rod + 16 fine iridium wire (circuit 1, 200 ticks, 7680 EU/t). Both need an IV Assembler (7680 EU/t), which is why the pack quest says the IV Assembler makes the energy hatches.
    - |-
      HPIC chip line (CircuitRecipes): phosphorus boule (EBF, 2484 K, 64 silicon + 8 phosphorus + 2 small gallium arsenide dust + 8 B nitrogen, 12 000 ticks = 10 min, 480 EU/t; Kanthal coils reach 2700 K) → HV Cutter, CLEANROOM, 800 ticks → 32 phosphorus wafers → HV Laser Engraver, CLEANROOM, brown lens, 900 ticks at 480 EU/t → 1 MPIC wafer. HPIC wafer: IV Chemical Reactor, CLEANROOM, 1200 ticks at 7680 EU/t: 1 MPIC wafer + 2 indium gallium phosphide dust + 288 mB molten vanadium gallium. HPIC chips: IV Cutter, CLEANROOM, 900 ticks at 7680 EU/t: 1 HPIC wafer → 2 chips.
    - |-
      So one boule feeds 32 hatches. One wafer of HPIC gives 2 chips = exactly one hatch. The slow, rare input is molten vanadium gallium: vanadium gallium is an EBF recipe at 4500 K (VA[EV] = 1920 EU/t, 1200 ticks = 60 s, argon gas tier), which needs RTM coils; 288 mB is 2 ingots from 2 × (3 vanadium + 1 gallium) dust (EV Mixer, 400 ticks, circuit 1: 3 vanadium + 1 gallium → 4 dust). Extract the ingot in an extractor (144 mB each).
    - |-
      Indium gallium phosphide dust: ULV Mixer, circuit 1, 1 indium + 1 gallium + 1 phosphorus dust → 3 dust (200 ticks, 7 EU/t). Sodium potassium: Chemical Reactor, 1 sodium + 1 potassium dust → 1 B (300 ticks, 30 EU/t). Indium is the odd one out: Unverified: its source in this pack.
    - |-
      The IV Chemical Reactor and IV Cutter are IV single machines: they need IV motors, pumps, conveyors and circuits from the iv_components chain, and they take 7680 EU/t straight from an IV cable (single machines do not use hatches; the hatches here are for multiblocks). The room only has to be big enough for the machines; a cleanroom machine runs only while the room is 95 % clean.
    - |-
      What the hatch unlocks: the Large Chemical Reactor rarest-metal step (iridium and osmium) at 7680 EU/t, the shellite superconductor EBF recipe (7680 EU/t, 4400 K), the Nuclear Reactor dynamo output (4096 EU/t per thorium rod) and every IV multiblock recipe above 1920 EU/t. The 1A hatch carries 8192 V; the 4A and 16A versions are pack assembler recipes (the stock ones are removed, kjs large_energy_hatches.js): 4A = IV 1A transformer + IV hatch + 2 platinum quadruple wire + 1 IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy (see luv_hatches); 16A = IV 4A transformer + IV 4A hatch + 2 quadruple wire + 2 IV voltage coils + 4 plates. All of them need the IV Assembler.
    - |-
      Sub-steps people skip: (1) four machines sit in the cleanroom (HV cutter, HV laser engraver, IV chemical reactor, IV cutter), so size the room for them before you close the walls; (2) the lens is brown, not the ones from the HV chain; (3) the HPIC wafer takes the vanadium gallium as a FLUID; (4) phosphorus is a boule recipe with nitrogen, not a plain furnace one; (5) iridium wire is 8 fine wires per ingot, so a coil is 2 iridium ingots.
    - |-
      Unverified: the lubricant amount of the cutters (copy the HV chain numbers), where indium comes from, whether a 16-circuit cleanroom fits the four machines (read the cleanroom size), and the brown lens recipe (look it up in EMI).
  b:
    - ["gtceu:iv_assembler", 1]
    - ["gtceu:iv_chemical_reactor", 1]
    - ["gtceu:iv_cutter", 1]
    - ["gtceu:hv_cutter", 1]
    - ["gtceu:hv_laser_engraver", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:lv_chemical_reactor", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:phosphorus_dust", "gtceu:silicon_dust", "gtceu:nitrogen_bucket"]
      t: |-
        Drawers first: silicon dust, phosphorus dust, small gallium arsenide dust, indium gallium phosphide dust, neodymium magnetic rods, iridium wire, IV hulls, tungsten cables and springs. Drums: nitrogen, molten vanadium gallium, sodium potassium. Each machine below has its own input drawer behind a Modular Router or Pipez route with an Item Filter, and a Keep Exact arm on the output.
    - i: ["gtceu:electric_blast_furnace", "gtceu:kanthal_coil_block", "gtceu:phosphorus_boule"]
      t: |-
        Phosphorus boule in an EBF with 16 Kanthal coils (2700 K is enough, so no nichrome needed): 64 silicon + 8 phosphorus + 2 small gallium arsenide dust in the bus, 8 B nitrogen in a hatch, 480 EU/t for 10 minutes. One boule per 10 minutes is the pace of every hatch you will ever make, so start it early.
    - i: ["gtceu:hv_cutter", "gtceu:phosphorus_wafer", "gtceu:cleanroom"]
      t: |-
        HV Cutter inside the Cleanroom: 1 boule → 32 phosphorus wafers in 40 s at 480 EU/t, with lubricant like the silicon cutter in the HV chain. Output into a drawer with Keep Exact 64; the wafers are the shared stock for MPIC wafers and later chips.
    - i: ["gtceu:hv_laser_engraver", "gtceu:brown_glass_lens", "gtceu:mpic_wafer"]
      t: |-
        HV Laser Engraver inside the Cleanroom, brown lens fixed in its slot: 1 phosphorus wafer → 1 MPIC wafer in 45 s at 480 EU/t. The same engraver with other lenses makes other chips: never change the lens, make a second engraver.
    - i: ["gtceu:iv_chemical_reactor", "gtceu:hpic_wafer", "gtceu:vanadium_gallium_bucket"]
      t: |-
        IV Chemical Reactor inside the Cleanroom (a single machine, 7680 EU/t straight from an IV cable): 1 MPIC wafer + 2 indium gallium phosphide dust + 288 mB molten vanadium gallium → 1 HPIC wafer, 60 s. The vanadium gallium comes from the 4500 K EBF (RTM coils) via the extractor; a separate drum and fluid hatch.
    - i: ["gtceu:iv_cutter", "gtceu:hpic_chip"]
      t: |-
        IV Cutter inside the Cleanroom: 1 HPIC wafer → 2 HPIC chips in 45 s at 7680 EU/t. That is exactly the two chips of one IV hatch. Hand the chips to a drawer with Keep Exact 8 beside the hatch assembler.
    - i: ["gtceu:iv_assembler", "gtceu:iv_voltage_coil", "gtceu:magnetic_neodymium_rod", "gtceu:fine_iridium_wire"]
      t: |-
        Voltage coil, IV Assembler with ghost circuit 1: 1 magnetic neodymium rod + 16 fine iridium wire (2 iridium ingots in a wiremill, circuit 3, 8 per ingot) → 1 IV voltage coil in 10 s at 7680 EU/t. Craft the first IV Assembler by hand: hull, 2 IV robot arms, 2 IV conveyors, 2 IV circuits, 2 platinum cables.
    - i:
        - gtceu:iv_assembler
        - gtceu:iv_energy_input_hatch
        - gtceu:iv_energy_output_hatch
        - gtceu:sodium_potassium_bucket
      t: |-
        Hatch assemblers, one per hatch type: IV hull + 2 tungsten single cables (input hatch) or 2 tungsten springs (dynamo hatch) + 2 HPIC chips + 1 voltage coil + 3 B sodium potassium → hatch in 10 s at 7680 EU/t. The sodium potassium is a fluid in a hatch; make it with the LV chemical reactor from sodium and potassium dust.
    - i: ["gtceu:iv_energy_input_hatch", "gtceu:large_chemical_reactor"]
      t: |-
        Easy to miss: the hatches are for multiblocks only. IV single machines (this line, the IV Assembler) run on IV cable, so build the first hatch for the Large Chemical Reactor (iridium and osmium) and the next ones for the EBF that makes shellite and for the reactor dynamo.
---
# IV Energy and Dynamo Hatch: phosphorus wafer → MPIC wafer → HPIC wafer → 2 HPIC chips, IV voltage coil, IV Assembler

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `iv_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [IV circuit and IV hatches](../../plan/p10.md#ivcirc)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · Kanthal 2484 K · 10 min · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="64 Silicon + 8 phosphorus + 2 small gallium arsenide dust + 8 B nitrogen (functionalstorage:oak_1)"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">64 Silicon + 8 phosphorus + 2 small gallium arsenide dust + 8 B nitrogen</span><span class="gt-sub"><span>Silicon dust</span><span>Phosphorus dust</span><span>Small gallium arsenide dust</span><span>Nitrogen</span></span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 min</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Phosphorus boule (gtceu:phosphorus_boule) - 1 / 10 min"><img class="gt-ico" src="../../assets/icons/gtceu__phosphorus_boule.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phosphorus Boule</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-hv" id="m-cu">
<div class="gt-head"><span class="gt-mname">HV Cutter in the cleanroom · 40 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Phosphorus boule (gtceu:phosphorus_boule) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__phosphorus_boule.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phosphorus Boule</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="32 Phosphorus wafer (gtceu:phosphorus_wafer) - 32"><img class="gt-ico" src="../../assets/icons/gtceu__phosphorus_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phosphorus Wafer</span><span class="gt-note">32 Phosphorus wafer</span><b class="gt-q">32</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_cutter</code></div>
</div>
<div class="gt-panel t-hv" id="m-le">
<div class="gt-head"><span class="gt-mname">HV Laser Engraver in the cleanroom · brown lens · 45 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="32 Phosphorus wafer (gtceu:phosphorus_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__phosphorus_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Phosphorus Wafer</span><span class="gt-note">32 Phosphorus wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_laser_engraver.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="MPIC wafer (power integrated circuit) (gtceu:mpic_wafer) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__mpic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mpic Wafer</span><span class="gt-note">MPIC wafer (power integrated circuit)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_laser_engraver</code></div>
</div>
<div class="gt-panel t-iv" id="m-cr">
<div class="gt-head"><span class="gt-mname">IV Chemical Reactor in the cleanroom · 60 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="MPIC wafer (power integrated circuit) (gtceu:mpic_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__mpic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mpic Wafer</span><span class="gt-note">MPIC wafer (power integrated circuit)</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Indium gallium phosphide dust (gtceu:indium_gallium_phosphide_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__indium_gallium_phosphide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Indium Gallium Phosphide Dust</span><span class="gt-note">2 Indium gallium phosphide dust</span><b class="gt-q">2</b></span><span class="gt-slot gt-fluid" title="288 mB molten vanadium gallium (gtceu:vanadium_gallium_bucket) - 288 mB"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_gallium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Gallium</span><span class="gt-note">288 mB molten vanadium gallium</span><b class="gt-q">288 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="HPIC wafer (gtceu:hpic_wafer) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__hpic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HPIC Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-iv" id="m-c2">
<div class="gt-head"><span class="gt-mname">IV Cutter in the cleanroom · 45 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="HPIC wafer (gtceu:hpic_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__hpic_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HPIC Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 HPIC chips (gtceu:hpic_chip) - 2 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__hpic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HPIC Chip</span><span class="gt-note">2 HPIC chips</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_cutter</code></div>
</div>
<div class="gt-panel t-iv" id="m-a1">
<div class="gt-head"><span class="gt-mname">IV Assembler · circuit 1 · 10 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Neodymium magnetic rod (gtceu:magnetic_neodymium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_neodymium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Neodymium Rod</span><span class="gt-note">Neodymium magnetic rod</span><b class="gt-q">1</b></span><span class="gt-slot" title="16 Fine iridium wire (gtceu:fine_iridium_wire) - 16"><img class="gt-ico" src="../../assets/icons/gtceu__fine_iridium_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Iridium Wire</span><span class="gt-note">16 Fine iridium wire</span><b class="gt-q">16</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="IV Voltage Coil (gtceu:iv_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Voltage Coil</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a2">
<div class="gt-head"><span class="gt-mname">IV Assembler · 10 s · 7680 EU/t (input hatch)</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Machine Hull (gtceu:iv_machine_hull) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Machine Hull</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Tungsten single cable (gtceu:tungsten_single_cable) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_single_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Single Cable</span><span class="gt-note">2 Tungsten single cable</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 HPIC chips (gtceu:hpic_chip) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__hpic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HPIC Chip</span><span class="gt-note">2 HPIC chips</span><b class="gt-q">2</b></span><span class="gt-slot" title="IV Voltage Coil (gtceu:iv_voltage_coil) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Voltage Coil</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="3 B sodium potassium (gtceu:sodium_potassium_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__sodium_potassium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sodium Potassium</span><span class="gt-note">3 B sodium potassium</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Energy Input Hatch (gtceu:iv_energy_input_hatch) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Input Hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
<div class="gt-panel t-iv" id="m-a3">
<div class="gt-head"><span class="gt-mname">IV Assembler · 10 s · 7680 EU/t (dynamo hatch)</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="IV Machine Hull (gtceu:iv_machine_hull) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Machine Hull</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Tungsten spring (gtceu:tungsten_spring) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_spring.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Spring</span><span class="gt-note">2 Tungsten spring</span><b class="gt-q">2</b></span><span class="gt-slot" title="2 HPIC chips (gtceu:hpic_chip) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__hpic_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HPIC Chip</span><span class="gt-note">2 HPIC chips</span><b class="gt-q">2</b></span><span class="gt-slot" title="IV Voltage Coil (gtceu:iv_voltage_coil) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Voltage Coil</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="3 B sodium potassium (gtceu:sodium_potassium_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__sodium_potassium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sodium Potassium</span><span class="gt-note">3 B sodium potassium</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="IV Dynamo Hatch (gtceu:iv_energy_output_hatch) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Output Hatch</span><span class="gt-note">IV Dynamo Hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_assembler</code></div>
</div>
</div>

## Flow

- [EBF · Kanthal 2484 K · 10 min · 480 EU/t](#m-eb) → [HV Cutter in the cleanroom · 40 s · 480 EU/t](#m-cu) → [HV Laser Engraver in the cleanroom · brown lens · 45 s · 480 EU/t](#m-le) → [IV Chemical Reactor in the cleanroom · 60 s · 7680 EU/t](#m-cr) → [IV Cutter in the cleanroom · 45 s · 7680 EU/t](#m-c2) → [IV Assembler · 10 s · 7680 EU/t (input hatch)](#m-a2) (also IV Cutter in the cleanroom · 45 s · 7680 EU/t → [IV Assembler · 10 s · 7680 EU/t (dynamo hatch)](#m-a3))
- [IV Assembler · circuit 1 · 10 s · 7680 EU/t](#m-a1) → [IV Assembler · 10 s · 7680 EU/t (dynamo hatch)](#m-a3) (also IV Assembler · circuit 1 · 10 s · 7680 EU/t → [IV Assembler · 10 s · 7680 EU/t (input hatch)](#m-a2))

## How to build

1. Drawers first: silicon dust, phosphorus dust, small gallium arsenide dust, indium gallium phosphide dust, neodymium magnetic rods, iridium wire, IV hulls, tungsten cables and springs. Drums: nitrogen, molten vanadium gallium, sodium potassium. Each machine below has its own input drawer behind a Modular Router or Pipez route with an Item Filter, and a Keep Exact arm on the output. — `functionalstorage:oak_1`, `gtceu:phosphorus_dust`, `gtceu:silicon_dust`, `gtceu:nitrogen_bucket`
2. Phosphorus boule in an EBF with 16 Kanthal coils (2700 K is enough, so no nichrome needed): 64 silicon + 8 phosphorus + 2 small gallium arsenide dust in the bus, 8 B nitrogen in a hatch, 480 EU/t for 10 minutes. One boule per 10 minutes is the pace of every hatch you will ever make, so start it early. — `gtceu:electric_blast_furnace`, `gtceu:kanthal_coil_block`, `gtceu:phosphorus_boule`
3. HV Cutter inside the Cleanroom: 1 boule → 32 phosphorus wafers in 40 s at 480 EU/t, with lubricant like the silicon cutter in the HV chain. Output into a drawer with Keep Exact 64; the wafers are the shared stock for MPIC wafers and later chips. — `gtceu:hv_cutter`, `gtceu:phosphorus_wafer`, `gtceu:cleanroom`
4. HV Laser Engraver inside the Cleanroom, brown lens fixed in its slot: 1 phosphorus wafer → 1 MPIC wafer in 45 s at 480 EU/t. The same engraver with other lenses makes other chips: never change the lens, make a second engraver. — `gtceu:hv_laser_engraver`, `gtceu:brown_glass_lens`, `gtceu:mpic_wafer`
5. IV Chemical Reactor inside the Cleanroom (a single machine, 7680 EU/t straight from an IV cable): 1 MPIC wafer + 2 indium gallium phosphide dust + 288 mB molten vanadium gallium → 1 HPIC wafer, 60 s. The vanadium gallium comes from the 4500 K EBF (RTM coils) via the extractor; a separate drum and fluid hatch. — `gtceu:iv_chemical_reactor`, `gtceu:hpic_wafer`, `gtceu:vanadium_gallium_bucket`
6. IV Cutter inside the Cleanroom: 1 HPIC wafer → 2 HPIC chips in 45 s at 7680 EU/t. That is exactly the two chips of one IV hatch. Hand the chips to a drawer with Keep Exact 8 beside the hatch assembler. — `gtceu:iv_cutter`, `gtceu:hpic_chip`
7. Voltage coil, IV Assembler with ghost circuit 1: 1 magnetic neodymium rod + 16 fine iridium wire (2 iridium ingots in a wiremill, circuit 3, 8 per ingot) → 1 IV voltage coil in 10 s at 7680 EU/t. Craft the first IV Assembler by hand: hull, 2 IV robot arms, 2 IV conveyors, 2 IV circuits, 2 platinum cables. — `gtceu:iv_assembler`, `gtceu:iv_voltage_coil`, `gtceu:magnetic_neodymium_rod`, `gtceu:fine_iridium_wire`
8. Hatch assemblers, one per hatch type: IV hull + 2 tungsten single cables (input hatch) or 2 tungsten springs (dynamo hatch) + 2 HPIC chips + 1 voltage coil + 3 B sodium potassium → hatch in 10 s at 7680 EU/t. The sodium potassium is a fluid in a hatch; make it with the LV chemical reactor from sodium and potassium dust. — `gtceu:iv_assembler`, `gtceu:iv_energy_input_hatch`, `gtceu:iv_energy_output_hatch`, `gtceu:sodium_potassium_bucket`
9. Easy to miss: the hatches are for multiblocks only. IV single machines (this line, the IV Assembler) run on IV cable, so build the first hatch for the Large Chemical Reactor (iridium and osmium) and the next ones for the EBF that makes shellite and for the reactor dynamo. — `gtceu:iv_energy_input_hatch`, `gtceu:large_chemical_reactor`

## Tips

- Recipes (MetaTileEntityMachineRecipeLoader, AssemblerRecipeLoader, CircuitRecipes; no pack override): IV Energy Input Hatch = IV hull + 2 tungsten single cables + 2 HPIC chips + 1 IV voltage coil + 3 B sodium potassium, assembler 200 ticks at 7680 EU/t. IV Dynamo Hatch = the same with 2 tungsten SPRINGS instead of cables. IV voltage coil = 1 magnetic neodymium rod + 16 fine iridium wire (circuit 1, 200 ticks, 7680 EU/t). Both need an IV Assembler (7680 EU/t), which is why the pack quest says the IV Assembler makes the energy hatches.
- HPIC chip line (CircuitRecipes): phosphorus boule (EBF, 2484 K, 64 silicon + 8 phosphorus + 2 small gallium arsenide dust + 8 B nitrogen, 12 000 ticks = 10 min, 480 EU/t; Kanthal coils reach 2700 K) → HV Cutter, CLEANROOM, 800 ticks → 32 phosphorus wafers → HV Laser Engraver, CLEANROOM, brown lens, 900 ticks at 480 EU/t → 1 MPIC wafer. HPIC wafer: IV Chemical Reactor, CLEANROOM, 1200 ticks at 7680 EU/t: 1 MPIC wafer + 2 indium gallium phosphide dust + 288 mB molten vanadium gallium. HPIC chips: IV Cutter, CLEANROOM, 900 ticks at 7680 EU/t: 1 HPIC wafer → 2 chips.
- So one boule feeds 32 hatches. One wafer of HPIC gives 2 chips = exactly one hatch. The slow, rare input is molten vanadium gallium: vanadium gallium is an EBF recipe at 4500 K (VA\[EV\] = 1920 EU/t, 1200 ticks = 60 s, argon gas tier), which needs RTM coils; 288 mB is 2 ingots from 2 × (3 vanadium + 1 gallium) dust (EV Mixer, 400 ticks, circuit 1: 3 vanadium + 1 gallium → 4 dust). Extract the ingot in an extractor (144 mB each).
- Indium gallium phosphide dust: ULV Mixer, circuit 1, 1 indium + 1 gallium + 1 phosphorus dust → 3 dust (200 ticks, 7 EU/t). Sodium potassium: Chemical Reactor, 1 sodium + 1 potassium dust → 1 B (300 ticks, 30 EU/t). Indium is the odd one out: Unverified: its source in this pack.
- The IV Chemical Reactor and IV Cutter are IV single machines: they need IV motors, pumps, conveyors and circuits from the iv\_components chain, and they take 7680 EU/t straight from an IV cable (single machines do not use hatches; the hatches here are for multiblocks). The room only has to be big enough for the machines; a cleanroom machine runs only while the room is 95 % clean.
- What the hatch unlocks: the Large Chemical Reactor rarest-metal step (iridium and osmium) at 7680 EU/t, the shellite superconductor EBF recipe (7680 EU/t, 4400 K), the Nuclear Reactor dynamo output (4096 EU/t per thorium rod) and every IV multiblock recipe above 1920 EU/t. The 1A hatch carries 8192 V; the 4A and 16A versions are pack assembler recipes (the stock ones are removed, kjs large\_energy\_hatches.js): 4A = IV 1A transformer + IV hatch + 2 platinum quadruple wire + 1 IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy (see luv\_hatches); 16A = IV 4A transformer + IV 4A hatch + 2 quadruple wire + 2 IV voltage coils + 4 plates. All of them need the IV Assembler.
- Sub-steps people skip: (1) four machines sit in the cleanroom (HV cutter, HV laser engraver, IV chemical reactor, IV cutter), so size the room for them before you close the walls; (2) the lens is brown, not the ones from the HV chain; (3) the HPIC wafer takes the vanadium gallium as a FLUID; (4) phosphorus is a boule recipe with nitrogen, not a plain furnace one; (5) iridium wire is 8 fine wires per ingot, so a coil is 2 iridium ingots.
- **Unverified** the lubricant amount of the cutters (copy the HV chain numbers), where indium comes from, whether a 16-circuit cleanroom fits the four machines (read the cleanroom size), and the brown lens recipe (look it up in EMI).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:iv_assembler` | 1 |
| `gtceu:iv_chemical_reactor` | 1 |
| `gtceu:iv_cutter` | 1 |
| `gtceu:hv_cutter` | 1 |
| `gtceu:hv_laser_engraver` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:cleanroom` | 1 |
| `gtceu:mv_mixer` | 1 |
| `gtceu:lv_chemical_reactor` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Needs:** [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](iv_components.md)
- **Main source for:** `gtceu:iv_energy_input_hatch`, `gtceu:iv_energy_output_hatch`, `gtceu:hpic_chip`, `gtceu:hpic_wafer`, `gtceu:iv_voltage_coil`
