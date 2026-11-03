# Blog "teloscrivo" - stato del progetto

> Riprendi da qui dopo un /clear. RIPARTENZA DA ZERO: 03/11/2026.

## Dove sta il progetto (dal 03/11/2026)
- Cartella ufficiale: `LANDING EVOLUTION/clienti/teloscrivo/` (la vecchia `PROGETTI AI/BLOG/` e' solo una copia di partenza).
- Mockup attivo: `mockup/04-scrivania-v4.html` (unico attivo). Gli altri stanno in `_archivio/` (`mockup-scrivania/` = 01-03, `vecchio-scartato/` = lavoro scartato). Logo e font in `assets/`.
- I percorsi nel testo sotto che dicono `mockups/` o `_asset-marca/` e `_archivio-vecchio/` vanno letti come `mockup/`, `assets/` e `_archivio/vecchio-scartato/`.

## Ripartenza
- Tomas ha scartato tutto il lavoro precedente (mockup 01-18, intro luna, direzioni A/B/C). Archiviato in `_archivio-vecchio/` (NON usarlo come base visiva; storia completa in `_archivio-vecchio/PROGETTO-vecchio.md`).
- Si riparte dal brief, con /grill-me da zero: chi legge, come ti trova, cosa deve sentire, struttura. Poi mockup.

## Brief deciso (grill-me, blocchi 1-2, 03/11/2026)
- **Lettori**: persone nuove, si parte da zero. Arrivano da link in bio TikTok/Instagram, passaparola e **SEO** (canale principale: una pagina vera per ogni post, titolo e testo reali, niente testo in immagini).
- **Scopo**: casa per scrivere, testi che restano nel tempo. Non portfolio per clienti.
- **Sensazione**: intimità e comfort, "come il computer di chi legge", a casa. Solo sensazione + tocchi leggeri (categorie come cartelle), NON un finto desktop con finestre.
- **Identità**: si firma solo "teloscrivo", una riga di presentazione, niente pagina "Chi sono" lunga.
- **Home**: una riga su cosa è, ultimi post, 4 categorie. Niente intro lunghe/animazioni d'ingresso.
- **Post**: colonna stretta, testo grande, tema chiaro (Seal Blue, default) o scuro (Navy) scelto dal lettore.
- **Lancio**: almeno 8-10 post (2-3 per categoria), poi 1 a settimana.
- **Funzioni**: solo ricerca e condividi. No commenti. Newsletter dopo il lancio.

## Brief deciso (blocco 3, 03/11/2026)
- **Pubblicazione**: un file Markdown per post + script che genera l'HTML. Niente pannello admin (la via più semplice e veloce).
- **Hosting**: dominio proprio su **Plesk** (NON GitHub Pages). Nome dominio e metodo di upload (SFTP/Git) ancora da chiarire.
- **Font**: Fibonacci per titoli/logo, Poppins per i post, Roboto Condensed per date/etichette. Vetro e Balligesta esclusi.
- **Dalle canzoni**: testo scritto + bottone "Ascolta su Spotify". **TikTok**: sezione con card-link, nascosta finché il profilo non esiste.
- **Fine post**: 2 "leggi anche" della stessa categoria + condividi. Niente popup/iscrizioni.

## Brief deciso (blocco 4, 03/11/2026)
- **Dominio**: `teloscrivo.it`. **Hosting**: da valutare (Plesk o GitHub Pages): si costruisce una cartella statica valida per entrambi.
- **Aspetto**: chiaro = carta/quaderno (fondo Seal Blue, testo Navy, rosa solo per link e dettagli); scuro = lume di lampada (fondo Navy, testo Seal Blue).
- **Logo**: piccolo in intestazione accanto al nome, mai gigante in home.
- **No**: gradienti, ombre pesanti, icone generiche, banner cookie invadenti.

## Direzione scelta (03/11/2026): B "Scrivania", rifinita
- Mockup 01 (`mockups/01-home-direzioni.html`): scelta B su A Quaderno e C Lampada.
- Feedback su B: troppo "bambinesco" (contorno spesso, rosa pieno sulle cartelle, Fibonacci ovunque) -> più professionale, vivo, realistico.
- Mockup 02 (`mockups/02-scrivania-v2.html`): finestra sobria con sidebar cartelle, lista file con icone SVG piatte, post come documento (barra titolo, indietro, condividi, status bar, "Leggi anche", bottone Spotify). Rosa solo come segnale (cartella aperta, file nuovo). Fibonacci solo per nome e titolo grande; interfaccia in Poppins/Roboto Condensed. Una sola ombra leggera sulla finestra. Movimento spento con prefers-reduced-motion.
- Mockup 03 (`mockups/03-scrivania-v3.html`, 03/11/2026): wordmark "teloscrivo" + punto rosa `#FD6E88` (cerchio CSS: Fibonacci non ha il carattere "."); home compatta (titolo piccolo); apertura file = lettura a fuoco (via menu, titolo e footer; resta barra con indietro/condividi/progresso); testo che si costruisce con lo scroll (righe per le poesie, parole per i racconti), sotto la linea di lettura è invisibile e risalendo si disfa. Con prefers-reduced-motion tutto visibile.
- Mockup 04 (`mockups/04-scrivania-v4.html`, 03/11/2026): lettura a "linea di lettura" (46% dell'altezza). Si vedono 1-4 righe/frasi alla volta: sotto la linea compare piano, sopra sfuma (floor .18). Unità = riga (poesie) o frase (racconti). La prima riga parte sulla linea (titolo in alto) e lo scroll finisce quando l'ultima arriva sulla linea, quindi la lunghezza dello scroll segue la quantità di testo. Contatore "3 / 7" in status bar.
- **04 BOCCIATO (03/11/2026)**: "così sembra già finita". Causa verificata nello screenshot di Tomas: a schermo intero si vede un paragrafo intero + "LEGGI ANCHE" + "SCORRI" in basso, quindi la pagina sembra già conclusa e non invita a scorrere. Tomas: "guarda il vecchio mockup con l'animazione iniziale e entra dentro una poesia o altro, era fatto meglio".
- **Prossimo passo (nuova sessione)**: 1) aprire e studiare il vecchio mockup, probabilmente `_archivio-vecchio/mockups/09-teloscrivo-intro-e-notte.html` (viste Intro / Home / Lettura; scorciatoie `#intro-d`, `#home-m-900`, `#read-m-780`; lettura = righe che si accendono e spengono con lo scroll, parole barrate in rosa e sostituite, ultima riga accesa) e/o `12`/`13` per l'intro. Chiedere a Tomas QUALE vecchio mockup intende (09, 12 o 13) e se vuole l'intro iniziale nella Scrivania o solo il modo di entrare/leggere. 2) Capire COME dà l'idea di "inizio" (cosa si vede appena entri) e rifarlo nella Scrivania (mockup 05 nuovo), senza rimettere dentro il look scartato. 3) Regole per non sembrare "già finita": nascondere "Leggi anche" e barra di stato finché non si arriva in fondo; nessun testo pieno all'ingresso; ingresso con un gesto d'apertura.
- Note: il vecchio archivio resta "NON base visiva": si copia solo il meccanismo di lettura/ingresso. Poi check A/B a due passaggi, /ui-check, costruzione vera (Markdown -> HTML con script).

## Vincoli confermati (restano)
- **Palette ufficiale (3 colori)**: Navy Blue `#072D59`, Seal Blue `#DBF2FC`, Crimson Pink `#FD6E88`. Bianco puro solo per il logo.
- **Nome**: teloscrivo. Sito = blog.
- **Stack**: HTML/CSS/JS statico, mobile-first (mockup sempre con vista Mobile e Desktop).
- **Categorie**: Testi, Poesie, Racconti brevi, Dalle canzoni (link Spotify, niente player) + sezione TikTok (card con link, niente embed; profilo non ancora creato).
- Mockup: Arc, finestra nuova.

## Asset di marca tenuti
- `_asset-marca/logo/monogramma-{navy,seal,mono}.svg` (t calligrafica + mezzaluna rosa, tracciati con potrace)
- `_asset-marca/fonts/`: Fibonacci (+corsivo), Vetro, Balligesta (solo uso personale; Fibonacci Demo senza accenti). Font dei post: Poppins e Roboto Condensed (Google Fonts).

## Da fare
1. Chat nuova (/clear), poi /grill-me da zero sul brief del sito.
2. Direzioni a confronto, mockup, scelta.
3. /ui-check, checklist-sito, costruzione vera.

## Sessione 03/11/2026 (pomeriggio): home e navigazione
- `mockup/05-home-nav.html`: 3 direzioni di nav senza barra classica (1 Dock, 2 Quaderno a linguette, 3 Cerca stile Spotlight). Tomas ha scelto di approfondire il **Dock**.
- `mockup/06-dock-v2.html` (attivo): dock con icone vere (tessere con glifo, badge con il numero di scritti), home viva (saluto con ora vera, testo che si scrive da solo, rosa sotto il dock che segue la cartella aperta). **La sfera di vetro con le strisce e' stata provata e BOCCIATA da Tomas (troppo grande, sbilancia l'intestazione): non rimetterla.**, palette fusa sul riferimento di Tomas (screenshot niki.aroca: Seal Blue in alto, Navy in basso, Rosa che si scioglie nel blu).
- **Cambio rispetto al brief**: il brief diceva "No gradienti"; Tomas ha portato un riferimento con sfumature, quindi ora le sfumature Seal/Navy/Rosa sono volute (solo mix delle 3 tinte ufficiali, in oklab). Restano vietati neon e ombre pesanti.
- Da decidere: intensita' del rosa; se tenere la sfera anche nelle pagine categoria; poi la lettura (ancora da rifare, vedi sopra).
- Note tecniche: i file logo sono nominati per lo sfondo (`seal` su chiaro, `navy` su scuro); Fibonacci Demo senza accenti (niente accenti nei titoli grandi); Poppins tenuto perche' nel brief anche se la skill mockup lo vieta.
- **Feedback su 06 (03/11/2026)**: dock/nav OK; intestazione "povera e debole" (frasi descrittive, struttura titolo+bottone). Decisioni (grill-me, tutte la prima opzione): 1) voce di teloscrivo in prima persona ("Scrivo quello che a voce non riesco a dire."); 2) il TITOLO stesso si scrive da solo e cicla 4-5 frasi (niente card piccola); 3) sotto: card grande "Ultimo scritto" (titolo, anteprima 3 righe, minuti di lettura, Leggi) + le 4 cartelle con la loro frase d'apertura; 4) tono editoriale tipografico, niente oggetti decorativi. Fibonacci Demo senza accenti: le frasi del titolo non devono avere accenti.
- Mockup attivo: `mockup/07-dock-v3.html` (06 = copia di sicurezza).
- **Feedback su 07/08 (03/11/2026)**: dock BOCCIATO ("non mi piace per niente"), non rimetterlo. `mockup/09-classica-v5.html` (attivo): header con solo logo a sinistra + nav classica (Testi, Poesie, Racconti, Canzoni, Cerca) e tema; titolo fisso "teloscrivo." con punto rosa e sottotitolo "la luna porta consiglio"; blocco a destra che SI SCRIVE da solo in loop sugli ultimi 5 pubblicati dal piu' recente (ordine per data ISO, pallini per saltare). Via la frase "Sono teloscrivo...". Verificato con screenshot Brave headless mobile + desktop.
- 03/11/2026: il blocco che scrive sta dentro una finestra (barra titolo con 3 pallini, pie' con pallini+Leggi), come da richiesta 'effetto finestra desktop'.
- 03/11/2026: il blocco che scrive sta dentro una finestra (barra titolo con 3 pallini, piede con pallini+Leggi), come da richiesta 'effetto finestra desktop'.
- **03/11/2026 sera**: `mockup/10-classica-v6.html` (attivo): tema SCURO FISSO (niente toggle), sfondo con alone-luna rosa/seal dietro la finestra + grana (via la macchina rosa sul fondo), via le 4 card cartelle (la nav filtra), un solo elenco 'Tutti gli scritti' raggruppato per mese con colonne allineate (data, titolo, sezione, anteprima). Verificato con screenshot Brave desktop+mobile.
- **03/11/2026**: `mockup/11-classica-v7.html` (attivo): nav in pillola vetro con testo chiaro e voce attiva piena rosa; intestazione con titolo + alone, sottotitolo 'la luna porta consiglio' in Fibonacci corsivo e riga di stato automatica.
- **03/11/2026**: 11-classica-v7: su mobile la nav sta nella riga del logo (pillola a destra, Cerca solo icona); desktop invariato. DA FARE (domande aperte a Tomas): migliorare 'come si vede il tutto', sezione TikTok con anteprima schermata e link, vista di lettura di uno scritto (ricordare: 04 bocciato perche' 'sembra gia' finita').
- **03/11/2026**: `mockup/12-classica-v8.html` (attivo). Home in 3 tappe numerate: 01 'Scegli cosa leggere' (4 tessere con ultimo scritto di ogni sezione), 02 'Tutti gli scritti' con filtri visibili + elenco per mesi, 03 'Su TikTok' (3 telefoni finti + bottone, il clic apre TikTok), piede con 'Torna su'. Vista di lettura: pagina intera, titolo grande + 'Scorri per leggere', testo che compare riga/frase mentre scorri (anche se salti), barra progresso, in fondo 'Leggi anche' (2), Spotify per le canzoni, Condividi. Esc/Indietro chiudono. Verificato con screenshot Brave (per i test con transizioni: in headless la dissolvenza resta a meta', non e' un bug). Da decidere: TikTok in nav solo quando il profilo esiste; pagina 'Cerca' vera.
