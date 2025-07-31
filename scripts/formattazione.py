def calculate_length(text):
    length = 0
    for char in text:
        if char.isupper():
            length += 1.7
        else:
            length += 1.2
    return length


def format_line(line, max_len=85): #85 dialoghi, 54 menu
    # Sostituisce {CL} con spazio temporaneamente per calcoli, ma li reinseriamo poi
    line = line.strip()
    blocks = line.split("ā")

    formatted_blocks = []

    for block in blocks:
        subline = block.replace("{CL}", " ").strip()
        while "  " in subline:
            subline = subline.replace("  ", " ")

        words = subline.split()
        formatted = ""
        current_line = ""

        for word in words:
            if calculate_length(current_line) + calculate_length(word) + 1 <= max_len:
                current_line += (" " if current_line else "") + word
            else:
                formatted += current_line + "{CL}"
                current_line = word

        formatted += current_line
        formatted_blocks.append(formatted)

        # Avviso se la linea supera max_len*2
        if calculate_length(subline) > max_len * 2:
            print(f"AVVISO: Blocco supera la lunghezza massima: {subline}")

    # Rimuovi l'ultimo block se vuoto
    if formatted_blocks and formatted_blocks[-1] == "":
        formatted_blocks = formatted_blocks[:-1]

    return "{CL}ā{CL}".join(formatted_blocks)



def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
            open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            stripped = line.strip()
            if stripped == "-":
                outfile.write("-\n")
            elif not stripped:
                outfile.write("\n")
            else:
                formatted = format_line(stripped)
                outfile.write(formatted + "\n")


if __name__ == "__main__":
    process_file("input.txt", "output.txt")
