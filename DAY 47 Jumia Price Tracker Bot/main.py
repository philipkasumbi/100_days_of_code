import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
import smtplib
from email.message import EmailMessage

url = "https://www.jumia.co.ke/apple-iphone-13-pro-max-256gb-new-327378921.html"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
price = float(soup.find("span",class_="-b -ubpt -tal -fs24 -prxs").getText().split(" ")[1].replace(",",""))

target_price = 69500

def send_mail(iphone_price):
    msg = EmailMessage()
    sender = os.getenv("SENDER")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER")

    msg['Subject'] = 'Iphone 13 promax  Price Alert'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content( f"""
            The iPhone 13 Pro Max price has dropped!
    
            Current price: Kshs {iphone_price}
    
            Go buy it now.
            """
        )
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

if price < target_price:
    send_mail(price)
