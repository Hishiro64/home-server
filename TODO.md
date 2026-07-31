# TODO
### Done
* [x] SMTP
* [x] Encrypted Folder
* [x] File Sharing
* [x] Look into container update notifications
* [x] Set this up https://opengist.io/
* [x] Look into Papra
* [x] Look into Flatnotes
* [x] Standardize Email format and record it on a doc
* [x] Add maintenance.md for `docker image prune -a` and `sudo journalctl --vacuum-size=500M`
* [x] Local livestream for homer
* [x] Look into Linkding (bookmarks)
* [x] Look into selfhosting TOTP
* [x] Make homer balanced again
* [x] Look into Beszel (Not a viable replacement for Netdata)
---
### Backup
* [ ] Add a minimal backup Solution for small important files.
* [ ] Evaluate cheap backup: Encrypted Gdrive, BuddyBackup, Pi-Zero with USB storage.
  * [ ] Look into Rclone
  * [ ] Look into Restic
### Services
* [ ] Replace Netdata
  * [ ] Find and deploy a new viable primary monitoring service
  * [ ] Move Netdata to be used as a secondary
* [ ] Integrate this: https://github.com/Tecnativa/docker-socket-proxy
* [ ] Look into Paperless-ngx
* [ ] Look into Archivebox
* [ ] Look into Audiobookshelf
* [ ] Look into a music requests container
* [ ] Service for Public ip change notifications
* [ ] NFS container
* [ ] Container that restarts LanguageTool every 24hrs
* [ ] Guest homepage 
### DNS
* [ ] Look into DNS nonsense (Recursive DNS and DoT/DoH), Technitium DNS, Pi-hole
  * [ ] Look into setting a *.home.arpa hostname
### Misc
* [ ] Completely redo `/stack/README.md`
  * [ ] Add benchmarks and results
* [ ] Self Generating Changelog (git-clif)
* [ ] Update `/scripts/tree.py` to be more descriptive: ports, volumes, etc...
---
### Docs
* [ ]  Move entire documentation to a dedicated docs project site using Vitepress 
### Event: Immich stack update created memory starvation scenario (7/30/2026)
* [ ] Document soft recovery solutions properly in case the a memory starvation event experienced today occurs again.
  * [ ] Under high load or memory starvation, authentication may need to take longer, and exceed the `LoginGraceTime` inside `/etc/ssh/sshd_config`, closing the connection before login. You can raise the interval or if you're already in this situation, you can attempt brute force: `while ! ssh -p 5522 admin@192.168.1.200; do sleep 2; done`. The interval was shorted at the beginning for hardening purposes, clearly needs to be updated since the trade-off is poor. Brute force may not work at all and require manual login. `LoginGraceTime` should be raised.
  * [ ] If docker commands becomes unresponsive due to memory starvation and are unable to kill high memory containers, you can use `top` to find the PID of a container, then use: `sudo kill -9 <PID>`, making it possible to reclaim memory.
  * [ ] Swap was disabled for performance reasons, but enabling it leniently could have avoided manual intervention.
