---
kind: chain
id: rare_residue
order: 540
data:
  t: Rare Ore Residue
  inf: true
  "n":
    - [rr, Rare Ore Residue, s, "gtceu:rare_ore_residue_bucket"]
    - [el, LV Electrolyzer, m, "gtceu:lv_electrolyzer"]
    - [s1, Chromite Sludge, x, "gtceu:chromite_sludge_dust"]
    - [s2, Rare Sludge, x, "gtceu:rare_sludge_dust"]
    - [s3, Vanadium Magnetite Sludge, x, "gtceu:vanadium_magnetite_sludge_dust"]
    - [s4, Cobaltite Sludge, x, "gtceu:cobaltite_sludge_dust"]
    - [ros, Raw Ore Slurry 250 mB, f, "gtceu:raw_ore_slurry_bucket"]
    - [ce, MV Centrifuge, m, "gtceu:mv_centrifuge"]
    - [o1, "Chromite ×2", o, "gtceu:chromite_dust"]
    - [o2, "Rare Earth ×2", o, "gtceu:rare_earth_dust"]
    - [o3, "Vanadium Magnetite ×2", o, "gtceu:vanadium_magnetite_dust"]
    - [o4, "Cobaltite ×2", o, "gtceu:cobaltite_dust"]
    - [rm, "Rare Metallic Residue → calcite + silver", o, "gtceu:rare_metallic_residue_dust"]
  e:
    - [rr, el, "1 B"]
    - [el, s1]
    - [el, s2]
    - [el, s3]
    - [el, s4]
    - [el, ros]
    - [s1, ce]
    - [s2, ce]
    - [s3, ce]
    - [s4, ce]
    - [ce, o1]
    - [ce, o2]
    - [ce, o3]
    - [ce, o4]
    - [ce, rm]
  tips: ["Chromite → chromium (stainless steel). Rare earth → neodymium. Vanadium magnetite → vanadium steel."]
  b: [["gtceu:lv_electrolyzer", 1], ["gtceu:mv_centrifuge", 2], ["gtceu:mv_electrolyzer", 1]]
---
# Rare Ore Residue

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `rare_residue` · **Tags:** Infinite source

**Era setup:** [MV](../../eras/mv.md)

**Plan modules:** [Chromium (Void Extractor residue)](../../plan/p7.md#chromium)

**Tips:** 1

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-el">
<div class="gt-head"><span class="gt-mname">LV Electrolyzer</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-inf" title="Rare Ore Residue (gtceu:rare_ore_residue_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__rare_ore_residue_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Ore Residue Bucket</span><span class="gt-tag">infinite</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Chromite Sludge (gtceu:chromite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Sludge Dust</span></span><span class="gt-slot" title="Rare Sludge (gtceu:rare_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__rare_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Sludge Dust</span></span><span class="gt-slot" title="Vanadium Magnetite Sludge (gtceu:vanadium_magnetite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_magnetite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Magnetite Sludge Dust</span></span><span class="gt-slot" title="Cobaltite Sludge (gtceu:cobaltite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__cobaltite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobaltite Sludge Dust</span></span><span class="gt-slot gt-fluid" title="Raw Ore Slurry 250 mB (gtceu:raw_ore_slurry_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__raw_ore_slurry_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Ore Slurry</span><span class="gt-note">Raw Ore Slurry 250 mB</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_electrolyzer</code></div>
</div>
<div class="gt-panel t-mv" id="m-ce">
<div class="gt-head"><span class="gt-mname">MV Centrifuge</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Chromite Sludge (gtceu:chromite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Sludge Dust</span></span><span class="gt-slot" title="Rare Sludge (gtceu:rare_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__rare_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Sludge Dust</span></span><span class="gt-slot" title="Vanadium Magnetite Sludge (gtceu:vanadium_magnetite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_magnetite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Magnetite Sludge Dust</span></span><span class="gt-slot" title="Cobaltite Sludge (gtceu:cobaltite_sludge_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__cobaltite_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobaltite Sludge Dust</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Chromite ×2 (gtceu:chromite_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__chromite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Chromite Dust</span><span class="gt-note">Chromite ×2</span></span><span class="gt-slot gt-outp" title="Rare Earth ×2 (gtceu:rare_earth_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__rare_earth_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Earth Dust</span><span class="gt-note">Rare Earth ×2</span></span><span class="gt-slot gt-outp" title="Vanadium Magnetite ×2 (gtceu:vanadium_magnetite_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__vanadium_magnetite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Vanadium Magnetite Dust</span><span class="gt-note">Vanadium Magnetite ×2</span></span><span class="gt-slot gt-outp" title="Cobaltite ×2 (gtceu:cobaltite_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__cobaltite_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Cobaltite Dust</span><span class="gt-note">Cobaltite ×2</span></span><span class="gt-slot gt-outp" title="Rare Metallic Residue → calcite + silver (gtceu:rare_metallic_residue_dust)"><img class="gt-ico" src="../../assets/icons/gtceu__rare_metallic_residue_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rare Metallic Residue Dust</span><span class="gt-note">Rare Metallic Residue → calcite + silver</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_centrifuge</code></div>
</div>
</div>

## Flow

- [LV Electrolyzer](#m-el) → [MV Centrifuge](#m-ce)

## Tips

- Chromite → chromium (stainless steel). Rare earth → neodymium. Vanadium magnetite → vanadium steel.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_electrolyzer` | 1 |
| `gtceu:mv_centrifuge` | 2 |
| `gtceu:mv_electrolyzer` | 1 |

## Needs / Feeds

- **Needs:** [Void Extractor](../lv/void.md)
- **Feeds:** [Elemental powders: blizz, blitz, basalz from dust + gas, then molten powder for the nether star loop](../iv/elemental.md)
- **Main source for:** `gtceu:cobalt_dust`
