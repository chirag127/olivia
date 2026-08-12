"""Offline STT layer: take_command uses local Whisper, no network."""

from olivia.core import speech


def test_take_command_transcribes_locally(monkeypatch):
    """Mic + model are mocked; take_command returns the local transcript."""
    monkeypatch.setattr(speech, "_record", lambda *a, **k: "FAKE_AUDIO")
    monkeypatch.setattr(speech, "transcribe", lambda audio: "hello olivia")
    assert speech.take_command() == "hello olivia"


def test_take_command_none_on_silence(monkeypatch):
    monkeypatch.setattr(speech, "_record", lambda *a, **k: "FAKE_AUDIO")
    monkeypatch.setattr(speech, "transcribe", lambda audio: "")
    assert speech.take_command() == "None"


def test_take_command_none_on_error(monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("no mic")

    monkeypatch.setattr(speech, "_record", boom)
    assert speech.take_command() == "None"


def test_transcribe_uses_whisper_model(monkeypatch):
    """transcribe joins segment text from the loaded faster-whisper model."""

    class Seg:
        def __init__(self, text):
            self.text = text

    class Model:
        def transcribe(self, audio, **kwargs):
            return [Seg(" what "), Seg("time")], object()

    monkeypatch.setattr(speech, "_get_whisper", lambda: Model())
    assert speech.transcribe("audio") == "what time"
