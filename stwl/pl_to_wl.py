from functions import *
import webbrowser
import pyautogui

# defining the function to open the playlist url in the browser


def open_playlist_url_of_trans_playlist():
    webbrowser.open(
        'https://www.youtube.com/playlist?list=PLrE9n-AXguljf_OCLyyGgdwJ-yW1xp3Zg')
    sleep(5)

# defining the function to click on the 3 dots on the top right corner of the playlist area at (1845,240)
# click on the 3 dots of the trans playlist


def click_on_the_three_dots_of_the_trans_playlist():
    pyautogui.click(1845, 190)
    sleep(0.5)


# defining the function to click on the checkbox of the playlist at (1600,245)
# click on the checkbox on the playlist of the trans playlist
def click_on_the_checkbox_on_the_playlist_of_the_trans_playlist():
    pyautogui.click(1600, 200)
    sleep(0.5)

# defining the function to the save to watch later button at (1600,380)
# name of the function is click on the save to watch later button on the playlist of the multi-select extension popup


def click_on_the_save_to_watch_later_button_on_the_playlist_of_the_multi_select_extension_popup():
    pyautogui.click(1600, 340)
    sleep(0.5)


def main():

    open_playlist_url_of_trans_playlist()

    click_on_the_three_dots_of_the_trans_playlist()

    click_on_the_checkbox_on_the_playlist_of_the_trans_playlist()

    click_on_the_save_to_watch_later_button_on_the_playlist_of_the_multi_select_extension_popup()


if __name__ == '__main__':

    wait_for_do_key()

    main()
