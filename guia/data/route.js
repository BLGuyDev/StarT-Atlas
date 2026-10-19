/* Plan view: phases -> modules, one fixed template per module:
   what it makes, what it uses (and which module makes that), what to keep in stock, what to watch out for,
   a 3D view of the whole line, and the diagram / steps / materials on demand.
   v4.4: collapsible phases, sticky phase navigator (IntersectionObserver), per-module "done" (saved as 'plan:<id>' in the quest set),
   deep links #plan-<module> and #phase-<phase>. */
(function () {
  const P = G.plan || [], PH = G.phases || [];
  const maker = {};
  P.forEach(m => (m.makes || []).forEach(i => { if (!maker[i]) maker[i] = m; }));
  const isDone = id => typeof done !== 'undefined' && done.has('plan:' + id);
  const cnt = ph => { const ms = P.filter(m => m.ph === ph); return [ms.filter(m => isDone(m.id)).length, ms.length]; };
  const $ = id => document.getElementById(id);
  const small = () => matchMedia('(max-width:620px)').matches;
  let openSet = null, io = null;
  function target() {
    const h = (location.hash || '').slice(1);
    if (h.indexOf('plan-') === 0) { const m = P.find(x => 'plan-' + x.id === h); return m ? { k: 'm', id: m.id, ph: m.ph } : null; }
    if (h.indexOf('phase-') === 0) { const p = PH.find(x => 'phase-' + x.id === h); return p ? { k: 'p', id: p.id, ph: p.id } : null; }
    return null;
  }
  const chip = (id, txt) => `<span class="pchip" title="${esc(nm(id))}">${icon(id, 24)}<span>${esc(txt || nm(id))}</span></span>`;
  const useChip = id => { const m = maker[id]; return m ? `<a class="pchip plink" href="#plan-${esc(m.id)}" data-pgo="${esc(m.id)}" title="made by module ${m.n}">${icon(id, 24)}<span>${esc(nm(id))}</span><b>${m.n}</b></a>` : chip(id); };

  function card(m) {
    const all = [m.chain].concat(m.more || []);
    return `<li class="pmod${isDone(m.id) ? ' isdone' : ''}" id="plan-${esc(m.id)}" style="--tc:${tc(m.era)}">
      <div class="phd"><span class="rnum">${m.n}</span><h4>${esc(m.t)}</h4><span class="chip tierchip" style="--tc:${tc(m.era)}">${ERA_N[m.era] || m.era}</span><label class="pdone"><input type="checkbox" data-pd="${esc(m.id)}"${isDone(m.id) ? ' checked' : ''}><span>Done</span></label></div>
      <div class="pgrid">
        <div><div class="pl">Makes</div><div class="prow">${(m.makes || []).map(i => chip(i)).join('')}</div></div>
        ${(m.uses || []).length ? `<div><div class="pl">Uses</div><div class="prow">${m.uses.map(useChip).join('')}</div></div>` : ''}
        ${(m.stock || []).length ? `<div><div class="pl">Keep in stock</div><div class="prow">${m.stock.map(([i, n]) => chip(i, n)).join('')}</div></div>` : ''}
        ${m.power ? `<div><div class="pl">Power</div><div class="pval">${esc(m.power)}</div></div>` : ''}
      </div>
      ${(m.watch || []).length ? `<div class="miss"><b>Watch out</b><ul>${m.watch.map(w => `<li>${esc(w)}</li>`).join('')}</ul></div>` : ''}
      <figure class="fig pfig"><div class="v3bar"><button type="button" class="b3d" data-v3d="${esc(m.chain)}">&#9654; 3D assembly line</button><span class="mono v3hint">drag to rotate &#183; wheel to zoom &#183; right-drag to pan</span><button type="button" class="b3r" data-v3reset>Reset view</button><button type="button" class="b3r" data-v3labels>Labels on/off</button></div><div class="v3d"><div class="v3c"></div></div></figure>
      <details class="rdet" data-chains="${esc(all.join(','))}"><summary>Diagram, step-by-step build &amp; materials${all.length > 1 ? ` (${all.length} lines)` : ''}</summary><div class="rfill"></div></details>
    </li>`;
  }

  window.planView = function () {
    if (!openSet) openSet = new Set(small() ? PH.slice(0, 1).map(p => p.id) : PH.map(p => p.id));
    const t = target(); if (t) openSet.add(t.ph);
    const tot = P.filter(m => isDone(m.id)).length;
    return `<h2>The plan</h2>
      <p class="goal">Phase by phase, each module is one self-running line: drawers as buffers between machines, routers to move things, one machine per product and a fixed stock of every key part, so later builds only pull from drawers.</p>
      <div class="pbar"><span class="mono" id="plantot">${tot}/${P.length} modules done</span><button type="button" class="b3r pbtn" data-phall="1">Expand all</button><button type="button" class="b3r pbtn" data-phall="0">Collapse all</button></div>
      <nav class="phnav" aria-label="Phases">${PH.map((p, i) => { const c = cnt(p.id); return `<a href="#phase-${esc(p.id)}" data-phgo="${esc(p.id)}" style="--tc:${tc(p.era)}" title="${esc(p.t)}"><b>${i + 1}</b><span class="pt">${esc(p.t)}</span><i data-phnc="${esc(p.id)}">${c[0]}/${c[1]}</i></a>`; }).join('')}</nav>
      ${PH.map((p, i) => { const o = openSet.has(p.id), c = cnt(p.id), eraOk = (G.eras || []).some(e => e.id === p.era);
        return `<section class="phase${o ? ' open' : ''}" id="phase-${esc(p.id)}" style="--tc:${tc(p.era)}"><div class="phh"><h3><button type="button" class="phtog" aria-expanded="${o}" aria-controls="phb-${esc(p.id)}" data-phtog="${esc(p.id)}"><span class="phar" aria-hidden="true">&#9656;</span><span class="pht">Phase ${i + 1} &#183; ${esc(p.t)}</span><span class="phc" data-phc="${esc(p.id)}">${c[0]}/${c[1]} done</span></button></h3>${eraOk ? `<a class="chip tierchip phera" style="--tc:${tc(p.era)}" href="#${esc(p.era)}" title="Open the ${esc(ERA_N[p.era] || p.era)} era page">${esc(ERA_N[p.era] || p.era)} &#8594;</a>` : ''}</div>
        <div class="phbody" id="phb-${esc(p.id)}"${o ? '' : ' hidden'}><p class="mono">${esc(p.goal)}</p><ol class="plist">${P.filter(m => m.ph === p.id).map(card).join('')}</ol></div></section>`; }).join('')}`;
  };

  function setOpen(id, on) {
    const s = $('phase-' + id); if (!s) return;
    on ? openSet.add(id) : openSet.delete(id);
    s.classList.toggle('open', on);
    $('phb-' + id).hidden = !on;
    s.querySelector('.phtog').setAttribute('aria-expanded', String(on));
  }
  function offsets() {
    const h = document.querySelector('header'), n = document.querySelector('.phnav'), r = document.documentElement.style;
    const hh = h && getComputedStyle(h).position === 'sticky' ? h.offsetHeight : 0;
    r.setProperty('--hh', hh + 'px'); r.setProperty('--sm', (hh + (n ? n.offsetHeight : 0) + 8) + 'px');
  }
  function setActive(id) {
    document.querySelectorAll('.phnav a').forEach(a => {
      const on = a.dataset.phgo === id; a.classList.toggle('on', on);
      if (on) {
        a.setAttribute('aria-current', 'true');
        const n = a.parentNode, l = a.offsetLeft - (n.clientWidth - a.offsetWidth) / 2;
        if (n.scrollWidth > n.clientWidth && Math.abs(n.scrollLeft - l) > 4) n.scrollTo({ left: l, behavior: 'smooth' });
      } else a.removeAttribute('aria-current');
    });
  }
  function watch() {
    if (io) { io.disconnect(); io = null; }
    const secs = document.querySelectorAll('.phase'); if (!secs.length || !window.IntersectionObserver) return;
    offsets();
    const off = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sm'), 10) || 120, vis = new Set();
    io = new IntersectionObserver(es => {
      es.forEach(e => e.isIntersecting ? vis.add(e.target.id) : vis.delete(e.target.id));
      const f = PH.find(p => vis.has('phase-' + p.id)); if (f) setActive(f.id);
    }, { rootMargin: '-' + off + 'px 0px -60% 0px' });
    secs.forEach(s => io.observe(s));
    setActive(PH[0] && PH[0].id);
  }
  function reveal(k, id, keepHash) {
    const m = k === 'm' ? P.find(x => x.id === id) : null, ph = m ? m.ph : id;
    setOpen(ph, true); offsets();
    const el = $((k === 'm' ? 'plan-' : 'phase-') + id); if (!el) return;
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    el.classList.add('flash'); setTimeout(() => el.classList.remove('flash'), 1400);
    if (!keepHash) try { history.replaceState(null, '', '#' + (k === 'm' ? 'plan-' : 'phase-') + id); } catch (e) {}
  }
  function refreshCounts() {
    PH.forEach(p => {
      const c = cnt(p.id), a = document.querySelector('[data-phc="' + p.id + '"]'), b = document.querySelector('[data-phnc="' + p.id + '"]');
      if (a) a.textContent = c[0] + '/' + c[1] + ' done';
      if (b) b.textContent = c[0] + '/' + c[1];
    });
    const t = $('plantot'); if (t) t.textContent = P.filter(m => isDone(m.id)).length + '/' + P.length + ' modules done';
  }

  document.addEventListener('toggle', e => {
    const d = e.target;
    if (!d.matches || !d.matches('.rdet') || !d.open) return;
    const f = d.querySelector('.rfill');
    if (f.dataset.done) return;
    f.dataset.done = '1';
    f.innerHTML = LEG + d.dataset.chains.split(',').filter(Boolean).map(chainHTML).join('');
    if (window.initCalcs) initCalcs();
  }, true);

  document.addEventListener('click', e => {
    const tg = e.target.closest('[data-phtog]');
    if (tg) { setOpen(tg.dataset.phtog, tg.getAttribute('aria-expanded') !== 'true'); return; }
    const all = e.target.closest('[data-phall]');
    if (all) { PH.forEach(p => setOpen(p.id, all.dataset.phall === '1')); return; }
    const a = e.target.closest('[data-pgo],[data-phgo]');
    if (!a) return;
    e.preventDefault();
    if (a.dataset.pgo) reveal('m', a.dataset.pgo); else reveal('p', a.dataset.phgo);
  });

  document.addEventListener('change', e => {
    const c = e.target, id = c.dataset && c.dataset.pd;
    if (!id) return;
    c.checked ? done.add('plan:' + id) : done.delete('plan:' + id);
    try { persist(); } catch (x) {}
    const li = $('plan-' + id); if (li) li.classList.toggle('isdone', c.checked);
    refreshCounts();
  });
  addEventListener('resize', () => { if ($('plantot')) offsets(); });

  const baseRender = window.render;
  window.render = function () {
    if (!VIEWS.some(x => x[0] === 'plan')) VIEWS.splice(1, 0, ['plan', 'Plan']);
    const q = document.getElementById('q').value.trim(), t = target(), h0 = location.hash;
    const v = t ? 'plan' : (h0 || '#home').slice(1);
    if (t) { try { history.replaceState(null, '', '#plan'); } catch (x) {} }
    baseRender();
    if (t) { try { history.replaceState(null, '', h0); } catch (x) {} }
    if (io) { io.disconnect(); io = null; }
    if ((v === 'plan' || v === 'route') && q.length < 2) {
      document.getElementById('main').innerHTML = planView(); watch();
      if (t) setTimeout(() => reveal(t.k, t.id, true), 120);
    } else if ((v === 'home' || !v) && q.length < 2)
      document.getElementById('main').insertAdjacentHTML('afterbegin', `<a class="start" href="#plan"><b>Start here: the plan</b><span>${PH.length} phases, ${P.length} self-running modules, each with a 3D view of the line.</span><span class="go">&#8594;</span></a>`);
  };
  render();
})();
