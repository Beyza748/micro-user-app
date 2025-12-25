from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    country = None
    holidays = []

    if request.method == "POST":
        code = request.form["country"]

        country_res = requests.get(f"http://country-service:5001/{code}").json()
        holiday_res = requests.get(f"http://holiday-service:5002/{code}").json()

        country = country_res["name"]
        holidays = holiday_res["holidays"]

    return render_template("index.html", country=country, holidays=holidays)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
