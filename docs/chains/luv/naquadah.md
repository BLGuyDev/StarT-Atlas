---
kind: chain
id: naquadah
order: 400
data:
  t: |-
    Naquadah: nether star shard + PCB coolant in the Dimensional Destabiliser → raw naquadah → ore line → dust → EBF 5000 K; byproducts by the fluoroantimonic acid line
  "n":
    - [ns, "Nether star shard · 1 per run", i, "kubejs:nether_star_shard"]
    - [pc, "8 B PCB coolant", f, "gtceu:pcb_coolant_bucket"]
    - [dd, "Dimensional Destabiliser · 60 s · 4096 EU/t", m, "gtceu:dimensional_destabiliser"]
    - [rn, "20 Raw naquadah", x, "gtceu:raw_naquadah"]
    - [hp, "9.6 B hot PCB coolant (back to the freezer)", f, "gtceu:hot_pcb_coolant_bucket"]
    - [vf, "Vacuum Freezer · 7 s · 512 EU/t", m, "gtceu:vacuum_freezer"]
    - [nd, "Naquadah dust (ore line)", x, "gtceu:naquadah_dust"]
    - [eb, "EBF · HSS-G coils 5400 K · 30 s · 7680 EU/t", m, "gtceu:electric_blast_furnace"]
    - [n1, Naquadah ingot, o, "gtceu:naquadah_ingot"]
    - - lc
      - Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 dust + 1 B fluoroantimonic acid
      - m
      - gtceu:large_chemical_reactor
    - [n2, "Enriched naquadah (7000 K)", o, "gtceu:enriched_naquadah_ingot"]
    - [n3, "Naquadria (9000 K)", o, "gtceu:naquadria_ingot"]
    - [n4, "Trinium (7200 K)", o, "gtceu:trinium_ingot"]
  e:
    - [ns, dd, "1"]
    - [pc, dd, "8 B"]
    - [dd, rn, "20 / 60 s"]
    - [dd, hp, "9.6 B"]
    - [hp, vf, "9.6 B"]
    - [rn, nd, ore line]
    - [nd, eb, "1"]
    - [eb, n1, "1 / 30 s"]
    - [nd, lc, "6"]
    - [lc, n2, separation]
    - [lc, n3, separation]
    - [lc, n4, separation]
  tips:
    - This is the only raw naquadah recipe in the pack. There is no vein, the naquadah sieve entry is commented out in sieving.js, and the Abydos naquadite line is much later, so nothing else gives naquadah until the Destabiliser runs. The controller is LuV (LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears) and the run needs an IV hatch (4096 EU/t); only the coolant cooling is HV (Vacuum Freezer 512 EU/t), so the freezer can exist long before the Destabiliser.
    - |-
      The run (kubejs systems/resource_gen/dimensional_destabilising.js): 1 nether star shard + 8 B PCB coolant → 20 raw naquadah + a 80 % chance of 1 tiny nether star dust + 9.6 B hot PCB coolant, 1200 ticks (60 s) at 4096 EU/t (an IV hatch). The multiblock has throughput boosting and batch mode (kjs startup); read the multi tooltip for the factor. Unverified: the throughput factor and the batch size.
    - |-
      Why shards are the limit: a nether star hammers into 5 shards (HV Forge Hammer, 15 s, 240 EU/t) and each shard makes 20 raw naquadah = 100 raw naquadah per star. The nether_star chain’s loop (1 star → about 1.19 stars) uses the same shards: a shard spent here is a shard not looped. Start the loop first, keep a stock of 2 or 3 stars, then draw down; the quest text says the same: loop nether stars first.
    - |-
      Controller (pack assembler recipe): LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears, 1800 ticks (90 s) at 7680 EU/t (an IV Assembler). It needs the hull line and the nano mainframe line. Pure netherite (kjs lines/netherite.js): netherrack in the centrifuge gives small debris dust at 0.5 %; debris dust + gold in an EBF (3300 K, 100 mB argon, 6000 ticks, 1890 EU/t) makes the netherite ingot; purified debris dust goes through an LCR (6500 EU/t, 400 ticks, chlorine trifluoride + hydrogen sulfide) and pure netherite dust through a chemical bath (20450 EU/t, tetrachloroethylene). Unverified: any passive debris loop at LuV; none was found, ancient debris only comes from the UEV nether magma centrifuge and ancient netherite (EBF 13300 K) is UHV.
    - |-
      Structure (multis card, startup script dimensional_destabiliser.js): 119 stress-proof casings (hatch spots included), 68 non-conducting casings, 56 tungsten carbide frames, 22 shellite glass (thermal_extra), 8 assembly line gratings, 5 molybdenum disilicide coil blocks and 1 nether star block. Hatches: up to 2 item/fluid input and output each, 2 energy hatches, exactly 1 maintenance. The shellite glass and the 56 tungsten carbide frames are the expensive part. Unverified: shellite glass recipe (thermal_extra), and the stress-proof / non-conducting casing recipes (GCYM).
    - |-
      Ore line: raw naquadah goes through the normal GT ore processing (macerator → crushed → purified → centrifuged dust) in the ore processing line; naquadah is an ore material with a naquadah dust output. Unverified: yield per raw ore in this pack (check the macerator recipe in EMI), and the by-products.
    - |-
      Naquadah ingot (ElementMaterials): EBF 5000 K = HSS-G coils, 7680 EU/t, 600 ticks, gas tier argon; the freezer then needs 500 mB LIQUID helium per ingot, 150 ticks at 1920 EU/t (5000 K rule, see luv_hsss). Naquadah dust is also the base of naquadah alloy, naquadah wires and the naquadah coil block (HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel, 700 ticks at 30 720 EU/t).
    - |-
      By-product line (NaquadahRecipes, quest naquadah_byproducts): Large Chemical Reactor at VA[LuV] = 30 720 EU/t, 600 ticks: 6 naquadah dust + 1 B fluoroantimonic acid → 2 B impure enriched naquadah solution + 2 B impure naquadria solution + 4 titanium trifluoride dust. Acid: 4 antimony trifluoride dust + 4 B hydrofluoric acid → 1 B acid + 2 B hydrogen, 300 ticks at 480 EU/t; antimony trifluoride = 1 antimony trioxide (2 antimony + 3 B oxygen) + 6 B HF. Further steps go to enriched naquadah (EBF 7000 K, naquadah coils), trinium (7200 K) and naquadria (9000 K, trinium coils). This is ZPM-era material: build the dust and ingot first.
    - |-
      Sub-steps people skip: (1) the shard stock (see above); (2) the coolant loop must exist before the first run (luv pcb_coolant chain); (3) the LuV hull and 2 LuV circuits for the controller; (4) the ingot route needs HSS-G coils and liquid helium: do the HSS-S chain first, it builds both; (5) keep the tiny nether star dust, it feeds the nether star loop (about 80 % of runs).
  b:
    - ["gtceu:dimensional_destabiliser", 1]
    - ["gtceu:iv_energy_input_hatch", 2]
    - ["gtceu:vacuum_freezer", 1]
    - ["gtceu:electric_blast_furnace", 1]
    - ["gtceu:hssg_coil_block", 16]
    - ["gtceu:hv_forge_hammer", 1]
    - ["functionalstorage:oak_1", 10]
    - ["modularrouters:modular_router", 6]
    - ["gtceu:lv_robot_arm", 6]
    - ["gtceu:item_filter", 6]
    - ["pipez:item_pipe", 16]
    - ["pipez:fluid_pipe", 6]
    - ["gtceu:steel_drum", 4]
  inf: true
  how:
    - i: ["gtceu:dimensional_destabiliser", "gtceu:luv_machine_hull", "gtceu:ruridit_gear"]
      t: |-
        Build the controller: LuV hull (luv_hull), 2 LuV circuits (luv_circuits), 4 double pure netherite plates, 2 ruridit gears, in an IV Assembler (90 s, 7680 EU/t). Then the big structure from the multis card; build the 119 casing / 68 casing / 56 frame / 22 glass shell as one session, with the nether star block in the centre.
    - i: ["gtceu:iv_energy_input_hatch", "gtceu:pcb_coolant_bucket", "gtceu:hot_pcb_coolant_bucket"]
      t: |-
        Hatches: 1 or 2 IV energy hatches (4096 EU/t per run), 1 fluid input for coolant, 1 fluid output for hot coolant, 1 item input bus for shards, 1 item output bus, maintenance. Pipe the output hatch into the Vacuum Freezer (see the PCB coolant chain), the freezer back into the input hatch.
    - i: ["gtceu:hv_forge_hammer", "kubejs:nether_star_shard", "minecraft:nether_star"]
      t: |-
        Shards: HV Forge Hammer, 1 nether star → 5 shards (15 s, 240 EU/t). Keep Exact 8 on the shard drawer and one Robot Arm into the input bus. Do not hammer your last star: keep one in the loop.
    - i: ["gtceu:dimensional_destabiliser", "gtceu:raw_naquadah"]
      t: |-
        Run: shard + 8 B coolant → 20 raw naquadah every 60 s. Raw naquadah goes out the output bus into a drawer; the tiny nether star dust goes to the nether_star chain’s drawers.
    - i: ["gtceu:electric_blast_furnace", "gtceu:hssg_coil_block", "gtceu:naquadah_ingot"]
      t: |-
        Ore line, then naquadah dust → EBF with 16 HSS-G coil blocks and an IV hatch (7680 EU/t), circuit 1: hot ingot in 30 s; Vacuum Freezer with 500 mB liquid helium → naquadah ingot in 7.5 s.
    - i: ["gtceu:large_chemical_reactor", "gtceu:luv_energy_input_hatch", "gtceu:fluoroantimonic_acid_bucket"]
      t: |-
        Later: the by-product Large Chemical Reactor needs a LuV hatch (30 720 EU/t). Feed 6 naquadah dust + 1 B fluoroantimonic acid per run; route the solutions to the enriched, naquadria and trinium chains, each in its own tank.
    - i: ["gtceu:naquadah_dust", "functionalstorage:oak_1"]
      t: |-
        Easy to miss: passive the destabiliser as soon as it runs, but only with the shard stock and loop in place. Keep Exact 32 on the raw drawer so the ore line never blocks the output bus.
---
# Naquadah: nether star shard + PCB coolant in the Dimensional Destabiliser → raw naquadah → ore line → dust → EBF 5000 K; byproducts by the fluoroantimonic acid line

<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->

**Chain id:** `naquadah` · **Tags:** Infinite source

**Era setup:** [LuV](../../eras/luv.md)

**Plan modules:** [Naquadah and PCB coolant](../../plan/p11.md#naquadah)

**Tips:** 9

## Machines

<div class="gt-panels">
<div class="gt-panel t-mod" id="m-dd">
<div class="gt-head"><span class="gt-mname">Dimensional Destabiliser · 60 s · 4096 EU/t</span><span class="gt-badge t-mod">GregTech</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Nether star shard · 1 per run (kubejs:nether_star_shard) - 1"><img class="gt-ico" src="../../assets/icons/kubejs__nether_star_shard.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Nether Star Shard</span><span class="gt-note">Nether star shard · 1 per run</span><b class="gt-q">1</b></span><span class="gt-slot gt-fluid" title="8 B PCB coolant (gtceu:pcb_coolant_bucket) - 8 B"><img class="gt-ico" src="../../assets/icons/gtceu__pcb_coolant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Pcb Coolant</span><span class="gt-note">8 B PCB coolant</span><b class="gt-q">8 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__dimensional_destabiliser.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">60 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot" title="20 Raw naquadah (gtceu:raw_naquadah) - 20 / 60 s"><img class="gt-ico" src="../../assets/icons/gtceu__raw_naquadah.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Raw Naquadah</span><span class="gt-note">20 Raw naquadah</span><b class="gt-q">20</b></span><span class="gt-slot gt-fluid" title="9.6 B hot PCB coolant (back to the freezer) (gtceu:hot_pcb_coolant_bucket) - 9.6 B"><img class="gt-ico" src="../../assets/icons/gtceu__hot_pcb_coolant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Pcb Coolant</span><span class="gt-note">9.6 B hot PCB coolant (back to the freezer)</span><b class="gt-q">9.6 B</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:dimensional_destabiliser</code></div>
</div>
<div class="gt-panel t-multi" id="m-vf">
<div class="gt-head"><span class="gt-mname">Vacuum Freezer · 7 s · 512 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot gt-fluid" title="9.6 B hot PCB coolant (back to the freezer) (gtceu:hot_pcb_coolant_bucket) - 9.6 B"><img class="gt-ico" src="../../assets/icons/gtceu__hot_pcb_coolant_bucket.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Hot Pcb Coolant</span><span class="gt-note">9.6 B hot PCB coolant (back to the freezer)</span><b class="gt-q">9.6 B</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__vacuum_freezer.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-empty">no listed output</span></div>
</div>
<div class="gt-foot"><code>gtceu:vacuum_freezer</code></div>
</div>
<div class="gt-panel t-multi" id="m-eb">
<div class="gt-head"><span class="gt-mname">EBF · HSS-G coils 5400 K · 30 s · 7680 EU/t</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Naquadah dust (ore line) (gtceu:naquadah_dust) - 1"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Dust</span><span class="gt-note">Naquadah dust (ore line)</span><b class="gt-q">1</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__electric_blast_furnace.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span><span class="gt-stat">30 s</span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Naquadah ingot (gtceu:naquadah_ingot) - 1 / 30 s"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Ingot</span><b class="gt-q">1</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:electric_blast_furnace</code></div>
</div>
<div class="gt-panel t-multi" id="m-lc">
<div class="gt-head"><span class="gt-mname">Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 dust + 1 B fluoroantimonic acid</span><span class="gt-badge t-multi">Multiblock</span></div>
<div class="gt-body">
<div class="gt-col gt-in" role="group" aria-label="Inputs"><span class="gt-slot" title="Naquadah dust (ore line) (gtceu:naquadah_dust) - 6"><img class="gt-ico" src="../../assets/icons/gtceu__naquadah_dust.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadah Dust</span><span class="gt-note">Naquadah dust (ore line)</span><b class="gt-q">6</b></span></div>
<div class="gt-mid"><img class="gt-ico" src="../../assets/icons/gtceu__large_chemical_reactor.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-arrow" aria-hidden="true"></span></div>
<div class="gt-col gt-outc" role="group" aria-label="Outputs"><span class="gt-slot gt-outp" title="Enriched naquadah (7000 K) (gtceu:enriched_naquadah_ingot) - separation"><img class="gt-ico" src="../../assets/icons/gtceu__enriched_naquadah_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Enriched Naquadah Ingot</span><span class="gt-note">Enriched naquadah (7000 K)</span><b class="gt-q">separation</b></span><span class="gt-slot gt-outp" title="Naquadria (9000 K) (gtceu:naquadria_ingot) - separation"><img class="gt-ico" src="../../assets/icons/gtceu__naquadria_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Naquadria Ingot</span><span class="gt-note">Naquadria (9000 K)</span><b class="gt-q">separation</b></span><span class="gt-slot gt-outp" title="Trinium (7200 K) (gtceu:trinium_ingot) - separation"><img class="gt-ico" src="../../assets/icons/gtceu__trinium_ingot.png" alt="" loading="lazy" onerror="this.remove()"><span class="gt-nm">Trinium Ingot</span><span class="gt-note">Trinium (7200 K)</span><b class="gt-q">separation</b></span></div>
</div>
<div class="gt-foot"><code>gtceu:large_chemical_reactor</code></div>
</div>
</div>

## Flow

- [Dimensional Destabiliser · 60 s · 4096 EU/t](#m-dd) → [EBF · HSS-G coils 5400 K · 30 s · 7680 EU/t](#m-eb) (also Dimensional Destabiliser · 60 s · 4096 EU/t → [Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 dust + 1 B fluoroantimonic acid](#m-lc), Dimensional Destabiliser · 60 s · 4096 EU/t → [Vacuum Freezer · 7 s · 512 EU/t](#m-vf))
- [Vacuum Freezer · 7 s · 512 EU/t](#m-vf)
- [Large Chemical Reactor · LuV hatch · 30 s · 30 720 EU/t · 6 dust + 1 B fluoroantimonic acid](#m-lc)

### Direct steps

- 20 Raw naquadah → Naquadah dust (ore line) (ore line)

## How to build

1. Build the controller: LuV hull (luv\_hull), 2 LuV circuits (luv\_circuits), 4 double pure netherite plates, 2 ruridit gears, in an IV Assembler (90 s, 7680 EU/t). Then the big structure from the multis card; build the 119 casing / 68 casing / 56 frame / 22 glass shell as one session, with the nether star block in the centre. — `gtceu:dimensional_destabiliser`, `gtceu:luv_machine_hull`, `gtceu:ruridit_gear`
2. Hatches: 1 or 2 IV energy hatches (4096 EU/t per run), 1 fluid input for coolant, 1 fluid output for hot coolant, 1 item input bus for shards, 1 item output bus, maintenance. Pipe the output hatch into the Vacuum Freezer (see the PCB coolant chain), the freezer back into the input hatch. — `gtceu:iv_energy_input_hatch`, `gtceu:pcb_coolant_bucket`, `gtceu:hot_pcb_coolant_bucket`
3. Shards: HV Forge Hammer, 1 nether star → 5 shards (15 s, 240 EU/t). Keep Exact 8 on the shard drawer and one Robot Arm into the input bus. Do not hammer your last star: keep one in the loop. — `gtceu:hv_forge_hammer`, `kubejs:nether_star_shard`, `minecraft:nether_star`
4. Run: shard + 8 B coolant → 20 raw naquadah every 60 s. Raw naquadah goes out the output bus into a drawer; the tiny nether star dust goes to the nether\_star chain’s drawers. — `gtceu:dimensional_destabiliser`, `gtceu:raw_naquadah`
5. Ore line, then naquadah dust → EBF with 16 HSS-G coil blocks and an IV hatch (7680 EU/t), circuit 1: hot ingot in 30 s; Vacuum Freezer with 500 mB liquid helium → naquadah ingot in 7.5 s. — `gtceu:electric_blast_furnace`, `gtceu:hssg_coil_block`, `gtceu:naquadah_ingot`
6. Later: the by-product Large Chemical Reactor needs a LuV hatch (30 720 EU/t). Feed 6 naquadah dust + 1 B fluoroantimonic acid per run; route the solutions to the enriched, naquadria and trinium chains, each in its own tank. — `gtceu:large_chemical_reactor`, `gtceu:luv_energy_input_hatch`, `gtceu:fluoroantimonic_acid_bucket`
7. Easy to miss: passive the destabiliser as soon as it runs, but only with the shard stock and loop in place. Keep Exact 32 on the raw drawer so the ore line never blocks the output bus. — `gtceu:naquadah_dust`, `functionalstorage:oak_1`

## Tips

- This is the only raw naquadah recipe in the pack. There is no vein, the naquadah sieve entry is commented out in sieving.js, and the Abydos naquadite line is much later, so nothing else gives naquadah until the Destabiliser runs. The controller is LuV (LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears) and the run needs an IV hatch (4096 EU/t); only the coolant cooling is HV (Vacuum Freezer 512 EU/t), so the freezer can exist long before the Destabiliser.
- The run (kubejs systems/resource\_gen/dimensional\_destabilising.js): 1 nether star shard + 8 B PCB coolant → 20 raw naquadah + a 80 % chance of 1 tiny nether star dust + 9.6 B hot PCB coolant, 1200 ticks (60 s) at 4096 EU/t (an IV hatch). The multiblock has throughput boosting and batch mode (kjs startup); read the multi tooltip for the factor. Unverified: the throughput factor and the batch size.
- Why shards are the limit: a nether star hammers into 5 shards (HV Forge Hammer, 15 s, 240 EU/t) and each shard makes 20 raw naquadah = 100 raw naquadah per star. The nether\_star chain’s loop (1 star → about 1.19 stars) uses the same shards: a shard spent here is a shard not looped. Start the loop first, keep a stock of 2 or 3 stars, then draw down; the quest text says the same: loop nether stars first.
- Controller (pack assembler recipe): LuV hull + 2 LuV circuits + 4 double pure netherite plates + 2 ruridit gears, 1800 ticks (90 s) at 7680 EU/t (an IV Assembler). It needs the hull line and the nano mainframe line. Pure netherite (kjs lines/netherite.js): netherrack in the centrifuge gives small debris dust at 0.5 %; debris dust + gold in an EBF (3300 K, 100 mB argon, 6000 ticks, 1890 EU/t) makes the netherite ingot; purified debris dust goes through an LCR (6500 EU/t, 400 ticks, chlorine trifluoride + hydrogen sulfide) and pure netherite dust through a chemical bath (20450 EU/t, tetrachloroethylene). Unverified: any passive debris loop at LuV; none was found, ancient debris only comes from the UEV nether magma centrifuge and ancient netherite (EBF 13300 K) is UHV.
- Structure (multis card, startup script dimensional\_destabiliser.js): 119 stress-proof casings (hatch spots included), 68 non-conducting casings, 56 tungsten carbide frames, 22 shellite glass (thermal\_extra), 8 assembly line gratings, 5 molybdenum disilicide coil blocks and 1 nether star block. Hatches: up to 2 item/fluid input and output each, 2 energy hatches, exactly 1 maintenance. The shellite glass and the 56 tungsten carbide frames are the expensive part. Unverified: shellite glass recipe (thermal\_extra), and the stress-proof / non-conducting casing recipes (GCYM).
- Ore line: raw naquadah goes through the normal GT ore processing (macerator → crushed → purified → centrifuged dust) in the ore processing line; naquadah is an ore material with a naquadah dust output. Unverified: yield per raw ore in this pack (check the macerator recipe in EMI), and the by-products.
- Naquadah ingot (ElementMaterials): EBF 5000 K = HSS-G coils, 7680 EU/t, 600 ticks, gas tier argon; the freezer then needs 500 mB LIQUID helium per ingot, 150 ticks at 1920 EU/t (5000 K rule, see luv\_hsss). Naquadah dust is also the base of naquadah alloy, naquadah wires and the naquadah coil block (HSS-G frame + 8 naquadah double wire + 8 osmium foil + 8 niobium nitride foil + 144 mB molten tungsten steel, 700 ticks at 30 720 EU/t).
- By-product line (NaquadahRecipes, quest naquadah\_byproducts): Large Chemical Reactor at VA\[LuV\] = 30 720 EU/t, 600 ticks: 6 naquadah dust + 1 B fluoroantimonic acid → 2 B impure enriched naquadah solution + 2 B impure naquadria solution + 4 titanium trifluoride dust. Acid: 4 antimony trifluoride dust + 4 B hydrofluoric acid → 1 B acid + 2 B hydrogen, 300 ticks at 480 EU/t; antimony trifluoride = 1 antimony trioxide (2 antimony + 3 B oxygen) + 6 B HF. Further steps go to enriched naquadah (EBF 7000 K, naquadah coils), trinium (7200 K) and naquadria (9000 K, trinium coils). This is ZPM-era material: build the dust and ingot first.
- Sub-steps people skip: (1) the shard stock (see above); (2) the coolant loop must exist before the first run (luv pcb\_coolant chain); (3) the LuV hull and 2 LuV circuits for the controller; (4) the ingot route needs HSS-G coils and liquid helium: do the HSS-S chain first, it builds both; (5) keep the tiny nether star dust, it feeds the nether star loop (about 80 % of runs).

## Bill of materials

| Item | Qty |
| --- | ---: |
| `gtceu:dimensional_destabiliser` | 1 |
| `gtceu:iv_energy_input_hatch` | 2 |
| `gtceu:vacuum_freezer` | 1 |
| `gtceu:electric_blast_furnace` | 1 |
| `gtceu:hssg_coil_block` | 16 |
| `gtceu:hv_forge_hammer` | 1 |
| `functionalstorage:oak_1` | 10 |
| `modularrouters:modular_router` | 6 |
| `gtceu:lv_robot_arm` | 6 |
| `gtceu:item_filter` | 6 |
| `pipez:item_pipe` | 16 |
| `pipez:fluid_pipe` | 6 |
| `gtceu:steel_drum` | 4 |

## Needs / Feeds

- **Needs:** [Nether star loop: shards → energized shards → infused shards → impure star → implosion](../iv/nether_star.md)
