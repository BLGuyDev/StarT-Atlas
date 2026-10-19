---
kind: chain
id: zpm_quantum
order: 1330
data:
  t: |-
    Quantum chips: nano CPU wafer + radon → qubit CPU wafer → 4 chips, and the extreme circuit board (reinforced epoxy → fiber board → extreme board)
  inf: true
  "n":
    - - rn
      - "50 mB radon + 1 indium gallium phosphide dust per wafer"
      - g
      - functionalstorage:oak_1
      - [[Radon, "gtceu:radon_bucket"], [Indium gallium phosphide dust, "gtceu:indium_gallium_phosphide_dust"]]
    - [nw, Nano CPU Wafer, i, "gtceu:nano_cpu_wafer"]
    - [m1, "EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t", m, "gtceu:ev_chemical_reactor"]
    - [qw, Qubit CPU Wafer, x, "gtceu:qbit_cpu_wafer"]
    - [m2, "EV Cutter in the cleanroom · 45 s · 1920 EU/t", m, "gtceu:ev_cutter"]
    - [qc, "Qubit CPU chip · 4 per wafer", o, "gtceu:qbit_cpu_chip"]
    - - re
      - Carbon fibers (or 1 fine borosilicate glass wire) + 144 mB epoxy
      - g
      - functionalstorage:oak_1
      - [[Carbon fibers, "gtceu:carbon_fibers"], [Epoxy, "gtceu:epoxy_bucket"]]
    - [m3, "LV Chemical Bath · 12 s · 16 EU/t", m, "gtceu:lv_chemical_bath"]
    - [rp, Reinforced Epoxy Resin plate, x, "gtceu:reinforced_epoxy_resin_plate"]
    - - fb
      - "8 annealed copper foil · 125 mB sulfuric acid"
      - g
      - functionalstorage:oak_1
      - [[Annealed copper foil, "gtceu:annealed_copper_foil"], [Sulfuric acid, "gtceu:sulfuric_acid_bucket"]]
    - [m4, "LV Chemical Reactor · 25 s · 10 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [fr, Fiber-Reinforced Circuit Board, x, "gtceu:fiber_reinforced_circuit_board"]
    - - m5
      - Chemical Reactor in the cleanroom · 60 s · 30 EU/t · 12 annealed copper foil + 1 B iron III chloride
      - m
      - gtceu:lv_chemical_reactor
    - [eb, Extreme Circuit Board, o, "gtceu:fiber_reinforced_printed_circuit_board"]
  e:
    - [rn, m1, "50 mB"]
    - [nw, m1, "1"]
    - [m1, qw, "1 / 60 s"]
    - [qw, m2, "1"]
    - [m2, qc, "4 / 45 s"]
    - [re, m3, "1"]
    - [m3, rp, "1 / 12 s"]
    - [rp, m4, "1"]
    - [fb, m4, "1"]
    - [m4, fr, "1 / 25 s"]
    - [fr, m5, "1"]
    - [m5, eb, "1 / 60 s"]
  tips:
    - |-
      Qubit CPU wafer (CircuitRecipes qbit_cpu_wafer_radon, not changed by the pack): 1 nano CPU wafer + 1 indium gallium phosphide dust + 50 mB radon, chemical reactor, CLEANROOM, 1200 ticks at VA[EV] = 1920 EU/t. The other recipe (qbit_cpu_wafer_quantum_eye: 1 nano CPU wafer + 2 quantum eyes + 288 mB gallium arsenide, 900 ticks) needs ender eyes, and the pack REMOVES every crafting recipe whose output is minecraft:ender_eye (mass_removals.js), so use the radon route. Cutter (cut_qbit_cpu): 1 wafer → 4 qubit CPU chips, 900 ticks at 1920 EU/t, cleanroom (EV Cutter). One ZPM mainframe needs 2 chips = half a wafer = 25 mB radon, so radon is a trickle, not a line.
    - |-
      Nano CPU wafer: the luv_chips chain (CPU wafer + 16 carbon fibers + 576 mB glowstone, EV chemical reactor in the cleanroom, 1200 ticks). Indium gallium phosphide dust is the same dust the HPIC and UHPIC wafers use (iv_hatches chain). So the quantum line costs one extra nano CPU wafer per 4 qubit chips and nothing from a new tier.
    - |-
      Radon sources (all verified in recipes, pick one): (1) the LuV Fusion Reactor, reflector tier 1: 144 mB gold + 100 mB mercury → 1000 mB radon, 28.8 s, 30 720 EU/t, start 200 MEU (kjs systems/fusion/fusion_scaling.js); (2) Large Chemical Reactor, 480 EU/t, 4000 ticks: 8 plutonium-239 ingots (returned) + 1 uranium-238 dust + 10 B air → 1 B radon (ReactorRecipes radon_from_uranium_238, not removed by the pack as far as the removal lists show); (3) distilling liquid ender air, IV Distillation Tower: 200 B → 1 B radon among nitrogen dioxide, deuterium, helium and others (DistillationRecipes); (4) the Exotic Gas Siphon (VA[ZPM]): 1000 mB radon per run in the End, 750 mB in Abydos, with circuit 4 / 2 (kjs systems/resource_gen/exotic_gas_siphon.js). Quantum stars (1250 mB radon each, HV Chemical Bath) are the big radon sink of the ZPM components.
    - |-
      Extreme board (CircuitRecipes, not changed by the pack): reinforced epoxy resin plate = 1 carbon fibers (or 1 fine borosilicate glass wire) + 144 mB epoxy in a Chemical Bath, 240 ticks at 16 EU/t. Fiber board = that plate + 8 annealed copper foil + 125 mB sulfuric acid, chemical reactor, 500 ticks at 10 EU/t (no cleanroom). Extreme circuit board = fiber board + 12 annealed copper foil + 1000 mB iron III chloride (or 2000 mB sodium persulfate), chemical reactor, CLEANROOM, 1200 ticks at 30 EU/t. The pack also adds a copper chloride etch (circuit_etching.js, 500 mB cupric chloride solution) but its only source is the Chemical Plant skip, so keep iron III chloride. Ids: gtceu:fiber_reinforced_circuit_board (unetched) and gtceu:fiber_reinforced_printed_circuit_board (extreme board).
    - |-
      Counts per ZPM mainframe on the quantum route: 6 extreme boards (2 + 2 + 2 over the three stages), 2 qubit chips, 2 nano CPU chips, 120 annealed copper foil in boards (6 x 20), 6 x 144 mB epoxy, 6 x 125 mB sulfuric acid, 6 B iron III chloride. Annealed copper foil: annealed copper ingot (EBF/freezer product of the copper line) into a bender, 1 plate → 4 foil.
    - |-
      Sub-steps people skip: (1) the fiber board step is NOT in the cleanroom but the extreme board step is; (2) borosilicate glass wire is an extruder recipe (96 EU/t, 160 ticks, 8 wire per borosilicate glass ingot) if you have no carbon fibers; (3) do not mix the fiber board with the multilayer board of the crystal line (zpm_crystal): different drawer; (4) 25 mB of radon needs only a tiny drum, set Keep Exact so a stuck reactor cannot swallow a whole bucket.
    - |-
      Unverified: which machine tier accepts the 50 mB radon input in an ordinary fluid hatch (a single EV hatch should), the supply of plutonium-239 for the Large Chemical Reactor route, and the mercury source for the fusion route.
  b:
    - ["gtceu:ev_chemical_reactor", 1]
    - ["gtceu:ev_cutter", 1]
    - ["gtceu:lv_chemical_bath", 1]
    - ["gtceu:lv_chemical_reactor", 2]
    - ["gtceu:cleanroom", 1]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 5]
    - ["gtceu:steel_drum", 4]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:nano_cpu_wafer
        - gtceu:indium_gallium_phosphide_dust
        - gtceu:annealed_copper_foil
      t: |-
        Drawers first, one per input: nano CPU wafers, indium gallium phosphide dust, carbon fibers, annealed copper foil. Drums: radon, epoxy, sulfuric acid, iron III chloride. Each machine gets its own input drawer/drum behind a Modular Router or Pipez pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:ev_chemical_reactor", "gtceu:radon_bucket", "gtceu:qbit_cpu_wafer"]
      t: |-
        Qubit wafer: the EV Chemical Reactor inside the cleanroom takes 1 nano CPU wafer + 1 indium gallium phosphide dust and 50 mB radon from the radon drum (Pipez fluid pipe) → 1 qubit CPU wafer in 60 s at 1920 EU/t. Keep Exact 2 on the output.
    - i: ["gtceu:ev_cutter", "gtceu:qbit_cpu_chip"]
      t: |-
        Cutter in the cleanroom, ghost nothing needed: 1 wafer → 4 qubit CPU chips in 45 s at 1920 EU/t. Chips into a drawer Keep Exact 8 (2 per mainframe).
    - i: ["gtceu:lv_chemical_bath", "gtceu:reinforced_epoxy_resin_plate", "gtceu:epoxy_bucket"]
      t: |-
        Reinforced plate: LV Chemical Bath, 1 carbon fibers + 144 mB epoxy → 1 plate in 12 s at 16 EU/t. Epoxy comes from the epoxy chain (large chemical reactor), a drum on a Pipez fluid pipe.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:fiber_reinforced_circuit_board", "gtceu:annealed_copper_foil"]
      t: |-
        Fiber board (outside the cleanroom): plate + 8 annealed copper foil + 125 mB sulfuric acid → fiber board in 25 s at 10 EU/t. Its own reactor, its own foil drawer.
    - i:
        - gtceu:lv_chemical_reactor
        - gtceu:iron_iii_chloride_bucket
        - gtceu:fiber_reinforced_printed_circuit_board
      t: |-
        Extreme board (inside the cleanroom): fiber board + 12 annealed copper foil + 1 B iron III chloride → extreme circuit board in 60 s at 30 EU/t. A third reactor; the board drawer feeds three circuit stages, so Keep Exact 16 and three routers.
    - i: ["functionalstorage:oak_1", "gtceu:fiber_reinforced_printed_circuit_board"]
      t: |-
        Easy to miss: build the boards before the circuit assemblers wait for them: 6 extreme boards per mainframe at 60 s each is 6 minutes of one reactor; make a second reactor or batch 24 boards while the line is idle.
---
# Quantum chips: nano CPU wafer + radon → qubit CPU wafer → 4 chips, and the extreme circuit board (reinforced epoxy → fiber board → extreme board)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_quantum` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [ZPM circuit (Quantum Mainframe)](../../plan/p12.md#zpmcirc)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-m1">
<div class="gt-head"><span class="gt-mname">EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="50 mB radon + 1 indium gallium phosphide dust per wafer (functionalstorage:oak_1) - 50 mB"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">50 mB radon + 1 indium gallium phosphide dust per wafer</span><span class="gt-sub"><span>Radon</span><span>Indium gallium phosphide dust</span></span><b class="gt-q">50 mB</b></span><span class="gt-slot" title="Nano CPU Wafer (gtceu:nano_cpu_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__nano_cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nano CPU Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Qubit CPU Wafer (gtceu:qbit_cpu_wafer) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__qbit_cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Qbit CPU Wafer</span><span class="gt-note">Qubit CPU Wafer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_reactor</code></div>
</div>
<div class="gt-panel t-ev" id="m-m2">
<div class="gt-head"><span class="gt-mname">EV Cutter in the cleanroom · 45 s · 1920 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Qubit CPU Wafer (gtceu:qbit_cpu_wafer) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__qbit_cpu_wafer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Qbit CPU Wafer</span><span class="gt-note">Qubit CPU Wafer</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_cutter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Qubit CPU chip · 4 per wafer (gtceu:qbit_cpu_chip) - 4 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__qbit_cpu_chip.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Qbit CPU Chip</span><span class="gt-note">Qubit CPU chip · 4 per wafer</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_cutter</code></div>
</div>
<div class="gt-panel t-lv" id="m-m3">
<div class="gt-head"><span class="gt-mname">LV Chemical Bath · 12 s · 16 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="Carbon fibers (or 1 fine borosilicate glass wire) + 144 mB epoxy (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">Carbon fibers (or 1 fine borosilicate glass wire) + 144 mB epoxy</span><span class="gt-sub"><span>Carbon fibers</span><span>Epoxy</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_bath.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">12 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Reinforced Epoxy Resin plate (gtceu:reinforced_epoxy_resin_plate) - 1 / 12 s"><img class="gt-ico" src="../../assets/icons/gtceu__reinforced_epoxy_resin_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Reinforced Epoxy Resin Plate</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_bath</code></div>
</div>
<div class="gt-panel t-lv" id="m-m4">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 25 s · 10 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Reinforced Epoxy Resin plate (gtceu:reinforced_epoxy_resin_plate) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__reinforced_epoxy_resin_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Reinforced Epoxy Resin Plate</span><b class="gt-q">1</b></span><span class="gt-slot gt-group" title="8 annealed copper foil · 125 mB sulfuric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 annealed copper foil · 125 mB sulfuric acid</span><span class="gt-sub"><span>Annealed copper foil</span><span>Sulfuric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">25 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Fiber-Reinforced Circuit Board (gtceu:fiber_reinforced_circuit_board) - 1 / 25 s"><img class="gt-ico" src="../../assets/icons/gtceu__fiber_reinforced_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fiber Reinforced Circuit Board</span><span class="gt-note">Fiber-Reinforced Circuit Board</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-lv" id="m-m5">
<div class="gt-head"><span class="gt-mname">Chemical Reactor in the cleanroom · 60 s · 30 EU/t · 12 annealed copper foil + 1 B iron III chloride</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Fiber-Reinforced Circuit Board (gtceu:fiber_reinforced_circuit_board) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__fiber_reinforced_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fiber Reinforced Circuit Board</span><span class="gt-note">Fiber-Reinforced Circuit Board</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Extreme Circuit Board (gtceu:fiber_reinforced_printed_circuit_board) - 1 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__fiber_reinforced_printed_circuit_board.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fiber Reinforced Printed Circuit Board</span><span class="gt-note">Extreme Circuit Board</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [EV Chemical Reactor in the cleanroom · 60 s · 1920 EU/t](#m-m1) → [EV Cutter in the cleanroom · 45 s · 1920 EU/t](#m-m2)
- [LV Chemical Bath · 12 s · 16 EU/t](#m-m3) → [LV Chemical Reactor · 25 s · 10 EU/t](#m-m4) → [Chemical Reactor in the cleanroom · 60 s · 30 EU/t · 12 annealed copper foil + 1 B iron III chloride](#m-m5)

## How to build

1. Drawers first, one per input: nano CPU wafers, indium gallium phosphide dust, carbon fibers, annealed copper foil. Drums: radon, epoxy, sulfuric acid, iron III chloride. Each machine gets its own input drawer/drum behind a Modular Router or Pipez pipe with an Item Filter, and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:nano_cpu_wafer`, `gtceu:indium_gallium_phosphide_dust`, `gtceu:annealed_copper_foil`
2. Qubit wafer: the EV Chemical Reactor inside the cleanroom takes 1 nano CPU wafer + 1 indium gallium phosphide dust and 50 mB radon from the radon drum (Pipez fluid pipe) → 1 qubit CPU wafer in 60 s at 1920 EU/t. Keep Exact 2 on the output. — `gtceu:ev_chemical_reactor`, `gtceu:radon_bucket`, `gtceu:qbit_cpu_wafer`
3. Cutter in the cleanroom, ghost nothing needed: 1 wafer → 4 qubit CPU chips in 45 s at 1920 EU/t. Chips into a drawer Keep Exact 8 (2 per mainframe). — `gtceu:ev_cutter`, `gtceu:qbit_cpu_chip`
4. Reinforced plate: LV Chemical Bath, 1 carbon fibers + 144 mB epoxy → 1 plate in 12 s at 16 EU/t. Epoxy comes from the epoxy chain (large chemical reactor), a drum on a Pipez fluid pipe. — `gtceu:lv_chemical_bath`, `gtceu:reinforced_epoxy_resin_plate`, `gtceu:epoxy_bucket`
5. Fiber board (outside the cleanroom): plate + 8 annealed copper foil + 125 mB sulfuric acid → fiber board in 25 s at 10 EU/t. Its own reactor, its own foil drawer. — `gtceu:lv_chemical_reactor`, `gtceu:fiber_reinforced_circuit_board`, `gtceu:annealed_copper_foil`
6. Extreme board (inside the cleanroom): fiber board + 12 annealed copper foil + 1 B iron III chloride → extreme circuit board in 60 s at 30 EU/t. A third reactor; the board drawer feeds three circuit stages, so Keep Exact 16 and three routers. — `gtceu:lv_chemical_reactor`, `gtceu:iron_iii_chloride_bucket`, `gtceu:fiber_reinforced_printed_circuit_board`
7. Easy to miss: build the boards before the circuit assemblers wait for them: 6 extreme boards per mainframe at 60 s each is 6 minutes of one reactor; make a second reactor or batch 24 boards while the line is idle. — `functionalstorage:oak_1`, `gtceu:fiber_reinforced_printed_circuit_board`

## Tips

- Qubit CPU wafer (CircuitRecipes qbit\_cpu\_wafer\_radon, not changed by the pack): 1 nano CPU wafer + 1 indium gallium phosphide dust + 50 mB radon, chemical reactor, CLEANROOM, 1200 ticks at VA\[EV\] = 1920 EU/t. The other recipe (qbit\_cpu\_wafer\_quantum\_eye: 1 nano CPU wafer + 2 quantum eyes + 288 mB gallium arsenide, 900 ticks) needs ender eyes, and the pack REMOVES every crafting recipe whose output is minecraft:ender\_eye (mass\_removals.js), so use the radon route. Cutter (cut\_qbit\_cpu): 1 wafer → 4 qubit CPU chips, 900 ticks at 1920 EU/t, cleanroom (EV Cutter). One ZPM mainframe needs 2 chips = half a wafer = 25 mB radon, so radon is a trickle, not a line.
- Nano CPU wafer: the luv\_chips chain (CPU wafer + 16 carbon fibers + 576 mB glowstone, EV chemical reactor in the cleanroom, 1200 ticks). Indium gallium phosphide dust is the same dust the HPIC and UHPIC wafers use (iv\_hatches chain). So the quantum line costs one extra nano CPU wafer per 4 qubit chips and nothing from a new tier.
- Radon sources (all verified in recipes, pick one): (1) the LuV Fusion Reactor, reflector tier 1: 144 mB gold + 100 mB mercury → 1000 mB radon, 28.8 s, 30 720 EU/t, start 200 MEU (kjs systems/fusion/fusion\_scaling.js); (2) Large Chemical Reactor, 480 EU/t, 4000 ticks: 8 plutonium-239 ingots (returned) + 1 uranium-238 dust + 10 B air → 1 B radon (ReactorRecipes radon\_from\_uranium\_238, not removed by the pack as far as the removal lists show); (3) distilling liquid ender air, IV Distillation Tower: 200 B → 1 B radon among nitrogen dioxide, deuterium, helium and others (DistillationRecipes); (4) the Exotic Gas Siphon (VA\[ZPM\]): 1000 mB radon per run in the End, 750 mB in Abydos, with circuit 4 / 2 (kjs systems/resource\_gen/exotic\_gas\_siphon.js). Quantum stars (1250 mB radon each, HV Chemical Bath) are the big radon sink of the ZPM components.
- Extreme board (CircuitRecipes, not changed by the pack): reinforced epoxy resin plate = 1 carbon fibers (or 1 fine borosilicate glass wire) + 144 mB epoxy in a Chemical Bath, 240 ticks at 16 EU/t. Fiber board = that plate + 8 annealed copper foil + 125 mB sulfuric acid, chemical reactor, 500 ticks at 10 EU/t (no cleanroom). Extreme circuit board = fiber board + 12 annealed copper foil + 1000 mB iron III chloride (or 2000 mB sodium persulfate), chemical reactor, CLEANROOM, 1200 ticks at 30 EU/t. The pack also adds a copper chloride etch (circuit\_etching.js, 500 mB cupric chloride solution) but its only source is the Chemical Plant skip, so keep iron III chloride. Ids: gtceu:fiber\_reinforced\_circuit\_board (unetched) and gtceu:fiber\_reinforced\_printed\_circuit\_board (extreme board).
- Counts per ZPM mainframe on the quantum route: 6 extreme boards (2 + 2 + 2 over the three stages), 2 qubit chips, 2 nano CPU chips, 120 annealed copper foil in boards (6 x 20), 6 x 144 mB epoxy, 6 x 125 mB sulfuric acid, 6 B iron III chloride. Annealed copper foil: annealed copper ingot (EBF/freezer product of the copper line) into a bender, 1 plate → 4 foil.
- Sub-steps people skip: (1) the fiber board step is NOT in the cleanroom but the extreme board step is; (2) borosilicate glass wire is an extruder recipe (96 EU/t, 160 ticks, 8 wire per borosilicate glass ingot) if you have no carbon fibers; (3) do not mix the fiber board with the multilayer board of the crystal line (zpm\_crystal): different drawer; (4) 25 mB of radon needs only a tiny drum, set Keep Exact so a stuck reactor cannot swallow a whole bucket.
- **Unverified** which machine tier accepts the 50 mB radon input in an ordinary fluid hatch (a single EV hatch should), the supply of plutonium-239 for the Large Chemical Reactor route, and the mercury source for the fusion route.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:ev_chemical_reactor` | 1 |
| `gtceu:ev_cutter` | 1 |
| `gtceu:lv_chemical_bath` | 1 |
| `gtceu:lv_chemical_reactor` | 2 |
| `gtceu:cleanroom` | 1 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 5 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Needs:** [LuV chips: Nano CPU chip (CPU wafer + carbon fibers + molten glowstone) and NOR memory chip (phosphorus wafer)](../luv/luv_chips.md)
- **Main source for:** `gtceu:qbit_cpu_chip`, `gtceu:qbit_cpu_wafer`, `gtceu:fiber_reinforced_printed_circuit_board`, `gtceu:fiber_reinforced_circuit_board`
