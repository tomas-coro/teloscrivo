#!/usr/bin/env python3
"""teloscrivo - generatore del sito statico.

Uso:   python3 genera.py
Legge: scritti/*.md  (uno per scritto, con intestazione tra due righe `---`)
Scrive: index.html, <sezione>/index.html, scritti/<slug>/index.html, cerca/index.html,
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
ARROW = '<svg class="ar" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg>'
ARROW_CTA = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_BACK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M16 10H5M9 5l-5 5 5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_DOWN = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M5 11l5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_UP = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 16V4M5 9l5-5 5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="6"/><path d="M13 13l5 5"/></svg>'
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
def nav_html(root, current=None):
    links = "".join(
        f'<a href="{root}{k}/"{" aria-current=\"page\"" if k == current else ""}>{short}</a>'
        for k, (_, short, _) in SECTIONS.items()
    )
    cur = ' aria-current="page"' if current == "cerca" else ""
    return (f'<nav class="mn" aria-label="Sezioni">{links}'
            f'<a href="{root}cerca/" data-search aria-label="Cerca"{cur}>{ICON_SEARCH}<span>Cerca</span></a></nav>')


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
<link rel="stylesheet" href="{root}style.css">
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
    return f'<script src="{root}app.js" defer></script>\n</body>\n</html>\n'


def icon(k):
    return f'<span class="ic ic-{k}"><svg viewBox="0 0 24 24" aria-hidden="true">{GLYPH[k]}</svg></span>'


def entries_html(posts, root, newest=None, heading="h3"):
    """Elenco raggruppato per mese."""
    groups = {}
    for p in posts:
        groups.setdefault(p.month_label(), []).append(p)
    out = []
    for month, items in groups.items():
        lis = "".join(
            f'<li data-cat="{p.cat}"><a class="entry" href="{root}{p.url}">'
            f'<span class="ed">{p.short_date()}</span>'
            f'<b class="et">{esc(p.title)}{"<em class=\"nw\">nuovo</em>" if p is newest else ""}</b>'
            f'<span class="ec">{SECTIONS[p.cat][1]}</span><span class="rx">{esc(p.flat)}</span>{ARROW}</a></li>'
            for p in items
        )
        out.append(f'<section class="mg" aria-label="{esc(month)}"><{heading} class="mh">{esc(month)}</{heading}><ul>{lis}</ul></section>')
    return "".join(out)


# ═══ PAGINE ═══
def page_home(posts):
    root = ""
    newest = posts[0]
    by_cat = {k: [p for p in posts if p.cat == k] for k in SECTIONS}
    latest = [{"t": p.title, "k": SECTIONS[p.cat][0], "d": p.short_date(), "x": p.excerpt, "u": p.url} for p in posts[:5]]
    first = latest[0]
    pick = ""
    for k, (name, _, opening) in SECTIONS.items():
        items = by_cat[k]
        ultimo = f'<span class="pl pu">Ultimo: <i>{esc(items[0].title)}</i></span>' if items else ""
        pick += (f'<a class="pk" href="{k}/">{icon(k)}<b>{name}</b><span class="pl">{opening}</span>{ultimo}'
                 f'<span class="cap">{plural(len(items), "scritto", "scritti")}</span></a>')
    chips = f'<button type="button" data-cat="" aria-pressed="true">Tutti<small>{len(posts)}</small></button>' + "".join(
        f'<button type="button" data-cat="{k}" aria-pressed="false">{short}<small>{len(by_cat[k])}</small></button>'
        for k, (_, short, _) in SECTIONS.items()
    )
    names = json.dumps({k: v[0] for k, v in SECTIONS.items()}, ensure_ascii=False)
    tiktok = ""
    if TIKTOK_URL:
        cards = "".join(f'<a class="tk" href="{esc(u)}" target="_blank" rel="noopener"><b>{esc(t)}<br><small>{esc(s)}</small></b></a>' for t, s, u in TIKTOK_VIDEOS)
        tiktok = (f'<section class="sec" aria-labelledby="h-tk"><div class="sh"><span class="sn">03</span><h2 class="st" id="h-tk">Su TikTok</h2></div>'
                  f'<div class="tks"><div class="tkintro"><p>Le poesie e i testi, letti a voce.</p>'
                  f'<a class="cta" href="{esc(TIKTOK_URL)}" target="_blank" rel="noopener">Seguimi su TikTok{ICON_EXT}</a></div>'
                  f'<div class="tkrow">{cards}</div></div></section>')
    desc = "Poesie, testi, racconti brevi e testi di canzoni, da leggere scorrendo. La luna porta consiglio."
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE_URL, "inLanguage": "it", "description": desc}]
    latest_json = json.dumps(latest, ensure_ascii=False).replace("</", "<\\/")
    body = f"""<body id="inizio">
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
  <section class="sec" aria-labelledby="h-pick"><div class="sh"><span class="sn">01</span><h2 class="st" id="h-pick">Scegli cosa leggere</h2></div><div class="pick">{pick}</div></section>
  <section class="sec" aria-labelledby="h-all"><div class="sh"><span class="sn">02</span><h2 class="st" id="h-all" data-lh>Tutti gli scritti</h2><span class="cap" data-lc>{plural(len(posts), "scritto", "scritti")}</span></div>
    <div class="chips2" data-chips data-names='{esc(names)}' role="group" aria-label="Filtra per sezione" hidden>{chips}</div>
    {entries_html(posts, root, newest=newest)}
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
    listing = entries_html(items, root, heading="h2") if items else '<p class="msg">Qui non c\'e\' ancora niente. Torna presto.</p>'
    body = f"""<body id="inizio" data-cat="{k}">
{top_html(root, k)}<main id="contenuto" class="page"><div class="wrapin">
  <header class="phead"><span class="cap">Sezione</span><h1>{name}</h1><p>{opening}</p></header>
  <p class="cap" style="margin:18px 0 0">{plural(len(items), "scritto", "scritti")}</p>
  {listing}
  {foot_html(root)}
</div></main>
{tail_html(root)}"""
    return head_html(root, f"{name} | {SITE}", desc, canon, jsonld=ld) + body


def page_reader(p, posts):
    root = "../../"
    name = SECTIONS[p.cat][0]
    rel = [x for x in posts if x is not p and x.cat == p.cat] + [x for x in posts if x is not p and x.cat != p.cat]
    rel_html = "".join(
        f'<a class="ra" href="{root}{x.url}"><b>{esc(x.title)}</b><small>{SECTIONS[x.cat][1]} · {x.short_date()}</small></a>'
        for x in rel[:2]
    )
    spotify = (f'<a class="cta" href="{esc(p.spotify)}" target="_blank" rel="noopener">Ascolta su Spotify{ICON_EXT}</a>' if p.spotify else "")
    canon = f"{BASE_URL}{p.url}"
    desc = p.flat[:155]
    ld = [{
        "@context": "https://schema.org", "@type": "Article", "headline": p.title, "inLanguage": "it",
        "datePublished": p.date.isoformat(), "dateModified": p.date.isoformat(), "articleSection": name,
        "author": {"@type": "Person", "name": SITE}, "publisher": {"@type": "Organization", "name": SITE},
        "mainEntityOfPage": canon, "url": canon, "image": f"{BASE_URL}og.png", "description": desc,
    }]
    body = f"""<body class="reader" id="inizio" data-cat="{p.cat}">
<a class="skip" href="#contenuto">Vai al testo</a>
<div class="sky" aria-hidden="true"></div>
<div class="rprog" aria-hidden="true"></div>
<header class="rbar"><a class="rbtn" data-rback href="{root}{p.cat}/">{ICON_BACK}Indietro</a><span class="cap">{name}</span><button type="button" class="rbtn" data-share hidden>Condividi</button></header>
<main id="contenuto" class="rsc"><article class="rart">
  <header class="rhead"><p class="cap">{name} · {p.short_date()} · {p.minutes} min</p><h1 class="rt">{esc(p.title)}</h1><p class="cue" data-cue aria-hidden="true"><span>Scorri per leggere</span>{ICON_DOWN}</p></header>
  <div class="rbody">{p.body_html()}</div>
  <footer class="rend"><span class="cap">Leggi anche</span>{rel_html}{spotify}
    <div class="sh2"><button type="button" class="rbtn" data-share hidden>Condividi</button><a class="rbtn" href="{root}">Torna alla home</a></div>
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
  <header class="phead"><span class="cap">Cerca</span><h1>Cerca</h1><p>Un titolo, una parola, un verso.</p></header>
  <div data-searchpage data-root="{root}">
    <label class="qbox"><span class="sr">Cerca tra i testi</span>{ICON_SEARCH}<input type="search" placeholder="Cerca tra i testi" autocomplete="off" disabled></label>
    <div data-results aria-live="polite"><noscript><p class="msg">La ricerca ha bisogno di JavaScript. Puoi comunque sfogliare le sezioni dal menu.</p></noscript></div>
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
    urls += [(f"{BASE_URL}{k}/", max([p.date for p in posts if p.cat == k] or [posts[0].date])) for k in SECTIONS]
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
    for k in SECTIONS:
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
    print(f"OK: {len(posts)} pagine scritto, {len(SECTIONS)} pagine sezione, cerca, 404, home ({n_html} pagine HTML), "
          f"cerca.json, sitemap.xml, robots.txt. Link interni controllati. URL base: {BASE_URL}")


if __name__ == "__main__":
    try:
        main()
    except SiteError as e:
        print(f"ERRORE: {e}", file=sys.stderr)
        sys.exit(1)
