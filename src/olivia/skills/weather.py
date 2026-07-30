"""Weather lookups and internet speed test."""

import re

from olivia.core import config
from olivia.core.speech import speak


def current_weather(query):
    """Speak current weather for a city (from 'current weather in X')."""
    m = re.search("current weather in (.*)", query)
    if not m:
        return
    city = m.group(1)
    from pyowm import OWM

    owm = OWM(config.OPENWEATHER_API_KEY)
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(city)
    w = obs.weather
    status = w.detailed_status
    temp = w.temperature("celsius")
    speak(
        "Current weather in %s is %s. The maximum temperature is %0.2f and the "
        "minimum temperature is %0.2f degree celcius"
        % (city, status, temp["temp_max"], temp["temp_min"])
    )


def fast_speed_test():
    """Run an internet speed test and speak the down/up rates."""
    import speedtest

    st = speedtest.Speedtest()
    down = st.download() / 1_000_000
    up = st.upload() / 1_000_000
    speak(f"Download speed is {down:.2f} megabits per second")
    speak(f"Upload speed is {up:.2f} megabits per second")
