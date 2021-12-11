import pyautogui
from functions import *


# defining the function to click on the first video in the watch later playlist
def play_youtube_watch_later_playlist():
    pyautogui.click(x=1000, y=270)


def main():

    play_youtube_watch_later_playlist()


if __name__ == "__main__":
    main()
