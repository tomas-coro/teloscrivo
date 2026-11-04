// teloscrivo - JS del sito. Tutto e' un miglioramento: senza JS le pagine si leggono comunque
// (il testo degli scritti sta sempre nell'HTML, qui si aggiunge solo l'effetto "compare scorrendo").
(function () {
  'use strict';
  const reduced = matchMedia('(prefers-reduced-motion:reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const br = s => esc(s).replace(/\n/g, '<br>');
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

  // ── avviso in basso ──
  let toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.setAttribute('role', 'status');
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.classList.remove('on');
    void toastEl.offsetWidth;
    toastEl.classList.add('on');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('on'), 3200);
  }

  // ── condividi: pannello del telefono, altrimenti copia il link; se fallisce tutto lo dice ──
  async function share() {
    const url = ($('link[rel="canonical"]') || {}).href || location.href;
    try {
      if (navigator.share) { await navigator.share({ title: document.title, url }); return; }
      await navigator.clipboard.writeText(url);
      toast('Link copiato');
    } catch (err) {
      if (err && err.name === 'AbortError') return; // ha chiuso il pannello: non e' un errore
      toast('Non riesco a copiare il link: copialo dalla barra del browser.');
    }
  }
  $$('[data-share]').forEach(b => { b.hidden = false; b.addEventListener('click', share); }); // nascosti nell'HTML: senza JS non servono

  // ── titolo che vola tra elenco e lettura (View Transitions, dove supportate) ──
  // Il titolo della pagina di lettura ha gia' il nome "titolo" (CSS). Qui lo diamo alla riga cliccata
  // (in uscita) o a quella da cui si torna (in ritorno), cosi' il browser le fa viaggiare insieme.
  function mark(url) {
    $$('a.entry').forEach(a => { const t = $('.et', a); if (t) t.style.viewTransitionName = a.href === url ? 'titolo' : ''; });
  }
  addEventListener('pageswap', e => { if (e.viewTransition && e.activation && e.activation.entry) mark(e.activation.entry.url); });
  addEventListener('pagereveal', e => {
    const from = window.navigation && navigation.activation && navigation.activation.from;
    if (e.viewTransition && from) mark(from.url);
  });

  // ── lettura: il testo compare riga per riga mentre scorri (e sparisce se risali) ──
  const units = $$('.u'), rend = $('.rend'), cue = $('[data-cue]');
  if (units.length) {
    let ticking = false;
    const reveal = () => {
      const lim = innerHeight * 0.88;
      units.forEach(u => u.classList.toggle('on', u.getBoundingClientRect().top < lim));
      if (rend) rend.classList.toggle('on', rend.getBoundingClientRect().top < lim);
      const max = document.documentElement.scrollHeight - innerHeight;
      document.documentElement.style.setProperty('--rp', max > 0 ? Math.min(1, scrollY / max) : 0);
      if (cue) cue.classList.toggle('off', scrollY > 40);
      ticking = false;
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(reveal); } }, { passive: true });
    addEventListener('resize', reveal);
    reveal();
  }
  // "Indietro": se si arriva da una pagina del sito torna davvero indietro (cosi' il titolo rivola),
  // altrimenti il link porta alla sezione.
  const back = $('[data-rback]');
  if (back) back.addEventListener('click', e => {
    try {
      if (document.referrer && new URL(document.referrer).origin === location.origin && history.length > 1) {
        e.preventDefault();
        history.back();
      }
    } catch (_) { /* referrer non leggibile: resta il link normale */ }
  });

  // ── apertura della home: una volta per scheda, senza bloccare chi riduce il movimento ──
  const opening = $('[data-opening]');
  if (opening && !reduced) {
    let seen = false;
    try { seen = sessionStorage.getItem('teloscrivo-opening') === '1'; sessionStorage.setItem('teloscrivo-opening', '1'); } catch (_) { /* storage disabilitato: mostra comunque l'apertura */ }
    if (!seen) {
      const max = $('[data-opening-max]', opening), skip = $('[data-opening-skip]', opening);
      const content = $('#contenuto'), header = $('.tbar'), skipLink = $('.skip');
      let autoTimer, pressTimer, expandTimer, endTimer;
      function finish(manual = false) {
        clearTimeout(autoTimer); clearTimeout(pressTimer); clearTimeout(expandTimer); clearTimeout(endTimer);
        const focused = opening.contains(document.activeElement);
        opening.hidden = true;
        document.body.style.overflow = '';
        content.inert = header.inert = skipLink.inert = false;
        if (focused) {
          if (manual) $('.brand').focus({ preventScroll: true });
          else opening.blur();
        }
      }
      function expand() {
        if (max.classList.contains('pressed')) return;
        clearTimeout(autoTimer);
        opening.classList.add('clicked');
        max.classList.add('pressed');
        skip.hidden = true;
        pressTimer = setTimeout(() => {
          opening.classList.add('expanding');
          expandTimer = setTimeout(() => {
            opening.classList.add('leaving');
            endTimer = setTimeout(finish, 300);
          }, 1000);
        }, 160);
      }
      opening.hidden = false;
      document.body.style.overflow = 'hidden';
      content.inert = header.inert = skipLink.inert = true;
      opening.focus({ preventScroll: true });
      max.addEventListener('click', expand);
      skip.addEventListener('click', () => finish(true));
      autoTimer = setTimeout(() => max.click(), 3400);
    }
  }

  // ── home: il blocco che si scrive da solo, dal piu' recente ──
  const latestEl = $('#latest');
  if (latestEl) {
    const LATEST = JSON.parse(latestEl.textContent);
    const lk = $('[data-lk]'), lt = $('[data-lt]'), lx = $('[data-lx]'), pg = $('[data-pg]'), cta = $('[data-cta]'), pause = $('[data-pause]');
    const cr = '<i class="cr"></i>';
    // il testo intero e' sempre nel layout (parte invisibile): le righe non saltano mentre scrive
    const part = (str, n, showCr) => br(str.slice(0, n)) + (showCr ? cr : '') + '<span class="gh">' + br(str.slice(n)) + '</span>';
    const draw = (p, n) => {
      const nt = Math.min(n, p.t.length), nx = Math.max(0, n - p.t.length);
      lt.innerHTML = part(p.t, nt, nx <= 0);
      lx.innerHTML = part(p.x, nx, nx > 0);
    };
    let tok = 0, auto = !reduced, current = 0;
    if (!reduced && LATEST.length > 1) pause.hidden = false;
    const syncPause = () => {
      pause.textContent = auto ? '❚❚' : '▶';
      pause.setAttribute('aria-label', auto ? 'Metti in pausa gli ultimi scritti' : 'Riprendi gli ultimi scritti');
    };
    pg.innerHTML = LATEST.map((p, i) => `<button type="button" data-i="${i}" aria-label="Scritto ${i + 1}: ${esc(p.t)}" aria-pressed="false"></button>`).join('');
    function meta(p, i) {
      lk.textContent = (i === 0 ? 'Ultimo scritto' : 'Prima ancora') + ' · ' + p.k + ' · ' + p.d;
      cta.href = p.u;
      pg.querySelectorAll('button').forEach((b, j) => b.setAttribute('aria-pressed', j === i ? 'true' : 'false'));
    }
    function play(i) {
      const my = ++tok, p = LATEST[i], full = p.t.length + p.x.length;
      let n = 0;
      current = i;
      meta(p, i);
      if (reduced) { draw(p, full); return; }
      const live = () => my === tok;
      function erase() {
        if (!live()) return;
        n = Math.max(0, n - 3); draw(p, n);
        if (n > 0) setTimeout(erase, 12); else setTimeout(() => live() && play((i + 1) % LATEST.length), 260);
      }
      (function type() {
        if (!live()) return;
        n++; draw(p, n);
        if (n < full) setTimeout(type, n <= p.t.length ? 70 : 34);
        else if (auto) setTimeout(erase, 3600); // se l'utente sceglie un pallino smette di girare da solo
      })();
    }
    pg.addEventListener('click', e => { const b = e.target.closest('button'); if (b) { auto = false; syncPause(); play(+b.dataset.i); } });
    pause.addEventListener('click', () => {
      auto = !auto;
      syncPause();
      if (auto) play(current);
      else { ++tok; draw(LATEST[current], LATEST[current].t.length + LATEST[current].x.length); }
    });
    if (LATEST.length > 1) play(0); else meta(LATEST[0], 0);
  }

  // ── home: filtri per sezione sull'elenco (senza JS l'elenco resta intero) ──
  const chips = $('[data-chips]');
  if (chips) {
    chips.hidden = false;
    const lh = $('[data-lh]'), lc = $('[data-lc]'), NAMES = JSON.parse(chips.dataset.names);
    chips.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      const k = b.dataset.cat;
      $$('button', chips).forEach(x => x.setAttribute('aria-pressed', x === b ? 'true' : 'false'));
      let shown = 0;
      $$('li[data-cat]').forEach(li => { const off = !!k && li.dataset.cat !== k; li.hidden = off; if (!off) shown++; });
      $$('.mg').forEach(g => { g.hidden = !$('li[data-cat]:not([hidden])', g); });
      lh.textContent = k ? NAMES[k] : 'Tutti gli scritti';
      lc.textContent = shown + (shown === 1 ? ' scritto' : ' scritti');
    });
  }

  // ── pagina Cerca: legge cerca.json e filtra mentre scrivi ──
  const sp = $('[data-searchpage]');
  if (sp) {
    const input = $('input', sp), out = $('[data-results]', sp), root = sp.dataset.root;
    const ARROW = '<svg class="ar" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg>';
    let DATA = null;
    const show = () => {
      const q = norm(input.value.trim());
      history.replaceState(null, '', q ? '?q=' + encodeURIComponent(input.value.trim()) : location.pathname);
      if (!q) { out.innerHTML = '<p class="msg">Scrivi una parola: cerco nei titoli e nei testi.</p>'; return; }
      const terms = q.split(/\s+/);
      const hits = DATA.filter(p => terms.every(t => p.h.includes(t)));
      out.innerHTML = hits.length
        ? '<ul>' + hits.map(p => `<li><a class="entry" href="${root}${p.u}"><span class="ed">${esc(p.d)}</span><b class="et">${esc(p.t)}</b><span class="ec">${esc(p.s)}</span><span class="rx">${esc(p.x)}</span>${ARROW}</a></li>`).join('') + '</ul>'
        : `<p class="msg">Nessun risultato per «${esc(input.value.trim())}».</p>`;
    };
    fetch(root + 'cerca.json')
      .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(rows => {
        DATA = rows.map(p => Object.assign(p, { h: norm(p.t + ' ' + p.b + ' ' + p.s) }));
        const q0 = new URLSearchParams(location.search).get('q');
        if (q0) input.value = q0;
        input.addEventListener('input', show);
        input.disabled = false;
        show();
        input.focus();
      })
      .catch(err => { // errore visibile, niente finta "nessun risultato"
        out.innerHTML = '<p class="msg err">La ricerca non si e\' caricata (' + esc(err.message) + '). Riprova tra poco o torna alla home.</p>';
      });
  }
})();
