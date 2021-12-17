import keyboard
import pyautogui
import webbrowser

from time import sleep


# defining the function to wait for user to press z key
def wait_for_do_key():
    while True:
        if keyboard.is_pressed("alt + d"):
            break
        sleep(0.1)


# defining the function to close the tab


def close_tab():
    pyautogui.hotkey("ctrl", "w")
