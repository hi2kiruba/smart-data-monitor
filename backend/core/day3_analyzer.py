import json
from file_manager import read_json

INPUT_FILE = "../../data/processed_readings.json"
OUTPUT_FILE = "../../data/analyzed_readings.json"


def analyze_reading(temp, battery):
    """Apply business rules to flag a device status."""

    flags = []

    if temp > 40:
        flags.append("High Temperature")

    if battery < 20:
        flags.append("Low Battery")

    return flags if flags else ["Normal"]


def analyze_readings():
    """Load processed readings and apply analysis rules."""

    try:
        readings = read_json(INPUT_FILE)
    except FileNotFoundError:
        print("Processed readings file missing. Run day2_process_data first.")
        return

    analyzed = []

    for reading in readings:
        device = reading.get("device_id")
        temp = reading.get("temperature", 0)
        battery = reading.get("battery", 0)

        flags = analyze_reading(temp, battery)

        analyzed.append({
            "device_id": device,
            "temperature": temp,
            "battery": battery,
            "status": flags
        })

    with open(OUTPUT_FILE, "w") as file:
        json.dump(analyzed, file, indent=4)

    print("Analysis complete → Saved:", OUTPUT_FILE)


if __name__ == "__main__":
    analyze_readings()
