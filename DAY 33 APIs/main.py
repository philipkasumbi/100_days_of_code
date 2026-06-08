import requests
from datetime import datetime


MY_LAT = -0.023559
MY_LNG = 37.906193

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position=(iss_longitude,iss_latitude)

    # your position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude >= MY_LAT+5 and MY_LNG-5 <= iss_longitude >= MY_LNG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    now = datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True

