from flask import Flask, send_file, jsonify
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from config import CSV_FILE, XML_FILE, EXCEL_FILE
from convert_data import convert_to_csv, convert_to_excel, convert_to_xml

