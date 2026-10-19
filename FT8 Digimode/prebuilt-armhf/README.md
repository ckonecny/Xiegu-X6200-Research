# Prebuilt ft8lib binaries (armhf, static)

Static armhf builds of [`kgoba/ft8_lib`](https://github.com/kgoba/ft8_lib) demo tools, for
quick on-device smoke testing over SSH without needing a cross-toolchain on the machine
you're SSH'd in from.

- Source commit: `9fec6ca39886edbf96f4f5e71edc76da5074e871` (2025-08-24), MIT licence.
- Built with `arm-linux-gnueabihf-gcc` (Ubuntu 13.3.0), statically linked (`-static`) so the
  target's own libc version doesn't matter — relevant because the X6200's Buildroot userspace
  almost certainly ships an older/smaller glibc than this build environment's, and a
  dynamically-linked binary built elsewhere is a common source of `GLIBC_2.XX not found`
  failures on embedded targets.
- Verified under `qemu-arm-static` (ARM user-mode emulation) only, in
  [this session](../README.md#what-was-verified-this-session) — not yet run on the real
  device. See [`../README.md`](../README.md) for what's confirmed vs. still open.

## Files

- `test_ft8_static` — runs the library's own internal test suite, no arguments needed.
- `gen_ft8_static MESSAGE OUT.wav [FREQUENCY]` — encodes a message to a 15 s/12 kHz WAV.
- `decode_ft8_static FILE.wav` — decodes a WAV file.
- `SHA256SUMS` — checksums for all three, to confirm nothing got mangled in transfer.

## Quick on-device check

```sh
scp decode_ft8_static gen_ft8_static test_ft8_static root@<radio>:/root/
ssh root@<radio>
cd /root
sha256sum -c <(echo "ae25ffd46d52f82db2b1ea426522ef765f4436a2e776ce9097e96de22e85eaa3  decode_ft8_static")
chmod +x ./*_static
./test_ft8_static            # should print "Test OK" several times
./gen_ft8_static "CQ TEST JO61" /tmp/t.wav
time ./decode_ft8_static /tmp/t.wav   # the 'real' time here is the number that matters
```

If `test_ft8_static` runs and `decode_ft8_static` reports back the message you encoded, the
codec itself works on real hardware. The `time` output is the first real data point on
whether decoding keeps up with FT8's 15-second cycle on this CPU.
