#!python3
# An auto-trader for Minecraft Hypixel Skyblock's bazaar. It works as an autoclicker.
# Enable your default texture pack. Add a .png image to images/ to the icon of the item you want to trade with the name of the item you are trading.
# This is bannable (i think), so please don't do this on the server. This was just for a programming challange.
# By Kevin Chen

import requests, time, keyboard, os, threading
import pyautogui as p

itemTrading = "WHEAT" # The item to trade
apiKey = 'b8ec178c-b211-48ea-be2f-7191e988efb7' # Your api key. Enter /api new on mc.hypixel.net.
maxTransactions = 10
currentTransactions = 0
maxTransactionAmount = 10
priceHistory = []
heldItems = 0
lastPurchase = None

def checkKeyPress():
    while True:
        if keyboard.read_key() == "x":
            os._exit(1)

keypressthread = threading.Thread(target=checkKeyPress)
keypressthread.start()

class Transaction():
    def __init__(self, ttype, amount):
        self.ttype = ttype
        self.amount = amount

def _fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData():
    statdata = _fetch("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey)
    return {'sellPrice' : statdata['products'][itemTrading]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][itemTrading]['quick_status']['buyPrice']}

def enterBazaar():
    p.click(button='right')
    buttonpos = p.locateOnScreen('images/'+itemTrading+'.png')
    p.moveTo(buttonPos)
    p.click()
    buttonpos = p.locateOnScreen('images/'+itemTrading+'.png')
    p.moveTo(buttonPos)
    p.click()
    p.move(100, 100)

def sell(amount):
    p.click('images/sell.png', button='right')
    time.sleep(1)
    p.move(100, 100)
    for i in range(0, amount):
        time.sleep(0.1)
        sellbuttonpos = p.locateOnScreen('images/'+itemTrading+'.png')
        p.moveTo(sellbuttonpos)
        time.sleep(0.1)
        p.click()
        time.sleep(1)
        p.move(100, 100)
    global heldItems
    heldItems -= amount
        
def buy(amount):
    p.click('images/buy.png')
    time.sleep(1)
    p.move(100, 100)
    for i in range(0, amount):
        time.sleep(0.1)
        buybuttonpos = p.locateOnScreen('images/'+itemTrading+'.png')
        p.moveTo(buybuttonpos)
        time.sleep(0.1)
        p.click()
        time.sleep(1)
        p.move(100, 100)

    backbuttonpos = p.locateOnScreen('images/back.png')
    p.moveTo(backbuttonpos)
    p.click()
    global heldItems
    heldItems += amount

def calculateTranscation():
    priceHistory.append(fetchPriceData())
    if heldItems == 0:
        lastPurchase = priceHistory[-1]
        return Transaction('buy', maxTransactionAmount)
    elif heldItems > 0 and lastPurchase.get('buyPrice') < priceHistory[-1].get('sellPrice'):
        return Transaction('sell', heldItems)

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
    time.sleep(10)
    trade()


