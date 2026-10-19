---
kind: chain
id: kanthal
order: 1030
data:
  t: |-
    Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block
  inf: true
  "n":
    - [fe, Iron dust, i, "gtceu:iron_dust"]
    - [al, Aluminium dust, i, "gtceu:aluminium_dust"]
    - [cr, Chromium dust, i, "gtceu:chromium_dust"]
    - [mx, "MV Mixer · circuit 1 · 15 s · 120 EU/t", m, "gtceu:mv_mixer"]
    - [kd, "3 Kanthal dust", x, "gtceu:kanthal_dust"]
    - [eb, "EBF · 1800 K · 45 s · 480 EU/t", m, "gtceu:electric_blast_furnace"]
    - [hi, Hot kanthal ingot, x, "gtceu:hot_kanthal_ingot"]
    - [cb, "MV Chemical Bath · 100 mB water · 20 s", m, "gtceu:mv_chemical_bath"]
    - [ki, Kanthal ingot, x, "gtceu:kanthal_ingot"]
    - [wm, "LV Wiremill · circuit 2", m, "gtceu:lv_wiremill"]
    - [dw, "8 Double wire", x, "gtceu:kanthal_double_wire"]
    - [ai, "2 Aluminium ingots", i, "gtceu:aluminium_ingot"]
    - [be, "LV Bender · circuit 10", m, "gtceu:lv_bender"]
    - [af, "8 Aluminium foil", x, "gtceu:aluminium_foil"]
    - [cu, "1 Copper ingot", i, "minecraft:copper_ingot"]
    - [ex, LV Extractor, m, "gtceu:lv_extractor"]
    - [cm, "144 mB molten copper", f, "gtceu:copper_bucket"]
    - [as, "MV Assembler · 15 s · 120 EU/t", m, "gtceu:mv_assembler"]
    - [co, Kanthal Coil Block, o, "gtceu:kanthal_coil_block"]
    - [sp, "Kanthal spring (HV machines)", o, "gtceu:kanthal_spring"]
  e:
    - [fe, mx]
    - [al, mx]
    - [cr, mx]
    - [mx, kd, "3"]
    - [kd, eb, "1"]
    - [eb, hi]
    - [hi, cb]
    - [cb, ki]
    - [ki, wm, "8"]
    - [wm, dw]
    - [ai, be, "2"]
    - [be, af, "1 → 4"]
    - [cu, ex]
    - [ex, cm]
    - [dw, as, "8"]
    - [af, as, "8"]
    - [cm, as, "144 mB"]
    - [as, co]
    - [ki, sp, rods]
  tips:
    - |-
      Mixer: 1 iron + 1 aluminium + 1 chromium dust (circuit 1) → 3 kanthal dust in 15 s at 120 EU/t, so 12 dust a minute: one mixer feeds nine EBFs.
    - |-
      EBF: 1 dust → 1 HOT ingot at 1800 K, 480 EU/t, 45 s (circuit 1). With circuit 2 and 1 B nitrogen per ingot it takes 30 s. The recipe is HV tier: a single MV energy hatch refuses it, use the HV Energy Hatch or two MV hatches (4 A at 120 V counts as 1 A at 480 V). Cupronickel coils are enough: 1800 K, plus 100 K at an HV hatch.
    - |-
      The hot ingot is a separate item: chemical bath with 100 mB water, 20 s at 120 EU/t (distilled water 12.5 s). The Vacuum Freezer would also work but its controller needs 3 EV circuits, so the bath is the HV route.
    - One coil block = 8 double wire (8 ingots) + 8 aluminium foil (2 ingots) + 144 mB molten copper, MV assembler 15 s at 120 EU/t. Sixteen coils = 128 kanthal ingots (128 iron + 128 aluminium + 128 chromium dust), 32 aluminium ingots, 16 copper ingots. One EBF needs 96 minutes for 128 ingots, 64 minutes with nitrogen.
    - |-
      What it unlocks: Kanthal coils are 2700 K (2800 K at an HV hatch). From the material list (gtsrc): black bronze 2000 K, vanadium 2183 K, ultimet 2700 K and niobium 2750 K become possible; nichrome (2700 K) also needs an EV hatch, titanium 1941 K is an EV job in this pack. The Pyrolyse Oven speed multiplier goes from x1.33 to x1.0 duration.
    - |-
      Kanthal wire and springs are inside HV machines: HV Electric Blast Furnace (2 double + 1 quadruple wire), HV electric furnace (4 double), alloy smelter, extruder (4 quadruple each), thermal centrifuge and fluid heater (2 quadruple), HV pulverizer (pack recipe), and 1 spring each in the HV brewery, HV distillery and the Industrial Barrel. Build this line before the HV machine row.
    - |-
      Unverified: the machine that turns 2 rods into a long rod (forge hammer or hand, read EMI), Chromium comes from chromite dust (Void Extractor rare ore residue) through an Electrolyzer: see the Chromium chain in the EV era; its timing is derived from the fork code, so confirm it in EMI before you commit to 16 coils.
  b:
    - ["gtceu:mv_mixer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:hv_energy_input_hatch", 1]
    - ["gtceu:mv_chemical_bath", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["gtceu:lv_bender", 2]
    - ["gtceu:mv_assembler", 1]
    - ["gtceu:lv_extractor", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 5]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:iron_dust", "gtceu:aluminium_dust", "gtceu:chromium_dust"]
      t: |-
        Three input drawers: iron dust, aluminium dust, chromium dust. Aluminium and iron come as ingots from the sieve and aluminium lines: a macerator (one per metal, 1 ingot → 1 dust) in front of each drawer. Chromium comes from the stainless chain’s source (chromite dust); both chains share that drawer, so size it for 128 more.
    - i: ["gtceu:mv_mixer", "gtceu:kanthal_dust"]
      t: |-
        MV Mixer with ghost circuit 1: 1 iron + 1 aluminium + 1 chromium dust → 3 kanthal dust, 15 s, 120 EU/t. A Modular Router (or Pipez item pipe with an Item Filter) pulls each dust from its drawer. A Robot Arm cover on the output in Keep Exact mode with an Item Filter on kanthal dust and 64 tops the output drawer up and then stops the mixer.
    - i:
        - gtceu:electric_blast_furnace
        - gtceu:cupronickel_coil_block
        - gtceu:hv_energy_input_hatch
        - gtceu:hot_kanthal_ingot
      t: |-
        EBF (the one from the stainless chain works): input bus with ghost circuit 1, output bus, HV Energy Hatch. 1 kanthal dust → 1 hot kanthal ingot in 45 s at 480 EU/t. For circuit 2, add an input hatch of nitrogen (1 B per ingot, from the oxygen line) and the time drops to 30 s. If stainless and kanthal share one furnace it keeps switching: give kanthal its own EBF when you build the 128.
    - i: ["gtceu:mv_chemical_bath", "gtceu:hot_kanthal_ingot", "gtceu:kanthal_ingot", "minecraft:water_bucket"]
      t: |-
        The sub-step people skip: hot ingots must be cooled. Put an MV Chemical Bath beside the EBF output bus (Pipez item pipe or a router straight from the bus, never through a drawer that also holds finished ingots). 1 hot ingot + 100 mB water → 1 kanthal ingot in 20 s at 120 EU/t. Water through an input hatch from the water line; distilled water makes it 12.5 s. One bath cools about 3 ingots a minute, enough for two EBFs.
    - i: ["gtceu:lv_wiremill", "gtceu:kanthal_double_wire"]
      t: |-
        Wiremill, ghost circuit 2: 1 kanthal ingot → 1 double wire (circuit 4 is quadruple wire: 2 ingots). A coil needs 8, so each coil swallows 8 ingots. Keep a second wiremill for quadruple wire only if you build HV machines (EBF, extruder, alloy smelter).
    - i: ["gtceu:lv_bender", "gtceu:aluminium_ingot", "gtceu:aluminium_foil"]
      t: |-
        Bender on ghost circuit 10: 1 aluminium ingot → 4 foil (24 EU/t). Circuit 1 would make plates instead. 2 ingots = 8 foil = one coil. Molten copper: LV Extractor, 1 copper ingot → 144 mB, then a fluid pipe or pump cover into the assembler.
    - i: ["gtceu:mv_assembler", "gtceu:kanthal_coil_block"]
      t: |-
        MV Assembler: 8 double wire + 8 aluminium foil + 144 mB molten copper → 1 Kanthal Coil Block in 15 s at 120 EU/t (4 a minute; an LV assembler cannot, 120 EU/t is MV). Output to a drawer with a Robot Arm Keep Exact 16.
    - i: ["gtceu:kanthal_spring", "gtceu:lv_lathe", "gtceu:lv_bender"]
      t: |-
        Springs for the HV distillery, brewery and Industrial Barrel: lathe 1 kanthal ingot → 2 rods (16 EU/t), 2 rods → 1 long rod (forge hammer or hand), bender on circuit 1: 1 long rod → 1 spring (10 s, 16 EU/t). Make a handful only.
    - i: ["gtceu:pyrolyse_oven", "gtceu:kanthal_coil_block"]
      t: |-
        Easy to miss: nothing in this guide’s HV chains needs the coil block itself. Build it when you want the recipes above 1900 K or to speed the Pyrolyse Oven (replace the 16 cupronickel coils, same slots). The wire and springs for HV machines are the part that blocks you.
---
# Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `kanthal` · **Tags:** Infinite source, Unverified

**Era setup:** [HV](../../eras/hv.md)

**Plan modules:** [Stainless steel and Kanthal](../../plan/p7.md#stainless)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-mx">
<div class="gt-head"><span class="gt-mname">MV Mixer · circuit 1 · 15 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Iron dust (gtceu:iron_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__iron_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iron Dust</span></span><span class="gt-slot" title="Aluminium dust (gtceu:aluminium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Dust</span></span><span class="gt-slot" title="Chromium dust (gtceu:chromium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__chromium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromium Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="3 Kanthal dust (gtceu:kanthal_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Dust</span><span class="gt-note">3 Kanthal dust</span><b class="gt-q">3</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · 1800 K · 45 s · 480 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Kanthal dust (gtceu:kanthal_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Dust</span><span class="gt-note">3 Kanthal dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Hot kanthal ingot (gtceu:hot_kanthal_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__hot_kanthal_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Kanthal Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-mv" id="m-cb">
<div class="gt-head"><span class="gt-mname">MV Chemical Bath · 100 mB water · 20 s</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Hot kanthal ingot (gtceu:hot_kanthal_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__hot_kanthal_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Kanthal Ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_bath.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Kanthal ingot (gtceu:kanthal_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_bath</code></div>
</div>
<div class="gt-panel t-lv" id="m-wm">
<div class="gt-head"><span class="gt-mname">LV Wiremill · circuit 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Kanthal ingot (gtceu:kanthal_ingot) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Ingot</span><b class="gt-q">8</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_wiremill.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Double wire (gtceu:kanthal_double_wire)"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Double Wire</span><span class="gt-note">8 Double wire</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_wiremill</code></div>
</div>
<div class="gt-panel t-lv" id="m-be">
<div class="gt-head"><span class="gt-mname">LV Bender · circuit 10</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Aluminium ingots (gtceu:aluminium_ingot) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Ingot</span><span class="gt-note">2 Aluminium ingots</span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_bender.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="8 Aluminium foil (gtceu:aluminium_foil) - 1 → 4"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Foil</span><span class="gt-note">8 Aluminium foil</span><b class="gt-q">1 → 4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_bender</code></div>
</div>
<div class="gt-panel t-lv" id="m-ex">
<div class="gt-head"><span class="gt-mname">LV Extractor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Copper ingot (minecraft:copper_ingot)"><img class="gt-ico" src="../../assets/icons/minecraft__copper_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper Ingot</span><span class="gt-note">1 Copper ingot</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="144 mB molten copper (gtceu:copper_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__copper_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper</span><span class="gt-note">144 mB molten copper</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_extractor</code></div>
</div>
<div class="gt-panel t-mv" id="m-as">
<div class="gt-head"><span class="gt-mname">MV Assembler · 15 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="8 Double wire (gtceu:kanthal_double_wire) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_double_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Double Wire</span><span class="gt-note">8 Double wire</span><b class="gt-q">8</b></span><span class="gt-slot" title="8 Aluminium foil (gtceu:aluminium_foil) - 8"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Foil</span><span class="gt-note">8 Aluminium foil</span><b class="gt-q">8</b></span><span class="gt-slot gt-fluid" title="144 mB molten copper (gtceu:copper_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__copper_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Copper</span><span class="gt-note">144 mB molten copper</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Kanthal Coil Block (gtceu:kanthal_coil_block)"><img class="gt-ico" src="../../assets/icons/gtceu__kanthal_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Kanthal Coil Block</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_assembler</code></div>
</div>
</div>

## Flow

- [MV Mixer · circuit 1 · 15 s · 120 EU/t](#m-mx) → [EBF · 1800 K · 45 s · 480 EU/t](#m-eb) → [MV Chemical Bath · 100 mB water · 20 s](#m-cb) → [LV Wiremill · circuit 2](#m-wm) → [MV Assembler · 15 s · 120 EU/t](#m-as)
- [LV Bender · circuit 10](#m-be) → [MV Assembler · 15 s · 120 EU/t](#m-as)
- [LV Extractor](#m-ex) → [MV Assembler · 15 s · 120 EU/t](#m-as)

### Direct steps

- Kanthal ingot → Kanthal spring (HV machines) (rods)

## How to build

1. Three input drawers: iron dust, aluminium dust, chromium dust. Aluminium and iron come as ingots from the sieve and aluminium lines: a macerator (one per metal, 1 ingot → 1 dust) in front of each drawer. Chromium comes from the stainless chain’s source (chromite dust); both chains share that drawer, so size it for 128 more. — `functionalstorage:oak_1`, `gtceu:iron_dust`, `gtceu:aluminium_dust`, `gtceu:chromium_dust`
2. MV Mixer with ghost circuit 1: 1 iron + 1 aluminium + 1 chromium dust → 3 kanthal dust, 15 s, 120 EU/t. A Modular Router (or Pipez item pipe with an Item Filter) pulls each dust from its drawer. A Robot Arm cover on the output in Keep Exact mode with an Item Filter on kanthal dust and 64 tops the output drawer up and then stops the mixer. — `gtceu:mv_mixer`, `gtceu:kanthal_dust`
3. EBF (the one from the stainless chain works): input bus with ghost circuit 1, output bus, HV Energy Hatch. 1 kanthal dust → 1 hot kanthal ingot in 45 s at 480 EU/t. For circuit 2, add an input hatch of nitrogen (1 B per ingot, from the oxygen line) and the time drops to 30 s. If stainless and kanthal share one furnace it keeps switching: give kanthal its own EBF when you build the 128. — `gtceu:electric_blast_furnace`, `gtceu:cupronickel_coil_block`, `gtceu:hv_energy_input_hatch`, `gtceu:hot_kanthal_ingot`
4. The sub-step people skip: hot ingots must be cooled. Put an MV Chemical Bath beside the EBF output bus (Pipez item pipe or a router straight from the bus, never through a drawer that also holds finished ingots). 1 hot ingot + 100 mB water → 1 kanthal ingot in 20 s at 120 EU/t. Water through an input hatch from the water line; distilled water makes it 12.5 s. One bath cools about 3 ingots a minute, enough for two EBFs. — `gtceu:mv_chemical_bath`, `gtceu:hot_kanthal_ingot`, `gtceu:kanthal_ingot`, `minecraft:water_bucket`
5. Wiremill, ghost circuit 2: 1 kanthal ingot → 1 double wire (circuit 4 is quadruple wire: 2 ingots). A coil needs 8, so each coil swallows 8 ingots. Keep a second wiremill for quadruple wire only if you build HV machines (EBF, extruder, alloy smelter). — `gtceu:lv_wiremill`, `gtceu:kanthal_double_wire`
6. Bender on ghost circuit 10: 1 aluminium ingot → 4 foil (24 EU/t). Circuit 1 would make plates instead. 2 ingots = 8 foil = one coil. Molten copper: LV Extractor, 1 copper ingot → 144 mB, then a fluid pipe or pump cover into the assembler. — `gtceu:lv_bender`, `gtceu:aluminium_ingot`, `gtceu:aluminium_foil`
7. MV Assembler: 8 double wire + 8 aluminium foil + 144 mB molten copper → 1 Kanthal Coil Block in 15 s at 120 EU/t (4 a minute; an LV assembler cannot, 120 EU/t is MV). Output to a drawer with a Robot Arm Keep Exact 16. — `gtceu:mv_assembler`, `gtceu:kanthal_coil_block`
8. Springs for the HV distillery, brewery and Industrial Barrel: lathe 1 kanthal ingot → 2 rods (16 EU/t), 2 rods → 1 long rod (forge hammer or hand), bender on circuit 1: 1 long rod → 1 spring (10 s, 16 EU/t). Make a handful only. — `gtceu:kanthal_spring`, `gtceu:lv_lathe`, `gtceu:lv_bender`
9. Easy to miss: nothing in this guide’s HV chains needs the coil block itself. Build it when you want the recipes above 1900 K or to speed the Pyrolyse Oven (replace the 16 cupronickel coils, same slots). The wire and springs for HV machines are the part that blocks you. — `gtceu:pyrolyse_oven`, `gtceu:kanthal_coil_block`

## Tips

- Mixer: 1 iron + 1 aluminium + 1 chromium dust (circuit 1) → 3 kanthal dust in 15 s at 120 EU/t, so 12 dust a minute: one mixer feeds nine EBFs.
- EBF: 1 dust → 1 HOT ingot at 1800 K, 480 EU/t, 45 s (circuit 1). With circuit 2 and 1 B nitrogen per ingot it takes 30 s. The recipe is HV tier: a single MV energy hatch refuses it, use the HV Energy Hatch or two MV hatches (4 A at 120 V counts as 1 A at 480 V). Cupronickel coils are enough: 1800 K, plus 100 K at an HV hatch.
- The hot ingot is a separate item: chemical bath with 100 mB water, 20 s at 120 EU/t (distilled water 12.5 s). The Vacuum Freezer would also work but its controller needs 3 EV circuits, so the bath is the HV route.
- One coil block = 8 double wire (8 ingots) + 8 aluminium foil (2 ingots) + 144 mB molten copper, MV assembler 15 s at 120 EU/t. Sixteen coils = 128 kanthal ingots (128 iron + 128 aluminium + 128 chromium dust), 32 aluminium ingots, 16 copper ingots. One EBF needs 96 minutes for 128 ingots, 64 minutes with nitrogen.
- What it unlocks: Kanthal coils are 2700 K (2800 K at an HV hatch). From the material list (gtsrc): black bronze 2000 K, vanadium 2183 K, ultimet 2700 K and niobium 2750 K become possible; nichrome (2700 K) also needs an EV hatch, titanium 1941 K is an EV job in this pack. The Pyrolyse Oven speed multiplier goes from x1.33 to x1.0 duration.
- Kanthal wire and springs are inside HV machines: HV Electric Blast Furnace (2 double + 1 quadruple wire), HV electric furnace (4 double), alloy smelter, extruder (4 quadruple each), thermal centrifuge and fluid heater (2 quadruple), HV pulverizer (pack recipe), and 1 spring each in the HV brewery, HV distillery and the Industrial Barrel. Build this line before the HV machine row.
- **Unverified** the machine that turns 2 rods into a long rod (forge hammer or hand, read EMI), Chromium comes from chromite dust (Void Extractor rare ore residue) through an Electrolyzer: see the Chromium chain in the EV era; its timing is derived from the fork code, so confirm it in EMI before you commit to 16 coils.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_mixer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:hv_energy_input_hatch` | 1 |
| `gtceu:mv_chemical_bath` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `gtceu:lv_bender` | 2 |
| `gtceu:mv_assembler` | 1 |
| `gtceu:lv_extractor` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 5 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |

## Needs / Feeds

- **Needs:** [Ore processing](../lv/ores.md), [Chromium: Void Extractor residue → chromite dust → electrolyzer → chromium dust, ingot and rod](chromium_line.md), [Infinite aluminium (clay)](../mv/aluminium.md), [Ingots, wrought iron, wires and foil from the sieve](../lv/ingots.md)
- **Feeds:** [EV components: titanium parts, motor, piston, robot arm, pump, conveyor, hull](../ev/ev_components.md)
- **Main source for:** `gtceu:kanthal_dust`, `gtceu:hot_kanthal_ingot`, `gtceu:kanthal_ingot`, `gtceu:kanthal_double_wire`, `gtceu:kanthal_coil_block`, `gtceu:kanthal_spring`
