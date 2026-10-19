'use strict';
/*
 * Machine UI panels for the chain pages (used by renderChain in wiki.js).
 *
 * Every machine / generator node of a chain becomes one HTML panel that looks like a GregTech machine GUI:
 * input slots on the left (edges that end at the machine), machine name + tier badge + EU/t + time in the
 * middle, output slots on the right (edges that start at the machine). Styles: docs/stylesheets/panels.css.
 * Only data from the chain front matter is used (node label / type / item id, edge label, G.tiers).
 *
 * Output is plain HTML without blank lines (so Markdown keeps it as one raw block) and needs no JavaScript.
 * Optional icons: <img src=".../assets/icons/<namespace>__<path>.png" onerror=...>. hooks/atlas_docs.py rewrites
 * the path for the built site and drops the <img> when the file does not exist.
 */
const path = require('path');

const ARROW = '\u2192', DOT = '\u00b7';
const UPPER = { lv: 'LV', mv: 'MV', hv: 'HV', ev: 'EV', iv: 'IV', luv: 'LuV', zpm: 'ZPM', uv: 'UV', uhv: 'UHV', uev: 'UEV',
  uiv: 'UIV', uxv: 'UXV', opv: 'OpV', ulv: 'ULV', hsla: 'HSLA', abs: 'ABS', ptfe: 'PTFE', pbi: 'PBI', pvc: 'PVC', smd: 'SMD',
  soc: 'SoC', asmd: 'ASMD', ram: 'RAM', cpu: 'CPU', led: 'LED', ebf: 'EBF', pbf: 'PBF', nand: 'NAND', nor: 'NOR',
  ulpic: 'ULPIC', lpic: 'LPIC', ppic: 'PPIC', hpic: 'HPIC', nanocpu: 'NanoCPU', qram: 'QRAM', uhpic: 'UHPIC', uepic: 'UEPIC',
  ae2: 'AE2', me: 'ME', rf: 'RF', dna: 'DNA', rna: 'RNA', cwu: 'CWU', ecr: 'ECR', lcr: 'LCR' };
const TIER_RE = /^(ulv|lv|mv|hv|ev|iv|luv|zpm|uv|uhv|uev|uiv|uxv|opv|max)_/;
const MULTI_RE = /^(large_|mega_|electric_blast_furnace|primitive_blast_furnace|pyrolyse_oven|distillation_tower|cracker$|vacuum_freezer|implosion_compressor|coke_oven$|cleanroom$|assembly_line$|alloy_blast_smelter|super_ebf)/;
const MODS = { gtceu: 'GregTech', create: 'Create', create_new_age: 'New Age', createlowheated: 'Create', thermal: 'Thermal',
  exnihilosequentia: 'Ex Nihilo', start_core: 'StarT', systeams: 'Systeams', minecraft: 'Vanilla', functionalstorage: 'Storage' };

function h(s) {
  return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function splitId(id) {
  const s = String(id || '').replace(/^#/, '');
  const i = s.indexOf(':');
  return i < 0 ? { ns: 'minecraft', p: s } : { ns: s.slice(0, i), p: s.slice(i + 1) };
}
// gtceu:copper_ingot -> "Copper Ingot", gtceu:lv_wiremill -> "LV Wiremill", gtceu:tin_alloy_bucket -> "Tin Alloy" (fluid)
function itemName(id, fluid) {
  let p = splitId(id).p.split('/').pop();
  if (fluid) p = p.replace(/_bucket$/, '');
  return p.split('_').filter(Boolean).map(w => UPPER[w] || (w.charAt(0).toUpperCase() + w.slice(1))).join(' ');
}
function iconFile(id) {
  const t = splitId(id);
  return t.ns + '__' + t.p.replace(/\//g, '__') + '.png';
}
function tierOf(id, tiers) {
  const m = TIER_RE.exec(splitId(id).p);
  if (!m) return null;
  const k = m[1];
  const t = (tiers || []).find(x => String(x.k).toLowerCase() === k);
  return t ? { k: t.k, cls: k, eu: t.eu } : { k: UPPER[k] || k.toUpperCase(), cls: k, eu: null };
}
function fmtNum(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '\u202f'); }

// "1 / 30 s" -> qty "1", time "30 s";  "10 s" -> time;  "500 mB \u00b7 10 s" -> qty + time;  anything else -> qty.
const TIME_RE = /^[~\u2248]?\s*[\d.,\u2013-]+\s*(?:s|sec|min|ticks?)\b/i;
function parseLabel(label) {
  const raw = label == null ? '' : String(label).trim();
  if (!raw) return { qty: '', time: '' };
  if (/^[\d.,]+\s*s$/i.test(raw)) return { qty: '', time: raw };
  const slash = raw.split(' / ');
  if (slash.length === 2 && TIME_RE.test(slash[1])) return { qty: slash[0].trim(), time: slash[1].trim() };
  const dots = raw.split(' ' + DOT + ' ');
  if (dots.length === 2 && TIME_RE.test(dots[1].trim())) return { qty: dots[0].trim(), time: dots[1].trim() };
  if (dots.length === 2 && TIME_RE.test(dots[0].trim())) return { qty: dots[1].trim(), time: dots[0].trim() };
  return { qty: raw, time: '' };
}

function iconImg(id, relIcons) {
  if (!id) return '';
  return '<img class="gt-ico" src="' + h(relIcons + '/' + iconFile(id)) + '" alt="" loading="lazy" onerror="this.remove()">';
}

function slotHtml(node, qty, ctx) {
  const type = node[2], id = node[3] || '';
  const fluid = type === 'f';
  const name = id ? itemName(id, fluid) : node[1];
  const cls = { f: 'gt-fluid', m: 'gt-mach', p: 'gt-power', s: 'gt-inf', o: 'gt-outp', g: 'gt-group' }[type] || '';
  const tip = node[1] + (id ? ' (' + id + ')' : '') + (qty.raw ? ' - ' + qty.raw : '');
  let inner = iconImg(id, ctx.relIcons);
  inner += '<span class="gt-nm">' + h(name) + '</span>';
  if (node[1] && name.toLowerCase().indexOf(node[1].toLowerCase()) < 0) inner += '<span class="gt-note">' + h(node[1]) + '</span>';
  if (type === 'g' && Array.isArray(node[4])) {
    inner += '<span class="gt-sub">' + node[4].map(s => '<span>' + h(s[0]) + (s[2] ? ' <i>' + h(s[2]) + '</i>' : '') + '</span>').join('') + '</span>';
  }
  if (type === 's') inner += '<span class="gt-tag">infinite</span>';
  if (qty.qty) inner += '<b class="gt-q">' + h(qty.qty) + '</b>';
  const open = (type === 'm' || type === 'p') && ctx.panelIds.has(node[0])
    ? '<a class="' + ('gt-slot ' + cls).trim() + '" href="#m-' + h(node[0]) + '" title="' + h(tip) + '">'
    : '<span class="' + ('gt-slot ' + cls).trim() + '" title="' + h(tip) + '">';
  return open + inner + (open.charAt(1) === 'a' ? '</a>' : '</span>');
}

function modeOf(id, tiers) {
  const t = splitId(id);
  const tier = tierOf(id, tiers);
  if (tier) {
    const amps = /(?:^|_)(\d+)a(?:_|$)/.exec(t.p); // e.g. lv_4a_energy_converter: 4 amps
    return { badge: tier.k, cls: 't-' + tier.cls, eu: tier.eu && amps ? tier.eu * Number(amps[1]) : tier.eu };
  }
  if (t.ns === 'gtceu' && MULTI_RE.test(t.p)) return { badge: 'Multiblock', cls: 't-multi', eu: null };
  return { badge: MODS[t.ns] || (t.ns.charAt(0).toUpperCase() + t.ns.slice(1)), cls: 't-mod', eu: null };
}
function panelHtml(node, ins, outs, ctx) {
  const id = node[3] || '';
  const mode = modeOf(id, ctx.tiers);
  const power = node[2] === 'p';
  const times = [];
  ins.concat(outs).forEach(x => { if (x.time && times.indexOf(x.time) < 0) times.push(x.time); });
  const L = [];
  L.push('<div class="gt-panel ' + mode.cls + (power ? ' gt-gen' : '') + '" id="m-' + h(node[0]) + '">');
  L.push('<div class="gt-head"><span class="gt-mname">' + h(node[1]) + '</span>' +
    '<span class="gt-badge ' + mode.cls + '">' + h(mode.badge) + '</span>' + (power ? '<span class="gt-badge t-gen">Generator</span>' : '') + '</div>');
  L.push('<div class="gt-body">');
  L.push('<div class="gt-col gt-in" role="group" aria-label="Inputs">' + (ins.length ? ins.map(x => slotHtml(x.node, x, ctx)).join('') : '<span class="gt-empty">no listed input</span>') + '</div>');
  const stats = [];
  if (mode.eu) stats.push('up to ' + fmtNum(mode.eu) + ' EU/t');
  if (times.length) stats.push(times.slice(0, 3).join(' ' + DOT + ' '));
  L.push('<div class="gt-mid">' + iconImg(id, ctx.relIcons) + '<span class="gt-arrow" aria-hidden="true"></span>' +
    stats.map(s => '<span class="gt-stat">' + h(s) + '</span>').join('') + '</div>');
  L.push('<div class="gt-col gt-outc" role="group" aria-label="Outputs">' + (outs.length ? outs.map(x => slotHtml(x.node, x, ctx)).join('') : '<span class="gt-empty">no listed output</span>') + '</div>');
  L.push('</div>');
  if (id) L.push('<div class="gt-foot"><code>' + h(id) + '</code></div>');
  L.push('</div>');
  return L.join('\n');
}

/*
 * Returns Markdown lines for the "Machines" and "Flow" sections of a chain, or null when the chain has no
 * machine node (the caller then keeps the plain node table).
 *   c      chain data (t, n, e, ...)
 *   opts   { tiers, relIcons, esc }   esc = Markdown escaper of wiki.js
 */
function renderMachineSections(c, opts) {
  const nodes = c.n || [], edges = c.e || [];
  const byId = {};
  nodes.forEach(n => { byId[n[0]] = n; });
  const isPanel = n => n[2] === 'm' || n[2] === 'p';
  const panels = nodes.filter(isPanel);
  if (!panels.length) return null;
  const ctx = { tiers: opts.tiers || [], relIcons: opts.relIcons, panelIds: new Set(panels.map(n => n[0])) };
  const esc = opts.esc;

  const ioOf = pid => {
    const ins = [], outs = [], seenIn = new Set(), seenOut = new Set();
    edges.forEach(e => {
      const p = parseLabel(e[2]);
      const rec = o => Object.assign({ raw: e[2] || '' }, p, o);
      if (e[1] === pid && byId[e[0]]) { const k = e[0] + '|' + (e[2] || ''); if (!seenIn.has(k)) { seenIn.add(k); ins.push(rec({ node: byId[e[0]] })); } }
      if (e[0] === pid && byId[e[1]]) { const k = e[1] + '|' + (e[2] || ''); if (!seenOut.has(k)) { seenOut.add(k); outs.push(rec({ node: byId[e[1]] })); } }
    });
    return { ins, outs };
  };

  const L = ['', '## Machines', '', '<div class="gt-panels">'];
  panels.forEach(n => { const io = ioOf(n[0]); L.push(panelHtml(n, io.ins, io.outs, ctx)); });
  L.push('</div>');

  // Collapsed graph: machine -> machines reached through any chain of non-machine nodes.
  const succ = {}; // direct successors of every node
  edges.forEach(e => { (succ[e[0]] = succ[e[0]] || []).push(e[1]); });
  const next = {};
  panels.forEach(n => {
    const found = [], seen = new Set();
    const walk = id => (succ[id] || []).forEach(t => {
      if (seen.has(t)) return;
      seen.add(t);
      if (ctx.panelIds.has(t)) { if (found.indexOf(t) < 0) found.push(t); } else walk(t);
    });
    walk(n[0]);
    next[n[0]] = found;
  });
  const hasPred = new Set();
  Object.keys(next).forEach(k => next[k].forEach(t => hasPred.add(t)));
  const link = id => '[' + esc(byId[id][1]) + '](#m-' + id + ')';
  const done = new Set(), lines = [];
  const order = panels.map(n => n[0]);
  // start from machines without a machine predecessor, then from whatever is left
  order.filter(id => !hasPred.has(id)).concat(order).forEach(start => {
    if (done.has(start)) return;
    const chain = [start];
    done.add(start);
    for (let cur = start; ;) {
      const nx = next[cur].filter(t => !done.has(t));
      if (!nx.length) break;
      cur = nx[0];
      done.add(cur);
      chain.push(cur);
    }
    const also = [];
    chain.forEach((m, i) => next[m].forEach(t => { if (i < chain.length - 1 && t !== chain[i + 1]) also.push([m, t]); }));
    let line = '- ' + chain.map(link).join(' ' + ARROW + ' ');
    const tail = next[chain[chain.length - 1]];
    if (tail.length) line += ' ' + ARROW + ' ' + tail.map(link).join(', ');
    if (also.length) line += ' (also ' + also.map(([a, b]) => esc(byId[a][1]) + ' ' + ARROW + ' ' + link(b)).join(', ') + ')';
    lines.push(line);
  });
  L.push('', '## Flow', '', ...lines);

  // Steps that do not touch any panel (hand crafting, alloying inside another recipe, ...).
  const direct = edges.filter(e => !ctx.panelIds.has(e[0]) && !ctx.panelIds.has(e[1]) && byId[e[0]] && byId[e[1]]);
  if (direct.length) {
    L.push('', '### Direct steps', '');
    direct.forEach(e => L.push('- ' + esc(byId[e[0]][1]) + ' ' + ARROW + ' ' + esc(byId[e[1]][1]) + (e[2] ? ' (' + esc(e[2]) + ')' : '')));
  }
  // Nodes that appear in no edge at all.
  const used = new Set();
  edges.forEach(e => { used.add(e[0]); used.add(e[1]); });
  const lone = nodes.filter(n => !used.has(n[0]));
  if (lone.length) L.push('', '### Other items', '', lone.map(n => esc(n[1])).join(', '));
  return L;
}

module.exports = { renderMachineSections, itemName, parseLabel, tierOf, iconFile, splitId };
