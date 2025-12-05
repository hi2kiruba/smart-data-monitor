from backend.core.day5_analyzer_dynamic import analyze_readings
from backend.core.logger_manager import get_logger


logger = get_logger("API-Service")


def run_analysis_service():
    """
    Service entry point for API trigger.
    """
    logger.info("API request → triggering analyzer")
    analyze_readings()
    return {"message": "Analysis triggered successfully"}
