---
kind: chain
id: charcoal_pile
order: 620
data:
  t: "Charcoal: Charcoal Pile Igniter"
  inf: false
  "n":
    - [lg, "Logs (filled pit)", i, "minecraft:oak_log"]
    - [pi, Charcoal Pile Igniter, m, "gtceu:charcoal_pile_igniter"]
    - [bc, Brittle Charcoal blocks, x, "gtceu:brittle_charcoal"]
    - [ch, Charcoal, o, "minecraft:charcoal"]
  e: [[lg, pi, ignite], [pi, bc, burns], [bc, ch, mine]]
  tips:
    - |-
      Big batch with no power: fill a pit of logs, walls of bricks, cover with dirt, ignite.
    - Must be mined by hand (or a Create drill), so it is not fully automatic.
  b: [["gtceu:charcoal_pile_igniter", 1], ["minecraft:flint_and_steel", 1]]
---
# Charcoal: Charcoal Pile Igniter

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `charcoal_pile`

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-pi">
<div class="gt-head"><span class="gt-mname">Charcoal Pile Igniter</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Logs (filled pit) (minecraft:oak_log) - ignite"><img class="gt-ico" src="../../assets/icons/minecraft__oak_log.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak Log</span><span class="gt-note">Logs (filled pit)</span><b class="gt-q">ignite</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__charcoal_pile_igniter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Brittle Charcoal blocks (gtceu:brittle_charcoal) - burns"><img class="gt-ico" src="../../assets/icons/gtceu__brittle_charcoal.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Brittle Charcoal</span><span class="gt-note">Brittle Charcoal blocks</span><b class="gt-q">burns</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:charcoal_pile_igniter</code></div>
</div>
</div>

## Flow

- [Charcoal Pile Igniter](#m-pi)

### Direct steps

- Brittle Charcoal blocks → Charcoal (mine)

## Tips

- Big batch with no power: fill a pit of logs, walls of bricks, cover with dirt, ignite.
- Must be mined by hand (or a Create drill), so it is not fully automatic.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:charcoal_pile_igniter` | 1 |
| `minecraft:flint_and_steel` | 1 |

## Needs / Feeds

- **Needs:** [Create tree farm (rotating saws + deployers)](../steam/tree_farm.md)
