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




# %%

data_df = pd.DataFrame(data)
    # print(data_df)

print(data_df['tags'])

def set_of_tags():
    programme_start_time = time.time()
    list_of_tags=[]
    for i in range(len(data_df)):
        list_of_tags = list_of_tags + data_df.at[i, 'tags']
        # print(data_df.at[i, 'tags'])
    # print(list_of_tags)

    set_of_tags = set(list_of_tags)
    print(set_of_tags)
    print("The size of the set of tags is {}.".format(len(set_of_tags)))
    print("Programme executed in {}".format(time.time()-programme_start_time))
    return set_of_tags

    
set_of_tags()



# print(data_df['tags'].apply(lambda x: concatenate(x)))
# print(data_df.columns)
    # pp.pprint(data['data'])