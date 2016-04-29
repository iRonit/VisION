#!/usr/bin/python
import os
def wifi_is_connected():
    wifi_name = os.popen('sudo iwlist wlan0 scan | grep ESSID | cut -f2 -d: ').read()
    if wifi_name.trim()=="":
        return False
    return True
