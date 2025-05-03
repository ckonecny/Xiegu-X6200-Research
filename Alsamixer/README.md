# Alsamixer
Alsamixer settings are configured on device start up in `/etc/init.d/S51amixer`.

It's probably best to SSH in and use the `alsamixer` GUI to set the values, then use `amixer -c 0 sget '<control id>'` to get the value and adjust in the init.d file to save for startup

## Get ADC gain
```bash
amixer -c 0 sget 'ADC Gain'
```

```bash
[root@XIEGU-x6200:/root]#  amixer -c 0 sget 'ADC Gain'
Simple mixer control 'ADC Gain',0
  Capabilities: cvolume cvolume-joined
  Capture channels: Mono
  Limits: Capture 0 - 7
  Mono: Capture 4 [57%] [1.50dB]
```

## Set ADC gain
```bash
amixer -c 0 sset 'ADC Gain',0 3 <0-7>
```

Default:
```bash
amixer -c 0 sset 'ADC Gain',0 3 1
```

## /etc/init.d/S51amixer
```bash
#!/bin/sh

source /etc/profile

start() {
        printf "Init amixer: "
        amixer cset numid=10,iface=MIXER,name='AIF1 Data Digital ADC Capture Switch' on 1> /dev/null
        amixer cset numid=19,iface=MIXER,name='Mic1 Capture Switch' on 1> /dev/null
        amixer -c 0 sset 'ADC Gain',0 3 1> /dev/null
        amixer -c 0 sset 'Mic1 Boost',0 0 1> /dev/null
        amixer -c 0 sset 'Mic1',0 7 1> /dev/null
        amixer -c 0 sset 'Mic1',0 unmute 1> /dev/null
        amixer cset numid=9,iface=MIXER,name='AIF1 Slot 0 Digital DAC Playback Switch' on 1> /dev/null
        amixer -c 0 sset 'DAC',0 on 1> /dev/null
        amixer -c 0 sset 'Headphone',0 63 1> /dev/null
        amixer -c 0 sset 'Headphone',0 unmute 1> /dev/null
        echo " OK"
}
stop() {
        printf "Deinit amixer: "
        amixer cset numid=10,iface=MIXER,name='AIF1 Data Digital ADC Capture Switch' off 1> /dev/null
        amixer cset numid=19,iface=MIXER,name='Mic1 Capture Switch' off 1> /dev/null
        amixer -c 0 sset 'ADC Gain',0 0 1> /dev/null
        amixer -c 0 sset 'Mic1 Boost',0 0 1> /dev/null
        amixer -c 0 sset 'Mic1',0 0 1> /dev/null
        amixer -c 0 sset 'Mic1',0 mute 1> /dev/null
        amixer cset numid=9,iface=MIXER,name='AIF1 Slot 0 Digital DAC Playback Switch' off 1> /dev/null
        amixer -c 0 sset 'DAC',0 off 1> /dev/null
        amixer -c 0 sset 'Headphone',0 0 1> /dev/null
        amixer -c 0 sset 'Headphone',0 mute 1> /dev/null
        echo " OK"
}
restart() {
        stop
        start
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart|reload)
        restart
        ;;
  *)
        echo "Usage: $0 {start|stop|restart|reload}"
        exit 1
esac

exit $?
```