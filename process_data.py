def process_weather_data(raw_data):
    if not raw_data:
        return None
    
    processed = {
        'city': raw_data.get('name'),
        'country': raw_data.get('sys', {}).get('country'),
        'temp': round(raw_data['main']['temp'], 1),
        'feels_like': round(raw_data['main']['feels_like'], 1),
        'humidity': raw_data['main']['humidity'],
        'wind_speed': raw_data['wind']['speed'],
        'conditions': raw_data['weather'][0]['description'],
        'icon': raw_data['weather'][0]['icon']
    }
    return processed