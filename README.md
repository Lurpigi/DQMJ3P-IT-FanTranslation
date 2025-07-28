# DQMJ3P – Italian Fan Translation

<p align="center">
    <img src="icon.png" alt="DQMJ3P Icon" width="400"/>
</p>

**_Dragon Quest Monsters: Joker 3 Professional_**

📊 **Stato della traduzione principale**: 18% (85/457 files)

📊 **Stato della traduzione update**: 18% (4/22 files)

# IT

Questo repository è dedicato allo sviluppo di una traduzione amatoriale in italiano per _Dragon Quest Monsters Joker 3 Professional_:

> Questo progetto fornisce esclusivamente file di patch `.mes`. Nessun contenuto protetto da copyright  
> è incluso, nel rispetto della legalità.

---

## 🧩 Installazione della Mod su Emulatore

### ✅ Requisiti

- Emulatore compatibile:  
  🔸 [Lime3DS-DQMJ3P](https://github.com/Lurpigi/lime3ds-dqmj3p) **(consigliato)**  
  🔸 Citra `nightly-1543` o precedente
- Aggiornamento del gioco `v1.3` (`CIA`)

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

- [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9)

### 🔧 Passaggi

1. Apri **HackingToolkit3DS** e estrai la tua ROM `.3ds` o `.cia`
2. Quando richiesto: seleziona **No** per non decomprimere il `code.bin`
3. Vai nella cartella `ExtractedRomFS/data`
4. Copia lì dentro i file della patch
5. Torna a HackingToolkit3DS e scegli **Rebuild**
6. Ripeti l’intero processo anche per l’aggiornamento `1.3`

🎮 Ora puoi caricare la ROM patchata e goderti il gioco in italiano!
