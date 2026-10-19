---
kind: chain
id: uhv_alloys
order: 1780
data:
  t: |-
    UHV metals: tritanium coil block (10 800 K), zalloy (ABS 10 799 K), zircalloy-4 (251 zirconium per batch), zirconium selenide diiodide
  inf: true
  "n":
    - - g1
      - trinaquadalloy frame · 8 tritanium double wire · 8 naquadria foil · 32 niobium nitride foil · 144 mB trinium
      - g
      - functionalstorage:oak_1
      - - [Trinaquadalloy frame, "gtceu:trinaquadalloy_frame"]
        - [Tritanium double wire, "gtceu:tritanium_double_wire"]
        - [Naquadria foil, "gtceu:naquadria_foil"]
        - [Niobium nitride foil, "gtceu:niobium_nitride_foil"]
    - [a1, "UV Assembler · 45 s · 491 520 EU/t", m, "gtceu:large_assembler"]
    - [co, "Tritanium Coil Block (10 800 K)", o, "gtceu:tritanium_coil_block"]
    - - g2
      - "3 zapolgium · 4 duranium · 2 europium (dusts) · circuit 3"
      - g
      - functionalstorage:oak_1
      - - [Zapolgium dust, "gtceu:zapolgium_dust"]
        - [Duranium dust, "gtceu:duranium_dust"]
        - [Europium dust, "gtceu:europium_dust"]
    - [a2, "Alloy Blast Smelter · 10 799 K · 16.9 min · 61 440 EU/t", m, "gtceu:alloy_blast_smelter"]
    - [za, "Zalloy 1296 mB (9 ingots)", o, "gtceu:zalloy_bucket"]
    - - g3
      - |-
        251 zirconium · 3 tin · 2 chromium · 1 iron (dusts) · circuit 4
      - g
      - functionalstorage:oak_1
      - - [Zirconium dust, "gtceu:zirconium_dust"]
        - [Tin dust, "gtceu:tin_dust"]
        - [Chromium dust, "gtceu:chromium_dust"]
        - [Iron dust, "gtceu:iron_dust"]
    - [a3, "Alloy Blast Smelter · 9100 K · 96 min · 30 720 EU/t", m, "gtceu:alloy_blast_smelter"]
    - [zc, "Zircalloy-4 37 B (257 ingots)", o, "gtceu:zircalloy_4_bucket"]
    - - g4
      - "1 zirconium · 1 selenium · 2 iodine (dusts) · circuit 3"
      - g
      - functionalstorage:oak_1
      - [[Selenium dust, "gtceu:selenium_dust"], [Iodine dust, "gtceu:iodine_dust"]]
    - [a4, "Alloy Blast Smelter · 9600 K · 9 min · 30 720 EU/t", m, "gtceu:alloy_blast_smelter"]
    - [zs, "Zirconium selenide diiodide 576 mB (4 ingots)", o, "gtceu:zirconium_selenide_diiodide_bucket"]
  e:
    - [g1, a1, "1"]
    - [a1, co, "1 / 45 s"]
    - [g2, a2, "9 dusts"]
    - [a2, za, "1296 mB"]
    - [g3, a3, "257 dusts"]
    - [a3, zc, "37 B"]
    - [g4, a4, "4 dusts"]
    - [a4, zs, "576 mB"]
  tips:
    - |-
      Tritanium coil block (kjs additions/machines_and_parts/coils.js, verified; the GT recipes for all coil blocks are removed): 1 trinaquadalloy frame + 8 tritanium DOUBLE wire + 8 naquadria foil + 32 niobium nitride foil + 144 mB trinium, assembler, 900 ticks at 491 520 EU/t (UV assembler), output 1 block. 10 800 K is the temperature this tier gives (GT standard); it is needed for every blast over 9001 K: zalloy 10 799 K, zirconium selenide diiodide 9600 K, ENTED 9900 K, RTAN 10 800 K, the rare earth EBF 7500 K only needs trinium coils.
    - |-
      Zalloy (kjs startup abydos_alloys.js, verified): 3 zapolgium + 4 duranium + 2 europium (9 parts), blast data [10 799 K, gas tier highest, VHA[ZPM] = 61 440 EU/t, 3000 ticks per ingot]; ABS rule (abs_super_ebf): circuit 3 (number of components), 0.75 x 3000 x 9 = 20 250 ticks (16.9 min), 1296 mB. Parts: plate, frame, rod, bolt, screw, round, long rod, gear, small gear, ring, dense plate. It is the primary metal of UHV components. Duranium is the fusion metal (uv_fusion_mats), zapolgium comes from zapolite (uhv_zapolgium).
    - |-
      Zircalloy-4 (same file): 251 zirconium + 3 tin + 2 chromium + 1 iron (257 parts), blast [9100 K, gas higher, VA[LuV] = 30 720 EU/t, 1800 ticks per ingot]; ABS circuit 4, 0.75 x 1800 x 257 = 346 950 ticks (96 min!) for 37 B, one batch. Parts: gear, small gear, rotor, round, frame. It is the secondary metal: UHV pump rotors, piston gears, drive mechanisms, catalyst-core rings, fusion double plates (UHV fusion reactor). Zirconium: titanite line (uhv_zirconium).
    - |-
      Zirconium selenide diiodide (same file, conductor): 1 zirconium + 1 selenium + 2 iodine (4 parts), blast [9600 K, gas higher, VA[LuV], 3600 ticks per ingot]; ABS circuit 3, 0.75 x 3600 x 4 = 10 800 ticks (9 min), 576 mB. It is the UHV cable wire (spring flag in the pack; V[UHV], 8 A). Selenium and iodine: the Abydos ores (kitkaite, crookesite, lautarite) and the zapolite chain give iodine; selenium Unverified.
    - |-
      Sub-steps people skip: (1) these four recipes only start with the right COIL TEMPERATURE: tritanium coils (10 800 K) in the ABS for zalloy and ZSD; (2) a zircalloy-4 batch is 257 dusts: 251 zirconium dust is 4 stacks (3 x 64 + 59) plus the other three dusts, so the ABS needs an input bus with at least 7 slots (Unverified bus size) and a router that delivers exactly 251; (3) never split a batch: the ABS recipe has one fixed ratio; (4) three different ABS machines or empty the hatches between recipes.
    - |-
      Unverified: selenium source, duranium dust supply for zalloy, ABS bus size for 251 dusts.
  b:
    - ["gtceu:alloy_blast_smelter", 3]
    - ["gtceu:uv_assembler", 1]
    - ["gtceu:uv_energy_input_hatch", 1]
    - ["functionalstorage:oak_1", 14]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 14]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:zapolgium_dust", "gtceu:zirconium_dust", "gtceu:tritanium_double_wire"]
      t: |-
        Drawers first: zapolgium (3), duranium (4), europium (2), zirconium (251 in 4 drawers), tin, chromium, iron, selenium, iodine; wire and foil drawers for the coil. Drums: trinium and the alloy outputs.
    - i: ["gtceu:uv_assembler", "gtceu:tritanium_coil_block"]
      t: |-
        Coils first: the UV assembler (45 s per block) makes the coils for the ABS and blast furnaces. Output drawer Keep Exact 24: every ABS needs 24 of them.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:zalloy_bucket"]
      t: |-
        ABS 1: zalloy, circuit 3, 16.9 min; output hatch to a drum, then a vacuum freezer with the ingot mold or a solidifier for plates and frames.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:zircalloy_4_bucket"]
      t: |-
        ABS 2: zircalloy-4, circuit 4, one batch every 96 min; 37 B into its own drum. This is the longest recipe of the era: start it before everything else.
    - i: ["gtceu:alloy_blast_smelter", "gtceu:zirconium_selenide_diiodide_bucket"]
      t: |-
        ABS 3: zirconium selenide diiodide, circuit 3, 9 min per 4 ingots; wires from a wiremill.
    - i: ["functionalstorage:oak_1", "gtceu:zalloy_ingot"]
      t: Output drawers Keep Exact 16 per metal.
---
# UHV metals: tritanium coil block (10 800 K), zalloy (ABS 10 799 K), zircalloy-4 (251 zirconium per batch), zirconium selenide diiodide

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_alloys` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Zapolgium, superconductors, alloys, void ingot](../../plan/p17.md#uhvmetals)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-a1">
<div class="gt-head"><span class="gt-mname">UV Assembler · 45 s · 491 520 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="trinaquadalloy frame · 8 tritanium double wire · 8 naquadria foil · 32 niobium nitride foil · 144 mB trinium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">trinaquadalloy frame · 8 tritanium double wire · 8 naquadria foil · 32 niobium nitride foil · 144 mB trinium</span><span class="gt-sub"><span>Trinaquadalloy frame</span><span>Tritanium double wire</span><span>Naquadria foil</span><span>Niobium nitride foil</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">45 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Tritanium Coil Block (10 800 K) (gtceu:tritanium_coil_block) - 1 / 45 s"><img class="gt-ico" src="../../assets/icons/gtceu__tritanium_coil_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritanium Coil Block</span><span class="gt-note">Tritanium Coil Block (10 800 K)</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_assembler</code></div>
</div>
<div class="gt-panel t-multi" id="m-a2">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · 10 799 K · 16.9 min · 61 440 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="3 zapolgium · 4 duranium · 2 europium (dusts) · circuit 3 (functionalstorage:oak_1) - 9 dusts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">3 zapolgium · 4 duranium · 2 europium (dusts) · circuit 3</span><span class="gt-sub"><span>Zapolgium dust</span><span>Duranium dust</span><span>Europium dust</span></span><b class="gt-q">9 dusts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Zalloy 1296 mB (9 ingots) (gtceu:zalloy_bucket) - 1296 mB"><img class="gt-ico" src="../../assets/icons/gtceu__zalloy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Zalloy Bucket</span><span class="gt-note">Zalloy 1296 mB (9 ingots)</span><b class="gt-q">1296 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
<div class="gt-panel t-multi" id="m-a3">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · 9100 K · 96 min · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="251 zirconium · 3 tin · 2 chromium · 1 iron (dusts) · circuit 4 (functionalstorage:oak_1) - 257 dusts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">251 zirconium · 3 tin · 2 chromium · 1 iron (dusts) · circuit 4</span><span class="gt-sub"><span>Zirconium dust</span><span>Tin dust</span><span>Chromium dust</span><span>Iron dust</span></span><b class="gt-q">257 dusts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Zircalloy-4 37 B (257 ingots) (gtceu:zircalloy_4_bucket) - 37 B"><img class="gt-ico" src="../../assets/icons/gtceu__zircalloy_4_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Zircalloy 4 Bucket</span><span class="gt-note">Zircalloy-4 37 B (257 ingots)</span><b class="gt-q">37 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
<div class="gt-panel t-multi" id="m-a4">
<div class="gt-head"><span class="gt-mname">Alloy Blast Smelter · 9600 K · 9 min · 30 720 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 zirconium · 1 selenium · 2 iodine (dusts) · circuit 3 (functionalstorage:oak_1) - 4 dusts"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 zirconium · 1 selenium · 2 iodine (dusts) · circuit 3</span><span class="gt-sub"><span>Selenium dust</span><span>Iodine dust</span></span><b class="gt-q">4 dusts</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__alloy_blast_smelter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Zirconium selenide diiodide 576 mB (4 ingots) (gtceu:zirconium_selenide_diiodide_bucket) - 576 mB"><img class="gt-ico" src="../../assets/icons/gtceu__zirconium_selenide_diiodide_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Zirconium Selenide Diiodide Bucket</span><span class="gt-note">Zirconium selenide diiodide 576 mB (4 ingots)</span><b class="gt-q">576 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:alloy_blast_smelter</code></div>
</div>
</div>

## Flow

- [UV Assembler · 45 s · 491 520 EU/t](#m-a1)
- [Alloy Blast Smelter · 10 799 K · 16.9 min · 61 440 EU/t](#m-a2)
- [Alloy Blast Smelter · 9100 K · 96 min · 30 720 EU/t](#m-a3)
- [Alloy Blast Smelter · 9600 K · 9 min · 30 720 EU/t](#m-a4)

## How to build

1. Drawers first: zapolgium (3), duranium (4), europium (2), zirconium (251 in 4 drawers), tin, chromium, iron, selenium, iodine; wire and foil drawers for the coil. Drums: trinium and the alloy outputs. — `functionalstorage:oak_1`, `gtceu:zapolgium_dust`, `gtceu:zirconium_dust`, `gtceu:tritanium_double_wire`
2. Coils first: the UV assembler (45 s per block) makes the coils for the ABS and blast furnaces. Output drawer Keep Exact 24: every ABS needs 24 of them. — `gtceu:uv_assembler`, `gtceu:tritanium_coil_block`
3. ABS 1: zalloy, circuit 3, 16.9 min; output hatch to a drum, then a vacuum freezer with the ingot mold or a solidifier for plates and frames. — `gtceu:alloy_blast_smelter`, `gtceu:zalloy_bucket`
4. ABS 2: zircalloy-4, circuit 4, one batch every 96 min; 37 B into its own drum. This is the longest recipe of the era: start it before everything else. — `gtceu:alloy_blast_smelter`, `gtceu:zircalloy_4_bucket`
5. ABS 3: zirconium selenide diiodide, circuit 3, 9 min per 4 ingots; wires from a wiremill. — `gtceu:alloy_blast_smelter`, `gtceu:zirconium_selenide_diiodide_bucket`
6. Output drawers Keep Exact 16 per metal. — `functionalstorage:oak_1`, `gtceu:zalloy_ingot`

## Tips

- Tritanium coil block (kjs additions/machines\_and\_parts/coils.js, verified; the GT recipes for all coil blocks are removed): 1 trinaquadalloy frame + 8 tritanium DOUBLE wire + 8 naquadria foil + 32 niobium nitride foil + 144 mB trinium, assembler, 900 ticks at 491 520 EU/t (UV assembler), output 1 block. 10 800 K is the temperature this tier gives (GT standard); it is needed for every blast over 9001 K: zalloy 10 799 K, zirconium selenide diiodide 9600 K, ENTED 9900 K, RTAN 10 800 K, the rare earth EBF 7500 K only needs trinium coils.
- Zalloy (kjs startup abydos\_alloys.js, verified): 3 zapolgium + 4 duranium + 2 europium (9 parts), blast data \[10 799 K, gas tier highest, VHA\[ZPM\] = 61 440 EU/t, 3000 ticks per ingot\]; ABS rule (abs\_super\_ebf): circuit 3 (number of components), 0.75 x 3000 x 9 = 20 250 ticks (16.9 min), 1296 mB. Parts: plate, frame, rod, bolt, screw, round, long rod, gear, small gear, ring, dense plate. It is the primary metal of UHV components. Duranium is the fusion metal (uv\_fusion\_mats), zapolgium comes from zapolite (uhv\_zapolgium).
- Zircalloy-4 (same file): 251 zirconium + 3 tin + 2 chromium + 1 iron (257 parts), blast \[9100 K, gas higher, VA\[LuV\] = 30 720 EU/t, 1800 ticks per ingot\]; ABS circuit 4, 0.75 x 1800 x 257 = 346 950 ticks (96 min!) for 37 B, one batch. Parts: gear, small gear, rotor, round, frame. It is the secondary metal: UHV pump rotors, piston gears, drive mechanisms, catalyst-core rings, fusion double plates (UHV fusion reactor). Zirconium: titanite line (uhv\_zirconium).
- Zirconium selenide diiodide (same file, conductor): 1 zirconium + 1 selenium + 2 iodine (4 parts), blast \[9600 K, gas higher, VA\[LuV\], 3600 ticks per ingot\]; ABS circuit 3, 0.75 x 3600 x 4 = 10 800 ticks (9 min), 576 mB. It is the UHV cable wire (spring flag in the pack; V\[UHV\], 8 A). Selenium and iodine: the Abydos ores (kitkaite, crookesite, lautarite) and the zapolite chain give iodine; selenium Unverified.
- Sub-steps people skip: (1) these four recipes only start with the right COIL TEMPERATURE: tritanium coils (10 800 K) in the ABS for zalloy and ZSD; (2) a zircalloy-4 batch is 257 dusts: 251 zirconium dust is 4 stacks (3 x 64 + 59) plus the other three dusts, so the ABS needs an input bus with at least 7 slots (Unverified bus size) and a router that delivers exactly 251; (3) never split a batch: the ABS recipe has one fixed ratio; (4) three different ABS machines or empty the hatches between recipes.
- **Unverified** selenium source, duranium dust supply for zalloy, ABS bus size for 251 dusts.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:alloy_blast_smelter` | 3 |
| `gtceu:uv_assembler` | 1 |
| `gtceu:uv_energy_input_hatch` | 1 |
| `functionalstorage:oak_1` | 14 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 14 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:zalloy_ingot`, `gtceu:zalloy_bucket`, `gtceu:zircalloy_4_ingot`, `gtceu:zircalloy_4_bucket`, `gtceu:zirconium_selenide_diiodide_ingot`, `gtceu:tritanium_coil_block`
