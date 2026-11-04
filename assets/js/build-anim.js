/* Home "build" animation: a crew of cursor agents assembles the page layer by layer.
   Runs only when <html> has .pre-build (set in <head> unless ?nobuild, reduced motion, or already seen this session).
   Everything runs on a simulated clock, so speed and pause apply to every effect. */
(() => {
  const root = document.documentElement;
  if (!root.classList.contains('pre-build')) return;

  const NAMES = ['Nova', 'Pixel', 'Echo', 'Orbit', 'Vega', 'Iris', 'Atlas', 'Juno', 'Kite', 'Lumen', 'Mira', 'Onyx', 'Pip', 'Quill', 'Rune',
    'Sol', 'Tau', 'Umber', 'Vale', 'Wren', 'Xeno', 'Yara', 'Zed', 'Bloom', 'Cleo', 'Dash', 'Ember', 'Fable', 'Glyph', 'Halo'];
  const COLORS = ['#ff5f57', '#ff9f0a', '#ffd60a', '#30d158', '#40c8e0', '#0a84ff', '#5e5ce6', '#bf5af2', '#ff375f', '#64d2ff', '#ac8e68', '#32d74b'];
  const CONTAINER = '.b, .tiles, .tile, .prow, .post, .row, .tool, .work, .stats > div, .cs-panel';
  const BUILDABLE = 'h1, h2, h3, h4, p, img, canvas, video, .portrait, a, button, li, .badge, .eyebrow, .b, .tiles, .tile, .prow, .post, .row, .tool, .work, .stats > div, .tile b, .tile small, .row b, .row small, .row .d, .post .t, .post .d, .tool b, .tool small, .tool .mk, .tile .ic, .prow .icon, .work b, .work small, .foot > *, .track';
  const SKIP_INSIDE = '.track, .portrait';
  const small = matchMedia('(max-width: 600px)').matches;
  const START_AGENTS = small ? 5 : 12, MAX_AGENTS = small ? 12 : 30, BAND = 60;

  let sim = 0, last = 0, speed = 1, paused = false, touring = true, raf = 0, nudge = 0, running = false, finished = false;
  let layers = [], agents = [], overlay, bar, rulers, marks = [], particles = [], nextSpawn = 0, heroHTML = '', statusEl;
  const store = { set: (k, v) => { try { sessionStorage.setItem(k, v); } catch (e) {} } };

  const ease = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  // dark text on light agent colours, white on dark ones (WCAG contrast for the name tags and labels)
  const inkOn = hex => { const n = parseInt(hex.slice(1), 16), c = [n >> 16, n >> 8 & 255, n & 255].map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * c[0] + .7152 * c[1] + .0722 * c[2] > .179 ? '#111110' : '#ffffff'; };
  const docRect = el => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };

  /* ---------- layers ---------- */
  function collect() {
    const main = document.querySelector('main.col');
    const picked = [];
    main.querySelectorAll(BUILDABLE).forEach(node => {
      const skipHost = node.parentElement && node.parentElement.closest(SKIP_INSIDE);
      if (skipHost && main.contains(skipHost)) return;
      if (node.closest('dialog')) return;
      // skip children of an already-collected element that is not a container
      const owner = picked.find(p => p.contains(node) && p !== node);
      if (owner && !owner.matches(CONTAINER)) return;
      picked.push(node);
    });
    layers = picked.map((n, i) => ({ el: n, i, kind: kindOf(n), parent: null, state: 'todo', rect: null }))
      .filter(l => { const r = l.el.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    layers.forEach(l => {
      l.rect = docRect(l.el);
      l.parent = layers.find(p => p !== l && p.kind === 'box' && p.el.contains(l.el)) || null;
      l.el.style.opacity = '0';
    });
    layers.sort((a, b) => Math.floor(a.rect.y / BAND) - Math.floor(b.rect.y / BAND) || a.i - b.i);
  }
  function kindOf(n) {
    if (n.matches('.hero h1')) return 'hero';
    if (n.matches('img, canvas, video, .portrait')) return 'image';
    if (n.matches(CONTAINER) || n.matches('.track')) return 'box';
    return 'text';
  }
  function durationOf(l) {
    const r = l.rect;
    if (l.kind === 'hero') return 1500;
    if (l.kind === 'image') return 950;
    if (l.kind === 'box') return 520;
    return clamp(240 + r.w * .9 + (r.h > 40 ? r.h * 2 : 0), 320, 1300);
  }

  /* hero name: letters rise from blur one by one */
  function splitHero(h) {
    heroHTML = h.innerHTML;
    h.setAttribute('aria-label', h.textContent.trim());
    [...h.childNodes].forEach(node => {
      if (node.nodeType !== 3) return;
      // one wrapper per text run, so a flex heading treats the letters as a single item
      const word = el('span', 'ba-word'); word.setAttribute('aria-hidden', 'true');
      [...node.textContent.replace(/\s+$/, '')].forEach(ch => word.appendChild(el('span', 'ba-ltr', ch === ' ' ? '&nbsp;' : ch)));
      if (word.childNodes.length) node.replaceWith(word); else node.remove();
    });
  }

  /* ---------- reveal effects (p is eased progress 0..1) ---------- */
  function paint(l, p, a) {
    const s = l.el.style, r = l.rect;
    s.opacity = '1';
    if (l.kind === 'text') {
      s.clipPath = `inset(-3px ${(1 - p) * 100}% -3px -3px)`;
      a.to(r.x + r.w * p, r.y + r.h * .5);
    } else if (l.kind === 'image') {
      s.clipPath = `inset(0 0 ${(1 - p) * 100}% 0)`;
      s.filter = `blur(${(1 - p) * 8}px) grayscale(${1 - p}) brightness(${1 + (1 - p) * .5})`;
      a.to(r.x + r.w * .5 + Math.sin(p * 9) * r.w * .18, r.y + r.h * p);
      l.box.scan.style.top = `${p * 100}%`;
    } else if (l.kind === 'box') {
      s.clipPath = `inset(0 ${(1 - p) * 100}% ${(1 - p) * 100}% 0 round 12px)`;
      a.to(r.x + r.w * p, r.y + r.h * p);
    } else if (l.kind === 'hero') {
      const ls = l.el.querySelectorAll('.ba-ltr'), n = ls.length;
      ls.forEach((x, i) => {
        const t = clamp((p * (n + 5) - i) / 5, 0, 1);
        x.style.opacity = t; x.style.transform = `translateY(${(1 - t) * .5}em)`; x.style.filter = `blur(${(1 - t) * 6}px)`;
      });
      const cur = ls[clamp(Math.floor(p * n), 0, n - 1)];
      if (cur) { const cr = docRect(cur); a.to(cr.x + cr.w, cr.y + cr.h * .5); }
      const dot = l.el.querySelector('.dot'); if (dot) dot.style.opacity = p > .9 ? 1 : 0;
    }
  }
  function settle(l) {
    const s = l.el.style;
    s.opacity = ''; s.clipPath = ''; s.filter = '';
    if (l.kind === 'hero') { l.el.innerHTML = heroHTML; l.el.removeAttribute('aria-label'); }
    l.state = 'done';
  }

  /* ---------- agents ---------- */
  function makeAgent(i) {
    const c = COLORS[i % COLORS.length], name = NAMES[i % NAMES.length];
    const node = el('div', 'ba-agent');
    node.style.setProperty('--c', c); node.style.setProperty('--tc', inkOn(c));
    node.innerHTML = `<svg viewBox="0 0 22 24" width="22" height="24" aria-hidden="true"><path d="M3 2.5v16.2l4.6-4.3 3.2 6.9 2.9-1.3-3.1-6.8h6.4z" fill="${c}" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"/></svg><span class="ba-tag">${name}</span>`;
    overlay.appendChild(node);
    const a = { i, c, name, node, x: -40, y: scrollY + innerHeight * (.2 + Math.random() * .6), state: 'idle', job: null, until: 0, fly: null };
    a.to = (x, y) => { a.x = x; a.y = y; node.style.transform = `translate(${x - 3}px, ${y - 2.5}px)`; };
    a.to(a.x, a.y);
    agents.push(a);
    renderAvatars();
    return a;
  }
  function flyTo(a, x, y, then, slow) {
    const dx = x - a.x, dy = y - a.y, d = Math.hypot(dx, dy);
    const k = (Math.random() < .5 ? -1 : 1) * Math.min(160, d * .28);
    a.fly = { t0: sim, dur: clamp(d / (slow ? .7 : 1.6) + 180, 220, slow ? 1800 : 900), x0: a.x, y0: a.y, x1: x, y1: y,
      cx: (a.x + x) / 2 - dy / (d || 1) * k, cy: (a.y + y) / 2 + dx / (d || 1) * k, then };
    a.state = 'fly';
  }
  function stepFly(a) {
    const f = a.fly, t = ease(clamp((sim - f.t0) / f.dur, 0, 1)), u = 1 - t;
    a.to(u * u * f.x0 + 2 * u * t * f.cx + t * t * f.x1, u * u * f.y0 + 2 * u * t * f.cy + t * t * f.y1);
    if (t >= 1) { a.fly = null; f.then(); }
  }

  /* ---------- jobs ---------- */
  function frontier() { return layers.find(l => l.state !== 'done'); }
  function assign() {
    const idle = agents.filter(a => a.state === 'idle' || a.state === 'drift');
    if (!idle.length) return;
    const queue = layers.filter(l => l.state === 'todo').slice(0, idle.length + 4);
    for (const l of queue) {
      if (l.parent && l.parent.state !== 'done') continue;
      const free = agents.filter(a => a.state === 'idle' || a.state === 'drift');
      if (!free.length) break;
      l.rect = docRect(l.el);
      const a = free.reduce((b, c) => Math.hypot(c.x - l.rect.x, c.y - l.rect.y) < Math.hypot(b.x - l.rect.x, b.y - l.rect.y) ? c : b);
      l.state = 'claimed'; a.job = l;
      flyTo(a, l.rect.x, l.rect.y, () => startWork(a));
    }
  }
  function startWork(a) {
    const l = a.job;
    l.rect = docRect(l.el);
    if (l.kind === 'hero') splitHero(l.el);
    l.box = selectionBox(l, a.c);
    l.t0 = sim; l.dur = durationOf(l); l.state = 'building';
    a.state = 'work';
  }
  function selectionBox(l, c) {
    const r = l.rect, b = el('div', 'ba-box');
    b.style.cssText = `--c:${c};--tc:${inkOn(c)};left:${r.x}px;top:${r.y}px;width:${r.w}px;height:${r.h}px`;
    const cls = [...l.el.classList].filter(x => !x.startsWith('ba-'))[0];
    b.innerHTML = `<i class="h tl"></i><i class="h tr"></i><i class="h bl"></i><i class="h br"></i><span class="ba-lab">${l.el.tagName.toLowerCase()}${cls ? '.' + cls : ''} · ${Math.round(r.w)} × ${Math.round(r.h)}</span><span class="ba-pr"><i></i></span>`;
    b.scan = el('span', 'ba-scan'); if (l.kind === 'image') b.appendChild(b.scan);
    overlay.appendChild(b);
    return b;
  }
  function stepWork(a) {
    const l = a.job, p = clamp((sim - l.t0) / l.dur, 0, 1);
    paint(l, ease(p), a);
    l.box.querySelector('.ba-pr i').style.transform = `scaleX(${p})`;
    if (p >= 1) {
      settle(l);
      const b = l.box; b.classList.add('out'); setTimeout(() => b.remove(), 260 / speed);
      a.job = null; a.state = 'rest'; a.until = sim + 120 + Math.random() * 220;
    }
  }
  function drift(a) {
    const f = frontier(); if (!f) return;
    const col = document.querySelector('main.col').getBoundingClientRect();
    flyTo(a, col.left + scrollX + Math.random() * col.width, f.rect.y + (Math.random() - .3) * 260, () => { a.state = 'rest'; a.until = sim + 400 + Math.random() * 600; }, true);
    a.state = 'drift';
  }

  /* ---------- chrome: rulers, marks, bar ---------- */
  function buildChrome() {
    overlay = el('div', 'ba-overlay'); overlay.setAttribute('aria-hidden', 'true');
    overlay.style.height = document.documentElement.scrollHeight + 'px';
    document.body.appendChild(overlay);
    rulers = el('div', 'ba-rulers', '<canvas class="rx"></canvas><canvas class="ry"></canvas><span class="rc"></span>');
    rulers.setAttribute('aria-hidden', 'true');
    document.body.appendChild(rulers);
    drawRulers();
    for (let i = 0; i < (small ? 8 : 16); i++) {
      const m = el('span', 'ba-mark', '+');
      m.style.left = (5 + Math.random() * 90) + '%'; m.style.top = (Math.random() * innerHeight * 1.8) + 'px';
      overlay.appendChild(m); marks.push(m);
    }
    bar = el('div', 'ba-bar');
    bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', 'Page build controls');
    document.body.appendChild(bar);
    statusEl = el('span', 'visually-hidden'); statusEl.setAttribute('role', 'status'); document.body.appendChild(statusEl);
    renderBar();
  }
  function renderBar() {
    bar.innerHTML = `<span class="ba-avs" aria-hidden="true"></span>
      <span class="ba-meta"><span class="ba-txt"></span><span class="ba-prog" aria-hidden="true"><i></i></span></span>
      <span class="ba-ctl">
        <button type="button" class="ba-btn ba-tour" aria-pressed="${touring}">Touring</button>
        <button type="button" class="ba-btn ba-speed" aria-label="Speed ${speed}x">${speed}x</button>
        <button type="button" class="ba-btn ba-pause" aria-label="${paused ? 'Resume' : 'Pause'}">${paused ? '▶' : '❚❚'}</button>
        <button type="button" class="ba-btn ba-skip">Skip</button>
      </span>`;
    bar.querySelector('.ba-tour').onclick = () => { touring = !touring; bar.querySelector('.ba-tour').setAttribute('aria-pressed', touring); };
    bar.querySelector('.ba-speed').onclick = e => { speed = speed === 4 ? 1 : speed * 2; e.currentTarget.textContent = speed + 'x'; e.currentTarget.setAttribute('aria-label', `Speed ${speed}x`); syncCssAnimations(); };
    bar.querySelector('.ba-pause').onclick = e => { paused = !paused; e.currentTarget.textContent = paused ? '▶' : '❚❚'; e.currentTarget.setAttribute('aria-label', paused ? 'Resume' : 'Pause'); syncCssAnimations(); };
    bar.querySelector('.ba-skip').onclick = skip;
    renderAvatars(); updateBar(true);
  }
  function renderAvatars() {
    const box = bar && bar.querySelector('.ba-avs'); if (!box) return;
    const show = agents.slice(0, small ? 3 : 6);
    box.innerHTML = show.map(a => `<i style="--c:${a.c};--tc:${inkOn(a.c)}" title="${a.name}">${a.name[0]}</i>`).join('') + (agents.length > show.length ? `<b>+${agents.length - show.length}</b>` : '');
  }
  let lastBar = 0, lastPct = -1;
  function updateBar(force) {
    if (!bar || finished) return;
    if (!force && sim - lastBar < 90) return; lastBar = sim;
    const done = layers.filter(l => l.state === 'done').length, pct = layers.length ? done / layers.length : 0;
    bar.querySelector('.ba-txt').textContent = `${agents.length} agents · ${done} / ${layers.length} layers`;
    bar.querySelector('.ba-prog i').style.transform = `scaleX(${pct})`;
    const q = Math.floor(pct * 4); if (q !== lastPct) { lastPct = q; statusEl.textContent = q === 0 ? 'Building the page' : `Page ${q * 25}% built`; }
  }
  function drawRulers() {
    if (!rulers) return;
    const dpr = Math.min(2, devicePixelRatio || 1), cs = getComputedStyle(root);
    const ink = cs.getPropertyValue('--mute').trim() || '#888', line = cs.getPropertyValue('--line-2').trim() || '#ccc';
    const draw = (cv, len, horiz, offset) => {
      const W = horiz ? len : 18, H = horiz ? 18 : len;
      cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + 'px'; cv.style.height = H + 'px';
      const g = cv.getContext('2d'); g.scale(dpr, dpr); g.clearRect(0, 0, W, H);
      g.strokeStyle = line; g.fillStyle = ink; g.font = '9px ui-monospace, Menlo, monospace'; g.lineWidth = 1;
      const start = Math.floor(offset / 10) * 10;
      for (let v = start; v < offset + len; v += 10) {
        const p = v - offset + .5, size = v % 100 === 0 ? 10 : v % 50 === 0 ? 6 : 3;
        g.beginPath();
        if (horiz) { g.moveTo(p, 18); g.lineTo(p, 18 - size); } else { g.moveTo(18, p); g.lineTo(18 - size, p); }
        g.stroke();
        if (v % 100 === 0) {
          if (horiz) g.fillText(v, p + 2, 8);
          else { g.save(); g.translate(8, p + 2); g.rotate(-Math.PI / 2); g.fillText(v, -g.measureText(v).width - 2, 0); g.restore(); }
        }
      }
    };
    draw(rulers.querySelector('.rx'), innerWidth, true, scrollX);
    draw(rulers.querySelector('.ry'), innerHeight, false, scrollY);
  }

  /* speed and pause also drive any CSS animation on the page */
  function syncCssAnimations() {
    document.getAnimations().forEach(an => {
      if (an.playState === 'finished') return;
      an.playbackRate = speed;
      paused ? an.pause() : an.play();
    });
  }

  /* ---------- touring: keep the build frontier ~30% down the viewport ---------- */
  function tour(dt) {
    if (!touring || paused) return;
    const f = frontier(); if (!f) return;
    const max = document.documentElement.scrollHeight - innerHeight;
    const target = clamp(f.rect.y - innerHeight * .3, 0, max);
    const y = scrollY + (target - scrollY) * (1 - Math.exp(-dt * speed / 420));
    if (Math.abs(y - scrollY) > .5) scrollTo(0, y);
  }
  const stopTour = e => {
    if (!running || finished) return;
    if (e.type === 'keydown' && !['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Home', 'End', ' '].includes(e.key)) return;
    if (e.type === 'keydown' && e.target.closest && e.target.closest('.ba-bar')) return;
    touring = false; const t = bar.querySelector('.ba-tour'); if (t) t.setAttribute('aria-pressed', 'false');
  };

  /* ---------- main loop ---------- */
  // next frame via rAF, with a timer fallback so the clock keeps moving if frames are starved
  function schedule() {
    raf = requestAnimationFrame(frame);
    nudge = setTimeout(() => { cancelAnimationFrame(raf); frame(performance.now()); }, 100);
  }
  function frame(now) {
    clearTimeout(nudge);
    const dt = Math.min(250, now - (last || now)); last = now;   // catch up on slow frames instead of crawling
    if (!paused) sim += dt * speed;
    if (!finished) {
      if (sim >= nextSpawn && agents.length < MAX_AGENTS) { const a = makeAgent(agents.length); flyTo(a, a.x + 80 + Math.random() * 120, a.y, () => { a.state = 'idle'; }); nextSpawn = sim + 2000; }
      if (!paused) {
        assign();
        agents.forEach(a => {
          if (a.state === 'fly' || a.state === 'drift') stepFly(a);
          else if (a.state === 'work') stepWork(a);
          else if (a.state === 'rest' && sim >= a.until) a.state = 'idle';
          else if (a.state === 'idle' && !layers.some(l => l.state === 'todo')) drift(a);
        });
      }
      marks.forEach(m => { m.style.opacity = clamp(1 - (sim - 1500) / 1500, 0, 1); });
      tour(dt);
      updateBar();
      if (layers.every(l => l.state === 'done')) finale();
    } else {
      agents.forEach(a => { if (a.fly && !paused) { stepFly(a); trail(a); } });
    }
    schedule();
  }
  function trail(a) {
    if (particles.length > 260) return;
    const p = el('i', 'ba-spark'); p.style.cssText = `--c:${a.c};left:${a.x}px;top:${a.y}px`;
    overlay.appendChild(p); particles.push(p);
    setTimeout(() => { p.remove(); particles.splice(particles.indexOf(p), 1); }, 700);
  }

  /* ---------- finale, skip, replay ---------- */
  function finale() {
    if (finished) return;
    finished = true;
    const secs = (sim / 1000).toFixed(1), crew = agents.length;
    agents.forEach((a, i) => {
      if (a.job && a.job.box) a.job.box.remove();
      setTimeout(() => flyTo(a, scrollX + innerWidth + 80, scrollY - 80 - Math.random() * 120, () => a.node.remove()), i * 40);
    });
    rulers.classList.add('out');
    document.querySelectorAll('.ba-box').forEach(b => b.remove());
    bar.classList.add('done');
    bar.innerHTML = `<span class="ba-txt">Rebuilt by ${crew} agents in ${secs}s</span><button type="button" class="ba-btn ba-replay">↻ Replay</button><button type="button" class="ba-x" aria-label="Close build controls">×</button>`;
    bar.querySelector('.ba-replay').onclick = replay;
    bar.querySelector('.ba-x').onclick = () => { bar.remove(); };
    statusEl.textContent = `Page built by ${crew} agents in ${secs} seconds`;
    root.classList.remove('building');
    store.set('built', '1');
    afterBuild();
    setTimeout(() => { cancelAnimationFrame(raf); clearTimeout(nudge); overlay.remove(); rulers.remove(); running = false; }, 2600);
  }
  function skip() {
    layers.forEach(l => {
      if (l.box) l.box.remove();
      if (l.state !== 'done') { if (l.kind === 'hero' && l.el.querySelector('.ba-ltr')) l.el.innerHTML = heroHTML; settle(l); }
    });
    agents.forEach(a => { a.job = null; });
    finale();
  }
  function replay() {
    cancelAnimationFrame(raf); clearTimeout(nudge);
    document.querySelectorAll('.ba-overlay, .ba-rulers, .ba-bar').forEach(n => n.remove());
    if (statusEl) statusEl.remove();
    agents = []; marks = []; particles = []; layers = []; sim = 0; last = 0; nextSpawn = 0; finished = false; touring = true; paused = false; speed = 1;
    document.querySelectorAll('.tile small').forEach(s => { if (s.dataset.n) s.firstChild.textContent = s.dataset.n; });
    scrollTo(0, 0);
    root.classList.add('pre-build');
    requestAnimationFrame(start);
  }

  /* after the build: counters count up */
  function afterBuild() {
    document.querySelectorAll('.tile small').forEach(s => {
      const m = s.textContent.match(/^(\d+)/); if (!m) return;
      const n = +m[1], node = s.firstChild; s.dataset.n = node.textContent;
      const rest = node.textContent.slice(m[1].length), t0 = performance.now();
      const tick = now => {
        const p = clamp((now - t0) / 900, 0, 1);
        node.textContent = Math.round(n * ease(p)) + rest;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }

  /* ---------- start ---------- */
  function start() {
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    scrollTo(0, 0);
    root.classList.add('building');
    collect();
    root.classList.remove('pre-build');
    buildChrome();
    for (let i = 0; i < START_AGENTS; i++) {
      const a = makeAgent(i);
      flyTo(a, 60 + Math.random() * 160, scrollY + innerHeight * (.15 + Math.random() * .5), () => { a.state = 'idle'; });
    }
    nextSpawn = 2000; running = true;
    last = 0; schedule();
    window.__build = { get layers() { return layers; }, get agents() { return agents; }, get sim() { return sim; } };  // inspection hook for debugging
  }

  addEventListener('wheel', stopTour, { passive: true });
  addEventListener('touchstart', stopTour, { passive: true });
  addEventListener('keydown', stopTour);
  addEventListener('scroll', () => { if (running) drawRulers(); }, { passive: true });
  addEventListener('resize', () => { if (!running) return; drawRulers(); if (overlay) overlay.style.height = document.documentElement.scrollHeight + 'px'; layers.forEach(l => { if (l.state === 'todo') l.rect = docRect(l.el); }); });

  // wait for fonts (at most 1.2s) so layer positions are final; never start after the safety reveal in <head> fired
  const go = () => Promise.race([document.fonts ? document.fonts.ready : Promise.resolve(), new Promise(r => setTimeout(r, 1200))])
    .then(() => { if (root.classList.contains('pre-build')) start(); });
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', go) : go();
})();
