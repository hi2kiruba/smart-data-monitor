import schedule
import time
from backend.scheduler.job_runner import run_job
from backend.core.logger_manager import get_logger

logger = get_logger("CronService")


def start_scheduler():
    """
    Starts the background job scheduler.
    """

    logger.info("Starting job scheduler...")

    # Run job every 1 minute (for demo)
    schedule.every(1).minutes.do(run_job)

    # alternative examples:
    # schedule.every().day.at("18:00").do(run_job)  # daily at 6PM
    # schedule.every(10).seconds.do(run_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
