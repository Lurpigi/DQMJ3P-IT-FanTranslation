import os


def count_mes_files(root):
    return sum(1 for dirpath, _, files in os.walk(root) for f in files if f.endswith('.mes'))


def update_progress_section(readme_path, section_title, eng_path, it_path):
    eng_files = count_mes_files(eng_path)
    it_files = count_mes_files(it_path)
    percent = int((it_files / eng_files) * 100) if eng_files else 0

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(readme_path, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip().startswith(section_title):
                f.write(
                    f"{section_title} {percent}% ({it_files}/{eng_files} files)\n")
            else:
                f.write(line)


readme_path = "README.md"

# Aggiorna lo stato della traduzione principale
update_progress_section(
    readme_path,
    "📊 **Stato della traduzione principale**:",
    "eng",
    "it"
)

# Aggiorna lo stato della traduzione update
update_progress_section(
    readme_path,
    "📊 **Stato della traduzione update**:",
    "update/eng",
    "update/it"
)
