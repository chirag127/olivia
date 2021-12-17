from functions import *
import webbrowser
import s_to_wl

# Open the web browser and navigate to the URL https://www.youtube.com/feed/subscriptions in Edge


def open_subscriptions_page_in_edge():
    webbrowser.register(
        "edge",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        ),
    )

    webbrowser.get("edge").open("https://www.youtube.com/feed/subscriptions")


if __name__ == "__main__":

    open_subscriptions_page_in_edge()

    s_to_wl.main()
