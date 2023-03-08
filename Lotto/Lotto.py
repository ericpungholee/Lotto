from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = "wastogi999"

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("home.html")


@app.route("/generate", methods=["POST", "GET"])
def lotto():
    numbers = range(1, 51)
    ticket = []
    i = 0
    while i != 7:
        while True:
            num = random.choice(numbers)
            if not num in ticket:
                ticket.append(num)
                i+=1
                break
    
    for i in range(len(ticket)):
        ticket = sorted(ticket)
        flash(f"{ticket[i]}")

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)