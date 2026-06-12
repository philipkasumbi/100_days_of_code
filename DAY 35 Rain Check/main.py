import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
url = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


parameters = {
    "lat":-1.365010,
    "lon":38.011570,
    "appid":api_key,
    "lang":"en",
    "units":"metric",
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
        if int(id_code) < 700:
            will_rain = True

if will_rain:
    try:
        message = client.messages.create(
            body="Today it might rain, don't forget to carry your ☔",
            from_="+19086417409",
            to="+254790553620"
        )
        print(message.sid)

    except Exception as e:
        print(e)



