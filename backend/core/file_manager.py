import json


def read_json(path):
    """Load data from a JSON file."""
    with open(path, "r") as file:
        return json.load(file)


def write_json(path, data):
    """Write results to a JSON file."""
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
