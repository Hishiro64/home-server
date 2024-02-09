# **🏚 Home Server**
Contains my config files, docker compose files, and documentation for setting up my home server. All hosted on one single Raspberry Pi and one 4TB SSD!

![preview](docs/assets/homer-preview.png)
## 📃 Index 
<!--ts-->
   * 📔 Docs 
      * [Preparing Raspberry Pi OS (Bookworm)](docs/1_Raspberry%20Pi%20OS%20Image%20Configuration.md) 🐛
        * [SATA SSD Setup](docs/SSD/SATA%20SSD%20Setup.md)
      * [OS Configuration](docs/2_OS%20Configuration.md)
      * [Portainer Setup](docs/3_Portainer%20Setup.md)
        * 📚 Stacks  
          * [Homer](stack/current/homer.yml)
          * [File Browser](stack/current/filebrowser.yml) <!-- Could be better -->
          * [JellyFin](stack/current/jellyfin.yml)
          * [Aria2 Pro](stack/current/aria2-pro.yml)
          * [Scrutiny](stack/current/scrutiny.yml)
          * [Netdata](stack/current/netdata.yml) <!-- Needs some work -->
          * [Dozzle](stack/current/dozzle.yml)
          * [WireGuard-Easy](stack/current/wg-easy.yml)
          * [qBittorrent](stack/current/qbittorrent.yml)
          * [Pi-hole](stack/current/pi-hole-vanilla.yml)
          * [Gitea](stack/current/gitea.yml)
          * [Stash](stack/current/stash.yml)
          * [Duplicacy](stack/current/duplicacy.yml)
          * [Syncthing](stack/current/syncthing.yml)
          * [QDirStat](stack/current/qdirstat.yml)
          * [Kavita](stack/current/kavita.yml)
          * [Doku](stack/current/doku.yml)
          * [Jellyseerr](stack/current/jellyseerr.yml) <!-- Want alternative -->
          * [Samba](stack/current/samba.yml) <!-- Needs work -->
        * ❌ Retired Services 
          * [IT-Tools](stack/retired/it-tools.yml) <!-- Don't find myself using it -->
          * [Tube Archivist](stack/retired/tube-archivist.yml) <!-- RAM intensive, Want alternative -->
          * [Watchtower](stack/current/watchtower.yml) <!-- I update manually now for reliability now -->
          * [Pi.Alert](stack/retired/pi.alert.yml) <!-- Want alternative -->
          * [Dashdot](stack/retired/dashdot.yml) <!-- CPU intensive -->
      * [Config Files](root)
      * 🚘Hardware
        * [Parts List](docs/HARDWARE/Parts%20List.md)
        * 🗒 SSD Notes
          * [Storage Considerations](docs/SSD/Storage%20Considerations.md)
              * [Storage Plan](docs/SSD/Storage%20Plan.md)
          * [SATA Adapter Nonsense](docs/SSD/SATA%20Adapter%20Nonsense.md)      
<!--te-->
## 🪂 Deployment
![hardware](/docs/assets/hardware.jpg)
I have deployed this same setup on Bullseye for around 9 months. No noticeable issues with a 1TB Kingston drive, running on the Pi 4. Nevertheless, I am not an expert, use this reference at your own risk. I don't always show or follow best practices. Some information may be out of date. I have updated this reference lightly for Bookworm and have not yet finished testing long term. I'm currently running Bookworm with a 4TB Samsung drive. This repository is mainly for me but you may find it useful.

## 🌴 Tree Map

```text
📁 /srv
    └── 📁 stacks
        ├── 📁 portainer
        ├── 📁 homer
        ├── 📁 file-browser
        │   └── 📁 branding
        ├── 📁 jellyfin
        │   ├── 📁 config
        │   └── 📁 media
        │       ├── 📁 movies
        │       ├── 📁 shows
        │       ├── 📁 anime
        │       └── 📁 restricted
        ├── 📁 kavita
        │   ├── 📁 config
        │   └── 📁 data
        │       ├── 📁 books
        │       └── 📁 light-novels
        ├── 📁 jellyseerr
        ├── 📁 wg-easy
        ├── 📁 syncthing
        ├── 📁 aria2-pro
        │   ├── 📁 config
        │   └── 📁 downloads
        ├── 📁 qbittorrent
        │   ├── 📁 config
        │   └── 📁 downloads
        ├── 📁 pi-hole
        │   ├── 📁 etc_pihole
        │   └── 📁 etc_dnsmasq
        ├── 📁 pi.alert
        │   └── 📁 config
        ├── 📁 gitea
        │   └── 📁 data
        │   └── 📁 lfs
        ├── 📁 stash
        │   ├── 📁 config
        │   │   └── 📁 scrapers
        │   ├── 📁 data
        │   ├── 📁 metadata
        │   ├── 📁 cache
        │   ├── 📁 blobs
        │   └── 📁 generated
        ├── 📁 netdata
        │   └── 📁 netdataconfig
        ├── 📁 samba
        │   ├── 📁 data
        │   └── 📁 Serva
        ├── 📁 scrutiny
        │   └── 📁 config
        └── 📁 duplicacy
            ├── 📁 config
            ├── 📁 backup
            └── 📁 restore
```
