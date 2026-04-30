--- How to Access ---

Serva is a read-only directory that is shared to the network.
---
Credentials:
user=admin
password=changeme
---

[From Web Browser] (HTTP)
1. In address bar: http://192.168.1.200:5001/

[In Windows] (SMB)

1. In Windows, open the File Explorer and right click on network.
2. Click "Map network drive"
3. Select a Drive letter and in the folder section, type in "\\server\Serva"
4. Check "Connect using different credentials" and click "Finish"
5. Fill out the credentials and click "Ok"

[In Fedora] (SMB)

1. In Fedora, open the Files (Nautilus) and click on network.
2. At the bottom, in server address, enter: smb://192.168.1.200/Serva/
3. Click "Connect"
5. Fill out the credentials and click "Ok"

[In Fedora] (WebDAV)
1. Same as SMB but in server address, enter: dav://192.168.1.200:5001/
2. No credentials
