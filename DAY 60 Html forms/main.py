from flask import Flask, render_template,request
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

PASSWORD =os.getenv("APP_PASSWORD")
EMAIL = os.getenv("EMAIL")

@app.route("/")
def contact_form():
    return render_template("index.html")

@app.route('/form-entry',methods=["POST"])
def receive_message():
    email = request.form.get('email')
    message = request.form.get('message')

    msg = EmailMessage()
    msg["Subject"] = "New Contact Form Message"
    msg["From"] = email
    msg["To"] = EMAIL

    msg.set_content(f"""Sender: {email}
    message:{message}
    """)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    return "<h1>Successfully sent your message!!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
