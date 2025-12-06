import json
import os

STORE_PATH = "analysis_results.json"


def save_results(data):
    """
    Saves analysis results to JSON file.
    """
    with open(STORE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def load_results():
    """
    Loads last saved analysis results.
    """
    if not os.path.exists(STORE_PATH):
        return None

    with open(STORE_PATH, "r") as file:
        return json.load(file)
