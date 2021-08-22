from binance.spot.wallet import withdraw
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
print(df)
# print(df['free'>0])

df['free']=pd.to_numeric(df['free'])
df['locked']=pd.to_numeric(df['locked'])
# print(df)
# print(df['free']>0)
ndf = df[df['free']>0]
print(ndf)


# df = pd.DataFrame(client.account)
# print(df)
# %%