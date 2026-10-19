---
kind: chain
id: combo_mcf
order: 2360
data:
  t: |-
    Combo: Modular Combustion Frame with combustion and rocket modules
  inf: true
  power: true
  "n":
    - - hu
      - LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter / sensor / regulator
      - i
      - gtceu:luv_machine_hull
    - [al, "Assembly Line · research: iridium frame", m, "gtceu:assembly_line"]
    - [mcf, "Modular Combustion Frame (up to 8 modules)", p, "start_core:modular_combustion_frame"]
    - [ucm, "UCM · LuV combustion module", x, "start_core:luv_combustion_module"]
    - [scm, "SCM · ZPM combustion module", x, "start_core:zpm_combustion_module"]
    - [srm, "SRM · UV rocket module", x, "start_core:uv_combustion_module"]
    - [lu, "Lubricant (combustion modules)", f, "gtceu:lubricant_bucket"]
    - [wd, "Tungsten disulfide (rocket modules)", f, "gtceu:tungsten_disulfide_bucket"]
    - [ox, "Oxidiser: red fuming nitric acid (120 mB/s, 2x fuel)", f, "gtceu:red_fuming_nitric_acid_bucket"]
    - [cw, "Distilled water +20 % (500 B/h per module)", f, "gtceu:distilled_water_bucket"]
    - [out, "SCM up to 786 432 EU/t, SRM up to 4 194 304 EU/t per module", o, "gtceu:zpm_energy_output_hatch"]
  e:
    - [hu, al]
    - [al, mcf]
    - [ucm, mcf]
    - [scm, mcf]
    - [srm, mcf]
    - [lu, mcf]
    - [wd, mcf]
    - [ox, mcf]
    - [cw, mcf]
    - [mcf, out, laser hatches accepted]
  tips:
    - |-
      Names (start_core lang): Modular Combustion Frame [MCF]; Unreal Combustion Module [UCM] (LuV), Supreme Combustion Module [SCM] (ZPM), Supreme Rocket Module [SRM] (UV), Nyinsane Rocket Module [NRM] (UEV). The frame holds up to 8 modules; modules accept laser hatches.
    - |-
      Recipes (pack additions/progression/power/modular_combustion.js): MCF = Assembly Line, LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter/sensor/regulator, LuV voltage, scanner research of the iridium frame. SCM = Assembly Line, ZPM hull, 6 ZPM circuits, ZPM voltage, station research of the UCM (24 CWU/t). SRM = 8 UV circuits, 6 UV regulators, UV voltage, research of the SCM (64 CWU/t). NRM research of the SRM (160 CWU/t).
    - |-
      Output (start_core bytecode + lang): base = V[tier] per module (SCM 131 072 EU/t). With red fuming nitric acid (120 mB/s, fuel use x2) up to 6 A of ZPM = 786 432 EU/t per SCM; SRM up to 8 A of UV = 4 194 304 EU/t (200 mB/s). Oxidiser tiers WFNA / RFNA / dioxygen difluoride / ferrocenium superoxide = x5 / x6 / x8 / x12.
    - |-
      Cooling per module (500 B/h): distilled water +20 %, deionized water +40 %, none -10 %. Theoretical max with 8 modules: SCM 48 A of ZPM (about 6.29 M EU/t), SRM 64 A of UV (about 33.6 M EU/t); with deionized water about 8.8 M and 47.0 M.
    - |-
      The community figures "5 MCF + SCM = 288 A ZPM" and "384 A UV" are exactly 6x those maxima and could not be reproduced from the pack data: do not plan on them. Only the SCM:SRM ratio 6:8 matches.
    - |-
      Unverified: which fuel each module burns and at what rate (in the mod Java, not in the scripts).
  b:
    - ["start_core:modular_combustion_frame", 1]
    - ["start_core:zpm_combustion_module", 8]
    - ["gtceu:zpm_energy_output_hatch", 1]
    - ["gtceu:steel_drum", 4]
    - ["pipez:fluid_pipe", 16]
  how:
    - i: ["gtceu:assembly_line", "start_core:modular_combustion_frame"]
      t: |-
        Frame: research the iridium frame in the scanner, then the Assembly Line recipe (LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter, sensor and regulator).
    - i: ["start_core:zpm_combustion_module", "start_core:uv_combustion_module"]
      t: |-
        Modules: research UCM → SCM (24 CWU/t) → SRM (64 CWU/t) at the Research Station and assemble them; fill the frame up to 8.
    - i: ["gtceu:lubricant_bucket", "gtceu:distilled_water_bucket"]
      t: |-
        Fluids: fuel, lubricant (combustion) or tungsten disulfide (rocket), an oxidiser for the boost and 500 B/h of distilled or deionized water per module. Output through dynamo or laser hatches into the substation.
---
# Combo: Modular Combustion Frame with combustion and rocket modules

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `combo_mcf` · **Tags:** Infinite source, Power, Unverified

**Plan modules:** [Modular Combustion Frame with SCM / SRM modules](../../plan/p20.md#cb_mcf)

**Tips:** 6, 1 unverified

!!! tip "Plan this chain"

    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493) (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](../../tools.md).

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-al">
<div class="gt-head"><span class="gt-mname">Assembly Line · research: iridium frame</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter / sensor / regulator (gtceu:luv_machine_hull)"><img class="gt-ico" src="../../assets/icons/gtceu__luv_machine_hull.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Machine Hull</span><span class="gt-note">LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter / sensor / regulator</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-power" href="#m-mcf" title="Modular Combustion Frame (up to 8 modules) (start_core:modular_combustion_frame)"><img class="gt-ico" src="../../assets/icons/start_core__modular_combustion_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Modular Combustion Frame</span><span class="gt-note">Modular Combustion Frame (up to 8 modules)</span></a></div>
</div>
<div class="gt-foot"><code>gtceu:assembly_line</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-mcf">
<div class="gt-head"><span class="gt-mname">Modular Combustion Frame (up to 8 modules)</span><span class="gt-badge t-mod">StarT</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-al" title="Assembly Line · research: iridium frame (gtceu:assembly_line)"><img class="gt-ico" src="../../assets/icons/gtceu__assembly_line.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Assembly Line</span><span class="gt-note">Assembly Line · research: iridium frame</span></a><span class="gt-slot" title="UCM · LuV combustion module (start_core:luv_combustion_module)"><img class="gt-ico" src="../../assets/icons/start_core__luv_combustion_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Combustion Module</span><span class="gt-note">UCM · LuV combustion module</span></span><span class="gt-slot" title="SCM · ZPM combustion module (start_core:zpm_combustion_module)"><img class="gt-ico" src="../../assets/icons/start_core__zpm_combustion_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Combustion Module</span><span class="gt-note">SCM · ZPM combustion module</span></span><span class="gt-slot" title="SRM · UV rocket module (start_core:uv_combustion_module)"><img class="gt-ico" src="../../assets/icons/start_core__uv_combustion_module.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Combustion Module</span><span class="gt-note">SRM · UV rocket module</span></span><span class="gt-slot gt-fluid" title="Lubricant (combustion modules) (gtceu:lubricant_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__lubricant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Lubricant</span><span class="gt-note">Lubricant (combustion modules)</span></span><span class="gt-slot gt-fluid" title="Tungsten disulfide (rocket modules) (gtceu:tungsten_disulfide_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__tungsten_disulfide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tungsten Disulfide</span><span class="gt-note">Tungsten disulfide (rocket modules)</span></span><span class="gt-slot gt-fluid" title="Oxidiser: red fuming nitric acid (120 mB/s, 2x fuel) (gtceu:red_fuming_nitric_acid_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__red_fuming_nitric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Red Fuming Nitric Acid</span><span class="gt-note">Oxidiser: red fuming nitric acid (120 mB/s, 2x fuel)</span></span><span class="gt-slot gt-fluid" title="Distilled water +20 % (500 B/h per module) (gtceu:distilled_water_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__distilled_water_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Distilled Water</span><span class="gt-note">Distilled water +20 % (500 B/h per module)</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__modular_combustion_frame.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="SCM up to 786 432 EU/t, SRM up to 4 194 304 EU/t per module (gtceu:zpm_energy_output_hatch) - laser hatches accepted"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_energy_output_hatch.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Energy Output Hatch</span><span class="gt-note">SCM up to 786 432 EU/t, SRM up to 4 194 304 EU/t per module</span><b class="gt-q">laser hatches accepted</b></span></div>
</div>
<div class="gt-foot"><code>start_core:modular_combustion_frame</code></div>
</div>
</div>

## Flow

- [Assembly Line · research: iridium frame](#m-al) → [Modular Combustion Frame (up to 8 modules)](#m-mcf)

## How to build

1. Frame: research the iridium frame in the scanner, then the Assembly Line recipe (LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter, sensor and regulator). — `gtceu:assembly_line`, `start_core:modular_combustion_frame`
2. Modules: research UCM → SCM (24 CWU/t) → SRM (64 CWU/t) at the Research Station and assemble them; fill the frame up to 8. — `start_core:zpm_combustion_module`, `start_core:uv_combustion_module`
3. Fluids: fuel, lubricant (combustion) or tungsten disulfide (rocket), an oxidiser for the boost and 500 B/h of distilled or deionized water per module. Output through dynamo or laser hatches into the substation. — `gtceu:lubricant_bucket`, `gtceu:distilled_water_bucket`

## Tips

- Names (start\_core lang): Modular Combustion Frame \[MCF\]; Unreal Combustion Module \[UCM\] (LuV), Supreme Combustion Module \[SCM\] (ZPM), Supreme Rocket Module \[SRM\] (UV), Nyinsane Rocket Module \[NRM\] (UEV). The frame holds up to 8 modules; modules accept laser hatches.
- Recipes (pack additions/progression/power/modular\_combustion.js): MCF = Assembly Line, LuV hull, 2 LuV circuits, lapotronic orb cluster, LuV emitter/sensor/regulator, LuV voltage, scanner research of the iridium frame. SCM = Assembly Line, ZPM hull, 6 ZPM circuits, ZPM voltage, station research of the UCM (24 CWU/t). SRM = 8 UV circuits, 6 UV regulators, UV voltage, research of the SCM (64 CWU/t). NRM research of the SRM (160 CWU/t).
- Output (start\_core bytecode + lang): base = V\[tier\] per module (SCM 131 072 EU/t). With red fuming nitric acid (120 mB/s, fuel use x2) up to 6 A of ZPM = 786 432 EU/t per SCM; SRM up to 8 A of UV = 4 194 304 EU/t (200 mB/s). Oxidiser tiers WFNA / RFNA / dioxygen difluoride / ferrocenium superoxide = x5 / x6 / x8 / x12.
- Cooling per module (500 B/h): distilled water +20 %, deionized water +40 %, none -10 %. Theoretical max with 8 modules: SCM 48 A of ZPM (about 6.29 M EU/t), SRM 64 A of UV (about 33.6 M EU/t); with deionized water about 8.8 M and 47.0 M.
- The community figures "5 MCF + SCM = 288 A ZPM" and "384 A UV" are exactly 6x those maxima and could not be reproduced from the pack data: do not plan on them. Only the SCM:SRM ratio 6:8 matches.
- **Unverified** which fuel each module burns and at what rate (in the mod Java, not in the scripts).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:modular_combustion_frame` | 1 |
| `start_core:zpm_combustion_module` | 8 |
| `gtceu:zpm_energy_output_hatch` | 1 |
| `gtceu:steel_drum` | 4 |
| `pipez:fluid_pipe` | 16 |

## Needs / Feeds

- **Needs:** [LuV Machine Hull: rhodium plated palladium casing + 2 niobium titanium cables (PPS foil + PVC foil + silicone rubber) + PBI](../luv/luv_hull.md)
- **Main source for:** `start_core:modular_combustion_frame`, `start_core:zpm_combustion_module`, `start_core:uv_combustion_module`
