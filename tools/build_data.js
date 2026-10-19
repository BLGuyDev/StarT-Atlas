#!/usr/bin/env node
'use strict';
/*
 * docs/ (front matter + docs/_data/*.yml)  ->  guia/data/wiki-data.js  (window.GUIDE)
 *
 *   node tools/build_data.js [--check]
 *
 * --check: build in memory and exit 1 if guia/data/wiki-data.js is out of date.
 */
const fs = require('fs');
const os = require('os');
const path = require('path');
const W = require('./lib/wiki');

const d = W.readDocs(W.DOCS);
const G = d.G;
if (process.argv.includes('--check')) {
  const tmp = path.join(os.tmpdir(), 'wiki-data-check-' + process.pid + '.js');
  W.writeDataJs(G, tmp);
  const same = fs.existsSync(W.DATA_JS) && fs.readFileSync(tmp, 'utf8') === fs.readFileSync(W.DATA_JS, 'utf8');
  fs.rmSync(tmp, { force: true });
  console.log(same ? 'wiki-data.js is up to date' : 'wiki-data.js is STALE: run node tools/build_data.js');
  process.exit(same ? 0 : 1);
}
W.writeDataJs(G, W.DATA_JS);
console.log('wrote ' + path.relative(W.ROOT, W.DATA_JS) + ': ' + G.eras.length + ' eras, ' + Object.keys(G.chains).length + ' chains, ' +
  G.phases.length + ' phases, ' + G.plan.length + ' modules (' + fs.statSync(W.DATA_JS).size + ' bytes)');
