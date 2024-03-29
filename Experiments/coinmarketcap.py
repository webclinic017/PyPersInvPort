import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint 

pp = pprint.PrettyPrinter(indent=1)
# %%
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
  # pp.pprint(data)
  print(data.keys())
  print(data['data'][1].keys())
except (ConnectionError, Timeout, TooManyRedirects) as e:
  pp.pprint(e)


# The data returned by 
# %%
