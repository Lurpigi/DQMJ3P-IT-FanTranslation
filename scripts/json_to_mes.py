import struct
import json
from pathlib import Path

def align4(x):
    return (x + 3) & ~3

def read_cstr(data, start):
    end = start
    while end < len(data) and data[end] != 0:
        end += 1
    return data[start:end].decode('ascii'), end + 1

def parse_mes_structure(original_mes_path):
    """Legge il MES originale e ritorna gruppi e chiavi in ordine."""
    with open(original_mes_path, "rb") as f:
        data = f.read()

    num_groups = struct.unpack_from("<I", data, 0)[0]
    offset = 4
    groups = []
    for _ in range(num_groups):
        active_count, key_offset = struct.unpack_from("<II", data, offset)
        groups.append((active_count, key_offset))
        offset += 8

    key_entries = []
    for group in groups:
        for _ in range(group[0]):
            # value_offset = struct.unpack_from("<I", data, offset)[0]
            offset += 4
            key_str, offset = read_cstr(data, offset)
            offset = align4(offset)
            key_entries.append(key_str)

    return num_groups, groups, key_entries

def build_mes(num_groups, groups, keys, translations, output_path):
    """Rigenera il file MES da zero usando le nuove traduzioni."""
    buf = bytearray()

    # header
    buf += struct.pack("<I", num_groups)
    for active_count, key_offset in groups:
        buf += struct.pack("<II", active_count, key_offset)

    # inizio blocco "keys + offsets valori"
    key_block_start = len(buf)

    # Riserva spazio per ogni key entry (offset valore + key string allineata)
    key_entries_bytes = []
    for key in keys:
        # offset valore (4 byte) + key string + null + padding
        key_bytes = key.encode("ascii") + b"\x00"
        key_bytes += b"\x00" * (align4(len(key_bytes)) - len(key_bytes))
        key_entries_bytes.append((4 + len(key_bytes), key_bytes))

    total_reserved = sum(size for size, _ in key_entries_bytes)
    buf += b"\x00" * total_reserved

    # Scrivi i valori e memorizza gli offset
    value_offsets = []
    for key in keys:
        value_offsets.append(len(buf))
        val_str = translations.get(key, "")
        val_bytes = val_str.encode("utf-16le") + b"\x00\x00"
        val_bytes += b"\x00" * (align4(len(val_bytes)) - len(val_bytes))
        buf += val_bytes

    # torniamo indietro e scriviamo gli offset + chiavi
    pos = key_block_start
    for i, key in enumerate(keys):
        buf[pos:pos+4] = struct.pack("<I", value_offsets[i])
        pos += 4
        key_bytes = key.encode("ascii") + b"\x00"
        key_bytes += b"\x00" * (align4(len(key_bytes)) - len(key_bytes))
        buf[pos:pos+len(key_bytes)] = key_bytes
        pos += len(key_bytes)

    with open(output_path, "wb") as f:
        f.write(buf)
    print(f"Creato {output_path}")

def main():
    json_base_dirs = ["./json/it", "./json/update/it"]
    mes_base_dirs = ["./it", "./update/it"]

    for json_base, mes_base in zip(json_base_dirs, mes_base_dirs):
        for json_file in Path(json_base).rglob("*.json"):
            relative_path = json_file.relative_to(json_base)
            mes_out_path = Path(mes_base) / relative_path.with_suffix(".mes")

            # Percorso del MES originale in inglese
            original_mes_path = Path("./eng") / relative_path.with_suffix(".mes")
            if "update" in mes_base:
                original_mes_path = Path("./update/eng") / relative_path.with_suffix(".mes")

            if not original_mes_path.exists():
                print(f"File originale mancante: {original_mes_path}")
                continue

            # Carica struttura dal MES originale
            num_groups, groups, keys = parse_mes_structure(original_mes_path)

            # Carica traduzioni italiane dal JSON
            with open(json_file, "r", encoding="utf-8") as f:
                translations = json.load(f)

            # Genera nuovo MES
            build_mes(num_groups, groups, keys, translations, mes_out_path)

if __name__ == "__main__":
    main()
