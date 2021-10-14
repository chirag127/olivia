import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import requests
import json
from googletrans import Translator


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


if __name__ == "__main__":
    # wishMe()

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

        elif 'hello' in query:
            speak("hello")
            wishMe()
        elif 'how are you' in query:
            speak("i am fine")

        elif 'what you' in query:
            sp("I am olivia. I Wish you According to the time of the day. I can Open websites like Google ,Youtube ,flipkart ,Stackoverflow. Give you a joke. Search websites like Google ,YouTube. Give the Introduction of someone or something according to wikipedia. Play music. Stop listening. Tell the current time. send email to someone.")

        elif 'wish me' in query:
            wishMe()

        elif 'play music' in query:
            music_dir = 'D:\\non critical\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

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

            if 'website' in query:
                query = query.replace("website ", "")
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")

            elif 'edge' in query:

                if 'youtube' in query:

                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.youtube.com/feed/subscriptions")

        elif 'clear' in query:
            clearConsole()

        elif 'bf' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            givejoke()

        elif 'kill me' in query:
            sp("I won't")

        elif 'your god' in query:
            sp("chriag singhal is my god")

        elif 'exit' in query:
            sp("exiting........")
            exitcode()


""""        


elif 'youtube' in query:

            webbrowser.open("https://www.youtube.com/")

        elif 'google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")
"""
