"""Translate language detection and target-code mapping."""

from olivia.skills import translate


def test_detect_simple_language():
    code, name = translate.detect_language(" hello to french")
    assert code == "fr"
    assert name == "french"


def test_detect_prefers_longest_match():
    # 'chinese (traditional)' must win over bare 'chinese'.
    code, name = translate.detect_language(" ni hao to chinese (traditional)")
    assert code == "zh-tw"


def test_detect_none_when_absent():
    code, name = translate.detect_language(" hello world")
    assert code is None
    assert name is None


def test_language_table_size():
    # The original monolith mapped ~100 languages; ensure coverage kept.
    assert len(translate.LANGUAGES) >= 100
    assert translate.LANGUAGES["hi"] == "hindi"
