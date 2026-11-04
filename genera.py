#!/usr/bin/env python3
"""teloscrivo - generatore del sito statico.

Uso:   python3 genera.py
Legge: scritti/*.md  (uno per scritto, con intestazione tra due righe `---`)
Scrive: index.html, <sezione>/index.html (solo sezioni con almeno uno scritto), scritti/<slug>/index.html, cerca/index.html,
        404.html, cerca.json, sitemap.xml, robots.txt, .nojekyll

Nessuna dipendenza: solo libreria standard di Python 3.

Intestazione di uno scritto (tutto su una riga ciascuno):
    titolo:   obbligatorio
    data:     obbligatorio, AAAA-MM-GG
    sezione:  obbligatorio, una tra testi | poesie | racconti | canzoni
    estratto: facoltativo (se manca: prime righe per poesie/canzoni, prima frase per il resto)
    spotify:  facoltativo, link https:// (compare il bottone "Ascolta su Spotify")
Righe che iniziano con # nell'intestazione sono commenti.
Il corpo: righe = versi (poesie, canzoni); righe vuote = pausa/paragrafo.
"""
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

# ═══ IMPOSTAZIONI (l'URL base sta qui, in un posto solo) ═══
# Quando il dominio vero e' pronto, cambia solo questa riga e rilancia lo script.
BASE_URL = "https://tomas-coro.github.io/teloscrivo/"
SITE = "teloscrivo"
# Sezione TikTok: resta nascosta finche' TIKTOK_URL e' vuoto (il profilo non esiste ancora).
TIKTOK_URL = ""
# Profili social mostrati in fondo a ogni scritto ("Trovami su"): chiave = icona, valore = (link, nome mostrato). Per aggiungerne uno, serve anche l'icona in SOCIAL_ICONS.
SOCIAL = {"instagram": ("https://www.instagram.com/teloscrivo.it/", "@teloscrivo.it")}
TIKTOK_VIDEOS = []  # elenco di (titolo, sottotitolo, link al video), facoltativo

ROOT = Path(__file__).resolve().parent
BASE_PATH = urlparse(BASE_URL).path  # "/teloscrivo/" su GitHub Pages, "/" sul dominio vero

SECTIONS = {  # ordine = ordine nel menu
    "testi": ("Testi", "Testi", "Pensieri che non stanno in una frase."),
    "poesie": ("Poesie", "Poesie", "Poche righe, dette piano."),
    "racconti": ("Racconti brevi", "Racconti", "Storie brevi, da leggere in un respiro."),
    "canzoni": ("Dalle canzoni", "Canzoni", "Quello che ho scritto cantando sottovoce."),
}
LINE_SECTIONS = {"poesie", "canzoni"}  # qui ogni riga e' un verso
MONTHS_SHORT = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
MONTHS_LONG = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
               "settembre", "ottobre", "novembre", "dicembre"]
BAD_DASHES = (chr(0x2014), chr(0x2013))  # trattini lunghi "da AI": vietati nei testi (chr: l'hook dei trattini riscrive i letterali)

GLYPH = {
    "testi": '<path d="M6.5 3h7.5l4 4v13.5h-11.5z"/><path d="M14 3v4h4"/><path d="M9.5 12h6"/><path class="ac" d="M9.5 15.5h4"/>',
    "poesie": '<path d="M19.5 4.5c-6.5-.5-11 3-12 9.5L5 19.5l.8.7 3.2-1.8c6.4-1 10-5.5 10.5-12.9z"/><path class="ac" d="M8 17l7-7"/>',
    "racconti": '<path d="M3 6c3-1.2 6-.8 9 1.2 3-2 6-2.4 9-1.2v12c-3-1.2-6-.8-9 1.2-3-2-6-2.4-9-1.2z"/><path class="ac" d="M12 7.2v12"/>',
    "canzoni": '<circle cx="7" cy="17.5" r="2.5"/><circle cx="17" cy="15.5" r="2.5"/><path d="M9.5 17.5V6l10-2v11.5"/><path class="ac" d="M9.5 9l10-2"/>',
}
ARROW_CTA = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_BACK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M16 10H5M9 5l-5 5 5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_HOME = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3.5 9.5L10 4l6.5 5.5M5.5 8.5V16h9V8.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_SHARE = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 12.5V3M6.5 6.5L10 3l3.5 3.5M4.5 10v5.5a1.5 1.5 0 0 0 1.5 1.5h8a1.5 1.5 0 0 0 1.5-1.5V10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SOCIAL_ICONS = {
    "instagram": ("Instagram", '<rect x="3.2" y="3.2" width="17.6" height="17.6" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.1" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.15" fill="currentColor"/>'),
    "facebook": ("Facebook", '<path d="M13.6 21v-8h2.7l.5-3.2h-3.2V7.9c0-.9.4-1.7 1.8-1.7h1.5V3.4S15.6 3.2 14.4 3.2c-2.6 0-4.1 1.5-4.1 4.3v2.3H7.6V13h2.7v8z" fill="currentColor"/>'),
    "tiktok": ("TikTok", '<path d="M16.6 3c.3 2.4 1.7 3.9 4 4.1v3c-1.4.1-2.6-.3-4-1.1v6.2c0 3.9-3.2 6-6.3 5.4-2.6-.5-4.5-2.8-4.3-5.6.2-3.2 3.2-5.2 6.3-4.6v3.1c-1.5-.5-3.2.3-3.2 2 0 1.5 1.4 2.4 2.7 2 1-.3 1.6-1.2 1.6-2.3V3z" fill="currentColor"/>'),
}
ICON_DOWN = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M5 11l5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_UP = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 16V4M5 9l5-5 5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="6"/><path d="M13 13l5 5"/></svg>'
ICON_X = '<svg class="x" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 4l12 12M16 4L4 16"/></svg>'
ICON_EXT = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 14L14 6M7 6h7v7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


class SiteError(Exception):
    """Errore nei contenuti: si ferma tutto con un messaggio chiaro, niente correzioni silenziose."""


def esc(s):
    return html.escape(str(s), quote=True)


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


# ═══ LETTURA DEGLI SCRITTI ═══
class Post:
    def __init__(self, path):
        self.slug = path.stem
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", self.slug):
            raise SiteError(f"{path.name}: il nome del file deve essere minuscolo con trattini (es. luce-bassa.md)")
        text = path.read_text(encoding="utf-8")
        for ch in BAD_DASHES:
            if ch in text:
                line = text[: text.index(ch)].count("\n") + 1
                raise SiteError(f"{path.name}, riga {line}: trattino lungo (em/en dash). Usa il trattino normale '-'.")
        m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text.replace("\r\n", "\n"), flags=re.S)
        if not m:
            raise SiteError(f"{path.name}: manca l'intestazione tra due righe '---' all'inizio del file")
        meta = {}
        for n, line in enumerate(m.group(1).split("\n"), start=2):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if ":" not in line:
                raise SiteError(f"{path.name}, riga {n}: atteso 'chiave: valore', trovato '{line}'")
            k, v = line.split(":", 1)
            k = k.strip().lower()
            if k not in ("titolo", "data", "sezione", "estratto", "spotify"):
                raise SiteError(f"{path.name}, riga {n}: chiave sconosciuta '{k}'")
            meta[k] = v.strip()
        for k in ("titolo", "data", "sezione"):
            if not meta.get(k):
                raise SiteError(f"{path.name}: manca '{k}' nell'intestazione")
        self.title = meta["titolo"]
        try:
            self.date = date.fromisoformat(meta["data"])
        except ValueError:
            raise SiteError(f"{path.name}: data '{meta['data']}' non valida (usa AAAA-MM-GG)")
        self.cat = meta["sezione"]
        if self.cat not in SECTIONS:
            raise SiteError(f"{path.name}: sezione '{self.cat}' sconosciuta (ammesse: {', '.join(SECTIONS)})")
        self.spotify = meta.get("spotify", "")
        if self.spotify and not self.spotify.startswith("https://"):
            raise SiteError(f"{path.name}: il link spotify deve iniziare con https://")
        self.body = m.group(2).strip("\n")
        if not self.body.strip():
            raise SiteError(f"{path.name}: il testo e' vuoto")
        self.excerpt = meta.get("estratto") or self._default_excerpt()

    def _default_excerpt(self):
        first = self.body.strip().split("\n\n")[0].strip()
        if self.cat in LINE_SECTIONS:
            return "\n".join(first.split("\n")[:3])
        return re.split(r"(?<=[.!?])\s+", first)[0]  # solo . ! ? (i due punti non chiudono la frase)

    @property
    def flat(self):  # estratto su una riga sola
        return self.excerpt.replace("\n", " / ")

    @property
    def minutes(self):
        return max(1, round(len(self.body.split()) / 200))

    @property
    def url(self):  # relativo alla radice del sito
        return f"scritti/{self.slug}/"

    def short_date(self):
        return f"{self.date.day} {MONTHS_SHORT[self.date.month - 1]}"

    def long_date(self):
        return f"{self.date.day} {MONTHS_LONG[self.date.month - 1]}"

    def month_label(self):
        return f"{MONTHS_LONG[self.date.month - 1]} {self.date.year}"

    def body_html(self):
        """Il testo e' tutto nell'HTML. Ogni riga/frase e' un <span class=u>: il JS la fa comparire scorrendo."""
        if self.cat in LINE_SECTIONS:
            out, gap = [], False
            for line in self.body.split("\n"):
                if not line.strip():
                    gap = bool(out)
                    continue
                if gap:
                    out.append('<span class="gap"></span>')
                    gap = False
                out.append(f'<span class="u l">{esc(line.strip())}</span>')
            return "".join(out)
        paras = [p for p in re.split(r"\n\s*\n", self.body) if p.strip()]
        return "".join(
            "<p>" + "".join(f'<span class="u">{esc(s)} </span>' for s in re.split(r"(?<=[.!?:])\s+", " ".join(p.split()))) + "</p>"
            for p in paras
        )


def load_posts():
    files = sorted((ROOT / "scritti").glob("*.md"))
    if not files:
        raise SiteError("nessun file in scritti/*.md")
    posts = [Post(f) for f in files]
    posts.sort(key=lambda p: (p.date, p.title), reverse=True)  # dal piu' recente
    return posts


# ═══ PEZZI DI PAGINA ═══
def present_cats(posts):
    """Solo le sezioni che hanno almeno uno scritto (le altre non hanno pagina e non compaiono nei menu)."""
    return [k for k in SECTIONS if any(p.cat == k for p in posts)]


def nav_html(root, current=None):
    """Bottone Cerca. Sulla pagina Cerca diventa una X che torna dov'eri (senza JS porta alla home)."""
    lens = '<svg class="lens" viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="6"/><path d="M13 13l5 5"/></svg>'
    if current == "cerca":
        return (f'<a class="sbtn" href="{root}" data-search-close data-open aria-current="page" aria-label="Chiudi la ricerca">'
                f'<span class="ico">{lens}{ICON_X}</span><span class="lbl">Cerca</span></a>')
    return (f'<a class="sbtn" href="{root}cerca/" aria-label="Apri la ricerca">'
            f'<span class="ico">{lens}{ICON_X}</span><span class="lbl">Cerca</span></a>')


def head_html(root, title, desc, canon, og_type="website", jsonld=None, noindex=False):
    ld = ""
    for obj in jsonld or []:
        ld += '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    canon_tag = f'<link rel="canonical" href="{esc(canon)}">\n' if canon else ""
    og_url = f'<meta property="og:url" content="{esc(canon)}">\n' if canon else ""
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}{canon_tag}<meta name="theme-color" content="#072D59">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
{og_url}<meta property="og:image" content="{BASE_URL}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="teloscrivo, la luna porta consiglio">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preload" href="{root}assets/fonts/fibonacci.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="{root}style.css?v=4">
<script>document.documentElement.classList.add('js')</script>
{ld}</head>
"""


def top_html(root, current=None):
    return f"""<a class="skip" href="#contenuto">Vai al contenuto</a>
<div class="sky" aria-hidden="true"></div>
<header class="tbar">
  <a class="brand" href="{root}" aria-label="teloscrivo, torna alla home"><img src="{root}assets/logo/monogramma-navy.svg" alt="" width="34" height="34"></a>
  {nav_html(root, current)}
</header>
"""


def foot_html(root):
    return (f'<footer class="foot"><span class="wm2">{SITE}<span class="dot" aria-hidden="true"></span></span>'
            f'<span>© {date.today().year} {SITE}</span>'
            f'<a class="up" href="#inizio">Torna su{ICON_UP}</a></footer>')


def tail_html(root):
    return f'<script src="{root}app.js?v=3" defer></script>\n</body>\n</html>\n'


def icon(k):
    return f'<span class="ic ic-{k}"><svg viewBox="0 0 24 24" aria-hidden="true">{GLYPH[k]}</svg></span>'


def card_html(p, root):
    """Una scheda della griglia: il clic apre subito lo scritto (niente anteprima)."""
    return (f'<article class="desk-window" data-cat="{p.cat}"><div class="desk-bar"><i></i><i></i><i></i><span>{esc(p.slug)}.txt</span></div>'
            f'<a href="{root}{p.url}" data-card><span class="desk-photo" aria-hidden="true"></span>'
            f'<span class="desk-info"><span class="desk-meta"><b>{esc(SECTIONS[p.cat][0])}</b>{p.long_date()}</span>'
            f'<span class="desk-title">{esc(p.title)}</span><span class="desk-excerpt">{esc(p.excerpt).replace(chr(10), " ")}</span>'
            f'<span class="desk-more">Apri lo scritto ↗</span></span></a></article>')


# ═══ PAGINE ═══
def page_home(posts):
    root = ""
    newest = posts[0]
    latest = [{"t": p.title, "k": SECTIONS[p.cat][0], "d": p.short_date(), "x": p.excerpt, "u": p.url} for p in posts[:5]]
    first = latest[0]
    windows = "".join(card_html(p, root) for p in posts)
    tiktok = ""
    if TIKTOK_VIDEOS:
        cards = "".join(f'<a class="desk-phone" href="{esc(u)}" target="_blank" rel="noopener noreferrer"><span class="desk-screen">teloscrivo <span>{esc(t)}<small>{esc(s)}</small></span></span></a>' for t, s, u in TIKTOK_VIDEOS)
        tiktok = (f'<section class="desk-videos" aria-labelledby="h-tk"><div class="desk-slider-top"><h2 id="h-tk">Le parole, in video</h2>'
                  f'<div class="desk-arrows"><button type="button" data-slide="-1" aria-label="Video precedenti">←</button><button type="button" data-slide="1" aria-label="Video successivi">→</button></div></div>'
                  f'<p>Le poesie e i testi, letti a voce.</p><div class="desk-phones">{cards}</div></section>')
    desc = "Poesie, testi, racconti brevi e testi di canzoni, da leggere scorrendo. La luna porta consiglio."
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE_URL, "inLanguage": "it", "description": desc}]
    latest_json = json.dumps(latest, ensure_ascii=False).replace("</", "<\\/")
    body = f"""<body id="inizio">
<div class="opening" data-opening role="dialog" aria-modal="true" aria-label="Apertura di teloscrivo" tabindex="-1" hidden>
  <div class="opening-window">
    <div class="opening-bar"><i></i><i></i><button type="button" class="opening-max" data-opening-max aria-label="Apri a schermo intero"></button></div>
    <div class="opening-content"><p class="opening-sign">teloscrivo<span>.</span></p><p class="opening-sub">la luna porta consiglio</p></div>
    <svg class="opening-pointer" viewBox="0 0 24 28" aria-hidden="true"><path d="M2 2v21l5-5 4 8 4-2-4-8 8-1z" fill="#DBF2FC" stroke="#072D59" stroke-width="2"/></svg>
  </div>
  <button type="button" class="opening-skip" data-opening-skip>Salta l'apertura</button>
</div>
{top_html(root)}<main id="contenuto" class="page"><div class="wrapin">
  <section class="hero">
    <div class="hero-l">
      <h1 class="hero-h">{SITE}<span class="dot" aria-hidden="true"></span></h1>
      <p class="hero-sub">la luna porta consiglio</p>
      <p class="hero-rule"><span class="cap">Ultimo scritto il {newest.long_date()} · {plural(len(posts), "scritto", "scritti")}</span></p>
    </div>
    <article class="last">
      <div class="wbar"><span class="wd" aria-hidden="true"><i></i><i></i><i></i></span><p class="cap lk"><span data-lk>Ultimo scritto · {SECTIONS[newest.cat][0]} · {newest.short_date()}</span></p><span aria-hidden="true"></span></div>
      <div class="wbody"><p class="lt" data-lt>{esc(first["t"])}</p><p class="lx" data-lx>{esc(first["x"]).replace(chr(10), "<br>")}</p></div>
      <div class="lf"><div class="last-controls"><div class="pg" data-pg role="group" aria-label="Ultimi scritti"></div><button class="pause" data-pause type="button" aria-label="Metti in pausa gli ultimi scritti" hidden>❚❚</button></div><a class="cta" data-cta href="{first["u"]}">Leggi{ARROW_CTA}</a></div>
    </article>
  </section>
  <section class="desk-section" aria-labelledby="h-all"><div class="sec-h"><h2 id="h-all">Gli scritti</h2><span class="cap count">{plural(len(posts), "scritto", "scritti")}</span></div><p>Una finestra per ogni scritto: aprila per leggere.</p>
    <div class="desk-shelf">{windows}</div>
  </section>
  {tiktok}
  {foot_html(root)}
</div></main>
<script type="application/json" id="latest">{latest_json}</script>
{tail_html(root)}"""
    return head_html(root, f"{SITE} · poesie, testi e racconti brevi", desc, BASE_URL, jsonld=ld) + body


def page_section(k, posts):
    root = "../"
    name, _, opening = SECTIONS[k]
    items = [p for p in posts if p.cat == k]
    desc = f"{opening} {plural(len(items), 'scritto', 'scritti')} in {name.lower()}."
    canon = f"{BASE_URL}{k}/"
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": f"{name} | {SITE}", "url": canon, "inLanguage": "it", "description": desc}]
    cards = "".join(card_html(p, root) for p in items)
    body = f"""<body class="reader swipe" id="inizio" data-cat="{k}">
<a class="skip" href="#contenuto">Vai al contenuto</a>
<div class="sky" aria-hidden="true"></div>
<header class="rbar"><div class="rbtns"><a class="rbtn rbtn-home" data-home="categoria" href="{root}" aria-label="Torna alla home" hidden>{ICON_HOME}<span>Home</span></a><a class="rbtn" data-rback href="{root}">{ICON_BACK}Indietro</a></div></header>
<main id="contenuto" class="page"><div class="wrapin">
  <header class="phead"><span class="cap">Categoria</span><h1>{name}</h1><p>{opening}</p></header>
  <p class="cap sec-n">{plural(len(items), "scritto", "scritti")}</p>
  <div class="desk-shelf">{cards}</div>
  {foot_html(root)}
</div></main>
{tail_html(root)}"""
    return head_html(root, f"{name} | {SITE}", desc, canon, jsonld=ld) + body


def page_reader(p, posts):
    root = "../../"
    name = SECTIONS[p.cat][0]
    rel = [x for x in posts if x is not p and x.cat == p.cat] + [x for x in posts if x is not p and x.cat != p.cat]
    rel_html = "".join(
        f'<a class="rcard" data-cat="{x.cat}" href="{root}{x.url}"><span class="desk-photo" aria-hidden="true"></span>'
        f'<span class="rcb"><span class="rcm"><b>{esc(SECTIONS[x.cat][0])}</b>{x.short_date()}</span>'
        f'<span class="rct">{esc(x.title)}</span><span class="rcx">{esc(x.excerpt).replace(chr(10), " ")}</span>'
        f'<span class="rcgo">Leggi{ARROW_CTA}</span></span></a>'
        for x in rel[:2]
    )
    soc = "".join(
        f'<a class="soc-a" href="{esc(url)}" target="_blank" rel="noopener noreferrer" aria-label="{SOCIAL_ICONS[k][0]}: {esc(label)}">'
        f'<svg viewBox="0 0 24 24" aria-hidden="true">{SOCIAL_ICONS[k][1]}</svg><span>{esc(label)}</span></a>'
        for k, (url, label) in SOCIAL.items() if url
    )
    find_html = f'<div class="rfind"><span class="wm2 wm-find">scrivoanchesu<span class="dot" aria-hidden="true"></span></span><div class="soc">{soc}</div></div>' if soc else ""
    spotify = (f'<a class="cta" href="{esc(p.spotify)}" target="_blank" rel="noopener">Ascolta su Spotify{ICON_EXT}</a>' if p.spotify else "")
    canon = f"{BASE_URL}{p.url}"
    desc = p.flat[:155]
    ld = [{
        "@context": "https://schema.org", "@type": "Article", "headline": p.title, "inLanguage": "it",
        "datePublished": p.date.isoformat(), "dateModified": p.date.isoformat(), "articleSection": name,
        "author": {"@type": "Person", "name": SITE}, "publisher": {"@type": "Organization", "name": SITE},
        "mainEntityOfPage": canon, "url": canon, "image": f"{BASE_URL}og.png", "description": desc,
    }]
    chip = (f'<a class="catchip" href="{root}{p.cat}/" aria-label="Tutti gli scritti: {esc(name)}">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true">{GLYPH[p.cat]}</svg>{esc(name)}</a>')
    links = "".join(f'<a href="{root}{k}/">{esc(SECTIONS[k][1])}</a>' for k in present_cats(posts))
    body = f"""<body class="reader swipe" id="inizio" data-cat="{p.cat}">
<a class="skip" href="#contenuto">Vai al testo</a>
<div class="sky" aria-hidden="true"></div>
<div class="rprog" aria-hidden="true"></div>
<header class="rbar"><div class="rbtns"><a class="rbtn rbtn-home" data-home="scritto" href="{root}" aria-label="Torna alla home">{ICON_HOME}<span>Home</span></a><a class="rbtn" data-rback href="{root}{p.cat}/">{ICON_BACK}Indietro</a></div></header>
<main id="contenuto" class="rsc"><article class="rart">
  <header class="rhead"><span class="rphoto" aria-hidden="true"></span><div class="rcard-b"><div class="metarow">{chip}<span class="cap">{p.short_date()} · {p.minutes} min</span></div><h1 class="rt">{esc(p.title)}</h1></div></header>
  <div class="rbody">{p.body_html()}</div>
  <footer class="rend"><span class="cap">Leggi anche</span><div class="rcards">{rel_html}</div>{spotify}
    <div class="rfoot"><button type="button" class="sharebtn" data-share hidden>{ICON_SHARE}<span data-share-lbl>Condividi</span></button>{find_html}</div>
  </footer>
</article></main>
{tail_html(root)}"""
    return head_html(root, f"{p.title} | {SITE}", desc, canon, og_type="article", jsonld=ld) + body


def page_search():
    root = "../"
    canon = f"{BASE_URL}cerca/"
    desc = "Cerca tra poesie, testi e racconti brevi di teloscrivo."
    body = f"""<body id="inizio">
{top_html(root, "cerca")}<main id="contenuto" class="page"><div class="wrapin">
  <h1 class="sr">Cerca</h1>
  <div class="srch-in" data-searchpage data-root="{root}">
    <label class="sfield"><span class="sr">Cerca tra i testi</span>{ICON_SEARCH}<input type="search" placeholder="Un titolo, una parola, un verso" autocomplete="off" enterkeyhint="search" disabled></label>
    <div data-results aria-live="polite"><noscript><p class="msg">La ricerca ha bisogno di JavaScript. Puoi comunque sfogliare le sezioni dalla home.</p></noscript></div>
  </div>
  {foot_html(root)}
</div></main>
{tail_html(root)}"""
    return head_html(root, f"Cerca | {SITE}", desc, canon) + body


def page_404():
    root = BASE_PATH  # pagina servita a qualsiasi indirizzo: i link devono partire dalla radice
    body = f"""<body id="inizio">
{top_html(root)}<main id="contenuto" class="page"><div class="wrapin nf">
  <h1>Pagina non trovata</h1>
  <p>Questo indirizzo non esiste, o lo scritto è stato spostato.</p>
  <p><a class="cta" href="{root}">Torna alla home{ARROW_CTA}</a></p>
</div></main>
{tail_html(root)}"""
    return head_html(root, f"Pagina non trovata | {SITE}", "Questa pagina non esiste.", None, noindex=True) + body


def sitemap(posts):
    urls = [(BASE_URL, posts[0].date)]
    urls += [(f"{BASE_URL}{k}/", max([p.date for p in posts if p.cat == k] or [posts[0].date])) for k in present_cats(posts)]
    urls.append((f"{BASE_URL}cerca/", posts[0].date))
    urls += [(f"{BASE_URL}{p.url}", p.date) for p in posts]
    rows = "".join(f"  <url><loc>{esc(u)}</loc><lastmod>{d.isoformat()}</lastmod></url>\n" for u, d in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'


def search_index(posts):
    return json.dumps([
        {"t": p.title, "s": SECTIONS[p.cat][0], "d": p.short_date(), "x": p.flat, "b": " ".join(p.body.split()), "u": p.url}
        for p in posts
    ], ensure_ascii=False, separators=(",", ":"))


# ═══ SCRITTURA E CONTROLLI ═══
written = []


def write(rel, content):
    if any(ch in content for ch in BAD_DASHES):
        raise SiteError(f"{rel}: contiene un trattino lungo (em/en dash)")
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    written.append(rel)


def check_links():
    """Ogni href/src interno delle pagine generate deve puntare a un file o a una cartella con index.html."""
    broken = []
    for rel in written:
        if not rel.endswith(".html"):
            continue
        src = (ROOT / rel).read_text(encoding="utf-8")
        for url in re.findall(r'(?:href|src)="([^"]+)"', src):
            if re.match(r"(https?:|mailto:|tel:|data:|#)", url):
                continue
            url = url.split("#")[0].split("?")[0]
            if not url:
                continue
            if url.startswith("/"):  # la 404 usa link dalla radice del sito (/teloscrivo/...)
                target = ROOT / url[len(BASE_PATH):] if url.startswith(BASE_PATH) else None
            else:
                target = (ROOT / rel).parent / url
            if target is None or not (target.is_file() or (target.is_dir() and (target / "index.html").is_file())):
                broken.append(f"{rel} -> {url}")
    if broken:
        raise SiteError("link interni rotti:\n  " + "\n  ".join(broken))


def main():
    posts = load_posts()
    slugs = {p.slug for p in posts}
    # niente pagine orfane: se un file .md e' stato tolto, sparisce anche la sua pagina generata
    for d in (ROOT / "scritti").iterdir():
        if d.is_dir() and d.name not in slugs and (d / "index.html").is_file():
            shutil.rmtree(d)
            print(f"  rimossa pagina orfana: scritti/{d.name}/")
    write("index.html", page_home(posts))
    live = present_cats(posts)
    for k in SECTIONS:  # una sezione senza scritti non ha pagina: se ce n'era una vecchia, sparisce solo il suo index.html generato
        stale = ROOT / k / "index.html"
        if k not in live and stale.is_file():
            stale.unlink()
            print(f"  rimossa pagina di sezione vuota: {k}/index.html")
    for k in live:
        write(f"{k}/index.html", page_section(k, posts))
    for p in posts:
        write(f"scritti/{p.slug}/index.html", page_reader(p, posts))
    write("cerca/index.html", page_search())
    write("404.html", page_404())
    write("cerca.json", search_index(posts))
    write("sitemap.xml", sitemap(posts))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n")
    write(".nojekyll", "")
    check_links()
    n_html = sum(1 for w in written if w.endswith(".html"))
    print(f"OK: {len(posts)} pagine scritto, {len(live)} pagine sezione, cerca, 404, home ({n_html} pagine HTML), "
          f"cerca.json, sitemap.xml, robots.txt. Link interni controllati. URL base: {BASE_URL}")


if __name__ == "__main__":
    try:
        main()
    except SiteError as e:
        print(f"ERRORE: {e}", file=sys.stderr)
        sys.exit(1)
