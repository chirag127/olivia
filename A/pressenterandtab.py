from tkinter.constants import W
import pyautogui
from time import sleep


def presskey(key):
    pyautogui.press(key)


if __name__ == '__main__':

    sleep(5)

    while True:

        presskey('enter')

        sleep(2)

        presskey('tab')
