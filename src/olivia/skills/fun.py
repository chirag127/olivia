"""Fun: jokes, card tricks, dice rolls, random passwords, greetings."""

import json
import math
import random

import requests

from olivia.core.speech import sp, speak

GREETING_INPUTS = ["hi", "hey", "hola", "wassup", "hello"]
GREETING_RESPONSES = ["howdy", "all that good", "hello master", "heythere"]

CARDS = ["Diamonds", "Spades", "Hearts", "Clubs"]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


def neutral_joke():
    """Return a neutral programming joke."""
    import pyjokes

    return pyjokes.get_joke()


def give_joke():
    """Fetch and speak a random dad joke."""
    res = requests.get("https://icanhazdadjoke.com/slack", timeout=10)
    joke = json.loads(res.text)["attachments"][0]["text"]
    print("The random joke is ", joke)
    speak(joke)
    return joke


def pick_card():
    """Speak a random playing card."""
    card = random.choice(CARDS)
    rank = random.choice(RANKS)
    text = f"The {rank} of {card}"
    sp(text)
    return text


def roll_dice():
    """Roll a six-sided die, speak and return the result."""
    r = random.randint(1, 6)
    speak("you got " + str(r))
    return r


def greeting(text):
    """Return a greeting response if the text is a greeting, else ''."""
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + "."
    return ""


def generate_random_password():
    """Build a random 8-13 char password (50% alpha, 30% num, 20% special)."""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*"
    pass_len = random.randint(8, 13)
    alpha_len = pass_len // 2
    num_len = math.ceil(pass_len * 30 / 100)
    special_len = pass_len - (alpha_len + num_len)

    chars = []

    def add(length, pool, mixed_case=False):
        for _ in range(length):
            c = random.choice(pool)
            if mixed_case and random.randint(0, 1):
                c = c.upper()
            chars.append(c)

    add(alpha_len, alpha, True)
    add(num_len, num)
    add(special_len, special)
    random.shuffle(chars)
    password = "".join(chars)
    sp(password)
    return password
