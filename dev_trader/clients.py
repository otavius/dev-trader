"""
clients.py will set up the needed clients for getting either historical or live data rather than calling it all the time in different files. I will just create them once here to be called from anywhere
"""
from env import api_key, secret_key
from alpaca.data  import StockHistoricalDataClient, CryptoHistoricalDataClient
# remove imports after testing
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe  import TimeFrame
from datetime import datetime

class MyClients:
    
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        
    def stock_historical_client(self):
        stock_client = StockHistoricalDataClient(self.api_key, self.secret_key)
        return stock_client
    
    

        
    
client = MyClients()



        