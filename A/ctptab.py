import keyboard
from time import sleep
import pyautogui


def main():
    pyautogui.press("enter")

    sleep(3)

    pyautogui.press("tab")


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("q"):

            while True:
                main()
        else:
            sleep(0.1)
