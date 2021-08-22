# This programme aims to analyze if there are Whales for a given token
# by utilising the Gini Coefficient

# %%
import ccxt
import config
  
import ccxt

binance = ccxt.binance({
    'apiKey': config.key,
    'secret': config.secret,
    'timeout': 30000,
    'enableRateLimit': True,
})


binance_markets = binance.load_markets()

# print(binance.id, binance_markets)

# %%
# print(binance.id, binance.load_markets())


# print(binance.fetch_order_book(binance.symbols[0]))
# print(binance.fetch_ticker('BTC/USD'))
# print(binance.fetch_trades('LTC/CNY'))

print(binance.fetch_balance())

# # sell one ฿ for market price and receive $ right now
# %%

