import requests
api_key = "1a7842126dc841430eaf9336166356d8"
url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":-1.365010,
    "lon":38.011570,
    "appid":api_key,
    "lang":"en",
    "units":"metrics",
    "cnt":4,
}

response = requests.get(url,params=parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = False

for forecast in weather_data["list"]:
    weather_list= forecast["weather"]
    for id in weather_list:
        id_code = id["id"]
        if int(id_code) <= 700:
            will_rain = True
            
if will_rain:
    print("Bring Umbrella")

