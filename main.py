import requests ,subprocess
from pystyle import *

#methode of auth you cant turn it to False
KEY = True
IP = True
HWID = True

#modif
PASTEBIN = "YOUR PASTEBIN LINK"
WEBHOOK = "YOUR WEEBHOOK"

banner = Center.XCenter(Colorate.Horizontal(Colors.blue_to_cyan,"""
    
 █████  ██    ██ ████████ ██   ██ 
██   ██ ██    ██    ██    ██   ██ 
███████ ██    ██    ██    ███████ 
██   ██ ██    ██    ██    ██   ██ 
██   ██  ██████     ██    ██   ██ 
                                  
simple auth -> By PLATIPUS#2535"""))
req = requests.get("https://api.ipify.org").text

def web():
    data = {
        "content" : "@everyone",
        "avatar_url": "https://platipuss.xyz/pdp.jpg",
        "username": 'Logs'
    }

    data["embeds"] = [
        {
            "title" : "Key login",
            "color": 16711680,
            "description": f"Suspicious connection detect ! ip {req}"
        }
    ]

    requests.post(WEBHOOK, json=data)

def key():
    resp = input(banner+"\nkey > ")
    url = requests.get(PASTEBIN).text

    if resp in url.split():
        input(banner + "\nauthenticate successfully")
    else:
        web()
        input(banner + "\nWrong Key!")

def ip(req):
    print(banner)
    url = requests.get(PASTEBIN).text

    if req in url.split():
           input(banner + "\nauthenticate successfully")

    else:
        web()
        input(banner + "\nNot Whitelised")

def hwid():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    whitelist = requests.get(PASTEBIN).text
    
    if hwid in whitelist.split():
        input(banner + "\nauthenticate successfully")
    else:
        web()
        input(banner + "\nNot Whitelised")

if KEY == True:
    key()

if IP == True:
    ip(req)

if HWID == True:
    hwid()
