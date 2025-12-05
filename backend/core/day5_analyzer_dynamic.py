import json
from file_manager import read_json
from logger_manager import get_logger
from config_manager import load_config

logger = get_logger("Analyzer-Dynamic")

INPUT_FILE = "../../data/processed_readings.json"
OUTPUT_FILE = "../../data/analyzed_readings.json"

config = load_config()
TEMP_LIMIT = config.get("temperature_threshold")
BAT_LIMIT = config.get("battery_threshold")


def analyze_reading(temp, battery):
    flags = []

    if temp > TEMP_LIMIT:
        flags.append(f"High Temperature > {TEMP_LIMIT}")

    if battery < BAT_LIMIT:
        flags.append(f"Low Battery < {BAT_LIMIT}")

    return flags if flags else ["Normal"]


def analyze_readings():
    try:
        readings = read_json(INPUT_FILE)
        logger.info("Loaded processed readings")
    except Exception as e:
        logger.error(f"Cannot read file: {e}")
        return

    analyzed = []

    for reading in readings:
        device = reading.get("device_id")
        temp = float(reading.get("temperature", 0))
        battery = float(reading.get("battery", 0))

        flags = analyze_reading(temp, battery)

        if config.get("enable_logging", True):
            logger.info(f"Device {device} → {flags}")

        analyzed.append({
            "device_id": device,
            "temperature": temp,
            "battery": battery,
            "status": flags
        })

    try:
        with open(OUTPUT_FILE, "w") as file:
            json.dump(analyzed, file, indent=4)
        logger.info("Analysis complete (config-driven)")
    except IOError:
        logger.error("Failed to save analysis file")


if __name__ == "__main__":
    analyze_readings()
