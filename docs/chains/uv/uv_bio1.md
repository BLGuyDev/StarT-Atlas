---
kind: chain
id: uv_bio1
order: 1540
data:
  t: |-
    Sterile bio line 1: bio chaff → bacteria → bacterial sludge → enriched sludge → mutagen (every step inside a Sterile Cleanroom)
  inf: true
  "n":
    - - g1
      - "4 bio chaff · 1 B distilled water"
      - g
      - functionalstorage:oak_1
      - [[Bio chaff, "gtceu:bio_chaff"], [Distilled water, "gtceu:distilled_water_bucket"]]
    - [b1, "HV Brewery · 15 s · 480 EU/t · Sterile Cleanroom", m, "gtceu:hv_brewery"]
    - [ba, Bacteria 1 B, f, "gtceu:bacteria_bucket"]
    - [g2, "1 B biomass", g, "functionalstorage:oak_1", [[Biomass, "gtceu:biomass_bucket"]]]
    - [c1, "EV Chemical Reactor · 30 s · 1920 EU/t · Sterile Cleanroom", m, "gtceu:ev_chemical_reactor"]
    - [sl, Bacterial sludge 1 B, f, "gtceu:bacterial_sludge_bucket"]
    - - g3
      - "1 uranium dust (238) OR 1 tiny naquadria dust"
      - g
      - functionalstorage:oak_1
      - [[Uranium 238 dust, "gtceu:uranium_dust"], [Tiny naquadria dust, "gtceu:tiny_naquadria_dust"]]
    - [b2, "Brewery (any tier) · 6.4 s · 4 EU/t · Sterile Cleanroom", m, "gtceu:hv_brewery"]
    - [es, "Enriched bacterial sludge 1 B (2 B with naquadria)", f, "gtceu:enriched_bacterial_sludge_bucket"]
    - [d1, "IV Distillery · 5 s · 7680 EU/t · circuit 1", m, "gtceu:iv_distillery"]
    - [mu, Mutagen 100 mB per B of enriched sludge, o, "gtceu:mutagen_bucket"]
  e:
    - [g1, b1, "1"]
    - [b1, ba, "1 B / 15 s"]
    - [ba, c1, "1 B"]
    - [g2, c1, "1 B"]
    - [c1, sl, "1 B / 30 s"]
    - [sl, b2, "1 B"]
    - [g3, b2, "1"]
    - [b2, es, "1 B / 6.4 s"]
    - [es, d1, "1 B"]
    - [d1, mu, "100 mB / 5 s"]
  tips:
    - |-
      Why this chain: wetware circuits (the UV circuit and the UHV circuit) need stem cells and sterilized growth medium, and both come from this line. Verified in gtsrc GrowthMediumRecipes: bacteria = brewery, 4 bio chaff + 1000 mB distilled water, 300 ticks at VA[HV]; bacterial sludge = chemical reactor, 1 B biomass + 1 B bacteria, 600 ticks at VA[EV]; enriched sludge = brewery, 1 uranium dust (238) (or 1 tiny uranium 235 dust, or 1 tiny naquadria dust for 2 B) + 1 B sludge, 128 ticks at 4 EU/t; mutagen = distillery, 1 B enriched sludge → 100 mB, circuit 1, 100 ticks at VA[IV]. All of them carry the STERILE cleanroom tag.
    - |-
      Sterile Cleanroom (quest text, kjs lang): the Sterilizing Filter Casing replaces the normal filter casings and turns the cleanroom into a Sterile Cleanroom; normal cleanroom recipes do NOT run in a sterile one, so keep a normal cleanroom for the circuit assemblers and a second sterile one for this line. Sterilizing Filter Casing (gtsrc CraftingRecipeLoader, crafting table, rows large PBI fluid pipe + ZPM emitter + large PBI fluid pipe / item filter + blacklight + item filter / ZPM motor + tritanium frame + naquadah alloy rotor): the cost is ZPM parts per casing, and the smallest cleanroom pattern has 8 filter spots in its ceiling (Unverified for larger rooms). The Sterile Cleaning Maintenance Hatch that would run sterile recipes outside a cleanroom is a UIV Assembly Line item (needs a UEV hull), so it is not an option in this era.
    - |-
      Yield warning: the distillery gives only 100 mB of mutagen per 1 B of enriched sludge. One batch of the raw growth medium (4 B) needs 4 B of mutagen = 40 B of enriched sludge = 40 B of sludge, i.e. 40 B of biomass and 40 B of bacteria (160 bio chaff) plus 20 tiny naquadria dust (naquadria route, 2 B per dust) or 40 uranium dust (238). The mutagen is by far the slow part of the wetware line; scale the brewery and the reactor in parallel (Large Chemical Reactor or the Chemical Plant are the multiblock options). A pack Chemical Plant recipe makes mutagen directly (mutagen_skip: 1 naquadria dust + 9 B biomass + 9 B bacteria → 1.8 B mutagen, 12 ticks) but at UEV power, so it is a later upgrade.
    - |-
      Sub-steps people skip: (1) distilled water and bio chaff come before everything: biomass and bio chaff sources are in the HV/EV chemistry chains, check that your biomass line exists; (2) the sludge reactor returns nothing but the sludge: keep Keep Exact 1000 mB on the biomass and bacteria drums with Pipez fluid pipes; (3) uranium dust (238) is consumed, 1 per B of sludge, so find a uranium source early (Unverified which pack route); (4) one dedicated brewery for the bacteria and a second for the enriched sludge, never share a machine between two recipes.
    - |-
      Unverified: the bio chaff and biomass sources (bio chaff from the Large Farm / composter chain is the GT default), the sterile cleanroom footprint in this pack, and the exact count of filter casings the sterile cleanroom needs.
  b:
    - ["gtceu:hv_brewery", 2]
    - ["gtceu:ev_chemical_reactor", 2]
    - ["gtceu:iv_distillery", 1]
    - ["gtceu:cleanroom", 1]
    - ["gtceu:sterilizing_filter_casing", 8]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 5]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:bio_chaff", "gtceu:uranium_dust"]
      t: |-
        Drawers first, one per solid input: bio chaff (Keep Exact 64), uranium dust (238) or tiny naquadria dust. Drums first for fluids: distilled water, biomass, bacteria, sludge, enriched sludge, mutagen. Everything in this chain sits INSIDE the Sterile Cleanroom: use the cleanroom passthrough hatches or put the machines in the room and run Pipez fluid pipes through the wall.
    - i: ["gtceu:hv_brewery", "gtceu:bacteria_bucket"]
      t: |-
        Bacteria brewery: a router from the chaff drawer (Item Filter, Robot Arm cover Keep Exact 4) and a Pipez fluid pipe from the distilled water drum. 4 chaff + 1 B water → 1 B bacteria every 15 s at 480 EU/t. Output drum for the bacteria.
    - i: ["gtceu:ev_chemical_reactor", "gtceu:bacterial_sludge_bucket"]
      t: |-
        Sludge reactor: bacteria drum and biomass drum each by their own Pipez fluid pipe, 1 B + 1 B → 1 B bacterial sludge every 30 s at 1920 EU/t. Keep the biomass drum filled before you open the bacteria valve.
    - i: ["gtceu:hv_brewery", "gtceu:uranium_dust", "gtceu:enriched_bacterial_sludge_bucket"]
      t: |-
        Enrichment brewery (second brewery, its own drawer of uranium dust (238)): 1 dust + 1 B sludge → 1 B enriched sludge in 6.4 s at 4 EU/t. With tiny naquadria dust the output doubles to 2 B.
    - i: ["gtceu:iv_distillery", "gtceu:mutagen_bucket"]
      t: |-
        Distillery: circuit 1 selects the mutagen output, 1 B enriched sludge → 100 mB mutagen in 5 s at 7680 EU/t. Put the mutagen in its own drum with a fluid pipe to the mixer of bio line 2.
    - i: ["gtceu:mutagen_bucket", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: the drums need to hold 40 B of enriched sludge buffer for one batch of medium. A steel drum holds 32 B, so use two drums per fluid for this buffer, and never merge sludge and enriched sludge in one drum.
---
# Sterile bio line 1: bio chaff → bacteria → bacterial sludge → enriched sludge → mutagen (every step inside a Sterile Cleanroom)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_bio1` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [Sterile bio lines](../../plan/p14.md#uvbio)

**Tips:** 5, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-b1">
<div class="gt-head"><span class="gt-mname">HV Brewery · 15 s · 480 EU/t · Sterile Cleanroom</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="4 bio chaff · 1 B distilled water (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 bio chaff · 1 B distilled water</span><span class="gt-sub"><span>Bio chaff</span><span>Distilled water</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_brewery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">15 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Bacteria 1 B (gtceu:bacteria_bucket) - 1 B / 15 s"><img class="gt-ico" src="../../assets/icons/gtceu__bacteria_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bacteria</span><span class="gt-note">Bacteria 1 B</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_brewery</code></div>
</div>
<div class="gt-panel t-ev" id="m-c1">
<div class="gt-head"><span class="gt-mname">EV Chemical Reactor · 30 s · 1920 EU/t · Sterile Cleanroom</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Bacteria 1 B (gtceu:bacteria_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__bacteria_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bacteria</span><span class="gt-note">Bacteria 1 B</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-group" title="1 B biomass (functionalstorage:oak_1) - 1 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 B biomass</span><span class="gt-sub"><span>Biomass</span></span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Bacterial sludge 1 B (gtceu:bacterial_sludge_bucket) - 1 B / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__bacterial_sludge_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bacterial Sludge</span><span class="gt-note">Bacterial sludge 1 B</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-b2">
<div class="gt-head"><span class="gt-mname">Brewery (any tier) · 6.4 s · 4 EU/t · Sterile Cleanroom</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Bacterial sludge 1 B (gtceu:bacterial_sludge_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__bacterial_sludge_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bacterial Sludge</span><span class="gt-note">Bacterial sludge 1 B</span><b class="gt-q">1 B</b></span><span class="gt-slot gt-group" title="1 uranium dust (238) OR 1 tiny naquadria dust (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">1 uranium dust (238) OR 1 tiny naquadria dust</span><span class="gt-sub"><span>Uranium 238 dust</span><span>Tiny naquadria dust</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_brewery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span><span class="gt-stat">6.4 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-fluid" title="Enriched bacterial sludge 1 B (2 B with naquadria) (gtceu:enriched_bacterial_sludge_bucket) - 1 B / 6.4 s"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_bacterial_sludge_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Bacterial Sludge</span><span class="gt-note">Enriched bacterial sludge 1 B (2 B with naquadria)</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_brewery</code></div>
</div>
<div class="gt-panel t-iv" id="m-d1">
<div class="gt-head"><span class="gt-mname">IV Distillery · 5 s · 7680 EU/t · circuit 1</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Enriched bacterial sludge 1 B (2 B with naquadria) (gtceu:enriched_bacterial_sludge_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_bacterial_sludge_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Bacterial Sludge</span><span class="gt-note">Enriched bacterial sludge 1 B (2 B with naquadria)</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span><span class="gt-stat">5 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Mutagen 100 mB per B of enriched sludge (gtceu:mutagen_bucket) - 100 mB / 5 s"><img class="gt-ico" src="../../assets/icons/gtceu__mutagen_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mutagen Bucket</span><span class="gt-note">Mutagen 100 mB per B of enriched sludge</span><b class="gt-q">100 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_distillery</code></div>
</div>
</div>

## Flow

- [HV Brewery · 15 s · 480 EU/t · Sterile Cleanroom](#m-b1) → [EV Chemical Reactor · 30 s · 1920 EU/t · Sterile Cleanroom](#m-c1) → [Brewery (any tier) · 6.4 s · 4 EU/t · Sterile Cleanroom](#m-b2) → [IV Distillery · 5 s · 7680 EU/t · circuit 1](#m-d1)

## How to build

1. Drawers first, one per solid input: bio chaff (Keep Exact 64), uranium dust (238) or tiny naquadria dust. Drums first for fluids: distilled water, biomass, bacteria, sludge, enriched sludge, mutagen. Everything in this chain sits INSIDE the Sterile Cleanroom: use the cleanroom passthrough hatches or put the machines in the room and run Pipez fluid pipes through the wall. — `functionalstorage:oak_1`, `gtceu:bio_chaff`, `gtceu:uranium_dust`
2. Bacteria brewery: a router from the chaff drawer (Item Filter, Robot Arm cover Keep Exact 4) and a Pipez fluid pipe from the distilled water drum. 4 chaff + 1 B water → 1 B bacteria every 15 s at 480 EU/t. Output drum for the bacteria. — `gtceu:hv_brewery`, `gtceu:bacteria_bucket`
3. Sludge reactor: bacteria drum and biomass drum each by their own Pipez fluid pipe, 1 B + 1 B → 1 B bacterial sludge every 30 s at 1920 EU/t. Keep the biomass drum filled before you open the bacteria valve. — `gtceu:ev_chemical_reactor`, `gtceu:bacterial_sludge_bucket`
4. Enrichment brewery (second brewery, its own drawer of uranium dust (238)): 1 dust + 1 B sludge → 1 B enriched sludge in 6.4 s at 4 EU/t. With tiny naquadria dust the output doubles to 2 B. — `gtceu:hv_brewery`, `gtceu:uranium_dust`, `gtceu:enriched_bacterial_sludge_bucket`
5. Distillery: circuit 1 selects the mutagen output, 1 B enriched sludge → 100 mB mutagen in 5 s at 7680 EU/t. Put the mutagen in its own drum with a fluid pipe to the mixer of bio line 2. — `gtceu:iv_distillery`, `gtceu:mutagen_bucket`
6. Easy to miss: the drums need to hold 40 B of enriched sludge buffer for one batch of medium. A steel drum holds 32 B, so use two drums per fluid for this buffer, and never merge sludge and enriched sludge in one drum. — `gtceu:mutagen_bucket`, `functionalstorage:oak_1`

## Tips

- Why this chain: wetware circuits (the UV circuit and the UHV circuit) need stem cells and sterilized growth medium, and both come from this line. Verified in gtsrc GrowthMediumRecipes: bacteria = brewery, 4 bio chaff + 1000 mB distilled water, 300 ticks at VA\[HV\]; bacterial sludge = chemical reactor, 1 B biomass + 1 B bacteria, 600 ticks at VA\[EV\]; enriched sludge = brewery, 1 uranium dust (238) (or 1 tiny uranium 235 dust, or 1 tiny naquadria dust for 2 B) + 1 B sludge, 128 ticks at 4 EU/t; mutagen = distillery, 1 B enriched sludge → 100 mB, circuit 1, 100 ticks at VA\[IV\]. All of them carry the STERILE cleanroom tag.
- Sterile Cleanroom (quest text, kjs lang): the Sterilizing Filter Casing replaces the normal filter casings and turns the cleanroom into a Sterile Cleanroom; normal cleanroom recipes do NOT run in a sterile one, so keep a normal cleanroom for the circuit assemblers and a second sterile one for this line. Sterilizing Filter Casing (gtsrc CraftingRecipeLoader, crafting table, rows large PBI fluid pipe + ZPM emitter + large PBI fluid pipe / item filter + blacklight + item filter / ZPM motor + tritanium frame + naquadah alloy rotor): the cost is ZPM parts per casing, and the smallest cleanroom pattern has 8 filter spots in its ceiling (Unverified for larger rooms). The Sterile Cleaning Maintenance Hatch that would run sterile recipes outside a cleanroom is a UIV Assembly Line item (needs a UEV hull), so it is not an option in this era.
- Yield warning: the distillery gives only 100 mB of mutagen per 1 B of enriched sludge. One batch of the raw growth medium (4 B) needs 4 B of mutagen = 40 B of enriched sludge = 40 B of sludge, i.e. 40 B of biomass and 40 B of bacteria (160 bio chaff) plus 20 tiny naquadria dust (naquadria route, 2 B per dust) or 40 uranium dust (238). The mutagen is by far the slow part of the wetware line; scale the brewery and the reactor in parallel (Large Chemical Reactor or the Chemical Plant are the multiblock options). A pack Chemical Plant recipe makes mutagen directly (mutagen\_skip: 1 naquadria dust + 9 B biomass + 9 B bacteria → 1.8 B mutagen, 12 ticks) but at UEV power, so it is a later upgrade.
- Sub-steps people skip: (1) distilled water and bio chaff come before everything: biomass and bio chaff sources are in the HV/EV chemistry chains, check that your biomass line exists; (2) the sludge reactor returns nothing but the sludge: keep Keep Exact 1000 mB on the biomass and bacteria drums with Pipez fluid pipes; (3) uranium dust (238) is consumed, 1 per B of sludge, so find a uranium source early (Unverified which pack route); (4) one dedicated brewery for the bacteria and a second for the enriched sludge, never share a machine between two recipes.
- **Unverified** the bio chaff and biomass sources (bio chaff from the Large Farm / composter chain is the GT default), the sterile cleanroom footprint in this pack, and the exact count of filter casings the sterile cleanroom needs.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_brewery` | 2 |
| `gtceu:ev_chemical_reactor` | 2 |
| `gtceu:iv_distillery` | 1 |
| `gtceu:cleanroom` | 1 |
| `gtceu:sterilizing_filter_casing` | 8 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 5 |

## Needs / Feeds

- **Main source for:** `gtceu:mutagen_bucket`, `gtceu:bacteria_bucket`, `gtceu:bacterial_sludge_bucket`, `gtceu:enriched_bacterial_sludge_bucket`, `gtceu:sterilizing_filter_casing`
