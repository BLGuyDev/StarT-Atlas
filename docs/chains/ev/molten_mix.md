---
kind: chain
id: molten_mix
order: 560
data:
  t: Molten Ore Mixture
  inf: true
  "n":
    - [mo, Molten Ore Mixture 10 B, s, "gtceu:molten_ore_mixture_bucket"]
    - [dt, "Distillation Tower (EV)", m, "gtceu:distillation_tower"]
    - [mx, Metal Mixture, x, "gtceu:metal_mixture_dust"]
    - [f1, "Molten Tungstate · Cooperite", f, "gtceu:molten_tungstate_ore_bucket"]
    - [f2, "Molten Bauxite · Ilmenite", f, "gtceu:molten_ilmenite_ore_bucket"]
    - [f3, "Molten Pitchblende · Molybdenite · Bastnasite", f, "gtceu:molten_pitchblende_ore_bucket"]
    - [sd, Stone Dust, i, "gtceu:stone_dust"]
    - [ac, HV Autoclave, m, "gtceu:hv_autoclave"]
    - [o1, Raw Tungstate, o, "gtceu:raw_tungstate"]
    - [o2, Raw Cooperite, o, "gtceu:raw_cooperite"]
    - [o3, "Raw Ilmenite / Bauxite", o, "gtceu:raw_ilmenite"]
    - [o4, "Raw Pitchblende…", o, "gtceu:raw_pitchblende"]
    - [loop, IV Mixer loop, m, "gtceu:iv_mixer"]
  e:
    - [mo, dt]
    - [dt, mx]
    - [dt, f1]
    - [dt, f2]
    - [dt, f3]
    - [f1, ac, "500 mB"]
    - [f2, ac]
    - [f3, ac]
    - [sd, ac, "1"]
    - [ac, o1]
    - [ac, o2]
    - [ac, o3]
    - [ac, o4]
    - [mx, loop, "48 B lava + 48 stone dust"]
  tips:
    - |-
      IV mixer: 2 metal mixture + 48 stone dust + 48 B lava → 20 B Molten Ore Mixture (self-feeding).
    - |-
      EV mixer: any 16 crushed ores + 32 stone dust + 32 B lava → 6 B.
  b: [["gtceu:distillation_tower", 1], ["gtceu:hv_autoclave", 2], ["gtceu:iv_mixer", 1]]
---
# Molten Ore Mixture

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `molten_mix` · **Tags:** Infinite source

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Titanium (molten ore line)](../../plan/p9.md#titanium)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-dt">
<div class="gt-head"><span class="gt-mname">Distillation Tower (EV)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Molten Ore Mixture 10 B (gtceu:molten_ore_mixture_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ore_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ore Mixture Bucket</span><span class="gt-note">Molten Ore Mixture 10 B</span><span class="gt-tag">infinite</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__distillation_tower.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Metal Mixture (gtceu:metal_mixture_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Metal Mixture Dust</span></span><span class="gt-slot gt-fluid" title="Molten Tungstate · Cooperite (gtceu:molten_tungstate_ore_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_tungstate_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Tungstate Ore</span><span class="gt-note">Molten Tungstate · Cooperite</span></span><span class="gt-slot gt-fluid" title="Molten Bauxite · Ilmenite (gtceu:molten_ilmenite_ore_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ilmenite_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ilmenite Ore</span><span class="gt-note">Molten Bauxite · Ilmenite</span></span><span class="gt-slot gt-fluid" title="Molten Pitchblende · Molybdenite · Bastnasite (gtceu:molten_pitchblende_ore_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_pitchblende_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Pitchblende Ore</span><span class="gt-note">Molten Pitchblende · Molybdenite · Bastnasite</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:distillation_tower</code></div>
</div>
<div class="gt-panel t-hv" id="m-ac">
<div class="gt-head"><span class="gt-mname">HV Autoclave</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Molten Tungstate · Cooperite (gtceu:molten_tungstate_ore_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__molten_tungstate_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Tungstate Ore</span><span class="gt-note">Molten Tungstate · Cooperite</span><b class="gt-q">500 mB</b></span><span class="gt-slot gt-fluid" title="Molten Bauxite · Ilmenite (gtceu:molten_ilmenite_ore_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ilmenite_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ilmenite Ore</span><span class="gt-note">Molten Bauxite · Ilmenite</span></span><span class="gt-slot gt-fluid" title="Molten Pitchblende · Molybdenite · Bastnasite (gtceu:molten_pitchblende_ore_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__molten_pitchblende_ore_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Pitchblende Ore</span><span class="gt-note">Molten Pitchblende · Molybdenite · Bastnasite</span></span><span class="gt-slot" title="Stone Dust (gtceu:stone_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__stone_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Stone Dust</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_autoclave.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Raw Tungstate (gtceu:raw_tungstate)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_tungstate.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Tungstate</span></span><span class="gt-slot gt-outp" title="Raw Cooperite (gtceu:raw_cooperite)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_cooperite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Cooperite</span></span><span class="gt-slot gt-outp" title="Raw Ilmenite / Bauxite (gtceu:raw_ilmenite)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ilmenite.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ilmenite</span><span class="gt-note">Raw Ilmenite / Bauxite</span></span><span class="gt-slot gt-outp" title="Raw Pitchblende… (gtceu:raw_pitchblende)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_pitchblende.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Pitchblende</span><span class="gt-note">Raw Pitchblende…</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_autoclave</code></div>
</div>
<div class="gt-panel t-iv" id="m-loop">
<div class="gt-head"><span class="gt-mname">IV Mixer loop</span><span class="gt-badge t-iv">IV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Metal Mixture (gtceu:metal_mixture_dust) - 48 B lava + 48 stone dust"><img class="gt-ico" src="../../assets/icons/gtceu__metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Metal Mixture Dust</span><b class="gt-q">48 B lava + 48 stone dust</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__iv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 8 192 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:iv_mixer</code></div>
</div>
</div>

## Flow

- [Distillation Tower (EV)](#m-dt) → [IV Mixer loop](#m-loop) (also Distillation Tower (EV) → [HV Autoclave](#m-ac))
- [HV Autoclave](#m-ac)

## Tips

- IV mixer: 2 metal mixture + 48 stone dust + 48 B lava → 20 B Molten Ore Mixture (self-feeding).
- EV mixer: any 16 crushed ores + 32 stone dust + 32 B lava → 6 B.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:distillation_tower` | 1 |
| `gtceu:hv_autoclave` | 2 |
| `gtceu:iv_mixer` | 1 |

## Needs / Feeds

- **Needs:** [Raw Ore Slurry &amp; mineral mixtures](../mv/slurry.md), [Infinite cobble &amp; blackstone](../stone/inf_cobble.md)
- **Feeds:** [Platinum group line: sludge → aqua regia centrifuge → platinum, palladium, rhodium, ruthenium, iridium, osmium](../iv/platline.md), [Tungsten and tungsten steel: chemical bath → electrolyzer → EBF 3600 K (nichrome coils) → Vacuum Freezer](../iv/tungsten.md)
- **Main source for:** `gtceu:tungstate_dust`, `gtceu:purified_cooperite_ore`
