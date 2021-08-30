
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


first_three_records_pd = pd.read_csv('first_three_records.csv')
full_records_pd = pd.read_csv('full_records.csv')

print(first_three_records_pd['time'].equals(full_records_pd['time']))

for i in range(len(first_three_records_pd)):
    print(first_three_records_pd.loc[i].equals(full_records_pd.loc[i]))


# print(first_three_records_pd.equals(full_records_pd))



