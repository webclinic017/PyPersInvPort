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
import time
import json

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

# def historicallyTraded():
#     starttime = time.time()
#     listHistoricallyTradedassets = []
#     json.dumps(list)

# 1. open json file of list of previously held assets
# 2. define new assets = assets not in previously held assets
# 3. look at whether new assets have been traded 
# 4. if new assets have been traded, then those new assets to the list of assets traded
# 5. use the new list to generate records of trades

def historicallyHeldAssets(original = False):
    
    ndf = myAccountBalances()[myAccountBalances()['free']>0]
    currently_held_assets = [x for x in ndf['asset']]

    if original == True: 
        previously_held_assets = ['BTC', 'ETH', 'USDT', 'SHIB', 'CRO', 'DOGE', 'FIL']
        outfile = open("assets_held_previously.json", 'w') 
        json.dump(previously_held_assets, outfile, indent = 1)

    else: 
        content = open('assets_held_previously.json', 'r') 
        previously_held_assets = json.load(content)
        previously_held_assets = list(set(previously_held_assets + currently_held_assets))
        previously_held_assets.sort()
        content.close()
        
        outfile = open("assets_held_previously.json", 'w') 
        json.dump(previously_held_assets, outfile, indent = 1)

# def historicallyTradedPairs(original = True):
    
#     ndf = myAccountBalances()[myAccountBalances()['free']>0]
#     currently_held_assets = [x for x in ndf['asset']]

#     if original == True: 
#         historically_traded_pairs = ['BTCUSDT', 'ETH', 'USDT', 'SHIB', 'CRO', 'DOGE']
#         outfile = open("assets_held_previously.json", 'w') 
#         json.dump(previously_held_assets, outfile, indent = 1)

#     else: 
#         content = open('assets_held_previously.json', 'r') 
#         previously_held_assets = json.load(content)
#         previously_held_assets = list(set(previously_held_assets + currently_held_assets))
#         previously_held_assets.sort()
#         content.close()
        
#         outfile = open("assets_held_previously.json", 'w') 
#         json.dump(previously_held_assets, outfile, indent = 1)

    

    # assets = myAccountBalances()['asset']
    
    

    # new_assets = set(assets)-set(assets_previously_held)-set(currently_held_assets)
    # listNewAssets = list(new_assets)
    # potential_newly_traded = list(set([x + y for x in new_assets for y in base_assets] + [x + y for x in base_assets for y in new_assets]))

    # print(potential_newly_traded)
    # print(len(potential_newly_traded))
    # new_assets <- check this first
    # # newly_traded_pairs = [list of all pairs with usdt or btc or eth as base but not against an old trading asset]
    # #     check and then append and export to a list to be exported as a json.
    

    # with open("mobos.json", "r") as content:
    #     print(json.load(content))
        
    # assets_previously_held = ['BTC', 'ETH', 'USDT', 'DOGE']
    
    # f = open('mobos.json', 'r')
    # db = f.read()
    # print(db)
    # data=json.load(db)
    # print(data)
    # assets_from_json=json.load(open('mobos.json', 'r'))
    # # output_file=open('test.json', 'w')
    # print(assets_from_json)


    

    # print(type(assets_previously_held))
    # print(assets_previously_held)
    
    # assets_previously_held.sort()
    # with open("assets_previously_held.json", "w") as out_file:
    #     assets_previously_held = list(json.load(out_file))
    #     assets_previously_held.append(currently_held_assets)
    #     assets_previously_held.sort()
    #     json.dump(assets_previously_held, out_file, indent = 1)
  
    
    # with open("previously_held_assets.json", "w") as outfile:
    #     json.dump(assets_previously_held, outfile, indent = 1)
    
        # take a look at all pairs related to usdt and btc and eth
        # mew assets = assets not previously held
        # check if new assets have been traded 
        # if new assets have been traded, add them 
    



def pairsPossiblyTraded():
    starttime = time.time()
    content = open('assets_held_previously.json', 'r') 
    assets_held_previously = json.load(content)
    # If #(assets_held_previously) = n, #(all_combos) = n*(n-1).
    all_combos = [x+y for x in assets_held_previously for y in assets_held_previously if y !=x] 
    print(all_combos)
    
    
    # all_combos is essentially defined as the list of all the trading pairs that the assets that I am currently holding
    # If I sold all my DOGE into USDT, then DOGE would not appear in ndf
    # But since there is a DOGE-USDT pair, by listing all trading pairs of the assets I hold, this pair would not be accidentally omitted
    # And therefore when I search for my trading records, it would pop up.
    # all_combos = [x+y for x in symbols for y in assets if y not in symbols] + [x+y for x in assets for y in symbols if y not in assets]
        
    pairs = [x['symbol'] for x in client.exchange_info()['symbols']]
    set_of_pairs = set(pairs)
    set_of_all_combos = set(all_combos)
    # The intersection of set_of_pairs and set_of_all_combos is the set of possibly traded pairs, because some of the pairs listed may not have been traded
    set_of_pairs_possibly_traded = set_of_pairs & set_of_all_combos 
    list_of_pairs_possibly_traded = list(set_of_pairs_possibly_traded)
    
    print(len(all_combos))
    print(len(pairs))
    print(len(set_of_pairs))
    print(len(set_of_all_combos))
    print(len(set_of_pairs_possibly_traded))
    print(time.time()-starttime)
    return list_of_pairs_possibly_traded



# set_of_pairs_possibly_traded = pairsPossiblyTraded()

# --------------------------------------------------------

def myTrades(list_of_symbols = list, sort_time = False, start_time = None, end_time = None):
    programme_start_time = time.time()

    def niceDates(binanceDate):
        
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
    print("Trades obtained in: {} sec".format(time.time()-programme_start_time))
    return df

    
def publish_as_csv(df, name: str = 'records'):
        cwd = os.getcwd()
        path = cwd + "/{}.csv".format(name)
        return df.to_csv(path)



# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True)
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, start_time = 1621223661011)
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, end_time =  1621223661065)
# trades_df = myTrades(pairsPossiblyTraded(), sort_time = True, start_time = 1621223661011, end_time = 1621223661171)
    
    
# publish_as_csv(trades_df, name = 'first_three_records')

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