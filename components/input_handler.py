# https://www.freeforexapi.com/api/live\?pairs\=USDCOP      -> DOLARES A PESOS
# https://www.freeforexapi.com/api/live\?pairs\=COPUSD      -> PESOS A DOLARES

import requests
import json

URL: str = "https://www.freeforexapi.com/api/live?pairs=USDCOP"

r = requests.get(URL)
j = r.json()

usdvalor = j['rates']['USDCOP']['rate']
print(int(usdvalor))

class Input:
    def __init__(self):
        self.dolar = usdvalor









