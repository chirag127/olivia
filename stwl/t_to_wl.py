from functions import *


# open the YouTube trending page
def open_trending():
    webbrowser.open('https://www.youtube.com/feed/trending')

# define a function to wait for the trending page to load


def wait_for_trending_page():
    sleep(3)

# click the three dots to the right of the video title on the trending page


def click_three_dots_trending():
    pyautogui.click(x=1482, y=393)

# click the checkbox to select all the videos on the trending page


def click_checkbox_trending():
    pyautogui.click(x=1595, y=403)

# click on the save to watch later button on the trending page


def click_save_to_wl_trending():
    pyautogui.click(x=1623, y=529)


def main():
    open_trending()

    wait_for_trending_page()

    click_three_dots_trending()

    sleep(0.1)

    click_checkbox_trending()

    sleep(0.1)

    click_save_to_wl_trending()


if __name__ == '__main__':

    while True:
        wait_for_do_key()

        main()
