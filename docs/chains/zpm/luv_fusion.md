---
kind: chain
id: luv_fusion
order: 1290
data:
  t: |-
    Fusion MK I: superconducting coil + ZPM circuits + UHPIC chips in the Assembly Line, then europium in the reactor (reflector tier 1)
  inf: true
  "n":
    - - sg
      - Enriched naquadah frame · 16 ITBTC double wire · 32 NbTi foil · 1728 mB molten trinium
      - g
      - functionalstorage:oak_1
      - - [Enriched naquadah frame, "gtceu:enriched_naquadah_frame"]
        - [ITBTC double wire, "gtceu:indium_tin_barium_titanium_cuprate_double_wire"]
        - [NbTi foil, "gtceu:niobium_titanium_foil"]
        - [Trinium, "gtceu:trinium_bucket"]
    - [as, "Assembler on a 4A hatch · 5 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [sc, Superconducting Coil, x, "gtceu:superconducting_coil"]
    - - fg
      - |-
        4 ZPM circuit · double plutonium-241 plate · double osmiridium plate · 2 IV field generator · 64 UHPIC chip · 32 ITBTC single wire · 1152 mB solder + 1152 mB molten NbTi
      - g
      - functionalstorage:oak_1
      - - [IV Field Generator, "gtceu:iv_field_generator"]
        - [UHPIC chip, "gtceu:uhpic_chip"]
        - [ITBTC single wire, "gtceu:indium_tin_barium_titanium_cuprate_single_wire"]
    - [al, "Assembly Line · 60 s · 30 720 EU/t (scan: superconducting coil, IV scanner)", m, "gtceu:assembly_line"]
    - [fr, LuV Fusion Reactor, o, "start_core:luv_fusion_reactor"]
    - [rf, "Basic reflector casing (neutron reflector tier 1)", i, "kubejs:basic_reflector_casing"]
    - [nd, "144 mB neodymium", f, "gtceu:neodymium_bucket"]
    - [hy, "3 B hydrogen", f, "gtceu:hydrogen_bucket"]
    - [fm, "Reactor run · 28.8 s · 24 576 EU/t · start 150 MEU", m, "start_core:luv_fusion_reactor"]
    - [eu, "144 mB europium", o, "gtceu:europium_bucket"]
  e:
    - [sg, as, "1"]
    - [as, sc, "1 / 5 s"]
    - [sc, al, "1"]
    - [fg, al, "1"]
    - [al, fr, "1 / 60 s"]
    - [fr, fm, controller]
    - [rf, fm, reflector]
    - [nd, fm, "144 mB"]
    - [hy, fm, "3 B"]
    - [fm, eu, "144 mB / 28.8 s"]
  tips:
    - |-
      Naming: "LuV" in start_core:luv_fusion_reactor = Fusion MK I, assembled with LuV-voltage power, but ZPM-gated by its 4 ZPM circuits. MK II (zpm_fusion_reactor) needs Research Station research of the MK I (CWU 16), MK III (uv_fusion_reactor) research of MK II (CWU 96). Pack recipes (kjs systems/fusion/start_fusion_machines.js; the vanilla ones are removed): superconducting coil (LuV row) = 1 enriched naquadah frame + 16 indium tin barium titanium cuprate double wire + 32 niobium titanium foil + 1728 mB molten trinium, assembler, 100 ticks at VA[IV] x 4 = 30 720 EU/t. LuV Fusion Reactor = 1 superconducting coil + 4 ZPM circuits + 1 double plutonium-241 plate + 1 double osmiridium plate + 2 IV field generators + 64 UHPIC chips + 32 ITBTC single wire, 1152 mB soldering alloy + 1152 mB molten niobium titanium, Assembly Line 1200 ticks at 30 720 EU/t, scanner research of the superconducting coil (1200 ticks, 7680 EU/t). So MK I needs only a scanner, no Research Station (which is why fusion1 sits before research in the plan); the Research Station is first needed for MK II.
    - |-
      Europium recipe (kjs fusion_scaling.js): 144 mB neodymium + 3000 mB hydrogen → 144 mB europium, 24 576 EU/t, 28.8 s, reflector tier 1, start energy 150 MEU. The machine type is the reflector fusion reactor: it needs the Basic Reflector Casing blocks. Quest: europium is the only thing you really use MK I for, so passive it. This is the only europium source before Abydos (the xenotime rare earth process, EBF 7500 K): there is no vein, sieve or earlier recipe. MK II then asks for 2 double europium plates.
    - |-
      Basic neutron reflector (panel): 1 ruridit plate + 2 double beryllium plates + 1 double tungsten carbide plate + 2304 mB molten tin alloy, assembler in the cleanroom, 1000 ticks at VHA[EV]. Basic reflector casing (2 per craft): 2 enriched naquadah frames + 1 IV field generator + 6 basic panels + 4 niobium nitride single cables + 288 mB polybenzimidazole + 6 trinium foil, 400 ticks at 7680 EU/t, cleanroom. So reflectors, the coil and the reactor all need ENRICHED NAQUADAH and TRINIUM: the naquadah by-product line (Large Chemical Reactor at 30 720 EU/t) comes before fusion.
    - |-
      UHPIC chips: HPIC wafer + 8 indium gallium phosphide dust + 576 mB molten naquadah, LuV chemical reactor in the cleanroom, 1200 ticks at 30 720 EU/t; then a LuV cutter, 900 ticks, 2 chips per wafer (CircuitRecipes). 64 chips = 32 UHPIC wafers = 32 HPIC wafers (iv_hatches chain: MPIC wafer + indium gallium phosphide + vanadium gallium) = 32 phosphorus wafers (one boule). A LuV Chemical Reactor and LuV Cutter are LuV hull + LuV parts machines: this is where the LuV component lines pay off.
    - |-
      ZPM circuits (4): the quantum processor mainframe is the first ZPM circuit; the quest places the LuV fusion reactor after the UHPIC and superconducting coil quests but its recipe wants 4 ZPM circuits, so the quantum line (quantum computer needs the IV Circuit Assembler) must be done. Quantum processor line: see the luv_circuits tips.
    - |-
      Sub-steps people skip: (1) the reactor controller is not enough: the reflector casings are separate crafts (and the superconducting coil blocks go into the fusion coil); (2) start energy 150 MEU needs a big buffer: a Power Substation or lots of batteries; (3) the plutonium-241 double plate: Unverified source; (4) keep UHPIC chips in a drawer with Keep Exact 64; (5) hydrogen 3 B per run: a pipe with a pump cover.
    - |-
      Unverified: the LuV reactor multiblock layout (not in the extracted multis), plutonium-241 source, neodymium route (neodymium is already needed for the IV motors), and the casing count of the reactor.
  b:
    - ["start_core:luv_fusion_reactor", 1]
    - ["gtceu:assembly_line", 1]
    - ["gtceu:large_assembler", 1]
    - ["gtceu:iv_scanner", 1]
    - ["kubejs:basic_reflector_casing", 16]
    - ["functionalstorage:oak_1", 18]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["gtceu:superconducting_coil", "gtceu:enriched_naquadah_frame", "gtceu:trinium_bucket"]
      t: |-
        Coil first: enriched naquadah frame + 16 ITBTC double wire + 32 NbTi foil + 1728 mB molten trinium in a Large Assembler on a 4A hatch (or a LuV Assembler): 5 s → 1 superconducting coil. Enriched naquadah and trinium come from the naquadah by-product line; ITBTC from the field-generator chain.
    - i: ["gtceu:uhpic_chip", "gtceu:iv_field_generator"]
      t: |-
        Chips and parts: 64 UHPIC chips (32 wafers), 2 IV field generators, 4 ZPM circuits, 1 double plutonium-241 plate, 1 double osmiridium plate, 32 ITBTC single wire; all in drawers, one per bus.
    - i: ["gtceu:iv_scanner", "gtceu:superconducting_coil", "gtceu:data_stick"]
      t: Scan the superconducting coil at the IV Scanner (60 s, 7680 EU/t) onto a stick; put it in the Assembly Line’s Data Access Hatch.
    - i: ["gtceu:assembly_line", "start_core:luv_fusion_reactor"]
      t: |-
        Assembly Line at 30 720 EU/t (a 4A hatch): load the buses in recipe order, fluids 1152 mB soldering alloy + 1152 mB molten niobium titanium. 60 s → LuV Fusion Reactor controller.
    - i: ["kubejs:basic_reflector_casing", "gtceu:enriched_naquadah_frame"]
      t: |-
        Reflectors: basic panels (ruridit + beryllium + tungsten carbide, cleanroom assembler), then basic reflector casings (2 per craft). Count the casings of the reactor structure before you build; the reactor needs the casings around its coil ring. Unverified count.
    - i: ["start_core:luv_fusion_reactor", "gtceu:europium_bucket", "gtceu:hydrogen_bucket"]
      t: |-
        Run: 144 mB neodymium + 3 B hydrogen → 144 mB europium, 28.8 s, 24 576 EU/t, 150 MEU start. Feed through fluid hatches with Pipez pumps; output to a drum. Passive it.
    - i: ["gtceu:power_substation", "start_core:luv_fusion_reactor"]
      t: |-
        Easy to miss: the start energy is stored inside the reactor via the energy hatches, so a plain IV hatch network is not enough; see the Power Substation chain for the buffer.
---
# Fusion MK I: superconducting coil + ZPM circuits + UHPIC chips in the Assembly Line, then europium in the reactor (reflector tier 1)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_fusion` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Fusion MK I (europium) and plasma power](../../plan/p12.md#fusion1)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler on a 4A hatch · 5 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Enriched naquadah frame · 16 ITBTC double wire · 32 NbTi foil · 1728 mB molten trinium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Enriched naquadah frame · 16 ITBTC double wire · 32 NbTi foil · 1728 mB molten trinium</span><span class="gt-sub"><span>Enriched naquadah frame</span><span>ITBTC double wire</span><span>NbTi foil</span><span>Trinium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Superconducting Coil (gtceu:superconducting_coil) - 1 / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__superconducting_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superconducting Coil</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · 60 s · 30 720 EU/t (scan: superconducting coil, IV scanner)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Superconducting Coil (gtceu:superconducting_coil) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__superconducting_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Superconducting Coil</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="4 ZPM circuit · double plutonium-241 plate · double osmiridium plate · 2 IV field generator · 64 UHPIC chip · 32 ITBTC single wire · 1152 mB solder + 1152 mB molten NbTi (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 ZPM circuit · double plutonium-241 plate · double osmiridium plate · 2 IV field generator · 64 UHPIC chip · 32 ITBTC single wire · 1152 mB solder + 1152 mB molten NbTi</span><span class="gt-sub"><span>IV Field Generator</span><span>UHPIC chip</span><span>ITBTC single wire</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="LuV Fusion Reactor (start_core:luv_fusion_reactor) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/start_core__luv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Fusion Reactor</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-luv" id="m-fm">
<div class="gt-head"><span class="gt-mname">Reactor run · 28.8 s · 24 576 EU/t · start 150 MEU</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-outp" title="LuV Fusion Reactor (start_core:luv_fusion_reactor) - controller"><img class="gt-ico" src="../../assets/icons/start_core__luv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Fusion Reactor</span><b class="gt-q">controller</b></span><span class="gt-slot" title="Basic reflector casing (neutron reflector tier 1) (kubejs:basic_reflector_casing) - reflector"><img class="gt-ico" src="../../assets/icons/kubejs__basic_reflector_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Basic Reflector Casing</span><span class="gt-note">Basic reflector casing (neutron reflector tier 1)</span><b class="gt-q">reflector</b></span><span class="gt-slot gt-fluid" title="144 mB neodymium (gtceu:neodymium_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__neodymium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neodymium</span><span class="gt-note">144 mB neodymium</span><b class="gt-q">144 mB</b></span><span class="gt-slot gt-fluid" title="3 B hydrogen (gtceu:hydrogen_bucket) - 3 B"><img class="gt-ico" src="../../assets/icons/gtceu__hydrogen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hydrogen</span><span class="gt-note">3 B hydrogen</span><b class="gt-q">3 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__luv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span><span class="gt-stat">28.8 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="144 mB europium (gtceu:europium_bucket) - 144 mB / 28.8 s"><img class="gt-ico" src="../../assets/icons/gtceu__europium_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Europium Bucket</span><span class="gt-note">144 mB europium</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:luv_fusion_reactor</code></div>
</div>
</div>

## Flow

- [Assembler on a 4A hatch · 5 s · 30 720 EU/t](#m-as) → [Assembly Line · 60 s · 30 720 EU/t (scan: superconducting coil, IV scanner)](#m-al) → [Reactor run · 28.8 s · 24 576 EU/t · start 150 MEU](#m-fm)

## How to build

1. Coil first: enriched naquadah frame + 16 ITBTC double wire + 32 NbTi foil + 1728 mB molten trinium in a Large Assembler on a 4A hatch (or a LuV Assembler): 5 s → 1 superconducting coil. Enriched naquadah and trinium come from the naquadah by-product line; ITBTC from the field-generator chain. — `gtceu:superconducting_coil`, `gtceu:enriched_naquadah_frame`, `gtceu:trinium_bucket`
2. Chips and parts: 64 UHPIC chips (32 wafers), 2 IV field generators, 4 ZPM circuits, 1 double plutonium-241 plate, 1 double osmiridium plate, 32 ITBTC single wire; all in drawers, one per bus. — `gtceu:uhpic_chip`, `gtceu:iv_field_generator`
3. Scan the superconducting coil at the IV Scanner (60 s, 7680 EU/t) onto a stick; put it in the Assembly Line’s Data Access Hatch. — `gtceu:iv_scanner`, `gtceu:superconducting_coil`, `gtceu:data_stick`
4. Assembly Line at 30 720 EU/t (a 4A hatch): load the buses in recipe order, fluids 1152 mB soldering alloy + 1152 mB molten niobium titanium. 60 s → LuV Fusion Reactor controller. — `gtceu:assembly_line`, `start_core:luv_fusion_reactor`
5. Reflectors: basic panels (ruridit + beryllium + tungsten carbide, cleanroom assembler), then basic reflector casings (2 per craft). Count the casings of the reactor structure before you build; the reactor needs the casings around its coil ring. Unverified count. — `kubejs:basic_reflector_casing`, `gtceu:enriched_naquadah_frame`
6. Run: 144 mB neodymium + 3 B hydrogen → 144 mB europium, 28.8 s, 24 576 EU/t, 150 MEU start. Feed through fluid hatches with Pipez pumps; output to a drum. Passive it. — `start_core:luv_fusion_reactor`, `gtceu:europium_bucket`, `gtceu:hydrogen_bucket`
7. Easy to miss: the start energy is stored inside the reactor via the energy hatches, so a plain IV hatch network is not enough; see the Power Substation chain for the buffer. — `gtceu:power_substation`, `start_core:luv_fusion_reactor`

## Tips

- Naming: "LuV" in start\_core:luv\_fusion\_reactor = Fusion MK I, assembled with LuV-voltage power, but ZPM-gated by its 4 ZPM circuits. MK II (zpm\_fusion\_reactor) needs Research Station research of the MK I (CWU 16), MK III (uv\_fusion\_reactor) research of MK II (CWU 96). Pack recipes (kjs systems/fusion/start\_fusion\_machines.js; the vanilla ones are removed): superconducting coil (LuV row) = 1 enriched naquadah frame + 16 indium tin barium titanium cuprate double wire + 32 niobium titanium foil + 1728 mB molten trinium, assembler, 100 ticks at VA\[IV\] x 4 = 30 720 EU/t. LuV Fusion Reactor = 1 superconducting coil + 4 ZPM circuits + 1 double plutonium-241 plate + 1 double osmiridium plate + 2 IV field generators + 64 UHPIC chips + 32 ITBTC single wire, 1152 mB soldering alloy + 1152 mB molten niobium titanium, Assembly Line 1200 ticks at 30 720 EU/t, scanner research of the superconducting coil (1200 ticks, 7680 EU/t). So MK I needs only a scanner, no Research Station (which is why fusion1 sits before research in the plan); the Research Station is first needed for MK II.
- Europium recipe (kjs fusion\_scaling.js): 144 mB neodymium + 3000 mB hydrogen → 144 mB europium, 24 576 EU/t, 28.8 s, reflector tier 1, start energy 150 MEU. The machine type is the reflector fusion reactor: it needs the Basic Reflector Casing blocks. Quest: europium is the only thing you really use MK I for, so passive it. This is the only europium source before Abydos (the xenotime rare earth process, EBF 7500 K): there is no vein, sieve or earlier recipe. MK II then asks for 2 double europium plates.
- Basic neutron reflector (panel): 1 ruridit plate + 2 double beryllium plates + 1 double tungsten carbide plate + 2304 mB molten tin alloy, assembler in the cleanroom, 1000 ticks at VHA\[EV\]. Basic reflector casing (2 per craft): 2 enriched naquadah frames + 1 IV field generator + 6 basic panels + 4 niobium nitride single cables + 288 mB polybenzimidazole + 6 trinium foil, 400 ticks at 7680 EU/t, cleanroom. So reflectors, the coil and the reactor all need ENRICHED NAQUADAH and TRINIUM: the naquadah by-product line (Large Chemical Reactor at 30 720 EU/t) comes before fusion.
- UHPIC chips: HPIC wafer + 8 indium gallium phosphide dust + 576 mB molten naquadah, LuV chemical reactor in the cleanroom, 1200 ticks at 30 720 EU/t; then a LuV cutter, 900 ticks, 2 chips per wafer (CircuitRecipes). 64 chips = 32 UHPIC wafers = 32 HPIC wafers (iv\_hatches chain: MPIC wafer + indium gallium phosphide + vanadium gallium) = 32 phosphorus wafers (one boule). A LuV Chemical Reactor and LuV Cutter are LuV hull + LuV parts machines: this is where the LuV component lines pay off.
- ZPM circuits (4): the quantum processor mainframe is the first ZPM circuit; the quest places the LuV fusion reactor after the UHPIC and superconducting coil quests but its recipe wants 4 ZPM circuits, so the quantum line (quantum computer needs the IV Circuit Assembler) must be done. Quantum processor line: see the luv\_circuits tips.
- Sub-steps people skip: (1) the reactor controller is not enough: the reflector casings are separate crafts (and the superconducting coil blocks go into the fusion coil); (2) start energy 150 MEU needs a big buffer: a Power Substation or lots of batteries; (3) the plutonium-241 double plate: Unverified source; (4) keep UHPIC chips in a drawer with Keep Exact 64; (5) hydrogen 3 B per run: a pipe with a pump cover.
- **Unverified** the LuV reactor multiblock layout (not in the extracted multis), plutonium-241 source, neodymium route (neodymium is already needed for the IV motors), and the casing count of the reactor.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:luv_fusion_reactor` | 1 |
| `gtceu:assembly_line` | 1 |
| `gtceu:large_assembler` | 1 |
| `gtceu:iv_scanner` | 1 |
| `kubejs:basic_reflector_casing` | 16 |
| `functionalstorage:oak_1` | 18 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:superconducting_coil`, `start_core:luv_fusion_reactor`, `gtceu:europium_bucket`
