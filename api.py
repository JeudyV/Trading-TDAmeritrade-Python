from flask import Flask
from flask_restful import Resource, Api

from flask import request

import Development_TD
import Demo

import json

app = Flask(__name__)
api = Api(app)

#test = Development_Binance.Binance()

@app.after_request
def after_request(response):

    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.set('Access-Control-Allow-Credentials', 'true')

    return response

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class demo_price_(Resource):
    def get(self):
        #data = request.get_json()
        #return test.get_all_prices()
        return Demo.demo_price()
        #return json.loads(json.dumps(result, default=json_serial))
    
class create_save_order_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.create_save_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class delete_save_order_(Resource):
    def delete(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.delete_save_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class get_order_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.get_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class create_order_buy_market_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))
    
class create_order_buy_limit_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class create_order_buy_limit_vertical_call_spread_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class create_order_custom_option_spread_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class COCO_one_triggers_another_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class COCO_one_cancels_another_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class COCO_one_triggers_a_one_cancels_another_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class CO_sell_trailing_stop_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.T_create_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class access_token_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.access_token(data)
        #return json.loads(json.dumps(result, default=json_serial))

class account_balance_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.account_balance(data)
        #return json.loads(json.dumps(result, default=json_serial))

class indicator_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.indicator(data)
        #return json.loads(json.dumps(result, default=json_serial))

class loop_indicator_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.loop_indicator(data)
        #return json.loads(json.dumps(result, default=json_serial))

class history_price_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.history_price(data)
        #return json.loads(json.dumps(result, default=json_serial))

class manual_indicator_(Resource):
    def get(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.manual_indicator(data)
        #return json.loads(json.dumps(result, default=json_serial))

class manual_history_price_(Resource):
    def get(self):
        #data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.manual_history_price()
        #return json.loads(json.dumps(result, default=json_serial))

class place_order_(Resource):
    def post(self):
        data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.place_order(data)
        #return json.loads(json.dumps(result, default=json_serial))

class async_method_(Resource):
    def get(self):
        #data = request.get_json()
        #return test.get_all_prices()
        return Development_TD.async_method()
        #return json.loads(json.dumps(result, default=json_serial))

api.add_resource(HelloWorld, '/test')
api.add_resource(demo_price_, '/demo_price')
api.add_resource(create_save_order_, '/create_save_order')
api.add_resource(get_order_, '/get_order')
api.add_resource(create_order_buy_market_, '/create_order_buy_market')
api.add_resource(create_order_buy_limit_, '/create_order_buy_limit')
api.add_resource(create_order_buy_limit_vertical_call_spread_, '/create_order_buy_limit_vertical_call_spread')
api.add_resource(create_order_custom_option_spread_, '/create_order_custom_option_spread')
api.add_resource(COCO_one_triggers_another_, '/COCO_one_triggers_another')
api.add_resource(COCO_one_cancels_another_, '/COCO_one_cancels_another')
api.add_resource(COCO_one_triggers_a_one_cancels_another_, '/COCO_one_triggers_a_one_cancels_another')
api.add_resource(CO_sell_trailing_stop_, '/CO_sell_trailing_stop')
api.add_resource(access_token_, '/access_token')
api.add_resource(account_balance_, '/account_balance')
api.add_resource(indicator_, '/indicator')
api.add_resource(loop_indicator_, '/loop_indicator')
api.add_resource(history_price_, '/history_price')
api.add_resource(manual_history_price_, '/manual_history_price')
api.add_resource(place_order_, '/place_order')
api.add_resource(async_method_, '/async_method')

#if __name__ == '__main__':
app.run(debug=True)