#!/usr/bin/env python3
"""Immagini di anteprima (Open Graph, 1200x630) del sito.

Cosa scrive:
  og.jpg                 la home (finestra coi tre pallini, direzione B del mockup 47)
  assets/og/<slug>.jpg   una per ogni scritto (foto con velatura blu, titolo grande, firma)

Come: disegna ogni immagine come una pagina HTML e la fotografa con un browser Chromium in modalita' headless
(Brave, Chrome o Chromium: lo cerca da solo). Cosi' i font sono quelli veri del sito (Instrument Serif, Poppins).
Va lanciato a mano dopo `python3 genera.py` quando cambia un titolo, una categoria o una foto:
    python3 genera_og.py
Se manca il browser o uno scatto fallisce, si ferma con un errore chiaro: niente immagini finte.
"""
import html
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import genera
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "assets" / "og"
W, H = 1200, 630
JPEG_QUALITY = 84  # sotto i ~300 KB: WhatsApp scarta le anteprime piu' pesanti

BROWSERS = [
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "brave", "brave-browser", "google-chrome", "chromium", "chrome",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

MOON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.2A8.4 8.4 0 0 1 9.8 4a8.6 8.6 0 1 0 10.2 10.2Z" fill="currentColor"/></svg>'

# i font del sito, con percorsi relativi alla cartella temporanea (_og_tmp/ dentro il progetto)
CSS = """
@font-face{font-family:"Instrument Serif";src:url(../assets/fonts/instrumentserif-400.woff2) format("woff2");font-weight:400;font-style:normal}
@font-face{font-family:"Instrument Serif";src:url(../assets/fonts/instrumentserif-italic.woff2) format("woff2");font-weight:400;font-style:italic}
@font-face{font-family:Poppins;src:url(../assets/fonts/poppins-400.woff2) format("woff2");font-weight:400}
@font-face{font-family:Poppins;src:url(../assets/fonts/poppins-500.woff2) format("woff2");font-weight:500}
*{box-sizing:border-box}html,body{margin:0;width:1200px;height:630px;overflow:hidden;background:#072D59}
.og{position:relative;width:1200px;height:630px;overflow:hidden;background:#072D59;color:#DBF2FC;font-family:"Instrument Serif",serif}
.sig{display:flex;align-items:baseline;font:400 44px/1 "Instrument Serif",serif;color:#DBF2FC}
.sig i{width:11px;height:11px;border-radius:50%;background:#FD6E88;margin-left:5px;display:inline-block}
/* home: finestra coi tre pallini su una foto sfocata e scura */
.hB .bg{position:absolute;inset:-30px;width:calc(100% + 60px);height:calc(100% + 60px);object-fit:cover;filter:blur(10px)}
.hB::before{content:"";position:absolute;inset:0;background:#071c3bd9}
.hB .win{position:absolute;left:130px;right:130px;top:105px;bottom:105px;border:2px solid #DBF2FC40;border-radius:26px;background:#072D59e6;overflow:hidden;display:flex;flex-direction:column}
.hB .wb{height:68px;border-bottom:2px solid #DBF2FC30;background:#DBF2FC14;display:flex;align-items:center;gap:12px;padding:0 30px;flex:none}
.hB .wb i{width:20px;height:20px;border-radius:50%;background:#DBF2FC40}.hB .wb i:first-child{background:#FD6E88}
.hB .wc{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 64px;gap:22px}
.hB h1{margin:0;font:400 150px/1 "Instrument Serif",serif;white-space:nowrap}
.hB h1 i{display:inline-block;width:24px;height:24px;border-radius:50%;background:#FD6E88;margin-left:6px}
.hB .tag{margin:0;display:flex;align-items:center;gap:16px;font:italic 400 46px/1 "Instrument Serif",serif;color:#DBF2FCd9}
.hB .tag svg{width:38px;height:38px;color:#FD6E88}
/* scritto: foto a tutta immagine con la stessa velatura blu della card in home */
.post .ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.post::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(to right,#071c3bf2 0%,#071c3bcc 45%,#071c3b66 100%),linear-gradient(to top,#071c3bf5 0%,#071c3b00 55%)}
.post>*:not(.ph){z-index:2}
.post .cat{position:absolute;left:92px;top:80px;margin:0;font:500 30px/1 Poppins,sans-serif;letter-spacing:.04em;color:#DBF2FC}
.post .cat b{color:#FD6E88;font-weight:500}
.post .ti{position:absolute;left:92px;right:300px;bottom:150px;margin:0;font:400 116px/1.02 "Instrument Serif",serif;text-wrap:balance;text-shadow:0 4px 40px #071c3b}
.post .sig{position:absolute;left:92px;bottom:64px}
.post .dt{position:absolute;right:92px;bottom:64px;font:400 28px/1 Poppins,sans-serif;color:#DBF2FCb3}
"""


class OgError(Exception):
    pass


def find_browser():
    for b in BROWSERS:
        found = shutil.which(b) or (b if Path(b).is_file() else None)
        if found:
            return found
    raise OgError("non trovo un browser Chromium (Brave, Chrome o Chromium). Installane uno o aggiungi il percorso in BROWSERS.")


def page(body):
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def best_photo(slug):
    """La foto piu' grande gia' filtrata da genera.py (assets/foto/<slug>-<larghezza>.webp)."""
    files = sorted((ROOT / "assets" / "foto").glob(f"{slug}-*.webp"), key=lambda f: int(f.stem.rsplit("-", 1)[1]))
    return files[-1] if files else None


def home_html():
    photo = best_photo("che-se-sparisci")
    bg = f'<img class="bg" src="../assets/foto/{photo.name}" alt="">' if photo else ""
    return page(f'<div class="og hB">{bg}<div class="win"><div class="wb"><i></i><i></i><i></i></div>'
                f'<div class="wc"><h1>teloscrivo<i></i></h1><p class="tag">la luna porta consiglio{MOON}</p></div></div></div>')


def post_html(p):
    photo = best_photo(p.slug)
    ph = f'<img class="ph" src="../assets/foto/{photo.name}" alt="">' if photo else ""
    return page(f'<div class="og post">{ph}<p class="cat">{html.escape(p.bar_label)}</p>'
                f'<h2 class="ti">{html.escape(p.title)}</h2><div class="sig">{genera.SITE}<i></i></div>'
                f'<span class="dt">{p.long_date()}</span></div>')


def shoot(browser, tmp, name, doc, out):
    """Scrive la pagina, la fotografa a 1200x630 e salva un JPEG leggero."""
    src = tmp / f"{name}.html"
    shot = tmp / f"{name}.png"
    src.write_text(doc, encoding="utf-8")
    cmd = [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
           f"--window-size={W},{H + 200}", "--virtual-time-budget=5000", f"--screenshot={shot}", src.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if not shot.is_file():
        raise OgError(f"{name}: il browser non ha prodotto lo scatto.\n{r.stderr[-400:]}")
    img = Image.open(shot).convert("RGB")
    if img.width < W or img.height < H:
        raise OgError(f"{name}: scatto troppo piccolo ({img.width}x{img.height}, servono {W}x{H}).")
    img = img.crop((0, 0, W, H))  # la finestra e' piu' alta di proposito: si taglia sul bordo alto, mai sul contenuto
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    kb = out.stat().st_size / 1024
    if kb > 300:
        print(f"  attenzione: {out.name} pesa {kb:.0f} KB (oltre 300 KB WhatsApp potrebbe non mostrarla)")
    return kb


def main():
    browser = find_browser()
    posts = genera.load_posts()
    tmp = ROOT / "_og_tmp"  # dentro il progetto cosi' i percorsi ../assets/ funzionano; si cancella a fine lavoro
    tmp.mkdir(exist_ok=True)
    try:
        kb = shoot(browser, tmp, "home", home_html(), ROOT / "og.jpg")
        print(f"og.jpg ({kb:.0f} KB)")
        for p in posts:
            kb = shoot(browser, tmp, p.slug, post_html(p), OUT_DIR / f"{p.slug}.jpg")
            print(f"assets/og/{p.slug}.jpg ({kb:.0f} KB)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"Fatto: 1 home + {len(posts)} scritti. Ora rilancia: python3 genera.py")


if __name__ == "__main__":
    try:
        main()
    except (OgError, subprocess.TimeoutExpired) as e:
        sys.exit(f"ERRORE: {e}")
