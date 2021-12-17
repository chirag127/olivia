import pyautogui
import webbrowser
from functions import *
import pl_to_wl
import t_to_wl
import removewatchedvideo

# Open the web browser and navigate to the URL https://www.youtube.com/feed/subscriptions


def open_subscriptions_page_in_default_browser():
    webbrowser.open("https://www.youtube.com/feed/subscriptions")


# defining the function to click on the 3 dots button at (x,y) coordinates = (680,480)
def click_on_three_dots_on_subcription():
    pyautogui.moveTo(680, 461)
    pyautogui.click()


# defining the function to click on the checkbox button to select all videos on the page at (x,y) coordinates = (730,490)
def click_on_checkbox_on_subcription():
    pyautogui.moveTo(730, 480)
    pyautogui.click()


# defining the function to click on the "save to wl" button at (x,y) coordinates
def click_on_save_to_wl_on_subcription():
    pyautogui.moveTo(730, 600)
    pyautogui.click()


def cstowl():

    open_subscriptions_page_in_default_browser()

    sleep(3)

    click_on_three_dots_on_subcription()

    sleep(0.5)

    click_on_checkbox_on_subcription()

    sleep(0.5)

    click_on_save_to_wl_on_subcription()


def main():

    cstowl()

    sleep(1)

    close_tab()

    pl_to_wl.main()

    sleep(1)

    close_tab()

    t_to_wl.main()

    sleep(1)

    close_tab()

    removewatchedvideo.main()


if __name__ == "__main__":

    main()
