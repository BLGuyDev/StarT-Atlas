---
kind: chain
id: slurry
order: 550
data:
  t: Raw Ore Slurry & mineral mixtures
  inf: true
  "n":
    - [rs, Raw Ore Slurry, s, "gtceu:raw_ore_slurry_bucket"]
    - [ce, MV Centrifuge, m, "gtceu:mv_centrifuge"]
    - [o1, Crushed Lepidolite, o, "gtceu:crushed_lepidolite_ore"]
    - [o2, Crushed Pyrochlore, o, "gtceu:crushed_pyrochlore_ore"]
    - [o3, Crushed Pyrolusite, o, "gtceu:crushed_pyrolusite_ore"]
    - [o4, Crushed Magnesite, o, "gtceu:crushed_magnesite_ore"]
    - [mm, Mixed Mineral Residue, f, "gtceu:mixed_mineral_residue_bucket"]
    - [mo, Molten Ore Mixture, f, "gtceu:molten_ore_mixture_bucket"]
    - [el, HV Electrolyzer, m, "gtceu:hv_electrolyzer"]
    - [o5, Crushed Beryllium, o, "gtceu:crushed_beryllium_ore"]
    - [o6, Crushed Zavaritskite, o, "gtceu:crushed_zavaritskite_ore"]
    - [sm, Sulfuric Mineral Mixture, f, "gtceu:sulfuric_mineral_mixture_bucket"]
    - [om, Oxygenous Mineral Mixture, f, "gtceu:oxygenous_mineral_mixture_bucket"]
    - [ce2, HV Centrifuge, m, "gtceu:hv_centrifuge"]
    - [o7, "Barite · Chalcopyrite · Bornite", o, "gtceu:crushed_chalcopyrite_ore"]
    - [o8, "Tantalite · Pollucite · Cassiterite", o, "gtceu:crushed_tantalite_ore"]
  e:
    - [rs, ce, "1 B"]
    - [ce, o1]
    - [ce, o2]
    - [ce, o3]
    - [ce, o4]
    - [ce, mm, "750 mB"]
    - [ce, mo, "250 mB"]
    - [mm, el]
    - [el, o5]
    - [el, o6]
    - [el, sm, "400 mB"]
    - [el, om, "600 mB"]
    - [sm, ce2]
    - [om, ce2]
    - [ce2, o7]
    - [ce2, o8]
  tips:
    - Pyrolusite → manganese, magnesite → magnesium, lepidolite → lithium + fluorine.
    - Molten Ore Mixture continues in EV (next chain).
  b: [["gtceu:mv_centrifuge", 1], ["gtceu:hv_electrolyzer", 1], ["gtceu:hv_centrifuge", 1]]
---
# Raw Ore Slurry &amp; mineral mixtures

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `slurry` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Titanium (molten ore line)](../../plan/p9.md#titanium)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-mv" id="m-ce">
<div class="gt-head"><span class="gt-mname">MV Centrifuge</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Raw Ore Slurry (gtceu:raw_ore_slurry_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ore_slurry_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ore Slurry Bucket</span><span class="gt-tag">infinite</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Lepidolite (gtceu:crushed_lepidolite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_lepidolite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Lepidolite Ore</span></span><span class="gt-slot gt-outp" title="Crushed Pyrochlore (gtceu:crushed_pyrochlore_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_pyrochlore_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Pyrochlore Ore</span></span><span class="gt-slot gt-outp" title="Crushed Pyrolusite (gtceu:crushed_pyrolusite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_pyrolusite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Pyrolusite Ore</span></span><span class="gt-slot gt-outp" title="Crushed Magnesite (gtceu:crushed_magnesite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_magnesite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Magnesite Ore</span></span><span class="gt-slot gt-fluid" title="Mixed Mineral Residue (gtceu:mixed_mineral_residue_bucket) - 750 mB"><img class="gt-ico" src="../../assets/icons/gtceu__mixed_mineral_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mixed Mineral Residue</span><b class="gt-q">750 mB</b></span><span class="gt-slot gt-fluid" title="Molten Ore Mixture (gtceu:molten_ore_mixture_bucket) - 250 mB"><img class="gt-ico" src="../../assets/icons/gtceu__molten_ore_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Molten Ore Mixture</span><b class="gt-q">250 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_centrifuge</code></div>
</div>
<div class="gt-panel t-hv" id="m-el">
<div class="gt-head"><span class="gt-mname">HV Electrolyzer</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Mixed Mineral Residue (gtceu:mixed_mineral_residue_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__mixed_mineral_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Mixed Mineral Residue</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Crushed Beryllium (gtceu:crushed_beryllium_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_beryllium_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Beryllium Ore</span></span><span class="gt-slot gt-outp" title="Crushed Zavaritskite (gtceu:crushed_zavaritskite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_zavaritskite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Zavaritskite Ore</span></span><span class="gt-slot gt-fluid" title="Sulfuric Mineral Mixture (gtceu:sulfuric_mineral_mixture_bucket) - 400 mB"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_mineral_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Mineral Mixture</span><b class="gt-q">400 mB</b></span><span class="gt-slot gt-fluid" title="Oxygenous Mineral Mixture (gtceu:oxygenous_mineral_mixture_bucket) - 600 mB"><img class="gt-ico" src="../../assets/icons/gtceu__oxygenous_mineral_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygenous Mineral Mixture</span><b class="gt-q">600 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_electrolyzer</code></div>
</div>
<div class="gt-panel t-hv" id="m-ce2">
<div class="gt-head"><span class="gt-mname">HV Centrifuge</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Sulfuric Mineral Mixture (gtceu:sulfuric_mineral_mixture_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__sulfuric_mineral_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Sulfuric Mineral Mixture</span></span><span class="gt-slot gt-fluid" title="Oxygenous Mineral Mixture (gtceu:oxygenous_mineral_mixture_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__oxygenous_mineral_mixture_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oxygenous Mineral Mixture</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Barite · Chalcopyrite · Bornite (gtceu:crushed_chalcopyrite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_chalcopyrite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Chalcopyrite Ore</span><span class="gt-note">Barite · Chalcopyrite · Bornite</span></span><span class="gt-slot gt-outp" title="Tantalite · Pollucite · Cassiterite (gtceu:crushed_tantalite_ore)"><img class="gt-ico" src="../../assets/icons/gtceu__crushed_tantalite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Crushed Tantalite Ore</span><span class="gt-note">Tantalite · Pollucite · Cassiterite</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_centrifuge</code></div>
</div>
</div>

## Flow

- [MV Centrifuge](#m-ce) → [HV Electrolyzer](#m-el) → [HV Centrifuge](#m-ce2)

## Tips

- Pyrolusite → manganese, magnesite → magnesium, lepidolite → lithium + fluorine.
- Molten Ore Mixture continues in EV (next chain).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:mv_centrifuge` | 1 |
| `gtceu:hv_electrolyzer` | 1 |
| `gtceu:hv_centrifuge` | 1 |

## Needs / Feeds

- **Needs:** [Void Extractor](../lv/void.md)
- **Feeds:** [Stainless steel: MV Mixer + HV Electric Blast Furnace](../hv/stainless.md), [Molten Ore Mixture](../ev/molten_mix.md), [Titanium: molten ilmenite → rutile → TiCl4 → Kanthal EBF → Vacuum Freezer](../ev/titanium_line.md), [ZPM power: argon plasma in Fusion MK II (carbon + magnesium) into Large Plasma Turbines](../zpm/zpm_argon.md)
- **Main source for:** `gtceu:manganese_dust`, `gtceu:magnesium_dust`, `gtceu:hydrofluoric_acid_bucket`, `gtceu:molten_ore_mixture_bucket`, `gtceu:fluorine_bucket`
