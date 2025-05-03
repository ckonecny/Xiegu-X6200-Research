# Firmware Update Log

```
U-Boot SPL 2017.11 (Aug 27 2024 - 13:23:06)
DRAM: 1024 MiB
Trying to boot from MMC1




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
mmc0 is current device
Scanning mmc 0:1...
Found U-Boot script /boot.scr
reading /boot.scr
493 bytes read in 20 ms (23.4 KiB/s)
## Executing script at 43100000
------------ x6200 boot script(TF debug version) ------------
reading logo.bmp
25654 bytes read in 24 ms (1 MiB/s)
reading zImage
4956144 bytes read in 252 ms (18.8 MiB/s)
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
[    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait panic=10 fbcon=rotate:3
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
[    0.000008] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[    0.000020] Switching to timer-based delay loop, resolution 41ns
[    0.000275] clocksource: timer: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635851949 ns
[    0.000771] Console: colour dummy device 80x30
[    0.000836] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=240000)
[    0.000850] pid_max: default: 32768 minimum: 301
[    0.001003] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.001019] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
[    0.001878] CPU: Testing write buffer coherency: ok
[    0.002302] CPU0: update cpu_capacity 1024
[    0.002313] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
[    0.002951] Setting up static identity map for 0x40100000 - 0x40100060
[    0.003097] rcu: Hierarchical SRCU implementation.
[    0.003746] smp: Bringing up secondary CPUs ...
[    0.004727] CPU1: update cpu_capacity 1024
[    0.004736] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
[    0.005791] CPU2: update cpu_capacity 1024
[    0.005798] CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
[    0.006746] CPU3: update cpu_capacity 1024
[    0.006752] CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
[    0.006850] smp: Brought up 1 node, 4 CPUs
[    0.006874] SMP: Total of 4 processors activated (192.00 BogoMIPS).
[    0.006880] CPU: All CPU(s) started in HYP mode.
[    0.006885] CPU: Virtualization extensions available.
[    0.007672] devtmpfs: initialized
[    0.014451] VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
[    0.014876] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.014905] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.019612] pinctrl core: initialized pinctrl subsystem
[    0.020483] thermal_sys: Registered thermal governor 'step_wise'
[    0.021680] NET: Registered protocol family 16
[    0.023485] DMA: preallocated 256 KiB pool for atomic coherent allocations
[    0.024863] hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
[    0.024879] hw-breakpoint: maximum watchpoint size is 8 bytes.
[    0.047671] vgaarb: loaded
[    0.048155] SCSI subsystem initialized
[    0.048672] usbcore: registered new interface driver usbfs
[    0.048721] usbcore: registered new interface driver hub
[    0.048801] usbcore: registered new device driver usb
[    0.049018] mc: Linux media interface: v0.10
[    0.049052] videodev: Linux video capture interface: v2.00
[    0.049123] pps_core: LinuxPPS API ver. 1 registered
[    0.049129] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.049164] PTP clock support registered
[    0.049651] Advanced Linux Sound Architecture Driver Initialized.
[    0.050886] clocksource: Switched to clocksource arch_sys_counter
[    0.058953] NET: Registered protocol family 2
[    0.059568] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
[    0.059598] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
[    0.059674] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.059790] TCP: Hash tables configured (established 8192 bind 8192)
[    0.059966] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.060055] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
[    0.060425] NET: Registered protocol family 1
[    0.061164] RPC: Registered named UNIX socket transport module.
[    0.061176] RPC: Registered udp transport module.
[    0.061182] RPC: Registered tcp transport module.
[    0.061188] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.061203] PCI: CLS 0 bytes, default 64
[    0.062968] Initialise system trusted keyrings
[    0.063215] workingset: timestamp_bits=30 max_order=18 bucket_order=0
[    0.069536] NFS: Registering the id_resolver key type
[    0.069585] Key type id_resolver registered
[    0.069593] Key type id_legacy registered
[    0.069709] Key type asymmetric registered
[    0.069720] Asymmetric key parser 'x509' registered
[    0.069775] bounce: pool size: 64 pages
[    0.069829] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.069840] io scheduler mq-deadline registered
[    0.069847] io scheduler kyber registered
[    0.075396] sun8i-a33-pinctrl 1c20800.pinctrl: initialized sunXi PIO driver
[    0.131093] Serial: 8250/16550 driver, 8 ports, IRQ sharing disabled
[    0.134236] printk: console [ttyS0] disabled
[    0.154461] 1c28000.serial: ttyS0 at MMIO 0x1c28000 (irq = 34, base_baud = 1500000) is a U6_16550A
[    0.834798] printk: console [ttyS0] enabled
[    0.860292] 1c28c00.serial: ttyS1 at MMIO 0x1c28c00 (irq = 35, base_baud = 1500000) is a U6_16550A
[    0.876911] lima 1c40000.gpu: gp - mali400 version major 1 minor 1
[    0.883246] lima 1c40000.gpu: pp0 - mali400 version major 1 minor 1
[    0.889564] lima 1c40000.gpu: pp1 - mali400 version major 1 minor 1
[    0.895887] lima 1c40000.gpu: l2 cache 64K, 4-way, 64byte cache line, 64bit external bus
[    0.904473] lima 1c40000.gpu: bus rate = 200000000
[    0.909265] lima 1c40000.gpu: mod rate = 384000000
[    0.914197] lima 1c40000.gpu: dev_pm_opp_set_regulators: no regulator (mali) found: -19
[    0.922638] lima 1c40000.gpu: Failed to register cooling device
[    0.929011] [drm] Initialized lima 1.1.0 20191231 for 1c40000.gpu on minor 0
[    0.941046] libphy: Fixed MDIO Bus: probed
[    0.945494] CAN device driver interface
[    0.950193] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.956785] ehci-pci: EHCI PCI platform driver
[    0.961323] ehci-platform: EHCI generic platform driver
[    0.966927] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.973174] ohci-pci: OHCI PCI platform driver
[    0.977657] ohci-platform: OHCI generic platform driver
[    0.986879] input: matrix_keypad@0 as /devices/platform/matrix_keypad@0/input/input0
[    0.995728] rotary-encoder rotary@0: gray
[    1.000379] input: rotary@0 as /devices/platform/rotary@0/input/input1
[    1.007237] rotary-encoder rotary@1: gray
[    1.011830] input: rotary@1 as /devices/platform/rotary@1/input/input2
[    1.018636] rotary-encoder rotary@2: gray
[    1.023164] input: rotary@2 as /devices/platform/rotary@2/input/input3
[    1.029983] rotary-encoder rotary@3: gray
[    1.034538] input: rotary@3 as /devices/platform/rotary@3/input/input4
[    1.042455] sun6i-rtc 1f00000.rtc: registered as rtc0
[    1.047505] sun6i-rtc 1f00000.rtc: RTC enabled
[    1.052326] i2c /dev entries driver
[    1.058833] sunxi-wdt 1c20ca0.watchdog: Watchdog enabled (timeout=16 sec, nowayout=0)
[    1.071283] sun4i-ss 1c15000.crypto-engine: Die ID 5
[    1.078214] usbcore: registered new interface driver usbhid
[    1.083834] usbhid: USB HID core driver
[    1.091407] NET: Registered protocol family 17
[    1.095884] can: controller area network core (rev 20170425 abi 9)
[    1.102315] NET: Registered protocol family 29
[    1.106760] can: raw protocol (rev 20170425)
[    1.111105] can: broadcast manager protocol (rev 20170425 t)
[    1.116766] can: netlink gateway (rev 20190810) max_hops=1
[    1.122546] Key type dns_resolver registered
[    1.127039] Registering SWP/SWPB emulation handler
[    1.131902] Loading compiled-in X.509 certificates
[    1.150244] sun8i-a23-r-pinctrl 1f02c00.pinctrl: initialized sunXi PIO driver
[    1.157774] sun8i-a23-r-pinctrl 1f02c00.pinctrl: supply vcc-pl not found, using dummy regulator
[    1.188562] 1f02800.serial: ttyS2 at MMIO 0x1f02800 (irq = 50, base_baud = 1500000) is a U6_16550A
[    1.199351] panel@0 enforce active low on chipselect handle
[    1.210677] asoc-simple-card sound: sun8i <-> 1c22c00.dai mapping ok
[    1.219190] sunxi-rsb 1f03400.rsb: RSB running at 3000000 Hz
[    1.225403] axp20x-rsb sunxi-rsb-3a3: AXP20x variant AXP223 found
[    1.233616] input: axp20x-pek as /devices/platform/soc/1f03400.rsb/sunxi-rsb-3a3/axp221-pek/input/input5
[    1.244796] axp20x-adc axp22x-adc: DMA mask not set
[    1.250597] axp20x-battery-power-supply axp20x-battery-power-supply: DMA mask not set
[    1.259261] dcdc1: supplied by regulator-dummy
[    1.263845] vcc-3v0: Bringing 3300000uV into 3000000-3000000uV
[    1.270021] dcdc2: supplied by regulator-dummy
[    1.275320] dcdc3: supplied by regulator-dummy
[    1.280025] dcdc4: supplied by regulator-dummy
[    1.284781] dcdc5: supplied by regulator-dummy
[    1.289524] dc1sw: supplied by vcc-3v0
[    1.293566] dc5ldo: supplied by vcc-dram
[    1.297787] aldo1: supplied by regulator-dummy
[    1.302520] aldo2: supplied by regulator-dummy
[    1.307265] aldo3: supplied by regulator-dummy
[    1.312018] eldo1: supplied by vcc-3v0
[    1.315836] vcc-1v2-hsic: Bringing 700000uV into 1200000-1200000uV
[    1.322250] eldo2: supplied by vcc-3v0
[    1.326101] vcc-dsp: Bringing 700000uV into 3000000-3000000uV
[    1.332085] eldo3: supplied by vcc-3v0
[    1.335902] eldo3: Bringing 700000uV into 3000000-3000000uV
[    1.341726] dldo1: supplied by regulator-dummy
[    1.346237] vcc-wifi0: Bringing 700000uV into 3300000-3300000uV
[    1.352463] dldo2: supplied by regulator-dummy
[    1.356974] vcc-wifi1: Bringing 700000uV into 3300000-3300000uV
[    1.363183] dldo3: supplied by regulator-dummy
[    1.367696] vcc-3v0-csi: Bringing 700000uV into 3000000-3000000uV
[    1.374063] dldo4: supplied by regulator-dummy
[    1.378810] rtc_ldo: supplied by regulator-dummy
[    1.383671] ldo_io0: supplied by regulator-dummy
[    1.388580] ldo_io1: supplied by regulator-dummy
[    1.394139] axp20x-ac-power-supply axp20x-ac-power-supply: DMA mask not set
[    1.402815] axp20x-usb-power-supply axp20x-usb-power-supply: DMA mask not set
[    1.411096] axp20x-rsb sunxi-rsb-3a3: AXP20X driver loaded
[    1.418536] sun4i-drm display-engine: bound 1e00000.display-frontend (ops 0xc0853258)
[    1.426842] sun4i-drm display-engine: bound 1e60000.display-backend (ops 0xc0852a98)
[    1.434660] sun4i-drm display-engine: bound 1e70000.drc (ops 0xc08525c8)
[    1.441970] sun4i-drm display-engine: bound 1c0c000.lcd-controller (ops 0xc08515f8)
[    1.449628] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.457308] [drm] Initialized sun4i-drm 1.0.0 20150629 for display-engine on minor 1
[    1.682448] Console: switching to colour frame buffer device 100x30
[    1.713682] sun4i-drm display-engine: fb0: sun4i-drmdrmfb frame buffer device
[    1.721632] ehci-platform 1c1a000.usb: EHCI Host Controller
[    1.727257] ehci-platform 1c1a000.usb: new USB bus registered, assigned bus number 1
[    1.735464] ehci-platform 1c1a000.usb: irq 28, io mem 0x01c1a000
[    1.770899] ehci-platform 1c1a000.usb: USB 2.0 started, EHCI 1.00
[    1.777242] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.08
[    1.785527] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.792754] usb usb1: Product: EHCI Host Controller
[    1.797626] usb usb1: Manufacturer: Linux 5.8.9 ehci_hcd
[    1.802955] usb usb1: SerialNumber: 1c1a000.usb
[    1.808183] hub 1-0:1.0: USB hub found
[    1.811996] hub 1-0:1.0: 1 port detected
[    1.816829] ohci-platform 1c1a400.usb: Generic Platform OHCI controller
[    1.823484] ohci-platform 1c1a400.usb: new USB bus registered, assigned bus number 2
[    1.831575] ohci-platform 1c1a400.usb: irq 29, io mem 0x01c1a400
[    1.905064] usb usb2: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 5.08
[    1.913343] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.920557] usb usb2: Product: Generic Platform OHCI controller
[    1.926485] usb usb2: Manufacturer: Linux 5.8.9 ohci_hcd
[    1.931818] usb usb2: SerialNumber: 1c1a400.usb
[    1.937797] hub 2-0:1.0: USB hub found
[    1.941603] hub 2-0:1.0: 1 port detected
[    1.947516] sunxi-mmc 1c0f000.mmc: Got CD GPIO
[    1.977448] sunxi-mmc 1c0f000.mmc: initialized, max. request size: 16384 KB
[    1.985873] sunxi-mmc 1c11000.mmc: allocated mmc-pwrseq
[    2.014299] sunxi-mmc 1c11000.mmc: initialized, max. request size: 16384 KB
[    2.021748] ALSA device list:
[    2.024720]   #0: sun8i-a33-audio
[    2.028970] Waiting for root device /dev/mmcblk0p2...
[    2.042161] mmc0: host does not support reading read-only switch, assuming write-enable
[    2.053423] mmc0: new high speed SDHC card at address aaaa
[    2.060014] mmcblk0: mmc0:aaaa SL16G 14.8 GiB
[    2.067558]  mmcblk0: p1 p2 p3
[    2.097813] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    2.106095] VFS: Mounted root (ext4 filesystem) readonly on device 179:2.
[    2.119676] devtmpfs: mounted
[    2.123958] Freeing unused kernel memory: 1024K
[    2.131130] Run /sbin/init as init process
[    2.147006] random: fast init done
[    2.165372] mmc1: new DDR MMC card at address 0001
[    2.171493] mmcblk1: mmc1:0001 8GTF4R 7.28 GiB
[    2.176543] mmcblk1boot0: mmc1:0001 8GTF4R partition 1 4.00 MiB
[    2.183331] mmcblk1boot1: mmc1:0001 8GTF4R partition 2 4.00 MiB
[    2.191690]  mmcblk1: p1 p2
[    2.526168] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Populating /dev using udev: [    2.714160] udevd[123]: starting version 3.2.9
[    2.748735] random: udevd: uninitialized urandom read (16 bytes read)
[    2.756075] random: udevd: uninitialized urandom read (16 bytes read)
[    2.763299] random: udevd: uninitialized urandom read (16 bytes read)
[    2.805902] udevd[123]: specified group 'gpib' unknown
[    2.815770] udevd[124]: starting eudev-3.2.9
[    3.060053] usb_phy_generic usb_phy_generic.1.auto: supply vcc not found, using dummy regulator
[    3.092684] musb-hdrc musb-hdrc.2.auto: MUSB HDRC host driver
[    3.098985] musb-hdrc musb-hdrc.2.auto: new USB bus registered, assigned bus number 3
[    3.107936] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.08
[    3.116590] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    3.124035] rtc rtc1: invalid alarm value: 1970-09-04T03:65:00
[    3.131106] rtc-pcf8563 1-0051: registered as rtc1
[    3.136062] usb usb3: Product: MUSB HDRC host driver
[    3.141539] usb usb3: Manufacturer: Linux 5.8.9 musb-hcd
[    3.147046] rtc-pcf8563 1-0051: setting system clock to 1970-09-28T00:04:27 UTC (23328267)
[    3.155957] usb usb3: SerialNumber: musb-hdrc.2.auto
[    3.176713] hub 3-0:1.0: USB hub found
[    3.182756] hub 3-0:1.0: 1 port detected
[    3.190669] phy phy-1c19400.phy.1: External vbus detected, not enabling our own vbus
done
Saving random seed: OK
Starting haveged: haveged: listening socket at 3
OK
Starting system message bus: done
Starting network: OK
Starting NetworkManager ... done.
Starting sntp: sntp 4.2.8p15@1.3728-o Tue Aug 27 04:52:21 UTC 2024 (1)
pool.ntp.org lookup error Temporary failure in name resolution
FAIL
Starting ntpd: OK
Starting pulseaudio: W: [pulseaudio] main.c: This program is not intended to be run as root (unless --system is specified).
[    5.345394] random: crng init done
[    5.348825] random: 7 urandom warning(s) missed due to ratelimiting
OK
ssh-keygen: generating new host keys: RSA DSA ECDSA ED25519
Starting sshd: OK
Init amixer:  OK
Starting bluetooth
[   14.276045] Bluetooth: Core ver 2.22
[   14.279763] NET: Registered protocol family 31
[   14.284487] Bluetooth: HCI device and connection manager initialized
[   14.290982] Bluetooth: HCI socket layer initialized
[   14.290997] Bluetooth: L2CAP socket layer initialized
[   14.305993] Bluetooth: SCO socket layer initialized
adding SP serviece (first time)
Serial Port service registered
Starting vsftpd: [   16.249365] Bluetooth: RFCOMM TTY layer initialized
[   16.254392] Bluetooth: RFCOMM socket layer initialized
OK[   16.259581] Bluetooth: RFCOMM ver 1.11

[   16.421471]  mmcblk1: p1 p2
[   16.581475] EXT4-fs (mmcblk1p2): mounted filesystem with ordered data mode. Opts: (null)
[INFO]: install result = 0
Stopping vsftpd: stopped /usr/sbin/vsftpd (pid 259)
OK
Stopping bluetooth
Deinit amixer:  OK
Stopping sshd: OK
Stopping pulseaudio: E: [pulseaudio] main.c: Failed to kill daemon: No such process
OK
Stopping ntpd: OK
Nothing to do, sntp is not a daemon.
Stopping NetworkManager ... done.
Stopping network: OK
Stopping system message bus: done
Stopping haveged: stopped /usr/sbin/haveged (pid 161)
OK
Saving random seed: OK
Stopping klogd: OK
Stopping syslogd: OK
Umounting removable devices: OK
Cleaning up leftovers in media dir: OK
[   47.977769] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
The system is going down NOW!
Sent SIGTERM to all processes
Sent SIGKILL to all processes
Requesting system poweroff
[   50.062773] reboot: Power down
```