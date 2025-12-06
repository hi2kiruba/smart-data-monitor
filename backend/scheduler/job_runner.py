from backend.core.day5_analyzer_dynamic import analyze_readings
from backend.core.logger_manager import get_logger

logger = get_logger("Scheduler")


def run_job():
    """
    Executes scheduled analysis task.
    """
    logger.info("Scheduled task started...")

    try:
        analyze_readings()
        logger.info("Scheduled task completed successfully.")
    except Exception as e:
        logger.error(f"Scheduled task failed: {e}")
