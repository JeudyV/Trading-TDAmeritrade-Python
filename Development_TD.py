import tdameritrade as td
import os
import json

class C_TDameritrade:
    def __init__(self):
        self.client_id = os.getenv('TDAMERITRADE_CLIENT_ID')
        self.account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID')
        self.refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN')

        tdclient = td.TDClient(self.client_id, self.refresh_token, self.account_id)

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