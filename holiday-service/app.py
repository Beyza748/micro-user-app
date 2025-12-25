from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/holidays/<code>")
def holidays(code):
    r = requests.get(
        f"https://date.nager.at/api/v3/PublicHolidays/2024/{code}"
    )

    data = r.json()
    return jsonify([
        {"date": h["date"], "name": h["localName"]}
        for h in data
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

