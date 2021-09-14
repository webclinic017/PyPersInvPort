# This programme looks at basic tokenomics to decide if a coin is a potential moon
# Right now I'm keeping it simple. The programme simply determines if a coin is ETH-like or not. 
# It does so statically by looking at the tokenonomics and the tags, without time-series data. 
# In other words, we do not analyze the price action. 
# If a token is indeed ETH-like, the programme spits out a multiple price targets.
# Two price targets are returned; one is computed by extrapolating the price of token using marketcap; 
# The price target approximates the price by use of TVL. 

# The structure of the code will be as such: 
# Each token will be constructed as a class. Attributes of each token will be taken from the information taken from the CMC api. 
# Analysis will then be done by mapping token attributes to a pandas dataframe. 
# Vectorisation and filtering will allow us to see which ones are potential moons. 

# tokens as classes

# The following piece of code merely defines the class of a Token, and its ontology. We are not going to initilise (generate) instances of the token in it. 
# We will obviously want to turn everything inside data.json into Token objects, but we will not be doing here. 
# It will require another piece of code.

import json
from token_data import data_df
import math


print(data_df)

print(data_df[''])



class Token: 
    class ETH: 
        name = data_df.loc[1, 'name']
        symbol = data_df.loc[1, 'symbol']
        num_market_pairs = data_df.loc[1, 'num_market_pairs']
        date_added = data_df.loc[1, 'date_added']
        tags = data_df.loc[1, 'tags']
        max_supply = data_df.loc[1, 'max_supply']
        circulating_supply = data_df.loc[1, 'circulating_supply']
        total_supply = data_df.loc[1, 'total_supply']

    eth = ETH()
    
    def __init__(self, name, symbol, num_market_pairs, date_added, tags, max_supply, circulating_supply, total_supply):
        self.name = name
        self.name = name
        self.symbol = symbol
        self.num_market_pairs = num_market_pairs
        self.date_added = date_added
        self.tags = tags
        self.max_supply = max_supply
        self.circulating_supply = float(circulating_supply)
        self.total_supply = total_supply
    
    def is_ETHlike(self, eth):
        dist_number_market_pairs = self.number_market_pairs - eth.number_market_pairs
        # self.max_supply = max_supply
        dist_circulating_supply = self.circulating_supply - eth.circulating_supply
        dist_total_supply = self.total_supply - eth.total_supply
        return(math.sqrt(dist_number_market_pairs ** 2 + dist_circulating_supply ** 2 + dist_total_supply ** 2))


# sol = Token()

# print(eth.name)
# print(eth.symbol)
# print(eth.num_market_pairs)
# print(eth.date_added)
# print(eth.tags)
# print(eth.max_supply)
# print(eth.circulating_supply)
# print(eth.total_supply)




# # print(data_df.iloc[1])
# # print(data_df.loc[1,'name'])
# # ETH = Token( )

#     # def isEthlike(self):
        

# #         return a number

# #         if ...:
# #             return True 
# #         else: 
# #             return False

 
# #    "name": "Bitcoin",
# #    "symbol": "BTC",
# #    "slug": "bitcoin",
# #    "num_market_pairs": 8853,
# #    "date_added": "2013-04-28T00:00:00.000Z",
# #    "tags": [
    
# #    "max_supply": 21000000,
# #    "circulating_supply": 18801462,
# #    "total_supply": 18801462,
# #    "platform": null,
# #    "cmc_rank": 1,
# #    "last_updated": "2021-08-30T08:00:12.000Z",
# #    "quote": {
# #     "USD": {
# #      "price": 47971.3459257753,
# #      "volume_24h": 27659747147.28271,
# #      "percent_change_1h": -0.05037202,
# #      "percent_change_24h": -1.2184614,
# #      "percent_change_7d": -4.39369761,
# #      "percent_change_30d": 15.47677732,
# #      "percent_change_60d": 43.64490789,
# #      "percent_change_90d": 30.12577507,
# #      "market_cap": 901931437512.3191,
# #      "market_cap_dominance": 43.5704,
# #      "fully_diluted_market_cap": 1007398264441.28,
# #      "last_updated": "2021-08-30T08:00:12.000Z"

# # # Is it ETH like?
# # # Is it a potential moon? 




