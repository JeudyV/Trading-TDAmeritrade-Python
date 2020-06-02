import tdameritrade as td
from tdameritrade.client import TDClient
import requests, os, json, random, time

from models import data_indicator
from flask_app import db

def get_token():
    f = open ('token_DB.txt','r')
    mensaje = f.read()
    f.close()
    return mensaje

client_id_ = os.getenv('TDAMERITRADE_CLIENT_ID', default='FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3')
account_id_ = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='493918836')
refresh_token_ = os.getenv('TDAMERITRADE_REFRESH_TOKEN', default='il0eggPn3999znfXxkJKBwkLsawtEUb1Uub2Oma6FjaRY5+a/CVEPybOC/GAmTwDx9nOGI+qfZDKU1yit4qc56R9Keolj0zINrL0LdgFM3unmdwudyRCwL4YG33iqYxZcRY3FnRj8HwkVVrVUtoDsTfAbycsVY6qHpm1/MRrJganGTEzurt2Yu63/cRdRre2n7Yr+hZQWsyVivByHkM3zj6m8I50Hrk5TSznUDN1k/vZLkqpUNFRmHOtpDRddJN+oVEVdoqytRF0MGW+TMka+G9i1n/fiUZzytEUM7pC02aOd5cR/rAf/FwuN0MQeVHt4kd06t8C5kskq0cPzm4Z8g3zLYR0D3de4O3PQXjS9CLfRdoFbeD+j7FXb30yY703Zx+9/WjN02oUSMtblqrgvJn9SYpPtltUDILhbe3RcdOwWGrydz06I0WyHBN100MQuG4LYrgoVi/JHHvl/UhFrpcXcpEUIqNb7ESHW+9px9bnFVCAtr9oBbTpP0eJ8SUsUNI5OkH2/x+zq4v1fiqasYeeLbwhhuOcFXz8WYHPGdokcQ7oB8aoybS5Fg6V0QlJqhzx/KanbWcQKhTPSjytbykt5UKBKwgmC6lIPqaTmbHstHEGW0S3cyhha1dRkqHbc7XELj54I8obKHbhB76MoOtL6rjDExiuExhQh+8f6n7H/OkH7CzPbx8vXeYBmdUq7ejszxcNiJIE0QaDDH7qtsr8Ah4e6yTfxm2GaEuc1gNOcoVK/c29e8XGf2lrC8sLoR/9B+i+qRdoy4bRMtkadsdmn/YFsexzL46Ohk4cvA+yu/+FRq++H77Zi5d/1rQVWy5o4y1BpS/WYf3Q0uaHmmZzgznMB4qemzosMz2fVboi5MLaYX62fqtZIbe8WG+4xnNrQG8+0gc=212FD3x19z9sWBHDJACbC00B75E')
access_token_ = os.getenv('TDAMERITRADE_ACCESS_TOKEN', default=get_token())
tc = td.TDClient(access_token=access_token_, accountIds=[account_id_])
MY_SECRET = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVsdG91Y2hAZ21haWwuY29tIiwiaWF0IjoxNTkwMjUxMDU2LCJleHAiOjc4OTc0NTEwNTZ9.vQtvoFRLaTbAe935CRZHPr-gjalbVAuCYXbv7GgE_f4')

# import time
# import asyncio
# from threading import Thread

# # async def cor1(jsonData):
# #     texto = jsonData["texto"]
# #     print("texto", texto)
# #     print(f"cor{texto} start")
# #     for i in range(10):
# #         await asyncio.sleep(4.5)
# #         print("cor1", i)

# async def do_some_work(x):
#     print("Waiting " + str(x))
#     for i in range(10):
#         await asyncio.sleep(x)
#         print("cor1", i)

# async def async_method():

#     loop = asyncio.get_event_loop()
#     #loop.run_until_complete(do_some_work(5))

#     tasks = [asyncio.ensure_future(do_some_work(2)), 
#             asyncio.ensure_future(do_some_work(5))]

#     loop.run_until_complete(asyncio.gather(*tasks))

def history_price(jsonData):
    bandera = True
    print("fuera", bandera)
    
    while (bandera == True):
        print("dentro",bandera)

        try:    
            symbol = jsonData['symbol']
            periodType = jsonData['periodType']
            period = jsonData['period']
            frequencyType = jsonData['frequencyType']
            frequency = jsonData['frequency']

            print(symbol)

            url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?periodType={}&period={}&frequencyType={}&frequency={}".format(symbol,periodType,period,frequencyType,frequency)

            payload = {}
            headers = {
            'Authorization': 'Bearer {}'.format(access_token_)
            }
            print(access_token_)

            response = requests.request("GET", url, headers=headers, data = payload)

            #print(response.text.encode('utf8'))
            print("requests status history price", response.status_code)

            result = response.json() 
            result = result['candles']

            bandera = False

            return result
        
        except:

            if(response.status_code == 401):
                bandera = True
                access_token()
                #return "Unauthorized, Error code 401"
        time.sleep(60)


def history_price_by_data(jsonData):

    bandera = True
    
    while (bandera == True):
        try:  

            symbol = jsonData['symbol']
            periodType = jsonData['periodType']
            frequencyType = jsonData['frequencyType']
            startDate = jsonData['startDate']
            endDate = jsonData['endDate']

            url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?periodType={}&frequencyType={}&startDate={}&endDate={}".format(symbol,periodType,frequencyType,startDate,endDate)

            print(url)

            payload = {}
            headers = {
                'Authorization': 'Bearer {}'.format(access_token_)
            }

            response = requests.request("GET", url, headers=headers, data = payload)

            #print(response.text.encode('utf8'))
            print("requests status history price by data", response.status_code)

            result = response.json() 
            result = result['candles']

            return result
        except:

            if(response.status_code == 401):
                bandera = True
                access_token()
                #return "Unauthorized, Error code 401"

def manual_indicator(history_price_candles, jsonData):

    try:

        # Get candles from your own source
        candles = history_price_candles; # Candles in json

        # Define indicator
        #indicator = "rsi"
        indicator = jsonData["indicator"]

        # Define endpoint
        endpoint = f"https://ta.taapi.io/{indicator}"

        # Parameters to be sent to API
        parameters = {
            'secret': MY_SECRET,
            'candles': candles,
            'period': jsonData["period"]
        }

        # Send post request and save response as response object
        response = requests.post(url = endpoint, json = parameters)

        print("requests status indicator", response.status_code)

        # Extract data in json format
        result = response.json()

        # Print result
        #print(result)

        print(result)

        return result['value']

    except:

        if(response.status_code == 413):
            return "coin after hours, Error code 413"

def manual_history_price(jsonData):
    history_price_candles = history_price_by_data(jsonData)
    #print(history_price_candles)
    valor = manual_indicator(history_price_candles, jsonData)
    #print(valor)
    return valor


def indicator(jsonData):
    # Define indicator
    #indicator = "hma"
    indicator = jsonData["indicator"]
    
    # Define endpoint 
    endpoint = f"https://ta.taapi.io/{indicator}"
    #MY_SECRET = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVsdG91Y2hAZ21haWwuY29tIiwiaWF0IjoxNTkwMjUxMDU2LCJleHAiOjc4OTc0NTEwNTZ9.vQtvoFRLaTbAe935CRZHPr-gjalbVAuCYXbv7GgE_f4'
    
    # Define a parameters dict for the parameters to be sent to the API 
    # parameters = {
    #     'secret': MY_SECRET,
    #     'exchange': 'binance',
    #     'symbol': 'BTC/USDT',
    #     'interval': '1m',
    #     'period' : 8
    #     } 

    parameters = {
        'secret': MY_SECRET,
        'exchange': jsonData["exchange"],
        'symbol': jsonData["symbol"],
        'interval': jsonData["interval"],
        'period' : jsonData["period"]
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)

    #response.status_code
    print(response.status_code)
    #print(response.text)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    for x, v in result.items():
        result = v

    return result




import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def loop_indicator(jsonData):
    bandera = True
    cont = 0
    contador = 0
    list_price_coin = {}
    a1 = 0
    a2 = 0


    while(bandera == True):
        if(cont < 2):
            #variable = indicator(jsonData)
            
            jsonData["endDate"] = int(unix_time_millis(datetime.datetime.now()))

            variable = manual_history_price(jsonData)
            print("indicator valor ", variable)
            list_price_coin.setdefault(cont, variable)
            print(cont)
            cont = cont + 1
            print("list indicator", list_price_coin)
        else:
            for x, v in list_price_coin.items():
                if (x == 0):
                    a1 = v
                if (x == 1):
                    a2 = v
            print("first indicator",a1 , "second indicator",a2)
            if (a1 < a2):
                instruction = "buy"
                jsonDataOrder =  {
                        "orderType": jsonData["orderType"],
                        "session": jsonData["session"],
                        "duration": jsonData["duration"],
                        "orderStrategyType": jsonData["orderStrategyType"],
                        "orderLegCollection": [
                            {
                            "instruction": instruction,
                            "quantity": jsonData["quantity"],
                            "instrument": {
                                "symbol": jsonData["symbol"],
                                "assetType": jsonData["assetType"]
                            }
                        }
                    ]
                }
                place_order(jsonDataOrder)
            elif(a1 > a2):
                instruction = 'sell'
                jsonDataOrder =  {
                        "orderType": jsonData["orderType"],
                        "session": jsonData["session"],
                        "duration": jsonData["duration"],
                        "orderStrategyType": jsonData["orderStrategyType"],
                        "orderLegCollection": [
                            {
                            "instruction": instruction,
                            "quantity": jsonData["quantity"],
                            "instrument": {
                                "symbol": jsonData["symbol"],
                                "assetType": jsonData["assetType"]
                            }
                        }
                    ]
                }
                place_order(jsonDataOrder)
            elif(a1 == a2):
                print("the indicators are the same")
            cont = 0
            list_price_coin = {}
            print(cont)
            print(list_price_coin)
            #bandera = False
        time.sleep(60.1)



#def access_token(refresh_token, client_id):
# def access_token():
#     resp_token = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
#                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
#                          data={'grant_type': 'refresh_token',
#                                'refresh_token': refresh_token_,
#                                'client_id': client_id_})
#     if resp_token.status_code != 200:
#         raise Exception('Could not authenticate!')
#     print("print ",resp_token)
#     print("print.json() ",resp_token.json())
#     token = resp_token.json()
#     print("json ",token["access_token"])
#     return token["access_token"]

def access_token():
    resp_token = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'refresh_token',
                               'refresh_token': refresh_token_,
                               'client_id': client_id_})
    if resp_token.status_code != 200:
        raise Exception('Could not authenticate!')
    print("print ",resp_token)
    print("print.json() ",resp_token.json())
    token = resp_token.json()
    print("json ",token["access_token"])
    f = open ('token_DB.txt','wb')
    s = token["access_token"]
    print(s)
    print(type(s))
    b1 = bytes(s, encoding = 'utf-8')
    print(b1)
    print(type(b1))
    f.write(b1)
    f.close()

# def access_token():
#     resp_token = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
#                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
#                          data={'grant_type': 'refresh_token',
#                                'refresh_token': refresh_token_,
#                                'client_id': client_id_})
#     print("resp_token", resp_token)
#     if resp_token.status_code != 200:
#         raise Exception('Could not authenticate!')
#     f = open ('token_DB.txt','wb')
#     s = resp_token["access_token"]
#     print(s)
#     print(type(s))
#     b1 = bytes(s, encoding = 'utf-8')
#     print(b1)
#     print(type(b1))
#     f.write(b1)
#     f.close()
#     return s


#def authenticate():

def process_random(jsonData):
    option_random = random.randint(0, 2)  
    bandera = True
    while(bandera == True):
        print(option_random)
        if(option_random == 0):
            print("0")
        elif(option_random == 1):
            print("1")
        elif(option_random == 2):
            print("2")


def T_create_order(jsonData):
    orde = tc.orders(account_id_, jsonData)
    print(orde)
    return orde

def place_order(jsonData):

    bandera = True
    
    while (bandera == True):
        try: 

            url = "https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id_)

            payload = json.dumps(jsonData)
            print(payload)
            headers = {
            'Authorization': 'Bearer {}'.format(access_token_),
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data = payload)

            print(response.text.encode('utf8'))

            result = response.json()

            return result
        except:

            if(response.status_code == 401):
                bandera = True
                access_token()
                #return "Unauthorized, Error code 401"


def account_balance(jsonData):
    positions = jsonData["positions"]
    orders = jsonData["orders"]

    balance = tc.accounts(positions, orders)
    #return balance
    #print(balance.status_code)
    return balance


class C_TDameritrade:
    def __init__(self):
        self.client_id = os.getenv('TDAMERITRADE_CLIENT_ID', default='FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3')
        self.account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='493918836')
        self.refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN', default='il0eggPn3999znfXxkJKBwkLsawtEUb1Uub2Oma6FjaRY5+a/CVEPybOC/GAmTwDx9nOGI+qfZDKU1yit4qc56R9Keolj0zINrL0LdgFM3unmdwudyRCwL4YG33iqYxZcRY3FnRj8HwkVVrVUtoDsTfAbycsVY6qHpm1/MRrJganGTEzurt2Yu63/cRdRre2n7Yr+hZQWsyVivByHkM3zj6m8I50Hrk5TSznUDN1k/vZLkqpUNFRmHOtpDRddJN+oVEVdoqytRF0MGW+TMka+G9i1n/fiUZzytEUM7pC02aOd5cR/rAf/FwuN0MQeVHt4kd06t8C5kskq0cPzm4Z8g3zLYR0D3de4O3PQXjS9CLfRdoFbeD+j7FXb30yY703Zx+9/WjN02oUSMtblqrgvJn9SYpPtltUDILhbe3RcdOwWGrydz06I0WyHBN100MQuG4LYrgoVi/JHHvl/UhFrpcXcpEUIqNb7ESHW+9px9bnFVCAtr9oBbTpP0eJ8SUsUNI5OkH2/x+zq4v1fiqasYeeLbwhhuOcFXz8WYHPGdokcQ7oB8aoybS5Fg6V0QlJqhzx/KanbWcQKhTPSjytbykt5UKBKwgmC6lIPqaTmbHstHEGW0S3cyhha1dRkqHbc7XELj54I8obKHbhB76MoOtL6rjDExiuExhQh+8f6n7H/OkH7CzPbx8vXeYBmdUq7ejszxcNiJIE0QaDDH7qtsr8Ah4e6yTfxm2GaEuc1gNOcoVK/c29e8XGf2lrC8sLoR/9B+i+qRdoy4bRMtkadsdmn/YFsexzL46Ohk4cvA+yu/+FRq++H77Zi5d/1rQVWy5o4y1BpS/WYf3Q0uaHmmZzgznMB4qemzosMz2fVboi5MLaYX62fqtZIbe8WG+4xnNrQG8+0gc=212FD3x19z9sWBHDJACbC00B75E')
        self.access_token = os.getenv('TDAMERITRADE_ACCESS_TOKEN', default='0cX5kefJbuTmoxGIxkQ+1KxskU05wVENPtkGn5EsoB0sKTvXbz64LdmEads09YTkGFXw4RI1nrkPOinwyx3GxiC4STsloneRrQWV4BuergeUs1KHkVfdYFoWQnVpbjBb0o0IvdeD2KgK1gFdRp+QAG5+JzDT4Flg87nFwR7yZqkS01VIRPxdw6kFzCe3G96N1Dfp3dA0NlXGa/WvC8gH3HIh/NhzYlKXMfHAiMKs3GvIybQo3vxaLwXplO33pa7jwDAFvGn6mnzWPuH6zxpkbRx1HOZyjONdX78EaN53ydBzEF0Ansm5M+I2AQGv5b3DC8zgiu49U2+cmbr/EQJxSnhxM30j+7omvMtSIF4vAz7xIXDcRheJDVL3XBNDagHOiFmEl+nSIp7YIQO/EG/sTsI9jySwzY/xkQJZ9HpnTFtDPNBoO424S3xbEsHnTNec/W1QIUITcKyaz95tIplSBRP7M38yIUqkXr1qxSyCBGRQV4cF+c7/ZtPrE+if2UCXMqSX9iWa2iNmy0ZDQIjebFyD+NXfd7au+Ef2MhWEVKcgtnx9M100MQuG4LYrgoVi/JHHvlQHUJaLeydgtvA1Fn71UVioaYAOPIitVuUabrG1dESyWNL17l7ISy1wYx7Zqa7xPiUutbIsfwPc5aHzFKJ/XGinFhj/x9MssARPvNV5iwFRB9iD+2fdP4uRqcBZUlX2pqh8SVPSclVd4iScWZbpfNx7Jo4/E8ooeD3zX/6wDBHlodvrDO4DVhCtVhB8D7kNwMe/X1QiHqK0ZkvLhqh0UFlLeupqiW3+3/XjmQ52WSd+YJSOHInLT0viuIr4ZrL+hCTzw9Fdyr7Vopk1FV4Pf+aaXCRlL55txTAhOdz0ZnvAC5a5ZG8RE7wUnd19wzTjIblen02nNnKgfVklQKBcECxBmoedAqfuKlDyVF3OUf0QLTt45M2Q5AlOWLpazKV4J3C8PtMruCSN/rMw+ZAM9eAId/pi3qsQKq7oVAV5Qs91GGIQSvATn1fFVZkkYToSuvLjpDkSp0Qa9SIrjYc3LGFz89R9Fi8B3dultssIsJsJelAkrLLzLGcmcDaNlbXZ4XI+t4eiRkE+GQ+YzjBSBfnpY9I8Q/5hLdmrqf5LtKfmaqtmbw==212FD3x19z9sWBHDJACbC00B75E')

        self.tdclient = td.TDClient(self.client_id, self.refresh_token, self.account_id)

    def create_order(self, account_id, jsonData):
        order = self.tdclient.orders(self, account_id, jsonData)
        o = json.loads(order)
        print(json.loads(order))
        return o

    def test(self):
        return "hola mundo"

    def create_save_order(self, order):

        """
        Save an order for a specific account.

         Args:
            accountId (int): id of account to place order under
            order (JSON): order instance to place
        """

        co = self.tdclient.createSavedOrder(self, client_id, order)
        return co
    
    def delete_save_order(self, savedOrderId):

        """
        Delete a specific saved order for a specific account

         Args:
            accountId (int): id of account to place order under
            savedOrderId (int): id of order instance to delete

        """

        do = self.tdclient.deleteSavedOrders(self, client_id, savedOrderId)
        return do

    def get_price_history(self, **jsonData):
        '''
        Get price history for a symbol

        Args:
            symbol (str): symbol to get price history for
            periodType (str): period type to request
            period (int): period to use
            frequencyType (str): frequency type to use
            frequency (int): frequency to use
            endDate (int): End date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided. Default is previous trading day.
            startDate (int): Start date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided.
            needExtendedHoursData (bool): true to return extended hours data, false for regular market hours only. Default is true
        '''
        history = self.tdclient.history(self, **jsonData)
        return history
    
    def get_quote(self, symbol):
        """
        get quote for symbol
            
         Args:
            symbol (str): symbol to get quote for
               
        """
        quote = self.tdclient.quote(self, symbol)
        return quote


    def get_transactions(self, **jsonData):
        """
        get quote for symbol
            
        Args:
            accountId (int): account id (defaults to client's ids)
            type (str): transaction type, in ('ALL', 'TRADE', 'BUY_ONLY', 'SELL_ONLY', 'CASH_IN_OR_CASH_OUT', 'CHECKING', 'DIVIDEND', 'INTEREST', 'OTHER', 'ADVISOR_FEES')
            symbol (str): transactions for given symbol
            start_date (str): start date as string yyyy-MM-dd
            end_date (str): end date as string yyyy-MM-dd
               
        """
        transactions = self.tdclient.transactions(self, **jsonData)
        return transactions


    def get_order(self, **jsonData):
        """
        get order
            
            Parameters:	
                accountId (int) – account id
                orderId (int) – orderId
                maxResults (int) – max number of results to return
                fromEnteredTime (str) – yyyy-MM-dd to filter by
                toEnteredTime (str) – yyyy-MM-dd to filter by
                status (str) – only return orders with this status
                   
            
        """
        order = self.tdclient.order(self, **jsonData)
        return order

    def cancel_order(self, accountId, orderId):
        """
        Cancel a specific order for a specific account.
            
        Args:
            accountId (int): account id the order is under
            orderId (int): order id of order to cancel
                   
            
        """
        c_order = self.tdclient.cancelOrder(self, account_id, orderId)
        return c_order