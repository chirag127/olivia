from functions import *
import os
import sys

# Physical: {X=676,Y=444}
# Physical: {X=736,Y=464}.\env\Scripts\activate
# Physical: {X=772,Y=542}


def add_100_to_quene():
    multiselect = pyautogui.locateOnScreen(
        os.path.join(sys.path[0], "multiselect1_add100.png")
    )
    x_three_dots = multiselect[0] + 20
    y_three_dots = multiselect[1] + 10
    # click on three dots
    pyautogui.click(x_three_dots, y_three_dots)

    # defining the function to click on the checkbox button to select all videos on the page at (x,y) coordinates = (730,490)
    pyautogui.click(x_three_dots + 50, y_three_dots + 20)
    sleep(0.05)

    # defining the function to click on the "Add to queue" button at (x,y) coordinates = (800,570)
    pyautogui.click(x_three_dots + 50, y_three_dots + 100)
    sleep(0.05)


# click on expand at 1400,680
def click_on_expand_on_subcription():
    pyautogui.moveTo(1400, 680)
    pyautogui.click()
    sleep(0.01)


# defining the function to click on the save button at (x,y) coordinates = (1350,270)
# click on the save above the queue playlist created by the addtop100toE function
def click_on_the_save_above_the_queue_playlist_created_by_the_add100totrans_function():
    pyautogui.moveTo(1350, 270)
    pyautogui.click()
    sleep(0.01)


# defining the function to click on the trans playlist at (x,y) coordinates = (880,500)
# click on the trans playlist after click on the save button above the queue playlist created by the addtop100toE function


def click_on_trans_playlist_after_click_on_the_save_button_above_the_queue_playlist_created_by_the_add100totrans_function():
    pyautogui.moveTo(880, 500)
    pyautogui.click()


def main():

    sleep(11)

    add_100_to_quene()

    sleep(5)

    click_on_expand_on_subcription()

    sleep(1)

    click_on_the_save_above_the_queue_playlist_created_by_the_add100totrans_function()

    sleep(2)

    click_on_trans_playlist_after_click_on_the_save_button_above_the_queue_playlist_created_by_the_add100totrans_function()

    sleep(2)


if __name__ == "__main__":
    while True:

        wait_for_do_key()

        main()
