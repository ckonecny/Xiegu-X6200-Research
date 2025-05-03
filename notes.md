# Wifi
Issues connecting to Wifi through UI can be resolved by using CLI.

**Note:** Ensure Wifi is switched on from the radio UI first

## List access points
```bash
nmcli device wifi
```

## Connect to an access point

```bash
nmcli device wifi connect '<AP NAME>' password '<PASSWORD>'
```

## AP Mode?
Doesn't seem to work. Errors when bringing up the connection.

```bash
nmcli con add type wifi ifname wlan0 mode ap con-name X6200-AP ssid X6200 autoconnect false
nmcli con modify X6200-AP wifi.band bg
nmcli con modify X6200-AP wifi.channel 3
nmcli con modify X6200-AP wifi-sec.key-mgmt wpa-psk
nmcli con modify X6200-AP wifi-sec.proto rsn
nmcli con modify X6200-AP wifi-sec.group ccmp
nmcli con modify X6200-AP wifi-sec.pairwise ccmp
nmcli con modify X6200-AP wifi-sec.psk "x6200wifipassword"
nmcli con modify X6200-AP ipv4.method shared ipv4.address 192.168.62.1/24
nmcli con modify X6200-AP ipv6.method disabled
```

```bash
nmcli con up X6200-AP
```

# hb9eue research (thank you!!!)
Adding [hb9eue's research](https://github.com/tom-acco/Xiegu-X6200-Research/issues/1) here for now to capture it.
TODO: Sort through this in more detail later

## Bugs
- RTTY demodulation most certainly completely broken (tested during EA contest right now, completely unable to decode even the strongest signals neither in USB nor U-DIGI Modem). Transmitting RTTY is fine.
- PSK demodulation most certainly also broken. Unable to decode ANY PSK transmissions. Transmitting PSK31 is fine.
- USB Audio from TRX to Computer => Over the limit, causes clipping, 'Line out' volume does not affect the level. 'USB Microphone Input Level' on Computer has to be reduced to about 37% for adequate level.
- USB Audio from Computer to TRX does overdrive the TRX when set to 0db, USB Playback volume has to be reduced to about 90% to achieve a good signal in digital modes.
- Audio from Handheld Microphone is not very clear. Mic Gain settings don't seem to change anything.
- Pairing Bluetooth via GUI, especially Headphones causes device to immediately crash (have not attemted via hcitool on commandline yet). - not re-attempted after fixing FPGA flashing.

## Further Research
- Sound is managed by Alsa and Pulseaudio
- The complete x6100 binary and gui also seem to exist under: /usr/app_qt/
- There are traces of an ofono and nginx installation but no binaries
- snmpd is installed, but no config file present
- /etc/init.d/ reveals what is being run at startup and shutdown
- the QT Gui application stores all settings in an sqlite database for which a client is installed, so you can .dump the database: # sqlite3 /usr/app_qt/xparam.db comes handy to edit for example stored messages.
- The device creates two WLAN interfaces linked to the same phy. Was one intended to work as AP?
- /etc/udev/rules.d also delivers some further insight
- Sunxi 8i ArmV7 4 Core CPU
- GPU: mali400
- Linux Kernel 5.8.9 with a lot of modules for network cards, unfortunately ipv6 modules are missing.
- Experimenting with alsamixer on the cli hints that audio from the microphones is routed to the FPGA (probably to performing equalizer stuff).
- Recorded Messages are under: /usr/app_qt/voice/ as
- voice_msg01: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz

## Updates
30.03.2024: Many of the Audio issues I previously described were most probably caused, because the FPGA firmware was not correctly flashed. After re-flashing audio is much better, levels are more reasonable! The Humming is almost completely gone. Also PSK is broken.