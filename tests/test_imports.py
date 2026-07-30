"""Smoke test: every skill/core/game module imports without third-party deps."""

import importlib

import pytest

MODULES = [
    "olivia",
    "olivia.__main__",
    "olivia.core.config",
    "olivia.core.speech",
    "olivia.core.assistant",
    "olivia.skills.search",
    "olivia.skills.weather",
    "olivia.skills.news",
    "olivia.skills.translate",
    "olivia.skills.system",
    "olivia.skills.media",
    "olivia.skills.communication",
    "olivia.skills.automation",
    "olivia.skills.fun",
    "olivia.games.tic_tac_toe",
    "olivia.utils.helpers",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    assert importlib.import_module(name) is not None
