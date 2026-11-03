/* Shared behaviour: theme, UI sounds, dot portrait, copy email, Best Design filter + lightbox */
(() => {
  const root = document.documentElement;
  const store = {
    get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- theme ---------- */
  const savedTheme = store.get('theme');
  if (savedTheme) root.dataset.theme = savedTheme;
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;

  /* ---------- UI sounds, synthesised with Web Audio ---------- */
  const Sound = (() => {
    let ctx = null, on = store.get('sound') !== 'off', armed = false;
    const ac = () => {
      if (!ctx) { const C = window.AudioContext || window.webkitAudioContext; if (!C) return null; ctx = new C(); }
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    };
    function tone(f1, f2, dur, gain, type) {
      const c = ac(); if (!c) return;
      const t = c.currentTime, o = c.createOscillator(), g = c.createGain();
      o.type = type; o.frequency.setValueAtTime(f1, t); o.frequency.exponentialRampToValueAtTime(f2, t + dur);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(gain, t + .004); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
      o.connect(g).connect(c.destination); o.start(t); o.stop(t + dur + .02);
    }
    function air(from, to, dur, gain) {
      const c = ac(); if (!c) return;
      const t = c.currentTime, n = Math.floor(c.sampleRate * dur), b = c.createBuffer(1, n, c.sampleRate), d = b.getChannelData(0);
      for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
      const s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
      s.buffer = b; f.type = 'bandpass'; f.Q.value = 1.4;
      f.frequency.setValueAtTime(from, t); f.frequency.exponentialRampToValueAtTime(to, t + dur);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(gain, t + dur * .3); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
      s.connect(f).connect(g).connect(c.destination); s.start(t);
    }
    const fx = {
      tick: () => tone(2400, 1900, .035, .016, 'triangle'),
      tap: () => tone(620, 300, .09, .07, 'sine'),
      whisk: () => air(700, 3200, .16, .05),
      pop: () => { tone(180, 60, .22, .12, 'sine'); air(2400, 500, .25, .035); },
      toggle: () => { tone(900, 1300, .05, .05, 'sine'); }
    };
    addEventListener('pointerdown', () => { armed = true; }, { once: true, capture: true });
    addEventListener('keydown', () => { armed = true; }, { once: true, capture: true });
    return {
      play(n) { if (on && armed) fx[n](); },
      get on() { return on; },
      set on(v) { on = v; store.set('sound', v ? 'on' : 'off'); }
    };
  })();
  window.Sound = Sound;

  function wireSounds(scope) {
    scope.querySelectorAll('a, button, .tile').forEach(el => {
      if (el.dataset.snd) return; el.dataset.snd = '1';
      el.addEventListener('pointerenter', () => Sound.play('tick'));
      el.addEventListener('click', () => {
        const internal = el.tagName === 'A' && el.getAttribute('href') && !/^https?:|^mailto:|^#/.test(el.getAttribute('href'));
        Sound.play(internal ? 'whisk' : 'tap');
      });
    });
  }

  /* ---------- dock controls ---------- */
  function initDock() {
    const snd = document.querySelector('.snd');
    if (snd) {
      const sync = () => { snd.setAttribute('aria-pressed', Sound.on); snd.querySelector('.tl').textContent = Sound.on ? 'Mute sounds' : 'Turn sounds on'; snd.setAttribute('aria-label', Sound.on ? 'Turn sound off' : 'Turn sound on'); };
      snd.addEventListener('click', () => { Sound.on = !Sound.on; sync(); Sound.play('toggle'); });
      sync();
    }
    const thm = document.querySelector('.thm');
    if (thm) {
      const sync = () => { const l = isDark() ? 'Light mode' : 'Dark mode'; thm.querySelector('.tl').textContent = l; thm.setAttribute('aria-label', l); };
      thm.addEventListener('click', () => {
        const next = isDark() ? 'light' : 'dark';
        root.classList.add('no-tx'); root.dataset.theme = next; store.set('theme', next); sync(); Sound.play('toggle');
        requestAnimationFrame(() => requestAnimationFrame(() => root.classList.remove('no-tx')));
        dispatchEvent(new Event('themechange'));
      });
      sync();
    }
  }

  /* ---------- keyboard shortcuts: G then a page letter, M for sound, T for theme ---------- */
  function initKeys() {
    let pending = 0;
    addEventListener('keydown', e => {
      if (e.metaKey || e.ctrlKey || e.altKey || e.target.closest('input, textarea, select, [contenteditable]')) return;
      if (document.querySelector('.lb:not([hidden]), dialog[open]')) return;
      const k = e.key.toLowerCase();
      if (pending && Date.now() - pending < 1200) {
        pending = 0;
        const a = document.querySelector(`.dock a[data-key="${k}"]`);
        if (a) { e.preventDefault(); Sound.play('whisk'); location.href = a.href; }
        return;
      }
      if (k === 'g') { pending = Date.now(); return; }
      if (k === 'm') document.querySelector('.snd')?.click();
      if (k === 't') document.querySelector('.thm')?.click();
    });
  }

  /* ---------- copy email ---------- */
  function initCopy() {
    document.querySelectorAll('[data-copy]').forEach(el => el.addEventListener('click', e => {
      e.preventDefault();
      const text = el.dataset.copy, lbl = el.querySelector('.lbl');
      // buttons with a label swap it to "Copied" in place; plain links fall back to a toast
      const done = () => {
        Sound.play('toggle');
        if (!lbl) return toast('Email copied');
        clearTimeout(el._t);
        if (!el.dataset.idle) el.dataset.idle = lbl.textContent;
        lbl.textContent = el.dataset.done; el.classList.add('copied');
        el._t = setTimeout(() => { lbl.textContent = el.dataset.idle; el.classList.remove('copied'); }, 1800);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, () => fallback(text, done)); else fallback(text, done);
    }));
    function fallback(text, done) {
      const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); done(); } catch (e) { toast(text); } t.remove();
    }
  }
  let toastTimer;
  function toast(msg) {
    document.querySelectorAll('.toast').forEach(t => t.remove());
    const t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = msg;
    document.body.appendChild(t); clearTimeout(toastTimer); toastTimer = setTimeout(() => t.remove(), 1800);
  }

  /* ---------- dot portrait: dots flee the pointer, spring home, click for a shockwave ---------- */
  function dots(host, { interactive = true, fadeRows = 12 } = {}) {
    const P = window.PORTRAIT; if (!P || !host) return;
    const cv = host.querySelector('canvas'), cx = cv.getContext('2d');
    const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
    let W = 0, H = 0, pts = [], ptr = { x: -1e4, y: -1e4 }, ink = '#000', raf = 0;
    function build() {
      const r = cv.getBoundingClientRect(), dpr = Math.min(2, devicePixelRatio || 1);
      W = r.width; H = r.height; if (!W) return;
      cv.width = W * dpr; cv.height = H * dpr; cx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const step = W / P.cols, dark = isDark(); pts = [];
      for (let y = 0; y < P.rows; y++) for (let x = 0; x < P.cols; x++) {
        const ch = P.data[y * P.cols + x]; if (ch === '.') continue;
        // light ink on a dark page: size dots by brightness so the photo stays positive
        const v = dark ? Math.max(.12, (10 - +ch) / 10) : (+ch + 1) / 10, a = y > P.rows - fadeRows ? Math.max(0, (P.rows - y) / fadeRows) : 1;
        const hx = (x + .5) * step, hy = (y + .5) * step;
        pts.push({ hx, hy, x: hx, y: hy, vx: 0, vy: 0, r: step * .48 * Math.pow(v, .75), a });
      }
      ink = getComputedStyle(root).getPropertyValue('--ink').trim() || '#000';
      draw();
    }
    function draw() {
      cx.clearRect(0, 0, W, H); cx.fillStyle = ink;
      for (const p of pts) { if (p.a <= 0) continue; cx.globalAlpha = p.a; cx.beginPath(); cx.arc(p.x, p.y, p.r, 0, 6.283); cx.fill(); }
      cx.globalAlpha = 1;
    }
    function frame() {
      const reach = W * .16, reach2 = reach * reach; let moving = false;
      for (const p of pts) {
        const dx = p.x - ptr.x, dy = p.y - ptr.y, d2 = dx * dx + dy * dy;
        if (d2 < reach2) { const d = Math.sqrt(d2) || 1, f = (1 - d / reach) * 1.6; p.vx += dx / d * f; p.vy += dy / d * f; }
        p.vx += (p.hx - p.x) * .06; p.vy += (p.hy - p.y) * .06; p.vx *= .84; p.vy *= .84; p.x += p.vx; p.y += p.vy;
        if (Math.abs(p.vx) + Math.abs(p.vy) > .02 || Math.abs(p.x - p.hx) + Math.abs(p.y - p.hy) > .1) moving = true;
      }
      draw();
      raf = (moving || ptr.x > -1e3) ? requestAnimationFrame(frame) : 0;
    }
    const wake = () => { if (!raf && !still) raf = requestAnimationFrame(frame); };
    const local = e => { const r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; };
    if (interactive) {
      host.addEventListener('pointermove', e => { ptr = local(e); wake(); });
      host.addEventListener('pointerleave', () => { ptr = { x: -1e4, y: -1e4 }; wake(); });
      host.addEventListener('pointerdown', e => {
        const o = local(e); Sound.play('pop'); if (still) return;
        for (const p of pts) { const dx = p.x - o.x, dy = p.y - o.y, d = Math.hypot(dx, dy) || 1, f = Math.max(0, 1 - d / (W * .9)) * 14; p.vx += dx / d * f; p.vy += dy / d * f; }
        wake();
      });
    }
    new ResizeObserver(build).observe(cv);
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', build);
    addEventListener('themechange', build);
  }

  /* ---------- Best Design: filter chips + lightbox ---------- */
  function initWorks() {
    const grid = document.querySelector('.works'); if (!grid) return;
    const items = [...grid.querySelectorAll('.work')];
    const chips = [...document.querySelectorAll('.chips button')];
    chips.forEach(c => c.addEventListener('click', () => {
      chips.forEach(x => x.setAttribute('aria-pressed', x === c));
      const f = c.dataset.filter;
      items.forEach(it => { it.hidden = f !== 'all' && it.dataset.cat !== f; });
    }));
    let lb = null, idx = 0;
    const visible = () => items.filter(i => !i.hidden);
    function open(i) {
      idx = i; const it = visible()[idx]; if (!it) return;
      if (!lb) {
        lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true');
        lb.innerHTML = '<button class="x" aria-label="Close">×</button><figure><figcaption><b></b><small></small></figcaption></figure>';
        lb.querySelector('figure').prepend(document.createElement('img'));
        lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('x')) close(); });
        document.body.appendChild(lb); wireSounds(lb);
      }
      lb.hidden = false;
      const img = lb.querySelector('img');
      img.src = it.dataset.full; img.alt = it.querySelector('img').alt;
      lb.querySelector('b').textContent = it.querySelector('b').textContent;
      lb.querySelector('small').textContent = it.querySelector('small').textContent;
      lb.querySelector('.x').focus();
      document.body.style.overflow = 'hidden';
    }
    function close() { if (!lb) return; lb.hidden = true; document.body.style.overflow = ''; visible()[idx]?.focus(); }
    items.forEach(it => it.addEventListener('click', () => open(visible().indexOf(it))));
    addEventListener('keydown', e => {
      if (!lb || lb.hidden) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight') { open((idx + 1) % visible().length); Sound.play('tick'); }
      if (e.key === 'ArrowLeft') { open((idx - 1 + visible().length) % visible().length); Sound.play('tick'); }
    });
  }

  /* ---------- tools carousel: arrows page the track, disable at the ends ---------- */
  function initCarousel() {
    document.querySelectorAll('.tools').forEach(sec => {
      const track = sec.querySelector('.track'), prev = sec.querySelector('.prev'), next = sec.querySelector('.next');
      if (!track) return;
      const sync = () => {
        const max = track.scrollWidth - track.clientWidth - 2;
        prev.disabled = track.scrollLeft <= 2;
        next.disabled = track.scrollLeft >= max;
        track.classList.toggle('end', track.scrollLeft >= max);
      };
      const page = dir => track.scrollBy({ left: dir * (track.clientWidth + 10), behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
      prev.addEventListener('click', () => page(-1));
      next.addEventListener('click', () => page(1));
      track.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight') { e.preventDefault(); page(1); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); page(-1); }
      });
      track.addEventListener('scroll', sync, { passive: true });
      new ResizeObserver(sync).observe(track);
      sync();
    });
  }

  /* ---------- case studies: before/after slider, image zoom, reading progress ---------- */
  function initCaseStudy() {
    document.querySelectorAll('.cs-cmp').forEach(c => {
      const frame = c.querySelector('.frame'), range = c.querySelector('input');
      const set = v => frame.style.setProperty('--x', v + '%');
      range.addEventListener('input', () => set(range.value));
      // dragging on the image itself also moves the divider
      let drag = false;
      const move = e => { const r = frame.getBoundingClientRect(); const v = Math.min(100, Math.max(0, (e.clientX - r.left) / r.width * 100)); range.value = v; set(v); };
      frame.addEventListener('pointerdown', e => { drag = true; frame.setPointerCapture(e.pointerId); move(e); });
      frame.addEventListener('pointermove', e => { if (drag) move(e); });
      frame.addEventListener('pointerup', () => { drag = false; });
    });

    let lb = null, last = null;
    const close = () => { if (!lb || lb.hidden) return; lb.hidden = true; document.body.style.overflow = ''; last?.focus(); };
    document.querySelectorAll('.cs-fig .zoom').forEach(btn => btn.addEventListener('click', () => {
      if (!lb) {
        lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true');
        lb.innerHTML = '<button class="x" aria-label="Close">×</button><figure><figcaption><small></small></figcaption></figure>';
        lb.querySelector('figure').prepend(document.createElement('img'));
        lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('x')) close(); });
        addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
        document.body.appendChild(lb); wireSounds(lb);
      }
      last = btn;
      const img = lb.querySelector('img'), cap = btn.closest('figure').querySelector('figcaption');
      const th = btn.querySelector('img');
      img.src = btn.dataset.full; img.alt = th.alt;
      lb.classList.toggle('scroll', th.naturalHeight / th.naturalWidth > 1.6);
      lb.querySelector('small').textContent = cap ? cap.textContent : '';
      lb.hidden = false; document.body.style.overflow = 'hidden'; lb.querySelector('.x').focus();
    }));

    const bar = document.querySelector('.cs-progress b');
    if (bar) {
      let ticking = false;
      const upd = () => { const h = document.documentElement.scrollHeight - innerHeight; bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`; ticking = false; };
      addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(upd); } }, { passive: true });
      upd();
    }
  }

  /* ---------- Lab popups: <dialog> with a #link per popup ---------- */
  function initDialogs() {
    const dialogs = document.querySelectorAll('dialog.pop');
    if (!dialogs.length) return;
    const open = id => {
      const d = document.getElementById('dlg-' + id); if (!d) return false;
      document.querySelectorAll('dialog.pop[open]').forEach(x => x.close());
      d.showModal(); d.querySelector('.pop-scroll').scrollTop = 0; Sound.play('whisk');
      history.replaceState(null, '', '#' + id);
      return true;
    };
    document.addEventListener('click', e => {
      const t = e.target.closest('[data-dialog]');
      if (t && open(t.dataset.dialog)) e.preventDefault();
    });
    dialogs.forEach(d => {
      d.querySelector('.pop-x').addEventListener('click', () => d.close());
      d.addEventListener('click', e => { if (e.target === d) d.close(); });   // click on the backdrop
      d.addEventListener('close', () => { if (location.hash) history.replaceState(null, '', location.pathname); });
      wireSounds(d);
    });
    if (location.hash) open(location.hash.slice(1));
  }

  document.addEventListener('DOMContentLoaded', () => {
    initDock(); initKeys(); initCopy(); initWorks(); initCarousel(); initCaseStudy(); initDialogs(); wireSounds(document);
    dots(document.querySelector('.portrait'));
    dots(document.querySelector('.dock .me'), { interactive: false, fadeRows: 0 });
  });
})();
