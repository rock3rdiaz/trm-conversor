import requests

def get_exchange_rate():

    url = "https://www.freeforexapi.com/api/live?pairs=USDCOP"
    response = requests.get(url).json()
    return response["rates"]["USDCOP"]["rate"]
