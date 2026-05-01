# Your API Key: ff65fb42666ad879f87f0b1f
# Example Request: https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD

import requests

def money(currency):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    user = input ('what currency u want USD into ? What 3letters  ')
    if user in data:
      print (data)
money("USD")