# import tdameritrade
# from tdameritrade import auth
# import os

# client_id='FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3'
# redirect_uri = 'http://localhost:8080'
# tdauser = 'eltouch8'
# tdapass = 'maradona10'

# tdameritrade.auth.authentication(client_id, redirect_uri, tdauser, tdapass)

# import tdameritrade as td
# import os
# import json

# # client_id = os.getenv('FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3')
# # account_id = os.getenv('493918836')
# # refresh_token = os.getenv('eTPph+UbLaY9LXXGPVAXURw1R3BVBD4INY4LKUXM0frRXBYIF92TYImIlsmo8N9BvqHmNZBXwfdNpVCElW8GynHhY5aIsT+okwHp6KScqsh9iVLSzHfeiIitQVFGUaah6SNrickbHx6vj9Do9oUGvSNKhZ6Uw1jTbGQiceg6cfxzYYcJD1z7OyjJODz9Xp3p5mQJ/EwQDugi0G/lp28RVODUZ79VvIgr8yN+xOK+ZUziEQQHxncUdHHjn5nJDzGqrMY8eDSXdVn2C5Od1iMZJk0SD80eA37RzlnlQ0XUzBVif9f7oJ0R+kq6Qomm7xYpsJgrf+echBeVdEYqziesFF0XtNTuMNlp7CQ/fpNnlDm2HKL1jX4CiTvYULtufGOrv36RlNTxvUEOlKcvR3Sd8CmPKHku1i/tf2+/u99r/PHNuolujU/PomjZfEv100MQuG4LYrgoVi/JHHvlc4VGK1xyG3lWrS1FhkzysbfYmDJjfhpHtPJ+Kp/VWH6ytlZ5XjmeQfyraonisKDHXU3YE9P6iFajeOpEQhLqLuZgb6sk7fVmvjXR1Fx0lin5WOLC1R4evRqoZUsdHmab4jwIwYBdAcnC546hQuMX1rTwsQqXHIHtfgsIifvIyAoyFgAp9UOqiGPLsDDLqv8BKtXvIhLTe3QcZvoZcLZn59CChC4jy3uPQ7ish2ckNsjKIELMX2kojYa0Qt1DoMaRgns9dycfsfW3HUuo2iAW6zAZkOmDlgj/WxVY8XYUJSa64x6WuqoAhLVs0pVre9fvO3+z4lrgV5saYWuTRVcnP4vxcTDbShx1Mzp8aZvWTdi/bIQ4JD30gKg7n+LYizAjXoY6tN3bNIm5u0zFoz13/Nqk7GGH5l0IdPNFKfDFPGKeBncmNzgbe4gFEjo=212FD3x19z9sWBHDJACbC00B75E')


# client_id = os.getenv('TDAMERITRADE_CLIENT_ID', default='FGCT7QNS3OXYT0R6DZQIDVIAYE3KFQA3')
# account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='493918836')
# refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN', default='20M9KSHj98FrEO0z/OXK9s62HqzIjjmz31UbuYNVcydTkMDPkscvzjxIGrAKe7gKnk0Ll9nAJ4ruYGpbUw36RYC/8HShYclGuXCaGhlWpJkaaTnfNEWQp5dGyS6Czc5tRF0OhZV4wGIWlhUscYHLwbTDixBRT3Q6aNgEBAmSgk5qrUObTOu2jbfv1VH6dRvC9nG/0UoNTpO61g+/fGQRbvGgJFdvnSqumGTdJ+3fkLYN29l1kVkA1suht73xOlob9LLAcOAlv/VjVFGmj7iuTj5VVzVmZntyW+jj1KU73euvPKTh48vTxUMm2IK4nLXdPoKG7Dn4tpBCeCHmmmGTPcX3/+cXQXussW4u0rfjGlwWnaTalFotxIbHtiBg1UMegkT59oU9usRpsNIPxLp52aoaoZ7HY2ID1J0E8sHpX9atKvIo9frqPy7NmkQ100MQuG4LYrgoVi/JHHvlNBF009DEkuq0D31yU5xuWG7ZKLL7RaBsqQboljdO63/DmBhqloW096uJ5qk+acAeTOH1b6iD27hu1gJcwCTEc7YsQhOawXxpFEDCC+drYn3bgtJBwkJyIFQJpNjdZQEq+lrq5Gl1q1plKtTGKSDTdNjotMwWqpTr8MBQDBHFM1V5BN4q3ox3WDbRH9v42+6S7v3MQwISXHDYFuM/hcNDMepdKb5SzloEBon0ncnX+XdGxGj5QFVLi82zsxy+e40l1EsWUmFUtGla21JZwUGwKeGU4BaKaCCbFsbQmqK9ZWX9q2mCh1HXbDl5RHfSzetu60g7MGmGGZERKqCPlNiRYWJXwe+6QX7uwBWeusBcEl+ttMNlV2FA4I01ShuKUXjPBs/gcJfsCJxztD/PWoagsxs8N7/IiXKIxYBgn6KU21MOP1+4yrfxed9ekOY=212FD3x19z9sWBHDJACbC00B75E')
# access_token = os.getenv('TDAMERITRADE_ACCESS_TOKEN', default='r70yZZ7REYQ2XuCcEKZKWwWxruYLpUJC9svViOx9Az2RkKSZ5AVdg54953VAehOtpRUHc39GdGXC4tRwEGM0cmY8cntX5oC//m6wJZeBhceuKBlmW7aZNR8OcCESJ6OYDihiYCSWaOe+wQErq2BaKscVMMrdnuaXuJ0NzXxJsERHeb3OWh/2ZT64mRgNkVXwxHhiiINgaWbVDqle/X8YXks/buaCH6WFLkkVqwUu36j9Pxofca4OVtBHxfd3YmYqVT2/3k0KIm7Sp6uKgklhWz4YxicPwckcZv5UpKRi8akbcYy27/uON7XyYHPhH+oVRjBa0w7S2ywP/qYEfwtoG8QfLpN7CipiGUSUUNmpalRwstof2D2QQEl8MZsZcVfcqV0YwS9QIbfroDoERVwSasD/k35slw9PJXDsPmQ1E0U0b1FxbCJL+QbrSVj77vu0ponL2OJoi/tXcqiPWqlzqPbfwgwDFSMjEfrp33xwzntCa9BkSFDIZxPFFiEz1FX5T8GPttgn/zZoegaZ9gTBUPLXTIrPf4NqPgDJSU12kFy2u2Ca8odMwbkqiLO100MQuG4LYrgoVi/JHHvlDg0nozmGHtAoLbYY6+7d2ScAoOnRUB/Rd8ODPvptgHpr55p3pXw0QQo5559kXp29ye9XTHGZkZSig/gAyVAzdfViJ+D1tE2sG9bjQWSvbpfQiJYzOtBxn6/+4Hk3Npg9xU39m6xgZj0t7aZ/Z67XPH3wfwHyEtgVCAiNls14KRXAx8OI7mcXxT7kWrYfY2VziWoqk9ldL4XcNsUV0jci+Io93HGrXjgjPDfmyTYaxeRWJjIu2XAAQbMJUBr8LQUWY2su6dhP/q5m/I0SZKkwZREovbAANccUVu5pa/v3hRQ6Kz3M8lzZthrBlg5iQDMd1zr8VtyLSuX9HeDDgg+t6tikWJ+d/VcMjgLDFtfse8vWDTbWkRVTFo6BxAfEY/MEeaHrTqrac6q2Qb+If1hr8fIN8U/S2IYnfq/RnGKF0yTwAz7Ovxo3OCar0HlSxr23NQcfU5MhgU/eqJNZ2KbhJav7iUyO8F0re5vokeyPwXgtoBUWipiqDwMfj8wP1qOejGKyAxa+zvNec6598V+zhAjocQm5K4s2kXidLpnfcyPMWB0C+HIh3kHU5S8=212FD3x19z9sWBHDJACbC00B75E')
# MY_SECRET = os.getenv('TDAMERITRADE_ACCOUNT_ID', default='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImVsdG91Y2hAZ21haWwuY29tIiwiaWF0IjoxNTkwMjUxMDU2LCJleHAiOjc4OTc0NTEwNTZ9.vQtvoFRLaTbAe935CRZHPr-gjalbVAuCYXbv7GgE_f4')

# tdclient = td.TDClient(access_token=access_token, accountIds=[account_id])

# tdclient.

# acc = tdclient.accounts(positions=False, orders=True)

# print(acc)

# jsonData = {
#   "orderType": "MARKE",
#   "session": "NORMAL",
#   "duration": "DAY",
#   "orderStrategyType": "SINGLE",
#   "orderLegCollection": [
#     {
#       "instruction": "Buy",
#       "quantity": 15,
#       "instrument": {
#         "symbol": "XYZ",
#         "assetType": "EQUITY"
#       }
#     }
#   ]
# }

# orde = tdclient.orders(account_id, jsonData)

# print(orde)

#help(td.access_token)

# # import the requests library
# import requests

# # Get candles from your own source
# candles = [{}]; # Candles in json




# # Define indicator
# indicator = "hma"

# # Define endpoint
# endpoint = f"https://ta.taapi.io/{indicator}"

# # Parameters to be sent to API
# parameters = {
#     'secret': MY_SECRET,
#     'candles': candles,
#     'period': 8
# }

# # Send post request and save response as response object
# response = requests.post(url = endpoint, json = parameters)

# # Extract data in json format
# result = response.json()

# # Print result
# print(result)

# import asyncio
# from codetiming import Timer

# async def task(name, work_queue):
#     timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
#     while not work_queue.empty():
#         delay = await work_queue.get()
#         print(f"Task {name} running")
#         timer.start()
#         await asyncio.sleep(delay)
#         timer.stop()

# async def main():
#     """
#     This is the main entry point for the program
#     """
#     # Create the queue of work
#     work_queue = asyncio.Queue()

#     # Put some work in the queue
#     for work in [15, 10, 5, 2]:
#         await work_queue.put(work)

#     # Run the tasks
#     with Timer(text="\nTotal elapsed time: {:.1f}"):
#         await asyncio.gather(
#             asyncio.create_task(task("One", work_queue)),
#             asyncio.create_task(task("Two", work_queue)),
#         )

# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio

# async def cor1():
#     print("cor1 start")
#     for i in range(10):
#         await asyncio.sleep(4.5)
#         print("cor1", i)

# async def cor2():
#     print("cor2 start")
#     for i in range(15):
#         await asyncio.sleep(1)
#         print("cor2", i)

# loop = asyncio.get_event_loop()
# cors = asyncio.wait([cor1(), cor2()])
# loop.run_until_complete(cors)

# Importando dependencias:

import time
import asyncio
from threading import Thread

# async def do_some_work(x):
#     print("Waiting " + str(x))
#     await asyncio.sleep(x) 

async def do_some_work(x):
    print("cor1 start")
    for i in range(3):
        await asyncio.sleep(x)
        print("cor1", i)

loop = asyncio.get_event_loop()
#loop.run_until_complete(do_some_work(5))

# tareas = [asyncio.ensure_future (do_some_work (2)), 
#          asyncio.ensure_future (do_some_work (5))]

# loop.run_until_complete (asyncio.gather (* tareas))

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

def more_work(x):
  print("More work %s" % x)
  time.sleep(x)
  print("Finished more work %s" % x)

def test():
    i = 0
    for i in 5:
        print(i)
        asyncio.run_coroutine_threadsafe (do_some_work (1), new_loop)


test()


# new_loop.call_soon_threadsafe(more_work, 6)
# new_loop.call_soon_threadsafe(more_work, 3)
# new_loop.call_soon_threadsafe (more_work, 20) 
# asyncio.run_coroutine_threadsafe (do_some_work (1), new_loop)
# asyncio.run_coroutine_threadsafe (do_some_work (2), new_loop)




# # async def do_some_work(x):
# #     print("Waiting " + str(x))
# #     await asyncio.sleep(x)

# async def do_some_work(x):
#     print("Waiting " + str(x))
#     for i in range(10):
#         await asyncio.sleep(x)
#         print("cor1", i)

# def start_loop(loop):
#     asyncio.set_event_loop(do_some_work(2))
#     loop.run_forever()

# def g():

#     #loop = asyncio.get_event_loop()
#     #loop.run_until_complete(do_some_work(5))

#     # tasks = [asyncio.ensure_future(do_some_work(2)), 
#     #         asyncio.ensure_future(do_some_work(5))]

#     # loop.run_until_complete(asyncio.gather(*tasks))

#     new_loop = asyncio.new_event_loop()
#     t = Thread(target=start_loop, args=(new_loop,))
#     t.start()

# g()






# from threading import Thread
# import asyncio

# def start_loop(loop):
#     asyncio.set_event_loop(loop)
#     loop.run_forever()

# new_loop = asyncio.new_event_loop()
# t = Thread(target=start_loop, args=(new_loop,))
# t.start()