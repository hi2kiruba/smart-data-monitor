from file_manager import read_json, write_json

import os
from file_manager import read_json, write_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "../../data/readings.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "../../reports/results.json")


def process_readings():
    readings = read_json(INPUT_FILE)
    results = []

    for record in readings:
        value = record.get("value")
        alert = value > 100
        results.append({
            "id": record.get("id"),
            "value": value,
            "alert": alert
        })

    write_json(OUTPUT_FILE, results)
    print("Processing complete! Results saved.")


process_readings()
