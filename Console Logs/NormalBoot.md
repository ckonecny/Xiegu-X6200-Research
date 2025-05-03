# Normal Boot

```
U-Boot SPL 2017.11 (Aug 27 2024 - 13:23:06)
DRAM: 1024 MiB
Trying to boot from MMC2




DRAM:  1 GiB
MMC:   SUNXI SD/MMC: 0, SUNXI SD/MMC: 1
*** Warning - bad CRC, using default environment

Setting up a 480x854 lcd console (overscan 0x0)
Video: Drawing the logo ...
Video: Call video_logo()
Video: splashimage = 0x40000000
Video: Call splash_screen_prepare()
Video: Call splash_source_load(), storage = MMC
Video: splashsource = mmc_fs
reading logo.bmp
In:    serial
Out:   serial
Err:   serial
Allwinner mUSB OTG (Peripheral)
Net:
Warning: usb_ether using MAC address from ROM
eth0: usb_ether
starting USB...
USB0:   USB EHCI 1.00
USB1:   USB OHCI 1.0
scanning bus 0 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
DEBUG: BootEnv bootdelay = 0
DEBUG: Use fdt bootdelay = 0
DEBUG: Actual bootdelay = 0
DEBUG: Call autoboot_command(), arg = run distro_bootcmd
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc1(part 0) is current device
Scanning mmc 1:1...
Found U-Boot script /boot.scr
reading /boot.scr
586 bytes read in 18 ms (31.3 KiB/s)
## Executing script at 43100000
------------ x6200 boot script ------------
reading logo.bmp
25654 bytes read in 24 ms (1 MiB/s)
reading zImage
4956144 bytes read in 251 ms (18.8 MiB/s)
reading sun8i-r16-x6200.dtb
26472 bytes read in 25 ms (1 MiB/s)
## Flattened Device Tree blob at 49000000
   Booting using the fdt blob at 0x49000000
   Loading Device Tree to 49ff6000, end 49fff767 ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 5.8.9 (jet@ubuntu) (arm-buildroot-linux-gnueabihf-gcc.br_real (Buildroot 2020.02.9) 8.4.0, GNU ld (GNU Binutils) 2.32) #116 SMP PREEMPT Sat Sep 21 11:59:57 HKT 2024
[    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
[    0.000000] CPU: div instructions available: patching division code
[    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
[    0.000000] OF: fdt: Machine model: XIEGU Tech X6200 Transceiver
[    0.000000] Memory policy: Data cache writealloc
[    0.000000] Reserved memory: created CMA memory pool at 0x4a000000, size 128 MiB
[    0.000000] OF: reserved mem: initialized node cma@4a000000, compatible id shared-dma-pool
[    0.000000] Zone ranges:
[    0.000000]   Normal   [mem 0x0000000040000000-0x000000006fffffff]
[    0.000000]   HighMem  [mem 0x0000000070000000-0x000000007fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000040000000-0x000000007fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000040000000-0x000000007fffffff]
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: Using PSCI v0.1 Function IDs from DT
[    0.000000] percpu: Embedded 15 pages/cpu s30988 r8192 d22260 u61440
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
[    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/mmcblk1p2 rootwait panic=10 fbcon=rotate:3
[    0.000000] video=VGA:480x800
[    0.000000] splashimage=0x40000000
[    0.000000] splashsource=mmc_fs
[    0.000000] splashpos=m,m
[    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
[    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] Memory: 895848K/1048576K available (7168K kernel code, 526K rwdata, 2072K rodata, 1024K init, 252K bss, 21656K reserved, 131072K cma-reserved, 262132K highmem)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
[    0.000000]  Trampoline variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x324/0x4c0 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 24.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[    0.000007] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000019] Switching to timer-based delay loop, resolution 41ns
[    0.000272] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635851949 ns
[    0.000767] Console: colour dummy device 80x30
[    0.000828] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=240000)
[    0.000843] pid_max: default: 32768 minimum: 301
[    0.001001] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.001021] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.001878] CPU: Testing write buffer coherency: ok
[    0.002314] CPU0: update cpu_capacity 1024
[    0.002326] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
[    0.002967] Setting up static identity map for 0x40100000 - 0x40100060
[    0.003112] rcu: Hierarchical SRCU implementation.
[    0.003737] smp: Bringing up secondary CPUs ...
[    0.004711] CPU1: update cpu_capacity 1024
[    0.004720] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
[    0.005767] CPU2: update cpu_capacity 1024
[    0.005773] CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
[    0.006752] CPU3: update cpu_capacity 1024
[    0.006758] CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
[    0.006855] smp: Brought up 1 node, 4 CPUs
[    0.006880] SMP: Total of 4 processors activated (192.00 BogoMIPS).
[    0.006886] CPU: All CPU(s) started in HYP mode.
[    0.006891] CPU: Virtualization extensions available.
[    0.007666] devtmpfs: initialized
[    0.014485] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
[    0.014908] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.014936] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.019646] pinctrl core: initialized pinctrl subsystem
[    0.020549] thermal_sys: Registered thermal governor 'step_wise'
[    0.021736] NET: Registered protocol family 16
[    0.023463] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.024840] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
[    0.024854] hw-breakpoint: maximum watchpoint size is 8 bytes.
[    0.047788] vgaarb: loaded
[    0.048266] SCSI subsystem initialized
[    0.048798] usbcore: registered new interface driver usbfs
[    0.048847] usbcore: registered new interface driver hub
[    0.048924] usbcore: registered new device driver usb
[    0.049147] mc: Linux media interface: v0.10
[    0.049181] videodev: Linux video capture interface: v2.00
[    0.049254] pps_core: LinuxPPS API ver. 1 registered
[    0.049261] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.049295] PTP clock support registered
[    0.049794] Advanced Linux Sound Architecture Driver Initialized.
[    0.051068] clocksource: Switched to clocksource arch_sys_counter
[    0.058976] NET: Registered protocol family 2
[    0.059595] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
[    0.059624] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
[    0.059698] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.059813] TCP: Hash tables configured (established 8192 bind 8192)
[    0.059990] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.060077] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.060464] NET: Registered protocol family 1
[    0.061228] RPC: Registered named UNIX socket transport module.
[    0.061243] RPC: Registered udp transport module.
[    0.061249] RPC: Registered tcp transport module.
[    0.061254] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.061269] PCI: CLS 0 bytes, default 64
[    0.063034] Initialise system trusted keyrings
[    0.063300] workingset: timestamp_bits=30 max_order=18 bucket_order=0
[    0.069686] NFS: Registering the id_resolver key type
[    0.069735] Key type id_resolver registered
[    0.069743] Key type id_legacy registered
[    0.069861] Key type asymmetric registered
[    0.069871] Asymmetric key parser 'x509' registered
[    0.069926] bounce: pool size: 64 pages
[    0.069993] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.070003] io scheduler mq-deadline registered
[    0.070010] io scheduler kyber registered
[    0.075567] sun8i-a33-pinctrl 1c20800.pinctrl: initialized sunXi PIO driver
[    0.128591] Serial: 8250/16550 driver, 8 ports, IRQ sharing disabled
[    0.131747] printk: console [ttyS0] disabled
[    0.151970] 1c28000.serial: ttyS0 at MMIO 0x1c28000 (irq = 34, base_baud = 1500000) is a U6_16550A
[    0.832363] printk: console [ttyS0] enabled
[    0.857881] 1c28c00.serial: ttyS1 at MMIO 0x1c28c00 (irq = 35, base_baud = 1500000) is a U6_16550A
[    0.874553] lima 1c40000.gpu: gp - mali400 version major 1 minor 1
[    0.880782] lima 1c40000.gpu: pp0 - mali400 version major 1 minor 1
[    0.887174] lima 1c40000.gpu: pp1 - mali400 version major 1 minor 1
[    0.893496] lima 1c40000.gpu: l2 cache 64K, 4-way, 64byte cache line, 64bit external bus
[    0.902055] lima 1c40000.gpu: bus rate = 200000000
[    0.906844] lima 1c40000.gpu: mod rate = 384000000
[    0.911780] lima 1c40000.gpu: dev_pm_opp_set_regulators: no regulator (mali) found: -19
[    0.920165] lima 1c40000.gpu: Failed to register cooling device
[    0.926583] [drm] Initialized lima 1.1.0 20191231 for 1c40000.gpu on minor 0
[    0.938526] libphy: Fixed MDIO Bus: probed
[    0.943021] CAN device driver interface
[    0.947726] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.954312] ehci-pci: EHCI PCI platform driver
[    0.958834] ehci-platform: EHCI generic platform driver
[    0.964477] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.970668] ohci-pci: OHCI PCI platform driver
[    0.975276] ohci-platform: OHCI generic platform driver
[    0.984393] input: matrix_keypad@0 as /devices/platform/matrix_keypad@0/input/input0
[    0.993245] rotary-encoder rotary@0: gray
[    0.997883] input: rotary@0 as /devices/platform/rotary@0/input/input1
[    1.004790] rotary-encoder rotary@1: gray
[    1.009292] input: rotary@1 as /devices/platform/rotary@1/input/input2
[    1.016183] rotary-encoder rotary@2: gray
[    1.020664] input: rotary@2 as /devices/platform/rotary@2/input/input3
[    1.027498] rotary-encoder rotary@3: gray
[    1.032107] input: rotary@3 as /devices/platform/rotary@3/input/input4
[    1.039861] sun6i-rtc 1f00000.rtc: registered as rtc0
[    1.044946] sun6i-rtc 1f00000.rtc: RTC enabled
[    1.049729] i2c /dev entries driver
[    1.056263] sunxi-wdt 1c20ca0.watchdog: Watchdog enabled (timeout=16 sec, nowayout=0)
[    1.068595] sun4i-ss 1c15000.crypto-engine: Die ID 5
[    1.075683] usbcore: registered new interface driver usbhid
[    1.081301] usbhid: USB HID core driver
[    1.088834] NET: Registered protocol family 17
[    1.093397] can: controller area network core (rev 20170425 abi 9)
[    1.099681] NET: Registered protocol family 29
[    1.104195] can: raw protocol (rev 20170425)
[    1.108463] can: broadcast manager protocol (rev 20170425 t)
[    1.114170] can: netlink gateway (rev 20190810) max_hops=1
[    1.119922] Key type dns_resolver registered
[    1.124468] Registering SWP/SWPB emulation handler
[    1.129309] Loading compiled-in X.509 certificates
[    1.147594] sun8i-a23-r-pinctrl 1f02c00.pinctrl: initialized sunXi PIO driver
[    1.155134] sun8i-a23-r-pinctrl 1f02c00.pinctrl: supply vcc-pl not found, using dummy regulator
[    1.185762] 1f02800.serial: ttyS2 at MMIO 0x1f02800 (irq = 50, base_baud = 1500000) is a U6_16550A
[    1.196457] panel@0 enforce active low on chipselect handle
[    1.207906] asoc-simple-card sound: sun8i <-> 1c22c00.dai mapping ok
[    1.216479] sunxi-rsb 1f03400.rsb: RSB running at 3000000 Hz
[    1.222682] axp20x-rsb sunxi-rsb-3a3: AXP20x variant AXP223 found
[    1.230761] input: axp20x-pek as /devices/platform/soc/1f03400.rsb/sunxi-rsb-3a3/axp221-pek/input/input5
[    1.242027] axp20x-adc axp22x-adc: DMA mask not set
[    1.247823] axp20x-battery-power-supply axp20x-battery-power-supply: DMA mask not set
[    1.256543] dcdc1: supplied by regulator-dummy
[    1.261138] vcc-3v0: Bringing 3300000uV into 3000000-3000000uV
[    1.267299] dcdc2: supplied by regulator-dummy
[    1.272571] dcdc3: supplied by regulator-dummy
[    1.277292] dcdc4: supplied by regulator-dummy
[    1.282022] dcdc5: supplied by regulator-dummy
[    1.286757] dc1sw: supplied by vcc-3v0
[    1.290762] dc5ldo: supplied by vcc-dram
[    1.295026] aldo1: supplied by regulator-dummy
[    1.299722] aldo2: supplied by regulator-dummy
[    1.304493] aldo3: supplied by regulator-dummy
[    1.309222] eldo1: supplied by vcc-3v0
[    1.313073] vcc-1v2-hsic: Bringing 700000uV into 1200000-1200000uV
[    1.319473] eldo2: supplied by vcc-3v0
[    1.323348] vcc-dsp: Bringing 700000uV into 3000000-3000000uV
[    1.329302] eldo3: supplied by vcc-3v0
[    1.333147] eldo3: Bringing 700000uV into 3000000-3000000uV
[    1.338971] dldo1: supplied by regulator-dummy
[    1.343536] vcc-wifi0: Bringing 700000uV into 3300000-3300000uV
[    1.349725] dldo2: supplied by regulator-dummy
[    1.354260] vcc-wifi1: Bringing 700000uV into 3300000-3300000uV
[    1.360423] dldo3: supplied by regulator-dummy
[    1.364959] vcc-3v0-csi: Bringing 700000uV into 3000000-3000000uV
[    1.371330] dldo4: supplied by regulator-dummy
[    1.376054] rtc_ldo: supplied by regulator-dummy
[    1.380874] ldo_io0: supplied by regulator-dummy
[    1.385804] ldo_io1: supplied by regulator-dummy
[    1.391332] axp20x-ac-power-supply axp20x-ac-power-supply: DMA mask not set
[    1.400032] axp20x-usb-power-supply axp20x-usb-power-supply: DMA mask not set
[    1.408249] axp20x-rsb sunxi-rsb-3a3: AXP20X driver loaded
[    1.415733] sun4i-drm display-engine: bound 1e00000.display-frontend (ops 0xc0853258)
[    1.424044] sun4i-drm display-engine: bound 1e60000.display-backend (ops 0xc0852a98)
[    1.431853] sun4i-drm display-engine: bound 1e70000.drc (ops 0xc08525c8)
[    1.439119] sun4i-drm display-engine: bound 1c0c000.lcd-controller (ops 0xc08515f8)
[    1.446808] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.453940] [drm] Initialized sun4i-drm 1.0.0 20150629 for display-engine on minor 1
[    1.679285] Console: switching to colour frame buffer device 100x30
[    1.710566] sun4i-drm display-engine: fb0: sun4i-drmdrmfb frame buffer device
[    1.718493] ehci-platform 1c1a000.usb: EHCI Host Controller
[    1.724136] ehci-platform 1c1a000.usb: new USB bus registered, assigned bus number 1
[    1.732335] ehci-platform 1c1a000.usb: irq 28, io mem 0x01c1a000
[    1.761077] ehci-platform 1c1a000.usb: USB 2.0 started, EHCI 1.00
[    1.767381] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.08
[    1.775663] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.782892] usb usb1: Product: EHCI Host Controller
[    1.787764] usb usb1: Manufacturer: Linux 5.8.9 ehci_hcd
[    1.793082] usb usb1: SerialNumber: 1c1a000.usb
[    1.798310] hub 1-0:1.0: USB hub found
[    1.802138] hub 1-0:1.0: 1 port detected
[    1.806949] ohci-platform 1c1a400.usb: Generic Platform OHCI controller
[    1.813627] ohci-platform 1c1a400.usb: new USB bus registered, assigned bus number 2
[    1.821704] ohci-platform 1c1a400.usb: irq 29, io mem 0x01c1a400
[    1.895256] usb usb2: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 5.08
[    1.903536] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.910749] usb usb2: Product: Generic Platform OHCI controller
[    1.916675] usb usb2: Manufacturer: Linux 5.8.9 ohci_hcd
[    1.921994] usb usb2: SerialNumber: 1c1a400.usb
[    1.927068] hub 2-0:1.0: USB hub found
[    1.930849] hub 2-0:1.0: 1 port detected
[    1.937718] sunxi-mmc 1c0f000.mmc: Got CD GPIO
[    1.967634] sunxi-mmc 1c0f000.mmc: initialized, max. request size: 16384 KB
[    1.976044] sunxi-mmc 1c11000.mmc: allocated mmc-pwrseq
[    2.006680] sunxi-mmc 1c11000.mmc: initialized, max. request size: 16384 KB
[    2.014151] ALSA device list:
[    2.017122]   #0: sun8i-a33-audio
[    2.021543] Waiting for root device /dev/mmcblk1p2...
[    2.123365] mmc1: new DDR MMC card at address 0001
[    2.129245] mmcblk1: mmc1:0001 8GTF4R 7.28 GiB
[    2.134368] mmcblk1boot0: mmc1:0001 8GTF4R partition 1 4.00 MiB
[    2.140806] mmcblk1boot1: mmc1:0001 8GTF4R partition 2 4.00 MiB
[    2.149527]  mmcblk1: p1 p2
[    2.178317] EXT4-fs (mmcblk1p2): mounted filesystem with ordered data mode. Opts: (null)
[    2.186569] VFS: Mounted root (ext4 filesystem) readonly on device 179:2.
[    2.196172] devtmpfs: mounted
[    2.200323] Freeing unused kernel memory: 1024K
[    2.221294] Run /sbin/init as init process
[    2.240227] random: fast init done
[    2.301445] EXT4-fs (mmcblk1p2): re-mounted. Opts: (null)
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Populating /dev using udev: [    2.444917] udevd[120]: starting version 3.2.9
[    2.463429] random: udevd: uninitialized urandom read (16 bytes read)
[    2.470624] random: udevd: uninitialized urandom read (16 bytes read)
[    2.477934] random: udevd: uninitialized urandom read (16 bytes read)
[    2.510995] udevd[120]: specified group 'gpib' unknown
[    2.520589] udevd[121]: starting eudev-3.2.9
[    2.736092] usb_phy_generic usb_phy_generic.1.auto: supply vcc not found, using dummy regulator
[    2.747228] musb-hdrc musb-hdrc.2.auto: MUSB HDRC host driver
[    2.753152] musb-hdrc musb-hdrc.2.auto: new USB bus registered, assigned bus number 3
[    2.761453] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.08
[    2.769756] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    2.771608] rtc rtc1: invalid alarm value: 1970-09-04T03:65:00
[    2.778901] usb usb3: Product: MUSB HDRC host driver
[    2.788368] rtc-pcf8563 1-0051: registered as rtc1
[    2.789066] usb usb3: Manufacturer: Linux 5.8.9 musb-hcd
[    2.798615] usb usb3: SerialNumber: musb-hdrc.2.auto
[    2.798631] rtc-pcf8563 1-0051: setting system clock to 1970-09-28T00:09:23 UTC (23328563)
[    2.814583] hub 3-0:1.0: USB hub found
[    2.818564] hub 3-0:1.0: 1 port detected
[    2.823133] phy phy-1c19400.phy.1: External vbus detected, not enabling our own vbus
done
Initializing random number generator: OK
Saving random seed: [    4.154353] urandom_read: 2 callbacks suppressed
[    4.154368] random: dd: uninitialized urandom read (512 bytes read)
OK
Starting haveged: haveged: listening socket at 3
OK
Starting system message bus: [    4.256353] random: dbus-uuidgen: uninitialized urandom read (12 bytes read)
[    4.263719] random: dbus-uuidgen: uninitialized urandom read (8 bytes read)
done
Starting network: OK
Starting NetworkManager ... done.
Starting sntp: sntp 4.2.8p15@1.3728-o Tue Aug 27 04:52:21 UTC 2024 (1)
pool.ntp.org lookup error Temporary failure in name resolution
FAIL
Starting ntpd: OK
Starting pulseaudio: W: [pulseaudio] main.c: This program is not intended to be run as root (unless --system is specified).
OK
[    6.103261] random: crng init done
[    6.106743] random: 2 urandom warning(s) missed due to ratelimiting
Starting sshd: OK
Init amixer:  OK
Starting bluetooth
[    6.550089] Bluetooth: Core ver 2.22
[    6.556380] NET: Registered protocol family 31
[    6.561233] Bluetooth: HCI device and connection manager initialized
[    6.568784] Bluetooth: HCI socket layer initialized
[    6.574406] Bluetooth: L2CAP socket layer initialized
[    6.580336] Bluetooth: SCO socket layer initialized
adding SP serviece (first time)
Serial Port service registered
[    8.552867] Bluetooth: RFCOMM TTY layer initialized
Starting vsftpd: [    8.558068] Bluetooth: RFCOMM socket layer initialized
[    8.564644] Bluetooth: RFCOMM ver 1.11
OK
Starting monit:
Starting Monit 5.26.0 daemon
OK

Welcome to XIEGU X6200!
XIEGU-x6200 login: [   28.615799] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[   28.669506] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
```