# DQMJ3p Fan Translation

This repository is dedicated to developing an Italian fan translation for _Dragon Quest Monsters Joker 3: Professional_. It contains only `.mes` patch files, ensuring no copyrighted material is shared.

# Installing the Mod for DQMJ3P

<h3>Emulator</h3>

1. You can use my version of [Lime3DS](https://github.com/Lurpigi/lime3ds-dqmj3p) or Citra 1543 (or older version).
2. Install update 1.3 via **File** → **Install CIA…**.
3. Right-click on `dqmj3p` in the ROM list and open the **mods location** folder.
4. Create the `romfs/data` folder.
5. Extract all patch data into the `romfs` folder (first the main patch, then the update patch).
6. The folder structure should look like this:

```
romfs/
└── data/
    ├── Font/
    ├── Message/
    ├── Script/
```

7. Launch the game and enjoy the mod!

<h3>Instructions for patching the ROM</h3>

1. Obtain a decrypted `.3ds` or `.cia` ROM (search online for how to dump the game).
2. Download and open [HackingToolkit3DS v9](https://github.com/Asia81/HackingToolkit9DS/releases/tag/9).
3. Use HackingToolkit3DS to extract a `.3ds` or `.cia` file.
4. When prompted, select **No** to decompress the `code.bin`.
5. Go to the `ExtractedRomFS/data` folder and copy the patch files there.
6. Open HackingToolkit3DS again and select **Rebuild** to create a new patched `.3ds` or `.cia` ROM.
7. Repeat these steps for both the base game and the 1.3 update.

Once finished, you can load the patched ROM into Citra and play with the mod installed!
