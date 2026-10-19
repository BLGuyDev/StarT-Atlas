---
kind: chain
id: combo_cubes
order: 2330
data:
  t: |-
    Combo: Perfect-OC cubes (Multiblock Upgrade Kit) built as a quad
  inf: true
  "n":
    - [lg, Thermal lumium glass, i, "thermal:lumium_glass"]
    - [ec, "1 EV circuit", i, "gtceu:micro_processor_computer"]
    - [sg, "2 double signalum plates", i, "gtceu:double_signalum_plate"]
    - [cf, "12 cobalt foil", i, "gtceu:cobalt_foil"]
    - [as, "HV Assembler · 800 ticks", m, "gtceu:hv_assembler"]
    - [kt, Multiblock Upgrade Kit, x, "kubejs:multiblock_upgrade_kit"]
    - [hm, "HV machine (17 types, e.g. HV centrifuge)", i, "gtceu:hv_centrifuge"]
    - [cn, "Canner 120 EU/t or Create item application", m, "gtceu:mv_canner"]
    - [ct, "Cube controller (t_large_<machine>)", x, "gtceu:t_large_centrifuge"]
    - [eh, Exactly one 2 A energy hatch, i, "gtceu:hv_energy_input_hatch"]
    - [mh, Exactly one maintenance hatch, i, "gtceu:maintenance_hatch"]
    - [out, "3x3x3 cube: perfect overclock + batch, no parallel", o, "gtceu:t_large_centrifuge"]
  e:
    - [lg, as]
    - [ec, as]
    - [sg, as]
    - [cf, as]
    - [as, kt]
    - [kt, cn]
    - [hm, cn]
    - [cn, ct]
    - [ct, out]
    - [eh, out, shared by 2 cubes]
    - [mh, out, per cube]
  tips:
    - |-
      Kit (additions/machines_and_parts/intermediate_multis.js): HV assembler, 800 ticks: 1 thermal lumium glass + 1 EV circuit + 2 double signalum plates + 12 cobalt foil. It needs an EV circuit, so the cubes are an end-of-HV build, not a plain HV one.
    - |-
      Use: gtceu:hv_<machine> + kit → controller gtceu:t_large_<machine> in a Canner (120 EU/t, 20 ticks) or by Create item application. 17 machines: bender, centrifuge, electrolyzer, extruder, forming press, lathe, mixer, ore washer, sifter, thermal centrifuge, wiremill, macerator, autoclave, pulverizer, arc furnace, electromagnetic separator, rock crusher (the last gives large_rock_crusher).
    - |-
      Structure (startup_scripts .../intermediate_multiblocks/large_cubes.js): hollow 3x3x3 cube, its own casing at least 5; the other cells take casings, item or fluid buses/hatches, exactly 1 maintenance hatch and exactly 1 2 A energy hatch (a 4 A hatch does not count). Recipe modifiers: perfect overclock + batch mode, no parallel at all. The cell behind the controller (centre of the middle layer) must be air.
    - |-
      Casings (lines/intermediate_multis.js alloys, made in mixers): ore washer hydronalium, thermal centrifuge silicon bronze, macerator blue steel, sifter zamak, mixer kovar, arc furnace black steel, rock crusher red steel.
    - |-
      Quad of cubes: four cubes side by side share casings and the item/fluid/energy hatches (one 2 A hatch powers two cubes at 1 A each); maintenance is never shared. The "7 casings per quad cube" in community screenshots is that layout; the pack minimum is 5 per cube, counted per controller.
    - |-
      Unverified: ULV (wrought iron) buses as cheap filler: any bus tier fits the pattern, but a ULV bus recipe was not found in the fork; the per-tier chance boost of the hatch.
  b:
    - ["kubejs:multiblock_upgrade_kit", 4]
    - ["gtceu:hv_energy_input_hatch", 2]
    - ["gtceu:maintenance_hatch", 4]
    - ["gtceu:hv_input_bus", 2]
    - ["gtceu:hv_output_bus", 2]
  how:
    - i: ["gtceu:hv_assembler", "kubejs:multiblock_upgrade_kit"]
      t: |-
        Kits: HV assembler with lumium glass, an EV circuit, 2 double signalum plates and 12 cobalt foil, 40 s each. One kit per cube.
    - i: ["gtceu:hv_centrifuge", "kubejs:multiblock_upgrade_kit"]
      t: |-
        Upgrade: put the HV machine and the kit in a canner (or apply the kit with Create item application): the HV machine becomes the cube controller.
    - i: ["gtceu:t_large_centrifuge", "gtceu:maintenance_hatch"]
      t: |-
        Build each 3x3x3 cube around its controller: at least 5 of its casings, one maintenance hatch, one 2 A energy hatch, buses where you like, and leave the block right behind the controller empty.
    - i: ["gtceu:hv_energy_input_hatch", "gtceu:hv_input_bus"]
      t: |-
        Quad: put four cubes in a 2x2 block; the walls where two cubes touch carry the shared 2 A energy hatch and the shared buses. Typical ore line: washer, thermal centrifuge, macerator, sifter.
---
# Combo: Perfect-OC cubes (Multiblock Upgrade Kit) built as a quad

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_cubes` · **Tags:** Infinite source, Unverified

**Plan modules:** [Perfect-OC cubes from the Multiblock Upgrade Kit](../../plan/p20.md#cb_cubes)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-as">
<div class="gt-head"><span class="gt-mname">HV Assembler · 800 ticks</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Thermal lumium glass (thermal:lumium_glass)"><img class="gt-ico" src="../../assets/icons/thermal__lumium_glass.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lumium Glass</span><span class="gt-note">Thermal lumium glass</span></span><span class="gt-slot" title="1 EV circuit (gtceu:micro_processor_computer)"><img class="gt-ico" src="../../assets/icons/gtceu__micro_processor_computer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Micro Processor Computer</span><span class="gt-note">1 EV circuit</span></span><span class="gt-slot" title="2 double signalum plates (gtceu:double_signalum_plate)"><img class="gt-ico" src="../../assets/icons/gtceu__double_signalum_plate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Double Signalum Plate</span><span class="gt-note">2 double signalum plates</span></span><span class="gt-slot" title="12 cobalt foil (gtceu:cobalt_foil)"><img class="gt-ico" src="../../assets/icons/gtceu__cobalt_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobalt Foil</span><span class="gt-note">12 cobalt foil</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Multiblock Upgrade Kit (kubejs:multiblock_upgrade_kit)"><img class="gt-ico" src="../../assets/icons/kubejs__multiblock_upgrade_kit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multiblock Upgrade Kit</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_assembler</code></div>
</div>
<div class="gt-panel t-mv" id="m-cn">
<div class="gt-head"><span class="gt-mname">Canner 120 EU/t or Create item application</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Multiblock Upgrade Kit (kubejs:multiblock_upgrade_kit)"><img class="gt-ico" src="../../assets/icons/kubejs__multiblock_upgrade_kit.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Multiblock Upgrade Kit</span></span><span class="gt-slot" title="HV machine (17 types, e.g. HV centrifuge) (gtceu:hv_centrifuge)"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">HV Centrifuge</span><span class="gt-note">HV machine (17 types, e.g. HV centrifuge)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_canner.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Cube controller (t_large_&lt;machine&gt;) (gtceu:t_large_centrifuge)"><img class="gt-ico" src="../../assets/icons/gtceu__t_large_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">T Large Centrifuge</span><span class="gt-note">Cube controller (t_large_&lt;machine&gt;)</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_canner</code></div>
</div>
</div>

## Flow

- [HV Assembler · 800 ticks](#m-as) → [Canner 120 EU/t or Create item application](#m-cn)

### Direct steps

- Cube controller (t\_large\_&lt;machine&gt;) → 3x3x3 cube: perfect overclock + batch, no parallel
- Exactly one 2 A energy hatch → 3x3x3 cube: perfect overclock + batch, no parallel (shared by 2 cubes)
- Exactly one maintenance hatch → 3x3x3 cube: perfect overclock + batch, no parallel (per cube)

## How to build

1. Kits: HV assembler with lumium glass, an EV circuit, 2 double signalum plates and 12 cobalt foil, 40 s each. One kit per cube. — `gtceu:hv_assembler`, `kubejs:multiblock_upgrade_kit`
2. Upgrade: put the HV machine and the kit in a canner (or apply the kit with Create item application): the HV machine becomes the cube controller. — `gtceu:hv_centrifuge`, `kubejs:multiblock_upgrade_kit`
3. Build each 3x3x3 cube around its controller: at least 5 of its casings, one maintenance hatch, one 2 A energy hatch, buses where you like, and leave the block right behind the controller empty. — `gtceu:t_large_centrifuge`, `gtceu:maintenance_hatch`
4. Quad: put four cubes in a 2x2 block; the walls where two cubes touch carry the shared 2 A energy hatch and the shared buses. Typical ore line: washer, thermal centrifuge, macerator, sifter. — `gtceu:hv_energy_input_hatch`, `gtceu:hv_input_bus`

## Tips

- Kit (additions/machines\_and\_parts/intermediate\_multis.js): HV assembler, 800 ticks: 1 thermal lumium glass + 1 EV circuit + 2 double signalum plates + 12 cobalt foil. It needs an EV circuit, so the cubes are an end-of-HV build, not a plain HV one.
- Use: gtceu:hv\_&lt;machine&gt; + kit → controller gtceu:t\_large\_&lt;machine&gt; in a Canner (120 EU/t, 20 ticks) or by Create item application. 17 machines: bender, centrifuge, electrolyzer, extruder, forming press, lathe, mixer, ore washer, sifter, thermal centrifuge, wiremill, macerator, autoclave, pulverizer, arc furnace, electromagnetic separator, rock crusher (the last gives large\_rock\_crusher).
- Structure (startup\_scripts .../intermediate\_multiblocks/large\_cubes.js): hollow 3x3x3 cube, its own casing at least 5; the other cells take casings, item or fluid buses/hatches, exactly 1 maintenance hatch and exactly 1 2 A energy hatch (a 4 A hatch does not count). Recipe modifiers: perfect overclock + batch mode, no parallel at all. The cell behind the controller (centre of the middle layer) must be air.
- Casings (lines/intermediate\_multis.js alloys, made in mixers): ore washer hydronalium, thermal centrifuge silicon bronze, macerator blue steel, sifter zamak, mixer kovar, arc furnace black steel, rock crusher red steel.
- Quad of cubes: four cubes side by side share casings and the item/fluid/energy hatches (one 2 A hatch powers two cubes at 1 A each); maintenance is never shared. The "7 casings per quad cube" in community screenshots is that layout; the pack minimum is 5 per cube, counted per controller.
- **Unverified** ULV (wrought iron) buses as cheap filler: any bus tier fits the pattern, but a ULV bus recipe was not found in the fork; the per-tier chance boost of the hatch.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `kubejs:multiblock_upgrade_kit` | 4 |
| `gtceu:hv_energy_input_hatch` | 2 |
| `gtceu:maintenance_hatch` | 4 |
| `gtceu:hv_input_bus` | 2 |
| `gtceu:hv_output_bus` | 2 |

## Needs / Feeds

- **Needs:** [IV circuit: Microprocessor Mainframe (microprocessor → assembly → supercomputer → mainframe, silicon wafers only)](../iv/iv_circuits.md)
- **Main source for:** `kubejs:multiblock_upgrade_kit`
