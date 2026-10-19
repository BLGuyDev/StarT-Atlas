---
kind: chain
id: hv_cleanroom
order: 1020
data:
  t: |-
    Cleanroom (5×5×5): plascrete, filter casings, one energy hatch
  inf: true
  "n":
    - [pe, "6 Polyethylene plate", i, "gtceu:polyethylene_plate"]
    - [fr, Steel frame, i, "gtceu:steel_frame"]
    - [cn, Concrete 144 mB, f, "gtceu:concrete_bucket"]
    - [as, "MV Assembler · 48 EU/t", m, "gtceu:mv_assembler"]
    - [pc, "2 Plascrete", x, "gtceu:plascrete"]
    - [fc, "8 Filter Casing", i, "gtceu:filter_casing"]
    - [cr, Cleanroom, m, "gtceu:cleanroom"]
    - [ok, Clean air for engravers and assemblers, o, "gtceu:cleanroom_glass"]
  e:
    - [pe, as, "6"]
    - [fr, as]
    - [cn, as, "144 mB"]
    - [as, pc, "10 s"]
    - [pc, cr, "89"]
    - [fc, cr, "8"]
    - [cr, ok, "95 % clean"]
  tips:
    - Nothing up to MV needs a cleanroom, and not the first HV circuits either. It matters for phosphorus wafers (HV), SoCs and every EV circuit. The controller is HV (HV hull, 2 HV motors, 1 HV circuit), so MV machines alone cannot build it.
    - |-
      The first EV circuit (Microprocessor Supercomputer) is a 120 EU/t recipe: an MV circuit assembler inside the room makes it; the HV circuit assembler (its recipe needs EV circuits) only speeds it up. Nano processor assemblies already want 600 EU/t, an EV assembler.
    - |-
      Smallest size: 5×5×5, 89 plascrete / cleanroom glass / iron-door blocks, 8 filter casings around the controller in the ceiling, 1 energy hatch (up to 2), 1 maintenance hatch. Doors: up to 8, saves plascrete.
    - |-
      Cost: about 45 plascrete crafts = 45 steel frames + 270 polyethylene plates (about 39 B of polyethylene) + 6.5 B concrete. Plan the plastic first.
    - |-
      Power: 30 / 120 / 480 EU/t (LV / MV / HV hatch) while cleaning, then 3/16 of the hatch voltage (6 / 24 / 96 EU/t). Gain per 100 ticks of cycling: 5 / 8 / 11 %. The room must reach 95 %.
    - |-
      Machines inside cannot be generators, mufflers or other cleanrooms. EBFs have mufflers: keep them outside.
  b: [["gtceu:cleanroom", 1]]
  how:
    - i: ["gtceu:polyethylene_plate", "gtceu:steel_frame", "gtceu:mv_assembler"]
      t: |-
        MV Assembler, one per casing type: 1 steel frame + 6 polyethylene plates + 144 mB concrete → 2 plascrete in 10 s at 48 EU/t; the same with 144 mB glass gives 2 cleanroom glass. 45 crafts for the smallest room: plates are the cost (270).
    - i: ["gtceu:filter_casing", "gtceu:item_filter"]
      t: |-
        Filter casing: 3 iron bars + 3 item filters + 1 MV motor + 1 steel frame + 1 steel rotor, crafting table. You need 8.
    - i: ["gtceu:cleanroom", "gtceu:hv_electric_motor"]
      t: |-
        Controller: 3 item filters + 2 stainless rotors + 1 HV hull + 2 HV motors + 1 HV circuit. Place it in the middle of the top layer and put the 8 filter casings in a ring around it; everything else in the walls, floor and ceiling edges is plascrete or glass.
    - i: ["gtceu:hv_energy_input_hatch", "gtceu:maintenance_hatch"]
      t: |-
        Hatches go in the wall: at least one energy input hatch (any tier from LV; a bigger hatch only cleans faster), one maintenance hatch, and passthrough hatches for items if you want (at most a quarter of the floor area).
    - i: ["gtceu:mv_laser_engraver", "gtceu:mv_circuit_assembler"]
      t: Machines standing inside the room volume join it when the structure forms, so place the laser engravers, cutters and circuit assemblers for phosphorus wafers and SoCs inside first, then complete the walls. Mufflers and generators are refused, so EBFs stay outside.
    - i: ["gtceu:cleanroom"]
      t: |-
        Easy to miss: the controller shows the clean amount; a recipe with the cleanroom tag runs only at 95 % or more. If you cut power it drops again. Tall rooms take longer per cycle ((w × d)^0.8 × h ticks, minimum 100), so build wide, not tall.
---
# Cleanroom (5×5×5): plascrete, filter casings, one energy hatch

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `hv_cleanroom` · **Tags:** Infinite source

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Cleanroom (5x5x5)](../../plan/p8.md#cleanroom)

**Tips:** 6

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-as">
<div class="gt-head"><span class="gt-mname">MV Assembler · 48 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 Polyethylene plate (gtceu:polyethylene_plate) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__polyethylene_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Polyethylene Plate</span><span class="gt-note">6 Polyethylene plate</span><b class="gt-q">6</b></span><span class="gt-slot" title="Steel frame (gtceu:steel_frame)"><img class="gt-ico" src="../../assets/icons/gtceu__steel_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Steel Frame</span></span><span class="gt-slot gt-fluid" title="Concrete 144 mB (gtceu:concrete_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__concrete_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Concrete</span><span class="gt-note">Concrete 144 mB</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="2 Plascrete (gtceu:plascrete) - 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__plascrete.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plascrete</span><span class="gt-note">2 Plascrete</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-cr">
<div class="gt-head"><span class="gt-mname">Cleanroom</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Plascrete (gtceu:plascrete) - 89"><img class="gt-ico" src="../../assets/icons/gtceu__plascrete.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plascrete</span><span class="gt-note">2 Plascrete</span><b class="gt-q">89</b></span><span class="gt-slot" title="8 Filter Casing (gtceu:filter_casing) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__filter_casing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Filter Casing</span><span class="gt-note">8 Filter Casing</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Clean air for engravers and assemblers (gtceu:cleanroom_glass) - 95 % clean"><img class="gt-ico" src="../../assets/icons/gtceu__cleanroom_glass.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cleanroom Glass</span><span class="gt-note">Clean air for engravers and assemblers</span><b class="gt-q">95 % clean</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:cleanroom</code></div>
</div>
</div>

## Flow

- [MV Assembler · 48 EU/t](#m-as) → [Cleanroom](#m-cr)

## How to build

1. MV Assembler, one per casing type: 1 steel frame + 6 polyethylene plates + 144 mB concrete → 2 plascrete in 10 s at 48 EU/t; the same with 144 mB glass gives 2 cleanroom glass. 45 crafts for the smallest room: plates are the cost (270). — `gtceu:polyethylene_plate`, `gtceu:steel_frame`, `gtceu:mv_assembler`
2. Filter casing: 3 iron bars + 3 item filters + 1 MV motor + 1 steel frame + 1 steel rotor, crafting table. You need 8. — `gtceu:filter_casing`, `gtceu:item_filter`
3. Controller: 3 item filters + 2 stainless rotors + 1 HV hull + 2 HV motors + 1 HV circuit. Place it in the middle of the top layer and put the 8 filter casings in a ring around it; everything else in the walls, floor and ceiling edges is plascrete or glass. — `gtceu:cleanroom`, `gtceu:hv_electric_motor`
4. Hatches go in the wall: at least one energy input hatch (any tier from LV; a bigger hatch only cleans faster), one maintenance hatch, and passthrough hatches for items if you want (at most a quarter of the floor area). — `gtceu:hv_energy_input_hatch`, `gtceu:maintenance_hatch`
5. Machines standing inside the room volume join it when the structure forms, so place the laser engravers, cutters and circuit assemblers for phosphorus wafers and SoCs inside first, then complete the walls. Mufflers and generators are refused, so EBFs stay outside. — `gtceu:mv_laser_engraver`, `gtceu:mv_circuit_assembler`
6. Easy to miss: the controller shows the clean amount; a recipe with the cleanroom tag runs only at 95 % or more. If you cut power it drops again. Tall rooms take longer per cycle ((w × d)^0.8 × h ticks, minimum 100), so build wide, not tall. — `gtceu:cleanroom`

## Tips

- Nothing up to MV needs a cleanroom, and not the first HV circuits either. It matters for phosphorus wafers (HV), SoCs and every EV circuit. The controller is HV (HV hull, 2 HV motors, 1 HV circuit), so MV machines alone cannot build it.
- The first EV circuit (Microprocessor Supercomputer) is a 120 EU/t recipe: an MV circuit assembler inside the room makes it; the HV circuit assembler (its recipe needs EV circuits) only speeds it up. Nano processor assemblies already want 600 EU/t, an EV assembler.
- Smallest size: 5×5×5, 89 plascrete / cleanroom glass / iron-door blocks, 8 filter casings around the controller in the ceiling, 1 energy hatch (up to 2), 1 maintenance hatch. Doors: up to 8, saves plascrete.
- Cost: about 45 plascrete crafts = 45 steel frames + 270 polyethylene plates (about 39 B of polyethylene) + 6.5 B concrete. Plan the plastic first.
- Power: 30 / 120 / 480 EU/t (LV / MV / HV hatch) while cleaning, then 3/16 of the hatch voltage (6 / 24 / 96 EU/t). Gain per 100 ticks of cycling: 5 / 8 / 11 %. The room must reach 95 %.
- Machines inside cannot be generators, mufflers or other cleanrooms. EBFs have mufflers: keep them outside.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:cleanroom` | 1 |

## Needs / Feeds

- **Feeds:** [Combo: Assembler Matrix and pattern buffers (AE2 automation)](../combos/combo_ae2.md)
- **Main source for:** `gtceu:filter_casing`, `gtceu:plascrete`
