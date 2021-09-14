import pandas as pd 
import json

df_traded_pairs = pd.read_csv("first_three_records.csv")
print(df_traded_pairs)
ancient_trades = pd.read_csv("ancient_trades.csv")
print(ancient_trades)
# list_of_ancient_trades = 
# pairs_previously_traded = list(set(df_traded_pairs['symbol']))
# print(pairs_previously_traded)
# # print(len(list(df_traded_pairs['symbol'])))
# # print(len(set(df_traded_pairs['symbol'])))
# # print(list(df_traded_pairs['symbol']))
# outfile = open("pairs_previously_traded.json", 'w') 
# json.dump(pairs_previously_traded, outfile, indent = 1)
