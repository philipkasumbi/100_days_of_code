from flask import Flask
import random

app = Flask(__name__)

random_int = random.randint(0, 9)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGg0MWhncWZrNngyZ2t2cWFyeDhnbThnZWVzOGt0Zmh6ZGN5ZGFuMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eID2S0eI8KRKVcrmts/giphy.webp' width=200>"
            )

@app.route("/userinput/<int:number>")
def number_entered(number):
    if number < random_int:
        return ("<h1 style=color:red;>Too low,Try Again</h1>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDN3Z3VqaHZ1ODJ3cWU0bXk2Z21icmh1aTBkenJ0bmgwYjIwbjBudiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fvBEGznNx4VhchaIgb/200.webp' width=200>"
                )

    elif number > random_int:
        return (
            "<h1 style='color:blue;'>Too High, Try Again</h1>"
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmswdXpyczZnbnVmNXVyeHFjd3k5dnZodDgxYmV6MThmamVyMGx2eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/27sdoZn8YhLbil01q6/200.webp' width='200'>"
        )

    else:
        return (
            "<h1 style='color:green;'>Correct! 🎉</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjV1NXg3Zmg1Z2lkYWp2N2t4dXp6aWY0Z3k2bmY3Nzd3ZTNsemlsYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ummeQH0c3jdm2o3Olp/200.webp' width='200'>"
        )


if __name__ == "__main__":
    app.run(debug=True)