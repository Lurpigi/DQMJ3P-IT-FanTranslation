# DQMJ3P – Italian Fan Translation

**_Dragon Quest Monsters: Joker 3 Professional_**

📊 **Stato della traduzione principale**: 9% (45/457 files)

📊 **Stato della traduzione update**: 0% (0/22 files)

# IT

Questo repository è dedicato allo sviluppo di una traduzione amatoriale in italiano per _Dragon Quest Monsters Joker 3_:

> Questo progetto fornisce esclusivamente file di patch `.mes`. Nessun contenuto protetto da copyright  
> è incluso, nel rispetto della legalità.

---

## 🧩 Installazione della Mod su Emulatore

### ✅ Requisiti

-   Emulatore compatibile:  
    🔸 [Lime3DS-DQMJ3P](https://github.com/Lurpigi/lime3ds-dqmj3p) **(consigliato)**  
    🔸 Citra `nightly-1543` o precedente
-   Aggiornamento del gioco `v1.3` (`CIA`)

---

### 🛠️ Istruzioni

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

4. Estrai il contenuto della patch nella cartella `romfs/`  
   ⚠️ Prima la patch **principale**, poi l’**aggiornamento**
5. Avvia il gioco. La mod dovrebbe essere attiva! 🎉

---

## 🧪 Istruzioni per Patchare la ROM Originale

> ⚠️ **Nota:** Hai bisogno di una ROM `.3ds` o `.cia` **decriptata**  
> Cerca online come effettuare il dump del gioco in tuo possesso.

### 📦 Strumenti necessari

-   [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9)

### 🔧 Passaggi

1. Apri **HackingToolkit3DS** e estrai la tua ROM `.3ds` o `.cia`
2. Quando richiesto: seleziona **No** per non decomprimere il `code.bin`
3. Vai nella cartella `ExtractedRomFS/data`
4. Copia lì dentro i file della patch
5. Torna a HackingToolkit3DS e scegli **Rebuild**
6. Ripeti l’intero processo anche per l’aggiornamento `1.3`

🎮 Ora puoi caricare la ROM patchata su Citra e goderti il gioco in italiano!

---

# ENG

This repository provides an Italian fan translation for _Dragon Quest Monsters: Joker 3 Professional_.  
Only `.mes` patch files are included—**no copyrighted content**

---

## 🧩 Installing the Mod on Emulator

### ✅ Requirements

-   Emulator:  
    🔸 [Lime3DS-DQMJ3P](https://github.com/Lurpigi/lime3ds-dqmj3p) **(recommended)**  
    🔸 Citra `nightly-1543` or older
-   Update 1.3 `.CIA` file

---

### 🛠️ Instructions

1. Launch the emulator and install update `1.3` via **File → Install CIA…**
2. Right-click on `dqmj3p` → **Open mods location**
3. Create the folder structure below (if not present):

```
romfs/
└── data/
    ├── Font/
    ├── Message/
    ├── Script/
```

4. Extract the patch into `romfs/`  
   ⚠️ First the **main patch**, then the **update patch**
5. Run the game and enjoy the mod! 🎉

---

## 🧪 ROM Patching Instructions

> ⚠️ **Note:** You need a **decrypted** `.3ds` or `.cia` ROM.  
> Search online for guides on how to dump your own cartridge.

### 📦 Required Tool

-   [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9)

### 🔧 Steps

1. Open **HackingToolkit3DS** and extract your ROM
2. When prompted: choose **No** to avoid decompressing `code.bin`
3. Go to `ExtractedRomFS/data` and paste in the patch files
4. Reopen HackingToolkit3DS and select **Rebuild**
5. Repeat the process for both the base game and the update `1.3`

🎮 Load your new patched ROM in Citra and enjoy the game in Italian!
