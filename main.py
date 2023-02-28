import requests

url = "https://www.random.org/integers/"
params = {
    "num": 6,
    "min": 1,
    "max": 60,
    "col": 1,
    "base": 10,
    "format": "plain",
    "rnd": "new"
}

response = requests.get(url, params=params)
if response.status_code == 200:
    numbers = list(map(int, response.text.strip().split()))
    print(numbers)
else:
    print("Error: Failed to generate random numbers")
