import pandas as pd
import json
import xml.etree.ElementTree as ET

def json_to_csv(json_data, filename):
    df = pd.DataFrame([json_data])
    df.to_csv(filename, index=False)

def json_to_excel(json_data, filename):
    df = pd.DataFrame([json_data])
    df.to_excel(filename, index=False)

def json_to_xml(json_data, filename):
    root = ET.Element("WeatherData")
    for key, value in json_data.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)