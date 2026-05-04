# Your API Key: ff65fb42666ad879f87f0b1f
# Example Request: https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD
import requests
currency = input("Enter currency (like EUR): ")

api = "https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD"
response = requests.get(api)

data = response.json()
rates = data["conversion_rates"]

if currency in rates:
    print("1 USD =", rates[currency])
else:
    print("Invalid currency")