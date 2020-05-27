import tdameritrade as td
from tdameritrade.client import TDClient
import requests, os, json, random, time

from models import data_indicator
from flask_app import db

client_id_ = os.getenv('TDAMERITRADE_CLIENT_ID', default='FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3')
account_id_ = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='493918836')
refresh_token_ = os.getenv('TDAMERITRADE_REFRESH_TOKEN', default='il0eggPn3999znfXxkJKBwkLsawtEUb1Uub2Oma6FjaRY5+a/CVEPybOC/GAmTwDx9nOGI+qfZDKU1yit4qc56R9Keolj0zINrL0LdgFM3unmdwudyRCwL4YG33iqYxZcRY3FnRj8HwkVVrVUtoDsTfAbycsVY6qHpm1/MRrJganGTEzurt2Yu63/cRdRre2n7Yr+hZQWsyVivByHkM3zj6m8I50Hrk5TSznUDN1k/vZLkqpUNFRmHOtpDRddJN+oVEVdoqytRF0MGW+TMka+G9i1n/fiUZzytEUM7pC02aOd5cR/rAf/FwuN0MQeVHt4kd06t8C5kskq0cPzm4Z8g3zLYR0D3de4O3PQXjS9CLfRdoFbeD+j7FXb30yY703Zx+9/WjN02oUSMtblqrgvJn9SYpPtltUDILhbe3RcdOwWGrydz06I0WyHBN100MQuG4LYrgoVi/JHHvl/UhFrpcXcpEUIqNb7ESHW+9px9bnFVCAtr9oBbTpP0eJ8SUsUNI5OkH2/x+zq4v1fiqasYeeLbwhhuOcFXz8WYHPGdokcQ7oB8aoybS5Fg6V0QlJqhzx/KanbWcQKhTPSjytbykt5UKBKwgmC6lIPqaTmbHstHEGW0S3cyhha1dRkqHbc7XELj54I8obKHbhB76MoOtL6rjDExiuExhQh+8f6n7H/OkH7CzPbx8vXeYBmdUq7ejszxcNiJIE0QaDDH7qtsr8Ah4e6yTfxm2GaEuc1gNOcoVK/c29e8XGf2lrC8sLoR/9B+i+qRdoy4bRMtkadsdmn/YFsexzL46Ohk4cvA+yu/+FRq++H77Zi5d/1rQVWy5o4y1BpS/WYf3Q0uaHmmZzgznMB4qemzosMz2fVboi5MLaYX62fqtZIbe8WG+4xnNrQG8+0gc=212FD3x19z9sWBHDJACbC00B75E')
access_token_ = os.getenv('TDAMERITRADE_ACCESS_TOKEN', default='OCWzKHKURmf896wdTWJIAWQcEiu4n+ovf9QXU+ZXA6VVIOubMDkIy65707fnVk7xUZ+/bvfR+mmFpDrkAarvmI9nuxelZql5p7V2weXmuMAaHX9dIBmQamHSxFx6FUhgs3/jjRX/dgoHVtAvCXnRm4Do2Y/k/Ck74cJDsJOr99pNy9WfjrytxPElVKMszGdnk+xCj1r2/ywGrOPgDQBzbP/UxePrzSeTWKcvp4k+hqYgbHOqtBJStL5VPNP+wkKDnTzCdFIy4mYRGMmZ6YcPdyx/oO1qwmFnW1poFI/s7Xs0a+RZT9XYm6aZbfNf5z9MHmJS0LUkRN9/9gCA7ORXxqS8UqViCTzsj37Hbad5tQGJwt81F1vjhtq279L5SSUigJUvf+srYJ9atl5y5HQ4aieQReTg9T2IkApphO065rC5cAmexLPciFkFAdJjNnNZWo4PpofEVwqUNmu+FAFlLIMy5zVnSDJnuZG/VQy+9pT/ZhB7rvxJdwHIHN0oFaAzQ0vekSYxX5r0Xxnvefsy2PHYX8dp4Ik5dmV2+aH3JLg0pJVYM100MQuG4LYrgoVi/JHHvltK192SXHGCwyPoEH2sjCYvKr4T6ejP4w2dUV5b7U1CCelGpo3T4Aciq70m7UWjE42iLly5bIsl5xyqZrZHl0RSxyDqmw+SLr/jAUokvfuZRg+23ViGy5+YuOfSfrHb45n6Hnhy1ADijNI0RH6hK/pveI2WH9Ru9vfS5BuIPJFRO3JqL0RKXotw7bNtauGcJenOthazDbNsMOQKHnyLgYy1VFR9tGAp67kAbmyG6KPnb7Oe6QbiiJ16ItXGIy21GLFI0xgbkGDxcApcQAEKbVmSUS5kWhowgSP72DU35e751bLlA063PAXC1WUVlBUYNsenOwD2ioYlHjlXvKME9u1mwbzg2zFQqi693tNtYdA6clfCzcqo+uKl5WtD9zoCY6FUGAwnjaNIOVV5r7bHsooHbhkDQIhQTJXt+Uz1W79N6xwnRv2wRXk71XL6bsbdyJjdKEmtqr5d76LEcc+5pUdu3pRMgaSQ6WMkuzl4vV7gla/PECoujVmlmeDJCJqgswJBHyd44Egc8LlIs5cktRmfluHIMx14iU978vAlmCIkYNUyHQ==212FD3x19z9sWBHDJACbC00B75E')
tc = td.TDClient(access_token=access_token_, accountIds=[account_id_])
MY_SECRET = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVsdG91Y2hAZ21haWwuY29tIiwiaWF0IjoxNTkwMjUxMDU2LCJleHAiOjc4OTc0NTEwNTZ9.vQtvoFRLaTbAe935CRZHPr-gjalbVAuCYXbv7GgE_f4')

def history_price(jsonData):

    symbol = jsonData['symbol']
    periodType = jsonData['periodType']
    period = jsonData['period']
    frequencyType = jsonData['frequencyType']
    frequency = jsonData['frequency']

    url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?periodType={}&period={}&frequencyType={}&frequency={}".format(symbol,periodType,period,frequencyType,frequency)

    payload = {}
    headers = {
    'Authorization': 'Bearer {}'.format(access_token_)
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    #print(response.text.encode('utf8'))

    result = response.json() 
    result = result['candles']

    return result

def manual_indicator(history_price_candles, jsonData):

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

    # Extract data in json format
    result = response.json()

    # Print result
    #print(result)

    return result['value']

def manual_history_price(jsonData):
    history_price_candles = history_price(jsonData)
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

def loop_indicator(jsonData):
    bandera = True
    cont = 0
    contador = 0
    list_price_coin = {}
    a1 = 0
    a2 = 0
    while(bandera == True):
        if(cont < 5):
            #variable = indicator(jsonData)
            variable = manual_history_price(jsonData)
            print(variable)
            list_price_coin.setdefault(cont,variable)
            cont = cont + 1
            print(cont)
            print(list_price_coin)
        else:
            for x, v in list_price_coin.items():
                print(v)
                if (x == 0):
                    a1 = v
                if (x == 4):
                    a2 = v
            print("a1",a1 , " a2",a2)
            if (a1 == a2):
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
                T_create_order(jsonDataOrder)
                if(contador < 2):
                    contador = contador + 1
                    print("contador", contador)
                else:
                    bandera == False
            else:
                instruction = 'sell'
            cont = 0
            list_price_coin = {}
            print(cont)
            print(list_price_coin)
            #bandera = False
        time.sleep(60.1)



#def access_token(refresh_token, client_id):
def access_token(jsonData):
    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'refresh_token',
                               'refresh_token': jsonData["refresh_token"],
                               'client_id': jsonData["client_id"]})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    print("print ",resp)
    print("print.json() ",resp.json())
    return resp.json()


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

def account_balance(jsonData):
    positions = jsonData["positions"]
    orders = jsonData["orders"]
    bandera = tc.accounts(positions, orders)
    print(bandera)
    return bandera


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