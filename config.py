from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Config:
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    CACHE_TIMEOUT = 3600  # 1 hour cache
    SUPPORTED_CITIES = ['London', 'New York', 'Tokyo', 'Paris', 'Berlin']