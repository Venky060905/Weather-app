
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "7175d230e8844e95b6065126251707"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get("cod") == 200:
            weather = {
                "city": city.title(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"]
            }
        else:
            error = f"City '{city}' not found. Please enter a valid city name."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
