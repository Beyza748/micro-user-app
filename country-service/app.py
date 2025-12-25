from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/countries")
def countries():
    r = requests.get("https://restcountries.com/v3.1/all")
    data = r.json()

    result = []
    for c in data:
        result.append({
            "code": c["cca2"],
            "name": c["name"]["common"],
            "capital": c.get("capital", ["-"])[0],
            "population": c["population"],
            "flag": c["flags"]["png"]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
