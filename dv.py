# Your API Key: ff65fb42666ad879f87f0b1f
# Example Request: https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD
import requests
cur = input("Enter currency like EUR ")

key = "https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD"
request = requests.get(key)

data = request.json()
rate = data["conversion_rates"]

if cur in rate:
    print("1 usd =", rate[cur])
else:
    print("Invalid currency")