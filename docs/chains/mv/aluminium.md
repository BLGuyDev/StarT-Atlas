---
kind: chain
id: aluminium
order: 180
data:
  t: Infinite aluminium (clay)
  inf: true
  "n":
    - [d, Sieve dust, s, "exnihilosequentia:dust"]
    - [b, "Barrel + water", m, "gtceu:barrel"]
    - [cl, Clay, x, "minecraft:clay"]
    - [mc, Macerator, m, "gtceu:mv_macerator"]
    - [cd, Clay Dust, x, "gtceu:clay_dust"]
    - [el, Electrolyzer, m, "gtceu:mv_electrolyzer"]
    - [al, Aluminium dust, x, "gtceu:aluminium_dust"]
    - [si, Silicon dust, o, "gtceu:silicon_dust"]
    - [na, "Sodium + Lithium", o, "gtceu:sodium_dust"]
    - [ebf, EBF, m, "gtceu:electric_blast_furnace"]
    - [ai, Aluminium, o, "gtceu:aluminium_ingot"]
  e: [[d, b], [b, cl], [cl, mc], [mc, cd], [cd, el], [el, al], [el, si], [el, na], [al, ebf, "1700 K"], [ebf, ai]]
  tips:
    - |-
      Other aluminium sources: sodalite (11 dust → 3 aluminium + 3 silicon, 30 EU/t) and sapphire or ruby gems. The MV hull needs it (8 plates per casing).
    - Silicon feeds the boule line.
  b:
    - ["gtceu:barrel", 2]
    - ["gtceu:mv_macerator", 1]
    - ["gtceu:mv_electrolyzer", 2]
    - ["gtceu:electric_blast_furnace", 1]
  how:
    - i: ["exnihilosequentia:dust", "gtceu:barrel"]
      t: Dust from the hammer line + water in Barrels (transformation mode) → clay blocks.
    - i: ["gtceu:mv_macerator", "gtceu:clay_dust"]
      t: Macerate clay → clay dust.
    - i: ["gtceu:mv_electrolyzer"]
      t: |-
        MV Electrolyzer: clay dust → aluminium, silicon, sodium, lithium dust + water.
    - i: ["gtceu:electric_blast_furnace", "gtceu:aluminium_ingot"]
      t: |-
        EBF (1 700 K, 120 EU/t, cupronickel coils are enough) → aluminium ingots. MV casings need them first: 8 plates each.
---
# Infinite aluminium (clay)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `aluminium` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Aluminium ingots](../../plan/p5.md#aluminium)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-b">
<div class="gt-head"><span class="gt-mname">Barrel + water</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Sieve dust (exnihilosequentia:dust)"><img class="gt-ico" src="../../assets/icons/exnihilosequentia__dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Dust</span><span class="gt-note">Sieve dust</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__barrel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Clay (minecraft:clay)"><img class="gt-ico" src="../../assets/icons/minecraft__clay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Clay</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:barrel</code></div>
</div>
<div class="gt-panel t-mv" id="m-mc">
<div class="gt-head"><span class="gt-mname">Macerator</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Clay (minecraft:clay)"><img class="gt-ico" src="../../assets/icons/minecraft__clay.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Clay</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_macerator.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Clay Dust (gtceu:clay_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__clay_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Clay Dust</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_macerator</code></div>
</div>
<div class="gt-panel t-mv" id="m-el">
<div class="gt-head"><span class="gt-mname">Electrolyzer</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Clay Dust (gtceu:clay_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__clay_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Clay Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Aluminium dust (gtceu:aluminium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Dust</span></span><span class="gt-slot gt-outp" title="Silicon dust (gtceu:silicon_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__silicon_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Silicon Dust</span></span><span class="gt-slot gt-outp" title="Sodium + Lithium (gtceu:sodium_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__sodium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sodium Dust</span><span class="gt-note">Sodium + Lithium</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_electrolyzer</code></div>
</div>
<div class="gt-panel t-multi" id="m-ebf">
<div class="gt-head"><span class="gt-mname">EBF</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Aluminium dust (gtceu:aluminium_dust) - 1700 K"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Dust</span><b class="gt-q">1700 K</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Aluminium (gtceu:aluminium_ingot)"><img class="gt-ico" src="../../assets/icons/gtceu__aluminium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aluminium Ingot</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
</div>

## Flow

- [Barrel + water](#m-b) → [Macerator](#m-mc) → [Electrolyzer](#m-el) → [EBF](#m-ebf)

## How to build

1. Dust from the hammer line + water in Barrels (transformation mode) → clay blocks. — `exnihilosequentia:dust`, `gtceu:barrel`
2. Macerate clay → clay dust. — `gtceu:mv_macerator`, `gtceu:clay_dust`
3. MV Electrolyzer: clay dust → aluminium, silicon, sodium, lithium dust + water. — `gtceu:mv_electrolyzer`
4. EBF (1 700 K, 120 EU/t, cupronickel coils are enough) → aluminium ingots. MV casings need them first: 8 plates each. — `gtceu:electric_blast_furnace`, `gtceu:aluminium_ingot`

## Tips

- Other aluminium sources: sodalite (11 dust → 3 aluminium + 3 silicon, 30 EU/t) and sapphire or ruby gems. The MV hull needs it (8 plates per casing).
- Silicon feeds the boule line.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:barrel` | 2 |
| `gtceu:mv_macerator` | 1 |
| `gtceu:mv_electrolyzer` | 2 |
| `gtceu:electric_blast_furnace` | 1 |

## Needs / Feeds

- **Needs:** [Infinite redstone, sulfur &amp; pearls (dust sieve)](../feeders/sieve_dust.md)
- **Feeds:** [Silicon wafers &amp; chips](wafer.md), [First MV hull and the LV → MV transformer](mv_hull.md), [MV components on LV machines](comp_mv.md), [Kanthal: MV Mixer, HV EBF, chemical bath, wire, spring and coil block](../hv/kanthal.md), [Nichrome: MV Mixer, EV EBF at 2700 K, Vacuum Freezer, wire and coil block](../ev/nichrome_line.md)
- **Main source for:** `gtceu:silicon_dust`, `gtceu:sodium_dust`, `gtceu:aluminium_ingot`
