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

## SITO VERO (da mockup a sito generato) - decisioni 03/11/2026, flusso `nuovo-sito`
> Stato 03/11/2026 sera: SITO COSTRUITO e verificato in locale (Fasi 2-7). Resta: Fase 8 (commit/push solo su conferma di Tomas), testi veri al posto di quelli di prova, decisioni sotto in "Da decidere". Come si usa: aggiungi `scritti/<slug>.md` e lancia `python3 genera.py`.
- **Base visiva**: `mockup/13-classica-v9.html` (= `index.html` in radice, copia). Home in 3 tappe, lettura con titolo che vola (apertura e chiusura C), testo che compare e sparisce scorrendo, tema SCURO FISSO (niente interruttore). Il 12 e' backup. Il 14 e' il confronto animazioni (scelta C e C).
- **Contenuti**: i 8 scritti del mockup diventano file veri `scritti/*.md`; Tomas li sostituisce coi suoi testi uno alla volta. Nessun testo finto nel sito finale.
- **Pagine**: home, una pagina per scritto (`/scritti/<slug>/`, titolo e testo reali per la SEO), una pagina per sezione (Testi, Poesie, Racconti, Canzoni), Cerca (indice JSON, JS), 404. Ogni pagina: title, description, canonical, og, JSON-LD Article.
- **Pubblicazione di un nuovo scritto**: file Markdown con frontmatter (titolo, data, sezione, estratto, link Spotify per le canzoni) + `python3 genera.py` che produce tutto l'HTML. CSS unico condiviso (`style.css`), non piu' inline. Python, niente pannello admin.
- **Hosting**: ora GitHub Pages sul repo `tomas-coro/teloscrivo` (attivo, URL https://tomas-coro.github.io/teloscrivo/). Dominio `teloscrivo.it` e hosting definitivo (Plesk o Pages) si decidono dopo: l'URL base sta in UN'unica impostazione di `genera.py` (usata per canonical, sitemap, og).
- **Da ricordare**: il repo e' PUBBLICO (reso tale da Tomas); `_archivio/` e `PROGETTO.md` sono visibili. Font Fibonacci = "Demo": controllare la licenza prima del dominio vero. Git: commit/push solo su conferma di Tomas (eccezione: oggi ha chiesto lui di pushare). `index.html` in radice va sostituito dal generato.
- **Sezioni ancora di prova nel mockup**: "Su TikTok" (card-link nascosta finche' il profilo non esiste), Cerca. Da decidere: schede delle 4 sezioni in home (altezze diverse, "Ultimo:" a capo irregolare: proposta stessa altezza + riga singola con puntini).

### Com'e' fatto il sito generato (03/11/2026)
- File sorgente: `scritti/*.md` (9 scritti, il mockup ne aveva 9, non 8), `genera.py` (UNICA impostazione URL: `BASE_URL`; `TIKTOK_URL` vuoto = sezione TikTok nascosta), `style.css`, `app.js`. Output generato: `index.html`, `testi|poesie|racconti|canzoni/`, `scritti/<slug>/`, `cerca/`, `404.html`, `cerca.json`, `sitemap.xml`, `robots.txt`, `.nojekyll`. Link tutti relativi (funzionano su `/teloscrivo/` e sul dominio vero); la 404 usa il percorso di `BASE_URL`.
- Il titolo che vola tra elenco e lettura usa le View Transitions del browser tra pagine vere (non piu' un overlay in home). Dove non sono supportate (Firefox) il titolo sale da solo. Il testo degli scritti sta sempre nell'HTML (SEO, no-JS): l'effetto "compare scorrendo" lo aggiunge il JS.
- Font in locale: Poppins e Roboto Condensed scaricati in `assets/fonts/` (niente Google Fonts, niente richieste a terzi). Scritto: nessun cookie, nessun tracker, quindi nessun banner. Footer senza "Cookie · Privacy" (non c'e' niente dietro).
- Cerca = pagina vera `cerca/` con `cerca.json` (non piu' il popup). Condividi = pannello del telefono, altrimenti copia il link.
- Stessa altezza per le 4 tessere "Scegli cosa leggere", con "Ultimo:" su una riga e puntini (proposta di PROGETTO accettata).
- Frontmatter: `titolo`, `data`, `sezione`, `estratto` (facoltativo), `spotify` (facoltativo: senza link niente bottone). `genera.py` si ferma con un errore chiaro se manca un campo, se c'e' un trattino lungo, se un link interno e' rotto.
- **Da decidere / da fare per Tomas**: 1) i 9 testi sono ancora quelli di prova del mockup; 2) licenza font Fibonacci "Demo" (senza accenti: titoli con accenti ricadono su Poppins); 3) il repo e' pubblico e contiene `vetro.otf` e `balligesta.otf` (uso personale) in `assets/fonts/`, valutare di toglierli; 4) dominio `teloscrivo.it` e hosting definitivo; 5) la `robots.txt` in sottocartella (github.io/teloscrivo) non ha effetto per Google, vale solo sul dominio vero; 6) link Spotify delle canzoni; 7) profilo TikTok; 8) il blocco "ultimi scritti" gira da solo senza tasto pausa (si ferma se scegli un pallino o con "riduci movimento").

## Mockup 21 - griglia e navigazione (04/11/2026) - APPROVATO a parole, da portare nel sito vero
- File: `mockup/21-griglia-navigazione.html` (interruttore Mobile/Desktop) + `mockup/21-app-navigazione.html` (app cliccabile, dati veri da `scritti/*.md`). Verificato con screenshot Brave headless a 390 e 1440 px, JS con `node --check`. NON ancora fatti: `/ui-check`, check A/B, prova con gesture reali su telefono.
- Decisioni (grill-me, 3 blocchi): griglia 3 colonne desktop / 2 tablet / 1 mobile; niente modale anteprima, clic su card = apre subito lo scritto (espansione della card, Indietro la richiude); via la barra chip dalla home; nello scritto il chip categoria (es. "Poesie") apre la lista di quella categoria; mostrare solo categorie con almeno uno scritto; un solo tasto Indietro (niente X negli scritti); X solo nella ricerca (il bottone Cerca ruota in X, torna dove eri); swipe verso destra = indietro, Esc e freccia sinistra anche; il testo segue lo scroll su e giu (come oggi, unita = riga o frase); `prefers-reduced-motion` = solo dissolvenze.
- **PORTATO nel sito vero (04/11/2026), in `genera.py` + `app.js` + `style.css`** (versioni `style.css?v=4`, `app.js?v=3`). Resta un sito a pagine vere (SEO e no-JS intatti): griglia 3/2/1 con tessere che aprono lo scritto; via filtri e anteprima modale dalla home; nello scritto chip categoria + foto segnaposto (colore per sezione), un solo Indietro in alto, Condividi solo in fondo; pagine categoria a griglia con Indietro (solo sezioni con scritti, le vuote non hanno pagina ne' sitemap); Cerca diventa X sulla pagina Cerca; Indietro unico (`goBack` in `app.js`): history.back() se arrivi dal sito, altrimenti categoria/home; Esc, freccia sinistra e swipe a destra (ignora i primi 24px dal bordo, pinch-zoom lasciato); `prefers-reduced-motion` = solo dissolvenze.
- **Apertura dalla card**: View Transitions tra pagine + ritaglio animato sul `root` (si apre dal rettangolo della card, al ritorno si richiude nella card). Dove non e' supportato (Firefox, Safari senza Navigation API) resta la dissolvenza. NON verificabile con screenshot: va provato a mano in Chrome/Brave e su telefono.
- **Verificato**: `python3 genera.py` (link interni ok), `node --check app.js`, nessun errore in console su home/categoria/scritto/cerca, screenshot a 390 e 1440 px di home, categoria, scritto, cerca. **NON ancora fatti**: `/ui-check`, check A/B, prova gesture e transizioni su telefono, commit.
- Hero della home lasciato com'era (blocco "ultimo scritto" che si scrive da solo): il mockup non lo mostrava, da confermare con Tomas.
- Per vedere il mockup da fuori casa: screenshot con Brave headless (iframe 390px, window 700 px, niente `--force-device-scale-factor`, ritaglio sips centrale).

## Sessione 04/11/2026 (sera): font e decisioni di Tomas
- **Font titoli: Instrument Serif** (OFL, accenti ok, in locale `assets/fonts/instrumentserif-*.woff2`) al posto di Fibonacci Demo (tolto, licenza non valida). Scelto su `mockup/28-font-alternativi.html`. `style.css?v=5`. Verificato con screenshot home e scritto a 1200 px.
- Tolti `vetro.otf` e `balligesta.otf` (inutilizzati). Restano nella storia git del repo pubblico: riscrivere la storia solo con ok di Tomas.
- Dominio: Tomas compra `teloscrivo.it`; poi cambiare `BASE_URL` in `genera.py`. Hosting (Pages o Plesk) ancora da decidere.
- TikTok: si aspetta (`TIKTOK_URL` vuoto). Spotify: solo negli scritti ispirati a una canzone, col link nel frontmatter.
- Da fare: `/ui-check` + check A/B sul sito (ora con il font nuovo), prova gesti/transizioni su telefono (la fa Tomas).
- **Fondo dello scritto (04/11/2026)**: saluto "Grazie per aver letto e ricorda che / la luna porta consiglio" (rosa che sfuma nel celeste + mezzaluna), Condividi + Copia link (impilati su mobile, affiancati su desktop), Leggi anche (con 1 solo scritto scheda a tutta larghezza), firma `scrivoanchesu.` + Instagram su una riga. Mockup `mockup/29-*`. Sito: `style.css?v=6`, `app.js?v=4`. Verificato con screenshot; NON ancora fatti `/ui-check`, check A/B, prova su telefono. Assunzione da confermare: l'emoticon e' la mezzaluna del logo.
