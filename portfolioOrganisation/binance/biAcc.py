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

from csv import writer

pp = pprint.PrettyPrinter(indent=1)


key    = biAccConfig.key
secret = biAccConfig.secret

client = Client(key, secret)

# %%


def myAccountBalances():
    account_balances_df = pd.DataFrame(client.account()["balances"])
    account_balances_df['free']=pd.to_numeric(account_balances_df['free'])
    account_balances_df['locked']=pd.to_numeric(account_balances_df['locked'])
    return account_balances_df

def myDepositHistory():
    deposit_history_df = pd.DataFrame(client.deposit_history())
    return deposit_history_df

def myWithdrawHistory():
    withdraw_history_df = pd.DataFrame(client.withdraw_history())
    return withdraw_history_df

def pairsPossiblyTraded():
    myAccountBalances()
    ndf = myAccountBalances()[myAccountBalances()['free']>0]
    
    symbols = [x for x in ndf['asset']]
    all_combos = [x+y for x in symbols for y in symbols]
    
    
    pairs = [x['symbol'] for x in client.exchange_info()['symbols']]
    set_of_pairs = set(pairs)
    set_of_all_combos = set(all_combos)
    # The intersection of set_of_pairs and set_of_all_combos is the set of possibly traded pairs, because some of the pairs listed may not have been traded
    set_of_pairs_possibly_traded = set_of_pairs & set_of_all_combos 
    
    return set_of_pairs_possibly_traded

set_of_pairs_possibly_traded = pairsPossiblyTraded()

def myTrades(list_of_symbols = list, sort_time = False, start_time = None, end_time = None):
    
    def niceDates(binanceDate):
        print(type(datetime.fromtimestamp(int(binanceDate/1000))))
        return datetime.fromtimestamp(int(binanceDate/1000))
    
    # Until I can learn enough python to write this more pythonically and elegantly, this will have to do for the time being
    Trades = []
    if start_time == None:
        print('There is no start time')
        if end_time == None: 
            print('There is no end time.') 
            for x in list_of_symbols:
                Trades = Trades + client.my_trades(x)
        else: 
            print('The end time is ' + str(end_time) +'.')        
            for x in list_of_symbols:
                Trades = Trades + client.my_trades(x, endTime = end_time)
    else: 
        print('The start time is ' + str(start_time) +'.') 
        if end_time == None: 
            print('There is no end time.')    
            for x in list_of_symbols:
                Trades = Trades + client.my_trades(x, startTime = start_time)
        else: 
            print('The end time is ' + str(end_time) +'.')  
            for x in list_of_symbols:
                Trades = Trades + client.my_trades(x, startTime = start_time, endTime = end_time) 
           
    df = pd.DataFrame(Trades)
    df['readable time'] = df['time'].apply(niceDates)
    arr = np.array(Trades)
    
    if sort_time == True:
        df = df.sort_values(by="time")
        
    print(df)
    return df

    
def publish_as_csv(df, name: str = 'records'):
        cwd = os.getcwd()
        path = cwd + "/{}.csv".format(name)
        return df.to_csv(path)

        
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True)
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, start_time = 1621223661011)
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, end_time =  1621223661065)
trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, start_time = 1621223661011, end_time = 1621223661171)
    
    
publish_as_csv(trades_df, name = 'first_three_records')

# # print(df)
# # print(df['free'>0])


# # print(df)
# # print(df['free']>0)
# # ndf = df[df['free']>0]
# # print(ndf)

# # print(type(set_of_pairs))



# # trades = []
# # for x in symbols: 
# #     trades.append
# # trade_history_df = pd.DataFrame(client.my_trades(symbols))
# # print(trade_history_df)
# # # pp.pprint(client.account())

# # # pp.pprint(client.funding_wallet())


# # # df = pd.DataFrame(client.account)
# # # print(df)
# # # %%