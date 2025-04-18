# DQMJ3p Fan Translation

Traduzione completata: 19%

# IT

Questo repository è dedicato allo sviluppo di una traduzione amatoriale in italiano per _Dragon Quest Monsters Joker 3: Professional_. Contiene solo file di patch `.mes`, garantendo che nessun materiale protetto da copyright venga condiviso.

## Installazione della Mod per DQMJ3P

<h3>Emulatore</h3>

1. Puoi utilizzare la mia versione di [Lime3DS](https://github.com/Lurpigi/lime3ds-dqmj3p) o Citra 1543 (o una versione precedente).
2. Installa l'aggiornamento 1.3 tramite **File** → **Install CIA…**.
3. Fai clic destro su `dqmj3p` nella lista delle ROM e apri la cartella **mods location**.
4. Crea la cartella `romfs/data`.
5. Estrai tutti i dati della patch nella cartella `romfs` (prima la patch principale, poi la patch di aggiornamento).
6. La struttura delle cartelle dovrebbe essere la seguente:

```
romfs/
└── data/
    ├── Font/
    ├── Message/
    ├── Script/
```

7. Avvia il gioco e goditi la mod!

<h3>Istruzioni per patchare la ROM</h3>

1. Ottieni una ROM `.3ds` o `.cia` decriptata (cerca online come effettuare il dump del gioco).
2. Scarica e apri [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9).
3. Usa HackingToolkit3DS per estrarre un file `.3ds` o `.cia`.
4. Quando richiesto, seleziona **No** per non decomprimere il `code.bin`.
5. Vai nella cartella `ExtractedRomFS/data` e copia lì i file della patch.
6. Apri nuovamente HackingToolkit3DS e seleziona **Rebuild** per creare una nuova ROM `.3ds` o `.cia` patchata.
7. Ripeti questi passaggi sia per il gioco base che per l'aggiornamento 1.3.

Una volta terminato, puoi caricare la ROM patchata in Citra e giocare con la mod installata!

# Eng

This repository is dedicated to developing an Italian fan translation for _Dragon Quest Monsters Joker 3: Professional_. It contains only `.mes` patch files, ensuring no copyrighted material is shared.

## Installing the Mod for DQMJ3P

<h3>Emulator</h3>

1. You can use my version of [Lime3DS](https://github.com/Lurpigi/lime3ds-dqmj3p) or Citra 1543 (or older version).
2. Install update 1.3 via **File** → **Install CIA…**.
3. Right-click on `dqmj3p` in the ROM list and open the **mods location** folder.
4. Create the `romfs/data` folder.
5. Extract all patch data into the `romfs` folder (first the main patch, then the update patch).
6. The folder structure should look like this:

```
romfs/
└── data/
    ├── Font/
    ├── Message/
    ├── Script/
```

7. Launch the game and enjoy the mod!

<h3>Instructions for patching the ROM</h3>

1. Obtain a decrypted `.3ds` or `.cia` ROM (search online for how to dump the game).
2. Download and open [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9).
3. Use HackingToolkit3DS to extract a `.3ds` or `.cia` file.
4. When prompted, select **No** to decompress the `code.bin`.
5. Go to the `ExtractedRomFS/data` folder and copy the patch files there.
6. Open HackingToolkit3DS again and select **Rebuild** to create a new patched `.3ds` or `.cia` ROM.
7. Repeat these steps for both the base game and the 1.3 update.

Once finished, you can load the patched ROM into Citra and play with the mod installed!
