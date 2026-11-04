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
      $$('[data-share]').forEach(b => { const l = $('[data-share-lbl]', b); if (!l) return; const t = l.textContent; l.textContent = 'Link copiato'; b.classList.add('done'); setTimeout(() => { l.textContent = t; b.classList.remove('done'); }, 2200); });
    } catch (err) {
      if (err && err.name === 'AbortError') return; // ha chiuso il pannello: non e' un errore
      toast('Non riesco a copiare il link: copialo dalla barra del browser.');
    }
  }
  // ── copia link: sempre copia negli appunti, anche dove c'e' il pannello di condivisione ──
  async function copyLink(e) {
    const b = e.currentTarget, l = $('[data-copy-lbl]', b), t = l.textContent;
    const url = ($('link[rel="canonical"]') || {}).href || location.href;
    try {
      await navigator.clipboard.writeText(url);
      l.textContent = 'Link copiato'; b.classList.add('done');
      setTimeout(() => { l.textContent = t; b.classList.remove('done'); }, 2200);
    } catch (err) {
      toast('Non riesco a copiare il link: copialo dalla barra del browser.');
    }
  }
  $$('[data-copy]').forEach(b => { b.hidden = false; b.addEventListener('click', copyLink); });
  $$('[data-share]').forEach(b => { b.hidden = false; b.addEventListener('click', share); }); // nascosti nell'HTML: senza JS non servono

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
  // ── Indietro: UN solo modo, usato da tasto, Esc, freccia sinistra, swipe e X della ricerca ──
  // Se si arriva da una pagina del sito torna davvero indietro (cosi' l'apertura si richiude nella scheda),
  // altrimenti (link da Google, link condiviso) va al collegamento di riserva: la categoria o la home.
  // ── logo: se sono gia' in questa pagina, risale dolcemente invece di ricaricarla ──
  const brandEl = $('.brand');
  if (brandEl) brandEl.addEventListener('click', e => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
    if (new URL(brandEl.href).pathname.replace(/index\.html$/, '') !== location.pathname.replace(/index\.html$/, '')) return;
    e.preventDefault();
    scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
  });
  // ── Home: serve solo quando Indietro non ci porta gia' alla home ──
  // Scritto: si nasconde se arrivo dalla home. Categoria: Indietro porta alla home, quindi compare solo se arrivo da un altro scritto.
  const homeBtn = $('[data-home]');
  if (homeBtn) {
    let from = null;
    try { if (document.referrer) { const r = new URL(document.referrer); if (r.origin === location.origin) from = r.pathname.replace(/index\.html$/, ''); } } catch (_) { /* referrer illeggibile: tratto come arrivo diretto */ }
    const atHome = from === new URL(homeBtn.href).pathname.replace(/index\.html$/, '');
    homeBtn.hidden = homeBtn.dataset.home === 'scritto' ? atHome : (from === null || atHome);
  }
  const backLink = $('[data-rback]') || $('[data-search-close]');
  function goBack() {
    try {
      if (document.referrer && new URL(document.referrer).origin === location.origin && history.length > 1) { history.back(); return; }
    } catch (_) { /* referrer non leggibile: usa il collegamento di riserva */ }
    location.href = backLink.href;
  }
  if (backLink) {
    backLink.addEventListener('click', e => { if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return; e.preventDefault(); goBack(); });
    addEventListener('keydown', e => {
      if (e.defaultPrevented || e.altKey || e.metaKey || e.ctrlKey) return;
      const typing = /^(input|textarea)$/i.test(e.target.tagName);
      if (e.key === 'Escape' || (e.key === 'ArrowLeft' && !typing)) { e.preventDefault(); goBack(); }
    });
  }
  // swipe verso destra = indietro, la pagina segue il dito. Solo scritti e categorie (body.swipe).
  const page = $('#contenuto');
  if (backLink && page && document.body.classList.contains('swipe')) {
    let sw = null;
    page.addEventListener('pointerdown', e => {
      if (e.pointerType === 'mouse' && (innerWidth >= 640 || e.clientX > 44)) return; // col mouse solo dal bordo, nella vista telefono
      if (e.pointerType !== 'mouse' && e.clientX < 24) return; // il bordo e' del gesto "indietro" del telefono: non lo duplico
      sw = { x: e.clientX, y: e.clientY, t: performance.now(), on: false };
    });
    page.addEventListener('pointermove', e => {
      if (!sw) return;
      const dx = e.clientX - sw.x, dy = e.clientY - sw.y;
      if (!sw.on) {
        if (Math.abs(dy) > 12 && Math.abs(dy) > Math.abs(dx)) { sw = null; return; } // e' uno scroll
        if (dx > 12 && dx > Math.abs(dy) * 1.4) { sw.on = true; try { page.setPointerCapture(e.pointerId); } catch (_) { /* senza cattura funziona lo stesso */ } }
        else return;
      }
      page.style.transform = `translateX(${Math.max(0, dx)}px)`;
    });
    const settle = (dx, commit) => {
      page.style.transform = '';
      if (commit) { goBack(); return; }
      if (!reduced) page.animate([{ transform: `translateX(${dx}px)` }, { transform: 'none' }], { duration: 240, easing: EASE });
    };
    page.addEventListener('pointerup', e => {
      if (!sw) return;
      const s = sw; sw = null;
      if (!s.on) return;
      const dx = Math.max(0, e.clientX - s.x), v = dx / Math.max(1, performance.now() - s.t);
      settle(dx, dx > innerWidth * 0.33 || v > 0.6);
    });
    page.addEventListener('pointercancel', e => { if (sw && sw.on) settle(Math.max(0, e.clientX - sw.x), false); sw = null; });
  }

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
        document.dispatchEvent(new Event('teloscrivo:opened')); // la home puo' iniziare a scrivere
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
    // se l'apertura copre la pagina, il blocco aspetta che sparisca e poi inizia a scrivere (non parte gia' scritto)
    const start = () => { if (LATEST.length > 1) play(0); else { meta(LATEST[0], 0); draw(LATEST[0], LATEST[0].t.length + LATEST[0].x.length); } };
    if (opening && !opening.hidden) {
      draw(LATEST[0], 0); meta(LATEST[0], 0);
      document.addEventListener('teloscrivo:opened', start, { once: true });
    } else start();
  }

  $$('[data-slide]').forEach(button => button.addEventListener('click', () => $('.desk-phones').scrollBy({ left: Number(button.dataset.slide) * 147, behavior: reduced ? 'instant' : 'smooth' })));

  // ── pagina Cerca: legge cerca.json e filtra mentre scrivi ──
  const sp = $('[data-searchpage]');
  if (sp) {
    const input = $('input', sp), out = $('[data-results]', sp), root = sp.dataset.root;
    let DATA = null;
    const row = p => `<li><a href="${root}${p.u}"><span class="cap cat">${esc(p.s)} · ${esc(p.d)}</span><b>${esc(p.t)}</b><small>${esc(p.x)}</small></a></li>`;
    const show = () => {
      const raw = input.value.trim(), q = norm(raw);
      history.replaceState(null, '', q ? '?q=' + encodeURIComponent(raw) : location.pathname);
      if (!q) { out.innerHTML = '<span class="cap scount">Gli ultimi scritti</span><ul class="sres">' + DATA.slice(0, 4).map(row).join('') + '</ul>'; return; }
      const terms = q.split(/\s+/);
      const hits = DATA.filter(p => terms.every(t => p.h.includes(t)));
      out.innerHTML = hits.length
        ? `<span class="cap scount">${hits.length} ${hits.length === 1 ? 'risultato' : 'risultati'}</span><ul class="sres">${hits.map(row).join('')}</ul>`
        : `<p class="msg">Nessun risultato per «${esc(raw)}». Prova con una parola più semplice.</p>`;
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
        input.focus({ preventScroll: true });
      })
      .catch(err => { // errore visibile, niente finta "nessun risultato"
        out.innerHTML = '<p class="msg err">La ricerca non si e\' caricata (' + esc(err.message) + '). Riprova tra poco o torna alla home.</p>';
      });
  }
})();
