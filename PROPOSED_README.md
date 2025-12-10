<div align="center">
  <img src="https://raw.githubusercontent.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/main/assets/echomind-hero.png" alt="EchoMind Logo" width="150"/>
  <h1>EchoMind: AI-Powered Voice Assistant Python System</h1>
  <p>The definitive, modular Python solution for highly customized, voice-controlled personal and professional automation.</p>
</div>

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/EchoMind-AI-Voice-Assistant-Python-System/ci.yml?branch=main&style=flat-square&label=Build%20Status)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/actions/workflows/ci.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/chirag127/EchoMind-AI-Voice-Assistant-Python-System?style=flat-square&token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/chirag127/EchoMind-AI-Voice-Assistant-Python-System)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Linting Status](https://img.shields.io/badge/Linter-Ruff-666666?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/EchoMind-AI-Voice-Assistant-Python-System?style=flat-square&label=Stars&color=yellow)](https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System/stargazers)

<div align="center">
  <a href="https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System" target="_blank">
    <img alt="GitHub stars" src="https://img.shields.io/badge/Star%20⭐%20This%20Repo-lightgrey?style=social&label=Support%20Development" />
  </a>
</div>

---

## 🌟 Briefing: Zero-Latency Voice Automation Engine

EchoMind is an enterprise-grade AI Voice Assistant framework written in Python, designed for high extensibility and low latency. It provides a foundational, modular architecture for integrating advanced Speech-to-Text (STT) and Natural Language Understanding (NLU) services into customizable, voice-driven workflows, optimizing productivity for technical users.

Built on the Modular Monolith principle, EchoMind ensures that core functionalities (Listening, Processing, Responding) are decoupled, allowing developers to easily swap out underlying AI models (e.g., swapping Whisper for proprietary STT) or add new Command Modules without altering the core loop.

## 🗂️ Table of Contents

1.  [Architecture & Modularity](#️-architecture--modularity)
2.  [Getting Started](#-getting-started)
3.  [Development Scripts](#️-development-scripts)
4.  [Core Development Principles](#-core-development-principles)
5.  [AI Agent Directives (System Documentation)](#-ai-agent-directives-system-documentation)
6.  [Contributing](.github/CONTRIBUTING.md)
7.  [Security](.github/SECURITY.md)
8.  [License](#-license)

## 🏗️ Architecture & Modularity

EchoMind employs a robust **Modular Monolith Architecture**, organized around the main operational loop (Listen -> Interpret -> Execute). This design isolates key components, ensuring maximum testability and seamless replacement of core services.

### System Diagram (Mermaid)

mermaid
graph TD
    A[Voice Input/Microphone] --> B(STT Service: Transcription);
    B --> C(NLP Core: Intent & Entity Parsing);
    C --> D{Command Dispatcher};
    D -- Task Command --> E[Module: Task Automation];
    D -- Info Query --> F[Module: Knowledge Base];
    D -- System Control --> G[Module: Configuration];
    E --> H(TTS Service: Synthesized Response);
    F --> H;
    G --> H;
    H --> I[Audio Output/Speaker];

    subgraph Core System Loop
        B; C; D; H;
    end
    style Core System Loop fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px


### Module Structure

The project structure enforces clean separation:


echomind/
├── core/             # Core operational logic (Listener, Dispatcher, TTS/STT interfaces)
│   ├── listener.py
│   ├── dispatcher.py
│   └── interfaces/
├── modules/          # Extensible command modules (e.g., Calendar, Email, Weather)
│   ├── automation/
│   ├── info_retrieval/
│   └── system_control/
├── models/           # Pydantic Schemas and data validation logic
├── testing/          # Integration fixtures and mocks
└── cli.py            # Main entry point using Click


## 🚀 Getting Started

To initialize the development environment, EchoMind utilizes **uv** for high-speed dependency management and virtual environment setup.

### Prerequisites

*   Python 3.11+
*   System dependencies for audio processing (e.g., PortAudio for `pyaudio` if required).

### Setup

1.  **Clone the Repository:**
    bash
    git clone https://github.com/chirag127/EchoMind-AI-Voice-Assistant-Python-System.git
    cd EchoMind-AI-Voice-Assistant-Python-System
    

2.  **Install Dependencies using uv:**
    bash
    # Create isolated virtual environment
    uv venv
    source .venv/bin/activate

    # Install production and development dependencies
    uv pip install -r requirements.txt -r requirements-dev.txt
    

3.  **Configuration:**
    Create a `.env` file in the root directory to store API keys (e.g., Google STT/NLU Keys, OpenAI TTS keys).

    ini
    # .env example
    API_KEY_NLU="sk-XXXXX"
    DEFAULT_VOICE="female-1"
    WAKE_WORD="Echo"
    

4.  **Run the System:**
    bash
    uv run start
    

## 🛠️ Development Scripts

This project uses the `uv` toolchain and adheres to strict formatting and testing standards enforced by Ruff and Pytest.

| Command | Description | Tooling |
| :--- | :--- | :--- |
| `uv run format` | Applies aggressive formatting and auto-fixes linting issues. | Ruff |
| `uv run lint` | Checks code quality and security without fixing. | Ruff |
| `uv run test` | Executes all unit and integration tests. | Pytest |
| `uv run cov` | Runs tests and generates a detailed coverage report. | Pytest, Coverage.py |
| `uv run start` | Executes the main voice assistant CLI entry point (`python echomind/cli.py run`). | Python |

## 📐 Core Development Principles

We adhere strictly to time-tested architectural principles to maintain code integrity and extensibility:

*   **S.O.L.I.D:** Ensuring modules are cohesive and loosely coupled, especially between the core loop and the specific command modules.
*   **D.R.Y (Don't Repeat Yourself):** Abstracting common functions like configuration loading, logging, and error handling into shared utility classes.
*   **Y.A.G.N.I (You Ain't Gonna Need It):** Focusing development strictly on the current scope (Voice Assistant Core) and avoiding premature complexity in command modules.
*   **High Cohesion, Low Coupling:** The Listener module should only concern itself with audio input; the Dispatcher should only concern itself with routing parsed intent.

## 🤖 AI Agent Directives (System Documentation)

<details>
<summary><strong>SYSTEM AUDIT AND EXECUTION PROTOCOL (INTERNAL USE)</strong></summary>

### 1. IDENTITY & PROJECT CONTEXT
*   **Project Name:** `EchoMind-AI-Voice-Assistant-Python-System`
*   **Current State:** Active Development (Modular Monolith Architecture).
*   **Primary Goal:** Maintain low-latency performance in the core I/O loop while ensuring command modules are infinitely extensible.

### 2. CORE APEX TOOLCHAIN (Python 3.11+ Standard)
| Category | Tool | Directive |
| :--- | :--- | :--- |
| **Package Manager** | `uv` | Must be used for all dependency operations (`install`, `lock`, `venv`, `run`). |
| **Linter/Formatter** | `Ruff` | Execute `uv run format` before every commit. Enforce Pylint rules via Ruff configuration. |
| **Testing Framework** | `Pytest` | All core loop components require 100% unit test coverage. Use fixtures extensively for mocking external STT/NLU API responses. |
| **Virtualization** | `.venv` | Environment must be isolated using `uv venv`. |

### 3. ARCHITECTURAL MANDATES
*   **Pattern:** Modular Monolith (Python).
*   **Principle:** Strictly separate I/O boundaries. The `core` package must *never* import specific command logic from `modules/`. Imports should flow one way: `core` calls abstracted interfaces, which are implemented by `modules`.
*   **Error Handling:** Use custom exceptions for I/O failures (e.g., `STTTranscriptionError`, `NLPIntentNotFound`) and log them using standard Python logging, rather than printing to stdout.

### 4. VERIFICATION AND SANITY CHECK COMMANDS
Agents must run these commands to verify operational integrity:

bash
# 1. Environment and toolchain verification
uv --version
python --version

# 2. Dependency audit
uv pip list --format freeze > installed_deps.txt

# 3. Code quality enforcement (LINT)
uv run lint

# 4. Full test suite execution
uv run test


### 5. EXECUTION DIRECTIVE
If tasked with implementing a new command module (e.g., `modules/finance/`), the Agent must first define the required input contract (data structure) in `echomind/models/` and ensure the module adheres to the generic `ICommand` interface expected by the Dispatcher.
</details>

## 🤝 Contributing

We welcome professional contributions. Please review the official guidelines before submitting a Pull Request:

*   [Contribution Guidelines](.github/CONTRIBUTING.md)
*   [Report a Bug](.github/ISSUE_TEMPLATE/bug_report.md)
*   [Security Policy](.github/SECURITY.md)

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License. See the [LICENSE](LICENSE) file for details.