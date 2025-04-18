import os

def count_mes_files(root):
    return sum(1 for dirpath, _, files in os.walk(root) for f in files if f.endswith('.mes'))

eng_files = count_mes_files('eng')
it_files = count_mes_files('it')
percent = int((it_files / eng_files) * 100) if eng_files else 0

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("README.md", "w", encoding="utf-8") as f:
    for line in lines:
        if line.strip().startswith("**Traduzione completata**:"):
            f.write(f"**Traduzione completata**: {percent}% ({it_files}/{eng_files} files)\n")
        else:
            f.write(line)
