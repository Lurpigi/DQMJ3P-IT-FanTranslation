# DQMJ3P – 🇮🇹 Italian Fan Translation - contribuisci anche tu

> Se vuoi contribuire alla traduzione, prima di tutto **grazie di cuore!**  
> Siamo una nicchia nella nicchia e supportarci a vicenda è una cosa preziosa.

Link al video Tutorial su [YouTube](https://www.youtube.com/watch?v=XKK9hgnbKWU)

# 📚 Come contribuire:

## 🧠 Requisiti di Base

Per partecipare attivamente è necessario conoscere **le basi di GitHub**, in particolare:

- Come creare una **fork** della repository
- Come **proporre modifiche** tramite una **pull request**

> IMPORTANTE: molto probabilmente dopo un push dovrai effettuare una pull per evitare merge conflict dato che ad ogni push di file `.mes` triggera delle action

Trovi moltissime guide online su questi concetti, anche video youtube fatti molto bene e facili da comprendere.

## 📁 Struttura della Repository

La repository è organizzata in diverse cartelle. Ecco una panoramica:

| Cartella   | Contenuto                                                                               |
| ---------- | --------------------------------------------------------------------------------------- |
| `eng/`     | File testuali originali in inglese (`.mes`), usati come base per la traduzione italiana |
| `it/`      | File tradotti in italiano (`.mes`) aggiornati                                           |
| `update/`  | File `.mes` aggiornati per l'**update 1.3** (sottocartelle `it/` e `eng/`)              |
| `legenda/` | Tabelle di riferimento per nomi di **mostri, abilità, tratti, luoghi e mosse**          |
| `json/`    | Cartella generata **automaticamente** via GitHub Action –                               |
| `scripts/` | Script utili **vedi sezione script**                                                    |

## 🔍 A cosa serve la cartella `json/`?

Questa cartella contiene una versione `.json` **di tutti i file `.mes`**, per `eng/`, `it/` e `update/`.

> ⚠️ **Pushare modifiche dei file json potrebbe non servire poiché verranno comunque sovrascritti da una Action per mantenerli aggiornati.**

Viene usata per:

- Fare **ricerche rapide** su stringhe specifiche usando, ad esempio, _Visual Studio Code_
- Trovare facilmente **in quale file** si trova una certa stringa

> Esempio: cercando `"Reclutamento riuscito!"` scoprirai che si trova in `BattleEventMessage.mes`, perché appare in `BattleEventMessage.json`.

- Modificare facilmente i file .mes senza programmi esterni usando uno script **vedi sezione script**

## 🧰 Strumenti consigliati

Per modificare i file `.mes`, usa questo programma creato da **LinkOFF7**:

🔗 [DragonQuestLoc – GitHub](https://github.com/LinkOFF7/DragonQuestLoc)

Questa fork permette di:

- **Importare/esportare** file `.mes`
- Convertire i `.mes` in **file `.txt` modificabili**
- **Mantenere i caratteri non stampabili**, necessari al funzionamento del gioco

> ❗ Quando modifichi i file `.mes`, **non rimuovere i caratteri speciali invisibili**: sono fondamentali per la corretta esecuzione in gioco.

### ✏️ Come salvare correttamente:

1. Importa il file `.mes`
2. Fai le modifiche necessarie
3. Premi `Update` (le modifiche compariranno nella colonna di destra)
4. Esporta il file `.mes` aggiornato

## 🧪 Script Utili

All'interno della cartella `scripts/` trovi alcuni tool utili:

- `formattazione.py`: riformatta un file `.txt` modificando i {CL} (newline) in base a una lunghezza massima (`max_len` Consulta [`note.md`](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/blob/main/note.md) per esempi e valori usati.)
- `json_to_mes.py`: usa i file `.json` italiani per aggiornare i file `.mes` italiani, in questo modo è possibile modificare i testi del gioco solo dai file Json senza usare applicazioni esterne
- `mes_to_json.py`: usa tutti i file `.mes` per generare e aggiornare tutti i file `.json`, è lo script usato dalla Action per mantenere i Json aggiornati
- `super_formattazione.py`: riformatta alcuni file Json italiani (menù e dialoghi) impostando la lunghezza delle righe (gli a capo per intenderci) adatte al contesto, non modifica i file `.mes`

per far runnare questi script hai bisogno di python 3 e poi facilmente tramite terminale:

```bash
python scripts/[nome].py
```

`formattazione.py` va runnato dentro la cartella scripts, mentre gli altri dalla root della repository

## 🤝 Contribuisci anche tu!

Se sei appassionato della saga, se ami l'idea di giocare a questo gioco in italiano, o se vuoi semplicemente dare una mano a un progetto della community, sei nel posto giusto.

Unisciti, esplora i file e **contribuisci con una pull request!**

Grazie ancora ❤️
