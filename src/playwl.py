import webbrowser
from time import sleep
import pyautogui

# Physical: {X=540,Y=356}

def open_watch_later():
    webbrowser.open('https://www.youtube.com/playlist?list=WL')


def click_play_button():

    pyautogui.click(x=540, y=356)

def main():
    open_watch_later()
    sleep(5)
    click_play_button()
    