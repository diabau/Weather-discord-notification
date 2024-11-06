import requests
params = {
    "apikey": "APIKEY",
    "lat": 45.43,
    "lon": 4.3872,
    "asl": 480, # Altitude
    "format": "json"
}


response = requests.get("https://my.meteoblue.com/packages/current", params=params)
temperture = response.json()['data_current']['temperature']

temperture = round(temperture, 2)
requete = requests.post("WEBHOOK", json={"username": "meteo", "content": "La température actuelle à Saint-Étienne est d'environ " + str(temperture) + "°C"})
