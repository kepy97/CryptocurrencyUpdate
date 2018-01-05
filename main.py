# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:49:48 2018

@author: admin
"""

buy = "https://api.coinbase.com/v2/prices/LTC-USD/buy"
sell = "https://api.coinbase.com/v2/prices/LTC-USD/sell"
exchange = "https://api.coinbase.com/v2/exchange-rates?currency=USD"
trx_btc = "https://api.binance.com/api/v1/ticker/price?symbol=TRXBTC"
btc_usd = "https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT"

import time
import requests
import json
from win10toast import ToastNotifier
toaster = ToastNotifier()
from datetime import datetime
while(True):
  page = requests.get(exchange)
  json_parsed = json.loads(page.content.decode('utf-8'))
  #ltc_data = json_parsed['data']['amount']
  #print("Current Litecoin Sell values : " +ltc_data)
  
  ltc_exchange = json_parsed['data']['rates']['LTC']
  ltc_exchange = str(1/float(ltc_exchange))
  ltc_exchange = "Litecoin : " +ltc_exchange
  
  btc_exchange = json_parsed['data']['rates']['BTC']
  btc_exchange = str(1/float(btc_exchange))
  btc_exchange = "Bitcoin  : " +btc_exchange
  
  page = requests.get(trx_btc)
  json_parsed = json.loads(page.content.decode('utf-8'))
  trx_binance = json_parsed['price']
  trx_binance = float(trx_binance)
  
  page = requests.get(btc_usd)
  json_parsed = json.loads(page.content.decode('utf-8'))
  btc_binance = json_parsed['price']
  btc_binance = float(btc_binance)
  
  trx_exchange = trx_binance * btc_binance
  trx_exchange = "TRX : " + str(trx_exchange)
  
  show = ltc_exchange +"\n" + btc_exchange +"\n" + trx_exchange
  print(show)
  toaster.show_toast("Python Program Update", show, duration = 900)
  time.sleep(5)
