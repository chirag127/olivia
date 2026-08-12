# Olivia

> A modular, offline-capable Python voice assistant for Windows. Speech-to-text runs locally with faster-whisper (no cloud STT); text-to-speech is the offline Windows SAPI5 engine. Core commands work with no internet; optional skills (search, weather, news, translate) use the network and degrade gracefully offline.

**Live site:** https://olivia.oriz.in

[![Stars](https://img.shields.io/github/stars/chirag127/olivia?style=flat-square)](https://github.com/chirag127/olivia/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](./LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chirag127/olivia/ci.yml?branch=main&style=flat-square)](https://github.com/chirag127/olivia/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/)

Olivia records your microphone, transcribes it **locally** with a Whisper model (`faster-whisper`, CTranslate2), routes the command to a skill, and replies out loud through the offline Windows SAPI5 voice. The Whisper model auto-downloads once from Hugging Face on first run; after that, speech recognition works fully offline.

## Offline vs online

Speech recognition (Whisper), text-to-speech (SAPI5), and command routing are **100% offline**. Skills split in two:

- **Offline skills** — system monitoring (CPU/RAM/disk/battery via psutil), desktop automation (launch/close apps, keyboard, screen lock, power control via pyautogui/ctypes), screenshots, clipboard read-aloud, offline jokes (pyjokes), Tic-Tac-Toe, time/date/greeting, notes.
- **Online skills** — web search + open-site, Wikipedia ("tell me about" / "who is"), weather (OpenWeatherMap), BBC news (NewsAPI), translation (googletrans), YouTube playback, public IP, dad jokes, internet speed test.

Set `OLIVIA_OFFLINE_ONLY=1` to disable every online skill: it announces "needs internet" instead of running, and the assistant keeps working for the offline skills. Without the flag, online skills run normally and only fail if the network is down (they report the error, they do not crash the loop).

## What it does

Voice-controlled, grouped by skill (O = offline, N = needs internet):

- **Search & knowledge** (N) — Google / YouTube / Wikipedia / Bing / DuckDuckGo and 40+ other engines; "tell me about X" and "who is X" read Wikipedia summaries aloud.
- **Weather** (N) — current conditions for any city (OpenWeatherMap) + an internet speed test.
- **News** (N) — top BBC headlines (NewsAPI).
- **Translation** (N) — text to 100+ languages via googletrans ("translate hello to french").
- **System monitoring** (O) — CPU / RAM / disk / battery usage (psutil); public IP (N).
- **Media** — play any song/video on YouTube and control it (N); take screenshots (O).
- **Communication** (N) — send email (env-var credentials) and WhatsApp messages.
- **Automation** (O) — launch and close apps, press keys, type dictation, lock the screen, power control (shutdown/restart/logout/hibernate).
- **Fun** — offline jokes / cards / dice / random-password generation (O); online dad jokes (N).
- **Games** (O) — a Tkinter Tic-Tac-Toe.

## Architecture

The former 8500-line monolith is split into a clean package under `src/olivia/`:

```
src/olivia/
  __init__.py
  __main__.py          # entry point: python -m olivia
  core/
    speech.py          # speak() offline SAPI5 TTS + take_command() local Whisper STT
    assistant.py       # main loop + command router + offline/online gating
    config.py          # env-var config (Whisper model, offline_only, email, API keys, voice)
  skills/
    search.py          # google/youtube/wikipedia/open-site
    weather.py         # weather + internet speed test
    news.py            # BBC news
    translate.py       # googletrans wrapper (100+ languages)
    system.py          # cpu/ram/disk/battery/ip
    media.py           # youtube play + controls, screenshots
    communication.py   # email + whatsapp
    automation.py      # launch/close apps, keyboard, notes, lock, power
    fun.py             # jokes, cards, dice, passwords
  games/
    tic_tac_toe.py     # Tkinter game with pure, testable win logic
  utils/
    helpers.py         # time/date/greeting, clipboard, tab helpers
```

The command router (`core/assistant.py`) maps spoken phrases to skill functions through small dispatch tables — every skill is independently importable and testable.

## Setup

```bash
git clone https://github.com/chirag127/olivia.git
cd olivia
pip install -r requirements.txt   # or: pip install -e .
cp .env.example .env              # then fill in the values (all optional)
python -m olivia
```

**First run downloads the Whisper model** (`base` ≈ 145 MB) from Hugging Face into the local cache — this needs internet once. After that, speech-to-text runs fully offline. Pick a size via `OLIVIA_WHISPER_MODEL` (`tiny` / `base` / `small` / `medium` / `large-v3`); bigger is more accurate and slower.

Then speak a command when Olivia starts listening. Say `bye` / `goodbye` / `exit` to quit.

To run without any network, download the model once, then start with:

```bash
OLIVIA_OFFLINE_ONLY=1 python -m olivia
```

## Environment variables

Copy `.env.example` to `.env` and set:

| Variable | Purpose |
| --- | --- |
| `OLIVIA_WHISPER_MODEL` | Local STT model size: `tiny`/`base`/`small`/`medium`/`large-v3` (default `base`) |
| `OLIVIA_WHISPER_DEVICE` | `cpu` (offline default) or `cuda` |
| `OLIVIA_WHISPER_COMPUTE_TYPE` | CTranslate2 compute type (default `int8`) |
| `OLIVIA_WHISPER_LANGUAGE` | Spoken-language hint, e.g. `en`; empty = auto-detect |
| `OLIVIA_OFFLINE_ONLY` | `1` disables all online skills (default `0`) |
| `OLIVIA_EMAIL` | Gmail address for the email / WhatsApp skills |
| `OLIVIA_EMAIL_PASSWORD` | Gmail app password (never a real login password) |
| `OPENWEATHER_API_KEY` | OpenWeatherMap key for weather |
| `NEWS_API_KEY` | NewsAPI key for BBC headlines |
| `OLIVIA_VOICE_INDEX` | SAPI5 voice index (0 = male, 1 = female) — optional |

No credentials are hardcoded in source. Load `.env` into your shell before launching (for example with `python-dotenv` or your own exporter).

## Feature reference

| Say | Olivia does |
| --- | --- |
| "search cats on youtube" | Opens a YouTube search |
| "tell me about python" | Reads a Wikipedia summary |
| "current weather in london" | Speaks current weather |
| "latest news" | Reads BBC headlines |
| "translate hello to french" | Speaks the translation |
| "what is the cpu usage" | Speaks CPU load |
| "play lofi beats" | Plays on YouTube; then "pause", "volume up", "next" |
| "take a screenshot" | Saves a timestamped PNG |
| "launch notepad" / "close chrome" | Starts / kills an app |
| "lock screen" | Locks Windows |
| "generate password" | Speaks a random password |
| "start tic tac toe game" | Opens the game window |
| "bye" | Exits |

## Requirements

- Windows (SAPI5 TTS, `winshell`, `pywin32`, `pyautogui`)
- Python 3.10+
- A working microphone
- ~150 MB disk + one-time internet for the Whisper model download (`base`)

## Testing

```bash
pip install pytest pytest-cov numpy
pytest -q
```

Tests cover the pure logic — Tic-Tac-Toe win/tie detection, command routing (mocked speech I/O), offline-only gating, local-Whisper STT (mocked mic + model, no network), translation language detection, search routing, config env reading, and password/greeting helpers.

## Contributing

Issues and PRs welcome. Keep skills self-contained: one module per feature group, heavy/native imports lazy inside functions so the module stays importable on headless CI. Run `pytest` before opening a PR.

## License

[MIT](./LICENSE)
