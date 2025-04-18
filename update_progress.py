import os
import re

ENG_DIR = 'eng'
IT_DIR = 'it'
README_PATH = 'README.md'

def collect_mes_files(root):
    mes_files = set()
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith('.mes'):
                rel_path = os.path.relpath(os.path.join(dirpath, f), root)
                mes_files.add(rel_path)
    return mes_files

def update_readme(progress_percent):
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(
        r'Traduzione completata: \d+%',
        f'Traduzione completata: {progress_percent}%',
        content
    )

    if count == 0:
        # Add at top if not found
        new_content = f'Traduzione completata: {progress_percent}%\n\n' + content

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    eng_files = collect_mes_files(os.path.join(ENG_DIR, 'Message'))
    it_files = collect_mes_files(os.path.join(IT_DIR, 'Message'))

    total = len(eng_files)
    translated = len(eng_files & it_files)
    percent = int((translated / total) * 100) if total > 0 else 0

    update_readme(percent)
    print(f"Traduzione completata: {percent}%")

if __name__ == '__main__':
    main()
