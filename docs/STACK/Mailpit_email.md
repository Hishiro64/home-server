# Guidelines
Used for forming email addresses 
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

- Emails should end in `...@server.home.arpa` to be valid.

## Final email address should have the form of
`{scope}+{container_name}+{attribute1}+{attribute2}+...+{attributeN}@server.home.arpa`

# Email Records

Reserved email addresses:

| Service / Container | Final Email Address | SMTP User | SMTP Auth? | Formed Tags  (Base rules) |
| :--- | :--- | :--- | :--- | :--- |
| **Hoodik** | `admin@server.home.arpa` | `Hoodik` | Yes | `Hoodik`, `Me` |
| **Wud** | `admin+notification@server.home.arpa` | `Wud` | Yes | `Me`, `Notification`, `Wud` |
| **Immich** | `admin+immich@server.home.arpa` | `Immich` | Yes | `Me`, `Immich` |
| **Seerr** | `seerr@server.home.arpa` | `Seerr` | Yes | `Me`, `Seerr` |
