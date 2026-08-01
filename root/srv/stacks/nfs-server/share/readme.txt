--- How to Access ---

"share" is a read-only nfs4 network share.
---
Credentials: None
---

[From Web Browser] (HTTP)
1. In address bar: http://192.168.1.200:5003/

[In Fedora] (NFS4/Mount)
1. Navigate to the location you want to mount the share.
2. In the terminal run `mkdir ./share` then `sudo mount -t nfs4 192.168.1.200:/ ./share`

[In Fedora] (NFS4/Nautilus)

1. Not yet supported :(
