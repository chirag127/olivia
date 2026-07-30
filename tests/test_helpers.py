"""Time/date/greeting helpers."""

from olivia.utils import helpers


def test_wish_me_morning(monkeypatch):
    import datetime

    class FakeDT(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 1, 1, 9, 0, 0)

    monkeypatch.setattr(helpers.datetime, "datetime", FakeDT)
    assert helpers.wish_me() == "Good Morning"


def test_wish_me_evening(monkeypatch):
    import datetime

    class FakeDT(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 1, 1, 20, 0, 0)

    monkeypatch.setattr(helpers.datetime, "datetime", FakeDT)
    assert helpers.wish_me() == "Good Evening"


def test_query_day(monkeypatch):
    monkeypatch.setattr(helpers, "speak", lambda *a, **k: None)
    day = helpers.query_day()
    assert day in [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
