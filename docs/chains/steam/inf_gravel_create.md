---
kind: chain
id: inf_gravel_create
order: 60
data:
  t: Infinite gravel (Create)
  inf: true
  "n":
    - [sb, Stone Barrel, s, "gtceu:stone_barrel"]
    - [c, Cobblestone, x, "minecraft:cobblestone"]
    - [ch, Smart Chute, m, "create:smart_chute"]
    - [cw, Crushing Wheels, m, "create:crushing_wheel"]
    - [wm, Windmill, p, "create:windmill_bearing"]
    - [g, Gravel, o, "minecraft:gravel"]
    - [dr, Drawer, o, "functionalstorage:oak_1"]
  e: [[sb, c], [c, ch, stacks], [ch, cw], [wm, cw, SU], [cw, g], [g, dr]]
  tips:
    - Crushing wheels take a whole stack at once — feed with a smart chute.
    - "LV Forge Hammer: gravel → sand → dust."
  store: ["functionalstorage:oak_1"]
  b: [["create:crushing_wheel", 2], ["create:smart_chute", 1], ["create:shaft", 4], ["functionalstorage:oak_1", 1]]
  how:
    - i: ["gtceu:stone_barrel", "functionalstorage:oak_1"]
      t: Stone Barrels fill a drawer with cobble (see Infinite cobble).
    - i: ["create:smart_chute", "create:brass_funnel"]
      t: A Smart Chute or Brass Funnel drops full stacks on top of the wheels — crushing wheels process a whole stack at once.
    - i: ["create:crushing_wheel"]
      t: Two Crushing Wheels side by side rotating inward (reverse one with a gear). 8 SU/RPM each.
    - i: ["create:chute", "functionalstorage:oak_1"]
      t: Gravel falls below into a chute → drawer, or straight into the Mechanical Sieve’s input bus.
  calc:
    rpm: 128
    windmills: 1
    sails: 128
    mag:
      magnetite: 0
      redstone: 0
      layered: 0
      fluxuated: 0
      netherite: 0
    wheels: 2
    coils: 0
    euNeed: 0
---
# Infinite gravel (Create)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `inf_gravel_create` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Sieve block (4 sieves)](../../plan/p2.md#sieves)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-ch">
<div class="gt-head"><span class="gt-mname">Smart Chute</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Cobblestone (minecraft:cobblestone) - stacks"><img class="gt-ico" src="../../assets/icons/minecraft__cobblestone.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobblestone</span><b class="gt-q">stacks</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__smart_chute.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cw" title="Crushing Wheels (create:crushing_wheel)"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushing Wheel</span><span class="gt-note">Crushing Wheels</span></a></div>
</div>
<div class="gt-foot"><code>create:smart_chute</code></div>
</div>
<div class="gt-panel t-mod" id="m-cw">
<div class="gt-head"><span class="gt-mname">Crushing Wheels</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-ch" title="Smart Chute (create:smart_chute)"><img class="gt-ico" src="../../assets/icons/create__smart_chute.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Smart Chute</span></a><a class="gt-slot gt-power" href="#m-wm" title="Windmill (create:windmill_bearing) - SU"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Windmill Bearing</span><b class="gt-q">SU</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Gravel (minecraft:gravel)"><img class="gt-ico" src="../../assets/icons/minecraft__gravel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Gravel</span></span></div>
</div>
<div class="gt-foot"><code>create:crushing_wheel</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-cw" title="Crushing Wheels (create:crushing_wheel) - SU"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushing Wheel</span><span class="gt-note">Crushing Wheels</span><b class="gt-q">SU</b></a></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
</div>

## Flow

- [Smart Chute](#m-ch) → [Crushing Wheels](#m-cw)
- [Windmill](#m-wm) → [Crushing Wheels](#m-cw)

### Direct steps

- Stone Barrel → Cobblestone
- Gravel → Drawer

## How to build

1. Stone Barrels fill a drawer with cobble (see Infinite cobble). — `gtceu:stone_barrel`, `functionalstorage:oak_1`
2. A Smart Chute or Brass Funnel drops full stacks on top of the wheels — crushing wheels process a whole stack at once. — `create:smart_chute`, `create:brass_funnel`
3. Two Crushing Wheels side by side rotating inward (reverse one with a gear). 8 SU/RPM each. — `create:crushing_wheel`
4. Gravel falls below into a chute → drawer, or straight into the Mechanical Sieve’s input bus. — `create:chute`, `functionalstorage:oak_1`

## Tips

- Crushing wheels take a whole stack at once — feed with a smart chute.
- LV Forge Hammer: gravel → sand → dust.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:crushing_wheel` | 2 |
| `create:smart_chute` | 1 |
| `create:shaft` | 4 |
| `functionalstorage:oak_1` | 1 |

## Storage

`functionalstorage:oak_1`

## Extras

- Power calculator defaults are stored in the front matter (`calc`).
