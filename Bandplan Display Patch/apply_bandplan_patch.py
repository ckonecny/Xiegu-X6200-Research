#!/usr/bin/env python3
"""
X6200 band-scope display patch: US license-class overlay -> single CEPT/IARU-R1
style band-edge bar (cyan = in-band, invisible = out-of-band).

Targets exactly: x6200_ui_v100, UI app version 1.0.7,
MD5 (unmodified) = a08ab13189bececa9995d3d19bc14c94

Background, methodology and a full explanation of every patch below:
see README.md in this directory.

This script ONLY changes how the band-scope bar is drawn. It does not touch
isTxEnable()/isHamBand() or the fullband-tx setting in
/etc/xgradio/xgradio.conf -- TX behavior is unaffected.

Usage:
    python3 apply_bandplan_patch.py <input_file> <output_file>

Example:
    python3 apply_bandplan_patch.py x6200_ui_v100 x6200_ui_v100.patched

The script verifies the input file's MD5 before writing anything, and
verifies every patch's expected "old" value at its offset before changing
it. Any mismatch aborts immediately without touching the output file.
"""

import struct
import sys
import hashlib

EXPECTED_MD5 = "a08ab13189bececa9995d3d19bc14c94"
LOAD_BASE_VADDR = 0x10000  # single PT_LOAD segment: file_offset = vaddr - 0x10000

# ---------------------------------------------------------------------------
# Country-specific band edges (Hz). Defaults below are the Austrian (OeVSV)
# band plan, which closely follows IARU Region 1 recommendations for most
# bands. If your national permissions differ -- most likely for 60 m, and
# possibly the top edge of 160 m / 80 m -- edit the values here before
# running the script. See README.md for which bands were verified against
# real hardware and which entries needed edge changes vs. color-only changes.
# ---------------------------------------------------------------------------
BAND_EDGES_HZ = {
    "160m": (1810000, 1950000),
    "80m":  (3500000, 3800000),   # segment boundary already sat exactly here
    "60m":  (5250000, 5450000),   # CHECK YOUR OWN ADMINISTRATION -- varies a lot by country
    "40m":  (7000000, 7200000),
    # 30m/20m/17m/15m/12m/10m/6m: shipped international edges already match
    # IARU Region 1 allocations, so no edge literal needs to move for these --
    # only the color-selecting instructions are patched (see PATCHES below).
}

# Each entry: (vaddr, expected_old_value, new_value, description)
PATCHES = [
    # --- Global color table: XBandPlan::regionMapColor(), 7-entry ARGB array ---
    # NOTE: displayed(R,G,B) = (table.Alpha, table.Red, table.Green) due to a
    # channel-mixup bug in the caller -- see README.md for the full writeup.
    (0x111248, 0xff000000, 0x00ffff00, "color table index 3 -> displays cyan"),
    (0x111254, 0xffffff00, 0x00000000, "color table index 6 -> displays black (blends into background)"),

    # --- Code: disable 3 of the 4 per-band display rows (global, one-time) ---
    # XBandScope::paintEvent() calls drawRegionMap() 4x per band (rows 0-3).
    # We keep row 0 (list offset +0x60) and NOP the other three calls.
    (0xee4f0, 0xebfff960, 0xe1a00000, "paintEvent: drawRegionMap call (row 1) -> NOP"),
    (0xee53c, 0xebfff94d, 0xe1a00000, "paintEvent: drawRegionMap call (row 2) -> NOP"),
    (0xee588, 0xebfff93a, 0xe1a00000, "paintEvent: drawRegionMap call (row 3) -> NOP"),

    # --- 40 m: shipped 7.000-7.300 (2 segments split at 7.125) ---
    # The split literal is re-used (value+1) as the 2nd segment's start, so
    # moving this one literal shifts both sides of the boundary at once.
    (0x9173c, 7124999, BAND_EDGES_HZ["40m"][1] - 1, "40m: segment boundary -> country high edge"),
    (0x91798, 0xe1a0200a, 0xe3a02006, "40m: segment 2 color -> index 6 (invisible)"),

    # --- 20 m: shipped 14.000-14.350 (2 segments), matches IARU R1 already ---
    (0x91d3c, 0xe1a02008, 0xe3a02003, "20m: segment 2 color -> index 3 (cyan)"),

    # --- 17 m: shipped 18.068-18.168 (2 segments), matches IARU R1 already ---
    (0x92198, 0xe1a0200b, 0xe3a02003, "17m: segment 2 color -> index 3 (cyan)"),

    # --- 12 m: shipped 24.890-24.990 (2 segments), matches IARU R1 already ---
    (0x928c0, 0xe1a02009, 0xe3a02003, "12m: segment 2 color -> index 3 (cyan)"),

    # --- 10 m: shipped 28.000-29.700 (2 segments), matches IARU R1 already ---
    (0x92b74, 0xe1a0200a, 0xe3a02003, "10m: segment 2 color -> index 3 (cyan)"),

    # --- 160 m: shipped 1.800-2.000 (single entry) ---
    (0x91248, 1800000, BAND_EDGES_HZ["160m"][0], "160m: low edge -> country low edge"),
    (0x9124c, 2000000, BAND_EDGES_HZ["160m"][1], "160m: high edge -> country high edge"),
    (0x90e60, 0xe1a02005, 0xe3a02003, "160m: color -> index 3 (cyan)"),

    # --- 80 m: shipped 3.500-4.000 (3 segments: ham/ham/75m-broadcast) ---
    # boundary between segment 2 and 3 already sits at 3.800 -- no edge change needed
    (0x91070, 0xe1a02008, 0xe3a02003, "80m: segment 2 color -> index 3 (cyan)"),
    (0x910b0, 0xe3a02001, 0xe3a02006, "80m: segment 3 (75m broadcast, non-ham) color -> index 6 (invisible)"),

    # --- 15 m: shipped 21.000-21.450 (2 segments), matches IARU R1 already ---
    (0x9242c, 0xe1a02005, 0xe3a02003, "15m: segment 2 color -> index 3 (cyan)"),

    # --- 60 m: shipped 5.332-5.405 (single entry) ---
    (0x9172c, 5332000, BAND_EDGES_HZ["60m"][0], "60m: low edge -> country low edge"),
    (0x91730, 5405000, BAND_EDGES_HZ["60m"][1], "60m: high edge -> country high edge"),
    (0x91574, 0xe3a02002, 0xe3a02003, "60m: color -> index 3 (cyan)"),

    # --- 6 m: shipped 50.000-54.000 (many segments built via chained adds), ---
    # --- matches IARU R1 already -- force every segment's color, no edges touched ---
    (0x92f0c, 0xe3a02005, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x92f5c, 0xe1a02009, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x92fac, 0xe3a02005, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x92ff4, 0xe1a02009, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x93040, 0xe3a02004, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x9308c, 0xe1a02009, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
    (0x930d0, 0xe3a02004, 0xe3a02003, "6m: segment color -> index 3 (cyan)"),
]


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]

    with open(infile, "rb") as f:
        data = bytearray(f.read())

    actual_md5 = hashlib.md5(data).hexdigest()
    if actual_md5 != EXPECTED_MD5:
        print("ABORTED: input file MD5 does not match.")
        print(f"  expected: {EXPECTED_MD5}")
        print(f"  found:    {actual_md5}")
        print("This script's byte offsets were verified only against UI app")
        print("version 1.0.7 with the exact hash above. Applying it to a")
        print("different build could crash the app or corrupt unrelated code.")
        print("Do not proceed unless you have redone the analysis for your")
        print("exact binary (see README.md's methodology section).")
        sys.exit(2)

    print(f"MD5 verified: {actual_md5}")
    print(f"Applying {len(PATCHES)} patches...\n")

    for vaddr, expect_old, new, label in PATCHES:
        off = vaddr - LOAD_BASE_VADDR
        old = struct.unpack_from("<I", data, off)[0]
        if old != expect_old:
            print(f"ABORTED at '{label}': offset {hex(off)} expected "
                  f"{hex(expect_old)}, found {hex(old)}.")
            sys.exit(3)
        struct.pack_into("<I", data, off, new)
        print(f"  OK  {label}")

    with open(outfile, "wb") as f:
        f.write(data)

    print(f"\nDone. Patched file written to: {outfile}")
    print(f"MD5 of patched file: {hashlib.md5(data).hexdigest()}")


if __name__ == "__main__":
    main()
