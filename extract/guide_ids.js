// prints every item id found anywhere in the evaluated guide data (covers ids built at runtime, e.g. 'gtceu:' + tier + '_machine_casing')
const fs = require('fs'), path = require('path'), vm = require('vm');
const dir = path.join(__dirname, '..', 'guia', 'data');
const files = fs.readdirSync(dir).filter(f => /^guide\d*\.js$/.test(f)).sort((a, b) => (parseInt(a.replace(/\D/g, '')) || 0) - (parseInt(b.replace(/\D/g, '')) || 0));
const ctx = vm.createContext({}); ctx.window = ctx; ctx.document = {};
for (const f of files) { try { vm.runInContext(fs.readFileSync(path.join(dir, f), 'utf8'), ctx, { filename: f }); } catch (e) { console.error('ERR', f, e.message); } }
const ids = new Set(), re = /^[a-z0-9_]+:[a-z0-9_./]+$/, seen = new Set();
(function walk(o) { if (typeof o === 'string') { if (re.test(o)) ids.add(o); return; } if (!o || typeof o !== 'object' || seen.has(o)) return; seen.add(o); for (const k of Object.keys(o)) { if (re.test(k)) ids.add(k); walk(o[k]); } })(ctx.GUIDE);
console.log(JSON.stringify([...ids]));
