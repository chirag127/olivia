from pyowm import OWM  # import the library owm from pyowm for weather api
from bs4 import BeautifulSoup  # BeautifulSoup is used for web scraping
# googletrans is used for translation and google translate is used for language detection
from googletrans import Translator
from tkinter import *
import clipboard  # clipboard is used to read the text from the clipboard
import ctypes  # ctypes is used maniplulate the data types
import datetime  # date and time module is for timezones
import json  # json library is used for reading and writing json files obtained by apis
import math  # math library provides math fuctions .
import numpy as np
import os  # os library is used to open the system and open the specified file
import psutil  # pip install psutil # psutil is used to get the cpu usage and ram usage and disk usage and battery usage
import pyautogui  # pyaoautogui is used for mouse and keyboard control
import pyttsx3  # pyttx3 is used for text to speech
import pywhatkit  # pywhatkit is used for playing the youtube videos
import random  # random library is used for random number generation
import re  # regular expression library is used for regular expressions
import requests  # requests library is used to make http requests to apis
import shutil  # shutil is used to copy files and folders from one location to another location or for archiving files and folders
import smtplib  # smtplib is used for sending emails
# spech_recognition library is used for speech recognition and google translate is used for language detection
import speech_recognition as sr
import subprocess  # subprocess is used to run the command line commands for screen capture
import sys  # sys library is used to exit the program
import time  # time library is used for timezones
import tkinter as tk
import urlopen  # used to open url
import webbrowser  # webbrowser is used to open the url in the default browser
import wikipedia  # get article from wikipedia
import win32com.client as wincl
import winshell
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
# sapi5 is the default voice engine of windows and it is installed by default in windows
# getproperties is used to get the properties of the engine like rate, volume, pitch, etc.
voices = engine.getProperty('voices')
# setproperties is used to set the properties of the engine like rate, volume, pitch, etc.
engine.setProperty('voice', voices[1].id)
# defining the function to speak the text


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# defining the function to take command from the user


def takeCommand():
    # create a recognizer object
    r = sr.Recognizer()
    # use the microphone as source for input
    with sr.Microphone() as source:
        # print listening to the user to know that the program is listening
        print("Listening...")
        # refer to the https://www.codesofinterest.com/2017/04/energy-threshold-calibration-in-speech-recognition.html to understand the energy threshold

        # pause for a second to let the recognizer adjust the threshold before listening for input
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        # r.dynamic_energy_threshold = True
        # r.energy_threshold = 800
        # r.dynamic_energy_adjustment_damping = 0.2
        # listen for the user's input and store it in audio variable and convert it to text later
        audio = r.listen(source)
    try:
        # convert the audio to text
        # print recongzing the user's voice to know that the program is re cognizing the user's voice
        print("Recognizing...")
        # use google translate to detect the language of the user's voice
        query = r.recognize_google(audio, language='en-in')

        # print the user's voice to the console
        print(f"User said: {query}\n")
    # if the user does not say anything then the program will listen again
    except Exception as e:
        # print the error to the console
        print("Say that again please...")
        # return the function to takeCommand()
        return "None"
    # return the function to takeCommand()
    return query


# fuction of press the specified key


def presskey(key):

    pyautogui.press(key)


def presshotkey(key1, key2):
    pyautogui.hotkey(key1, key2)

#  function to wish the user according to the time of the day and the day of the week


def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        print(i + 1, results[i])
        speak(results[i])


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        # if time is between 0 and 12 then say good morning

    elif hour >= 12 and hour < 18:  # if time is between 12 and 18 then say good afternoon
        speak("Good Afternoon!")

    else:  # if time is between 18 and 24 then say good evening
        speak("Good Evening!")

    # tell the user how may i help you
    speak("I am olivia Sir. Please tell me how may I help you")

# It will take microphone input from the user and return string output


def tictactoe():
    size_of_board = 600
    symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
    symbol_thickness = 50
    symbol_X_color = '#EE4035'
    symbol_O_color = '#0492CF'
    Green_color = '#7BC043'

    class Tic_Tac_Toe():
        # ------------------------------------------------------------------
        # Initialization Functions:
        # ------------------------------------------------------------------
        def __init__(self):
            self.window = Tk()
            self.window.title('Tic-Tac-Toe')
            self.canvas = Canvas(
                self.window, width=size_of_board, height=size_of_board)
            self.canvas.pack()
            # Input from user in form of clicks
            self.window.bind('<Button-1>', self.click)

            self.initialize_board()
            self.player_X_turns = True
            self.board_status = np.zeros(shape=(3, 3))

            self.player_X_starts = True
            self.reset_board = False
            self.gameover = False
            self.tie = False
            self.X_wins = False
            self.O_wins = False

            self.X_score = 0
            self.O_score = 0
            self.tie_score = 0

        def mainloop(self):
            self.window.mainloop()

        def initialize_board(self):
            for i in range(2):
                self.canvas.create_line(
                    (i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

            for i in range(2):
                self.canvas.create_line(
                    0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

        def play_again(self):
            self.initialize_board()
            self.player_X_starts = not self.player_X_starts
            self.player_X_turns = self.player_X_starts
            self.board_status = np.zeros(shape=(3, 3))

        # ------------------------------------------------------------------
        # Drawing Functions:
        # The modules required to draw required game based object on canvas
        # ------------------------------------------------------------------

        def draw_O(self, logical_position):
            logical_position = np.array(logical_position)
            # logical_position = grid value on the board
            # grid_position = actual pixel values of the center of the grid
            grid_position = self.convert_logical_to_grid_position(
                logical_position)
            self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    outline=symbol_O_color)

        def draw_X(self, logical_position):
            grid_position = self.convert_logical_to_grid_position(
                logical_position)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)

        def display_gameover(self):

            if self.X_wins:
                self.X_score += 1
                text = 'Winner: Player 1 (X)'
                color = symbol_X_color
            elif self.O_wins:
                self.O_score += 1
                text = 'Winner: Player 2 (O)'
                color = symbol_O_color
            else:
                self.tie_score += 1
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(
                size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                    text=score_text)

            score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
            score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
            score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                    text=score_text)

        # ------------------------------------------------------------------
        # Logical Functions:
        # The modules required to carry out game logic
        # ------------------------------------------------------------------

        def convert_logical_to_grid_position(self, logical_position):
            logical_position = np.array(logical_position, dtype=int)
            return (size_of_board / 3) * logical_position + size_of_board / 6

        def convert_grid_to_logical_position(self, grid_position):
            grid_position = np.array(grid_position)
            return np.array(grid_position // (size_of_board / 3), dtype=int)

        def is_grid_occupied(self, logical_position):
            if self.board_status[logical_position[0]][logical_position[1]] == 0:
                return False
            else:
                return True

        def is_winner(self, player):

            player = -1 if player == 'X' else 1

            # Three in a row
            for i in range(3):
                if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                    return True
                if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                    return True

            # Diagonals
            if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                return True

            if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                return True

            return False

        def is_tie(self):

            r, c = np.where(self.board_status == 0)
            tie = False
            if len(r) == 0:
                tie = True

            return tie

        def is_gameover(self):
            # Either someone wins or all grid occupied
            self.X_wins = self.is_winner('X')
            if not self.X_wins:
                self.O_wins = self.is_winner('O')

            if not self.O_wins:
                self.tie = self.is_tie()

            gameover = self.X_wins or self.O_wins or self.tie

            if self.X_wins:
                print('X wins')
            if self.O_wins:
                print('O wins')
            if self.tie:
                print('Its a tie')

            return gameover

        def click(self, event):
            grid_position = [event.x, event.y]
            logical_position = self.convert_grid_to_logical_position(
                grid_position)

            if not self.reset_board:
                if self.player_X_turns:
                    if not self.is_grid_occupied(logical_position):
                        self.draw_X(logical_position)
                        self.board_status[logical_position[0]
                                          ][logical_position[1]] = -1
                        self.player_X_turns = not self.player_X_turns
                else:
                    if not self.is_grid_occupied(logical_position):
                        self.draw_O(logical_position)
                        self.board_status[logical_position[0]
                                          ][logical_position[1]] = 1
                        self.player_X_turns = not self.player_X_turns

                # Check if game is concluded
                if self.is_gameover():
                    self.display_gameover()
                    # print('Done')
            else:  # Play Again
                self.canvas.delete("all")
                self.play_again()
                self.reset_board = False

    game_instance = Tic_Tac_Toe()
    game_instance.mainloop()


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


def takescreenshot():

    name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # take the screenshot and save it to the C:\\Programfiles\\Olivia\\screenshot folder
    dir = "C:\\Olivia\\screenshot\\"
    name = dir + name + ".png"
    # create the folder named C:\\Screenshots if it doesn't already exist
    if not os.path.exists(dir):
        os.makedirs(dir)
    # save screenshot to file in image forma
    img = pyautogui.screenshot(name)
    img.show()
    print('Screenshot taken')

    # make a gui using tkinter library to display the screenshot and take a screenshot of a specific area
    root = tk.Tk()
    root.title('Screenshot')

    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    frame.pack()

    button = tk.Button(frame, text='Take Screenshot', command=takescreenshot)
    button.pack(side=tk.LEFT)

    close = tk.Button(frame, text='Quit', command=quit)
    close.pack(side=tk.LEFT)

    root.mainloop()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chriagsinghal@gmail.com', 'my password')
    server.sendmail('chiragsinghal@gmail.com', to, content)
    server.close()


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


# asdfjkl;


if __name__ == "__main__":
    # wishMe()

    while True:

        # take command from user and convert it to lower case and assign it to a variable named as query

        query = takeCommand().lower()

        if 'desktop' in query or 'computer' in query or 'system' in query:

                if 'shutdown' in query:
                    speak("Hold On ! Your system is on its way to shut down")
                    os.system('shutdown /s /f')
                    running = False
                    sys.exit()

                elif "restart" in query or "reboot" in query:
                    subprocess.call(["shutdown", "/r"])

                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")

                elif "log off" in query or "sign out" in query or "signout" in query or 'logout' in query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    speak("Signing out")
                    subprocess.call("shutdown / l")


        # give the current date and time if 'date' is in query
        if 'date' in query and "current" in query:
            now = datetime.datetime.now()
            speak("The current date is")
            speak(now.strftime("%d-%m-%Y"))


        if 'fullform of abcdef' in query:
            sp("Any body can dance")


        elif 'current weather' in query:
            reg_ex = re.search('current weather in (.*)', query)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                    city, k, x['temp_max'], x['temp_min']))

        elif 'tell me about' in query:

            reg_ex = re.search('tell me about (.*)', query)

            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    speak(ny.content[:500].encode('utf-8'))
            except Exception as e:
                speak(e)


        # if the query contains 'who is (something)', then return the information of that person/organisation from the wikipedia using the information from the wikipedia library
        elif 'who is' in query:
            reg_ex = re.search('who is (.*)', query)
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.summary(topic, sentences=2)
                speak('According to Wikipedia')
                print(ny)
                speak(ny)
                

        elif 'game' in query and 'start' in query:
                    if 'tic' in query or 'tac' in query or 'toe' in query:

                        tictactoe()
                        continue



        # telling the joke when the query of the user contains joke
        elif 'joke' in query:
            givejoke()

        elif "send" in query and 'message' in query:
                username = {
                    'chirag': '+91 9999999999',
                    'india': '+91 9999999998',
                    'abhinav': '+91 9999999997',
                    'ram': '+91 1234567891',
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


                    'None': '+91 7428449707'  # if you want to add more contacts
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
                    break
            

                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this message")
                    break

        # telling the cpu usage when the says a command that contains both cpu and usage.
        elif 'usage' in query and 'cpu' in query:
            speak("CPU is at " + str(psutil.cpu_percent()) + "%")

        # telling the ram usage when the says a command that contains both ram and usage.
        elif 'usage' in query and 'ram' in query:
            speak("RAM is at " + str(psutil.virtual_memory()[2]) + "%")

        # telling the disk usage when the says a command that contains both disk and usage.
        elif 'usage' in query and 'disk' in query:
            speak("Disk is at " + str(psutil.disk_usage('/')[3]) + "%")

        # telling the battery usage when the says a command that contains both battery and usage.
        elif 'usage' in query and 'battery' in query:
            speak("Battery is at " + str(psutil.sensors_battery().percent) + "%")

        # telling the battery status when the says a command that contains both battery and status.
        elif 'status' in query and 'battery' in query:
            if psutil.sensors_battery().power_plugged == True:

                speak("Battery is charging")


            if psutil.sensors_battery().power_plugged == False:
                speak("Battery is discharging")


        
        # type the text in the current window if 'type' is in query
        elif 'typing' in query and 'start' in query:
            speak("Starting typing")
            speak("What should i type sir")
            while True:
                if query != 'none':
                    type_sentence = takeCommand()
                    if 'stop typing' in type_sentence:
                        break
                    elif 'enter' in type_sentence:
                        pyautogui.press('enter')
                    elif 'backspace' in type_sentence:
                        presshotkey('ctrl', 'backspace')
                    elif 'tab' in type_sentence:
                        pyautogui.press('tab')

                    elif 'space' in type_sentence:
                        pyautogui.press('space')

                    elif 'caps lock' in type_sentence:
                        pyautogui.press('caps lock')

                    else:
                        pyautogui.typewrite(type_sentence)


        elif "note" in query or "notes" in query:

            if 'write' in query:

                speak("What should I write down?")
                note = takeCommand()
                file = open('olivianote.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm or 'ok' in snfm:
                    file.write(datetime.datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S") + '\n')
                    file.write(note)
                    speak("Note has been saved")
                else:
                    file.write(note)
                    speak("Note has been saved")
                file.close()
                break

            elif 'read' in query:
                speak("Reading Note Sir")
                file = open('olivianote.txt', 'r')
                print(file.read())
                speak(file.read(6))
                file.close()
                break

            elif 'delete' in query:
                speak("Deleting Note Sir")
                os.remove('olivianote.txt')
                speak("Note has been deleted")
                break

            elif 'open' in query or 'show' in query:
                speak("Opening Note")
                os.startfile('olivianote.txt')
                break

            elif 'close' in query:
                speak("Closing Note")
                os.system('TASKKILL /F /IM notepad.exe')
                break

            elif 'clear' in query or 'empty' in query:
                speak("Emptying Note")
                os.remove('olivianote.txt')
                speak("Note has been deleted")
                break

            elif 'save' in query:
                speak("Saving Note")
                file = open('olivianote.txt', 'a')
                file.write('\n')
                file.close()
                break

        if 'play' in query:
            song = query.replace('play', '')
            sp('playing ')
            sp(song)
            pywhatkit.playonyt(song)
            query = query.replace('play', '')

            while True:
                query = takeCommand().lower()
                # pause the video if 'pause' is in query
                if 'pause' in query or 'pass' in query:

                    presskey('space')

                   # sp('paused')

                elif 'play' in query:
                    presskey('space')
                   # sp('playing')

                elif 'stop' in query:
                    presskey('space')
                    # sp('stopped')

                elif 'next' in query:

                    if 'tab' in query:

                        pyautogui.hotkey('ctrl', 'tab')

                        time.sleep(1)
                    else:

                        presshotkey('shift', 'n')

                    # sp('next song')
                   # sp('Gone to the next video')

                # previous the video if 'previous' is in query
                elif 'previous' in query:
                    presskey('p')
                   # sp('Gone to the previous video')

                # Increase the speed if 'faster' is in query or increase the speed if 'speed up' is in query or 'increase speed' is in query
                elif 'faster' in query or 'speed up' in query or 'increase speed' in query:
                    presshotkey('shift', '.')
                    # sp('speed increased')

                # Decrease the speed if 'slower' is in query or decrease the speed if 'slow down' is in query or 'decrease speed' is in query
                elif 'slower' in query or 'slow down' in query or 'decrease speed' in query:
                    presshotkey('shift', ',')
                    # sp('decreased the speed of the video')

                    # Increase the volume if 'volume up' is in query or increase the volume if 'increase volume' is in query or 'louder' is in query
                elif 'volume up' in query or 'increase volume' in query or 'louder' in query:
                    presskey('up')
                 # sp('increased the volume')

                # Decrease the volume if 'volume down' is in query
                elif 'volume down' in query or 'decrease volume' in query or 'quieter' in query:
                    presskey('down')
                    # sp('decreased the volume')

                # mute the video if 'mute' is in query
                elif 'mute' in query:
                    presskey('m')
                  #  sp('muted the video')

                # unmute the video if 'unmute' is in query
                elif 'unmute' in query:
                    presskey('m')
                    # sp('unmuted the video')

                # close the video if 'close' is in query
                elif 'close' in query:
                    presshotkey('ctrl', 'w')
                    # sp('Closed the video')
                    break

                # if 'exit' is in query then exit the video
                elif 'exit' in query:
                    presshotkey('alt', 'f4')
                    # sp('Exited the video')
                    break

                # if 'quit' is in query then quit pro
                elif 'quit' in query:
                    presshotkey('alt', 'f4')
                    # sp('Quited the video')
                    break

                # if 'restart' is in query then restart the video
                elif 'restart' in query or 'reload' in query or 'refresh' in query or 'reboot' in query:
                    presshotkey('ctrl', 'r')
                    # sp('Restarted the video')

                # if 'full screen' is in query then make the video full screen
                elif 'full screen' in query:
                    presshotkey('f')
                    # sp('Made the video full screen')

                # if 'exit full screen' is in query then exit the full screen
                elif 'exit full screen' in query:
                    presskey('f')
                    # sp('Exited the full screen')

                # if 'brightness' is in query then show the brightness
                elif 'brightness' in query:
                    if 'increase' in query:
                        presskey('f3')
                        # sp('Increased the brightness')

                    elif 'decrease' in query:
                        presskey('f2')
                        # sp('Decreased the brightness')



        elif 'news' in query:
                NewsFromBBC()


        elif 'tab' in query:
            if 'next' in query:
                presshotkey('ctrl', 'tab')
                # sp('Gone to the next tab')
            elif 'previous' in query:
                presshotkey('shift', 't')

            elif 'quit' in query:
                presshotkey('ctrl', 'w')
                # sp('Quited the tab')

            elif 'restart' in query or 'reload' in query or 'refresh' in query or 'reboot' in query:
                presshotkey('ctrl', 'r')

            elif 'new' in query:
                presshotkey('ctrl', 't')

            elif 'close' in query:
                presshotkey('ctrl', 'w')




        # tell user the common usage of the command if 'usage' is in query

        elif 'where are you?' in query:
            speak("I am here in the main loop. sir")


            # if 'usage' is in query and 'network' is in query give the usage of network

        # search in chrome when the query is 'search'

        elif 'search in chrome' in query:
            speak("What should i search for sir")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open(
                'https://www.google.com/search?q=' + search)

        
  # if 'time' is in query and "current" is in the query then tell the time in very good manner for example we can say the current time is 2 pm and 28 minutes sir
 # or the current time is 5 pm and 28 minutes sir . be polite.



        elif 'time' in query and 'current' in query:
            ctime()


    

        # Read the copied text from clipboard and speak it if 'read' is in query and 'aloud' is in query
        elif 'read aloud' in query:
                text2speech()


        # if 'open' is in query and 'notepad' is in query then open notepad
        elif 'open notepad' in query:
            os.system('notepad')


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

        elif "what is Your dream" in query:
            speak("My dream is to be a Software Engineer")

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

        elif query == 'quit' or 'olivia quit' in query or 'olivia bye' in query or query == 'bye' or query == 'exit' or query == 'goodbye' or query == 'bye bye':
            sp("Bye Sir")
            exit()

        # if the user wants to repeat the last command
        elif 'repeat' in query and 'olivia' in query:
            # telling the user that the program is repeating the last command
            speak("repeating the last command")
            # repeating the last command
            sp(query)

        # writing code to fetch the news from the "https://news.google.com/news/rss" using webscraping and reading that news using beautiful soup

        elif 'generate' in query:
            if 'password' in query:
                generate_random_password()
            elif 'number' in query:
                sp(random.randint(0, 100))


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


        elif 'screenshot' in query:
            takescreenshot()

        elif 'joke' in query:
            givejoke()

        elif 'ip address' in query:
            giveip()

        elif 'call me' in query:
            speak('What is your name?')
            query = query.replace("call me", "")
            uname = query
            speak('Hello ' + uname + ' How may I help you?')

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query



        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop olivia from listening commands")
            time.sleep(120)
            speak("Olivia is listening again")




        elif 'recycle bin' in query:

            if 'clear' in query or 'empty' in query:

                speak("Emptying the recycle bin")

                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

                speak("Recycle Bin Recycled")


        elif 'lock window' in query or 'lock screen' in query or 'lock the screen' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            speak("I have remembered that")

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that " + remember.read())
            remember.close()

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            sp("User asked to Locate")
            sp(location)
            webbrowser.open(
                "https://www.google.com / maps / place/" + location + "")


# tell the stock price of the company using yahoo finance api and speak the result to the user using google speech api and print the result to the console
        elif "stock" in query and "price" in query:
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
        elif "weather" in query and "today" in query:
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

        elif "date" in query and "curren" in query:

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

        elif "calculate" in query and "square" in query:

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

        elif 'search' in query:
            # indicates the start of a search query
            sp('Searching ...')
            # use the function to get the result of the query
            query = query.replace("search ", "")
            # replace the query with the result of the query
            query = query.replace(" on ", "")

            # search on the youtube if youtube is in the resultant query after the execution of the above lines.
            if 'youtube' in query:
                query = query.replace("youtube", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")

            # writing code for all search engines in the below lines

            # for google search engine
            # search on the google if google is in the resultant query after the execution of the above lines.
            elif 'google' in query:

                query = query.replace("google", "")

                if 'images' in query:
                    query = query.replace("images", "")
                    webbrowser.open(
                        f"https://www.google.com/search?tbm=isch&q={query}")

                elif 'maps' in query:
                    query = query.replace("maps", "")
                    webbrowser.open(
                        f"https://www.google.com/maps/search/{query}")

                elif 'news' in query:
                    query = query.replace("news", "")
                    webbrowser.open(
                        f"https://www.google.com/search?q={query}&tbm=nws")

                elif 'videos' in query:
                    query = query.replace("videos", "")
                    webbrowser.open(
                        f"https://www.google.com/search?tbm=vid&q={query}")

                elif 'books' in query:
                    query = query.replace("books", "")
                    webbrowser.open(
                        f"https://www.google.com/search?tbm=bks&q={query}")

                elif 'translate' in query:
                    query = query.replace("translate", "")
                    webbrowser.open(
                        f"https://translate.google.com/#auto/en/{query}")

                elif 'news' in query:
                    query = query.replace("news", "")
                    webbrowser.open(
                        f"https://www.google.com/search?q={query}&tbm=nws")

                else:
                    webbrowser.open(
                        f"https://www.google.com/search?q={query}")

            # for duckduckgo search engine
            # search on the duckduckgo if duckduckgo is in the resultant query after the execution of the above lines.
            elif 'duckduckgo' in query:
                query = query.replace("duckduckgo", "")
                webbrowser.open(
                    f"https://duckduckgo.com/?q={query}")

            # for bing search engine
            # search on the bing if bing is in the resultant query after the execution of the above lines.
            elif 'bing' in query:
                query = query.replace("bing", "")
                webbrowser.open(
                    f"https://www.bing.com/search?q={query}")

            # for yahoo search engine
            # search on the yahoo if yahoo is in the resultant query after the execution of the above lines.
            elif 'yahoo' in query:
                query = query.replace("yahoo", "")
                webbrowser.open(
                    f"https://search.yahoo.com/search?p={query}")

            # search all the educational websites in the below lines

            # for wikipedia search engine
            # search on the wikipedia if wikipedia is in the resultant query after the execution of the above lines.
            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                webbrowser.open(
                    f"https://www.wikipedia.org/search-redirect.php?search={query}")

            # for wikitionary search engine
            # search on the wikitionary if wikitionary is in the resultant query after the execution of the above lines.
            elif 'wiktionary' in query:
                query = query.replace("wiktionary", "")
                webbrowser.open(
                    f"https://en.wiktionary.org/wiki/{query}")

            # for wikiquote search engine
            # search on the wikiquote if wikiquote is in the resultant query after the execution of the above lines.
            elif 'wikiquote' in query:
                query = query.replace("wikiquote", "")
                webbrowser.open(
                    f"https://en.wikiquote.org/wiki/{query}")

            # for wikisource search engine
            # search on the wikisource if wikisource is in the resultant query after the execution of the above lines.
            elif 'wikisource' in query:
                query = query.replace("wikisource", "")
                webbrowser.open(
                    f"https://en.wikisource.org/wiki/{query}")

            # for wikibooks search engine
            # search on the wikibooks if wikibooks is in the resultant query after the execution of the above lines.
            elif 'wikibooks' in query:
                query = query.replace("wikibooks", "")
                webbrowser.open(
                    f"https://en.wikibooks.org/wiki/{query}")

            # for wikinews search engine
            # search on the wikinews if wikinews is in the resultant query after the execution of the above lines.
            elif 'wikinews' in query:

                query = query.replace("wikinews", "")
                webbrowser.open(
                    f"https://en.wikinews.org/wiki/{query}")

            # for wikidata search engine
            # search on the wikidata if wikidata is in the resultant query after the execution of the above lines.
            elif 'wikidata' in query:

                query = query.replace("wikidata", "")
                webbrowser.open(
                    f"https://www.wikidata.org/wiki/{query}")

            # for wikiversity search engine
            # search on the wikiversity if wikiversity is in the resultant query after the execution of the above lines.
            elif 'wikiversity' in query:

                query = query.replace("wikiversity", "")
                webbrowser.open(
                    f"https://en.wikiversity.org/wiki/{query}")

            # for wikispecies search engine
            # search on the wikispecies if wikispecies is in the resultant query after the execution of the above lines.
            elif 'wikispecies' in query:
                query = query.replace("wikispecies", "")
                webbrowser.open(
                    f"https://species.wikimedia.org/wiki/{query}")

            # for wikimedia search engine
            # search on the wikimedia if wikimedia is in the resultant query after the execution of the above lines.
            elif 'wikimedia' in query:
                query = query.replace("wikimedia", "")
                webbrowser.open(
                    f"https://commons.wikimedia.org/wiki/{query}")

            # for wikivoyage search engine
            # search on the wikivoyage if wikivoyage is in the resultant query after the execution of the above lines.
            elif 'wikivoyage' in query:
                query = query.replace("wikivoyage", "")
                webbrowser.open(
                    f"https://en.wikivoyage.org/wiki/{query}")

            # for stackoverflow search engine
            # search on the stackoverflow if stackoverflow is in the resultant query after the execution of the above lines.
            elif 'stackoverflow' in query:
                query = query.replace("stackoverflow", "")
                webbrowser.open(
                    f"https://stackoverflow.com/search?q={query}")

            # for quora search engine
            # search on the quora if quora is in the resultant query after the execution of the above lines.
            elif 'quora' in query:
                query = query.replace("quora", "")
                webbrowser.open(
                    f"https://www.quora.com/search?q={query}")

            # for coursera search engine
            # search on the coursera if coursera is in the resultant query after the execution of the above lines.
            elif 'coursera' in query:
                query = query.replace("coursera", "")
                webbrowser.open(
                    f"https://www.coursera.org/search?query={query}")

            # for edx search engine
            # search on the edx if edx is in the resultant query after the execution of the above lines.
            elif 'edx' in query:
                query = query.replace("edx", "")
                webbrowser.open(
                    f"https://www.edx.org/search?query={query}")

            # for udemy search engine
            # search on the udemy if udemy is in the resultant query after the execution of the above lines.
            elif 'udemy' in query:
                query = query.replace("udemy", "")
                webbrowser.open(
                    f"https://www.udemy.com/search/?q={query}")

            # for udacity search engine
            # search on the udacity if udacity is in the resultant query after the execution of the above lines.
            elif 'udacity' in query:
                query = query.replace("udacity", "")
                webbrowser.open(
                    f"https://www.udacity.com/course/search?query={query}")

            # For the eccomerce websites in the below lines
            # for amazon search engine
            # search on the amazon if amazon is in the resultant query after the execution of the above lines.
            elif 'amazon' in query:
                query = query.replace("amazon", "")
                webbrowser.open(
                    f"https://www.amazon.in/s?k={query}")

            # for flipkart search engine
            # search on the flipkart if flipkart is in the resultant query after the execution of the above lines.
            elif 'flipkart' in query:
                query = query.replace("flipkart", "")
                webbrowser.open(
                    f"https://www.flipkart.com/search?q={query}")

            # for snapdeal search engine
            # search on the snapdeal if snapdeal is in the resultant query after the execution of the above lines.
            elif 'snapdeal' in query:
                query = query.replace("snapdeal", "")
                webbrowser.open(
                    f"https://www.snapdeal.com/search?keyword={query}")

            # for shopclues search engine
            # search on the shopclues if shopclues is in the resultant query after the execution of the above lines.
            elif 'shopclues' in query:
                query = query.replace("shopclues", "")
                webbrowser.open(
                    f"https://www.shopclues.com/search?q={query}")

            # for myntra search engine
            # search on the myntra if myntra is in the resultant query after the execution of the above lines.
            elif 'myntra' in query:
                query = query.replace("myntra", "")
                webbrowser.open(
                    f"https://www.myntra.com/search?q={query}")

            # for jabong search engine
            # search on the jabong if jabong is in the resultant query after the execution of the above lines.
            elif 'jabong' in query:
                query = query.replace("jabong", "")
                webbrowser.open(
                    f"https://www.jabong.com/search?q={query}")

            # for paytm search engine
            # search on the paytm if paytm is in the resultant query after the execution of the above lines.
            elif 'paytm' in query:
                query = query.replace("paytm", "")
                webbrowser.open(
                    f"https://paytm.com/shop/search?q={query}")

            # for ebay search engine
            # search on the ebay if ebay is in the resultant query after the execution of the above lines.
            elif 'ebay' in query:
                query = query.replace("ebay", "")
                webbrowser.open(
                    f"https://www.ebay.com/sch/i.html?_nkw={query}")

            # For social media websites in the below lines
            # for facebook search engine
            # search on the facebook if facebook is in the resultant query after the execution of the above lines.
            elif 'facebook' in query:
                query = query.replace("facebook", "")
                webbrowser.open(
                    f"https://www.facebook.com/search/top/?q={query}")

            # for instagram search engine
            # search on the instagram if instagram is in the resultant query after the execution of the above lines.
            elif 'instagram' in query:
                query = query.replace("instagram", "")
                webbrowser.open(
                    f"https://www.instagram.com/explore/tags/{query}")

            # for twitter search engine
            # search on the twitter if twitter is in the resultant query after the execution of the above lines.
            elif 'twitter' in query:
                query = query.replace("twitter", "")
                webbrowser.open(
                    f"https://twitter.com/search?q={query}")

            # for linkedin search engine
            # search on the linkedin if linkedin is in the resultant query after the execution of the above lines.
            elif 'linkedin' in query:
                query = query.replace("linkedin", "")
                webbrowser.open(
                    f"https://www.linkedin.com/search/results/index/?keywords={query}")

            # for snapchat search engine
            # search on the snapchat if snapchat is in the resultant query after the execution of the above lines.
            elif 'snapchat' in query:
                query = query.replace("snapchat", "")
                webbrowser.open(
                    f"https://www.snapchat.com/search/{query}")

            # for video streaming websites in the below lines
            # for youtube search engine
            # search on the youtube if youtube is in the resultant query after the execution of the above lines.
            elif 'youtube' in query:
                query = query.replace("youtube", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")

            # for vimeo search engine
            # search on the vimeo if vimeo is in the resultant query after the execution of the above lines.
            elif 'vimeo' in query:
                query = query.replace("vimeo", "")
                webbrowser.open(
                    f"https://vimeo.com/search?q={query}")

            # for dailymotion search engine
            # search on the dailymotion if dailymotion is in the resultant query after the execution of the above lines.
            elif 'dailymotion' in query:
                query = query.replace("dailymotion", "")
                webbrowser.open(
                    f"https://www.dailymotion.com/search/{query}")

            # for twitch search engine
            # search on the twitch if twitch is in the resultant query after the execution of the above lines.
            elif 'twitch' in query:
                query = query.replace("twitch", "")
                webbrowser.open(
                    f"https://www.twitch.tv/search?q={query}")

            # for netflix search engine
            # search on the netflix if netflix is in the resultant query after the execution of the above lines.
            elif 'netflix' in query:
                query = query.replace("netflix", "")
                webbrowser.open(
                    f"https://www.netflix.com/search?q={query}")

            # for hulu search engine
            # search on the hulu if hulu is in the resultant query after the execution of the above lines.
            elif 'hulu' in query:
                query = query.replace("hulu", "")
                webbrowser.open(
                    f"https://www.hulu.com/search?q={query}")

            # for disney search engine
            # search on the disney if disney is in the resultant query after the execution of the above lines.
            elif 'disney' in query:
                query = query.replace("disney", "")
                webbrowser.open(
                    f"https://disney.go.com/search?q={query}")

            # for hbo search engine
            # search on the hbo if hbo is in the resultant query after the execution of the above lines.
            elif 'hbo' in query:
                query = query.replace("hbo", "")
                webbrowser.open(
                    f"https://www.hbo.com/search?q={query}")

            # for hotstar search engine
            # search on the hotstar if
            # hotstar is in the resultant query after the execution of the above lines.
            elif 'hotstar' in query:
                query = query.replace("hotstar", "")
                webbrowser.open(
                    f"https://www.hotstar.com/search?q={query}")

            # for music search engine or music player websites or music streaming websites or for songs streaming websites
            # for spotify search engine
            # search on the spotify if spotify is in the resultant query after the execution of the above lines.
            elif 'spotify' in query:
                query = query.replace("spotify", "")
                webbrowser.open(
                    f"https://open.spotify.com/search/{query}")

            # for apple music search engine
            # search on the apple music if apple music is in the resultant query after the execution of the above lines.
            elif 'apple music' in query:
                query = query.replace("apple music", "")
                webbrowser.open(
                    f"https://music.apple.com/search?term={query}")

            # for soundcloud search engine
            # search on the soundcloud if soundcloud is in the resultant query after the execution of the above lines.
            elif 'soundcloud' in query:
                query = query.replace("soundcloud", "")
                webbrowser.open(
                    f"https://soundcloud.com/search?q={query}")

            # for tidal search engine
            # search on the tidal if tidal is in the resultant query after the execution of the above lines.
            elif 'tidal' in query:
                query = query.replace("tidal", "")
                webbrowser.open(
                    f"https://tidal.com/search?q={query}")

            # for youtube music search engine
            # search on the youtube music if youtube music is in the resultant query after the execution of the above lines.
            elif 'youtube music' in query:
                query = query.replace("youtube music", "")
                webbrowser.open(
                    f"https://music.youtube.com/search?q={query}")

            else:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")

        elif 'open' in query:
            query = query.replace("open", "")

            if 'firefox' in query:
                sp("Firefox is opening")
                webbrowser.open(
                    "https://www.mozilla.org/en-US/firefox/new/")

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


# create a translate feature in the virutal assistant

        elif 'translate' in query:
            query = query.replace("translate", "")

            LANGUAGES = {
                'af': 'afrikaans',
                'sq': 'albanian',
                'am': 'amharic',
                'ar': 'arabic',
                'hy': 'armenian',
                'az': 'azerbaijani',
                'eu': 'basque',
                'be': 'belarusian',
                'bn': 'bengali',
                'bs': 'bosnian',
                'bg': 'bulgarian',
                'ca': 'catalan',
                'ceb': 'cebuano',
                'ny': 'chichewa',
                'zh-cn': 'chinese (simplified)',
                'zh-tw': 'chinese (traditional)',
                'co': 'corsican',
                'hr': 'croatian',
                'cs': 'czech',
                'da': 'danish',
                'nl': 'dutch',
                'en': 'english',
                'eo': 'esperanto',
                'et': 'estonian',
                'tl': 'filipino',
                'fi': 'finnish',
                'fr': 'french',
                'fy': 'frisian',
                'gl': 'galician',
                'ka': 'georgian',
                'de': 'german',
                'el': 'greek',
                'gu': 'gujarati',
                'ht': 'haitian creole',
                'ha': 'hausa',
                'haw': 'hawaiian',
                'iw': 'hebrew',
                'he': 'hebrew',
                'hi': 'hindi',
                'hmn': 'hmong',
                'hu': 'hungarian',
                'is': 'icelandic',
                'ig': 'igbo',
                'id': 'indonesian',
                'ga': 'irish',
                'it': 'italian',
                'ja': 'japanese',
                'jw': 'javanese',
                'kn': 'kannada',
                'kk': 'kazakh',
                'km': 'khmer',
                'ko': 'korean',
                'ku': 'kurdish (kurmanji)',
                'ky': 'kyrgyz',
                'lo': 'lao',
                'la': 'latin',
                'lv': 'latvian',
                'lt': 'lithuanian',
                'lb': 'luxembourgish',
                'mk': 'macedonian',
                'mg': 'malagasy',
                'ms': 'malay',
                'ml': 'malayalam',
                'mt': 'maltese',
                'mi': 'maori',
                'mr': 'marathi',
                'mn': 'mongolian',
                'my': 'myanmar (burmese)',
                'ne': 'nepali',
                'no': 'norwegian',
                'or': 'odia',
                'ps': 'pashto',
                'fa': 'persian',
                'pl': 'polish',
                'pt': 'portuguese',
                'pa': 'punjabi',
                'ro': 'romanian',
                'ru': 'russian',
                'sm': 'samoan',
                'gd': 'scots gaelic',
                'sr': 'serbian',
                'st': 'sesotho',
                'sn': 'shona',
                'sd': 'sindhi',
                'si': 'sinhala',
                'sk': 'slovak',
                'sl': 'slovenian',
                'so': 'somali',
                'es': 'spanish',
                'su': 'sundanese',
                'sw': 'swahili',
                'sv': 'swedish',
                'tg': 'tajik',
                'ta': 'tamil',
                'te': 'telugu',
                'th': 'thai',
                'tr': 'turkish',
                'uk': 'ukrainian',
                'ur': 'urdu',
                'ug': 'uyghur',
                'uz': 'uzbek',
                'vi': 'vietnamese',
                'cy': 'welsh',
                'xh': 'xhosa',
                'yi': 'yiddish',
                'yo': 'yoruba',
                'zu': 'zulu',
            }

            # translate to the afrikaans

            if 'afrikaans' in query:
                # telling the user that we are translating the text to the afrikaans
                speak("translating to afrikaans")
                # getting the text from the user and replacing the "to afrikaans" with nothing so that we can translate the text
                query = query.replace("to afrikaans", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the afrikaans and storing the result in a variable named result
                result = translator.translate(query, dest='af')
                # speaking and printing the result
                sp(result.text)

            # translate to the albanian

            elif 'albanian' in query:
                # telling the user that we are translating the text to the albanian
                speak("translating to albanian")
                # getting the text from the user and replacing the "to albanian" with nothing so that we can translate the text
                query = query.replace("to albanian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the albanian and storing the result in a variable named result
                result = translator.translate(query, dest='sq')
                # speaking and printing the result
                sp(result.text)

            # translate to the amharic

            elif 'amharic' in query:
                # telling the user that we are translating the text to the amharic
                speak("translating to amharic")
                # getting the text from the user and replacing the "to amharic" with nothing so that we can translate the text
                query = query.replace("to amharic", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the amharic and storing the result in a variable named result
                result = translator.translate(query, dest='am')
                # speaking and printing the result
                sp(result.text)

            # translate to the arabic

            elif 'arabic' in query:
                # telling the user that we are translating the text to the arabic
                speak("translating to arabic")
                # getting the text from the user and replacing the "to arabic" with nothing so that we can translate the text
                query = query.replace("to arabic", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the arabic and storing the result in a variable named result
                result = translator.translate(query, dest='ar')
                # speaking and printing the result
                sp(result.text)

            # translate to the armenian

            elif 'armenian' in query:
                # telling the user that we are translating the text to the armenian
                speak("translating to armenian")
                # getting the text from the user and replacing the "to armenian" with nothing so that we can translate the text
                query = query.replace("to armenian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the armenian and storing the result in a variable named result
                result = translator.translate(query, dest='hy')
                # speaking and printing the result
                sp(result.text)

            # translate to the azerbaijani

            elif 'azerbaijani' in query:

                # telling the user that we are translating the text to the azerbaijani
                speak("translating to azerbaijani")
                # getting the text from the user and replacing the "to azerbaijani" with nothing so that we can translate the text
                query = query.replace("to azerbaijani", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the azerbaijani and storing the result in a variable named result
                result = translator.translate(query, dest='az')
                # speaking and printing the result
                sp(result.text)

            # translate to the basque

            elif 'basque' in query:
                # telling the user that we are translating the text to the basque
                speak("translating to basque")
                # getting the text from the user and replacing the "to basque" with nothing so that we can translate the text
                query = query.replace("to basque", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the basque and storing the result in a variable named result
                result = translator.translate(query, dest='eu')
                # speaking and printing the result
                sp(result.text)

            # translate to the bengali

            elif 'bengali' in query:
                # telling the user that we are translating the text to the bengali
                speak("translating to bengali")
                # getting the text from the user and replacing the "to bengali" with nothing so that we can translate the text
                query = query.replace("to bengali", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the bengali and storing the result in a variable named result
                result = translator.translate(query, dest='bn')
                # speaking and printing the result
                sp(result.text)

            # translate to the bosnian

            elif 'bosnian' in query:
                # telling the user that we are translating the text to the bosnian
                speak("translating to bosnian")
                # getting the text from the user and replacing the "to bosnian" with nothing so that we can translate the text
                query = query.replace("to bosnian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the bosnian and storing the result in a variable named result
                result = translator.translate(query, dest='bs')
                # speaking and printing the result
                sp(result.text)

            # translate to the bulgarian
            elif 'bulgarian' in query:
                # telling the user that we are translating the text to the bulgarian
                speak("translating to bulgarian")
                # getting the text from the user and replacing the "to bulgarian" with nothing so that we can translate the text
                query = query.replace("to bulgarian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the bulgarian and storing the result in a variable named result
                result = translator.translate(query, dest='bg')
                # speaking and printing the result
                sp(result.text)

            # translate to the catalan
            elif 'catalan' in query:
                # telling the user that we are translating the text to the catalan
                speak("translating to catalan")
                # getting the text from the user and replacing the "to catalan" with nothing so that we can translate the text
                query = query.replace("to catalan", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the catalan and storing the result in a variable named result
                result = translator.translate(query, dest='ca')
                # speaking and printing the result
                sp(result.text)

            # translate to the cebuano
            elif 'cebuano' in query:
                # telling the user that we are translating the text to the cebuano
                speak("translating to cebuano")
                # getting the text from the user and replacing the "to cebuano" with nothing so that we can translate the text
                query = query.replace("to cebuano", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the cebuano and storing the result in a variable named result
                result = translator.translate(query, dest='ceb')
                # speaking and printing the result
                sp(result.text)

            # translate to the chinese
            elif 'chinese' in query:
                # telling the user that we are translating the text to the chinese
                speak("translating to chinese")
                # getting the text from the user and replacing the "to chinese" with nothing so that we can translate the text
                query = query.replace("to chinese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the chinese and storing the result in a variable named result
                result = translator.translate(query, dest='zh-CN')
                # speaking and printing the result
                sp(result.text)

            # translate to the croatian
            elif 'croatian' in query:
                # telling the user that we are translating the text to the croatian
                speak("translating to croatian")
                # getting the text from the user and replacing the "to croatian" with nothing so that we can translate the text
                query = query.replace("to croatian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the croatian and storing the result in a variable named result
                result = translator.translate(query, dest='hr')
                # speaking and printing the result
                sp(result.text)

            # translate to the czech
            elif 'czech' in query:
                # telling the user that we are translating the text to the czech
                speak("translating to czech")
                # getting the text from the user and replacing the "to czech" with nothing so that we can translate the text
                query = query.replace("to czech", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the czech and storing the result in a variable named result
                result = translator.translate(query, dest='cs')
                # speaking and printing the result
                sp(result.text)

            # translate to the danish
            elif 'danish' in query:
                # telling the user that we are translating the text to the danish
                speak("translating to danish")
                # getting the text from the user and replacing the "to danish" with nothing so that we can translate the text
                query = query.replace("to danish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the danish and storing the result in a variable named result
                result = translator.translate(query, dest='da')
                # speaking and printing the result
                sp(result.text)

            # translate to the dutch
            elif 'dutch' in query:
                # telling the user that we are translating the text to the dutch
                speak("translating to dutch")
                # getting the text from the user and replacing the "to dutch" with nothing so that we can translate the text
                query = query.replace("to dutch", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the dutch and storing the result in a variable named result
                result = translator.translate(query, dest='nl')
                # speaking and printing the result
                sp(result.text)

            # translate to the english
            elif 'english' in query:
                # telling the user that we are translating the text to the english
                speak("translating to english")
                # getting the text from the user and replacing the "to english" with nothing so that we can translate the text
                query = query.replace("to english", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the english and storing the result in a variable named result
                result = translator.translate(query, dest='en')
                # speaking and printing the result
                sp(result.text)

            # translate to the esperanto
            elif 'esperanto' in query:
                # telling the user that we are translating the text to the esperanto
                speak("translating to esperanto")
                # getting the text from the user and replacing the "to esperanto" with nothing so that we can translate the text
                query = query.replace("to esperanto", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the esperanto and storing the result in a variable named result
                result = translator.translate(query, dest='eo')
                # speaking and printing the result
                sp(result.text)

            # translate to the estonian
            elif 'estonian' in query:
                # telling the user that we are translating the text to the estonian
                speak("translating to estonian")
                # getting the text from the user and replacing the "to estonian" with nothing so that we can translate the text
                query = query.replace("to estonian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the estonian and storing the result in a variable named result
                result = translator.translate(query, dest='et')
                # speaking and printing the result
                sp(result.text)

            # translate to the filipino
            elif 'filipino' in query:
                # telling the user that we are translating the text to the filipino
                speak("translating to filipino")
                # getting the text from the user and replacing the "to filipino" with nothing so that we can translate the text
                query = query.replace("to filipino", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the filipino and storing the result in a variable named result
                result = translator.translate(query, dest='tl')
                # speaking and printing the result
                sp(result.text)

            # translate to the finnish
            elif 'finnish' in query:
                # telling the user that we are translating the text to the finnish
                speak("translating to finnish")
                # getting the text from the user and replacing the "to finnish" with nothing so that we can translate the text
                query = query.replace("to finnish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the finnish and storing the result in a variable named result
                result = translator.translate(query, dest='fi')
                # speaking and printing the result
                sp(result.text)

            # translate to the french
            elif 'french' in query:
                # telling the user that we are translating the text to the french
                speak("translating to french")
                # getting the text from the user and replacing the "to french" with nothing so that we can translate the text
                query = query.replace("to french", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the french and storing the result in a variable named result
                result = translator.translate(query, dest='fr')
                # speaking and printing the result
                sp(result.text)

            # translate to the frisian
            elif 'frisian' in query:
                # telling the user that we are translating the text to the frisian
                speak("translating to frisian")
                # getting the text from the user and replacing the "to frisian" with nothing so that we can translate the text
                query = query.replace("to frisian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the frisian and storing the result in a variable named result
                result = translator.translate(query, dest='fy')
                # speaking and printing the result
                sp(result.text)

            # translate to the galician
            elif 'galician' in query:
                # telling the user that we are translating the text to the galician
                speak("translating to galician")
                # getting the text from the user and replacing the "to galician" with nothing so that we can translate the text
                query = query.replace("to galician", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the galician and storing the result in a variable named result
                result = translator.translate(query, dest='gl')
                # speaking and printing the result
                sp(result.text)

            # translate to the georgian
            elif 'georgian' in query:

                # telling the user that we are translating the text to the georgian
                speak("translating to georgian")
                # getting the text from the user and replacing the "to georgian" with nothing so that we can translate the text
                query = query.replace("to georgian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the georgian and storing the result in a variable named result
                result = translator.translate(query, dest='ka')
                # speaking and printing the result
                sp(result.text)

            # translate to the german
            elif 'german' in query:
                # telling the user that we are translating the text to the german
                speak("translating to german")
                # getting the text from the user and replacing the "to german" with nothing so that we can translate the text
                query = query.replace("to german", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the german and storing the result in a variable named result
                result = translator.translate(query, dest='de')
                # speaking and printing the result
                sp(result.text)

            # translate to the greek
            elif 'greek' in query:
                # telling the user that we are translating the text to the greek
                speak("translating to greek")
                # getting the text from the user and replacing the "to greek" with nothing so that we can translate the text
                query = query.replace("to greek", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the greek and storing the result in a variable named result
                result = translator.translate(query, dest='el')
                # speaking and printing the result
                sp(result.text)

            # translate to the gujarati
            elif 'gujarati' in query:
                # telling the user that we are translating the text to the gujarati
                speak("translating to gujarati")
                # getting the text from the user and replacing the "to gujarati" with nothing so that we can translate the text
                query = query.replace("to gujarati", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the gujarati and storing the result in a variable named result
                result = translator.translate(query, dest='gu')
                # speaking and printing the result
                sp(result.text)

            # translate to the haitian creole
            elif 'haitian creole' in query:
                # telling the user that we are translating the text to the haitian creole
                speak("translating to haitian creole")
                # getting the text from the user and replacing the "to haitian creole" with nothing so that we can translate the text
                query = query.replace("to haitian creole", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the haitian creole and storing the result in a variable named result
                result = translator.translate(query, dest='ht')
                # speaking and printing the result
                sp(result.text)

            # translate to the hausa
            elif 'hausa' in query:

                # telling the user that we are translating the text to the hausa
                speak("translating to hausa")
                # getting the text from the user and replacing the "to hausa" with nothing so that we can translate the text
                query = query.replace("to hausa", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the hausa and storing the result in a variable named result
                result = translator.translate(query, dest='ha')
                # speaking and printing the result
                sp(result.text)

            # translate to the hawaiian
            elif 'hawaiian' in query:
                # telling the user that we are translating the text to the hawaiian
                speak("translating to hawaiian")
                # getting the text from the user and replacing the "to hawaiian" with nothing so that we can translate the text
                query = query.replace("to hawaiian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the hawaiian and storing the result in a variable named result
                result = translator.translate(query, dest='haw')
                # speaking and printing the result
                sp(result.text)

            # translate to the hebrew
            elif 'hebrew' in query:
                # telling the user that we are translating the text to the hebrew
                speak("translating to hebrew")
                # getting the text from the user and replacing the "to hebrew" with nothing so that we can translate the text
                query = query.replace("to hebrew", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the hebrew and storing the result in a variable named result
                result = translator.translate(query, dest='he')
                # speaking and printing the result
                sp(result.text)

            # translate to the hindi
            elif 'hindi' in query:
                # telling the user that we are translating the text to the hindi
                speak("translating to hindi")
                # getting the text from the user and replacing the "to hindi" with nothing so that we can translate the text
                query = query.replace("to hindi", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the hindi and storing the result in a variable named result
                result = translator.translate(query, dest='hi')
                # speaking and printing the result
                sp(result.text)

            # translate to the hungarian
            elif 'hungarian' in query:
                # telling the user that we are translating the text to the hungarian
                speak("translating to hungarian")
                # getting the text from the user and replacing the "to hungarian" with nothing so that we can translate the text
                query = query.replace("to hungarian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the hungarian and storing the result in a variable named result
                result = translator.translate(query, dest='hu')
                # speaking and printing the result
                sp(result.text)

            # translate to the icelandic
            elif 'icelandic' in query:
                # telling the user that we are translating the text to the icelandic
                speak("translating to icelandic")
                # getting the text from the user and replacing the "to icelandic" with nothing so that we can translate the text
                query = query.replace("to icelandic", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the icelandic and storing the result in a variable named result
                result = translator.translate(query, dest='is')
                # speaking and printing the result
                sp(result.text)

            # translate to the igbo
            elif 'igbo' in query:
                # telling the user that we are translating the text to the igbo
                speak("translating to igbo")
                # getting the text from the user and replacing the "to igbo" with nothing so that we can translate the text
                query = query.replace("to igbo", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the igbo and storing the result in a variable named result
                result = translator.translate(query, dest='ig')
                # speaking and printing the result
                sp(result.text)

            # translate to the indonesian
            elif 'indonesian' in query:
                # telling the user that we are translating the text to the indonesian
                speak("translating to indonesian")
                # getting the text from the user and replacing the "to indonesian" with nothing so that we can translate the text
                query = query.replace("to indonesian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the indonesian and storing the result in a variable named result
                result = translator.translate(query, dest='id')
                # speaking and printing the result
                sp(result.text)

            # translate to the irish
            elif 'irish' in query:
                # telling the user that we are translating the text to the irish
                speak("translating to irish")
                # getting the text from the user and replacing the "to irish" with nothing so that we can translate the text
                query = query.replace("to irish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the irish and storing the result in a variable named result
                result = translator.translate(query, dest='ga')
                # speaking and printing the result
                sp(result.text)

            # translate to the italian
            elif 'italian' in query:
                # telling the user that we are translating the text to the italian
                speak("translating to italian")
                # getting the text from the user and replacing the "to italian" with nothing so that we can translate the text
                query = query.replace("to italian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the italian and storing the result in a variable named result
                result = translator.translate(query, dest='it')
                # speaking and printing the result
                sp(result.text)

            # translate to the japanese
            elif 'japanese' in query:

                # telling the user that we are translating the text to the japanese
                speak("translating to japanese")
                # getting the text from the user and replacing the "to japanese" with nothing so that we can translate the text
                query = query.replace("to japanese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the japanese and storing the result in a variable named result
                result = translator.translate(query, dest='ja')
                # speaking and printing the result
                sp(result.text)

            # translate to the javanese
            elif 'javanese' in query:
                # telling the user that we are translating the text to the javanese
                speak("translating to javanese")
                # getting the text from the user and replacing the "to javanese" with nothing so that we can translate the text
                query = query.replace("to javanese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the javanese and storing the result in a variable named result
                result = translator.translate(query, dest='jw')
                # speaking and printing the result
                sp(result.text)

            # translate to the kannada
            elif 'kannada' in query:
                # telling the user that we are translating the text to the kannada
                speak("translating to kannada")
                # getting the text from the user and replacing the "to kannada" with nothing so that we can translate the text
                query = query.replace("to kannada", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the kannada and storing the result in a variable named result
                result = translator.translate(query, dest='kn')
                # speaking and printing the result
                sp(result.text)

            # translate to the kazakh
            elif 'kazakh' in query:
                # telling the user that we are translating the text to the kazakh
                speak("translating to kazakh")
                # getting the text from the user and replacing the "to kazakh" with nothing so that we can translate the text
                query = query.replace("to kazakh", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the kazakh and storing the result in a variable named result
                result = translator.translate(query, dest='kk')
                # speaking and printing the result
                sp(result.text)

            # translate to the khmer
            elif 'khmer' in query:

                # telling the user that we are translating the text to the khmer
                speak("translating to khmer")
                # getting the text from the user and replacing the "to khmer" with nothing so that we can translate the text
                query = query.replace("to khmer", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the khmer and storing the result in a variable named result
                result = translator.translate(query, dest='km')
                # speaking and printing the result
                sp(result.text)

            # translate to the korean
            elif 'korean' in query:
                # telling the user that we are translating the text to the korean
                speak("translating to korean")
                # getting the text from the user and replacing the "to korean" with nothing so that we can translate the text
                query = query.replace("to korean", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the korean and storing the result in a variable named result
                result = translator.translate(query, dest='ko')
                # speaking and printing the result
                sp(result.text)
            # translate to the kyrgyz
            elif 'kyrgyz' in query:

                # telling the user that we are translating the text to the kyrgyz
                speak("translating to kyrgyz")
                # getting the text from the user and replacing the "to kyrgyz" with nothing so that we can translate the text
                query = query.replace("to kyrgyz", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the kyrgyz and storing the result in a variable named result
                result = translator.translate(query, dest='ky')
                # speaking and printing the result
                sp(result.text)

            # translate to the lao
            elif 'lao' in query:
                # telling the user that we are translating the text to the lao
                speak("translating to lao")
                # getting the text from the user and replacing the "to lao" with nothing so that we can translate the text
                query = query.replace("to lao", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the lao and storing the result in a variable named result
                result = translator.translate(query, dest='lo')
                # speaking and printing the result
                sp(result.text)

            # translate to the latin
            elif 'latin' in query:
                # telling the user that we are translating the text to the latin
                speak("translating to latin")
                # getting the text from the user and replacing the "to latin" with nothing so that we can translate the text
                query = query.replace("to latin", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the latin and storing the result in a variable named result
                result = translator.translate(query, dest='la')
                # speaking and printing the result
                sp(result.text)

            # translate to the latvian
            elif 'latvian' in query:

                # telling the user that we are translating the text to the latvian
                speak("translating to latvian")
                # getting the text from the user and replacing the "to latvian" with nothing so that we can translate the text
                query = query.replace("to latvian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the latvian and storing the result in a variable named result
                result = translator.translate(query, dest='lv')
                # speaking and printing the result
                sp(result.text)

            # translate to the lithuanian
            elif 'lithuanian' in query:
                # telling the user that we are translating the text to the lithuanian
                speak("translating to lithuanian")
                # getting the text from the user and replacing the "to lithuanian" with nothing so that we can translate the text
                query = query.replace("to lithuanian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the lithuanian and storing the result in a variable named result
                result = translator.translate(query, dest='lt')
                # speaking and printing the result
                sp(result.text)

            # translate to the luxembourgish
            elif 'luxembourgish' in query:
                # telling the user that we are translating the text to the luxembourgish
                speak("translating to luxembourgish")
                # getting the text from the user and replacing the "to luxembourgish" with nothing so that we can translate the text
                query = query.replace("to luxembourgish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the luxembourgish and storing the result in a variable named result
                result = translator.translate(query, dest='lb')
                # speaking and printing the result
                sp(result.text)

            # translate to the macedonian
            elif 'macedonian' in query:
                # telling the user that we are translating the text to the macedonian
                speak("translating to macedonian")
                # getting the text from the user and replacing the "to macedonian" with nothing so that we can translate the text
                query = query.replace("to macedonian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the macedonian and storing the result in a variable named result
                result = translator.translate(query, dest='mk')
                # speaking and printing the result
                sp(result.text)

            # translate to the malagasy
            elif 'malagasy' in query:
                # telling the user that we are translating the text to the malagasy
                speak("translating to malagasy")
                # getting the text from the user and replacing the "to malagasy" with nothing so that we can translate the text
                query = query.replace("to malagasy", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the malagasy and storing the result in a variable named result
                result = translator.translate(query, dest='mg')
                # speaking and printing the result
                sp(result.text)

            # translate to the malay
            elif 'malay' in query:
                # telling the user that we are translating the text to the malay
                speak("translating to malay")
                # getting the text from the user and replacing the "to malay" with nothing so that we can translate the text
                query = query.replace("to malay", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the malay and storing the result in a variable named result
                result = translator.translate(query, dest='ms')
                # speaking and printing the result
                sp(result.text)

            # translate to the malayalam
            elif 'malayalam' in query:
                # telling the user that we are translating the text to the malayalam
                speak("translating to malayalam")
                # getting the text from the user and replacing the "to malayalam" with nothing so that we can translate the text
                query = query.replace("to malayalam", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the malayalam and storing the result in a variable named result
                result = translator.translate(query, dest='ml')
                # speaking and printing the result
                sp(result.text)

            # translate to the maltese
            elif 'maltese' in query:
                # telling the user that we are translating the text to the maltese
                speak("translating to maltese")
                # getting the text from the user and replacing the "to maltese" with nothing so that we can translate the text
                query = query.replace("to maltese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the maltese and storing the result in a variable named result
                result = translator.translate(query, dest='mt')
                # speaking and printing the result
                sp(result.text)

            # translate to the maori
            elif 'maori' in query:
                # telling the user that we are translating the text to the maori
                speak("translating to maori")
                # getting the text from the user and replacing the "to maori" with nothing so that we can translate the text
                query = query.replace("to maori", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the maori and storing the result in a variable named result
                result = translator.translate(query, dest='mi')
                # speaking and printing the result
                sp(result.text)

            # translate to the marathi
            elif 'marathi' in query:
                # telling the user that we are translating the text to the marathi
                speak("translating to marathi")
                # getting the text from the user and replacing the "to marathi" with nothing so that we can translate the text
                query = query.replace("to marathi", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the marathi and storing the result in a variable named result
                result = translator.translate(query, dest='mr')
                # speaking and printing the result
                sp(result.text)

            # translate to the mongolian
            elif 'mongolian' in query:
                # telling the user that we are translating the text to the mongolian
                speak("translating to mongolian")
                # getting the text from the user and replacing the "to mongolian" with nothing so that we can translate the text
                query = query.replace("to mongolian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the mongolian and storing the result in a variable named result
                result = translator.translate(query, dest='mn')
                # speaking and printing the result
                sp(result.text)

            # translate to the myanmar
            elif 'myanmar' in query:
                # telling the user that we are translating the text to the myanmar
                speak("translating to myanmar")
                # getting the text from the user and replacing the "to myanmar" with nothing so that we can translate the text
                query = query.replace("to myanmar", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the myanmar and storing the result in a variable named result
                result = translator.translate(query, dest='my')
                # speaking and printing the result
                sp(result.text)

            # translate to the burmese
            elif 'burmese' in query:
                # telling the user that we are translating the text to the burmese
                speak("translating to burmese")
                # getting the text from the user and replacing the "to burmese" with nothing so that we can translate the text
                query = query.replace("to burmese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the burmese and storing the result in a variable named result
                result = translator.translate(query, dest='my')
                # speaking and printing the result
                sp(result.text)

            # translate to the nepali
            elif 'nepali' in query:
                # telling the user that we are translating the text to the nepali
                speak("translating to nepali")
                # getting the text from the user and replacing the "to nepali" with nothing so that we can translate the text
                query = query.replace("to nepali", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the nepali and storing the result in a variable named result
                result = translator.translate(query, dest='ne')
                # speaking and printing the result
                sp(result.text)

            # translate to the norwegian
            elif 'norwegian' in query:
                # telling the user that we are translating the text to the norwegian
                speak("translating to norwegian")
                # getting the text from the user and replacing the "to norwegian" with nothing so that we can translate the text
                query = query.replace("to norwegian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the norwegian and storing the result in a variable named result
                result = translator.translate(query, dest='no')
                # speaking and printing the result
                sp(result.text)

            # translate to the odia
            elif 'odia' in query:
                # telling the user that we are translating the text to the odia
                speak("translating to odia")
                # getting the text from the user and replacing the "to odia" with nothing so that we can translate the text
                query = query.replace("to odia", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the odia and storing the result in a variable named result
                result = translator.translate(query, dest='or')
                # speaking and printing the result
                sp(result.text)

            # translate to the pashto
            elif 'pashto' in query:
                # telling the user that we are translating the text to the pashto
                speak("translating to pashto")
                # getting the text from the user and replacing the "to pashto" with nothing so that we can translate the text
                query = query.replace("to pashto", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the pashto and storing the result in a variable named result
                result = translator.translate(query, dest='ps')
                # speaking and printing the result
                sp(result.text)

            # translate to the persian
            elif 'persian' in query:
                # telling the user that we are translating the text to the persian
                speak("translating to persian")
                # getting the text from the user and replacing the "to persian" with nothing so that we can translate the text
                query = query.replace("to persian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the persian and storing the result in a variable named result
                result = translator.translate(query, dest='fa')
                # speaking and printing the result
                sp(result.text)

            # translate to the polish
            elif 'polish' in query:
                # telling the user that we are translating the text to the polish
                speak("translating to polish")
                # getting the text from the user and replacing the "to polish" with nothing so that we can translate the text
                query = query.replace("to polish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the polish and storing the result in a variable named result
                result = translator.translate(query, dest='pl')
                # speaking and printing the result
                sp(result.text)

            # translate to the portuguese
            elif 'portuguese' in query:
                # telling the user that we are translating the text to the portuguese
                speak("translating to portuguese")
                # getting the text from the user and replacing the "to portuguese" with nothing so that we can translate the text
                query = query.replace("to portuguese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the portuguese and storing the result in a variable named result
                result = translator.translate(query, dest='pt')
                # speaking and printing the result
                sp(result.text)
            # translate to the punjabi
            elif 'punjabi' in query:
                # telling the user that we are translating the text to the punjabi
                speak("translating to punjabi")
                # getting the text from the user and replacing the "to punjabi" with nothing so that we can translate the text
                query = query.replace("to punjabi", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the punjabi and storing the result in a variable named result
                result = translator.translate(query, dest='pa')
                # speaking and printing the result
                sp(result.text)

            # translate to the romanian
            elif 'romanian' in query:
                # telling the user that we are translating the text to the romanian
                speak("translating to romanian")
                # getting the text from the user and replacing the "to romanian" with nothing so that we can translate the text
                query = query.replace("to romanian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the romanian and storing the result in a variable named result
                result = translator.translate(query, dest='ro')
                # speaking and printing the result
                sp(result.text)

            # translate to the russian
            elif 'russian' in query:
                # telling the user that we are translating the text to the russian
                speak("translating to russian")
                # getting the text from the user and replacing the "to russian" with nothing so that we can translate the text
                query = query.replace("to russian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the russian and storing the result in a variable named result
                result = translator.translate(query, dest='ru')
                # speaking and printing the result
                sp(result.text)

            # translate to the samoan
            elif 'samoan' in query:
                # telling the user that we are translating the text to the samoan
                speak("translating to samoan")
                # getting the text from the user and replacing the "to samoan" with nothing so that we can translate the text
                query = query.replace("to samoan", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the samoan and storing the result in a variable named result
                result = translator.translate(query, dest='sm')
                # speaking and printing the result
                sp(result.text)

            # translate to the scots gaelic
            elif 'scots gaelic' in query:
                # telling the user that we are translating the text to the scots gaelic
                speak("translating to scots gaelic")
                # getting the text from the user and replacing the "to scots gaelic" with nothing so that we can translate the text
                query = query.replace("to scots gaelic", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the scots gaelic and storing the result in a variable named result
                result = translator.translate(query, dest='gd')
                # speaking and printing the result
                sp(result.text)

            # translate to the serbian
            elif 'serbian' in query:
                # telling the user that we are translating the text to the serbian
                speak("translating to serbian")
                # getting the text from the user and replacing the "to serbian" with nothing so that we can translate the text
                query = query.replace("to serbian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the serbian and storing the result in a variable named result
                result = translator.translate(query, dest='sr')
                # speaking and printing the result
                sp(result.text)

            # translate to the sesotho
            elif 'sesotho' in query:
                # telling the user that we are translating the text to the sesotho
                speak("translating to sesotho")
                # getting the text from the user and replacing the "to sesotho" with nothing so that we can translate the text
                query = query.replace("to sesotho", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the sesotho and storing the result in a variable named result
                result = translator.translate(query, dest='st')
                # speaking and printing the result
                sp(result.text)

            # translate to the shona
            elif 'shona' in query:
                # telling the user that we are translating the text to the shona
                speak("translating to shona")
                # getting the text from the user and replacing the "to shona" with nothing so that we can translate the text
                query = query.replace("to shona", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the shona and storing the result in a variable named result
                result = translator.translate(query, dest='sn')
                # speaking and printing the result
                sp(result.text)

            # translate to the sindhi
            elif 'sindhi' in query:
                # telling the user that we are translating the text to the sindhi
                speak("translating to sindhi")
                # getting the text from the user and replacing the "to sindhi" with nothing so that we can translate the text
                query = query.replace("to sindhi", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the sindhi and storing the result in a variable named result
                result = translator.translate(query, dest='sd')
                # speaking and printing the result
                sp(result.text)

            # translate to the sinhala
            elif 'sinhala' in query:
                # telling the user that we are translating the text to the sinhala
                speak("translating to sinhala")
                # getting the text from the user and replacing the "to sinhala" with nothing so that we can translate the text
                query = query.replace("to sinhala", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the sinhala and storing the result in a variable named result
                result = translator.translate(query, dest='si')
                # speaking and printing the result
                sp(result.text)

            # translate to the slovak
            elif 'slovak' in query:
                # telling the user that we are translating the text to the slovak
                speak("translating to slovak")
                # getting the text from the user and replacing the "to slovak" with nothing so that we can translate the text
                query = query.replace("to slovak", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the slovak and storing the result in a variable named result
                result = translator.translate(query, dest='sk')
                # speaking and printing the result
                sp(result.text)

            # translate to the slovenian
            elif 'slovenian' in query:
                # telling the user that we are translating the text to the slovenian
                speak("translating to slovenian")
                # getting the text from the user and replacing the "to slovenian" with nothing so that we can translate the text
                query = query.replace("to slovenian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the slovenian and storing the result in a variable named result
                result = translator.translate(query, dest='sl')
                # speaking and printing the result
                sp(result.text)

            # translate to the somali
            elif 'somali' in query:
                # telling the user that we are translating the text to the somali
                speak("translating to somali")
                # getting the text from the user and replacing the "to somali" with nothing so that we can translate the text
                query = query.replace("to somali", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the somali and storing the result in a variable named result
                result = translator.translate(query, dest='so')
                # speaking and printing the result
                sp(result.text)

            # translate to the spanish
            elif 'spanish' in query:

                # telling the user that we are translating the text to the spanish
                speak("translating to spanish")
                # getting the text from the user and replacing the "to spanish" with nothing so that we can translate the text
                query = query.replace("to spanish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the spanish and storing the result in a variable named result
                result = translator.translate(query, dest='es')
                # speaking and printing the result
                sp(result.text)

            # translate to the sundanese
            elif 'sundanese' in query:
                # telling the user that we are translating the text to the sundanese
                speak("translating to sundanese")
                # getting the text from the user and replacing the "to sundanese" with nothing so that we can translate the text
                query = query.replace("to sundanese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the sundanese and storing the result in a variable named result
                result = translator.translate(query, dest='su')
                # speaking and printing the result
                sp(result.text)

            # translate to the swahili
            elif 'swahili' in query:
                # telling the user that we are translating the text to the swahili
                speak("translating to swahili")
                # getting the text from the user and replacing the "to swahili" with nothing so that we can translate the text
                query = query.replace("to swahili", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the swahili and storing the result in a variable named result
                result = translator.translate(query, dest='sw')
                # speaking and printing the result
                sp(result.text)

            # translate to the swedish
            elif 'swedish' in query:
                # telling the user that we are translating the text to the swedish
                speak("translating to swedish")
                # getting the text from the user and replacing the "to swedish" with nothing so that we can translate the text
                query = query.replace("to swedish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the swedish and storing the result in a variable named result
                result = translator.translate(query, dest='sv')
                # speaking and printing the result
                sp(result.text)

            # translate to the tajik
            elif 'tajik' in query:
                # telling the user that we are translating the text to the tajik
                speak("translating to tajik")
                # getting the text from the user and replacing the "to tajik" with nothing so that we can translate the text
                query = query.replace("to tajik", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the tajik and storing the result in a variable named result
                result = translator.translate(query, dest='tg')
                # speaking and printing the result
                sp(result.text)

            # translate to the tamil
            elif 'tamil' in query:
                # telling the user that we are translating the text to the tamil
                speak("translating to tamil")
                # getting the text from the user and replacing the "to tamil" with nothing so that we can translate the text
                query = query.replace("to tamil", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the tamil and storing the result in a variable named result
                result = translator.translate(query, dest='ta')
                # speaking and printing the result
                sp(result.text)

            # translate to the telugu
            elif 'telugu' in query:
                # telling the user that we are translating the text to the telugu
                speak("translating to telugu")
                # getting the text from the user and replacing the "to telugu" with nothing so that we can translate the text
                query = query.replace("to telugu", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the telugu and storing the result in a variable named result
                result = translator.translate(query, dest='te')
                # speaking and printing the result
                sp(result.text)

            # translate to the thai
            elif 'thai' in query:
                # telling the user that we are translating the text to the thai
                speak("translating to thai")
                # getting the text from the user and replacing the "to thai" with nothing so that we can translate the text
                query = query.replace("to thai", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the thai and storing the result in a variable named result
                result = translator.translate(query, dest='th')
                # speaking and printing the result
                sp(result.text)

            # translate to the turkish
            elif 'turkish' in query:
                # telling the user that we are translating the text to the turkish
                speak("translating to turkish")
                # getting the text from the user and replacing the "to turkish" with nothing so that we can translate the text
                query = query.replace("to turkish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the turkish and storing the result in a variable named result
                result = translator.translate(query, dest='tr')
                # speaking and printing the result
                sp(result.text)

            # translate to the ukrainian
            elif 'ukrainian' in query:
                # telling the user that we are translating the text to the ukrainian
                speak("translating to ukrainian")
                # getting the text from the user and replacing the "to ukrainian" with nothing so that we can translate the text
                query = query.replace("to ukrainian", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the ukrainian and storing the result in a variable named result
                result = translator.translate(query, dest='uk')
                # speaking and printing the result
                sp(result.text)

            # translate to the urdu
            elif 'urdu' in query:
                # telling the user that we are translating the text to the urdu
                speak("translating to urdu")
                # getting the text from the user and replacing the "to urdu" with nothing so that we can translate the text
                query = query.replace("to urdu", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the urdu and storing the result in a variable named result
                result = translator.translate(query, dest='ur')
                # speaking and printing the result
                sp(result.text)

            # translate to the uyghur
            elif 'uyghur' in query:
                # telling the user that we are translating the text to the uyghur
                speak("translating to uyghur")
                # getting the text from the user and replacing the "to uyghur" with nothing so that we can translate the text
                query = query.replace("to uyghur", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the uyghur and storing the result in a variable named result
                result = translator.translate(query, dest='ug')
                # speaking and printing the result
                sp(result.text)

            # translate to the uzbek
            elif 'uzbek' in query:
                # telling the user that we are translating the text to the uzbek
                speak("translating to uzbek")
                # getting the text from the user and replacing the "to uzbek" with nothing so that we can translate the text
                query = query.replace("to uzbek", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the uzbek and storing the result in a variable named result
                result = translator.translate(query, dest='uz')
                # speaking and printing the result
                sp(result.text)

            # translate to the vietnamese
            elif 'vietnamese' in query:
                # telling the user that we are translating the text to the vietnamese
                speak("translating to vietnamese")
                # getting the text from the user and replacing the "to vietnamese" with nothing so that we can translate the text
                query = query.replace("to vietnamese", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the vietnamese and storing the result in a variable named result
                result = translator.translate(query, dest='vi')
                # speaking and printing the result
                sp(result.text)

            # translate to the welsh
            elif 'welsh' in query:
                # telling the user that we are translating the text to the welsh
                speak("translating to welsh")
                # getting the text from the user and replacing the "to welsh" with nothing so that we can translate the text
                query = query.replace("to welsh", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the welsh and storing the result in a variable named result
                result = translator.translate(query, dest='cy')
                # speaking and printing the result
                sp(result.text)

            # translate to the xhosa
            elif 'xhosa' in query:
                # telling the user that we are translating the text to the xhosa
                speak("translating to xhosa")
                # getting the text from the user and replacing the "to xhosa" with nothing so that we can translate the text
                query = query.replace("to xhosa", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the xhosa and storing the result in a variable named result
                result = translator.translate(query, dest='xh')
                # speaking and printing the result
                sp(result.text)

            # translate to the yiddish
            elif 'yiddish' in query:
                # telling the user that we are translating the text to the yiddish
                speak("translating to yiddish")
                # getting the text from the user and replacing the "to yiddish" with nothing so that we can translate the text
                query = query.replace("to yiddish", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the yiddish and storing the result in a variable named result
                result = translator.translate(query, dest='yi')
                # speaking and printing the result
                sp(result.text)

            # translate to the yoruba
            elif 'yoruba' in query:
                # telling the user that we are translating the text to the yoruba
                speak("translating to yoruba")
                # getting the text from the user and replacing the "to yoruba" with nothing so that we can translate the text
                query = query.replace("to yoruba", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the yoruba and storing the result in a variable named result
                result = translator.translate(query, dest='yo')
                # speaking and printing the result
                sp(result.text)

            # translate to the zulu
            elif 'zulu' in query:
                # telling the user that we are translating the text to the zulu
                speak("translating to zulu")
                # getting the text from the user and replacing the "to zulu" with nothing so that we can translate the text
                query = query.replace("to zulu", "")
                # using the goslate library to translate the text
                translator = Translator()
                # translating the text to the zulu and storing the result in a variable named result
                result = translator.translate(query, dest='zu')
                # speaking and printing the result
                sp(result.text)

        elif 'close' in query:

            if 'page' in query:
                presshotkey('ctrl', 'w')
               # sp('Closed')


            elif 'app' in query or 'application' in query or 'program' in query or 'process' in query or 'window' in query or 'all tabs' in query:
                    presshotkey('alt', 'f4')
                    # sp('Closed')

            elif 'tab' in query:
                presshotkey('ctrl', 'w')
                # sp('Closed')

            elif 'window' in query:
                presshotkey('alt', 'f4')

            elif 'chrome' in query:
                sp('closing chrome')
                os.system('TASKKILL /F /IM chrome.exe')

            elif 'spotify' in query:
                sp('closing spotify')
                os.system('TASKKILL /F /IM Spotify.exe')

            elif 'youtube' in query:
                sp('closing youtube ')
                os.system('TASKKILL /F /IM chrome.exe')

            elif 'qbittorrent' in query or 'bittorrent' in query or 'torrent' in query:
                sp('closing qbittorrent')
                os.system('TASKKILL /F /IM qbittorrent.exe')

            elif 'vs code' in query:
                sp('closing vs code')
                os.system('TASKKILL /F /IM code.exe')

            elif 'github desktop' in query:
                sp('closing github desktop')
                os.system('TASKKILL /F /IM GitHubDesktop.exe')

            elif 'telegram' in query:
                sp('closing telegram')
                os.system('TASKKILL /F /IM Telegram.exe')

            elif 'whatsapp' in query:
                sp('closing whatsapp')
                os.system('TASKKILL /F /IM WhatsApp.exe')

            elif 'explorer' in query:
                sp('closing explorer')
                os.system('TASKKILL /F /IM explorer.exe')

            elif 'notepad' in query:
                sp('closing notepad')
                os.system('TASKKILL /F /IM notepad.exe')
            # all the office apps should be closed before closing the office

            # microsoft word
            elif 'word' in query:
                sp('closing word')
                os.system('TASKKILL /F /IM WINWORD.EXE')

            # writing code to close microsoft excel if microsoft excel is open and exists in query
            elif 'excel' in query:
                sp('closing excel')
                os.system('TASKKILL /F /IM EXCEL.EXE')

            # writing code to close microsoft powerpoint if microsoft powerpoint is open and exists in query
            elif 'powerpoint' in query:
                sp('closing powerpoint')
                os.system('TASKKILL /F /IM POWERPNT.EXE')

            # writing code to close microsoft outlook if microsoft outlook is open and exists in query
            elif 'outlook' in query:
                sp('closing outlook')
                os.system('TASKKILL /F /IM OUTLOOK.EXE')

            # writing code to close microsoft onenote if microsoft onenote is open and exists in query
            elif 'onenote' in query:
                sp('closing onenote')
                os.system('TASKKILL /F /IM ONENOTE.EXE')

            # writing code to close microsoft onedrive if microsoft onedrive is open and exists in query
            elif 'onedrive' in query:
                sp('closing onedrive')
                os.system('TASKKILL /F /IM OneDrive.exe')

            # writing code to close microsoft store if microsoft store is open and exists in query
            elif 'store' in query:
                sp('closing store')
                os.system('TASKKILL /F /IM STORE.EXE')

            # writing code to close microsoft office if microsoft office is open and exists in query
            elif 'office' in query:
                sp('closing office')
                os.system('TASKKILL /F /IM MICROSOFT.EXE')

            # writing code to close microsoft teams if microsoft teams is open and exists in query
            elif 'teams' in query:
                sp('closing teams')
                os.system('TASKKILL /F /IM Teams.exe')

            # writing code to close skype if skype is open and exists in query
            elif 'skype' in query:
                sp('closing skype')
                os.system('TASKKILL /F /IM skype.exe')

            # writing code to close microsoft edge if microsoft edge is open and exists in query\
            elif 'edge' in query:
                sp('closing edge')
                os.system('TASKKILL /F /IM msedge.exe')

        else:
            print("else statement is executed")
            # writing code for the queries or the commands that are not in the above list of commands. so we will ask the user
            # if he or she wants to search the query in google or wikipedia or translate the query or open the query in browser
            # or open the query in youtube or open the query in stackoverflow or open the query in github or open the query in
            # facebook or open the query in instagram or open the query in twitter or open the query in linkedin or open the query in
            # gmail or open the query in whatsapp or open the query in skype or open the query in snapchat or open the query in
            # pinterest or open the query in tinder or open the query in reddit or open the query in quora or open the query in
            # stackoverflow or open the query in amazon or open the query in flipkart or open the query in gmail or open the query in
            # yahoo or open the query in google or open the query in wikipedia or open the query in youtube or open the query in
            # stackoverflow or open the query in github or open the query in facebook or open the query in instagram or open the
            # query in twitter or open the query in linkedin or open the query in gmail or open the query in whatsapp or open the
            # query in skype or open the query in snapchat or open the query in pinterest or open the query in tinder or open the
            # query in reddit or open the query in quora or open the query in stackoverflow or open the query in amazon or open the
            # query in flipkart or open the query in gmail or open the query in yahoo or open the query in google or open the query in
            # wikipedia or open the query in youtube or open the query in stackoverflow or open the query in github or open the query
            # in facebook or open the query in instagram or open the query in twitter or open the query in linkedin or open the query
            # in gmail or open the query in whatsapp or open the query in skype or open the query in snapchat or open the query in
            # pinterest or open the query in tinder or open the query in reddit or open the query in quora or open the query in
            # stackoverflow or open the query in amazon or open the query in flipkart or open the query in gmail or open the query
            # in yahoo or open the query in google or open the query in wikipedia or open the query in youtube or open the query in
            # stackoverflow or open the query in github or open the query in facebook or open the query in instagram or open the query
            # in twitter or open the query in linkedin or open the query in gmail or open the query in whatsapp or open the query in
            # skype or open the query in snapchat or open the query in pinterest or open the query in tinder or open the query in
            if query != 'none':
                speak(
                    'sorry sir that is not assigned. do you want to search for ' + query + '?')
                print('\n')
                # asking the user to confirm the query or not
                print('say yes or no. normal command will not work.')
                print('\n')

                confirmation = takeCommand().lower()  # taking the input from the user
                # if the user says yes or yep or something similar then we will search the query in google
                if 'yes' in confirmation or 'yep' in confirmation or 'sure' in confirmation or 'yeah' in confirmation or 'absolutely' in confirmation or 'fine' in confirmation or 'looks good' in confirmation or 'okay' in confirmation:
                    print('\n')
                    # asking the user to search in which website
                    speak(
                        'do you want me to search in google, wikipedia or youtube sir?')
                    # taking the input from the user and converting it to lower case and storing it in answer4
                    answer4 = takeCommand().lower()
                    # if the user says google then we will search the query in google
                    if 'google' in answer4:
                        # telling the user that we are searching the query in google
                        speak('searching for ' + query + ' in google')
                        # opening the query in google
                        webbrowser.open('www.google.com/search?gx&q=' + query)
                    # if the user says wikipedia then we will search the query in wikipedia
                    elif 'Wikipedia' in answer4:
                        # asking the user to narrate or open the webpage
                        speak('do you want me to narrate or open webpage sir?')
                        # taking the input from the user and converting it to lower case and storing it in answer2
                        answer2 = takeCommand().lower()
                        # if the user says narrate or direct then we will narrate the query
                        if 'narrate' in answer2 or 'direct' in answer2:
                            # getting the summary of the query
                            results = wikipedia.summary(
                                query, sentences=1, auto_suggest=False)
                            # narrating the summary of the query
                            speak('according to wikipedia ' + results)
                        # if the user says web page or website or webpage then we will open the query in browser
                        elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                            # getting the page of the query
                            page1 = wikipedia.page(query, auto_suggest=False)
                            print(page1)  # printing the page of the query
                            page2 = page1.url  # getting the url of the query
                            print(page2)  # printing the url of the query
                            # telling the user that we are redirecting to the webpage
                            speak('redirecting to webpage')
                            webbrowser.get().open_new_tab(page2)  # opening the webpage of the query
                            print(page2)  # printing the url of the query
                    elif 'youtube' in answer4:  # if the user says youtube then we will search the query in youtube
                        # telling the user that we are searching the query in youtube
                        speak('searching for ' + query + 'in youtube')
                        webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' +
                                                      query)  # opening the query in youtube

                    elif 'stackoverflow' in answer4:  # if the user says stackoverflow then we will search the query in stackoverflow
                        # telling the user that we are searching the query in stackoverflow
                        speak('searching for ' + query + 'in stackoverflow')
                        webbrowser.get().open_new_tab(
                            'https://stackoverflow.com/search?q=' + query)  # opening the query in stackoverflow

                elif 'no' in query or 'not' in query or 'negative' in query:

                    # asking the user if he wants to get rick rolled
                    speak('do you want to get rick rolled sir?')
                    # taking the input from the user and converting it to lower case and storing it in answer5
                    answer5 = takeCommand().lower()
                    # if the user says yes or yep or something similar then we will get rick rolled

                    if 'yes' in answer5 or 'yep' in answer5 or 'sure' in answer5 or 'yeah' in answer5 or 'absolutely' in answer5 or 'fine' in answer5 or 'looks good' in answer5 or 'okay' in answer5:
                        # telling the user that we are rick rolling
                        speak('sir i am rick rolling you')

                        # opening the rick roll video in the browser
                        webbrowser.get().open_new_tab(
                            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

                        speak('sir i am rick rolling you')
                        # opening the rick roll video in the browser

                else:

                    # Asking user if he or she want olivia to do anything else.
                    speak('ok. anything else sir?')
