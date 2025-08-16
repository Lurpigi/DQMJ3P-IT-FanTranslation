import os
import json

UPDATE_DIR = "./json/update/it"
BASE_DIR = "./json/it"

def overwrite_with_base(update_file, base_file):
    # Carica JSON di update
    with open(update_file, "r", encoding="utf-8") as f:
        update_data = json.load(f)

    # Carica JSON di base
    with open(base_file, "r", encoding="utf-8") as f:
        base_data = json.load(f)

    modified = False

    # Sostituisci valori di update con quelli presenti in base
    for key in update_data.keys():
        if key in base_data:
            if update_data[key] != base_data[key]:
                update_data[key] = base_data[key]
                modified = True

    # Salva solo se ci sono modifiche
    if modified:
        with open(update_file, "w", encoding="utf-8") as f:
            json.dump(update_data, f, ensure_ascii=False, indent=2)
        print(f"Aggiornato: {update_file}")
    else:
        print(f"Nessuna modifica: {update_file}")

def process_all_files():
    for root, _, files in os.walk(UPDATE_DIR):
        for filename in files:
            if filename.endswith(".json"):
                update_path = os.path.join(root, filename)
                rel_path = os.path.relpath(update_path, UPDATE_DIR)
                base_path = os.path.join(BASE_DIR, rel_path)

                if os.path.exists(base_path):
                    overwrite_with_base(update_path, base_path)
                else:
                    print(f"File base mancante: {base_path}")

if __name__ == "__main__":
    # process_all_files() ora servirà solo per gli Event/ ATTENZIONE A NON SOVRASCRIVERE ALTRI FILE IN FUTURO
    ...