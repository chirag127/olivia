"""Media: play YouTube videos, take screenshots."""

import os
import time

from olivia.core import config
from olivia.core.speech import speak


def play_on_youtube(query):
    """Play the requested song/video on YouTube (from 'play ...')."""
    song = query.replace("play ", "")
    speak("Playing " + song)
    print(song)
    import pywhatkit

    pywhatkit.playonyt(song)
    return song


def take_screenshot():
    """Save a timestamped screenshot to the configured directory."""
    import pyautogui

    name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
    path = os.path.join(config.SCREENSHOT_DIR, name + ".png")
    img = pyautogui.screenshot(path)
    print("Screenshot taken")
    return path


# YouTube / browser hotkeys keyed by trigger word, in match order.
PLAYER_HOTKEYS = [
    (("close",), ("ctrl", "w")),
    (("pause", "pass", "stop", "resume", "continue"), ("space",)),
    (("next tab",), ("ctrl", "tab")),
    (("previous tab",), ("ctrl", "shift", "tab")),
    (("next", "skip"), ("shift", "n")),
    (("reload", "refresh", "restart", "reboot"), ("ctrl", "r")),
    (("mute", "unmute"), ("ctrl", "m")),
    (("increase volume", "volume up", "louder"), ("ctrl", "up")),
    (("decrease volume", "volume down", "quieter"), ("ctrl", "down")),
    (("increase speed", "speed up", "faster"), ("shift", ".")),
    (("decrease speed", "speed down", "slower"), ("shift", ",")),
    (("download",), ("ctrl", "j")),
    (("history page",), ("ctrl", "h")),
    (("bookmark manager", "bookmark page"), ("ctrl", "shift", "o")),
    (("bookmark bar",), ("ctrl", "shift", "b")),
]


def player_control(query):
    """Send the browser/YouTube hotkey matching a control phrase. Returns True if handled."""
    import pyautogui

    if "next tab" in query:
        pyautogui.hotkey("ctrl", "tab")
        return True
    if "previous tab" in query:
        pyautogui.hotkey("ctrl", "shift", "tab")
        return True
    for triggers, keys in PLAYER_HOTKEYS:
        if any(t in query for t in triggers):
            pyautogui.hotkey(*keys)
            return True
    return False
