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

# --- Offline speech-to-text (local faster-whisper) ---
# Model size: tiny / base / small / medium / large-v3. Bigger = more accurate,
# slower, larger download. Model auto-downloads once, then runs fully offline.
WHISPER_MODEL = _get("OLIVIA_WHISPER_MODEL", "base")
# CTranslate2 compute type. "int8" is the low-memory CPU default.
WHISPER_COMPUTE_TYPE = _get("OLIVIA_WHISPER_COMPUTE_TYPE", "int8")
# "cpu" (fully offline, no GPU needed) or "cuda".
WHISPER_DEVICE = _get("OLIVIA_WHISPER_DEVICE", "cpu")
# Spoken language hint for Whisper (e.g. "en"); empty = auto-detect.
WHISPER_LANGUAGE = _get("OLIVIA_WHISPER_LANGUAGE", "en") or None
# Mic capture: sample rate (Whisper wants 16 kHz) and per-utterance seconds.
MIC_SAMPLE_RATE = int(_get("OLIVIA_MIC_SAMPLE_RATE", "16000"))
MIC_RECORD_SECONDS = float(_get("OLIVIA_MIC_RECORD_SECONDS", "5"))

# When true, online skills (search/wikipedia, weather, news, translate) are
# disabled and report "needs internet" instead of running. Core + offline
# skills keep working. Set OLIVIA_OFFLINE_ONLY=1 to enable.
OFFLINE_ONLY = _get("OLIVIA_OFFLINE_ONLY", "0").strip().lower() in ("1", "true", "yes", "on")
