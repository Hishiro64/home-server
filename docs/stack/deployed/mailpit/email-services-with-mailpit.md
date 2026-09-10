# 💌 Email Services with Mailpit

A simple catch-all SMTP server, used with services to be able to deliver mail. All mail captured will be pooled into a single inbox. **Using POP3 will only retrieve the last 100 entries and delete them from the server as well**.

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

## Filtering Inbox 

Since no relaying is done by default, mail destinations can be filtered by search from the `To` header.

In Mailpit's web UI, mail can be filtered using tags. Tags only show in the web UI and are assigned to messages through several means.

1. The `SMTP_USERNAME` used to send the message becomes the tag. 

2. Match cases defined in `tags.yaml` (special cases)

3. Plus addressing in either the `From` or `To` header. (public)

From address conventions are not required but recommended, an example being:

`service@noreply.{service-name}.server.home.arpa`

# Guidelines
## Scope
1. From only 2 base rules defined in `tags.yaml`:
   - Emails that start with `mailpit+...` tagged as `All`
   - Emails that start with `admin+...` tagged as `Me`
2. Not from rules:
   - Emails that start with `any+...` Will not be tagged
3. Extra rules will be handled automatically by `tags.yaml`.

## Service Identification
1. Services that send emails should have their SMTP Username set as `container_name` from stack, with the first letter capitalized.
2. If the above is not possible use plus addressing instead: `{scope}+{container_name}+...`
3. You can set both.

## Optional  
- Chain plus addressing to add 1 or more attributes: `{scope}+{container_name}+{attribute1}+{attribute2}+...`

## Ending

- Emails should end in `...@server.home.arpa` to be valid unless it is a noreply address.

## Final email address should have the form of
`{scope}+{container_name}+{attribute1}+{attribute2}+...+{attributeN}@server.home.arpa`

# Email Records

Reserved email addresses:

| Service / Container | Final Email Address | SMTP User | SMTP Auth? | Generated Tags (Base rules) |
| :--- | :--- | :--- | :--- | :--- |
| **Hoodik** | `admin@server.home.arpa` | `Hoodik` | Yes | `Hoodik`, `Me` |
| **Wud** | `admin+notification@server.home.arpa` | `Wud` | Yes | `Me`, `Notification`, `Wud` |
| **Immich** | `admin+immich@server.home.arpa` | `Immich` | Yes | `Me`, `Immich` |
| **Seerr** | `seerr@server.home.arpa` | `Seerr` | Yes | `Me`, `Seerr` |
| **Beszel** | `admin+alerts+beszel@server.home.arpa` | `None` | No | `Me`, `Beszel`, `Alerts` |
| **Gitea** | `gitea@server.home.arpa` | `Gitea` | Yes | `Gitea` |
| **Gitea (auto-generated)** | `1+hishiro@users.noreply.gitea.server.home.arpa` | `Gitea` | Yes | `Gitea`, `Hishiro` |