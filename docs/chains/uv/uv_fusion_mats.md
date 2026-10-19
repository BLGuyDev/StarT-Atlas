---
kind: chain
id: uv_fusion_mats
order: 1630
data:
  t: |-
    Fusion metals: lutetium → americium, gallium + radon → duranium → tritanium, then neutronium (americium + naquadria); everything but neutronium runs in the ZPM Fusion Reactor (MK II) with tier-2/3 reflectors, neutronium needs the UV reactor (MK III)
  inf: true
  "n":
    - - g1
      - "144 mB lanthanum · 144 mB silicon"
      - g
      - functionalstorage:oak_1
      - [[Lanthanum, "gtceu:lanthanum_bucket"], [Silicon, "gtceu:silicon_bucket"]]
    - - m1
      - Fusion · reflector tier 1 · 7.2 s · 7680 EU/t · start 80 MEU (MK II) → 144 mB lutetium
      - m
      - start_core:zpm_fusion_reactor
    - [g2, "144 mB chromium", g, "functionalstorage:oak_1", [[Chromium, "gtceu:chromium_bucket"]]]
    - - m2
      - Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium
      - m
      - start_core:zpm_fusion_reactor
    - - g3
      - "144 mB gallium · 1 B radon"
      - g
      - functionalstorage:oak_1
      - [[Gallium, "gtceu:gallium_bucket"], [Radon, "gtceu:radon_bucket"]]
    - - m3
      - Fusion · tier 2 · 28.8 s · 16 384 EU/t · start 170 MEU (MK II) → 144 mB duranium
      - m
      - start_core:zpm_fusion_reactor
    - [g4, "288 mB titanium", g, "functionalstorage:oak_1", [[Titanium, "gtceu:titanium_bucket"]]]
    - - m4
      - Fusion · tier 3 · 21.6 s · 30 720 EU/t · start 200 MEU (MK II, T3 reflectors) → 144 mB tritanium
      - m
      - start_core:zpm_fusion_reactor
    - [g5, "288 mB naquadria", g, "functionalstorage:oak_1", [[Naquadria, "gtceu:naquadria_bucket"]]]
    - - m5
      - Fusion · tier 3 · 72 s · 117 964 EU/t · start 600 MEU (needs MK III, 640 MEU buffer) → 144 mB neutronium
      - m
      - start_core:uv_fusion_reactor
    - [nt, "Neutronium (the UV exit item)", o, "gtceu:neutronium_ingot"]
    - [tt, "Tritanium → frames, plates", o, "gtceu:tritanium_ingot"]
  e:
    - [g1, m1, "1 : 1"]
    - [m1, m2, "144 mB"]
    - [g2, m2, "1"]
    - [g3, m3, "1"]
    - [m3, m4, "144 mB"]
    - [g4, m4, "2"]
    - [m4, tt, "144 mB"]
    - [m2, m5, "216 mB"]
    - [g5, m5, "2"]
    - [m5, nt, "144 mB / 72 s"]
  tips:
    - |-
      Source: kjs systems/fusion/fusion_scaling.js (all verified; the pack removes every GT fusion recipe and adds its own `reflector_fusion_reactor` recipes with a reflector tier). Numbers: lutetium = lanthanum + silicon (tier 1, 7680 EU/t, 7.2 s, 80 MEU); americium = lutetium + chromium (tier 3, 49 152 EU/t, 14.4 s, 200 MEU); duranium = gallium + 1 B radon (tier 2, 16 384 EU/t, 28.8 s, 170 MEU); tritanium = 288 mB titanium + 144 mB duranium (tier 3, 30 720 EU/t, 21.6 s, 200 MEU); neutronium = 216 mB americium + 288 mB naquadria (tier 3, 117 964 EU/t, 72 s, 600 MEU). Radon: 144 mB gold + 100 mB mercury (tier 1, 30 720 EU/t, 28.8 s, 200 MEU).
    - |-
      Reflector tiers (start_fusion_machines.js): tier 1 basic, 2 advanced (zpm_fusion), 3 COMPLEX reflector casing. Complex casing = 2 advanced reflector casings + 1 ZPM field generator + 6 complex neutron reflector panels + 4 YBCO single cables + 24 trinium foil + 288 mB PEEK (reflectorBlock tier 3, cleanroom assembler, 400 ticks at VA[EV] x 4^3 = 122 880 EU/t, 2 per craft). Complex panel = 1 trinaquadalloy plate + 2 double zirconium plates + 1 advanced panel + 2304 mB soldering alloy (cleanroom assembler, 1000 ticks at VHA[LuV]). Tier 4 (reinforced) and above need a sterile cleanroom and belong to the UHV page.
    - |-
      Neutronium is the UV era exit item: 144 mB per run, so 1 ingot per 72 s per reactor; one UHV hull is 8 plates = 1152 mB = 8 runs = 9.6 min, plus the hatches. The recipe needs 600 MEU to start: the start_core reactor buffers are 160 / 320 / 640 MEU for MK I / II / III (reactor descriptions in the jar lang), so only the UV reactor (MK III) can start it. The others in this chain (lutetium 80, duranium 170, americium 200, tritanium 200 MEU) fit the 320 MEU MK II, so tritanium, and with it zapolgium, tritan steel and the wetware mainframe frames, do NOT wait for the UV reactor; tier-3 recipes only need tier-3 reflectors.
    - Americium is also the wire for the UV motor (64 fine americium wire = 8 ingots per motor) and the UV fusion reactor plate (double americium plate). Tritanium is the frame of the wetware mainframe (2 per craft) and of the sterilizing filter casing, and the wire material of the UV voltage coil (16 fine tritanium wire = 2 ingots per coil).
    - |-
      Sub-steps people skip: (1) each fusion run needs its fluids in the hatch in the right proportions: use fluid drums with Keep Exact valves, never overfill one input; (2) swap the recipe by emptying both input hatches first, a half-filled hatch locks the wrong recipe; (3) products are molten metals: send them to a fluid solidifier (ingot mold) or keep the fluid for the Alloy Blast Smelter; (4) keep the reactor feeding itself with radon and duranium before tritanium.
    - |-
      Unverified: lanthanum, silicon (EV), chromium (nichrome_line source), gallium and naquadria routes (zpm_naq_products) are earlier chains.
  b:
    - ["start_core:uv_fusion_reactor", 1]
    - ["start_core:zpm_fusion_reactor", 1]
    - ["kubejs:complex_reflector_casing", 16]
    - ["gtceu:power_substation", 1]
    - ["gtceu:lv_fluid_solidifier", 1]
    - ["functionalstorage:oak_1", 2]
    - ["modularrouters:modular_router", 4]
    - ["gtceu:lv_robot_arm", 4]
    - ["gtceu:item_filter", 4]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["start_core:uv_fusion_reactor", "kubejs:complex_reflector_casing", "gtceu:power_substation"]
      t: |-
        Prerequisites: a ZPM Fusion Reactor (MK II, zpm_fusion) with tier-3 complex reflector casings in its reflector ring for lutetium to tritanium (80 to 200 MEU); the UV Fusion Reactor (uv_fusion, MK III) only for the 600 MEU neutronium run. Plus a Power Substation (or a big battery bank) for the start energy. Output hatches go to drums.
    - i: ["start_core:uv_fusion_reactor", "gtceu:lutetium_bucket", "gtceu:americium_bucket"]
      t: |-
        Run 1: lutetium (lanthanum + silicon, 7.2 s), then americium (lutetium + chromium, 14.4 s). Americium drum buffer 1 B.
    - i: ["start_core:uv_fusion_reactor", "gtceu:duranium_bucket", "gtceu:tritanium_bucket"]
      t: |-
        Run 2: duranium (gallium + 1 B radon, 28.8 s), then tritanium (288 mB titanium + 144 mB duranium, 21.6 s).
    - i: ["start_core:uv_fusion_reactor", "gtceu:neutronium_bucket", "gtceu:naquadria_bucket"]
      t: |-
        Run 3: neutronium (216 mB americium + 288 mB naquadria, 72 s). One run uses the americium of 1.5 americium runs.
    - i: ["gtceu:lv_fluid_solidifier", "gtceu:neutronium_ingot"]
      t: Solidifier (ingot mold) for neutronium and tritanium; the other molten metals stay as fluids for the ABS and the component recipes.
    - i: ["functionalstorage:oak_1", "gtceu:neutronium_ingot"]
      t: Output drawer Keep Exact 8; this is the exit item of the era.
---
# Fusion metals: lutetium → americium, gallium + radon → duranium → tritanium, then neutronium (americium + naquadria); everything but neutronium runs in the ZPM Fusion Reactor (MK II) with tier-2/3 reflectors, neutronium needs the UV reactor (MK III)

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uv_fusion_mats` · **Tags:** Infinite source, Unverified

**Era setup:** [UV · Abydos](../../eras/uv.md)

**Plan modules:** [UV Fusion Reactor and fusion metals](../../plan/p15.md#uvfusion)

**Tips:** 6, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-zpm" id="m-m1">
<div class="gt-head"><span class="gt-mname">Fusion · reflector tier 1 · 7.2 s · 7680 EU/t · start 80 MEU (MK II) → 144 mB lutetium</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="144 mB lanthanum · 144 mB silicon (functionalstorage:oak_1) - 1 : 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">144 mB lanthanum · 144 mB silicon</span><span class="gt-sub"><span>Lanthanum</span><span>Silicon</span></span><b class="gt-q">1 : 1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium (start_core:zpm_fusion_reactor) - 144 mB"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium</span><b class="gt-q">144 mB</b></a></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m2">
<div class="gt-head"><span class="gt-mname">Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="Fusion · reflector tier 1 · 7.2 s · 7680 EU/t · start 80 MEU (MK II) → 144 mB lutetium (start_core:zpm_fusion_reactor) - 144 mB"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">Fusion · reflector tier 1 · 7.2 s · 7680 EU/t · start 80 MEU (MK II) → 144 mB lutetium</span><b class="gt-q">144 mB</b></a><span class="gt-slot gt-group" title="144 mB chromium (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">144 mB chromium</span><span class="gt-sub"><span>Chromium</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="Fusion · tier 3 · 72 s · 117 964 EU/t · start 600 MEU (needs MK III, 640 MEU buffer) → 144 mB neutronium (start_core:uv_fusion_reactor) - 216 mB"><img class="gt-ico" src="../../assets/icons/start_core__uv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">UV Fusion Reactor</span><span class="gt-note">Fusion · tier 3 · 72 s · 117 964 EU/t · start 600 MEU (needs MK III, 640 MEU buffer) → 144 mB neutronium</span><b class="gt-q">216 mB</b></a></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m3">
<div class="gt-head"><span class="gt-mname">Fusion · tier 2 · 28.8 s · 16 384 EU/t · start 170 MEU (MK II) → 144 mB duranium</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="144 mB gallium · 1 B radon (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">144 mB gallium · 1 B radon</span><span class="gt-sub"><span>Gallium</span><span>Radon</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m4" title="Fusion · tier 3 · 21.6 s · 30 720 EU/t · start 200 MEU (MK II, T3 reflectors) → 144 mB tritanium (start_core:zpm_fusion_reactor) - 144 mB"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">Fusion · tier 3 · 21.6 s · 30 720 EU/t · start 200 MEU (MK II, T3 reflectors) → 144 mB tritanium</span><b class="gt-q">144 mB</b></a></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m4">
<div class="gt-head"><span class="gt-mname">Fusion · tier 3 · 21.6 s · 30 720 EU/t · start 200 MEU (MK II, T3 reflectors) → 144 mB tritanium</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="Fusion · tier 2 · 28.8 s · 16 384 EU/t · start 170 MEU (MK II) → 144 mB duranium (start_core:zpm_fusion_reactor) - 144 mB"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">Fusion · tier 2 · 28.8 s · 16 384 EU/t · start 170 MEU (MK II) → 144 mB duranium</span><b class="gt-q">144 mB</b></a><span class="gt-slot gt-group" title="288 mB titanium (functionalstorage:oak_1) - 2"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">288 mB titanium</span><span class="gt-sub"><span>Titanium</span></span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Tritanium → frames, plates (gtceu:tritanium_ingot) - 144 mB"><img class="gt-ico" src="../../assets/icons/gtceu__tritanium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Tritanium Ingot</span><span class="gt-note">Tritanium → frames, plates</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:zpm_fusion_reactor</code></div>
</div>
<div class="gt-panel t-uv" id="m-m5">
<div class="gt-head"><span class="gt-mname">Fusion · tier 3 · 72 s · 117 964 EU/t · start 600 MEU (needs MK III, 640 MEU buffer) → 144 mB neutronium</span><span class="gt-badge t-uv">UV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium (start_core:zpm_fusion_reactor) - 216 mB"><img class="gt-ico" src="../../assets/icons/start_core__zpm_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Fusion Reactor</span><span class="gt-note">Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium</span><b class="gt-q">216 mB</b></a><span class="gt-slot gt-group" title="288 mB naquadria (functionalstorage:oak_1) - 2"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">288 mB naquadria</span><span class="gt-sub"><span>Naquadria</span></span><b class="gt-q">2</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/start_core__uv_fusion_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 524 288 EU/t</span><span class="gt-stat">72 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Neutronium (the UV exit item) (gtceu:neutronium_ingot) - 144 mB / 72 s"><img class="gt-ico" src="../../assets/icons/gtceu__neutronium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Neutronium Ingot</span><span class="gt-note">Neutronium (the UV exit item)</span><b class="gt-q">144 mB</b></span></div>
</div>
<div class="gt-foot"><code>start_core:uv_fusion_reactor</code></div>
</div>
</div>

## Flow

- [Fusion · reflector tier 1 · 7.2 s · 7680 EU/t · start 80 MEU (MK II) → 144 mB lutetium](#m-m1) → [Fusion · tier 3 · 14.4 s · 49 152 EU/t · start 200 MEU (MK II) → 144 mB americium](#m-m2) → [Fusion · tier 3 · 72 s · 117 964 EU/t · start 600 MEU (needs MK III, 640 MEU buffer) → 144 mB neutronium](#m-m5)
- [Fusion · tier 2 · 28.8 s · 16 384 EU/t · start 170 MEU (MK II) → 144 mB duranium](#m-m3) → [Fusion · tier 3 · 21.6 s · 30 720 EU/t · start 200 MEU (MK II, T3 reflectors) → 144 mB tritanium](#m-m4)

## How to build

1. Prerequisites: a ZPM Fusion Reactor (MK II, zpm\_fusion) with tier-3 complex reflector casings in its reflector ring for lutetium to tritanium (80 to 200 MEU); the UV Fusion Reactor (uv\_fusion, MK III) only for the 600 MEU neutronium run. Plus a Power Substation (or a big battery bank) for the start energy. Output hatches go to drums. — `start_core:uv_fusion_reactor`, `kubejs:complex_reflector_casing`, `gtceu:power_substation`
2. Run 1: lutetium (lanthanum + silicon, 7.2 s), then americium (lutetium + chromium, 14.4 s). Americium drum buffer 1 B. — `start_core:uv_fusion_reactor`, `gtceu:lutetium_bucket`, `gtceu:americium_bucket`
3. Run 2: duranium (gallium + 1 B radon, 28.8 s), then tritanium (288 mB titanium + 144 mB duranium, 21.6 s). — `start_core:uv_fusion_reactor`, `gtceu:duranium_bucket`, `gtceu:tritanium_bucket`
4. Run 3: neutronium (216 mB americium + 288 mB naquadria, 72 s). One run uses the americium of 1.5 americium runs. — `start_core:uv_fusion_reactor`, `gtceu:neutronium_bucket`, `gtceu:naquadria_bucket`
5. Solidifier (ingot mold) for neutronium and tritanium; the other molten metals stay as fluids for the ABS and the component recipes. — `gtceu:lv_fluid_solidifier`, `gtceu:neutronium_ingot`
6. Output drawer Keep Exact 8; this is the exit item of the era. — `functionalstorage:oak_1`, `gtceu:neutronium_ingot`

## Tips

- Source: kjs systems/fusion/fusion\_scaling.js (all verified; the pack removes every GT fusion recipe and adds its own \`reflector\_fusion\_reactor\` recipes with a reflector tier). Numbers: lutetium = lanthanum + silicon (tier 1, 7680 EU/t, 7.2 s, 80 MEU); americium = lutetium + chromium (tier 3, 49 152 EU/t, 14.4 s, 200 MEU); duranium = gallium + 1 B radon (tier 2, 16 384 EU/t, 28.8 s, 170 MEU); tritanium = 288 mB titanium + 144 mB duranium (tier 3, 30 720 EU/t, 21.6 s, 200 MEU); neutronium = 216 mB americium + 288 mB naquadria (tier 3, 117 964 EU/t, 72 s, 600 MEU). Radon: 144 mB gold + 100 mB mercury (tier 1, 30 720 EU/t, 28.8 s, 200 MEU).
- Reflector tiers (start\_fusion\_machines.js): tier 1 basic, 2 advanced (zpm\_fusion), 3 COMPLEX reflector casing. Complex casing = 2 advanced reflector casings + 1 ZPM field generator + 6 complex neutron reflector panels + 4 YBCO single cables + 24 trinium foil + 288 mB PEEK (reflectorBlock tier 3, cleanroom assembler, 400 ticks at VA\[EV\] x 4^3 = 122 880 EU/t, 2 per craft). Complex panel = 1 trinaquadalloy plate + 2 double zirconium plates + 1 advanced panel + 2304 mB soldering alloy (cleanroom assembler, 1000 ticks at VHA\[LuV\]). Tier 4 (reinforced) and above need a sterile cleanroom and belong to the UHV page.
- Neutronium is the UV era exit item: 144 mB per run, so 1 ingot per 72 s per reactor; one UHV hull is 8 plates = 1152 mB = 8 runs = 9.6 min, plus the hatches. The recipe needs 600 MEU to start: the start\_core reactor buffers are 160 / 320 / 640 MEU for MK I / II / III (reactor descriptions in the jar lang), so only the UV reactor (MK III) can start it. The others in this chain (lutetium 80, duranium 170, americium 200, tritanium 200 MEU) fit the 320 MEU MK II, so tritanium, and with it zapolgium, tritan steel and the wetware mainframe frames, do NOT wait for the UV reactor; tier-3 recipes only need tier-3 reflectors.
- Americium is also the wire for the UV motor (64 fine americium wire = 8 ingots per motor) and the UV fusion reactor plate (double americium plate). Tritanium is the frame of the wetware mainframe (2 per craft) and of the sterilizing filter casing, and the wire material of the UV voltage coil (16 fine tritanium wire = 2 ingots per coil).
- Sub-steps people skip: (1) each fusion run needs its fluids in the hatch in the right proportions: use fluid drums with Keep Exact valves, never overfill one input; (2) swap the recipe by emptying both input hatches first, a half-filled hatch locks the wrong recipe; (3) products are molten metals: send them to a fluid solidifier (ingot mold) or keep the fluid for the Alloy Blast Smelter; (4) keep the reactor feeding itself with radon and duranium before tritanium.
- **Unverified** lanthanum, silicon (EV), chromium (nichrome\_line source), gallium and naquadria routes (zpm\_naq\_products) are earlier chains.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `start_core:uv_fusion_reactor` | 1 |
| `start_core:zpm_fusion_reactor` | 1 |
| `kubejs:complex_reflector_casing` | 16 |
| `gtceu:power_substation` | 1 |
| `gtceu:lv_fluid_solidifier` | 1 |
| `functionalstorage:oak_1` | 2 |
| `modularrouters:modular_router` | 4 |
| `gtceu:lv_robot_arm` | 4 |
| `gtceu:item_filter` | 4 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Feeds:** [UHV Machine Hull: neutronium casing + 2 europium cables (PPS foil + PVC foil + silicone) + 288 mB PEEK](../uhv/uhv_hull.md), [Void ingot: echo shard → echo fluid; neutronium ingot + echo fluid → raw void ingot → Heat Chamber → hot void ingot → vacuum freezer](../uhv/uhv_void.md)
- **Main source for:** `gtceu:neutronium_ingot`, `gtceu:neutronium_bucket`, `gtceu:tritanium_ingot`, `gtceu:tritanium_frame`, `gtceu:americium_bucket`, `gtceu:duranium_bucket`, `gtceu:lutetium_bucket`, `kubejs:complex_reflector_casing`
