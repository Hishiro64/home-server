[<- index](/README.md)

# Storage Plan

Ignoring drive failures. In the case where you have to migrate drives, migrate OS, or you have a bricked OS, it will always be a hassle. So, it's best to mitigate as much as we can by planning around these issues, to have an easier time later.

 * The Raspberry Pi Imager is limited, so you can't create or write to just one or more partitions. There's no way to create multi-boot natively from the imager. You will have to flash the whole thing. You can also have trouble with copying the contents temporarily over to another drive because of the lack of ext4 support outside of Linux. Additionally, the cost scales up with drive size. Lastly, the Raspberry Pi Imager was designed for micro-SD cards. SATA SSD support was added for native usb boot, but still creates partitions in MBR. There are community solutions available, but official ones would be preferred. 

   * Sometimes Raspberry Pi OS can't be migrated like with Bullseye --> Bookworm. You can read about it in the [last section](https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/#:~:text=We%20have%20always,tool%20of%20choice.) of this post. If you have a 2TB drive that's filled up all the way, you will need to move the contents to another 2TB drive and back again. The cost will scale up with size. 
   
   * If you need to read/write to the drive, you can really only do this easily on Linux. Windows doesn't support ext4, and only [partial support](https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk) exists through WSL2. (No SATA to USB) There's no great solution to interacting with ext4 outside of Linux.

 ## Spilt Storage?

* Use a primary small drive and a secondary large drive. Keep persistent data on the larger drive and you may want to format it as NTFS, so it will be readable on Windows. Having now two storage devices means you'll likely need external power if you didn't already. You could use a micro-SD as the primary small drive if you have too.

* Mount Docker volumes and binds to a NFS share. And just use a small SSD on the pi. Splitting it with two systems. Probably more reliable if that NFS share is on a dedicated NAS. Depends on the setup.

* Use a spare micro-SD or SATA-SSD for testing changes, then deploy them to your main drive. If you don't want downtime, you can test Docker changes on any PC, and OS changes on another Pi... Maybe a good excuse to buy that Pi-5?

It's a simple fix until a better solution is available. Some of this will probably be resolved with the Pi-5 having PCIe NVMe/M.2 boot in the future.

Or be like me and just yolo it, putting it all on one large drive.
