import requests
api_key = "1a7842126dc841430eaf9336166356d8"
url = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat":-1.365010,
    "lon":38.011570,
    "appid":api_key,
    "lang":"en"
}

response = requests.get(url,params=parameters)

print(response.json())

