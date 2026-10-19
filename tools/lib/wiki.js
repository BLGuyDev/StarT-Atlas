'use strict';
/*
 * Shared helpers for the Markdown wiki (docs/) <-> window.GUIDE pipeline.
 *   loadGuideFiles(dir)   run the legacy guide*.js in a fake browser window
 *   loadScript(file)      run any data script (e.g. wiki-data.js) in a fake window
 *   readDocs(docsDir)     parse every page / _data file and assemble window.GUIDE
 *   renderAll(docsDir)    rebuild every Markdown body from the front matter
 *   writeDataJs(G, file)  write guia/data/wiki-data.js
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const YAML = require('./yaml');
const PANELS = require('./panels');

const ROOT = path.resolve(__dirname, '..', '..');
const DOCS = path.join(ROOT, 'docs');
const DATA_JS = path.join(ROOT, 'guia', 'data', 'wiki-data.js');
const GUIDE_FILES = ['guide.js'].concat(Array.from({ length: 23 }, (_, i) => 'guide' + (i + 2) + '.js'));
const BODY_MARK = '<!-- Generated from the front matter by tools/refresh_body.js. Edit the front matter, not this text. -->';

// Pages that hold data ("kind") and the _data files that hold everything else.
const DATA_FILES = ['tiers', 'mechanics', 'legend', 'resources', 'src', 'once', 'options', 'route'];
const DERIVED = ['optOf']; // rebuilt by build_data.js from options (keeps object identity)
// The only calculator the official wiki links (dynamo fuel / FE per tick). See docs/tools.md.
const POWER_SHEET_URL = 'https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493';

/* ------------------------------------------------------------ fake window */
function makeWindow() {
  const el = () => ({ style: {}, classList: { add() {}, remove() {}, toggle() {} }, setAttribute() {}, appendChild() {}, addEventListener() {}, getContext() { return null; } });
  const sb = {
    document: { addEventListener() {}, getElementById() { return null; }, createElement: el, querySelector() { return null; }, querySelectorAll() { return []; }, body: el() },
    navigator: {}, console,
  };
  sb.window = sb;
  vm.createContext(sb);
  sb.__baseline = Object.keys(sb);
  return sb;
}
function newGlobals(sb) {
  const base = new Set(sb.__baseline.concat(['__baseline']));
  return Object.keys(sb).filter(k => !base.has(k)).sort();
}
function loadGuideFiles(dir) {
  const sb = makeWindow();
  for (const f of GUIDE_FILES) {
    const p = path.join(dir, f);
    if (!fs.existsSync(p)) throw new Error('missing ' + p);
    vm.runInContext(fs.readFileSync(p, 'utf8'), sb, { filename: f });
  }
  return sb;
}
function loadScripts(files) {
  const sb = makeWindow();
  for (const f of files) vm.runInContext(fs.readFileSync(f, 'utf8'), sb, { filename: path.basename(f) });
  return sb;
}
// Brings an object created in another vm context into this realm (plain data only).
function plainCopy(v) { return JSON.parse(JSON.stringify(v)); }

/* ------------------------------------------------------------ page IO */
function splitPage(text, label) {
  text = text.replace(/\r\n?/g, '\n');
  if (!text.startsWith('---\n')) throw new Error('no front matter in ' + label);
  const end = text.indexOf('\n---\n', 3);
  const end2 = end < 0 && text.endsWith('\n---') ? text.length - 4 : end;
  if (end2 < 0) throw new Error('unterminated front matter in ' + label);
  return { fm: YAML.parse(text.slice(4, end2 + 1), label), body: text.slice(end2 + 5) };
}
function writePage(file, fm, body) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, '---\n' + YAML.stringify(fm) + '---\n' + (body || ''), 'utf8');
}
function walkMd(dir, out) {
  out = out || [];
  if (!fs.existsSync(dir)) return out;
  for (const e of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name < b.name ? -1 : 1)) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== '_data') walkMd(p, out); }
    else if (e.name.endsWith('.md')) out.push(p);
  }
  return out;
}
function rel(from, to) { return path.relative(path.dirname(from), to).split(path.sep).join('/'); }

/* ------------------------------------------------------------ docs -> GUIDE */
function readDocs(docsDir) {
  docsDir = docsDir || DOCS;
  const dataDir = path.join(docsDir, '_data');
  const readY = n => YAML.parse(fs.readFileSync(path.join(dataDir, n + '.yml'), 'utf8'), '_data/' + n + '.yml');
  const meta = readY('meta');
  const pages = { chain: [], era: [], phase: [], view: [] };
  const files = {};
  for (const f of walkMd(docsDir)) {
    const label = path.relative(docsDir, f).split(path.sep).join('/');
    const text = fs.readFileSync(f, 'utf8');
    if (!text.startsWith('---')) continue; // plain hand-written page (e.g. CONTRIBUTING-CONTENT.md)
    const { fm, body } = splitPage(text, label);
    if (!fm || !fm.kind) continue;
    if (!pages[fm.kind]) throw new Error('unknown kind "' + fm.kind + '" in ' + label);
    pages[fm.kind].push({ fm, body, file: f, label });
  }
  const byOrder = (a, b) => (a.fm.order - b.fm.order) || (String(a.fm.id) < String(b.fm.id) ? -1 : 1);
  for (const k of ['chain', 'era', 'phase']) {
    const seen = new Set();
    for (const pg of pages[k]) {
      if (typeof pg.fm.id !== 'string' || !pg.fm.id) throw new Error('missing id in ' + pg.label);
      if (typeof pg.fm.order !== 'number') throw new Error('missing numeric order in ' + pg.label);
      if (seen.has(pg.fm.id)) throw new Error('duplicate ' + k + ' id ' + pg.fm.id + ' (' + pg.label + ')');
      seen.add(pg.fm.id);
    }
    pages[k].sort(byOrder);
  }

  const parts = {};
  parts.pack = meta.pack;
  parts.flagship = meta.flagship;
  for (const n of DATA_FILES) parts[n] = readY(n).value;
  parts.eras = pages.era.map(pg => pg.fm.data);
  parts.chains = {};
  for (const pg of pages.chain) parts.chains[pg.fm.id] = pg.fm.data;
  parts.phases = pages.phase.map(pg => pg.fm.data);
  parts.plan = [];
  const modSeen = new Set();
  for (const pg of pages.phase) {
    for (const m of (pg.fm.modules || [])) {
      if (modSeen.has(m.id)) throw new Error('duplicate plan module id ' + m.id + ' (' + pg.label + ')');
      modSeen.add(m.id);
      if (m.ph !== pg.fm.id) console.warn('warning: module ' + m.id + ' has ph=' + m.ph + ' but lives in ' + pg.label);
      parts.plan.push(m);
    }
  }
  parts.optOf = {}; // filled in by deriveOptOf

  const G = {};
  for (const k of meta.key_order) {
    if (!(k in parts)) throw new Error('meta.key_order names unknown key ' + k);
    G[k] = parts[k];
  }
  for (const k of Object.keys(parts)) if (!(k in G)) G[k] = parts[k];
  deriveOptOf(G);

  const paths = { chain: {}, era: {}, phase: {}, docs: docsDir };
  for (const pg of pages.chain) paths.chain[pg.fm.id] = pg.file;
  for (const pg of pages.era) paths.era[pg.fm.id] = pg.file;
  for (const pg of pages.phase) paths.phase[pg.fm.id] = pg.file;
  return { G, pages, paths, meta };
}
function deriveOptOf(G) {
  if (!('optOf' in G)) return;
  const o = {};
  (G.options || []).forEach(g => (g.o || []).forEach(x => { (o[x.c] = o[x.c] || []).push(g); }));
  G.optOf = o;
}

/* ------------------------------------------------------------ GUIDE -> wiki-data.js */
function asciiJson(v) {
  return JSON.stringify(v).replace(/[\u007f-\uffff]/g, c => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0'));
}
function writeDataJs(G, file) {
  const out = ['/* GENERATED by tools/build_data.js from docs/ (the source of truth). Do not edit by hand:',
    '   edit the front matter in docs/ and run "node tools/build_data.js". */',
    'window.GUIDE = {'];
  const keys = Object.keys(G);
  keys.forEach((k, ki) => {
    const v = G[k], last = ki === keys.length - 1 ? '' : ',';
    if (DERIVED.indexOf(k) >= 0) { out.push(asciiJson(k) + ': {}' + last); return; }
    if (Array.isArray(v) && v.length) {
      out.push(asciiJson(k) + ': [');
      v.forEach((x, i) => out.push('  ' + asciiJson(x) + (i === v.length - 1 ? '' : ',')));
      out.push(']' + last);
    } else if (v && typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length > 20) {
      out.push(asciiJson(k) + ': {');
      const ks = Object.keys(v);
      ks.forEach((x, i) => out.push('  ' + asciiJson(x) + ': ' + asciiJson(v[x]) + (i === ks.length - 1 ? '' : ',')));
      out.push('}' + last);
    } else out.push(asciiJson(k) + ': ' + asciiJson(v) + last);
  });
  out.push('};');
  if (keys.indexOf('optOf') >= 0) {
    out.push('/* Derived index: chain id -> farm option groups that list it (same objects as GUIDE.options). */');
    out.push('(function (G) { G.optOf = {}; G.options.forEach(function (g) { g.o.forEach(function (o) { (G.optOf[o.c] = G.optOf[o.c] || []).push(g); }); }); })(window.GUIDE);');
  }
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, out.join('\n') + '\n', 'utf8');
}

/* ------------------------------------------------------------ Markdown rendering */
const ARROW = '\u2192', DOT = '\u00b7', DASH = '\u2014';
function esc(s) {
  return String(s).replace(/\\/g, '\\\\').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/([*_`\[\]])/g, '\\$1');
}
function cell(s) { return esc(s).replace(/\|/g, '\\|'); }
function code(id) { return '`' + String(id).replace(/`/g, '') + '`'; }
function items(list) { return (list || []).map(code).join(', '); }
function tipTag(t) {
  if (/^Unverified:/i.test(t)) return '**Unverified** ';
  if (/^Verified:/i.test(t)) return '**Verified** ';
  return '';
}
function tipText(t) { return tipTag(t) + esc(String(t).replace(/^(Unverified|Verified):\s*/i, '')); }

function buildIndex(G, paths) {
  const ix = { srcBy: {}, eraOfChain: {}, modsOfChain: {}, needs: {}, feeds: {}, phaseOfEra: {} };
  for (const item of Object.keys(G.src || {})) (ix.srcBy[G.src[item]] = ix.srcBy[G.src[item]] || []).push(item);
  (G.eras || []).forEach(e => (e.setups || []).forEach(c => (ix.eraOfChain[c] = ix.eraOfChain[c] || []).push(e)));
  (G.plan || []).forEach(m => [m.chain].concat(m.more || []).forEach(c => { if (c) (ix.modsOfChain[c] = ix.modsOfChain[c] || []).push(m); }));
  (G.phases || []).forEach(p => (ix.phaseOfEra[p.era] = ix.phaseOfEra[p.era] || []).push(p));
  for (const id of Object.keys(G.chains || {})) {
    const c = G.chains[id], need = new Set();
    (c.n || []).forEach(n => { if ((n[2] === 'i' || n[2] === 's') && n[3]) { const s = G.src[n[3]]; if (s && s !== id && G.chains[s]) need.add(s); } });
    ix.needs[id] = [...need];
    need.forEach(s => (ix.feeds[s] = ix.feeds[s] || []).push(id));
  }
  ix.paths = paths;
  return ix;
}
function chainLink(ix, from, id) {
  const c = ix.G.chains[id];
  if (!c || !ix.paths.chain[id]) return code(id);
  return '[' + esc(c.t) + '](' + rel(from, ix.paths.chain[id]) + ')';
}
function eraLink(ix, from, id) {
  const e = (ix.G.eras || []).find(x => x.id === id);
  if (!e || !ix.paths.era[id]) return code(id);
  return '[' + esc(e.name) + '](' + rel(from, ix.paths.era[id]) + ')';
}
function modLink(ix, from, m) {
  const f = ix.paths.phase[m.ph];
  return f ? '[' + esc(m.t) + '](' + rel(from, f) + '#' + m.id + ')' : esc(m.t);
}

function renderChain(ix, id, file) {
  const G = ix.G, c = G.chains[id], L = [];
  const tips = c.tips || [];
  const unv = tips.filter(t => /^Unverified:/i.test(t)).length, ver = tips.filter(t => /^Verified:/i.test(t)).length;
  const tags = [];
  if (c.inf) tags.push('Infinite source');
  if (c.hero) tags.push('Hero build');
  if (c.power) tags.push('Power');
  if (c.s3d) tags.push('3D scene');
  if (unv) tags.push('Unverified'); else if (ver) tags.push('Verified');
  L.push('# ' + esc(c.t), '', BODY_MARK, '');
  L.push('**Chain id:** ' + code(id) + (tags.length ? ' ' + DOT + ' **Tags:** ' + tags.join(', ') : ''));
  const eras = ix.eraOfChain[id] || [], mods = ix.modsOfChain[id] || [];
  if (eras.length) L.push('', '**Era setup:** ' + eras.map(e => eraLink(ix, file, e.id)).join(', '));
  if (mods.length) L.push('', '**Plan modules:** ' + mods.map(m => modLink(ix, file, m)).join(', '));
  if (tips.length) L.push('', '**Tips:** ' + tips.length + (ver ? ', ' + ver + ' verified' : '') + (unv ? ', ' + unv + ' unverified' : ''));

  if (c.power && POWER_SHEET_URL) {
    L.push('', '!!! tip "Plan this chain"', '',
      '    Estimate dynamo fuel use and FE/t with the community [dynamo calculator](' + POWER_SHEET_URL + ') (a Google Sheet linked from the official wiki; Unverified: its contents and whether it is specific to this pack). More in [Calculators and planners](' + rel(file, path.join(ix.paths.docs, 'tools.md')) + ').');
  }
  const mach = PANELS.renderMachineSections(c, { tiers: G.tiers, relIcons: rel(file, path.join(ix.paths.docs, 'assets', 'icons')), esc });
  if (mach) mach.forEach(x => L.push(x));
  else if ((c.n || []).length) {
    L.push('', '## Flow', '', '| Node | Role | Item |', '| --- | --- | --- |');
    const lbl = {};
    c.n.forEach(n => { lbl[n[0]] = n[1]; L.push('| ' + cell(n[1]) + ' | ' + cell((G.legend || {})[n[2]] || n[2]) + ' | ' + (n[3] ? code(n[3]) : '') + ' |'); });
    if ((c.e || []).length) {
      L.push('');
      c.e.forEach(e => L.push('- ' + esc(lbl[e[0]] || e[0]) + ' ' + ARROW + ' ' + esc(lbl[e[1]] || e[1]) + (e[2] ? ' (' + esc(e[2]) + ')' : '')));
    }
  }
  if ((c.how || []).length) {
    L.push('', '## How to build', '');
    c.how.forEach((h, i) => L.push((i + 1) + '. ' + esc(h.t) + ((h.i || []).length ? ' ' + DASH + ' ' + items(h.i) : '')));
  }
  if (tips.length) { L.push('', '## Tips', ''); tips.forEach(t => L.push('- ' + tipText(t))); }
  if ((c.b || []).length) {
    L.push('', '## Bill of materials', '', '| Item | Qty |', '| --- | ---: |');
    c.b.forEach(b => L.push('| ' + code(b[0]) + ' | ' + b[1] + ' |'));
  }
  if ((c.store || []).length) L.push('', '## Storage', '', items(c.store));
  const needs = ix.needs[id] || [], feeds = ix.feeds[id] || [], prod = ix.srcBy[id] || [];
  if (needs.length || feeds.length || prod.length) {
    L.push('', '## Needs / Feeds', '');
    if (needs.length) L.push('- **Needs:** ' + needs.map(s => chainLink(ix, file, s)).join(', '));
    if (feeds.length) L.push('- **Feeds:** ' + feeds.map(s => chainLink(ix, file, s)).join(', '));
    if (prod.length) L.push('- **Main source for:** ' + items(prod));
  }
  const extra = [];
  if (c.s3d) extra.push('3D assembly scene with ' + ((c.s3d.b || []).length) + ' blocks (open it in the Atlas page).');
  if (c.calc) extra.push('Power calculator defaults are stored in the front matter (`calc`).');
  if (extra.length) { L.push('', '## Extras', ''); extra.forEach(x => L.push('- ' + x)); }
  return L.join('\n') + '\n';
}

function renderEra(ix, e, file) {
  const G = ix.G, L = [];
  L.push('# ' + esc(e.name) + (e.sub ? ' ' + DASH + ' ' + esc(e.sub) : ''), '', BODY_MARK, '');
  L.push('**Era id:** ' + code(e.id) + ' ' + DOT + ' **Tier:** ' + code(e.tier));
  if (e.goal) L.push('', '**Goal:** ' + esc(e.goal));
  if ((e.exit || []).length) L.push('', '**Exit items:** ' + items(e.exit));
  if (e.route) L.push('', '> ' + esc(e.route));
  if ((e.steps || []).length) {
    L.push('', '## Steps', '');
    e.steps.forEach((s, i) => L.push((i + 1) + '. **' + esc(s.t) + '** ' + DASH + ' ' + esc(s.d || '') + ((s.i || []).length ? ' (' + items(s.i) + ')' : '')));
  }
  if ((e.build || []).length) {
    L.push('', '## Machines to build', '', '| Machine | Count |', '| --- | ---: |');
    e.build.forEach(b => L.push('| ' + code(b.id) + ' | ' + cell(b.n) + ' |'));
  }
  if ((e.setups || []).length) { L.push('', '## Setups', ''); e.setups.forEach(s => L.push('- ' + chainLink(ix, file, s))); }
  if (e.power) L.push('', '## Power', '', chainLink(ix, file, e.power));
  if ((e.storage || []).length) {
    L.push('', '## Storage', '');
    e.storage.forEach(s => L.push('- **' + esc(s.k) + ':** ' + esc(s.v) + ((s.i || []).length ? ' (' + items(s.i) + ')' : '')));
  }
  if ((e.multis || []).length) L.push('', '## Multiblocks', '', items(e.multis));
  const ph = ix.phaseOfEra[e.id] || [];
  if (ph.length) {
    L.push('', '## Plan phases', '');
    ph.forEach(p => L.push('- [' + esc(p.t) + '](' + rel(file, ix.paths.phase[p.id]) + ')'));
  }
  return L.join('\n') + '\n';
}

function renderPhase(ix, ph, mods, file) {
  const L = [];
  L.push('# ' + esc(ph.t), '', BODY_MARK, '');
  L.push('**Phase id:** ' + code(ph.id) + ' ' + DOT + ' **Era:** ' + eraLink(ix, file, ph.era));
  if (ph.goal) L.push('', esc(ph.goal));
  mods.forEach(m => {
    L.push('', '<a id="' + m.id + '"></a>', '', '## ' + esc(m.t), '');
    L.push('- **Module key:** ' + code('plan:' + m.id) + (m.n != null ? ' ' + DOT + ' step ' + m.n : '') + (m.cera ? ' ' + DOT + ' combo for era ' + code(m.cera) : ''));
    if (m.chain) L.push('- **Chain:** ' + chainLink(ix, file, m.chain) + ((m.more || []).length ? '; also ' + m.more.map(c => chainLink(ix, file, c)).join(', ') : ''));
    if ((m.uses || []).length) L.push('- **Uses:** ' + items(m.uses));
    if ((m.makes || []).length) L.push('- **Makes:** ' + items(m.makes));
    if ((m.stock || []).length) L.push('- **Stock:** ' + m.stock.map(s => code(s[0]) + ' in ' + esc(s[1])).join(', '));
    if (m.power) L.push('- **Power:** ' + esc(m.power));
    if ((m.watch || []).length) { L.push('- **Watch out:**'); m.watch.forEach(w => L.push('    - ' + tipText(w))); }
  });
  return L.join('\n') + '\n';
}

function renderView(ix, view, file) {
  const G = ix.G, L = [];
  const head = t => { L.push('# ' + t, '', BODY_MARK, ''); };
  if (view === 'index') {
    head('Star Technology Atlas ' + DASH + ' wiki');
    L.push('**Pack:** ' + esc(G.pack), '', 'This wiki is the source of truth for the Atlas page data. See [CONTRIBUTING-CONTENT.md](CONTRIBUTING-CONTENT.md).');
    L.push('', '## Eras', '');
    (G.eras || []).forEach(e => L.push('- ' + eraLink(ix, file, e.id) + (e.sub ? ' ' + DASH + ' ' + esc(e.sub) : '')));
    L.push('', '## Plan', '');
    (G.phases || []).forEach(p => L.push('- [' + esc(p.t) + '](' + rel(file, ix.paths.phase[p.id]) + ') (' + G.plan.filter(m => m.ph === p.id).length + ' modules)'));
    L.push('', '## Chains', '');
    const groups = {};
    Object.keys(G.chains).forEach(id => { const g = path.basename(path.dirname(ix.paths.chain[id])); (groups[g] = groups[g] || []).push(id); });
    Object.keys(groups).forEach(g => L.push('- [' + esc(g) + '](' + rel(file, path.join(ix.paths.docs, 'chains', 'index.md')) + '#' + g + ') ' + DASH + ' ' + groups[g].length + ' chains'));
    L.push('', '## Reference', '', '- [Resources (sieve tables)](resources.md)', '- [Farm options](farms.md)', '- [Build route](route.md)', '- [Tiers, mechanics, legend](reference.md)', '- [Combos](combos/index.md)', '- [Calculators and planners](tools.md)');
    L.push('', 'Flagship build: ' + chainLink(ix, file, G.flagship));
  } else if (view === 'chains') {
    head('All chains');
    const groups = {};
    Object.keys(G.chains).forEach(id => { const g = path.basename(path.dirname(ix.paths.chain[id])); (groups[g] = groups[g] || []).push(id); });
    Object.keys(groups).forEach(g => { L.push('', '<a id="' + g + '"></a>', '', '## ' + esc(g), ''); groups[g].forEach(id => L.push('- ' + chainLink(ix, file, id) + ' ' + code(id))); });
  } else if (view === 'resources') {
    head('Resources');
    L.push('Data: `docs/_data/resources.yml`.');
    for (const k of Object.keys(G.resources || {})) {
      L.push('', '## ' + esc(k), '');
      (G.resources[k] || []).forEach(r => {
        L.push('### ' + code(r.b), '', '| Drop | Value |', '| --- | ---: |');
        (r.r || []).forEach(x => L.push('| ' + code(x[0]) + ' | ' + x[1] + ' |'));
        L.push('');
      });
    }
  } else if (view === 'farms') {
    head('Farm options');
    L.push('Data: `docs/_data/options.yml`.');
    (G.options || []).forEach(g => {
      L.push('', '## ' + esc(g.t) + ' (' + code(g.p) + ')', '', '| Chain | Tier | Power | Rate | Pro | Con | Best |', '| --- | --- | --- | --- | --- | --- | --- |');
      (g.o || []).forEach(o => L.push('| ' + chainLink(ix, file, o.c) + ' | ' + cell(o.tier || '') + ' | ' + cell(o.pow || '') + ' | ' + cell(o.rate || '') + ' | ' + cell(o.pro || '') + ' | ' + cell(o.con || '') + ' | ' + cell(o.best || '') + ' |'));
    });
  } else if (view === 'route') {
    head('Build route');
    L.push('Data: `docs/_data/route.yml`.');
    (G.route || []).forEach((r, i) => {
      L.push('', '## ' + (i + 1) + '. ' + esc(r.t), '', '**Era:** ' + eraLink(ix, file, r.era) + ' ' + DOT + ' **Chains:** ' + (r.chains || []).map(c => chainLink(ix, file, c)).join(', '));
      if (r.goal) L.push('', esc(r.goal));
      (r.miss || []).forEach(m => L.push('- ' + tipText(m)));
    });
  } else if (view === 'reference') {
    head('Tiers, mechanics and legend');
    L.push('Data: `docs/_data/tiers.yml`, `mechanics.yml`, `legend.yml`, `once.yml`, `meta.yml`.');
    L.push('', '## Tiers', '', '| Tier | EU/t | Superconductor | Hull | Material |', '| --- | ---: | --- | --- | --- |');
    (G.tiers || []).forEach(t => L.push('| ' + cell(t.k) + ' | ' + t.eu + ' | ' + (t.sc ? code(t.sc) : '') + ' | ' + (t.hull ? code(t.hull) : '') + ' | ' + (t.mat ? code(t.mat) : '') + ' |'));
    L.push('', '## Mechanics', '');
    (G.mechanics || []).forEach(m => L.push('- **' + esc(m.t) + '** (' + code(m.i) + '): ' + esc(m.d)));
    L.push('', '## Node legend', '');
    Object.keys(G.legend || {}).forEach(k => L.push('- ' + code(k) + ': ' + esc(G.legend[k])));
    L.push('', '## Build once', '', items(G.once));
  } else if (view === 'combos') {
    head('Combos');
    const ph = (G.phases || []).filter(p => G.plan.some(m => m.ph === p.id && m.cera));
    ph.forEach(p => {
      L.push('Phase: [' + esc(p.t) + '](' + rel(file, ix.paths.phase[p.id]) + ')', '');
      G.plan.filter(m => m.ph === p.id).forEach(m => L.push('- ' + modLink(ix, file, m) + (m.cera ? ' (era ' + code(m.cera) + ')' : '') + ' ' + DASH + ' ' + chainLink(ix, file, m.chain)));
    });
    const combos = Object.keys(G.chains).filter(id => /^combo_/.test(id));
    if (combos.length) { L.push('', '## Combo chains', ''); combos.forEach(id => L.push('- ' + chainLink(ix, file, id))); }
  } else throw new Error('unknown view ' + view);
  return L.join('\n') + '\n';
}

// Rebuilds every generated body from the front matter. Returns number of pages written.
function renderAll(docsDir) {
  const d = readDocs(docsDir);
  const ix = buildIndex(d.G, d.paths);
  ix.G = d.G;
  let n = 0;
  const put = (pg, body) => {
    const text = fs.readFileSync(pg.file, 'utf8').replace(/\r\n?/g, '\n');
    const fmEnd = text.indexOf('\n---\n', 3) + 5;
    const next = text.slice(0, fmEnd) + body;
    if (next !== text) fs.writeFileSync(pg.file, next, 'utf8');
    n++;
  };
  for (const pg of d.pages.chain) put(pg, renderChain(ix, pg.fm.id, pg.file));
  for (const pg of d.pages.era) put(pg, renderEra(ix, pg.fm.data, pg.file));
  for (const pg of d.pages.phase) put(pg, renderPhase(ix, pg.fm.data, pg.fm.modules || [], pg.file));
  for (const pg of d.pages.view) put(pg, renderView(ix, pg.fm.view, pg.file));
  return n;
}

module.exports = {
  ROOT, DOCS, DATA_JS, GUIDE_FILES, DATA_FILES, BODY_MARK,
  loadGuideFiles, loadScripts, newGlobals, plainCopy,
  splitPage, writePage, readDocs, writeDataJs, renderAll, YAML,
};
