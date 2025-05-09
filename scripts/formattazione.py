def calculate_length(text):
    length = 0
    for char in text:
        if char.isupper():
            length += 1.7
        else:
            length += 1.2
    return length


def format_line(line, max_len=50):
    # Sostituisce {CL} con spazio e rimuove spazi multipli
    line = line.replace("{CL}", " ").strip()
    while "  " in line:
        line = line.replace("  ", " ")

    words = line.split()
    formatted = ""
    current_line = ""

    for word in words:
        if calculate_length(current_line) + calculate_length(word) + 1 <= max_len:
            current_line += (" " if current_line else "") + word
        else:
            formatted += current_line + "{CL}"
            current_line = word

    formatted += current_line
    return formatted


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
    process_file("aaa.txt", "output.txt")
    # print(format_line("3 frammenti dell’anima di Wildcard{CL}frantumati dalla Furia della Madre.", 50))
