---
kind: chain
id: luv_power
order: 1300
data:
  t: |-
    Power Substation and Active Transformer: palladium substation casing, lapotron crystals, LuV circuits, UHPIC chips
  inf: true
  "n":
    - [lc, "4 Lapotron crystal", i, "gtceu:lapotron_crystal"]
    - - pc
      - "2 Power integrated circuit · 2 LuV circuit"
      - g
      - functionalstorage:oak_1
      - [[Power IC, "gtceu:power_integrated_circuit"], [Nanoprocessor Mainframe, "gtceu:nano_processor_mainframe"]]
    - [cs, Palladium substation casing, x, "gtceu:palladium_substation"]
    - [ps, "Power Substation (crafting table)", o, "gtceu:power_substation"]
    - [gl, "41 laminated glass", i, "gtceu:laminated_glass"]
    - [ba, "Capacitor blocks, 9 per layer", x, "gtceu:palladium_substation"]
    - - tr
      - LuV Power Transformer · 2 LuV circuit · 8 ITBTC single wire · 2 UHPIC chip · 1 B PCB coolant
      - g
      - functionalstorage:oak_1
      - [[UHPIC chip, "gtceu:uhpic_chip"], [PCB coolant, "gtceu:pcb_coolant_bucket"]]
    - [a1, "Assembler on a 4A hatch · 15 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [at, Active Transformer, o, "gtceu:active_transformer"]
  e:
    - [lc, ps, "4"]
    - [pc, ps, "2 + 2"]
    - [cs, ps, "1"]
    - [gl, ps]
    - [ba, ps, "9 per layer"]
    - [tr, a1, "1"]
    - [a1, at, "1 / 15 s"]
  tips:
    - |-
      Power Substation (MetaTileEntityLoader): crafting table LPL / CBC / LPL: 4 lapotron crystals, 2 power integrated circuits, 2 LuV circuits, 1 palladium substation casing (Secure Pallaridium Machine Casing). Casing: 6 palladium plates + 1 iridium frame, crafting table, 2 per craft. Structure: 5 x 5 footprint, 41 laminated glass and 40 + 9 palladium casings for the smallest size (multis card), a 3 x 3 block of capacitor blocks per layer (1 to 18 layers), energy and dynamo hatches in the casing ring. The structure does not store power: the capacitor blocks do (quest).
    - |-
      Active Transformer (ComputerRecipes): assembler 300 ticks at 30 720 EU/t: 1 LuV Power Transformer + 2 LuV circuits + 8 ITBTC single wire + 2 UHPIC chips + 1 B PCB coolant. Structure: 25 high power casings (12 hatch spots) and 1 superconducting coil, the pack coil (see luv_fusion: enriched naquadah frame + trinium) in the middle, laser cables between. So it also waits for the naquadah by-product line and the UHPIC chips.
    - |-
      Iridium and palladium: each substation casing is 1 iridium frame (2 iridium ingots) + 6 palladium plates for 2 casings, 49 casings = 25 crafts = 50 iridium + 150 palladium, again the platinum group line. A large substation is a big iridium sink; build the minimum (3 layers) first and upgrade capacitors later (the quest says it can be upgraded to UHV).
    - |-
      Capacitor blocks: the PSS battery items (empty capacitor + lapotron/lapotronic cells); Unverified in this pack: the recipe and the capacity per tier, read EMI for the block list.
    - |-
      LuV rotor holder (the pack replaces the GT recipe, kjs systems/fusion/plasma_turbines.js): assembler, LuV hull + 4 HSS-S gears + 1 LuV motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 RPP ring + 288 mB PTFE, circuit 3, LuV power. It needs the LuV motor from the Assembly Line and the HSS-S metals first. Quest rule: each holder tier doubles power and parallels for 1.8x fuel, on top of a 10 % efficiency bonus. Dragonsteel rotors are not a LuV item: dragonsteel is a ZPM superconductor (blast 7100 K, ZPM hatch, 1800 ticks; dust = 4 tungsten + 8 magnesium diboride + 2 cadmium in a mixer, 900 ticks, 16 000 EU/t) and needs naquadah coils (7200 K), so it only fits a LuV holder once you are in ZPM.
    - |-
      Why at LuV: the 100 000 EU/t Assembly Line recipes (ZPM-gated), the fusion start energy of 150 MEU and the 4A hatches all want a buffer. Do not build the substation before the LuV hatches exist, it only accepts hatch voltage you can supply.
    - |-
      Sub-steps people skip: (1) the controller is a crafting recipe, the casing is a separate craft; (2) the substation needs at least 1 energy-in and 1 energy-out hatch (or laser); (3) UHPIC chips are the rare input of the transformer, not the glass; (4) laser cables need osmiridium foil and PTFE (cleanroom assembler).
    - |-
      Unverified: the capacitor block recipes, the exact casing totals for your layer count (use the multis card BOM), the Active Transformer laser-cable layout.
  b:
    - ["gtceu:power_substation", 1]
    - ["gtceu:active_transformer", 1]
    - ["gtceu:luv_energy_input_hatch", 1]
    - ["gtceu:large_assembler", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 2]
  how:
    - i: ["gtceu:palladium_substation", "gtceu:iridium_frame", "gtceu:palladium_plate"]
      t: |-
        Casings: crafting table, 6 palladium plates + 1 iridium frame (hammer and wrench in the grid) → 2 casings. Make 49 for the smallest substation: palladium and iridium drawers first.
    - i: ["gtceu:power_substation", "gtceu:lapotron_crystal", "gtceu:power_integrated_circuit"]
      t: |-
        Controller: crafting table LPL / CBC / LPL with 4 lapotron crystals, 2 power integrated circuits, 2 LuV circuits and a casing. Lapotron crystals come from the IV power line (battery chain).
    - i: ["gtceu:laminated_glass", "gtceu:palladium_substation"]
      t: |-
        Build: 5 x 5 base ring of casings with 3 x 3 capacitors per layer and glass walls: 1 to 18 battery layers, start with 1. Energy-in hatch top, dynamo/energy-out hatch beside it, maintenance.
    - i: ["gtceu:large_assembler", "gtceu:uhpic_chip", "gtceu:active_transformer"]
      t: |-
        Active Transformer: LuV power transformer + 2 LuV circuits + 8 ITBTC single wire + 2 UHPIC chips + 1 B PCB coolant, 15 s at 30 720 EU/t (Large Assembler on a 4A hatch). Then the 25 high power casings and the superconducting coil.
    - i: ["gtceu:luv_energy_input_hatch", "gtceu:power_substation"]
      t: |-
        Easy to miss: hatches of the same tier only; use the luv_hatches chain’s LuV hatch for the substation input and an IV dynamo output for the network.
---
# Power Substation and Active Transformer: palladium substation casing, lapotron crystals, LuV circuits, UHPIC chips

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `luv_power` · **Tags:** Infinite source, Unverified

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Assembly Line, LuV hull, hatch and components](../../plan/p11.md#luvmach)

**Tips:** 8, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Assembler on a 4A hatch · 15 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="LuV Power Transformer · 2 LuV circuit · 8 ITBTC single wire · 2 UHPIC chip · 1 B PCB coolant (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">LuV Power Transformer · 2 LuV circuit · 8 ITBTC single wire · 2 UHPIC chip · 1 B PCB coolant</span><span class="gt-sub"><span>UHPIC chip</span><span>PCB coolant</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Active Transformer (gtceu:active_transformer) - 1 / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__active_transformer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Active Transformer</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
</div>

## Flow

- [Assembler on a 4A hatch · 15 s · 30 720 EU/t](#m-a1)

### Direct steps

- 4 Lapotron crystal → Power Substation (crafting table) (4)
- 2 Power integrated circuit · 2 LuV circuit → Power Substation (crafting table) (2 + 2)
- Palladium substation casing → Power Substation (crafting table) (1)
- 41 laminated glass → Power Substation (crafting table)
- Capacitor blocks, 9 per layer → Power Substation (crafting table) (9 per layer)

## How to build

1. Casings: crafting table, 6 palladium plates + 1 iridium frame (hammer and wrench in the grid) → 2 casings. Make 49 for the smallest substation: palladium and iridium drawers first. — `gtceu:palladium_substation`, `gtceu:iridium_frame`, `gtceu:palladium_plate`
2. Controller: crafting table LPL / CBC / LPL with 4 lapotron crystals, 2 power integrated circuits, 2 LuV circuits and a casing. Lapotron crystals come from the IV power line (battery chain). — `gtceu:power_substation`, `gtceu:lapotron_crystal`, `gtceu:power_integrated_circuit`
3. Build: 5 x 5 base ring of casings with 3 x 3 capacitors per layer and glass walls: 1 to 18 battery layers, start with 1. Energy-in hatch top, dynamo/energy-out hatch beside it, maintenance. — `gtceu:laminated_glass`, `gtceu:palladium_substation`
4. Active Transformer: LuV power transformer + 2 LuV circuits + 8 ITBTC single wire + 2 UHPIC chips + 1 B PCB coolant, 15 s at 30 720 EU/t (Large Assembler on a 4A hatch). Then the 25 high power casings and the superconducting coil. — `gtceu:large_assembler`, `gtceu:uhpic_chip`, `gtceu:active_transformer`
5. Easy to miss: hatches of the same tier only; use the luv\_hatches chain’s LuV hatch for the substation input and an IV dynamo output for the network. — `gtceu:luv_energy_input_hatch`, `gtceu:power_substation`

## Tips

- Power Substation (MetaTileEntityLoader): crafting table LPL / CBC / LPL: 4 lapotron crystals, 2 power integrated circuits, 2 LuV circuits, 1 palladium substation casing (Secure Pallaridium Machine Casing). Casing: 6 palladium plates + 1 iridium frame, crafting table, 2 per craft. Structure: 5 x 5 footprint, 41 laminated glass and 40 + 9 palladium casings for the smallest size (multis card), a 3 x 3 block of capacitor blocks per layer (1 to 18 layers), energy and dynamo hatches in the casing ring. The structure does not store power: the capacitor blocks do (quest).
- Active Transformer (ComputerRecipes): assembler 300 ticks at 30 720 EU/t: 1 LuV Power Transformer + 2 LuV circuits + 8 ITBTC single wire + 2 UHPIC chips + 1 B PCB coolant. Structure: 25 high power casings (12 hatch spots) and 1 superconducting coil, the pack coil (see luv\_fusion: enriched naquadah frame + trinium) in the middle, laser cables between. So it also waits for the naquadah by-product line and the UHPIC chips.
- Iridium and palladium: each substation casing is 1 iridium frame (2 iridium ingots) + 6 palladium plates for 2 casings, 49 casings = 25 crafts = 50 iridium + 150 palladium, again the platinum group line. A large substation is a big iridium sink; build the minimum (3 layers) first and upgrade capacitors later (the quest says it can be upgraded to UHV).
- Capacitor blocks: the PSS battery items (empty capacitor + lapotron/lapotronic cells); Unverified in this pack: the recipe and the capacity per tier, read EMI for the block list.
- LuV rotor holder (the pack replaces the GT recipe, kjs systems/fusion/plasma\_turbines.js): assembler, LuV hull + 4 HSS-S gears + 1 LuV motor + 4 small rhodium plated palladium gears + 6 HSS-S rounds + 1 RPP ring + 288 mB PTFE, circuit 3, LuV power. It needs the LuV motor from the Assembly Line and the HSS-S metals first. Quest rule: each holder tier doubles power and parallels for 1.8x fuel, on top of a 10 % efficiency bonus. Dragonsteel rotors are not a LuV item: dragonsteel is a ZPM superconductor (blast 7100 K, ZPM hatch, 1800 ticks; dust = 4 tungsten + 8 magnesium diboride + 2 cadmium in a mixer, 900 ticks, 16 000 EU/t) and needs naquadah coils (7200 K), so it only fits a LuV holder once you are in ZPM.
- Why at LuV: the 100 000 EU/t Assembly Line recipes (ZPM-gated), the fusion start energy of 150 MEU and the 4A hatches all want a buffer. Do not build the substation before the LuV hatches exist, it only accepts hatch voltage you can supply.
- Sub-steps people skip: (1) the controller is a crafting recipe, the casing is a separate craft; (2) the substation needs at least 1 energy-in and 1 energy-out hatch (or laser); (3) UHPIC chips are the rare input of the transformer, not the glass; (4) laser cables need osmiridium foil and PTFE (cleanroom assembler).
- **Unverified** the capacitor block recipes, the exact casing totals for your layer count (use the multis card BOM), the Active Transformer laser-cable layout.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:power_substation` | 1 |
| `gtceu:active_transformer` | 1 |
| `gtceu:luv_energy_input_hatch` | 1 |
| `gtceu:large_assembler` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 2 |

## Needs / Feeds

- **Main source for:** `gtceu:power_substation`, `gtceu:active_transformer`
