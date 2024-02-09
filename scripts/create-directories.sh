#!/bin/bash

#################
# RUN WITH SUDO #
#################

cd /

mkdir -p /srv/stacks

cd /srv/stacks

mkdir -p {portainer,homer,wg-easy,file-browser/branding,jellyfin/{config,media/{movies,shows,anime,restricted}},kavita/{config,data/{Light Novels,Books}},jellyseerr,syncthing,aria2-pro/{config,downloads},qbittorrent/{config,downloads},pi-hole/{etc_pihole,etc_dnsmasq},pi.alert/config,gitea/data,stash/{config/scrapers,data,metadata,cache,blobs,generated},netdata/netdataconfig,samba/{data,Serva},scrutiny/config,duplicacy/{config,backup,restore},qdirstat/config}

# File Browser
cd ./file-browser

touch database.db

cd ./branding

#touch ./custom.css #wget

# Own every file
chown 1000:1000 -R /srv
