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
          * [File Browser](stack/current/filebrowser.yml)
          * [JellyFin](stack/current/jellyfin.yml)
          * [Aria2 Pro](stack/current/aria2-pro.yml)
          * [qBittorrent](stack/current/qbittorrent.yml)
          * [Pi-hole](stack/current/pi-hole-vanilla.yml)
          * [Gitea](stack/current/gitea.yml)
          * [Stash](stack/current/stash.yml)
          * [Dozzle](stack/current/dozzle.yml)
          * [Scrutiny](stack/current/scrutiny.yml)
          * [Duplicacy](stack/current/duplicacy.yml)
          * [Watchtower](stack/current/watchtower.yml)
          * [QDirStat](stack/current/qdirstat.yml)
          * [Doku](stack/current/doku.yml)
          * [Netdata](stack/current/netdata.yml) <!-- Needs work -->
          * [Samba](stack/current/samba.yml) <!-- Needs work -->
        * ❌ Retired Services 
          * [Jellyseerr](stack/retired/jellyseerr.yml) <!-- Want alternative -->
          * [IT-Tools](stack/retired/it-tools.yml) <!-- Don't find myself using it -->
          * [Tube Archivist](stack/retired/tube-archivist.yml) <!-- RAM intensive, Want alternative -->
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
## Deployment
![hardware](/docs/assets/hardware.jpg)
I have deployed this same setup on Bullseye for around 9 months. With no noticeable issues with a Kingston drive, on the Pi 4. I am not an expert, use this reference at your own risk. I don't always show or follow best practices. Some information may be out of date. I have updated this reference lightly for Bookworm and have not yet tested that long term. I'm now running Bookworm with a 4TB Samsung drive. This repository is mainly for me but can be useful for others.

## 🌴Tree Map

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
        │       └── 📁 anime
        ├── 📁 jellyseerr
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
