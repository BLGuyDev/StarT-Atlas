/* Bills of materials with multiplier, raw-material expansion, Create power calculator, farm options. */
(function () {
  const R = window.RECIPES || {};
  const ALIAS = (window.ICONS && window.ICONS.alias) || {};
  const QTY = {};
  const BOMS = {};

  /* ---------- tags -> a representative item for icons/names ---------- */
  window.tagAlias = function (id) {
    if (!id || id[0] !== '#') return id;
    if (ALIAS[id]) return ALIAS[id];
    return id;
  };

  function isBase(i) {
    if (!i || i[0] === '#' || i.indexOf(':') < 0) return true;
    if ((G.src || {})[i] && !R[i]) return true; /* farmed by a setup in this guide */
    const [ns, p] = i.split(':');
    if (ns === 'gtceu') return /_(ingot|plate|dust|rod|bolt|screw|gear|foil|nugget|gem|wire|spring|ring|round|rotor|lens|bucket)$/.test(p) || /^(raw_|crushed_)/.test(p);
    if (ns === 'minecraft') return ['hopper', 'chest', 'furnace', 'piston', 'sticky_piston', 'dispenser', 'observer', 'comparator', 'repeater', 'anvil', 'campfire', 'soul_campfire', 'crafting_table', 'barrel', 'blast_furnace', 'smoker', 'cauldron', 'bucket', 'flint_and_steel', 'glass_pane', 'iron_bars', 'redstone_block', 'lever', 'composter'].indexOf(p) < 0;
    if (ns === 'create') return ['andesite_alloy', 'brass_ingot', 'zinc_ingot', 'iron_sheet', 'copper_sheet', 'brass_sheet', 'golden_sheet', 'polished_rose_quartz', 'rose_quartz', 'precision_mechanism', 'sturdy_sheet'].indexOf(p) >= 0;
    return false;
  }
  function expand(id, qty, out, depth) {
    if (/tools\//.test(id)) return;
    const r = R[id];
    if (depth > 7 || !r || isBase(id)) { out[id] = (out[id] || 0) + qty; return; }
    const crafts = Math.ceil(qty / (r.o || 1));
    r.in.forEach(([a, n]) => expand(a, crafts * n, out, depth + 1));
    (r.fl || []).forEach(([f, amt]) => { const k = '~' + f; out[k] = (out[k] || 0) + crafts * (parseInt(amt, 10) || 0); });
  }
  const fmt = n => n >= 10000 ? (n / 1000).toFixed(1) + 'k' : String(n);
  const sl = (id, q) => slot(tagAlias(id), fmt(q));

  function recipeSmall(id, r) {
    const ins = r.in.filter(([a]) => !/tools\//.test(a)).map(([a, n]) => sl(a, n)).join('');
    const kind = r.t === 'crafting' || r.t === 'shapeless' || r.t === 'mechanical_crafting' ? r.t.replace('_', ' ') : r.t.replace(/_/g, ' ');
    return `<div class="recipe"><div class="row">${ins}</div><span class="arrow">&#8594;</span>${slot(id, r.o)}<span class="chip">${esc(kind)}${r.eu ? ' &#183; ' + esc(r.eu) + ' EU/t' : ''}${r.circuit ? ' &#183; circuit ' + r.circuit : ''}</span><span class="chip">${esc(r.s || '')}</span></div>`;
  }

  function bomBody(key) {
    const items = BOMS[key], q = QTY[key] || 1;
    const parts = items.map(([id, n]) => sl(id, n * q)).join('');
    const raw = {};
    items.forEach(([id, n]) => expand(id, n * q, raw, 0));
    const rawList = Object.entries(raw).sort((a, b) => b[1] - a[1]);
    const withRec = items.filter(([id]) => R[id]);
    const missing = items.filter(([id]) => !R[id] && !isBase(id)).map(([id]) => nm(id));
    return `<div class="bomrow"><span class="bl">Parts</span><div class="row">${parts}</div></div>
      <div class="bomrow"><span class="bl">Raw materials</span><div class="row">${rawList.filter(([id]) => id[0] !== '~').map(([id, n]) => sl(id, n)).join('')}${rawList.filter(([id]) => id[0] === '~').map(([id, n]) => `<span class="chip" style="color:var(--fluid);border-color:var(--fluid)">${fmt(n)} mB ${esc(nm(id.slice(1).indexOf(':') < 0 ? 'gtceu:' + id.slice(1) + '_bucket' : id.slice(1) + '_bucket'))}</span>`).join('')}</div></div>
      ${missing.length ? `<p class="mono">No crafting recipe found for: ${esc(missing.join(', '))} (check EMI).</p>` : ''}
      ${withRec.length ? `<details><summary>Recipes for each part</summary>${withRec.map(([id]) => `<div class="mono" style="margin-top:6px">${esc(nm(id))}</div>${recipeSmall(id, R[id])}`).join('')}</details>` : ''}`;
  }
  /* ---------- a multiblock in a list = its whole structure + controller + the buses/hatches it needs ---------- */
  const MI = Object.fromEntries((window.MULTIS || []).map(m => [m.id, m]));
  const HID = { 'Input Bus': 'input_bus', 'Output Bus': 'output_bus', 'Input Hatch': 'input_hatch', 'Output Hatch': 'output_hatch', 'Energy Hatch': 'energy_input_hatch', 'Maintenance Hatch': 'maintenance_hatch', 'Muffler Hatch': 'muffler_hatch' };
  const STD = ['Input Bus', 'Output Bus', 'Input Hatch', 'Output Hatch', 'Energy Hatch', 'Maintenance Hatch'];
  /* where the structure data only says "Buses/Hatches + Energy + Maintenance", or lists more than a working build needs */
  const NEED = {
    'gtceu:electric_blast_furnace': ['Input Bus', 'Output Bus', 'Input Hatch', 'Energy Hatch', 'Maintenance Hatch'],
    'gtceu:pyrolyse_oven': STD, 'gtceu:vacuum_freezer': STD, 'gtceu:large_chemical_reactor': STD,
    'gtceu:cracker': ['Input Hatch', 'Input Hatch', 'Output Hatch', 'Energy Hatch', 'Maintenance Hatch'],
    'gtceu:implosion_compressor': ['Input Bus', 'Output Bus', 'Energy Hatch', 'Maintenance Hatch'],
    'gtceu:distillation_tower': ['Input Hatch', 'Output Bus', 'Energy Hatch', 'Maintenance Hatch', 'Output Hatch', 'Output Hatch', 'Output Hatch', 'Output Hatch'],
    'gtceu:cleanroom': ['Energy Hatch', 'Maintenance Hatch'], 'gtceu:power_substation': ['Maintenance Hatch'],
    'gtceu:kiln': [], 'gtceu:coke_oven': [], 'gtceu:charcoal_pile_igniter': [],
    'gtceu:large_stone_barrel': ['Input Bus', 'Output Hatch'], 'gtceu:large_barrel': ['Input Bus', 'Input Hatch', 'Output Hatch'],
  };
  const TIER = { stone: 'ulv', steam: 'ulv', lv: 'lv', mv: 'mv', hv: 'hv', ev: 'ev', iv: 'iv', luv: 'luv', zpm: 'zpm', uv: 'uv', uhv: 'uhv', uev: 'uev', uiv: 'uiv' };
  window.hatchesOf = function (m) {
    let names = NEED[m.id];
    if (!names) { names = []; m.s.forEach(s => (s.h || []).forEach(h => { if (HID[h] && names.indexOf(h) < 0) names.push(h); })); }
    const et = TIER[m.era] === 'ulv' ? 'lv' : (TIER[m.era] || 'lv'), bt = TIER[m.era] === 'ulv' ? 'ulv' : 'lv';
    const id = n => n === 'Maintenance Hatch' ? 'gtceu:maintenance_hatch' : `gtceu:${n === 'Energy Hatch' || n === 'Muffler Hatch' ? et : bt}_${HID[n]}`;
    return { inSlots: names.map(id), extra: (m.hx || []).map(x => x.nm).filter(n => HID[n]).map(id) };
  };
  window.expandMultis = function (items) {
    const out = {}, add = (id, n) => { if (n > 0) out[id] = (out[id] || 0) + n; };
    items.forEach(([id, n]) => {
      const m = MI[id];
      if (!m) return add(id, n);
      const hs = hatchesOf(m);
      let free = hs.inSlots.length;
      const slots = m.s.some(s => s.h && s.h.length) ? m.s.filter(s => s.h && s.h.length) : m.s.slice(0, 1);
      const cut = new Map();
      slots.forEach(s => { const take = Math.min(free, s.n - (s.min || 0)); if (take > 0) { cut.set(s, take); free -= take; } });
      m.s.forEach(s => add(s.id || 'gtceu:cupronickel_coil_block', (s.n - (cut.get(s) || 0)) * n));
      add(id, n);
      hs.inSlots.concat(hs.extra).forEach(h => add(h, n));
    });
    return Object.entries(out);
  };
  window.bomBox = function (key, items, label) {
    if (!items || !items.length) return '';
    BOMS[key] = items;
    const q = QTY[key] || 1;
    return `<div class="bom" data-bom="${esc(key)}"><div class="bomhead"><b>${esc(label || 'Materials')}</b>
      <span class="qty"><button type="button" data-q-dec="${esc(key)}" aria-label="One less">&#8722;</button><input id="qty-${esc(key)}" data-q-in="${esc(key)}" type="number" min="1" max="999" value="${q}" aria-label="How many to build"><button type="button" data-q-inc="${esc(key)}" aria-label="One more">+</button><span class="mono">&#215; build</span></span></div>
      <div class="bombody">${bomBody(key)}</div></div>`;
  };
  function setQty(key, v) {
    QTY[key] = Math.max(1, Math.min(999, v | 0 || 1));
    document.querySelectorAll(`[data-bom="${CSS.escape(key)}"]`).forEach(el => {
      el.querySelector('.bombody').innerHTML = bomBody(key);
      const inp = el.querySelector('input[data-q-in]'); if (inp && document.activeElement !== inp) inp.value = QTY[key];
    });
  }
  document.addEventListener('click', e => {
    const d = e.target.closest('[data-q-dec]'), i = e.target.closest('[data-q-inc]');
    if (d) setQty(d.dataset.qDec, (QTY[d.dataset.qDec] || 1) - 1);
    if (i) setQty(i.dataset.qInc, (QTY[i.dataset.qInc] || 1) + 1);
  });
  document.addEventListener('input', e => {
    const k = e.target.dataset && e.target.dataset.qIn; if (k) setQty(k, parseInt(e.target.value, 10));
    const c = e.target.closest && e.target.closest('[data-calc]'); if (c) calcUpdate(c);
  });

  /* ---------- Create power calculator ---------- */
  /* magnetic force per magnet, from the StarT wiki (Carbon Brushes and Magnets); a coil takes at most 12 magnets */
  const MAGS = [['magnetite', 'create_new_age:magnetite_block', 1, true], ['redstone', 'create_new_age:redstone_magnet', 2, true], ['layered', 'create_new_age:layered_magnet', 4, true], ['fluxuated', 'create_new_age:fluxuated_magnetite', 8, true], ['netherite', 'create_new_age:netherite_magnet', 24, true]];
  function calcHTML(id, p) {
    const f = (k, l, v, ic) => `<label class="cf">${ic ? icon(ic, 24) : ''}<span class="lbl">${l}</span><input type="number" min="0" data-k="${k}" value="${v}"></label>`;
    return `<div class="calc" data-calc="${esc(id)}"><div class="ttl2">Create power calculator</div>
      <div class="cgrid">${f('rpm', 'Target RPM', p.rpm, 'create:rotation_speed_controller')}${f('engines', 'Steam engines (16 384 SU each)', p.engines || 0, 'create:steam_engine')}${f('windmills', 'Windmills', p.windmills, 'create:windmill_bearing')}${f('sails', 'Sails per windmill', p.sails, 'create:white_sail')}
      ${f('wheels', 'Crushing wheels', p.wheels, 'create:crushing_wheel')}${f('coils', 'Generator coils', p.coils, 'create_new_age:generator_coil')}${f('euNeed', 'EU/t needed', p.euNeed, 'gtceu:lv_1a_energy_converter')}</div>
      <div class="tw"><table class="mtab"><thead><tr><th>Magnet</th><th>per coil (max 12)</th><th>force each</th></tr></thead><tbody>${MAGS.map(([k, ic, s, sure]) => `<tr><td><span class="row">${icon(ic, 24)}<span>${esc(nm(ic))}</span></span></td><td><input type="number" min="0" data-k="m_${k}" value="${p.mag[k] || 0}" aria-label="${esc(nm(ic))} per coil"></td><td><input type="number" min="0" data-k="s_${k}" value="${s}" aria-label="${esc(nm(ic))} force"> ${sure ? '' : '<span class="mono">check tooltip</span>'}</td></tr>`).join('')}</tbody></table></div>
      <div class="cout"></div></div>`;
  }
  function calcUpdate(el) {
    const v = k => { const i = el.querySelector(`[data-k="${k}"]`); return Math.max(0, parseFloat(i && i.value) || 0); };
    const rpm = Math.min(256, v('rpm')), wm = v('windmills'), sails = v('sails'), eng = v('engines');
    const wrpm = Math.min(16, Math.floor(sails / 8));
    const cap = wm * 512 * (sails >= 8 ? wrpm : 0) + eng * 16384;
    const force = MAGS.reduce((s, [k]) => s + v('m_' + k) * v('s_' + k), 0);
    const coils = v('coils'), wheels = v('wheels');
    const perRpm = wheels * 8 + coils * (force + 24);
    const load = perRpm * rpm;
    const fe = coils * rpm * force / 20, eu = fe / 4;
    const maxRpm = perRpm ? Math.min(256, Math.floor(cap / perRpm)) : 256;
    const ok = load <= cap, need = v('euNeed'), at256 = perRpm * 256;
    const pill = (good, t) => `<span class="pill ${good ? 'okp' : 'badp'}">${t}</span>`;
    el.querySelector('.cout').innerHTML = `<div class="row" style="gap:14px">
      ${wm ? `<div><b class="n">${wrpm}</b><span class="mono"> RPM per windmill</span></div>` : ''}${eng ? `<div><b class="n">64</b><span class="mono"> RPM per engine</span></div>` : ''}
      <div><b class="n">${cap.toLocaleString('en')}</b><span class="mono"> SU capacity</span></div>
      <div><b class="n">${Math.round(load).toLocaleString('en')}</b><span class="mono"> SU load</span></div>
      <div><b class="n">${maxRpm}</b><span class="mono"> max RPM</span></div>
      <div><b class="n">${Math.round(fe)}</b><span class="mono"> FE/t</span> = <b class="n">${eu.toFixed(1)}</b><span class="mono"> EU/t</span></div>
      ${pill(ok, ok ? 'stress OK' : 'overstressed')}${need ? pill(eu >= need, eu >= need ? 'enough power' : 'not enough EU') : ''}</div>
      <p class="mono" style="max-width:none">Force per coil ${force} &#183; load ${perRpm} SU per RPM &#183; at 256 RPM that is ${at256.toLocaleString('en')} SU = ${Math.ceil(at256 / 16384)} steam engine(s) or ${Math.ceil(at256 / 8192)} windmill(s) with 128 sails.</p>`;
  }
  window.initCalcs = function () { document.querySelectorAll('[data-calc]').forEach(calcUpdate); };

  /* ---------- setups: how-to + calculator + BOM + options link ---------- */
  const baseChain = window.chainHTML;
  window.chainHTML = function (id) {
    const c = G.chains[id];
    let h = baseChain(id);
    if (!c) return h;
    const extra = (c.how ? `<div class="how"><div class="ttl2">How it is built</div><ol>${c.how.map(s => `<li><span class="row">${s.i.map(x => icon(x, 24)).join('')}</span><span>${esc(s.t)}</span></li>`).join('')}</ol></div>` : '')
      + (c.calc ? calcHTML(id, c.calc) : '')
      + (c.b ? bomBox('ch:' + id, expandMultis(c.b), 'Materials for this setup') + (c.b.some(([x]) => MI[x]) ? '<p class="mono">Multiblocks are counted whole: every structure block, the controller and the buses/hatches it needs (they replace casings).</p>' : '') : '')
      + ((G.optOf || {})[id] ? `<div class="feeds">${G.optOf[id].map(g => `<a class="feed" href="#farms" data-farm="${esc(g.p)}">${icon(g.p, 24)}<span>Other ways to make ${esc(g.t.toLowerCase())}</span><b>&#8594;</b></a>`).join('')}</div>` : '');
    return h.replace(/<\/figure>$/, extra + '</figure>');
  };

  /* ---------- multiblocks: materials x N ---------- */
  const baseMulti = window.multiHTML;
  window.multiHTML = function (m, open) {
    const h = baseMulti(m, open);
    const hs = hatchesOf(m), items = expandMultis([[m.id, 1]]);
    return h.replace(/<\/article>$/, bomBox('m:' + m.id, items, 'Materials to build') + `<p class="mono">Includes ${hs.inSlots.length + hs.extra.length ? 'the minimum buses/hatches (' + esc(hs.inSlots.concat(hs.extra).map(nm).join(', ')) + '), placed instead of casings' : 'every block'}. Coils: any tier.</p></article>`);
  };

  /* ---------- farms tab ---------- */
  window.farmsView = function () {
    return `<h2>Farms &amp; alternatives</h2><p class="goal">Several ways to make each basic resource. Pick by tier, power and what else you need (creosote, oxygen\u2026).</p>
      ${G.options.map(g => `<h3 id="farm-${esc(g.p)}">${icon(g.p)} ${esc(g.t)}</h3><div class="cards">${g.o.map(o => {
        const c = G.chains[o.c] || { t: o.c };
        return `<div class="card opt" id="opt-${esc(o.c)}"><div class="ohd">${o.best ? `<span class="pill okp">Best: ${esc(o.best)}</span>` : ''}${o.mine ? '<span class="pill mine">Your build</span>' : ''}<h4>${esc(c.t)}</h4>
          <div class="row"><span class="chip">${esc(o.tier)}</span><span class="chip">${esc(o.pow)}</span></div>
          <p style="font-size:13.5px"><b>Rate:</b> ${esc(o.rate)}</p><p style="font-size:13.5px;color:var(--ok)">+ ${esc(o.pro)}</p><p style="font-size:13.5px;color:var(--accent)">&#8722; ${esc(o.con)}</p></div>
          <details><summary>Show setup, build steps &amp; materials</summary>${chainHTML(o.c)}</details></div>`;
      }).join('')}</div>`).join('')}`;
  };

  const baseRender = window.render;
  window.render = function () {
    const q = document.getElementById('q').value.trim(), v = (location.hash || '#home').slice(1);
    if (!VIEWS.some(x => x[0] === 'farms')) VIEWS.splice(VIEWS.length - 2, 0, ['farms', 'Farms']);
    if (v === 'farms' && q.length < 2) {
      baseRender();
      document.getElementById('main').innerHTML = farmsView();
    } else baseRender();
    initCalcs();
    document.querySelectorAll('details').forEach(d => d.addEventListener('toggle', initCalcs, { once: true }));
  };
  /* an opened farm option takes the whole row, so its diagram and build steps get full width */
  document.addEventListener('toggle', e => {
    const d = e.target;
    if (!d.matches || !d.matches('.card.opt > details')) return;
    const c = d.parentNode;
    c.classList.toggle('wide', d.open);
    if (d.open) { initCalcs(); requestAnimationFrame(() => c.scrollIntoView({ behavior: 'smooth', block: 'start' })); }
  }, true);
  document.addEventListener('click', e => {
    const f = e.target.closest('[data-farm]');
    if (!f) return;
    e.preventDefault();
    const id = 'farm-' + f.dataset.farm;
    const go = () => { const el = document.getElementById(id); if (el) el.scrollIntoView({ behavior: 'smooth' }); };
    if (location.hash !== '#farms') { location.hash = 'farms'; setTimeout(go, 80); } else go();
  });
  render();
})();
