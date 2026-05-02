import smtplib
from email.message import EmailMessage

# Helper script to test if Mailpit tags are working as intended.

# Mailpit configuration
MAILPIT_HOST = "192.168.1.200"
MAILPIT_PORT = 1025
DEFAULT_FROM = "test_mailpit@server.home.arpa"

# Send test email with params
def send_test_email(to_address, subject, body, username=None, password=None, from_address=DEFAULT_FROM):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    msg.set_content(body)

    try:
        # Connect to the Mailpit SMTP server
        with smtplib.SMTP(MAILPIT_HOST, MAILPIT_PORT) as server:
            if username and password:
                server.login(username, password)
            server.send_message(msg)
        print(f"Success: Email sent to {to_address}")
    except Exception as e:
        print(f"Error sending to {to_address}: {e}")

# Usage: python test_mailpit.py
def main():
    # 1. Tests untagged
    send_test_email(
        to_address="user@server.home.arpa",
        subject="1/6 Test Email | Tag: none",
        body="This email should be untagged."
    )

    # 2. Tests 'Me=to:admin' rule
    send_test_email(
        to_address="admin@server.home.arpa",
        subject="2/6 Test Email | Tag: Me",
        body="This email should be auto-tagged with 'Me'."
    )

    # 3. Tests plus-addressing
    send_test_email(
        to_address="user+test@server.home.arpa",
        subject="3/6 Test Email | Tag: Test",
        body="This email should be auto-tagged with 'Test' from plus addressing."
    )

    # 4. Tests username auto-tagging
    send_test_email(
        to_address="user@server.home.arpa",
        subject="4/6 Test Email | Tag: Python",
        body="This email should be auto-tagged from the username 'Python'.",
        username="Python",
        password="none"
    )

    # 5. Tests Me=to:admin' rule + username auto-tagging + plus-addressing
    send_test_email(
        to_address="admin+alerts@server.home.arpa",
        subject="5/6 Test Email | Tags: Alerts, Me, ServiceA",
        body="This email should be auto-tagged with 'Alerts', 'Me', 'ServiceA'.",
        username="ServiceA",
        password="none"
    )

    # 6. Tests 'All=to:mailpit' rule + multi-plus-addressing + username auto-tagging
    send_test_email(
        to_address="mailpit+channel+notification@server.home.arpa",
        subject="6/6 Test Email | Tags: All, Channel, Notification, ServiceB",
        body="This email should be auto-tagged with 'All', 'Channel', 'Notification', 'ServiceB'.",
        username="ServiceB",
        password="none"
    )

if __name__ == "__main__":
    main()