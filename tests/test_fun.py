"""Fun skill pure logic: password, greeting, dice, card."""

import re

from olivia.skills import fun


def test_password_length_and_charset(monkeypatch):
    monkeypatch.setattr(fun, "sp", lambda *a, **k: None)
    pw = fun.generate_random_password()
    assert 8 <= len(pw) <= 13
    assert re.search(r"[a-zA-Z]", pw)
    assert any(c in "@#$%&*" for c in pw)


def test_greeting_detects():
    assert fun.greeting("hello there").endswith(".")
    assert fun.greeting("random words") == ""


def test_roll_dice_range(monkeypatch):
    monkeypatch.setattr(fun, "speak", lambda *a, **k: None)
    for _ in range(20):
        assert 1 <= fun.roll_dice() <= 6


def test_pick_card_format(monkeypatch):
    monkeypatch.setattr(fun, "sp", lambda *a, **k: None)
    card = fun.pick_card()
    assert card.startswith("The ")
    assert any(suit in card for suit in fun.CARDS)
