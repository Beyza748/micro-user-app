from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/holidays/<code>")
def holidays(code):
    year = 2024
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{code}"
    data = requests.get(url).json()

    return jsonify([
        {"date": h["date"], "name": h["localName"]}
        for h in data[:10]
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
