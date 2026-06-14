import requests

"""
One Stock
    ↓
Check Price
    ↓
Get News
    ↓
Send Notification
"""

API_KEY = "4VG9N5R4AZIRBBSY"
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":API_KEY
}
url = 'https://www.alphavantage.co/query'
response = requests.get(url,params=parameters)
daily_data = response.json()["Time Series (Daily)"]

dates = list(daily_data.keys())
sorted_dates = sorted(dates,reverse=True)

# today and yesterday
latest = sorted_dates[0]
previous = sorted_dates[1]

# opening and closing values
today_closing = daily_data[latest]["4. close"]
yesterday_closing = daily_data[previous]["4. close"]

# percentage change
value_change = today_closing-yesterday_closing
percentage_change = (value_change/yesterday_closing)*100


