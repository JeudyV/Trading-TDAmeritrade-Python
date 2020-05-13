import requests
import json

def demo_price():
    
    # symbol = jsonData["symbol"],
    # periodType = jsonData["periodType"],
    # period = jsonData["period"],
    # frequencyType = jsonData["frequencyType"],
    # frequency = jsonData["frequency"],
    # endDate = jsonData["endDate"]


    #url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?periodType={}&period={}&frequencyType={}&frequency={}&endDate={}".format(symbol,periodType,period,frequencyType,frequency,endDate)

    url = "https://api.tdameritrade.com/v1/marketdata/XYZ/pricehistory?periodType=day&period=5&frequencyType=minute&frequency=1&endDate=1464825600000"

    payload = {}
    headers = {
        'Authorization': 'Bearer DHn4Td4HJyherGPdYC+rOKByWPWKeuEeK/5JDRgzt3Otro8BtQ9Qal6Z+jpN9W6o9dhhwST8Zgb+DnLFX7Uzga8YOoxQG3k+WVSyXkLvM/4AYGF/FkrmFuXmb3lu8CzLMD80OjTdPZi/aVwCu+MetJsfpGmfiS5yvhB0vaavJPs6k2G4Cdj2vQRSGfFwMnecZBDnDVnbNw9Bs9LUP1bbmt5Evzr1MNk9Ucv1EJJvq+4I30AfiAPGx7b29CQU4SExfLUk9ldm0obiwt/pXlV4mm5OOTeH0yVhl/gdEurtJCmmP83DrILejU3W9Y5qzyGlGtMiHKYhYfd6PJo6bipFuhWndhVGfsANcWPryQ36l4K3bfFG9Z9UEpMN42yyuXR+ZHm2FPIUd/0zMmQKEBm2dGtVL/1E6BGY4fXC7grNFYlMgiFG5UnKhLiuh8YCcVA09aII3LTugLURR8i1w6GkTWOCHP1hClXjM167gW6PzVHWXOXjfS1kQcQlizaCgvaf9y6gRxyed/8T24+FsOMnh6yox/QUx7VbwCRUQ5eL7cicfOFXW100MQuG4LYrgoVi/JHHvlrt5WOEUBhWrqh3a1QnhxxhOCsDW4AP6tasQlmf+4ZMuhz+lmcuHSfoOBmDmo8wQDUsajgH7QfKSqSE2Sihh8SQcuzJSQBRSEup8lXaRZZiZ8zGM6QMAvoD7fodUWjeVK92uVE06zexujNYauWD05lYliD808PUt8QPP5PU5/HAR8vrIb7AEqWiNc79inMzSuvkXj38UYLoz9SzzweCRgkA8pCH7ezqzIxT0lzSbekaxN4FTn6hgo7whcw6EGOHEGjT0+V0+W5mov6AlxtRpzdVKTmckgig65KvbaNwXDK2tfcTdJYMS0IsSrBdXaWOc56GT2ZudmwBY7ZpYoMfiAcBy/h9GoSpbOmFqb1MVmmsyflASElGgilxFEvTwouX2KOJ2T72WJI+MefgXXAo03WSMfGst2Pt+wEWtXouBsKcQ5UG/dRvrBUlQPokY4AW8Peg4eEgSLFqeAr+dpwV2DrGxGjaemDPuv8uZkbYa1GVE6sNqrakxDF/i1q2yi4xhAvK3x3Ot7v2Rkc5U4bPwEG56kms37HWEXRxAMGJ3JmPqO+sHA==212FD3x19z9sWBHDJACbC00B75E'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

    response = json.loads(response.text)

    print(response)

    return response