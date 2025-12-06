from backend.core.logger_manager import get_logger

logger = get_logger("Analyzer")


def analyze_readings():
    logger.info("Running analyzer...")

    # Example data — in reality fetch from DB
    readings = [14, 18, 26, 45, 8, 12, 20]

    result = {
        "min": min(readings),
        "max": max(readings),
        "avg": round(sum(readings) / len(readings), 2),
        "count": len(readings)
    }

    logger.info(f"Analysis complete: {result}")
    return result
