#!/bin/bash

#################
# RUN WITH SUDO #
#################

cd /

mkdir -p /srv/stacks

cd /srv/stacks

mkdir -p {aria2-pro/{config,downloads},calibre-web-automated/{config,cwa-book-ingest,calibre-library},duplicacy/{config,backup,restore},file-browser/branding,gitea/data,homer,immich/{library,postgres},jellyfin/{config,media/{movies,shows,anime,music,restricted}},jellyseerr,kavita/{config,data/{light-novels,books}},kiwix-serve/zim,lanraragi/content,languagetool/ngrams,memos,netdata/netdataconfig,pi-hole/{etc_pihole,etc_dnsmasq},pi.alert/config,portainer,qbittorrent/{config,downloads},qdirstat/config,samba/{data,Serva},scrutiny/config,seerr,snippet-box/data,stash/{config/scrapers,data,metadata,cache,blobs,generated},syncthing,wg-easy}

# File Browser
cd ./file-browser

touch database.db

cd ./branding

#touch ./custom.css #wget

# Own every file
chown 1000:1000 -R /srv
