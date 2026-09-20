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

È disponibile anche la traduzione del gioco precedente, _Dragon Quest Monsters: Joker 2 Professional_: [DQMJ2P-IT-FanTranslation](https://github.com/Lurpigi/DQMJ2P-IT-FanTranslation)

## 🆕 Novità

### 20/09/26 - Patch exefs

Questa versione include una patch migrata dal progetto GitHub di **Akoi89** [DQMJ3P-english-fixed](https://github.com/Akoi89/DQMJ3P-english-fixed), che ringrazio infinitamente per avermi aiutato personalmente a portare la sua modifica anche per questa versione italiana

- la tastiera dei nomi apre direttamente la scheda alfabetica latina;
- alcuni buffer per nomi di mostri, abilità e azioni sono più grandi;
- diminuiscono i nomi troncati nei menu, nella Libreria e durante le battaglie;
- vengono corrette alcune condizioni che potevano causare crash o blocchi.

La patch tecnica modifica 153 word del codice dell'update, ma non cambia il formato dei salvataggi.


## 📌 Premessa

Tradurre senza il contesto diretto del gioco è estremamente complicato.
Spesso mi è capitato di rivedere e correggere testi già tradotti dopo averli testati in game, perché non suonavano bene o erano completamente fuori luogo.
Mi scuso in anticipo per eventuali errori e incoerenze che potresti incontrare: finché non avrò provato ogni stringa nel contesto del gioco, **non posso garantire una traduzione adeguata al 100%**.

Continuerò a testare tutto in gioco, compatibilmente con il tempo disponibile, per migliorare costantemente la qualità della localizzazione.

### ⚠️ Limitazioni tecniche del gioco, parzialmente risolti dalla patch exefs

- **Alcuni nomi di mostri non appaiono in combattimento.**
  Questo sembra essere un bug o una limitazione del codice interno del gioco. Lo stesso problema è presente anche nella traduzione francese e in quella inglese, quindi non è possibile risolverlo al momento.

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

~~~text
/luma/titles/00040000001ACB00/romfs/
~~~

3. Copia il contenuto di main_it/ dentro romfs/ e poi il contenuto di update_it/ nella stessa romfs/, unendo le cartelle e sostituendo i file.
4. Copia exefs/code.ips nella cartella della title ID, accanto a romfs/, rinominandolo code.ips se necessario.
5. Inserisci la SD nel 3DS, avvia il gioco e verifica la traduzione.

Su console il file IPS va quindi in:

~~~text
/luma/titles/00040000001ACB00/code.ips
~~~

La versione per emulatore usa invece la sottocartella exefs/ descritta nella sezione successiva.

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

~~~text
romfs/
└── data/
exefs/
~~~

#### Android

1. Installa il gioco e l'update 1.3 dal menù **Install CIA file**
2. Apri la cartella di root di Azahar con un qualsiasi gestore di file
3. Crea la seguente struttura:

~~~text
Azahar_root
└── load
    └── mods
        └── 00040000001ACB00
            ├── romfs/
            │   └── data/
            └── exefs/
~~~

#### Tutti

4. Estrai il contenuto della patch nella cartella romfs/: prima il contenuto della patch **principale** (main_it/), poi quello dell'**aggiornamento** (update_it/). Le cartelle vanno unite e i file dell'update devono sostituire quelli del main.
5. Copia exefs/code.ips nella cartella exefs/ che hai creato.
6. Avvia il gioco. La mod dovrebbe essere attiva! 🎉

⚠️ code.ips deve trovarsi nella cartella mod della title ID principale 00040000001ACB00. Non inserirlo nella cartella della title ID dell'update.

### Problemi comuni

- Installa sempre il gioco principale e l'aggiornamento v1.3 prima di attivare la mod.
- La struttura deve iniziare con romfs/data/; non deve diventare romfs/main_it/data/ o romfs/update_it/data/.
- Copia prima main_it/ e poi update_it/, unendo le cartelle nella stessa romfs/.
- Se il gioco resta in inglese, disattiva temporaneamente eventuali vecchie mod inglesi: una loro romfs può sovrascrivere i file italiani.
- Se la traduzione funziona ma i nomi restano troncati, controlla che code.ips sia dentro exefs/ della mod principale.

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
5. Se vuoi includere anche la patch tecnica, estrai l'ExeFS dell'update, decomprimi il suo .code/code.bin e applica exefs/code.ips con un patcher IPS. Non applicare questa patch al codice della versione principale.
6. Torna a HackingToolkit3DS e scegli **Rebuild** per il gioco e per l'aggiornamento.

🎮 Ora puoi caricare la ROM patchata e goderti il gioco in italiano!

La patch IPS va applicata soltanto al codice decompresso dell'update, non al codice della versione principale, ai file .mes o al RomFS. La title ID del gioco principale è 00040000001ACB00; quella dell'update è 0004000E001ACB00.

## Contenuti online

Per sbloccare contenuti che dipendevano da servizi ormai disattivati è disponibile il plugin di Anthcny:

[DQMJ3P Unobtainable Content](https://github.com/Anthcny144/DQMJ3P-unobtainable-content)

Il progetto è un plugin 3GX per DQMJ3 e DQMJ3P che può sbloccare contenuti legati a online, StreetPass, SpotPass, trasferimenti di mostri, dischi scaricabili, ricompense Wi-Fi, oggetti, abilità e titoli. Il README del plugin dichiara compatibilità con DQMJ3P 1.0 e 1.3 e con versioni tradotte o non tradotte, purché il codice del gioco non sia stato modificato.

Il plugin è indipendente da questa traduzione e va scaricato dalla sua [pagina Releases](https://github.com/Anthcny144/DQMJ3P-unobtainable-content/releases). Per l'installazione e l'elenco completo dei contenuti sbloccabili seguire il [README ufficiale del plugin](https://github.com/Anthcny144/DQMJ3P-unobtainable-content#readme).

> ⚠️ Questa traduzione include exefs/code.ips, quindi il codice dell'update viene modificato. Il progetto inglese ha verificato che gli indirizzi usati dal plugin non risultano modificati e ritiene possibile la coesistenza, ma non è stata eseguita una prova completa con il plugin attivo. In caso di problemi, testare prima il plugin e la traduzione separatamente.


## 📚 Guide e Risorse

- Per guide specifiche sul gioco, consulta la [Wiki del progetto](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/wiki).
- [Plugin DQMJ3P Unobtainable Content di Anthcny](https://github.com/Anthcny144/DQMJ3P-unobtainable-content)
- [DQMJ3P English Fixed di Akoi89](https://github.com/Akoi89/DQMJ3P-english-fixed)

## 🙏 Ringraziamenti

Grazie ad **Anthcny** per il plugin [DQMJ3P-unobtainable-content](https://github.com/Anthcny144/DQMJ3P-unobtainable-content), che permette di recuperare contenuti legati a funzioni online non più disponibili.

Un ringraziamento anche ad **Akoi89** e ai collaboratori di DQMJ3P English Fixed per le analisi tecniche, ad **oho** per la guida alla preparazione dei CIA, al Joker 3 Translation Team e a tutte le persone che hanno testato e migliorato i progetti della comunità.

[server Discord English patch](https://discord.com/invite/W5yRJpDd5e)
