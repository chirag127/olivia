# this python script will remove the watched video from the list from the https://www.youtube.com/playlist?list=WL

# import the necessary modules
from functions import *

x = 0

# define a function to open the youtube watch later playlist url in the browser = https://www.youtube.com/playlist?list=WL
# name of the function is open_youtube_watch_later_playlist


def open_youtube_watch_later_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=WL")


# define a function to click on the three dots button on the watch later playlist to remove watched videos
# name of the function is click_on_three_dots_button_on_watch_later_playlist_to_remove_watched_videos
def click_on_three_dots_button_on_watch_later_playlist_to_remove_watched_videos():
    # click on the three dots button on the watch later playlist to remove watched videos
    pyautogui.click(x=400, y=580 + x)


# define a function to click on the remove watched videos button on the watch later playlist to remove watched videos
# name of the function is click_on_remove_watched_videos_button_on_watch_later_playlist_to_remove_watched_videos
def click_on_remove_watched_videos_button_on_watch_later_playlist_to_remove_watched_videos():
    pyautogui.click(x=500, y=680 + x)


# defining the function to click on the remove button in the popup on the watch later playlist to remove watched videos
# name of the function is click_on_remove_button_in_popup_on_watch_later_playlist_to_remove_watched_videos
def click_on_remove_button_in_popup_on_watch_later_playlist_to_remove_watched_videos():
    pyautogui.click(x=1140, y=616 + x)


# defining teh main function
def main():

    open_youtube_watch_later_playlist()

    sleep(5)

    # click_on_three_dots_button_on_watch_later_playlist_to_remove_watched_videos()

    # sleep(0.5)

    click_on_remove_watched_videos_button_on_watch_later_playlist_to_remove_watched_videos()

    sleep(1)

    click_on_remove_button_in_popup_on_watch_later_playlist_to_remove_watched_videos()


if __name__ == "__main__":

    wait_for_do_key()

    main()
