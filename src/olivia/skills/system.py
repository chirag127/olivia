"""System monitoring: CPU, RAM, disk, battery, IP."""

import json

from olivia.core.speech import sp, speak


def cpu():
    import psutil

    speak("CPU is at " + str(psutil.cpu_percent()) + "%")


def ram():
    import psutil

    speak("RAM is at " + str(psutil.virtual_memory()[2]) + "%")


def disk():
    import psutil

    speak("Disk is at " + str(psutil.disk_usage("/")[3]) + "%")


def battery():
    import psutil

    speak("Battery is at " + str(psutil.sensors_battery().percent) + "%")


def battery_status():
    import psutil

    plugged = psutil.sensors_battery().power_plugged
    speak("Battery is charging" if plugged else "Battery is discharging")


def give_ip():
    """Speak the public IP address."""
    import requests

    res = requests.get("https://api.ipify.org?format=json", timeout=10)
    ip = json.loads(res.text)["ip"]
    sp("Your IP address is ")
    sp(ip)
