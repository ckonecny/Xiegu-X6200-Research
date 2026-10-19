# Native FT8/FT4 on the X6200 — feasibility research

## Goal

The X6200's own "U-DIGI" digital-mode menu only really supports RTTY/PSK (and even those
have decode bugs — see [notes.md](../notes.md#bugs)), with no FT8/FT4 support at all. FT8 is
normally run from a PC (WSJT-X) over CAT + USB audio, but this document looks at whether
FT8/FT4 could instead run **on the radio itself**, inside the legal amateur bands and power
limits the radio already operates in — no RF/TX-range change of any kind, purely a
baseband/software question.

**Why this has to mean on the physical display, not a companion device.** The X6200 already
pairs with phone FT8 apps over Bluetooth (CAT + audio), and that already works today. A
version of this project that just serves a web page over Wi-Fi for a phone/laptop to drive
would be a worse rebuild of something that already exists — still a second device, just over
a different link. The only thing actually worth building is the case that removes the second
device entirely: FT8 decoded/shown/operated from the radio's own screen and
buttons/encoder — useful for POTA/SOTA or just not wanting a phone out. That sets the target
for "Still open" below: the end goal is native UI integration (same binary-patching approach
as the [bandplan display patches](../Bandplan%20Display%20Patch/README.md)), not a
network-facing control surface.

## Starting point: survey of the X6100's alternative-firmware ecosystem

The X6200's older sibling, the Xiegu X6100, has a mature open-source alternative firmware
("R1CBU", actively maintained as [`gdyuldin/x6100_gui`](https://github.com/gdyuldin/x6100_gui),
built on [`AetherX6100Buildroot`](https://github.com/OpenX6100/AetherX6100Buildroot)) with a
full LVGL UI replacement, its own software SSB/CW DSP chain, and — relevantly — native
FT8/FT4/JS8 with CQ automation and ADIF logging.

Looking at its source tree and the underlying
[`AetherRadio/X6100Control`](https://github.com/AetherRadio/X6100Control) hardware library
to judge how much of it could be ported:

- **Not portable as-is — the low-level hardware layer.** `X6100Control` talks to the X6100's
  FPGA over a custom **I2C register protocol** (fixed register map, e.g. `x6100_vfoa_freq`,
  address `0x72`) plus a **custom CRC-framed serial "flow" channel** that streams *raw IQ
  samples* from the FPGA to the CPU. The GUI app does SSB/CW demodulation itself in software
  from those raw IQ samples (classic SDR design, see `src/dsp.cpp`). Xiegu markets the X6200
  as a new "DRFS" RF architecture, distinct from the X6100's "Zero-IF" design, and our own
  console-log/Alsamixer research (see [`../Alsamixer/README.md`](../Alsamixer/README.md))
  shows the X6200 already demodulates in hardware and exposes plain **ALSA** audio
  (`ADC Gain`, `Mic1`, `DAC` mixer controls) — there's no X6100-style raw-IQ/I2C-register
  interface to reuse, and reverse-engineering an X6200 equivalent of `X6100Control` would be
  its own, separate, large project.
- **Portable — the FT8 codec itself.** The GUI's FT8/FT4 glue code
  (`src/ft8/audio_worker.c`, `cq_scheduler.c`, `tx_worker.c`, `gfsk.c` "Based on gcFT8 de
  F4HTB") wraps an external library, `ft8lib`
  ([`kgoba/ft8_lib`](https://github.com/kgoba/ft8_lib), MIT licence) — a small, portable C
  FT8/FT4 encoder/decoder explicitly written for embedded/microcontroller use, independent of
  any X6100-specific hardware code. This is the reusable part.

**Conclusion:** rather than porting the X6100 alt-firmware's SDR/UI stack, the right-sized
approach for the X6200 is the same one sketched in the previous session's plan — a background
daemon on the existing Linux userspace, reading/writing through the **already-working ALSA
audio path** (same interface the "U-DIGI" RTTY/PSK modem already uses) — just built on
`ft8lib` instead of writing an FT8 codec from scratch, and with the X6100 GUI's
scheduler/TX-player code as a design reference (LGPL-2.1, MIT — both fine to draw on with
attribution).

## What was verified this session

All of this ran in the cloud sandbox, which has no network path to the radio's LAN — so this
is build/logic verification only, not an on-device test (see "Still open" below).

1. **Native build** of `ft8_lib` (`make`) — clean build, all binaries produced.
2. **Internal test suite** (`make run_tests`) — all sample messages decode correctly.
3. **End-to-end round trip**: `gen_ft8` encodes a message to a 15 s/12 kHz WAV, `decode_ft8`
   reads it back — confirmed for two different messages/tones (1200 Hz and 800 Hz), including
   correct text, SNR, and time offset.
4. **Cross-compiled for the X6200's actual target architecture**: installed
   `gcc-arm-linux-gnueabihf` and rebuilt with `make CC=arm-linux-gnueabihf-gcc`. Output
   confirmed as `ELF 32-bit LSB ... ARM, EABI5 ... for GNU/Linux 3.2.0` — i.e. a real armhf
   binary, not just a successful compile.
5. **Ran the cross-compiled ARM binary** under `qemu-arm-static` (installed via
   `qemu-user-static`) — internal test suite passes, and a full generate→WAV→decode round
   trip on the actual ARM binary decodes correctly:
   ```
   000000 +16.5 +1.36 1500 ~  CQ DK5XYZ JN59
   ```

So: the codec is correct, portable C with no non-portable dependencies that trip up an ARMv7
build, and runs under ARM emulation exactly as expected. This de-risks the core building
block before any device-specific integration work starts.

## Getting this onto the device

[`prebuilt-armhf/`](./prebuilt-armhf/) has the statically-linked armhf binaries built and
verified this session (`gen_ft8_static`, `decode_ft8_static`, `test_ft8_static`) plus the
`scp`/`ssh` commands to smoke-test them on a real X6200 — see that folder's README for the
exact steps. Static linking means the target's own libc version doesn't matter, so these can
go straight onto the device without a cross-toolchain on whichever machine has SSH access to
it.

## Still open — needs the real device

QEMU user-mode emulation proves the binary is correct and runs; it says nothing about
**real-time performance** on the X6200's actual CPU (quad-core ARMv7, per our boot-log
research), which matters because FT8 decoding has to finish inside roughly the 15 s cycle
time to be useful live. The next steps need SSH access to a live X6200 and can't be done from
this sandboxed session:

- Cross-compile and copy the binaries to the device; time a real decode of a generated WAV on
  the actual CPU.
- Check wall-clock time sync (FT8 needs the system clock within roughly ±1–2 s of UTC) — does
  the X6200 run NTP over Wi-Fi, or does its RTC drift without it?
- Capture real audio from the existing ALSA "U-DIGI" input path (same device already used for
  RTTY/PSK) and confirm `ft8lib`'s decoder can lock onto it (sample rate, levels, DC offset).
- Only after both of those hold up: look at TX (reusing the existing PTT mechanism).

A Wi-Fi/web-page control surface is only worth building as a **throwaway debug aid** during
that work (fastest way to see decoded messages while the above is still being verified) — not
as the project's deliverable, since Bluetooth-to-phone FT8 already covers that case today.
The actual target, once the above holds up, is native integration into the existing physical
display/menu — a new screen/state in the running Qt UI binary, driven by the existing
buttons/rotary encoder, following the same disassemble-hypothesize-patch-verify approach as
the bandplan display patches. That's a materially bigger step than those patches (finding and
hooking into the menu state machine and text rendering, not just rewriting a lookup table),
so budget for it as its own phase once the groundwork above is confirmed.

## Licence notes for future code

- `ft8lib` (`kgoba/ft8_lib`): MIT — no obligations beyond keeping the licence notice.
- Reference code from `gdyuldin/x6100_gui`'s FT8 glue layer: LGPL-2.1-or-later. Fine to use
  as a design reference or to adapt directly; LGPL doesn't require the whole X6200 project to
  be LGPL, just that modifications to *that* code stay under the same licence if redistributed.
- Not used/needed: JS8 support in `x6100_gui` pulls in GPL-3.0 code (`third-party/js8core`) —
  irrelevant here since this plan doesn't touch JS8, but worth remembering if that's ever
  revisited.
