from Olivia import *


def enjoy_watching():

    while True:

        query = takeCommand().lower()

        print("In while loop of the play video")

        if query == "bye" or query == "goodbye" or query == "bye bye":

            sp("Bye Sir")

            exit()

        elif (
            "pause" in query
            or "pass" in query
            or "stop" in query
            or "resume" in query
            or "continue" in query
            or "play" in query
        ):

            pyautogui.press("space")

        # go to the next tab by pressing control + tab

        # if the query contains 'next tab' or 'next tab'

        # if the query contains not this then check next elif statement

        elif "next" in query:

            # go to next tab by pressing control + tab

            if "tab" in query:

                pyautogui.hotkey("ctrl", "tab")

            # go to next frame by pressing .

            elif "frame" in query:

                pyautogui.press(".")

            else:

                # go to next video by pressing shift + n

                pyautogui.hotkey("shift", "n")

        elif "skip" in query and "video" in query:

            pyautogui.hotkey("shift", "n")

        # go to the previous tab by pressing control + shift + tab

        # if the query contains 'previous tab' or 'previous tab'

        # if the query contains not this then check next elif statement

        elif "previous" in query:

            # if the query contains 'tab' then go to previous tab by pressing control + shift + tab

            if "tab" in query:

                pyautogui.hotkey("ctrl", "shift", "tab")

            # go to previous frame by pressing ,

            elif "frame" in query:

                pyautogui.press(",")

            else:

                # go to previous video by pressing shift + p

                pyautogui.hotkey("shift", "p")

        # reload the video by pressing control + r if the

        # query contains 'reload' or 'refresh' or 'reload' or 'restart' or 'reboot'

        # if the query contains not this then check next elif statement

        elif (
            "reload" in query
            or "refresh" in query
            or "reload" in query
            or "restart" in query
            or "reboot" in query
            and "tab" in query
        ):

            pyautogui.hotkey("ctrl", "r")

        # mute the video by pressing control + m if the query contains 'mute' or 'unmute' or 'mute' or 'unmute'

        # if the query contains not this then check next elif statement

        elif "mute" in query or "unmute" in query:

            pyautogui.hotkey("ctrl", "m")

        # enter the miniplayer by pressing i

        # if the query contains 'miniplayer' or 'mini player' or 'miniplayer on' or 'mini player on' or 'miniplayer off' or 'mini player off'

        elif "mini" in query and "player" in query:

            pyautogui.press("i")

        # replay the video by pressing home button if the query contains 'replay' or 'replay' or 'replay' or 'replay' or 'replay' or 'replay'

        elif "replay" in query:

            pyautogui.press("home")

        # dislike the video by pressing d if the query contains 'dislike'

        elif "dislike" in query:

            pyautogui.press("d")

            print("Disliked the video")

            sleep(0.1)

            pyautogui.hotkey("shift", "n")

        # like the video by pressing s if the query contains 'like'

        elif "like" in query:

            pyautogui.hotkey("s")

            print("Liked the video")

        # seek backward by pressing  left arrow if the query contains 'backward' or 'rewind'

        if "backward" in query or "rewind" in query:

            pyautogui.hotkey("left")

            print("Seeked backward")

        # seek forward by pressing right arrow if the query contains 'forward' or 'fast forward'

        elif "forward" in query:

            pyautogui.hotkey("right")

            print("Seeked forward")

        # move to full screen mode by pressing f

        # if the query contains 'full screen' or 'full mode' or 'full screen mode'

        # if the query contains not this then check next elif statement

        elif "full" in query and "screen" in query or "mode" in query:

            pyautogui.press("f")

            print("Moved to full screen mode")

        # move to windowed mode by pressing f

        # go to download page

        # if the query contains 'download' or 'downloads' or 'download page' or 'downloads page'

        # if the query contains not this then check next elif statement

        elif (
            "download" in query
            or "downloads" in query
            or "download page" in query
            or "downloads page" in query
        ):

            pyautogui.hotkey("ctrl", "j")

            print("Moved to download page")

        # go to the history page by pressing control + h

        # if the query contains 'history' and 'page'

        # if the query contains not this then check next elif statement

        elif "history" in query and "page" in query:

            pyautogui.hotkey("ctrl", "h")

            print("Moved to history page")

        # go to the bookmark page by pressing control + shift + o

        # if the query contains 'bookmark' and 'page'

        # if the query contains not this then check next elif statement

        elif "bookmark manager" in query or "bookmark page" in query:

            pyautogui.hotkey("ctrl", "shift", "o")

            print("Moved to bookmark page")

        # show the bookmark mark bar by pressing control + shift + b

        # if the query contains 'bookmark bar' or 'bookmark bar'

        # if the query contains not this then check next elif statement

        elif "bookmark bar" in query:

            pyautogui.hotkey("ctrl", "shift", "b")

            print("Showed the bookmark bar")

        # increase the volume by pressing up arrow

        # if the query contains 'increase volume' or 'volume up' or 'louder'

        # if the query contains not this then check next elif statement

        elif (
            "increase volume" in query
            or "volume up" in query
            or "louder" in query
        ):

            query = query.replace("increase volume by", "")
            query = query.replace("volume up by", "")
            query = query.replace("louder", "")

            if "percent" in query or "percentage" in query or "%" in query:
                query = query.replace("percent", "")
                query = query.replace("percentage", "")
                query = query.replace("%", "")

                # volume is increased by the number of percentage mentioned in the query
                # volume is increased by 5 percentage by one up press
                # volume is increased by 10 percentage by two up presses
                # volume is increased by 15 percentage by three up presses
                # volume is increased by 20 percentage by four up presses
                # volume is increased by 25 percentage by five up presses

                query = query.replace(" ", "")
                percent = int(query)

                no_of_up_presses = int(percent / 5)
                for i in range(no_of_up_presses):
                    pyautogui.press("up")
                    sleep(0.5)

                if percent > 100:
                    sp("I can only increase the volume to 100%")
                else:
                    pass

            else:
                # volume is increased by 5 percentage by one up press
                pyautogui.press("up")

        # decrease the volume by pressing down arrow

        # if the query contains 'decrease volume' or 'volume down' or 'quieter'

        # if the query contains not this then check next elif statement

        elif (
            "decrease volume" in query
            or "volume down" in query
            or "quieter" in query
        ):

            query = query.replace("decrease volume by", "")
            query = query.replace("volume down by", "")
            query = query.replace("quieter", "")

            if "percent" in query or "percentage" in query or "%" in query:
                query = query.replace("percent", "")
                query = query.replace("percentage", "")
                query = query.replace("%", "")

                # volume is decreased by the number of percentage mentioned in the query
                # volume is decreased by 5 percentage by one down press

                query = query.replace(" ", "")
                percent = int(query)
                no_of_down_presses = int(percent / 5)
                for i in range(no_of_down_presses):
                    pyautogui.press("down")
                    sleep(0.5)

            else:
                # volume is decreased by 5 percentage by one down press
                pyautogui.press("down")

            # increase the speed of the video by pressing shift + . arrow

            # if the query contains 'increase speed' or 'speed up' or 'faster'

            # if the query contains not this then check next elif statement

        elif (
            "increase speed" in query
            or "speed up" in query
            or "faster" in query
        ):
            key_to_increase_speed = "]"

            query = query.replace("increase speed by", "")
            query = query.replace("speed up by", "")
            query = query.replace("faster", "")

            if "percent" in query or "percentage" in query or "%" in query:
                query = query.replace("percent", "")
                query = query.replace("percentage", "")
                query = query.replace("%", "")

                # speed is increased by the number of percentage mentioned in the query
                # speed is increased by 5 percentage by one shift + . press
                # speed is increased by 10 percentage by two shift + . press
                # speed is increased by 15 percentage by three shift + . press
                # speed is increased by 20 percentage by four shift + . press
                # speed is increased by 25 percentage by five shift + . press

                query = query.replace(" ", "")
                percent = int(query)

                no_of_shift_dot_presses = int(percent / 25)
                for i in range(no_of_shift_dot_presses):
                    pyautogui.press(key_to_increase_speed)
                    sleep(0.5)

            else:

                # speed is increased by 25 percentage by one shift + . press
                pyautogui.press(key_to_increase_speed)

        # decrease the speed of the video by pressing shift + , arrow

        # if the query contains 'decrease speed' or 'speed down' or 'slower'

        # if the query contains not this then check next elif statement

        elif (
            "decrease speed" in query
            or "speed down" in query
            or "slower" in query
        ):

            query = query.replace("decrease speed by", "")
            query = query.replace("speed down by", "")
            query = query.replace("slower", "")

            key_to_decrease_speed = "["

            if "percent" in query or "percentage" in query or "%" in query:
                query = query.replace("percent", "")
                query = query.replace("percentage", "")
                query = query.replace("%", "")

                # speed is decreased by the number of percentage mentioned in the query
                # speed is decreased by 5 percentage by one shift + , press
                # speed is decreased by 10 percentage by two shift + , press
                # speed is decreased by 15 percentage by three shift + , press
                # speed is decreased by 20 percentage by four shift + , press
                # speed is decreased by 25 percentage by five shift + , press

                query = query.replace(" ", "")
                percent = int(query)

                no_of_shift_dot_presses = int(percent / 25)
                for i in range(no_of_shift_dot_presses):
                    pyautogui.hotkey(key_to_decrease_speed)
                    sleep(0.5)

            pyautogui.hotkey(key_to_decrease_speed)

        # exit the video by pressing alt + f4

        # if the query contains 'exit' or 'quit'

        # if the query contains not this then check next elif statement

        elif "exit" in query or "quit" in query:

            pyautogui.hotkey("alt", "f4")

            break

        # if the query contains 50% percent or 50 percent or 50% or 50 then change go to the video length to 50 percent

        # if query contains 10 percent or 10% or 10 then change go to the video length to 10 percent by pressing number pad1

        elif "10%" in query:

            pyautogui.press("1")

        elif "20%" in query:

            pyautogui.press("2")

        elif "30%" in query:

            pyautogui.press("3")

        elif "40%" in query:

            pyautogui.press("4")

        elif "50%" in query:

            pyautogui.press("5")

        elif "60%" in query:

            pyautogui.press("6")

        elif "70%" in query:

            pyautogui.press("7")

        elif "80%" in query:

            pyautogui.press("8")

        elif "90%" in query:

            pyautogui.press("9")

        elif "100%" in query:

            pyautogui.press("0")

        # close the video by pressing control + w

        # if the query contains 'close'

        # if the query contains not this then check next elif statement

        elif "close" in query and "tab" in query:

            pyautogui.hotkey("ctrl", "w")

        elif ("stop" in query and "watching" in query) or ("close" in query and "video" and "tab" not in query):

            pyautogui.hotkey("ctrl", "w")

            sp("I have closed the video")

            break

        # close other tabs by pressing control + shift + t
