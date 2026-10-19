---
kind: chain
id: uhv_gate
order: 2250
data:
  t: "Milky Way Stargate (Ancient Gate): mechanical crafting"
  "n":
    - [rg, "Ring Block · 14", i, "kubejs:ancient_stargate_ring_block"]
    - [ch, "Chevron Block · 9", i, "kubejs:ancient_stargate_chevron_block"]
    - [bs, "Base Block · 1", i, "kubejs:ancient_stargate_base_block"]
    - [mc, Create mechanical crafting 7 x 7, m, "create:mechanical_crafter"]
    - [gt, Milky Way Stargate, o, "sgjourney:milky_way_stargate"]
  e: [[rg, mc, "14"], [ch, mc, "9"], [bs, mc, "1"], [mc, gt]]
  tips:
    - |-
      Pack script asg.js: 14 ring + 9 chevron + 1 base block in the same 7 x 7 pattern as the Classic Stargate.
    - |-
      The three Ancient blocks have their own assembly recipes in asg.js (the base block alone: 3750 mB utopian akreyrium, 1200 ticks, UEV rate); they are not detailed here.
---
# Milky Way Stargate (Ancient Gate): mechanical crafting

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_gate`

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Akreyrium refining, UHV controllers](../../plan/p17.md#uhvmulti)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-mc">
<div class="gt-head"><span class="gt-mname">Create mechanical crafting 7 x 7</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Ring Block · 14 (kubejs:ancient_stargate_ring_block) - 14"><img class="gt-ico" src="../../assets/icons/kubejs__ancient_stargate_ring_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ancient Stargate Ring Block</span><span class="gt-note">Ring Block · 14</span><b class="gt-q">14</b></span><span class="gt-slot" title="Chevron Block · 9 (kubejs:ancient_stargate_chevron_block) - 9"><img class="gt-ico" src="../../assets/icons/kubejs__ancient_stargate_chevron_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ancient Stargate Chevron Block</span><span class="gt-note">Chevron Block · 9</span><b class="gt-q">9</b></span><span class="gt-slot" title="Base Block · 1 (kubejs:ancient_stargate_base_block) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__ancient_stargate_base_block.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ancient Stargate Base Block</span><span class="gt-note">Base Block · 1</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_crafter.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Milky Way Stargate (sgjourney:milky_way_stargate)"><img class="gt-ico" src="../../assets/icons/sgjourney__milky_way_stargate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Milky Way Stargate</span></span></div>
</div>
<div class="gt-foot"><code>create:mechanical_crafter</code></div>
</div>
</div>

## Flow

- [Create mechanical crafting 7 x 7](#m-mc)

## Tips

- Pack script asg.js: 14 ring + 9 chevron + 1 base block in the same 7 x 7 pattern as the Classic Stargate.
- The three Ancient blocks have their own assembly recipes in asg.js (the base block alone: 3750 mB utopian akreyrium, 1200 ticks, UEV rate); they are not detailed here.
