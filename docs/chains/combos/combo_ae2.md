---
kind: chain
id: combo_ae2
order: 2340
data:
  t: "Combo: Assembler Matrix and pattern buffers (AE2 automation)"
  inf: true
  "n":
    - [pc, Plascrete or cleanroom glass, i, "gtceu:plascrete"]
    - [fc, "Fluix smart cables (4) or dense (2)", i, "ae2:fluix_smart_cable"]
    - [ru, "2 to 4 ruthenium plates", i, "gtceu:ruthenium_dust"]
    - [fs, "Fluix steel · 576 mB", f, "gtceu:fluix_steel_dust"]
    - [ea, "EV Assembler · 1 920 EU/t · 20 s", m, "gtceu:ev_assembler"]
    - [fr, "Matrix frame / wall / glass", x, "expatternprovider:assembler_matrix_frame"]
    - [pp, "2 ex pattern providers", i, "expatternprovider:ex_pattern_provider"]
    - [ma, "or 2 ex molecular assemblers / 2 speed cards", i, "expatternprovider:ex_molecular_assembler"]
    - [nc, "Netherite certus skystone alloy · 576 mB", f, "gtceu:netherite_certus_quartz_skystone_alloy_bucket"]
    - [eb, EV Assembler, m, "gtceu:ev_assembler"]
    - [out, "Assembler Matrix: pattern / crafter / speed", o, "expatternprovider:assembler_matrix_frame"]
    - [pb, "ME Pattern Buffer + proxies", x, "gtceu:me_pattern_buffer"]
    - [sh, "ME stocking input bus / hatch", x, "gtceu:me_stocking_input_bus"]
    - [al, "GT multiblocks / Assembly Line", o, "gtceu:assembly_line"]
  e:
    - [pc, ea]
    - [fc, ea]
    - [ru, ea]
    - [fs, ea]
    - [ea, fr]
    - [fr, eb, "1 wall"]
    - [pp, eb]
    - [ma, eb]
    - [nc, eb]
    - [eb, out]
    - [pb, al, shared patterns]
    - [sh, al, ordered slots]
  tips:
    - |-
      Assembler Matrix (pack modifications/ae2/machinery.js): every piece is an EV assembler recipe, 400 ticks at 1 920 EU/t. Frame = plascrete + 2 fluix smart dense cables + 4 ruthenium plates + 576 mB fluix steel; wall = plascrete + 4 fluix smart cables + 2 ruthenium plates + 576 mB fluix steel; glass = cleanroom glass + 4 fluix smart cables + 2 ruthenium plates + 576 mB fluix steel; pattern / crafter / speed = 1 wall + 2 ex pattern providers / 2 ex molecular assemblers / 2 speed cards + 576 mB netherite certus quartz skystone alloy.
    - |-
      Gates: ruthenium from the platinum group line (EV chemical reactor step), plascrete and cleanroom glass from the cleanroom line. The netherite certus skystone alloy needs netherite (EBF 3 300 K with argon) and blasts at 4 000 K at IV voltage, so the pattern, crafter and speed blocks are late EV to IV.
    - |-
      Ex pattern provider (machinery.js, EV assembler): MEGA pattern provider + 4 calculation processors + 1 EV circuit + 4 double gold skystone alloy plates + 576 mB sky steel. ExpandedAE 1.4.2.e is in the pack.
    - |-
      Pattern buffer combo (a community nickname, not an item): gtceu:me_pattern_buffer stores AE2 patterns for GT multiblocks; gtceu:me_pattern_buffer_proxy links more machines (data stick) to share the patterns of that one buffer. ME stocking input buses/hatches and AE2 toggle buses also exist. Unverified: how many machines one buffer can feed.
    - |-
      Smart blocking: plain AE2 15.5.4 only has simple Blocking Mode; ExpandedAE adds Default / Full / Smart ("allows same pattern to be pushed"). Community advice: Smart blocking misbehaves with parallels of the same item.
    - |-
      Assembly Lines on stocking buses: pack config orderedAssemblyLineItems: true and orderedAssemblyLineFluids: false (config/gtceu.yaml), so items must reach the buses in recipe order; players force each item into its own slot by renaming stacks. Unverified: the renaming mechanism itself.
  b:
    - ["expatternprovider:assembler_matrix_frame", 1]
    - ["gtceu:ev_assembler", 1]
    - ["gtceu:me_pattern_buffer", 1]
    - ["gtceu:me_pattern_buffer_proxy", 4]
  how:
    - i: ["gtceu:ev_assembler", "expatternprovider:assembler_matrix_frame"]
      t: |-
        Frames, walls and glass first: EV assembler, plascrete (or cleanroom glass) + fluix smart cables + ruthenium plates + 576 mB fluix steel, 20 s each. The matrix is a hollow structure of these; the functional blocks sit in its walls.
    - i: ["expatternprovider:ex_pattern_provider", "expatternprovider:ex_molecular_assembler"]
      t: |-
        Function blocks: one wall + 2 ex pattern providers (pattern), 2 ex molecular assemblers (crafter) or 2 speed cards (speed) + 576 mB netherite certus skystone alloy, same EV assembler.
    - i: ["gtceu:me_pattern_buffer", "gtceu:me_pattern_buffer_proxy"]
      t: |-
        For GT machines: one ME Pattern Buffer holds the patterns; proxies on the other machines of the same kind link to it with a data stick and share its patterns, so one set of patterns serves a row of machines.
---
# Combo: Assembler Matrix and pattern buffers (AE2 automation)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_ae2` · **Tags:** Infinite source

**Plan modules:** [Assembler Matrix and pattern buffers (AE2)](../../plan/p20.md#cb_ae2)

**Tips:** 6

## Machines

<div class="gt-panels">
<div class="gt-panel t-ev" id="m-ea">
<div class="gt-head"><span class="gt-mname">EV Assembler · 1 920 EU/t · 20 s</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Plascrete or cleanroom glass (gtceu:plascrete)"><img class="gt-ico" src="../../assets/icons/gtceu__plascrete.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Plascrete</span><span class="gt-note">Plascrete or cleanroom glass</span></span><span class="gt-slot" title="Fluix smart cables (4) or dense (2) (ae2:fluix_smart_cable)"><img class="gt-ico" src="../../assets/icons/ae2__fluix_smart_cable.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluix Smart Cable</span><span class="gt-note">Fluix smart cables (4) or dense (2)</span></span><span class="gt-slot" title="2 to 4 ruthenium plates (gtceu:ruthenium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Dust</span><span class="gt-note">2 to 4 ruthenium plates</span></span><span class="gt-slot gt-fluid" title="Fluix steel · 576 mB (gtceu:fluix_steel_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__fluix_steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluix Steel Dust</span><span class="gt-note">Fluix steel · 576 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Matrix frame / wall / glass (expatternprovider:assembler_matrix_frame)"><img class="gt-ico" src="../../assets/icons/expatternprovider__assembler_matrix_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembler Matrix Frame</span><span class="gt-note">Matrix frame / wall / glass</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_assembler</code></div>
</div>
<div class="gt-panel t-ev" id="m-eb">
<div class="gt-head"><span class="gt-mname">EV Assembler</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Matrix frame / wall / glass (expatternprovider:assembler_matrix_frame) - 1 wall"><img class="gt-ico" src="../../assets/icons/expatternprovider__assembler_matrix_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembler Matrix Frame</span><span class="gt-note">Matrix frame / wall / glass</span><b class="gt-q">1 wall</b></span><span class="gt-slot" title="2 ex pattern providers (expatternprovider:ex_pattern_provider)"><img class="gt-ico" src="../../assets/icons/expatternprovider__ex_pattern_provider.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ex Pattern Provider</span><span class="gt-note">2 ex pattern providers</span></span><span class="gt-slot" title="or 2 ex molecular assemblers / 2 speed cards (expatternprovider:ex_molecular_assembler)"><img class="gt-ico" src="../../assets/icons/expatternprovider__ex_molecular_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ex Molecular Assembler</span><span class="gt-note">or 2 ex molecular assemblers / 2 speed cards</span></span><span class="gt-slot gt-fluid" title="Netherite certus skystone alloy · 576 mB (gtceu:netherite_certus_quartz_skystone_alloy_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__netherite_certus_quartz_skystone_alloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Netherite Certus Quartz Skystone Alloy</span><span class="gt-note">Netherite certus skystone alloy · 576 mB</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Assembler Matrix: pattern / crafter / speed (expatternprovider:assembler_matrix_frame)"><img class="gt-ico" src="../../assets/icons/expatternprovider__assembler_matrix_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembler Matrix Frame</span><span class="gt-note">Assembler Matrix: pattern / crafter / speed</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_assembler</code></div>
</div>
</div>

## Flow

- [EV Assembler · 1 920 EU/t · 20 s](#m-ea) → [EV Assembler](#m-eb)

### Direct steps

- ME Pattern Buffer + proxies → GT multiblocks / Assembly Line (shared patterns)
- ME stocking input bus / hatch → GT multiblocks / Assembly Line (ordered slots)

## How to build

1. Frames, walls and glass first: EV assembler, plascrete (or cleanroom glass) + fluix smart cables + ruthenium plates + 576 mB fluix steel, 20 s each. The matrix is a hollow structure of these; the functional blocks sit in its walls. — `gtceu:ev_assembler`, `expatternprovider:assembler_matrix_frame`
2. Function blocks: one wall + 2 ex pattern providers (pattern), 2 ex molecular assemblers (crafter) or 2 speed cards (speed) + 576 mB netherite certus skystone alloy, same EV assembler. — `expatternprovider:ex_pattern_provider`, `expatternprovider:ex_molecular_assembler`
3. For GT machines: one ME Pattern Buffer holds the patterns; proxies on the other machines of the same kind link to it with a data stick and share its patterns, so one set of patterns serves a row of machines. — `gtceu:me_pattern_buffer`, `gtceu:me_pattern_buffer_proxy`

## Tips

- Assembler Matrix (pack modifications/ae2/machinery.js): every piece is an EV assembler recipe, 400 ticks at 1 920 EU/t. Frame = plascrete + 2 fluix smart dense cables + 4 ruthenium plates + 576 mB fluix steel; wall = plascrete + 4 fluix smart cables + 2 ruthenium plates + 576 mB fluix steel; glass = cleanroom glass + 4 fluix smart cables + 2 ruthenium plates + 576 mB fluix steel; pattern / crafter / speed = 1 wall + 2 ex pattern providers / 2 ex molecular assemblers / 2 speed cards + 576 mB netherite certus quartz skystone alloy.
- Gates: ruthenium from the platinum group line (EV chemical reactor step), plascrete and cleanroom glass from the cleanroom line. The netherite certus skystone alloy needs netherite (EBF 3 300 K with argon) and blasts at 4 000 K at IV voltage, so the pattern, crafter and speed blocks are late EV to IV.
- Ex pattern provider (machinery.js, EV assembler): MEGA pattern provider + 4 calculation processors + 1 EV circuit + 4 double gold skystone alloy plates + 576 mB sky steel. ExpandedAE 1.4.2.e is in the pack.
- Pattern buffer combo (a community nickname, not an item): gtceu:me\_pattern\_buffer stores AE2 patterns for GT multiblocks; gtceu:me\_pattern\_buffer\_proxy links more machines (data stick) to share the patterns of that one buffer. ME stocking input buses/hatches and AE2 toggle buses also exist. Unverified: how many machines one buffer can feed.
- Smart blocking: plain AE2 15.5.4 only has simple Blocking Mode; ExpandedAE adds Default / Full / Smart ("allows same pattern to be pushed"). Community advice: Smart blocking misbehaves with parallels of the same item.
- Assembly Lines on stocking buses: pack config orderedAssemblyLineItems: true and orderedAssemblyLineFluids: false (config/gtceu.yaml), so items must reach the buses in recipe order; players force each item into its own slot by renaming stacks. Unverified: the renaming mechanism itself.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `expatternprovider:assembler_matrix_frame` | 1 |
| `gtceu:ev_assembler` | 1 |
| `gtceu:me_pattern_buffer` | 1 |
| `gtceu:me_pattern_buffer_proxy` | 4 |

## Needs / Feeds

- **Needs:** [Cleanroom (5×5×5): plascrete, filter casings, one energy hatch](../hv/hv_cleanroom.md)
- **Main source for:** `expatternprovider:assembler_matrix_frame`
