# Send to Kindle

Mail addressed outside our domain has to be relayed. A good example of this would be the *Send to Kindle* option. It has to be delivered to `@kindle.com`. Mailpit can do this for us and the compose file is already setup to handle these domains. But rather than relaying the message from Mailpit to `smtp.gmail.com` to do the transfer, we can just use it directly instead. Both Amazon and Google will scan your EPUBs anyways. You should do this if this is the only service that uses SMTP.

## SMTP Configuration (Gmail) 
If you use Gmail to log in to Amazon, just use that email for using Google's SMTP server. If not, put your Gmail in the allow list from Personal Document Settings inside Amazon.

```yml
SMTP_ADDRESS: smtp.gmail.com
SMTP_PORT: 587
SMTP_TLS: true
SMTP_USERNAME: <your_gmail_user>@gmail.com # Full address
SMTP_PASSWORD: <app_password> # Manage your Google Account -> Search -> "App passwords"
SMTP_FROM: <your_gmail_user>@gmail.com # If not, it will be moved to `X-Google-Original-From`, renamed, labeled as spam to anyone else.
```

## Ereaders
To find this address look for "Send to Kindle" in your Kindle's settings menu. Append as a new Ereader Device. You can also add other peoples kindles so long as they have your Gmail in their allow list. If you do, you should send them an another copy to their personal email as well. 

| Display Name | Primary Email |
| :--- | :--- |
| **Main Kindle** | <your_amz_username_randomstring@kindle.com> |
| **Friend's Kindle** | <your_friend's_amz_username_randomstring@kindle.com> |
| **Friend's Email** | <your_your_friend's_email@provider.com> |

# Mailpit Relay
The original from addresses will be moved to `X-Original-From` and only use the Gmail address. This can get confusing when multiple services are using the same address.

## Service Account Overrides
| X-Original-From | From |
| :--- | :--- |
| `Your eBook <ebook@noreply.calibre-web-automated.server.home.arpa>` | `Your eBook <your_gmail_user@gmail.com>` |
| `Your eBook <ebook@noreply.audiobookshelf.server.home.arpa>` | `Your eBook <your_gmail_user@gmail.com>` |