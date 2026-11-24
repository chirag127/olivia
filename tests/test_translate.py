"""Translate language detection and target-code mapping."""

import sys
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from olivia.skills import translate


class TestAsyncTranslation(unittest.TestCase):
    def test_awaits_translation_and_closes_client(self):
        client = AsyncMock()
        client.__aenter__.return_value = client
        client.translate.return_value = SimpleNamespace(text="bonjour")
        with patch.dict(sys.modules, {"googletrans": SimpleNamespace(Translator=lambda: client)}):
            with patch.object(translate, "sp") as speak:
                self.assertEqual(translate.translate("translate hello to french"), "bonjour")
        client.translate.assert_awaited_once_with(" hello ", dest="fr")
        client.__aexit__.assert_awaited_once()
        speak.assert_called_once_with("bonjour")

    def test_closes_client_when_translation_fails(self):
        client = AsyncMock()
        client.__aenter__.return_value = client
        client.__aexit__.return_value = False
        client.translate.side_effect = RuntimeError("translation unavailable")
        with patch.dict(sys.modules, {"googletrans": SimpleNamespace(Translator=lambda: client)}):
            with patch.object(translate, "sp") as speak:
                with self.assertRaisesRegex(RuntimeError, "translation unavailable"):
                    translate.translate("translate hello to french")
        client.__aexit__.assert_awaited_once()
        speak.assert_not_called()


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
