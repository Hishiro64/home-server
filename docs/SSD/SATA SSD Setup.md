[<- index](/README.md)
# GPT Partition Tables

Since the Raspberry Pi imager makes an MBR partition. The max size of a partition is limited to 2TB. This won't use the full capacity on a drive above 2TB in one neat partition. Using a community script, we can change this MBR partition into a GPT partition.

**Before**

![image.png](/docs/assets/ShareX_RsDKpx2PNH.png)

**After**

![image.png](/docs/assets/ShareX_6ObjNW9dYi.png)

**This is not an official method, but it does seem to work fine.**

1. After flashing the large Primary drive, redo [steps 1-6](/docs/1_Raspberry%20Pi%20OS%20Image%20Configuration.md) again, but on a separate micro-SD card.

2. Without the micro-SD card inserted, just plug in the Primary drive, and boot to the pi.

3. Wait a couple minutes for the initial setup to automatically complete on the Primary drive.

4. SSH into the pi with the credentials you set in the imager. On Windows it's `ssh {USERNAME}@{ASSIGNED-IP-FOR-PI}`. For my values it's `ssh admin@192.168.1.164`. Where my assigned ip `192.168.1.164` is automatically set by my router. This will be different; you need to use the address to your own pi.

5. Once you are SSH in, `sudo shutdown -h now`

6. Unplug in the Primary drive, insert micro-SD card, and Boot to the pi.

7. Wait again for that initial setup to automatically complete, now on the micro-SD card.

> [!CAUTION]
> 8. Read The first and last few posts [here](https://forums.raspberrypi.com/viewtopic.php?t=196778) on this thread. Bookworm is new and the Raspberry Pi 5 only just released. Things could change! **The very first post containing the instructions is actively maintained and should take precedence over the following instructions presented below.**

9. Once you are SSH in, plug in the large drive. It should be inserted in the bottom blue USB port.

10. Back on the [thread](https://forums.raspberrypi.com/viewtopic.php?t=196778) you will see the attachment named `usb-boot.zip`. Download and extract the contents.

11. Find the file called `mbr2gpt`. Open it up using Notepad. <kbd>CTRL+a</kbd> and <kbd>CTRL+c</kbd>. **Make sure everything is copied.**

12. In the SSH session, run `nano mbr2gpt`, paste, and save using <kbd>CTRL+X</kbd> <kbd>Y</kbd> <kbd>ENTER</kbd>.

13. Make the script executable by running `sudo chmod +x ./mbr2gpt`

14. Run `sudo ./mbr2gpt /dev/sda`.

15. Here are the settings I used. Set them according to your setup.

    ![image.png](/docs/assets/chrome_BYq8OSm1Vt.png)

16. Shutdown by using `sudo shutdown -h now`, remove the sd-card, and boot again.

 Once you SSH back in, all of the storage is now accessible, you can continue to enable Trim.

# Enable Trim
Enable Trim support, use [Jeff Geerling's guide](https://www.jeffgeerling.com/blog/2020/enabling-trim-on-external-ssd-on-raspberry-pi).

# Lower reserved space for root
You can get some remaining space by downsizing the ratio of reserved blocks for root. The default is 5%, but that scales up with drive size. You can lower it to 1-3%.
```bash    
    sudo tune2fs -m 3 /dev/sda2
```
![image.png](/docs/assets/WindowsTerminal_pubchefax4.png)

Now move on to [OS Configuration](/docs/2_OS%20Configuration.md).
