# Olivia

> A modular Python voice assistant for Windows. Speak a command, get a spoken answer — search, weather, news, translation, system monitoring, desktop automation, and more.

**Live site:** https://olivia.oriz.in

[![Stars](https://img.shields.io/github/stars/chirag127/olivia?style=flat-square)](https://github.com/chirag127/olivia/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](./LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chirag127/olivia/ci.yml?branch=main&style=flat-square)](https://github.com/chirag127/olivia/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/)

Olivia listens on your microphone, recognizes speech (Google STT), acts on the command, and replies out loud through the Windows SAPI5 voice engine. It automates common desktop and web tasks entirely by voice.

## What it does

Voice-controlled, grouped by skill:

- **Search & knowledge** — Google / YouTube / Wikipedia / Bing / DuckDuckGo and 40+ other engines; "tell me about X" and "who is X" read Wikipedia summaries aloud.
- **Weather** — current conditions for any city (OpenWeatherMap) + an internet speed test.
- **News** — top BBC headlines (NewsAPI).
- **Translation** — text to 100+ languages via googletrans ("translate hello to french").
- **System monitoring** — CPU / RAM / disk / battery usage and public IP (psutil).
- **Media** — play any song/video on YouTube and control it (pause, volume, speed, tabs); take screenshots.
- **Communication** — send email (env-var credentials) and WhatsApp messages.
- **Automation** — launch and close apps, press keys, type dictation, lock the screen, power control (shutdown/restart/logout/hibernate).
- **Fun** — jokes, card tricks, dice rolls, random-password generation.
- **Games** — a Tkinter Tic-Tac-Toe.

## Architecture

The former 8500-line monolith is split into a clean package under `src/olivia/`:

```
src/olivia/
  __init__.py
  __main__.py          # entry point: python -m olivia
  core/
    speech.py          # speak() TTS + take_command() STT
    assistant.py       # main loop + command router
    config.py          # env-var config (email, API keys, voice)
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
pip install -r requirements.txt
cp .env.example .env      # then fill in the values
python -m olivia
```

On Windows, if `PyAudio` fails to install from the requirements file:

```bash
pip install pipwin && pipwin install pyaudio
```

Then speak a command when Olivia starts listening. Say `bye` / `goodbye` / `exit` to quit.

## Environment variables

Copy `.env.example` to `.env` and set:

| Variable | Purpose |
| --- | --- |
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

- Windows (SAPI5, `winshell`, `pywin32`, `pyautogui`)
- Python 3.10+
- A working microphone

## Testing

```bash
pip install pytest pytest-cov numpy
pytest -q
```

Tests cover the pure logic — Tic-Tac-Toe win/tie detection, command routing (mocked speech I/O), translation language detection, search routing, config env reading, and password/greeting helpers.

## Contributing

Issues and PRs welcome. Keep skills self-contained: one module per feature group, heavy/native imports lazy inside functions so the module stays importable on headless CI. Run `pytest` before opening a PR.

## License

[MIT](./LICENSE)
