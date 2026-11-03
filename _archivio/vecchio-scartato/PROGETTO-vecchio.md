# Blog personale di Tomas - stato del progetto

> Riprendi da qui dopo un /clear. Aggiornato: 02/11/2026.

## Cosa è
Blog personale: poesie, mini racconti, pensieri, altro (anche con immagini). Dominio proprio (da decidere). Nome del blog PROVVISORIO: "Appunti a margine".

## Decisioni prese
- **Stack**: HTML + CSS + JS statico, animazioni con GSAP. Testi in Markdown + script Python che genera le pagine. Pubblicazione su GitHub Pages con dominio proprio.
- **Struttura**: Home (intro animata + stanze + ultimi testi), pagina Stanza (elenco di un genere), pagina Testo (lettura), Chi sono. Da valutare ancora se servono altre pagine.
- **Direzione scelta**: "Le Stanze" = 4 grandi fasce di colore (Poesie, Racconti, Pensieri, Altro) che si aprono al tocco; su desktop colonne verticali che si espandono.
- **Intro**: ~4 secondi, a tutto schermo, titolo lettera per lettera + sipario a colori; tasto "Salta"; si salta con prefers-reduced-motion.
- **Social**: Instagram con link segnaposto (account da creare). TikTok nascosto nel codice finché non esiste.
- **Sito mobile-first**, sempre mockup con vista Mobile e Desktop.
- **Palette: ANCORA DA DECIDERE.** Le 7 del mockup 01 non convincono. Il mockup 02 ne propone 3 nuove (Inchiostro e ciliegia, Notte e pesca, Carta e cobalto).

## File
- `mockups/01-blog-direzioni.html` - 3 direzioni (Quaderno, Stanze, Bacheca) x 7 palette.
- `mockups/02-sito-le-stanze.html` - sito intero navigabile (home, stanza, testo, chi sono) con intro.

## Da fare
1. Scegliere palette (e dire cosa non convinceva delle prime).
2. Decidere pagine definitive e nome/dominio.
3. Costruire il sito vero (checklist-sito.html, /ui-check, /web-design-guidelines prima di pubblicare).

## Aggiornamento 02/11/2026 (sera) - mockup 01 e 02 BOCCIATI
- Tomas sul mockup 02: "orrendo e tanto AI stock, non mi piace sotto nessun punto di vista".
- Causa probabile: ho usato gli stessi trucchi di ogni sito generato (titolo gigante grotesque pesante, blocchi di colore pieni, forme geometriche che fluttuano, sipario colorato, marquee). Palette incluse: nessuna approvata.
- NON ripartire da quei file. Prima servono RIFERIMENTI REALI di Tomas (siti, riviste, copertine, locandine che gli piacciono) e 3 aggettivi sul tono. Poi si progetta.
- Resta valido: stack HTML+CSS+JS, struttura a stanze (da rivalutare), Instagram segnaposto, TikTok dopo, intro animata ma di gusto.

## Aggiornamento 02/11/2026 (notte) - mockup 03 (5 direzioni) BOCCIATO, nuova rotta
- Mockup `03-blog-cinque-direzioni.html` bocciato: "noiosi, senza carattere, banali, asettici, non ti rimangono impressi, non danno emozioni".
- Rotta nuova (parole di Tomas): far capire SUBITO l'emozione di ogni testo; ogni racconto/poesia NON deve sembrare uguale agli altri. Vuole animazioni, stile, icone, cose che si muovono, "dare vita" al sito, niente "copia della copia".
- FONT scelti da Tomas (in ~/Downloads): **Vetro** (titoli/sezioni importanti, DOSATO, non un logo da spammare), **Balligesta** (firme), **Fibonacci** (dubbio: forse troppo strano per testi normali).
- Fatti sui font (verificati): tutti e 3 licenza SOLO USO PERSONALE (vietato uso commerciale/introiti: serve licenza a pagamento se il blog guadagna). Vetro e' DEMO ma ha accenti italiani (a0-ff). Balligesta ha gli accenti. **Fibonacci Demo NON ha accenti ne' punteggiatura (solo A-Z a-z 0-9)**: usabile solo per decori/numeri, non per testi italiani.
- Idea in discussione: sistema "emozione per testo" (ogni testo dichiara un'emozione e la pagina cambia colore, movimento, icona, tipografia). Da confermare con /grill-me.

## DECISIONI CONFERMATE 02/11/2026 (notte) - rotta "emozione per testo"
1. **Concetto**: ogni testo dichiara un'emozione; scheletro del sito unico, ma cambiano colore, movimento, icona animata e ritmo del testo. Il sito non e' 40 siti diversi, e' un sistema con "meteo" diverso per testo.
2. **Emozioni di partenza (default, Tomas non ha risposto)**: malinconia, rabbia, tenerezza, ansia, ironia, meraviglia. Tomas non ha dato testi veri: usare testi di esempio scritti per evocare ogni emozione, dichiarandolo, e chiedergli i suoi veri appena ha scelto la direzione.
3. **Home**: niente elenco uguale per tutti; ogni testo e' una "scheda-mondo" con animazione e icona sue, pochissimo testo, l'emozione si sente prima di leggere.
4. **Icone**: linee disegnate a mano in SVG, una per emozione, ANIMATE (es. battito che si spezza, foglia che cade, crepa che si allarga). Niente emoji, niente librerie di icone.
5. **Font** (file in ~/Downloads, da copiare nel progetto e caricare con @font-face):
   - Vetro: `~/Downloads/vetro-demo/Vetro DEMO.otf` - solo titoli/sezioni importanti, dosato.
   - Balligesta: `~/Downloads/balligesta/Balligesta.otf` - solo firme.
   - Fibonacci: `~/Downloads/fibonacci-demo/Fibonacci-Demo.ttf` (+ Italic) - solo numeri/decori (non ha accenti).
   - Testo di lettura: un serif calmo scelto dall'art director (non in blocklist mockup).
   - Licenze: tutti solo uso personale; se il blog guadagna, comprare le licenze.
- **Prossimo passo**: mockup `04-...html` con la skill mockup/impeccable: home a schede-mondo + pagina di lettura per almeno 3 emozioni molto diverse tra loro (mobile + desktop), movimento vero, font di Tomas. NON riusare mockup 01, 02, 03.

## Aggiornamento 02/11/2026 (notte tarda) - mockup 04 costruito
- File: `mockups/04-blog-emozione-per-testo.html` (+ cartella `mockups/fonts/` con Vetro, Balligesta, Fibonacci copiati). Home a 6 schede-mondo (malinconia, rabbia, meraviglia, tenerezza, ansia, ironia) + pagine di lettura per 3 (malinconia chiara/lenta, rabbia nera-rossa/secca, meraviglia gialla/leggera). Interruttore Mobile/Desktop. Testi di ESEMPIO scritti da Claude.
- GOTCHA Vetro DEMO: le legature sono rotte (spariscono lettere: "MO", "AS", "ZA"). Sempre `font-variant-ligatures:none`. Vetro e' solo maiuscolo.
- Font di lettura scelto: Newsreader (Google Fonts). Fibonacci solo per numeri e "novembre" (ha le lettere base, non gli accenti).
- Dubbi aperti: Vetro e' usato anche sul nome emozione di ogni scheda (non solo sui titoli): troppo? Tomas deve ancora scegliere/valutare.

## DECISIONI CONFERMATE 02/11/2026 (notte tarda) - dopo il mockup 04 (BOCCIATO)
- Mockup 04 bocciato: "terribile". Salvato di buono: l'idea che il testo SEGUA LO SCROLL, ma in ENTRAMBE le direzioni (giu' si accende, su si spegne). Le icone SVG fatte a codice: "malissimo, brutte, per niente coerenti e professionali" -> TOLTE. Non rifarle a codice.
- Categorie (Tomas): **Testi, Poesie, Racconti brevi, "Dalle canzoni"** (frasi/testi nati da canzoni che citera', con link Spotify) + sezione **TikTok** (video pubblicati con link).
- Categoria = dove sta il testo; emozione = come appare la pagina (ogni testo ha entrambe).
- Home: 4 porte (categorie) + sotto "ultimi testi" come schede-mondo per emozione. TikTok quinta voce del menu.
- Identita' di ogni emozione SENZA disegni: tipografia gigante (Vetro), colore, grana, movimento del testo. Illustrazioni (Ideogram) solo dopo, se manca qualcosa.
- Spotify: card con titolo+artista+bottone "Ascolta su Spotify", NIENTE player incorporato. TikTok: griglia card 9:16 con copertina+link, NIENTE embed.
- Scroll: effetto legato alla posizione (progress per riga), reversibile, rispetta prefers-reduced-motion.
- Da chiarire (blocco 2): riferimenti reali, 3 aggettivi di tono, tema chiaro/scuro, cosa mostra il mockup 05.

## 02/11/2026 (notte tarda) - tono e svolta
- Tono (Tomas): **intimo, graffiante, notturno**. NON vuole le emozioni "in quel senso" (sistema meteo per emozione abbandonato), ma NON vuole nemmeno post tutti uguali: la varieta' deve venire da come e' composto ogni post, non dall'emozione dichiarata.
- Mockup 05: 3 direzioni diverse da provare (file `mockups/05-blog-tre-direzioni.html`): A "Fogli strappati" (collage di carte su scrivania notturna), B "Cinema di parole" (scene a tutto schermo, testo come sottotitoli legato allo scroll), C "Manifesti" (poster tipografici giganti, righe che si ingrandiscono al passaggio).
- 02/11/2026: mockup 05 costruito e verificato (screenshot mobile+desktop, nessuno scroll orizzontale). In attesa che Tomas scelga A, B o C (o un mix). Nel file: interruttori Direzione, Mobile/Desktop, Home/Lettura; categorie e TikTok sono sezioni della home (nel sito vero saranno pagine). Link Spotify/TikTok sono di esempio.

## DECISIONI CONFERMATE 03/11/2026 - nuova identita' "teloscrivo" (sostituisce il nome provvisorio e le rotte 01-07)
- **Nome: teloscrivo** ("te lo scrivo"). Frase: "quello che a voce non so dire". Scelto da Tomas dopo molte proposte scartate (le iniziali T e C NON servono piu' nel nome: restano al massimo nel marchio, l'icona app e' una "t." con puntino rosa).
- **Concept di identita'** (immagine "Orbita contemporanea", direzione creativa 02): cielo morbido, luna, bordo di luce rosa/azzurro. Intro animata in 4 frame: cielo dall'alto, zoom sulla luna, luna che diventa portale di luce, ambiente del blog (sfondo luna). Animazione da definire dopo i mockup.
- **Palette**: azzurro #DBF2FC, blu notte #072D59, rosa #FD6E88.
- **Font (al posto di Playfair/Inter del concept)**: logo e frase = Fibonacci Corsivo (la frase e il nome non hanno accenti: ok; il puntino rosa del logo e' un cerchio disegnato); titoli dosati = Vetro MAIUSCOLO (ligature spente); firme = Balligesta; testi di lettura = Newsreader; etichette piccole = Newsreader maiuscoletto. Licenze solo uso personale.
- **Luna**: immagini generate con Ideogram (mai disegnata a codice). Prima prova = luna fotografica con crateri: scartata perche' "stock". Si rifa' come nel concept (disco scuro liscio con bordo di luce), in 9:16 per mobile e 16:9 per desktop. File in `mockups/img/`.
- **Mockup 08**: stessi palette/logo/luna/font in tutte le direzioni; varia l'architettura della home, il passaggio lista-lettura e il tema della pagina di lettura (chiaro #DBF2FC o scuro).
- **03/11/2026 - mockup 08 costruito**: `mockups/08-teloscrivo-tre-architetture.html` (immagini luna in `mockups/img/`: luna-mobile.webp 9:16, luna-desktop.webp 16:9 ma solo 1024x576, da rifare in alta). Tre architetture con stesso logo/luna/palette/font: A "Notte editoriale" (cielo fisso, lettura scura riga per riga), B "Carta di luna" (cielo che diventa carta #DBF2FC, lettura chiara), C "Discesa" (zoom sulla luna mentre scorri, lettura una strofa per schermata). Interruttori Direzione / Mobile-Desktop / Home-Lettura. Testi, date, link Spotify/TikTok di ESEMPIO. Verificato con screenshot (mobile+desktop); da fare: prova a mano di scroll/hover. In attesa che Tomas scelga A, B o C (o un mix). Intro con zoom sulla luna: non ancora fatta.

## 03/11/2026 (mattina) - SCELTA: direzione A "Notte editoriale", ma da MIGLIORARE + lavoro sull'animazione
- Tomas sceglie **A** ma "non mi convince ancora al 100%". Cosa non va (sue risposte, punti 2-3-4): **hero fermo e poco emozionante; pagina di lettura ordinata ma poco memorabile; tono troppo pulito/freddo rispetto a "intimo, graffiante, notturno"**. (Il punto 1, home piatta sotto il cielo, NON l'ha scelto ma resta un sospetto mio: la luna sparisce dopo la prima schermata.)
- **Esempio di animazione di Tomas**: `~/Downloads/teloscrivo_intro_apertura.html` (4,8 MB, immagini incorporate). Come e' fatto: intro 7,6 s a tutto schermo; canvas di stelle che zoomano; curva della Terra con bordo azzurro + 2 strati di nuvole; luna PNG che si avvicina (zoom accelerato, rotazione -2 gradi); 2 frasi che entrano/escono ("Alcune cose esistono solo quando le scriviamo." poi "La luna porta consiglio. Le parole, un posto dove restare."); lampo di luce azzurro-rosa che copre tutto; poi appare il sito (hero con luna grande a destra che fluttua, "Tra le righe", scritti, lettura in pannello). Barra di progresso, tasto "Salta intro", una volta per sessione (sessionStorage), reduced-motion = salta. Usa Playfair Display e DM Sans: DA SOSTITUIRE coi nostri font. Il suo "logo" e' una "t." con puntino.
- **Asset estratti** in `mockups/img/`: `esempio-tomas-1.png` (nuvole 2200x740 trasparenti, utili) e `esempio-tomas-2.png` (luna 1500x1500 con crateri nebbiosi: peggiore della nostra luna Ideogram a disco scuro con bordo di luce; usare la nostra o rifare).
- **Prossimi passi (nuova sessione, partire da qui)**: (1) mockup 09 = direzione A migliorata: luna/bordo di luce che resta dentro tutta la home, testi con piu' carattere/graffio, lettura piu' memorabile (da grillare con Tomas: cosa vuol dire "graffiante" per lui); (2) intro costruita sulla linea di tempo del suo esempio ma coi nostri font/luna/palette; (3) rifare luna desktop in alta risoluzione; (4) poi checklist-sito e costruzione vera (Markdown + script Python, GitHub Pages).

## 03/11/2026 (pomeriggio) - mockup 09 costruito (direzione A migliorata + intro mix)
- File: `mockups/09-teloscrivo-intro-e-notte.html`. Viste: Intro, Home, Lettura (Mobile/Desktop). Scorciatoia per prove: `#intro-d`, `#home-m-900`, `#read-m-780` (vista-schermo-scroll). Verificato con screenshot headless Brave (intro, home, lettura, mobile+desktop). NON ancora provato a mano da Tomas.
- Decisioni di Tomas: UNA intro mix ~5 s. Frase 1 "Alcune cose esistono solo quando le scriviamo" a macchina col cursore rosa che avanza con le lettere. Frase 2 "La luna porta consiglio" animata con la luna (lettere che salgono, luna che si avvicina, alone). Nuvole "piu vere e vive". Finisce con la home. Frase del sito (tagline) = "La luna porta consiglio" (al posto di "quello che a voce non so dire"). Frase intro 2 resta "Le parole, un posto dove restare."
- Nuvole: Ideogram ha dato errore di piano/limite, quindi SONO costruite a codice (filtri SVG feTurbulence + illuminazione, 2 strati che scorrono). Se le vuole piu fotografiche: generare con Ideogram (quando il limite si resetta) o usare foto reali.
- Home: luna dietro tutta la pagina (si abbassa con lo scroll), testi composti in modi diversi (titolo con cancellatura, incipit enorme, una riga in Vetro). Lettura: righe che si accendono/spengono con lo scroll, parole barrate in rosa e sostituite, ultima riga accesa. Testi di ESEMPIO.
- Da fare: (1) Tomas prova e dice cosa non va; (2) /ui-check completo + prova a mano; (3) luna desktop in alta risoluzione; (4) i suoi testi veri; (5) checklist-sito e costruzione vera.

## 03/11/2026 (pomeriggio, 2) - mockup 10: 3 varianti per fase (feedback su 09)
- Feedback Tomas su 09: frase iniziale da migliorare e da lasciare leggere; punto rosa finale come in "teloscrivo."; "La luna porta consiglio" meglio con 3 mockup; la luna che "esplode" (anello di luce finale) = TERRIBILE, vuole 3 chiusure diverse. NON rifare mai esplosioni/flash.
- File: `mockups/10-teloscrivo-frasi-e-chiusure.html` (09 resta com'e). Intro a 3 fasi (~9,6 s: frase 1 5 s, luna 3 s, chiusura 1,6 s), ogni fase con 3 varianti, si rivede una fase sola toccando la variante, "Tutto insieme" per la combinazione. Scorciatoia prove: `#intro-m-p1-a` (vista-schermo-fase-variante).
- Frase 1: A Macchina (serif), B Fibonacci (font del logo), C Ripensata (scrive "dico", cancella, scrive "scriviamo"). Punto rosa = cerchio come il logo.
- Luna: A Sale (lettere nella luce), B Luce che scorre (la luce accende le parole), C Manifesto (la / LUNA / porta / consiglio a scale diverse).
- Chiusura: A Alba (luce che sale), B Fiato (sfuma sfocando), C Iride (si chiude intorno alla luna). Cielo intro = cielo home (nessun salto); nuvole e velo notturno restano fino alla chiusura.
- Verificato con screenshot headless; l'animazione nel tempo non l'ho vista (solo frame). In attesa che Tomas scelga una variante per fase.

## 03/11/2026 (sera) - mockup 11: scelte su 10 + nuove chiusure
- Scelte di Tomas su 10: frase 1 = "Ripensata" ma in stile Fibonacci e con "diciamo" al posto di "dico" (scrive "...quando le diciamo", cancella, scrive "scriviamo", punto rosa tondo). Luna = Manifesto (la / LUNA / porta / consiglio) da migliorare e da far vedere bene a schermo. Chiusure A Alba, B Fiato, C Iride: NESSUNA gli piace; vuole 3 nuove: Alba migliorata + 2 diverse.
- File: `mockups/11-teloscrivo-frasi-chiusure-2.html` (09 e 10 intatti). Frase 1 e Manifesto sono ora fissi (un solo tasto ciascuno). Manifesto: misure in cqh/cqw (mai tagliato), velo scuro dietro, ancorato in basso su mobile; su desktop a sinistra a centro schermo.
- Chiusure nuove: A Alba migliorata (luce che nasce sotto le nuvole, non copre lo schermo, il velo notturno si alza), B Il titolo si scrive (la macchina scrive "teloscrivo." dove sta il titolo della home), C Dentro le nuvole (strato di nebbia scura che si ingrandisce e si dirada).
- Durata totale ~10,2 s (frase 1 5 s, luna 3,4 s, chiusura 1,8 s). Verificato con screenshot headless; animazione nel tempo NON vista. In attesa che Tomas scelga la chiusura.
- Dopo la scelta: /ui-check completo, luna desktop in alta risoluzione, testi veri di Tomas, checklist-sito e costruzione vera.

## 03/11/2026 (sera, 2) - mockup 12: intro quasi definitiva
- Scelte di Tomas su 11: (1) frase 1: "scriviamo" con effetto rosa solo su PARTE della parola, "gestito diversamente" -> mia interpretazione: "amo" rosa (scri-vi-AMO), resto bianco, poi punto rosa. DA CONFERMARE con Tomas. (2) Manifesto ok ma deve sfruttare anche la LARGHEZZA: righe non tutte sulla stessa linea -> fatto zig-zag (mobile: porta a destra, consiglio rientrato; desktop: porta accanto a LUNA, consiglio in diagonale). (3) Chiusura = C + A unite (nuvole + alba). (4) "La luna porta consiglio" non deve ripetersi: resta solo nel manifesto; tagline della home = "scriviamo: l'esigenza di esprimermi" (parole di Tomas, interpretazione da confermare; in Newsreader italico maiuscoletto perche' Fibonacci non ha ":" ne' apostrofo).
- File: `mockups/12-teloscrivo-intro-definitiva.html` (11, 10, 09 intatti). Un solo percorso fisso ~10,4 s (frase 1 5 s, luna 3,4 s, chiusura 2 s). Verificato con screenshot headless (manifesto mobile+desktop, home con nuova tagline, "amo" rosa nel DOM, frame della chiusura); animazione nel tempo NON vista.
- Prossimi passi: Tomas conferma/aggiusta; poi /ui-check completo (intro + home + lettura) e prova a mano; luna desktop in alta risoluzione; testi veri; checklist-sito e costruzione vera (Markdown + Python, GitHub Pages).

## 03/11/2026 (sera, 3) - mockup 13: manifesto in 3 modi + frase e chiusura corrette
- Feedback di Tomas su 12: (1) chiusura = nuvole + titolo che si scrive (NON piu' nuvole + alba); (2) "scriviamo": non "amo" rosa ma un rosa che sfuma dall'inizio alla fine della parola ed e' animato dentro la parola; (3) manifesto: vuole 3 mockup diversi per capire come gestirlo.
- File: `mockups/13-teloscrivo-manifesto-tre-modi.html` (12 e precedenti intatti). Durata ~10,8 s (frase 1 5 s, manifesto 3,8 s, chiusura 2 s).
- Frase 1: "scriviamo" ha un colore per lettera, bianco->rosa da sinistra a destra, che scorre avanti e indietro (onda con ritardo). Interpretazione di "sfuma e animato": DA CONFERMARE.
- Manifesto, 3 varianti (tasti nella barra): A Zig-zag (quello di prima), B Colonna (LUNA verticale a tutta altezza, si legge dal basso; la / porta / consiglio accanto), C Una parola alla volta (ognuna a schermo pieno, poi lascia il posto; resta "consiglio"). Misure calcolate sulla parola misurata (mai fuori schermo).
- Chiusura: la nebbia scura si attraversa e si dirada mentre la macchina scrive "teloscrivo." dove sta il titolo della home, poi compare la tagline. Nessun flash.
- Verificato con screenshot headless (mobile + desktop, fotogrammi fermi con `#intro-m-p2-w-t2600`; le prove di tempo reale sono approssimate). L'animazione fluida NON vista da me. In attesa che Tomas scelga A/B/C.

## 03/11/2026 (sera, 4) - mockup 13 aggiornato dopo feedback
- Tomas: il titolo della chiusura sembrava fuso con le nuvole e solo alla fine prendeva colore/opacita' giusti. Fix: la nebbia si dirada entro ~1,1 s, il titolo parte a 0,5 s con una leggera ombra scura dietro (solo nell'intro), tagline a 1,15 s.
- Manifesto: Tomas sceglie ZIG-ZAG (A) "da migliorare, meglio su mobile che su desktop". Fix desktop: LUNA 35% altezza, "porta" accanto, "consiglio" spostato a destra a scalini, composizione su tutta la larghezza; tolto il rettangolo scuro visibile dietro (velo sfumato a zero ai bordi). B e C restano nel file ma sono scartate.
- Da confermare con Tomas: zig-zag ok anche su mobile o da ritoccare? Poi /ui-check, luna desktop alta risoluzione, testi veri, costruzione vera.

## 03/11/2026 (sera, 5) - mockup 13: tolta la fase "La luna porta consiglio"
- Tomas: la sezione luna/manifesto dura troppo -> TOLTA dall'intro (nessuna fase manifesto, nessuna frase "Le parole, un posto dove restare"). Manifesto A/B/C archiviati nel codice (non usati). Intro ora = frase 1 (5 s) + chiusura (3,6 s) = ~8,6 s.
- Titolo (richiesta: nasce fuso con le nuvole e poi si riempie, "ancora scarso"): ora ogni lettera di "teloscrivo" nasce dentro la nebbia, velata, sfocata e color nuvola, e si condensa a bianco pieno e nitido da sinistra a destra (onda ~0,09 s a lettera, ~1,5 s per lettera); poi punto rosa che scatta e la tagline. Nebbia piu' lunga (2,9 s). Verificato solo con 4 fotogrammi fermi.

## 03/11/2026 (sera, 6) - mockup 13: il sito si costruisce mentre si scrive il titolo
- Tomas: tagline home = "La luna porta consiglio" (al posto di "scriviamo: l'esigenza di esprimermi"); la comparsa del resto deve avvenire MENTRE si scrive il titolo, "come a costruirsi il sito, semplice ma d'impatto". Fatto: nella chiusura (2,9 s) logo piccolo e voci del menu entrano una a una dall'alto (0,35-1,1 s), riga rosa che si disegna + frase (1,1 s), "Scorri" (1,55 s), mentre le lettere del titolo si condensano; poi dissolvenza sulla home identica. Verificato con fotogrammi fermi.
- APERTO: "header" (non gli piace, "basic"). Chiesto a Tomas: 1) intende barra in alto o tutta la prima schermata (consigliato: tutta); 2) cosa lo rende basic; 3) 3 varianti da confrontare (consigliato: si). In attesa di risposta.

## 03/11/2026 (sera, 7) - mockup 14: logo + header + nav bar in 3 direzioni
- Tomas: logo in alto a sinistra, creato dalla sua immagine di riferimento (Playfair/Inter NON usati: restano Fibonacci per il logo); 3 mockup sia di logo sia di header + nav bar.
- File: `mockups/14-teloscrivo-logo-header-nav.html`. Viste: Header + navigazione / Solo logo (su notte, su carta chiara, icona app, favicon); Mobile/Desktop; menu mobile apribile.
- A Orbita: logo in un rigo con "s" rosa + arco di luce; barra trasparente, voci con puntino rosa; mobile = schermata intera. B Pillola di vetro: "teloscrivo." con punto rosa; barra-pillola di vetro fluttuante; voce attiva = pillola chiara; mobile = tendina; titolo centrato. C Indice laterale: logo impilato "telo. / scrivo" + arco; voci numerate 01-05 sul bordo destro con linea verticale; mobile = cassetto a destra.
- Tagline usata: "La luna porta consiglio" (quella del logo di riferimento "Quello che a voce non so dire" NON usata).
- Verificato con screenshot headless (mobile+desktop, menu aperti, vista logo). Interazioni non provate a mano. In attesa che Tomas scelga logo (A/B/C) e header (A/B/C), anche in combinazioni miste.

## 03/11/2026 (sera, 8) - mockup 15 CORREGGE il 14 (errore mio)
- Errore: nel 14 avevo ridisegnato anche hero e nav bar (pillola di vetro, indice laterale) mentre Tomas voleva SOLO il logo in alto a sinistra e la home come in 13. Il 14 e' da ignorare (restano utili solo le 3 versioni del logo).
- `mockups/15-teloscrivo-home-con-logo.html`: home identica a 13 (luna, titolo grande "teloscrivo." con punto rosa, frase "La luna porta consiglio", voci menu, "Menu" su mobile) + logo in alto a sinistra in 3 varianti: A "s" rosa + arco di luce; B punto rosa; C impilato "telo. / scrivo" + arco. Vista "Solo logo" (notte, carta chiara, icona, favicon). Verificato con screenshot; clic non provati.
- Prossimo: Tomas sceglie il logo (A/B/C); poi integrare logo + intro (13) in un unico file, /ui-check, luna desktop alta risoluzione, testi veri, costruzione vera.

## 03/11/2026 (notte) - NUOVO BRIEF: intro luna -> monogramma t + mezzaluna -> header (grillato, tutto confermato)
- Brief completo di Tomas (Creative Developer/Motion Designer): viaggio verso la luna con parallasse, la luna si trasforma per continuita' di silhouette nella mezzaluna del logo, compare la t, il monogramma si riduce e VOLA nell'header in alto a sinistra (e' lo stesso elemento, non svanisce e ricompare). Poi emergono home e menu sfalsati. 4-6 s, "Salta intro" sempre, "Rivedi intro", prefers-reduced-motion, mobile senza tagli, niente salti di layout.
- Decisioni (blocchi 1-3, "ok a tutti"): (1) la nuova intro SOSTITUISCE quella del mockup 13 (frase "scriviamo" + nebbia + titolo): niente doppia intro; (2) la frase "scriviamo" esce dall'intro, puo' stare nella hero come testo fisso; (3) lavoro in file nuovo `mockups/16-...` partendo da 13 e 15, lasciati intatti; (4) luna = immagine Ideogram a disco scuro con bordo di luce + GSAP + livelli di parallasse, NIENTE Three.js; (5) rifare la luna in alta (>=2400 px; se Ideogram e' ancora in limite, usare quella attuale e dirlo); monogramma = simbolo in alto a sinistra con wordmark "teloscrivo" (s rosa) accanto, sostituisce i logo A/B/C del 15; t = Fibonacci CORSIVO estratta come tracciato SVG (licenza solo uso personale); punto rosa solo nella variante C; prima la pagina di confronto, Tomas sceglie, poi l'animazione; monogramma definitivo = anche favicon e icona app (SVG + PNG 32/180/512); intro una volta per sessione (sessionStorage); "Salta intro" in basso a destra, "Rivedi intro" nel footer e nel menu mobile; reduced-motion/salto = home subito col monogramma al suo posto; verifica a 375, 390, 768, 1440; transizione per continuita' di forma, MAI flash ne' esplosioni.
- FATTO: `mockups/16a-teloscrivo-monogrammi.html` = 3 monogrammi a confronto (A Luna sottile, B Luna avvolgente con t davanti e taglio netto, C Integrato con punto rosa), su Navy e Seal Blue, mono e con rosa, a 24/32/40 px + striscia "header". Verificato con screenshot headless; non ancora visto da Tomas.
- PROSSIMO: Tomas sceglie A/B/C -> costruire `mockups/16-teloscrivo-intro-luna-monogramma.html`, poi /ui-check, favicon, checklist-sito, costruzione vera.

## 03/11/2026 (notte, 2) - 16a BOCCIATO, arriva il logo vero di Tomas
- Tomas su 16a: "mockup di scarsa qualita, fatti male, per niente professionali ne pubblicabili". Causa mia: luna = cerchio meno cerchio (icona generica), t grezza accostata senza rapporto di forma. NON riusare 16a ne le forme a codice.
- Tomas porta il LOGO: una "t" calligrafica in cui il gancio del piede diventa la mezzaluna rosa (immagine Navy / Seal Blue / monocromatica, #072D59 / #DBF2FC / #000000). Questo E' il monogramma definitivo: niente piu A/B/C.
- Tracciato in SVG vettoriale da me con potrace (2 path: t + luna, rosa piatto #FD6E88, senza sfumature): `mockups/logo/monogramma-navy.svg`, `-seal.svg`, `-mono.svg`. Sono circa 1,5 KB l'uno. Fedelta' buona; non ancora ritoccati a mano punto per punto.
- Limiti noti: a 24 px la luna rosa e' sottile e la fessura fra t e luna quasi sparisce; da valutare una versione "piccola" (luna piu spessa) per favicon/header.
- PROSSIMO: Tomas valida il tracciato; poi costruire `mockups/16-...` con la luna che si trasforma in QUESTA t (la luna diventa il gancio rosa, la t si disegna sopra), header e favicon.

## 03/11/2026 (notte, 3) - header + nav bar (desktop e mobile) con il monogramma
- Tomas: "ok meglio" sul 15b (monogramma in alto a sinistra, da solo). Poi: l'header "non convince" -> grillato: solo la BARRA (logo + menu), hero invariata; problema = piatto + muto; allo scroll la barra si compatta con velo notturno sfumato e il monogramma resta sempre visibile; mobile = schermata intera notturna con voci grandi e luna sullo sfondo, il monogramma si inclina aprendo il menu.
- File: `mockups/15c-teloscrivo-header-nav-monogramma.html` (15b e precedenti intatti). 3 direzioni: A Orbita (luna rosa che scivola sotto le voci), B Penna (voci in corsivo, tratto rosa tracciato al passaggio), C Indice (colonne 01-05 con riga che si colora; allo scroll i numeri spariscono). Interruttori Direzione / Mobile-Desktop / Stato (In alto, Scrollato, Menu aperto). Scorciatoia: `#B-m-menu` (direzione-schermo-stato).
- Verificato con screenshot headless (3 varianti x desktop/mobile x in alto/scrollato/menu aperto). NON provati a mano: hover, orbita animata nel tempo, tratto di penna, tasto Esc.
- In attesa: Tomas sceglie A/B/C (o un mix). Poi /ui-check, favicon dal monogramma, intro 16.

## 03/11/2026 (notte, 4) - 15c BOCCIATO + nuova rotta "ARCHIVIO DA CONSULTARE" (decisioni di Tomas, da qui si riparte)
- Tomas su 15c (3 header A Orbita / B Penna / C Indice): "di basso livello e per niente coerente". Causa mia: trucchi standard da menu (maiuscoletto spaziato, righe sottili, sottolineature), 3 varianti sullo stesso scheletro, 3 font nel menu, nessun legame col logo calligrafico. NON riusare 15c.
- FONT: Tomas vuole VALUTARE (non aggiungere a priori) PP Editorial New (Pangram Pangram, serif stretto ad alto contrasto, "licenses start at $40", prova gratuita) e Aeonik (Cotype Foundry, neo-grottesca geometrica, prezzi non indicati). Mia raccomandazione: Editorial New merita la prova (parente del logo), Aeonik debole (look tech/generico). Lapa.ninja da' 403, info lette dai siti dei produttori. Tomas deve scaricare le prove in ~/Downloads (NON ancora trovate al 03/11 notte). Controllare gli ACCENTI (a e i o u, apostrofo) appena arrivano: Fibonacci Demo non li aveva. Poi pagina banco di prova: stesso header+titolo con font attuali vs Editorial New vs Aeonik.
- NUOVO CONCETTO: i testi vivono nel sito "come dentro un archivio da consultare". La home deve essere in stile archivio: la gente si MUOVE liberamente tra gli scritti, SENZA ordine preciso ne' suddivisione obbligata; le categorie (Testi, Poesie, Racconti brevi, Dalle canzoni, TikTok) esistono ma sono "una cosa in piu".
- Risposte al grill (blocco 1):
  1. Come ci si muove: Tomas vuole 3 MOCKUP DIVERSI (mie ipotesi: A schede sparse a mosaico, B riga d'archivio fitta, C una scheda alla volta con "a caso"; liberi di proporne altri piu' forti).
  2. Su ogni scheda: SOLO titolo, categoria, numero identificativo (es. N° 014). NIENTE incipit, niente data in primo piano.
  3. Categorie: "capiamo in diversi modi" = ogni mockup tratta le categorie in un modo diverso (es. filtro che abbassa di luce le altre schede, un indice a parte, un gesto/mazzo), sempre come "in piu".
  4. Header/nav: POCHE voci, su questo stile (immagine di riferimento): voci scritte a mano, ciascuna fra PARENTESI QUADRE, tipo [ABOUT] [WORK] [LINKS], centrate, barra chiara con ombra leggera. Da ADATTARE al sito notturno (non copiare il chiaro). Mia proposta voci: [A CASO] [CERCA] [CATEGORIE] [CHI SONO]; Dalle canzoni e TikTok diventano categorie. Font a mano: valutare Balligesta (finora solo firme) o altro; verificare accenti.
  5. NON ANCORA RISPOSTO: intro e hero con luna restano? Default assunto (da confermare): si', la luna+titolo sono la prima schermata e l'archivio inizia subito sotto.
- Resta valido: monogramma t+luna (`mockups/logo/monogramma-*.svg`), home 15b come base della hero, palette #072D59/#DBF2FC/#FD6E88, font Fibonacci Corsivo (wordmark), Newsreader (lettura), Vetro/Balligesta da rivalutare.
- PROSSIMO PASSO (sessione nuova, `/clear` prima): costruire `mockups/16-teloscrivo-archivio-tre-modi.html` = 3 mockup della home-archivio (stessa hero 15b + monogramma in alto a sinistra + nav a parentesi quadre in 3 declinazioni coerenti col logo) con interruttori Mobile/Desktop. Poi blocco 2 del grill (pagina del singolo testo, ricerca, mobile). Ricordare: il file 16 era prima riservato all'intro luna->monogramma, che e' sospesa: chiamare questo 17 se serve.

## 03/11/2026 (pomeriggio) - SVOLTA: il sito 17 NON convince, nuovo riferimento = i CONCEPT DEI POST
- Tomas su 17 (Mosaico/Registro/Faldoni): "il sito non mi convince". Mi manda i concept dei post che vuole fare: `~/Downloads/quote/1.png ... 5.png` (1296x1620, 4:5).
- Cosa sono: 1-2 = stessa frase ("Guardarsi allo specchio puo' portarci a dubitare di quello che vediamo.") su bianco e su blu #072D59; sans geometrico tipo Poppins Light, UNA parola ("dubitare") evidenziata come testo selezionato su telefono con maniglie rosa. 3 = cielo rosa con luna sottile + serif nero + selezione iOS blu col menu "Copy / Select All / Look Up". 4-5 = frase ("Ed e' quel bacio che scocca mentre stai ridendo...") in Roboto Condensed bianco/blu, giustificata con buchi grandi tra le parole (da chiarire se voluta). Tutti: monogramma t+luna in alto a sinistra (nel 1-2), wordmark "teloscrivo." in Fibonacci in basso.
- Lettura mia: identita' = sobria, editoriale, bianco/blu pieno, UN gesto firma = "testo selezionato". Il sito 17 (notte, luna, voci a mano, Vetro) parla un'altra lingua.
- Domande aperte a Tomas (con mia raccomandazione): 1 sito parte da bianco/blu pieno, luna solo eccezione; 2 "testo selezionato" come firma del sito; 3 font dei post (Poppins + Roboto Condensed) al posto di Vetro/Balligesta/Newsreader, Fibonacci solo wordmark; 4 archivio = griglia dei post 4:5 alternati bianco/blu; 5 intro luna sospesa. Piu' dubbio sulla giustificazione dei post 4-5.
- NON riusare 17 come base visiva (restano utili: struttura dati archivio, filtri per categoria, sticky bar). Prossimo: dopo le risposte, mockup 18 che parte dai post.

## 03/11/2026 (pomeriggio, 2) - RISPOSTE di Tomas al blocco 1 (post come riferimento)
1. Colori: quelli che ho gia' (#DBF2FC, #072D59, #FD6E88), ma la STRUTTURA del sito 17 non convince (non ha detto quale parte: da chiedere).
2. "Testo selezionato" come firma del sito: "potrebbe essere un'idea" (si, ma non ancora deciso come).
3. Font dei post OK: Poppins (post 1-2) e Roboto Condensed (post 4-5), Fibonacci per il wordmark. (Vetro/Balligesta/Newsreader/voci a parentesi: archiviati.)
4. Archivio come griglia dei post: NO. "Qua gestiamo in modo diverso: voglio gestire sempre i testi con lo scroll."
5. Intro luna: sospesa (si).
- Aperto (blocco 2): cosa non convince della struttura; come funziona "i testi con lo scroll"; categorie dentro un flusso; fondi bianco/blu; cornice fissa (monogramma alto sx, wordmark basso) come nei post.

## 03/11/2026 (pomeriggio, 3) - DECISIONI blocco 2 (da qui si riparte, mockup 18)
- **Intestazione/hero**: deve COLPIRE e piacere: "intrigante e viva, con i colori" (usare i 3 colori), tono "profondo", e Tomas ha scritto "senza di graffiante ma profonda" (DUBBIO mio: forse "non graffiante, ma profonda": confermare). Non vuole "impostato". Non e' una copia dei post.
- **Lettura**: il testo (poesia o altro) si legge SCORRENDO, per dare movimento e piacere nella lettura. Idea scroll: testo legato alla posizione, reversibile, rispetta prefers-reduced-motion. Vuole sfruttare lo stile dei due post 1-2 e 4-5: bianco e blu #072D59, testo GIUSTIFICATO (anche coi buchi larghi tra le parole, da valutare se resta voluto), font Poppins / Roboto Condensed.
- **Testo selezionato** (parola rosa con maniglie) = idea buona ma non ancora decisa come usarla.
- **Categorie**: Testi, Poesie, Racconti brevi, Dalle canzoni = categorie. **TikTok NON e' una categoria: e' una SEZIONE del sito**, ancora senza profilo TikTok: "vediamo come verrebbe" (mostrarla nel mockup con contenuti d'esempio, senza link veri).
- **Fondi bianco/blu**: "dipende, sul sito non sara' come nei post, o anche si, valutiamo": provare sia alternati allo scroll sia fissi.
- **Cornice fissa** (monogramma alto sx + wordmark basso): "non so, non voglio la stessa cosa dei post, voglio il sito meno impostato" -> NON copiare l'impaginazione dei post; solo il linguaggio (colori, font, giustificato, selezione).
- Struttura del 17 (hero + archivio a schede + nav a parentesi) = scartata. Non ha detto quale singola parte; basta: si riparte.
- **PROSSIMO PASSO (chat nuova, /clear prima)**: `mockups/18-teloscrivo-intestazioni-e-lettura.html` = (A) 3 INTESTAZIONI diverse e vive (non impostate, coi 3 colori, nessuna notte/luna come base, monogramma t+luna), mobile+desktop; (B) una pagina di LETTURA a scroll con testo giustificato bianco/blu, parola selezionata che si evidenzia con lo scroll; (C) accenno alla sezione TikTok. Prima del mockup: breve /grill-me per chiarire "senza graffiante ma profonda" e cosa vuol dire "meno impostato" per lui (esempi di siti/riviste che gli piacciono, se ne ha). Aprire in ARC, finestra nuova.

## 03/11/2026 (sera) - RISPOSTE al blocco 1 del grill (prima del mockup 18)
1. Tono = **graffiante E profondo** (non "non graffiante": chiarito da Tomas). Intimo, notturno nel sentire, ma con il colore a dare vita.
2. "Meno impostato" = qualcosa di **unico**: stile **archivio personale** che pero' fa **sentire a casa** chi legge. Niente cosa classica/impostata (niente cornice fissa, niente griglia simmetrica). Riferimenti reali: nessuno dato, si procede senza.
3. Fondi bianco/blu nella lettura: **alternati mentre si scorre** (mockup con interruttore alternati/fisso).
4. Testo giustificato: sillabazione automatica (`lang="it"`, `hyphens:auto`); buchi larghi solo di proposito su una frase-citazione.
5. Parola selezionata rosa con maniglie: nella lettura, si evidenzia da sola a meta' schermo. Non nell'hero.
- Blocco 2 del grill (da fare): testi d'esempio, come si naviga tra i testi, forma della sezione TikTok.

## 03/11/2026 (sera, 2) - RISPOSTE blocco 2 + mockup 18 costruito
- Risposte di Tomas al blocco 2: casa/archivio ok (note a margine, N° d'archivio, con misura); navigazione = **3 mockup diversi** (non uno solo); testi d'esempio ok (graffianti); TikTok = 3 card 9:16 con link finti; file unico con interruttori.
- File: `mockups/18-teloscrivo-archivio-tre-modi.html`. Interruttori: Direzione (A Diario / B Tavolo / C Indice vivo), Mobile/Desktop, Vista (Home / Lettura / TikTok / Menu aperto), Fondo lettura (Alternato / Fisso). Scorciatoie: `#B-d-home`, `#C-m-lettura`, `#A-m-home-menu`, `#B-m-home-s500` (s = scroll in px).
- A Diario: hero rosa con titolo enorme ("Quello che a voce ~~non so~~ dire"), poi flusso di fasce luce/blu/rosa con titoli giganti che scorrono di lato con lo scroll; note a margine ruotate. B Tavolo: hero chiara con parola selezionata rosa (maniglie), titoli sparsi e inclinati su carta, TRASCINABILI; tocco = apre la lettura; barra in basso. C Indice vivo: blu, righe-titolo che si accendono al centro schermo (barra rosa + prima riga del testo), "MENU" verticale a destra.
- Categorie = filtro in piu': A attenua le altre fasce, B evidenzia in rosa e sfoca le altre, C chiude le altre righe.
- Lettura: testo giustificato Poppins con sillabazione, una frase alla volta si accende con lo scroll (reversibile), fondo che passa da luce a blu, citazione in Roboto Condensed con buchi larghi voluti, parola "sbagliare" che si evidenzia rosa, barra di avanzamento, monogramma che cambia colore col fondo.
- Menu aperto in 3 modi: A schermata rosa a tutta altezza, B foglio che sale dal basso, C pannello a destra.
- Verificato con screenshot headless Brave (mobile 390 e desktop 1280, home x3, lettura, TikTok, menu x3). NON provato a mano: trascinamento B, clic sui titoli, filtri categorie, fondo "Fisso", reduced-motion, scroll fluido nel tempo. Testi, numeri, note, link TikTok = ESEMPIO. Luna/intro: sospese.
- PROSSIMO: Tomas prova (Arc, finestra nuova) e dice quale direzione (A/B/C o mix) e cosa non va; poi /ui-check completo, scelta definitiva, testi veri, checklist-sito, costruzione vera.
