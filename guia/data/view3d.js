/* 3D assembly-line viewer. Turns any setup (chain nodes + edges) into a small Minecraft-like scene:
   machines with their real pack textures, multiblocks with their real structure, drawers showing the item they hold,
   tanks for fluids, pipes for every connection (grey items, blue fluids, amber power), floating labels.
   three.js r128 + OrbitControls load on first use; only one 3D view is alive at a time. */
(function () {
  const B = window.BLOCKS3D || { f: {}, s: {}, cols: 32, rows: 1 };
  let THREEP = null, live = null;

  function loadScript(src) {
    return new Promise((ok, bad) => { const s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = bad; document.head.appendChild(s); });
  }
  function three() {
    if (!THREEP) THREEP = loadScript('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js')
      .then(() => loadScript('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js'));
    return THREEP;
  }

  /* ---------- layout: columns by flow rank, like the 2D diagram ---------- */
  function ranks(N, E) {
    const by = Object.fromEntries(N.map(n => [n.id, n]));
    N.forEach(n => n.r = 0);
    for (let k = 0; k < N.length; k++) E.forEach(e => { if (by[e.b].r < by[e.a].r + 1) by[e.b].r = Math.min(by[e.a].r + 1, N.length); });
    for (let k = 0; k < N.length; k++) N.forEach(n => { const t = E.filter(e => e.a === n.id).map(e => by[e.b].r); if (t.length) { const r = Math.min(...t) - 1; if (r > n.r) n.r = r; } });
    const used = [...new Set(N.map(n => n.r))].sort((a, b) => a - b);
    N.forEach(n => n.r = used.indexOf(n.r));
    return by;
  }
  const countOf = l => { const m = /^(\d+)\s/.exec(l) || /\u00d7\s*(\d+)/.exec(l); return m ? Math.min(9, Math.max(1, +m[1])) : 1; };

  /* what each node becomes in the world */
  function unitOf(n) {
    const id = n.ic;
    if ((n.t === 'm' || n.t === 'p' || n.t === 's') && B.s[id]) { const d = B.s[id].d; return { kind: 'struct', id, w: d[0], h: d[1], l: d[2] }; }
    if ((n.t === 'm' || n.t === 'p' || n.t === 's') && B.f[id]) { const c = countOf(n.l); return { kind: 'block', id, n: c, w: 1, h: 1, l: c * 1.5 - 0.5 }; }
    if (n.t === 'g') return { kind: 'drawers', items: n.items, w: 1, h: 1, l: n.items.length * 1.25 - 0.25 };
    if (n.t === 'f') return { kind: 'tank', id, w: 1, h: 1, l: 1 };
    return { kind: 'drawer', id, w: 1, h: 1, l: 1 };
  }

  function build(c, el) {
    const T = window.THREE;
    let N = c.n.map(([id, l, t, ic, it]) => ({ id, l, t, ic, items: t === 'g' ? (it || []).map(([a, b, q]) => ({ l: a, ic: b, q })) : null }));
    const E = c.e.filter(e => N.some(n => n.id === e[0]) && N.some(n => n.id === e[1])).map(([a, b, l]) => ({ a, b, l: l == null ? '' : String(l) }));
    const by = ranks(N, E);
    N.forEach(n => n.u = unitOf(n));
    const cols = [];
    N.forEach(n => (cols[n.r] = cols[n.r] || []).push(n));
    /* order inside a column by the average z of what feeds it */
    let x = 0;
    cols.forEach((col, ci) => {
      if (ci) col.forEach(n => { const ps = E.filter(e => e.b === n.id).map(e => by[e.a].zc); n.k = ps.length ? ps.reduce((a, b) => a + b) / ps.length : 0; });
      if (ci) col.sort((a, b) => a.k - b.k);
      const W = Math.max(...col.map(n => n.u.w)), L = col.reduce((s, n) => s + n.u.l, 0) + 1.5 * (col.length - 1);
      let z = -L / 2;
      col.forEach(n => { n.x = x + (W - n.u.w) / 2; n.z = z; n.zc = z + n.u.l / 2; z += n.u.l + 1.5; });
      x += W + 3.5;
    });

    const scene = new T.Scene();
    const bg = getComputedStyle(document.body).getPropertyValue('--bg').trim() || '#121619';
    scene.background = new T.Color(bg);
    scene.add(new T.AmbientLight(0xffffff, 0.78));
    const sun = new T.DirectionalLight(0xffffff, 0.55); sun.position.set(-4, 10, 7); scene.add(sun);

    const loader = new T.TextureLoader();
    const tex = src => { const t = loader.load(src, () => draw()); t.magFilter = T.NearestFilter; t.minFilter = T.NearestFilter; t.encoding = T.sRGBEncoding; return t; };
    const blockTex = tex('img/blocks.png'), iconTex = tex('img/atlas.png');
    const blockMat = new T.MeshLambertMaterial({ map: blockTex, transparent: true, alphaTest: 0.1 });
    const iconMat = new T.MeshBasicMaterial({ map: iconTex, transparent: true, alphaTest: 0.1 });
    const geoCache = {};
    function cellUV(i) { const cx = i % B.cols, cy = Math.floor(i / B.cols); return [cx / B.cols, 1 - (cy + 1) / B.rows, (cx + 1) / B.cols, 1 - cy / B.rows]; }
    function boxGeo(id) {
      if (geoCache[id]) return geoCache[id];
      const g = new T.BoxGeometry(1, 1, 1), f = B.f[id], uv = g.attributes.uv;
      /* BoxGeometry faces: +x, -x, +y, -y, +z, -z ; +z faces the camera = front */
      const pick = [f[1], f[1], f[0], f[0], f[2], f[1]];
      for (let face = 0; face < 6; face++) {
        const [u0, v0, u1, v1] = cellUV(pick[face]);
        for (let k = 0; k < 4; k++) { const i = face * 4 + k; uv.setXY(i, u0 + uv.getX(i) * (u1 - u0), v0 + uv.getY(i) * (v1 - v0)); }
      }
      uv.needsUpdate = true;
      return (geoCache[id] = g);
    }
    const pickable = [], labels = [];
    function block(id, px, py, pz, label) {
      if (!B.f[id]) return null;
      const m = new T.Mesh(boxGeo(id), blockMat); m.position.set(px + 0.5, py + 0.5, pz + 0.5); m.userData.label = label || nm(id); scene.add(m); pickable.push(m); return m;
    }
    function iconPlane(id, px, py, pz, s) {
      const k = IC.i[circuitAlias(id)];
      if (k == null) return;
      const rows = (IC.rows || (IC.rows = Math.ceil((Math.max(...Object.values(IC.i)) + 1) / IC.cols))), cx = k % IC.cols, cy = Math.floor(k / IC.cols);
      const g = new T.PlaneGeometry(s, s), uv = g.attributes.uv;
      const u0 = cx / IC.cols, u1 = (cx + 1) / IC.cols, v0 = 1 - (cy + 1) / rows, v1 = 1 - cy / rows;
      for (let i = 0; i < 4; i++) uv.setXY(i, u0 + uv.getX(i) * (u1 - u0), v0 + uv.getY(i) * (v1 - v0));
      const m = new T.Mesh(g, iconMat); m.position.set(px, py, pz); scene.add(m);
    }
    function label(text, px, py, pz, small) {
      const cv = document.createElement('canvas'), ctx = cv.getContext('2d'), fs = small ? 26 : 30;
      const lines = wrap(text, small ? 22 : 18);
      ctx.font = `600 ${fs}px IBM Plex Sans, sans-serif`;
      const w = Math.max(...lines.map(l => ctx.measureText(l).width)) + 24, h = lines.length * (fs + 6) + 14;
      cv.width = w; cv.height = h;
      ctx.font = `600 ${fs}px IBM Plex Sans, sans-serif`;
      ctx.fillStyle = small ? 'rgba(20,24,28,.78)' : 'rgba(20,24,28,.9)'; ctx.strokeStyle = small ? 'rgba(255,255,255,.25)' : '#f08a3c'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.rect(1.5, 1.5, w - 3, h - 3); ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      lines.forEach((l, i) => ctx.fillText(l, w / 2, 8 + i * (fs + 6)));
      const t = new T.CanvasTexture(cv); t.encoding = T.sRGBEncoding;
      const sp = new T.Sprite(new T.SpriteMaterial({ map: t, depthTest: false, sizeAttenuation: false }));
      const sc = small ? 0.00042 : 0.0005; sp.scale.set(w * sc, h * sc, 1); sp.position.set(px, py, pz); sp.renderOrder = 10; scene.add(sp); labels.push(sp);
      return sp;
    }

    /* hand-built scene: real block positions instead of the auto layout */
    if (c.s3d) {
      N = []; E.length = 0;
      c.s3d.b.forEach(([id, bx, by2, bz, dx, dy, dz, lb]) => { for (let i = 0; i < (dx || 1); i++) for (let j = 0; j < (dy || 1); j++) for (let k = 0; k < (dz || 1); k++) block(id, bx + i, by2 + j, bz + k, lb); });
      (c.s3d.l || []).forEach(([tx, lx, ly, lz]) => label(tx, lx, ly, lz));
    }
    /* place every unit */
    N.forEach(n => {
      const u = n.u;
      if (u.kind === 'struct') {
        const s = B.s[u.id];
        s.b.forEach(([bx, by2, bz, ch]) => block(s.k[ch], n.x + bx, by2, n.z + bz, nm(u.id)));
      } else if (u.kind === 'block') {
        for (let i = 0; i < u.n; i++) block(u.id, n.x, 0, n.z + i * 1.5, n.l);
      } else if (u.kind === 'drawers') {
        u.items.forEach((it, i) => { block('functionalstorage:oak_1', n.x, 0, n.z + i * 1.25, it.l); iconPlane(it.ic, n.x + 0.5, 0.5, n.z + i * 1.25 + 1.01, 0.62); });
      } else if (u.kind === 'tank') {
        block('create:fluid_tank', n.x, 0, n.z, n.l); iconPlane(u.id, n.x + 0.5, 0.5, n.z + 1.01, 0.6);
      } else {
        block('functionalstorage:oak_1', n.x, 0, n.z, n.l); iconPlane(u.id, n.x + 0.5, 0.5, n.z + 1.01, 0.62);
      }
      n.top = u.kind === 'struct' ? u.h : 1;
      label(n.l, n.x + n.u.w / 2, n.top + 0.75, n.zc);
    });

    /* pipes: out of the source's east side, along the gap, into the target's west side */
    const pipeMat = { i: new T.MeshLambertMaterial({ color: 0xb9c0c6 }), f: new T.MeshLambertMaterial({ color: 0x3f93d8 }), p: new T.MeshLambertMaterial({ color: 0xe0a326 }) };
    function seg(a, b, mat) {
      const d = new T.Vector3().subVectors(b, a), len = d.length();
      if (len < 0.01) return;
      const g = new T.BoxGeometry(Math.abs(d.x) + 0.14, Math.abs(d.y) + 0.14, Math.abs(d.z) + 0.14);
      const m = new T.Mesh(g, mat); m.position.set((a.x + b.x) / 2, (a.y + b.y) / 2, (a.z + b.z) / 2); scene.add(m);
    }
    pipeMat.r = new T.MeshLambertMaterial({ color: 0x8a6a45 });
    if (c.s3d) (c.s3d.p || []).forEach(([kind, ...pts]) => { for (let i = 0; i + 1 < pts.length; i++) seg(new T.Vector3(...pts[i]), new T.Vector3(...pts[i + 1]), pipeMat[kind] || pipeMat.i); });
    E.forEach((e, k) => {
      const A = by[e.a], Bn = by[e.b];
      const kind = A.t === 'f' || Bn.t === 'f' ? 'f' : A.t === 'p' || Bn.t === 'p' ? 'p' : 'i';
      const y = 0.22 + (k % 3) * 0.2;
      const x1 = A.x + A.u.w, x2 = Bn.x, xm = x2 - 1.2 - (k % 3) * 0.35;
      const p1 = new T.Vector3(x1, y, A.zc), p2 = new T.Vector3(Math.max(x1 + 0.3, xm), y, A.zc), p3 = new T.Vector3(Math.max(x1 + 0.3, xm), y, Bn.zc), p4 = new T.Vector3(x2, y, Bn.zc);
      seg(p1, p2, pipeMat[kind]); seg(p2, p3, pipeMat[kind]); seg(p3, p4, pipeMat[kind]);
      if (e.l) label(e.l, p3.x, y + 0.55, (p3.z + p4.z) / 2 + 0.01, true);
    });

    /* floor */
    let minX = -1.5, maxX = x - 2, zs = N.flatMap(n => [n.z, n.z + n.u.l]), minZ = Math.min(...zs) - 1.5, maxZ = Math.max(...zs) + 1.5;
    if (c.s3d) {
      const bb = new T.Box3(); pickable.forEach(m => bb.expandByObject(m));
      minX = bb.min.x - 1.5; maxX = bb.max.x + 1.5; minZ = bb.min.z - 1.5; maxZ = bb.max.z + 1.5;
      N = [{ top: bb.max.y }];
    }
    const floor = new T.Mesh(new T.PlaneGeometry(maxX - minX, maxZ - minZ), new T.MeshLambertMaterial({ color: new T.Color(getComputedStyle(document.body).getPropertyValue('--sunk').trim() || '#0e1215') }));
    floor.rotation.x = -Math.PI / 2; floor.position.set((minX + maxX) / 2, -0.001, (minZ + maxZ) / 2); scene.add(floor);
    const gp = [];
    for (let gx = Math.ceil(minX); gx <= maxX; gx++) gp.push(gx, 0.002, minZ, gx, 0.002, maxZ);
    for (let gz = Math.ceil(minZ); gz <= maxZ; gz++) gp.push(minX, 0.002, gz, maxX, 0.002, gz);
    const gg = new T.BufferGeometry(); gg.setAttribute('position', new T.Float32BufferAttribute(gp, 3));
    scene.add(new T.LineSegments(gg, new T.LineBasicMaterial({ color: 0x3a444c, transparent: true, opacity: 0.55 })));

    /* camera framing the whole line */
    const W = el.clientWidth || 800, H = el.clientHeight || 440;
    const cam = new T.PerspectiveCamera(42, W / H, 0.1, 500);
    const cx = (minX + maxX) / 2, cz = (minZ + maxZ) / 2, topY = Math.max(2, ...N.map(n => n.top + 1.5));
    /* fit the whole line: bounding sphere of the floor + tallest block, seen from front-above */
    const rad = 0.5 * Math.sqrt((maxX - minX) ** 2 + (maxZ - minZ) ** 2 + topY ** 2);
    const fovV = cam.fov * Math.PI / 180, fovH = 2 * Math.atan(Math.tan(fovV / 2) * W / H);
    const dist = rad / Math.sin(Math.min(fovV, fovH) / 2) * 0.7;
    const dir = new T.Vector3(-0.1, 0.62, 0.78).normalize();
    cam.position.set(cx + dir.x * dist, topY * 0.3 + dir.y * dist, cz + dir.z * dist);
    const renderer = new T.WebGLRenderer({ antialias: true });
    renderer.outputEncoding = T.sRGBEncoding; renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1)); renderer.setSize(W, H);
    el.appendChild(renderer.domElement);
    const ctl = new T.OrbitControls(cam, renderer.domElement);
    ctl.target.set(cx, topY * 0.3, cz); ctl.enableDamping = true; ctl.maxPolarAngle = Math.PI * 0.49; ctl.update();
    const home = { p: cam.position.clone(), t: ctl.target.clone() };

    const tip = document.createElement('div'); tip.className = 'v3tip'; el.appendChild(tip);
    const ray = new T.Raycaster(), mouse = new T.Vector2();
    renderer.domElement.addEventListener('pointermove', ev => {
      const r = renderer.domElement.getBoundingClientRect();
      mouse.set(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
      ray.setFromCamera(mouse, cam);
      const hit = ray.intersectObjects(pickable)[0];
      if (hit) { tip.textContent = hit.object.userData.label; tip.style.left = (ev.clientX - r.left + 12) + 'px'; tip.style.top = (ev.clientY - r.top + 12) + 'px'; tip.style.display = 'block'; }
      else tip.style.display = 'none';
      draw();
    });
    let raf = 0;
    function draw() { if (raf) return; raf = requestAnimationFrame(() => { raf = 0; if (ctl.update()) draw(); renderer.render(scene, cam); }); }
    ctl.addEventListener('change', draw);
    const ro = new ResizeObserver(() => { const w = el.clientWidth, h = el.clientHeight; if (!w || !h) return; renderer.setSize(w, h); cam.aspect = w / h; cam.updateProjectionMatrix(); draw(); });
    ro.observe(el);
    draw();
    return {
      reset() { cam.position.copy(home.p); ctl.target.copy(home.t); ctl.update(); draw(); },
      labels() { const v = !(labels[0] && labels[0].visible); labels.forEach(l => l.visible = v); draw(); },
      dispose() { ro.disconnect(); ctl.dispose(); renderer.dispose(); scene.traverse(o => { if (o.geometry) o.geometry.dispose(); if (o.material && o.material.map && o.material.map.isCanvasTexture) o.material.map.dispose(); }); el.innerHTML = ''; }
    };
  }

  function close() { if (!live) return; live.view.dispose(); live.fig.classList.remove('is3d'); live.btn.innerHTML = '&#9654; 3D assembly line'; live = null; }
  document.addEventListener('click', e => {
    const r = e.target.closest('[data-v3reset]');
    if (r && live) { live.view.reset(); return; }
    const lb = e.target.closest('[data-v3labels]');
    if (lb && live) { live.view.labels(); return; }
    const b = e.target.closest('[data-v3d]');
    if (!b) return;
    const fig = b.closest('figure'), id = b.dataset.v3d, c = G.chains[id];
    if (!fig || !c) return;
    if (live && live.fig === fig) { close(); return; }
    close();
    const box = fig.querySelector('.v3d');
    fig.classList.add('is3d'); b.textContent = 'Loading 3D\u2026';
    three().then(() => {
      live = { fig, btn: b, view: build(c, box.querySelector('.v3c')) };
      b.innerHTML = '&#9632; Back to the diagram';
    }).catch(() => { b.textContent = '3D could not load (offline?)'; fig.classList.remove('is3d'); });
  });

  /* every setup figure gets the 3D button and an empty stage */
  const baseChain = window.chainHTML;
  window.chainHTML = function (id) {
    const h = baseChain(id);
    if (!G.chains[id]) return h;
    return h.replace('<div class="svgw">', `<div class="v3bar"><button type="button" class="b3d" data-v3d="${esc(id)}">&#9654; 3D assembly line</button><span class="mono v3hint">drag to rotate &#183; wheel to zoom &#183; right-drag to pan</span><button type="button" class="b3r" data-v3reset>Reset view</button><button type="button" class="b3r" data-v3labels>Labels on/off</button></div><div class="v3d"><div class="v3c"></div></div><div class="svgw">`);
  };
  addEventListener('hashchange', close);
  render();
})();
