#!/usr/bin/env node
'use strict';
/*
 * Rebuilds the human-readable Markdown body of every wiki page from its front matter
 * (chains, eras, plan phases and the overview pages). The front matter is never touched.
 *
 *   node tools/refresh_body.js
 */
const W = require('./lib/wiki');
const n = W.renderAll(W.DOCS);
console.log('refreshed ' + n + ' page bodies');
