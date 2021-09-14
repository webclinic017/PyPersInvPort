from numpy import concatenate
import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint 
import pandas as pd 
import time
import json

pp = pprint.PrettyPrinter(indent=1)

data = json.load(open('data.json', 'r'))

data_df = pd.DataFrame(data)