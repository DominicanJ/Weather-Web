from flask import Flask, render_template
import datetime
import requests
import os

app = Flask(__name__)

# Configuración (reemplaza con tu API key de OpenWeatherMap)
API_KEY = "284aacbc74abd5275879b5699b844e30"  # 🔑 Obtén una en: https://openweathermap.org/

def get_weather():
    try:
        # Coordenadas aproximadas (ej: Madrid) o usa geolocalización en producción
        lat, lon = 40.4168, -3.7038  # Por defecto: Madrid, España
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=es"
        response = requests.get(url)
        data = response.json()
        return {
            "temp": round(data["main"]["temp"]),
            "city": data["name"],
            "country": data["sys"]["country"],
            "weather": data["weather"][0]["main"]
        }
    except:
        return None

@app.route("/")
def home():
    # Obtener hora y fecha actual
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%A, %d de %B de %Y")  # Formato: "Lunes, 2 de Abril de 2023"
    
    # Obtener clima
    weather_data = get_weather()
    
    return render_template(
        "index.html",
        time=time,
        date=date,
        weather=weather_data
    )

if __name__ == "__main__":
    app.run(debug=True)