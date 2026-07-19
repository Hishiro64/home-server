# **🛖 Home Server**
[![OS](https://img.shields.io/badge/OS-Raspberry_Pi_OS_(Bookworm)-C51A4A?logo=raspberry-pi&logoColor=white&style=flat-square)](https://www.raspberrypi.com/software/)
[![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_4_(8GB)-A22846?logo=arm&logoColor=white&style=flat-square)](docs/HARDWARE/Parts%20List.md)
[![Management](https://img.shields.io/badge/Managed_by-Portainer-13BEF9?logo=portainer&logoColor=white&style=flat-square)](docs/3_Portainer%20Setup.md)
[![Docker](https://img.shields.io/badge/Docker_Compose-30_Services-2496ED?logo=docker&logoColor=white&style=flat-square)](./stack/)
[![Uptime](https://img.shields.io/badge/Last_Uptime-1_Year,_8_Days-success?style=flat-square&logo=uptimekuma&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square&logo=opensourceinitiative&logoColor=white)](./LICENSE)

![preview](docs/assets/homer-preview.png)
Contains my config files, docker compose files, and documentation for setting up my home server. All hosted on one single Raspberry Pi and one 4TB SSD!
<!--<img src="docs/assets/uptime-2024-11-12%2011-28-24.png" width="400" /> -->
## 📃 Index
<!--ts-->
   * 📔 Docs 
      * 🍓 [Preparing Raspberry Pi OS (Bookworm)](docs/1_Raspberry%20Pi%20OS%20Image%20Configuration.md) 
        * [SATA SSD Setup](docs/SSD/SATA%20SSD%20Setup.md)
      * ⚙️ [OS Configuration](docs/2_OS%20Configuration.md)
          * [Locale](docs/2_OS%20Configuration.md#locale)
          * [Time Zone](docs/2_OS%20Configuration.md#time-zone)
          * [Update/Upgrade](docs/2_OS%20Configuration.md#updateupgrade)
          * [EEPROM](docs/2_OS%20Configuration.md#eeprom)
          * [Password](docs/2_OS%20Configuration.md#password)
          * [Sudo](docs/2_OS%20Configuration.md#sudo)
          * [config.txt](docs/2_OS%20Configuration.md#configtxt)
          * [cmdline.txt](docs/2_OS%20Configuration.md#cmdlinetxt)
          * [nmtui](docs/2_OS%20Configuration.md#nmtui)
          * [Processes (Minimizing idle load)](docs/2_OS%20Configuration.md#processes)
          * [Generating SSH Keys](docs/2_OS%20Configuration.md#generating-ssh-keys)
          * [sshd_config (Hardening)](docs/2_OS%20Configuration.md#sshd_config)
          * [Issue banner](docs/2_OS%20Configuration.md#issue-banner)
          * [cpufreq (Changing governor)](docs/2_OS%20Configuration.md#cpufreq)
      * 🐳 [Portainer Setup](docs/3_Portainer%20Setup.md)
        * 📚 [**Stacks (Compose Files)**](stack/) 🌟 <!-- Docker Compose Files -->
      * 🗒️ [Config Files](root)
      * 🔧 [Maintenance](docs/4_Maintenance.md)
      * 🚘 [Hardware](docs/HARDWARE/)
        * 🔨 [Parts List](docs/HARDWARE/Parts%20List.md)
        * 💾 [SSD Notes](docs/SSD/)
          * [Storage Considerations](docs/SSD/Storage%20Considerations.md)
          * [Storage Plan](docs/SSD/Storage%20Plan.md)
          * [SATA SSD Setup (Above 2TB)](docs/SSD/SATA%20SSD%20Setup.md)
          * [SATA Adapter Nonsense](docs/SSD/SATA%20Adapter%20Nonsense.md) 
               
<!--te-->
## 🪂 Deployment
![hardware](/docs/assets/hardware.jpg)
I'm currently running with Bookworm on a Pi 4 for the last 2.5 years with a 4TB Samsung drive. I have deployed this same setup on Bullseye for around 9 months, no noticeable issues with a 1TB Kingston drive, also running on the Pi 4. The larger Samsung drive requires some [initial setup](docs/SSD/SATA%20SSD%20Setup.md) to get it fully up and running, documented in this repository. Nevertheless, I am not an expert, use this entire reference at your own risk. I don't always show or follow best practices. Some information may be out of date. I have updated this reference lightly for initial setup with Bookworm. This repository is mainly for me, but you may find it useful.

## 🌴 Tree Map

```ruby
📁 /srv/stacks
├── 📁 aria2-pro
│   ├── 📁 config
│   └── 📁 downloads
├── 📁 bytestash
│   └── 📁 snippets
├── 📁 calibre-web-automated
│   ├── 📁 calibre-library
│   ├── 📁 config
│   └── 📁 cwa-book-ingest
├── 📁 dufs
│   └── 📁 homer:ro
├── 📁 file-browser
│   ├── 📁 branding
│   └── 📁 filebrowser.db
├── 📁 flatnotes
│   └── 📁 data
├── 📁 gitea
│   └── 📁 data
├── 📁 homer
├── 📁 hoodik
│   └── 📁 data
├── 📁 immich
│   ├── 📁 library
│   └── 📁 postgres
├── 📁 jellyfin
│   ├── 📁 config
│   └── 📁 media
│       ├── 📁 anime:ro
│       ├── 📁 movies:ro
│       ├── 📁 music:ro
│       ├── 📁 restricted:ro
│       └── 📁 shows:ro
├── 📁 kiwix-serve
│   └── 📁 zim
├── 📁 lanraragi
│   └── 📁 content
├── 📁 linkding
├── 📁 mailpit
│   └── 📁 data
├── 📁 netdata
│   └── 📁 netdataconfig
├── 📁 opengist
├── 📁 qbittorrent
│   ├── 📁 config
│   └── 📁 downloads
├── 📁 samba
│   ├── 📁 data
│   └── 📁 Serva:ro
├── 📁 scrutiny
│   └── 📁 config
├── 📁 seerr
├── 📁 stash
│   ├── 📁 blobs
│   ├── 📁 cache
│   ├── 📁 config
│   ├── 📁 data:ro
│   ├── 📁 generated
│   └── 📁 metadata
└── 📁 syncthing
```
