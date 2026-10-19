---
kind: chain
id: mv_diode
order: 990
data:
  t: Diodes (gallium arsenide + glass + fine wire)
  inf: true
  "n":
    - [gs, Gallium arsenide dust, i, "gtceu:gallium_arsenide_dust"]
    - [pk, "LV Packer · circuit 2", m, "gtceu:lv_packer"]
    - [sd, "1 Small gallium arsenide dust", x, "gtceu:small_gallium_arsenide_dust"]
    - [sn, Glass dust, i, "gtceu:glass_dust"]
    - [fu, Kiln or furnace, m, "minecraft:furnace"]
    - [gb, Glass, i, "minecraft:glass"]
    - [ex, LV Extractor, m, "gtceu:lv_extractor"]
    - [mg, "Molten glass 144 mB (gtceu:glass)", f, "gtceu:glass_bucket"]
    - [fw, "4 Fine copper wire", i, "gtceu:fine_copper_wire"]
    - [as, "Assembler · 20 s", m, "gtceu:lv_assembler"]
    - [di, Diode, o, "gtceu:diode"]
  e:
    - [gs, pk, "1"]
    - [pk, sd, "1 → 4"]
    - [sn, fu]
    - [fu, gb]
    - [gb, ex]
    - [ex, mg, "144 mB"]
    - [sd, as, "1"]
    - [fw, as, "4"]
    - [mg, as, "144 mB"]
    - [as, di, "1 / 20 s"]
  tips:
    - |-
      Each assembler makes 3 diodes a minute and one MV circuit needs 2, so a circuit assembler (4 MV circuits a minute) eats 8 diodes a minute: build 3 diode assemblers feeding the same drawer.
    - Annealed copper wire (arc furnace) doubles the output to 2 diodes per craft even with glass. With polyethylene instead of glass it is also 2 (4 with annealed wire).
    - |-
      Fine copper wire comes from the wires line (wiremill circuit 3: 1 copper → 8).
  b:
    - ["gtceu:lv_assembler", 3]
    - ["gtceu:lv_packer", 1]
    - ["gtceu:lv_extractor", 1]
    - ["minecraft:furnace", 1]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["functionalstorage:oak_1", 9]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
  how:
    - i: ["gtceu:lv_packer", "gtceu:small_gallium_arsenide_dust"]
      t: |-
        Small dust: put 1 gallium arsenide dust alone in the crafting grid for 4 small dust, or automate it with an LV Packer on ghost circuit 2 (1 dust → 4 small dust).
    - i: ["minecraft:furnace", "minecraft:glass", "gtceu:lv_extractor", "gtceu:glass_bucket"]
      t: |-
        Glass: make glass dust (quartz sand dust from sand in a macerator, plus tiny flint dust, shapeless in the grid), bake it into a glass block (Kiln 30 ticks, or a campfire), then an LV Extractor turns the block into 144 mB molten glass (fluid gtceu:glass). That last extractor recipe is GregTech’s automatic recycling (yield 1.0 in gtceu.yaml, about 3 s at 30 EU/t) and is not in the local dumps: confirm in EMI. A drum holds it; 1 diode = 144 mB.
    - i: ["gtceu:lv_assembler", "gtceu:diode"]
      t: |-
        Three LV Assemblers on the same recipe (no circuit): 4 fine copper wire + 1 small gallium arsenide dust + 144 mB molten glass → 1 diode in 20 s (30 EU/t). One shared input drawer per ingredient, one shared output drawer; Robot Arm cover on Keep Exact 64.
---
# Diodes (gallium arsenide + glass + fine wire)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `mv_diode` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Diodes](../../plan/p6.md#diodes)

**Tips:** 3

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-pk">
<div class="gt-head"><span class="gt-mname">LV Packer · circuit 2</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Gallium arsenide dust (gtceu:gallium_arsenide_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__gallium_arsenide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gallium Arsenide Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_packer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="1 Small gallium arsenide dust (gtceu:small_gallium_arsenide_dust) - 1 → 4"><img class="gt-ico" src="../../assets/icons/gtceu__small_gallium_arsenide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Gallium Arsenide Dust</span><span class="gt-note">1 Small gallium arsenide dust</span><b class="gt-q">1 → 4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_packer</code></div>
</div>
<div class="gt-panel t-mod" id="m-fu">
<div class="gt-head"><span class="gt-mname">Kiln or furnace</span><span class="gt-badge t-mod">Vanilla</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Glass dust (gtceu:glass_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__glass_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/minecraft__furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Glass (minecraft:glass)"><img class="gt-ico" src="../../assets/icons/minecraft__glass.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass</span></span></div>
</div>
<div class="gt-foot"><code>minecraft:furnace</code></div>
</div>
<div class="gt-panel t-lv" id="m-ex">
<div class="gt-head"><span class="gt-mname">LV Extractor</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Glass (minecraft:glass)"><img class="gt-ico" src="../../assets/icons/minecraft__glass.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_extractor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Molten glass 144 mB (gtceu:glass) (gtceu:glass_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glass_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass</span><span class="gt-note">Molten glass 144 mB (gtceu:glass)</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_extractor</code></div>
</div>
<div class="gt-panel t-lv" id="m-as">
<div class="gt-head"><span class="gt-mname">Assembler · 20 s</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Small gallium arsenide dust (gtceu:small_gallium_arsenide_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__small_gallium_arsenide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Small Gallium Arsenide Dust</span><span class="gt-note">1 Small gallium arsenide dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="4 Fine copper wire (gtceu:fine_copper_wire) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__fine_copper_wire.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fine Copper Wire</span><span class="gt-note">4 Fine copper wire</span><b class="gt-q">4</b></span><span class="gt-slot gt-fluid" title="Molten glass 144 mB (gtceu:glass) (gtceu:glass_bucket) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__glass_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Glass</span><span class="gt-note">Molten glass 144 mB (gtceu:glass)</span><b class="gt-q">144 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_assembler.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Diode (gtceu:diode) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/gtceu__diode.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Diode</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_assembler</code></div>
</div>
</div>

## Flow

- [LV Packer · circuit 2](#m-pk) → [Assembler · 20 s](#m-as)
- [Kiln or furnace](#m-fu) → [LV Extractor](#m-ex) → [Assembler · 20 s](#m-as)

## How to build

1. Small dust: put 1 gallium arsenide dust alone in the crafting grid for 4 small dust, or automate it with an LV Packer on ghost circuit 2 (1 dust → 4 small dust). — `gtceu:lv_packer`, `gtceu:small_gallium_arsenide_dust`
2. Glass: make glass dust (quartz sand dust from sand in a macerator, plus tiny flint dust, shapeless in the grid), bake it into a glass block (Kiln 30 ticks, or a campfire), then an LV Extractor turns the block into 144 mB molten glass (fluid gtceu:glass). That last extractor recipe is GregTech’s automatic recycling (yield 1.0 in gtceu.yaml, about 3 s at 30 EU/t) and is not in the local dumps: confirm in EMI. A drum holds it; 1 diode = 144 mB. — `minecraft:furnace`, `minecraft:glass`, `gtceu:lv_extractor`, `gtceu:glass_bucket`
3. Three LV Assemblers on the same recipe (no circuit): 4 fine copper wire + 1 small gallium arsenide dust + 144 mB molten glass → 1 diode in 20 s (30 EU/t). One shared input drawer per ingredient, one shared output drawer; Robot Arm cover on Keep Exact 64. — `gtceu:lv_assembler`, `gtceu:diode`

## Tips

- Each assembler makes 3 diodes a minute and one MV circuit needs 2, so a circuit assembler (4 MV circuits a minute) eats 8 diodes a minute: build 3 diode assemblers feeding the same drawer.
- Annealed copper wire (arc furnace) doubles the output to 2 diodes per craft even with glass. With polyethylene instead of glass it is also 2 (4 with annealed wire).
- Fine copper wire comes from the wires line (wiremill circuit 3: 1 copper → 8).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_assembler` | 3 |
| `gtceu:lv_packer` | 1 |
| `gtceu:lv_extractor` | 1 |
| `minecraft:furnace` | 1 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `functionalstorage:oak_1` | 9 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |

## Needs / Feeds

- **Needs:** [Gallium arsenide (sphalerite + realgar)](mv_gaas.md), [Infinite gems (sand sieve)](../feeders/sieve_sand.md), [Parts row 2: wires, fine wire, cables](../lv/comp_wires.md)
- **Feeds:** [MV circuit line (Good Electronic Circuit)](mv_circuit.md)
- **Main source for:** `gtceu:small_gallium_arsenide_dust`, `gtceu:diode`
