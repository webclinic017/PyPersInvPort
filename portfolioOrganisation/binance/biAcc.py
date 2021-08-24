from binance.spot.wallet import deposit_history, withdraw
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from datetime import datetime
import array
import numpy as np
import biAccConfig
import os
import pandas as pd
import logging
import pprint

pp = pprint.PrettyPrinter(indent=1)

# %%
key    = biAccConfig.key
secret = biAccConfig.secret

client = Client(key, secret)


df=pd.DataFrame(client.account()["balances"])
# print(df)
# print(df['free'>0])

df['free']=pd.to_numeric(df['free'])
df['locked']=pd.to_numeric(df['locked'])
# print(df)
# print(df['free']>0)
ndf = df[df['free']>0]
print(ndf)
symbols = [x for x in ndf['asset']]

all_combos = [x+y for x in symbols for y in symbols]
print(type(all_combos))





pairs = [x['symbol'] for x in client.exchange_info()['symbols']]


# print(pairs)

set_of_pairs = set(pairs)
set_of_all_combos = set(all_combos)
set_of_pairs_possibly_traded = set_of_pairs & set_of_all_combos

# print(type(set_of_pairs))
print(set_of_pairs_possibly_traded)




deposit_history_df = pd.DataFrame(client.deposit_history())

# pp.pprint(client.withdraw_history())
withdraw_history_df = pd.DataFrame(client.withdraw_history())


def myTrades(listOfSymbols = list, readableTime = False, csv = False):
    Trades = []
    
    def niceDates(binanceDate):
        return str(datetime.fromtimestamp(int(binanceDate/1000)))

    for x in listOfSymbols:
        Trades = Trades + client.my_trades(x)
        df = pd.DataFrame(Trades)
        arr = np.array(Trades)
    if readableTime == True: 
        df['time'] = df['time'].apply(niceDates)
    
    cwd = os.getcwd()
    path = cwd + "/{}.csv".format("biAcc")
    if csv == True: 
        return df.to_csv(path)
    else: 
        return df


myTrades(set_of_pairs_possibly_traded)
print(myTrades(set_of_pairs_possibly_traded))

print(deposit_history_df)

# %%


# %%



# trades = []
# for x in symbols: 
#     trades.append
# trade_history_df = pd.DataFrame(client.my_trades(symbols))
# print(trade_history_df)
# # pp.pprint(client.account())

# # pp.pprint(client.funding_wallet())


# # df = pd.DataFrame(client.account)
# # print(df)
# # %%