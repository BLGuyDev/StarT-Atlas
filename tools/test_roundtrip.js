#!/usr/bin/env node
'use strict';
/*
 * Round-trip test: legacy guide*.js  vs  guia/data/wiki-data.js (+ tools/runtime-patches.js if present).
 *
 *   ORIGINAL_GUIDE_DIR=<dir with guide.js..guide24.js> node tools/test_roundtrip.js [--build]
 *
 * Default ORIGINAL_GUIDE_DIR is guia/data. --build regenerates wiki-data.js from docs/ first.
 * Each side runs in its own fake browser window. Checks: same set of new globals, and a strict
 * deep-equal of every global (types, array lengths, values, object key ORDER).
 * Prints the first differing path and exits 1 on failure; prints ROUNDTRIP OK on success.
 */
const fs = require('fs');
const path = require('path');
const W = require('./lib/wiki');

const origDir = path.resolve(process.env.ORIGINAL_GUIDE_DIR || path.join(W.ROOT, 'guia', 'data'));
if (!fs.existsSync(path.join(origDir, 'guide.js'))) {
  console.error('No original guide.js in ' + origDir + '. Set ORIGINAL_GUIDE_DIR to a copy of the legacy guide*.js files.');
  process.exit(2);
}
if (process.argv.includes('--build')) W.writeDataJs(W.readDocs(W.DOCS).G, W.DATA_JS);

const s1 = W.loadGuideFiles(origDir);
const patches = path.join(__dirname, 'runtime-patches.js');
const s2 = W.loadScripts([W.DATA_JS].concat(fs.existsSync(patches) ? [patches] : []));

function kind(v) {
  if (v === null) return 'null';
  if (Array.isArray(v)) return 'array';
  return typeof v;
}
let fail = null, compared = 0;
function eq(a, b, p) {
  if (fail) return;
  compared++;
  const ka = kind(a), kb = kind(b);
  if (ka !== kb) { fail = p + ': type ' + ka + ' vs ' + kb; return; }
  if (ka === 'function') { fail = p + ': function values cannot be compared (move them to tools/runtime-patches.js)'; return; }
  if (ka === 'number') { if (!Object.is(a, b)) fail = p + ': ' + a + ' vs ' + b; return; }
  if (ka !== 'object' && ka !== 'array') { if (a !== b) fail = p + ': ' + JSON.stringify(a) + ' vs ' + JSON.stringify(b); return; }
  if (ka === 'array') {
    if (a.length !== b.length) { fail = p + ': array length ' + a.length + ' vs ' + b.length; return; }
    for (let i = 0; i < a.length && !fail; i++) {
      if ((i in a) !== (i in b)) { fail = p + '[' + i + ']: hole mismatch'; return; }
      eq(a[i], b[i], p + '[' + i + ']');
    }
    return;
  }
  const xa = Object.keys(a), xb = Object.keys(b);
  for (const k of xa) if (!Object.prototype.hasOwnProperty.call(b, k)) { fail = p + '.' + k + ': missing in wiki-data'; return; }
  for (const k of xb) if (!Object.prototype.hasOwnProperty.call(a, k)) { fail = p + '.' + k + ': extra in wiki-data'; return; }
  if (xa.join('\u0000') !== xb.join('\u0000')) {
    const i = xa.findIndex((k, j) => k !== xb[j]);
    fail = p + ': key order differs at #' + i + ' (' + xa[i] + ' vs ' + xb[i] + ')'; return;
  }
  for (const k of xa) { eq(a[k], b[k], p + '.' + k); if (fail) return; }
}

const g1 = W.newGlobals(s1), g2 = W.newGlobals(s2);
console.log('original globals : ' + g1.join(', ') + '   (from ' + origDir + ')');
console.log('wiki-data globals: ' + g2.join(', '));
if (g1.join() !== g2.join()) fail = 'globals differ: [' + g1.join(', ') + '] vs [' + g2.join(', ') + ']';
for (const g of g1) if (!fail) eq(s1[g], s2[g], g);

// Informational: object identity the legacy files had for the derived optOf index.
if (!fail && s2.GUIDE && s2.GUIDE.optOf) {
  let shared = 0, total = 0;
  for (const k of Object.keys(s2.GUIDE.optOf)) for (const g of s2.GUIDE.optOf[k]) { total++; if (s2.GUIDE.options.indexOf(g) >= 0) shared++; }
  console.log('optOf entries sharing identity with options: ' + shared + '/' + total);
}

if (fail) { console.log('ROUNDTRIP FAILED at ' + fail); process.exit(1); }
console.log('compared ' + compared + ' values');
console.log('ROUNDTRIP OK');
