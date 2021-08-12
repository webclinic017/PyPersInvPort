# %%
import pandas as pd 
import numpy as np 
import biCon
import config
from binance.spot import Spot as Client
import os

data = {"time": [], "symbol": [], "isBuyer": [], "Price": [], "Amount": [], "Total": [], "Fee": [], "Fee Coin": []}


key    = config.key
secret = config.secret

client = Client(key, secret)

pairs = ["ETHBTC", "ETHUSDT", "BTCUSDT"]
# %%
tradeHistorydf = pd.read_csv("biCon.csv")

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

    

def calculateAveragePrices(dataframe, csv = False):

    average = {
        "time": [],
        "USDT": [], 
        "ETH" : [],
        "BTC" : [],
        "Avg. USDT price": [],
        "Avg. ETH price": [],
        "Avg. BTC price": []
        # "balance in USDT": [],
        # "balance in ETH": [],
        # "balance in BTC": []
        }

    USDTheld       = 0
    ETHheld        = 0
    BTCheld        = 0
    USDT_avg_price = 1
    ETH_avg_price  = 0
    BTC_avg_price  = 0
    # bal_in_USDT    = 0
    # bal_in_ETH     = 0
    # bal_in_BTC     = 0
    df = dataframe.sort_values(by='time',ascending=True)

    for i in range(len(df.loc[:,"time"])):     
        
        amountSpent             = float(df.loc[:,"qty"][i]) # "Amount" is the amount that you have bought or sold - this is the currency you receive. If the pair is "ETHBTC", and you're selling, the "Amount" is the amount of ETH you have sold for BTC.
        price                   = float(df.loc[:,"price"][i]) # "Price" is the the price in which you have bought or sold it. If the pair is "ETHBTC", and you're buying, then "Price" is the price of ETH you have bought for BTC. If the pair is "ETHBTC", and you're selling, the "Price" is the price of ETH you have sold for BTC.
        received                = float(df.loc[:, "quoteQty"][i]) # "Total" is the amount of currency you have spent to buy or sell the asset.  If the pair is "ETHBTC", and you're buying, you have bought ETH for BTC (ie you receive ETH). The "Total" is the amount of ETH you have bought. If you're selling, you have sold ETH for BTC (ie you receive BTC). The "Total" is the amount of BTC you have recieved.
        fee                     = float(df.loc[:, "commission"][i]) # The fee is always paid in the currency you receive. If the pair is "ETHBTC", and you're buying, the fee will be in ETH; if you're selling, the "fee" will be in BTC. 
        BTCprice = float(df.loc[:, "BTCprice"][i])
        ETHprice = float(df.loc[:, "ETHprice"][i])
        commissionAsset         = df.loc[:,"commissionAsset"][i]
        amountObtained          = received - fee 
        priceOfAssetObtained    = amountObtained/amountSpent
        

        if df.loc[:,"isBuyer"][i] == True:
            if df.loc[:,"symbol"][i] == "ETHUSDT":      # update the ethereum and usdt average prices and amounts, btc remains unchanged
            
                USDTheld       = USDTheld - amountSpent
                ETHheld        = ETHheld + amountObtained
                BTCheld        = BTCheld        
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = (ETH_avg_price * ETHheld +  priceOfAssetObtained * amountObtained)/(ETHheld + amountObtained)
                BTC_avg_price  = BTC_avg_price
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)    
            elif df.loc[:,"symbol"][i] == "ETHBTC":
                #         # update the ethereum and btc average prices and amounts, USDT remains unchanged
                USDTheld       = USDTheld
                ETHheld        = ETHheld + amountObtained        
                BTCheld        = BTCheld - amountSpent      
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = (ETH_avg_price * ETHheld + priceOfAssetObtained * (ETHprice / BTCprice) * amountObtained)/(ETHheld + amountObtained)
                BTC_avg_price  = BTC_avg_price
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)
       
            elif df.loc[:,"symbol"][i] == "BTCUSDT":
                USDTheld       = USDTheld - amountSpent 
                ETHheld        = ETHheld
                BTCheld        = BTCheld + amountObtained        
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = ETH_avg_price
                BTC_avg_price  = (BTC_avg_price * BTCheld + priceOfAssetObtained * amountObtained)/(BTCheld + amountObtained)
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)
                # update the btc and usdt average prices and amounts, eth remains unchanged
#       
        elif df.loc[:,"isBuyer"][i] == False:      
            if df.loc[:,"symbol"][i] == "ETHUSDT":      # update the ethereum and usdt average prices and amounts, btc remains unchanged
                USDTheld       = USDTheld + amountObtained        
                ETHheld        = ETHheld - amountSpent 
                BTCheld        = BTCheld        
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = ETH_avg_price
                BTC_avg_price  = BTC_avg_price
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)    
            elif df.loc[:,"symbol"][i] == "ETHBTC":
                #         # update the ethereum and btc average prices and amounts, USDT remains unchanged
                USDTheld       = USDTheld
                ETHheld        = ETHheld - amountSpent 
                BTCheld        = BTCheld + amountObtained             
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = ETH_avg_price
                BTC_avg_price  = (BTC_avg_price * BTCheld + priceOfAssetObtained * (BTCprice / ETHprice) * amountObtained)/(BTCheld + amountObtained)
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)
       
            elif df.loc[:,"symbol"][i] == "BTCUSDT":
                USDTheld       = USDTheld - amountSpent 
                ETHheld        = ETHheld
                BTCheld        = BTCheld + amountObtained        
                USDT_avg_price = USDT_avg_price 
                ETH_avg_price  = ETH_avg_price
                BTC_avg_price  = (BTC_avg_price * BTCheld + priceOfAssetObtained * amountObtained)/(BTCheld + amountObtained)
                average["time"].append(df.loc[:,"time"][i])
                average["USDT"].append(USDTheld)
                average["ETH"].append(ETHheld)
                average["BTC"].append(BTCheld)
                average["Avg. USDT price"].append(USDT_avg_price)
                average["Avg. ETH price"].append(ETH_avg_price)
                average["Avg. BTC price"].append(BTC_avg_price)
                # update the btc and usdt average prices and amounts, eth remains unchanged
    CompleteDataFrame = pd.DataFrame(average)
    cwd = os.getcwd()
    path = cwd + "/{}.csv".format("AvgPrices")
    if csv == True: 
        print(CompleteDataFrame) 
        return CompleteDataFrame.to_csv(path)
    else:
        print(CompleteDataFrame) 

calculateAveragePrices(tradeHistorydf, csv = True)

# %%


# # # # # fee = df.loc[:,"Fee"][i]
# # # #                 # 
# # # #                 # average["USDT"].append(df.loc[:,"time"][i])
# # # #                 # average["ETH"].append(df.loc[:,"time"][i])
# # # #                 # average["BTC"].append(df.loc[:,"time"][i])
# # # #                 # average[].append(df.loc[:,"time"][i])
# # # #                 # average[].append(df.loc[:,"time"][i])
# # # #                 # average[].append(df.loc[:,"time"][i])
# # # #                 # average[].append(df.loc[:,"time"][i])
# # # #                 # average[].append(df.loc[:,"time"][i])


# # # # #                 def loop():
# # # # #         a = 0
# # # # #     for i in range(5):
# # # # #         if i % 2 == 0:
# # # # #             a = a
# # # # #             print(a)
# # # # #         else: 
# # # # #             a = a+1
# # # # #             print(a)
        
# # # # # loop()

# # # # # pd.read_csv("Export Trade History-2021-07-26 17_16_16.csv") 


# # # # # print(tradeHistorydf.loc[:,"Price"])
