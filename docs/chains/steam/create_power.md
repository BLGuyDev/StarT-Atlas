---
kind: chain
id: create_power
order: 50
data:
  t: Free rotation (Create)
  inf: true
  "n":
    - [wm, "Windmill + sails", p, "create:windmill_bearing"]
    - [ww, Water Wheel, p, "create:water_wheel"]
    - [sh, Shafts, x, "create:shaft"]
    - [pr, Press, m, "create:mechanical_press"]
    - [mx, Heated Mixer, m, "create:mechanical_mixer"]
    - [cw, Crushing Wheels, m, "create:crushing_wheel"]
    - [gc, Generator Coil, m, "create_new_age:generator_coil"]
  e: [[wm, sh, SU], [ww, sh, SU], [sh, pr], [sh, mx], [sh, cw], [sh, gc]]
  tips:
    - More sails = more stress capacity.
    - Encased fan at max RPM superheats the Basic Burner (32× fuel).
    - Past EV Create adds nothing.
    - |-
      Big option: Huge Diesel Engine on crude biodiesel gives 12 288 SU at 224 RPM per engine; 208 engines = 2.56 M SU. Create mixer: 100 plant oil + 100 ethanol → 200 biodiesel. Unverified in game: the burn rate (config 0.05).
    - |-
      Biodiesel without oil: LCR (LV recipe), 54 B fish oil + 9 B ethanol or methanol + NaOH dust → 54 B biodiesel + 9 B glycerol in 270 s. Fish oil needs fish: the only fish source in the pack is the Industrial Fishery (IV controller).
  b:
    - ["create:windmill_bearing", 1]
    - ["create:white_sail", 24]
    - ["create:shaft", 8]
    - ["create:cogwheel", 4]
    - ["create:large_cogwheel", 2]
    - ["create:gearbox", 2]
  how:
    - i: ["create:windmill_bearing", "create:white_sail"]
      t: Windmill Bearing + at least 8 sails (pack minimum). Every 8 sails add 1 RPM, up to 16 RPM with 128 sails.
    - i: ["create:windmill_bearing"]
      t: |-
        Capacity is 512 SU per RPM of the windmill: 16 RPM → 8 192 SU. Gearing up keeps the SU total; the faster you run machines, the fewer you can power.
    - i: ["create:large_cogwheel", "create:cogwheel"]
      t: Large→small cogwheel doubles RPM. Chain a few to go from 16 to 128 RPM; a Rotation Speed Controller sets any exact speed up to 256.
    - i: ["create:water_wheel"]
      t: |-
        Water wheels: 32 SU/RPM, cheap but weak; Large Water Wheel 128 SU/RPM. Windmills win on skyblock.
  calc:
    rpm: 64
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
# Free rotation (Create)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `create_power` · **Tags:** Infinite source

**Era setup:** [Steam &amp; Create](../../eras/steam.md)

**Plan modules:** [Steam engines + generator coils](../../plan/p1.md#power)

**Tips:** 5

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod gt-gen" id="m-wm">
<div class="gt-head"><span class="gt-mname">Windmill + sails</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__windmill_bearing.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Shafts (create:shaft) - SU"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span><b class="gt-q">SU</b></span></div>
</div>
<div class="gt-foot"><code>create:windmill_bearing</code></div>
</div>
<div class="gt-panel t-mod gt-gen" id="m-ww">
<div class="gt-head"><span class="gt-mname">Water Wheel</span><span class="gt-badge t-mod">Create</span><span class="gt-badge t-gen">Generator</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-empty">no listed input</span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__water_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="Shafts (create:shaft) - SU"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span><b class="gt-q">SU</b></span></div>
</div>
<div class="gt-foot"><code>create:water_wheel</code></div>
</div>
<div class="gt-panel t-mod" id="m-pr">
<div class="gt-head"><span class="gt-mname">Press</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shafts (create:shaft)"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_press.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>create:mechanical_press</code></div>
</div>
<div class="gt-panel t-mod" id="m-mx">
<div class="gt-head"><span class="gt-mname">Heated Mixer</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shafts (create:shaft)"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__mechanical_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>create:mechanical_mixer</code></div>
</div>
<div class="gt-panel t-mod" id="m-cw">
<div class="gt-head"><span class="gt-mname">Crushing Wheels</span><span class="gt-badge t-mod">Create</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shafts (create:shaft)"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create__crushing_wheel.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>create:crushing_wheel</code></div>
</div>
<div class="gt-panel t-mod" id="m-gc">
<div class="gt-head"><span class="gt-mname">Generator Coil</span><span class="gt-badge t-mod">New Age</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Shafts (create:shaft)"><img class="gt-ico" src="../../assets/icons/create__shaft.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Shaft</span><span class="gt-note">Shafts</span></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/create_new_age__generator_coil.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>create_new_age:generator_coil</code></div>
</div>
</div>

## Flow

- [Windmill + sails](#m-wm) → [Press](#m-pr) (also Windmill + sails → [Heated Mixer](#m-mx), Windmill + sails → [Crushing Wheels](#m-cw), Windmill + sails → [Generator Coil](#m-gc))
- [Water Wheel](#m-ww) → [Heated Mixer](#m-mx) (also Water Wheel → [Press](#m-pr), Water Wheel → [Crushing Wheels](#m-cw), Water Wheel → [Generator Coil](#m-gc))
- [Crushing Wheels](#m-cw)
- [Generator Coil](#m-gc)

## How to build

1. Windmill Bearing + at least 8 sails (pack minimum). Every 8 sails add 1 RPM, up to 16 RPM with 128 sails. — `create:windmill_bearing`, `create:white_sail`
2. Capacity is 512 SU per RPM of the windmill: 16 RPM → 8 192 SU. Gearing up keeps the SU total; the faster you run machines, the fewer you can power. — `create:windmill_bearing`
3. Large→small cogwheel doubles RPM. Chain a few to go from 16 to 128 RPM; a Rotation Speed Controller sets any exact speed up to 256. — `create:large_cogwheel`, `create:cogwheel`
4. Water wheels: 32 SU/RPM, cheap but weak; Large Water Wheel 128 SU/RPM. Windmills win on skyblock. — `create:water_wheel`

## Tips

- More sails = more stress capacity.
- Encased fan at max RPM superheats the Basic Burner (32× fuel).
- Past EV Create adds nothing.
- Big option: Huge Diesel Engine on crude biodiesel gives 12 288 SU at 224 RPM per engine; 208 engines = 2.56 M SU. Create mixer: 100 plant oil + 100 ethanol → 200 biodiesel. Unverified in game: the burn rate (config 0.05).
- Biodiesel without oil: LCR (LV recipe), 54 B fish oil + 9 B ethanol or methanol + NaOH dust → 54 B biodiesel + 9 B glycerol in 270 s. Fish oil needs fish: the only fish source in the pack is the Industrial Fishery (IV controller).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `create:windmill_bearing` | 1 |
| `create:white_sail` | 24 |
| `create:shaft` | 8 |
| `create:cogwheel` | 4 |
| `create:large_cogwheel` | 2 |
| `create:gearbox` | 2 |

## Extras

- Power calculator defaults are stored in the front matter (`calc`).
