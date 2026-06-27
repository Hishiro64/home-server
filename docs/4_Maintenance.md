[<- index](/README.md)
# Maintenance
Some stuff I do to keep the system running nicely.

## Journalctl
The size of the Journal can get pretty large. You can check by running the following:
```bash
journalctl --disk-usage
```
You can reduce the size by running this:
```bash
sudo journalctl --vacuum-size=500M
```
## Docker 
You can free up space by deleting unused images.
```bash
docker image prune
```
