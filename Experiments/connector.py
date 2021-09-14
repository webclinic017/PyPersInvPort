import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint 
import pandas as pd 
import time
pp = pprint.PrettyPrinter(indent=1)
# %%


def connectCMC():
  ''' The data returned by
          response = session.get(url, params=parameters)
          data = json.loads(response.text)
      is a dictionary, of two keys, namely "status" and "data". Most of the interesting stuff is in "data". 
      data['data'] is a list of dictionaries. And each dictionary has keys:
      'id', 'name', 'symbol', 'slug', 'num_market_pairs', 'date_added', 'tags', 'max_supply', 'circulating_supply', 'total_supply', 'platform', 'cmc_rank', 'last_updated', 'quote'
  '''
  start_time = time.time()
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.coinmarketcap["key"],
  }

  session = Session()
  session.headers.update(headers)
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    pp.pprint(e)
  

  with open("raw.json", "w") as outfile:
    json.dump(data, outfile, indent = 1)
  with open("data.json", "w") as outfile:
    json.dump(data['data'], outfile, indent = 1)
  
  print(time.time()-start_time)
    

if __name__ == "__main__":
    connectCMC()
# %%
# help(connectCMC)
# data_df = pd.DataFrame(data)
    
# data = connectCMC()