from flask import Flask
from flask_restful import Resource, Api

#from flask_app import app, api
#from DevelopmentBotV_test import create_user

from flask import request

import Development_TD

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

api.add_resource(HelloWorld, '/test')
api.add_resource(create_save_order_, '/create_save_order')
api.add_resource(get_order_, '/get_order')

#if __name__ == '__main__':
app.run(debug=True)