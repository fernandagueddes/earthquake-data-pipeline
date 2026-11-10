import requests
import json 
from pathlib import Path

def extract_data():

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    output_path = Path("data/raw/earthquakes.json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path,"w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return data

extract_data()

