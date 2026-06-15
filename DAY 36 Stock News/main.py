import requests
import os
from twilio.rest import Client

"""
One Stock
    ↓
Check Price
    ↓
Get News
    ↓
Send Notification
"""

stock_key = os.environ["STOCK_KEY"]
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":stock_key
}
url = 'https://www.alphavantage.co/query'
response = requests.get(url,params=stock_parameters)
daily_data = response.json()["Time Series (Daily)"]

dates = list(daily_data.keys())
sorted_dates = sorted(dates,reverse=True)

# today and yesterday
latest = sorted_dates[0]
previous = sorted_dates[1]

# opening and closing values
today_closing = float(daily_data[latest]["4. close"])
yesterday_closing = float(daily_data[previous]["4. close"])

# percentage change
value_change = today_closing-yesterday_closing
percentage_change = (value_change/yesterday_closing)*100

# news
news_key = os.environ["NEWS_KEY"]

news_parameters = {
    "q":"tesla",
    "from":previous,
    "sortBy":"publishedAt",
    "apiKey":news_key
}
url = "https://newsapi.org/v2/everything"

if abs(percentage_change) > 5:

    news = requests.get(url, params=news_parameters)
    news_data = news.json()["articles"]

    message = ""

    for news in news_data[:3]:
        title = news["title"]
        description = news["description"]
        url = news["url"]
        news_message =(f"\n\ntitle:{title},\ndescription:{description},\nread more:{url}")
        message += news_message

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="message",
        from_="+19086417409",
        to="+254790553620",
    )












