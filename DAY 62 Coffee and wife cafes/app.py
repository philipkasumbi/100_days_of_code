from flask import Flask, render_template
import csv
from flask import request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return  render_template("home.html")

@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as file:
        cafes = list(csv.reader(file))
    return  render_template("cafes.html",cafes=cafes)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        with open("cafe-data.csv","a",newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                request.form["cafe"],
                request.form["location"],
                request.form["open"],
                request.form["close"],
                request.form["coffee"],
                request.form["wifi"],
                request.form["power"]
            ])

        return redirect(url_for("cafes"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)