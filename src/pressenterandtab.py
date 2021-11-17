from tkinter.constants import W
import pyautogui
import time

def presskey(key):
    pyautogui.press(key)


if __name__ == '__main__':

    time.sleep(5)

    while True:

        presskey('enter')

        time.sleep(2)

        presskey('tab')



        

        



        