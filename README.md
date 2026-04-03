# **🛖 Home Server**
Contains my config files, docker compose files, and documentation for setting up my home server. All hosted on one single Raspberry Pi and one 4TB SSD!

![preview](docs/assets/homer-preview.png)
<img src="docs/assets/uptime-2024-11-12%2011-28-24.png" width="400" />
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
          * [Netdata](stack/current/netdata.yml) <!-- Will force a cloud requirement! -->
          * [Dozzle](stack/current/dozzle.yml)
          * [WireGuard-Easy](stack/current/wg-easy.yml)
          * [qBittorrent](stack/current/qbittorrent.yml)
          * [Pi-hole](stack/current/pi-hole-vanilla.yml)
          * [Gitea](stack/current/gitea.yml)
          * [Stash](stack/current/stash.yml)
          * [Duplicacy](stack/current/duplicacy.yml)
          * [LanguageTool](stack/current/languagetool.yml) <!-- Version 8.13.2 of the Firefox add-on -->
          * [Syncthing](stack/current/syncthing.yml)
          * [QDirStat](stack/current/qdirstat.yml)
          * [Doku](stack/current/doku.yml)
          * [Jellyseerr](stack/current/jellyseerr.yml) <!-- Would perfer an alternative -->
          * [Samba](stack/current/samba.yml)
          * [LANraragi](stack/current/lanraragi.yml)
          * [Calibre Web Automated](stack/current/calibre-web-automated.yml)
          * [Memos](stack/current/memos.yml)
          * [Immich](stack/current/immich.yml)
          * [Kiwix-Serve](stack/current/kiwix-serve.yml)
          * [Snippet Box](stack/current/snippet-box.yml) <!-- Need alternative, unmaintained, CVE-2023-23277 -->
        * ❌ Retired Services 
          * [Kavita](stack/retired/kavita.yml)
          * [ByteStash](stack/retired/bytestash.yml) <!-- Kinda worse than snippet-box at the moment-->
          * [IT-Tools](stack/retired/it-tools.yml) <!-- Don't find myself using it -->
          * [Tube Archivist](stack/retired/tube-archivist.yml) <!-- RAM intensive, would like an alternative, otherwise use Stash -->
          * [Watchtower](stack/current/watchtower.yml) <!-- Update manually now for reliability now -->
          * [Pi.Alert](stack/retired/pi.alert.yml) <!-- Alternative fork available -->
          * [Dashdot](stack/retired/dashdot.yml) <!-- Quite CPU intensive -->
          * [Komga](stack/retired/komga.yml) <!-- Not much better than Kavita, everything other than *.cbz files is slow -->
      * [Config Files](root)
      * 🚘 Hardware
        * [Parts List](docs/HARDWARE/Parts%20List.md)
        * 🗒 SSD Notes
          * [Storage Considerations](docs/SSD/Storage%20Considerations.md)
              * [Storage Plan](docs/SSD/Storage%20Plan.md)
          * [SATA Adapter Nonsense](docs/SSD/SATA%20Adapter%20Nonsense.md)      
<!--te-->
## 🪂 Deployment
![hardware](/docs/assets/hardware.jpg)
I'm currently running with Bookworm on a Pi 4 for the last year with a 4TB Samsung drive. I have deployed this same setup on Bullseye for around 9 months, no noticeable issues with a 1TB Kingston drive, also running on the Pi 4. The Samsung drive requires some initial setup to get it fully up and running, documented in this repository. Nevertheless, I am not an expert, use this entire reference at your own risk. I don't always show or follow best practices. Some information may be out of date. I have updated this reference lightly for initial setup with Bookworm. This repository is mainly for me, but you may find it useful.

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
        ├── 📁 languagetool
        │   ├── 📁 ngrams
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
