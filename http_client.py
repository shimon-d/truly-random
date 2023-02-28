# This is an alternative version to the requests

import http.client
import urllib.parse

url = "/integers/"
params = {
    "num": 6,
    "min": 1,
    "max": 60,
    "col": 1,
    "base": 10,
    "format": "plain",
    "rnd": "new"
}

conn = http.client.HTTPSConnection("www.random.org")
query_string = urllib.parse.urlencode(params)
conn.request("GET", url + "?" + query_string)

response = conn.getresponse()
if response.status == 200:
    numbers = list(map(int, response.read().decode().strip().split()))
    print(numbers)
else:
    print("Error: Failed to generate random numbers")

conn.close()
