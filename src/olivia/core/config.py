"""Env-var configuration for Olivia. No secrets in source."""

import os


def _get(name, default=None):
    return os.environ.get(name, default)


# Email (WhatsApp/email skills). Never hardcode credentials.
OLIVIA_EMAIL = _get("OLIVIA_EMAIL")
OLIVIA_EMAIL_PASSWORD = _get("OLIVIA_EMAIL_PASSWORD")

# API keys
OPENWEATHER_API_KEY = _get("OPENWEATHER_API_KEY")
NEWS_API_KEY = _get("NEWS_API_KEY")

# Voice index for the SAPI5 engine (0 = male, 1 = female on most Windows setups).
VOICE_INDEX = int(_get("OLIVIA_VOICE_INDEX", "1"))

# Where screenshots and notes are written.
SCREENSHOT_DIR = _get("OLIVIA_SCREENSHOT_DIR", r"C:\Olivia\screenshot")
NOTES_FILE = _get("OLIVIA_NOTES_FILE", "notes.txt")
