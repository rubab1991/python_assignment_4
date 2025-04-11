# streamlit_weather.py

import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
    return None

st.title("🌤️ Weather App")
city = st.text_input("Enter a city name")
api_key = "fd2a0a3743e9998f336e8aacd1bad820"

if city:
    weather = get_weather(city, api_key)
    if weather:
        st.write(f"**Temperature**: {weather['temp']} °C")
        st.write(f"**Description**: {weather['desc']}")
        st.write(f"**Humidity**: {weather['humidity']}%")
        st.write(f"**Wind Speed**: {weather['wind']} m/s")
    else:
        st.error("City not found or API error.")
