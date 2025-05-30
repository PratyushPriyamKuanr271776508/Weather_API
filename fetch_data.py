import requests
from config import Config

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': Config.OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(Config.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None