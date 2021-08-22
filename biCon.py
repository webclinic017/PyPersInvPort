from binance.spot.wallet import withdraw
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from datetime import datetime
import array
import numpy as np
import config
import os
import pandas as pd
import logging


# %%
key    = config.key
secret = config.secret

client = Client(key, secret)

print(client.account())
# # depositHist = client.deposit_history()
# # withdrawHist = client.withdraw_history()
# # depositDF = pd.DataFrame(depositHist)
# # withdrawDF = pd.DataFrame(withdrawHist)
# print(depositDF)
# print(withdrawDF)

# %%



# Depositcollist = depositDF.columns
# Withdrawcollist= withdrawDF.columns

# print(Depositcollist)
# print(Withdrawcollist)


# %%

pairs = ["ETHBTC", "ETHUSDT", "BTCUSDT"]


def myTrades(listOfSymbols = list, readableTime = False, csv = False):
    Trades = []
    Dates = []
    BTCprice = []
    ETHprice = []
    
    for symbol in listOfSymbols:
        Trades = Trades + client.my_trades(symbol)
        df = pd.DataFrame(Trades)
        arr = np.array(Trades)
    if readableTime == True: 
        for binanceDate in df['time']: 
            date = str(datetime.fromtimestamp(int(binanceDate/1000)))
            print(date)
            Dates.append(date)
        df['time'] = pd.Series(Dates)
    else: 
        pass 

    for i in range(len(df['symbol'])):
        if df['symbol'][i] == "ETHUSDT":       
            btcprice = client.klines("BTCUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            ethprice = client.klines("ETHUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            BTCprice.append(btcprice[0][1])
            ETHprice.append(df['price'][i])

        elif df['symbol'][i] == "ETHBTC":
            btcprice = client.klines("BTCUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            ethprice = client.klines("ETHUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            BTCprice.append(btcprice[0][1])
            ETHprice.append(ethprice[0][1])

        elif df['symbol'][i] == "BTCUSDT":
            btcprice = client.klines("BTCUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            ethprice = client.klines("ETHUSDT", "1m", startTime = df['time'][i], endTime = df['time'][i]+60*1000)
            BTCprice.append(df['price'][i])
            ETHprice.append(ethprice[0][1])
    
    df['BTCprice'] = BTCprice
    df['ETHprice'] = ETHprice 

    cwd = os.getcwd()
    path = cwd + "/{}.csv".format("biCon")
    if csv == True: 
        return df.to_csv(path)
    else: 
        return df

myTrades(pairs, csv=True)

# %%


# %%

