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

> Questo progetto fornisce esclusivamente file di patch `.mes`. Nessun contenuto protetto da copyright è incluso, nel rispetto della legalità.

Link al video Tutorial su [YouTube](https://youtu.be/1YdTg-ZxD-M)

## 🆕 Novità

È disponibile anche la traduzione del gioco precedente, _Dragon Quest Monsters: Joker 2 Professional_: [DQMJ2P-IT-FanTranslation](https://github.com/Lurpigi/DQMJ2P-IT-FanTranslation)

## 📌 Premessa

Tradurre senza il contesto diretto del gioco è estremamente complicato.  
Spesso mi è capitato di rivedere e correggere testi già tradotti dopo averli testati in game, perché non suonavano bene o erano completamente fuori luogo.  
Mi scuso in anticipo per eventuali errori e incoerenze che potresti incontrare: finché non avrò provato ogni stringa nel contesto del gioco, **non posso garantire una traduzione adeguata al 100%**.

Continuerò a testare tutto in gioco, compatibilmente con il tempo disponibile, per migliorare costantemente la qualità della localizzazione.

### ⚠️ Limitazioni tecniche del gioco

- **Alcuni nomi di mostri non appaiono in combattimento.**  
  Questo sembra essere un bug o una limitazione del codice interno del gioco. Lo stesso problema è presente anche nella traduzione francese e in quella inglese, quindi non è possibile risolverlo al momento

- **Spazi di testo molto limitati.**  
  Alcune interfacce del gioco sono pensate per la lingua giapponese, che utilizza meno caratteri.  
  Di conseguenza, testi in italiano (o qualsiasi lingua occidentale) vengono **troncati** in alcune schermate, come ad esempio gli oggetti nel menu degli oggetti che invece non vengono troncati nel menù della libreria, quindi è una situazione abbastanza casuale. Anche qui, si tratta di una limitazione condivisa da tutte le altre traduzioni fan-made.

---

## 🚀 Vuoi contribuire?

Se vuoi aiutare con la traduzione, leggi la guida su come contribuire:  
👉 [contribute.md](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/blob/main/contribute.md)

---

# 🧩 Istruzioni per installare la Mod su 3DS

> ⚠️ è necessario avere un 3DS moddato con Luma3ds

1. Spegni il 3DS, tieni premuto il pulsante Select mentre riaccendi il 3DS (questo dovrebbe aprire il menù di configurazione) controlla che la voce **Enable game patching** sia attiva. poi premi Start per salvare e riavviare
2. Nella root della SD card crea il path `/luma/titles/00040000001ACB00/romfs`
3. Continua come mostrato nella guida per l'emulatore dal punto 4 (compreso) ma nella cartella `romfs` della SD

# 🧩 Installazione della Mod su Emulatore

### ✅ Requisiti

- Emulatore compatibile:  
  🔸 [Azahar](https://github.com/azahar-emu/azahar) **(consigliato)**  
  🔸 Oppure [Lime3DS-DQMJ3P](https://github.com/Lurpigi/lime3ds-dqmj3p) o Citra <= `nightly-1543`
  > Questi emulatori del 3ds sono quelli che funzionano meglio con questo gioco nello specifico, leggi [qui](https://github.com/Lurpigi/lime3ds-dqmj3p/blob/master/README.md) per maggiori info
- Aggiornamento del gioco `v1.3` (`CIA`)

- l'ultima versione della traduzione disponibile in release: [Download](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/releases/latest)

---

### 🛠️ Istruzioni

#### PC

1. Avvia l’emulatore e installa l’update `1.3` con **File → Install CIA…**
2. Nella lista delle ROM, fai clic destro su `dqmj3p` → **Open mods location**
3. Crea la seguente struttura di cartelle (se non esiste già):

```
romfs/
└── data/
    ├── Font/
    ├── Message/
    ├── Script/
```

#### Android

1. Installa il gioco e l'update `1.3` dal menù **Install CIA file**
2. Apri la cartella di root di Lime3ds con un qualsiasi gestore di file
3. Crea la seguente struttura di cartelle

```
Lime_root
└── load
    └── mods
        └── 00040000001ACB00
            └── romfs/
                └── data/
                    ├── Font/
                    ├── Message/
                    ├── Script/
```

#### Tutti

4. Estrai il contenuto della patch nella cartella `romfs/`  
   ⚠️ Prima la patch **principale**, poi l’**aggiornamento**
   (rispettivamente le cartelle `main_it/` e `update_it/`)
5. Avvia il gioco. La mod dovrebbe essere attiva! 🎉

---

# 🧪 Istruzioni per Patchare la ROM Originale

> ⚠️ **Nota:** Hai bisogno di una ROM `.3ds` o `.cia` **decriptata**  
> Cerca online come effettuare il dump del gioco in tuo possesso.

### 📦 Strumenti necessari

- [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9)

### 🔧 Passaggi

1. Apri **HackingToolkit3DS** e estrai la tua ROM `.3ds` o `.cia`
2. Quando richiesto: seleziona **No** per non decomprimere il `code.bin`
3. Vai nella cartella `ExtractedRomFS/data`
4. Copia lì dentro i file della patch
5. Torna a HackingToolkit3DS e scegli **Rebuild**
6. Ripeti l’intero processo anche per l’aggiornamento `1.3`

🎮 Ora puoi caricare la ROM patchata e goderti il gioco in italiano!

## 📚 Guide e Risorse

Per guide specifiche sul gioco, consulta la [Wiki del progetto](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/wiki).
