from backend.core.day5_analyzer_dynamic import analyze_readings
from backend.core.logger_manager import get_logger
from backend.storage.result_store import save_results

logger = get_logger("API-Service")


def run_analysis_service():
    logger.info("API request → triggering analyzer")

    result = analyze_readings()

    logger.info("Saving analysis result")
    save_results(result)

    return {"message": "Analysis successful", "result": result}
