[<- index](/README.md)
# Parts List

* ### Required
    * [Raspberry Pi 4 Model B (8gb)](https://www.amazon.com/LANDZO-Raspberry-Pi-Model-8gb/dp/B08R87H4RR)
       * [CanaKit 3.5A Raspberry Pi 4 Power Supply (USB-C)](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-USB-C/dp/B07TYQRXTK/)

    OR

    * ❗ Raspberry Pi 5 8GB (Untested, **read note**)
       * ❗ Raspberry Pi 5 compatible power supply (Untested)

* ### Storage
    I would recommend using a SATA drive. See [here](/docs/SSD/Storage%20Considerations.md) for a small rundown of drive types. Before scaling, [plan it out](/docs/SSD/Storage%20Plan.md), and read [this](/docs/SSD/SATA%20SSD%20Setup.md) for previewing how a SATA SSD would be setup. Please arrange to your setup. Here are my recommendations.
    * [Kingston 960GB A400 SATA3 2.5" Internal SSD SA400S37/960G](https://www.amazon.com/Kingston-240GB-Solid-SA400S37-240G/dp/B079XC5PVV/) (9 months with no issues on Bullseye, with no external power)
    * [SAMSUNG 870 EVO 4TB 2.5 Inch SATA III Internal SSD (MZ-77E4T0B/AM)](https://www.amazon.com/SAMSUNG-Inch-Internal-MZ-77E4T0B-AM/dp/B08QBL36GF/) (4 months in, currently using on Bookworm, no issues, with no external power)
        * [StarTech.com USB 3.1 to 2.5" SATA Hard Drive Adapter ](https://www.amazon.com/StarTech-com-SATA-USB-Cable-USB3S2SAT3CB/dp/B00XLAZODE/) 
    * [SanDisk 128GB Extreme microSDXC UHS-I Memory Card with Adapter](https://www.amazon.com/SanDisk-Extreme-microSDXC-Memory-Adapter/dp/B09X7BK27V/)
* ### Recommended
    Patch cables will always be faster than Wi-Fi.

    * [Monoprice 124352 Cat6A Ethernet Patch Cable](https://www.amazon.com/Monoprice-Cat6A-Ethernet-Patch-Cable/dp/B077H4SXHB/)
    
    The Pi always thermal throttles without any cooling.
    * [SunFounder Raspberry Pi Cooling Fan, Raspberry Pi Ice Tower Cooler](https://www.amazon.com/SunFounder-Raspberry-Cooling-Heatsink-Radiator/dp/B09QPBT4GL/)
        * ❗ I had one of the included fans, fail on me after around 8 months. I expect the 2nd one it came with to also fail as well. These small fans are cheap, and it might be better off it just get a reliable one in the first place.
        * ❗ [Noctua NF-A4x10 5V](https://www.amazon.com/Noctua-Cooling-Bearing-NF-A4X10-FLX-5V/dp/B00NEMGCIA/) (Untested)

    This case can house all the combinations in this hardware section.    
    * [ElectroCookie Raspberry Pi 4 Case](https://www.amazon.com/ElectroCookie-Raspberry-Aluminum-Cooling-Changing/dp/B09QG349ZL/)

    Always recommended to maximize uptime on your pi server during power outages. It's important to minimize the issues from brownouts. A small one will do, as the pi doesn't do use much power. 
    * [APC UPS Battery Backup and Surge Protector, 600VA](https://www.amazon.com/APC-Battery-Protector-Back-UPS-BE600M1/dp/B01FWAZEIU/)
* ### Optional 
    The server will be running headless, but in the case where you get locked out of SSH or need to debug without a network connection, it will be a lifesaver.
    * [Amazon Basics Flexible and Durable Micro HDMI Cable (18Gpbs, 4K/60Hz) - 6 Feet, Black](https://www.amazon.com/Amazon-Basics-Flexible-Durable-18Gpbs/dp/B07KSDB25X/)

    You should probably just use tape. 
     * [VELCRO Brand ONE-WRAP Cable Ties](https://www.amazon.com/VELCRO-Brand-Cable-Ties-100Pk/dp/B001E1Y5O6/)

    The SATA connection on the adapter I use, does get a bit toasty. Unnecessary, but did put a heatsink on it anyway. If you're using the same case as I am, you can use the black heatsink it comes with for the adapter. Any would do. 
    * [Raspberry Pi 4b Heatsink](https://www.amazon.com/Raspberry-Heatsink-Aluminum-Conductive-Adhesive/dp/B07ZLZRDXZ/)

# Note about the Raspberry Pi 5
My current build is made and deployed on the Raspberry Pi 4. I am planning to wait while for the Raspberry Pi 5 to mature before migrating over. If you're lucky and already bought a Raspberry Pi 5, and want to use a similar build, know that some of these parts are not compatible, like the case, and cooler. Other parts may be redundant, like the SATA to USB adapter as there is native PCIe on the newer model. It's likely that 3rd parties will soon make a SATA to FPC adapter, made for the Pi. It could be faster and open up other possibilities. Once the Raspberry Pi 5 matures, people will find a far more superior way to set it up as a home server, that takes full advantage of the software and hardware, among other benefits from waiting it out.

# Final note about the Raspberry Pi 5
I have decided that my home server won't be running on the Raspberry Pi 5 or any Pi platform in the future. The platform is great to start out on, but it won't scale or provide for my needs. I’m going to keep milking what I can from my Pi 4 and switch over to an x86 server in the future.
