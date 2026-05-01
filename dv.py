import requests

def money(currency):
    response = requests.get(f"https://v6.exchangerate-api.com/v6/ff65fb42666ad879f87f0b1f/latest/USD")
    if response.status_code != 200:
        print("Error fetching data!")
        
    data = response.json()
    User = input ("what currency u want 1 USD in(the letters)")
    for d in data:
      if User in d:
        print(d)