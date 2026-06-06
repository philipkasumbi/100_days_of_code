import smtplib

my_email = "pythont695@gmail.com"
password = "juid frmf tund wnwy"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="kasumbipeter5@gmail.com",
    msg="Subject:Hello\n\nThis is a test email from Python.")
connection.close()