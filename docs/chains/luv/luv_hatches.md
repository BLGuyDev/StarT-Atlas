---
kind: chain
id: luv_hatches
order: 1270
data:
  t: |-
    LuV Energy Input Hatch: IV 4A hatch gives the 30 720 EU/t, osmiridium → LuV voltage coil, Assembly Line recipe
  inf: true
  "n":
    - - os
      - "1 osmium dust · 3 iridium dust"
      - g
      - functionalstorage:oak_1
      - [[Osmium dust, "gtceu:osmium_dust"], [Iridium dust, "gtceu:iridium_dust"]]
    - [mx, "Large Mixer on an IV 4A hatch · circuit 1 · 15 s · 30 720 EU/t", m, "gtceu:large_mixer"]
    - [od, "4 Osmiridium dust", x, "gtceu:osmiridium_dust"]
    - [eb, "EBF · RTM coils 4500 K · IV 4A hatch · 45 s · 30 720 EU/t", m, "gtceu:electric_blast_furnace"]
    - [vf, "Vacuum Freezer · 10 s · 1920 EU/t", m, "gtceu:vacuum_freezer"]
    - [oi, "Osmiridium ingot → wiremill → 16 fine wire", x, "gtceu:fine_osmiridium_wire"]
    - [sr, "1 magnetic samarium rod", i, "gtceu:magnetic_samarium_rod"]
    - [la, "Large Assembler on an IV 4A hatch · circuit 1 · 10 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [vc, "LuV Voltage Coil · 2 per hatch", x, "gtceu:luv_voltage_coil"]
    - - g1
      - LuV hull · 4 NbTi cable · 2 HPIC chip · 1 LuV circuit · 6 B sodium potassium · 720 mB solder
      - g
      - functionalstorage:oak_1
      - - [LuV Machine Hull, "gtceu:luv_machine_hull"]
        - [HPIC chip, "gtceu:hpic_chip"]
        - [Nanoprocessor Mainframe, "gtceu:nano_processor_mainframe"]
        - [Sodium potassium, "gtceu:sodium_potassium_bucket"]
    - [hi, "IV Energy Input Hatch 4A (IV Assembler · 5 s · 3840 EU/t)", x, "gtceu:iv_energy_input_hatch_4a"]
    - [al, "Assembly Line · 20 s · 30 720 EU/t", m, "gtceu:assembly_line"]
    - [lh, LuV Energy Input Hatch, o, "gtceu:luv_energy_input_hatch"]
  e:
    - [os, mx, "1 + 3"]
    - [mx, od, "4 / 15 s"]
    - [od, eb, "1"]
    - [eb, vf, "hot ingot / 45 s"]
    - [vf, oi, "1"]
    - [oi, la, "16"]
    - [sr, la, "1"]
    - [la, vc, "1 / 10 s"]
    - [vc, al, "2"]
    - [g1, al, "1"]
    - [hi, al, power]
    - [al, lh, "1 / 20 s"]
  tips:
    - |-
      The loop: the LuV hatch is an Assembly Line recipe at VA[LuV] = 30 720 EU/t (MetaTileEntityMachineRecipeLoader energy_hatch_luv): LuV hull + 4 niobium titanium single cables + 2 HPIC chips + 1 LuV circuit + 2 LuV voltage coils + 6 B sodium potassium + 720 mB soldering alloy, 400 ticks, scanner research of the IV Energy Input Hatch at an EV scanner (1920 EU/t). 30 720 EU/t is above an IV hatch (8192 V), so the line needs more than one amp: build the IV 4A hatch first.
    - |-
      IV Energy Input Hatch 4A (pack recipe, tiered_machines/large_energy_hatches.js, tier row iv): IV 1A Transformer + IV Energy Input Hatch + 2 platinum quadruple wire + 1 IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy, IV Assembler, 100 ticks at 3840 EU/t. The pack’s IV transformer (transformers.js) = IV hull + 1 niobium titanium single cable + 4 platinum single cables + 2 HPIC chips, 5 ticks at 30 EU/t; the NbTi cable is the LuV-rated cable of the luv_hull chain (PPS foil), so you need that chain a step early.
    - |-
      Hatch tiers in this pack: a 4A hatch counts one tier up (the quest: the LuV 4A gives ZPM recipe speeds, the 16A UV), so an IV 4A hatch should run 30 720 EU/t recipes. Unverified: read the tooltip of the IV 4A hatch in game before you rely on it; if it does not carry LuV recipes the fallback is a LuV dynamo hatch route, which is a circular recipe.
    - |-
      LuV voltage coil (AssemblerRecipeLoader): 1 magnetic samarium rod + 16 fine osmiridium wire, circuit 1, 200 ticks at 30 720 EU/t. Osmiridium (MixerRecipes, FirstDegreeMaterials): 1 osmium + 3 iridium dust → 4 dust, circuit 1, 300 ticks at 30 720 EU/t; EBF 4500 K at 30 720 EU/t for 900 ticks (45 s), freezer 1920 EU/t 200 ticks (10 s); 16 fine wire from 2 ingots. Every one of these steps is a 30 720 EU/t recipe: use the Large Mixer, the EBF and the Large Assembler (multis, any hatch combination) on the IV 4A hatch, since a single LuV machine needs a LuV cable network that you do not have yet.
    - |-
      A LuV Assembler (single machine) would be hull + 2 LuV robot arms + 2 LuV conveyors + 2 LuV circuits + 2 NbTi cables by the same crafting pattern as the IV one (derived, Unverified): it is the machine the naquadah coil block (30 720 EU/t, 700 ticks, HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel) and many ZPM chains need. Do the Large Assembler route first.
    - |-
      Iridium cost: a hatch eats 2 coils = 32 fine osmiridium wire = 4 osmiridium ingots; one ingot is 3/4 iridium + 1/4 osmium, so 3 iridium + 1 osmium per hatch, plus 2 samarium rods. The platinum group chain is the limit again; passive it (platline chain).
    - |-
      Sodium potassium: 1 sodium + 1 potassium dust → 1 B in a chemical reactor (300 ticks at 30 EU/t, iv_hatches chain); 6 B per hatch. HPIC chips and the LuV circuit: iv_hatches and luv_circuits chains.
    - |-
      Sub-steps people skip: (1) circuit 1 on the Large Mixer, Large Assembler and the EBF input bus; (2) two coils per hatch, not one; (3) the research stick is an IV Energy Input Hatch scan, so keep one IV hatch aside; (4) the samarium rod is the magnetic one (rod from a magnetised samarium ingot); (5) the Assembly Line needs the 4A hatch in its energy slot, not a plain IV hatch.
    - |-
      Unverified: the duration of the scanner research (default of the builder), the Large Mixer / Large Assembler accepting these recipes through a 4A hatch, and the samarium and niobium supply.
  b:
    - ["gtceu:large_mixer", 1]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:rtm_alloy_coil_block", 16]
    - ["gtceu:iv_energy_input_hatch_4a", 2]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:iv_assembler", 1]
    - ["gtceu:assembly_line", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 4]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["gtceu:iv_assembler", "gtceu:iv_energy_input_hatch", "gtceu:iv_voltage_coil"]
      t: |-
        IV transformer first: IV hull + 1 NbTi single cable + 4 platinum single cables + 2 HPIC chips (assembler, 5 ticks). Then the 4A hatch in an IV Assembler: transformer + IV Energy Input Hatch + 2 platinum quadruple wire + IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy, 3840 EU/t, 5 s. Make 2 of them: one for the Assembly Line and one for the EBF or Large Assembler.
    - i: ["gtceu:large_mixer", "gtceu:osmiridium_dust", "gtceu:iridium_dust"]
      t: |-
        Large Mixer on a 4A hatch, circuit 1: 1 osmium + 3 iridium dust → 4 osmiridium dust in 15 s at 30 720 EU/t. Dust drawers with Keep Exact 16 so a stuck mixer does not drain the iridium.
    - i: ["gtceu:electric_blast_furnace", "gtceu:rtm_alloy_coil_block", "gtceu:iv_energy_input_hatch_4a"]
      t: |-
        EBF with 16 RTM coil blocks (4500 K exactly) and a 4A hatch, ghost circuit 1: osmiridium dust → hot ingot in 45 s at 30 720 EU/t. Vacuum Freezer for the hot ingot (10 s, 1920 EU/t, no helium below 5000 K). Wiremill: 1 ingot → 8 fine wire, so 2 ingots per coil.
    - i: ["gtceu:large_assembler", "gtceu:magnetic_samarium_rod", "gtceu:luv_voltage_coil"]
      t: |-
        Large Assembler on a 4A hatch: circuit 1, magnetic samarium rod + 16 fine osmiridium wire → 1 LuV Voltage Coil in 10 s. Need 2 per hatch; output drawer Keep Exact 4.
    - i: ["gtceu:ev_scanner", "gtceu:data_stick", "gtceu:iv_energy_input_hatch"]
      t: Scan an IV Energy Input Hatch at the EV Scanner (1920 EU/t) onto a data stick and put it in the Assembly Line’s Data Access Hatch (luv_assembly_line chain).
    - i: ["gtceu:assembly_line", "gtceu:luv_machine_hull", "gtceu:hpic_chip"]
      t: |-
        Assembly Line bus order: LuV hull, 4 NbTi single cables, 2 HPIC chips, 1 LuV circuit, 2 LuV voltage coils; hatches: 6 B sodium potassium + 720 mB soldering alloy. It needs the 4A hatch, 400 ticks (20 s) at 30 720 EU/t → LuV Energy Input Hatch.
    - i: ["gtceu:luv_energy_input_hatch", "gtceu:large_circuit_assembler"]
      t: |-
        Easy to miss: the first LuV hatch goes to the LCAF (luv_lcaf) or the Large Chemical Reactor for the naquadah separation (30 720 EU/t); a 4A hatch version of each tier is a transformer + the 1A hatch (same recipe shape one tier up).
---
# LuV Energy Input Hatch: IV 4A hatch gives the 30 720 EU/t, osmiridium → LuV voltage coil, Assembly Line recipe

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_hatches` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-mx">
<div class="gt-head"><span class="gt-mname">Large Mixer on an IV 4A hatch · circuit 1 · 15 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 osmium dust · 3 iridium dust (functionalstorage:oak_1) - 1 + 3"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 osmium dust · 3 iridium dust</span><span class="gt-sub"><span>Osmium dust</span><span>Iridium dust</span></span><b class="gt-q">1 + 3</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Osmiridium dust (gtceu:osmiridium_dust) - 4 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__osmiridium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osmiridium Dust</span><span class="gt-note">4 Osmiridium dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · RTM coils 4500 K · IV 4A hatch · 45 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Osmiridium dust (gtceu:osmiridium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__osmiridium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osmiridium Dust</span><span class="gt-note">4 Osmiridium dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-vf" title="Vacuum Freezer · 10 s · 1920 EU/t (gtceu:vacuum_freezer) - hot ingot / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vacuum Freezer</span><span class="gt-note">Vacuum Freezer · 10 s · 1920 EU/t</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 10 s · 1920 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-eb" title="EBF · RTM coils 4500 K · IV 4A hatch · 45 s · 30 720 EU/t (gtceu:electric_blast_furnace) - hot ingot / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF · RTM coils 4500 K · IV 4A hatch · 45 s · 30 720 EU/t</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Osmiridium ingot → wiremill → 16 fine wire (gtceu:fine_osmiridium_wire) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__fine_osmiridium_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Osmiridium Wire</span><span class="gt-note">Osmiridium ingot → wiremill → 16 fine wire</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-la">
<div class="gt-head"><span class="gt-mname">Large Assembler on an IV 4A hatch · circuit 1 · 10 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Osmiridium ingot → wiremill → 16 fine wire (gtceu:fine_osmiridium_wire) - 16"><img class="gt-ico" src="../../assets/icons/gtceu__fine_osmiridium_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Osmiridium Wire</span><span class="gt-note">Osmiridium ingot → wiremill → 16 fine wire</span><b class="gt-q">16</b></span><span class="gt-slot" title="1 magnetic samarium rod (gtceu:magnetic_samarium_rod) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__magnetic_samarium_rod.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Magnetic Samarium Rod</span><span class="gt-note">1 magnetic samarium rod</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="LuV Voltage Coil · 2 per hatch (gtceu:luv_voltage_coil) - 1 / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Voltage Coil</span><span class="gt-note">LuV Voltage Coil · 2 per hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 20 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV Voltage Coil · 2 per hatch (gtceu:luv_voltage_coil) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__luv_voltage_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Voltage Coil</span><span class="gt-note">LuV Voltage Coil · 2 per hatch</span><b class="gt-q">2</b></span><span class="gt-slot gt-group" title="LuV hull · 4 NbTi cable · 2 HPIC chip · 1 LuV circuit · 6 B sodium potassium · 720 mB solder (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">LuV hull · 4 NbTi cable · 2 HPIC chip · 1 LuV circuit · 6 B sodium potassium · 720 mB solder</span><span class="gt-sub"><span>LuV Machine Hull</span><span>HPIC chip</span><span>Nanoprocessor Mainframe</span><span>Sodium potassium</span></span><b class="gt-q">1</b></span><span class="gt-slot" title="IV Energy Input Hatch 4A (IV Assembler · 5 s · 3840 EU/t) (gtceu:iv_energy_input_hatch_4a) - power"><img class="gt-ico" src="../../assets/icons/gtceu__iv_energy_input_hatch_4a.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Energy Input Hatch 4a</span><span class="gt-note">IV Energy Input Hatch 4A (IV Assembler · 5 s · 3840 EU/t)</span><b class="gt-q">power</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Energy Input Hatch (gtceu:luv_energy_input_hatch) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__luv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Energy Input Hatch</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
</div>

## Flow

- [Large Mixer on an IV 4A hatch · circuit 1 · 15 s · 30 720 EU/t](#m-mx) → [EBF · RTM coils 4500 K · IV 4A hatch · 45 s · 30 720 EU/t](#m-eb) → [Vacuum Freezer · 10 s · 1920 EU/t](#m-vf) → [Large Assembler on an IV 4A hatch · circuit 1 · 10 s · 30 720 EU/t](#m-la) → [Assembly Line · 20 s · 30 720 EU/t](#m-al)

## How to build

1. IV transformer first: IV hull + 1 NbTi single cable + 4 platinum single cables + 2 HPIC chips (assembler, 5 ticks). Then the 4A hatch in an IV Assembler: transformer + IV Energy Input Hatch + 2 platinum quadruple wire + IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy, 3840 EU/t, 5 s. Make 2 of them: one for the Assembly Line and one for the EBF or Large Assembler. — `gtceu:iv_assembler`, `gtceu:iv_energy_input_hatch`, `gtceu:iv_voltage_coil`
2. Large Mixer on a 4A hatch, circuit 1: 1 osmium + 3 iridium dust → 4 osmiridium dust in 15 s at 30 720 EU/t. Dust drawers with Keep Exact 16 so a stuck mixer does not drain the iridium. — `gtceu:large_mixer`, `gtceu:osmiridium_dust`, `gtceu:iridium_dust`
3. EBF with 16 RTM coil blocks (4500 K exactly) and a 4A hatch, ghost circuit 1: osmiridium dust → hot ingot in 45 s at 30 720 EU/t. Vacuum Freezer for the hot ingot (10 s, 1920 EU/t, no helium below 5000 K). Wiremill: 1 ingot → 8 fine wire, so 2 ingots per coil. — `gtceu:electric_blast_furnace`, `gtceu:rtm_alloy_coil_block`, `gtceu:iv_energy_input_hatch_4a`
4. Large Assembler on a 4A hatch: circuit 1, magnetic samarium rod + 16 fine osmiridium wire → 1 LuV Voltage Coil in 10 s. Need 2 per hatch; output drawer Keep Exact 4. — `gtceu:large_assembler`, `gtceu:magnetic_samarium_rod`, `gtceu:luv_voltage_coil`
5. Scan an IV Energy Input Hatch at the EV Scanner (1920 EU/t) onto a data stick and put it in the Assembly Line’s Data Access Hatch (luv\_assembly\_line chain). — `gtceu:ev_scanner`, `gtceu:data_stick`, `gtceu:iv_energy_input_hatch`
6. Assembly Line bus order: LuV hull, 4 NbTi single cables, 2 HPIC chips, 1 LuV circuit, 2 LuV voltage coils; hatches: 6 B sodium potassium + 720 mB soldering alloy. It needs the 4A hatch, 400 ticks (20 s) at 30 720 EU/t → LuV Energy Input Hatch. — `gtceu:assembly_line`, `gtceu:luv_machine_hull`, `gtceu:hpic_chip`
7. Easy to miss: the first LuV hatch goes to the LCAF (luv\_lcaf) or the Large Chemical Reactor for the naquadah separation (30 720 EU/t); a 4A hatch version of each tier is a transformer + the 1A hatch (same recipe shape one tier up). — `gtceu:luv_energy_input_hatch`, `gtceu:large_circuit_assembler`

## Tips

- The loop: the LuV hatch is an Assembly Line recipe at VA\[LuV\] = 30 720 EU/t (MetaTileEntityMachineRecipeLoader energy\_hatch\_luv): LuV hull + 4 niobium titanium single cables + 2 HPIC chips + 1 LuV circuit + 2 LuV voltage coils + 6 B sodium potassium + 720 mB soldering alloy, 400 ticks, scanner research of the IV Energy Input Hatch at an EV scanner (1920 EU/t). 30 720 EU/t is above an IV hatch (8192 V), so the line needs more than one amp: build the IV 4A hatch first.
- IV Energy Input Hatch 4A (pack recipe, tiered\_machines/large\_energy\_hatches.js, tier row iv): IV 1A Transformer + IV Energy Input Hatch + 2 platinum quadruple wire + 1 IV voltage coil + 2 tungsten steel plates + 144 mB soldering alloy, IV Assembler, 100 ticks at 3840 EU/t. The pack’s IV transformer (transformers.js) = IV hull + 1 niobium titanium single cable + 4 platinum single cables + 2 HPIC chips, 5 ticks at 30 EU/t; the NbTi cable is the LuV-rated cable of the luv\_hull chain (PPS foil), so you need that chain a step early.
- Hatch tiers in this pack: a 4A hatch counts one tier up (the quest: the LuV 4A gives ZPM recipe speeds, the 16A UV), so an IV 4A hatch should run 30 720 EU/t recipes. Unverified: read the tooltip of the IV 4A hatch in game before you rely on it; if it does not carry LuV recipes the fallback is a LuV dynamo hatch route, which is a circular recipe.
- LuV voltage coil (AssemblerRecipeLoader): 1 magnetic samarium rod + 16 fine osmiridium wire, circuit 1, 200 ticks at 30 720 EU/t. Osmiridium (MixerRecipes, FirstDegreeMaterials): 1 osmium + 3 iridium dust → 4 dust, circuit 1, 300 ticks at 30 720 EU/t; EBF 4500 K at 30 720 EU/t for 900 ticks (45 s), freezer 1920 EU/t 200 ticks (10 s); 16 fine wire from 2 ingots. Every one of these steps is a 30 720 EU/t recipe: use the Large Mixer, the EBF and the Large Assembler (multis, any hatch combination) on the IV 4A hatch, since a single LuV machine needs a LuV cable network that you do not have yet.
- A LuV Assembler (single machine) would be hull + 2 LuV robot arms + 2 LuV conveyors + 2 LuV circuits + 2 NbTi cables by the same crafting pattern as the IV one (derived, Unverified): it is the machine the naquadah coil block (30 720 EU/t, 700 ticks, HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel) and many ZPM chains need. Do the Large Assembler route first.
- Iridium cost: a hatch eats 2 coils = 32 fine osmiridium wire = 4 osmiridium ingots; one ingot is 3/4 iridium + 1/4 osmium, so 3 iridium + 1 osmium per hatch, plus 2 samarium rods. The platinum group chain is the limit again; passive it (platline chain).
- Sodium potassium: 1 sodium + 1 potassium dust → 1 B in a chemical reactor (300 ticks at 30 EU/t, iv\_hatches chain); 6 B per hatch. HPIC chips and the LuV circuit: iv\_hatches and luv\_circuits chains.
- Sub-steps people skip: (1) circuit 1 on the Large Mixer, Large Assembler and the EBF input bus; (2) two coils per hatch, not one; (3) the research stick is an IV Energy Input Hatch scan, so keep one IV hatch aside; (4) the samarium rod is the magnetic one (rod from a magnetised samarium ingot); (5) the Assembly Line needs the 4A hatch in its energy slot, not a plain IV hatch.
- **Unverified** the duration of the scanner research (default of the builder), the Large Mixer / Large Assembler accepting these recipes through a 4A hatch, and the samarium and niobium supply.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_mixer` | 1 |
| `gtceu:large_assembler` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:rtm_alloy_coil_block` | 16 |
| `gtceu:iv_energy_input_hatch_4a` | 2 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:iv_assembler` | 1 |
| `gtceu:assembly_line` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 4 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:luv_energy_input_hatch`, `gtceu:luv_voltage_coil`, `gtceu:osmiridium_dust`, `gtceu:iv_energy_input_hatch_4a`
