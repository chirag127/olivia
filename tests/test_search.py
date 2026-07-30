"""Search / open command routing (webbrowser mocked)."""

from olivia.skills import search


def test_search_youtube(monkeypatch):
    opened = []
    monkeypatch.setattr(search.webbrowser, "open", opened.append)
    monkeypatch.setattr(search, "sp", lambda *a, **k: None)
    search.search("search cats on youtube")
    assert opened
    assert "youtube.com/results" in opened[0]
    assert "cats" in opened[0]


def test_search_default_google(monkeypatch):
    opened = []
    monkeypatch.setattr(search.webbrowser, "open", opened.append)
    monkeypatch.setattr(search, "sp", lambda *a, **k: None)
    search.search("search quantum physics")
    assert "google.com/search" in opened[0]


def test_open_known_site(monkeypatch):
    opened = []
    monkeypatch.setattr(search.webbrowser, "open", opened.append)
    monkeypatch.setattr(search, "speak", lambda *a, **k: None)
    search.open_site("open github")
    assert opened[0] == "https://www.github.com/"


def test_open_unknown_falls_back_to_ddg(monkeypatch):
    opened = []
    monkeypatch.setattr(search.webbrowser, "open", opened.append)
    monkeypatch.setattr(search, "speak", lambda *a, **k: None)
    search.open_site("open somethingweird")
    assert "duckduckgo.com" in opened[0]
