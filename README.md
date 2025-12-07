# EchoMind: AI Voice Assistant Python System

[![Build Status](https://img.shields.io/github/actions/workflow/user/chirag127/EchoMind-AI-Voice-Assistant-Python-System/ci.yml?style=flat-square)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/EchoMind-AI-Voice-Assistant-Python-System?style=flat-square)](https://codecov.io/gh/chirag127/EchoMind-AI-Voice-Assistant-Python-System)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3100/)
[![Ruff Lint](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/main/api/ruff.json&style=flat-square)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-orange.svg?style=flat-square)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/EchoMind-AI-Voice-Assistant-Python-System.svg?style=flat-square)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System)

**EchoMind** is an advanced AI-powered, voice-controlled personal assistant system built in Python, designed to automate daily tasks and enhance productivity through intuitive voice commands.

Star ⭐ this Repo

## Features

*   **Voice Command Interface:** Interact with your system using natural language.
*   **AI-Powered NLP:** Understands and processes complex voice commands.
*   **Task Automation:** Automates everyday tasks like scheduling, reminders, and information retrieval.
*   **Information Management:** Organizes and retrieves data efficiently.
*   **Speech-to-Text (STT) & Text-to-Speech (TTS):** Seamless voice input and output.
*   **Modular Architecture:** Easily extensible and maintainable.

## Architecture

ascii
EchoMind/
├── app/                # Core application logic
│   ├── __init__.py
│   ├── assistant.py      # Main assistant class
│   ├── nlp/
│   │   ├── __init__.py
│   │   └── processor.py    # NLP processing module
│   ├── stt/
│   │   ├── __init__.py
│   │   └── recognizer.py   # Speech-to-text module
│   └── tts/
│       ├── __init__.py
│       └── speaker.py      # Text-to-speech module
├── cli/                # Command Line Interface
│   ├── __init__.py
│   └── main.py         # Entry point
├── config/
│   ├── __init__.py
│   └── settings.py     # Configuration settings
├── tests/
│   ├── __init__.py
│   └── ...             # Unit and integration tests
├── .gitignore
├── AGENTS.md
├── LICENSE
├── pyproject.toml
├── README.md
└── SECURITY.md


## Table of Contents

*   [Features](#features)
*   [Architecture](#architecture)
*   [AI Agent Directives](#ai-agent-directives)
*   [Development Setup](#development-setup)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Security](#security)

<details>
<summary><strong>🤖 AI Agent Directives (December 2025 Edition)</strong></summary>

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**. This repository, `EchoMind-AI-Voice-Assistant-Python-System`, is a Python-based AI voice assistant system.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like STT/TTS integration, NLP processing, and CLI interface, while maintaining a unified deployment.
    *   **AI Integration:** Deeply integrated with advanced STT/TTS models and NLP libraries. Prioritize modular design, clear API contracts, and robust error handling for all AI model interactions.
    *   **CLI Framework:** Uses `Click` for a powerful and intuitive command-line interface.

</details>

## Development Setup

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System.git
    cd EchoMind-AI-Voice-Assistant-Python-System
    

2.  **Set up the environment using uv:**
    bash
    uv venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    uv pip install -r requirements.txt
    

3.  **Install Ruff for linting and formatting:**
    bash
    uv pip install ruff
    

## Scripts

| Script Name         | Description                                         |
| :------------------ | :-------------------------------------------------- |
| `python cli/main.py`  | Starts the EchoMind voice assistant.                  |
| `pytest`            | Runs all unit and integration tests.                |
| `ruff check .`      | Checks code for linting errors.                     |
| `ruff format .`     | Formats code according to style guidelines.         |

## Principles

*   **SOLID:** Ensuring maintainable and scalable object-oriented design.
*   **DRY:** Avoiding repetition of code.
*   **YAGNI:** Not over-engineering; implementing only what is necessary.

## Usage

Once the environment is set up, you can start the EchoMind assistant from your terminal:

bash
python cli/main.py


Follow the on-screen prompts or simply speak your commands.

## Contributing

Contributions are welcome! Please refer to [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. See the [LICENSE](LICENSE) file for more details.

## Security

For security-related issues, please consult the [.github/SECURITY.md](.github/SECURITY.md) guidelines.
