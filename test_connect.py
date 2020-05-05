import tdameritrade
from tdameritrade import auth
import os

client_id='UKWKG17C0BCS52FEZ84GWB6TEZIT8O2S'
redirect_uri = 'http://localhost:8080'
tdauser = 'jehu09cr@gmail.com'
tdapass = 'Mm123456'

tdameritrade.auth.authentication(client_id, redirect_uri, tdauser, tdapass)