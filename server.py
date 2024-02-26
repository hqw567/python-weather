from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")
    data = get_weather(city)
    result = data["result"]
    if data["code"] != 200:
        return render_template(
            "error.html",
        )
    else:
        return render_template(
            "weather.html",
            city_name=result["city_name"],
            current_condition=result["current_condition"],
            current_temperature=result["current_temperature"],
            dat_low_temperature=result["dat_low_temperature"],
            dat_high_temperature=result["dat_high_temperature"],
        )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port="3000")
