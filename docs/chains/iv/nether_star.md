---
kind: chain
id: nether_star
order: 390
data:
  t: |-
    Nether star loop: shards → energized shards → infused shards → impure star → implosion
  inf: true
  "n":
    - [ns, Nether star, i, "minecraft:nether_star"]
    - [fh, "HV Forge Hammer · 15 s · 240 EU/t", m, "gtceu:hv_forge_hammer"]
    - [sh, "5 Nether star shard", x, "kubejs:nether_star_shard"]
    - [po, "EV Polarizer · 20 s · 960 EU/t", m, "gtceu:ev_polarizer"]
    - [es, Energized nether star shard, x, "kubejs:energized_nether_star_shard"]
    - [fl, "720 mB molten powder: blaze, blizz, blitz or basalz", f, "gtceu:blaze_bucket"]
    - [ac, "IV Autoclave · 48 s · 3840 EU/t", m, "gtceu:iv_autoclave"]
    - [inf, "Infused shard: fire, ice, lightning, earth", x, "kubejs:fire_infused_shard"]
    - [fp, "IV Forming Press · star casting mold · 15 s · 7680 EU/t", m, "gtceu:iv_forming_press"]
    - [im, Impure nether star, x, "kubejs:impure_nether_star"]
    - [ex, "4 TNT or 1 industrial TNT", i, "minecraft:tnt"]
    - [ic, "Implosion Compressor · 1 s · 960 EU/t", m, "gtceu:implosion_compressor"]
    - [out, Nether star, o, "minecraft:nether_star"]
  e:
    - [ns, fh, "1"]
    - [fh, sh, "5"]
    - [sh, po, "1"]
    - [po, es, "1 / 20 s"]
    - [es, ac, "1 per run"]
    - [fl, ac, "720 mB"]
    - [ac, inf, "0.95 (50 % + 45 %)"]
    - [inf, fp, "4, one of each"]
    - [fp, im, "1"]
    - [im, ic, "1"]
    - [ex, ic]
    - [ic, out, "1"]
  tips:
    - |-
      Source: kubejs additions/progression/lines/nether_stars.js. Hammer: 1 nether star → 5 nether star shards, 300 ticks, 240 EU/t. Polarizer: 1 shard → 1 energized shard, 400 ticks (20 s), 960 EU/t, which is above the HV 512 V, so it is an EV Polarizer; the old node said IV.
    - |-
      The shard autoclave: 1 energized shard + 720 mB of the molten powder → two independent chances, 50 % and 45 %, of one infused shard each, 960 ticks (48 s) at 3840 EU/t, so an IV Autoclave (3840 is above the EV 2048). On average 0.95 infused shards per run. You need 4 different ones (fire from blaze, ice from blizz, lightning from blitz, earth from basalz), so 4 energized shards and about 4.2 runs per star.
    - |-
      Impure star: IV Forming Press with the star casting mold (shaped: ball casting mold + file) in the not-consumed slot, 1 each of fire, ice, lightning and earth infused shard → 1 impure nether star, 300 ticks at 7680 EU/t. Implosion Compressor: impure star + 4 TNT (or 2 dynamite, 1 industrial TNT or 8 powderbarrels) → 1 nether star + 25 % dark ash, 20 ticks at 960 EU/t (an EV hatch).
    - |-
      Net yield: 1 star → 5 shards → about 4.75 infused shards → 1.19 stars. The loop grows by roughly a fifth per pass, so it is NOT free: every quantum star (emitter, sensor, field generator) eats a whole nether star. Keep the first star out of the loop until the IV circuits and the hull line are ready.
    - |-
      Alternative start without shards: 8 charges (fire, ice, lightning or earth) + 720 mB molten powder → 20 % of one infused shard, 720 ticks at 960 EU/t in an EV Autoclave (kjs). Charges: mixer, coal dust + gunpowder + the powder → 3 charges (100 ticks, 30 EU/t). That is 40 charges per infused shard, so only useful when you have lots of powder.
    - |-
      The Heat Chamber (energized molten powders) and the nether tempered routes in the same script are LuV and ZPM recipes: ignore them at IV.
    - |-
      Per star the powders are small: 4 × about 760 mB molten powder, i.e. 4 × 5.3 powder items. One craft of the powder reactor gives 16 powder (see the elemental chain). Quantum star: 1 nether star + 1250 mB radon, HV Chemical Bath, 96 s at 480 EU/t.
    - |-
      Sub-steps people skip: (1) the shard is polarized in an EV machine, an HV polarizer does nothing; (2) the autoclave takes the powder as a FLUID (extractor from the powder item), not the powder item; (3) the forming press mold must not be consumed from the input bus: leave it in its slot; (4) four different infused shards: a drawer per type with Keep Exact 4, so one type does not pile up while another is missing.
    - |-
      Unverified: where blaze powder comes from (the pack removes the vanilla recipe and the Create crushing of blaze rods; a GT macerator recipe was not checked), and the first nether star itself (it is in the one-off items list, vanilla drops).
  b:
    - ["gtceu:hv_forge_hammer", 1]
    - ["gtceu:ev_polarizer", 1]
    - ["gtceu:iv_autoclave", 1]
    - ["gtceu:iv_forming_press", 1]
    - ["kubejs:star_casting_mold", 1]
    - ["gtceu:implosion_compressor", 1]
    - ["gtceu:lv_extractor", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 8]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 8]
    - ["gtceu:steel_drum", 4]
  how:
    - i: ["functionalstorage:oak_1", "minecraft:nether_star", "kubejs:nether_star_shard", "minecraft:tnt"]
      t: |-
        Drawers first: nether stars, shards, energized shards, one drawer per infused shard type (4), TNT, and a drum per molten powder (blaze, blizz, blitz, basalz). Every machine has its own input drawer behind a Modular Router or Pipez item pipe with an Item Filter and a Keep Exact Robot Arm on the output.
    - i: ["gtceu:hv_forge_hammer", "kubejs:nether_star_shard"]
      t: |-
        HV Forge Hammer: 1 nether star → 5 nether star shards, 15 s at 240 EU/t. One drawer for stars; the first star is the only one you ever feed by hand.
    - i: ["gtceu:ev_polarizer", "kubejs:energized_nether_star_shard"]
      t: |-
        EV Polarizer: 1 shard → 1 energized shard, 20 s at 960 EU/t. Dedicated machine; Keep Exact 8 on the output so the autoclave always has shards.
    - i:
        - gtceu:iv_autoclave
        - kubejs:fire_infused_shard
        - kubejs:ice_infused_shard
        - kubejs:lightning_infused_shard
        - kubejs:earth_infused_shard
      t: |-
        IV Autoclave (3840 EU/t): energized shard in the bus, 720 mB of ONE molten powder in a fluid hatch, 48 s, 0.95 shards on average. Use one autoclave per element (four machines) or one autoclave with one drum at a time: a Modular Router with an Item Filter would otherwise mix the elements. The output stays the element of the powder: blaze → fire, blizz → ice, blitz → lightning, basalz → earth.
    - i: ["gtceu:lv_extractor", "gtceu:blizz_bucket"]
      t: |-
        Molten powders: LV Extractor, 1 powder (blaze, blizz, blitz or basalz) → 144 mB, 22 ticks at 30 EU/t. 5 powders per autoclave run. The powders come from the elemental chain (blizz, blitz, basalz) and from blaze powder.
    - i: ["gtceu:iv_forming_press", "kubejs:star_casting_mold", "kubejs:impure_nether_star"]
      t: |-
        IV Forming Press: the star casting mold in a non-consumed slot, then 1 fire + 1 ice + 1 lightning + 1 earth infused shard → 1 impure nether star in 15 s at 7680 EU/t. Wire the press with an input bus that holds the mold in a slot and an Item Filter on the four shard types.
    - i: ["gtceu:implosion_compressor", "minecraft:nether_star"]
      t: |-
        Implosion Compressor (EV hatch, 960 EU/t): impure star + explosive in the input bus → nether star + 25 % dark ash in 1 s. The explosive: 4 TNT or 1 industrial TNT per star (GT industrial TNT is the cheap one). Route the new star back to the hammer drawer through a Robot Arm: that closes the loop, while a second Item Filter route skims stars for the radon chemical bath.
    - i: ["gtceu:quantum_star", "gtceu:hv_chemical_bath"]
      t: |-
        Easy to miss: every star you divert to a quantum star is gone from the loop. Count stars, not shards: at 1.19 per pass the loop only sustains a star drain of about a fifth per pass. Build a backup stock of 4 infused shards per element before you start emitters and sensors in bulk.
---
# Nether star loop: shards → energized shards → infused shards → impure star → implosion

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `nether_star` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [Nether star loop and elemental powders](../../plan/p10.md#netherstar)

**Tips:** 9, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-hv" id="m-fh">
<div class="gt-head"><span class="gt-mname">HV Forge Hammer · 15 s · 240 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nether star (minecraft:nether_star) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__nether_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_forge_hammer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Nether star shard (kubejs:nether_star_shard) - 5"><img class="gt-ico" src="../../assets/icons/kubejs__nether_star_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star Shard</span><span class="gt-note">5 Nether star shard</span><b class="gt-q">5</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_forge_hammer</code></div>
</div>
<div class="gt-panel t-ev" id="m-po">
<div class="gt-head"><span class="gt-mname">EV Polarizer · 20 s · 960 EU/t</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="5 Nether star shard (kubejs:nether_star_shard) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__nether_star_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star Shard</span><span class="gt-note">5 Nether star shard</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_polarizer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span><span class="gt-stat">20 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Energized nether star shard (kubejs:energized_nether_star_shard) - 1 / 20 s"><img class="gt-ico" src="../../assets/icons/kubejs__energized_nether_star_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energized Nether Star Shard</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_polarizer</code></div>
</div>
<div class="gt-panel t-iv" id="m-ac">
<div class="gt-head"><span class="gt-mname">IV Autoclave · 48 s · 3840 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Energized nether star shard (kubejs:energized_nether_star_shard) - 1 per run"><img class="gt-ico" src="../../assets/icons/kubejs__energized_nether_star_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Energized Nether Star Shard</span><b class="gt-q">1 per run</b></span><span class="gt-slot gt-fluid" title="720 mB molten powder: blaze, blizz, blitz or basalz (gtceu:blaze_bucket) - 720 mB"><img class="gt-ico" src="../../assets/icons/gtceu__blaze_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Blaze</span><span class="gt-note">720 mB molten powder: blaze, blizz, blitz or basalz</span><b class="gt-q">720 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Infused shard: fire, ice, lightning, earth (kubejs:fire_infused_shard) - 0.95 (50 % + 45 %)"><img class="gt-ico" src="../../assets/icons/kubejs__fire_infused_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fire Infused Shard</span><span class="gt-note">Infused shard: fire, ice, lightning, earth</span><b class="gt-q">0.95 (50 % + 45 %)</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_autoclave</code></div>
</div>
<div class="gt-panel t-iv" id="m-fp">
<div class="gt-head"><span class="gt-mname">IV Forming Press · star casting mold · 15 s · 7680 EU/t</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Infused shard: fire, ice, lightning, earth (kubejs:fire_infused_shard) - 4, one of each"><img class="gt-ico" src="../../assets/icons/kubejs__fire_infused_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fire Infused Shard</span><span class="gt-note">Infused shard: fire, ice, lightning, earth</span><b class="gt-q">4, one of each</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_forming_press.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Impure nether star (kubejs:impure_nether_star) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__impure_nether_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Impure Nether Star</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_forming_press</code></div>
</div>
<div class="gt-panel t-multi" id="m-ic">
<div class="gt-head"><span class="gt-mname">Implosion Compressor · 1 s · 960 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Impure nether star (kubejs:impure_nether_star) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__impure_nether_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Impure Nether Star</span><b class="gt-q">1</b></span><span class="gt-slot" title="4 TNT or 1 industrial TNT (minecraft:tnt)"><img class="gt-ico" src="../../assets/icons/minecraft__tnt.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tnt</span><span class="gt-note">4 TNT or 1 industrial TNT</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__implosion_compressor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Nether star (minecraft:nether_star) - 1"><img class="gt-ico" src="../../assets/icons/minecraft__nether_star.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:implosion_compressor</code></div>
</div>
</div>

## Flow

- [HV Forge Hammer · 15 s · 240 EU/t](#m-fh) → [EV Polarizer · 20 s · 960 EU/t](#m-po) → [IV Autoclave · 48 s · 3840 EU/t](#m-ac) → [IV Forming Press · star casting mold · 15 s · 7680 EU/t](#m-fp) → [Implosion Compressor · 1 s · 960 EU/t](#m-ic)

## How to build

1. Drawers first: nether stars, shards, energized shards, one drawer per infused shard type (4), TNT, and a drum per molten powder (blaze, blizz, blitz, basalz). Every machine has its own input drawer behind a Modular Router or Pipez item pipe with an Item Filter and a Keep Exact Robot Arm on the output. — `functionalstorage:oak_1`, `minecraft:nether_star`, `kubejs:nether_star_shard`, `minecraft:tnt`
2. HV Forge Hammer: 1 nether star → 5 nether star shards, 15 s at 240 EU/t. One drawer for stars; the first star is the only one you ever feed by hand. — `gtceu:hv_forge_hammer`, `kubejs:nether_star_shard`
3. EV Polarizer: 1 shard → 1 energized shard, 20 s at 960 EU/t. Dedicated machine; Keep Exact 8 on the output so the autoclave always has shards. — `gtceu:ev_polarizer`, `kubejs:energized_nether_star_shard`
4. IV Autoclave (3840 EU/t): energized shard in the bus, 720 mB of ONE molten powder in a fluid hatch, 48 s, 0.95 shards on average. Use one autoclave per element (four machines) or one autoclave with one drum at a time: a Modular Router with an Item Filter would otherwise mix the elements. The output stays the element of the powder: blaze → fire, blizz → ice, blitz → lightning, basalz → earth. — `gtceu:iv_autoclave`, `kubejs:fire_infused_shard`, `kubejs:ice_infused_shard`, `kubejs:lightning_infused_shard`, `kubejs:earth_infused_shard`
5. Molten powders: LV Extractor, 1 powder (blaze, blizz, blitz or basalz) → 144 mB, 22 ticks at 30 EU/t. 5 powders per autoclave run. The powders come from the elemental chain (blizz, blitz, basalz) and from blaze powder. — `gtceu:lv_extractor`, `gtceu:blizz_bucket`
6. IV Forming Press: the star casting mold in a non-consumed slot, then 1 fire + 1 ice + 1 lightning + 1 earth infused shard → 1 impure nether star in 15 s at 7680 EU/t. Wire the press with an input bus that holds the mold in a slot and an Item Filter on the four shard types. — `gtceu:iv_forming_press`, `kubejs:star_casting_mold`, `kubejs:impure_nether_star`
7. Implosion Compressor (EV hatch, 960 EU/t): impure star + explosive in the input bus → nether star + 25 % dark ash in 1 s. The explosive: 4 TNT or 1 industrial TNT per star (GT industrial TNT is the cheap one). Route the new star back to the hammer drawer through a Robot Arm: that closes the loop, while a second Item Filter route skims stars for the radon chemical bath. — `gtceu:implosion_compressor`, `minecraft:nether_star`
8. Easy to miss: every star you divert to a quantum star is gone from the loop. Count stars, not shards: at 1.19 per pass the loop only sustains a star drain of about a fifth per pass. Build a backup stock of 4 infused shards per element before you start emitters and sensors in bulk. — `gtceu:quantum_star`, `gtceu:hv_chemical_bath`

## Tips

- Source: kubejs additions/progression/lines/nether\_stars.js. Hammer: 1 nether star → 5 nether star shards, 300 ticks, 240 EU/t. Polarizer: 1 shard → 1 energized shard, 400 ticks (20 s), 960 EU/t, which is above the HV 512 V, so it is an EV Polarizer; the old node said IV.
- The shard autoclave: 1 energized shard + 720 mB of the molten powder → two independent chances, 50 % and 45 %, of one infused shard each, 960 ticks (48 s) at 3840 EU/t, so an IV Autoclave (3840 is above the EV 2048). On average 0.95 infused shards per run. You need 4 different ones (fire from blaze, ice from blizz, lightning from blitz, earth from basalz), so 4 energized shards and about 4.2 runs per star.
- Impure star: IV Forming Press with the star casting mold (shaped: ball casting mold + file) in the not-consumed slot, 1 each of fire, ice, lightning and earth infused shard → 1 impure nether star, 300 ticks at 7680 EU/t. Implosion Compressor: impure star + 4 TNT (or 2 dynamite, 1 industrial TNT or 8 powderbarrels) → 1 nether star + 25 % dark ash, 20 ticks at 960 EU/t (an EV hatch).
- Net yield: 1 star → 5 shards → about 4.75 infused shards → 1.19 stars. The loop grows by roughly a fifth per pass, so it is NOT free: every quantum star (emitter, sensor, field generator) eats a whole nether star. Keep the first star out of the loop until the IV circuits and the hull line are ready.
- Alternative start without shards: 8 charges (fire, ice, lightning or earth) + 720 mB molten powder → 20 % of one infused shard, 720 ticks at 960 EU/t in an EV Autoclave (kjs). Charges: mixer, coal dust + gunpowder + the powder → 3 charges (100 ticks, 30 EU/t). That is 40 charges per infused shard, so only useful when you have lots of powder.
- The Heat Chamber (energized molten powders) and the nether tempered routes in the same script are LuV and ZPM recipes: ignore them at IV.
- Per star the powders are small: 4 × about 760 mB molten powder, i.e. 4 × 5.3 powder items. One craft of the powder reactor gives 16 powder (see the elemental chain). Quantum star: 1 nether star + 1250 mB radon, HV Chemical Bath, 96 s at 480 EU/t.
- Sub-steps people skip: (1) the shard is polarized in an EV machine, an HV polarizer does nothing; (2) the autoclave takes the powder as a FLUID (extractor from the powder item), not the powder item; (3) the forming press mold must not be consumed from the input bus: leave it in its slot; (4) four different infused shards: a drawer per type with Keep Exact 4, so one type does not pile up while another is missing.
- **Unverified** where blaze powder comes from (the pack removes the vanilla recipe and the Create crushing of blaze rods; a GT macerator recipe was not checked), and the first nether star itself (it is in the one-off items list, vanilla drops).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:hv_forge_hammer` | 1 |
| `gtceu:ev_polarizer` | 1 |
| `gtceu:iv_autoclave` | 1 |
| `gtceu:iv_forming_press` | 1 |
| `kubejs:star_casting_mold` | 1 |
| `gtceu:implosion_compressor` | 1 |
| `gtceu:lv_extractor` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 8 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 8 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Feeds:** [Naquadah: nether star shard + PCB coolant in the Dimensional Destabiliser → raw naquadah → ore line → dust → EBF 5000 K; byproducts by the fluoroantimonic acid line](../luv/naquadah.md), [Gravi star: nether star → quantum star (radon bath) → gravi star (autoclave with 288 mB neutronium) - 1 per UV emitter, sensor and field generator](../uv/uv_gravi.md)
- **Main source for:** `minecraft:nether_star`, `kubejs:nether_star_shard`
