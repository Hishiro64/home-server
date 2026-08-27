# The Build

The build is quite simple. You only need a Raspberry Pi 4 8Gb, USB-C power adapter, some active cooling solution (heat sink + fan), RJ45 Patch cable, storage, and housing. The only thing that may vary would be the storage and ram. The more ram you have the more simultaneous services you can have running at the same time. Since RAM is soldered, and you'll be hopefully running this server for years like I have, I wouldn't consider anything other than the 8Gb version. It's more of a mixed bag for storage, and with fluctuating costs, you will have to plan ahead.

## Storage
I don't want anyone to pretend that this platform has the foundation for robust storage configurations. While it may be doable, you should reserve that route for some other x86 platform. My recommendation would be to keep it simple with one mass storage device like a SATA SSD and regular offsite backups for important directories. If you need to expand, use NFS volumes on a hosted on a separate machine.

## Planning Around Limitations

Ignoring drive failures. In the case where you have to migrate drives, migrate OS, or you have a bricked OS, it will always be a hassle. So, it's best to mitigate as much as we can by planning around these issues, to have an easier time later.

* The Raspberry Pi Imager is limited, so you can't create or write to just one or more partitions. There's no way to create multi-boot natively from the imager. You will have to flash the whole thing. You could also have trouble with copying the contents temporarily over to another drive because of lackluster ext4 support outside of Linux. Additionally, the cost scales up with drive size. Lastly, the Raspberry Pi Imager was designed for micro-SD cards. SATA SSD support was added with native USB Boot, but still creates partitions in MBR. There are community solutions available that work fine. But it's one more manual step that can be messed up. Official fixes would be preferred. 

* Sometimes Raspberry Pi OS can't be migrated like with Bullseye --> Bookworm. You can read about it in the [last section](https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/#:~:text=We%20have%20always,tool%20of%20choice.) of this post. If you have a 2TB drive that's filled up all the way, you will need to move the contents to another 2TB drive and back again. That migration cost will scale up with size. 

* If you need to read/write to the drive unmounted from the server, you can only really do this easily on Linux. Windows doesn't support ext4, and only [partial support](https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk) exists through WSL2. (No SATA to USB) There's no great solution to interacting with ext4 outside of Linux.

 ### Spilt Storage Solutions

1. Use a primary small drive and a secondary large drive. Keep persistent data on the larger drive, and you may want to format it as NTFS, so it will be readable on Windows. Having now two storage devices means you'll likely need external power if you didn't already. You could use a micro-SD as the primary small drive if you have too.

2. Mount Docker volumes and binds to a NFS share. And just use a small SSD on the pi. Splitting it with two systems. Probably more reliable if that NFS share is on a dedicated NAS. Depends on the setup.

3. Use a spare micro-SD or SATA-SSD for testing changes, then deploy them to your main drive. If you don't want downtime, you can test Docker changes on any PC, and OS changes on another Pi... Maybe a good excuse to buy that Pi-5?

It's a simple fix until a better solution is available. Some of this will probably be resolved with the Pi-5 having PCIe NVMe/M.2 boot in the future.

Or be like me and just yolo it, putting it all on one large drive.

## Storage Options

### Micro SD card
If you plan to use a micro-SD card, just proceed with the Raspberry Pi Imager. Note that it will be less reliable and slower. Otherwise, it's cheaper, uses less power, and more portable. Consider a SATA SSD for an upgrade.

### Hard Drive
A hard drive might be a cheap choice for lots of storage space. However, would likely require external power. It's less portable and less reliable without a secure mounting solution. Needs SATA adapter.

### M.2/NVME
Excessive and expensive but does great in terms of portability and speed. It needs a different adapter/enclosure and heat can be a minor issue, but nothing a small heatsink wouldn't solve. It won't be close to utilizing the max capable speed. External power might be needed. **I wouldn't recommend unless you already have one laying around.** 

### SATA SSD *(Recommended)*
The best balance of all worlds, and the one I selected and recommend.

* Cheaper than M.2/NVME

* Most should work fine. Avoid buying a DRAM-less SSD. 

* Cooling should not be a problem, but if you are worried, you can just put a plane heat sink on top of the SSD's hottest sections. You can even take off the top cover and place the heat sinks directly over the controller, cache, NAND Flash chips; Removing the top cover sometimes makes lower capacity drives take up less space. Overkill and may void your warranty.

* Not as bottlenecked. Still won't use the max capable speed. But closer in line than compared to the M.2/NVME. 

* Probably get away without external power. (Without external power, I never received an under voltage warning on neither of my tested SSDs.)

* The USB to SATA adapter should support UASP and Trim. The adapter I selected does support Trim only after a [firmware update](/docs/SSD/SATA%20Adapter%20Nonsense.md). Trim will also need to be enabled manually.

* Drives above 2TB requires some [additional setup](/docs/SSD/SATA%20SSD%20Setup.md).

### Network Drives (Off-site)
* If you already have one set up on a NAS or a separate server/pi, you may want to incorporate it. Whether it's to serve a backup or used directly by docker as a NFS Volume, depending on how it's set up, it may be advantageous. You will know if this applies to you.
