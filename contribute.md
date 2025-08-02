# DQMJ3P – 🇮🇹 Italian Fan Translation - contribuisci anche tu

> Se vuoi contribuire alla traduzione, prima di tutto **grazie di cuore!**  
> Siamo una nicchia nella nicchia, e supportarci a vicenda è una cosa preziosa.

---

# 📌 Premessa

Tradurre senza il contesto diretto del gioco è estremamente complicato.  
Spesso mi è capitato di rivedere e correggere testi già tradotti dopo averli testati in game, perché non suonavano bene o erano completamente fuori luogo.  
Mi scuso in anticipo per eventuali errori che potresti incontrare: finché non avrò provato ogni stringa nel contesto del gioco, **non posso garantire una traduzione perfetta al 100%**.

Continuerò a testare tutto in gioco, compatibilmente con il tempo disponibile, per migliorare costantemente la qualità della localizzazione.

## ⚠️ Limitazioni tecniche del gioco

- **Alcuni nomi di mostri non appaiono in combattimento.**  
  Questo sembra essere un bug o una limitazione del codice interno del gioco. Lo stesso problema è presente anche nella traduzione francese e in quella inglese, quindi non è possibile risolverlo al momento

- **Spazi di testo molto limitati.**  
  Alcune interfacce del gioco sono pensate per la lingua giapponese, che utilizza meno caratteri.  
  Di conseguenza, testi in italiano (o qualsiasi lingua occidentale) vengono **troncati** in alcune schermate, come ad esempio gli oggetti nel menu degli oggetti che invece non vengono troncati nel menù della libreria, quindi è una situazione abbastanza casuale. Anche qui, si tratta di una limitazione condivisa da tutte le altre traduzioni fan-made.

---

# 📚 Come contribuire

## 🧠 Requisiti di Base

Per partecipare attivamente è necessario conoscere **le basi di GitHub**, in particolare:

- Come creare una **fork** della repository
- Come **proporre modifiche** tramite una **pull request**

Trovi moltissime guide online su questi concetti, ma se hai dubbi puoi anche chiedere nei commenti della repo.

---

## 📁 Struttura della Repository

La repository è organizzata in diverse cartelle. Ecco una panoramica:

| Cartella   | Contenuto                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------- |
| `eng/`     | File testuali originali in inglese (`.mes`), usati come base per la traduzione italiana            |
| `it/`      | File tradotti in italiano (`.mes`) aggiornati                                                      |
| `update/`  | File `.mes` aggiornati per l'**update 1.3** (sottocartelle `it/` e `eng/`)                         |
| `legenda/` | Tabelle di riferimento per nomi di **mostri, abilità, tratti, luoghi e mosse**                     |
| `json/`    | Cartella generata **automaticamente** via GitHub Action – **non modificare i file al suo interno** |
| `scripts/` | Script utili                                                                                       |

---

## 🔍 A cosa serve la cartella `json/`?

Questa cartella contiene una versione `.json` **di tutti i file `.mes`**, per `eng/`, `it/` e `update/`.

> ⚠️ **NON modificare manualmente questi file.**

Viene usata per:

- Fare **ricerche rapide** su stringhe specifiche usando, ad esempio, _Visual Studio Code_
- Trovare facilmente **in quale file** si trova una certa stringa

> Esempio: cercando `"Reclutamento riuscito!"` scoprirai che si trova in `BattleEventMessage.mes`, perché appare in `BattleEventMessage.json`.

---

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

---

## 🧪 Script Utili

All'interno della cartella `scripts/` trovi alcuni tool utili:

- `formattazione.py`: riformatta un file `.txt` modificando i {CL} (newline) in base a una lunghezza massima (`max_len` Consulta [`note.md`](https://github.com/Lurpigi/DQMJ3P-IT-FanTranslation/blob/main/note.md) per esempi e valori usati.)
- Altri script per:
  - Generare i file `.json`
  - Aggiornare il `README.md` con i progressi della traduzione

---

## 🤝 Contribuisci anche tu!

Se sei appassionato della saga, se ami l'idea di giocare a questo gioco in italiano, o se vuoi semplicemente dare una mano a un progetto della community, sei nel posto giusto.

Unisciti, esplora i file, e **contribuisci con una pull request!**

Grazie ancora ❤️
