import struct
import json
import os
from pathlib import Path


def align4(x):
    return (x + 3) & ~3


def read_cstr(data, start):
    end = start
    while end < len(data) and data[end] != 0:
        end += 1
    return data[start:end].decode('ascii'), end + 1


def read_utf16le_cstr(data, start):
    end = start
    while end + 1 < len(data):
        if data[end] == 0 and data[end + 1] == 0:
            break
        end += 2
    return data[start:end].decode('utf-16le'), end + 2


def parse_mes_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    mes_dict = {}

    # Header
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
            value_offset = struct.unpack_from("<I", data, offset)[0]
            offset += 4
            key_str, offset = read_cstr(data, offset)
            offset = align4(offset)
            key_entries.append((key_str, value_offset))

    for key, value_offset in key_entries:
        value_str, _ = read_utf16le_cstr(data, value_offset)
        mes_dict[key] = value_str

    return mes_dict


def main():
    base_dirs = ["./eng", "./it", "./update"]
    out_root = Path("./json")
    out_root.mkdir(parents=True, exist_ok=True)

    for base in base_dirs:
        for mes_file in Path(base).rglob("*.mes"):
            relative_path = mes_file.relative_to(".")
            out_path = out_root / relative_path.with_suffix(".json")
            out_path.parent.mkdir(parents=True, exist_ok=True)

            mes_data = parse_mes_file(mes_file)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(mes_data, f, indent=2, ensure_ascii=False)
            print(f"✓ {mes_file} → {out_path}")


if __name__ == "__main__":
    main()
