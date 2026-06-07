import datetime as dt
import random
import smtplib
from email.message import EmailMessage

from multiprocessing import connection

my_email = "pythont695@gmail.com"
password = "juid frmf tund wnwy"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="kasumbipeter5@gmail.com",
#         msg="Subject:Hello\n\nThis is a test email from Python.")

now= dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt","r",encoding="utf-8") as quotes:
    content = quotes.readlines()
    random_quote = random.choice(content)

message = EmailMessage()
message["Subject"] ="Sunday Motivation"
message["From"] = my_email
message["To"] = "kasumbipeter5@gmail.com"
message.set_content(random_quote)

if day_of_week == 6:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.send_message(message)


