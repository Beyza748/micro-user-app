from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

COUNTRY_SERVICE = "http://country-service:5001"
HOLIDAY_SERVICE = "http://holiday-service:5002"

@app.route("/")
def index():
    return render_template("index.html")

# 🔹 API 1 → Countries
@app.route("/api/countries")
def countries():
    r = requests.get(f"{COUNTRY_SERVICE}/countries")
    return jsonify(r.json())

# 🔹 API 2 → Holidays
@app.route("/api/holidays")
def holidays():
    code = request.args.get("code")
    r = requests.get(f"{HOLIDAY_SERVICE}/holidays/{code}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
