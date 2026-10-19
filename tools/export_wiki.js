#!/usr/bin/env node
'use strict';
/*
 * One-time migration: legacy guia/data/guide*.js  ->  docs/ Markdown wiki.
 *
 *   ORIGINAL_GUIDE_DIR=<dir with guide.js..guide24.js> node tools/export_wiki.js [--force]
 *
 * Default source dir is guia/data. Writes docs/eras, docs/chains, docs/plan, docs/_data and the
 * generated overview pages, then renders every Markdown body from the front matter.
 * Refuses to overwrite an existing wiki (docs/_data/meta.yml) unless --force is given,
 * because docs/ is the source of truth once migrated.
 */
const fs = require('fs');
const path = require('path');
const W = require('./lib/wiki');

const force = process.argv.includes('--force');
const srcDir = path.resolve(process.env.ORIGINAL_GUIDE_DIR || path.join(W.ROOT, 'guia', 'data'));
const docs = W.DOCS;

if (fs.existsSync(path.join(docs, '_data', 'meta.yml')) && !force) {
  console.error('docs/ already holds a wiki (docs/_data/meta.yml). Re-run with --force to overwrite it from ' + srcDir);
  process.exit(1);
}

const sb = W.loadGuideFiles(srcDir);
const globals = W.newGlobals(sb);
if (globals.join() !== 'GUIDE') {
  console.error('guide*.js define unexpected globals: ' + globals.join(', ') + ' (export only handles window.GUIDE)');
  process.exit(1);
}
const G = W.plainCopy(sb.GUIDE);

// --- clean previously generated content (keeps hand-written files such as CONTRIBUTING-CONTENT.md)
for (const d of ['eras', 'chains', 'plan', 'combos', '_data']) fs.rmSync(path.join(docs, d), { recursive: true, force: true });
for (const f of ['index.md', 'resources.md', 'farms.md', 'route.md', 'reference.md']) fs.rmSync(path.join(docs, f), { force: true });

// --- _data
const dataDir = path.join(docs, '_data');
fs.mkdirSync(dataDir, { recursive: true });
const handled = new Set(['pack', 'flagship', 'eras', 'chains', 'phases', 'plan', 'optOf'].concat(W.DATA_FILES));
for (const k of Object.keys(G)) if (!handled.has(k)) { console.error('unhandled GUIDE key ' + k); process.exit(1); }
fs.writeFileSync(path.join(dataDir, 'meta.yml'),
  '# Top-level GUIDE scalars and the key order of window.GUIDE (used by tools/build_data.js).\n' +
  W.YAML.stringify({ pack: G.pack, flagship: G.flagship, key_order: Object.keys(G) }), 'utf8');
for (const n of W.DATA_FILES) {
  fs.writeFileSync(path.join(dataDir, n + '.yml'),
    '# window.GUIDE.' + n + ' - edit here; rebuild with: node tools/build_data.js\n' + W.YAML.stringify({ value: G[n] }), 'utf8');
}

// --- eras
G.eras.forEach((e, i) => W.writePage(path.join(docs, 'eras', e.id + '.md'), { kind: 'era', id: e.id, order: (i + 1) * 10, data: e }, ''));

// --- chains, grouped in folders (folder is cosmetic: build_data.js reads every page)
const eraOf = {}, planEra = {};
G.eras.forEach(e => (e.setups || []).forEach(c => { if (!eraOf[c]) eraOf[c] = e.id; }));
G.plan.forEach(m => { if (m.chain && !planEra[m.chain]) planEra[m.chain] = m.era; });
function group(id) {
  if (/^combo_/.test(id)) return 'combos';
  if (eraOf[id]) return eraOf[id];
  if (/power/.test(id)) return 'power';
  if (planEra[id]) return planEra[id];
  return 'feeders';
}
Object.keys(G.chains).forEach((id, i) => {
  if (!/^[a-z0-9_]+$/.test(id)) throw new Error('chain id not file-safe: ' + id);
  W.writePage(path.join(docs, 'chains', group(id), id + '.md'), { kind: 'chain', id, order: (i + 1) * 10, data: G.chains[id] }, '');
});

// --- plan: one page per phase, modules in plan order
G.phases.forEach((ph, i) => {
  const modules = G.plan.filter(m => m.ph === ph.id);
  W.writePage(path.join(docs, 'plan', ph.id + '.md'), { kind: 'phase', id: ph.id, order: (i + 1) * 10, data: ph, modules }, '');
});
const placed = G.plan.filter(m => G.phases.some(p => p.id === m.ph)).length;
if (placed !== G.plan.length) throw new Error('some plan modules reference an unknown phase');
// plan order must be phase-contiguous for the per-phase layout to be lossless
const runs = G.plan.map(m => m.ph).filter((p, i, a) => i === 0 || a[i - 1] !== p);
if (runs.join() !== G.phases.map(p => p.id).filter(id => runs.indexOf(id) >= 0).join()) throw new Error('plan order is not grouped by phase order');

// --- generated overview pages (no data of their own)
const views = { 'index.md': 'index', 'chains/index.md': 'chains', 'resources.md': 'resources', 'farms.md': 'farms', 'route.md': 'route', 'reference.md': 'reference', 'combos/index.md': 'combos' };
for (const f of Object.keys(views)) W.writePage(path.join(docs, f), { kind: 'view', view: views[f] }, '');

const n = W.renderAll(docs);
console.log('exported ' + G.eras.length + ' eras, ' + Object.keys(G.chains).length + ' chains, ' + G.phases.length + ' phases / ' + G.plan.length + ' modules; ' + n + ' pages rendered into ' + docs);
