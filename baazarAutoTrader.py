# An auto-trader for Minecraft Hypixel Skyblock's bazaar. It works as an autoclicker.
# Enable your default texture pack.
# This is bannable (i think), so please don't do this on the server. This was just for a programming challange.

import requests
import pyautogui as p

itemTrading = "BROWN_MUSHROOM" # The item to trade
apiKey = '9be4bedf-a55a-4fcb-9155-969b9a1d47c2' # Your api key. Enter /api new on mc.hypixel.net.
maxTransactions = 10
currentTransactions = 0

def _fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData():
    statdata = _fetch("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey)
    return {'sellPrice' : statdata['products'][item_name]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][item_name]['quick_status']['buyPrice']}

def sell(amount):
    p.

while 


