---
kind: chain
id: uhv_zirconium
order: 1790
data:
  t: |-
    Zirconium from titanite: perchloric acid leach, slurry, hydroxide, chloride, hydrogen reduction - 8 titanite dust per 1 zirconium dust
  inf: true
  "n":
    - - g1
      - "8 titanite dust · 3 B perchloric acid"
      - g
      - functionalstorage:oak_1
      - [[Titanite dust, "gtceu:titanite_dust"], [Perchloric acid, "gtceu:perchloric_acid_bucket"]]
    - [m1, "LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry", m, "gtceu:luv_mixer"]
    - - m2
      - LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water
      - m
      - gtceu:luv_centrifuge
    - - g2
      - "6 sodium hydroxide dust"
      - g
      - functionalstorage:oak_1
      - [[Sodium hydroxide dust, "gtceu:sodium_hydroxide_dust"]]
    - [m3, "LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture", m, "gtceu:large_chemical_reactor"]
    - - m4
      - ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water
      - m
      - gtceu:zpm_electrolyzer
    - - g3
      - "2 carbon dust · 8 B hydrochloric acid"
      - g
      - functionalstorage:oak_1
      - [[Carbon dust, "gtceu:carbon_dust"], [Hydrochloric acid, "gtceu:hydrochloric_acid_bucket"]]
    - [m5, "LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol", m, "gtceu:large_chemical_reactor"]
    - [m6, "LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4", m, "gtceu:luv_centrifuge"]
    - [g4, "4 B hydrogen", g, "functionalstorage:oak_1", [[Hydrogen, "gtceu:hydrogen_bucket"]]]
    - [m7, "LCR · 30 s · 1640 EU/t → 1 zirconium dust + 4 B HCl", m, "gtceu:large_chemical_reactor"]
    - - lp
      - |-
        Loop: 11 calcium perchlorate + 1 B sulfuric → 2 B perchloric acid; 1 B silica gel → 1 B perchloric acid (centrifuge 6 s)
      - x
      - gtceu:perchloric_acid_bucket
    - [zr, Zirconium dust, o, "gtceu:zirconium_dust"]
  e:
    - [g1, m1, "1"]
    - [m1, m2, "1 B"]
    - [m2, m3, "1 B residue"]
    - [g2, m3, "6"]
    - [m3, m4, "1 B"]
    - [m4, m5, "1 B"]
    - [g3, m5, "1"]
    - [m5, m6, "1 B"]
    - [m6, m7, "5"]
    - [g4, m7, "4 B"]
    - [m7, zr, "1"]
    - [m2, lp, "11 + 1 B"]
    - [lp, g1, "3 B"]
  tips:
    - |-
      Source: kjs additions/progression/lines/abydos_lines/zirconium.js (verified). Titanite dust is processed in: 1) mixer 8 titanite + 3 B perchloric acid → 1 B titanite slurry (400 ticks, 28 000 EU/t); 2) centrifuge 1 B slurry → 11 calcium perchlorate + 1 B slurry residue + 1 B silica gel + 1 B water (360 ticks, 28 000); 3) LCR 6 sodium hydroxide + 1 B residue → 1 B hydroxo dioxo titanite mixture (400 ticks, 17 500); 4) electrolyzer 1 B mixture → 3 sodium oxide + 1 B titanite residue + 1 B water (800 ticks, 50 000); 5) LCR 2 carbon + 1 B residue + 8 B hydrochloric acid → 1 B titanium tetrachloride/zirconium tetrachloride mixture + 2 B methanol (900 ticks, 6400); 6) centrifuge 1 B mixture → 5 zirconium tetrachloride dust + 1 B titanium tetrachloride (1200 ticks, 23 000); 7) LCR 5 ZrCl4 + 4 B hydrogen → 1 zirconium dust + 4 B HCl (600 ticks, 1640).
    - |-
      Perchloric acid loop (same file): the 11 calcium perchlorate dust (step 2) return 2 B acid with 1 B sulfuric acid (chemical reactor or LCR, 120 ticks, 496 EU/t, 6 calcium sulfate dust out); the 1 B silica gel returns 1 B acid in a centrifuge (120 ticks, 1984 EU/t, 3 silicon dioxide out). That is 3 B back for the 3 B used: closed loop, only the sulfuric acid is consumed. First fill: 6 sodium perchlorate dust + 1 B hydrochloric acid → 1 B perchloric acid + 2 salt (200 ticks, 120 EU/t, chemical reactor or LCR).
    - |-
      Yield warning: ONE zirconium dust per 8 titanite dust. A zircalloy-4 batch (uhv_alloys) needs 251 zirconium = 2008 titanite dust; a UV Cyclonic Sifter / destabiliser line gives 22 raw ores per residue run of which 8 are titanite on the refractory magma, so a batch of zircalloy-4 is on the order of 250 residue runs. Zirconium is also in the astrenalloy and hafnide lines, the UHV fusion reactor plates and ZSD (1 per 4). Plan this line early, big.
    - |-
      Source and coil (verified): titanite exists only in Abydos (refractory vein weight 3, 4 raw titanite per refractory magma run), and zirconium has no other source in the scripts. The alloy zircalloy-4 (251 Zr + 3 Sn + 2 Cr + 1 Fe, EBF 9100 K, VA[LuV], 1800 ticks) is above the 9001 K trinium coil, so it needs TRITANIUM coils (10 800 K). Tritanium coil block: assembler at 491 520 EU/t (a UV hatch): trinaquadalloy frame + 8 tritanium double wire + 8 naquadria foil + 32 niobium nitride foil + 144 mB trinium. Zirconium comes right after the Classic Stargate (abydos -> uvzirconium).
    - |-
      Machine tiers: 28 000 EU/t needs LuV, 17 500 LuV (LCR on a LuV hatch), 50 000 ZPM, 23 000 LuV, 6400 IV, 1640 EV. Large Chemical Reactors on a ZPM hatch run every step except the electrolyzer.
    - |-
      Sub-steps people skip: (1) three centrifuges and three LCRs: one machine per step; (2) sodium hydroxide dust is consumed 6 per run (Unverified source); (3) hydrochloric acid out of step 7 (4 B) goes back into step 5 (8 B); (4) keep methanol and water drums empty or voided.
    - |-
      Unverified: sodium hydroxide, sodium perchlorate and carbon supply, titanite ore chain (dust from raw titanite by the ore line).
  b:
    - ["gtceu:large_chemical_reactor", 3]
    - ["gtceu:luv_mixer", 1]
    - ["gtceu:luv_centrifuge", 2]
    - ["gtceu:zpm_electrolyzer", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 8]
    - ["gtceu:lv_robot_arm", 8]
    - ["gtceu:item_filter", 10]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 10]
    - ["gtceu:steel_drum", 10]
  how:
    - i: ["functionalstorage:oak_1", "gtceu:titanite_dust", "gtceu:sodium_hydroxide_dust", "gtceu:carbon_dust"]
      t: |-
        Drawers first: titanite (Keep Exact 8), sodium hydroxide (6), carbon (2), zirconium output; drums: perchloric acid, slurry, residue, mixture, TiCl4, hydrochloric acid, hydrogen, methanol, sulfuric acid.
    - i: ["gtceu:luv_mixer", "gtceu:luv_centrifuge"]
      t: Slurry mixer then the first centrifuge; calcium perchlorate and silica gel go straight into the acid loop machines.
    - i: ["gtceu:large_chemical_reactor", "gtceu:zpm_electrolyzer"]
      t: |-
        Hydroxide LCR → ZPM electrolyzer → chloride LCR: one pipe each; water and sodium oxide to drains.
    - i: ["gtceu:luv_centrifuge", "gtceu:zirconium_dust"]
      t: Second centrifuge splits ZrCl4 from TiCl4; the final LCR reduces ZrCl4 with hydrogen. Output drawer Keep Exact 64 for zirconium dust.
    - i: ["gtceu:perchloric_acid_bucket", "functionalstorage:oak_1"]
      t: |-
        Loop machines: calcium perchlorate + sulfuric acid, and silica gel centrifuge, both back into the perchloric acid drum.
    - i: ["gtceu:zirconium_dust", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: a single zircalloy batch eats 251 dust: stock ahead and make several lines in parallel.
---
# Zirconium from titanite: perchloric acid leach, slurry, hydroxide, chloride, hydrogen reduction - 8 titanite dust per 1 zirconium dust

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `uhv_zirconium` · **Tags:** Infinite source, Unverified

**Era setup:** [UHV · Ancient Gate](../../eras/uhv.md)

**Plan modules:** [Zirconium (needed by the UV reflectors)](../../plan/p14.md#uvzirconium)

**Tips:** 7, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-luv" id="m-m1">
<div class="gt-head"><span class="gt-mname">LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-group" title="8 titanite dust · 3 B perchloric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">8 titanite dust · 3 B perchloric acid</span><span class="gt-sub"><span>Titanite dust</span><span>Perchloric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m2" title="LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water (gtceu:luv_centrifuge) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Centrifuge</span><span class="gt-note">LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:luv_mixer</code></div>
</div>
<div class="gt-panel t-luv" id="m-m2">
<div class="gt-head"><span class="gt-mname">LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m1" title="LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry (gtceu:luv_mixer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__luv_mixer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Mixer</span><span class="gt-note">LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture (gtceu:large_chemical_reactor) - 1 B residue"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture</span><b class="gt-q">1 B residue</b></a><span class="gt-slot" title="Loop: 11 calcium perchlorate + 1 B sulfuric → 2 B perchloric acid; 1 B silica gel → 1 B perchloric acid (centrifuge 6 s) (gtceu:perchloric_acid_bucket) - 11 + 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__perchloric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Perchloric Acid Bucket</span><span class="gt-note">Loop: 11 calcium perchlorate + 1 B sulfuric → 2 B perchloric acid; 1 B silica gel → 1 B perchloric acid (centrifuge 6 s)</span><b class="gt-q">11 + 1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:luv_centrifuge</code></div>
</div>
<div class="gt-panel t-multi" id="m-m3">
<div class="gt-head"><span class="gt-mname">LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m2" title="LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water (gtceu:luv_centrifuge) - 1 B residue"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Centrifuge</span><span class="gt-note">LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water</span><b class="gt-q">1 B residue</b></a><span class="gt-slot gt-group" title="6 sodium hydroxide dust (functionalstorage:oak_1) - 6"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">6 sodium hydroxide dust</span><span class="gt-sub"><span>Sodium hydroxide dust</span></span><b class="gt-q">6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m4" title="ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water (gtceu:zpm_electrolyzer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electrolyzer</span><span class="gt-note">ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-zpm" id="m-m4">
<div class="gt-head"><span class="gt-mname">ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water</span><span class="gt-badge t-zpm">ZPM</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m3" title="LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 131 072 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:zpm_electrolyzer</code></div>
</div>
<div class="gt-panel t-multi" id="m-m5">
<div class="gt-head"><span class="gt-mname">LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m4" title="ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water (gtceu:zpm_electrolyzer) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__zpm_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">ZPM Electrolyzer</span><span class="gt-note">ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water</span><b class="gt-q">1 B</b></a><span class="gt-slot gt-group" title="2 carbon dust · 8 B hydrochloric acid (functionalstorage:oak_1) - 1"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">2 carbon dust · 8 B hydrochloric acid</span><span class="gt-sub"><span>Carbon dust</span><span>Hydrochloric acid</span></span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m6" title="LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4 (gtceu:luv_centrifuge) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Centrifuge</span><span class="gt-note">LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4</span><b class="gt-q">1 B</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-luv" id="m-m6">
<div class="gt-head"><span class="gt-mname">LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4</span><span class="gt-badge t-luv">LuV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m5" title="LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol (gtceu:large_chemical_reactor) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol</span><b class="gt-q">1 B</b></a></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 768 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><a class="gt-slot gt-mach" href="#m-m7" title="LCR · 30 s · 1640 EU/t → 1 zirconium dust + 4 B HCl (gtceu:large_chemical_reactor) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Large Chemical Reactor</span><span class="gt-note">LCR · 30 s · 1640 EU/t → 1 zirconium dust + 4 B HCl</span><b class="gt-q">5</b></a></div>
</div>
<div class="gt-foot"><code>gtceu:luv_centrifuge</code></div>
</div>
<div class="gt-panel t-multi" id="m-m7">
<div class="gt-head"><span class="gt-mname">LCR · 30 s · 1640 EU/t → 1 zirconium dust + 4 B HCl</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><a class="gt-slot gt-mach" href="#m-m6" title="LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4 (gtceu:luv_centrifuge) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__luv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">LuV Centrifuge</span><span class="gt-note">LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4</span><b class="gt-q">5</b></a><span class="gt-slot gt-group" title="4 B hydrogen (functionalstorage:oak_1) - 4 B"><img class="gt-ico" src="../../assets/icons/functionalstorage__oak_1.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Oak 1</span><span class="gt-note">4 B hydrogen</span><span class="gt-sub"><span>Hydrogen</span></span><b class="gt-q">4 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Zirconium dust (gtceu:zirconium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__zirconium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Zirconium Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry](#m-m1) → [LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water](#m-m2) → [LCR · 20 s · 17 500 EU/t → 1 B hydroxo dioxo titanite mixture](#m-m3) → [ZPM Electrolyzer · 40 s · 50 000 EU/t → 3 sodium oxide + 1 B titanite residue + 1 B water](#m-m4) → [LCR · 45 s · 6400 EU/t → 1 B TiCl4/ZrCl4 mixture + 2 B methanol](#m-m5) → [LuV Centrifuge · 60 s · 23 000 EU/t → 5 zirconium tetrachloride + 1 B TiCl4](#m-m6) → [LCR · 30 s · 1640 EU/t → 1 zirconium dust + 4 B HCl](#m-m7) (also LuV Centrifuge · 18 s · 28 000 EU/t → 11 calcium perchlorate + 1 B residue + 1 B silica gel + 1 B water → [LuV Mixer · 20 s · 28 000 EU/t → 1 B titanite slurry](#m-m1))

### Direct steps

- Loop: 11 calcium perchlorate + 1 B sulfuric → 2 B perchloric acid; 1 B silica gel → 1 B perchloric acid (centrifuge 6 s) → 8 titanite dust · 3 B perchloric acid (3 B)

## How to build

1. Drawers first: titanite (Keep Exact 8), sodium hydroxide (6), carbon (2), zirconium output; drums: perchloric acid, slurry, residue, mixture, TiCl4, hydrochloric acid, hydrogen, methanol, sulfuric acid. — `functionalstorage:oak_1`, `gtceu:titanite_dust`, `gtceu:sodium_hydroxide_dust`, `gtceu:carbon_dust`
2. Slurry mixer then the first centrifuge; calcium perchlorate and silica gel go straight into the acid loop machines. — `gtceu:luv_mixer`, `gtceu:luv_centrifuge`
3. Hydroxide LCR → ZPM electrolyzer → chloride LCR: one pipe each; water and sodium oxide to drains. — `gtceu:large_chemical_reactor`, `gtceu:zpm_electrolyzer`
4. Second centrifuge splits ZrCl4 from TiCl4; the final LCR reduces ZrCl4 with hydrogen. Output drawer Keep Exact 64 for zirconium dust. — `gtceu:luv_centrifuge`, `gtceu:zirconium_dust`
5. Loop machines: calcium perchlorate + sulfuric acid, and silica gel centrifuge, both back into the perchloric acid drum. — `gtceu:perchloric_acid_bucket`, `functionalstorage:oak_1`
6. Easy to miss: a single zircalloy batch eats 251 dust: stock ahead and make several lines in parallel. — `gtceu:zirconium_dust`, `functionalstorage:oak_1`

## Tips

- Source: kjs additions/progression/lines/abydos\_lines/zirconium.js (verified). Titanite dust is processed in: 1) mixer 8 titanite + 3 B perchloric acid → 1 B titanite slurry (400 ticks, 28 000 EU/t); 2) centrifuge 1 B slurry → 11 calcium perchlorate + 1 B slurry residue + 1 B silica gel + 1 B water (360 ticks, 28 000); 3) LCR 6 sodium hydroxide + 1 B residue → 1 B hydroxo dioxo titanite mixture (400 ticks, 17 500); 4) electrolyzer 1 B mixture → 3 sodium oxide + 1 B titanite residue + 1 B water (800 ticks, 50 000); 5) LCR 2 carbon + 1 B residue + 8 B hydrochloric acid → 1 B titanium tetrachloride/zirconium tetrachloride mixture + 2 B methanol (900 ticks, 6400); 6) centrifuge 1 B mixture → 5 zirconium tetrachloride dust + 1 B titanium tetrachloride (1200 ticks, 23 000); 7) LCR 5 ZrCl4 + 4 B hydrogen → 1 zirconium dust + 4 B HCl (600 ticks, 1640).
- Perchloric acid loop (same file): the 11 calcium perchlorate dust (step 2) return 2 B acid with 1 B sulfuric acid (chemical reactor or LCR, 120 ticks, 496 EU/t, 6 calcium sulfate dust out); the 1 B silica gel returns 1 B acid in a centrifuge (120 ticks, 1984 EU/t, 3 silicon dioxide out). That is 3 B back for the 3 B used: closed loop, only the sulfuric acid is consumed. First fill: 6 sodium perchlorate dust + 1 B hydrochloric acid → 1 B perchloric acid + 2 salt (200 ticks, 120 EU/t, chemical reactor or LCR).
- Yield warning: ONE zirconium dust per 8 titanite dust. A zircalloy-4 batch (uhv\_alloys) needs 251 zirconium = 2008 titanite dust; a UV Cyclonic Sifter / destabiliser line gives 22 raw ores per residue run of which 8 are titanite on the refractory magma, so a batch of zircalloy-4 is on the order of 250 residue runs. Zirconium is also in the astrenalloy and hafnide lines, the UHV fusion reactor plates and ZSD (1 per 4). Plan this line early, big.
- Source and coil (verified): titanite exists only in Abydos (refractory vein weight 3, 4 raw titanite per refractory magma run), and zirconium has no other source in the scripts. The alloy zircalloy-4 (251 Zr + 3 Sn + 2 Cr + 1 Fe, EBF 9100 K, VA\[LuV\], 1800 ticks) is above the 9001 K trinium coil, so it needs TRITANIUM coils (10 800 K). Tritanium coil block: assembler at 491 520 EU/t (a UV hatch): trinaquadalloy frame + 8 tritanium double wire + 8 naquadria foil + 32 niobium nitride foil + 144 mB trinium. Zirconium comes right after the Classic Stargate (abydos -&gt; uvzirconium).
- Machine tiers: 28 000 EU/t needs LuV, 17 500 LuV (LCR on a LuV hatch), 50 000 ZPM, 23 000 LuV, 6400 IV, 1640 EV. Large Chemical Reactors on a ZPM hatch run every step except the electrolyzer.
- Sub-steps people skip: (1) three centrifuges and three LCRs: one machine per step; (2) sodium hydroxide dust is consumed 6 per run (Unverified source); (3) hydrochloric acid out of step 7 (4 B) goes back into step 5 (8 B); (4) keep methanol and water drums empty or voided.
- **Unverified** sodium hydroxide, sodium perchlorate and carbon supply, titanite ore chain (dust from raw titanite by the ore line).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:large_chemical_reactor` | 3 |
| `gtceu:luv_mixer` | 1 |
| `gtceu:luv_centrifuge` | 2 |
| `gtceu:zpm_electrolyzer` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 8 |
| `gtceu:lv_robot_arm` | 8 |
| `gtceu:item_filter` | 10 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 10 |
| `gtceu:steel_drum` | 10 |

## Needs / Feeds

- **Main source for:** `gtceu:zirconium_dust`, `gtceu:titanite_dust`, `gtceu:perchloric_acid_bucket`
