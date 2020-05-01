import tdameritrade as td
from tdameritrade import auth

c = td.TDClient()

df = c.optionsDF('SPY')

df.iloc[0]

consumer_key = "UKWKG17C0BCS52FEZ84GWB6TEZIT8O2S"
redirect_uri = "http://localhost:8080"
client_id=consumer_key

# help(td)

auth.authentication("UKWKG17C0BCS52FEZ84GWB6TEZIT8O2S", "http://localhost:8080")

# import selenium
# help (selenium)