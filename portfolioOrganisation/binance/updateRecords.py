from biAcc import myTrades
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
import biAcc
import time


# This programme updates the trade history records 
# Note that the definition of set_of_pairs_possibly_traded includes a pair only if at least one of the tokens in that pair has a non-zero balance in the binance account right now
# This means if I had sold off all my DOGE holdings to USDT, I would not see my DOGE holdings
pairs = biAcc.pairsPossiblyTraded()
# def latestTradingHistory():
#     try: 
#         df = pd.read_csv('biAcc.csv')
#     except: 
#         print("there is no file there.")
    # else: 
    #     print(df['time'].iloc[-1:])
# latest_trade_history = biAcc.myTrades(pairs, start_time = 1621258074086)

def update_trade_records(list_of_symbols = list, old_csv_file=str):
    starttime = time.time()
    df = pd.read_csv(old_csv_file)

    def arraySortedOrNot(arr):     
    # Calculating length
        n = len(arr)
        # Array has one or no element or the
        # rest are already checked and approved.
        if n == 1 or n == 0:
            return True
        # Recursion applied till last element
        return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])

    def last_time_of_record(df):
        if arraySortedOrNot(df['time'].to_list()) == False:
            df = df.sort_values(by="time")
        time = df['time'].to_list()
        return time[-3] 
    
    latest_trade_records_df = biAcc.myTrades(pairs, sort_time = True, start_time = last_time_of_record(df))
    print(latest_trade_records_df)
    print(time.time())
    return latest_trade_records_df.to_csv(old_csv_file, mode = 'a', header = False)
    

if __name__ == "__main__":
    update_trade_records(list_of_symbols = pairs, old_csv_file='first_three_records.csv')

    # appending to csv should be able to create a new file if there isn't one. 
    # If i just need data, the my_trades() function already does it
    # This thing here is strictly for updating binance trading records 
    # If I have no previous records, this should also be where I generate new records
    # If I already have some records, I DO NOT WANT to retrieve the same records again 
    # I want to start off from where I left off and retrieve the new trade records and append them to the existing records 
    # I would in fact want to obliterate the "change to csv" function
    # Because that function can allow for the overwriting of all past records





    # # def append_to_csv(file_name, newdf):
    # # # Open file in append mode
    # #     with open(file_name, 'a+', newline='') as write_obj:
    # #         # Create a writer object from csv module
    # #         csv_writer = writer(write_obj)
    # #         # Add contents of list as last row in the csv file
    # #         for i in range(len(newdf.index)):
    # #             if i == 0:
    # #                 pass
    # #             if i > 0: 
    # #                 csv_writer.writerow(newdf.iloc[[i]])
    
    # return append_to_csv(old_csv_file, latest_trade_records)

    # return last_time_of_record(df)
    
    
    
# update_trade_records(list_of_symbols = pairs, old_csv_file='biAcc.csv')



# def append_to_csv(file_name, newdf):
#     # Open file in append mode
#     with open(file_name, 'a+', newline='') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)
#         # Add contents of list as last row in the csv file
#         for i in range(len(newdf.index)):
#             if i == 0:
#                 pass
#             if i > 0: 
#                 csv_writer.writerow(newdf.iloc[[i]])
                

# # # append_to_csv("biAcc.csv", latest_trade_history)

# # # def append_to_csv(file_name, list_of_elem):
# # #     # Open file in append mode
# # #     with open(file_name, 'a+', newline='') as write_obj:
# # #         # Create a writer object from csv module
# # #         csv_writer = writer(write_obj)
# # #         # Add contents of list as last row in the csv file
# # #         csv_writer.writerow(list_of_elem)

# # # append_to_csv("biAcc.csv", df.columns.tolist())


# # # with open("biAcc.csv", 'r', newline='') as write_obj:
# # #     old_trades = pd.DataFrame(write_obj)
# # # pd.read_csv("Export Trade History-2021-07-26 17_16_16.csv") 


# # # def append_list_as_row(file_name, list_of_elem):
# # #     # Open file in append mode
# # #     with open(file_name, 'a+', newline='') as write_obj:
# # #         # Create a writer object from csv module
# # #         csv_writer = writer(write_obj)
# # #         # Add contents of list as last row in the csv file
# # #         csv_writer.writerow(list_of_elem)
