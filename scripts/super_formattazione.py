import json
import os

def calculate_length(text):
    length = 0
    length += text.count("\u0001ȁ") * 10.2
    text = text.replace("\u0001ȁ", "")
    for char in text:
        if char.isupper():
            length += 1.7
        else:
            length += 1.2
    return length

def format_line_json(line, max_len=85):  # 85 dialoghi, 54 menu
    line = line.strip()
    blocks = line.split("\u0001ā")

    formatted_blocks = []

    for block in blocks:
        subline = block.replace("\n", " ").strip()  # Sostituisce \n per calcoli
        while "  " in subline:
            subline = subline.replace("  ", " ")

        words = subline.split()
        formatted = ""
        current_line = ""

        for word in words:
            if calculate_length(current_line) + calculate_length(word) + 1 <= max_len:
                current_line += (" " if current_line else "") + word
            else:
                formatted += current_line + "\n"
                current_line = word

        formatted += current_line
        if max_len == 85:
            # Avviso se ci sono due \n consecutivi (equivalente a 2 {CL}) solo nei dialoghi
            if formatted.count("\n") > 1:
                print(f"AVVISO: Due o più '\\n' trovati nel blocco: {formatted}")

        formatted_blocks.append(formatted)

        # Avviso se la linea supera max_len*2
        if calculate_length(subline) > max_len * 2:
            print(f"AVVISO: Blocco supera la lunghezza massima: {subline}")

    # Rimuovi l'ultimo blocco se vuoto
    if formatted_blocks and formatted_blocks[-1] == "":
        formatted_blocks = formatted_blocks[:-1]

    return "\n\u0001ā\n".join(formatted_blocks)

def process_json(input_path, output_path, max_len):
    with open(input_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    formatted_data = {}
    for key, value in data.items():
        stripped = value.strip()
        if stripped == "-":
            formatted_data[key] = "-"
        elif not stripped:
            formatted_data[key] = ""
        else:
            formatted_data[key] = format_line_json(stripped, max_len)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(formatted_data, outfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_dirs = [
        "./json/it/Script/Field/Demo",
        "./json/it/Script/Field/Event"
    ]
    for input_dir in input_dirs:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".json"):
                    input_path = os.path.join(root, file)
                    process_json(input_path, input_path, 85)
