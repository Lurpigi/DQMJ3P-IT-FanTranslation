# DQMJ3P – 🇮🇹 Italian Fan Translation

[![](https://img.shields.io/github/v/release/Lurpigi/DQMJ3P-IT-FanTranslation?include_prereleases&label=Release)](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/releases/latest)
[![](https://img.shields.io/github/downloads/Lurpigi/DQMJ3P-IT-FanTranslation/total.svg)](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/releases)

<p align="center">
    <img src="icon.png" alt="DQMJ3P Icon" width="400"/>
</p>

**_Dragon Quest Monsters: Joker 3 Professional_**

📊 **Stato della traduzione principale**: 100% (457/457 files)

📊 **Stato della traduzione update**: 100% (22/22 files)

---

Questo repository è dedicato allo sviluppo di una traduzione amatoriale in italiano per _Dragon Quest Monsters Joker 3 Professional_:

> Questo progetto fornisce file di patch .mes, font, layout e una piccola patch IPS per l'eseguibile. Nessun gioco completo o contenuto protetto da copyright è incluso, nel rispetto della legalità.

Link al video Tutorial su [YouTube](https://youtu.be/1YdTg-ZxD-M)

### È disponibile anche la traduzione del gioco precedente, _Dragon Quest Monsters: Joker 2 Professional_: [DQMJ2P-IT-FanTranslation](https://github.com/Lurpigi/DQMJ2P-IT-FanTranslation)

## 🆕 Novità

### 06/11/26 - DQMJ3P Online

Entrambi i file IPS includono ora il collegamento ai server sostitutivi di [DQMJ3P Online](https://github.com/Lurpigi/DQMJ3P-Online), mantenendo le correzioni della traduzione:

- battaglie Wi-Fi libere e classificate, comunità e comunità ufficiali per lingua;
- G-Cup (Corsa in classifica) e Grand Prix, con classifiche e ricompense;
- codici regalo originali, dischi regalo e inventario del negozio a monete della Piazza Wi-Fi;
- nella versione Enhanced, correzioni specifiche per le richieste HTTP e l'invio dei replay su Azahar.

Con questi IPS serve un account Pretendo per il login di sistema, anche per le funzioni diverse dalle battaglie tra amici. I servizi di gioco sono gestiti dai server di DQMJ3P Online. Consulta [DQMJ3P Online: configurazione e limiti](#dqmj3p-online-configurazione-e-limiti) qui sotto.

### 16/10/26 - Fix dalla patch inglese v2.21

Questa versione include una patch migrata dal progetto GitHub [DQMJ3P-english-fixed](https://github.com/Akoi89/DQMJ3P-english-fixed):

- la tastiera dei nomi apre direttamente la scheda alfabetica latina;
- alcuni buffer per nomi di mostri, abilità e azioni sono più grandi;
- diminuiscono i nomi troncati nei menu, nella Biblioteca e durante le battaglie;
- vengono corrette alcune condizioni che potevano causare crash o blocchi.
- i nomi lunghi di alcuni boss usano forme brevi in battaglia, entro il limite di 11 caratteri;

## 📌 Premessa

Tradurre senza il contesto diretto del gioco è estremamente complicato.
Spesso mi è capitato di rivedere e correggere testi già tradotti dopo averli testati in game, perché non suonavano bene o erano completamente fuori luogo.
Mi scuso in anticipo per eventuali errori e incoerenze che potresti incontrare: finché non avrò provato ogni stringa nel contesto del gioco, **non posso garantire una traduzione adeguata al 100%**.

Continuerò a testare tutto in gioco, compatibilmente con il tempo disponibile, per migliorare costantemente la qualità della localizzazione.

### ⚠️ Limitazioni tecniche del gioco, parzialmente risolti dalla patch exefs

- **Alcuni nomi di mostri possono essere troncati in combattimento.**
  La patch exefs risolve il caso dei mostri selvatici che restavano senza nome e amplia alcuni buffer dei pannelli. Possono comunque rimanere tagli in schermate non ancora coperte dalla patch, soprattutto con nomi italiani molto lunghi.

- **Spazi di testo molto limitati.**
  Alcune interfacce del gioco sono pensate per la lingua giapponese, che utilizza meno caratteri.
  Di conseguenza, testi in italiano (o qualsiasi lingua occidentale) vengono **troncati** in alcune schermate, come ad esempio gli oggetti nel menu degli oggetti che invece non vengono troncati nel menù della libreria, quindi è una situazione abbastanza casuale. Anche qui, si tratta di una limitazione condivisa da tutte le altre traduzioni fan-made.

---

## 🚀 Vuoi contribuire?

Se vuoi aiutare con la traduzione, leggi la guida su come contribuire:
👉 [contribute.md](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/blob/main/contribute.md)

# 🧩 Istruzioni per installare la Mod su 3DS

> ⚠️ È necessario avere un 3DS modificato con [Luma3DS](https://github.com/LumaTeam/Luma3DS).

1. Spegni il 3DS e tieni premuto **Select** mentre lo riaccendi per aprire il menu di configurazione di Luma3DS. Controlla che **Enable game patching** sia attivo, poi premi **Start** per salvare.
2. Nella root della scheda SD crea questa cartella:

```text
/luma/titles/00040000001ACB00/romfs/
```

3. Copia il contenuto di main_it/ dentro romfs/ e poi il contenuto di update_it/ nella stessa romfs/, unendo le cartelle e sostituendo i file.
4. Copia exefs/code.ips nella cartella della title ID, accanto a romfs/, rinominandolo code.ips se necessario.
5. Inserisci la SD nel 3DS, avvia il gioco e verifica la traduzione.

Su console il file IPS va quindi in:

```text
/luma/titles/00040000001ACB00/code.ips
```

La versione per emulatore usa invece la sottocartella exefs/ descritta nella sezione successiva.

⚠️ Su console usa sempre exefs/code.ips: exefs/code_enhanced.ips è solo per emulatore.

# 🧩 Installazione della Mod su Emulatore

### ✅ Requisiti

- Emulatore compatibile:
  🔸 [Azahar](https://github.com/azahar-emu/azahar) **(consigliato)**
  🔸 Oppure [Lime3DS-DQMJ3P](https://github.com/Lurpigi/lime3ds-dqmj3p) o Citra <= nightly-1543
  > Questi emulatori del 3DS sono quelli che funzionano meglio con questo gioco nello specifico; leggi [qui](https://github.com/Lurpigi/lime3ds-dqmj3p/blob/master/README.md) per maggiori informazioni.
- Aggiornamento del gioco v1.3 (CIA)
- L'ultima versione della traduzione disponibile in [release](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/releases/latest)

---

### 🛠️ Istruzioni

#### PC

1. Avvia l'emulatore e installa l'update 1.3 con **File → Install CIA…**
2. Nella lista delle ROM, fai clic destro su dqmj3p → **Open Mods Location**
3. Crea la seguente struttura di cartelle, se non esiste già:

```text
romfs/
└── data/
exefs/
```

#### Android

1. Installa il gioco e l'update 1.3 dal menù **Install CIA file**
2. Apri la cartella di root di Azahar con un qualsiasi gestore di file
3. Crea la seguente struttura:

```text
Azahar_root
└── load
    └── mods
        └── 00040000001ACB00
            ├── romfs/
            │   └── data/
            └── exefs/
```

#### Tutti

4. Estrai il contenuto della patch nella cartella romfs/: prima il contenuto della patch **principale** (main_it/), poi quello dell'**aggiornamento** (update_it/). Le cartelle vanno unite e i file dell'update devono sostituire quelli del main.
5. Copia nella cartella exefs/ che hai creato **uno solo** dei due file della patch:
   - exefs/code.ips, la versione normale;
   - exefs/code_enhanced.ips, rinominandolo code.ips, se il tuo PC o Android è potente (vedi [Versione Enhanced](#-versione-enhanced-solo-emulatore)).
6. Avvia il gioco. La mod dovrebbe essere attiva! 🎉

⚠️ code.ips deve trovarsi nella cartella mod della title ID principale 00040000001ACB00, anche se il codice corretto appartiene all'update 0004000E001ACB00. Non inserirlo nella cartella della title ID dell'update.

### ⚡ Versione Enhanced (solo emulatore)

La release contiene due patch del codice:

| File | Dove si usa | Contenuto |
| --- | --- | --- |
| exefs/code.ips | 3DS ed emulatore | Correzioni dei testi e collegamento a DQMJ3P Online; su Azahar l'online richiede i fix della Enhanced |
| exefs/code_enhanced.ips | Solo emulatore, su PC o Android potenti | Le stesse correzioni e il collegamento online, più i fix per Azahar e i miglioramenti elencati qui sotto |

Per usarla, copia exefs/code_enhanced.ips nella cartella exefs/ della mod e **rinominalo code.ips**: l'emulatore carica solo un file con questo nome.

Cosa aggiunge:

- **Distanza di visibilità x5** per mostri, NPC e oggetti, per ridurre il pop-in.
- **Animazioni fluide dei mostri lontani**, che nel gioco originale vengono aggiornate a scatti.
- **60 fps nelle battaglie a velocità x2.**
- **Passaggi di dettaglio della mappa più gradevoli**, con i tile migliori mantenuti un po' più a lungo.
- **Più memoria per i modelli**, necessaria per gestire i mostri in più.
- **Fix online per Azahar**: richieste SIL senza contenuto, lettura degli header di risposta e invio dei replay G-Cup in un solo blocco.

Cosa sapere prima di usarla:

- **Non usarla su 3DS.**
- Serve la **modalità New 3DS** attiva nelle impostazioni di sistema dell'emulatore. Senza, i mostri restano alla distanza originale.
- I 60 fps valgono **solo nelle battaglie a velocità x2**. Nel resto del gioco la logica è legata ai frame: sbloccarli renderebbe tutto due volte più veloce, quindi resta a 30 fps.
- Con più mostri in scena l'emulatore lavora di più. Se il gioco rallenta, torna a exefs/code.ips.
- È stata provata su Azahar per PC, non ancora su Android.

### Problemi comuni

- Installa sempre il gioco principale e l'aggiornamento v1.3 prima di attivare la mod.
- La struttura deve iniziare con romfs/data/; non deve diventare romfs/main_it/data/ o romfs/update_it/data/.
- Copia prima main_it/ e poi update_it/, unendo le cartelle nella stessa romfs/.
- Se il gioco resta in inglese, disattiva temporaneamente eventuali vecchie mod inglesi: una loro romfs può sovrascrivere i file italiani.
- Se la traduzione funziona ma i nomi restano troncati, controlla che code.ips sia dentro exefs/ della mod principale.
- Se la versione enhanced sembra non avere effetto, controlla di averla rinominata code.ips e che la modalità New 3DS sia attiva.

---

# 🧪 Istruzioni per Patchare la ROM Originale

> ⚠️ **Nota:** Hai bisogno di una ROM .3ds o .cia **decriptata**.
> Cerca online come effettuare il dump del gioco in tuo possesso.

### 📦 Strumenti necessari

- [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9)
- [Lunar IPS (LIPS)](https://fusoya.eludevisibility.org/lips/), patcher IPS per Windows consigliato per applicare code.ips.

### 🔧 Passaggi

1. Apri **HackingToolkit3DS** ed estrai la ROM .3ds o .cia.
2. Per la sola sostituzione dei file del RomFS, quando richiesto seleziona **No** per non decomprimere il code.bin.
3. Vai nella cartella ExtractedRomFS/data.
4. Per il gioco principale copia lì dentro il contenuto di main_it/; ripeti per l'update usando update_it/.
5. Se vuoi includere anche la patch tecnica, estrai l'ExeFS dell'update, decomprimi il suo .code/code.bin e applica exefs/code.ips con un patcher IPS. Non applicare questa patch al codice della versione principale. Usa exefs/code_enhanced.ips al suo posto solo se la ROM è destinata a un emulatore.
6. Torna a HackingToolkit3DS e scegli **Rebuild** per il gioco e per l'aggiornamento.

🎮 Ora puoi caricare la ROM patchata e goderti il gioco in italiano!

La patch IPS va applicata soltanto al codice decompresso dell'update, non al codice della versione principale, ai file .mes o al RomFS. La title ID del gioco principale è 00040000001ACB00; quella dell'update è 0004000E001ACB00.

## Contenuti online

### DQMJ3P Online: configurazione e limiti

I due IPS della traduzione includono già la patch del progetto [DQMJ3P Online](https://github.com/Lurpigi/DQMJ3P-Online), che ripristina le funzioni online tramite server sostitutivi. Installa **l'update 1.3** e usa un solo `code.ips`, nel percorso descritto sopra: non occorre sovrapporre un'altra patch online.

**A cosa serve Pretendo:** gli IPS attuali mantengono il login al servizio amici di sistema (`frd`), da cui il gioco ricava l'ID del giocatore e la credenziale usata per autenticarsi ai server sostitutivi. Questo passaggio serve anche per battaglie casuali, comunità e G-Cup; la patch usa una credenziale derivata dalla stessa fonte anche per Grand Prix e codici regalo. Il nome «servizio amici» non indica quindi soltanto la modalità di battaglia tra amici. I download SpotPass arrivano direttamente dal server del progetto, ma questi IPS mantengono il login di sistema nel percorso di connessione del gioco.

- **Su 3DS:** configura [Pretendo con Nimbus](https://pretendo.network/docs/install/3ds), attiva il tuo account Pretendo e usa `exefs/code.ips` con **Enable game patching** attivo in Luma3DS.
- **Su Azahar:** segui la [guida Pretendo per Azahar](https://pretendo.network/docs/install/citra), configura il tuo account e i moduli di sistema online **LLE**, poi usa `exefs/code_enhanced.ips`, rinominato `code.ips`. La patch normale resta utilizzabile per la traduzione su emulatore, ma non contiene i fix HTTP necessari per queste funzioni online. La configurazione online è stata verificata dal progetto su Azahar; non è stata verificata su Android o sugli altri emulatori elencati sopra.
- Avvia il gioco ed entra nella **Piazza Wi-Fi**.

Stato delle funzioni riportato dal progetto DQMJ3P Online:

| Funzione | Stato |
| --- | --- |
| Battaglie libere e classificate | Verificate tra due istanze Azahar e tra 3DS e Azahar |
| Battaglie con amici | Implementate; resta da verificare con due account registrati reciprocamente come amici |
| Creazione comunità, comunità ufficiali per lingua, comunità in evidenza e Sfida comunità | Verificate |
| G-Cup: coppe settimanali, classifiche, replay e ricompense | Verificato |
| Grand Prix: Masters e Challenger, classifiche e ricompense | Verificato |
| Tutti i 130 codici regalo originali | Verificati lato server |
| Dischi regalo e negozio a monete della Piazza Wi-Fi | Verificati |
| Eventi SpotPass sul campo: scatola nascosta, mostro della mappa celeste e sicario StreetPass | Solo la scatola nascosta è stata verificata dal progetto; su Azahar i task in background non vengono eseguiti e questi IPS non ne forzano il download |

Le patch puntano al server pubblico di prova del progetto (`188.245.46.173`, con `78.47.138.100` per il secondo controllo NAT). La disponibilità delle funzioni dipende dal server. La nuova combinazione con questa versione della traduzione è stata verificata a livello di patch; resta da provarla in gioco.

Problemi noti:

- La conferma **«Gioco Salvato!»** può restare visibile per circa 30 secondi prima dell'ingresso nella Piazza Wi-Fi.
- Su Azahar una VPN può impedire di rilevare l'indirizzo locale e causare errori di comunicazione: disattivala durante la prova.
- Le battaglie collegano direttamente i giocatori (**P2P**), senza relay: reti con CGNAT o NAT simmetrico possono impedire l'avvio dello scontro.
- Se il login NEX viene rifiutato dopo un cambio di account Pretendo, chiedi all'amministratore del server di reimpostare l'associazione dell'ID.
- Se la Enhanced rallenta sul tuo dispositivo, usa la patch normale per giocare offline. Per l'online su Azahar senza i miglioramenti grafici, genera una patch con l'opzione `--azahar` del progetto DQMJ3P Online, unendola alla patch normale; non attivare due IPS insieme.

Per istruzioni e stato aggiornati consulta il [README di DQMJ3P Online](https://github.com/Lurpigi/DQMJ3P-Online#readme). Le correzioni Azahar vengono mantenute anche dallo script `scripts/build_enhanced_ips.py` quando rigenera la Enhanced dalla patch normale.

### Plugin per sbloccare contenuti non più ottenibili

Per sbloccare contenuti che dipendevano da servizi ormai disattivati è disponibile il plugin di Anthcny:

[DQMJ3P Unobtainable Content](https://github.com/Anthcny144/DQMJ3P-unobtainable-content)

Il progetto è un plugin 3GX per DQMJ3 e DQMJ3P che può sbloccare contenuti legati a online, StreetPass, SpotPass, trasferimenti di mostri, dischi scaricabili, ricompense Wi-Fi, oggetti, abilità e titoli. Il README del plugin dichiara compatibilità con DQMJ3P 1.0 e 1.3 e con versioni tradotte o non tradotte, purché il codice del gioco non sia stato modificato.

Il plugin è indipendente da questa traduzione e va scaricato dalla sua [pagina Releases](https://github.com/Anthcny144/DQMJ3P-unobtainable-content/releases). Per l'installazione e l'elenco completo dei contenuti sbloccabili seguire il [README ufficiale del plugin](https://github.com/Anthcny144/DQMJ3P-unobtainable-content#readme).

> ⚠️ Entrambi gli IPS di questa traduzione modificano il codice dell'update e ora includono anche DQMJ3P Online. La precedente verifica degli indirizzi svolta dal progetto inglese non copre queste aggiunte: la compatibilità del plugin con i nuovi IPS, normale ed Enhanced, non è stata verificata. In caso di problemi, testare prima il plugin e la traduzione separatamente.

## 📚 Guide e Risorse

- Per guide specifiche sul gioco, consulta la [Wiki del progetto](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/wiki).
- [DQMJ3P Online: server sostitutivi e guida alla configurazione](https://github.com/Lurpigi/DQMJ3P-Online)
- [Plugin DQMJ3P Unobtainable Content di Anthcny](https://github.com/Anthcny144/DQMJ3P-unobtainable-content)
- [DQMJ3P English Fixed di Akoi89](https://github.com/Akoi89/DQMJ3P-english-fixed)

## 🙏 Ringraziamenti

Grazie ad **Anthcny** per il plugin [DQMJ3P-unobtainable-content](https://github.com/Anthcny144/DQMJ3P-unobtainable-content), che permette di recuperare contenuti legati a funzioni online non più disponibili.

Un ringraziamento anche ad **Akoi89** e ai collaboratori di DQMJ3P English Fixed per le analisi tecniche, ad **oho** per la guida alla preparazione dei CIA, al Joker 3 Translation Team e a tutte le persone che hanno testato e migliorato i progetti della comunità.

[server Discord English patch](https://discord.com/invite/W5yRJpDd5e)
