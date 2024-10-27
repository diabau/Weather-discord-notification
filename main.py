import requests

url = "https://my.meteoblue.com/packages/current?apikey=(API_KEY)&lat=45.43&lon=4.4&asl=479&format=json"

response = requests.get(url)

temperture = response.json()['data_current']['temperature']

print(temperture)