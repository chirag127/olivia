from bs4 import BeautifulSoup
from googletrans import Translator
import ctypes
import datetime
import json
import operator
import os
import pyttsx3  # pip install pyttsx3
import random
import requests
import shutil
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import subprocess
import sys
import time
import tkinter
import webbrowser
import wikipedia  # pip install wikipedia
import win32com.client as wincl
import winshell


# I was getting error so i install pyaudio
# error in that too so i googled it on the stackover flow.

"""
# Text to Speech Engine
# Define Text to Speech Engine

"""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am olivia Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chriagsinghal@gmail.com', 'my password')
    server.sendmail('chiragsinghal@gmail.com', to, content)
    server.close()


def exitcode():
    sys.exit()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def sp(text):
    print(text)
    speak(text)


def givejoke():
    response_API = requests.get(
        'https://icanhazdadjoke.com/slack')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['attachments']
    joketext = key[0]['text']
    print("The random joke is ", joketext)
    speak(joketext)


def translatelanguage(languageptext):
    query = takeCommand().lower()
    if languageptext in query:
        query = query.replace(languageptext, "")
        k = Translator().translate(query, dest=languageptext)
        translated = str(k.text)
        sp(translated)


def clear():
    return os.system('cls')


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


if __name__ == "__main__":
    # wishMe()

    clear()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        #  if 'olivia' in query:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            sp(results)

        elif 'Call Me' in query:
            speak('What is your name?')
            query = query.replace("call me", "")
            uname = query
            speak('Hello ' + uname + ' How may I help you?')

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query

        elif 'hello' in query:
            speak("hello")
            wishMe()
        elif 'how are you' in query:
            speak("i am fine")

        elif 'what you' in query:
            sp("I am olivia. I Wish you According to the time of the day. I can Open websites like Google ,Youtube ,flipkart ,Stackoverflow. Give you a joke. Search websites like Google ,YouTube. Give the Introduction of someone or something according to wikipedia. Play music. Stop listening. Tell the current time. send email to someone.")

        elif 'wish me' in query:
            wishMe()

        elif 'play video' in query:
            music_dir = 'D:\\non critical\\video'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music' in query or "play song" in query:
            sp("Here you go with music")
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            sp(f"Sir, the time is {strTime}")

        elif 'email to chirag' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chriagsinghal@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend chirag sir. I am not able to send this email")

        elif 'stop music' in query:
            os.close("C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe")

        elif 'search' in query:
            speak('Searching ...')
            query = query.replace("search ", "")
            query = query.replace(" on ", "")

            if 'youtube' in query:
                query = query.replace("youtube", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")

            elif 'flipkart' in query:
                query = query.replace("flipkart", "")
                webbrowser.open(
                    f"https://www.flipkart.com/search?q={query}&otracker1=olivia")
            else:
                query = query.replace("google", "")

                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")

        elif 'open' in query:
            print("opening.....")
            query = query.replace("open ", "")

            if 'edge' in query:
                if 'youtube' in query:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.youtube.com/feed/subscriptions")

            else:
                query = query.replace("website ", "")
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")

        elif 'clear' in query:
            clearConsole()

        elif 'code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            givejoke()

        elif 'kill me' in query:
            sp("I won't")

        elif 'your god' in query:
            sp("chriag singhal is my god")

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Chirag singhal")

        elif 'exit' in query:
            sp("exiting........")
            exitcode()

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'translate' in query:
            query = query.replace("translate", "")
            query = query.replace("to", "")

            if 'spanish' in query:
                query = query.replace("spanish", "")
                k = Translator().translate(query, dest='spanish')
                translated = str(k.text)
                sp(translated)

            elif 'hindi' in query:
                query = query.replace("hindi", "")
                k = Translator().translate(query, dest='hindi')
                translated = str(k.text)
                sp(translated)
            elif 'french' in query:
                query = query.replace("french", "")
                k = Translator().translate(query, dest='french')
                translated = str(k.text)
                sp(translated)
            elif 'german' in query:
                query = query.replace("german", "")
                k = Translator().translate(query, dest='german')
                translated = str(k.text)
                sp(translated)
            elif 'dutch' in query:
                query = query.replace("dutch", "")
                k = Translator().translate(query, dest='dutch')
                translated = str(k.text)
                sp(translated)

            if 'chinese' in query:
                query = query.replace("chinese", "")

                if 'traditional' in query:
                    query = query.replace("traditional", "")
                    query = query.replace("simplified", "")

                    k = Translator().translate(query, dest='chinese (traditional)')
                    translated = str(k.text)
                    sp(translated)

                else:
                    query = query.replace("traditional", "")
                    query = query.replace("simplified", "")
                    k = Translator().translate(query, dest='chinese (simplified)')
                    translated = str(k.text)
                    sp(translated)

""""        


alllanguage = ['afrikaans',
               'albanian',
               'amharic',
               'arabic',
               'armenian',
               'azerbaijani',
               'basque',
               'belarusian',
               'bengali',
               'bosnian',
               'bulgarian',
               'catalan',
               'cebuano',
               'chichewa',
               'corsican',
               'croatian',
               'czech',
               'danish',
               'dutch',
               'english',
               'esperanto',
               'estonian',
               'filipino',
               'finnish',
               'french',
               'frisian',
               'galician',
               'georgian',
               'german',
               'greek',
               'gujarati',
               'haitian creole',
               'hausa',
               'hawaiian',
               'hebrew',
               'hindi',
               'hmong',
               'hungarian',
               'icelandic',
               'igbo',
               'indonesian',
               'irish',
               'italian',
               'japanese',
               'javanese',
               'kannada',
               'kazakh',
               'khmer',
               'korean',
               'kurdish (kurmanji)',
               'kyrgyz',
               'lao',
               'latin',
               'latvian',
               'lithuanian',
               'luxembourgish',
               'macedonian',
               'malagasy',
               'malay',
               'malayalam',
               'maltese',
               'maori',
               'marathi',
               'mongolian',
               'myanmar (burmese)',
               'nepali',
               'norwegian',
               'odia',
               'pashto',
               'persian',
               'polish',
               'portuguese',
               'punjabi',
               'romanian',
               'russian',
               'samoan',
               'scots gaelic',
               'serbian',
               'sesotho',
               'shona',
               'sindhi',
               'sinhala',
               'slovak',
               'slovenian',
               'somali',
               'spanish',
               'sundanese',
               'swahili',
               'swedish',
               'tajik',
               'tamil',
               'telugu',
               'thai',
               'turkish',
               'ukrainian',
               'urdu',
               'uyghur',
               'uzbek',
               'vietnamese',
               'welsh',
               'xhosa',
               'yiddish',
               'yoruba',
               'zulu'
               ]

elif 'youtube' in query:

            webbrowser.open("https://www.youtube.com/")

        elif 'google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")
"""
