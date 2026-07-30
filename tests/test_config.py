"""Config reads env vars."""

import importlib


def test_config_reads_env(monkeypatch):
    monkeypatch.setenv("OLIVIA_EMAIL", "a@b.com")
    monkeypatch.setenv("OLIVIA_EMAIL_PASSWORD", "secret")
    monkeypatch.setenv("OPENWEATHER_API_KEY", "owm-key")
    monkeypatch.setenv("NEWS_API_KEY", "news-key")
    monkeypatch.setenv("OLIVIA_VOICE_INDEX", "0")

    from olivia.core import config

    importlib.reload(config)
    assert config.OLIVIA_EMAIL == "a@b.com"
    assert config.OLIVIA_EMAIL_PASSWORD == "secret"
    assert config.OPENWEATHER_API_KEY == "owm-key"
    assert config.NEWS_API_KEY == "news-key"
    assert config.VOICE_INDEX == 0


def test_config_defaults(monkeypatch):
    for k in ("OLIVIA_EMAIL", "OLIVIA_EMAIL_PASSWORD", "OPENWEATHER_API_KEY", "NEWS_API_KEY"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.delenv("OLIVIA_VOICE_INDEX", raising=False)

    from olivia.core import config

    importlib.reload(config)
    assert config.OLIVIA_EMAIL is None
    assert config.VOICE_INDEX == 1
