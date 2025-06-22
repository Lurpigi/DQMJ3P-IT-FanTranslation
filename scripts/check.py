import os
import hashlib

# Cartelle di origine
folder_updt = '../update/eng/Message'
folder_nm = '../eng/Message'

def sha256sum(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

matching_files = []

for filename in os.listdir(folder_updt):
    if filename.endswith('.mes'):
        path_updt = os.path.join(folder_updt, filename)
        path_nm = os.path.join(folder_nm, filename)

        if os.path.exists(path_nm):
            hash_updt = sha256sum(path_updt)
            hash_nm = sha256sum(path_nm)

            if hash_updt == hash_nm:
                matching_files.append(filename)

print("File con hash SHA-256 identici:")
for fname in matching_files:
    print(f"- {fname}")
