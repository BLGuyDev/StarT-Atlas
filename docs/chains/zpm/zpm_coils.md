---
kind: chain
id: zpm_coils
order: 1410
data:
  t: |-
    EBF coils: naquadah coil block (30 720 EU/t) → trinium → trinium coil block (122 880 EU/t), niobium nitride foil in both
  inf: true
  "n":
    - - nb
      - "1 niobium dust + 1 B nitrogen"
      - g
      - functionalstorage:oak_1
      - [[Niobium dust, "gtceu:niobium_dust"], [Nitrogen, "gtceu:nitrogen_bucket"]]
    - [r1, "HV Chemical Reactor · 10 s · 480 EU/t → 2 niobium nitride dust", m, "gtceu:hv_chemical_reactor"]
    - [nn, "Niobium nitride foil (EBF 2846 K, bender)", x, "gtceu:niobium_nitride_foil"]
    - - g1
      - HSS-G frame · 8 naquadah double wire · 8 osmium foil · 8 niobium nitride foil · 144 mB tungsten steel
      - g
      - functionalstorage:oak_1
      - - [HSS-G frame, "gtceu:hssg_frame"]
        - [Naquadah double wire, "gtceu:naquadah_double_wire"]
        - [Osmium foil, "gtceu:osmium_foil"]
        - [Tungsten steel, "gtceu:tungsten_steel_bucket"]
    - [a1, "Large Assembler on a 4A hatch · 35 s · 30 720 EU/t", m, "gtceu:large_assembler"]
    - [c1, "Naquadah Coil Block (7200 K)", x, "gtceu:naquadah_coil_block"]
    - - g2
      - HSS-E frame · 8 trinium double wire · 8 enriched naquadah foil · 16 niobium nitride foil · 144 mB molten naquadah
      - g
      - functionalstorage:oak_1
      - - [HSS-E frame, "gtceu:hsse_frame"]
        - [Trinium double wire, "gtceu:trinium_double_wire"]
        - [Enriched naquadah foil, "gtceu:enriched_naquadah_foil"]
        - [Naquadah, "gtceu:naquadah_bucket"]
    - [a2, "Large Assembler on a LuV 4A hatch · 40 s · 122 880 EU/t", m, "gtceu:large_assembler"]
    - [c2, "Trinium Coil Block (9001 K)", o, "gtceu:trinium_coil_block"]
  e:
    - [nb, r1, "1 + 1 B"]
    - [r1, nn, "2 dust / 10 s"]
    - [nn, g1, "8 foil"]
    - [nn, g2, "16 foil"]
    - [g1, a1, "1"]
    - [a1, c1, "1 / 35 s"]
    - [c1, g2, EBF 7200 K makes the trinium]
    - [g2, a2, "1"]
    - [a2, c2, "1 / 40 s"]
  tips:
    - |-
      Pack recipes (kjs additions/machines_and_parts/coils.js; all GT coil recipes are removed first): Naquadah Coil Block = 1 HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel, assembler, 700 ticks (35 s) at 30 720 EU/t. Trinium Coil Block = 1 HSS-E frame + 8 trinium double wire + 8 enriched naquadah foil + 16 niobium nitride foil + 144 mB molten naquadah, 800 ticks (40 s) at 122 880 EU/t. The trinium one is a ZPM-power recipe: a Large Assembler on a LuV 4A hatch (4 x 32 768 = 131 072 EU/t) or a ZPM assembler. The quest: the trinium coil is the 7th coil tier and ‘worth getting all your EBFs to it’.
    - |-
      Temperatures: by the GT coil table the naquadah coil is 7200 K and the trinium coil 9001 K (the pack keeps cupronickel 1800, kanthal 2700, nichrome 3600, RTM 4500, HSS-G 5400 as the earlier guide chapters verified; the fork CoilType table verifies naquadah 7200, trinium 9001 and tritanium 10 800 K, and the pack adds zalloy 13 499, magmada 16 199 and abyssal 18 888 K in kubejs coils.js; 13 custom multis such as the HIF, CAT and Ultimate EBF use heating coils). What runs where: naquadah alloy 7200 K, osthendah 7050 K, trinium 7200 K, enriched naquadah 7000 K and dragonsteel 7100 K all fit the naquadah coil; naquadria and uranium rhodium dinaquadide need 9000 K = the trinium coil. So the trinium coil is the gate to URD, which the Research Station and fusion MK II need.
    - |-
      Raw cost per coil block (1 ingot per double wire, 1/4 ingot per foil, frame 2 ingots): naquadah coil = 8 naquadah + 2 osmium + 2 niobium nitride + 2 HSS-G (frame) + 144 mB tungsten steel; trinium coil = 8 trinium + 2 enriched naquadah + 4 niobium nitride + 2 HSS-E (frame) + 144 mB naquadah. An EBF needs its full coil ring (16 blocks: the EBF multis card has 16 coil positions): 16 naquadah coils = 128 naquadah ingots; 16 trinium coils = 128 TRINIUM ingots = 768 naquadah dust at 6 dust per trinium. Build ONE trinium-coil furnace for naquadria and URD, not an upgrade of every furnace.
    - |-
      Niobium nitride (ReactorRecipes niobium_nitride, FirstDegreeMaterials): 1 niobium dust + 1 B nitrogen → 2 niobium nitride dust, chemical reactor, 200 ticks at 480 EU/t; the ingot is an EBF product at 2846 K (Unverified power/time: the default blast stats), then plate and foil (bender, 4 foil per plate). Each naquadah coil eats 2 NbN ingots and each trinium coil 4. Niobium itself: Unverified (see luv_alloys: no pack script gives a niobium route, check EMI for niobium dust).
    - |-
      Frames: HSS-G frame (IV era HSS-G line) and HSS-E frame (HSS-E from the IV abs_super_ebf chain; HSS-E has a frame flag by GT), each 2 ingots with the frame recipe at the assembler/hand. Molten tungsten steel and naquadah: 144 mB = 1 ingot, from the Fluid Extractor, or by the ABS.
    - |-
      Sub-steps people skip: (1) the wire is DOUBLE wire (a wiremill with the double mold), not single; (2) the foil of the trinium coil is ENRICHED naquadah (zpm_naq_products), the foil of the naquadah coil is OSMIUM; (3) the trinium coil recipe is 122 880 EU/t, so the power hatch decides, not the machine name; (4) keep one drawer per ingredient and a Keep Exact 8 on the NbN foil: it feeds two coil recipes.
    - |-
      Unverified: the Large Assembler accepting the 122 880 EU/t recipe through a 4A hatch, and the niobium nitride EBF time.
  b:
    - ["gtceu:large_assembler", 1]
    - ["gtceu:hv_chemical_reactor", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:iv_energy_input_hatch_4a", 1]
    - ["gtceu:luv_energy_input_hatch_4a", 1]
    - ["gtceu:lv_bender", 1]
    - ["gtceu:lv_wiremill", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 10]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 3]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:naquadah_double_wire", "gtceu:osmium_foil", "gtceu:niobium_nitride_foil"]
      t: |-
        Drawers first, one per part: naquadah double wire, osmium foil, niobium nitride foil, HSS-G frames, HSS-E frames, trinium double wire, enriched naquadah foil. Drums: tungsten steel, naquadah. Each assembler gets its own input drawers behind Modular Routers or Pipez pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output.
    - i: ["gtceu:hv_chemical_reactor", "gtceu:niobium_nitride_foil", "gtceu:nitrogen_bucket"]
      t: |-
        Niobium nitride: HV Chemical Reactor, 1 niobium dust + 1 B nitrogen → 2 dust in 10 s at 480 EU/t; EBF (2846 K) to ingots, a bender for plates, a second bender or a foil mold for foil, 4 foil per plate. Make 100 foil before the first coil.
    - i: ["gtceu:lv_wiremill", "gtceu:naquadah_double_wire"]
      t: |-
        Wire: a wiremill with the double-wire mold: naquadah ingots → double wire (1 ingot each), 8 per coil. The same wiremill later does trinium double wire. Output drawers Keep Exact 16.
    - i: ["gtceu:large_assembler", "gtceu:naquadah_coil_block"]
      t: |-
        Naquadah coil: the Large Assembler on a 4A hatch, HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 NbN foil + 144 mB molten tungsten steel → 1 coil in 35 s at 30 720 EU/t. Make 16 for the first EBF.
    - i: ["gtceu:electric_blast_furnace", "gtceu:trinium_ingot"]
      t: Then the naquadah-coil EBF makes trinium (zpm_naq_products), naquadah alloy and osthendah (zpm_alloys). Collect 128 trinium ingots before the first trinium coil furnace is plausible; the first few go to double wire for one test coil.
    - i: ["gtceu:large_assembler", "gtceu:trinium_coil_block", "gtceu:enriched_naquadah_foil"]
      t: |-
        Trinium coil: HSS-E frame + 8 trinium double wire + 8 enriched naquadah foil + 16 NbN foil + 144 mB molten naquadah → 1 coil in 40 s at 122 880 EU/t on a LuV 4A hatch.
    - i: ["functionalstorage:oak_1", "gtceu:trinium_coil_block"]
      t: |-
        Easy to miss: do not rebuild old EBFs first; the EBFs with RTM or HSS-G coils keep doing their jobs. Only naquadria, URD and the highest recipes need the 9000 K furnace, so build that one furnace and feed it with a long drawer queue.
---
# EBF coils: naquadah coil block (30 720 EU/t) → trinium → trinium coil block (122 880 EU/t), niobium nitride foil in both

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `zpm_coils` · **Tags:** Infinite source, Unverified

**Era setup:** [ZPM &amp; Classic Stargate](../../eras/zpm.md)

**Plan modules:** [Naquadah metals and ZPM coils](../../plan/p12.md#zpmmetals)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-r1">
<div class="gt-head"><span class="gt-mname">HV Chemical Reactor · 10 s · 480 EU/t → 2 niobium nitride dust</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 niobium dust + 1 B nitrogen (functionalstorage:oak_1) - 1 + 1 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 niobium dust + 1 B nitrogen</span><span class="gt-sub"><span>Niobium dust</span><span>Nitrogen</span></span><b class="gt-q">1 + 1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">10 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Niobium nitride foil (EBF 2846 K, bender) (gtceu:niobium_nitride_foil) - 2 dust / 10 s"><img class="gt-ico" src="../../assets/icons/gtceu__niobium_nitride_foil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Niobium Nitride Foil</span><span class="gt-note">Niobium nitride foil (EBF 2846 K, bender)</span><b class="gt-q">2 dust</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">Large Assembler on a 4A hatch · 35 s · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="HSS-G frame · 8 naquadah double wire · 8 osmium foil · 8 niobium nitride foil · 144 mB tungsten steel (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">HSS-G frame · 8 naquadah double wire · 8 osmium foil · 8 niobium nitride foil · 144 mB tungsten steel</span><span class="gt-sub"><span>HSS-G frame</span><span>Naquadah double wire</span><span>Osmium foil</span><span>Tungsten steel</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">35 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Naquadah Coil Block (7200 K) (gtceu:naquadah_coil_block) - 1 / 35 s"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Coil Block</span><span class="gt-note">Naquadah Coil Block (7200 K)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Large Assembler on a LuV 4A hatch · 40 s · 122 880 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="HSS-E frame · 8 trinium double wire · 8 enriched naquadah foil · 16 niobium nitride foil · 144 mB molten naquadah (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">HSS-E frame · 8 trinium double wire · 8 enriched naquadah foil · 16 niobium nitride foil · 144 mB molten naquadah</span><span class="gt-sub"><span>HSS-E frame</span><span>Trinium double wire</span><span>Enriched naquadah foil</span><span>Naquadah</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">40 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Trinium Coil Block (9001 K) (gtceu:trinium_coil_block) - 1 / 40 s"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Coil Block</span><span class="gt-note">Trinium Coil Block (9001 K)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
</div>

## Flow

- [HV Chemical Reactor · 10 s · 480 EU/t → 2 niobium nitride dust](#m-r1) → [Large Assembler on a 4A hatch · 35 s · 30 720 EU/t](#m-a1) → [Large Assembler on a LuV 4A hatch · 40 s · 122 880 EU/t](#m-a2) (also HV Chemical Reactor · 10 s · 480 EU/t → 2 niobium nitride dust → [Large Assembler on a LuV 4A hatch · 40 s · 122 880 EU/t](#m-a2))

### Direct steps

- Niobium nitride foil (EBF 2846 K, bender) → HSS-G frame · 8 naquadah double wire · 8 osmium foil · 8 niobium nitride foil · 144 mB tungsten steel (8 foil)
- Niobium nitride foil (EBF 2846 K, bender) → HSS-E frame · 8 trinium double wire · 8 enriched naquadah foil · 16 niobium nitride foil · 144 mB molten naquadah (16 foil)
- Naquadah Coil Block (7200 K) → HSS-E frame · 8 trinium double wire · 8 enriched naquadah foil · 16 niobium nitride foil · 144 mB molten naquadah (EBF 7200 K makes the trinium)

## How to build

1. Drawers first, one per part: naquadah double wire, osmium foil, niobium nitride foil, HSS-G frames, HSS-E frames, trinium double wire, enriched naquadah foil. Drums: tungsten steel, naquadah. Each assembler gets its own input drawers behind Modular Routers or Pipez pipes with Item Filters, and a Robot Arm cover in Keep Exact mode on its output. — `functionalstorage:oak_1`, `gtceu:naquadah_double_wire`, `gtceu:osmium_foil`, `gtceu:niobium_nitride_foil`
2. Niobium nitride: HV Chemical Reactor, 1 niobium dust + 1 B nitrogen → 2 dust in 10 s at 480 EU/t; EBF (2846 K) to ingots, a bender for plates, a second bender or a foil mold for foil, 4 foil per plate. Make 100 foil before the first coil. — `gtceu:hv_chemical_reactor`, `gtceu:niobium_nitride_foil`, `gtceu:nitrogen_bucket`
3. Wire: a wiremill with the double-wire mold: naquadah ingots → double wire (1 ingot each), 8 per coil. The same wiremill later does trinium double wire. Output drawers Keep Exact 16. — `gtceu:lv_wiremill`, `gtceu:naquadah_double_wire`
4. Naquadah coil: the Large Assembler on a 4A hatch, HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 NbN foil + 144 mB molten tungsten steel → 1 coil in 35 s at 30 720 EU/t. Make 16 for the first EBF. — `gtceu:large_assembler`, `gtceu:naquadah_coil_block`
5. Then the naquadah-coil EBF makes trinium (zpm\_naq\_products), naquadah alloy and osthendah (zpm\_alloys). Collect 128 trinium ingots before the first trinium coil furnace is plausible; the first few go to double wire for one test coil. — `gtceu:electric_blast_furnace`, `gtceu:trinium_ingot`
6. Trinium coil: HSS-E frame + 8 trinium double wire + 8 enriched naquadah foil + 16 NbN foil + 144 mB molten naquadah → 1 coil in 40 s at 122 880 EU/t on a LuV 4A hatch. — `gtceu:large_assembler`, `gtceu:trinium_coil_block`, `gtceu:enriched_naquadah_foil`
7. Easy to miss: do not rebuild old EBFs first; the EBFs with RTM or HSS-G coils keep doing their jobs. Only naquadria, URD and the highest recipes need the 9000 K furnace, so build that one furnace and feed it with a long drawer queue. — `functionalstorage:oak_1`, `gtceu:trinium_coil_block`

## Tips

- Pack recipes (kjs additions/machines\_and\_parts/coils.js; all GT coil recipes are removed first): Naquadah Coil Block = 1 HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel, assembler, 700 ticks (35 s) at 30 720 EU/t. Trinium Coil Block = 1 HSS-E frame + 8 trinium double wire + 8 enriched naquadah foil + 16 niobium nitride foil + 144 mB molten naquadah, 800 ticks (40 s) at 122 880 EU/t. The trinium one is a ZPM-power recipe: a Large Assembler on a LuV 4A hatch (4 x 32 768 = 131 072 EU/t) or a ZPM assembler. The quest: the trinium coil is the 7th coil tier and ‘worth getting all your EBFs to it’.
- Temperatures: by the GT coil table the naquadah coil is 7200 K and the trinium coil 9001 K (the pack keeps cupronickel 1800, kanthal 2700, nichrome 3600, RTM 4500, HSS-G 5400 as the earlier guide chapters verified; the fork CoilType table verifies naquadah 7200, trinium 9001 and tritanium 10 800 K, and the pack adds zalloy 13 499, magmada 16 199 and abyssal 18 888 K in kubejs coils.js; 13 custom multis such as the HIF, CAT and Ultimate EBF use heating coils). What runs where: naquadah alloy 7200 K, osthendah 7050 K, trinium 7200 K, enriched naquadah 7000 K and dragonsteel 7100 K all fit the naquadah coil; naquadria and uranium rhodium dinaquadide need 9000 K = the trinium coil. So the trinium coil is the gate to URD, which the Research Station and fusion MK II need.
- Raw cost per coil block (1 ingot per double wire, 1/4 ingot per foil, frame 2 ingots): naquadah coil = 8 naquadah + 2 osmium + 2 niobium nitride + 2 HSS-G (frame) + 144 mB tungsten steel; trinium coil = 8 trinium + 2 enriched naquadah + 4 niobium nitride + 2 HSS-E (frame) + 144 mB naquadah. An EBF needs its full coil ring (16 blocks: the EBF multis card has 16 coil positions): 16 naquadah coils = 128 naquadah ingots; 16 trinium coils = 128 TRINIUM ingots = 768 naquadah dust at 6 dust per trinium. Build ONE trinium-coil furnace for naquadria and URD, not an upgrade of every furnace.
- Niobium nitride (ReactorRecipes niobium\_nitride, FirstDegreeMaterials): 1 niobium dust + 1 B nitrogen → 2 niobium nitride dust, chemical reactor, 200 ticks at 480 EU/t; the ingot is an EBF product at 2846 K (Unverified power/time: the default blast stats), then plate and foil (bender, 4 foil per plate). Each naquadah coil eats 2 NbN ingots and each trinium coil 4. Niobium itself: Unverified (see luv\_alloys: no pack script gives a niobium route, check EMI for niobium dust).
- Frames: HSS-G frame (IV era HSS-G line) and HSS-E frame (HSS-E from the IV abs\_super\_ebf chain; HSS-E has a frame flag by GT), each 2 ingots with the frame recipe at the assembler/hand. Molten tungsten steel and naquadah: 144 mB = 1 ingot, from the Fluid Extractor, or by the ABS.
- Sub-steps people skip: (1) the wire is DOUBLE wire (a wiremill with the double mold), not single; (2) the foil of the trinium coil is ENRICHED naquadah (zpm\_naq\_products), the foil of the naquadah coil is OSMIUM; (3) the trinium coil recipe is 122 880 EU/t, so the power hatch decides, not the machine name; (4) keep one drawer per ingredient and a Keep Exact 8 on the NbN foil: it feeds two coil recipes.
- **Unverified** the Large Assembler accepting the 122 880 EU/t recipe through a 4A hatch, and the niobium nitride EBF time.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_assembler` | 1 |
| `gtceu:hv_chemical_reactor` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:iv_energy_input_hatch_4a` | 1 |
| `gtceu:luv_energy_input_hatch_4a` | 1 |
| `gtceu:lv_bender` | 1 |
| `gtceu:lv_wiremill` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 10 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 3 |

## Needs / Feeds

- **Main source for:** `gtceu:naquadah_coil_block`, `gtceu:trinium_coil_block`, `gtceu:niobium_nitride_foil`
