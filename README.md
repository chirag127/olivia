# EchoMind — AI Voice Assistant (Python)

> A Windows desktop voice assistant ("Olivia") written in Python. Listens to spoken commands and responds with speech, using speech-to-text, text-to-speech, and web/OS automation.

[![Live](https://img.shields.io/badge/live-demo-brightgreen?style=flat-square)](https://echomind-ai-voice-assistant-python-system.oriz.in)
[![Stars](https://img.shields.io/github/stars/chirag127/EchoMind-AI-Voice-Assistant-Python-System?style=flat-square)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square)](https://www.python.org/)

Live page: https://echomind-ai-voice-assistant-python-system.oriz.in

## What it does

EchoMind (internally named Olivia) is a voice-controlled assistant for Windows. Speak a command and it recognizes speech via the microphone, acts on it, and replies out loud through the SAPI5 voice engine. It automates common desktop and web tasks entirely by voice.

## Features

- Speech-to-text input (`SpeechRecognition`) and text-to-speech output (`pyttsx3`, SAPI5 voice)
- Google, YouTube, and Wikipedia search by voice
- Play songs / videos on YouTube (`pywhatkit`)
- Send WhatsApp messages and emails
- Tell the time, date, weather, jokes, and IP address
- Take screenshots and control the mouse/keyboard (`pyautogui`)
- Open websites and local applications
- Internet speed test, clipboard operations, and system info (`psutil`)
- Simple Tkinter GUI

## Requirements

- Windows (uses SAPI5, `winshell`, `pywin32`, `pyautogui`)
- Python 3.9+
- A working microphone

## Setup

```bash
git clone https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System.git
cd EchoMind-AI-Voice-Assistant-Python-System
pip install -r requirements.txt
```

Note: `PyAudio` may need a platform wheel on Windows — install it with `pip install pipwin && pipwin install pyaudio` if the requirements install fails.

## Run

```bash
python src/Olivia.py
```

Then speak your command when the assistant starts listening. Say `bye` / `goodbye` to exit.

## Project layout

```
src/
  Olivia.py                        # main assistant entry point
  functions.py                     # helper functions (keys, tabs, etc.)
  jokes.py                         # joke command
  playwl.py                        # play-related helpers
  enjoy_youtube_watching_video.py  # YouTube watching helper
requirements.txt                   # Python dependencies
docs/                              # GitHub Pages landing page
```

## License

[MIT](./LICENSE)
