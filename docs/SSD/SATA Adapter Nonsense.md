[<- index](/README.md)
# SATA Adapter Nonsense

If you happen to use the same **exact** SATA to USB adapter as I am, which is _USB312SAT3CB_ you might need to update the firmware.

This is the exact one: [StarTech.com USB 3.1 to 2.5" SATA Hard Drive Adapter ](https://www.amazon.com/StarTech-com-SATA-USB-Cable-USB3S2SAT3CB/dp/B00XLAZODE/)

![image](https://m.media-amazon.com/images/I/61lsiuFNDvL._SL1500_.jpg)

You can find firmware on this [page](https://www.startech.com/en-us/hdd/usb312sat3cb).

The firmware update notes:

```text
This update was to add trim support to the adapter when connected to SSD Drives.

Connect a drive to the adapter before running the firmware update.

```

You can run the Windows executable while a drive is connected and proceed. 
*(I'm not sure about updating the firmware from a linux machine.)*

Be wary of other small stuff like this. Not all SATA to USB adapters work well. Mainly, you want to look for adapters that use the ASM1153E chipset. To make the most of it, make sure it has UASP and Trim support. Do research for your own adapter.

Last thing is that I noticed the SATA side of the adapter runs a bit toasty. Probably unimportant, but I did mount a spare heatsink from the case I bought on top of it. 

