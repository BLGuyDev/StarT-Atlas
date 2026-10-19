---
kind: chain
id: platline
order: 380
data:
  t: |-
    Platinum group line: sludge → aqua regia centrifuge → platinum, palladium, rhodium, ruthenium, iridium, osmium
  "n":
    - [co, Purified cooperite ore, i, "gtceu:purified_cooperite_ore"]
    - [na, "Nitric acid · 100 mB", f, "gtceu:nitric_acid_bucket"]
    - [r1, "LV Chemical Reactor · 2.5 s · 30 EU/t", m, "gtceu:lv_chemical_reactor"]
    - [sl, "4 Platinum group sludge dust", x, "gtceu:platinum_group_sludge_dust"]
    - [by, "1 B sulfuric nickel solution (void it)", f, "gtceu:fluid_voiding_cover"]
    - [ar, "Aqua regia · 1200 mB per 6 sludge", f, "gtceu:aqua_regia_bucket"]
    - [c1, "HV Centrifuge · 25 s · 480 EU/t", m, "gtceu:hv_centrifuge"]
    - [pr, "3 Raw platinum dust", x, "gtceu:platinum_raw_dust"]
    - [pp, "3 Raw palladium dust", x, "gtceu:palladium_raw_dust"]
    - [im, "2 Inert metal mixture dust", x, "gtceu:inert_metal_mixture_dust"]
    - [rm, "1 Rarest metal mixture dust", x, "gtceu:rarest_metal_mixture_dust"]
    - [rs, "2 Platinum sludge residue (trash)", x, "gtceu:platinum_sludge_residue_dust"]
    - [e1, "MV Electrolyzer · 5 s · 120 EU/t", m, "gtceu:mv_electrolyzer"]
    - [pt, Platinum dust, o, "gtceu:platinum_dust"]
    - [r2, "MV Chemical Reactor · 10 s · 120 EU/t (5 raw + 1 B HCl)", m, "gtceu:mv_chemical_reactor"]
    - [pd, Palladium dust, o, "gtceu:palladium_dust"]
    - [r3, "EV Chemical Reactor · 22.5 s · 1920 EU/t (6 + 1.5 B sulfuric acid)", m, "gtceu:ev_chemical_reactor"]
    - [rt, "5 Ruthenium tetroxide dust", x, "gtceu:ruthenium_tetroxide_dust"]
    - [rhs, "500 mB rhodium sulfate", f, "gtceu:rhodium_sulfate_bucket"]
    - [e2, "MV Electrolyzer · 5 s · 120 EU/t", m, "gtceu:mv_electrolyzer"]
    - [rh, Rhodium dust, o, "gtceu:rhodium_dust"]
    - [r4, "MV Chemical Reactor · 10 s (5 + 2 carbon)", m, "gtceu:mv_chemical_reactor"]
    - [ru, Ruthenium dust, o, "gtceu:ruthenium_dust"]
    - [lc, "Large Chemical Reactor · IV hatch · 20 s · 7680 EU/t (7 + 4 B HCl)", m, "gtceu:large_chemical_reactor"]
    - [ir5, "5 Iridium metal residue", x, "gtceu:iridium_metal_residue_dust"]
    - [os2, "2 B acidic osmium solution", f, "gtceu:acidic_osmium_solution_bucket"]
    - [c2, "MV Centrifuge · 10 s · 120 EU/t", m, "gtceu:mv_centrifuge"]
    - [ic, "4 Iridium chloride dust", x, "gtceu:iridium_chloride_dust"]
    - [r5, "LV Chemical Reactor · 5 s (4 + 3 B hydrogen)", m, "gtceu:lv_chemical_reactor"]
    - [ir, Iridium dust, o, "gtceu:iridium_dust"]
    - [ds, "MV Distillery · 20 s · 120 EU/t", m, "gtceu:mv_distillery"]
    - [ot, "5 Osmium tetroxide dust", x, "gtceu:osmium_tetroxide_dust"]
    - [r6, "LV Chemical Reactor · 10 s (5 + 8 B hydrogen)", m, "gtceu:lv_chemical_reactor"]
    - [os, Osmium dust, o, "gtceu:osmium_dust"]
  e:
    - [co, r1, "1"]
    - [na, r1, "100 mB"]
    - [r1, sl, "4"]
    - [r1, by, "1 B"]
    - [sl, c1, "6"]
    - [ar, c1, "1200 mB"]
    - [c1, pr, "3"]
    - [c1, pp, "3"]
    - [c1, im, "2"]
    - [c1, rm, "1"]
    - [c1, rs, "2"]
    - [pr, e1, "3"]
    - [e1, pt, "1"]
    - [pp, r2, "5"]
    - [r2, pd, "1"]
    - [im, r3, "6"]
    - [r3, rt, "5"]
    - [r3, rhs, "500 mB"]
    - [rhs, e2, "1 B"]
    - [e2, rh, "2"]
    - [rt, r4, "5"]
    - [r4, ru, "1"]
    - [rm, lc, "7"]
    - [lc, ir5, "5"]
    - [lc, os2, "2 B"]
    - [ir5, c2, "5"]
    - [c2, ic, "4"]
    - [ic, r5, "4"]
    - [r5, ir, "1"]
    - [os2, ds, "2 B"]
    - [ds, ot, "5"]
    - [ot, r6, "5"]
    - [r6, os, "1"]
  tips:
    - |-
      Where the numbers come from: PlatGroupMetalsRecipes (the pack leaves the line unchanged except for the ZPM skip below). Per 6 sludge dust the centrifuge makes 3 raw platinum + 3 raw palladium + 2 inert metal mixture + 1 rarest metal mixture + 2 platinum sludge residue. Per 42 sludge (7 runs) the whole line yields 7 platinum, 4.2 palladium, 2.3 ruthenium, 2.3 rhodium, 1 iridium and 1 osmium. A purified cooperite ore gives 4 sludge; chalcopyrite, chalcocite, bornite, tetrahedrite and pentlandite give 2.
    - |-
      Sludge (LV Chemical Reactor, 50 ticks, 30 EU/t): 1 purified ore + 100 mB nitric acid → sludge + 1 B sulfuric nickel solution (cooperite, pentlandite) or sulfuric copper solution (the others). Nothing in the fork uses either solution, so the tank fills and the reactor stops silently. Put a Fluid Voiding Cover on the output hatch or drum (and an Item Voiding Cover on the platinum sludge residue, which is also unused).
    - |-
      Aqua regia: LV Mixer, 1 B nitric acid + 2 B hydrochloric acid → 3 B (30 ticks, 30 EU/t). The centrifuge takes 1200 mB per 6 sludge, so 400 mB nitric acid and 800 mB hydrochloric acid per run. Nitric acid: chemical reactor, circuit 1, 3 B nitrogen dioxide + 1 B water → 2 B nitric acid + 1 B nitric oxide (240 ticks, 30 EU/t); the Large Chemical Reactor does it from ammonia + oxygen (circuit 24).
    - |-
      The step list in the era text says LCR for everything, but only ONE step needs the Large Chemical Reactor: the rarest metal mixture (iridium and osmium) at 7680 EU/t = an IV Energy Hatch on the LCR. The rhodium/ruthenium step is an EV Chemical Reactor (1920 EU/t); the centrifuge is HV (480 EU/t); everything else is LV or MV.
    - |-
      Ruthenium: 6 inert metal mixture → 5 ruthenium tetroxide + 500 mB rhodium sulfate + 3 B hydrogen; then 5 tetroxide + 2 carbon dust → 1 ruthenium (+ 2 B carbon dioxide). So 1 ruthenium = 6 mixture = 18 sludge = 4.5 cooperite ore. The RTM coil chain needs about 4.6 ruthenium per block. This line is the only ruthenium source in the pack (no vein, sieve or fusion recipe gives it; the ZPM Chemical Plant skip is the same line in one recipe) and every stage except iridium and osmium is LV to EV, so ruthenium and the RTM coils never wait for IV. The same mixture gives 1 rhodium per 6 (500 mB rhodium sulfate → 1 rhodium in an electrolyzer, 100 ticks, 120 EU/t), which LuV needs later.
    - |-
      Platinum: 3 raw platinum → 1 platinum + 800 mB chlorine in an MV Electrolyzer. Palladium: 5 raw palladium + 1 B hydrochloric acid → 1 palladium + 2 ammonium chloride dust (MV Chemical Reactor). Platinum is the IV hull and IV cable metal (platinum single cable) and the EV emitter rod; palladium feeds the later chips.
    - |-
      Iridium and osmium: LCR, 7 rarest metal mixture + 4 B hydrochloric acid → 5 iridium metal residue + 2 B acidic osmium solution + 3 B hydrogen (400 ticks, 7680 EU/t). Residue: MV Centrifuge 5 → 4 iridium chloride + 1 platinum sludge residue; then LV Chemical Reactor 4 chloride + 3 B hydrogen → 1 iridium dust + 3 B hydrochloric acid. Osmium: MV distillery 2 B solution → 5 osmium tetroxide + 1 B hydrochloric acid + 1 B water; then LV reactor 5 tetroxide + 8 B hydrogen → 1 osmium + 4 B water. Iridium: 2 per IV emitter (4 rods), 0.5 per sensor.
    - |-
      The ZPM Chemical Plant skip (kjs chemical_plant.js) does the whole line in one recipe: 30 purified cooperite ore + 24 B aqua regia → 20 platinum, 12 palladium, 7 ruthenium, 7 rhodium, 3 osmium, 3 iridium dust (+ 8 B nitric and 16 B hydrochloric acid back), 485 ticks at ZPM. That matches the by-hand yields above, so it is a convenience, not a better ratio; do the manual line first.
    - |-
      Sub-steps people skip: (1) one dedicated machine per recipe, because the reactors share circuit-less recipes with other chains; (2) hydrogen and hydrochloric acid come back as by-products, route them to their drums, do not void them; (3) 3 raw palladium per run is not enough for the 5-raw recipe, so let the raw dust accumulate in a drawer; (4) the by-product voiding above; (5) purify the cooperite first (the ore washer step).
    - |-
      Unverified: where the purified cooperite comes from in practice. The pack sieve (kjs sieving.js) gives crushed cooperite ore at 25 % from crushed blackstone with an emerald mesh, and the ore washer should purify it; read the washer recipe in EMI. Also unverified: whether the single MV Distillery offers the osmium step (the source recipe is a Distillation Tower recipe with an item output); if EMI shows only the tower, use the EV Distillation Tower.
  b:
    - ["gtceu:lv_chemical_reactor", 3]
    - ["gtceu:mv_chemical_reactor", 2]
    - ["gtceu:ev_chemical_reactor", 1]
    - ["gtceu:hv_centrifuge", 1]
    - ["gtceu:mv_centrifuge", 1]
    - ["gtceu:mv_electrolyzer", 2]
    - ["gtceu:lv_mixer", 1]
    - ["gtceu:mv_distillery", 1]
    - ["gtceu:large_chemical_reactor", 1]
    - ["gtceu:iv_energy_input_hatch", 1]
    - ["gtceu:fluid_voiding_cover", 2]
    - ["gtceu:item_voiding_cover", 1]
    - ["functionalstorage:oak_1", 16]
    - ["modularrouters:modular_router", 10]
    - ["gtceu:lv_robot_arm", 12]
    - ["gtceu:item_filter", 12]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 12]
    - ["gtceu:steel_drum", 8]
  inf: true
  how:
    - i:
        - functionalstorage:oak_1
        - gtceu:purified_cooperite_ore
        - gtceu:nitric_acid_bucket
        - gtceu:hydrochloric_acid_bucket
      t: |-
        Buffers first: an ore drawer, drums for nitric acid, hydrochloric acid, aqua regia, sulfuric acid, hydrogen, and a drum or voiding cover for every by-product. Every reactor below is its own machine with its own input drawer and Item Filter route and an output Keep Exact arm, because several of these reactors have circuit-less recipes that compete for the same bus.
    - i: ["gtceu:lv_chemical_reactor", "gtceu:platinum_group_sludge_dust"]
      t: |-
        Sludge reactor (LV Chemical Reactor): 1 purified cooperite ore + 100 mB nitric acid → 4 platinum group sludge dust in 2.5 s at 30 EU/t, plus 1 B sulfuric nickel solution. Put a Fluid Voiding Cover on the by-product hatch before the first run. That is the whole sludge step: the ore and the nitric acid are the only things you have to supply.
    - i: ["gtceu:lv_mixer", "gtceu:aqua_regia_bucket"]
      t: |-
        Aqua regia: LV Mixer, 1 B nitric acid + 2 B hydrochloric acid → 3 B aqua regia, 1.5 s at 30 EU/t. Keep it in its own drum with a pump cover to the centrifuge; never share a drum with plain nitric acid.
    - i: ["gtceu:hv_centrifuge", "gtceu:inert_metal_mixture_dust", "gtceu:rarest_metal_mixture_dust"]
      t: |-
        HV Centrifuge: 6 sludge dust + 1200 mB aqua regia → 3 raw platinum + 3 raw palladium + 2 inert metal mixture + 1 rarest metal mixture + 2 platinum sludge residue, 25 s at 480 EU/t. Five outputs mean five output slots: a Robot Arm cover with an Item Filter per item sends each one to its own drawer, and an Item Voiding Cover takes the residue.
    - i: ["gtceu:mv_electrolyzer", "gtceu:platinum_dust", "gtceu:mv_chemical_reactor", "gtceu:palladium_dust"]
      t: |-
        Platinum and palladium: MV Electrolyzer, 3 raw platinum → 1 platinum + 800 mB chlorine (5 s, 120 EU/t); MV Chemical Reactor, 5 raw palladium + 1 B hydrochloric acid → 1 palladium + 2 ammonium chloride (10 s). Chlorine goes back to the chlorine drum of the MV chain.
    - i: ["gtceu:ev_chemical_reactor", "gtceu:ruthenium_tetroxide_dust", "gtceu:rhodium_sulfate_bucket"]
      t: |-
        Ruthenium and rhodium: EV Chemical Reactor, 6 inert metal mixture + 1.5 B sulfuric acid → 500 mB rhodium sulfate + 5 ruthenium tetroxide + 3 B hydrogen, 22.5 s at 1920 EU/t. The rhodium sulfate goes to an MV Electrolyzer (1 B → 2 rhodium dust + 3 B sulfur trioxide + 3 B oxygen); the tetroxide to an MV Chemical Reactor with 2 carbon dust per 5 → 1 ruthenium dust + 2 B carbon dioxide (10 s).
    - i: ["gtceu:large_chemical_reactor", "gtceu:iv_energy_input_hatch", "gtceu:iridium_metal_residue_dust"]
      t: |-
        The only Large Chemical Reactor step: 7 rarest metal mixture + 4 B hydrochloric acid → 5 iridium metal residue + 2 B acidic osmium solution + 3 B hydrogen, 20 s at 7680 EU/t. It needs an IV Energy Hatch on the LCR (the pack quest chain makes the hatch with the IV Assembler). Mixture arrives through an input bus, the acid through a hatch, residue through an output bus, solution and hydrogen through two output hatches.
    - i: ["gtceu:mv_centrifuge", "gtceu:iridium_chloride_dust", "gtceu:lv_chemical_reactor", "gtceu:iridium_dust"]
      t: |-
        Iridium: MV Centrifuge, 5 residue → 4 iridium chloride + 1 platinum sludge residue (10 s, 120 EU/t), then LV Chemical Reactor, 4 chloride + 3 B hydrogen → 1 iridium dust + 3 B hydrochloric acid (5 s). Iridium dust is an EBF recipe at 4500 K (RTM coils), see the rtm_coil and iv_components chains.
    - i: ["gtceu:mv_distillery", "gtceu:osmium_tetroxide_dust", "gtceu:osmium_dust"]
      t: |-
        Osmium: MV Distillery on the acidic osmium solution, 2 B → 5 osmium tetroxide dust + 1 B hydrochloric acid + 1 B water (20 s, 120 EU/t); then LV Chemical Reactor, 5 tetroxide + 8 B hydrogen → 1 osmium dust + 4 B water (10 s). Osmium is a later metal (its ingot is a LuV furnace recipe), but it comes out of the same LCR run as iridium.
    - i: ["functionalstorage:oak_1", "gtceu:platinum_group_sludge_dust"]
      t: |-
        Easy to miss: the common sulfides give only 2 sludge per ore and cooperite 4, so cooperite is worth a dedicated sieve. When the line stalls, check the by-product hatch of the sludge reactor first, then the hydrogen supply of the iridium and osmium reactors.
---
# Platinum group line: sludge → aqua regia centrifuge → platinum, palladium, rhodium, ruthenium, iridium, osmium

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `platline` · **Tags:** Infinite source, Unverified

**Era setup:** [IV](../../eras/iv.md)

**Plan modules:** [Platinum group line](../../plan/p9.md#platinum)

**Tips:** 10, 1 unverified

## Machines

<div class="gt-panels">
<div class="gt-panel t-lv" id="m-r1">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 2.5 s · 30 EU/t</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Purified cooperite ore (gtceu:purified_cooperite_ore) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__purified_cooperite_ore.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Purified Cooperite Ore</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="Nitric acid · 100 mB (gtceu:nitric_acid_bucket) - 100 mB"><img class="gt-ico" src="../../assets/icons/gtceu__nitric_acid_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nitric Acid</span><span class="gt-note">Nitric acid · 100 mB</span><b class="gt-q">100 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Platinum group sludge dust (gtceu:platinum_group_sludge_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_group_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Group Sludge Dust</span><span class="gt-note">4 Platinum group sludge dust</span><b class="gt-q">4</b></span><span class="gt-slot gt-fluid" title="1 B sulfuric nickel solution (void it) (gtceu:fluid_voiding_cover) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__fluid_voiding_cover.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Fluid Voiding Cover</span><span class="gt-note">1 B sulfuric nickel solution (void it)</span><b class="gt-q">1 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-hv" id="m-c1">
<div class="gt-head"><span class="gt-mname">HV Centrifuge · 25 s · 480 EU/t</span><span class="gt-badge t-hv">HV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Platinum group sludge dust (gtceu:platinum_group_sludge_dust) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_group_sludge_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Group Sludge Dust</span><span class="gt-note">4 Platinum group sludge dust</span><b class="gt-q">6</b></span><span class="gt-slot gt-fluid" title="Aqua regia · 1200 mB per 6 sludge (gtceu:aqua_regia_bucket) - 1200 mB"><img class="gt-ico" src="../../assets/icons/gtceu__aqua_regia_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Aqua Regia</span><span class="gt-note">Aqua regia · 1200 mB per 6 sludge</span><b class="gt-q">1200 mB</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__hv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 512 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="3 Raw platinum dust (gtceu:platinum_raw_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_raw_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Raw Dust</span><span class="gt-note">3 Raw platinum dust</span><b class="gt-q">3</b></span><span class="gt-slot" title="3 Raw palladium dust (gtceu:palladium_raw_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__palladium_raw_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Palladium Raw Dust</span><span class="gt-note">3 Raw palladium dust</span><b class="gt-q">3</b></span><span class="gt-slot" title="2 Inert metal mixture dust (gtceu:inert_metal_mixture_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__inert_metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Inert Metal Mixture Dust</span><span class="gt-note">2 Inert metal mixture dust</span><b class="gt-q">2</b></span><span class="gt-slot" title="1 Rarest metal mixture dust (gtceu:rarest_metal_mixture_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__rarest_metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rarest Metal Mixture Dust</span><span class="gt-note">1 Rarest metal mixture dust</span><b class="gt-q">1</b></span><span class="gt-slot" title="2 Platinum sludge residue (trash) (gtceu:platinum_sludge_residue_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_sludge_residue_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Sludge Residue Dust</span><span class="gt-note">2 Platinum sludge residue (trash)</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:hv_centrifuge</code></div>
</div>
<div class="gt-panel t-mv" id="m-e1">
<div class="gt-head"><span class="gt-mname">MV Electrolyzer · 5 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Raw platinum dust (gtceu:platinum_raw_dust) - 3"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_raw_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Raw Dust</span><span class="gt-note">3 Raw platinum dust</span><b class="gt-q">3</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Platinum dust (gtceu:platinum_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__platinum_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Platinum Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_electrolyzer</code></div>
</div>
<div class="gt-panel t-mv" id="m-r2">
<div class="gt-head"><span class="gt-mname">MV Chemical Reactor · 10 s · 120 EU/t (5 raw + 1 B HCl)</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="3 Raw palladium dust (gtceu:palladium_raw_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__palladium_raw_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Palladium Raw Dust</span><span class="gt-note">3 Raw palladium dust</span><b class="gt-q">5</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Palladium dust (gtceu:palladium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__palladium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Palladium Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-ev" id="m-r3">
<div class="gt-head"><span class="gt-mname">EV Chemical Reactor · 22.5 s · 1920 EU/t (6 + 1.5 B sulfuric acid)</span><span class="gt-badge t-ev">EV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="2 Inert metal mixture dust (gtceu:inert_metal_mixture_dust) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__inert_metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Inert Metal Mixture Dust</span><span class="gt-note">2 Inert metal mixture dust</span><b class="gt-q">6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__ev_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 2 048 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Ruthenium tetroxide dust (gtceu:ruthenium_tetroxide_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_tetroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Tetroxide Dust</span><span class="gt-note">5 Ruthenium tetroxide dust</span><b class="gt-q">5</b></span><span class="gt-slot gt-fluid" title="500 mB rhodium sulfate (gtceu:rhodium_sulfate_bucket) - 500 mB"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_sulfate_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Sulfate</span><span class="gt-note">500 mB rhodium sulfate</span><b class="gt-q">500 mB</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:ev_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-e2">
<div class="gt-head"><span class="gt-mname">MV Electrolyzer · 5 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="500 mB rhodium sulfate (gtceu:rhodium_sulfate_bucket) - 1 B"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_sulfate_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Sulfate</span><span class="gt-note">500 mB rhodium sulfate</span><b class="gt-q">1 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_electrolyzer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Rhodium dust (gtceu:rhodium_dust) - 2"><img class="gt-ico" src="../../assets/icons/gtceu__rhodium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rhodium Dust</span><b class="gt-q">2</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_electrolyzer</code></div>
</div>
<div class="gt-panel t-mv" id="m-r4">
<div class="gt-head"><span class="gt-mname">MV Chemical Reactor · 10 s (5 + 2 carbon)</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="5 Ruthenium tetroxide dust (gtceu:ruthenium_tetroxide_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_tetroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Tetroxide Dust</span><span class="gt-note">5 Ruthenium tetroxide dust</span><b class="gt-q">5</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Ruthenium dust (gtceu:ruthenium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__ruthenium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Ruthenium Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-multi" id="m-lc">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · IV hatch · 20 s · 7680 EU/t (7 + 4 B HCl)</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="1 Rarest metal mixture dust (gtceu:rarest_metal_mixture_dust) - 7"><img class="gt-ico" src="../../assets/icons/gtceu__rarest_metal_mixture_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Rarest Metal Mixture Dust</span><span class="gt-note">1 Rarest metal mixture dust</span><b class="gt-q">7</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Iridium metal residue (gtceu:iridium_metal_residue_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_metal_residue_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Metal Residue Dust</span><span class="gt-note">5 Iridium metal residue</span><b class="gt-q">5</b></span><span class="gt-slot gt-fluid" title="2 B acidic osmium solution (gtceu:acidic_osmium_solution_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__acidic_osmium_solution_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Acidic Osmium Solution</span><span class="gt-note">2 B acidic osmium solution</span><b class="gt-q">2 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-c2">
<div class="gt-head"><span class="gt-mname">MV Centrifuge · 10 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="5 Iridium metal residue (gtceu:iridium_metal_residue_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_metal_residue_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Metal Residue Dust</span><span class="gt-note">5 Iridium metal residue</span><b class="gt-q">5</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_centrifuge.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="4 Iridium chloride dust (gtceu:iridium_chloride_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_chloride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Chloride Dust</span><span class="gt-note">4 Iridium chloride dust</span><b class="gt-q">4</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_centrifuge</code></div>
</div>
<div class="gt-panel t-lv" id="m-r5">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 5 s (4 + 3 B hydrogen)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="4 Iridium chloride dust (gtceu:iridium_chloride_dust) - 4"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_chloride_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Chloride Dust</span><span class="gt-note">4 Iridium chloride dust</span><b class="gt-q">4</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Iridium dust (gtceu:iridium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__iridium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Iridium Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
<div class="gt-panel t-mv" id="m-ds">
<div class="gt-head"><span class="gt-mname">MV Distillery · 20 s · 120 EU/t</span><span class="gt-badge t-mv">MV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="2 B acidic osmium solution (gtceu:acidic_osmium_solution_bucket) - 2 B"><img class="gt-ico" src="../../assets/icons/gtceu__acidic_osmium_solution_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Acidic Osmium Solution</span><span class="gt-note">2 B acidic osmium solution</span><b class="gt-q">2 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__mv_distillery.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 128 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="5 Osmium tetroxide dust (gtceu:osmium_tetroxide_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__osmium_tetroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osmium Tetroxide Dust</span><span class="gt-note">5 Osmium tetroxide dust</span><b class="gt-q">5</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:mv_distillery</code></div>
</div>
<div class="gt-panel t-lv" id="m-r6">
<div class="gt-head"><span class="gt-mname">LV Chemical Reactor · 10 s (5 + 8 B hydrogen)</span><span class="gt-badge t-lv">LV</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="5 Osmium tetroxide dust (gtceu:osmium_tetroxide_dust) - 5"><img class="gt-ico" src="../../assets/icons/gtceu__osmium_tetroxide_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osmium Tetroxide Dust</span><span class="gt-note">5 Osmium tetroxide dust</span><b class="gt-q">5</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__lv_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">up to 32 EU/t</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Osmium dust (gtceu:osmium_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__osmium_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Osmium Dust</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:lv_chemical_reactor</code></div>
</div>
</div>

## Flow

- [LV Chemical Reactor · 2.5 s · 30 EU/t](#m-r1) → [HV Centrifuge · 25 s · 480 EU/t](#m-c1) → [MV Electrolyzer · 5 s · 120 EU/t](#m-e1) (also HV Centrifuge · 25 s · 480 EU/t → [MV Chemical Reactor · 10 s · 120 EU/t (5 raw + 1 B HCl)](#m-r2), HV Centrifuge · 25 s · 480 EU/t → [EV Chemical Reactor · 22.5 s · 1920 EU/t (6 + 1.5 B sulfuric acid)](#m-r3), HV Centrifuge · 25 s · 480 EU/t → [Large Chemical Reactor · IV hatch · 20 s · 7680 EU/t (7 + 4 B HCl)](#m-lc))
- [MV Chemical Reactor · 10 s · 120 EU/t (5 raw + 1 B HCl)](#m-r2)
- [EV Chemical Reactor · 22.5 s · 1920 EU/t (6 + 1.5 B sulfuric acid)](#m-r3) → [MV Chemical Reactor · 10 s (5 + 2 carbon)](#m-r4) (also EV Chemical Reactor · 22.5 s · 1920 EU/t (6 + 1.5 B sulfuric acid) → [MV Electrolyzer · 5 s · 120 EU/t](#m-e2))
- [MV Electrolyzer · 5 s · 120 EU/t](#m-e2)
- [Large Chemical Reactor · IV hatch · 20 s · 7680 EU/t (7 + 4 B HCl)](#m-lc) → [MV Centrifuge · 10 s · 120 EU/t](#m-c2) → [LV Chemical Reactor · 5 s (4 + 3 B hydrogen)](#m-r5) (also Large Chemical Reactor · IV hatch · 20 s · 7680 EU/t (7 + 4 B HCl) → [MV Distillery · 20 s · 120 EU/t](#m-ds))
- [MV Distillery · 20 s · 120 EU/t](#m-ds) → [LV Chemical Reactor · 10 s (5 + 8 B hydrogen)](#m-r6)

## How to build

1. Buffers first: an ore drawer, drums for nitric acid, hydrochloric acid, aqua regia, sulfuric acid, hydrogen, and a drum or voiding cover for every by-product. Every reactor below is its own machine with its own input drawer and Item Filter route and an output Keep Exact arm, because several of these reactors have circuit-less recipes that compete for the same bus. — `functionalstorage:oak_1`, `gtceu:purified_cooperite_ore`, `gtceu:nitric_acid_bucket`, `gtceu:hydrochloric_acid_bucket`
2. Sludge reactor (LV Chemical Reactor): 1 purified cooperite ore + 100 mB nitric acid → 4 platinum group sludge dust in 2.5 s at 30 EU/t, plus 1 B sulfuric nickel solution. Put a Fluid Voiding Cover on the by-product hatch before the first run. That is the whole sludge step: the ore and the nitric acid are the only things you have to supply. — `gtceu:lv_chemical_reactor`, `gtceu:platinum_group_sludge_dust`
3. Aqua regia: LV Mixer, 1 B nitric acid + 2 B hydrochloric acid → 3 B aqua regia, 1.5 s at 30 EU/t. Keep it in its own drum with a pump cover to the centrifuge; never share a drum with plain nitric acid. — `gtceu:lv_mixer`, `gtceu:aqua_regia_bucket`
4. HV Centrifuge: 6 sludge dust + 1200 mB aqua regia → 3 raw platinum + 3 raw palladium + 2 inert metal mixture + 1 rarest metal mixture + 2 platinum sludge residue, 25 s at 480 EU/t. Five outputs mean five output slots: a Robot Arm cover with an Item Filter per item sends each one to its own drawer, and an Item Voiding Cover takes the residue. — `gtceu:hv_centrifuge`, `gtceu:inert_metal_mixture_dust`, `gtceu:rarest_metal_mixture_dust`
5. Platinum and palladium: MV Electrolyzer, 3 raw platinum → 1 platinum + 800 mB chlorine (5 s, 120 EU/t); MV Chemical Reactor, 5 raw palladium + 1 B hydrochloric acid → 1 palladium + 2 ammonium chloride (10 s). Chlorine goes back to the chlorine drum of the MV chain. — `gtceu:mv_electrolyzer`, `gtceu:platinum_dust`, `gtceu:mv_chemical_reactor`, `gtceu:palladium_dust`
6. Ruthenium and rhodium: EV Chemical Reactor, 6 inert metal mixture + 1.5 B sulfuric acid → 500 mB rhodium sulfate + 5 ruthenium tetroxide + 3 B hydrogen, 22.5 s at 1920 EU/t. The rhodium sulfate goes to an MV Electrolyzer (1 B → 2 rhodium dust + 3 B sulfur trioxide + 3 B oxygen); the tetroxide to an MV Chemical Reactor with 2 carbon dust per 5 → 1 ruthenium dust + 2 B carbon dioxide (10 s). — `gtceu:ev_chemical_reactor`, `gtceu:ruthenium_tetroxide_dust`, `gtceu:rhodium_sulfate_bucket`
7. The only Large Chemical Reactor step: 7 rarest metal mixture + 4 B hydrochloric acid → 5 iridium metal residue + 2 B acidic osmium solution + 3 B hydrogen, 20 s at 7680 EU/t. It needs an IV Energy Hatch on the LCR (the pack quest chain makes the hatch with the IV Assembler). Mixture arrives through an input bus, the acid through a hatch, residue through an output bus, solution and hydrogen through two output hatches. — `gtceu:large_chemical_reactor`, `gtceu:iv_energy_input_hatch`, `gtceu:iridium_metal_residue_dust`
8. Iridium: MV Centrifuge, 5 residue → 4 iridium chloride + 1 platinum sludge residue (10 s, 120 EU/t), then LV Chemical Reactor, 4 chloride + 3 B hydrogen → 1 iridium dust + 3 B hydrochloric acid (5 s). Iridium dust is an EBF recipe at 4500 K (RTM coils), see the rtm\_coil and iv\_components chains. — `gtceu:mv_centrifuge`, `gtceu:iridium_chloride_dust`, `gtceu:lv_chemical_reactor`, `gtceu:iridium_dust`
9. Osmium: MV Distillery on the acidic osmium solution, 2 B → 5 osmium tetroxide dust + 1 B hydrochloric acid + 1 B water (20 s, 120 EU/t); then LV Chemical Reactor, 5 tetroxide + 8 B hydrogen → 1 osmium dust + 4 B water (10 s). Osmium is a later metal (its ingot is a LuV furnace recipe), but it comes out of the same LCR run as iridium. — `gtceu:mv_distillery`, `gtceu:osmium_tetroxide_dust`, `gtceu:osmium_dust`
10. Easy to miss: the common sulfides give only 2 sludge per ore and cooperite 4, so cooperite is worth a dedicated sieve. When the line stalls, check the by-product hatch of the sludge reactor first, then the hydrogen supply of the iridium and osmium reactors. — `functionalstorage:oak_1`, `gtceu:platinum_group_sludge_dust`

## Tips

- Where the numbers come from: PlatGroupMetalsRecipes (the pack leaves the line unchanged except for the ZPM skip below). Per 6 sludge dust the centrifuge makes 3 raw platinum + 3 raw palladium + 2 inert metal mixture + 1 rarest metal mixture + 2 platinum sludge residue. Per 42 sludge (7 runs) the whole line yields 7 platinum, 4.2 palladium, 2.3 ruthenium, 2.3 rhodium, 1 iridium and 1 osmium. A purified cooperite ore gives 4 sludge; chalcopyrite, chalcocite, bornite, tetrahedrite and pentlandite give 2.
- Sludge (LV Chemical Reactor, 50 ticks, 30 EU/t): 1 purified ore + 100 mB nitric acid → sludge + 1 B sulfuric nickel solution (cooperite, pentlandite) or sulfuric copper solution (the others). Nothing in the fork uses either solution, so the tank fills and the reactor stops silently. Put a Fluid Voiding Cover on the output hatch or drum (and an Item Voiding Cover on the platinum sludge residue, which is also unused).
- Aqua regia: LV Mixer, 1 B nitric acid + 2 B hydrochloric acid → 3 B (30 ticks, 30 EU/t). The centrifuge takes 1200 mB per 6 sludge, so 400 mB nitric acid and 800 mB hydrochloric acid per run. Nitric acid: chemical reactor, circuit 1, 3 B nitrogen dioxide + 1 B water → 2 B nitric acid + 1 B nitric oxide (240 ticks, 30 EU/t); the Large Chemical Reactor does it from ammonia + oxygen (circuit 24).
- The step list in the era text says LCR for everything, but only ONE step needs the Large Chemical Reactor: the rarest metal mixture (iridium and osmium) at 7680 EU/t = an IV Energy Hatch on the LCR. The rhodium/ruthenium step is an EV Chemical Reactor (1920 EU/t); the centrifuge is HV (480 EU/t); everything else is LV or MV.
- Ruthenium: 6 inert metal mixture → 5 ruthenium tetroxide + 500 mB rhodium sulfate + 3 B hydrogen; then 5 tetroxide + 2 carbon dust → 1 ruthenium (+ 2 B carbon dioxide). So 1 ruthenium = 6 mixture = 18 sludge = 4.5 cooperite ore. The RTM coil chain needs about 4.6 ruthenium per block. This line is the only ruthenium source in the pack (no vein, sieve or fusion recipe gives it; the ZPM Chemical Plant skip is the same line in one recipe) and every stage except iridium and osmium is LV to EV, so ruthenium and the RTM coils never wait for IV. The same mixture gives 1 rhodium per 6 (500 mB rhodium sulfate → 1 rhodium in an electrolyzer, 100 ticks, 120 EU/t), which LuV needs later.
- Platinum: 3 raw platinum → 1 platinum + 800 mB chlorine in an MV Electrolyzer. Palladium: 5 raw palladium + 1 B hydrochloric acid → 1 palladium + 2 ammonium chloride dust (MV Chemical Reactor). Platinum is the IV hull and IV cable metal (platinum single cable) and the EV emitter rod; palladium feeds the later chips.
- Iridium and osmium: LCR, 7 rarest metal mixture + 4 B hydrochloric acid → 5 iridium metal residue + 2 B acidic osmium solution + 3 B hydrogen (400 ticks, 7680 EU/t). Residue: MV Centrifuge 5 → 4 iridium chloride + 1 platinum sludge residue; then LV Chemical Reactor 4 chloride + 3 B hydrogen → 1 iridium dust + 3 B hydrochloric acid. Osmium: MV distillery 2 B solution → 5 osmium tetroxide + 1 B hydrochloric acid + 1 B water; then LV reactor 5 tetroxide + 8 B hydrogen → 1 osmium + 4 B water. Iridium: 2 per IV emitter (4 rods), 0.5 per sensor.
- The ZPM Chemical Plant skip (kjs chemical\_plant.js) does the whole line in one recipe: 30 purified cooperite ore + 24 B aqua regia → 20 platinum, 12 palladium, 7 ruthenium, 7 rhodium, 3 osmium, 3 iridium dust (+ 8 B nitric and 16 B hydrochloric acid back), 485 ticks at ZPM. That matches the by-hand yields above, so it is a convenience, not a better ratio; do the manual line first.
- Sub-steps people skip: (1) one dedicated machine per recipe, because the reactors share circuit-less recipes with other chains; (2) hydrogen and hydrochloric acid come back as by-products, route them to their drums, do not void them; (3) 3 raw palladium per run is not enough for the 5-raw recipe, so let the raw dust accumulate in a drawer; (4) the by-product voiding above; (5) purify the cooperite first (the ore washer step).
- **Unverified** where the purified cooperite comes from in practice. The pack sieve (kjs sieving.js) gives crushed cooperite ore at 25 % from crushed blackstone with an emerald mesh, and the ore washer should purify it; read the washer recipe in EMI. Also unverified: whether the single MV Distillery offers the osmium step (the source recipe is a Distillation Tower recipe with an item output); if EMI shows only the tower, use the EV Distillation Tower.

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:lv_chemical_reactor` | 3 |
| `gtceu:mv_chemical_reactor` | 2 |
| `gtceu:ev_chemical_reactor` | 1 |
| `gtceu:hv_centrifuge` | 1 |
| `gtceu:mv_centrifuge` | 1 |
| `gtceu:mv_electrolyzer` | 2 |
| `gtceu:lv_mixer` | 1 |
| `gtceu:mv_distillery` | 1 |
| `gtceu:large_chemical_reactor` | 1 |
| `gtceu:iv_energy_input_hatch` | 1 |
| `gtceu:fluid_voiding_cover` | 2 |
| `gtceu:item_voiding_cover` | 1 |
| `functionalstorage:oak_1` | 16 |
| `modularrouters:modular_router` | 10 |
| `gtceu:lv_robot_arm` | 12 |
| `gtceu:item_filter` | 12 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 12 |
| `gtceu:steel_drum` | 8 |

## Needs / Feeds

- **Needs:** [Molten Ore Mixture](../ev/molten_mix.md)
- **Feeds:** [Elemental powders: blizz, blitz, basalz from dust + gas, then molten powder for the nether star loop](elemental.md)
- **Main source for:** `gtceu:platinum_dust`, `gtceu:rhodium_dust`
