---
kind: chain
id: tree_farm
order: 410
data:
  t: Create tree farm (rotating saws + deployers)
  inf: true
  hero: true
  "n":
    - [wm, Windmill, p, "create:windmill_bearing"]
    - [mb, Mechanical Bearing arm, m, "create:mechanical_bearing"]
    - [dp, "Deployers · saplings + bone meal", m, "create:deployer"]
    - [tr, Trees grow, x, "minecraft:oak_sapling"]
    - [sw, Mechanical Saws, m, "create:mechanical_saw"]
    - [ch, Chest on the arm, x, "minecraft:chest"]
    - [psi, Portable Storage Interface, m, "create:portable_storage_interface"]
    - [lg, Logs, o, "minecraft:oak_log"]
    - [sp, "Saplings (refill arm)", o, "minecraft:oak_sapling"]
    - [ap, "Apples / sticks", o, "minecraft:apple"]
  e:
    - [wm, mb, SU]
    - [mb, dp, sweeps]
    - [dp, tr, plant]
    - [tr, sw, grown]
    - [mb, sw]
    - [sw, ch, drops]
    - [ch, psi, docks]
    - [psi, lg]
    - [psi, sp]
    - [psi, ap]
  tips:
    - Ring of dirt around the bearing; saws and deployers on the rotating arm.
    - Saw drops go straight into storage mounted on the contraption.
    - Feed leftover saplings to an Advanced Composter → bone meal → deployers.
    - Same build with jungle saplings = rubber trees.
  store: ["functionalstorage:oak_1"]
  b:
    - ["create:windmill_bearing", 1]
    - ["create:white_sail", 16]
    - ["create:mechanical_bearing", 1]
    - ["create:radial_chassis", 6]
    - ["create:super_glue", 1]
    - ["create:mechanical_saw", 4]
    - ["create:deployer", 4]
    - ["minecraft:chest", 1]
    - ["create:portable_storage_interface", 2]
    - ["functionalstorage:oak_1", 3]
    - ["minecraft:dirt", 16]
  how:
    - i: ["minecraft:dirt"]
      t: Lay a ring of dirt (radius 4–6) around the spot for the bearing. Leave 7+ blocks of air above for the trees.
    - i: ["create:mechanical_bearing", "create:radial_chassis", "create:super_glue"]
      t: A Mechanical Bearing in the centre facing up, with an arm of Radial Chassis glued together that reaches over the dirt ring.
    - i: ["create:deployer", "minecraft:oak_sapling"]
      t: Deployers facing down along the arm hold saplings and plant them as they sweep. A second row holding Bone Meal speeds the growth.
    - i: ["create:mechanical_saw"]
      t: Mechanical Saws on the arm, facing the direction of rotation at trunk height. A saw on a contraption fells the whole tree.
    - i: ["minecraft:chest"]
      t: |-
        A chest on the arm: saw drops go straight into it, and deployers refill saplings from it.
    - i: ["create:portable_storage_interface", "functionalstorage:oak_1"]
      t: |-
        A Portable Storage Interface on the arm plus a fixed one at the dock: each pass, logs and apples go to the drawers and saplings come back.
    - i: ["create:windmill_bearing"]
      t: Run the bearing slowly (2–8 RPM) from the windmill line so the deployers have time to plant.
---
# Create tree farm (rotating saws + deployers)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `tree_farm` · **Tags:** Infinite source, Hero build

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Wood farm](../../plan/p1.md#wood)

**Tips:** 4

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-mb" title="Mechanical Bearing arm (create:mechanical_bearing) - SU"><img class="gt-ico" src="../../assets/icons/create__mechanical_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Bearing</span><span class="gt-note">Mechanical Bearing arm</span><b class="gt-q">SU</b></a></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
<div class="gt-panel t-mod" id="m-mb">
<div class="gt-head"><span class="gt-mname">Mechanical Bearing arm</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-power" href="#m-wm" title="Windmill (create:windmill_bearing) - SU"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Windmill Bearing</span><b class="gt-q">SU</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-dp" title="Deployers · saplings + bone meal (create:deployer) - sweeps"><img class="gt-ico" src="../../assets/icons/create__deployer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Deployer</span><span class="gt-note">Deployers · saplings + bone meal</span><b class="gt-q">sweeps</b></a><a class="gt-slot gt-mach" href="#m-sw" title="Mechanical Saws (create:mechanical_saw)"><img class="gt-ico" src="../../assets/icons/create__mechanical_saw.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Saw</span><span class="gt-note">Mechanical Saws</span></a></div>
</div>
<div class="gt-foot"><code>create:mechanical_bearing</code></div>
</div>
<div class="gt-panel t-mod" id="m-dp">
<div class="gt-head"><span class="gt-mname">Deployers · saplings + bone meal</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-mb" title="Mechanical Bearing arm (create:mechanical_bearing) - sweeps"><img class="gt-ico" src="../../assets/icons/create__mechanical_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Bearing</span><span class="gt-note">Mechanical Bearing arm</span><b class="gt-q">sweeps</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__deployer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Trees grow (minecraft:oak_sapling) - plant"><img class="gt-ico" src="../../assets/icons/minecraft__oak_sapling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Sapling</span><span class="gt-note">Trees grow</span><b class="gt-q">plant</b></span></div>
</div>
<div class="gt-foot"><code>create:deployer</code></div>
</div>
<div class="gt-panel t-mod" id="m-sw">
<div class="gt-head"><span class="gt-mname">Mechanical Saws</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Trees grow (minecraft:oak_sapling) - grown"><img class="gt-ico" src="../../assets/icons/minecraft__oak_sapling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Sapling</span><span class="gt-note">Trees grow</span><b class="gt-q">grown</b></span><a class="gt-slot gt-mach" href="#m-mb" title="Mechanical Bearing arm (create:mechanical_bearing)"><img class="gt-ico" src="../../assets/icons/create__mechanical_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mechanical Bearing</span><span class="gt-note">Mechanical Bearing arm</span></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_saw.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Chest on the arm (minecraft:chest) - drops"><img class="gt-ico" src="../../assets/icons/minecraft__chest.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chest</span><span class="gt-note">Chest on the arm</span><b class="gt-q">drops</b></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_saw</code></div>
</div>
<div class="gt-panel t-mod" id="m-psi">
<div class="gt-head"><span class="gt-mname">Portable Storage Interface</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chest on the arm (minecraft:chest) - docks"><img class="gt-ico" src="../../assets/icons/minecraft__chest.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chest</span><span class="gt-note">Chest on the arm</span><b class="gt-q">docks</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__portable_storage_interface.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Logs (minecraft:oak_log)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs</span></span><span class="gt-slot gt-outp" title="Saplings (refill arm) (minecraft:oak_sapling)"><img class="gt-ico" src="../../assets/icons/minecraft__oak_sapling.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Sapling</span><span class="gt-note">Saplings (refill arm)</span></span><span class="gt-slot gt-outp" title="Apples / sticks (minecraft:apple)"><img class="gt-ico" src="../../assets/icons/minecraft__apple.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Apple</span><span class="gt-note">Apples / sticks</span></span></div>
</div>
<div class="gt-foot"><code>create:portable_storage_interface</code></div>
</div>
</div>

## Flow

- [Windmill](#m-wm) → [Mechanical Bearing arm](#m-mb) → [Deployers · saplings + bone meal](#m-dp) → [Mechanical Saws](#m-sw) → [Portable Storage Interface](#m-psi) (also Mechanical Bearing arm → [Mechanical Saws](#m-sw))

## How to build

1. Lay a ring of dirt (radius 4–6) around the spot for the bearing. Leave 7+ blocks of air above for the trees. — `minecraft:dirt`
2. A Mechanical Bearing in the centre facing up, with an arm of Radial Chassis glued together that reaches over the dirt ring. — `create:mechanical_bearing`, `create:radial_chassis`, `create:super_glue`
3. Deployers facing down along the arm hold saplings and plant them as they sweep. A second row holding Bone Meal speeds the growth. — `create:deployer`, `minecraft:oak_sapling`
4. Mechanical Saws on the arm, facing the direction of rotation at trunk height. A saw on a contraption fells the whole tree. — `create:mechanical_saw`
5. A chest on the arm: saw drops go straight into it, and deployers refill saplings from it. — `minecraft:chest`
6. A Portable Storage Interface on the arm plus a fixed one at the dock: each pass, logs and apples go to the drawers and saplings come back. — `create:portable_storage_interface`, `functionalstorage:oak_1`
7. Run the bearing slowly (2–8 RPM) from the windmill line so the deployers have time to plant. — `create:windmill_bearing`

## Tips

- Ring of dirt around the bearing; saws and deployers on the rotating arm.
- Saw drops go straight into storage mounted on the contraption.
- Feed leftover saplings to an Advanced Composter → bone meal → deployers.
- Same build with jungle saplings = rubber trees.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:windmill_bearing` | 1 |
| `create:white_sail` | 16 |
| `create:mechanical_bearing` | 1 |
| `create:radial_chassis` | 6 |
| `create:super_glue` | 1 |
| `create:mechanical_saw` | 4 |
| `create:deployer` | 4 |
| `minecraft:chest` | 1 |
| `create:portable_storage_interface` | 2 |
| `functionalstorage:oak_1` | 3 |
| `minecraft:dirt` | 16 |

## Storage

`functionalstorage:oak_1`

## Needs / Feeds

- **Feeds:** [Methane &amp; wood chemicals](../mv/wood_gas.md), [LV circuit parts from earlier lines](../feeders/circuit_parts.md), [Charcoal: Create fan smelting](charcoal_fan.md), [Charcoal: Pyrolyse Oven](../feeders/charcoal_pyro.md), [Charcoal: Charcoal Pile Igniter](../feeders/charcoal_pile.md), [Treated wood: cutter + spout](../lv/treated_wood.md)
- **Main source for:** `minecraft:oak_log`, `minecraft:jungle_sapling`
