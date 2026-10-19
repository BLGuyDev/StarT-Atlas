'use strict';
/*
 * Minimal YAML emitter + parser for the wiki front matter (no npm packages).
 *
 * The emitter writes a strict, PyYAML/MkDocs-compatible subset:
 *   - block mappings and block sequences (2-space indent, compact "- key: v" items)
 *   - flow sequences "[a, b, [1, 2]]" for short arrays of scalars / nested scalar arrays
 *   - plain scalars only when they cannot be mistaken for anything else,
 *     otherwise JSON-style double-quoted strings, or "|-" literal blocks for long prose
 *   - numbers, true/false, null, [] and {}
 *
 * The parser reads everything the emitter writes plus the usual hand edits:
 * comments, blank lines, single-quoted strings, "|", "|-", ">", ">-" block scalars,
 * flow sequences/mappings that wrap over several lines, sequences indented at the
 * same column as their parent key. It does NOT implement anchors, aliases, tags,
 * multi-document streams or YAML 1.1 yes/no booleans (write true/false).
 */

const SPECIAL_WORDS = /^(y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF|null|Null|NULL|~)$/;
const BAD_CHARS = /[\u0000-\u001f\u007f-\u009f\u2028\u2029\ufeff]/;
const NUM_RE = /^-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?$/;

function quote(s) {
  // JSON escaping is a subset of YAML double-quoted escaping, except for a few
  // code points YAML treats as line breaks / BOM: escape those explicitly.
  return JSON.stringify(s).replace(/[\u007f-\u009f\u2028\u2029\ufeff]/g,
    c => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0'));
}

function plainOkBlock(s) {
  if (!/^[A-Za-z_]/.test(s)) return false;
  if (BAD_CHARS.test(s)) return false;
  if (/\s$/.test(s) || /:$/.test(s)) return false;
  if (s.indexOf(': ') >= 0 || s.indexOf(' #') >= 0) return false;
  if (SPECIAL_WORDS.test(s)) return false;
  return true;
}
function plainOkFlow(s) {
  return /^[A-Za-z_][A-Za-z0-9_ .\-]*$/.test(s) && !/\s$/.test(s) && !SPECIAL_WORDS.test(s);
}
function keyOut(k) {
  return (/^[A-Za-z_][A-Za-z0-9_\-]*$/.test(k) && !SPECIAL_WORDS.test(k)) ? k : quote(k);
}
function numOut(n) {
  if (!isFinite(n)) throw new Error('yaml: non-finite number ' + n);
  if (Object.is(n, -0)) throw new Error('yaml: -0 is not representable');
  const s = String(n);
  if (!NUM_RE.test(s)) throw new Error('yaml: number format ' + s);
  return s;
}
function isScalar(v) { return v === null || typeof v === 'string' || typeof v === 'number' || typeof v === 'boolean'; }
function scalarFlow(v) {
  if (v === null) return 'null';
  if (typeof v === 'boolean') return v ? 'true' : 'false';
  if (typeof v === 'number') return numOut(v);
  return plainOkFlow(v) ? v : quote(v);
}
function flowable(v) {
  if (!Array.isArray(v)) return false;
  return v.every(x => isScalar(x) || (Array.isArray(x) && flowable(x)));
}
function flowOut(v) {
  return '[' + v.map(x => Array.isArray(x) ? flowOut(x) : scalarFlow(x)).join(', ') + ']';
}
function checkPlain(v, path) {
  if (v === undefined) throw new Error('yaml: undefined at ' + path);
  if (typeof v === 'function') throw new Error('yaml: function at ' + path);
  if (typeof v === 'object' && v !== null && !Array.isArray(v)) {
    const p = Object.getPrototypeOf(v);
    if (p !== null && Object.getPrototypeOf(p) !== null) throw new Error('yaml: non-plain object at ' + path);
  }
}

const FLOW_MAX = 110;

// Returns array of lines for value v placed after "key:" (or "-") at indent `ind`.
// Result: { inline: string } for same-line values, or { lines: [...] } for nested blocks.
function valueOut(v, ind, path) {
  checkPlain(v, path);
  const pad = ' '.repeat(ind + 2);
  if (v === null || typeof v === 'boolean' || typeof v === 'number') return { inline: scalarFlow(v) };
  if (typeof v === 'string') {
    if (plainOkBlock(v)) return { inline: v };
    if (v.length > 60 && !BAD_CHARS.test(v) && !/^\s|\s$/.test(v)) return { inline: '|-', lines: [pad + v] };
    return { inline: quote(v) };
  }
  if (Array.isArray(v)) {
    if (v.length === 0) return { inline: '[]' };
    if (flowable(v)) {
      const f = flowOut(v);
      if (f.length <= FLOW_MAX) return { inline: f };
    }
    return { inline: '', lines: seqOut(v, ind + 2, path) };
  }
  const keys = Object.keys(v);
  if (keys.length === 0) return { inline: '{}' };
  return { inline: '', lines: mapOut(v, ind + 2, path) };
}

function mapOut(obj, ind, path) {
  const out = [], pad = ' '.repeat(ind);
  for (const k of Object.keys(obj)) {
    const r = valueOut(obj[k], ind, path + '.' + k);
    out.push(pad + keyOut(k) + ':' + (r.inline ? ' ' + r.inline : ''));
    if (r.lines) for (const l of r.lines) out.push(l);
  }
  return out;
}

function seqOut(arr, ind, path) {
  const out = [], pad = ' '.repeat(ind);
  arr.forEach((v, i) => {
    const p = path + '[' + i + ']';
    checkPlain(v, p);
    const isObj = v !== null && typeof v === 'object';
    const nonEmptyObj = isObj && !Array.isArray(v) && Object.keys(v).length > 0;
    const blockArr = Array.isArray(v) && v.length > 0 && !(flowable(v) && flowOut(v).length <= FLOW_MAX);
    if (nonEmptyObj || blockArr) {
      const inner = nonEmptyObj ? mapOut(v, ind + 2, p) : seqOut(v, ind + 2, p);
      inner[0] = pad + '- ' + inner[0].slice(ind + 2);
      for (const l of inner) out.push(l);
    } else {
      const r = valueOut(v, ind, p);
      out.push(pad + '-' + (r.inline ? ' ' + r.inline : ''));
      if (r.lines) for (const l of r.lines) out.push(l);
    }
  });
  return out;
}

function stringify(obj) {
  if (obj === null || typeof obj !== 'object' || Array.isArray(obj)) throw new Error('yaml.stringify: top level must be a mapping');
  return mapOut(obj, 0, '$').join('\n') + '\n';
}

/* ------------------------------------------------------------------ parser */

function decodeDouble(body, where) {
  let out = '';
  for (let i = 0; i < body.length; i++) {
    const c = body[i];
    if (c !== '\\') { out += c; continue; }
    const e = body[++i];
    const map = { '0': '\0', a: '\x07', b: '\b', t: '\t', '\t': '\t', n: '\n', v: '\x0b', f: '\f', r: '\r', e: '\x1b', ' ': ' ', '"': '"', '/': '/', '\\': '\\', N: '\u0085', _: '\u00a0', L: '\u2028', P: '\u2029' };
    if (e in map) { out += map[e]; continue; }
    const len = e === 'x' ? 2 : e === 'u' ? 4 : e === 'U' ? 8 : 0;
    if (!len) throw new Error('yaml: bad escape \\' + e + ' ' + where);
    const hex = body.substr(i + 1, len);
    if (!/^[0-9a-fA-F]+$/.test(hex) || hex.length !== len) throw new Error('yaml: bad hex escape ' + where);
    out += String.fromCodePoint(parseInt(hex, 16));
    i += len;
  }
  return out;
}

function plainValue(s) {
  if (s === '' || s === '~' || s === 'null' || s === 'Null' || s === 'NULL') return null;
  if (s === 'true' || s === 'True' || s === 'TRUE') return true;
  if (s === 'false' || s === 'False' || s === 'FALSE') return false;
  if (NUM_RE.test(s)) return Number(s);
  return s;
}

// Parses an inline (single-line, possibly joined) scalar or flow collection.
function parseInline(text, where) {
  let i = 0;
  const ws = () => { while (i < text.length && /\s/.test(text[i])) i++; };
  function node(inFlow) {
    ws();
    const c = text[i];
    if (c === '"') {
      let j = i + 1;
      while (j < text.length && text[j] !== '"') { if (text[j] === '\\') j++; j++; }
      if (j >= text.length) throw new Error('yaml: unterminated string ' + where);
      const v = decodeDouble(text.slice(i + 1, j), where); i = j + 1; return v;
    }
    if (c === "'") {
      let j = i + 1, v = '';
      for (;;) {
        if (j >= text.length) throw new Error('yaml: unterminated string ' + where);
        if (text[j] === "'") { if (text[j + 1] === "'") { v += "'"; j += 2; continue; } break; }
        v += text[j++];
      }
      i = j + 1; return v;
    }
    if (c === '[') {
      i++; const arr = []; ws();
      if (text[i] === ']') { i++; return arr; }
      for (;;) {
        arr.push(node(true)); ws();
        if (text[i] === ',') { i++; ws(); if (text[i] === ']') { i++; return arr; } continue; }
        if (text[i] === ']') { i++; return arr; }
        throw new Error('yaml: bad flow sequence ' + where);
      }
    }
    if (c === '{') {
      i++; const obj = {}; ws();
      if (text[i] === '}') { i++; return obj; }
      for (;;) {
        ws();
        let k;
        if (text[i] === '"' || text[i] === "'") k = String(node(true));
        else { let j = i; while (j < text.length && text[j] !== ':') j++; k = text.slice(i, j).trim(); i = j; }
        ws(); if (text[i] !== ':') throw new Error('yaml: bad flow mapping ' + where);
        i++; obj[k] = node(true); ws();
        if (text[i] === ',') { i++; ws(); if (text[i] === '}') { i++; return obj; } continue; }
        if (text[i] === '}') { i++; return obj; }
        throw new Error('yaml: bad flow mapping ' + where);
      }
    }
    // plain scalar
    let j = i;
    if (inFlow) { while (j < text.length && !/[,\]\}]/.test(text[j])) j++; }
    else j = text.length;
    let s = text.slice(i, j);
    const hash = s.search(/\s#/); if (hash >= 0) s = s.slice(0, hash);
    i = j;
    return plainValue(s.trim());
  }
  const v = node(false); ws();
  if (i < text.length && text[i] !== '#') throw new Error('yaml: trailing text "' + text.slice(i) + '" ' + where);
  return v;
}

function flowBalanced(s) {
  let depth = 0, q = null;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (q) { if (c === '\\' && q === '"') i++; else if (c === q) { if (q === "'" && s[i + 1] === "'") i++; else q = null; } continue; }
    if (c === '"' || c === "'") q = c;
    else if (c === '[' || c === '{') depth++;
    else if (c === ']' || c === '}') depth--;
    else if (c === '#' && (i === 0 || /\s/.test(s[i - 1])) && depth === 0) break;
  }
  return depth <= 0;
}

function parse(src, fileLabel) {
  const raw = src.replace(/\r\n?/g, '\n').split('\n');
  // lines: {ind, text, no} ; comment / blank lines kept as null for block scalars
  const L = raw.map((t, no) => ({ raw: t, no: no + 1, ind: t.length - t.replace(/^ +/, '').length, text: t.replace(/^ +/, '') }));
  let p = 0;
  const where = () => '(' + (fileLabel || 'yaml') + ' line ' + (L[Math.min(p, L.length - 1)] || { no: '?' }).no + ')';
  const isSkip = l => l.text === '' || l.text[0] === '#';
  function skip() { while (p < L.length && isSkip(L[p])) p++; }
  function isSeqItem(t) { return t === '-' || t.startsWith('- '); }

  function blockScalar(head, parentInd) {
    const style = head[0], chomp = head.slice(1).replace(/[0-9]/g, '').trim();
    const lines = [];
    let blockInd = -1;
    while (p < L.length) {
      const l = L[p];
      if (l.text === '') { lines.push(''); p++; continue; }
      if (l.ind <= parentInd) break;
      if (blockInd < 0) blockInd = l.ind;
      if (l.ind < blockInd) break;
      lines.push(l.raw.slice(blockInd)); p++;
    }
    while (lines.length && lines[lines.length - 1] === '') { lines.pop(); }
    let s;
    if (style === '|') s = lines.join('\n');
    else {
      s = ''; lines.forEach((ln, idx) => {
        if (idx === 0) { s = ln; return; }
        if (ln === '') s += '\n'; else s += (s.endsWith('\n') || s === '' ? '' : ' ') + ln;
      });
    }
    if (chomp !== '-' && lines.length) s += '\n';
    return s;
  }

  function inlineValue(rest, parentInd) {
    if (/^[|>][-+0-9]*(\s+#.*)?$/.test(rest)) return blockScalar(rest.replace(/\s+#.*$/, ''), parentInd);
    if (rest[0] === '[' || rest[0] === '{') {
      let txt = rest;
      while (!flowBalanced(txt) && p < L.length) { txt += ' ' + L[p].text; p++; }
      return parseInline(txt, where());
    }
    return parseInline(rest, where());
  }

  function parseNode(ind) {
    skip();
    if (p >= L.length || L[p].ind < ind) return null;
    const l = L[p];
    if (isSeqItem(l.text)) return parseSeq(l.ind);
    if (/^("([^"\\]|\\.)*"|'([^']|'')*'|[^\s#'"\-\[\{][^:]*?|-[^\s][^:]*?)\s*:(\s|$)/.test(l.text)) return parseMap(l.ind);
    // bare scalar on its own line
    p++;
    return inlineValue(l.text, l.ind - 1);
  }

  function splitKey(text) {
    let k, rest;
    if (text[0] === '"' || text[0] === "'") {
      let j = 1;
      if (text[0] === '"') { while (j < text.length && text[j] !== '"') { if (text[j] === '\\') j++; j++; } }
      else { for (;;) { if (text[j] === "'" && text[j + 1] === "'") { j += 2; continue; } if (text[j] === "'" || j >= text.length) break; j++; } }
      k = String(parseInline(text.slice(0, j + 1), where()));
      rest = text.slice(j + 1).replace(/^\s*:/, '');
    } else {
      const m = /^(.*?)\s*:(\s|$)/.exec(text);
      if (!m) throw new Error('yaml: expected "key:" ' + where());
      k = m[1]; rest = text.slice(m[0].length - (m[2] ? 1 : 0)).replace(/^:/, '');
    }
    return { k, rest: rest.trim() };
  }

  function parseMap(ind) {
    const obj = {};
    for (;;) {
      skip();
      if (p >= L.length) break;
      const l = L[p];
      if (l.ind < ind) break;
      if (l.ind > ind) throw new Error('yaml: bad indentation ' + where());
      if (isSeqItem(l.text)) break;
      const { k, rest } = splitKey(l.text);
      if (Object.prototype.hasOwnProperty.call(obj, k)) throw new Error('yaml: duplicate key "' + k + '" ' + where());
      p++;
      if (rest === '' || rest[0] === '#') {
        skip();
        if (p < L.length && (L[p].ind > ind || (L[p].ind === ind && isSeqItem(L[p].text)))) obj[k] = parseNode(L[p].ind);
        else obj[k] = null;
      } else obj[k] = inlineValue(rest, ind);
    }
    return obj;
  }

  function parseSeq(ind) {
    const arr = [];
    for (;;) {
      skip();
      if (p >= L.length) break;
      const l = L[p];
      if (l.ind < ind || !isSeqItem(l.text)) {
        if (l.ind > ind) throw new Error('yaml: bad indentation ' + where());
        break;
      }
      if (l.ind > ind) throw new Error('yaml: bad indentation ' + where());
      const after = l.text === '-' ? '' : l.text.slice(2);
      const afterTrim = after.replace(/^ +/, '');
      if (afterTrim === '' || afterTrim[0] === '#') {
        p++; skip();
        arr.push(p < L.length && L[p].ind > ind ? parseNode(L[p].ind) : null);
        continue;
      }
      const col = ind + 2 + (after.length - afterTrim.length);
      if (isSeqItem(afterTrim) || /^("([^"\\]|\\.)*"|'([^']|'')*'|[^\s#'"\[\{][^:]*?)\s*:(\s|$)/.test(afterTrim) && !/^[|>]/.test(afterTrim)) {
        // compact nested node: rewrite this line as if it started at column `col`
        L[p] = { raw: ' '.repeat(col) + afterTrim, no: l.no, ind: col, text: afterTrim };
        arr.push(parseNode(col));
      } else {
        p++;
        arr.push(inlineValue(afterTrim, ind));
      }
    }
    return arr;
  }

  skip();
  if (p >= L.length) return {};
  const v = parseNode(L[p].ind);
  skip();
  if (p < L.length) throw new Error('yaml: unexpected content ' + where());
  return v;
}

module.exports = { stringify, parse };
