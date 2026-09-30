"""Gets simple weather data from Open-Meteo."""

import requests

API_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude, longitude):
    """Return the last 7 days of temperature and rainfall."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "past_days": 7,
        "forecast_days": 1,
        "daily": "temperature_2m_mean,precipitation_sum",
        "timezone": "auto",
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "dates": data["daily"]["time"],
        "temperatures": data["daily"]["temperature_2m_mean"],
        "rainfall": data["daily"]["precipitation_sum"],
        "tomorrow": data["daily"]["time"][-1],
    }
