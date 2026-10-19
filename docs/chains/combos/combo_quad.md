---
kind: chain
id: combo_quad
order: 2320
data:
  t: "Combo: a quad of multiblocks sharing walls and hatches"
  inf: true
  "n":
    - [pw, "Two 2 A MV hatches = 1 A at HV", i, "gtceu:mv_energy_input_hatch"]
    - [eh, Shared energy hatch, x, "gtceu:hv_energy_input_hatch"]
    - [ib, "Shared input bus / hatch", x, "gtceu:hv_input_bus"]
    - [wl, "Shared walls: coils and casings count for each controller", x, "gtceu:cupronickel_coil_block"]
    - [mh, "Maintenance hatch: one per machine, never shared", x, "gtceu:auto_maintenance_hatch"]
    - [c1, EBF 1, m, "gtceu:electric_blast_furnace"]
    - [c2, EBF 2, m, "gtceu:electric_blast_furnace"]
    - [c3, EBF 3, m, "gtceu:electric_blast_furnace"]
    - [c4, EBF 4, m, "gtceu:electric_blast_furnace"]
    - [ob, Shared output bus, o, "gtceu:hv_output_bus"]
  e:
    - [pw, eh, "4 A at MV"]
    - [eh, c1, "1 A"]
    - [eh, c2, "1 A"]
    - [ib, c3]
    - [ib, c4]
    - [wl, c1]
    - [wl, c3]
    - [mh, c2, "1 each"]
    - [mh, c4, "1 each"]
    - [c1, ob]
    - [c2, ob]
    - [c3, ob]
    - [c4, ob]
  tips:
    - |-
      Sharing rule (gtceu jar, IMultiPart.canShared, true by default): a part can belong to several controllers. Never shared: maintenance hatches (also auto and cleaning ones), parallel hatches, laser hatches, rotor holders, tank valves, coke oven hatches, optical computation/data hatches and HPCA parts. Energy hatches, item buses and fluid hatches can be shared. Casings, coils, frames and glass have no owner: a block in two patterns counts toward both minimums.
    - |-
      Shared energy hatch: both machines drain the same buffer and each running recipe draws up to 1 A at the hatch voltage, so a hatch shared by two machines needs 2 A. Tier rule (EnergyContainerList): total amperage in a power of four lifts the tier, so two 2 A MV hatches = 4 A at MV = 1 A at HV (the guide already notes that assemblers are the exception).
    - |-
      Patterns that quad well (gtsrc GTMultiMachines): EBF 3x4x3, 16 coils, at least 9 heatproof casings, 1 muffler on top; Large Chemical Reactor 3x3x3, at least 10 inert PTFE casings, at most 1 coil, PTFE pipe in the centre; Pyrolyse Oven 3 wide x 4 deep, at least 6 ULV casings, 16 coils; Vacuum Freezer 3x3x3, 25 frostproof casings (14 minimum), controller needs 3 EV circuits. None needs air outside its own interior.
    - |-
      What a quad saves: in a 2x2 block each pair of neighbours shares one wall, e.g. a quad EBF skips 2 walls of 12 coils/casings against 4 loose EBFs; the exact count depends on the layout. Wall-sharing pyrolyse ovens or Large Gas Turbines saves casings and space, never the unshareable parts (turbine rotor holders).
    - |-
      LCR vs ECR: only the Extreme Chemical Reactor takes a parallel hatch; both use coil benefits (pack config lcrCoilBenefits: true), not perfect overclock.
    - |-
      Auto Maintenance Hatch = HV craft (4 HV circuits, 2 maintenance hatches, 2 HV robot arms, HV hull): worth it once you run four controllers.
    - |-
      Unverified: that the EBF muffler needs free air above it (standard GT, not checked in pack data). Left out on purpose: "octa ABS" (the Alloy Blast Smelter takes no parallel hatch; the term has no pack meaning) and shared fusion walls.
  b:
    - ["gtceu:electric_blast_furnace", 4]
    - ["gtceu:cupronickel_coil_block", 64]
    - ["gtceu:heatproof_machine_casing", 36]
    - ["gtceu:hv_energy_input_hatch", 2]
    - ["gtceu:hv_input_bus", 2]
    - ["gtceu:hv_output_bus", 2]
    - ["gtceu:auto_maintenance_hatch", 4]
    - ["gtceu:lv_muffler_hatch", 4]
  how:
    - i: ["gtceu:electric_blast_furnace", "gtceu:cupronickel_coil_block"]
      t: Lay four EBF footprints (3x3 each) in a 2x2 block so that each furnace touches two neighbours. The touching coil and casing columns are placed once and count for both furnaces. Controllers on the outside faces.
    - i: ["gtceu:hv_energy_input_hatch", "gtceu:mv_energy_input_hatch"]
      t: |-
        Energy: put one energy hatch where two furnaces touch so both see it; give it 2 A (or two 2 A MV hatches to reach HV recipes from MV power). A second shared hatch serves the other pair.
    - i: ["gtceu:hv_input_bus", "gtceu:hv_output_bus"]
      t: |-
        Buses on shared casings: one input bus per pair, one output bus that all four reach. Fluid hatches (nitrogen, oxygen) can also sit on a shared wall.
    - i: ["gtceu:auto_maintenance_hatch", "gtceu:lv_muffler_hatch"]
      t: |-
        Per furnace, never shared: one maintenance hatch (auto maintenance saves the hassle) and its muffler on its own top face.
---
# Combo: a quad of multiblocks sharing walls and hatches

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_quad` · **Tags:** Infinite source, Unverified

**Plan modules:** [Quad: four multiblocks sharing walls and hatches](../../plan/p20.md#cb_quad)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-c1">
<div class="gt-head"><span class="gt-mname">EBF 1</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shared energy hatch (gtceu:hv_energy_input_hatch) - 1 A"><img class="gt-ico" src="../../assets/icons/gtceu__hv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Energy Input Hatch</span><span class="gt-note">Shared energy hatch</span><b class="gt-q">1 A</b></span><span class="gt-slot" title="Shared walls: coils and casings count for each controller (gtceu:cupronickel_coil_block)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Coil Block</span><span class="gt-note">Shared walls: coils and casings count for each controller</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Shared output bus (gtceu:hv_output_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Output Bus</span><span class="gt-note">Shared output bus</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-c2">
<div class="gt-head"><span class="gt-mname">EBF 2</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shared energy hatch (gtceu:hv_energy_input_hatch) - 1 A"><img class="gt-ico" src="../../assets/icons/gtceu__hv_energy_input_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Energy Input Hatch</span><span class="gt-note">Shared energy hatch</span><b class="gt-q">1 A</b></span><span class="gt-slot" title="Maintenance hatch: one per machine, never shared (gtceu:auto_maintenance_hatch) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__auto_maintenance_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Auto Maintenance Hatch</span><span class="gt-note">Maintenance hatch: one per machine, never shared</span><b class="gt-q">1 each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Shared output bus (gtceu:hv_output_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Output Bus</span><span class="gt-note">Shared output bus</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-c3">
<div class="gt-head"><span class="gt-mname">EBF 3</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shared input bus / hatch (gtceu:hv_input_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_input_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Input Bus</span><span class="gt-note">Shared input bus / hatch</span></span><span class="gt-slot" title="Shared walls: coils and casings count for each controller (gtceu:cupronickel_coil_block)"><img class="gt-ico" src="../../assets/icons/gtceu__cupronickel_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cupronickel Coil Block</span><span class="gt-note">Shared walls: coils and casings count for each controller</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Shared output bus (gtceu:hv_output_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Output Bus</span><span class="gt-note">Shared output bus</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-c4">
<div class="gt-head"><span class="gt-mname">EBF 4</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shared input bus / hatch (gtceu:hv_input_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_input_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Input Bus</span><span class="gt-note">Shared input bus / hatch</span></span><span class="gt-slot" title="Maintenance hatch: one per machine, never shared (gtceu:auto_maintenance_hatch) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__auto_maintenance_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Auto Maintenance Hatch</span><span class="gt-note">Maintenance hatch: one per machine, never shared</span><b class="gt-q">1 each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Shared output bus (gtceu:hv_output_bus)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_output_bus.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Output Bus</span><span class="gt-note">Shared output bus</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [EBF 1](#m-c1)
- [EBF 2](#m-c2)
- [EBF 3](#m-c3)
- [EBF 4](#m-c4)

### Direct steps

- Two 2 A MV hatches = 1 A at HV → Shared energy hatch (4 A at MV)

## How to build

1. Lay four EBF footprints (3x3 each) in a 2x2 block so that each furnace touches two neighbours. The touching coil and casing columns are placed once and count for both furnaces. Controllers on the outside faces. — `gtceu:electric_blast_furnace`, `gtceu:cupronickel_coil_block`
2. Energy: put one energy hatch where two furnaces touch so both see it; give it 2 A (or two 2 A MV hatches to reach HV recipes from MV power). A second shared hatch serves the other pair. — `gtceu:hv_energy_input_hatch`, `gtceu:mv_energy_input_hatch`
3. Buses on shared casings: one input bus per pair, one output bus that all four reach. Fluid hatches (nitrogen, oxygen) can also sit on a shared wall. — `gtceu:hv_input_bus`, `gtceu:hv_output_bus`
4. Per furnace, never shared: one maintenance hatch (auto maintenance saves the hassle) and its muffler on its own top face. — `gtceu:auto_maintenance_hatch`, `gtceu:lv_muffler_hatch`

## Tips

- Sharing rule (gtceu jar, IMultiPart.canShared, true by default): a part can belong to several controllers. Never shared: maintenance hatches (also auto and cleaning ones), parallel hatches, laser hatches, rotor holders, tank valves, coke oven hatches, optical computation/data hatches and HPCA parts. Energy hatches, item buses and fluid hatches can be shared. Casings, coils, frames and glass have no owner: a block in two patterns counts toward both minimums.
- Shared energy hatch: both machines drain the same buffer and each running recipe draws up to 1 A at the hatch voltage, so a hatch shared by two machines needs 2 A. Tier rule (EnergyContainerList): total amperage in a power of four lifts the tier, so two 2 A MV hatches = 4 A at MV = 1 A at HV (the guide already notes that assemblers are the exception).
- Patterns that quad well (gtsrc GTMultiMachines): EBF 3x4x3, 16 coils, at least 9 heatproof casings, 1 muffler on top; Large Chemical Reactor 3x3x3, at least 10 inert PTFE casings, at most 1 coil, PTFE pipe in the centre; Pyrolyse Oven 3 wide x 4 deep, at least 6 ULV casings, 16 coils; Vacuum Freezer 3x3x3, 25 frostproof casings (14 minimum), controller needs 3 EV circuits. None needs air outside its own interior.
- What a quad saves: in a 2x2 block each pair of neighbours shares one wall, e.g. a quad EBF skips 2 walls of 12 coils/casings against 4 loose EBFs; the exact count depends on the layout. Wall-sharing pyrolyse ovens or Large Gas Turbines saves casings and space, never the unshareable parts (turbine rotor holders).
- LCR vs ECR: only the Extreme Chemical Reactor takes a parallel hatch; both use coil benefits (pack config lcrCoilBenefits: true), not perfect overclock.
- Auto Maintenance Hatch = HV craft (4 HV circuits, 2 maintenance hatches, 2 HV robot arms, HV hull): worth it once you run four controllers.
- **Unverified** that the EBF muffler needs free air above it (standard GT, not checked in pack data). Left out on purpose: "octa ABS" (the Alloy Blast Smelter takes no parallel hatch; the term has no pack meaning) and shared fusion walls.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:electric_blast_furnace` | 4 |
| `gtceu:cupronickel_coil_block` | 64 |
| `gtceu:heatproof_machine_casing` | 36 |
| `gtceu:hv_energy_input_hatch` | 2 |
| `gtceu:hv_input_bus` | 2 |
| `gtceu:hv_output_bus` | 2 |
| `gtceu:auto_maintenance_hatch` | 4 |
| `gtceu:lv_muffler_hatch` | 4 |
