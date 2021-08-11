# %%
import pandas as pd 
import numpy as np 
import biCon
import config
from binance.spot import Spot as Client

data = {"Date(UTC)": [], "symbol": [], "isBuyer": [], "Price": [], "Amount": [], "Total": [], "Fee": [], "Fee Coin": []}


key    = config.key
secret = config.secret

client = Client(key, secret)

pairs = ["ETHBTC", "ETHUSDT", "BTCUSDT"]
# %%
tradeHistorydf = biCon.myTrades(pairs)


# %%

# symbol -- the pair that's traded: ETHBTC, BTCUSDT, ETHUSDT, etc.
# id --
# orderId --
# orderListId --
# price -- "price" is the the price in which you have bought or sold. If the pair is "ETHBTC", and you're buying, then "Price" is the price of ETH you have bought for BTC. If the pair is "ETHBTC", and you're selling, the "Price" is the price of ETH you have sold for BTC.
# qty -- the amount in which you receive. 
# quoteQty -- the amount in which you give up for the trade. 
# commission -- the fees. 
# commissionAsset -- the asset in which the fee is paid
# time -- time
# isBuyer -- "true" if action is "True", "false" if action is "sell"
# isMaker -- ?
# isBestMatch --


# symbol
# id
# orderId
# orderListId
# price
# qty
# quoteQty
# commission
# commissionAsset
# time
# isBuyer
# isMaker
# isBestMatch
    
# %%

    

def calculateAveragePrices(dataframe):
    # dataframe = dataframe.sort_values(by='time',ascending=True) 
    print(dataframe)
calculateAveragePrices(tradeHistorydf)
# %%

#     average = {
#         "Date(UTC)": [],
#         "USDT": [], 
#         "ETH" : [],
#         "BTC" : [],
#         "Avg. USDT price": [],
#         "Avg. ETH price": [],
#         "Avg. BTC price": []
#         # "balance in USDT": [],
#         # "balance in ETH": [],
#         # "balance in BTC": []
#         }

#     USDTheld       = 0
#     ETHheld        = 0
#     BTCheld        = 0
#     USDT_avg_price = 1
#     ETH_avg_price  = 0
#     BTC_avg_price  = 0
#     # bal_in_USDT    = 0
#     # bal_in_ETH     = 0
#     # bal_in_BTC     = 0
    

#     for i in range(len(dataframe.loc[:,"time"])):     
        
#         amount                  = float(dataframe.loc[:,"qty"][i]) # "Amount" is the amount that you have bought or sold - this is the currency you receive. If the pair is "ETHBTC", and you're selling, the "Amount" is the amount of ETH you have sold for BTC.
#         price                   = float(dataframe.loc[:,"price"][i]) # "Price" is the the price in which you have bought or sold it. If the pair is "ETHBTC", and you're buying, then "Price" is the price of ETH you have bought for BTC. If the pair is "ETHBTC", and you're selling, the "Price" is the price of ETH you have sold for BTC.
#         total                   = float(dataframe.loc[:, "quoteQty"][i]) # "Total" is the amount of currency you have spent to buy or sell the asset.  If the pair is "ETHBTC", and you're buying, you have bought ETH for BTC (ie you receive ETH). The "Total" is the amount of ETH you have bought. If you're selling, you have sold ETH for BTC (ie you receive BTC). The "Total" is the amount of BTC you have recieved.
#         fee                     = float(dataframe.loc[:, "commission"][i]) # The fee is always paid in the currency you receive. If the pair is "ETHBTC", and you're buying, the fee will be in ETH; if you're selling, the "fee" will be in BTC. 
#         amount_Obtained         = amount - fee 
#         price_of_Asset_Obtained = amount_Obtained + total

#         if dataframe.loc[:,"isBuyer"][i] == True:
#             if dataframe.loc[:,"symbol"][i] == "ETHUSDT":      # update the ethereum and usdt average prices and amounts, btc remains unchanged
#                 USDTheld       = USDTheld - total
#                 ETHheld        = ETHheld + amount_Obtained        
#                 BTCheld        = BTCheld        
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = (ETH_avg_price * ETHheld + price_of_Asset_Obtained * amount_Obtained)/(ETHheld + amount_Obtained)
#                 BTC_avg_price  = BTC_avg_price
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)    
#             elif dataframe.loc[:,"symbol"][i] == "ETHBTC":
#                 #         # update the ethereum and btc average prices and amounts, USDT remains unchanged
#                 USDTheld       = USDTheld
#                 ETHheld        = ETHheld + amount_Obtained        
#                 BTCheld        = BTCheld - total      
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = (ETH_avg_price * ETHheld + price_of_Asset_Obtained * amount_Obtained)/(ETHheld + amount_Obtained)
#                 BTC_avg_price  = BTC_avg_price
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)
       
#             elif dataframe.loc[:,"symbol"][i] == "BTCUSDT":
#                 USDTheld       = USDTheld - total 
#                 ETHheld        = ETHheld
#                 BTCheld        = BTCheld + amount_Obtained        
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = ETH_avg_price
#                 BTC_avg_price  = (BTC_avg_price * BTCheld + price_of_Asset_Obtained * amount_Obtained)/(BTCheld + amount_Obtained)
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)
#                 # update the btc and usdt average prices and amounts, eth remains unchanged
# #       
#         elif dataframe.loc[:,"isBuyer"][i] == False:      
#             if dataframe.loc[:,"symbol"][i] == "ETHUSDT":      # update the ethereum and usdt average prices and amounts, btc remains unchanged
#                 USDTheld       = USDTheld + amount_Obtained        
#                 ETHheld        = ETHheld - total 
#                 BTCheld        = BTCheld        
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = ETH_avg_price
#                 BTC_avg_price  = BTC_avg_price
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)    
#             elif dataframe.loc[:,"symbol"][i] == "ETHBTC":
#                 #         # update the ethereum and btc average prices and amounts, USDT remains unchanged
#                 USDTheld       = USDTheld
#                 ETHheld        = ETHheld - total 
#                 BTCheld        = BTCheld + amount_Obtained             
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = (ETH_avg_price * ETHheld + price_of_Asset_Obtained * amount_Obtained)/(ETHheld + amount_Obtained)
#                 BTC_avg_price  = BTC_avg_price
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)
       
#             elif dataframe.loc[:,"symbol"][i] == "BTCUSDT":
#                 USDTheld       = USDTheld - total 
#                 ETHheld        = ETHheld
#                 BTCheld        = BTCheld + amount_Obtained        
#                 USDT_avg_price = USDT_avg_price 
#                 ETH_avg_price  = ETH_avg_price
#                 BTC_avg_price  = (BTC_avg_price * BTCheld + price_of_Asset_Obtained * amount_Obtained)/(BTCheld + amount_Obtained)
#                 average["Date(UTC)"].append(dataframe.loc[:,"time"][i])
#                 average["USDT"].append(USDTheld)
#                 average["ETH"].append(ETHheld)
#                 average["BTC"].append(BTCheld)
#                 average["Avg. USDT price"].append(USDT_avg_price)
#                 average["Avg. ETH price"].append(ETH_avg_price)
#                 average["Avg. BTC price"].append(BTC_avg_price)
#                 # update the btc and usdt average prices and amounts, eth remains unchanged

            
#             if dataframe.loc[:,"symbol"][i] == "ETHUSDT":    
#                 print("Hullo")
                
#             elif dataframe.loc[:,"symbol"][i] == "BTCUSDT":
#                 print("Hullo")
                
#             elif dataframe.loc[:,"symbol"][i] == "ETHBTC":
#                 print("Hullo")
               
#         else: 
#             print("The Godel Incompleteness Theorem is good.")
#     CompleteDataFrame = pd.DataFrame(average)
#     print(CompleteDataFrame) 

calculateAveragePrices(tradeHistorydf)

# %%


# # # # fee = df.loc[:,"Fee"][i]
# # #                 # 
# # #                 # average["USDT"].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average["ETH"].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average["BTC"].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average[].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average[].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average[].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average[].append(df.loc[:,"Date(UTC)"][i])
# # #                 # average[].append(df.loc[:,"Date(UTC)"][i])


# # # #                 def loop():
# # # #         a = 0
# # # #     for i in range(5):
# # # #         if i % 2 == 0:
# # # #             a = a
# # # #             print(a)
# # # #         else: 
# # # #             a = a+1
# # # #             print(a)
        
# # # # loop()

# # # # pd.read_csv("Export Trade History-2021-07-26 17_16_16.csv") 


# # # # print(tradeHistorydf.loc[:,"Price"])
