"""Communication: email (env-var creds) and WhatsApp messages."""

import smtplib
import time
import webbrowser

from olivia.core import config

# Voice-addressable contacts. Numbers are placeholders; edit for real use.
CONTACTS = {
    "chirag": "+91 9999999999",
    "india": "+91 9999999998",
    "abhinav": "+91 9999999997",
    "ram": "+91 1234567891",
    "None": "+91 7428449707",
}


def send_email(to, content):
    """Send a plain-text email via Gmail SMTP using env-var credentials."""
    if not config.OLIVIA_EMAIL or not config.OLIVIA_EMAIL_PASSWORD:
        raise RuntimeError("Set OLIVIA_EMAIL and OLIVIA_EMAIL_PASSWORD")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(config.OLIVIA_EMAIL, config.OLIVIA_EMAIL_PASSWORD)
    server.sendmail(config.OLIVIA_EMAIL, to, content)
    server.close()


def send_whatsapp(to, content):
    """Open WhatsApp Web to a number and send the message."""
    import pyautogui

    webbrowser.open(f"https://web.whatsapp.com/send?phone={to}&text={content}")
    time.sleep(20)
    pyautogui.press("enter")
