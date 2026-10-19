---
kind: chain
id: uhv_sc
order: 1810
data:
  t: |-
    UHV superconductors: thorium plutonium duranide 241 (voltage coil wire) and ruthenium trinium americium neutronate (RTAN, UHV cable and fusion wire)
  inf: true
  "n":
    - - g1
      - "4 thorium · 1 duranium · 3 plutonium 241 (dusts) · circuit 4"
      - g
      - functionalstorage:oak_1
      - - [Thorium dust, "gtceu:thorium_dust"]
        - [Duranium dust, "gtceu:duranium_dust"]
        - [Plutonium 241 dust, "gtceu:plutonium_241_dust"]
    - [m1, "UV Mixer · 50 s · 491 520 EU/t → 8 dust", m, "gtceu:uv_mixer"]
    - [e1, "EBF 10 199 K · 42.5 s · 491 520 EU/t (tritanium coils)", m, "gtceu:electric_blast_furnace"]
    - [f1, "Vacuum freezer → ingot → fine wire (32 per voltage coil)", o, "gtceu:thorium_plut_duranide_241_ingot"]
    - - g2
      - |-
        1 ruthenium · 2 trinium · 1 americium · 2 neutronium (dusts) · 8 B oxygen · circuit 4
      - g
      - functionalstorage:oak_1
      - - [Ruthenium dust, "gtceu:ruthenium_dust"]
        - [Trinium dust, "gtceu:trinium_dust"]
        - [Americium dust, "gtceu:americium_dust"]
        - [Neutronium dust, "gtceu:neutronium_dust"]
    - [m2, "UV Mixer · 20 s · 491 520 EU/t → 14 dust", m, "gtceu:uv_mixer"]
    - [e2, "EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils)", m, "gtceu:electric_blast_furnace"]
    - [f2, "Vacuum freezer · 10 s · 1 966 080 EU/t (Mega Vacuum Freezer)", m, "gtceu:mega_vacuum_freezer"]
    - [o2, "RTAN ingot → fine / single / double wire", o, "gtceu:ruthenium_trinium_americium_neutronate_ingot"]
  e:
    - [g1, m1, "8 dust"]
    - [m1, e1, "1 each"]
    - [e1, f1, hot ingot]
    - [g2, m2, "14 dust"]
    - [m2, e2, "1 each"]
    - [e2, f2, hot ingot]
    - [f2, o2, "1"]
  tips:
    - |-
      Thorium plutonium duranide 241 (kjs misc_materials.js mixer + startup abydos_alloys.js): UV mixer, circuit 4, 4 thorium + 1 duranium + 3 plutonium 241 dust → 8 dust, 1000 ticks at VA[UV] = 491 520 EU/t; blast data [10 199 K, gas highest, VA[UV], 850 ticks]; flags fine wire, foil. It is the wire of the UHV voltage coil (32 fine wire per coil, uhv_parts). Plutonium 241 comes from the reactor chain (Unverified), thorium from monazite (Unverified).
    - |-
      RTAN (gtsrc MixerRecipes + FirstDegreeMaterials, verified): mixer, circuit 4, 1 ruthenium + 2 trinium + 1 americium + 2 neutronium dust + 8 B oxygen → 14 dust, 400 ticks at VA[UV]; EBF 10 800 K at VA[ZPM] = 122 880 EU/t, 1000 ticks; vacuum freezer 200 ticks at VA[UHV] = 1 966 080 EU/t (cooling stats), cable V[UHV] 24 A, fine wire flag added by the pack. 10 800 K is exactly the tritanium coil: no other coil works. RTAN is the UHV fusion reactor wire, the UHV field generator wire (64 fine wire), the UHV hatch 2-wire and zalloy coil foils.
    - |-
      Americium and neutronium are made by the UV Fusion Reactor (uv_fusion_mats): per 14 dust batch 1 americium (144 mB) + 2 neutronium (288 mB), i.e. 1 americium run + 2 neutronium runs; ruthenium and trinium come from the platinum and naquadah lines. Oxygen is the 8 B per batch.
    - |-
      Freezer tier: RTAN’s freezing recipe is a 1.97 MEU/t recipe: only the Mega Vacuum Freezer on a UV 4A hatch (uv_multis) can run it; a plain vacuum freezer cannot. The same applies to many UHV hot ingots; get the Mega Vacuum Freezer early.
    - |-
      Sub-steps people skip: (1) oxygen is a fluid input of the mixer; (2) the EBF needs 10 800 K: 24 tritanium coils; (3) fine wire: a wiremill on the ingot, circuit 1; (4) separate UV mixers for TPD and RTAN (circuit 4 both).
    - |-
      Unverified: plutonium 241 and thorium supply, TPD freezing tier, gas usage of the highest-tier blasts.
  b:
    - ["gtceu:uv_mixer", 2]
    - ["gtceu:electric_blast_furnace", 2]
    - ["gtceu:mega_vacuum_freezer", 1]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:tritanium_coil_block", 24]
    - ["functionalstorage:oak_1", 12]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 3]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:thorium_dust", "gtceu:plutonium_241_dust", "gtceu:neutronium_dust"]
      t: |-
        Drawers first: thorium (4), duranium (1), plutonium 241 (3), ruthenium, trinium (2), americium, neutronium dust (2). Drum: oxygen. Output drawers for the ingots and wires.
    - i: ["gtceu:uv_mixer", "gtceu:thorium_plut_duranide_241_dust"]
      t: |-
        Mixer 1 (circuit 4): 8 dust per 50 s. Mixer 2 (circuit 4 + 8 B oxygen): 14 dust per 20 s.
    - i: ["gtceu:electric_blast_furnace", "gtceu:tritanium_coil_block"]
      t: |-
        Two EBFs with tritanium coils: TPD at 10 199 K (UV power), RTAN at 10 800 K (ZPM power). Hot ingots go to the freezer.
    - i: ["gtceu:mega_vacuum_freezer", "gtceu:ruthenium_trinium_americium_neutronate_ingot"]
      t: Mega Vacuum Freezer (UV 4A hatch) for RTAN; the TPD ingot can use a plain vacuum freezer at UV power (Unverified).
    - i: ["gtceu:lv_wiremill", "gtceu:fine_ruthenium_trinium_americium_neutronate_wire"]
      t: |-
        Wiremill circuit 1 for fine wire (RTAN fine wire needs the pack’s extra flag): the UHV field generator eats 64 per craft.
    - i: ["functionalstorage:oak_1", "gtceu:thorium_plut_duranide_241_ingot"]
      t: Output drawers Keep Exact 16 per metal.
---
# UHV superconductors: thorium plutonium duranide 241 (voltage coil wire) and ruthenium trinium americium neutronate (RTAN, UHV cable and fusion wire)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_sc` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Zapolgium, superconductors, alloys, void ingot](../../plan/p17.md#uhvmetals)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-uv" id="m-m1">
<div class="gt-head"><span class="gt-mname">UV Mixer · 50 s · 491 520 EU/t → 8 dust</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 thorium · 1 duranium · 3 plutonium 241 (dusts) · circuit 4 (functionalstorage:oak_1) - 8 dust"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 thorium · 1 duranium · 3 plutonium 241 (dusts) · circuit 4</span><span class="gt-sub"><span>Thorium dust</span><span>Duranium dust</span><span>Plutonium 241 dust</span></span><b class="gt-q">8 dust</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-e1" title="EBF 10 199 K · 42.5 s · 491 520 EU/t (tritanium coils) (gtceu:electric_blast_furnace) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 10 199 K · 42.5 s · 491 520 EU/t (tritanium coils)</span><b class="gt-q">1 each</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:uv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e1">
<div class="gt-head"><span class="gt-mname">EBF 10 199 K · 42.5 s · 491 520 EU/t (tritanium coils)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="UV Mixer · 50 s · 491 520 EU/t → 8 dust (gtceu:uv_mixer) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Mixer</span><span class="gt-note">UV Mixer · 50 s · 491 520 EU/t → 8 dust</span><b class="gt-q">1 each</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Vacuum freezer → ingot → fine wire (32 per voltage coil) (gtceu:thorium_plut_duranide_241_ingot) - hot ingot"><img class="gt-ico" src="../../assets/icons/gtceu__thorium_plut_duranide_241_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Thorium Plut Duranide 241 Ingot</span><span class="gt-note">Vacuum freezer → ingot → fine wire (32 per voltage coil)</span><b class="gt-q">hot ingot</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-uv" id="m-m2">
<div class="gt-head"><span class="gt-mname">UV Mixer · 20 s · 491 520 EU/t → 14 dust</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="1 ruthenium · 2 trinium · 1 americium · 2 neutronium (dusts) · 8 B oxygen · circuit 4 (functionalstorage:oak_1) - 14 dust"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 ruthenium · 2 trinium · 1 americium · 2 neutronium (dusts) · 8 B oxygen · circuit 4</span><span class="gt-sub"><span>Ruthenium dust</span><span>Trinium dust</span><span>Americium dust</span><span>Neutronium dust</span></span><b class="gt-q">14 dust</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-e2" title="EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils) (gtceu:electric_blast_furnace) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils)</span><b class="gt-q">1 each</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:uv_mixer</code></div>
</div>
<div class="gt-panel t-multi" id="m-e2">
<div class="gt-head"><span class="gt-mname">EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="UV Mixer · 20 s · 491 520 EU/t → 14 dust (gtceu:uv_mixer) - 1 each"><img class="gt-ico" src="../../assets/icons/gtceu__uv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Mixer</span><span class="gt-note">UV Mixer · 20 s · 491 520 EU/t → 14 dust</span><b class="gt-q">1 each</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-f2" title="Vacuum freezer · 10 s · 1 966 080 EU/t (Mega Vacuum Freezer) (gtceu:mega_vacuum_freezer) - hot ingot"><img class="gt-ico" src="../../assets/icons/gtceu__mega_vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mega Vacuum Freezer</span><span class="gt-note">Vacuum freezer · 10 s · 1 966 080 EU/t (Mega Vacuum Freezer)</span><b class="gt-q">hot ingot</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-f2">
<div class="gt-head"><span class="gt-mname">Vacuum freezer · 10 s · 1 966 080 EU/t (Mega Vacuum Freezer)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-e2" title="EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils) (gtceu:electric_blast_furnace) - hot ingot"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Electric Blast Furnace</span><span class="gt-note">EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils)</span><b class="gt-q">hot ingot</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mega_vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="RTAN ingot → fine / single / double wire (gtceu:ruthenium_trinium_americium_neutronate_ingot) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_trinium_americium_neutronate_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Trinium Americium Neutronate Ingot</span><span class="gt-note">RTAN ingot → fine / single / double wire</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mega_vacuum_freezer</code></div>
</div>
</div>

## Flow

- [UV Mixer · 50 s · 491 520 EU/t → 8 dust](#m-m1) → [EBF 10 199 K · 42.5 s · 491 520 EU/t (tritanium coils)](#m-e1)
- [UV Mixer · 20 s · 491 520 EU/t → 14 dust](#m-m2) → [EBF 10 800 K · 50 s · 122 880 EU/t (tritanium coils)](#m-e2) → [Vacuum freezer · 10 s · 1 966 080 EU/t (Mega Vacuum Freezer)](#m-f2)

## How to build

1. Drawers first: thorium (4), duranium (1), plutonium 241 (3), ruthenium, trinium (2), americium, neutronium dust (2). Drum: oxygen. Output drawers for the ingots and wires. — `functionalstorage:oak_1`, `gtceu:thorium_dust`, `gtceu:plutonium_241_dust`, `gtceu:neutronium_dust`
2. Mixer 1 (circuit 4): 8 dust per 50 s. Mixer 2 (circuit 4 + 8 B oxygen): 14 dust per 20 s. — `gtceu:uv_mixer`, `gtceu:thorium_plut_duranide_241_dust`
3. Two EBFs with tritanium coils: TPD at 10 199 K (UV power), RTAN at 10 800 K (ZPM power). Hot ingots go to the freezer. — `gtceu:electric_blast_furnace`, `gtceu:tritanium_coil_block`
4. Mega Vacuum Freezer (UV 4A hatch) for RTAN; the TPD ingot can use a plain vacuum freezer at UV power (Unverified). — `gtceu:mega_vacuum_freezer`, `gtceu:ruthenium_trinium_americium_neutronate_ingot`
5. Wiremill circuit 1 for fine wire (RTAN fine wire needs the pack’s extra flag): the UHV field generator eats 64 per craft. — `gtceu:lv_wiremill`, `gtceu:fine_ruthenium_trinium_americium_neutronate_wire`
6. Output drawers Keep Exact 16 per metal. — `functionalstorage:oak_1`, `gtceu:thorium_plut_duranide_241_ingot`

## Tips

- Thorium plutonium duranide 241 (kjs misc\_materials.js mixer + startup abydos\_alloys.js): UV mixer, circuit 4, 4 thorium + 1 duranium + 3 plutonium 241 dust → 8 dust, 1000 ticks at VA\[UV\] = 491 520 EU/t; blast data \[10 199 K, gas highest, VA\[UV\], 850 ticks\]; flags fine wire, foil. It is the wire of the UHV voltage coil (32 fine wire per coil, uhv\_parts). Plutonium 241 comes from the reactor chain (Unverified), thorium from monazite (Unverified).
- RTAN (gtsrc MixerRecipes + FirstDegreeMaterials, verified): mixer, circuit 4, 1 ruthenium + 2 trinium + 1 americium + 2 neutronium dust + 8 B oxygen → 14 dust, 400 ticks at VA\[UV\]; EBF 10 800 K at VA\[ZPM\] = 122 880 EU/t, 1000 ticks; vacuum freezer 200 ticks at VA\[UHV\] = 1 966 080 EU/t (cooling stats), cable V\[UHV\] 24 A, fine wire flag added by the pack. 10 800 K is exactly the tritanium coil: no other coil works. RTAN is the UHV fusion reactor wire, the UHV field generator wire (64 fine wire), the UHV hatch 2-wire and zalloy coil foils.
- Americium and neutronium are made by the UV Fusion Reactor (uv\_fusion\_mats): per 14 dust batch 1 americium (144 mB) + 2 neutronium (288 mB), i.e. 1 americium run + 2 neutronium runs; ruthenium and trinium come from the platinum and naquadah lines. Oxygen is the 8 B per batch.
- Freezer tier: RTAN’s freezing recipe is a 1.97 MEU/t recipe: only the Mega Vacuum Freezer on a UV 4A hatch (uv\_multis) can run it; a plain vacuum freezer cannot. The same applies to many UHV hot ingots; get the Mega Vacuum Freezer early.
- Sub-steps people skip: (1) oxygen is a fluid input of the mixer; (2) the EBF needs 10 800 K: 24 tritanium coils; (3) fine wire: a wiremill on the ingot, circuit 1; (4) separate UV mixers for TPD and RTAN (circuit 4 both).
- **Unverified** plutonium 241 and thorium supply, TPD freezing tier, gas usage of the highest-tier blasts.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:uv_mixer` | 2 |
| `gtceu:electric_blast_furnace` | 2 |
| `gtceu:mega_vacuum_freezer` | 1 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:tritanium_coil_block` | 24 |
| `functionalstorage:oak_1` | 12 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 3 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Main source for:** `gtceu:ruthenium_trinium_americium_neutronate_ingot`, `gtceu:fine_ruthenium_trinium_americium_neutronate_wire`, `gtceu:thorium_plut_duranide_241_ingot`, `gtceu:fine_thorium_plut_duranide_241_wire`
