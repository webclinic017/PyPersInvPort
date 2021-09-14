import etherscan_API_config as config
from etherscan import Etherscan

address = config.address
apikey = config.APIkey

eth = Etherscan(apikey) # key in quotation marks

print(eth.get_eth_balance(address=address))
print(eth.get_all_events(address, topic, enriched_data=False, from_block=0, to_block='latest', thread_count=1))

print(eth.get_contract_execution_status())



# client = etherscan_py.Client(apikey)

# print(client.get_eth_price())
# print(client.get_all_transactions(from_address = address, status = 2, to_address='', fn_signature='', from_block=0, to_block='latest', thread_count=1))




