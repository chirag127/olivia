"""Command router dispatch: handle() routes queries to the right skill."""

import pytest

from olivia.core import assistant


@pytest.fixture(autouse=True)
def _mute(monkeypatch):
    """Silence all speech and take_command across the router."""
    monkeypatch.setattr(assistant, "speak", lambda *a, **k: None)
    monkeypatch.setattr(assistant, "sp", lambda *a, **k: None)
    monkeypatch.setattr(assistant, "take_command", lambda: "none")


def test_exit_returns_false():
    assert assistant.handle("bye") is False
    assert assistant.handle("olivia quit") is False


def test_none_keeps_running():
    assert assistant.handle("none") is True
    assert assistant.handle("") is True


def test_joke_dispatch(monkeypatch):
    called = {}
    monkeypatch.setattr(assistant.fun, "give_joke", lambda: called.setdefault("joke", True))
    assert assistant.handle("tell me a joke") is True
    assert called.get("joke")


def test_cpu_usage_dispatch(monkeypatch):
    called = {}
    monkeypatch.setattr(assistant.system, "cpu", lambda: called.setdefault("cpu", True))
    assert assistant.handle("what is the cpu usage") is True
    assert called.get("cpu")


def test_translate_dispatch(monkeypatch):
    seen = {}
    monkeypatch.setattr(assistant.translate, "translate", lambda q: seen.setdefault("q", q))
    assert assistant.handle("translate hello to french") is True
    assert "french" in seen["q"]


def test_search_dispatch(monkeypatch):
    seen = {}
    monkeypatch.setattr(assistant.search, "search", lambda q: seen.setdefault("q", q))
    assert assistant.handle("search cats on youtube") is True
    assert "cats" in seen["q"]


def test_weather_dispatch(monkeypatch):
    seen = {}
    monkeypatch.setattr(assistant.weather, "current_weather", lambda q: seen.setdefault("q", q))
    assert assistant.handle("current weather in london") is True
    assert "london" in seen["q"]


def test_screenshot_dispatch(monkeypatch):
    called = {}
    monkeypatch.setattr(assistant.media, "take_screenshot", lambda: called.setdefault("s", True))
    assert assistant.handle("take a screenshot") is True
    assert called.get("s")


def test_canned_answer(monkeypatch):
    said = []
    monkeypatch.setattr(assistant, "speak", said.append)
    assert assistant.handle("what is your name") is True
    assert any("Olivia" in s for s in said)


def test_fallback_opens_google(monkeypatch):
    opened = []
    monkeypatch.setattr(assistant.webbrowser, "open", opened.append)
    assert assistant.handle("some unrecognized thing") is True
    assert opened and "google.com/search" in opened[0]


def test_lock_screen_dispatch(monkeypatch):
    called = {}
    monkeypatch.setattr(assistant.automation, "lock_screen", lambda: called.setdefault("l", True))
    assert assistant.handle("lock screen") is True
    assert called.get("l")
