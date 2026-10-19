---
kind: chain
id: stainless
order: 270
data:
  t: "Stainless steel: MV Mixer + HV Electric Blast Furnace"
  "n":
    - [fe, "6 Iron", i, "gtceu:iron_dust"]
    - [cr, Chromium, i, "gtceu:chromium_dust"]
    - [mn, Manganese, i, "gtceu:manganese_dust"]
    - [ni, Nickel, i, "gtceu:nickel_dust"]
    - [mx, Mixer, m, "gtceu:mv_mixer"]
    - [sd, "9 Stainless dust", x, "gtceu:stainless_steel_dust"]
    - [ebf, EBF, m, "gtceu:electric_blast_furnace"]
    - [ss, Stainless, o, "gtceu:stainless_steel_ingot"]
  e: [[fe, mx], [cr, mx], [mn, mx], [ni, mx], [mx, sd], [sd, ebf, "1700 K"], [ebf, ss]]
  tips:
    - |-
      Mixer: 6 iron + 1 nickel + 1 manganese + 1 chromium dust (circuit 3) → 9 stainless steel dust in 30 s at 120 EU/t. Alternative (circuit 1): 4 iron + 3 invar + 1 manganese + 1 chromium → 9 dust.
    - |-
      EBF: 1 dust → 1 ingot at 1700 K, 480 EU/t, 55 s (circuit 1). With circuit 2 and 1 B nitrogen per ingot it takes 36.9 s. One furnace = 1.1 ingots a minute (1.6 with nitrogen).
    - |-
      480 EU/t is HV tier: a single MV energy hatch refuses the recipe. The BOM adds the EBF’s own LV hatch; build the HV Energy Hatch listed with it instead, or use two MV hatches (4 A at 120 V counts as 1 A at 480 V). Recipe: 1700 K, 1100 ticks.
    - |-
      If one mixer ever limits you: Large Mixer = HV Mixer + Multiblock Upgrade Kit (the kit needs an EV circuit).
    - An HV Machine Hull alone is 9 stainless plates (8 in the casing + 1), so run a first batch of 9 dust well before you need hulls.
    - |-
      Coil heat: cupronickel 1800 K (1900 K once you have an HV hatch), Kanthal 2700 K, Nichrome 3600 K. Stainless only needs 1700 K, so more heat just saves 5 % EU per 900 K.
  b:
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:hv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 6]
    - ["modularrouters:modular_router", 2]
    - ["gtceu:lv_robot_arm", 2]
    - ["gtceu:item_filter", 2]
    - ["pipez:item_pipe", 16]
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:iron_dust
        - gtceu:nickel_dust
        - gtceu:manganese_dust
        - gtceu:chromium_dust
      t: |-
        Four input drawers (functionalstorage), one dust each: iron, nickel, manganese, chromium. Chromium is the scarce one and has no sieve route (the chromite and pyrolusite sieves are disabled in this pack): Void Extractor rare ore residue → LV electrolyzer → chromite sludge → MV centrifuge → chromite dust → electrolyzer (derived: 7 dust → 1 iron + 2 chromium + 4 B oxygen; read the exact recipe in EMI). Manganese: pyrolusite from the MV centrifuge on raw ore slurry, or spessartine geodes from the MV Rock Filtrator. Nickel: pentlandite (blackstone sieve, Void Extractor).
    - i: ["gtceu:mv_mixer", "gtceu:stainless_steel_dust"]
      t: |-
        MV Mixer with ghost circuit 3: 6 iron + 1 nickel + 1 manganese + 1 chromium dust → 9 stainless steel dust, 30 s, 120 EU/t. That is 18 dust a minute, enough for 16 furnaces, so one mixer is plenty. If you already run invar, circuit 1 takes 4 iron + 3 invar + 1 manganese + 1 chromium for the same 9 dust.
    - i: ["modularrouters:modular_router", "gtceu:lv_robot_arm", "gtceu:item_filter"]
      t: |-
        A Modular Router (or a Pipez item pipe with an Item Filter) pulls each dust from its drawer into the mixer. On the mixer output face put a Robot Arm cover in Keep Exact mode with an Item Filter set to stainless steel dust and 64: it tops the output drawer up to 64 and then stops, so the mixer idles instead of flooding.
    - i: ["gtceu:electric_blast_furnace", "gtceu:cupronickel_coil_block", "gtceu:heatproof_machine_casing"]
      t: |-
        EBF: 16 cupronickel coils (1800 K) + 16 heat proof invar casings (9 minimum, the rest can be hatches) + muffler hatch + controller; hatches: input bus, output bus, input hatch (nitrogen), maintenance and an HV Energy Hatch. Working temperature is coil heat + 100 K per tier above MV, so cupronickel reaches 1900 K at HV and the 1700 K recipe starts. Keep the muffler’s front face free.
    - i: ["gtceu:stainless_steel_ingot", "gtceu:nitrogen_bucket"]
      t: |-
        Input bus gets the dust (ghost circuit 1): 1 dust → 1 ingot in 55 s at 480 EU/t. For speed put circuit 2 and feed 1000 mB nitrogen per ingot through the input hatch: 36.9 s per ingot. The nitrogen comes from the air centrifuge (about 2.6 B of air per ingot). A Robot Arm cover on the output bus drops ingots in a drawer, Keep Exact 64.
    - i: ["gtceu:kanthal_coil_block", "gtceu:hot_kanthal_ingot", "gtceu:nichrome_coil_block"]
      t: |-
        Next coil tier is a pack recipe: Kanthal coil = 8 kanthal double wire + 8 aluminium foil + 144 mB copper (assembler 15 s, 120 EU/t). Kanthal ingot: iron + aluminium + chromium dust in the mixer (circuit 1, 15 s, 120 EU/t) → 3 dust → EBF 1800 K, 480 EU/t, 45 s → HOT ingot → chemical bath with 100 mB water (20 s, 120 EU/t; 12.5 s with distilled water). Nichrome coil needs 2700 K and 1920 EU/t ingots, so it is an EV job.
    - i: ["gtceu:hv_machine_hull", "gtceu:stainless_steel_plate"]
      t: |-
        Easy to miss: the EBF eats one item per run, there is no parallel, and batch mode only helps recipes shorter than 5 s. Need more stainless? Build a second EBF, not a better coil. Plates: bender (1 ingot → 1 plate). One HV hull = 9 plates + 2 polyethylene plates + 2 gold cables.
---
# Stainless steel: MV Mixer + HV Electric Blast Furnace

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `stainless`

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Stainless steel and Kanthal](../../plan/p7.md#stainless)

**Tips:** 6

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-mx">
<div class="gt-head"><span class="gt-mname">Mixer</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="6 Iron (gtceu:iron_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span><span class="gt-note">6 Iron</span></span><span class="gt-slot" title="Chromium (gtceu:chromium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Dust</span></span><span class="gt-slot" title="Manganese (gtceu:manganese_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__manganese_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Manganese Dust</span></span><span class="gt-slot" title="Nickel (gtceu:nickel_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__nickel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nickel Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="9 Stainless dust (gtceu:stainless_steel_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Dust</span><span class="gt-note">9 Stainless dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-ebf">
<div class="gt-head"><span class="gt-mname">EBF</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="9 Stainless dust (gtceu:stainless_steel_dust) - 1700 K"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Dust</span><span class="gt-note">9 Stainless dust</span><b class="gt-q">1700 K</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Stainless (gtceu:stainless_steel_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__stainless_steel_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stainless Steel Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [Mixer](#m-mx) → [EBF](#m-ebf)

## How to build

1. Four input drawers (functionalstorage), one dust each: iron, nickel, manganese, chromium. Chromium is the scarce one and has no sieve route (the chromite and pyrolusite sieves are disabled in this pack): Void Extractor rare ore residue → LV electrolyzer → chromite sludge → MV centrifuge → chromite dust → electrolyzer (derived: 7 dust → 1 iron + 2 chromium + 4 B oxygen; read the exact recipe in EMI). Manganese: pyrolusite from the MV centrifuge on raw ore slurry, or spessartine geodes from the MV Rock Filtrator. Nickel: pentlandite (blackstone sieve, Void Extractor). — `functionalstorage:oak_1`, `gtceu:iron_dust`, `gtceu:nickel_dust`, `gtceu:manganese_dust`, `gtceu:chromium_dust`
2. MV Mixer with ghost circuit 3: 6 iron + 1 nickel + 1 manganese + 1 chromium dust → 9 stainless steel dust, 30 s, 120 EU/t. That is 18 dust a minute, enough for 16 furnaces, so one mixer is plenty. If you already run invar, circuit 1 takes 4 iron + 3 invar + 1 manganese + 1 chromium for the same 9 dust. — `gtceu:mv_mixer`, `gtceu:stainless_steel_dust`
3. A Modular Router (or a Pipez item pipe with an Item Filter) pulls each dust from its drawer into the mixer. On the mixer output face put a Robot Arm cover in Keep Exact mode with an Item Filter set to stainless steel dust and 64: it tops the output drawer up to 64 and then stops, so the mixer idles instead of flooding. — `modularrouters:modular_router`, `gtceu:lv_robot_arm`, `gtceu:item_filter`
4. EBF: 16 cupronickel coils (1800 K) + 16 heat proof invar casings (9 minimum, the rest can be hatches) + muffler hatch + controller; hatches: input bus, output bus, input hatch (nitrogen), maintenance and an HV Energy Hatch. Working temperature is coil heat + 100 K per tier above MV, so cupronickel reaches 1900 K at HV and the 1700 K recipe starts. Keep the muffler’s front face free. — `gtceu:electric_blast_furnace`, `gtceu:cupronickel_coil_block`, `gtceu:heatproof_machine_casing`
5. Input bus gets the dust (ghost circuit 1): 1 dust → 1 ingot in 55 s at 480 EU/t. For speed put circuit 2 and feed 1000 mB nitrogen per ingot through the input hatch: 36.9 s per ingot. The nitrogen comes from the air centrifuge (about 2.6 B of air per ingot). A Robot Arm cover on the output bus drops ingots in a drawer, Keep Exact 64. — `gtceu:stainless_steel_ingot`, `gtceu:nitrogen_bucket`
6. Next coil tier is a pack recipe: Kanthal coil = 8 kanthal double wire + 8 aluminium foil + 144 mB copper (assembler 15 s, 120 EU/t). Kanthal ingot: iron + aluminium + chromium dust in the mixer (circuit 1, 15 s, 120 EU/t) → 3 dust → EBF 1800 K, 480 EU/t, 45 s → HOT ingot → chemical bath with 100 mB water (20 s, 120 EU/t; 12.5 s with distilled water). Nichrome coil needs 2700 K and 1920 EU/t ingots, so it is an EV job. — `gtceu:kanthal_coil_block`, `gtceu:hot_kanthal_ingot`, `gtceu:nichrome_coil_block`
7. Easy to miss: the EBF eats one item per run, there is no parallel, and batch mode only helps recipes shorter than 5 s. Need more stainless? Build a second EBF, not a better coil. Plates: bender (1 ingot → 1 plate). One HV hull = 9 plates + 2 polyethylene plates + 2 gold cables. — `gtceu:hv_machine_hull`, `gtceu:stainless_steel_plate`

## Tips

- Mixer: 6 iron + 1 nickel + 1 manganese + 1 chromium dust (circuit 3) → 9 stainless steel dust in 30 s at 120 EU/t. Alternative (circuit 1): 4 iron + 3 invar + 1 manganese + 1 chromium → 9 dust.
- EBF: 1 dust → 1 ingot at 1700 K, 480 EU/t, 55 s (circuit 1). With circuit 2 and 1 B nitrogen per ingot it takes 36.9 s. One furnace = 1.1 ingots a minute (1.6 with nitrogen).
- 480 EU/t is HV tier: a single MV energy hatch refuses the recipe. The BOM adds the EBF’s own LV hatch; build the HV Energy Hatch listed with it instead, or use two MV hatches (4 A at 120 V counts as 1 A at 480 V). Recipe: 1700 K, 1100 ticks.
- If one mixer ever limits you: Large Mixer = HV Mixer + Multiblock Upgrade Kit (the kit needs an EV circuit).
- An HV Machine Hull alone is 9 stainless plates (8 in the casing + 1), so run a first batch of 9 dust well before you need hulls.
- Coil heat: cupronickel 1800 K (1900 K once you have an HV hatch), Kanthal 2700 K, Nichrome 3600 K. Stainless only needs 1700 K, so more heat just saves 5 % EU per 900 K.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:hv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 6 |
| `modularrouters:modular_router` | 2 |
| `gtceu:lv_robot_arm` | 2 |
| `gtceu:item_filter` | 2 |
| `pipez:item_pipe` | 16 |

## Needs / Feeds

- **Needs:** [Ore processing](../lv/ores.md), [Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod](chromium_line.md), [Raw Ore Slurry &amp; mineral mixtures](../mv/slurry.md)
- **Feeds:** [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../ev/nichrome_line.md)
- **Main source for:** `gtceu:stainless_steel_ingot`, `gtceu:stainless_steel_dust`
