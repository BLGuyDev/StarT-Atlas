---
kind: chain
id: epoxy
order: 360
data:
  t: Epoxy
  "n":
    - [ph, Phenol, f, "gtceu:phenol_bucket"]
    - [ac, Acetone, f, "gtceu:acetone_bucket"]
    - [bpa, Bisphenol A, f, "gtceu:bisphenol_a_bucket"]
    - [pr, "Propene + chlorine", f, "gtceu:propene_bucket"]
    - [ep, Epichlorohydrin, f, "gtceu:epichlorohydrin_bucket"]
    - [lcr, LCR, m, "gtceu:large_chemical_reactor"]
    - [out, Epoxy, o, "gtceu:epoxy_bucket"]
  e: [[ph, bpa], [ac, bpa], [pr, ep], [bpa, lcr], [ep, lcr], [lcr, out]]
  tips: [LCR circuit 24 skips most steps., "Phenol from wood tar, acetone from wood vinegar."]
  b: [["gtceu:large_chemical_reactor", 2]]
---
# Epoxy

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `epoxy`

**Era setup:** [EV](../../eras/ev.md)

**Plan modules:** [Refinery gases, liquid air, radon, epoxy](../../plan/p9.md#evfluids)

**Tips:** 2

## Machines

<div class="gt-panels">
<div class="gt-panel t-multi" id="m-lcr">
<div class="gt-head"><span class="gt-mname">LCR</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="Bisphenol A (gtceu:bisphenol_a_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__bisphenol_a_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Bisphenol A</span></span><span class="gt-slot gt-fluid" title="Epichlorohydrin (gtceu:epichlorohydrin_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__epichlorohydrin_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epichlorohydrin</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Epoxy (gtceu:epoxy_bucket)"><img class="gt-ico" src="../../assets/icons/gtceu__epoxy_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Epoxy Bucket</span></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LCR](#m-lcr)

### Direct steps

- Phenol → Bisphenol A
- Acetone → Bisphenol A
- Propene + chlorine → Epichlorohydrin

## Tips

- LCR circuit 24 skips most steps.
- Phenol from wood tar, acetone from wood vinegar.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 2 |
