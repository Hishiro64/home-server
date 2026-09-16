# 💌 Email Services with Mailpit

A simple catch-all SMTP server, used with services to be able to deliver mail. All captured mail is pooled into a single inbox. **Using POP3 will only retrieve the last 100 entries and delete them from the server as well**.

## SMTP Configuration

```yml
SMTP_ADDRESS: 192.168.1.200
SMTP_PORT: 1025
SMTP_AUTH_ACCEPT_ANY: true # Auth any pair
SMTP_USERNAME: <any> # Becomes tag in web UI
SMTP_PASSWORD: <any>
POP3_PORT: 1010
POP3_AUTH: admin:changeme # user:passwd
```
No strict verification is done, thus a set of loose guidelines are recommended, alongside a maintained address book for reference.

This is nice because it avoids an interdependent mail system. Which would otherwise be dependent on a configured DNS, domain name, certificates, recipient SMTP server(s), reverse proxy, etc... While this system is in place, we can put these on the back burner and create functional service accounts.

## Filtering Recipients

Since no relaying is done by default, reading mail sent to a particular destination has to be filtered by searching for it inside of Mailpit's web UI. This does require you to know the recipient mailing address. For viewing unknown recipients use the search query with all known recipients, example:

`to: !user1 to: !user2` -> leaves only unknown recipients.

---

If you are using Thunderbird with POP3, you can create search folders for each recipient:

 1. Open the Search Messages window: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>

 2. Create the search query: **Match all the following -> To -> contain -> \<user\> -> Search**

 3. Save as search folder. Give it the Display Name of the recipient.
 
 4. Repeat for each recipient.

You can also use this window to create a search folder for unknown recipients. That should be self-explanatory.

## Mailpit Tags

In Mailpit's web UI, mail can be filtered using tags. Tags only show in the web UI and are assigned to messages through several means.

1. The `SMTP_USERNAME` becomes the tag, used by the service account to log in and send messages.

2. Match cases defined in `tags.yaml` (complex cases)

3. Plus addressing in either the `From` or `To` header get generated into Mailpit tags.

Don't become heavily dependent on these tags as they are exclusive to Mailpit. Use plus addressing in the user account's mailing address instead, that is preferred, and can be translated outside of Mailpit.

## Email Guidelines
Since this SMTP server is not dependent on anything else, we root our conventions on written guidelines that can be loosely followed rather than aligning with existing foundations such as registered domains and subdomains. 

## Service Accounts
Service Accounts should:
   1. Use the mailing address `<type>@noreply.<container_name>.server.home.arpa`
   2. Should have their `SMTP_USERNAME` set as `container_name` from stack, with the first letter capitalized.

   Note: `<type>` is user-defined and default of `service` is used.  

## User Accounts
User Accounts should:
   1. Use the mailing address `<name>@server.home.arpa` (no tag by default)

User Accounts can:
   1. Use chained plus addressing `<name>+<type>+...+<type>@server.home.arpa` (recommended)
      - `<type>` can derive from the service account mailing address.
   2. Use `<name>` from `tags.yaml` to be assigned tags in Mailpit. For Example:

         ```yaml
         filters:
            - match: to:user1 # user1@server.home.arpa
              tags: First-User
         ```

# Temporary Email Records

These are in use for the time being and may not follow guidelines:

| Container | Display Name + Primary Email |
| :--- | :--- |
| **Hoodik** | `Hoodik <service@noreply.hoodik.server.home.arpa>` | `Hoodik` |
| **Wud** | `Docker <notification@noreply.wud.server.home.arpa>` | `Wud` |
| **Immich** | `Immich <service@noreply.immich.server.home.arpa>` | `Immich` |
| **Seerr** | `Seerr <notification@noreply.seerr.server.home.arpa>` | `Seerr` |
| **Gitea** | `Tea <service@noreply.gitea.server.home.arpa>` | `Gitea` |
| **Scrutiny** | `Alert <alert@noreply.scrutiny.server.home.arpa>` | None |
| **Calibre-web-automated** | `Your eBook <ebook@noreply.calibre-web-automated.server.home.arpa>` | `Calibre-web-automated` |
| **Audiobookshelf** | `Your eBook <ebook@noreply.audiobookshelf.server.home.arpa>` | `Audiobookshelf` |

# Service Account Address Book
Import the following entries to your Thunderbird address book:

| Display Name | Primary Email |
| :--- | :--- |
| **Hoodik** |  <service@noreply.hoodik.server.home.arpa> |
| **Docker** |  <notification@noreply.wud.server.home.arpa> | 
| **Immich** |  <service@noreply.immich.server.home.arpa> | 
| **Seerr** |  <notification@noreply.seerr.server.home.arpa> | 
| **Tea** |  <service@noreply.gitea.server.home.arpa> |
| **Alert** | <alert@noreply.scrutiny.server.home.arpa> |
| **Alert** |  <alert@noreply.beszel.server.home.arpa> |
| **Your eBook** | <ebook@noreply.calibre-web-automated.server.home.arpa> |
| **Your eBook** | <ebook@noreply.audiobookshelf.server.home.arpa> |

# Send to Kindle

Mail addressed outside our domain has to be relayed. A good example of this would be the *Send to Kindle* option. It has to be delivered to `@kindle.com`. Rather than relaying the message from Mailpit to `smtp.gmail.com` to do the transfer, we can just use it directly instead. Both Amazon and Google will scan your EPUB files anyways.

## SMTP Configuration (Gmail) 
If you use Gmail to log in to Amazon, just use that email for using Google's SMTP server.
```yml
SMTP_ADDRESS: smtp.gmail.com
SMTP_PORT: 587
SMTP_TLS: true
SMTP_USERNAME: <your_gmail_user>@gmail.com # Full address
SMTP_PASSWORD: <app_password> # Manage your Google Account -> Search -> "App passwords"
```
## Service Account Overrides
| X-Google-Original-From | From |
| :--- | :--- |
| `Your eBook <ebook@noreply.calibre-web-automated.server.home.arpa>` | `Your eBook <your_gmail_user@gmail.com>` |
| `Your eBook <ebook@noreply.audiobookshelf.server.home.arpa>` | `Your eBook <your_gmail_user@gmail.com>` |

## Ereader Address Book
To find this address look for "Send to Kindle" in your Kindle's settings menu. Append as a new Ereader Device.
| Display Name | Primary Email |
| :--- | :--- |
| **Kindle** | <your_amz_username_randomstring@kindle.com> |