#!python3
# An auto-trader for Minecraft Hypixel Skyblock's bazaar. It works as an autoclicker.
# Enable your default texture pack. Add a .png image to images/ to the icon of the item you want to trade with the name of the item you are trading.
# This is bannable (i think), so please don't do this on the server. This was just for a programming challange.
# By Kevin Chen

import requests, time
import pyautogui as p

itemTrading = "WHEAT" # The item to trade
apiKey = '9be4bedf-a55a-4fcb-9155-969b9a1d47c2' # Your api key. Enter /api new on mc.hypixel.net.
maxTransactions = 10
currentTransactions = 0
priceHistory = []

class Transaction():
    def __init__(self, ttype, amount):
        self.ttype = ttype
        self.amount = amount

def _fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData():
    statdata = _fetch("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey)
    return {'sellPrice' : statdata['products'][itemTrading]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][itemTrading]['quick_status']['buyPrice']}

def sell(amount):
    p.click('sell.png', button='right')
    time.sleep(1)
    for i in range(0, amount):
        p.click(itemTrading+'.png')
        time.sleep(1)
    currentTransactions += 1
        
def buy(amount):
    p.click('buy.png')
    time.sleep(1)
    for i in range(0, amount):
        p.click(itemTrading+'.png')
        time.sleep(1)
    currentTransactions += 1
    p.click('back.png')

def calculateTranscation():
    priceHistory.append(fetchPriceData())
    return Transaction('none', 0)

def trade():
    while currentTransactions < maxTransactions:
        trans = calculateTranscation()
        if trans.ttype == 'buy':
            buy(trans.amount)
        elif trans.ttype == 'sell':
            sell(trans.amount)
        elif trans.ttype == 'none':
            continue

if __name__ == '__main__':
    trade()


