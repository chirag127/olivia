"""Misc helpers: time/date/greeting, clipboard read-aloud, tab and YouTube helpers."""

import datetime
import webbrowser
from time import sleep

from olivia.core.speech import speak


def wish_me():
    """Return a greeting appropriate for the current hour."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning"
    if 12 <= hour < 18:
        return "Good Afternoon"
    return "Good Evening"


def current_time():
    """Speak the current time."""
    now = datetime.datetime.now()
    speak("The current time is")
    speak(now.strftime("%I:%M:%S"))


def current_date():
    """Speak the current date."""
    now = datetime.datetime.now()
    speak("The current date is")
    speak(now.strftime("%d-%m-%Y"))


def query_day():
    """Speak today's weekday name."""
    weekday = datetime.datetime.today().weekday()
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    speak("Today is " + days[weekday])
    return days[weekday]


def read_clipboard_aloud():
    """Print and speak the clipboard contents."""
    import pyperclip

    text = pyperclip.paste()
    print(text)
    speak(text)


def close_tab():
    """Close the current browser tab (Ctrl+W)."""
    import pyautogui

    pyautogui.hotkey("ctrl", "w")


def open_watch_later():
    """Open the YouTube Watch Later playlist and start playback."""
    webbrowser.open("https://www.youtube.com/playlist?list=WL")
    sleep(5)
    import pyautogui

    pyautogui.click(x=540, y=356)
