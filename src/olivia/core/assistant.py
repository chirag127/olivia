"""Command router + main loop wiring speech I/O to skill modules."""

import webbrowser

from olivia.core.speech import sp, speak, take_command
from olivia.games import tic_tac_toe
from olivia.skills import (
    automation,
    communication,
    fun,
    media,
    news,
    search,
    system,
    translate,
    weather,
)
from olivia.utils import helpers

BANNER = r"""
    ,----..
   /   /   \    ,--,
  /   .     : ,--.'|     ,--,            ,--,
 .   /   ;.  \|  | :   ,--.'|          ,--.'|
.   ;   /  ` ;:  : '   |  |,      .---.|  |,
;   |  ; \ ; ||  ' |   `--'_    /.  ./|`--'_      ,--.--.
|   :  | ; | ''  | |   ,' ,'| .-' . ' |,' ,'|    /       \
'   ;  \; /  |'  : |__ |  | :.   \  ' .|  | :    \__\/: . .
  ;   :    /  ;  :    ;|  | '.'\   \   |  | '.'|/  /  ,.  |
   \   \ .'   |  ,   / ;  :    ;\   \ |;  :    ;  :   .'   \
    `---`      ---`-'  |  ,   /  '---" |  ,   /|  ,     .-./
                        ---`-'          ---`-'  `--`---'
"""

EXIT_WORDS = {"quit", "bye", "exit", "goodbye", "bye bye"}

# Simple canned answers: (predicate over query) -> spoken reply.
CANNED = {
    "what is your name": "My name is Olivia",
    "what is your age": "I am a computer program",
    "what is your job": "I am a Virtual assistant",
    "what is your favorite color": "My favorite color is black",
    "what is your purpose": "I am a Virtual assistant",
    "who made you": "I was created by Chirag Singhal",
    "who is your creator": "I was created by Chirag Singhal",
    "who are you": "I am a Virtual assistant",
    "thank you": "Welcome Sir",
    "how are you": "i am fine",
    "kill me": "I won't",
}


def handle(query):
    """Route one lowercased query to the right skill. Return False to stop the loop."""
    if query == "none" or not query.strip():
        return True

    # Exit
    if query in EXIT_WORDS or "olivia quit" in query or "olivia bye" in query:
        sp("Bye Sir")
        return False

    # Power control
    if any(k in query for k in ("desktop", "computer", "system")):
        if automation.power_command(query):
            return False

    # Date / time
    if "date" in query and "current" in query:
        helpers.current_date()
        return True
    if "time" in query and "current" in query:
        helpers.current_time()
        return True

    # Weather / news
    if "current weather" in query:
        weather.current_weather(query)
        return True
    if "news" in query and "latest" in query:
        news.news_from_bbc()
        return True

    # Wikipedia
    if "tell me about" in query:
        search.tell_me_about(query)
        return True
    if "who is" in query:
        search.who_is(query)
        return True

    # Games
    if (
        "game" in query
        and "start" in query
        and any(w in query for w in ("tic", "tac", "toe"))
    ):
        tic_tac_toe.play()
        return True

    # Fun
    if "pick" in query and "card" in query:
        fun.pick_card()
        return True
    if "roll" in query and "dice" in query:
        fun.roll_dice()
        return True
    if "joke" in query:
        sp(fun.neutral_joke()) if "neutral" in query else fun.give_joke()
        return True
    if "generate" in query:
        if "password" in query:
            fun.generate_random_password()
        elif "number" in query:
            import random

            sp(random.randint(0, 100))
        return True

    # System monitoring
    if "usage" in query:
        if "cpu" in query:
            system.cpu()
        elif "ram" in query:
            system.ram()
        elif "disk" in query:
            system.disk()
        elif "battery" in query:
            system.battery()
        return True
    if "status" in query and "battery" in query:
        system.battery_status()
        return True
    if "ip address" in query:
        system.give_ip()
        return True

    # Communication
    if "send" in query and "message" in query:
        _send_whatsapp_flow()
        return True
    if "email" in query:
        _send_email_flow()
        return True

    # Media
    if "screenshot" in query:
        media.take_screenshot()
        return True
    if "play" in query:
        _play_flow(query)
        return True

    # Search / open
    if "search in chrome" in query:
        _chrome_search_flow()
        return True
    if query.startswith("search") or "search" in query:
        search.search(query)
        return True
    if "open notepad" in query:
        automation.launch_app("launch notepad")
        return True
    if query.strip().startswith("open") or " open " in f" {query} ":
        search.open_site(query)
        return True

    # Translate
    if "translate" in query:
        translate.translate(query)
        return True

    # Launch / close apps
    if "launch" in query:
        automation.launch_app(query)
        return True
    if "close" in query:
        automation.close_app(query)
        return True

    # Keyboard
    if "press" in query:
        automation.press_key(query)
        return True

    # Lock
    if any(p in query for p in ("lock window", "lock screen", "lock the screen")):
        automation.lock_screen()
        return True

    # Notes
    if "read aloud" in query:
        helpers.read_clipboard_aloud()
        return True

    # Greetings / canned
    if query in ("hello", "hi", "hey", "hii"):
        speak("Hello Sir")
        speak(helpers.wish_me())
        return True
    for key, reply in CANNED.items():
        if key in query:
            speak(reply)
            return True
    if "wish me" in query:
        speak(helpers.wish_me())
        return True

    # Fallback: Google it
    webbrowser.open(f"https://www.google.com/search?q={query}&sourceid=olivia")
    return True


def _play_flow(query):
    media.play_on_youtube(query)
    while True:
        q = take_command().lower()
        if q in {"bye", "goodbye", "bye bye"}:
            sp("Bye Sir")
            return
        if "close" in q or "exit" in q or "quit" in q:
            media.player_control(q)
            return
        media.player_control(q)


def _send_whatsapp_flow():
    try:
        speak("to whom should i send to?")
        name = take_command().lower()
        to = communication.CONTACTS.get(name, communication.CONTACTS["None"])
        speak("What should i say?")
        content = take_command()
        communication.send_whatsapp(to, content)
        speak("Message has been sent")
    except Exception as e:
        print(e)
        speak("Sorry Sir, I am not able to send this message")


def _send_email_flow():
    try:
        speak("What should I say?")
        content = take_command().lower()
        communication.send_email(communication.CONTACTS["None"], content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email")


def _chrome_search_flow():
    speak("What should i search for sir")
    q = take_command().lower()
    webbrowser.open(f"https://www.google.com/search?q={q}")


def run():
    """Start Olivia: greet, then listen and dispatch until an exit command."""
    print(BANNER)
    print(helpers.wish_me())
    running = True
    while running:
        query = take_command().lower()
        running = handle(query)
