"""OS/desktop automation: power control, app launch/close, keyboard, notes, screen lock."""

import ctypes
import os
import re
import subprocess

from olivia.core import config
from olivia.core.speech import sp, speak

# Power commands keyed by trigger word.
POWER_COMMANDS = {
    "shutdown": "shutdown /s /f",
    "restart": "shutdown /r ",
    "logout": "shutdown /l",
    "hibernate": "shutdown /h",
    "lock": "rundll32.exe user32.dll,LockWorkStation",
}

# Apps the 'launch <app>' command can start, by trigger word -> exe path.
LAUNCH_APPS = {
    "notepad": r"C:\Windows\System32\notepad.exe",
    "calculator": r"C:\Windows\System32\calc.exe",
    "task manager": r"C:\Windows\System32\taskmgr.exe",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "paint": r"C:\Windows\System32\mspaint.exe",
    "media player": r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe",
    "wordpad": r"C:\Windows\System32\wordpad.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "sublime text": r"C:\Program Files\Sublime Text 3\sublime_text.exe",
    "notepad++": r"C:\Program Files\Notepad++\notepad++.exe",
    "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
    "microsoft edge": r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "microsoft word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
}

# Processes the 'close <app>' command can kill, by trigger word -> image name.
CLOSE_PROCESSES = {
    "chrome": "chrome.exe",
    "spotify": "Spotify.exe",
    "youtube": "chrome.exe",
    "torrent": "qbittorrent.exe",
    "vs code": "code.exe",
    "github desktop": "GitHubDesktop.exe",
    "telegram": "Telegram.exe",
    "whatsapp": "WhatsApp.exe",
    "explorer": "explorer.exe",
    "notepad": "notepad.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    "outlook": "OUTLOOK.EXE",
    "onenote": "ONENOTE.EXE",
    "teams": "Teams.exe",
    "skype": "skype.exe",
    "edge": "msedge.exe",
}


def power_command(query):
    """Run a shutdown/restart/logout/hibernate/lock command. Returns True if handled."""
    for trigger, cmd in POWER_COMMANDS.items():
        if trigger in query:
            speak(f"Hold On ! Your system is on its way to {trigger}")
            os.system(cmd)
            return True
    return False


def launch_app(query):
    """Launch a local application named in a 'launch <app>' command."""
    q = query.replace("launch", "")
    sp("Launching ")
    sp(q)
    for trigger, path in LAUNCH_APPS.items():
        if trigger in q:
            os.startfile(path)
            return
    if "control panel" in q or "setting" in q:
        os.system("control")
        return
    m = re.search("launch (.*)", query)
    if m:
        try:
            subprocess.Popen([m.group(1).strip()])
            sp("I have launched the desired application")
        except Exception:
            sp("I am not sure what application you want to launch")


def close_app(query):
    """Close a window/tab or kill an app named in a 'close ...' command."""
    import pyautogui

    if "page" in query or "tab" in query:
        pyautogui.hotkey("ctrl", "w")
        return
    for trigger, image in CLOSE_PROCESSES.items():
        if trigger in query:
            sp("closing " + trigger)
            os.system("TASKKILL /F /IM " + image)
            return
    if any(w in query for w in ("app", "application", "program", "process", "window")):
        pyautogui.hotkey("alt", "f4")
        return
    sp("Sorry, I could not find that")


def lock_screen():
    speak("locking the device")
    ctypes.windll.user32.LockWorkStation()


def type_text(text):
    """Type text, honouring simple key words (enter/tab/space/backspace)."""
    import pyautogui

    keymap = {
        "enter": "enter",
        "tab": "tab",
        "space": "space",
        "backspace": "backspace",
        "caps lock": "capslock",
    }
    for word, key in keymap.items():
        if word in text:
            pyautogui.press(key)
            return
    pyautogui.typewrite(text)


def press_key(query):
    """Press a key named in a 'press <key>' command."""
    import pyautogui

    m = re.search("press (.*)", query)
    if m:
        pyautogui.press(m.group(1).strip())


def write_note(note, with_timestamp=False):
    """Write a note to the notes file (overwrites)."""
    import datetime

    with open(config.NOTES_FILE, "w", encoding="utf-8") as f:
        if with_timestamp:
            f.write(str(datetime.datetime.now()) + " : " + note)
        else:
            f.write(note)


def read_note():
    """Return the notes file contents, or empty string if missing."""
    try:
        with open(config.NOTES_FILE, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
