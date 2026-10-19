---
kind: chain
id: combo_ecr
order: 2350
data:
  t: "Combo: Extreme Chemical Reactor with a parallel hatch"
  inf: true
  "n":
    - [lcr, Large Chemical Reactor, i, "gtceu:large_chemical_reactor"]
    - [ic, "1 IV circuit", i, "gtceu:micro_processor_mainframe"]
    - [em, "2 IV emitters", i, "gtceu:iv_emitter"]
    - [nq, "Naquadah pipes, plates and wire", i, "gtceu:naquadah_ingot"]
    - - st
      - |-
        5x5x5: inert PTFE casings, heat vents, PTFE pipes, black steel frames, 3 coils
      - i
      - gtceu:inert_machine_casing
    - [pa, "Parallel hatch (IV..UV, never shared)", x, "gtceu:iv_parallel_hatch"]
    - [ct, Extreme Chemical Reactor, m, "gtceu:extreme_chemical_reactor"]
    - [cr, "Cleanroom of at least 7x7x7 (cleanroom recipes only)", x, "gtceu:cleanroom"]
    - [out, Large chemical recipes in parallel, o, "gtceu:extreme_chemical_reactor"]
  e:
    - [lcr, ct, craft]
    - [ic, ct]
    - [em, ct]
    - [nq, ct]
    - [st, ct, structure]
    - [pa, ct, parallels]
    - [cr, ct, optional]
    - [ct, out]
  tips:
    - |-
      ECR vs LCR (gtsrc GTMultiMachines): both run LARGE_CHEMICAL recipes; only the ECR lists PARALLEL_HATCH in its modifiers and allows a parallel hatch. The parallel hatch is optional, comes in IV to UV (Elite, Master, Ultimate, Super; GCYMMachines) and is never shared between machines.
    - |-
      Controller (MetaTileEntityLoader): Large Chemical Reactor + 1 IV circuit + 2 IV emitters + 2 huge naquadah pipes + 2 naquadah double plates + naquadah quadruple wire. Naquadah comes from the Dimensional Destabiliser (LuV), so this is a LuV-time build even though the circuit is IV.
    - |-
      Structure 5x5x5 (multis): 62 inert PTFE casings (10 minimum), 24 heat vents, 15 PTFE pipe casings, 8 black steel frames, 3 coils. Pack config: parallelLCR true and lcrCoilBenefits true, so better coils help; it is not perfect overclock.
    - |-
      Cleanroom: the ECR pattern itself does not ask for one; recipes marked cleanroom do. A 5x5x5 machine does not fit the smallest cleanroom: plan a room of at least 7x7x7. Unverified: whether the whole ECR or only its controller must be inside.
    - |-
      Use: naquadah separation (zpm_naq_products) is a LARGE_CHEMICAL recipe, so an ECR with a parallel hatch batches it. Community report: one ECR outran a quad of furnaces on naquadria.
  b:
    - ["gtceu:extreme_chemical_reactor", 1]
    - ["gtceu:iv_parallel_hatch", 1]
    - ["gtceu:inert_machine_casing", 62]
    - ["gtceu:heat_vent", 24]
    - ["gtceu:ptfe_pipe_casing", 15]
    - ["gtceu:black_steel_frame", 8]
  how:
    - i: ["gtceu:extreme_chemical_reactor", "gtceu:large_chemical_reactor"]
      t: |-
        Controller: an existing Large Chemical Reactor + IV circuit + 2 IV emitters + naquadah pipes, plates and wire. Build it once the naquadah line runs.
    - i: ["gtceu:inert_machine_casing", "gtceu:heat_vent", "gtceu:ptfe_pipe_casing"]
      t: |-
        Structure: 5x5x5 of inert PTFE casings with heat vents, a PTFE pipe core, black steel frames and 3 coils; hatches and buses replace casings.
    - i: ["gtceu:iv_parallel_hatch"]
      t: Add one parallel hatch (it cannot be shared with a neighbour). Batch the long LARGE_CHEMICAL chains into it instead of building more LCRs.
---
# Combo: Extreme Chemical Reactor with a parallel hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_ecr` · **Tags:** Infinite source

**Plan modules:** [Extreme Chemical Reactor with a parallel hatch](../../plan/p20.md#cb_ecr)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-ct">
<div class="gt-head"><span class="gt-mname">Extreme Chemical Reactor</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Large Chemical Reactor (gtceu:large_chemical_reactor) - craft"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><b class="gt-q">craft</b></span><span class="gt-slot" title="1 IV circuit (gtceu:micro_processor_mainframe)"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_mainframe.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Mainframe</span><span class="gt-note">1 IV circuit</span></span><span class="gt-slot" title="2 IV emitters (gtceu:iv_emitter)"><img class="gt-ico" src="../../assets/icons/gtceu__iv_emitter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Emitter</span><span class="gt-note">2 IV emitters</span></span><span class="gt-slot" title="Naquadah pipes, plates and wire (gtceu:naquadah_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Ingot</span><span class="gt-note">Naquadah pipes, plates and wire</span></span><span class="gt-slot" title="5x5x5: inert PTFE casings, heat vents, PTFE pipes, black steel frames, 3 coils (gtceu:inert_machine_casing) - structure"><img class="gt-ico" src="../../assets/icons/gtceu__inert_machine_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Inert Machine Casing</span><span class="gt-note">5x5x5: inert PTFE casings, heat vents, PTFE pipes, black steel frames, 3 coils</span><b class="gt-q">structure</b></span><span class="gt-slot" title="Parallel hatch (IV..UV, never shared) (gtceu:iv_parallel_hatch) - parallels"><img class="gt-ico" src="../../assets/icons/gtceu__iv_parallel_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">IV Parallel Hatch</span><span class="gt-note">Parallel hatch (IV..UV, never shared)</span><b class="gt-q">parallels</b></span><span class="gt-slot" title="Cleanroom of at least 7x7x7 (cleanroom recipes only) (gtceu:cleanroom) - optional"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cleanroom</span><span class="gt-note">Cleanroom of at least 7x7x7 (cleanroom recipes only)</span><b class="gt-q">optional</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__extreme_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Large chemical recipes in parallel (gtceu:extreme_chemical_reactor)"><img class="gt-ico" src="../../assets/icons/gtceu__extreme_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Extreme Chemical Reactor</span><span class="gt-note">Large chemical recipes in parallel</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:extreme_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Extreme Chemical Reactor](#m-ct)

## How to build

1. Controller: an existing Large Chemical Reactor + IV circuit + 2 IV emitters + naquadah pipes, plates and wire. Build it once the naquadah line runs. — `gtceu:extreme_chemical_reactor`, `gtceu:large_chemical_reactor`
2. Structure: 5x5x5 of inert PTFE casings with heat vents, a PTFE pipe core, black steel frames and 3 coils; hatches and buses replace casings. — `gtceu:inert_machine_casing`, `gtceu:heat_vent`, `gtceu:ptfe_pipe_casing`
3. Add one parallel hatch (it cannot be shared with a neighbour). Batch the long LARGE\_CHEMICAL chains into it instead of building more LCRs. — `gtceu:iv_parallel_hatch`

## Tips

- ECR vs LCR (gtsrc GTMultiMachines): both run LARGE\_CHEMICAL recipes; only the ECR lists PARALLEL\_HATCH in its modifiers and allows a parallel hatch. The parallel hatch is optional, comes in IV to UV (Elite, Master, Ultimate, Super; GCYMMachines) and is never shared between machines.
- Controller (MetaTileEntityLoader): Large Chemical Reactor + 1 IV circuit + 2 IV emitters + 2 huge naquadah pipes + 2 naquadah double plates + naquadah quadruple wire. Naquadah comes from the Dimensional Destabiliser (LuV), so this is a LuV-time build even though the circuit is IV.
- Structure 5x5x5 (multis): 62 inert PTFE casings (10 minimum), 24 heat vents, 15 PTFE pipe casings, 8 black steel frames, 3 coils. Pack config: parallelLCR true and lcrCoilBenefits true, so better coils help; it is not perfect overclock.
- Cleanroom: the ECR pattern itself does not ask for one; recipes marked cleanroom do. A 5x5x5 machine does not fit the smallest cleanroom: plan a room of at least 7x7x7. Unverified: whether the whole ECR or only its controller must be inside.
- Use: naquadah separation (zpm\_naq\_products) is a LARGE\_CHEMICAL recipe, so an ECR with a parallel hatch batches it. Community report: one ECR outran a quad of furnaces on naquadria.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:extreme_chemical_reactor` | 1 |
| `gtceu:iv_parallel_hatch` | 1 |
| `gtceu:inert_machine_casing` | 62 |
| `gtceu:heat_vent` | 24 |
| `gtceu:ptfe_pipe_casing` | 15 |
| `gtceu:black_steel_frame` | 8 |

## Needs / Feeds

- **Needs:** [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../iv/iv_circuits.md), [IV components: tungsten steel parts, motor, piston, pump, conveyor, robot arm, emitter, sensor and hull on LV assemblers](../iv/iv_components.md)
- **Main source for:** `gtceu:extreme_chemical_reactor`
