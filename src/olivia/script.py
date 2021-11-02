from typing import Mapping
from bs4 import BeautifulSoup  # pip install bs4
from googletrans import Translator
import ctypes
import datetime
import json
import math
import os
import pyautogui  # pip install pyautogui
import pyttsx3  # pip install pyttsx3
import pywhatkit
import random
import re
import requests
import shutil
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import subprocess
import sys
import time
import tkinter
import urlopen
import webbrowser
import wikipedia  # pip install wikipedia
import win32com.client as wincl
import winshell
import clipboard

# from youtube_video_play_pause_bot import *

import psutil  # pip install psutil


# I was getting error so i install pyaudio
# error in that too so i googled it on the stackover flow.

"""
# Text to Speech Engine
# Define Text to Speech Engine

"""

# create a wonderful virtual voice assistant named olivia and she will help you in your daily life with her amazing features like text to speech, voice to text, google search, wikipedia search, youtube search, news search, weather search, time search, date search, screenshot, email, jokes, ip address, and many more.
# olivia is a virtual voice assistant and she will help you in your daily life with her amazing features like text to speech, voice to text, google search, wikipedia search, youtube search, news search, weather search, time search, date search, screenshot, email, jokes, ip address, and many more.
# Olivia is created by chirag singhal.
# chirag singhal is a software engineer and she is a virtual voice assistant.
# chirag singhal made this virtual voice assistant for his mini-project in his college.


# reqiured engines
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def presskey(key):

    pyautogui.press(key)


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


def cpu():
    usage = psutil.cpu_percent()
    print("CPU is at")
    print(usage)
    speak("CPU is at")
    speak(usage)
    sp("pencentage")


def ram():
    usage = psutil.virtual_memory()
    print("RAM is at")
    print(usage)
    speak("RAM is at")
    speak(usage)


def disk():
    usage = psutil.disk_usage('/')
    sp("Disk is at")
    sp(usage)


def battery():

    sp("Battery is at")
    sp(psutil.sensors_battery())


def query_day():
    day = datetime.datetime.today()
    # print the day of the week
    weekday = day.weekday()

    # print = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    Mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
               3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    try:
        speak("Today is " + Mapping[weekday])
    except:
        pass


def send_whatapp(to, content):
    webbrowser.open('https://web.whatsapp.com/send?phone=' +
                    to + '&text=' + content)
    import time
    time.sleep(20)
    pyautogui.press('enter')


def takescreenshot():
    subprocess.call(["screencapture", "-x", "image.png"])
    speak("Sir, I have taken a screenshot of your screen")
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:\\dl\\Critical\\code\\screenshot_1.png')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chriagsinghal@gmail.com', 'my password')
    server.sendmail('chiragsinghal@gmail.com', to, content)
    server.close()


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def exitcode():
    sys.exit()


def clearConsole():
    command = 'clear'
    speak("Clearing the console")
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def sp(text):
    print(text)
    speak(text)


def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'wassup', 'hello']

    # Greeting response
    GREETING_RESPONSES = ['howdy', 'all that good', 'hello master', 'heythere']

    # If users input is a greeting, then return a randomly chosen greetng response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # If no greeting was detected
    return ''


def givejoke():
    response_API = requests.get(
        'https://icanhazdadjoke.com/slack')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['attachments']
    joketext = key[0]['text']
    print("The random joke is ", joketext)
    speak(joketext)


def giveip():
    response_API = requests.get(
        'https://api.ipify.org?format=json')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['ip']
    iptext = key
    sp("Your IP address is ")
    sp(iptext)


def clear():
    return os.system('cls')


def open_chrome():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('https://www.google.com')


def ctime():
    now = datetime.datetime.now()
    speak("The current time is")
    speak(now.strftime("%I:%M:%S"))


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


def generate_random_password():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*"

    # pass_len=random.randint(8,13)  #without User INput

    pass_len = random.randint(8, 13)

    # length of password by 50-30-20 formula
    alpha_len = pass_len//2
    num_len = math.ceil(pass_len*30/100)
    special_len = pass_len-(alpha_len+num_len)

    password = []

    def generate_pass(length, array, is_alpha=False):
        for i in range(length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
            password.append(character)

    # alpha password
    generate_pass(alpha_len, alpha, True)
    # numeric password
    generate_pass(num_len, num)
    # special Character password
    generate_pass(special_len, special)
    # suffle the generated password list
    random.shuffle(password)
    # convert List To string
    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)
    sp(gen_password)


if __name__ == "__main__":
    # wishMe()
    # clear the console on the start

    while True:

        # take command from user and convert it to lower case and assign it to a variable named as query

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        #  if 'olivia' in query:
        #     speak("Yes Sir")

        # open google chrome if 'chrome' is in query
        if 'open chrome' in query:
            open_chrome()

        # search the wikipedia if 'wikipedia' is in query and speak first 2 sentences of the the wikipedia page

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # tell user the common usage of the command if 'usage' is in query

        elif 'usage' in query:

            # if 'usage' is in query and 'cpu' is in query give the usage of cpu
            if 'cpu' in query:
                cpu()

            # if 'usage' is in query and 'ram' is in query give the usage of ram

            elif 'ram' in query:
                ram()

            # if 'usage' is in query and 'battery' is in query give the usage of battery

            elif 'battery' in query:
                battery()

            # if 'usage' is in query and 'disk' is in query give the usage of disk

            elif 'disk' in query:
                disk()

            # if 'usage' is in query and 'network' is in query give the usage of network

        # search in chrome when the query is 'search'

        elif 'search in chrome' in query:
            speak("What should i search for sir")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open(
                'https://www.google.com/search?q=' + search)

        # if 'time' is in query then tell the time

        elif 'time' in query:
            ctime()

        # if 'joke' is in query then tell the random joke

        elif 'joke' in query:
            givejoke()

        # Read the copied text from clipboard and speak it if 'read' is in query and 'aloud' is in query
        elif 'read' in query:
            if 'aloud' in query:
                text2speech()

# give the current date and time if 'date' is in query
        elif 'date' in query:
            now = datetime.datetime.now()
            speak("The current date is")
            speak(now.strftime("%d-%m-%Y"))

# play the video on the youtube. e.g. play the video on youtube of the song 'song name'
# example: play lonely by justin bieber will play the video of the song 'lonely by justin bieber'

        elif 'play' in query and 'music' in query or 'playlist' in query:
            speak('ok sir enjoy your music')
            spotify_path = 'C:/Users/hp/AppData/Roaming/Spotify/Spotify.exe'
            os.startfile(spotify_path)
            time.sleep(1)
            pyautogui.click(button='left')
            pyautogui.press('space')
            pyautogui.hotkey('alt', 'f4')
            while not 'wake up' in wakeup_txt:
                wakeup_txt = time.sleep()
                if wakeup_txt == 'quit':
                    speak('bye bye sir. have a great day')
                    running = False
                    sys.exit()
                elif 'pause' in wakeup_txt or 'play' in wakeup_txt:
                    os.system('spotify')
                    time.sleep(1)
                    pyautogui.press('space')
                    pyautogui.hotkey('alt', 'f4')
                elif 'close spotify' in wakeup_txt:
                    os.system('TASKKILL /F /IM Spotify.exe')
            speak('hello again sir')

        elif 'play' in query:
            song = query.replace('play', '')
            sp('playing ')
            sp(song)
            pywhatkit.playonyt(song)
            query = query.replace('play', '')

            while True:
                query = takeCommand().lower()
                # pause the video if 'pause' is in query
                if 'pause' in query:
                    presskey('space')
                   # sp('paused')

                elif 'play' in query:
                    presskey('space')
                   # sp('playing')

                elif 'stop' in query:
                    presskey('space')
                    # sp('stopped')

                elif 'next' in query:
                    pyautogui.hotkey('shift', 'n')
                   # sp('Gone to the next video')

                # previous the video if 'previous' is in query
                elif 'previous' in query:
                    pyautogui.hotkey('shift', 'p')
                   # sp('Gone to the previous video')

                # mute the video if 'mute' is in query
                elif 'mute' in query:
                    presskey('m')
                  #  sp('muted the video')

                # unmute the video if 'unmute' is in query
                elif 'unmute' in query:
                    presskey('m')
                    #sp('unmuted the video')

                # Increase the volume if 'volume up' is in query
                elif 'volume up' in query:
                    presskey('up')
                 ##   sp('Increased the volume')

                # Decrease the volume if 'volume down' is in query
                elif 'volume down' in query:
                    presskey('down')
                  #  sp('Decreased the volume')

                # close the video if 'close' is in query
                elif 'close' in query:
                    pyautogui.hotkey('ctrl', 'w')
                    # sp('Closed the video')
                    break

        elif 'news for today' in query:
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "xml")
                news_list = soup_page.findAll("item")

                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
                    print(news.title.text.encode('utf-8'))
                    speak("Moving on...")
                    print("Moving on...")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to fetch news")

        elif 'generate' in query:
            if 'password' in query:
                generate_random_password()
            elif 'number' in query:
                sp(random.randint(0, 100))

        elif 'call me' in query:
            speak('What is your name?')
            query = query.replace("call me", "")
            uname = query
            speak('Hello ' + uname + ' How may I help you?')

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "chriagsinghal@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(
                    "Sorry my friend chirag sir. I am not able to send this email")

        elif 'lock window' in query or 'lock screen' in query or 'lock the screen' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shut down the computer' in query or 'shutdown the computer' in query or 'shot down the computer' in query or 'shutdown system' in query:
            speak("Hold On ! Your system is on its way to shut down")
            os.system('shutdown /s /f')
            running = False
            sys.exit()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop olivia from listening commands")
            time.sleep(120)
            speak("Olivia is listening again")

        elif "restart" in query or "reboot" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "note" in query or "notes" in query:
            if 'read' in query:
                speak("Reading Note Sir")
                file = open('olivianote.txt', 'r')
                print(file.read())
                speak(file.read(6))

            elif 'write' in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('olivianote.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()

                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%m-%d-%Y %T:%M%p")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write("\n")
                    file.write(note)
                    speak("Note has been saved")
                else:
                    file.write(note)
                    speak("Note has been saved without date and time")

            elif "show" in query:
                speak("Showing Notes")
                file = open("olivianote.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "delete" in query:
                speak("Deleting Note")
                file = open("olivianote.txt", "w")
                file.truncate()
                speak("Note has been deleted")

        elif "send" in query:

            # send whatsapp message
            if 'message' in query:
                username = {
                    'chirag': '+91 9999999999',
                    'india': '+91 9999999998',
                    'abhinav': '+91 9999999997',
                    'ram': '+91 9999999996',
                    'shivam': '+91 9999999995',
                    'saurabh': '+91 9999999994',
                    'sahil': '+91 9999999993',
                    'siddharth': '+91 9999999992',
                    'sagar': '+91 9999999991',
                    'shubham': '+91 9999999990',
                    'shivani': '+91 9999999989',
                    'shivam': '+91 9999999988',
                    'shubham': '+91 9999999987',
                    'shivam': '+91 9999999986',
                    'shivam': '+91 9999999985',
                    'shivam': '+91 9999999984',
                    'sourya': '+91 9999999983',
                    'sourya': '+91 9999999982',
                    'aryan': '+91 9999999981',
                    'aviral': '+91 9999999980',
                    'kushi': '+91 9999999979',
                    'kushal': '+91 9999999978',
                    'jatin': '+91 9999999977',


                    'None': '+91 9999999995'  # if you want to add more contacts
                    # 'None' : '+91 9999999995' # if you want to add more contacts
                    # 'None' : '+91 9999999995' # if you want to default contact


                }
                try:
                    speak("to whom should i send to?")
                    name = takeCommand().lower()
                    to = username[name]
                    speak("What should i say?")
                    content = takeCommand()
                    send_whatapp(to, content)
                    speak("Message has been sent")

                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this message")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            sp("User asked to Locate")
            sp(location)
            webbrowser.open(
                "https://www.google.com / maps / place/" + location + "")

# tell the stock price of the company using yahoo finance api and speak the result to the user using google speech api and print the result to the console
        elif "stock" in query:
            if 'price' in query:
                speak("What company's stock price you want to check?")
                company = takeCommand()
                speak("Checking the stock price of " + company)
                try:
                    url = "https://in.finance.yahoo.com/quote/" + company + "?p=" + company
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    price = soup.find(
                        "div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").get_text()
                    sp(price)
                    print(price)
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to fetch the stock price")
# tell the weather of the city using openweathermap api and speak the result to the user using google speech api and print the result to the console
        elif "weather" in query:
            if 'today' in query:
                speak("What city's weather you want to check?")
                city = takeCommand()
                speak("Checking the weather of " + city)
                try:
                    url = "https://openweathermap.org/data/2.5/weather?q=" + \
                        city + "&appid=b6907d289e10d714a6e88b30761fae22"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    weather = soup.find(
                        "div", {"class": "weather-widget__container"}).find("p").get_text()
                    sp(weather)
                    print(weather)
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to fetch the weather")

        elif "date" in query:
            speak("Sir, What date you want to check")
            date = takeCommand()
            speak("Checking the date of " + date)
            try:
                url = "https://www.timeanddate.com/worldclock/fixedtime.html?msg=" + date + "&iso=&p1=150"
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                date = soup.find(
                    "div", {"class": "time-date"}).find("p").get_text()
                sp(date)
                print(date)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to fetch the date")

        elif "calculate" in query:
            speak("Sir, What you want to calculate")
            query = takeCommand()
            speak("Calculating " + query)
            try:
                url = "https://www.google.com/search?q=" + query
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(
                    "div", {"class": "kno-ecr-pt"}).find("span").get_text()
                sp(result)
                print(result)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to fetch the result")

# tell the user the current time using datetime module and speak the result to the user using google speech api and print the result to the console
        elif "current time" in query:
            speak("Sir, What time you want to check")
            time = takeCommand()
            speak("Checking the time of " + time)
            try:
                url = "https://www.timeanddate.com/worldclock/fixedtime.html?msg=" + time + "&iso=&p1=150"
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                time = soup.find(
                    "div", {"class": "time-date"}).find("p").get_text()
                sp(time)
                print(time)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to fetch the time")

        elif 'search' in query:
            sp('Searching ...')
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

            elif 'google' in query:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjNy7Ph39ndAhXGFYgKHcc8D_AQ_AUoAXoECAsQAw&biw=1366&bih=657")

            elif 'stack overflow' in query:
                query = query.replace("stack overflow", "")
                webbrowser.open(
                    f"https://stackoverflow.com/search?q={query}")

            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                webbrowser.open(
                    f"https://en.wikipedia.org/wiki/{query}")

            elif 'facebook' in query:
                query = query.replace("facebook", "")
                webbrowser.open(
                    f"https://www.facebook.com/search/top/?q={query}")  # facebook

            elif 'instagram' in query:
                query = query.replace("instagram", "")
                webbrowser.open(
                    f"https://www.instagram.com/{query}")

            elif 'twitter' in query:
                query = query.replace("twitter", "")
                webbrowser.open(
                    f"https://www.twitter.com/{query}")

            elif 'linkedin' in query:
                query = query.replace("linkedin", "")
                webbrowser.open(
                    f"https://www.linkedin.com/in/{query}")

            elif 'google' in query:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}")

            elif 'amazon' in query:
                query = query.replace("amazon", "")
                webbrowser.open(
                    f"https://www.amazon.in/s?k={query}")

            elif 'ebay' in query:
                query = query.replace("ebay", "")
                webbrowser.open(
                    f"https://www.ebay.com/sch/i.html?_nkw={query}")

            elif 'netflix' in query:
                query = query.replace("netflix", "")
                webbrowser.open(
                    f"https://www.netflix.com/search?q={query}")

            elif 'spotify' in query:
                query = query.replace("spotify", "")
                webbrowser.open(
                    f"https://open.spotify.com/search/{query}")

            elif 'snapchat' in query:
                query = query.replace("snapchat", "")
                webbrowser.open(
                    f"https://www.snapchat.com/search/{query}")

            elif 'pinterest' in query:
                query = query.replace("pinterest", "")
                webbrowser.open(
                    f"https://www.pinterest.com/search/{query}")

            elif 'quora' in query:
                query = query.replace("quora", "")
                webbrowser.open(
                    f"https://www.quora.com/{query}")

            elif 'duckduckgo' in query:
                query = query.replace("duckduckgo", "")
                webbrowser.open(
                    f"https://duckduckgo.com/?q={query}")

            elif 'bing' in query:
                query = query.replace("bing", "")
                webbrowser.open(
                    f"https://www.bing.com/search?q={query}")

            elif 'yahoo' in query:
                query = query.replace("yahoo", "")
                webbrowser.open(
                    f"https://search.yahoo.com/search?p={query}")

            else:
                query = query.replace("google", "")

                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")

        elif 'open word' in query:
            speak('ok. opening word')
            os.startfile(
                'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
            speak('do you want me to type sir?')
            typin = takeCommand()
            if 'yes' in typin:
                pyautogui.press('enter')
                speak('sir you can start. say stop typing if I have to stop')
                while True:
                    type_sentence = takeCommand()
                    if 'stop typing' in type_sentence:
                        break
                    elif 'enter' in type_sentence:
                        pyautogui.press('enter')
                    else:
                        pyautogui.typewrite(type_sentence)
                speak('stopped typing')
            elif 'no' in typin:
                speak('ok sir')
        elif 'stop typing' in query:
            speak('sir I already stopped typing')

        elif 'launch' in query:
            query = query.replace("launch", "")
            sp("Launching ")
            sp(query)

            if 'control panel' in query:
                speak("okay")
                os.system("control")

            elif 'quick assist' in query:
                speak("okay")
                os.system("quickassist")

            elif 'game panel' in query:
                speak("okay")
                os.system("gamepanel")

            elif 'edge' in query:
                if 'youtube' in query:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.youtube.com/feed/subscriptions")

                else:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.google.com/")

            elif 'chrome' in query:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif 'notepad' in query:
                notepadPath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(notepadPath)

            elif 'calculator' in query:
                calculatorPath = "C:\\Windows\\System32\\calc.exe"
                os.startfile(calculatorPath)

            elif 'task manager' in query:
                taskManagerPath = "C:\\Windows\\System32\\taskmgr.exe"
                os.startfile(taskManagerPath)

            elif 'excel' in query:
                speak("okay")
                excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(excelPath)

            elif 'powerpoint' in query:
                speak("okay")
                powerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(powerpointPath)

            elif 'paint' in query:
                speak("okay")
                paintPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(paintPath)

            elif 'camera' in query:
                speak("okay")
                cameraPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(cameraPath)

            elif 'media player' in query:
                speak("okay")
                mediaPlayerPath = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
                os.startfile(mediaPlayerPath)

            elif 'setting' in query:
                speak("okay")
                settingPath = "C:\\Windows\\System32\\control.exe"
                os.startfile(settingPath)

            elif 'wordpad' in query:
                speak("okay")
                wordpadPath = "C:\\Windows\\System32\\wordpad.exe"
                os.startfile(wordpadPath)

            elif 'calculator' in query:

                speak("okay")
                calculatorPath = "C:\\Windows\\System32\\calc.exe"
                os.startfile(calculatorPath)

            elif 'mspaint' in query:
                speak("okay")
                mspaintPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(mspaintPath)

            elif 'chrome' in query:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif 'sublime text' in query:
                sublimeTextPath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(sublimeTextPath)

            elif 'pycharm' in query:
                pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
                os.startfile(pycharmPath)

            elif 'notepad++' in query:
                notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(notepadPath)

            elif 'vlc' in query:
                vlcPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                os.startfile(vlcPath)

            elif 'pot player' in query:
                potPlayerPath = "C:\\Program Files\\PotPlayer\\PotPlayerMini64.exe"
                os.startfile(potPlayerPath)

            elif 'github desktop' in query:
                githubPath = "C:\\Users\\hp\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
                os.startfile(githubPath)

            elif 'treesize free' in query:
                treesizefreePath = "C:\\Program Files\\TreesizeFree\\TreesizeFree.exe"
                os.startfile(treesizefreePath)

            elif 'microsoft store' in query:
                microsoftStorePath = "C:\\Program Files\\Microsoft Store\\Microsoft Store.exe"
                os.startfile(microsoftStorePath)

            elif 'microsoft edge' in query:
                microsoftEdgePath = "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoftEdgePath)

            elif 'microsoft mail' in query:
                microsoftMailPath = "C:\\Program Files\\Microsoft\\Windows Live Mail\\wlmail.exe"
                os.startfile(microsoftMailPath)

            elif 'microsoft office' in query:
                microsoftOfficePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(microsoftOfficePath)

            elif 'microsoft excel' in query:

                microsoftExcelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(microsoftExcelPath)

            elif 'microsoft powerpoint' in query:
                microsoftPowerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(microsoftPowerpointPath)

            elif 'spotify' in query:
                spotifyPath = "C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(spotifyPath)

            else:
                try:
                    reg_ex = re.search('launch (.*)', query)
                    if reg_ex:
                        appname = reg_ex.group(1)
                        appname1 = appname+".exe"
                        subprocess.Popen(
                            ["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
                        sp('I have launched the desired application')
                except:
                    sp('I am not sure what application you want to launch')

        elif 'open' in query:
            query = query.replace("open", "")

            if 'firefox' in query:
                sp("Firefox is opening")
                webbrowser.open(
                    "https://www.mozilla.org/en-US/firefox/new/")

            elif 'youtube' in query:
                speak("Youtube is opening")
                webbrowser.open("https://www.youtube.com/")

            elif 'facebook' in query:
                speak("Facebook is opening")
                webbrowser.open("https://www.facebook.com/")

            elif 'whatsapp' in query:
                speak("Whatsapp is opening")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'instagram' in query:
                speak("Instagram is opening")
                webbrowser.open("https://www.instagram.com/")

            elif 'twitter' in query:
                speak("Twitter is opening")
                webbrowser.open("https://twitter.com/")

            elif 'linkedin' in query:
                speak("Linkedin is opening")
                webbrowser.open("https://www.linkedin.com/")

            elif 'pinterest' in query:
                speak("Pinterest is opening")
                webbrowser.open("https://www.pinterest.com/")

            elif 'quora' in query:
                speak("Quora is opening")
                webbrowser.open("https://www.quora.com/")

            elif 'amazon' in query:
                speak("Amazon is opening")
                webbrowser.open("https://www.amazon.in/")

            elif 'ebay' in query:
                speak("Ebay is opening")
                webbrowser.open("https://www.ebay.com/")

            elif 'netflix' in query:
                speak("Netflix is opening")
                webbrowser.open("https://www.netflix.com/")

            elif 'spotify' in query:
                speak("Spotify is opening")
                webbrowser.open("https://open.spotify.com/")

            elif 'snapchat' in query:

                speak("Snapchat is opening")
                webbrowser.open("https://www.snapchat.com/")

            elif 'gmail' in query:
                speak("Gmail is opening")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'google' in query:
                speak("Google is opening")
                webbrowser.open("https://www.google.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'flipkart' in query:
                webbrowser.open("https://www.flipkart.com/")

            elif 'hackerearth' in query:
                webbrowser.open("https://www.hackerearth.com/")

            elif 'bing' in query:
                webbrowser.open("https://www.bing.com/")

            elif 'duckduckgo' in query:
                webbrowser.open("https://duckduckgo.com/")

            elif 'github' in query:
                webbrowser.open("https://www.github.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'wikipedia' in query:
                webbrowser.open("https://www.wikipedia.org/")

            elif 'quora' in query:
                webbrowser.open("https://www.quora.com/")

            elif 'reddit' in query:
                if 'reddit' in query:
                    reg_ex = re.search('reddit (.*)', query)
                    url = 'https://www.reddit.com/'
                    if reg_ex:
                        subreddit = reg_ex.group(1)
                        url = url + 'r/' + subreddit
                    webbrowser.open(url)
                    sp('The Reddit content has been opened for you Sir.')

                else:
                    webbrowser.open("https://www.reddit.com/")

            else:
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")

        elif "what is your name" in query:
            speak("My name is Olivia")

        elif "what is your age" in query:
            speak("I am a computer program")

        elif "what is your job" in query:
            speak("I am a Virtual assistant")

        elif "what is your favorite food" in query:
            speak("I Like renewable electricity")

        elif "what is your favorite animal" in query:
            speak("I like dogs")

        elif "what is your favorite sport" in query:
            speak("I like cricket")

        elif "what is your favorite color" in query:
            speak("My favorite color is black")

        elif "what is your favorite song" in query:
            speak("My favorite song is the one by the Justin bieber")

        elif "what is your favorite movie" in query:
            speak("My favorite movie is the dead poet Society")

        elif "what is your favorite actor" in query:
            speak("My favorite actor is Alex Lawther")

        elif "what is your favorite actress" in query:
            speak("My favorite actress is Jessica Barden")

        elif "what is your favorite cartoon" in query:
            speak("My favorite cartoon is the one by the Tom and Jerry")

        elif "what is your favorite cartoon character" in query:
            speak("My favorite cartoon character is Jerry")

        elif "what is your favorite book" in query:
            speak("My favorite book is Automate the boring stuff")
            speak("I also like the books by the author of the book The Alchemist")

        elif "what is your favorite place" in query:
            speak("My favorite place is Ghaziabad")

        elif "thank you" in query:
            speak("Welcome Sir")

        elif "who are you" in query:
            speak("I am a Virtual assistant")

        elif "who made you" in query:
            speak("I was created by Chirag singhal")

        elif "who is your creator" in query:
            speak("I was created by Chirag singhal")

        elif "who made you" in query:
            speak("I was made by Chirag singhal")

        elif "what is your country of origin" in query:
            speak("I was made in India")

        elif "what is your language" in query:
            speak("I am a computer program")

        elif "what is your purpose" in query:

            speak("I am a Virtual assistant")
        elif query == "hello" or query == "hi" or query == "hey" or query == "hii":
            speak("Hello Sir")  # Hello Sir
            wishMe()

        elif 'how are you' in query:
            speak("i am fine")
        elif 'what time is it' in query:
            speak(ctime())
        elif 'who are you' in query:
            speak("i am olivia")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'kill me' in query:
            sp("I won't")

        elif 'your god' in query:
            sp("chriag singhal is my god")

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Chirag singhal")
        elif 'what you can do' in query:
            speak("I can do many things")

        elif 'wish me' in query:
            wishMe()
        elif 'roll' in query and 'dice' in query:
            r = random.randint(1, 6)
            dice = str(r)
            speak('you got ' + dice)
        elif 'who is' in query:
            query = query.replace("who is", "")
            k = wikipedia.summary(query, sentences=2)
            speak(k)
        elif 'tell me about' in query:
            query = query.replace("tell me about", "")
            k = wikipedia.summary(query, sentences=2)
            speak(k)

        elif query == 'quit' or 'olivia quit' in query or 'olivia bye' in query or query == 'bye' or query == 'exit' or query == 'close' or query == 'goodbye' or query == 'bye bye':
            sp("Bye Sir")
            exit()

        elif 'close chrome' in query or 'close google chrome' in query:
            speak("closing chrome")
            os.system("TASKKILL /F /IM chrome.exe")

            # close spotify
        elif 'close spotify' in query:
            speak("closing spotify")
            os.system("TASKKILL /F /IM spotify.exe")


# create a translate feature in the virutal assistant
        elif 'translate' in query:
            query = query.replace("translate", "")

            # translate to arabic
            if 'to arabic' in query:
                query = query.replace("to arabic", "")
                translator = Translator()
                result = translator.translate(query, dest='ar')
                sp(result.text)
                # translate to bengali
            elif 'to bengali' in query:
                query = query.replace("to bengali", "")
                translator = Translator()
                result = translator.translate(query, dest='bn')
                sp(result.text)

                # translate to bulgarian
            elif 'to bulgarian' in query:
                query = query.replace("to bulgarian", "")
                translator = Translator()
                result = translator.translate(query, dest='bg')
                sp(result.text)

                # translate to catalan

            elif 'to catalan' in query:
                query = query.replace("to catalan", "")
                translator = Translator()
                result = translator.translate(query, dest='ca')
                sp(result.text)

                # translate to chinese

            elif 'to chinese' in query:
                query = query.replace("to chinese", "")
                translator = Translator()
                result = translator.translate(query, dest='zh-cn')
                sp(result.text)

                # translate to croatian

            elif 'to croatian' in query:
                query = query.replace("to croatian", "")
                translator = Translator()
                result = translator.translate(query, dest='hr')
                sp(result.text)

                # translate to czech

            elif 'to czech' in query:
                query = query.replace("to czech", "")
                translator = Translator()
                result = translator.translate(query, dest='cs')
                sp(result.text)

                # translate to danish

            elif 'to danish' in query:
                query = query.replace("to danish", "")
                translator = Translator()
                result = translator.translate(query, dest='da')
                sp(result.text)

                # translate to dutch

            elif 'to dutch' in query:
                query = query.replace("to dutch", "")
                translator = Translator()
                result = translator.translate(query, dest='nl')
                sp(result.text)

                # translate to estonian

            elif 'to estonian' in query:
                query = query.replace("to estonian", "")
                translator = Translator()
                result = translator.translate(query, dest='et')
                sp(result.text)

                # translate to finnish

            elif 'to finnish' in query:
                query = query.replace("to finnish", "")
                translator = Translator()
                result = translator.translate(query, dest='fi')
                sp(result.text)

                # translate to greek

            elif 'to greek' in query:

                query = query.replace("to greek", "")
                translator = Translator()
                result = translator.translate(query, dest='el')
                sp(result.text)

                # translate to hebrew

            elif 'to hebrew' in query:
                query = query.replace("to hebrew", "")
                translator = Translator()
                result = translator.translate(query, dest='he')
                speak(result.text)

                # translate to hindi

            elif 'to hindi' in query:
                query = query.replace("to hindi", "")
                translator = Translator()
                result = translator.translate(query, dest='hi')
                speak(result.text)

                # translate to hungarian

            elif 'to hungarian' in query:
                query = query.replace("to hungarian", "")
                translator = Translator()
                result = translator.translate(query, dest='hu')
                speak(result.text)

                # translate to indonesian

            elif 'to indonesian' in query:
                query = query.replace("to indonesian", "")
                translator = Translator()
                result = translator.translate(query, dest='id')
                speak(result.text)

                # translate to italian

            elif 'to italian' in query:

                query = query.replace("to italian", "")
                translator = Translator()
                result = translator.translate(query, dest='it')
                speak(result.text)

                # translate to japanese

            elif 'to japanese' in query:
                query = query.replace("to japanese", "")
                translator = Translator()
                result = translator.translate(query, dest='ja')
                speak(result.text)

                # translate to korean

            elif 'to korean' in query:
                query = query.replace("to korean", "")
                translator = Translator()
                result = translator.translate(query, dest='ko')
                speak(result.text)

                # translate to chinese

            elif 'to chinese' in query:
                query = query.replace("to chinese", "")
                translator = Translator()
                result = translator.translate(query, dest='zh-cn')
                sp(result.text)

                # translate to portuguese

            elif 'to portuguese' in query:
                query = query.replace("to portuguese", "")
                translator = Translator()
                result = translator.translate(query, dest='pt')
                sp(result.text)

                # translate to latvian

            elif 'to latvian' in query:
                query = query.replace("to latvian", "")
                translator = Translator()
                result = translator.translate(query, dest='lv')
                sp(result.text)

                # translate to lithuanian

            elif 'to lithuanian' in query:
                query = query.replace("to lithuanian", "")
                translator = Translator()
                result = translator.translate(query, dest='lt')
                sp(result.text)

                # translate to malay

            elif 'to malay' in query:
                query = query.replace("to malay", "")
                translator = Translator()
                result = translator.translate(query, dest='ms')
                sp(result.text)

                # translate to norwegian

            elif 'to norwegian' in query:
                query = query.replace("to norwegian", "")
                translator = Translator()
                result = translator.translate(query, dest='no')
                sp(result.text)

                # translate to persian

            elif 'to persian' in query:
                query = query.replace("to persian", "")
                translator = Translator()
                result = translator.translate(query, dest='fa')
                sp(result.text)

                # translate to polish

            elif 'to polish' in query:
                query = query.replace("to polish", "")
                translator = Translator()
                result = translator.translate(query, dest='pl')
                sp(result.text)

                # translate to portuguese

            elif 'to portuguese' in query:
                query = query.replace("to portuguese", "")
                translator = Translator()
                result = translator.translate(query, dest='pt')
                sp(result.text)

                # translate to romanian

            elif 'to romanian' in query:
                query = query.replace("to romanian", "")
                translator = Translator()
                result = translator.translate(query, dest='ro')
                sp(result.text)

                # translate to russian

            elif 'to russian' in query:
                query = query.replace("to russian", "")
                translator = Translator()
                result = translator.translate(query, dest='ru')
                sp(result.text)
                # translate to slovak

            elif 'to slovak' in query:
                query = query.replace("to slovak", "")
                translator = Translator()
                result = translator.translate(query, dest='sk')
                sp(result.text)

                # translate to spanish

            elif 'to spanish' in query:
                query = query.replace("to spanish", "")
                translator = Translator()
                result = translator.translate(query, dest='es')
                sp(result.text)
                # translate to swedish

            elif 'to swedish' in query:
                query = query.replace("to swedish", "")
                translator = Translator()
                result = translator.translate(query, dest='sv')
                sp(result.text)

                # translate to thai

            elif 'to thai' in query:
                query = query.replace("to thai", "")
                translator = Translator()
                result = translator.translate(query, dest='th')
                sp(result.text)

                # translate to turkish

            elif 'to turkish' in query:
                query = query.replace("to turkish", "")
                translator = Translator()
                result = translator.translate(query, dest='tr')
                sp(result.text)

                # translate to ukrainian

            elif 'to ukrainian' in query:
                query = query.replace("to ukrainian", "")
                translator = Translator()
                result = translator.translate(query, dest='uk')
                sp(result.text)

                # translate to urdu

            elif 'to urdu' in query:
                query = query.replace("to urdu", "")
                translator = Translator()
                result = translator.translate(query, dest='ur')
                sp(result.text)

                # translate to vietnamese

            elif 'to vietnamese' in query:
                query = query.replace("to vietnamese", "")
                translator = Translator()
                result = translator.translate(query, dest='vi')
                sp(result.text)

            # translate to hindi
            elif 'to hindi' in query:
                query = query.replace("to hindi", "")
                translator = Translator()
                result = translator.translate(query, dest='hi')
                sp(result.text)

            # translate to marathi
            elif 'to marathi' in query:
                query = query.replace("to marathi", "")
                translator = Translator()
                result = translator.translate(query, dest='mr')
                sp(result.text)

            # translate to tamil

            elif 'to tamil' in query:
                query = query.replace("to tamil", "")
                translator = Translator()
                result = translator.translate(query, dest='ta')
                sp(result.text)

            # translate to telugu
            elif 'to telugu' in query:

                query = query.replace("to telugu", "")
                translator = Translator()
                result = translator.translate(query, dest='te')
                sp(result.text)

            # translate to malayalam
            elif 'to malayalam' in query:
                query = query.replace("to malayalam", "")
                translator = Translator()
                result = translator.translate(query, dest='ml')
                sp(result.text)

            # translate to punjabi
            elif 'to punjabi' in query:
                query = query.replace("to punjabi", "")
                translator = Translator()
                result = translator.translate(query, dest='pa')
                sp(result.text)

            # translate to gujarati
            elif 'to gujarati' in query:
                query = query.replace("to gujarati", "")
                translator = Translator()
                result = translator.translate(query, dest='gu')
                sp(result.text)

            # translate to kannada
            elif 'to kannada' in query:
                query = query.replace("to kannada", "")
                translator = Translator()
                result = translator.translate(query, dest='kn')
                sp(result.text)

            # translate to malayalam
            elif 'to malayalam' in query:
                query = query.replace("to malayalam", "")
                translator = Translator()
                result = translator.translate(query, dest='ml')
                sp(result.text)

        elif 'close' in query:
            if 'tab' in query or 'this page' in query or 'tabs' in query:
                pyautogui.hotkey('ctrl', 'w')
               # sp('Closed')

            elif'app' in query or 'application' in query or 'program' in query or 'process' in query or 'window' in query or 'all tabs' in query:
                pyautogui.hotkey('alt', 'f4')
               # sp('Closed')

        elif 'clear' in query:
            clearConsole()

        elif 'exit' in query:
            exitcode()

        elif 'screenshot' in query:
            takescreenshot()

        elif 'joke' in query:
            givejoke()

        elif 'ip address' in query:
            giveip()

        elif 'username' in query:
            username()


"""


        else:
            speak(
                'sorry sir that is not assigned. do you want to search for ' + query + '?')
            confirmation = takeCommand().lower()
            if 'yes' in confirmation:
                speak('do you want me to search in google, wikipedia or youtube sir?')
                answer4 = takeCommand().lower()
                if 'google' in answer4:
                    speak('searching for ' + query + ' in google')
                    webbrowser.open('www.google.com/search?gx&q=' + query)

                elif 'Wikipedia' in answer4:
                    speak('do you want me to narrate or open webpage sir?')
                    answer2 = takeCommand().lower()
                    if 'narrate' in answer2 or 'direct' in answer2:
                        results = wikipedia.summary(
                            query, sentences=1, auto_suggest=False)
                        speak('according to wikipedia ' + results)
                    elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                        page1 = wikipedia.page(query, auto_suggest=False)
                        print(page1)
                        page2 = page1.url
                        print(page2)
                        speak('redirecting to webpage')
                        webbrowser.get().open_new_tab(page2)
                        print(page2)
                elif 'youtube' in answer4:
                    speak('searching for ' + query + 'in youtube')
                    webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + query)
            else:
                speak('ok. anything else sir?')
"""
