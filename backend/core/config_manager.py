import json

CONFIG_FILE = "../../core/config.json"


def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("⚠ config.json missing — using defaults")
        return {
            "temperature_threshold": 40,
            "battery_threshold": 20,
            "enable_logging": True
        }
