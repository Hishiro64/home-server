[<- index](/README.md)
# Storage Considerations

* ### Micro SD card
    If you plan to use a micro-SD card, just proceed with the Raspberry Pi Imager. Note that it will be less reliable and slower. Otherwise, it's cheaper, uses less power, and more portable. Consider a SATA SSD for an upgrade.

* ### Hard Drive
    A hard drive might be a cheap choice for lots of storage. However, would likely require external power. It's less portable without a secure mounting solution. Needs SATA adapter.

* ### M.2/NVME
    Excessive and expensive but does great in terms of portability and speed. It needs a different adapter/enclosure and heat can be a minor issue, but nothing a small heatsink wouldn't solve. Won't be close to utilizing the max capable speed. External power might be needed. **I wouldn't recommend unless you already have one laying around.** 

* ### SATA SSD *(Recommended)*
    The best balance of all worlds, and the one I use and recommend.

    * Cheaper than M.2/NVME

    * Most should work fine. Try to avoid buying a DRAM-less SSD. 

    * Cooling should not be a problem, but if you are worried, you can just put a plane heat sink on top of the SSD's hottest sections. You can even take off the top cover and place the heat sinks directly over the controller, cache, NAND Flash chips; Removing the top cover sometimes makes lower capacity drives take up less space. Overkill and may void your warranty.

    * Still will not use the max capable speed. But closer to them compared to M.2/NVME. Not as bottlenecked.

    * Probably get away without external power. (Without external power, I never received undervoltage warnings on neither of my tested SSDs.)

    * The USB to SATA adapter should support UASP and Trim. The one I used does support Trim only after a [firmware update](/docs/SSD/SATA%20Adapter%20Nonsense.md).

    * Drives above 2TB requires some [additional setup](/docs/SSD/SATA%20SSD%20Setup.md).

* ### Network Drives
    * If you already have one set up on a NAS or a separate server/pi, you may want to incorporate it. Whether it's to serve a backup or used directly by docker as a NFS Volume, depending on how it's set up, it may be advantageous. You will know if this applies to you.
