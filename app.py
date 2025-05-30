from flask import Flask, render_template, request, jsonify, send_file
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from convert_data import json_to_csv, json_to_excel, json_to_xml
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def weather_api():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    raw_data = fetch_weather_data(city)
    if not raw_data:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    
    processed_data = process_weather_data(raw_data)
    return jsonify(processed_data)

@app.route('/export/<format>')
def export_data(format):
    city = request.args.get('city')
    if not city:
        return "City parameter is required", 400
    
    raw_data = fetch_weather_data(city)
    if not raw_data:
        return "Failed to fetch weather data", 500
    
    processed_data = process_weather_data(raw_data)
    
    filename = f"weather_data.{format}"
    filepath = os.path.join('data', filename)
    
    if format == 'csv':
        json_to_csv(processed_data, filepath)
    elif format == 'excel':
        json_to_excel(processed_data, filepath)
    elif format == 'xml':
        json_to_xml(processed_data, filepath)
    else:
        return "Invalid format", 400
    
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)