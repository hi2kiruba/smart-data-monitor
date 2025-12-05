import json
from file_manager import read_json
from logger_manager import get_logger

logger = get_logger("Analyzer")

INPUT_FILE = "../../data/processed_readings.json"
OUTPUT_FILE = "../../data/analyzed_readings.json"


def analyze_reading(temp, battery):
    """
    Business rule engine applying threshold logic.
    """

    flags = []

    if temp > 40:
        flags.append("High Temperature")

    if battery < 20:
        flags.append("Low Battery")

    return flags if flags else ["Normal"]


def analyze_readings():
    """
    Reads processed readings, applies analyzer rules,
    logs every step, and handles errors gracefully.
    """

    try:
        readings = read_json(INPUT_FILE)
        logger.info("Loaded processed readings file")
    except FileNotFoundError:
        logger.error("Processed readings file missing.")
        return
    except json.JSONDecodeError:
        logger.error("Invalid JSON format in processed readings file.")
        return

    analyzed = []

    for reading in readings:
        try:
            device = reading["device_id"]
            temp = float(reading.get("temperature", 0))
            battery = float(reading.get("battery", 0))

        except (KeyError, ValueError) as e:
            logger.warning(f"Skipping invalid reading: {reading} — {e}")
            continue

        flags = analyze_reading(temp, battery)

        logger.info(
            f"Device {device}: Temp={temp} Batt={battery} Status={flags}"
        )

        analyzed.append({
            "device_id": device,
            "temperature": temp,
            "battery": battery,
            "status": flags
        })

    try:
        with open(OUTPUT_FILE, "w") as file:
            json.dump(analyzed, file, indent=4)
        logger.info(f"Analysis complete → Saved: {OUTPUT_FILE}")
    except IOError:
        logger.error("Failed to write analyzed output file")


if __name__ == "__main__":
    analyze_readings()
