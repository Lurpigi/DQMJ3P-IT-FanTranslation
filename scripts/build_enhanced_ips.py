"""Genera exefs/code_enhanced.ips: exefs/code.ips + miglioramenti e fix Azahar.

Il codice è quello dell'update 1.3 (code.bin decompresso, caricato a 0x100000).
Le patch aggiunte sono descritte in PATCHES; quelle che servono più istruzioni di
quante ne occupa l'originale saltano nella cave a fine .text (2032 byte azzerati).

uso: build_enhanced_ips.py [--code CODE.BIN]
Con --code controlla che i byte sostituiti siano quelli attesi e che le patch non
si sovrappongano a quelle di code.ips, poi stampa il disassemblato se c'è capstone.
"""
import argparse
import os
import struct

BASE = 0x100000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "exefs", "code.ips")
DST = os.path.join(ROOT, "exefs", "code_enhanced.ips")

CAVE = 0x7B9810
CAVE_END = 0x7BA000

SET_DEVICE_MEMORY_SIZE = 0x1067F4
DEVICE_HEAP_SIZE_VAR = 0x8C0328

# Quanto più lontano restano visibili oggetti, NPC e mostri (default del gioco: 360-410
# per gli NPC, 310-360 per i mostri, 2000-2500 per i mostri giganti).
FADE_SCALE = 5.0

# Device heap, dove finiscono i modelli dei mostri: il gioco chiede 39 MB e, se finiscono,
# si ferma con 0xE0E046BC perché legge il file in un buffer nullo. L'exheader dell'update
# ha già n3ds_mode = 1, quindi su New 3DS ha 124 MB a disposizione: qui ne chiede di più.
DEVICE_HEAP = 0x4700000
DEVICE_HEAP_ORIGINAL = 0x2700000

# Fix HTTP di DQMJ3P Online (re/tools/make_url_patch.py, opzione --azahar).
# La patch normale contiene già il collegamento ai server; questi fix servono
# solo nell'emulatore per SIL e l'invio dei replay G-Cup.
UPLOAD_SIZE_CAVE = 0x7B9B60

# Oltre questa soglia il gruppo di mostri viene distrutto, quindi deve crescere insieme
# alla dissolvenza: gli stub in build_cave() la moltiplicano per 5 come FADE_SCALE, ma solo
# se il device heap è stato ingrandito, altrimenti la memoria non basterebbe.
# (slot +0x1c della vtable di ogni tipo di spawner, funzione originale)
GROUP_DISTANCE_SLOTS = [
    (0x838104, 0x40DAE8),  # campo normale
    (0x8438BC, 0x58AD94),
    (0x831B4C, 0x3DB6C0),
    (0x834F48, 0x3F4680),
    (0x834ED0, 0x3F4440),
    (0x834FC0, 0x3F470C),
]


def branch(src, dst, link=False):
    return (0xEB000000 if link else 0xEA000000) | (((dst - src - 8) >> 2) & 0xFFFFFF)


def vldr_pc(opcode, src, target):
    """vldr sN, [pc, #off]: opcode è l'istruzione con offset 0 e bit U azzerato."""
    offset = target - src - 8
    return opcode | (0x800000 if offset >= 0 else 0) | (abs(offset) >> 2)


def build_cave():
    """Ritorna (word della cave, hook dissolvenza, hook LOD, stub attivazione, stub gruppi, heap)."""
    fade = CAVE
    words = [
        0xEC910A03,  # vldmia r1, {s0-s2}        ; start, end, velocità della dissolvenza
        0xEDDF1A04,  # vldr   s3, [pc, #0x10]    ; FADE_SCALE
        0xEE200A21,  # vmul.f32 s0, s0, s3
        0xEE600AA1,  # vmul.f32 s1, s1, s3
        0xE2800F49,  # add    r0, r0, #0x124
        0xEC800A03,  # vstmia r0, {s0-s2}
        0xE12FFF1E,  # bx     lr
        struct.unpack("<I", struct.pack("<f", FADE_SCALE))[0],
    ]
    lod = CAVE + len(words) * 4
    words += [
        0xEE300A00,  # vadd.f32 s0, s0, s0       ; raggio x2
        0xEE200A00,  # vmul.f32 s0, s0, s0       ; istruzione sostituita dall'hook
        0xE12FFF1E,  # bx     lr
    ]
    scale = CAVE + 7 * 4  # il FADE_SCALE scritto qui sopra
    active_s16 = CAVE + len(words) * 4
    words += [
        0xED908A01,  # vldr   s16, [r0, #4]      ; istruzione sostituita dall'hook
        vldr_pc(0xED1F0A00, active_s16 + 4, scale),  # vldr s0, FADE_SCALE
        0xEE288A00,  # vmul.f32 s16, s16, s0
        0xE12FFF1E,  # bx     lr
    ]
    active_s0 = CAVE + len(words) * 4
    words += [
        0xED900A01,  # vldr   s0, [r0, #4]       ; istruzione sostituita dall'hook
        vldr_pc(0xED5F0A00, active_s0 + 4, scale),  # vldr s1, FADE_SCALE
        0xEE200A20,  # vmul.f32 s0, s0, s1
        0xE12FFF1E,  # bx     lr
    ]
    scale_group = CAVE + len(words) * 4
    words += [
        0xE59F100C,  # ldr    r1, [pc, #0xc]      ; dimensione del device heap
        0xE5911000,  # ldr    r1, [r1]
        0xE3510627,  # cmp    r1, #0x2700000
        0x80800100,  # addhi  r0, r0, r0, lsl #2  ; soglia x5
        0xE12FFF1E,  # bx     lr
        DEVICE_HEAP_SIZE_VAR,
    ]
    stubs = []
    for _, original in GROUP_DISTANCE_SLOTS:
        stub = CAVE + len(words) * 4
        stubs.append(stub)
        words += [
            0xE92D4008,  # push   {r3, lr}
            branch(stub + 4, original, link=True),
            0xE8BD4008,  # pop    {r3, lr}
            branch(stub + 12, scale_group),
        ]
    heap = CAVE + len(words) * 4
    words += [
        0xE92D4010,  # push   {r4, lr}
        0xE1A04000,  # mov    r4, r0              ; DEVICE_HEAP_ORIGINAL
        0xE3A00647,  # mov    r0, #DEVICE_HEAP
        branch(heap + 12, SET_DEVICE_MEMORY_SIZE, link=True),
        0xE3500000,  # cmp    r0, #0
        0xB1A00004,  # movlt  r0, r4              ; rifiutato: Old 3DS, resta il valore originale
        branch(heap + 24, SET_DEVICE_MEMORY_SIZE, link=True) & 0x0FFFFFFF | 0xB0000000,  # bllt
        0xE8BD8010,  # pop    {r4, pc}
    ]
    return words, fade, lod, (active_s16, active_s0), stubs, heap


def build_patches():
    """(indirizzo, word nuovi, word originali)"""
    cave, fade, lod, (active_s16, active_s0), stubs, heap = build_cave()
    slots = [
        (slot, [stub], [original])
        for (slot, original), stub in zip(GROUP_DISTANCE_SLOTS, stubs)
    ]
    return slots + [
        # Battaglia x2: la logica gira già a 60 Hz, il render saltava un frame su due.
        # eorlo r0, r0, #1 -> movlo r0, #0
        (0x1050F0, [0x33A00000], [0x32200001]),
        # Device heap più grande (unica chiamata a FUN_001067f4).
        (0x105460, [branch(0x105460, heap, link=True)], [0xEB0004E3]),
        # Animazioni dei mostri (FUN_00216398): oltre 200/360 unità lo scheletro veniva
        # aggiornato ogni 2 o 6 tick. beq #0x216440 -> b #0x216450, il ramo dei mostri vicini.
        (0x216420, [branch(0x216420, 0x216450)], [0x0A000006]),
        # Soglie fisse (410, 410, 1020) che spengono gli oggetti delle liste del campo
        # (FUN_003011a0): senza scalarle sparirebbero prima della dissolvenza.
        (0x301584, [branch(0x301584, active_s16, link=True)], [0xED908A01]),
        (0x301844, [branch(0x301844, active_s0, link=True)], [0xED900A01]),
        (0x3018D8, [branch(0x3018D8, active_s0, link=True)], [0xED900A01]),
        # Setter unico della dissolvenza lontana (FUN_001d96a0).
        (0x1D96A0, [branch(0x1D96A0, fade)], [0xE8910 << 12 | 0x00E]),
        # Scelta del livello dei tile LOD nelle celle miste di VP.lod (FUN_006eca08).
        (0x6ECB4C, [branch(0x6ECB4C, lod, link=True)], [0xEE200A00]),
        (CAVE, cave, [0] * len(cave)),
        # POST vuoti: forza SetLazyPostDataSetting e invia un byte nullo,
        # riconosciuto come corpo vuoto dal server SIL.
        (0x603E88, [0xE320F000], [0x03A09000]),
        (0x603E8C, [0xE320F000], [0x0A00000E]),
        (0x7D5F8C, [0, 0x7D5F8C, 0, 1], [0, 0, 0, 0]),
        # Buffer degli header a 4 KiB: Azahar riporta male la dimensione
        # nella chiamata di prova, impedendo di leggere X-Sil-Digest.
        (0x604290, [0xE3A00A01], [0xE3100102]),
        (0x604294, [0xE5840014], [0x1A000020]),
        # Upload in un solo blocco: evita che Azahar riordini i pezzi del replay.
        (0x4AA3B4, [branch(0x4AA3B4, UPLOAD_SIZE_CAVE, link=True)], [0xE5951018]),
        (UPLOAD_SIZE_CAVE, [0xE5951020, 0xE2811901, 0xE12FFF1E], [0, 0, 0]),
    ]


def read_ips(path):
    data = open(path, "rb").read()
    if data[:5] != b"PATCH" or data[-3:] != b"EOF":
        raise SystemExit(f"{path}: IPS non valido")
    records, p = [], 5
    while p < len(data) - 3:
        off = int.from_bytes(data[p:p + 3], "big")
        size = int.from_bytes(data[p + 3:p + 5], "big")
        p += 5
        if size == 0:
            raise SystemExit(f"{path}: record RLE non previsto")
        records.append((off, data[p:p + size]))
        p += size
    return records


def write_ips(path, records):
    out = bytearray(b"PATCH")
    for off, payload in records:
        out += off.to_bytes(3, "big") + len(payload).to_bytes(2, "big") + payload
    out += b"EOF"
    with open(path, "wb") as f:
        f.write(out)


def verify(code_path, records, patches):
    code = open(code_path, "rb").read()
    used = {o for off, payload in records for o in range(off, off + len(payload))}
    for va, new, old in patches:
        off = va - BASE
        raw = struct.pack(f"<{len(old)}I", *old)
        if code[off:off + len(raw)] != raw:
            raise SystemExit(f"{va:#x}: byte originali diversi da quelli attesi")
        if used & set(range(off, off + len(raw))):
            raise SystemExit(f"{va:#x}: si sovrappone a code.ips")
    if CAVE + sum(len(n) for va, n, _ in patches if va == CAVE) * 4 > CAVE_END:
        raise SystemExit("cave esaurita")
    print("verifica OK")
    try:
        from capstone import CS_ARCH_ARM, CS_MODE_ARM, Cs
    except ImportError:
        return
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    for va, new, _ in patches:
        for i, word in enumerate(new):
            ins = list(md.disasm(struct.pack("<I", word), va + i * 4))
            text = f"{ins[0].mnemonic} {ins[0].op_str}" if ins else f".word {word:#x}"
            print(f"{va + i * 4:#x}: {word:08x}  {text}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--code", help="code.bin originale dell'update per la verifica")
    args = parser.parse_args()

    records = read_ips(SRC)
    patches = build_patches()
    if args.code:
        verify(args.code, records, patches)
    extra = [(va - BASE, struct.pack(f"<{len(new)}I", *new)) for va, new, _ in patches]
    write_ips(DST, records + extra)
    print(f"{os.path.relpath(DST, ROOT)}: {os.path.getsize(DST)} byte")


if __name__ == "__main__":
    main()
