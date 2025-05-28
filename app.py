from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Функция для получения координат города через Open-Meteo Geocoding API
def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}
    response = requests.get(url, params=params)
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        return lat, lon
    else:
        return None, None

# Главная страница с формой
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            lat, lon = get_coordinates(city)
            if lat is None or lon is None:
                error = "Город не найден. Попробуйте другой."
            else:
                # Запрос погоды у Open-Meteo
                weather_url = "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": lat,
                    "longitude": lon,
                    "hourly": "temperature_2m,precipitation,weathercode",
                    "current_weather": True,
                    "timezone": "auto"
                }
                response = requests.get(weather_url, params=params)
                weather_data = response.json()
        else:
            error = "Пожалуйста, введите название города."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)