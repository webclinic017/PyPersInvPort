from binance.spot.wallet import deposit_history, withdraw
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from datetime import datetime
import array
import numpy as np
import biAccConfig
import os
import pandas as pd
import pprint as pp
import biAcc


key    = biAccConfig.key
secret = biAccConfig.secret

client = Client(key, secret)

pairs = biAcc.set_of_pairs_possibly_traded

for x in pairs: 
    pp.pprint(client.my_trades(x))

# # def foo(x = int, **time):
# #     print(x)
# #     print(time[start_time])
# #     print(time['end_time'])

# # foo(3, start_time = 3)
# def trades(symbols, **time):
#     if type(time['start_time']) != None:
#         print(time['start_time'])
#     if type(time['end_time']) != None:
#         print(time['end_time'])
#     for x in symbols:
#         client.my_trades(x, startTime=time['start_time'])

# trades(pairs, start_time=1621223661011)